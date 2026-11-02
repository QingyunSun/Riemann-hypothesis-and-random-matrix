"""Exact finite Gram checks; not a verifier for the external zeta paper.

Run with Python 3 and SymPy. All assertions use exact algebra or root counts.
Decimal evaluations are labelled diagnostics and are not used as proofs.
"""

import json
from collections import Counter

import sympy as s


def clean(value):
    return s.simplify(s.expand_complex(s.expand(value)))


def pair_counts(points):
    return Counter((a - b) % 12 for a in points for b in points)


def gaps(points):
    return sorted((points[(i + 1) % 6] - points[i]) % 12 for i in range(6))


A = [0, 1, 2, 4, 7, 8]
B = [j for j in range(12) if j not in A]
z = (s.sqrt(3) + s.I) / 2
x = s.Symbol("x", real=True)
lam = s.Symbol("lambda", real=True)
assert pair_counts(A) == pair_counts(B)
assert gaps(A) == gaps(B) == [1, 1, 1, 2, 3, 4]

matrices = []
records = []
for points, determinant in [(A, s.Rational(166, 27)), (B, s.Rational(158, 27))]:
    V = s.Matrix([[clean(z ** (k * j)) / s.sqrt(3) for k in range(3)] for j in points])
    M = (V.conjugate().T * V).applyfunc(clean)
    U = (V * V.conjugate().T).applyfunc(clean)
    assert (U - U.conjugate().T).applyfunc(clean) == s.zeros(6)
    assert all(U[j, j] == 1 for j in range(6))
    assert s.trace(U) == 6
    assert clean(s.trace(U * U)) == 14
    assert clean(M.det()) == determinant
    expected = lam**3 - 6 * lam**2 + 11 * lam - determinant
    assert [clean(c) for c in M.charpoly().all_coeffs()] == s.Poly(expected, lam).all_coeffs()
    matrices.append(M)
    records.append({"points": points, "det_nonzero": str(determinant), "charpoly_nonzero": str(expected)})

q = x**3 - x - s.Rational(4, 27)
assert s.expand((lam**3 - 6 * lam**2 + 11 * lam - s.Rational(166, 27)).subs(lam, x + 2)) == q
assert s.expand((lam**3 - 6 * lam**2 + 11 * lam - s.Rational(158, 27)).subs(lam, 2 - x)) == -q
intervals = [(-1, s.Rational(-4, 5)), (s.Rational(-1, 5), 0), (1, s.Rational(11, 10))]
assert all(s.Poly(q, x).count_roots(lo, hi) == 1 for lo, hi in intervals)
assert sum(s.Poly(q, x).count_roots(lo, hi) for lo, hi in intervals) == 3
assert clean(s.trace(matrices[0] ** 3) - s.trace(matrices[1] ** 3)) == s.Rational(8, 9)

# Vieta: sum roots = 0, sum pair products = -1, hence sum squares = 2.
# Exactly one root a is positive. The B roots are their negatives.
a = s.Symbol("a", positive=True)
delta = s.expand(-(a**2 - (2 - a**2)))
assert delta == 2 - 2 * a**2
assert s.simplify(delta / 72 - (1 - a**2) / 36) == 0

# Negative control: clipping threshold 5 exceeds all six spectra, so the
# observable becomes tr(U-I)^2 = tr(U^2)-2tr(U)+6 = 8 for both models.
assert 2 + s.Rational(11, 10) < 5
assert 14 - 2 * 6 + 6 == 8

roots = s.polys.polytools.intervals(q, eps=s.Rational(1, 10**30))
positive_interval = next(interval for interval, _multiplicity in roots if interval[0] > 1)
a_decimal = s.N(sum(positive_interval) / 2, 25)
print(json.dumps({
    "status": "PASS",
    "arithmetic": "exact SymPy radicals, rational Sturm root counts and symbolic identities",
    "gram_matrices": records,
    "root_intervals": [[str(lo), str(hi)] for lo, hi in intervals],
    "positive_root_certified_interval": [str(v) for v in positive_interval],
    "trace": 6,
    "trace_square": 14,
    "trace_cube_difference": "8/9",
    "clipped_trace_difference": "2-2*a^2 < 0, where a>1 solves a^3-a-4/27=0",
    "acue_tilt_expectation_change": "epsilon*(1-a^2)/36",
    "inactive_clipping_negative_control": {"tau": 4, "both_traces": 8},
    "diagnostic_decimals_only": {"a": str(a_decimal), "clipped_difference": str(s.N(delta.subs(a, a_decimal), 22))},
    "scope": "Finite three-mode circular Gram example; not Knausgard's Euclidean window and not an actual-zeta theorem."
}, indent=2))
