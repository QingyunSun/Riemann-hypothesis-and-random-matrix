#!/usr/bin/env python3
"""Exact rational extension of short-gaps Proposition 3.11 / equation (3.35).

Only Fraction arithmetic enters each certified inequality. Decimal displays are
diagnostic; use exact_upper_numerator/exact_upper_denominator as the certificate.
No numerical quadrature, float arithmetic, or external packages are used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path

A = F(40481, 100000)
XI = F(9519, 50000)
XI0 = F(19037, 100000)
SLACK_HALF = F(1, 10000)
BINS = 1024
H = (A - 2 * XI) / BINS
SCALE = 10**25
BASELINE = F(840334010068226419110401, 2500000000000000000000000)
DEFAULT_RADII = ("0.272", "0.2742997", "0.275", "0.276", "0.278", "0.28", "0.282")


def display(q: F, digits: int = 64) -> str:
    with localcontext() as ctx:
        ctx.prec = digits
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def ceil_fraction(q: F) -> int:
    return -(-q.numerator // q.denominator)


def alternating_log(t: F, degree: int = 21) -> F:
    return sum(((-1) ** (m + 1) * t**m / m for m in range(1, degree + 1)), F(0))


def build_grid() -> list[tuple[F, F, F]]:
    out = []
    for j in range(1, BINS + 1):
        s = 2 * XI + j * H
        t = (s - 2 * XI) / XI
        assert 0 < t < 1
        upper_log = alternating_log(t)
        lower_log = alternating_log(t, 22)
        assert upper_log - lower_log == t**22 / 22
        assert 0 < lower_log < upper_log
        out.append((s, t, upper_log))
    assert out[-1][0] == A
    return out


def certify(radius_text: str, grid: list[tuple[F, F, F]]) -> dict[str, object]:
    radius = F(radius_text)
    c = 1 - 2 * radius - 2 * SLACK_HALF
    ceiling_sum = 0
    pre_rounded = F(0)
    log_polynomial_excess = F(0)
    floor_sum = 0
    for s, t, upper_log in grid:
        z = (c - s) / 2
        assert 0 < z < XI0 < XI, (radius_text, s, z)
        assert s + 2 * radius + 2 * z == 1 - 2 * SLACK_HALF
        prefactor = 24 * H / (5 * s * (c - s))
        term = prefactor * upper_log
        pre_rounded += term
        log_polynomial_excess += prefactor * t**22 / 22
        ceiling_sum += ceil_fraction(SCALE * term)
        left_s = s - H
        left_t = (left_s - 2 * XI) / XI
        lower_term = 24 * H * alternating_log(left_t, 22) / (5 * left_s * (c - s))
        scaled_lower = SCALE * lower_term
        floor_sum += scaled_lower.numerator // scaled_lower.denominator
    result = F(ceiling_sum, SCALE)
    bin_lower = F(floor_sum, SCALE)
    assert 0 <= result - pre_rounded < F(BINS, SCALE)
    if radius == F(11, 40):
        assert result == BASELINE, (result, BASELINE)
    # A deliberately conservative six-decimal constant suitable for a screen.
    easy = F(ceil_fraction(result * 10**6), 10**6)
    return {
        "radius": radius_text,
        "radius_fraction": str(radius),
        "z_min_exact": str((c - A) / 2),
        "z_max_exact": str((c - grid[0][0]) / 2),
        "z_min_decimal": display((c - A) / 2),
        "z_max_decimal": display((c - grid[0][0]) / 2),
        "crt_error_exponent_exact": str(1 - 2 * SLACK_HALF),
        "integer_ceiling_sum": str(ceiling_sum),
        "exact_upper_numerator": str(result.numerator),
        "exact_upper_denominator": str(result.denominator),
        "upper_decimal_display": display(result),
        "six_decimal_safe_upper": str(easy),
        "six_decimal_safe_upper_display": display(easy),
        "bin_lower_numerator": str(bin_lower.numerator),
        "bin_lower_denominator": str(bin_lower.denominator),
        "bin_lower_decimal_display": display(bin_lower),
        "bin_constant_exceeds_17_over_50": bin_lower > F(17, 50),
        "rounding_excess_upper": str(F(BINS, SCALE)),
        "degree21_excess_upper_decimal": display(log_polynomial_excess),
        "baseline_exact_match": result == BASELINE if radius == F(11, 40) else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--radii", nargs="+", default=DEFAULT_RADII)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    grid = build_grid()
    values = [certify(s, grid) for s in args.radii]
    exacts = [F(int(v["exact_upper_numerator"]), int(v["exact_upper_denominator"])) for v in values]
    radii = [F(s) for s in args.radii]
    for ra, rb, va, vb in zip(radii, radii[1:], exacts, exacts[1:]):
        if ra <= rb:
            assert va <= vb
    s1 = grid[0][0]
    payload = {
        "method": "1024 exact rational right-endpoint terms; L21 logarithm upper; individual ceil at 10^-25",
        "source": "Improved short gaps between primes, Proposition 3.11, equations (3.32)-(3.35)",
        "source_url": "https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf",
        "large_integer_serialization": "Decimal strings prevent loss in JavaScript JSON readers.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "constants": {"a_star": str(A), "xi_star": str(XI), "xi0": str(XI0), "bins": BINS, "h_ex": str(H), "rounding_scale": str(SCALE)},
        "radius_range_with_z_less_than_xi0_strict": {
            "lower_exact": str((1 - s1 - 2 * SLACK_HALF - 2 * XI0) / 2),
            "lower_decimal": display((1 - s1 - 2 * SLACK_HALF - 2 * XI0) / 2),
            "upper_exact": str((1 - A - 2 * SLACK_HALF) / 2),
            "upper_decimal": display((1 - A - 2 * SLACK_HALF) / 2),
        },
        "radius_range_required_by_prop3_10_strict": {
            "lower_exact": str((1 - s1 - 2 * SLACK_HALF - 2 * XI) / 2),
            "lower_decimal": display((1 - s1 - 2 * SLACK_HALF - 2 * XI) / 2),
            "upper_exact": str((1 - A - 2 * SLACK_HALF) / 2),
        },
        "results": values,
    }
    local_source = Path(__file__).resolve().parents[2] / "sources" / "openai-short-gaps.txt"
    if local_source.is_file():
        payload["source_text_sha256"] = hashlib.sha256(local_source.read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
