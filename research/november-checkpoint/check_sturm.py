"""Check the eleven-root survival vector independently with Cayley and Sturm.

Requires Python 3.10+ and python-flint. Run: python check_sturm.py
The SHA-256 input is described in classification_digest() and the emitted JSON.
"""

import argparse
import hashlib
import json
from collections import Counter
from itertools import accumulate, combinations

import flint
from flint import acb, acb_poly, arb, ctx


N = 11
PERIOD = 2 * N
PRECISION = 256


def gaps(sites, period):
    """Cyclic gaps for a sorted set of sites, beginning at its first site."""
    return tuple(v - u for u, v in zip(sites, sites[1:])) + (
        sites[0] + period - sites[-1],
    )


def canonical_gaps(g):
    """Lexicographically first rooted orientation of the gap necklace."""
    return min(v[k:] + v[:k] for v in (g, g[::-1]) for k in range(len(v)))


def complementary_pairs(n=N, same_gaps=True):
    """Enumerate necklaces from anchored sets; half filling ensures equal pair data."""
    period = 2*n
    all_sites = set(range(period))
    for others in combinations(range(1, period), n - 1):
        a = (0,) + others
        g = gaps(a, period)
        if g != canonical_gaps(g):
            continue
        b_gaps = canonical_gaps(gaps(tuple(sorted(all_sites.difference(a))), period))
        # A sorted rooted set is recovered from its first N-1 gaps.
        b = (0,) + tuple(accumulate(b_gaps[:-1]))
        if a < b and (not same_gaps or sorted(g) == sorted(b_gaps)):
            # Check the complete ordered pair displacements independently.
            assert Counter((x-y) % period for x in a for y in a) == Counter(
                (x-y) % period for x in b for y in b
            )
            yield a, b


def cayley_basis(n=N, numerator=85, denominator=84):
    root = acb(arb(1) / n).exp_pi_i()
    sites = [root**j for j in range(2*n)]
    z0 = acb(7, 24) / 25
    plus = acb_poly([acb(0, 1), 1])
    minus = acb_poly([acb(0, -1), 1])
    w = arb(numerator) / denominator
    columns = [
        plus**j * minus**(n-j) * (z0**j * w**(j*(n-j)))
        for j in range(n+1)
    ]
    return sites, columns


def survives(configuration, sites, columns):
    """Certify simple roots on the unit circle, or certify failure at this time."""
    n = len(configuration)
    initial = acb_poly.from_roots([sites[k] for k in configuration])
    transformed = sum((columns[j] * initial[j] for j in range(n+1)), acb_poly())
    leading = transformed[n]
    if leading.contains(0):
        raise ArithmeticError('Cayley normalization contains zero')
    coefficients = [transformed[j] / leading for j in range(n)]
    if any(not z.imag.contains(0) for z in coefficients):
        raise ArithmeticError('A normalized coefficient fails reality')
    dividend = [z.real for z in coefficients] + [arb(1)]
    divisor = [j*dividend[j] / n for j in range(1, n+1)]
    while len(divisor) > 1:
        # Both are monic; their degrees differ by one. The first quotient
        # coefficient is 1 and its constant term is q. Cancel out the two
        # top coefficients symbolically before testing the negative remainder.
        q = dividend[-2] - divisor[-2]
        remainder = [
            q*divisor[k] + (divisor[k-1] if k else 0) - dividend[k]
            for k in range(len(divisor)-1)
        ]
        pivot = remainder[-1]
        if pivot < 0:
            return 0
        if not pivot > 0:
            raise ArithmeticError(f'Unresolved Sturm sign for {configuration}')
        dividend, divisor = divisor, [v/pivot for v in remainder[:-1]] + [arb(1)]
    return 1


def classification_digest(rows):
    """Hash LF-terminated compact JSON [A,B,survives_A,survives_B], in (A,B) lex order."""
    digest = hashlib.sha256()
    for row in sorted(rows):
        digest.update((json.dumps(row, separators=(',', ':')) + '\n').encode('ascii'))
    return digest.hexdigest()


def classification_rows(n=N, numerator=85, denominator=84, same_gaps=True):
    ctx.prec = PRECISION
    sites, columns = cayley_basis(n, numerator, denominator)
    return [(a, b, survives(a, sites, columns), survives(b, sites, columns))
            for a, b in complementary_pairs(n, same_gaps)]


def summarize(rows, n, numerator, denominator):
    assert len({s for a, b, _, _ in rows for s in (a, b)}) == 2*len(rows)
    differences = Counter(y-x for _, _, x, y in rows)
    survivors = [sum(r[j] for r in rows) for j in (2, 3)]
    return {
        'python_flint': flint.__version__,
        'bits': PRECISION,
        'n': n,
        'exp_time': [numerator, denominator],
        'pairs': len(rows),
        'survivors': survivors,
        'differences': dict(sorted(differences.items())),
        'digest_format': 'sorted pairs, compact ASCII JSON [A,B,survives_A,survives_B] plus LF per pair',
        'sha256': classification_digest(rows),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ten', action='store_true',
                        help='check all N=10 complementary orbit-pairs at 73/72 and 71/70')
    args = parser.parse_args()
    if args.ten:
        reports = []
        for numerator, denominator in [(73, 72), (71, 70)]:
            rows = classification_rows(10, numerator, denominator, same_gaps=False)
            assert len(rows) == 2234
            reports.append(summarize(rows, 10, numerator, denominator))
        print(json.dumps(reports, indent=2))
    else:
        rows = classification_rows()
        report = summarize(rows, N, 85, 84)
        assert report['pairs'] == 1489 and report['survivors'] == [324, 443]
        assert report['differences'] == {-1: 137, 0: 1096, 1: 256}
        print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
