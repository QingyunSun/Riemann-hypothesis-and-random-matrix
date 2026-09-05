#!/usr/bin/env python3
"""Tiny exact normalization checks; no prime-height experiment or asymptotic test."""
from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

import sympy as sp

HERE = Path(__file__).resolve().parent


def pin(path: Path) -> dict:
    data = path.read_bytes()
    return {"name": path.name, "bytes": len(data), "sha256": sha256(data).hexdigest()}


def kernel(d: int, n: int, h: int) -> F:
    return F(int(gcd(n, d) == 1)) * (
        F(int((n - h) % d == 0))
        - F(int(gcd(h, d) == 1), int(sp.totient(d)))
    )


def formal_log(n: int):
    return sum(
        int(exponent) * sp.Symbol(f"log_{p}")
        for p, exponent in sp.factorint(n).items()
    )


def mangoldt(n: int):
    factors = sp.factorint(n)
    return sp.Symbol(f"log_{next(iter(factors))}") if len(factors) == 1 else sp.Integer(0)


checks = []
rho = F(523, 1000)
theta_lo = 1 - F(5, 11)
theta_hi = 1 - F(4, 9)
nu = F(2, 5) * F(501, 2000)
values = {
    "physical_shift_gap_lower": theta_lo - rho,
    "completion_power_J24": 24 * (theta_lo - rho) - rho,
    "nonprimitive_power_eta_1_100": 1 - theta_hi - nu - F(1, 100),
    "owner_largest_prime_exponent": nu,
    "source_cutoff": F(1, 2) + 2 * F(29, 2500) - F(1, 10000),
    "source_parameter_slack": 3 - 240 * F(29, 2500) - 80 * F(1, 1000),
    "height_boundary": 1 / (1 - rho),
}
expected = {
    "physical_shift_gap_lower": F(247, 11000),
    "completion_power_J24": F(7, 440),
    "nonprimitive_power_eta_1_100": F(15041, 45000),
    "owner_largest_prime_exponent": F(501, 5000),
    "source_cutoff": F(5231, 10000),
    "source_parameter_slack": F(17, 125),
    "height_boundary": F(1000, 477),
}
assert values == expected
assert values["source_cutoff"] > rho
checks.append({
    "name": "rational_exponent_and_source_margins",
    "status": "PASS", "values": {k: str(v) for k, v in values.items()},
})

case_count = 0
for d in (3, 5, 15, 21, 35):
    phi = int(sp.totient(d))
    for n in range(1, 2 * d + 1):
        for h in range(0, 2 * d):
            lhs = F(int((n - h) % d == 0))
            principal = F(int(gcd(n, d) == 1) * int(gcd(h, d) == 1), phi)
            nonprimitive = F(int(gcd(h, d) > 1) * int((n - h) % d == 0))
            assert lhs == kernel(d, n, h) + principal + nonprimitive
            case_count += 1
checks.append({"name": "exact_primitive_principal_nonprimitive_identity",
               "status": "PASS", "cases": case_count})

period_count = 0
for d in (3, 5, 15, 21, 35):
    for n in range(1, 2 * d, 2):
        rows = [kernel(d, n, 2 * r) for r in range(d)]
        assert sum(rows, F(0)) == 0
        if gcd(n, d) == 1:
            a = (pow(2, -1, d) * n) % d
            for r in range(d):
                expected_row = F(int(r == a)) - F(int(gcd(r, d) == 1), int(sp.totient(d)))
                assert rows[r] == expected_row
        else:
            assert all(row == 0 for row in rows)
        period_count += 1
checks.append({"name": "even_grid_period_and_exact_zero_mean",
               "status": "PASS", "periods": period_count, "grid_spacing": "2d"})

# The finite Fourier coefficient of the unit mask is the integer Ramanujan sum.
# Reduction modulo Phi_d checks exact roots of unity, without floating point.
z = sp.Symbol("z")
fourier_count = 0
for d in (3, 5, 15):
    cyclo = sp.Poly(sp.cyclotomic_poly(d, z), z, domain=sp.QQ)
    for k in range(d):
        units_poly = sum(z ** ((k * r) % d) for r in range(d) if gcd(r, d) == 1)
        g = gcd(d, k)
        ramanujan = int(sp.mobius(d // g)) * F(int(sp.totient(d)), int(sp.totient(d // g)))
        assert sp.rem(sp.Poly(units_poly - sp.Rational(ramanujan.numerator, ramanujan.denominator),
                              z, domain=sp.QQ), cyclo).is_zero
        for a in range(d):
            if gcd(a, d) != 1:
                continue
            finite = sum(
                (sp.Rational(int(r == a)) - sp.Rational(int(gcd(r, d) == 1), int(sp.totient(d))))
                * z ** ((k * r) % d)
                for r in range(d)
            )
            desired = z ** ((k * a) % d) - sp.Rational(ramanujan.numerator,
                                                           ramanujan.denominator * int(sp.totient(d)))
            assert sp.rem(sp.Poly(finite - desired, z, domain=sp.QQ), cyclo).is_zero
            fourier_count += 1
checks.append({"name": "positive_phase_fourier_ramanujan_coefficient",
               "status": "PASS", "coefficients": fourier_count,
               "poisson_prefactor": "1/(2d)", "zero_frequency": "exactly zero"})

# Formal logarithms distinguish identities from numerical approximations.
# These small divisors test algebra only; they are not a finite realization
# of the asymptotic canonical complementary-modulus family.
test_divisors = {3, 5, 7, 15, 21, 35}
test_pairs = [(3, 2), (9, 6), (9, 16), (9, 18), (15, 10), (15, 16),
              (21, 4), (25, 24), (27, 22), (35, 14), (45, 4), (49, 32)]
singular = sp.Symbol("singular_series_h")
for m, h in test_pairs:
    n = m + h
    assert m % 2 and h % 2 == 0
    exact_divisor = sum(int(sp.mobius(d)) * formal_log(m // d) for d in sp.divisors(m))
    assert sp.expand(exact_divisor - mangoldt(m)) == 0
    primitive = principal = nonprimitive = sp.Integer(0)
    for d in test_divisors:
        logfactor = formal_log(m) - formal_log(d)
        coefficient = int(sp.mobius(d)) * logfactor * mangoldt(n)
        kval = kernel(d, n, h)
        primitive += coefficient * sp.Rational(kval.numerator, kval.denominator)
        principal += coefficient * sp.Rational(
            int(gcd(n, d) == 1) * int(gcd(h, d) == 1), int(sp.totient(d))
        )
        nonprimitive += coefficient * int(gcd(h, d) > 1) * int(m % d == 0)
    complementary = mangoldt(n) * sum(
        int(sp.mobius(d)) * formal_log(m // d)
        for d in sp.divisors(m) if d not in test_divisors
    )
    marginal = singular * (mangoldt(m) + mangoldt(n) - 2)
    lhs = mangoldt(m) * mangoldt(n) - marginal
    rhs = primitive + principal + nonprimitive + complementary - marginal
    assert sp.expand(lhs - rhs) == 0
assert formal_log(1) == mangoldt(1) == 0
checks.append({"name": "full_five_term_divisor_identity_with_formal_prime_logs",
               "status": "PASS", "cases": len(test_pairs), "n_equals_one_endpoint": "PASS",
               "scope": "finite algebra only; no canonical-family numerical realization"})

report = HERE / "UPPER_WING_SHIFT_COMPLETION.md"
manifest = HERE / "source_manifest.json"
out = {
    "status": "PASS",
    "scope": "exact algebra and normalization checks; no asymptotic or prime-height experiment",
    "author": pin(report),
    "checker": pin(Path(__file__).resolve()),
    "source_manifest": pin(manifest),
    "checks": checks,
}
encoded = json.dumps(out, indent=2, sort_keys=True) + "\n"
(HERE / "upper_wing_completion_checks.json").write_text(encoded)
print(encoded, end="")

