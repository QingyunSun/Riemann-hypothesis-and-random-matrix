#!/usr/bin/env python3
"""Exact scalar checks only; no factorization, divisor enumeration or prime data."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    root = Path(__file__).resolve().parent
    lam, u = sp.symbols("lambda u", nonnegative=True)
    A, kappa, T, ell, c = sp.symbols("A kappa T ell c", positive=True)
    xi = sp.symbols("xi", real=True)
    checks = []

    def equal(name: str, left: sp.Expr, right: sp.Expr) -> None:
        assert sp.simplify(left - right) == 0, (name, left, right)
        checks.append({"name": name, "status": "PASS"})

    equal("complete exponential length mass", sp.integrate(sp.exp(-lam), (lam, 0, sp.oo)), 1)
    equal("complete exponential length second moment", sp.integrate(lam**2 * sp.exp(-lam), (lam, 0, sp.oo)), 2)
    equal("cumulative profile exponential square integral", sp.integrate((A + kappa * u)**2 * sp.exp(-u), (u, 0, sp.oo)), A**2 + 2 * A * kappa + 2 * kappa**2)
    equal("profile Minkowski upper bound difference", (A + sp.sqrt(2) * kappa)**2 - (A**2 + 2 * A * kappa + 2 * kappa**2), 2 * (sp.sqrt(2) - 1) * A * kappa)
    equal("uniform outer multiplier upper difference", sp.Rational(7, 3) - (2 * T - 1) / (T - 1), (T - 4) / (3 * (T - 1)))
    denominator = (T - sp.Rational(1, 2))**2 + xi**2
    equal("resolvent factor upper difference", 1 - (xi**2 + sp.Rational(1, 4)) / denominator, T * (T - 1) / denominator)
    assert (Fraction(1) - Fraction(7, 4)) / 2 == Fraction(-3, 8)
    checks.append({"name": "square-root window mass exponent", "exact_value": "-3/8", "status": "PASS"})
    equal("primorial logarithmic scale limit", sp.limit(sp.log(c * ell * sp.log(ell)) / sp.log(ell), ell, sp.oo), 1)
    output = {
        "status": "PASS",
        "scope": "Eight exact scalar moment/multiplier/exponent checks only. No wheel or divisor enumeration, factoring, prime-height sample, or verification of PNT or the ordinary proof.",
        "sympy_version": sp.__version__,
        "report_sha256": hashlib.sha256((root / "GROWING_WHEEL_CENTERING.md").read_bytes()).hexdigest(),
        "checks": checks,
        "number_of_checks": len(checks),
    }
    rendered = json.dumps(output, indent=2) + "\n"
    (root / "wheel_norm_algebra_checks.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
