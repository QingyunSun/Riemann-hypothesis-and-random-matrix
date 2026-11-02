#!/usr/bin/env python3
"""Exact source-parameter and modular checks; no prime search or asymptotic test."""

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import re


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parent
    base = root.parents[1]
    omega, delta, retreat, sigma = F(3, 250), F(1, 1000), F(1, 1000), F(101, 1000)
    rho, n_exp, m_exp = F(523, 1000), F(2, 5), F(3, 5)
    large, small = F(9, 100), F(343, 346000)
    values = [
        72 * omega + 24 * delta,
        48 * omega + 16 * delta + 4 * sigma,
        64 * omega + 20 * delta + 2 * sigma,
    ]
    assert values == [F(111, 125), F(249, 250), F(99, 100)]
    assert all(value < 1 for value in values)
    assert F(1, 2) + 2 * omega - retreat == rho
    assert n_exp + m_exp == 1
    assert F(1, 2) - sigma < n_exp < F(1, 2)
    assert m_exp - rho == F(77, 1000) > 0
    assert rho - n_exp == F(123, 1000) > 0
    assert rho - F(2, 7) == F(1661, 7000) > 0
    assert F(1, 6) - large == F(23, 300) > 0
    assert 2 * large + 346 * small == rho
    assert small < delta < large
    sigma_ceiling = (1 - 48 * omega - 16 * delta) / 4
    shorter_floor = F(1, 2) - sigma_ceiling
    assert sigma_ceiling == F(51, 500)
    assert shorter_floor == F(199, 500)
    assert shorter_floor - F(2, 7) == F(393, 3500) > 0

    # Exact cubic-phase algebra in Q(i sqrt(3)): z = real + coeff*i*sqrt(3).
    e_one_third = (F(-1, 2), F(1, 2))
    e_two_thirds = (F(-1, 2), F(-1, 2))
    discrepancy = tuple((x - y) / 4 for x, y in zip(e_one_third, e_two_thirds))
    assert discrepancy == (F(0), F(1, 4))

    # Fixed toy moduli check only the two sign branches and unit selection.
    # They are not asserted to satisfy the large-X canonical support conditions.
    modular_cases = []
    for d in [35, 55, 65, 77, 85, 143]:
        assert math.gcd(d, 3) == 1
        if d % 3 == 1:
            k, phase_sign = (d - 1) // 3, -1
        else:
            k, phase_sign = (d + 1) // 3, 1
        assert math.gcd(k, d) == 1
        assert F(k, d) - F(1, 3) == F(phase_sign, 3 * d)
        lower = 100 * d + 17
        m = lower + (k - lower) % d
        assert lower <= m < lower + d < 2 * lower
        assert m % d == k and math.gcd(m, d) == 1
        modular_cases.append({
            "d": d, "k": k, "sign_relative_to_one_third": phase_sign,
            "phase_difference": str(F(k, d) - F(1, 3)),
            "toy_lower_endpoint": lower, "unit_representative": m,
        })

    pdf = base / "sources/openai-short-gaps.pdf"
    text = base / "sources/openai-short-gaps.txt"
    conductor = base / "research-round11/conductor-arithmetic/CONDUCTOR_MASS_LOWER_BOUND.md"
    previous = base / "research-round11/prime-frequency/CENTERED_SMALL_ARC_BOUND.md"
    expected = {
        pdf: "456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930",
        text: "ded13a7c74fcfce64e85769e05b5869803dccdf53b88be2c2f3c0b344f95ee84",
        conductor: "46347799005bb0f53af25c2a7e8ffb2b2217d92688c7651327dde3562f114b92",
    }
    for path, wanted in expected.items():
        assert digest(path) == wanted, f"Pinned source changed: {path}"
    report = root / "DISPERSION_HYPOTHESIS_OBSTRUCTION.md"
    report_bytes = report.read_bytes()
    controls = [(i, value) for i, value in enumerate(report_bytes) if value < 32 and value not in (9, 10)]
    assert not controls, controls
    report_text = report_bytes.decode("utf-8")
    assert "\ufffd" not in report_text
    for left, right in [(r"\[", r"\]"), (r"\(", r"\)")]:
        # TeX row breaks followed by "(" are not Markdown math delimiters.
        count = lambda token: len(re.findall(r"(?<!\\)" + re.escape(token), report_text))
        assert count(left) == count(right)

    receipt = {
        "status": "PASS: exact source inequalities, modular identities, cubic-phase sign, and pinned sources",
        "assumptions": {
            "X": "all sufficiently large real X",
            "H": "X^(1/6) <= H <= X^(2/7)",
            "V": "fixed nonnegative nonzero C_c^infinity(1,2)",
            "RH": "not used for the two obstruction lemmas",
            "prime_counts": "ordinary PNT in fixed-ratio intervals and fixed reduced classes modulo 3",
        },
        "source_parameters": {
            "omega": str(omega), "delta": str(delta), "retreat": str(retreat),
            "sigma": str(sigma), "modulus_exponent": str(rho),
            "N_exponent": str(n_exp), "M_exponent": str(m_exp),
            "prop_2_18_left_sides": [str(value) for value in values],
            "prop_2_18_positive_margins": [str(1 - value) for value in values],
        },
        "positive_exponent_margins": {
            "M_over_d_growth": str(m_exp - rho),
            "d_over_N_growth": str(rho - n_exp),
            "nonzero_low_numerator": str(rho - F(2, 7)),
            "primitive_shift_class_count": str(F(1, 6) - large),
            "short_factor_scale_gap": str(shorter_floor - F(2, 7)),
        },
        "phase_discrepancy": {
            "normalization": "N/log N",
            "exact_leading_coefficient_in_Q_i_sqrt3": [str(x) for x in discrepancy],
            "meaning": "i sqrt(3)/4 for both d mod 3 branches",
            "perturbation": "O(N^2/(d log N)) = o(N/log N)",
            "failed_test": "source SW definition r=3, s=1, a=1, L=2",
        },
        "crt_hull": {
            "number_of_distinct_prime_factors": 348,
            "primitive_class_lower_bound": "(ell H/p)(1-347/(lambda X^kappa))-348",
            "local_images_after_global_coprimality": "all p-1 nonzero classes",
            "product_hull_cost": "phi(d) ~ d",
            "divisor_count": str(2**348),
        },
        "fixed_modular_algebra_cases": modular_cases,
        "primary_source": {
            "url": "https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf",
            "pdf_path": str(pdf), "pdf_sha256": digest(pdf),
            "text_path": str(text), "text_sha256": digest(text),
            "official_repository_commit": "61340d0b74163003b32756bb16e91d9209a5e330",
            "printed_locations": [
                "Proposition 2.3 pp4-5",
                "Definitions 2.6-2.9 p6",
                "Proposition 2.10 and equation (2.5) p7",
                "Proposition 2.14 pp9-10",
                "Proposition 2.18 pp10-11",
                "Appendix A.4.2 pp35-36",
            ],
        },
        "frozen_dependencies": {
            "conductor_report_path": str(conductor), "conductor_report_sha256": digest(conductor),
            "previous_prime_bound_path": str(previous), "previous_prime_bound_sha256": digest(previous),
        },
        "report_sha256": digest(report),
        "script_sha256": digest(Path(__file__)),
        "scope_limits": [
            "not a counterexample to the source theorem",
            "not a counterexample to cancellation in the actual signed prime pairing",
            "not proof every specific Heath-Brown factor loses SW",
            "CRT failure concerns the product-local hull, not every correlated residue-set method",
            "no numerical prime realization or parameter sweep",
            "finite script verifies algebra, not the asymptotic PNT statements",
            "no improvement of the current X^1.023 log^5 bound is claimed",
        ],
    }
    (root / "dispersion_hypotheses_certificate.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS: exact source scales and strict parameter inequalities.")
    print("PASS: phase discrepancy coefficient is +i*sqrt(3)/4 in both sign branches.")
    print("PASS: six fixed modular-selection examples; these are algebra checks only.")
    print("PASS: positive CRT and short-factor exponent margins.")
    print("PASS: primary PDF/text and frozen conductor hashes; report text checks.")
    print("Report SHA256:", receipt["report_sha256"])
    print("Script SHA256:", receipt["script_sha256"])


if __name__ == "__main__":
    main()
