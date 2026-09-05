"""Independent endpoint, generator, and ODE checks; see adjacent review.

Residue Gram checks use integer arithmetic. Angle/ODE checks use float64.
This does not import the original generator audit or its computed answers.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp


HERE = Path(__file__).resolve().parent


def partitions(n: int, ceiling: int | None = None):
    if n == 0:
        yield ()
        return
    if ceiling is None:
        ceiling = n
    for first in range(min(n, ceiling), 0, -1):
        for tail in partitions(n-first, first):
            yield (first,) + tail


def exponents(partition: tuple[int, ...], n: int) -> list[int]:
    padded = partition + (0,) * (n-len(partition))
    return [a+n-i-1 for i, a in enumerate(padded)]


def residue_gram(alpha: tuple[int, ...], beta: tuple[int, ...], n: int) -> int:
    a = [x % (2*n) for x in exponents(alpha, n)]
    b = [x % (2*n) for x in exponents(beta, n)]
    if len(set(a)) < n or len(set(b)) < n or set(a) != set(b):
        return 0
    permutation = [b.index(x) for x in a]
    inversions = sum(permutation[i] > permutation[j]
                     for i in range(n) for j in range(i+1, n))
    return (-1)**inversions


def integer_endpoint_checks() -> list[dict]:
    rows = []
    for n in range(1, 11):
        ps = [p for m in range(n+1) for p in partitions(m)]
        for alpha in ps:
            assert min(exponents(alpha, n)) >= 0
            assert max(exponents(alpha, n)) < 2*n
            for beta in ps:
                assert residue_gram(alpha, beta, n) == int(alpha == beta)
        outside = (n+1,)
        outside_norm = residue_gram(outside, outside, n)
        assert outside_norm == (1 if n == 1 else 0)
        rows.append({
            "N": n, "partitions_of_all_weights_up_to_N": len(ps),
            "integer_Gram_entries_checked": len(ps)**2,
            "boundary_partition": [n],
            "boundary_exponents": exponents((n,), n),
            "first_outside_partition": list(outside),
            "first_outside_exponents": exponents(outside, n),
            "first_outside_ACUE_squared_norm": outside_norm,
            "first_outside_CUE_squared_norm": 1,
        })
    return rows


def velocity(theta: np.ndarray) -> np.ndarray:
    dif = (theta[:, None] - theta[None, :])/2
    mask = ~np.eye(len(theta), dtype=bool)
    c = np.zeros(dif.shape)
    c[mask] = 1/np.tan(dif[mask])
    return c.sum(axis=1)


def floating_generator_and_flow_checks() -> list[dict]:
    rng = np.random.default_rng(20260905)
    rows = []
    for n in [2, 3, 5, 8]:
        theta = 2*np.pi*(np.arange(n)+rng.uniform(-0.18, 0.18, n))/n
        z = np.exp(1j*theta)
        v = velocity(theta)
        max_generator_error = 0.0
        for m in range(1, n+3):
            direct = np.sum(1j*m*z**m*v)
            formula = -m*((n-m)*np.sum(z**m)
                          + sum(np.sum(z**a)*np.sum(z**(m-a))
                                for a in range(1, m)))
            max_generator_error = max(max_generator_error, abs(direct-formula))
        initial = np.poly(z)
        elementary_error = 0.0
        for k in range(1, n+1):
            # d e_k/d theta_i = i z_i e_{k-1}(z without i).
            direct = 0j
            for i in range(n):
                omitted = np.poly(np.delete(z, i))
                e_without_i = (-1)**(k-1)*omitted[k-1]
                direct += v[i]*1j*z[i]*e_without_i
            target = -k*(n-k)*((-1)**k)*initial[k]
            elementary_error = max(elementary_error, abs(direct-target))
        times = np.asarray([0.03, 0.1, 0.3])
        solution = solve_ivp(lambda _t, y: velocity(y), (0, times[-1]), theta,
                             method="DOP853", t_eval=times,
                             rtol=2e-12, atol=2e-13)
        assert solution.success
        k = np.arange(n+1)
        coefficient_error = 0.0
        for t, y in zip(solution.t, solution.y.T):
            evolved = np.poly(np.exp(1j*y))
            predicted = initial*np.exp(-k*(n-k)*t)
            coefficient_error = max(coefficient_error,
                                    float(np.max(np.abs(evolved-predicted))))
        assert max_generator_error < 2e-10
        assert elementary_error < 2e-10
        assert coefficient_error < 2e-9
        rows.append({"N": n, "max_L_p_m_error_m_through_N_plus_2": max_generator_error,
                     "max_L_e_k_error": elementary_error,
                     "max_integrated_coefficient_error": coefficient_error,
                     "physical_times": times.tolist(),
                     "arithmetic": "float64 numerical diagnostic, not proof"})
    return rows


if __name__ == "__main__":
    result = {
        "integer_endpoint_checks": integer_endpoint_checks(),
        "independent_floating_checks": floating_generator_and_flow_checks(),
        "all_assertions_passed": True,
    }
    payload = json.dumps(result, indent=2)
    (HERE/"dynamic_generator_independent_review.json").write_text(payload+"\n")
    print(payload)
