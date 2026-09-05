"""Exact algebra/constants checks for galilean-proof-audit.md.

This script does not prove the analytic/root-tracking theorem.  It checks the
particular rational choices and symbolic derivative identities used there.
"""

from fractions import Fraction
import json
from pathlib import Path

import sympy as sp


def main() -> dict:
    k = 2**14
    eta0 = Fraction(1, 32 * k)
    a = Fraction(8, 7)
    assert a**3 < 2
    gaussian_upper = 2 * (65 * 2 + 16 * 2 + 3 * 2)
    assert gaussian_upper == 336
    normal_form_upper = 37 * gaussian_upper
    assert normal_form_upper < k
    assert eta0 < Fraction(1, 64)
    tau_star_upper = Fraction(1, 8) + k * eta0
    assert tau_star_upper == Fraction(5, 32)
    assert tau_star_upper < Fraction(1, 4)
    boundary_lower = Fraction(15, 4) - k * eta0
    assert boundary_lower > 0
    assert eta0 < Fraction(1, 4)

    c, v, u = sp.symbols("c v u", real=True)
    r = sp.cos(v) - c * sp.sin(v)
    # A denominator-free identity checks (log r)'' without introducing a
    # complex logarithm branch into the symbolic computation.
    centered_second_numerator = sp.trigsimp(sp.diff(r, v, 2) * r - sp.diff(r, v) ** 2)
    assert sp.simplify(centered_second_numerator + 1 + c**2) == 0
    f_left = u**2 / 2 - u - sp.log(1 - u)
    f_right = u**2 / 2 - u - sp.log(u - 1)
    assert sp.simplify(sp.diff(f_left, u) - u * (2 - u) / (1 - u)) == 0
    assert sp.simplify(sp.diff(f_right, u) - u * (u - 2) / (u - 1)) == 0

    result = {
        "scope": "exact constants and symbolic identities, not a formal proof of the theorem",
        "K": k,
        "eta0": str(eta0),
        "Gaussian_moment_upper": gaussian_upper,
        "normal_form_error_coefficient_upper": normal_form_upper,
        "tau_star_upper": str(tau_star_upper),
        "moving_boundary_lower": str(boundary_lower),
        "centered_sine_log_second_derivative_numerator": str(centered_second_numerator),
        "canonical_factor_derivative_left": str(sp.factor(sp.diff(f_left, u))),
        "canonical_factor_derivative_right": str(sp.factor(sp.diff(f_right, u))),
        "all_assertions_passed": True,
    }
    return result


if __name__ == "__main__":
    payload = json.dumps(main(), indent=2)
    Path(__file__).with_suffix(".json").write_text(payload + "\n")
    print(payload)
