"""Independent exact rational spline checks; no zeta asymptotic computation."""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / "compact-packet" / "COMPACT_POLE_PACKET.md"


def derivative(p):
    return [i * p[i] for i in range(1, len(p))] or [F(0)]


def at(p, x):
    return sum((c * x**i for i, c in enumerate(p)), F(0))


def integral(p, left, right):
    return sum((c * (right**(i+1)-left**(i+1)) / (i+1)
                for i, c in enumerate(p)), F(0))


def main():
    # Positive-half formulas, using the actual y coordinate on both cells.
    inner = [F(2, 3), F(0), F(-1), F(1, 2)]
    outer = [F(4, 3), F(-2), F(1), F(-1, 6)]
    di = [inner]
    do = [outer]
    for _ in range(3):
        di.append(derivative(di[-1]))
        do.append(derivative(do[-1]))
    for j in range(3):
        assert at(di[j], F(1)) == at(do[j], F(1))
        assert at(do[j], F(2)) == 0
    assert at(di[1], F(0)) == 0  # Even extension is C^2 at zero.
    assert at(di[0], F(0)) == F(2, 3)
    assert at(di[2], F(0)) == -2
    norms = {
        "B": 2*(integral(inner, F(0), F(1)) + integral(outer, F(1), F(2))),
        "B_prime": -2*(integral(di[1], F(0), F(1))
                       + integral(do[1], F(1), F(2))),
        "B_second": 2*(-integral(di[2], F(0), F(2, 3))
                        + integral(di[2], F(2, 3), F(1))
                        + integral(do[2], F(1), F(2))),
        "B_third": 2*(integral(di[3], F(0), F(1))
                       - integral(do[3], F(1), F(2))),
    }
    assert norms == {"B": F(1), "B_prime": F(4, 3),
                     "B_second": F(8, 3), "B_third": F(8)}
    positive_b0 = -2*integral(di[2], F(0), F(2, 3))
    negative_b0 = 2*(integral(di[2], F(2, 3), F(1))
                     + integral(do[2], F(1), F(2)))
    assert positive_b0 == negative_b0 == F(4, 3)
    # Outer -K mass has coefficients 1 - x/12, where x=b^2.
    outer_constant = 2*integral(do[2], F(1), F(2))
    outer_x = -2*integral(outer, F(1), F(2))
    assert (outer_constant, outer_x) == (F(1), F(-1, 12))
    x = F(1, 4)
    numerator = outer_constant + outer_x*x
    denominator = F(2) + F(2, 3)*x
    assert numerator == F(47, 48)
    assert denominator == F(13, 6)
    assert numerator / denominator == F(47, 104)
    # The numerator of the derivative of their ratio is exactly -5/6.
    derivative_numerator = F(-1, 12)*2 - F(2, 3)
    assert derivative_numerator == F(-5, 6) < 0
    # z in (0,1], x<=1/4: -K=z(1-x*z^2/6)>=23z/24>0.
    assert 1-F(1, 4)/6 == F(23, 24)
    result = {
        "status": "PASS",
        "scope": "Exact rational spline/constant checks plus an independently written ordinary analytic review; no numerical prime experiment.",
        "author_sha256": hashlib.sha256(AUTHOR.read_bytes()).hexdigest(),
        "author_bytes": AUTHOR.stat().st_size,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "spline_L1_norms": {k: str(v) for k, v in norms.items()},
        "full_positive_mass_b0": str(positive_b0),
        "full_negative_mass_b0": str(negative_b0),
        "outer_negative_mass_lower": str(numerator),
        "normalized_outer_negative_mass_lower": str(numerator/denominator),
        "ratio_derivative_numerator": str(derivative_numerator),
        "C2_junctions_and_support_endpoints": "PASS",
    }
    (HERE / "spline_review_receipt.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
