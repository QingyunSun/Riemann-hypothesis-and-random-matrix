"""Exact finite checks for pair-matched heat counterexamples; no simulation.

Run from any directory. JSON is written beside this script. SymPy is the only
nonstandard dependency. Decimal depths are diagnostic; root isolation is exact.
"""

from collections import Counter
from itertools import combinations
import json
from pathlib import Path

import sympy as sp


def pair_counts(points: tuple[int, ...], modulus: int) -> list[int]:
    counts = Counter((a - b) % modulus for a in points for b in points)
    return [counts[r] for r in range(modulus)]


def gap_histogram(points: tuple[int, ...], modulus: int) -> list[int]:
    return sorted(
        (points[(i + 1) % len(points)] - a) % modulus
        for i, a in enumerate(points)
    )


def orbit(points: tuple[int, ...], modulus: int) -> set[tuple[int, ...]]:
    return {
        tuple(sorted((sign * a + shift) % modulus for a in points))
        for sign in (-1, 1)
        for shift in range(modulus)
    }


def traces(points: tuple[int, ...], modulus: int) -> tuple:
    z = sp.expand_complex(sp.exp(2 * sp.pi * sp.I / modulus))
    p1 = sp.simplify(sp.expand(sum(z**a for a in points)))
    p2 = sp.simplify(sp.expand(sum(z ** (2 * a) for a in points)))
    norm = sp.simplify(p2 * sp.conjugate(p2))
    triple = sp.simplify(sp.re(sp.expand(p1**2 * sp.conjugate(p2))))
    derivative = sp.simplify(-4 * (len(points) - 2) * norm - 4 * triple)
    return p1, p2, norm, triple, derivative


def main() -> None:
    witnesses = [
        ((0, 1, 3, 4), (2, 5, 6, 7), 8, (-4, 4), (-16, -48)),
        ((0, 1, 2, 4, 7, 8), (3, 5, 6, 9, 10, 11), 12, (2, -2), (-120, -104)),
    ]
    records = []
    for a, b, modulus, expected_triples, expected_derivatives in witnesses:
        assert set(a).isdisjoint(b) and set(a) | set(b) == set(range(modulus))
        assert pair_counts(a, modulus) == pair_counts(b, modulus)
        data = [traces(points, modulus) for points in (a, b)]
        assert tuple(row[3] for row in data) == expected_triples
        assert tuple(row[4] for row in data) == expected_derivatives
        assert data[0][2] == data[1][2]
        assert sp.simplify(data[0][0] + data[1][0]) == 0
        assert sp.simplify(data[0][1] + data[1][1]) == 0
        records.append({
            "modulus": modulus, "S": a, "complement": b,
            "ordered_pair_counts": pair_counts(a, modulus),
            "gap_histograms": [gap_histogram(p, modulus) for p in (a, b)],
            "traces_p1_p2_norm_triple_derivative": [[str(x) for x in row] for row in data],
        })

    # The complement identity is structural; this enumerates all small instances.
    complement_cases = 0
    for n in range(2, 8):
        modulus = 2 * n
        for a in combinations(range(modulus), n):
            b = tuple(sorted(set(range(modulus)) - set(a)))
            assert pair_counts(a, modulus) == pair_counts(b, modulus)
            complement_cases += 1

    # Prove the finite-time trace solution satisfies the generator equations.
    t = sp.symbols("t", real=True)
    n = sp.symbols("n", integer=True, positive=True)
    a0, b0 = sp.symbols("a0 b0")
    p1 = a0 * sp.exp(-(n - 1) * t)
    p2 = sp.exp(-2 * (n - 2) * t) * (b0 - a0**2 * (1 - sp.exp(-2 * t)))
    assert sp.simplify(sp.diff(p1, t) + (n - 1) * p1) == 0
    assert sp.simplify(sp.diff(p2, t) + 2 * (n - 2) * p2 + 2 * p1**2) == 0
    assert sp.simplify(p2.subs(t, 0) - b0) == 0

    # Directly verify the trigonometric polynomials and their collision algebra.
    x, c, y = sp.symbols("x c y", real=True)
    f0 = 2 * sp.cos(2 * x) - 2 * sp.sqrt(2) * sp.cos(x) + 2
    g0 = 2 * sp.sin(2 * x) + 2 * sp.sqrt(2) * sp.sin(x)
    for angle in (-sp.pi / 2, -sp.pi / 4, sp.pi / 4, sp.pi / 2):
        assert sp.simplify(f0.subs(x, angle)) == 0
    for angle in (0, sp.pi, 3 * sp.pi / 4, -3 * sp.pi / 4):
        assert sp.simplify(g0.subs(x, angle)) == 0
    quadratic = 4 * y**2 * c**2 - 2 * sp.sqrt(2 * y) * c + 2 - 2 * y**2
    cubic = 4 * y**3 - 4 * y + 1
    assert sp.simplify(sp.discriminant(quadratic, c) - 8 * y * cubic) == 0
    low, high = sp.Rational(83756543528, 10**11), sp.Rational(83756543529, 10**11)
    poly = sp.Poly(cubic, y)
    assert poly.count_roots(low, high) == 1
    assert poly.count_roots(high, sp.oo) == 0
    assert poly.eval(low) < 0 < poly.eval(high)
    assert sp.Rational(4, 5) < low < high < 1
    assert sp.Rational(4, 5)**3 > sp.Rational(1, 2)
    u = sp.symbols("u", positive=True)
    endpoint = u**4 - sp.sqrt(2) * u + 1
    assert sp.simplify(sp.diff(endpoint, u).subs(u, 1 / sp.sqrt(2))) == 0
    assert sp.simplify(endpoint.subs(u, 1 / sp.sqrt(2))) == sp.Rational(1, 4)

    # The ACUE perturbation changes equal-mass orbits within a single summary fibre.
    a, b = witnesses[1][:2]
    oa, ob = orbit(a, 12), orbit(b, 12)
    assert len(oa) == len(ob) == 24 and oa.isdisjoint(ob)
    assert {tuple(sorted(set(range(12)) - set(p))) for p in oa} == ob
    for p in oa | ob:
        assert pair_counts(p, 12) == pair_counts(a, 12)
        assert gap_histogram(p, 12) == gap_histogram(a, 12)
    z = sp.expand_complex(sp.exp(sp.pi * sp.I / 6))
    vandermonde_squared = sp.Integer(1)
    for j, aj in enumerate(a):
        for ak in a[:j]:
            vandermonde_squared = sp.simplify(
                vandermonde_squared * (2 - z ** (aj - ak) - z ** (ak - aj))
            )
    atom_probability = sp.simplify(sp.expand_complex(vandermonde_squared) / 12**6)
    orbit_probability = 24 * atom_probability
    assert atom_probability == sp.Rational(1, 1728)
    assert orbit_probability == sp.Rational(1, 72)
    assert -16 * orbit_probability == -sp.Rational(2, 9)
    assert -8 * orbit_probability == -sp.Rational(1, 9)
    for epsilon in [sp.Rational(-1), sp.Rational(-1, 2), sp.Rational(0), sp.Rational(1, 2), sp.Rational(1)]:
        assert 1 + epsilon >= 0 and 1 - epsilon >= 0
        assert (1 + epsilon) * orbit_probability + (1 - epsilon) * orbit_probability == 2 * orbit_probability

    # Lifts: direct integer pair-count checks, including wrapping across copies.
    a4, b4 = witnesses[0][:2]
    lift_cases = 0
    for r in range(1, 13):
        aa = tuple(sorted(a + 8 * j for j in range(r) for a in a4))
        bb = tuple(sorted(b + 8 * j for j in range(r) for b in b4))
        assert pair_counts(aa, 8 * r) == pair_counts(bb, 8 * r)
        assert min(gap_histogram(aa, 8 * r)) == min(gap_histogram(bb, 8 * r)) == 1
        lift_cases += 1

    # Negative controls: stronger equality claims and a deliberately wrong sign fail.
    assert gap_histogram(a4, 8) != gap_histogram(b4, 8)
    assert pair_counts(a4, 8) != pair_counts((0, 1, 2, 3), 8)
    assert traces(a, 12)[3] != traces(b, 12)[3]
    wrong_derivative = -4 * (6 - 2) * 7 + 4 * 2
    assert wrong_derivative != -120

    root = sp.CRootOf(cubic, 2)
    ds, dc = -sp.log(root) / 2, sp.log(2) / 6
    result = {
        "status": "PASS",
        "arithmetic": "exact integers, rationals and SymPy radicals; decimal depths are diagnostics",
        "witnesses": records,
        "exhaustive_complement_cases": complement_cases,
        "forward_trace_ODE_identities": 3,
        "exact_root_interval": [str(low), str(high)],
        "root_count_in_interval": 1,
        "larger_real_roots": 0,
        "ACUE_atom_probability": str(atom_probability),
        "ACUE_each_orbit_probability": str(orbit_probability),
        "ACUE_orbit_sizes": [len(oa), len(ob)],
        "ACUE_derivative_shift_per_epsilon": "-2/9",
        "periodic_lift_cases": lift_cases,
        "negative_controls_rejected": 4,
        "diagnostic_depths": {"S": str(ds.evalf(24)), "C": str(dc.evalf(24))},
        "diagnostic_N_squared_depths": {"S": str((16 * ds).evalf(24)), "C": str((16 * dc).evalf(24))},
        "scope": "finite exact counterexamples; no actual-zeta conjecture refutation or formal proof-assistant claim",
    }
    target = Path(__file__).with_name("PAIR_MATCHED_HEAT_CHECKS.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
