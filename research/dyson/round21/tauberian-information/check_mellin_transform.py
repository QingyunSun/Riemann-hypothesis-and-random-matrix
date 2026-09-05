#!/usr/bin/env python3
"""Bounded exact algebra checks for the fixed-bump Tauberian note.

These checks do not prove Wiener's theorem, an analytic limit, or a zeta bound.
Run with Python 3 and SymPy; no numerical scan or network access is used.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    root = Path(__file__).resolve().parent
    y, t = sp.symbols("y t", positive=True)
    u, tau = sp.symbols("u tau", real=True)
    delta = sp.symbols("delta", positive=True)
    p = 4 * y**2 / (sp.pi * (1 + y**2) ** 2)
    q = 4 * sp.exp(3 * u) / (sp.pi * (1 + sp.exp(2 * u)) ** 2)
    multiplier = (1 + sp.I * tau) / sp.cosh(sp.pi * tau / 2)
    checks: list[dict[str, str]] = []

    def equal(name: str, left: sp.Expr, right: sp.Expr) -> None:
        residue = sp.simplify(sp.expand_complex(left - right))
        assert residue == 0, (name, residue)
        checks.append({"name": name, "status": "PASS", "exact_residue": "0"})

    equal("logarithmic change of variables", p.subs(y, sp.exp(u)) * sp.exp(u), q)
    equal("positive kernel normalization", sp.integrate(p, (y, 0, sp.oo)), sp.Integer(1))
    equal("square-variable Jacobian", p.subs(y, sp.sqrt(t)) / (2 * sp.sqrt(t)),
          2 * sp.sqrt(t) / (sp.pi * (1 + t) ** 2))
    z = (1 + sp.I * tau) / 2
    equal("gamma reflection trigonometric factor", sp.sin(sp.pi * z), sp.cosh(sp.pi * tau / 2))
    equal("gamma recurrence and reflection multiplier", (2 / sp.pi) * z * sp.pi / sp.sin(sp.pi * z), multiplier)
    equal("reflected kernel transform at zero", multiplier.subs(tau, 0), sp.Integer(1))
    equal("opposite Fourier-sign conjugacy", sp.conjugate(multiplier), multiplier.subs(tau, -tau))
    equal("squared Fourier modulus", multiplier * sp.conjugate(multiplier),
          (1 + tau**2) / sp.cosh(sp.pi * tau / 2) ** 2)
    equal("first Mellin derivative at zero", sp.diff(multiplier, tau).subs(tau, 0), sp.I)
    equal("height modulus for positive logarithmic shift", (sp.exp(delta) - 1) / sp.exp(delta), 1 - sp.exp(-delta))

    result = {
        "status": "PASS",
        "scope": "Exact kernel/Jacobian/gamma-algebra/normalization checks only; not a proof of Wiener density, analytic limits, a numerical inverse, or a zeta deficit.",
        "sympy_version": sp.__version__,
        "report_sha256": hashlib.sha256((root / "FIXED_BUMP_TAUBERIAN_EQUIVALENCE.md").read_bytes()).hexdigest(),
        "checks": checks,
        "number_of_checks": len(checks),
        "nonvanishing_argument": "For real tau, 1+tau^2>0 and cosh(pi*tau/2)>0; the exact squared modulus is therefore strictly positive.",
    }
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    (root / "mellin_transform_checks.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
