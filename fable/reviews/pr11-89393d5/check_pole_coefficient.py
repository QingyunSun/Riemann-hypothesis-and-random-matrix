"""Independent exact pole check; a small numerical sign diagnostic is secondary."""
from fractions import Fraction
from pathlib import Path
import json
import mpmath as mp


def main() -> None:
    # zeta'/zeta(1+eps) = -1/eps + analytic. Three derivatives give +6/eps^4.
    power, coefficient = -1, Fraction(-1)
    derivatives = []
    for _ in range(3):
        coefficient *= power
        power -= 1
        derivatives.append({"power": power, "coefficient": str(coefficient)})
    assert (power, coefficient) == (-4, 6)
    a = Fraction(16, 15) ** 2
    pi4 = coefficient * a
    m4 = a * a + pi4
    assert pi4 == 6 * a
    assert m4 == a * a + 6 * a
    assert m4 != 7 * a * a
    mp.mp.dps = 50
    probes = []
    for eps_string in (".001", ".0002", ".00005"):
        eps = mp.mpf(eps_string)
        value = eps**4 * mp.diff(lambda s: mp.zeta(s, derivative=1) / mp.zeta(s), 1 + eps, 3)
        assert abs(value - 6) < mp.mpf("1e-10")
        probes.append({"eps": eps_string, "correct_positive_probe": mp.nstr(value, 18),
                       "original_refuter_probe": mp.nstr(-value, 18)})
    result = {
        "status": "PASS",
        "scope": "Exact leading pole algebra, plus a numerical sign diagnostic; not a full arithmetic transfer proof",
        "successive_derivatives_of_minus_inverse_eps": derivatives,
        "a": str(a), "Pi4_leading": str(pi4), "m4_correct": str(m4),
        "m4_from_incorrect_proposer_Pi4": str(7 * a * a),
        "Pi4_formula": "6*a", "m4_formula": "a*a+6*a",
        "numeric_probes": probes,
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
