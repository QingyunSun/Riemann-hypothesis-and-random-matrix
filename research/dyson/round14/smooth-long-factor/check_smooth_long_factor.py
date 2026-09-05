#!/usr/bin/env python3
"""Exact arithmetic checks and a fixed Gaussian Poisson sign diagnostic."""

from fractions import Fraction as F
from pathlib import Path
import cmath
import hashlib
import json
import math
import re


def factor(n: int) -> dict[int, int]:
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def mu(n: int) -> int:
    fs = factor(n)
    return 0 if any(e > 1 for e in fs.values()) else (-1) ** len(fs)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def ramanujan(q: int, a: int) -> int:
    return sum(d * mu(q // d) for d in divisors(math.gcd(q, a)))


def add_symbolic(target: dict[int, int], value: dict[int, int], multiplier: int) -> None:
    for p, coefficient in value.items():
        target[p] = target.get(p, 0) + multiplier * coefficient
        if target[p] == 0:
            del target[p]


def convolution(a: list[int], b: list[int]) -> list[int]:
    limit = len(a) - 1
    result = [0] * (limit + 1)
    for d in range(1, limit + 1):
        if a[d]:
            for m in range(1, limit // d + 1):
                result[d * m] += a[d] * b[m]
    return result


def symbolic_divisor_identity() -> dict:
    """Represent log(n) exactly as sum_p v_p(n) L_p with formal variables L_p."""
    k, y = 3, 5
    limit = y**k
    one = [0] + [1] * limit
    identity = [0, 1] + [0] * (limit - 1)
    short_mu = [0] + [mu(n) if n <= y else 0 for n in range(1, limit + 1)]
    mu_power = identity
    one_power = identity
    hb = [{} for _ in range(limit + 1)]
    for j in range(1, k + 1):
        mu_power = convolution(mu_power, short_mu)
        if j > 1:
            one_power = convolution(one_power, one)
        coefficient = convolution(mu_power, one_power)
        multiplier = (-1) ** (j - 1) * math.comb(k, j)
        for n in range(1, limit + 1):
            for d in divisors(n):
                add_symbolic(hb[n], factor(n // d), multiplier * coefficient[d])

    cutoff = F(9, 2)
    for n in range(1, limit + 1):
        fs = factor(n)
        expected = {next(iter(fs)): 1} if len(fs) == 1 else {}
        assert hb[n] == expected, (n, hb[n], expected)
        short, long = {}, {}
        for r in divisors(n):
            add_symbolic(short if r <= cutoff else long, factor(n // r), mu(r))
        combined = short.copy()
        add_symbolic(combined, long, 1)
        assert combined == expected, (n, combined, expected)
    return {
        "k": k, "Y": y, "range_including_n1": [1, limit],
        "formal_basis": "independent symbols L_p for log(p)",
        "real_short_cutoff": str(cutoff),
        "checks": "HB identity and exact short+long mu*log partition",
    }


def centering_checks() -> dict:
    cases = 0
    for q in [5, 8, 15, 35]:
        phi = ramanujan(q, 0)
        assert phi == sum(math.gcd(m, q) == 1 for m in range(q))
        for a in range(q):
            total = F(0)
            for n in range(1, 12):
                if math.gcd(n, q) == 1:
                    weight = F((-1) ** n * (n + 1), 7)
                    assert ramanujan(q, a * n) == ramanujan(q, a)
                    total += weight * (ramanujan(q, a * n) - ramanujan(q, a))
            assert total == 0
            cases += 1
    return {"periodic_numerator_cases": cases, "includes_non_squarefree_modulus": True}


def gaussian_poisson_check() -> list[dict]:
    records = []
    for q, length, residue, center in [(5, 9, 2, 1.25), (8, 11, 3, 1.3)]:
        assert math.gcd(residue, q) == 1
        phi = ramanujan(q, 0)
        profile = lambda s: math.exp(-math.pi * (s / length - center) ** 2)
        progression = sum(profile(s) for s in range(-150, 151) if s % q == residue)
        primitive = sum(profile(s) for s in range(-150, 151) if math.gcd(s, q) == 1)
        direct = progression - primitive / phi
        fourier = 0j
        for k in range(-20, 21):
            if k == 0:
                continue
            frequency = k * length / q
            transform = math.exp(-math.pi * frequency**2) * cmath.exp(
                -2j * math.pi * center * frequency
            )
            fourier += length / q * transform * (
                cmath.exp(2j * math.pi * k * residue / q) - ramanujan(q, k) / phi
            )
        difference = abs(direct - fourier)
        assert difference < 1e-12, difference
        records.append({
            "q": q, "L": length, "b": residue, "gaussian_center": center,
            "direct_centered_progression": direct,
            "fourier_real": fourier.real, "fourier_imaginary": fourier.imag,
            "absolute_difference": difference,
            "scope": "binary64 sign/normalization diagnostic for a Schwartz Gaussian, not a rigorous analytic certificate",
        })
    return records


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parent
    base = root.parents[1]
    rho, u, theta = F(523, 1000), F(2, 5), F(2, 7)
    ratio_margin = 1 - rho - u
    exponent4 = 1 + theta - 4 * ratio_margin
    exponent17 = 1 + theta - 17 * ratio_margin
    assert ratio_margin == F(77, 1000)
    assert exponent4 == F(1711, 1750)
    assert 1 - exponent4 == F(39, 1750)
    assert exponent17 == F(-163, 7000)
    assert 1 - rho == F(477, 1000)

    hb = symbolic_divisor_identity()
    center = centering_checks()
    poisson = gaussian_poisson_check()
    report = root / "SMOOTH_LONG_FACTOR_REMOVAL.md"
    body = report.read_text()
    assert "\ufffd" not in body
    assert not [c for c in body if ord(c) < 32 and c not in "\n\t"]
    for left, right in [(r"\[", r"\]"), (r"\(", r"\)")]:
        count = lambda token: len(re.findall(r"(?<!\\)" + re.escape(token), body))
        assert count(left) == count(right)
    source = base / "sources/openai-short-gaps.pdf"
    assert digest(source) == "456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930"
    previous = base / "research-round13/phase-resonance/AVERAGED_RATIONAL_PHASE_TEST.md"
    assert digest(previous) == "7f4285cb02241e22bdb29a1ad4952f7ab8249e3ec3bef984455a57ae05e41ebb"
    bridge = base / "research-round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md"
    assert digest(bridge) == "982039f0e163b84c1c5b8f2b52f215eb40e7b89863085f2840c039853606f39a"

    receipt = {
        "status": "PASS: exact centering, symbolic divisor identities, exponents and fixed Poisson diagnostic",
        "main_bound": "H X (U Q/X)^J log(X)^2",
        "scales": {"Q_exponent": str(rho), "witness_U_exponent": str(u), "max_H_exponent": str(theta)},
        "witness": {
            "derivative_order": 4, "Q_over_long_scale_power": str(ratio_margin),
            "bound_exponent": str(exponent4), "margin_below_X": str(1 - exponent4),
        },
        "general_range": {
            "eta": "any fixed 0<eta<477/1000",
            "U": "U<=X^(477/1000-eta)",
            "derivative_condition_for_o_XlogX": "fixed integer J>=2 with J*eta>2/7",
            "uniformity": "profile seminorms O_J(log(X)^2), constants may depend on eta",
        },
        "symbolic_convolution_checks": hb,
        "exact_period_centering": center,
        "gaussian_poisson_diagnostics": poisson,
        "source": {
            "path": str(source), "sha256": digest(source),
            "url": "https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf",
            "role": "coefficient terminology and HB context; Poisson component proof written directly",
        },
        "frozen_dependencies": {
            "R9_bridge_sha256": digest(bridge), "R13_phase_report_sha256": digest(previous),
        },
        "report_sha256": digest(report), "script_sha256": digest(Path(__file__)),
        "scope_limits": [
            "unconditional classical Poisson application, no novelty claim",
            "actual complete smooth kernel and primitive main retained",
            "an individual smooth long variable is required",
            "arithmetic shorter coefficient may have signs",
            "Lambda_>U is an exact signed remainder, not necessarily balanced",
            "no estimate for the remaining full discrepancy",
            "no large-prime realization, parameter scan or high-J numerical work",
        ],
    }
    (root / "smooth_long_factor_certificate.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS: exact uniform mean centering on 63 fixed numerator cases.")
    print("PASS: symbolic mu*log and Heath-Brown identities including n=1 and real cutoff.")
    print("PASS: fixed Gaussian Poisson sign diagnostics; each absolute error <1e-12.")
    print("PASS: exponent 1711/1750 with margin 39/1750; general cutoff condition recorded.")
    print("PASS: pinned source and frozen R9/R13 dependencies.")
    print("Report SHA256:", receipt["report_sha256"])
    print("Script SHA256:", receipt["script_sha256"])


if __name__ == "__main__":
    main()
