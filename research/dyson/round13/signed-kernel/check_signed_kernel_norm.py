#!/usr/bin/env python3
"""Fixed exact CRT/mean/remainder checks; no asymptotic or prime-data test."""

from fractions import Fraction as F
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import json


def mobius(n):
    sign, p = 1, 2
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
    rho, cutoff = F(523, 1000), F(1, 10)
    assert 2 * rho - 1 == F(23, 500)
    assert 2 * rho - cutoff == F(473, 500)
    assert 1 - (2 * rho - cutoff) == F(27, 500)
    assert F(1, 6) - cutoff == F(1, 15)
    ordered_pairs_constant = F(1, 128) ** 2 / (8 * 2)
    coherent_constant = ordered_pairs_constant / 16
    assert ordered_pairs_constant == F(1, 262144)
    assert coherent_constant == F(1, 4194304)
    assert F(1, 4) + F(3, 100) == F(7, 25) < F(1, 3)

    # These are toy moduli, not a realization of the asymptotic source family.
    moduli, v = (6, 7, 10, 15, 30), {4: F(1), 5: F(2)}
    V0 = sum(v.values())
    U = {q: sum((value for h, value in v.items() if gcd(h, q) == 1), F(0))
         for q in moduli}
    b = {q: U[q] / phi(q) for q in moduli}

    def B(q, n):
        return sum((value for h, value in v.items() if (n - h) % q == 0), F(0))

    def K(n):
        return sum((mobius(q) * (B(q, n) - b[q]) for q in moduli), F(0))

    common_period = lcm(*moduli)
    M = sum((mobius(q) * (V0 / q - b[q]) for q in moduli), F(0))
    assert sum((K(n) for n in range(common_period)), F(0)) / common_period == M

    R = {}
    C2 = F(0)
    crt_cases = 0
    for q1 in moduli:
        for q2 in moduli:
            g, period = gcd(q1, q2), lcm(q1, q2)
            compatible_mass = F(0)
            for h1, v1 in v.items():
                for h2, v2 in v.items():
                    residues = [r for r in range(period)
                                if (r - h1) % q1 == 0 and (r - h2) % q2 == 0]
                    assert len(residues) == int((h1 - h2) % g == 0)
                    if residues:
                        compatible_mass += v1 * v2
                    crt_cases += 1
            R[g] = g * compatible_mass - V0 * V0
            assert R[g] >= 0
            C2 += mobius(q1) * mobius(q2) * R[g] / (q1 * q2)
    variance = sum(((K(n) - M) ** 2 for n in range(common_period)), F(0)) / common_period
    assert variance == C2 > 0

    # A compact rational polynomial window, used only for finite algebra.
    # W(u)=(u-1)^2(3/2-u)^2 on [1,3/2], zero outside, has integral 1/960.
    # It is not C-infinity; no rapid-decay estimate is being numerically tested.
    X = 60
    weights = {n: F((n - X) ** 2 * (3 * X // 2 - n) ** 2, X ** 4)
               for n in range(X, 3 * X // 2 + 1)}
    w0 = F(1, 960)
    W0 = X * w0
    Wsum = sum(weights.values())
    actual_norm = sum((w * K(n) ** 2 for n, w in weights.items()), F(0))
    norm_main = W0 * (M * M + C2)
    single = {q: sum((w * B(q, n) for n, w in weights.items()), F(0)) for q in moduli}
    pair_remainder, single_remainder, constant_remainder = F(0), F(0), F(0)
    by_gcd = {}
    for q1 in moduli:
        for q2 in moduli:
            sign = mobius(q1) * mobius(q2)
            g, period = gcd(q1, q2), lcm(q1, q2)
            compatible_mass, pair_count = F(0), F(0)
            for h1, v1 in v.items():
                for h2, v2 in v.items():
                    if (h1 - h2) % g:
                        continue
                    compatible_mass += v1 * v2
                    residue = next(r for r in range(period)
                                   if (r - h1) % q1 == 0 and (r - h2) % q2 == 0)
                    pair_count += v1 * v2 * sum((w for n, w in weights.items()
                                                if (n - residue) % period == 0), F(0))
            direct = sum((w * B(q1, n) * B(q2, n) for n, w in weights.items()), F(0))
            assert pair_count == direct
            piece = sign * (pair_count - W0 * compatible_mass / period)
            pair_remainder += piece
            by_gcd[g] = by_gcd.get(g, F(0)) + piece
            single_remainder -= sign * (b[q2] * (single[q1] - W0 * V0 / q1)
                                       + b[q1] * (single[q2] - W0 * V0 / q2))
            constant_remainder += sign * b[q1] * b[q2] * (Wsum - W0)
    assert actual_norm == norm_main + pair_remainder + single_remainder + constant_remainder

    result = {
        "status": "PASS",
        "scope": "One exact signed CRT family and rational window; no prime experiment or numerical proof of cancellation",
        "cutoff_exponents": {
            "Q_squared_over_X": str(2 * rho - 1),
            "G": str(cutoff),
            "max_large_g_period": str(2 * rho - cutoff),
            "large_g_Poisson_gain": str(1 - (2 * rho - cutoff)),
            "min_H_over_G_gain": str(F(1, 6) - cutoff),
        },
        "coherent_constants_relative_to_c0_squared": {
            "ordered_pairs": str(ordered_pairs_constant),
            "norm_subsum_with_w0_m_v_squared": str(coherent_constant),
            "phase_bound_in_pi_units": "7/25 < 1/3",
        },
        "toy_moduli": list(moduli),
        "toy_shifts": {str(h): str(value) for h, value in v.items()},
        "crt_compatibility_cases": crt_cases,
        "common_period": common_period,
        "full_period_mean": str(M),
        "full_period_variance": str(C2),
        "R_v_by_gcd": {str(g): str(value) for g, value in sorted(R.items())},
        "rational_window": {
            "X": X, "integral_w0": str(w0), "sum_W": str(Wsum),
            "actual_norm": str(actual_norm), "main_Xw0_times_mean_square": str(norm_main),
            "pair_remainder": str(pair_remainder),
            "single_centering_remainder": str(single_remainder),
            "constant_window_remainder": str(constant_remainder),
            "pair_remainder_by_gcd": {str(g): str(value) for g, value in sorted(by_gcd.items())},
        },
        "global_norm_lower_bound_claimed": False,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (here / "check_signed_kernel_norm.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
