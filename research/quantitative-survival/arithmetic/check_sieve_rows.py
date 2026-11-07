"""Check exact finite examples for the common-sieve construction.

Run with Python 3: python3 check_sieve_rows.py > sieve_checks.json
"""

from collections import Counter
from fractions import Fraction as F
import json
from math import ceil, floor, gcd, prod


def row_density(primes, n, h):
    """CRT density from the number of excluded residues at each prime."""
    factors = []
    for p in primes:
        if n % p == 0 and h % p == 0:
            excluded = p
        elif n % p == 0 or h % p == 0:
            excluded = 1
        else:
            excluded = 2
        factors.append(F(p - excluded, p))
    return prod(factors)


def tent(t, period):
    """Positive multiplier on the m=x/n coordinate, with peak 5/4."""
    a = F(period, 4)
    return 1 + (max(t-a, F(0)) - 2*max(t-2*a, F(0)) + max(t-3*a, F(0)))/period


def integral(t, period):
    """Integral of tent from 0 to t."""
    a = F(period, 4)
    return t + (max(t-a, F(0))**2 - 2*max(t-2*a, F(0))**2
                + max(t-3*a, F(0))**2)/(2*period)


def insist(condition, context):
    if not condition:
        raise AssertionError(context)


def main():
    counts = Counter()
    largest_prefix_fraction = F(0)
    largest_cumulative_fraction = F(0)
    for primes in ((2,), (2, 3), (2, 3, 5), (2, 3, 5, 7)):
        q = prod(primes)
        for n in (2, 3, 4, 5, 9, 11):
            for h in (*range(-12, 0), *range(1, 13)):
                key = (q, n, h)
                d = row_density(primes, n, h)
                mask = [gcd(m*(n*m+h), q) == 1 for m in range(1, q+1)]
                insist(sum(mask) == q*d, key)
                counts["period_density_rows"] += 1
                admissible = gcd(n, h) == 1 and n*h % 2 == 0
                # This positive rational is a test row scale in place of S_n(h).
                s = 1 + F(abs(h) % 5, 4) if admissible else 0
                insist(not admissible or d > 0, key)
                counts["admissible_rows" if admissible else "zero_rows"] += 1
                endpoint = max(F(0), F(-h, n))
                cumulative = F(0)
                prefix = 0
                previous_floor = 0
                for m in range(1, 2*q+1):
                    chosen = mask[(m-1) % q]
                    prefix += int(chosen)
                    if d > 0:
                        # Between jumps this discrepancy is affine. Check both
                        # endpoint limits over every interval in two periods.
                        for selected in (prefix - int(chosen), prefix):
                            delta = abs(F(selected)/d - m)
                            insist(delta <= q, (key, m, "prefix"))
                            largest_prefix_fraction = max(largest_prefix_fraction, delta/q)
                            counts["prefix_endpoint_checks"] += 1
                    eligible = admissible and chosen and m > endpoint
                    if eligible:
                        cumulative += s*tent(F(m), q)/d
                    rounded = floor(cumulative)
                    jump = rounded - previous_floor
                    insist(jump >= 0 and (eligible or jump == 0), (key, m, "support"))
                    if eligible:
                        insist(jump <= ceil(F(5, 4)*s/d), (key, m, "atom size"))
                    # C is increasing. At m check both limiting values of
                    # the grid primitive, covering the whole interval.
                    continuous = s*(integral(F(m), q) - integral(endpoint, q)) if m > endpoint else F(0)
                    bound = 1 + 3*s*q
                    for mass in (previous_floor, rounded):
                        delta = abs(mass-continuous)
                        insist(delta <= bound, (key, m, "cumulative"))
                        largest_cumulative_fraction = max(largest_cumulative_fraction, delta/bound)
                        counts["cumulative_endpoint_checks"] += 1
                    counts["grid_jump_checks"] += 1
                    counts["positive_integer_atoms"] += jump > 0
                    previous_floor = rounded
    print(json.dumps({
        "scope": "Supplementary finite invariant checks with exact rational arithmetic. "
                 "The packet limit requires the analytic proof.",
        "moduli": [2, 6, 30, 210],
        "prime_power_twists": [2, 3, 4, 5, 9, 11],
        "shifts": "all nonzero integers from -12 to 12",
        "weight": "positive rational row scale times a piecewise-linear multiplier "
                  "of height 1 to 5/4 on the m=x/n coordinate",
        "checks": dict(sorted(counts.items())),
        "largest_prefix_error_divided_by_Q": str(largest_prefix_fraction),
        "largest_rounded_primitive_error_divided_by_1_plus_3sQ": str(largest_cumulative_fraction),
        "status": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
