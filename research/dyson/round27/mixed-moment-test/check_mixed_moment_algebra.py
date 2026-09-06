"""Exact scalar checks only; no prime-height or parameter scans."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s


def main():
    u, v, a, R, m = s.symbols("u v a R m", real=True)
    lp, lq, lr = s.symbols("log_p log_q log_r", real=True)
    checks = {
        "polarization": s.expand(2*a*u*v-a*a*v*v+(u-a*v)**2-u*u) == 0,
        "zero_diagonal_negative_determinant": s.det(s.Matrix([[0, 1], [1, 0]])) == -1,
        "cutoff_log_identity": s.expand((m-R)+R-m) == 0,
        "positive_three_prime_witness": s.expand(-((lp+lq+lr)-(lq+lr)-(lp+lr))-lr) == 0,
        "negative_semiprime_witness": s.expand(-((lp+lr)-lr)+lp) == 0,
        "prime_power_remainder": s.expand(lp-a*lp-(1-a)*lp) == 0,
        "real_cutoff_between_five_and_six": 5**3 < 150 < 6**3,
        "uniform_Q_upper_exponent": F(2, 3)*(1-1/F(9, 4)) == F(10, 27) < F(2, 5),
        "natural_pair_CRT_lower_exponent": F(4, 3)*F(7, 4)-F(7, 3) == 0,
        "natural_pair_CRT_upper_exponent": F(4, 3)*F(9, 4)-F(7, 3) == F(2, 3),
        "natural_mixed_tail_lower_exponent": (F(7, 4)-1)/3 == F(1, 4),
        "natural_mixed_tail_upper_exponent": (F(9, 4)-1)/3 == F(5, 12),
        "triple_mixed_range_misses_natural_packets": F(3, 8) < F(3, 7),
        "smooth_pure_packet_Y_exponent": 1+6*F(2, 3) == 5,
        "smooth_pure_global_T_exponent": 2*F(9, 4)-5 == F(-1, 2),
    }
    result = {"status": "PASS" if all(checks.values()) else "FAIL", "scope": "Fifteen exact scalar and formal-log checks; no asymptotic correlation certification.", "checks": checks}
    payload = json.dumps(result, indent=2, sort_keys=True)+"\n"
    Path(__file__).with_name("mixed_moment_checks.json").write_text(payload)
    print(payload, end="")
    assert all(checks.values())


if __name__ == "__main__":
    main()
