#!/usr/bin/env python3
"""Small checks for the centered-tail identity; no critical-line series is used."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp


Interval = tuple[F, F]


def add(a: Interval, b: Interval) -> Interval:
    return a[0] + b[0], a[1] + b[1]


def scale(a: Interval, b: F) -> Interval:
    values = (a[0] * b, a[1] * b)
    return min(values), max(values)


def mul(a: Interval, b: Interval) -> Interval:
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def inv(a: Interval) -> Interval:
    assert a[0] > 0
    return 1 / a[1], 1 / a[0]


def rational_constant_check() -> dict:
    lower = sum((F(1, math.factorial(n)) for n in range(51)), F(0))
    upper = lower + F(1, math.factorial(51)) / (1 - F(1, 52))
    e = (lower, upper)
    e2 = mul(e, e)
    ei = inv(e)
    ei2 = mul(ei, ei)
    ei4 = mul(ei2, ei2)
    b = add(
        add(add(scale(e2, F(1, 4)), scale(e, F(-1))), (F(5, 4), F(5, 4))),
        add(add(ei, scale(ei2, F(-9, 4))), scale(ei4, F(3, 4))),
    )
    threshold = add((F(1, 16), F(1, 16)), scale(b, F(-1)))
    assert F("0.45609397932923") < b[0] < b[1] < F("0.45609397932924")
    assert F("-0.39359397932924") < threshold[0] < threshold[1] < F("-0.39359397932923")
    return {
        "arithmetic": "exact fractions; Taylor lower sum through degree 50",
        "B_strict_enclosure": ["0.45609397932923", "0.45609397932924"],
        "one_sixteenth_minus_B_strict_enclosure": [
            "-0.39359397932924", "-0.39359397932923"
        ],
        "B_exact_rational_endpoints": [str(x) for x in b],
        "threshold_exact_rational_endpoints": [str(x) for x in threshold],
        "passed": True,
    }


def prime_powers(limit: int) -> list[tuple[int, int]]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    result = []
    for p in range(2, limit + 1):
        if sieve[p]:
            n = p
            while n <= limit:
                result.append((n, p))
                n *= p
    return sorted(result)


def complex_json(z: mp.mpc | mp.mpf) -> dict[str, str]:
    return {"real": mp.nstr(mp.re(z), 45), "imaginary": mp.nstr(mp.im(z), 45)}


def finite_step_identity_check() -> list[dict]:
    atoms = [(mp.mpf(n), mp.log(p)) for n, p in prime_powers(256)]
    x = mp.mpf("31.5")
    psi_x = mp.fsum(weight for n, weight in atoms if n <= x)
    output = []
    for sigma, height in [("2.3", "0.7"), ("3.1", "2.2")]:
        s = mp.mpc(sigma, height)
        # Independently integrate the piecewise-constant psi, including
        # its explicit infinite tail after the final atom.
        psi = psi_x
        left = x
        integral = mp.mpc(0)
        for right, weight in atoms:
            if right <= x:
                continue
            integral += psi * (left ** (-s) - right ** (-s)) / s
            integral -= (right ** (1 - s) - left ** (1 - s)) / (1 - s)
            psi += weight
            left = right
        integral += psi * left ** (-s) / s - left ** (1 - s) / (s - 1)
        lhs = mp.fsum(weight * n ** (-s) for n, weight in atoms)
        partial = mp.fsum(weight * n ** (-s) for n, weight in atoms if n <= x)
        rhs = partial + x ** (1 - s) / (s - 1) - (psi_x - x) * x ** (-s) + s * integral
        error = abs(lhs - rhs)
        assert error < mp.mpf("1e-50")
        output.append({
            "s": complex_json(s),
            "cutoff_X": str(x),
            "finite_measure_max_atom": 256,
            "left_side": complex_json(lhs),
            "independently_integrated_right_side": complex_json(rhs),
            "absolute_error": mp.nstr(error, 12),
            "scope": "finite step measure, Re(s)>1, all tails evaluated",
            "passed": True,
        })
    return output


def actual_zeta_absolute_half_plane_check() -> dict:
    limit = 10_000
    s = mp.mpc(3, mp.mpf("0.7"))
    partial = mp.fsum(mp.log(p) * mp.mpf(n) ** (-s) for n, p in prime_powers(limit))
    actual = -mp.diff(mp.zeta, s) / mp.zeta(s)
    error = abs(actual - partial)
    # Lambda(n) <= log n; log(x)/x^3 is decreasing for x>=limit.
    upper = (mp.log(limit) / 2 + mp.mpf(1) / 4) / limit**2
    assert error < upper
    return {
        "s": complex_json(s),
        "cutoff": limit,
        "actual_minus_zeta_log_derivative": complex_json(actual),
        "absolutely_convergent_partial_sum": complex_json(partial),
        "absolute_error": mp.nstr(error, 30),
        "analytic_tail_upper_bound": mp.nstr(upper, 30),
        "scope": "numerical evaluation plus an explicit analytic tail bound; not an Arb enclosure",
        "passed": True,
    }


def regularized_critical_strip_diagnostic() -> dict:
    s = mp.mpf("0.75")
    actual = -mp.diff(mp.zeta, s) / mp.zeta(s)
    atoms = prime_powers(100_000)
    rows = []
    for cutoff in [1000, 10_000, 100_000]:
        positive_sum = math.fsum(math.log(p) * n ** (-0.75) for n, p in atoms if n <= cutoff)
        pole_counterterm = -4.0 * cutoff**0.25
        regularized = positive_sum + pole_counterterm
        rows.append({
            "cutoff": cutoff,
            "positive_finite_prime_sum": positive_sum,
            "pole_counterterm": pole_counterterm,
            "regularized_sum": regularized,
            "difference_from_actual": float(mp.mpf(regularized) - actual),
        })
    return {
        "s": "0.75",
        "actual_minus_zeta_log_derivative": mp.nstr(actual, 45),
        "rows": rows,
        "scope": (
            "finite regularized-sum diagnostics with binary64 arithmetic; "
            "not an unregularized critical-strip Dirichlet series, "
            "not a certified tail estimate, and not a W_T calculation"
        ),
    }


def main() -> None:
    mp.mp.dps = 60
    root = Path(__file__).resolve().parent
    b_integral = 2 * mp.quad(
        lambda u: u * (mp.sinh(2) * mp.exp(-2 * u) - mp.sinh(1) * mp.exp(-u)),
        [0, 1],
    )
    b_closed = mp.e**2 / 4 - mp.e + mp.mpf(5) / 4 + 1 / mp.e - 9 / (4 * mp.e**2) + 3 / (4 * mp.e**4)
    assert abs(b_integral - b_closed) < mp.mpf("1e-55")
    report = {
        "status": "analytic identity checks; requested 1/16 lower bound remains unproved",
        "exact_constant_certificate": rational_constant_check(),
        "high_precision_B_integral": mp.nstr(b_integral, 50),
        "high_precision_B_closed": mp.nstr(b_closed, 50),
        "finite_step_identity_checks": finite_step_identity_check(),
        "actual_zeta_absolute_half_plane_check": actual_zeta_absolute_half_plane_check(),
        "regularized_critical_strip_diagnostic": regularized_critical_strip_diagnostic(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    target = root / "check_centered_tail.json"
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS: exact rational constants and two finite-step integral checks.")
    print("PASS: actual zeta check at Re(s)=3 lies within its elementary tail bound.")
    print("B =", mp.nstr(b_integral, 35))
    print("1/16 - B =", mp.nstr(mp.mpf(1) / 16 - b_integral, 35))
    print("Critical-strip rows are diagnostics only; no 1/16 theorem is established.")
    print("Output:", target)


if __name__ == "__main__":
    main()
