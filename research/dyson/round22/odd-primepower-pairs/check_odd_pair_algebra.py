#!/usr/bin/env python3
"""Bounded exact scalar checks; no prime samples or parameter scan."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    root = Path(__file__).resolve().parent
    checks = []

    def zero(name: str, expression: sp.Expr) -> None:
        assert sp.simplify(expression) == 0, (name, expression)
        checks.append({"name": name, "status": "PASS"})

    lm, ln, singular = sp.symbols("lambda_m lambda_n S")
    old = (lm - 1) * (ln - 1) - (singular - 1)
    new = lm * ln - singular * (lm + ln - 1)
    zero("exact old-to-new singleton correction", old - new - (singular - 1) * (lm + ln - 2))

    x, r, T = sp.symbols("x r T", positive=True)
    primitive = -r**T * x ** (1 - T) * (sp.log(x) / (T - 1) + 1 / (T - 1) ** 2)
    zero("decreasing logarithmic tail primitive", sp.diff(primitive, x) - (r / x) ** T * sp.log(x))
    zero("increasing power-sum comparison primitive", sp.diff(x**T / T, x) - x ** (T - 1))

    main = Fraction(33, 4) * (Fraction(16, 9) + Fraction(4, 3)) + Fraction(16, 9)
    assert main == Fraction(247, 9) < 32
    checks.append({"name": "main rational upper constant", "exact_value": str(main), "status": "PASS"})
    geometric = Fraction(2, 1) / (1 - Fraction(1, 8))
    assert geometric == Fraction(16, 7)
    checks.append({"name": "dyadic tail factor at T at least four", "exact_value": str(geometric), "status": "PASS"})
    tail = 8 * (Fraction(16, 9) + Fraction(4, 3)) * geometric
    assert tail == Fraction(512, 9) < 64
    checks.append({"name": "tail rational upper constant", "exact_value": str(tail), "status": "PASS"})
    assert Fraction(3, 2) * Fraction(11, 4) == Fraction(33, 8)
    checks.append({"name": "number-of-powers times maximum log factor", "exact_value": "33/8", "status": "PASS"})

    result = {
        "status": "PASS",
        "scope": "Seven exact algebra/primitive/rational-constant checks only; not verification of prime data or the infinite-sum ordinary proof.",
        "sympy_version": sp.__version__,
        "report_sha256": hashlib.sha256((root / "ALL_ODD_PRIMEPOWER_PAIRS.md").read_bytes()).hexdigest(),
        "checks": checks,
        "number_of_checks": len(checks),
    }
    output = json.dumps(result, indent=2) + "\n"
    (root / "odd_pair_algebra_checks.json").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
