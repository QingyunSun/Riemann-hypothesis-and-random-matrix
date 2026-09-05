"""Independent exact finite marked-coordinate test of the full signed operator.

This is a structural regression model, not a k=39 sieve calculation. Product
measure is nonuniform, the cap domain is not rectangular, and a radial subspace
does not contain the original polynomial subspace. Every claimed identity is
checked using rational arithmetic before any displayed eigenvalue is computed.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

import numpy as np
import sympy as sp

Q = sp.Rational
HERE = Path(__file__).resolve().parent


def main():
    # (total-cell index, fragment-cap label). Label 1 never occurs at total 0.
    atoms = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1)]
    mu = [Q(1, 2), Q(2, 9), Q(1, 9), Q(1, 18), Q(1, 9)]
    assert sum(mu) == 1
    k, rho = 3, Q(2, 5)

    def allowed(state):
        total = sum(atoms[j][0] for j in state)
        return total <= 4 and (total < 3 or max(atoms[j][1] for j in state) == 0)

    def face_weight(background):
        total = sum(atoms[j][0] for j in background)
        if total <= 1 and max(atoms[j][1] for j in background) == 0:
            return Q(1)
        return Q(3, 4) if total <= 3 else Q(-1, 4)

    states = [x for x in product(range(len(atoms)), repeat=k) if allowed(x)]
    lookup = {x: j for j, x in enumerate(states)}
    masses = sp.Matrix([sp.prod(mu[j] for j in x) for x in states])
    W = sp.diag(*masses)
    T = sp.zeros(len(states))
    for row, state in enumerate(states):
        for i in range(k):
            background = state[:i] + state[i + 1:]
            weight = rho * face_weight(background)
            for j in range(len(atoms)):
                replaced = state[:i] + (j,) + state[i + 1:]
                if replaced in lookup:
                    T[row, lookup[replaced]] += weight * mu[j]
    assert W * T == T.T * W

    def inner(x, y):
        return (x.T * W * y)[0]

    def norm2(x):
        return inner(x, x)

    def projection(columns, x):
        gram = columns.T * W * columns
        assert gram.det() != 0
        return columns * gram.inv() * (columns.T * W * x)

    totals = [sum(atoms[j][0] for j in x) for x in states]
    products = sp.Matrix([sp.prod(Q(1, 1 + atoms[j][0]) for j in x) for x in states])
    power2 = [sum(atoms[j][0] ** 2 for j in x) for x in states]
    U = sp.Matrix([[g, g * s, g * s * s, g * p] for g, s, p in zip(products, totals, power2)])
    V = sp.Matrix([[g if s == radial else 0 for radial in range(5)] for g, s in zip(products, totals)])
    PU = lambda x: projection(U, x)
    PV = lambda x: projection(V, x)
    f = U * sp.Matrix([1, Q(1, 7), Q(-1, 11), Q(2, 9)])
    action = T * f
    r = action - PU(action)
    h = PV(r)
    w = h - PU(h)
    assert U.T * W * r == sp.zeros(4, 1)
    assert U.T * W * w == sp.zeros(4, 1)
    assert norm2(r) > 0 and norm2(h) > 0 and norm2(w) > 0
    assert inner(f, T * r) == norm2(r)
    assert inner(f, T * w) == norm2(h)
    assert norm2(w) == norm2(h) - norm2(PU(h))
    assert norm2(w) <= norm2(h) <= norm2(r)
    # Radial projection and the original mass projection do not commute.
    assert PU(PV(f)) != PV(PU(f))
    wrongly_ordered = PV(action) - PU(PV(action))
    wrong_identity_error = inner(f, T * wrongly_ordered) - norm2(PV(action))
    assert wrong_identity_error != 0

    # Product conjugation requires 1/g outside, not a normalized g^2 average.
    D = sp.diag(*products)
    conjugated = D.inv() * T * D
    weighted_mass = D * W * D
    assert weighted_mass * conjugated == conjugated.T * weighted_mass
    assert products.multiply_elementwise(conjugated * D.inv() * f) == action

    # An exact negative quadratic witness rejects a PSD assumption.
    witness = sp.zeros(len(states), 1)
    witness[lookup[(0, 3, 3)]] = 1
    negative_square = inner(witness, T * witness)
    assert negative_square < 0

    f2, w2 = norm2(f), norm2(w)
    a = inner(f, action) / f2
    b = inner(w, T * w) / w2
    cross2 = inner(f, T * w) ** 2 / (f2 * w2)
    largest = (float(a + b) + ((float(a - b)) ** 2 + 4 * float(cross2)) ** .5) / 2
    assert largest > float(a)
    entries = ["mass_self_adjoint", "orthogonal_full_residual", "nonnested_compression_identity",
               "compressed_norm_chain", "projection_order_counterexample", "product_conjugation",
               "exact_indefiniteness_witness", "positive_two_dimensional_gain"]
    output = {"status": "PASS: independent rational marked-coordinate model",
              "scope": "Structural operator/projection check only; no k39 numerical or prime-gap conclusion.",
              "coordinate_atoms": atoms, "coordinate_masses": [str(x) for x in mu],
              "dimension": len(states), "U_dimension": U.cols, "radial_dimension": V.cols,
              "checks": entries,
              "exact": {"f_norm_squared": str(f2), "r_norm_squared": str(norm2(r)),
                        "h_norm_squared": str(norm2(h)), "w_norm_squared": str(w2),
                        "wrong_projection_identity_error": str(wrong_identity_error),
                        "negative_square_witness": str(negative_square),
                        "two_dimensional_a": str(a), "two_dimensional_b": str(b), "cross_squared": str(cross2)},
              "display_only": {"a": float(a), "b": float(b), "cross": float(cross2) ** .5,
                               "two_dimensional_largest": largest, "gain": largest - float(a),
                               "compressed_fraction_of_full_residual_energy": float(norm2(h) / norm2(r))},
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE / "finite_marked_operator_check.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
