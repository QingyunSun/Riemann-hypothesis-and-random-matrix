"""Exact algebraic certificate that the frozen radial vector is outside old U.

This certifies linear independence, not a Rayleigh-value enclosure. Floating
witness entries are interpreted as their exact stored binary rational values.
"""
from pathlib import Path
from fractions import Fraction as F
import ast
import hashlib
import json
import os
import random

import numpy as np

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / "residual-trial/radial_residual_n98304_cut1e-09_tilt20_compact.npz"
SOURCE_SHA = "7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4"


def main():
    source = Path(os.environ["PRIME186_SOURCE"])
    assert hashlib.sha256(source.read_bytes()).hexdigest() == SOURCE_SHA
    signatures = None
    for node in ast.parse(source.read_text()).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and getattr(node.targets[0], "id", None) == "COEFFICIENT_SIGNATURES":
            signatures = tuple(map(tuple, ast.literal_eval(node.value)))
    assert signatures is not None and len(signatures) == 11
    degree = 6 + max(map(sum, signatures))
    assert degree == 12
    with np.load(INPUT, allow_pickle=False) as z:
        radial = z["h"]
    nonzero = np.flatnonzero(radial)
    j_star = int(nonzero[0])
    value = F.from_float(float(radial[j_star]))
    assert value != 0 and j_star == 18422
    assert np.array_equal(radial[:degree + 1], np.zeros(degree + 1))

    k, N = 39, 98304
    rho, rs = F(".262499"), F(".2624989")
    S = F(".2742997") / rs
    mesh = S / N
    T0, T1 = F("1.997") - S, F(".251") / rs
    eps = F(1, 10**7) / rho
    minimum_cap = F(63, 160) * (T0 + eps / 2)
    first_outer_upper = F(1, 2) / rho - T1
    # Every selected coordinate cell is below every cap, and the whole product
    # cell is strictly inside the first outer shell. Its exact mass is mesh^k.
    assert (j_star + 1) * mesh < minimum_cap
    assert (j_star + k) * mesh < first_outer_upper

    # Optional second witness: rank77 of exact evaluations modulo a prime.
    # Dividing each positive G factor leaves the actual polynomial basis.
    prime = 1_000_000_007
    def mod(x):
        x = F(x)
        return x.numerator % prime * pow(x.denominator % prime, -1, prime) % prime
    mh, half, center = mod(mesh), mod(F(1, 2)), mod(F(9, 10))
    basis = [(sig, d) for sig in signatures for d in range(7)]
    pivots, selected = {}, []
    rng = random.Random(18639)
    for _ in range(512):
        indices = tuple(rng.randrange(9) for _ in range(6))
        assert sum(indices) < j_star and radial[sum(indices)] == 0
        ts = [((j + half) * mh) % prime for j in indices] + [(half * mh) % prime] * (k - 6)
        powers = {p: sum(pow(t, p, prime) for t in ts) % prime for p in range(1, 7)}
        centered = (powers[1] - center) % prime
        row = []
        for sig, d in basis:
            item = pow(centered, d, prime)
            for exponent in sig:
                item = item * powers[exponent] % prime
            row.append(item)
        for column, pivot in sorted(pivots.items()):
            multiplier = row[column]
            if multiplier:
                row = [(a - multiplier * b) % prime for a, b in zip(row, pivot)]
        leading = next((i for i, v in enumerate(row) if v), None)
        if leading is not None:
            inverse = pow(row[leading], -1, prime)
            pivots[leading] = [(v * inverse) % prime for v in row]
            selected.append(indices)
        if len(pivots) == 77:
            break
    assert len(pivots) == len(selected) == 77
    assert (48 + k) * mesh < first_outer_upper
    assert 9 * mesh < minimum_cap
    # The radial column is zero on all77 rows, and nonzero on the extra state.
    # Hence the augmented matrix has rank78 over Q. The13-zero proof above
    # independently excludes radial membership without this rank computation.
    result = {"status": "PASS: exact outside-span and dimension78 certificate for the frozen profile",
              "source_sha256": SOURCE_SHA, "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
              "restricted_polynomial_degree_bound": degree, "zero_indices": list(range(degree + 1)),
              "nonzero_index": j_star, "nonzero_exact_binary_rational": str(value),
              "mesh": str(mesh), "minimum_cap": str(minimum_cap),
              "first_outer_upper": str(first_outer_upper),
              "single_coordinate_cap_slack": str(minimum_cap - (j_star + 1) * mesh),
              "whole_cell_outer_slack": str(first_outer_upper - (j_star + k) * mesh),
              "positive_product_cell_mass": {"base": str(mesh), "exponent": k},
              "modular_rank": 77, "modulus_prime": prime,
              "rank_witness_first_six_cell_indices": selected,
              "remaining_coordinate_indices": [0] * (k - 6),
              "augmented_rank_over_rationals": 78,
              "scope": "Exact membership and linear independence only. The new quotient and projection norms remain floating diagnostics; no arithmetic support restoration is certified."}
    (HERE / "outside_span_certificate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("rank_witness_first_six_cell_indices", "remaining_coordinate_indices")}, indent=2))


if __name__ == "__main__":
    main()
