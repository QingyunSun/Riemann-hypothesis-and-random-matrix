"""Finite algebra/lattice checks; no primes or asymptotic certification."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as s


def run() -> dict[str, object]:
    t, r, y, x, d, m, scale, ell = s.symbols(
        "t r y x d m scale ell", positive=True
    )
    z, u = s.symbols("z u", real=True)
    checks: list[str] = []

    def exact(name: str, expression: s.Expr) -> None:
        assert s.simplify(s.expand_log(expression, force=True)) == 0, name
        checks.append(name)

    xr = t / (s.pi * r)
    phase = t * s.log(xr * y) - s.pi * r * xr * y
    canonical = t * s.log(xr) - t - t * (y - 1 - s.log(y))
    exact("canonical_stationary_phase", phase - canonical)
    exact("stationary_point", (t / x - s.pi * r).subs(x, xr))
    exact("stationary_curvature", (-t / x**2).subs(x, xr) + s.pi**2 * r**2 / t)
    derivative_at_one = s.limit(s.sqrt(2 * (z - s.log(1 + z)) / z**2), z, 0)
    exact("canonical_coordinate_derivative", derivative_at_one - 1)

    h = s.Function("H")
    oscillator = s.exp(-s.I * u**2 / 2)
    primitive = s.I * h(u / s.sqrt(t)) * oscillator
    expected = u * h(u / s.sqrt(t)) * oscillator + s.I * s.diff(
        h(u / s.sqrt(t)), u
    ) * oscillator
    exact("amplitude_error_integration_by_parts", s.diff(primitive, u) - expected)
    fresnel_primitive = s.sqrt(s.pi) * (
        s.fresnelc(u / s.sqrt(s.pi)) - s.I * s.fresnels(u / s.sqrt(s.pi))
    )
    exact(
        "fresnel_primitive_normalization",
        s.diff(fresnel_primitive, u) - s.cos(u**2 / 2) + s.I * s.sin(u**2 / 2),
    )
    exact(
        "interior_stationary_coefficient",
        s.sqrt(t) / (2 * s.pi) * s.sqrt(2 * s.pi) - s.sqrt(t / (2 * s.pi)),
    )
    exact("three_normalization_factors", (1 / s.pi) * s.Rational(1, 2) * (2 * s.pi) - 1)
    exact(
        "integrated_error_scale",
        (s.sqrt(scale) * ell) * scale * ell / (scale**2 * ell**2) - scale**s.Rational(-1, 2),
    )
    exact(
        "carrier_bound_scale",
        (s.sqrt(scale) * ell) ** 2 * scale / (scale**2 * ell**2) - 1,
    )
    dual_phase = t * s.log(xr) - t + t * s.log(d) - t * s.log(m)
    exact("dual_phase_stationary_point", s.diff(dual_phase, t).subs(t, s.pi * r * m / d))
    exact("dual_phase_value", dual_phase.subs(t, s.pi * r * m / d) + s.pi * r * m / d)

    lattice_cases = 0
    for lower in (s.Integer(3), s.Rational(7, 2), s.Integer(4), s.Rational(17, 4), s.Integer(5)):
        upper = 2 * lower
        odd = list(range(1, int(s.ceiling(upper)) + 2, 2))
        weight = lambda k: s.Integer(k) ** 2 + 3 * k + 1
        sharp = sum(weight(k) for k in odd if lower < k <= upper)
        midpoint = sum(
            weight(k) * (s.Rational(1, 2) if k == lower or k == upper else 1)
            for k in odd
            if lower <= k <= upper
        )
        correction = s.Rational(1, 2) * (
            sum(weight(k) for k in odd if k == upper)
            - sum(weight(k) for k in odd if k == lower)
        )
        assert sharp == midpoint + correction
        lattice_cases += 1
    checks.append("sharp_halfendpoint_convention")

    parity_cases = 0
    for index in range(-12, 13):
        assert s.simplify(s.exp(s.I * s.pi * index) - s.Integer(-1) ** index) == 0
        parity_cases += 1
    checks.append("odd_lattice_parity_both_signs")

    return {
        "status": "passed",
        "scope": "Exact algebra and finite lattice identities only; no prime data or asymptotic proof certification.",
        "groups": len(checks),
        "checks": checks,
        "endpoint_cases": lattice_cases,
        "parity_cases": parity_cases,
    }


if __name__ == "__main__":
    result = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("sharp_odd_stationary_checks.json").write_text(result)
    print(result, end="")
