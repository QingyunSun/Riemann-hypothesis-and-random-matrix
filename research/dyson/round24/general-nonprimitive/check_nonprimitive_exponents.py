"""Exact scalar checks only: no prime, factor, or divisor enumeration."""

from fractions import Fraction as F
import json
from pathlib import Path


def main() -> None:
    alpha_min, alpha_max, rho, eta = F(11, 5), F(9, 4), F(523, 1000), F(1, 100)
    checks = {
        "support_upper_ratio_at_T4": F(2) + F(2, 4),
        "H_over_sqrtX_min_exponent": F(1, 2) - 1 / alpha_min,
        "H_over_Q_min_exponent": 1 - 1 / alpha_min - rho,
        "nonprimitive_decay_exponent": 1 / alpha_max - eta,
        "primitive_completion_decay_exponent": 24 * (1 - 1 / alpha_min - rho) - rho,
        "H_over_X_T_exponent": F(-1),
    }
    assert checks["support_upper_ratio_at_T4"] == F(5, 2) < 3
    assert checks["H_over_sqrtX_min_exponent"] == F(1, 22) > 0
    assert checks["H_over_Q_min_exponent"] == F(247, 11000) > 0
    assert checks["nonprimitive_decay_exponent"] == F(391, 900) > 0
    assert checks["primitive_completion_decay_exponent"] == F(7, 440) > 0
    assert checks["H_over_X_T_exponent"] == -1
    result = {
        "status": "PASS",
        "exact_assertions": 6,
        "scope": "Rational scalar normalization and exponents only; no arithmetic enumeration or numerical asymptotic claim.",
        "values": {key: str(value) for key, value in checks.items()},
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("nonprimitive_exponent_checks.json").write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
