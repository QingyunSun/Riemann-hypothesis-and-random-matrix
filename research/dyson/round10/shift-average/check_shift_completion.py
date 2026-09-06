#!/usr/bin/env python3
"""Exact finite checks of conductor regrouping and exponent accounting."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


def factor(n: int) -> dict[int, int]:
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mu(n: int) -> int:
    a = factor(n)
    return 0 if any(e > 1 for e in a.values()) else (-1) ** len(a)


def phi(n: int) -> int:
    out = n
    for p in factor(n):
        out = out // p * (p - 1)
    return out


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def ramanujan_ratio_checks() -> dict:
    cases, zero_modes = 0, 0
    for q in range(2, 181):
        if not mu(q):
            continue
        for r in range(q):
            # Integer Ramanujan sum from finite geometric sums and
            # the Mobius expansion of the unit indicator.
            c = sum(k * mu(q // k) for k in divisors(math.gcd(q, r)))
            d = q // math.gcd(q, r)
            assert F(c, phi(q)) == F(mu(d), phi(d)), (q, r, d)
            if r == 0:
                assert d == 1 and F(c, phi(q)) == 1
                zero_modes += 1
            cases += 1
    return {"cases": cases, "zero_modes_cancelled": zero_modes, "passed": True}


def add_vector(target: dict, source: dict, weight: F) -> None:
    for p, exponent in source.items():
        target[p] = target.get(p, F(0)) + weight * exponent
        if target[p] == 0:
            del target[p]


def regrouping_checks() -> dict:
    moduli = [6, 10, 14, 15, 21, 22, 30]
    assert all(mu(q) for q in moduli)
    plain, log_weight = {}, {}
    for q in moduli:
        for r in range(1, q):
            frequency = F(r, q)
            plain[frequency] = plain.get(frequency, F(0)) + F(mu(q), q)
            add_vector(log_weight.setdefault(frequency, {}), factor(q), F(mu(q), q))
    grouped, grouped_log = {}, {}
    for frequency in plain:
        d = frequency.denominator
        grouped[frequency] = sum((F(mu(q), q) for q in moduli if q % d == 0), F(0))
        coefficients = {}
        for q in moduli:
            if q % d == 0:
                add_vector(coefficients, factor(q), F(mu(q), q))
        grouped_log[frequency] = coefficients
    assert grouped == plain
    assert grouped_log == log_weight
    return {
        "toy_squarefree_moduli": moduli,
        "unreduced_nonzero_modes": sum(q - 1 for q in moduli),
        "distinct_reduced_frequencies": len(plain),
        "plain_and_formal_log_weight_regrouping": "passed",
        "scope": "exact algebra; no claim of an asymptotic distribution test",
    }


def exponent_checks() -> list[dict]:
    cap, eta = F(523, 1000), F(1, 100)
    assert cap > F(1, 2)
    rows = []
    for theta in [F(1, 6), F(2, 7)]:
        completed = cap + F(1, 2) + theta / 2
        triangle = 1 + theta
        saving = triangle - completed
        prime_power = F(1, 2) + eta + theta
        assert saving == theta / 2 - F(23, 1000) > 0
        assert prime_power < 1 < completed < triangle
        rows.append({
            "theta": str(theta),
            "completion_exponent": str(completed),
            "triangle_exponent": str(triangle),
            "power_improvement_before_logs": str(saving),
            "normalized_error_exponent": str(completed - 1),
            "prime_power_error_exponent_eta_1_100": str(prime_power),
        })
    assert rows[0]["completion_exponent"] == "3319/3000"
    assert rows[1]["completion_exponent"] == "8161/7000"
    assert rows[0]["power_improvement_before_logs"] == "181/3000"
    return rows


def main() -> None:
    root = Path(__file__).resolve().parent
    base = root.parents[1]
    report = root / "SMOOTH_SHIFT_COMPLETION_BOUND.md"
    r9 = base / "research-round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md"
    source = base / "sources/openai-short-gaps.pdf"
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest(r9) == "982039f0e163b84c1c5b8f2b52f215eb40e7b89863085f2840c039853606f39a"
    result = {
        "status": "exact checks passed; smooth-packet bound is above the target covariance scale",
        "ramanujan_ratios": ramanujan_ratio_checks(),
        "conductor_regrouping": regrouping_checks(),
        "power_exponents": exponent_checks(),
        "report_sha256": digest(report),
        "script_sha256": digest(Path(__file__)),
        "frozen_round9": {"path": str(r9), "sha256": digest(r9)},
        "primary_source": {
            "path": str(source), "sha256": digest(source),
            "url": "https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf",
            "locations": "Proposition 2.3 pp4-5; equation 2.5 p7; Corollary 2.19 p11",
        },
        "arithmetic": "exact Python integers, fractions, and formal prime-log vectors",
        "scope": [
            "actual smooth packet of the progression discrepancy",
            "no bound of order o(X log X)",
            "no theorem for the whole unsmoothed range or the complementary divisor remainder",
            "no proof of AH refutation or Montgomery's conjecture",
        ],
    }
    (root / "check_shift_completion.json").write_text(json.dumps(result, indent=2) + "\n")
    print("PASS:", result["ramanujan_ratios"]["cases"], "exact Ramanujan-ratio cases.")
    print("PASS: conductor regrouping, including formal log(q) coefficients.")
    print("PASS: both endpoint power exponents and prime-power error comparison.")
    print("The smooth-packet bound still exceeds X log X.")
    print("Report SHA256:", result["report_sha256"])


if __name__ == "__main__":
    main()
