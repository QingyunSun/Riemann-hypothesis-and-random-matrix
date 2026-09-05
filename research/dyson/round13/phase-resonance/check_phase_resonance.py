#!/usr/bin/env python3
"""Exact exponent, centering, Fourier and residue checks. No prime scan."""

from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import math
import re


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    value, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
        p += 1
    return -value if n > 1 else value


def ramanujan(d: int, k: int) -> int:
    return sum(r * mobius(d // r) for r in divisors(math.gcd(d, k)))


def trim(values: list[F]) -> list[F]:
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def divide(poly: list[F], divisor: list[F]) -> tuple[list[F], list[F]]:
    rem = trim(poly[:])
    result = [F(0)] * max(1, len(poly) - len(divisor) + 1)
    while len(rem) >= len(divisor) and any(rem):
        degree = len(rem) - len(divisor)
        scale = rem[-1] / divisor[-1]
        result[degree] += scale
        for j, coefficient in enumerate(divisor):
            rem[degree + j] -= scale * coefficient
        trim(rem)
    return trim(result), trim(rem)


@lru_cache
def cyclotomic(n: int) -> tuple[F, ...]:
    polynomial = [F(-1)] + [F(0)] * (n - 1) + [F(1)]
    for d in divisors(n):
        if d < n:
            polynomial, remainder = divide(polynomial, list(cyclotomic(d)))
            assert not any(remainder)
    return tuple(polynomial)


def exact_completion() -> dict:
    """Test (5) in Q(zeta_35), including nonunit m and both principal masks."""
    d = 35
    phi = ramanujan(d, 0)
    alpha = {m: F(m % 7 - 3, 4) for m in range(101, 117)}
    beta = {11: F(2), 13: F(3), 17: F(5), 19: F(7)}
    weights = {h: F(h + 1, 5) for h in range(1, 8)}
    assert all(math.gcd(n, d) == 1 for n in beta)
    unit_mass = sum(
        x * y for m, x in alpha.items() for n, y in beta.items()
        if math.gcd(m * n, d) == 1
    )
    lhs = F(0)
    for h, w in weights.items():
        if math.gcd(h, d) != 1:
            continue
        progression = sum(
            x * y for m, x in alpha.items() for n, y in beta.items()
            if (m * n - h) % d == 0
        )
        lhs += w * (progression - unit_mass / phi)
    rhs = [F(0)] * d
    for a in range(d):
        for h, w in weights.items():
            for m, x in alpha.items():
                for n, y in beta.items():
                    if math.gcd(m * n, d) == 1:
                        rhs[(a * (m * n - h)) % d] += w * x * y / d
            rhs[(-a * h) % d] -= w * ramanujan(d, a) * unit_mass / (d * phi)
    rhs[0] -= lhs
    _, remainder = divide(rhs, list(cyclotomic(d)))
    assert not any(remainder), remainder

    p0 = sum(beta.values())
    unit_second = sum(
        x * y * ramanujan(d, n - k)
        for n, x in beta.items() for k, y in beta.items()
    )
    unit_mean = sum(x * ramanujan(d, n) for n, x in beta.items()) / phi
    assert unit_mean == mobius(d) * p0 / phi
    centered = unit_second - p0 * p0 / phi
    full_second = d * sum(x * x for x in beta.values())
    assert 0 <= centered <= full_second
    assert max(beta) - min(beta) < d
    return {
        "modulus": d, "totient": phi,
        "ordinary_progression_value": str(lhs),
        "cyclotomic_remainder": [str(x) for x in remainder],
        "unit_mean": str(unit_mean),
        "centered_unit_second_moment": str(centered),
        "full_parseval_second_moment": str(full_second),
        "scope": "fixed rational coefficients on prime indices; checks the algebra, not asymptotic prime estimates",
    }


def residue_checks() -> dict:
    arcs = [(F(0), F(1, 40)), (F(1, 3) - F(1, 80), F(1, 3) + F(1, 80))]
    total_length = sum(right - left for left, right in arcs)
    cases = 0
    for d in [35, 55, 77, 143]:
        length = 413
        start = 413
        bound = (F(length, d) + 1) * (d * total_length + 2 * len(arcs))
        for a in range(1, d):
            if math.gcd(a, d) != 1:
                continue
            count = sum(
                any(left <= F((a * m) % d, d) <= right for left, right in arcs)
                for m in range(start, start + length)
            )
            assert count <= bound
            unit_count = sum(
                math.gcd(m, d) == 1
                and any(left <= F((a * m) % d, d) <= right for left, right in arcs)
                for m in range(start, start + length)
            )
            assert unit_count <= count
            cases += 1
    # Integer cutoff matters: use expanded width 2R/(qN).
    for n, r in [(101, 7), (103, 9), (200, 11)]:
        cut = n // r
        assert F(n, 2 * r) <= cut <= F(n, r)
        for q in range(1, cut + 1):
            assert F(1, q * cut) <= F(1, q * q)
            assert F(1, q * cut) <= F(2 * r, q * n)
    return {"unit_numerator_cases": cases, "integer_dirichlet_cutoff_cases": 3}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parent
    base = root.parents[1]
    q, m, n = F(523, 1000), F(3, 5), F(2, 5)
    exponents = {
        "q1_RH_extraction_error": q + m - n / 2,
        "restricted_positive_core": q + m,
        "centered_m_mean_square_bound": q + m + n / 2,
        "trivial_factored_bound": q + m + n,
        "Vaughan_N_4_5_term": q + m + F(4, 5) * n,
    }
    assert exponents == {
        "q1_RH_extraction_error": F(923, 1000),
        "restricted_positive_core": F(1123, 1000),
        "centered_m_mean_square_bound": F(1323, 1000),
        "trivial_factored_bound": F(1523, 1000),
        "Vaughan_N_4_5_term": F(1443, 1000),
    }
    assert 1 - exponents["q1_RH_extraction_error"] == F(77, 1000)
    assert q - n == F(123, 1000) > 0
    assert m - q == F(77, 1000) > 0
    assert F(523, 2000) < n
    core_count = F(1, 64) * F(1, 2)
    lower_constant = F(1, 16) * core_count * F(1, 32) * F(1, 2)
    assert core_count == F(1, 128)
    assert lower_constant == F(1, 131072)
    assert F(1, 2) - F(1, 4) == F(1, 4)
    assert F(1, 4) * F(1, 2) * F(1, 2) == F(1, 16)
    # The phase of e(s*p/d-a*h/d) lies in cycles (-1/8,1/16).
    assert F(2) * F(1, 32) == F(1, 16)
    assert F(2) * F(1, 16) == F(1, 8)

    completion = exact_completion()
    counts = residue_checks()
    source_dir = base / "research-round13/minor-arc-source/sources"
    sources = [
        (
            base / "sources/openai-short-gaps.pdf",
            "456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930",
            "https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf",
            "Propositions 2.3, 2.10, 2.18; Definition 2.9",
        ),
        (
            source_dir / "montgomery-vaughan-II-author-draft.pdf",
            "72448ec23158a3aeee534c9cde633d5402f916d0367b4f320212cd7ad179d340",
            "https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf",
            "Theorem17.1 equation17.29, printed65/PDF77",
        ),
        (
            source_dir / "schoenfeld-1976-II.pdf",
            "8c3cac1ee52eb05af05ec410adc587a18505a46aacdde41ae097038b0e7c3897",
            "https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf",
            "Theorem10 equation6.3, printed337/PDF1",
        ),
    ]
    source_receipts = []
    for path, expected, url, location in sources:
        got = digest(path)
        assert got == expected, path
        source_receipts.append({"path": str(path), "sha256": got, "url": url, "location": location})
    conductor = base / "research-round11/conductor-arithmetic/CONDUCTOR_MASS_LOWER_BOUND.md"
    assert digest(conductor) == "46347799005bb0f53af25c2a7e8ffb2b2217d92688c7651327dde3562f114b92"

    report = root / "AVERAGED_RATIONAL_PHASE_TEST.md"
    body = report.read_text()
    assert "\ufffd" not in body
    assert not [c for c in body if ord(c) < 32 and c not in "\n\t"]
    for left, right in [(r"\[", r"\]"), (r"\(", r"\)")]:
        count = lambda token: len(re.findall(r"(?<!\\)" + re.escape(token), body))
        assert count(left) == count(right)

    certificate = {
        "status": "PASS: exact algebra, rational exponents, residue bounds, centering and primary-source hashes",
        "exponents": {key: str(value) for key, value in exponents.items()},
        "q1_error_power_margin_below_X": "77/1000",
        "positive_core_lower_constant_after_c0_integralV": str(lower_constant),
        "positive_core_scope": "restricted actual F_X block, low primitive a, alpha=1, positive rational core",
        "positive_core_not_a_claim_about": [
            "the full signed family", "all rational arcs together",
            "a specific actual-zeta or Heath-Brown coefficient sequence",
        ],
        "exact_fourier_and_centered_variance": completion,
        "finite_residue_checks": counts,
        "source_receipts": source_receipts,
        "inherited_conductor_report_sha256": digest(conductor),
        "report_sha256": digest(report),
        "script_sha256": digest(Path(__file__)),
        "assumption_ledger": {
            "q1_integral_extraction": "ordinary RH for zeta",
            "positive_restricted_core": "ordinary PNT, no RH",
            "small_q_main_extraction": "classical SW; only logarithmic remainder asserted",
            "Vaughan_and_m_mean_square": "unconditional",
            "outer_coefficients": "|alpha_m|<=1; divisor-bounded extension costs X^eta",
            "support": "fixed inner prime interval independent of m",
        },
        "limitations": [
            "no numerical realization of the asymptotic canonical family",
            "no parameter scan",
            "no claim that R13 improves the existing R11 bound",
            "no GRH assumption silently inferred from ordinary RH",
            "finite exact tests verify algebra, not the analytic source theorems",
        ],
    }
    (root / "phase_resonance_certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
    print("PASS: exact exponent ledger and lower constant 1/131072.")
    print("PASS: unit-mask Fourier completion in Q(zeta_35) and exact centered variance.")
    print("PASS: finite residue bounds and integer Dirichlet-cutoff inequalities.")
    print("PASS: three primary-source hashes and the inherited arithmetic support hash.")
    print("Report SHA256:", certificate["report_sha256"])
    print("Script SHA256:", certificate["script_sha256"])


if __name__ == "__main__":
    main()
