#!/usr/bin/env python3
"""Exact edge algebra and two fixed diagnostics; no optimization or zeta run."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math


def sine(b, q):
    return (1 - q) / b**2


def acue(b, q):
    return (1 - q) / ((1 + q) * b**2) + q**2 / (1 - q**2)


def diagonal(b, q):
    return (1 - (1 + b) * q) / b**2


def sinh_from_q(q):
    return (1 / q - q) / 2


def h(b, q):
    return (1 - q)**2 / b**2 - q


def contrast(b, q, residual, nuisance=F(0)):
    s1, s2 = sinh_from_q(q), sinh_from_q(q**2)
    r1 = residual(b, q) + nuisance / s1
    r2 = residual(2 * b, q**2) + nuisance / s2
    return b**2 * (2 * s1 * r1 - 2 * s2 * r2 - 1 / (2 * b))


exact_cases = 0
for b, q in [(F(2), F(1, 7)), (F(7, 3), F(1, 11)),
             (F(5), F(1, 37)), (F(11, 2), F(2, 101))]:
    rs = lambda z, p: p / z
    ra = lambda z, p: acue(z, p) - diagonal(z, p)
    assert sine(b, q) - diagonal(b, q) == rs(b, q)
    assert sine(b, q) - acue(b, q) == (
        q * (1 - q) / ((1 + q) * b**2) - q**2 / (1 - q**2))
    cs = contrast(b, q, rs)
    ca = contrast(b, q, ra)
    assert cs == -b * q**2 + b * q**4 / 2
    assert cs - ca == b**2 * (h(b, q) - h(2 * b, q**2))
    assert contrast(b, q, ra, F(3, 17)) == ca
    exact_cases += 1

diagnostics = []
for b in (8.0, 16.0):
    q = math.exp(-b)
    s = sine(b, q)
    aa = acue(b, q)
    lower = diagonal(b, q) + (1 / b + 1 / math.sqrt(3)) * math.exp(
        -b * (1 + 1 / math.sqrt(3)))
    upper = ((1 + q) / ((1 - q) * b**2)
             - 2 * q / (b * (1 - q)**2) + q / (1 - q))
    edge = q / b**2
    cs = -b * q**2 + b * q**4 / 2
    ca = cs - b**2 * (h(b, q) - h(2 * b, q**2))
    diagnostics.append({
        "b": b,
        "edge_scale": edge,
        "sine_minus_acue_over_edge": (s - aa) / edge,
        "sine_minus_RH_lower_over_edge": (s - lower) / edge,
        "RH_upper_minus_sine_over_edge": (upper - s) / edge,
        "coupled_sine": cs,
        "coupled_ACUE": ca,
    })

result = {
    "status": "exact algebra passed; two illustrative floating evaluations only",
    "exact_rational_cases": exact_cases,
    "exact_checks": ["diagonal subtraction", "sine minus ACUE identity",
                     "coupled sine expression", "coupled signal identity",
                     "finite-height nuisance cancellation"],
    "diagnostics": diagnostics,
    "limitations": "No arithmetic edge estimate, numerical enclosure, or zeta evaluation.",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
