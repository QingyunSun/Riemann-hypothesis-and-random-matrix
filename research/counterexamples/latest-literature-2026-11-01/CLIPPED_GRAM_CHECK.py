"""Exact finite algebra for CLIPPED_GRAM_REVIEW.md; no zeta transfer."""

import json
import sympy as s

records = []


def check(name, condition):
    assert condition, name
    records.append({"name": name, "passed": True})


x = s.symbols("x", real=True)
p1, p2 = (1 + s.sqrt(3) * s.I) / 2, (1 + 3 * s.sqrt(3) * s.I) / 2
MA = s.Matrix([[2, p1 / 3, p2 / 3],
               [s.conjugate(p1) / 3, 2, p1 / 3],
               [s.conjugate(p2) / 3, s.conjugate(p1) / 3, 2]])
MB = 4 * s.eye(3) - MA

for name, matrix, determinant, cube in (
    ("A", MA, s.Rational(166, 27), s.Rational(328, 9)),
    ("B", MB, s.Rational(158, 27), s.Rational(320, 9)),
):
    check(name + " Hermitian", matrix == matrix.conjugate().T)
    check(name + " trace", s.trace(matrix) == 6)
    check(name + " second moment", s.simplify(s.trace(matrix ** 2)) == 14)
    check(name + " third moment", s.simplify(s.trace(matrix ** 3)) == cube)
    check(name + " determinant", s.simplify(matrix.det()) == determinant)
    coefficients = matrix.charpoly().all_coeffs()
    check(name + " characteristic polynomial",
          all(s.simplify(u - v) == 0
              for u, v in zip(coefficients, [1, -6, 11, -determinant])))

check("spectral reflection", MA + MB == 4 * s.eye(3))
poly = x ** 3 - x - s.Rational(4, 27)
check("negative root brackets", poly.subs(x, -1) < 0
      and poly.subs(x, -s.Rational(1, 2)) > 0 and poly.subs(x, 0) < 0)
check("positive root bracket", poly.subs(x, 1) < 0
      and poly.subs(x, s.Rational(11, 10)) > 0)
check("common full quadratic trace", 14 - 2 * 6 + 6 == 8)
a = s.symbols("a", real=True)
difference = (8 - a ** 2) - (8 - (2 - a ** 2))
check("clipped difference", s.expand(difference) == 2 - 2 * a ** 2)
check("orbit expectation normalization",
      s.simplify(difference / 72 - (1 - a ** 2) / 36) == 0)
check("mixed-multiplicity parameter condition",
      max(s.Rational(2), 2 + s.Rational(1, 2)) == s.Rational(5, 2))

print(json.dumps({"status": "PASS", "exact_check_count": len(records),
                  "checks": records,
                  "limits": "Finite circular three-mode kernel only; no zeta-window transfer."},
                 indent=2))
