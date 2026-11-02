#!/usr/bin/env python3
"""Small exact algebra checks, without sampling primes or scanning parameters."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    root = Path(__file__).resolve().parent
    p = sp.symbols("p", positive=True)
    checks = []

    def zero(name: str, expression: sp.Expr) -> None:
        assert sp.factor(expression) == 0, (name, expression)
        checks.append({"name": name, "status": "PASS"})

    zero("reciprocal local Euler factors", (1 - 1 / (p - 1) ** 2) * (1 + 1 / (p * (p - 2))) - 1)

    # One finite product identity; these are fixed formal local factors, not data.
    prime_factors = (3, 5, 7)
    c2 = Fraction(1)
    for prime in prime_factors:
        c2 *= 1 - Fraction(1, (prime - 1) ** 2)
    total = Fraction(0)
    for indicators in itertools.product((False, True), repeat=3):
        term = Fraction(1)
        for prime, present in zip(prime_factors, indicators):
            if present:
                term *= Fraction(1, prime * (prime - 2))
        total += term
    assert c2 * total == 1
    checks.append({"name": "finite eight-divisor Euler expansion", "status": "PASS"})

    # Generic symbols retain every singleton and the integer endpoint correction.
    lambdas = sp.symbols("l0:14")

    def psi(x: Fraction) -> sp.Expr:
        return sum(lambdas[j] for j in range(1, x.numerator // x.denominator + 1))

    prefix_cases = ((Fraction(3), Fraction(6), 1),
                    (Fraction(13, 4), Fraction(25, 4), 3),
                    (Fraction(7, 2), Fraction(6), 5))
    for number, (left, right, shift) in enumerate(prefix_cases, start=1):
        indices = range(left.numerator // left.denominator + 1, right.numerator // right.denominator + 1)
        direct = sum((lambdas[m] - 1) * (lambdas[m + shift] - 1) + 1 for m in indices)
        pair = sum(lambdas[m] * lambdas[m + shift] for m in indices)
        endpoint = 2 * (len(indices) - sp.Rational(right - left))
        error_difference = psi(right) - psi(left) - sp.Rational(right - left)
        shifted_error_difference = psi(right + shift) - psi(left + shift) - sp.Rational(right - left)
        zero(f"formal centered prefix with endpoints {number}", direct - (pair - error_difference - shifted_error_difference + endpoint))

    T, y = sp.symbols("T y", positive=True)
    tail = y ** (1 - T) * (sp.log(2 * y) ** 2 / (T - 1)
                            + 2 * sp.log(2 * y) / (T - 1) ** 2
                            + 2 / (T - 1) ** 3)
    zero("exact far-tail integral derivative", sp.diff(tail, y) + y ** (-T) * sp.log(2 * y) ** 2)
    assert Fraction(7, 4) * Fraction(-1, 2) == Fraction(-7, 8)
    checks.append({"name": "RH lower-window exponent minus seven eighths", "status": "PASS"})

    result = {
        "status": "PASS",
        "scope": "Seven exact scalar/formal-coefficient checks only. No prime samples, parameter scans, sieve verification or numerical constant enclosure.",
        "sympy_version": sp.__version__,
        "checks": checks,
        "number_of_checks": len(checks),
        "report_sha256": hashlib.sha256((root / "SMALL_SHIFT_REMOVAL.md").read_bytes()).hexdigest(),
    }
    output = json.dumps(result, indent=2) + "\n"
    (root / "small_shift_algebra_checks.json").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
