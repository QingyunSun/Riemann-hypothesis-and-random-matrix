"""Check exact scale identities only; no prime calculation or analytic certification."""

import json
from pathlib import Path

import sympy as s

X, T, ell, eta, R = s.symbols("X T ell eta R", positive=True)
alpha, delta = s.symbols("alpha delta", real=True)
Y = X / T
D = s.sqrt(X)
L = s.sqrt(T) * ell
checks = []


def exact(name, difference):
    assert s.simplify(s.powsimp(difference, force=True)) == 0, name
    checks.append(name)


exact("selberg_scale_after_partial_summation", (X**3 / T**2) / (X * Y) - Y)
exact("negative_sobolev_schur_scale", Y**2 * X**2 / X**3 - X / T**2)
exact("low_middle_optimal_split", s.sqrt(L) / (T * ell) - 1 / s.sqrt(T * L))
exact("split_value", s.sqrt(L) / (T * ell) - T**s.Rational(-3, 4) / s.sqrt(ell))
exact("low_middle_height_exponent", alpha * (s.Rational(1, 2) + eta) / 2 - s.Rational(3, 4) - ((alpha - 3) / 4 + alpha * eta / 2))
exact("high_band_scale", R * s.sqrt(Y * D) / X - R / s.sqrt(D * T))
exact("high_band_at_alias", (R / s.sqrt(D * T) * (T / R) ** 2).subs(R, D) - (T / D) ** s.Rational(3, 2))
exact("tail_height_exponent", s.Rational(3, 2) * (1 - alpha / 2) + 3 * (alpha - 2) / 4)
exact("uniform_low_exponent", ((alpha - 3) / 4 + alpha * eta / 2).subs({alpha: s.Rational(9, 4), eta: s.Rational(1, 100)}) + s.Rational(141, 800))
exact("uniform_tail_exponent", (-3 * (alpha - 2) / 4).subs(alpha, 2 + delta) + 3 * delta / 4)
p = s.symbols("p", positive=True)
epsilon = eta / (4 * p)
exact("perron_vertical_exponent", s.Rational(1, 2) + eta / 4 + p * epsilon + eta / 4 - (s.Rational(1, 2) + 3 * eta / 4))
z, F = s.symbols("z F")
exact("odd_euler_factor_removal", (1 - z) * F / (1 - z) - F)

result = {
    "status": "passed",
    "scope": "Exact exponent and norm algebra only; no analytic proof certification or prime calculation.",
    "groups": len(checks),
    "checks": checks,
}
serialized = json.dumps(result, sort_keys=True, indent=2) + "\n"
Path(__file__).with_name("upper_height_algebra_checks.json").write_text(serialized)
print(serialized, end="")
