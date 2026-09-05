"""Floating-point exhaustive checks of the circular force-energy identities.

All N-subsets of the 2N grid are visited for N=2,...,10.  Enumeration is
exhaustive, but weights/expectations are FLOATING POINT, not exact arithmetic.
The mathematical proofs are in force_energy.md.
"""

from __future__ import annotations

from itertools import combinations, islice
import json
from math import comb
from pathlib import Path
import time

import numpy as np


HERE = Path(__file__).resolve().parent


def acue_expectations(n: int, batch_size: int = 4096) -> dict:
    m = 2 * n
    differences = np.arange(1, m)
    angles = np.pi * differences / m
    cot = np.zeros(m)
    csc2 = np.zeros(m)
    log_vand2 = np.zeros(m)
    cot[1:] = 1 / np.tan(angles)
    csc2[1:] = 1 / np.sin(angles) ** 2
    log_vand2[1:] = np.log(4 * np.sin(angles) ** 2)
    upper_i, upper_j = np.triu_indices(n, 1)
    iterator = combinations(range(m), n)
    mass = energy = pair_energy = generator_energy = 0.0
    identity_error = 0.0
    seen = 0
    constant = n * (n*n - 1) / 3
    while True:
        subset_list = list(islice(iterator, batch_size))
        if not subset_list:
            break
        subsets = np.asarray(subset_list, dtype=np.int64)
        diff = (subsets[:, :, None] - subsets[:, None, :]) % m
        force = cot[diff].sum(axis=2)
        d_value = (force * force).sum(axis=1)
        q_value = csc2[diff].sum(axis=(1, 2))
        pair_diff = diff[:, upper_i, upper_j]
        weight = np.exp(log_vand2[pair_diff].sum(axis=1) - n*np.log(m))
        force_diff = force[:, upper_i] - force[:, upper_j]
        ld_value = -(csc2[pair_diff] * force_diff**2).sum(axis=1)
        mass += float(weight.sum())
        energy += float(weight @ d_value)
        pair_energy += float(weight @ q_value)
        generator_energy += float(weight @ ld_value)
        identity_error = max(identity_error, float(np.max(np.abs(d_value - q_value + constant))))
        seen += len(subsets)

    predicted_d = n * (n*n - 1) / 6
    predicted_q = n * (n*n - 1) / 2
    predicted_ld = -2 * n * (n**4 - 1) / 15
    assert seen == comb(m, n)
    assert abs(mass - 1) < 2e-12
    assert abs(energy - predicted_d) < 2e-9
    assert abs(pair_energy - predicted_q) < 2e-9
    assert identity_error < 2e-8
    assert np.isfinite(generator_energy)
    assert abs(generator_energy - predicted_ld) < 2e-8
    return {
        "N": n,
        "subsets_visited": seen,
        "floating_mass": mass,
        "floating_E_D": energy,
        "proved_E_D": predicted_d,
        "floating_E_Q": pair_energy,
        "proved_E_Q": predicted_q,
        "floating_E_L_D": generator_energy,
        "proved_E_L_D": predicted_ld,
        "max_pointwise_identity_error": identity_error,
        "arithmetic": "float64, not exact enumeration arithmetic",
    }


def energy_and_generator(theta: np.ndarray) -> tuple[float, float]:
    n = len(theta)
    mask = ~np.eye(n, dtype=bool)
    x = (theta[:, None] - theta[None, :]) / 2
    c = np.zeros((n, n))
    w = np.zeros((n, n))
    c[mask] = 1 / np.tan(x[mask])
    w[mask] = 1 / np.sin(x[mask])**2
    v = c.sum(axis=1)
    d = float(v @ v)
    ld = -0.5 * float(np.sum(w * (v[:, None] - v[None, :])**2))
    return d, ld


def directional_derivative_checks() -> list[dict]:
    rows = []
    rng = np.random.default_rng(20260905)
    for n in [2, 3, 5, 10]:
        theta = 2*np.pi*(np.arange(n) + rng.uniform(-0.12, 0.12, n))/n
        dif = (theta[:, None] - theta[None, :]) / 2
        mask = ~np.eye(n, dtype=bool)
        cot = np.zeros((n, n))
        cot[mask] = 1 / np.tan(dif[mask])
        v = cot.sum(axis=1)
        h = 1e-6 / (1 + np.max(np.abs(v)))
        numerical = (energy_and_generator(theta+h*v)[0] - energy_and_generator(theta-h*v)[0])/(2*h)
        analytic = energy_and_generator(theta)[1]
        relative = abs(numerical-analytic)/(1+abs(analytic))
        assert relative < 2e-7
        rows.append({"N": n, "finite_difference_L_D": numerical, "formula_L_D": analytic, "relative_error": relative})
    return rows


def main() -> dict:
    started = time.perf_counter()
    rows = [acue_expectations(n) for n in range(2, 11)]
    n2 = []
    for epsilon in [0.1, 0.03, 0.01, 0.003, 0.001]:
        e_d_cut = 2 - 2*(epsilon + np.sin(epsilon))/np.pi
        e_ld_cut = 8 - 16/np.pi/np.tan(epsilon/2) - 8*epsilon/np.pi
        n2.append({"cutoff_radians": epsilon, "E_D_with_cutoff": float(e_d_cut), "E_L_D_with_cutoff": float(e_ld_cut)})
    return {
        "description": "exhaustive subset traversal with floating-point weights; mathematical proofs are separate",
        "ACUE": rows,
        "directional_derivative": directional_derivative_checks(),
        "CUE_N2_truncated_integrals": n2,
        "elapsed_seconds": time.perf_counter()-started,
        "all_assertions_passed": True,
    }


if __name__ == "__main__":
    payload = json.dumps(main(), indent=2)
    (HERE/"force_energy.json").write_text(payload+"\n")
    print(payload)
