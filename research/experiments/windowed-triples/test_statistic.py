import itertools
import unittest

import numpy as np
from numpy.polynomial.legendre import leggauss

from controls import RANK, acue_points, cue_expected
from run import endpoints, unfold
from statistic import HIGH, LOW, WIDTHS, dense_window_weights, window_scores


class WindowTests(unittest.TestCase):
    def test_explicit_triples_with_edges_and_deletions(self):
        x = np.array([0, .7, 2, 3.5, 8.1, 10, 10.8, 14, 19, 20, 50])
        for subset in (x, x[::2]):
            score, _ = window_scores(subset, 10, 3)
            for j in range(3):
                local = subset[(10*j <= subset) & (subset < 10*(j+1))] - 10*j
                expected = 0.
                for triple in itertools.permutations(local, 3):
                    w = np.prod(np.sin(np.pi*np.array(triple)/10)**2)
                    expected += w*(np.cos(2*np.pi*np.dot(HIGH, triple)/5)
                                   - np.cos(2*np.pi*np.dot(LOW, triple)/5))
                self.assertAlmostEqual(score[j], expected / (50/16), places=12)

    def test_translated_half_grid_and_thinning(self):
        x = acue_points(1, np.random.default_rng(17))[0]
        self.assertEqual(len(np.unique(x)), RANK)
        for width in WIDTHS:
            for points in (x + .1234, x[::2] + .1234):
                score, _ = window_scores(points, width, RANK//width)
                self.assertLess(np.max(np.abs(score)), 1e-12)

    def test_crowding_ties_and_wrapped_gap(self):
        for counts in (np.ones(40), np.repeat([5, 6, 7], [6, 8, 87])):
            weights = dense_window_weights(counts)
            self.assertAlmostEqual(weights.sum(), .95*len(counts))
            self.assertTrue(np.all((weights >= 0) & (weights <= 1)))
        x = (np.arange(100) + .1)[None, :]
        x[0, -1] = 99.99
        flagged = endpoints(x, 100)
        self.assertEqual(set(np.flatnonzero(flagged)), {0, 99})

    def test_relative_unfolding_preserves_small_gaps_at_high_altitude(self):
        t0 = 1.44e20
        d = np.array([538., 538.11, 538.28])
        expected = (d-d[0])*np.log(t0/(2*np.pi))/(2*np.pi)
        np.testing.assert_allclose(unfold(d, t0), expected, rtol=1e-14)

    def test_determinant_integral_matches_fourier_trace(self):
        # Independent 3D quadrature against the ordered CUE three-point density.
        width = 10
        nodes, weights = leggauss(100)
        x = (nodes + 1) * width/2
        q = weights * (width/2)*np.sin(np.pi*x/width)**2
        d = x[:, None] - x[None, :]
        k = np.sinc(d) / np.sinc(d/RANK)
        kab, kbc, kca = k[:, :, None], k[None, :, :], k[:, None, :]
        rho = 1 - kab**2 - kbc**2 - kca**2 + 2*kab*kbc*kca
        avg = []
        for modes in (HIGH, LOW):
            a, b, c = (q*np.exp(2j*np.pi*h*x/5) for h in modes)
            avg.append(np.einsum('i,j,k,ijk', a,b,c,rho, optimize=True).real)
        self.assertAlmostEqual((avg[0]-avg[1])/(5*width/16), cue_expected(width), places=11)


if __name__ == '__main__':
    unittest.main()
