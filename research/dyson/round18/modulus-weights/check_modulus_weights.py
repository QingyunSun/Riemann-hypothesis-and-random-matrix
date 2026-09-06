"""Exact arithmetic checks, not a scan of the asymptotic modulus family."""
from __future__ import annotations

from fractions import Fraction as F
from math import gcd
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent


def factors(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


def mu(n):
    fs = factors(n)
    return 0 if any(e > 1 for e in fs.values()) else (-1)**len(fs)


def phi(n):
    out = n
    for p in factors(n):
        out = out//p*(p-1)
    return out


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def ramanujan(d, k):
    return sum(r*mu(d//r) for r in divisors(d) if k % r == 0)


def add_vec(target, source, factor=F(1)):
    for key, value in source.items():
        target[key] = target.get(key, F(0))+factor*value
        if not target[key]:
            del target[key]


def main():
    rho, kappa, delta = F(523, 1000), F(343, 346000), F(1, 1000)
    assert 2*F(9, 100)+346*kappa == rho
    assert F(9, 100)+173*kappa == F(523, 2000)
    assert F(5, 2)*F(9, 100) < F(501, 2000)
    assert rho+2*kappa == F(45411, 86500)
    assert rho+2*delta == F(21, 40)
    assert 2*(delta-kappa) == F(3, 173000)
    assert F(3, 5)-(rho+2*delta) == F(3, 40)
    # One genuine-integer support witness for Lemma 1.
    n, level, s = 30, F(100), F(19, 10)
    levels = [s, s, level/s**2]
    assert s < min(factors(n)) and levels[2] < n
    admissible = [(a, b, n//a//b)
                  for a in divisors(n) for b in divisors(n//a)
                  if a <= levels[0] and b <= levels[1]
                  and n//a//b <= levels[2]]
    assert admissible == []

    families = [
        [6, 10, 15, 21, 30, 35, 42],
        [n for n in range(2, 61) if mu(n) != 0],
        [n for n in range(2, 61) if mu(n) != 0 and n % 5 != 0],
    ]
    inversions = 0
    norm_checks = []
    for family in families:
        qmax = max(family)
        for j in [0, 1]:
            # Formal log-prime vectors make the j=1 check exact.
            lam = {q: ({0: F(mu(q))} if j == 0 else
                       {p: F(mu(q)*e) for p, e in factors(q).items()})
                   for q in family}
            completed = {d: {} for d in range(1, qmax+1)}
            for q in family:
                for d in divisors(q):
                    add_vec(completed[d], lam[q], F(1, q))
            for r in range(1, qmax+1):
                inverse = {}
                for d in range(r, qmax+1, r):
                    add_vec(inverse, completed[d], F(r*mu(d//r)))
                assert inverse == lam.get(r, {})
                inversions += 1
            if j == 0:
                norm = sum(abs(v.get(0, F(0))) for v in completed.values())
                upper = sum(F(len(divisors(q)), q) for q in family)
                harmonic = sum(F(1, q) for q in range(1, qmax+1))
                assert norm <= upper <= harmonic**2
                norm_checks.append({"qmax": qmax, "completed_l1": str(norm),
                                    "divisor_bound": str(upper),
                                    "harmonic_square": str(harmonic**2)})
    primitive_checks = 0
    full_kernel_checks = 0
    for d in range(1, 61):
        if not mu(d):
            continue
        for h in range(0, 2*d+1):
            lhs = sum(F(r*mu(d//r), phi(r))
                      for r in divisors(d) if gcd(h, r) == 1)
            rhs = F(mu(d)*ramanujan(d, h), phi(d))
            assert lhs == rhs
            primitive_checks += 1
            for p in [101, 103]:
                assert gcd(p, d) == 1
                total = sum(r*mu(d//r)*(
                    F(int((p-h) % r == 0)) -
                    F(int(gcd(h, r) == 1), phi(r)))
                    for r in divisors(d))
                expected = (F(ramanujan(d, p-h))
                            - F(mu(d)*ramanujan(d, h), phi(d)))
                assert total == expected
                full_kernel_checks += 1
    report = HERE / "MODULUS_WEIGHT_LEVEL_AND_NORMALIZATION.md"
    result = {
        "status": "PASS",
        "scope": "Exact support/exponent, formal-log coefficient inversion and primitive Ramanujan checks. Not a finite realization of the 348-prime family or an aggregate estimate.",
        "report_sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "necessary_level_exponent": str(rho+2*kappa),
        "sufficient_level_exponent": str(rho+2*delta),
        "exponent_gap": str(2*(delta-kappa)),
        "support_witness": {"integer": n, "level": str(level),
                            "factor_levels": list(map(str, levels)),
                            "admissible_factorizations": 0},
        "formal_coefficient_inversions": inversions,
        "primitive_principal_checks": primitive_checks,
        "full_prime_kernel_checks": full_kernel_checks,
        "completed_norm_checks": norm_checks,
    }
    (HERE / "modulus_weight_checks.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
