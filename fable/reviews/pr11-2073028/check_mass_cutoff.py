"""Bounded finite-model check of the mass inequality; no asymptotic certificate.

Only imports the pinned source's matrix builder. Never calls either source main
or its large reproduction sweep. Run with --source PATH --out PATH.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("pinned_f3", args.source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    mp.mp.dps = 60
    integral = 2 * mp.pi * mp.si(mp.pi) - 4
    integral_quad = mp.quad(lambda u: 4 * mp.sin(mp.pi*u/2)**2/u**2, [0, 1])
    assert abs(integral - integral_quad) < mp.mpf("1e-55")
    rows = []
    for grid in (6, 8, 10):
        dim, sparse, _, _, nonzero = module.build_operators(grid)
        keys, masses = module.enumerate_partitions(grid)
        assert len(keys) == dim
        creation = sparse.toarray()
        annihilation = creation.T
        coeff = np.array([2*np.sin(np.pi*j/(2*grid))/np.sqrt(j)
                          for j in range(1, grid+1)])
        discrete = float(np.sum(coeff**2 / (np.arange(1, grid+1)/grid)))
        slack = discrete*np.diag(np.array(masses)/grid) - creation@annihilation
        min_slack = float(np.linalg.eigvalsh(slack)[0])
        operator = annihilation@creation + (creation@creation + annihilation@annihilation)/2
        eigenvalues = np.linalg.eigvalsh(operator)
        norm = float(np.max(np.abs(eigenvalues)))
        assert min_slack >= -1e-11
        assert discrete <= float(integral)
        assert norm <= 2*discrete + 1e-11
        # Independent occupation-number coefficient check, including the 1/sqrt(j).
        indices = {key: index for index, key in enumerate(keys)}
        comparisons = 0
        for index, key in enumerate(keys):
            state = dict(key)
            for j in range(1, grid-masses[index]+1):
                target = dict(state)
                target[j] = target.get(j, 0) + 1
                row = indices[tuple(sorted(target.items(), reverse=True))]
                expected = coeff[j-1]*np.sqrt(state.get(j, 0)+1)
                assert abs(creation[row, index] - expected) < 1e-14
                comparisons += 1
        assert comparisons == nonzero
        rows.append({"M": grid, "dimension": dim, "nonzero_creation": nonzero,
                     "mass_inequality_minimum_eigenvalue": min_slack,
                     "B_M_squared": discrete, "K_operator_norm": norm,
                     "K_largest_eigenvalue": float(eigenvalues[-1]),
                     "occupation_coefficient_checks": comparisons})
    fractions = {}
    for epsilon in (mp.mpf(".125"), mp.mpf(".0625")):
        z = epsilon*mp.log(2_000_000)
        fraction = 1-mp.exp(-z)*(1+z+z*z/2+z**3/6)
        fractions[str(epsilon)] = {"epsilon_log_P": str(z),
                                  "incomplete_gamma_fraction": str(fraction)}
    result = {"status": "PASS: bounded floating checks, not a spectral enclosure",
              "source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
              "B_g_squared_60dps": str(integral),
              "quadrature_formula_difference": str(abs(integral-integral_quad)),
              "small_grids": rows,
              "F1_cutoff_scalars_not_finite_prime_error_certificates": fractions,
              "not_run": "source main, refuter main, grids above M=10, prime scan",
              "claim_scope": "analytic proofs are in separate reviewed notes"}
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS: three grids, mass slack, every creation entry, integral identity.")


if __name__ == "__main__":
    main()
