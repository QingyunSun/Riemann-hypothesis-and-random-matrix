"""Projection identities and exact scalar replay of the published k=40 ledger.

Does not import or execute the official physical-integral certificate.
"""

from __future__ import annotations

from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path
import re

import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
import os
SOURCE = Path(os.environ.get("PRIME186_NUMERICS_TEXT", '/Users/qingyunsun/Library/CloudStorage/Dropbox/Research/ACUE-Astra-Handoff-2026-09-04/research-round1/prime186-work/short_gaps_numerics.txt'))


def rational(x: Fr) -> dict:
    return {"exact": str(x), "float": float(x)}


def published_scalar_replay() -> dict:
    source = SOURCE.read_text()
    start = source.index("Table 2.1: Component bounds")
    end = source.index("Consequently,", start)
    rows = []
    for line in source[start:end].splitlines():
        m = re.match(r"^\s*(L\d+|P\d+|H)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$", line)
        if m:
            rows.append({"component": m[1], **dict(zip(("q", "A", "B", "E"),
                                                     map(int, m.groups()[1:])))})
    assert len(rows) == 52
    assert sum(row["E"] for row in rows[:17]) == 38927522
    assert sum(row["E"] for row in rows[17:]) == 622829241
    for row in rows:
        c = Fr(row["q"], 10**6)
        assert c*Fr(row["A"], 10**18) + Fr(row["B"], 10**18)/c <= Fr(row["E"], 10**12)
    rho = Fr(2624989, 10**7)
    b = Fr(843183, 10**9)
    ah = Fr(2479900401, 2500000000)
    d0 = 1-ah+b
    cop = Fr(4)
    coefficient = 1-rho*b*cop
    r_sum = Fr(sum(row["A"] for row in rows), 10**18)
    v_sum = Fr(sum(row["B"] for row in rows), 10**18)
    e_sum = Fr(sum(row["E"] for row in rows), 10**12)
    alpha_upper = min(Fr(1), r_sum/(40*b))
    new_inner_weighted = Fr(1405159+32422390, 10**12)
    overlap_gain_upper = rho*d0*new_inner_weighted/(1+b)
    gram_upper = 40*v_sum
    square_debt = rho*rho*gram_upper/coefficient
    young_debt = rho*e_sum
    threshold = coefficient*e_sum/(rho*v_sum)
    result = {
        "status": "EXACT_SCALAR_REPLAY_OF_PUBLISHED_UPPER_BOUNDS_ONLY",
        "source": str(SOURCE),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "outer_rows": rows,
        "constants": {k: rational(v) for k, v in
                      {"rho": rho, "abs_bh": b, "d0": d0,
                       "C_op": cop, "positive_alpha_coefficient": coefficient}.items()},
        "bounds": {k: rational(v) for k, v in {
            "root_square_sum_over_I_floor": r_sum,
            "face_square_sum_over_I_floor": v_sum,
            "outer_Young_loss_over_I_floor": e_sum,
            "alpha_over_I_upper": alpha_upper,
            "positive_alpha_credit_over_I_upper": coefficient*alpha_upper,
            "guaranteed_alpha_lower_from_these_upper_ledgers": Fr(0),
            "inner_overlap_margin_gain_upper": overlap_gain_upper,
            "published_outer_Young_margin_debt": young_debt,
            "coarse_completed_square_margin_debt_upper": square_debt,
            "required_G_Gram_to_V_ledger_ratio_to_beat_Young": threshold,
        }.items()},
    }
    return result


def lift(face: np.ndarray, axis: int) -> np.ndarray:
    return np.expand_dims(face, axis)


def finite_projection_checks() -> dict:
    rng = np.random.default_rng(20260906)
    k, n = 3, 3
    rho, b, ah = 0.26, 0.001, 0.99
    d0 = 1-ah+b
    coefficient = 1-rho*b*k
    worst = {"exact_projection": 0.0, "exact_inner_overlap": 0.0}
    for _ in range(200):
        f = rng.normal(size=(n,)*k)  # Signed, not assumed nonnegative.
        retained = rng.uniform(size=f.shape) > 0.3
        removed = ~retained
        e = removed*f
        pf = retained*f
        ma, mb, overlap = [], [], []
        for i in range(k):
            h1 = rng.uniform(size=(n,)*(k-1)) > 0.2
            h0 = h1 & (rng.uniform(size=h1.shape) > 0.3)
            old = h0 & (rng.uniform(size=h1.shape) > 0.2)
            l1 = h1 & (rng.uniform(size=h1.shape) > 0.2)
            l0 = old & l1
            ma.append(d0*h0+ah*h1-b)
            mb.append(d0*l0+ah*l1-b)
            a = h0 & ~old
            c = h1 & ~l1
            overlap.append((a, c, (c & ~h0) | (a & c)))

        def apply(x, multipliers):
            return sum(lift(m*np.mean(x, axis=i), i) for i, m in enumerate(multipliers))

        bf = apply(f, mb)
        be = apply(e, mb)
        alpha = np.mean(e*e)
        initial = rho*np.mean(f*bf)-np.mean(f*f)
        restored = rho*np.mean(pf*apply(pf, mb))-np.mean(pf*pf)
        exact = initial+alpha-2*rho*np.mean(e*bf)+rho*np.mean(e*be)
        worst["exact_projection"] = max(worst["exact_projection"], abs(exact-restored))
        root_residual = coefficient*f*f-2*rho*f*bf
        assert restored+2e-13 >= initial+np.mean(removed*root_residual)
        completed_square = initial-rho*rho/coefficient*np.mean(removed*bf*bf)
        assert restored+2e-13 >= completed_square
        face_bound = alpha
        beta = 0.0
        beta_formula = 0.0
        for i, m in enumerate(mb):
            v = np.mean(f, axis=i)
            w = np.mean(e, axis=i)
            a_i = np.mean(removed, axis=i)
            z_i = np.mean(e*e, axis=i)
            radius = np.sqrt(a_i*z_i)
            assert np.all(np.abs(w) <= radius+1e-13)
            loss = np.maximum(m, 0)*(v*v-np.maximum(np.abs(v)-radius, 0)**2)
            loss += np.maximum(-m, 0)*(radius*radius+2*radius*np.abs(v))
            face_bound -= rho*np.mean(loss)
            a, c, correction = overlap[i]
            beta += np.mean((ma[i]-mb[i])*v*v)
            beta_formula += np.mean((d0*a+(1+b)*c-d0*correction)*v*v)
        assert restored+2e-13 >= initial+face_bound
        worst["exact_inner_overlap"] = max(worst["exact_inner_overlap"], abs(beta-beta_formula))
    assert max(worst.values()) < 2e-13
    return {"signed_finite_product_examples": 200, "dimensions": [3, 3, 3],
            "max_errors": worst, "arithmetic": "float64 diagnostic, proof is in the report",
            "all_assertions_passed": True}


if __name__ == "__main__":
    result = {"published_ledger": published_scalar_replay(),
              "finite_projection_checks": finite_projection_checks()}
    output = json.dumps(result, indent=2)
    (HERE/"restoration_checks.json").write_text(output+"\n")
    print(output)
