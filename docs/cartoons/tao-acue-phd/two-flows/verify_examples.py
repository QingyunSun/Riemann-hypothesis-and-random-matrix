"""Numerical illustration checks, not formal verification of the research proofs."""
import cmath
import itertools
import math
import unittest
from collections import Counter


def pairs(sites: tuple[int, ...], period: int) -> Counter[int]:
    return Counter((b - a) % period for a in sites for b in sites)


def gaps(sites: tuple[int, ...], period: int) -> list[int]:
    ordered = sorted(sites)
    return sorted((ordered[(i + 1) % len(ordered)] - a) % period
                  for i, a in enumerate(ordered))


def trace(sites: tuple[int, ...], period: int, k: int) -> complex:
    return sum(cmath.exp(2j * math.pi * k * x / period) for x in sites)


class IllustratedFacts(unittest.TestCase):
    def test_complement_pair_identity_exhaustively(self) -> None:
        for period in (4, 6, 8, 10):
            for sites in itertools.combinations(range(period), period // 2):
                complement = tuple(x for x in range(period) if x not in sites)
                self.assertEqual(pairs(sites, period), pairs(complement, period))

    def test_four_point_distances(self) -> None:
        for sites in ((0, 1, 3, 4), (2, 5, 6, 7)):
            distances = sorted(min(abs(a - b), 8 - abs(a - b))
                               for a, b in itertools.combinations(sites, 2))
            self.assertEqual(distances, [1, 1, 2, 3, 3, 4])

    def test_six_point_pair_and_gap_equality(self) -> None:
        a, b = (0, 1, 2, 4, 7, 8), (3, 5, 6, 9, 10, 11)
        self.assertEqual(pairs(a, 12), pairs(b, 12))
        self.assertEqual(gaps(a, 12), [1, 1, 1, 2, 3, 4])
        self.assertEqual(gaps(a, 12), gaps(b, 12))

    def test_cubic_and_independent_root_velocity(self) -> None:
        for sites, expected_cubic, expected_slope in (
            ((0, 1, 2, 4, 7, 8), 2, 120),
            ((3, 5, 6, 9, 10, 11), -2, 104),
        ):
            p1, p2 = trace(sites, 12, 1), trace(sites, 12, 2)
            self.assertAlmostEqual(abs(p2) ** 2, 7, places=10)
            cubic = (p1 ** 2 * p2.conjugate()).real
            self.assertAlmostEqual(cubic, expected_cubic, places=10)
            theta = [2 * math.pi * a / 12 for a in sites]
            velocities = [-sum(1 / math.tan((x - y) / 2)
                               for j, y in enumerate(theta) if i != j)
                          for i, x in enumerate(theta)]
            dp2 = sum(2j * cmath.exp(2j * x) * velocity
                      for x, velocity in zip(theta, velocities))
            slope = 2 * (dp2 * p2.conjugate()).real
            self.assertAlmostEqual(slope, expected_slope, places=9)

    def test_collision_times(self) -> None:
        polynomial = lambda y: 4 * y ** 3 - 4 * y + 1
        lower, upper = 0.8, 1.0
        self.assertLess(polynomial(lower), 0)
        self.assertGreater(polynomial(upper), 0)
        for _ in range(60):
            midpoint = (lower + upper) / 2
            if polynomial(midpoint) > 0:
                upper = midpoint
            else:
                lower = midpoint
        tau_s = -math.log((lower + upper) / 2) / 2
        tau_c = math.log(2) / 6
        self.assertAlmostEqual(tau_s, 0.0886279433267, places=12)
        self.assertAlmostEqual(tau_c, 0.1155245300933, places=12)
        self.assertLess(tau_s, tau_c)


if __name__ == "__main__":
    unittest.main(verbosity=2)
