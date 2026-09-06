#!/usr/bin/env python3
"""Exact exponent/constant checks; no numerical prime search is performed."""

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    base = root.parents[1]
    rho, radius, budget, delta = F(523, 1000), F(523, 2000), F(501, 2000), F(1, 1000)
    large, small = F(9, 100), F(343, 346000)
    total_factors, small_count, small_per_root = 348, 346, 173
    assert 2 * large + small_count * small == rho
    assert large + small_per_root * small == radius
    assert 2 * budget == F(1, 2) + delta
    assert small < delta < large
    owner_margin = budget - F(5, 2) * large
    opposite_margin = budget - F(3, 2) * large
    assert owner_margin == F(51, 2000) > 0
    assert opposite_margin > 0
    assert rho - F(1, 2) == F(23, 1000) > 0
    assert rho - F(2, 7) == F(1661, 7000) > 0
    assert (-1) ** total_factors == 1
    assert 1 - F(1, 4) - F(1, 4) == F(1, 2)
    single_conductor_constant = F(1, 2) ** 2 * F(1, 2) * F(1, 32)
    assert single_conductor_constant == F(1, 256)
    full_mass_constant = single_conductor_constant * F(1, 2)
    log_mass_constant = full_mass_constant * F(1, 4)
    assert full_mass_constant == F(1, 512)
    assert log_mass_constant == F(1, 2048)
    report = root / "CONDUCTOR_MASS_LOWER_BOUND.md"
    source = base / "sources/openai-short-gaps.pdf"
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    certificate = {
        "status": "exact arithmetic passed; ordinary PNT proof supplies the prime counts",
        "exponents": {
            "large_prime": str(large), "small_prime": str(small),
            "density_budget": str(delta), "root_radius": str(radius),
            "owner_budget": str(budget), "total_modulus": str(rho),
        },
        "factor_counts": {"large": 2, "small": 346, "per_root_small": 173, "total": 348},
        "lambda": "2^(-1/348), hence lambda^348=1/2 exactly",
        "positive_margins": {
            "small_prime_below_density_budget": str(delta - small),
            "owner_predicate": str(owner_margin),
            "opposite_root_guard": str(opposite_margin),
            "modulus_above_square_root": str(rho - F(1, 2)),
            "low_numerator_count_uniform_growth": str(rho - F(2, 7)),
        },
        "permutation_factor": {
            "formula": "2! * 346!",
            "exact_integer": str(math.factorial(2) * math.factorial(346)),
        },
        "counting_constant": "(1-lambda)^348 / (2! * 346! * u^2 * kappa^346)",
        "lower_bound_factors_after_c0_mV_squared": {
            "plain": str(full_mass_constant), "log_weight": str(log_mass_constant),
        },
        "norm_log_denominator_exponents": {"plain": 348, "log_weight": 346},
        "report_sha256": digest(report),
        "script_sha256": digest(Path(__file__)),
        "primary_source": {
            "path": str(source), "sha256": digest(source),
            "url": "https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf",
            "locations": "divisor inheritance p4; Proposition 2.3 pp4-5",
        },
        "scope": [
            "full canonical Round9 balanced complementary family with coefficient mu(q)",
            "fixed nonnegative nonzero smooth V supported in (1,2)",
            "all sufficiently large real X, uniformly X^(1/6)<=H<=X^(2/7)",
            "not a lower bound for the joint prime pairing",
            "not a lower bound for every pruned family or modified sieve weights",
            "no numerical prime realization or effective asymptotic threshold claimed",
        ],
    }
    (root / "conductor_construction_certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
    print("PASS: all exact exponent identities, source guards, and counting constants.")
    print("Plain coefficient mass is at least c0*mV^2/512 * H/log(X)^348 eventually.")
    print("The prime-counting statement is justified by the written PNT proof, not this script.")
    print("Report SHA256:", certificate["report_sha256"])


if __name__ == "__main__":
    main()
