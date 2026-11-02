#!/usr/bin/env python3
"""Exact source-parameter and formal-log algebra checks; no asymptotic test."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


def factors(n: int) -> dict[int, int]:
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
    a = factors(n)
    return 0 if any(v > 1 for v in a.values()) else (-1) ** len(a)


def phi(n: int) -> int:
    out = n
    for p in factors(n):
        out = out // p * (p - 1)
    return out


def add_scaled(a: dict, b: dict, scale: F | int = 1) -> None:
    for k, v in b.items():
        a[k] = a.get(k, F(0)) + scale * v
        if a[k] == 0:
            del a[k]


def mangoldt_vector(n: int) -> dict:
    a = factors(n)
    return {next(iter(a)): F(1)} if len(a) == 1 else {}


def log_ratio_vector(n: int, q: int) -> dict:
    out = {p: F(e) for p, e in factors(n).items()}
    add_scaled(out, factors(q), -1)
    return out


def product(a: dict, b: dict) -> dict:
    out = {}
    for p, v in a.items():
        for q, w in b.items():
            key = tuple(sorted((p, q)))
            out[key] = out.get(key, F(0)) + v * w
    return {k: v for k, v in out.items() if v}


def parameter_check() -> dict:
    omega, delta, retreat = F(3, 250), F(1, 1000), F(1, 1000)
    lhs = 240 * omega + 80 * delta
    level = F(1, 2) + 2 * omega - retreat
    assert lhs == F(74, 25) < 3
    assert level == F(523, 1000)
    budget, root_cap = F(501, 2000), F(523, 2000)
    assert 2 * budget == F(1, 2) + delta
    assert 2 * root_cap == level
    large_lo, large_hi = F(89, 1000), F(9, 100)
    small_lo, small_hi = F(17, 100), F(171, 1000)
    assert large_lo > delta
    root_lo, root_hi = large_lo + small_lo, large_hi + small_hi
    assert root_hi < root_cap
    assert 2 * root_lo > F(1, 2)
    assert 2 * root_hi < level
    assert F(5, 2) * large_hi < budget
    return {
        "omega": str(omega), "delta": str(delta), "epsilon": str(retreat),
        "full_prime_condition_lhs": str(lhs),
        "strict_full_prime_margin": str(3 - lhs),
        "modulus_level": str(level),
        "root_size_exponent_interval": [str(root_lo), str(root_hi)],
        "coprime_lcm_exponent_interval": [str(2 * root_lo), str(2 * root_hi)],
        "owner_predicate_exponent_margin": str(budget - F(5, 2) * large_hi),
        "passed": True,
    }


def convolution_checks() -> int:
    for n in range(1, 301):
        out = {}
        for q in range(1, n + 1):
            if n % q == 0:
                add_scaled(out, factors(n // q), mu(q))
        assert out == mangoldt_vector(n), n
    return 300


def finite_progression_check(h: int) -> dict:
    low, high = 60, 90
    moduli = [q for q in range(8, 31) if mu(q)]
    direct, discrepancy, principal, nonprimitive = {}, {}, {}, {}
    exceptional_pairs = 0
    for n in range(low, high + 1):
        weight = F((n - low) * (high - n), (high - low) ** 2)
        divisor_vector = {}
        for q in moduli:
            if n % q == 0:
                add_scaled(divisor_vector, factors(n // q), mu(q))
        add_scaled(direct, product(mangoldt_vector(n + h), divisor_vector), weight)
    # Independent modulus-first progression enumeration, with explicit
    # subtraction of its coprime principal term.
    for q in moduli:
        residue, mean = {}, {}
        for m in range(low + h, high + h + 1):
            n = m - h
            weight = F((n - low) * (high - n), (high - low) ** 2)
            term = product(mangoldt_vector(m), log_ratio_vector(n, q))
            if math.gcd(q, h) == 1:
                if m % q == h % q:
                    add_scaled(residue, term, weight)
                if math.gcd(m, q) == 1:
                    add_scaled(mean, term, weight / phi(q))
            elif n % q == 0:
                add_scaled(nonprimitive, term, mu(q) * weight)
                if term and weight:
                    p = next(iter(factors(m)))
                    assert len(factors(m)) == 1 and h % p == 0 and q % p == 0
                    exceptional_pairs += 1
        if math.gcd(q, h) == 1:
            add_scaled(discrepancy, residue, mu(q))
            add_scaled(discrepancy, mean, -mu(q))
            add_scaled(principal, mean, mu(q))
    reconstructed = {}
    for part in [discrepancy, principal, nonprimitive]:
        add_scaled(reconstructed, part)
    assert reconstructed == direct
    return {
        "h": h, "n_interval": [low, high], "moduli": moduli,
        "direct_formal_log_quadratic_monomials": len(direct),
        "nonprimitive_formal_monomials": len(nonprimitive),
        "nonzero_exceptional_prime_power_pairs": exceptional_pairs,
        "identity_passed": True,
        "scope": "exact finite algebra; moduli are a toy family, not an asymptotic certificate",
    }


def main() -> None:
    root = Path(__file__).resolve().parent
    base = root.parents[1]
    rows = [finite_progression_check(h) for h in [1, 2, 4, 6, 13]]
    assert any(r["nonzero_exceptional_prime_power_pairs"] for r in rows)
    source_url = "https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf"
    sources = []
    for name in ["openai-short-gaps.pdf", "openai-short-gaps.txt"]:
        p = base / "sources" / name
        sources.append({"local_file": str(p), "source_url": source_url,
                        "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    report_path = root / "COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md"
    result = {
        "status": "exact checks passed; no zeta covariance estimate newly proved",
        "parameter_certificate": parameter_check(),
        "mobius_log_convolution_cases": convolution_checks(),
        "finite_progression_checks": rows,
        "sources": sources,
        "report_sha256": hashlib.sha256(report_path.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "Python integers and fractions; formal logarithm monomials",
    }
    (root / "check_divisor_bridge.json").write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: exact 186 parameter inequalities and complementary-family exponents.")
    print("PASS: 300 exact Mobius-log convolution identities.")
    print("PASS: five exact progression/discrepancy decompositions, including nonprimitive terms.")
    print("No numerical asymptotic, zeta bound, or prime-gap improvement is asserted.")
    print("Report SHA256:", result["report_sha256"])


if __name__ == "__main__":
    main()
