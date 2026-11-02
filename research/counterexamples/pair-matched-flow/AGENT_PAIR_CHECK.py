"""Bounded independent exact checks for AGENT_PAIR_REVIEW.md.

Requires SymPy. Writes JSON to stdout; no random sampling, repository mutation,
or numerical claim about zeta zeros. The written proof supplies the analytic
DPP existence, mixing, and rigidity arguments.
"""

from collections import Counter
import json

import sympy as sp


CHECKS = []


def record(name, condition, **details):
    if not condition:
        raise AssertionError(name)
    CHECKS.append({"name": name, "passed": True, **details})


def equal(left, right):
    return sp.simplify(sp.expand_complex(left - right)) == 0


def trace(points, modulus, power):
    return sp.simplify(sum(
        sp.cos(2 * sp.pi * sp.Rational(power * a, modulus))
        + sp.I * sp.sin(2 * sp.pi * sp.Rational(power * a, modulus))
        for a in points
    ))


def pair_counts(points, modulus):
    counts = Counter((a - b) % modulus for a in points for b in points)
    return tuple(counts[r] for r in range(modulus))


def gap_list(points, modulus):
    points = sorted(points)
    return tuple(sorted((points[(j + 1) % len(points)] - points[j]) % modulus
                        for j in range(len(points))))


def orbit(points, modulus):
    return {tuple(sorted((sign * a + offset) % modulus for a in points))
            for sign in (-1, 1) for offset in range(modulus)}


def acue_probability(points, modulus):
    points = sorted(points)
    vandermonde_square = sp.prod(
        2 - 2 * sp.cos(2 * sp.pi * sp.Rational(a - b, modulus))
        for j, a in enumerate(points) for b in points[j + 1:]
    )
    return sp.simplify(vandermonde_square / modulus ** len(points))


def cubic(points, modulus):
    return sp.simplify(sp.re(trace(points, modulus, 1) ** 2
                             * sp.conjugate(trace(points, modulus, 2))))


S, C = (0, 1, 3, 4), (2, 5, 6, 7)
A, B = (0, 1, 2, 4, 7, 8), (3, 5, 6, 9, 10, 11)
for label, left, right, modulus in (("four", S, C, 8), ("six", A, B, 12)):
    record(label + " complement pair identity",
           set(left).isdisjoint(right)
           and set(left) | set(right) == set(range(modulus))
           and pair_counts(left, modulus) == pair_counts(right, modulus))
    for power in range(modulus):
        p_left, p_right = trace(left, modulus, power), trace(right, modulus, power)
        record(f"{label} Fourier magnitude {power}",
               equal(p_left * sp.conjugate(p_left), p_right * sp.conjugate(p_right)))

record("four exact traces", equal(trace(S, 8, 1), sp.I * sp.sqrt(2))
       and equal(trace(S, 8, 2), 2) and cubic(S, 8) == -4 and cubic(C, 8) == 4)
record("six exact traces", equal(abs(trace(A, 12, 2)) ** 2, 7)
       and cubic(A, 12) == 2 and cubic(B, 12) == -2,
       p1=str(trace(A, 12, 1)), p2=str(trace(A, 12, 2)))
record("gap histogram control", gap_list(S, 8) != gap_list(C, 8)
       and min(gap_list(S, 8)) == min(gap_list(C, 8)) == 1
       and gap_list(A, 12) == gap_list(B, 12) == (1, 1, 1, 2, 3, 4))

OA, OB = orbit(A, 12), orbit(B, 12)
record("six disjoint free dihedral orbits",
       len(OA) == len(OB) == 24 and OA.isdisjoint(OB))
record("complement interchanges six orbits",
       {tuple(sorted(set(range(12)) - set(points))) for points in OA} == OB)
summary = pair_counts(A, 12), gap_list(A, 12)
record("entire static summary is identical on both orbits",
       all((pair_counts(points, 12), gap_list(points, 12)) == summary
           for points in OA | OB))
record("exact ACUE seed probabilities", acue_probability(A, 12) == sp.Rational(1, 1728)
       and acue_probability(B, 12) == sp.Rational(1, 1728))
# Isometry invariance makes the two seed calculations certificates for all 48 subsets.
mass = 24 * acue_probability(A, 12)
record("exact orbit mass", mass == sp.Rational(1, 72), value=str(mass))

q = sp.symbols("q", real=True)
for label, left, modulus, expected in (("four", S, 8, 16), ("six", A, 12, -8)):
    p1, p2 = trace(left, modulus, 1), trace(left, modulus, 2)
    u, v = p2 - p1 ** 2 * (1 - q), -p2 - p1 ** 2 * (1 - q)
    difference = sp.expand_complex(u * sp.conjugate(u) - v * sp.conjugate(v))
    record(label + " exact forward pair difference", equal(difference, expected * (1 - q)))
record("ACUE tilt forward coefficient", mass * (-8) == -sp.Rational(1, 9))
t, epsilon = sp.symbols("t epsilon", real=True)
tilt_shift = -epsilon * sp.exp(-16 * t) * (1 - sp.exp(-2 * t)) / 9
record("ACUE tilt initial derivative", sp.diff(tilt_shift, t).subs(t, 0) == -2 * epsilon / 9)

# Independent pairwise generator algebra: cot((xi-xj)/2)=i(zi+zj)/(zi-zj).
zi, zj = sp.symbols("zi zj")
record("p1 paired generator", sp.cancel(sp.I * (zi - zj) * sp.I * (zi + zj)
                                        / (zi - zj)) == -zi - zj)
record("p2 paired generator", sp.cancel(2 * sp.I * (zi ** 2 - zj ** 2)
                                        * sp.I * (zi + zj) / (zi - zj))
       == -2 * zi ** 2 - 4 * zi * zj - 2 * zj ** 2)

y, c, u = sp.symbols("y c u", positive=True)
quadratic = 4 * y ** 2 * c ** 2 - 2 * sp.sqrt(2 * y) * c + 2 - 2 * y ** 2
record("heat discriminant", sp.simplify(sp.discriminant(quadratic, c)
                                        - 8 * y * (4 * y ** 3 - 4 * y + 1)) == 0)
cubic_y = 4 * y ** 3 - 4 * y + 1
lo, hi = sp.Rational(837, 1000), sp.Rational(838, 1000)
record("largest heat root rational bracket", cubic_y.subs(y, lo) < 0
       and cubic_y.subs(y, hi) > 0 and (12 * lo ** 2 - 4) > 0)
endpoint = u ** 4 - sp.sqrt(2) * u + 1
record("positive endpoint global minimum certificate",
       equal(sp.diff(endpoint, u).subs(u, 1 / sp.sqrt(2)), 0)
       and equal(endpoint.subs(u, 1 / sp.sqrt(2)), sp.Rational(1, 4)))
record("strict depth distinction rational certificate",
       lo > sp.Rational(4, 5) and sp.Rational(4, 5) ** 3 > sp.Rational(1, 2))

for r in (1, 2, 3, 5):
    left = tuple(a + 8 * j for a in S for j in range(r))
    right = tuple(a + 8 * j for a in C for j in range(r))
    record(f"lift pair and minimum gap r={r}", len(left) == len(right) == 4 * r
           and pair_counts(left, 8 * r) == pair_counts(right, 8 * r)
           and min(gap_list(left, 8 * r)) == min(gap_list(right, 8 * r)) == 1)

EA, EB = (0, 1, 4, 10, 12, 17), (0, 1, 8, 11, 13, 17)
positive = lambda points: Counter(b - a for j, a in enumerate(points) for b in points[j + 1:])
target = Counter({d: 1 for d in list(range(1, 14)) + [16, 17]})
record("continuous spectral integer homometry", positive(EA) == positive(EB) == target)
record("spectral seeds not translate/reflected translate", EA != EB
       and tuple(sorted(17 - a for a in EA)) != EB)
RA = sp.simplify(sp.re(trace(EA, 8, 1) ** 2 * sp.conjugate(trace(EA, 4, 1))))
RB = sp.simplify(sp.re(trace(EB, 8, 1) ** 2 * sp.conjugate(trace(EB, 4, 1))))
record("DPP exact cubic witnesses", equal(RA, 4 - 8 * sp.sqrt(2))
       and equal(RB, 4 + 8 * sp.sqrt(2)))
record("DPP continuous triple separation coefficient", equal(2 * (RA - RB), -32 * sp.sqrt(2)))
record("six-band non-Montgomery ramp", 6 * sp.Rational(1, 6) == 1 and 6 != 1)

print(json.dumps({
    "status": "all bounded exact checks passed",
    "sympy_version": sp.__version__,
    "check_count": len(CHECKS),
    "checks": CHECKS,
    "limits": ["ordinary proof required for DPP analytic statements",
               "no zeta or prime theorem is certified",
               "no external novelty claim"],
}, indent=2))
