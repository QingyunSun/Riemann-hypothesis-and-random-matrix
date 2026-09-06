#!/usr/bin/env python3
"""Exact constants and one finite signed-completion identity; no prime scan."""

from fractions import Fraction as F
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import json


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def remainder(p, divisor):
    p = [F(x) for x in p]
    while len(p) >= len(divisor):
        c = p[-1] / divisor[-1]
        shift = len(p) - len(divisor)
        for j, a in enumerate(divisor):
            p[shift + j] -= c * a
        trim(p)
        if p == [0]:
            break
    return trim(p)


def exact_divide(p, divisor):
    p = [F(x) for x in p]
    q = [F(0)] * (len(p) - len(divisor) + 1)
    while len(p) >= len(divisor):
        c = p[-1] / divisor[-1]
        shift = len(p) - len(divisor)
        q[shift] = c
        for j, a in enumerate(divisor):
            p[shift + j] -= c * a
        trim(p)
        if p == [0]:
            break
    assert p == [0]
    return trim(q)


def cyclotomic(n):
    cache = {}
    for m in range(1, n + 1):
        p = [F(-1)] + [F(0)] * (m - 1) + [F(1)]
        for d in range(1, m):
            if m % d == 0:
                p = exact_divide(p, cache[d])
        cache[m] = p
    return cache[n]


def mobius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def phi(n):
    return sum(gcd(a, n) == 1 for a in range(1, n + 1))


def main():
    here = Path(__file__).resolve().parent
    rho = F(523, 1000)
    assert 2 * rho - 1 == F(23, 500) > 0
    # Constants are relative to the positive c0 from the inherited source.
    number_moduli = F(1, 2)
    numerators_per_modulus = F(1, 64)
    total_frequency_constant = number_moduli * numerators_per_modulus
    cluster_constant = total_frequency_constant / 8
    positive_sampling_constant = cluster_constant / (20 * 4)
    weighted_sampling_constant = positive_sampling_constant / 8
    assert total_frequency_constant == F(1, 128)
    assert cluster_constant == F(1, 1024)
    assert positive_sampling_constant == F(1, 81920)
    assert weighted_sampling_constant == F(1, 655360)

    # One algebraic toy: not an instance of the large-X source predicates.
    moduli = (6, 10, 15, 30)
    shifts = {4: F(1), 5: F(2), 7: F(1)}
    L = lcm(*moduli)
    cyclo = cyclotomic(L)
    assert cyclo == [F(x) for x in (1, 1, 0, -1, -1, -1, 0, 1, 1)]
    conductors = sorted({d for q in moduli for d in range(2, q + 1) if q % d == 0})
    merged = {d: sum((F(mobius(q), q) for q in moduli if q % d == 0), F(0))
              for d in conductors}
    values = []
    for n in range(1, 61):
        polynomial = [F(0)] * L
        for d in conductors:
            rd = F(mobius(d), phi(d))
            for a in range(1, d):
                if gcd(a, d) != 1:
                    continue
                step = L * a // d
                for h, value in shifts.items():
                    polynomial[(step * (n - h)) % L] += merged[d] * value
                    polynomial[(-step * h) % L] -= merged[d] * value * rd
        kernel = sum((
            mobius(q) * (
                sum((value for h, value in shifts.items() if (n - h) % q == 0), F(0))
                - sum((value for h, value in shifts.items() if gcd(h, q) == 1), F(0)) / phi(q)
            ) for q in moduli
        ), F(0))
        assert remainder(polynomial, cyclo) == [kernel]
        values.append(kernel)
    assert any(x != 0 for x in values)
    # The exact signed-functional norm on this one toy coefficient interval.
    norm_square = sum(x * x for x in values[30:36])
    assert norm_square > 0

    result = {
        "status": "PASS",
        "scope": "Exact rational bookkeeping and one formal cyclotomic completion check; no asymptotic prime experiment",
        "Q_squared_over_X_exponent": str(2 * rho - 1),
        "constants_relative_to_c0": {
            "actual_frequency_count": str(total_frequency_constant),
            "cluster_count": str(cluster_constant),
            "positive_sampling": str(positive_sampling_constant),
            "weighted_sampling_with_m_v_squared": str(weighted_sampling_constant),
        },
        "toy_moduli": list(moduli),
        "toy_shifts": {str(k): str(v) for k, v in shifts.items()},
        "common_cyclotomic_order": L,
        "cyclotomic_polynomial_ascending": [str(x) for x in cyclo],
        "signed_kernel_identities_checked": len(values),
        "toy_kernel_values_first_twelve": [str(x) for x in values[:12]],
        "toy_signed_dual_norm_square_n31_to36": str(norm_square),
        "prime_obstruction_proved": False,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (here / "check_sampling_geometry.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
