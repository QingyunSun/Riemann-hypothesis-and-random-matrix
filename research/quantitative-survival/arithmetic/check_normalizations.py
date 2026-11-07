#!/usr/bin/env python3
"""Independent numerical diagnostics; not proofs of prime-pair assumptions.

Requires Python 3, NumPy, SciPy. Uses exact positive-prime singular-series
factors with a truncated Euler product for the twin-prime constant.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre


def primes_through(n: int) -> np.ndarray:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p::p] = False
    return np.flatnonzero(sieve)


def height_quadrature(order: int) -> tuple[np.ndarray, np.ndarray]:
    z, w = roots_legendre(order)
    t = 1.5 + z / 2
    mass = w / 2 * np.exp(-1 / ((t - 1) * (2 - t)))
    return t, mass / mass.sum()


def kernel_values(u: np.ndarray, order: int) -> np.ndarray:
    t, mass = height_quadrature(order)
    out = np.empty_like(u)
    for i in range(0, len(u), 4096):
        out[i:i+4096] = np.cos(u[i:i+4096, None] * t) @ mass
    return out


def singular_series(max_h: int, euler_limit: int) -> tuple[np.ndarray, float]:
    primes = primes_through(max(max_h, euler_limit))
    ep = primes[(primes > 2) & (primes <= euler_limit)].astype(float)
    twin_product = float(np.prod(1 - 1 / (ep - 1)**2))
    series = np.zeros(max_h + 1)
    series[2::2] = 2 * twin_product
    for p in primes[(primes > 2) & (primes <= max_h)]:
        series[2*p::2*p] *= (p - 1) / (p - 2)
    return series, twin_product


def packet_identity(beta: float, eta: float, order: int) -> dict[str, float]:
    z, w = roots_legendre(order)
    a = eta * z
    weights = eta * w
    def q(x: np.ndarray) -> np.ndarray:
        v = 1 - (x / eta)**2
        out = np.zeros_like(v)
        valid = v > 0
        out[valid] = np.exp(-1 / v[valid])
        return out
    prod = q(a)[:, None] * q(a)[None, :] * q(a[:, None] + a[None, :])
    measure = weights[:, None] * weights[None, :]
    c = float(np.sum(prod * measure))
    odd = float(np.sum(a[None, :] * prod * measure))
    raw_main = -float(np.sum((beta + a[None, :]) * prod * measure))
    return {"order": order, "c_psi": c, "odd_integral": odd,
            "negative_prime_main_over_c": raw_main / c,
            "positive_zero_mean": -raw_main / c}


def main() -> None:
    configurations = [(11, 110), (11, 1100), (101, 1010), (101, 10100)]
    max_h = max(h for _, h in configurations) * 80
    series, twin = singular_series(max_h, 2_000_000)
    records = []
    for p, hscale in configurations:
        h = np.arange(1, hscale * 80 + 1)
        modified = series[h] * ((p - 1) / (p - 2))
        modified[h % p == 0] = 0
        row = {"p": p, "H": hscale, "predicted": -float(np.log(p))}
        for order in (128, 256):
            values = kernel_values(h / hscale, order)
            for cutoff in (40, 80):
                row[f"sum_q{order}_cut{cutoff}"] = 2 * float(
                    np.dot(modified[:hscale*cutoff] - 1, values[:hscale*cutoff])) - 1
        records.append(row)
    result = {"status": "numerical diagnostics, not interval-certified",
              "euler_product_limit": 2_000_000,
              "twin_prime_product": twin,
              "height_weight": "normalized exp(-1/((t-1)*(2-t))) on (1,2)",
              "kernel": "K(u)=integral Phi(t)*cos(t*u) dt",
              "tail_stabilization": "sum over nonzero h of K(h/H) is exactly -1 by Poisson; compute -1+2*sum(S_p(h)-1)*K(h/H)",
              "singular_series_checks": records,
              "packet_identity": [packet_identity(.2, .04, n) for n in (128, 256)]}
    path = Path(__file__).with_name("normalizations.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
