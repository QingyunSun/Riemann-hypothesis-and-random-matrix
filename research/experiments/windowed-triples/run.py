"""Replay the Odlyzko/CUE/ACUE comparison. Inputs are verified before use."""
import argparse
import csv
import hashlib
from pathlib import Path
from urllib.request import urlretrieve

import numpy as np

from controls import RANK, acue_points, cue_expected, cue_points
from statistic import WIDTHS, batch_summary, dense_window_weights, window_scores

SOURCE = "https://www-users.cse.umn.edu/~odlyzko/zeta_tables/"
HASHES = {
    "zeros6.gz": "6acacb4707c429bf368f32823a8eef0e0737b6318d3e144c78975a4986d155da",
    "zeros3": "75a1f1a978d5e3eddd16518f661d41a95a40b33782389ba02ec4ed0ce0764807",
    "zeros4": "10d9f7dab2bbfff6b8befbe6f765969b0b3f38f6110ed1df423931addd52da8f",
    "zeros5": "250ac4ba722c6face4d07c05777376fc2b9bc021b05232e8f53c91b1eb2b7e0d",
}
BASES = (267653395647, 144176897509546973000, 1370919909931995300000)
SEED = 20261105


def unfold(offsets, base=0):
    """Relative smooth Riemann-von Mangoldt count; never add a high base to each offset."""
    t0 = float(base) + offsets[0]
    d = offsets - offsets[0]
    return (d*np.log(t0/(2*np.pi)) + (t0+d)*np.log1p(d/t0) - d) / (2*np.pi)


def endpoints(points, length=0):
    """Flag both ends of the lowest 1% of gaps. Matrix rows are independent circles."""
    if points.ndim == 1:
        gaps = np.diff(points)
    else:
        gaps = np.diff(points, axis=1, append=points[:, :1] + length)
    if np.any(gaps <= 0):
        raise ValueError("input gaps must be positive")
    chosen = np.argsort(gaps.ravel(), kind="stable")[:int(gaps.size * 0.01)]
    mask = np.zeros(points.shape, dtype=bool)
    if points.ndim == 1:
        mask[chosen] = mask[chosen+1] = True
    else:
        row, col = np.unravel_index(chosen, gaps.shape)
        mask[row, col] = mask[row, (col+1) % points.shape[1]] = True
    return mask


def analyze(name, x, span, flagged, matrices=0):
    rows = []
    for width in WIDTHS:
        windows = int(span // width)
        score, counts = window_scores(x, width, windows)
        trimmed, _ = window_scores(x[~flagged], width, windows)
        if matrices:
            group = (np.arange(windows) // (RANK//width)) * min(40, matrices) // matrices
        else:
            group = np.arange(windows) * min(40, windows//5) // windows
        weights = np.ones(windows)
        mean, se = batch_summary(score, weights, group)
        gap_mean, gap_se = batch_summary(trimmed, weights, group)
        crowded = dense_window_weights(counts)
        crowd_mean, crowd_se = batch_summary(score, crowded, group)
        included = (x >= 0) & (x < width*windows)
        flagged_bins = (x[included & flagged] // width).astype(int)
        clean = np.bincount(flagged_bins, minlength=windows) == 0
        clean_mean, clean_se = batch_summary(score, clean, group)
        if matrices:
            local = x.reshape(matrices, RANK) - RANK*np.arange(matrices)[:, None]
            shifted_local = np.sort(np.mod(local - width/2, RANK), axis=1)
            shifted_x = (shifted_local + RANK*np.arange(matrices)[:, None]).ravel()
            shifted_windows = windows
        else:
            shifted_x = x - width/2
            shifted_windows = int((span-width/2) // width)
        shifted, _ = window_scores(shifted_x, width, shifted_windows)
        if matrices:
            shifted_group = group
        else:
            shifted_group = np.arange(shifted_windows) * min(40, shifted_windows//5) // shifted_windows
        shifted_mean, shifted_se = batch_summary(shifted, np.ones(shifted_windows), shifted_group)
        rows.append(dict(sample=name, width=width, windows=windows, points=int(included.sum()),
                         batches=int(group[-1]+1), mean=mean, se=se, gap_trim=gap_mean,
                         gap_trim_se=gap_se, flagged_fraction=float(flagged[included].mean()),
                         density_trim=crowd_mean, density_trim_se=crowd_se,
                         no_tight_window=clean_mean, no_tight_window_se=clean_se,
                         clean_window_fraction=float(clean.mean()), shifted_mean=shifted_mean, shifted_se=shifted_se,
                         max_abs_window=float(np.max(np.abs(score))),
                         analytic_cue=cue_expected(width)))
    print(f"{name}: " + ", ".join(f"W{r['width']}={r['mean']:.5f}" for r in rows), flush=True)
    return rows


def read_tables(directory):
    directory.mkdir(parents=True, exist_ok=True)
    for name, expected in HASHES.items():
        path = directory / name
        if not path.exists():
            staging = directory / (name + ".part")
            urlretrieve(SOURCE + name, staging)
            if hashlib.sha256(staging.read_bytes()).hexdigest() != expected:
                raise ValueError(f"download checksum mismatch: {name}")
            staging.replace(path)
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f"checksum mismatch: {name}")
    low = np.loadtxt(directory / "zeros6.gz")
    if low.shape != (2001052,):
        raise ValueError("unexpected low table size")
    for start, end in ((0, 100000), (100000, 1000000), (1000000, 2001052)):
        yield f"zeta_{start+1}_{end}", unfold(low[start:end])
    for index, (base, exponent) in enumerate(zip(BASES, (12, 21, 22)), start=3):
        lines = (directory / f"zeros{index}").read_text().splitlines()
        values = np.array([float(s) for s in lines if s.strip() and s.strip()[0].isdigit()
                           and len(s.split()) == 1])
        if len(values) != 10000:
            raise ValueError(f"unexpected high table size: zeros{index}")
        yield f"zeta_after_1e{exponent}", unfold(values, base)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for name, x in read_tables(args.data):
        rows += analyze(name, x, x[-1], endpoints(x))
    for name, sampler, draws, seed in (("CUE", cue_points, 2400, SEED),
                                       ("ACUE", acue_points, 80, SEED+1)):
        points = sampler(draws, np.random.default_rng(seed))
        flagged = endpoints(points, RANK)
        x = (points + RANK*np.arange(draws)[:, None]).ravel()
        rows += analyze(name, x, RANK*draws, flagged.ravel(), draws)
    with args.output.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
