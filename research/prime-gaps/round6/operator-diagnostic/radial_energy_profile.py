"""Locate the observed energy of the frozen radial compression, not the full residual."""
from pathlib import Path
import argparse
import hashlib
import json
from fractions import Fraction

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=HERE.parent / "residual-trial/radial_residual_n98304_cut1e-09_tilt20_compact.npz")
    args = parser.parse_args()
    with np.load(args.input, allow_pickle=False) as data:
        q, h, s = data["q"], data["h"], data["radial"]
    positive = np.maximum(q, 0)
    energy = positive * h * h
    cdf = np.cumsum(energy) / np.sum(energy)
    quantiles = {str(a): float(s[np.searchsorted(cdf, a)]) for a in [.01, .05, .1, .25, .5, .75, .9, .95, .99]}
    rs, radius = Fraction(".2624989"), Fraction(".2742997")
    S = float(radius / rs)
    T0 = float(Fraction("1.997") - radius / rs)
    T1 = float((Fraction(".5252997") - radius) / rs)
    mesh = float(s[1] - s[0])
    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True, constrained_layout=True,
                             gridspec_kw={"height_ratios": [2, 1]})
    axes[0].plot(s, energy / np.sum(energy) / mesh, color="#9c3f37", label="Radial compression energy")
    axes[0].plot(s, positive / np.sum(positive) / mesh, color="#245b78", label="Product-weight mass", alpha=.8)
    axes[0].set_ylabel("Normalized density")
    axes[0].legend(frameon=False, loc="upper left")
    axes[1].plot(s, cdf, color="#9c3f37")
    axes[1].set_ylabel("Cumulative energy")
    axes[1].set_xlabel("Normalized radial cell representative")
    for ax in axes:
        ax.axvline(T0, color="#68744e", linestyle=":", linewidth=.9)
        ax.axvline(T1, color="#68744e", linestyle="--", linewidth=.9)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=.2)
    axes[0].text(T1+.005, axes[0].get_ylim()[1]*.85, "Inner cutoffs\nT0, T1", fontsize=9)
    axes[1].set_xlim(0, S)
    axes[1].set_ylim(0, 1.02)
    fig.suptitle("Where the new radial direction is detected\nExploratory fixed-grid cap model, k = 39", fontsize=13)
    fig.savefig(HERE / "radial_energy_profile.png", dpi=180)
    plt.close(fig)
    out = {"status": "Exploratory diagnostic of the frozen radial projection only",
           "input": args.input.name, "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
           "energy_quantiles": quantiles, "peak_radial": float(s[np.argmax(energy)]),
           "energy_above_1_fraction": float(np.sum(energy[s > 1]) / np.sum(energy)),
           "inner_cutoffs": {"T0": T0, "T1": T1}, "outer_radius_S": S,
           "rounding_convention": "Negative q values are set to zero for the plot; h is already zero there.",
           "interpretation_limit": "Concentration near an inner cutoff does not prove causation or bound the uncomputed full residual. Product-weight mass is G^2 mass, not the optimized f^2 mass."}
    (HERE / "radial_energy_profile.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
