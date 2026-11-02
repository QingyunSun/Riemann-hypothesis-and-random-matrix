#!/usr/bin/env python3
"""Independent exact algebra audit of force_energy.md; no floating arithmetic."""
from __future__ import annotations

import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

BASE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "generator_audit_dependency", BASE.parent / "dynamic-generator" / "generator_audit.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)
CyclotomicRing = MODULE.CyclotomicRing


def scaled(a: tuple, scalar) -> tuple:
    return tuple(scalar * x for x in a)


def inverse(ring, a: tuple) -> tuple:
    z = sp.Symbol("z")
    polynomial = sp.Poly(sum(x * z**k for k, x in enumerate(a)), z, domain=sp.QQ)
    modulus = sp.Poly(sp.cyclotomic_poly(ring.order, z), z, domain=sp.QQ)
    inv = sp.invert(polynomial, modulus)
    result = tuple(Fraction(int(inv.nth(k).p), int(inv.nth(k).q)) for k in range(ring.degree))
    assert ring.multiply(result, a) == ring.one
    return result


def direct_exact(n: int) -> dict:
    ring = CyclotomicRing(2 * n)
    w, b = {}, {}
    for d in range(1, 2 * n):
        root = ring.power(d)
        gap = ring.add(root, scaled(ring.one, -1))
        b[d] = ring.multiply(ring.add(root, ring.one), inverse(ring, gap))
        squared_distance = ring.add(
            scaled(ring.one, 2), scaled(ring.add(root, ring.power(-d)), -1)
        )
        w[d] = scaled(inverse(ring, squared_distance), 4)
    total_weight = ring.zero
    total_d = ring.zero
    total_ld = ring.zero
    count = 0
    for sites in itertools.combinations(range(2 * n), n):
        count += 1
        weight = ring.one
        for i, j in itertools.combinations(range(n), 2):
            d = sites[i] - sites[j]
            gap = ring.add(scaled(ring.one, 2),
                           scaled(ring.add(ring.power(d), ring.power(-d)), -1))
            weight = ring.multiply(weight, gap)
        forces_without_i = []
        for i in range(n):
            value = ring.zero
            for j in range(n):
                if j != i:
                    value = ring.add(value, b[(sites[i] - sites[j]) % (2 * n)])
            forces_without_i.append(value)
        energy = ring.zero
        derivative = ring.zero
        reduced_derivative = ring.zero
        # V_i = i*B_i, so D=-sum B_i^2 and LD=+sum w_ij(B_i-B_j)^2.
        for value in forces_without_i:
            energy = ring.add(energy, scaled(ring.multiply(value, value), -1))
        for i, j in itertools.combinations(range(n), 2):
            wij = w[(sites[i] - sites[j]) % (2 * n)]
            difference = ring.add(forces_without_i[i], scaled(forces_without_i[j], -1))
            derivative = ring.add(derivative, ring.multiply(wij, ring.multiply(difference, difference)))
            reduced_derivative = ring.add(
                reduced_derivative, scaled(ring.add(ring.multiply(wij, wij), scaled(wij, -1)), -4)
            )
        for i, j, k in itertools.combinations(range(n), 3):
            a = w[(sites[i] - sites[j]) % (2 * n)]
            bpair = w[(sites[i] - sites[k]) % (2 * n)]
            c = w[(sites[j] - sites[k]) % (2 * n)]
            for x, y in ((a, bpair), (a, c), (bpair, c)):
                reduced_derivative = ring.add(reduced_derivative, ring.multiply(x, y))
        assert derivative == reduced_derivative
        total_weight = ring.add(total_weight, weight)
        total_d = ring.add(total_d, ring.multiply(weight, energy))
        total_ld = ring.add(total_ld, ring.multiply(weight, derivative))
    denominator = (2 * n) ** n
    target_d = Fraction(n * (n * n - 1), 6)
    target_ld = Fraction(-2 * n * (n**4 - 1), 15)
    assert total_weight == scaled(ring.one, denominator)
    assert total_d == scaled(ring.one, denominator * target_d)
    assert total_ld == scaled(ring.one, denominator * target_ld)
    return {"N": n, "subsets": count, "ED": str(target_d), "ELD": str(target_ld),
            "normalization_exact": True, "pointwise_pair_triple_reduction_exact": True,
            "direct_force_expectations_exact": True}


def main() -> None:
    c, a, n = sp.symbols("c a N")
    b = (c * a - 1) / (c + a)
    triple = ((1 + c*c)*c*(b-a) + (1+b*b)*b*(c+a) + (1+a*a)*a*(b-c)
              + sp.Rational(1, 2)*((1+c*c)*(1+a*a)+(1+c*c)*(1+b*b)+(1+a*a)*(1+b*b)))
    assert sp.cancel(triple) == 0
    s2 = (4*n*n-1)/3
    s4 = (16*n**4+40*n*n-11)/45
    o4 = n*n*(n*n+2)/3
    o6 = n*n*(2*n**4+5*n*n+8)/15
    expression = 2*n/sp.Integer(16)*(s2*s2-9*s4+8*s2+16*o6/n**2
                                     -16*(n*n+2)*o4/(3*n*n))
    target = -2*n*(n**4-1)/15
    assert sp.cancel(expression-target) == 0
    t = sp.Symbol("M")
    full_six = (2*t**6+21*t**4+168*t*t-191)/945
    assert sp.cancel(full_six.subs(t, 2*n)-full_six.subs(t, n)-o6) == 0
    full_four = (t**4+10*t*t-11)/45
    assert sp.cancel(full_four.subs(t, 2*n)-full_four.subs(t, n)-o4) == 0
    output = {
        "status": "exact symbolic and cyclotomic audit; mathematical Fatou argument reviewed separately",
        "sympy_version": sp.__version__,
        "triple_identity_exact": True,
        "all_N_final_polynomial_identity_exact": True,
        "odd_cosecant_fourth_and_sixth_sums_exact": True,
        "independent_direct_force_enumeration": [direct_exact(k) for k in range(2, 5)],
        "dependency": "dynamic-generator/generator_audit.py: CyclotomicRing only",
    }
    path = BASE / "force_energy_review_results.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
