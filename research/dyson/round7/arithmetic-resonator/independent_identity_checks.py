#!/usr/bin/env python3
"""Small exact algebra checks; no quadrature, spectral solve, or parameter scan.

The integer cutoff is fixed at 120. Rational prime labels substitute for log p
only to check formal insertion identities without floating arithmetic. This is
not an asymptotic test and does not certify the reported numerical margin.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json

L = 120
ELL = Q(27, 25)
A = ELL**2


def factor(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


FACTORS = {n: factor(n) for n in range(1, L + 1)}
PRIMES = [n for n in range(2, L + 1) if FACTORS[n] == {n: 1}]
U = {p: Q(p, L) for p in PRIMES}
ALPHA = {p: Q(p % 7 + 1, 5) for p in PRIMES}


def divisor_coefficient(fs):
    value = Q(1)
    for e in fs.values():
        for j in range(e):
            value *= (ELL + j) / (j + 1)
    return value


D = {n: divisor_coefficient(fs) for n, fs in FACTORS.items()}
C = {n: sum(p * p > L for p in fs) for n, fs in FACTORS.items()}
V = {n: sum((e * U[p] for p, e in fs.items()), Q(0))
     for n, fs in FACTORS.items()}
S2 = {n: sum((U[p]**2 for p in fs), Q(0)) for n, fs in FACTORS.items()}
S3 = {n: sum((U[p]**3 for p in fs), Q(0)) for n, fs in FACTORS.items()}


def phi(v, s2, s3):
    return 1 + v + s2 * s3 + s2**2


assert all(c in (0, 1) for c in C.values())
marked_lhs = sum((D[n]**2 * C[n] * phi(V[n], S2[n], S3[n]) / n
                  for n in range(1, L + 1)), Q(0))
marked_rhs = Q(0)
large_pairs = 0
for p in PRIMES:
    if p * p <= L:
        continue
    for m in range(1, L // p + 1):
        assert m < p and p not in FACTORS[m]
        assert D[p * m]**2 == A * D[m]**2
        marked_rhs += A * D[m]**2 / (p * m) * phi(
            V[m] + U[p], S2[m] + U[p]**2, S3[m] + U[p]**3)
        large_pairs += 1
assert marked_lhs == marked_rhs

R = {n: D[n] * (1 - 3 * V[n] + 2 * S2[n] + C[n] * (S3[n] - V[n]))
     for n in range(1, L + 1)}


def creation(r):
    return {n: sum((ALPHA[p] * r[n // p] for p in FACTORS[n]), Q(0))
            for n in range(1, L + 1)}


Y = creation(R)
Z = creation(Y)
norm_ax = sum((Y[n]**2 / n for n in range(1, L + 1)), Q(0))
norm_expanded = sum((ALPHA[p] * ALPHA[q] * R[n // p] * R[n // q] / n
                     for n in range(1, L + 1)
                     for p, q in product(FACTORS[n], repeat=2)), Q(0))
assert norm_ax == norm_expanded
diag_expanded = sum((ALPHA[p]**2 * R[n // p]**2 / n
                     for n in range(1, L + 1) for p in FACTORS[n]), Q(0))
diag_inserted = sum((ALPHA[p]**2 * R[m]**2 / (m * p)
                     for p in PRIMES for m in range(1, L // p + 1)), Q(0))
assert diag_expanded == diag_inserted
quad_a2 = sum((R[n] * Z[n] / n for n in range(1, L + 1)), Q(0))
quad_a2_expanded = sum((ALPHA[p] * ALPHA[q] * R[m] * R[m * p * q] / (m * p * q)
                        for p, q in product(PRIMES, repeat=2)
                        for m in range(1, L // (p * q) + 1)), Q(0))
assert quad_a2 == quad_a2_expanded

coprime_triples = 0
for p, q in product(PRIMES, repeat=2):
    if p == q:
        continue
    for m in range(1, L // (p * q) + 1):
        if p in FACTORS[m] or q in FACTORS[m]:
            continue
        assert D[m * p] * D[m * q] == A * D[m]**2
        assert D[m] * D[m * p * q] == A * D[m]**2
        coprime_triples += 1

boolean_checks = 0
for c, dl, dr in product((0, 1), repeat=3):
    assert (c + dl) * (c + dr) == c * (1 + dl + dr) + dl * dr
    boolean_checks += 1

result = {
    "status": "all exact Fraction/integer algebra checks passed",
    "cutoff": L,
    "ell": str(ELL),
    "integers_checked": L,
    "unique_large_prime_pairs": large_pairs,
    "coprime_ordered_distinct_prime_triples": coprime_triples,
    "boolean_product_checks": boolean_checks,
    "checks": ["binary mark", "unique large prime and automatic coprimality",
               "mixed marked integer identity", "AstarA ordered expansion",
               "AstarA same-prime term uses uninserted amplitude",
               "A2 ordered expansion", "distinct-prime coefficient factor a",
               "C-product insertion rule"],
    "limitations": "Rational formal labels and kernels; not numerical quadrature, an asymptotic test, or a zeta result.",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
