"""Exact finite checks of shared atom weights and periodic prime-pair densities."""

import json
from fractions import Fraction
from math import gcd, isqrt, prod


def primes_through(limit: int) -> list[int]:
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit - p*p) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def is_prime(k: int) -> bool:
    return k >= 2 and all(k % d for d in range(2, isqrt(k) + 1))


def twin_interval(limit: int = 1_000_000, places: int = 30) -> tuple[Fraction, Fraction]:
    scale = 10**places
    lower = upper = scale
    for p in primes_through(limit)[1:]:
        denominator = (p - 1)**2
        lower = lower * (denominator - 1) // denominator
        upper = (upper * (denominator - 1) + denominator - 1) // denominator
    # Taking every integer beyond the cutoff gives a telescoping lower tail.
    return Fraction(lower * (limit - 1), scale * limit), Fraction(upper, scale)


def admissible_count(endpoint: int, n: int, h: int, modulus: int = 210) -> tuple[int, Fraction]:
    allowed = [gcd(m * (n*m + h), modulus) == 1 for m in range(1, modulus + 1)]
    blocks, tail = divmod(endpoint, modulus)
    return blocks * sum(allowed) + sum(allowed[:tail]), Fraction(sum(allowed), modulus)


def row_factor(n: int, h: int) -> Fraction:
    """Singular series divided by the allowed density and by the common C2."""
    factor = Fraction(2)
    for p in primes_through(abs(n*h)):
        if p > 2 and (n*h) % p == 0:
            factor *= Fraction(p - 1, p - 2)
    _, density = admissible_count(0, n, h)
    return factor / density


def rectangle(n: int, left: list[int], right: list[int], interval: tuple[Fraction, Fraction]) -> dict:
    assert all(is_prime(k) for k in [n, *left, *right])
    cells = []
    for m in left:
        row = []
        for r in right:
            h = r - n*m
            assert h and gcd(n, h) == 1 and gcd(m*r, 210) == 1
            assert abs(h) < Fraction(n*m, n**5)
            count, _ = admissible_count(m, n, h)
            excluded, _ = admissible_count(max(0, (-h) // n), n, h)
            count -= excluded
            factor = row_factor(n, h)
            floors = [[int(k * factor * b) for b in interval] for k in (count - 1, count)]
            certified = all(lo == hi for lo, hi in floors)
            atom = floors[1][0] - floors[0][0] if certified else None
            row.append(dict(h=h, primitive_multiplier=str(factor), count=count,
                            floor_ranges=floors, certified_atom=atom))
        cells.append(row)
    entries = [cell for row in cells for cell in row]
    a, b, c, d = [Fraction(cell['primitive_multiplier']) for cell in entries]
    i, j, k, l = [cell['certified_atom'] for cell in entries]
    determinant = None if None in (i, j, k, l) else i*l - j*k
    return dict(twist=n, height=n**5, left=left, right=right, cells=cells,
                pre_floor_cross_ratio=str(a*d / (b*c)), floor_determinant=determinant)


def check_period_averages() -> int:
    checked = 0
    for z, modulus in [(2, 2), (3, 6), (5, 30), (7, 210)]:
        primes = primes_through(z)
        weight = Fraction(modulus, sum(gcd(k, modulus) == 1 for k in range(1, modulus + 1)))
        for n in (11, 13, 17):
            for h in (-10, -8, -6, -4, -2, 2, 4, 6, 8, 10):
                count, _ = admissible_count(modulus, n, h, modulus)
                observed = weight**2 * count / modulus
                expected = prod((1 - Fraction(1 if h % p == 0 else 2, p)) /
                                (1 - Fraction(1, p))**2 for p in primes)
                assert observed == expected
                if abs(h) == 2:
                    assert observed == 2 * prod(1 - Fraction(1, (p - 1)**2) for p in primes if p > 2)
                checked += 1
    return checked


def main() -> None:
    interval = twin_interval()
    before = rectangle(11, [1771387, 1771397], [19485283, 19485341], interval)
    after = rectangle(5, [15329, 15331], [76631, 76649], interval)
    assert before['pre_floor_cross_ratio'] == '144/121'
    assert after['pre_floor_cross_ratio'] == '1' and after['floor_determinant'] == -18
    print(json.dumps(dict(
        c2_enclosure=[str(x) for x in interval],
        scope='Atomic rank-one witnesses and finite exact wheel-density checks. The packet limit uses the analytic argument.',
        pre_floor_example=before, floor_example=after, local_product_checks=check_period_averages(),
    ), indent=2))


if __name__ == '__main__':
    main()
