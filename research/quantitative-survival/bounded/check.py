"""Deterministic supplementary checks for REPORT.md; standard library only."""
from itertools import permutations
from math import cos, factorial, pi, prod
from random import Random
import json


HIGH = (6 / 5, 1 / 5, -7 / 5)
LOW = (-4 / 5, 1 / 5, 3 / 5)


def falling(n, r):
    return prod(n - j for j in range(r)) if n >= r else 0


def kernel(x):
    return cos(2 * pi * sum(a * b for a, b in zip(HIGH, x))) - cos(
        2 * pi * sum(a * b for a, b in zip(LOW, x))
    )


def score(x):
    if len(x) < 3:
        return 0.0
    return sum(kernel(t) for t in permutations(x, 3)) / falling(len(x), 3)


def main():
    rng = Random(46198662)
    checks = 0
    for n in range(3, 31):
        assert falling(n, 3) ** 2 == (
            falling(n, 6) + 9 * falling(n, 5)
            + 18 * falling(n, 4) + 6 * falling(n, 3)
        )
        assert n * falling(n, 3) == falling(n, 4) + 3 * falling(n, 3)
        checks += 2
    for _ in range(1000):
        x = tuple(rng.uniform(-0.125, 0.125) for _ in range(3))
        average = sum(kernel(t) for t in permutations(x)) / 6
        mean = sum(x) / 3
        variance = sum((v - mean) ** 2 for v in x)
        assert average <= -pi**2 / 2 * variance + 1e-13
        checks += 1
    for _ in range(100):
        k = rng.randint(3, 10)
        translation = rng.uniform(-1, 1)
        grid = [translation + v / 2 for v in rng.sample(range(-20, 21), k)]
        assert abs(score(grid)) < 1e-12
        eta = 10 ** rng.uniform(-7, -2)
        bad = rng.randint(0, k)
        x = [v + rng.uniform(-eta, eta) for v in grid]
        for j in range(bad):
            x[j] += rng.uniform(-1, 1)
        assert abs(score(x)) <= 8 * pi * eta + 6 * bad / k + 1e-12
        retained = x[bad:]
        assert abs(score(x) - score(retained)) <= min(4, 12 * bad / k) + 1e-12
        checks += 3
    l, m, r = 40, 100, 40
    numerator = 2 * l ** (3 + r)
    denominator = falling(m - 2, r)
    receipt = {
        "checks": checks,
        "seed": 46198662,
        "short_window_length": 0.25,
        "short_window_quadratic_coefficient": 12*pi*pi/5 - 926*pi**4/375/16,
        "claimed_weaker_coefficient": pi*pi/2,
        "cutoff_tail_example": {
            "L": l, "M": m, "r": r,
            "exact_numerator": numerator,
            "exact_denominator": denominator,
            "bound": numerator / denominator,
        },
        "status": "supplementary checks passed; proofs in REPORT.md",
    }
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
