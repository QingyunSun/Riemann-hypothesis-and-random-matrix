"""Numerical diagnostics for the initial-data circular heat lemma.

These are targeted checks, not machine proofs.  All angles use circumference
2*pi, and time is the coefficient-flow time exp(s*j*(N-j)).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import brentq, root


HERE = Path(__file__).resolve().parent
NODES, WEIGHTS = hermgauss(100)
WEIGHTS = WEIGHTS / np.sqrt(np.pi)


def background_ratio(y: np.ndarray, others: np.ndarray) -> np.ndarray:
    if not len(others):
        return np.ones_like(y)
    ratios = np.sin((y[:, None] - others[None, :]) / 2)
    ratios /= np.sin(-others[None, :] / 2)
    return np.prod(ratios, axis=1)


def normal_form(x: float, tau: float, delta: float, others: np.ndarray) -> float:
    # hermgauss integrates against exp(-z*z); sqrt(4*tau)*z is N(0,2*tau).
    y = delta * (x + np.sqrt(4 * tau) * NODES)
    pair = 4 / delta**2 * np.sin((y - delta / 2) / 2) * np.sin(
        (y + delta / 2) / 2
    )
    return float(WEIGHTS @ (pair * background_ratio(y, others)))


def reciprocal_sum(others: np.ndarray) -> float:
    return float(np.sum(1 / (2 * np.abs(np.sin(others / 2)))))


def tilted_normal_form(x: float, tau: float, delta: float, others: np.ndarray) -> float:
    y = delta * (x + np.sqrt(4 * tau) * NODES)
    ratios = np.sin((y[:, None] - others[None, :]) / 2)
    ratios /= np.sin(-others[None, :] / 2)
    linear_drift = -0.5 * np.sum(1 / np.tan(others / 2))
    log_abs_r = np.sum(np.log(np.abs(ratios)), axis=1) - linear_drift * y
    r = np.prod(np.sign(ratios), axis=1) * np.exp(log_abs_r)
    pair = 4 / delta**2 * np.sin((y - delta / 2) / 2) * np.sin(
        (y + delta / 2) / 2
    )
    return float(WEIGHTS @ (pair * r))


def planted_background(n: int) -> np.ndarray:
    positive = np.arange(1, n // 2) * 2 * np.pi / n
    return np.r_[-positive[::-1], positive]


def diagnostics() -> dict:
    output: dict = {"status": "numerical diagnostics, not formal verification"}
    exact_cases = []
    for delta in [0.01, 0.1, 0.5, 1.0]:
        tau = brentq(lambda t: normal_form(0, t, delta, np.array([])), 0, 0.3)
        exact = -np.log(np.cos(delta / 2)) / delta**2
        assert abs(tau - exact) < 2e-11
        exact_cases.append({"delta": delta, "tau": tau, "exact_tau": exact})
    output["exact_two_root_time"] = exact_cases

    planted = []
    for n in [16, 32, 64, 128, 256]:
        delta = 0.2 * n ** (-4 / 3)
        others = planted_background(n)
        a = reciprocal_sum(others)
        tau = brentq(lambda t: normal_form(0, t, delta, others), 0.1, 0.3)
        error = max(
            abs(normal_form(x, t, delta, others) - (x * x - 0.25 + 2 * t))
            for x in [-2, -1, 0, 1, 2]
            for t in [0.0, 0.08, 0.125, 0.2]
        )
        assert tau >= 0.125 - 1e-10
        assert tau < 0.126
        planted.append(
            {
                "N": n,
                "delta": delta,
                "delta_A": delta * a,
                "collision_tau": tau,
                "eight_tau": 8 * tau,
                "grid_normal_form_error": error,
            }
        )
    assert planted[-1]["eight_tau"] < planted[0]["eight_tau"]
    output["symmetric_planted_pair"] = planted

    # Direct numerical check of the GLOBAL product bound, including y far
    # outside the isolated pair neighborhood and across the periodic cut.
    rng = np.random.default_rng(20260905)
    bound_cases = []
    for n in [8, 24, 64]:
        others = planted_background(n)
        a = reciprocal_sum(others)
        y = rng.uniform(-8, 8, 1000)
        actual = np.abs(background_ratio(y, others) - 1)
        exponent = a * np.abs(y)
        # Only evaluate exp below overflow; above that the finite product is
        # already far below the bound in log scale.
        safe = exponent < 600
        bound = np.expm1(exponent[safe])
        assert np.all(actual[safe] <= bound + 1e-10)
        bound_cases.append({"N": n, "tested_points": int(np.sum(safe))})
    output["global_product_bound_samples"] = bound_cases

    # The candidate three-point determinant inequality, tested at distinct
    # nonconfluent points so determinant cancellation is not misreported.
    ratios = []
    for n in [4, 8, 16]:
        for scale in [0.03, 0.1, 0.3]:
            x = scale * np.array([0.0, 0.4, 1.0]) / n
            frequencies = np.arange(n)
            v = np.exp(1j * x[:, None] * frequencies[None, :]) / np.sqrt(2 * np.pi)
            gram = v @ v.conj().T
            rho = float(np.linalg.det(gram).real)
            vandermonde_sq = float(np.prod([abs(x[j] - x[i]) ** 2 for i in range(3) for j in range(i + 1, 3)]))
            ratio = rho / (n**9 * vandermonde_sq)
            theoretical_bound = (9 / 8) / (2 * np.pi) ** 3
            assert rho > 0
            assert ratio < theoretical_bound
            ratios.append({"N": n, "scaled_span": scale, "normalized_rho3": ratio})
    output["three_point_bound_samples"] = ratios

    # Check the Galilean refinement where delta*A is LARGE, but delta^2*B
    # remains small.  These configurations have many other minimum-size
    # gaps, so the computed selected-pair double-root time is not claimed
    # to be the first global collision.
    tilted = []
    for n in [100, 1000, 10000]:
        delta = n ** -2
        m = 50
        others = (m + np.arange(n - 2)) * delta
        b = float(0.25 * np.sum(1 / np.sin(others / 2) ** 2))

        def system(v: np.ndarray) -> list[float]:
            x, tau = v
            dx = 1e-4
            return [
                tilted_normal_form(x, tau, delta, others),
                (tilted_normal_form(x + dx, tau, delta, others)
                 - tilted_normal_form(x - dx, tau, delta, others)) / (2 * dx),
            ]

        solved = root(system, np.array([0.0, 0.125]))
        assert solved.success
        assert np.linalg.norm(system(solved.x)) < 1e-7
        assert solved.x[1] >= 0.125 - 1e-8
        assert solved.x[1] < 0.13
        tilted.append({
            "N": n,
            "delta_A": delta * reciprocal_sum(others),
            "delta_squared_B": delta * delta * b,
            "moving_frame_double_root_x": float(solved.x[0]),
            "selected_pair_double_root_tau": float(solved.x[1]),
            "scope": "local double root, not certified first global collision",
        })
    output["galilean_large_drift_samples"] = tilted

    max_tilted_factor_excess = -np.inf
    for c in np.r_[-np.logspace(-3, 6, 60), np.logspace(-3, 6, 60)]:
        for w in np.r_[np.linspace(-5, -0.001, 60), np.linspace(0.001, 5, 60)]:
            v = w / np.sqrt(1 + c*c)
            log_left = np.log(abs(np.cos(v) - c*np.sin(v))) + c*v
            excess = log_left - 4*(1+c*c)*v*v
            max_tilted_factor_excess = max(max_tilted_factor_excess, excess)
    assert max_tilted_factor_excess <= 1e-12
    output["centered_sine_factor_max_log_excess"] = float(max_tilted_factor_excess)
    return output


if __name__ == "__main__":
    results = diagnostics()
    rendered = json.dumps(results, indent=2)
    (HERE / "yau_flow_checks.json").write_text(rendered + "\n")
    print(rendered)
