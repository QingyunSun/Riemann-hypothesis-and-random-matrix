"""Exact obstruction certificates for three short admissible-tuple targets.

Run with Python 3.11+, with assertions enabled. Output includes witnesses for
necessity of each prime. No solver or third-party package is required.
"""

from __future__ import annotations

import json
from itertools import combinations
from math import isqrt
from typing import Sequence


def primes_through(n: int) -> list[int]:
    return [p for p in range(2, n + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def find(k: int, diameter: int, primes: Sequence[int]) -> tuple[list[int] | None, int]:
    """A normalized witness, or exhaustive failure. Every candidate includes 0."""
    step = 2 if 2 in primes else 1
    grid = range(0, diameter + 1, step)
    masks = [[sum(1 << i for i, x in enumerate(grid) if x % p == a)
              for a in range(1, p)] for p in primes if p != 2]
    nodes = 0

    def visit(level: int, remaining: int) -> list[int] | None:
        nonlocal nodes
        nodes += 1
        if remaining.bit_count() < k:
            return None
        if level == len(masks):
            return [x for i, x in enumerate(grid) if remaining >> i & 1][:k]
        children = [remaining & ~mask for mask in masks[level]]
        if remaining in children:
            # A class is already absent; this child contains every other child.
            return visit(level + 1, remaining)
        for child in children:
            result = visit(level + 1, child)
            if result is not None:
                return result
        return None

    return visit(0, (1 << len(grid)) - 1), nodes


def check_witness(w: list[int], k: int, diameter: int, primes: Sequence[int]) -> None:
    assert len(set(w)) == len(w) == k
    assert w[0] == 0 and sorted(w) == w and w[-1] <= diameter
    assert all(len({v % p for v in w}) < p for p in primes)


def exact_case(k: int, diameter: int, last_core_prime: int) -> dict:
    all_primes = primes_through(k)
    core = primes_through(last_core_prime)
    impossible, nodes = find(k, diameter, core)
    assert impossible is None
    lower, _ = find(k - 1, diameter, core)
    assert lower is not None
    check_witness(lower, k - 1, diameter, core)
    upper, _ = find(k, diameter + 2, all_primes)
    assert upper is not None
    check_witness(upper, k, diameter + 2, all_primes)
    essential = {}
    for omitted in core:
        tested = [q for q in all_primes if q != omitted]
        w, _ = find(k, diameter, tested)
        assert w is not None
        check_witness(w, k, diameter, tested)
        assert len({a % omitted for a in w}) == omitted
        essential[omitted] = w
    return dict(k=k, diameter=diameter, minimal_core=core, refutation_nodes=nodes,
                max_core_survivors=k - 1, core_maximizer=lower,
                optimal_diameter=upper[-1], optimal_witness=upper,
                deletion_witnesses=essential)


def test_small_inputs() -> None:
    # Independent brute-force backend checks both parity conventions and partial primes.
    for k in (2, 3, 4, 5):
        pool = primes_through(k)
        for size in range(len(pool) + 1):
            for tested in combinations(pool, size):
                for d in range(12):
                    expected = any(all(len({x % p for x in w}) < p for p in tested)
                                   for w in combinations(range(d + 1), k) if w[0] == 0)
                    result, _ = find(k, d, tested)
                    assert (result is not None) == expected


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError("Run with assertions enabled.")
    test_small_inputs()
    print(json.dumps([exact_case(38, 174, 17), exact_case(39, 180, 19),
                      exact_case(40, 184, 19)], indent=2))
