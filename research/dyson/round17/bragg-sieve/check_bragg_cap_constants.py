"""Exact constants for one specified centered short-interval cap argument."""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent


def main():
    # On scaling u=x*z, the moment is x^2*(int_0^1 z^2 dz
    # + int_1^infinity z^-2 dz).
    moment = F(1, 3) + 1
    assert moment == F(4, 3)
    rows = []
    for alpha, cap, centered in [
        (F(7, 4), F(14, 3), F(44, 9)),
        (F(2), F(4), F(4)),
        (F(9, 4), F(18, 5), F(52, 15)),
    ]:
        actual_cap = 2*alpha/(alpha-1)
        actual_centered = moment*(actual_cap-2+1)
        assert actual_cap == cap
        assert actual_centered == centered
        rows.append({
            "alpha": str(alpha),
            "short_interval_exponent_in_x": str(1-1/alpha),
            "von_mangoldt_cap": str(actual_cap),
            "centered_J_coefficient": str(actual_centered),
            "normalized_F_bound_power_of_T": str(alpha-1),
        })
    q, amin = F(5, 4), F(7, 4)
    powers = [3*q-3*amin, 2*q+1-3*amin, q+2-3*amin]
    assert powers == [F(-3, 2), F(-7, 4), F(-2)]
    assert 2*q/(q-1) == 10  # Uniform large-u cap, enlarged to 11.
    # log-Lipschitz slopes for the exact original a_u weight.
    assert max(abs(F(1, 2)), abs(F(-3, 2))) == F(3, 2)
    report = HERE / "BRAGG_SHORT_INTERVAL_CAP_TEST.md"
    result = {
        "status": "PASS",
        "scope": "Exact rational constants and exponent margins for a proved upper-bound calculation. No prime computation, no numerical bound for the Bragg limit.",
        "report_sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "moment_constant": str(moment),
        "rows": rows,
        "low_u_relative_powers_at_alpha_min": list(map(str, powers)),
        "uniform_large_u_cap_limit": "10",
        "kept_center_terms": "A^2 - 2*A*m + m^2",
    }
    (HERE / "bragg_cap_constants.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
