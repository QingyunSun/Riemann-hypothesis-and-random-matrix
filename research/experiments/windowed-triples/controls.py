"""Independent finite-rank controls and an exact-expectation check for the same taper."""
import numpy as np
from scipy.linalg import eigvals
from scipy.stats import unitary_group

from statistic import HIGH, LOW

RANK = 120


def cue_points(n_draws: int, rng: np.random.Generator) -> np.ndarray:
    draws = []
    for _ in range(n_draws):
        u = unitary_group.rvs(RANK, random_state=rng)
        phase = np.angle(eigvals(u, overwrite_a=True, check_finite=False))
        draws.append(np.sort(np.mod(phase / (2*np.pi), 1)) * RANK)
    return np.array(draws)


def acue_points(n_draws: int, rng: np.random.Generator) -> np.ndarray:
    # Projection DPP on 2N sites, gauged to its real Dirichlet kernel.
    sites = np.arange(2 * RANK)
    d = sites[:, None] - sites[None, :]
    kernel = 0.5 * np.sinc(d/2) / np.sinc(d/(2*RANK))
    draws = []
    for _ in range(n_draws):
        residual = kernel.copy()
        selected = []
        for _ in range(RANK):
            diagonal = np.maximum(residual.diagonal(), 0)
            pos = rng.choice(len(diagonal), p=diagonal/diagonal.sum())
            selected.append(pos)
            col = residual[:, pos].copy()
            residual -= np.outer(col, col) / diagonal[pos]
            residual[pos, :] = residual[:, pos] = 0.0
        draws.append(np.sort(np.asarray(selected) / 2 + rng.uniform(0, 0.5)))
    return np.array(draws)


def cue_expected(width: int) -> float:
    """Integrate the finite Haar three-point determinant over the Hann window.

    All singleton integrals vanish for these widths/modes, so only the two
    3-cycles survive. The Fourier integral is centered on the window midpoint.
    """
    d = np.arange(RANK)[:, None] - np.arange(RANK)[None, :]

    def matrix(k):
        u = width * (k/5 + d/RANK)
        return width / RANK * (0.5*np.sinc(u) + 0.25*(np.sinc(u-1) + np.sinc(u+1)))

    def cycles(modes):
        a, b, c = map(matrix, modes)
        return np.trace(a @ b @ c) + np.trace(a @ c @ b)

    return float((cycles(HIGH) - cycles(LOW)) / (5 * width/16))
