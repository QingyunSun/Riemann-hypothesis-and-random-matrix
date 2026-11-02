#!/usr/bin/env python3
"""One finite float diagnostic, with separate exact rational checks.

No float result is a rigorous numerical enclosure. The ordinary proof is in
LOCAL_BRAGG_PRODUCTION.md. This checks all 8-element subsets of 16 sites once;
it does not scan N, evolve an ODE, or compute zeta zeros.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path


def main() -> None:
    n = 8
    sites = 2 * n
    beta = Fraction(1, 84)
    acceleration_bound = 12288
    s_star = beta / (4 * acceleration_bound)
    pi_upper = Fraction(22, 7)
    exact = {
        "s_star": str(s_star),
        "s_star_matches": s_star == Fraction(1, 4128768),
        "opening_rational_lower": str(Fraction(4, 105) / pi_upper),
        "opening_exceeds_beta": Fraction(4, 105) / pi_upper > beta,
        "chebyshev_hole_event_lower": str(Fraction(1, 8) - Fraction(4, 64)),
        "gap_increment_upper": str(128 * s_star + acceleration_bound * s_star**2),
        "gap_increment_below_quarter": 128 * s_star + acceleration_bound * s_star**2 < Fraction(1, 4),
        "acceleration_envelope": 40 * (128 * 2 + 16 * 3),
        "acceleration_below_chosen_bound": 40 * (128 * 2 + 16 * 3) < acceleration_bound,
        "deficit_coefficient_without_kappa": str(2 * beta**2),
    }
    assert all(value for key, value in exact.items() if isinstance(value, bool))

    kernel = [0.0] * sites
    derivative = [0.0] * sites
    pair_factor = [0.0] * sites
    for d in range(1, sites):
        sine = math.sin(math.pi * d / sites)
        kernel[d] = (2 * math.pi / n) / math.tan(math.pi * d / sites)
        derivative[d] = -(2 * math.pi**2 / n**2) / sine**2
        pair_factor[d] = 4 * sine**2

    masses: list[float] = []
    adjacent_masses: list[float] = []
    event_masses: list[float] = []
    weighted_good_bonds: list[float] = []
    weighted_force_energy: list[float] = []
    weighted_curvature: list[float] = []
    minimum_good_speed = math.inf
    maximum_acceleration = 0.0
    maximum_hole_identity_error = 0.0
    maximum_center_velocity_error = 0.0
    maximum_center_acceleration_error = 0.0
    maximum_curvature_normalization_error = 0.0
    good_pair_checks = 0
    config_count = 0

    for selected in combinations(range(sites), n):
        config_count += 1
        selected_set = set(selected)
        holes = set(range(sites)) - selected_set
        weight = sites ** (-n)
        for i, r in enumerate(selected):
            for u in selected[i + 1 :]:
                weight *= pair_factor[(r - u) % sites]
        masses.append(weight)
        velocities = {
            r: math.fsum(kernel[(r - u) % sites] for u in selected if u != r)
            for r in selected
        }
        accelerations = {
            r: math.fsum(
                derivative[(r - u) % sites] * (velocities[r] - velocities[u])
                for u in selected if u != r
            )
            for r in selected
        }
        maximum_acceleration = max(maximum_acceleration, *(abs(x) for x in accelerations.values()))
        maximum_center_velocity_error = max(maximum_center_velocity_error, abs(math.fsum(velocities.values())))
        maximum_center_acceleration_error = max(maximum_center_acceleration_error, abs(math.fsum(accelerations.values())))
        good_count = 0
        for r in range(sites):
            u = (r + 1) % sites
            good = r in selected_set and u in selected_set and any(
                (r + h) % sites in holes for h in range(2, 16)
            )
            if not good:
                continue
            good_count += 1
            good_pair_checks += 1
            gap_speed = velocities[u] - velocities[r]
            minimum_good_speed = min(minimum_good_speed, gap_speed)
            hole_expression = (2 * math.pi / n) * math.sin(math.pi / sites) * math.fsum(
                1 / (math.sin(math.pi * h / sites) * math.sin(math.pi * (h - 1) / sites))
                for h in range(2, sites)
                if (r + h) % sites in holes
            )
            maximum_hole_identity_error = max(maximum_hole_identity_error, abs(gap_speed - hole_expression))
        weighted_good_bonds.append(weight * good_count)
        if 0 in selected_set and 1 in selected_set:
            adjacent_masses.append(weight)
            if any(h in holes for h in range(2, 16)):
                event_masses.append(weight)

        sum_v_squared = math.fsum(v * v for v in velocities.values())
        force_energy = (n / (2 * math.pi)) ** 2 * sum_v_squared
        curvature_direct = -32 * math.pi**2 / n * sum_v_squared
        curvature_angular = -128 * math.pi**4 / n**3 * force_energy
        maximum_curvature_normalization_error = max(
            maximum_curvature_normalization_error, abs(curvature_direct - curvature_angular)
        )
        weighted_force_energy.append(weight * force_energy)
        weighted_curvature.append(weight * curvature_direct)

    normalization = math.fsum(masses)
    adjacent_probability = math.fsum(adjacent_masses)
    expected_adjacent = 0.25 - 1 / (4 * n**2 * math.sin(math.pi / sites) ** 2)
    event_probability = math.fsum(event_masses)
    expected_good_bonds = math.fsum(weighted_good_bonds)
    mean_force_energy = math.fsum(weighted_force_energy)
    expected_force_energy = n * (n**2 - 1) / 6
    mean_curvature = math.fsum(weighted_curvature)
    expected_curvature = -(64 * math.pi**4 / 3) * (1 - 1 / n**2)
    passed = (
        config_count == math.comb(16, 8)
        and abs(normalization - 1) < 1e-12
        and abs(adjacent_probability - expected_adjacent) < 1e-12
        and event_probability >= 1 / 16 - 1e-12
        and expected_good_bonds >= n / 8 - 1e-12
        and minimum_good_speed > float(beta)
        and maximum_acceleration < acceleration_bound
        and maximum_hole_identity_error < 1e-10
        and maximum_center_velocity_error < 1e-10
        and maximum_center_acceleration_error < 1e-10
        and abs(mean_force_energy - expected_force_energy) < 1e-10
        and abs(mean_curvature - expected_curvature) < 1e-9
        and maximum_curvature_normalization_error < 1e-9
    )
    output = {
        "status": "PASS" if passed else "FAIL",
        "scope": "One N=8 exhaustive FLOAT subset enumeration, not exact numerical proof; exact rational checks are separated.",
        "N": n,
        "configuration_count": config_count,
        "good_pair_checks": good_pair_checks,
        "exact_rational_checks": exact,
        "float_diagnostics": {
            "probability_mass": normalization,
            "adjacent_probability": adjacent_probability,
            "adjacent_formula": expected_adjacent,
            "good_event_probability": event_probability,
            "expected_good_unordered_bonds": expected_good_bonds,
            "minimum_good_initial_gap_speed": minimum_good_speed,
            "maximum_absolute_initial_acceleration": maximum_acceleration,
            "maximum_hole_formula_absolute_error": maximum_hole_identity_error,
            "maximum_center_velocity_error": maximum_center_velocity_error,
            "maximum_center_acceleration_error": maximum_center_acceleration_error,
            "mean_angular_force_square": mean_force_energy,
            "force_square_formula": expected_force_energy,
            "mean_coherent_B_second_derivative": mean_curvature,
            "coherent_B_formula": expected_curvature,
            "maximum_curvature_normalization_error": maximum_curvature_normalization_error,
        },
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "author_report_sha256": sha256(Path(__file__).with_name("LOCAL_BRAGG_PRODUCTION.md").read_bytes()).hexdigest(),
    }
    target = Path(__file__).with_name("local_bragg_checks.json")
    target.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
