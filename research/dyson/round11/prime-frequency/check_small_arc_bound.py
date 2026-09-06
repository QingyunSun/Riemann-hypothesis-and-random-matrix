#!/usr/bin/env python3
"""Exact bookkeeping checks, not a numerical test of an RH estimate."""

from fractions import Fraction as F
from hashlib import sha256
from math import gcd
from pathlib import Path
import json


def main() -> None:
    here = Path(__file__).resolve().parent
    q_exp = F(523, 1000)
    new_exp = F(1, 2) + q_exp
    comparisons = []
    for theta in (F(1, 6), F(2, 7)):
        old_exp = new_exp + theta / 2
        assert old_exp - new_exp == theta / 2
        comparisons.append({
            "theta": str(theta),
            "old_exponent": str(old_exp),
            "RH_exponent": str(new_exp),
            "power_saving": str(theta / 2),
        })
    assert new_exp == F(1023, 1000)
    assert new_exp - 1 == F(23, 1000)
    assert F(2, 7) + F(1, 2) + F(1, 100) == F(557, 700) < 1

    # One fixed finite Farey instance checks the range partition, not asymptotics.
    H, Q = 16, 97
    radii = [F(1, H), F(2, H), F(4, H), F(1, 2)]
    membership_count = 0
    arc_checks = 0
    all_frequencies = []
    band_counts = [0] * len(radii)
    for d in range(2, Q + 1):
        for rho in radii:
            count = sum(F(min(a, d - a), d) <= rho for a in range(1, d))
            assert count <= 2 * rho * d
            if count:
                assert d >= 1 / rho
            arc_checks += 1
        for a in range(1, d):
            if gcd(a, d) != 1:
                continue
            beta = F(a, d)
            distance = min(beta, 1 - beta)
            memberships = [distance <= radii[0]] + [
                radii[j - 1] < distance <= radii[j]
                for j in range(1, len(radii))
            ]
            assert sum(memberships) == 1
            band_counts[memberships.index(True)] += 1
            membership_count += 1
            all_frequencies.append(beta)
    all_frequencies.sort()
    separations = [b - a for a, b in zip(all_frequencies, all_frequencies[1:])]
    separations.append(1 + all_frequencies[0] - all_frequencies[-1])
    assert min(separations) >= F(1, Q * Q)

    # Squaring the Cauchy factor avoids square-root floating arithmetic.
    factors = []
    J = 2
    for j in range(9):
        coefficient_square_factor = F(2) ** ((1 - 2 * J) * j)
        energy_factor = F(2) ** j
        product = coefficient_square_factor * energy_factor
        assert product == (F(2) ** ((1 - J) * j)) ** 2
        factors.append(str(F(2) ** ((1 - J) * j)))
    assert sum(F(x) for x in factors) < 2

    result = {
        "status": "PASS",
        "scope": "Exact range, exponent, dyadic factor and one finite Farey partition checks only",
        "assumption_for_analytic_bound": "RH; the program does not test or prove the source theorem",
        "comparisons": comparisons,
        "remaining_power_above_covariance_scale": str(new_exp - 1),
        "prime_power_error_exponent": "557/700",
        "finite_instance": {
            "H": H,
            "Q": Q,
            "arc_count_checks": arc_checks,
            "unique_frequency_memberships": membership_count,
            "band_counts": band_counts,
            "minimum_spacing": str(min(separations)),
            "required_spacing": str(F(1, Q * Q)),
        },
        "J2_cauchy_band_factors_first_nine": factors,
        "J2_infinite_geometric_sum": "2",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    target = here / "check_small_arc_bound.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
