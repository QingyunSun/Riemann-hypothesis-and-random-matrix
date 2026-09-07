"""Small exact identities only; no prime or matrix computation."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as s


def main() -> None:
    x, y, u, T, Y, lam = s.symbols("x y u T Y lam", positive=True)
    p = s.exp(T * s.log(x / (x + y)))
    A = lambda f: x * (s.diff(f, x) - s.diff(f, y))
    checks: dict[str, bool] = {}
    checks["fixed_endpoint_pareto"] = s.simplify(A(p) - T * p) == 0
    checks["fixed_endpoint_pareto_second"] = s.simplify(A(A(p)) - T**2 * p) == 0
    V = s.Function("V")
    checks["fixed_endpoint_profile"] = s.simplify(
        A(V(y / Y)) + x * s.diff(V(y / Y), y)
    ) == 0
    k = V((u - x) / Y) * s.exp(T * s.log(x / u))
    checks["kernel_translation_commutator"] = s.simplify(
        s.diff(k, x) + s.diff(k, u) - T * (1 / x - 1 / u) * k
    ) == 0
    # dy=(x/T) d lambda, so (dx/x) dy=(dx/T) d lambda.
    checks["short_interval_measure_change"] = s.simplify(
        s.diff(lam * x / T, lam) / x - 1 / T
    ) == 0
    z = s.symbols("z")
    for j in range(7):
        checks[f"mellin_binomial_{j}"] = s.expand(
            (1 + z**2 / T**2) ** j
            - sum(s.binomial(j, r) * z ** (2 * r) / T ** (2 * r)
                  for r in range(j + 1))
        ) == 0
    # Exact derivative of the odd-index phase, in cycles.
    r = s.symbols("r", positive=True)
    phase = z * s.log(2 * r + 1) / (2 * s.pi)
    checks["odd_phase_stationary_normalization"] = s.simplify(
        s.diff(phase, r) - z / (s.pi * (2 * r + 1))
    ) == 0
    result = {
        "scope": "exact elementary symbolic identities; no analytic source verification",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "count": len(checks),
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    (Path(__file__).parent / "mellin_energy_checks.json").write_text(payload)
    print(payload, end="")
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
