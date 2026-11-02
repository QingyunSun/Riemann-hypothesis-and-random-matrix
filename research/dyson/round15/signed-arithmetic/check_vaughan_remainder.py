#!/usr/bin/env python3
"""Exact finite checks for the R15 arithmetic reduction; no zeta experiment.

Run: python3 check_vaughan_remainder.py [--output result.json] [--research-base BASE]
Only the Python standard library is required. Logarithms are represented by
independent formal symbols log(p), with integer coefficients throughout.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

N_MAX = 4096
BASE = Path(__file__).resolve().parents[2]
SOURCES = {
    "r14_smooth": "research-round14/smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md",
    "r13_phase": "research-round13/phase-resonance/AVERAGED_RATIONAL_PHASE_TEST.md",
    "r9_bridge": "research-round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md",
    "r12_dispersion": "research-round12/dispersion-transfer/DISPERSION_HYPOTHESIS_OBSTRUCTION.md",
    "primary_pdf": "sources/openai-short-gaps.pdf",
    "primary_text": "sources/openai-short-gaps.txt",
}


def factor(n: int) -> dict[int, int]:
    ans = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            ans[d] = ans.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def mobius(fac: dict[int, int]) -> int:
    return 0 if any(v > 1 for v in fac.values()) else (-1) ** len(fac)


def divisors(fac: dict[int, int]) -> list[int]:
    ds = [1]
    for p, v in fac.items():
        ds = [d * p**j for d in ds for j in range(v + 1)]
    return sorted(ds)


def add(out: dict[int, int], val: dict[int, int], scale: int = 1) -> None:
    for p, c in val.items():
        out[p] = out.get(p, 0) + scale * c
        if not out[p]:
            del out[p]


def lam(fac: dict[int, int]) -> dict[int, int]:
    return {next(iter(fac)): 1} if len(fac) == 1 else {}


def beta_from_factor(fac: dict[int, int], cutoff: F) -> dict[int, int]:
    return {p: sum(p**j > cutoff for j in range(1, v + 1))
            for p, v in fac.items() if any(p**j > cutoff for j in range(1, v + 1))}


def remainder_from_factor(fac: dict[int, int], A: F, B: F) -> dict[int, int]:
    out = {}
    for a in divisors(fac):
        if a > A:
            af = factor(a)
            rem = {p: v - af.get(p, 0) for p, v in fac.items() if v > af.get(p, 0)}
            add(out, beta_from_factor(rem, B), mobius(af))
    return out


def finite_identities() -> list[dict]:
    fac = [None] + [factor(n) for n in range(1, N_MAX + 1)]
    ds = [None] + [divisors(fac[n]) for n in range(1, N_MAX + 1)]
    mu = [0] + [mobius(fac[n]) for n in range(1, N_MAX + 1)]
    lm = [None] + [lam(fac[n]) for n in range(1, N_MAX + 1)]
    output = []
    for A, B, U in [(F(2), F(3), F(6)), (F(5, 2), F(9, 2), F(45, 4)),
                    (F(7), F(5), F(35))]:
        beta = [{} for _ in range(N_MAX + 1)]
        lowbeta = [{} for _ in range(N_MAX + 1)]
        for d in range(1, N_MAX + 1):
            if lm[d]:
                target = beta if d > B else lowbeta
                for n in range(d, N_MAX + 1, d):
                    add(target[n], lm[d])
        # Independent ordered (a,d,s) construction, grouped only after summation.
        triple_R = [{} for _ in range(N_MAX + 1)]
        triple_terms = 0
        for a in range(int(A) + 1, N_MAX + 1):
            if not mu[a]:
                continue
            for d in range(int(B) + 1, N_MAX // a + 1):
                if lm[d]:
                    for n in range(a * d, N_MAX + 1, a * d):
                        add(triple_R[n], lm[d], mu[a])
                        triple_terms += 1
        for n in range(1, N_MAX + 1):
            TA, TU, C, R, old = {}, {}, {}, {}, {}
            for a in ds[n]:
                m = n // a
                if a <= A:
                    add(TA, fac[m], mu[a])
                    add(C, lowbeta[m], mu[a])
                else:
                    add(R, beta[m], mu[a])
                if a <= U:
                    add(TU, fac[m], mu[a])
                else:
                    add(old, fac[m], mu[a])
            rhs = dict(lm[n] if n <= B else {})
            add(rhs, TA)
            add(rhs, C, -1)
            add(rhs, R)
            assert rhs == lm[n], ("Vaughan", n, A, B)
            rhs_old = dict(lm[n] if n <= B else {})
            add(rhs_old, R)
            add(rhs_old, C, -1)
            add(rhs_old, TA)
            add(rhs_old, TU, -1)
            assert old == rhs_old, ("old_remainder", n, A, B, U)
            assert R == triple_R[n], ("triple_grouping", n, A, B)
            assert beta[n] == beta_from_factor(fac[n], B)
            if len(fac[n]) == 1 and next(iter(fac[n].values())) == 1:
                assert R == {}
            if B < n <= 2 * B:
                assert beta[n] == lm[n]
        output.append({"A": str(A), "B": str(B), "U0": str(U),
                       "n_range": [1, N_MAX], "identities_per_n": 4,
                       "independent_triple_terms": triple_terms, "status": "PASS"})
    return output


def support_witnesses() -> list[dict]:
    X, H, T, h = 10**10, 100, 10**8, 150
    facts = [({100003: 1, 120011: 1}, {100003: -1, 120011: -1}, "negative"),
             ({50021: 1, 59: 1, 61: 1, 67: 1}, {50021: 2}, "positive")]
    output = []
    for fac, expected, sign in facts:
        assert all(factor(p) == {p: 1} for p in fac), fac
        n = 1
        for p, v in fac.items():
            n *= p**v
        got = remainder_from_factor(fac, F(100), F(100))
        assert got == expected, (fac, got)
        assert X < n - h < F(3, 2) * X
        # log(1+x)<x: the exact rational upper bound proves the sinc is positive.
        phase_upper = F(T * h, n - h)
        assert 0 < phase_upper < F(3, 2) < 3
        assert F(h, H) == F(3, 2)
        output.append({"factorization": fac, "n": n, "R_formal_log_coefficients": got,
                       "sign": sign, "support_ratio": str(F(n - h, X)),
                       "sinc_phase_strict_upper_bound": str(phase_upper),
                       "parameters": {"X": X, "H": H, "T": T, "h": h,
                                      "A": 100, "B": 100}, "status": "PASS"})
    return output


def rational_checks() -> dict:
    q = F(523, 1000)
    sym_eta = 1 - q - F(2, 5)
    sym_exp = 1 + F(2, 7) - 4 * sym_eta
    asym_eta = 1 - q - F(47, 100)
    asym_exp = 1 + F(2, 7) - 41 * asym_eta
    assert sym_exp == F(1711, 1750) < 1
    assert asym_exp == F(6991, 7000) < 1
    omega, delta, sigma = F(12, 1000), F(1, 1000), F(101, 1000)
    # Proposition 2.18's three printed inequalities.
    source_left = [
        72 * omega + 24 * delta,
        48 * omega + 16 * delta + 4 * sigma,
        64 * omega + 20 * delta + 2 * sigma,
    ]
    # Exact source transcription: Proposition 2.18, equation (2.14).
    source_claimed = [F(888, 1000), F(996, 1000), F(990, 1000)]
    assert source_left == source_claimed
    assert all(x < 1 for x in source_left)
    max_sigma = min((1 - 48 * omega - 16 * delta) / 4,
                    (1 - 64 * omega - 20 * delta) / 2)
    assert max_sigma == F(102, 1000)
    assert F(1, 2) - max_sigma == F(398, 1000)
    return {"Q_exponent": str(q), "symmetric_eta": str(sym_eta),
            "symmetric_error_exponent": str(sym_exp), "symmetric_margin_below_one": str(1 - sym_exp),
            "asymmetric_eta": str(asym_eta), "asymmetric_error_exponent": str(asym_exp),
            "asymmetric_margin_below_one": str(1 - asym_exp),
            "fixed_source_lower_exponent": str(F(1, 2) - sigma),
            "strict_limiting_source_lower_exponent": str(F(398, 1000)),
            "cutoff_sum_upper_bound": str(1 - q),
            "both_source_cutoffs_would_require": str(2 * (F(1, 2) - sigma)),
            "source_inequality_left_sides": [str(x) for x in source_claimed]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("vaughan_checks.json"))
    parser.add_argument("--research-base", type=Path, default=BASE)
    args = parser.parse_args()
    result = {"status": "PASS", "arithmetic": "exact formal logarithm coefficients and rational numbers",
              "finite_identities": finite_identities(), "signed_support_witnesses": support_witnesses(),
              "rational_checks": rational_checks(),
              "limitations": ["No finite test proves Siegel-Walfisz or Poisson decay.",
                              "No estimate of the full signed bilinear form or actual zeta zeros.",
                              "Support witnesses do not determine a full discrepancy sign."]}
    missing = []
    src = {}
    for key, rel in SOURCES.items():
        path = args.research_base / rel
        if path.exists():
            src[key] = {"relative_to_research_base": rel,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        else:
            missing.append(rel)
    assert not missing, missing
    result["sources"] = src
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "n_max": N_MAX,
                      "finite_identity_equalities": 3 * N_MAX * 4,
                      "signed_support_witnesses": len(result["signed_support_witnesses"]),
                      "result_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
