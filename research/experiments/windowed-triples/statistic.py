"""Distinct ordered three-point scores in complete, nonoverlapping spatial windows."""
import numpy as np

WIDTHS = (10, 20, 40)
HIGH = (6, 1, -7)
LOW = (-4, 1, 3)


def window_scores(points: np.ndarray, width: int, windows: int) -> tuple[np.ndarray, np.ndarray]:
    """Each frequency is in fifths of a cycle per mean spacing. Keep original spatial units."""
    if width <= 0 or windows <= 0 or np.any(~np.isfinite(points)) or np.any(np.diff(points) < 0):
        raise ValueError("expected sorted finite points and positive window dimensions")
    points = points[(points >= 0) & (points < windows * width)]
    index = (points // width).astype(int)
    local = points - width * index
    weights = np.sin(np.pi * local / width) ** 2

    def sum_bins(values):
        return (np.bincount(index, values.real, minlength=windows)
                + 1j * np.bincount(index, values.imag, minlength=windows))

    first, second = {}, {}
    for k in (1, 3, 4, 6, 7):
        wave = np.exp((2j * np.pi * k / 5) * local)
        first[k] = sum_bins(weights * wave)
        second[k] = sum_bins(weights**2 * wave)

    def moment(modes):
        a, b, c = (first[k] if k > 0 else first[-k].conj() for k in modes)
        # Remove the three pairwise coincidences. The all-equal correction
        # +2 sum(w^3) is the same in both moments and cancels in the difference.
        repeated = sum((second[abs(k)].conj() * first[abs(k)]).real for k in modes)
        return (a*b*c).real - repeated

    return (moment(HIGH) - moment(LOW)) / (5 * width / 16), np.bincount(index, minlength=windows)


def dense_window_weights(counts: np.ndarray) -> np.ndarray:
    """Drop exactly 5% by occupancy; equal occupancy receives equal weight at the cutoff."""
    cut = np.quantile(counts, 0.95, method="higher")
    tied = counts == cut
    keep = (counts < cut).astype(float)
    keep[tied] = (0.95 * len(counts) - keep.sum()) / tied.sum()
    return keep


def batch_summary(score: np.ndarray, weights: np.ndarray, batch_id: np.ndarray) -> tuple[float, float]:
    """Weighted grand mean and disjoint-batch standard error (descriptive for zeta)."""
    mean = np.average(score, weights=weights)
    residual = np.bincount(batch_id, weights * (score - mean))
    groups = len(residual)
    se = np.sqrt(groups / (groups - 1) * (residual @ residual)) / weights.sum()
    return float(mean), float(se)
