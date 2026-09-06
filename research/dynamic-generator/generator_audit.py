#!/usr/bin/env python3
"""Exact circular-Coulomb generator and protected ACUE/Haar moment audit.

No Monte Carlo is used. Three independent checks are retained:
1. exact character/residue Gram formulas, N=2,...,10;
2. direct enumeration in Z[z]/Phi_(2N)(z), N=2,...,5;
3. floating direct subset enumeration, N=2,...,10 (explicitly non-exact).
"""
from __future__ import annotations

import itertools
import json
import math
import platform
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import sympy as sp

N_SYMBOL = sp.Symbol("N", integer=True, positive=True)
PARTITIONS = {1: [(1,)], 2: [(2,), (1, 1)], 3: [(3,), (2, 1), (1, 1, 1)]}
CHARACTERS = {
    1: sp.Matrix([[1]]),
    2: sp.Matrix([[1, 1], [-1, 1]]),
    3: sp.Matrix([[1, 1, 1], [-1, 0, 2], [1, -1, 1]]),
}


def canonical(parts: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    return tuple(sorted(parts, reverse=True))


def generator(coefficients: dict, n: sp.Expr = N_SYMBOL) -> dict:
    """Derivation on balanced products p_lambda * conjugate(p_mu)."""
    result = defaultdict(lambda: sp.Integer(0))
    for (positive, negative), coefficient in coefficients.items():
        for side, parts in enumerate((positive, negative)):
            for i, k in enumerate(parts):
                result[(positive, negative)] += -k * (n - k) * coefficient
                other = parts[:i] + parts[i + 1 :]
                for a in range(1, k):
                    split = canonical(other + (a, k - a))
                    key = (split, negative) if side == 0 else (positive, split)
                    result[key] += -k * coefficient
    return {key: sp.expand(value) for key, value in result.items() if value != 0}


def schur_gram(n: int, m: int, discrete: bool) -> sp.Matrix:
    parts = PARTITIONS[m]
    result = sp.zeros(len(parts))
    for i, alpha in enumerate(parts):
        for j, beta in enumerate(parts):
            if len(alpha) > n or len(beta) > n:
                continue
            if not discrete:
                result[i, j] = int(i == j)
                continue
            a = alpha + (0,) * (n - len(alpha))
            b = beta + (0,) * (n - len(beta))
            exponents_a = [a[k] + n - k - 1 for k in range(n)]
            exponents_b = [b[k] + n - k - 1 for k in range(n)]
            residue_matrix = sp.Matrix(
                n, n,
                lambda k, ell: int((exponents_a[k] - exponents_b[ell]) % (2 * n) == 0),
            )
            result[i, j] = residue_matrix.det()
    return result


def power_gram(n: int, m: int, discrete: bool) -> sp.Matrix:
    chars = CHARACTERS[m]
    return chars.T * schur_gram(n, m, discrete) * chars


def integer_matrix(matrix: sp.Matrix) -> list[list[int]]:
    return [[int(x) for x in row] for row in matrix.tolist()]


def expectation(coefficients: dict, gram: sp.Matrix, m: int, n: int) -> int:
    indices = {parts: i for i, parts in enumerate(PARTITIONS[m])}
    return int(sum(
        coefficient.subs(N_SYMBOL, n) * gram[indices[pos], indices[neg]]
        for (pos, neg), coefficient in coefficients.items()
    ))


class CyclotomicRing:
    """Small exact integer quotient ring, independent of Schur moments."""

    def __init__(self, order: int):
        self.order = order
        z = sp.Symbol("z")
        polynomial = sp.Poly(sp.cyclotomic_poly(order, z), z)
        self.degree = polynomial.degree()
        self.modulus = [int(polynomial.nth(k)) for k in range(self.degree + 1)]
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)
        self.powers = [self.reduce([0] * k + [1]) for k in range(order)]

    def reduce(self, values: list[int]) -> tuple[int, ...]:
        values = values[:] + [0] * max(0, self.degree - len(values))
        for k in range(len(values) - 1, self.degree - 1, -1):
            coefficient = values[k]
            if coefficient:
                for j in range(self.degree):
                    values[k - self.degree + j] -= coefficient * self.modulus[j]
        return tuple(values[: self.degree])

    def add(self, a: tuple, b: tuple) -> tuple:
        return tuple(x + y for x, y in zip(a, b))

    def multiply(self, a: tuple, b: tuple) -> tuple:
        values = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                values[i + j] += x * y
        return self.reduce(values)

    def power(self, exponent: int) -> tuple:
        return self.powers[exponent % self.order]


def exact_subset_enumeration(n: int) -> dict:
    ring = CyclotomicRing(2 * n)
    total = ring.zero
    grams = {
        m: [[ring.zero for _ in PARTITIONS[m]] for _ in PARTITIONS[m]]
        for m in PARTITIONS
    }
    count = 0
    for subset in itertools.combinations(range(2 * n), n):
        count += 1
        weight = ring.one
        for a, b in itertools.combinations(subset, 2):
            factor = tuple(
                2 * x - y - z
                for x, y, z in zip(ring.one, ring.power(a - b), ring.power(b - a))
            )
            weight = ring.multiply(weight, factor)
        total = ring.add(total, weight)
        traces = {}
        for k in range(-3, 4):
            if k == 0:
                continue
            value = ring.zero
            for site in subset:
                value = ring.add(value, ring.power(k * site))
            traces[k] = value
        for m, partitions in PARTITIONS.items():
            positive, negative = [], []
            for partition in partitions:
                vpos, vneg = ring.one, ring.one
                for k in partition:
                    vpos = ring.multiply(vpos, traces[k])
                    vneg = ring.multiply(vneg, traces[-k])
                positive.append(vpos)
                negative.append(vneg)
            for i, vpos in enumerate(positive):
                for j, vneg in enumerate(negative):
                    integrand = ring.multiply(weight, ring.multiply(vpos, vneg))
                    grams[m][i][j] = ring.add(grams[m][i][j], integrand)
    denominator = (2 * n) ** n
    assert total == (denominator,) + (0,) * (ring.degree - 1)
    output = {}
    for m, gram in grams.items():
        expected = power_gram(n, m, True)
        for i, row in enumerate(gram):
            for j, value in enumerate(row):
                assert value == (denominator * int(expected[i, j]),) + (0,) * (ring.degree - 1)
        output[str(m)] = integer_matrix(expected)
    return {"N": n, "subset_count": count, "cyclotomic_degree": ring.degree,
            "normalization_exact": True, "all_gram_entries_exactly_equal": True,
            "power_grams": output}


def floating_subset_enumeration(n: int, coefficients_by_m: dict) -> dict:
    roots = np.exp(1j * np.pi * np.arange(2 * n) / n)
    iterator = iter(itertools.combinations(range(2 * n), n))
    total = 0.0
    grams = {m: np.zeros((len(parts), len(parts)), complex) for m, parts in PARTITIONS.items()}
    count = 0
    while batch := list(itertools.islice(iterator, 8192)):
        sites = np.asarray(batch, dtype=np.int64)
        z = roots[sites]
        weight = np.full(len(batch), 1.0 / (2 * n) ** n)
        for i in range(n):
            for j in range(i):
                weight *= abs(z[:, i] - z[:, j]) ** 2
        traces = {k: (z ** k).sum(axis=1) for k in range(1, 4)}
        total += float(weight.sum())
        count += len(batch)
        for m, partitions in PARTITIONS.items():
            basis = np.column_stack([
                np.prod(np.column_stack([traces[k] for k in part]), axis=1)
                for part in partitions
            ])
            grams[m] += basis.T @ (weight[:, None] * basis.conj())
    max_gram_error = 0.0
    max_scaled_derivative_error = 0.0
    for m, gram in grams.items():
        target = np.asarray(power_gram(n, m, True)).astype(float)
        max_gram_error = max(max_gram_error, float(np.max(abs(gram - target))))
        indices = {parts: i for i, parts in enumerate(PARTITIONS[m])}
        for coefficients in coefficients_by_m[m]:
            actual = 0j
            exact = 0.0
            scale = 1.0
            for (pos, neg), coefficient in coefficients.items():
                c = int(coefficient.subs(N_SYMBOL, n))
                i, j = indices[pos], indices[neg]
                actual += c * gram[i, j]
                exact += c * target[i, j]
                scale += abs(c) * max(1.0, abs(target[i, j]))
            max_scaled_derivative_error = max(max_scaled_derivative_error, abs(actual - exact) / scale)
    assert abs(total - 1) < 1e-11
    assert max_gram_error < 1e-10
    assert max_scaled_derivative_error < 1e-11
    return {"N": n, "subset_count": count, "normalization": total,
            "max_gram_absolute_error": max_gram_error,
            "max_derivative_scaled_absolute_error": float(max_scaled_derivative_error),
            "evidence_level": "floating independent check, not exact"}


def direct_generator_checks() -> list[dict]:
    output = []
    for n in range(2, 5):
        z = sp.symbols(f"z0:{n}")
        for m in range(1, 4):
            actual = sum(
                -m * (z[k] ** m - z[j] ** m) * (z[k] + z[j]) / (z[k] - z[j])
                for k in range(n) for j in range(k)
            )
            p = lambda k: sum(x ** k for x in z)
            target = -m * ((n - m) * p(m) + sum(p(a) * p(m - a) for a in range(1, m)))
            assert sp.cancel(actual - target) == 0
            output.append({"N": n, "m": m, "rational_identity_exact": True})
    return output


def elementary_symmetric_checks() -> list[dict]:
    output = []
    for n in range(2, 5):
        z = sp.symbols(f"z0:{n}")
        for degree in range(1, n + 1):
            elementary = sum(math.prod(subset) for subset in itertools.combinations(z, degree))
            actual = sum(
                -(z[k] + z[j]) / (z[k] - z[j])
                * (z[k] * sp.diff(elementary, z[k]) - z[j] * sp.diff(elementary, z[j]))
                for k in range(n) for j in range(k)
            )
            assert sp.cancel(actual + degree * (n - degree) * elementary) == 0
            output.append({"N": n, "degree": degree,
                           "eigenvalue": -degree * (n - degree), "identity_exact": True})
    return output


def main() -> None:
    start = time.monotonic()
    coefficients_by_m = {}
    coefficient_output = {}
    for m in PARTITIONS:
        coefficients = {((m,), (m,)): sp.Integer(1)}
        coefficients_by_m[m] = []
        coefficient_output[str(m)] = []
        for r in range(9):
            assert all(sum(pos) == m and sum(neg) == m for pos, neg in coefficients)
            coefficients_by_m[m].append(coefficients)
            coefficient_output[str(m)].append({
                "r": r, "terms": [
                    {"positive_partition": list(pos), "negative_partition": list(neg),
                     "coefficient_polynomial_in_N": str(coefficient)}
                    for (pos, neg), coefficient in sorted(coefficients.items())
                ],
            })
            coefficients = generator(coefficients)
    rows = []
    gram_output = []
    protected_count = 0
    for n in range(2, 11):
        for m in PARTITIONS:
            haar = power_gram(n, m, False)
            acue = power_gram(n, m, True)
            if m <= n:
                assert haar == acue
            gram_output.append({"N": n, "m": m,
                                "haar": integer_matrix(haar), "acue": integer_matrix(acue)})
            for r, coefficients in enumerate(coefficients_by_m[m]):
                ehaar = expectation(coefficients, haar, m, n)
                eacue = expectation(coefficients, acue, m, n)
                if m <= n:
                    assert ehaar == eacue
                    protected_count += 1
                rows.append({"N": n, "m": m, "r": r, "protected": m <= n,
                             "haar_expectation": ehaar, "acue_expectation": eacue,
                             "acue_minus_haar": eacue - ehaar})
    output = {
        "status": "exact finite audit and self-contained algebraic no-leakage proof; no zeta theorem",
        "convention": "radians; V_k=sum_{j!=k}cot((theta_k-theta_j)/2); L=sum V_k partial_theta_k",
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "sympy": sp.__version__},
        "symbolic_coefficients": coefficient_output,
        "direct_generator_identity_checks": direct_generator_checks(),
        "elementary_symmetric_eigenvalue_checks": elementary_symmetric_checks(),
        "character_residue_grams": gram_output,
        "exact_moment_results": rows,
        "exact_protected_equalities_count": protected_count,
        "total_exact_moment_results": len(rows),
        "direct_exact_cyclotomic_enumeration": [exact_subset_enumeration(n) for n in range(2, 6)],
        "direct_floating_enumeration": [floating_subset_enumeration(n, coefficients_by_m) for n in range(2, 11)],
    }
    output["elapsed_seconds"] = time.monotonic() - start
    path = Path(__file__).with_name("generator_audit_results.json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"output": str(path), "protected_equalities": protected_count,
                      "total_exact_results": len(rows),
                      "unprotected_results": [row for row in rows if not row["protected"]],
                      "floating_checks": output["direct_floating_enumeration"],
                      "elapsed_seconds": output["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
