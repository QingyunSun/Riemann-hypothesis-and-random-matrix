"""Eight exact scalar checks only; no prime data, parameter sweep, or numerical integration."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

root = Path(__file__).resolve().parent
rho, lo, hi = F(523, 1000), F(11, 5), F(9, 4)
checks = {
    "small_cofactor_exponent": (1-rho, F(477, 1000)),
    "physical_shift_over_cofactor_gap": ((1-1/lo)-(1-rho), F(753, 11000)),
    "strong_bad_row_power": (1/hi-F(1, 100), F(391, 900)),
    "coarse_bad_row_power": (F(2, 3)-(1-1/hi)-F(1, 100), F(91, 900)),
    "RH_norm_lower_power": ((1-1/lo)/2, F(3, 11)),
    "RH_norm_upper_power": ((1-1/hi)/2, F(5, 18)),
    "relative_RH_lower_power": (F(1, 2)-1/lo, F(1, 22)),
    "relative_RH_upper_power": (F(1, 2)-1/hi, F(1, 18)),
}
for actual, expected in checks.values():
    assert actual == expected
report = root / "SMALL_COFACTOR_CENTERED_TARGET.md"
data = {
    "status": "PASS",
    "scope": "Eight exact exponent identities only; ordinary proofs require independent review.",
    "report_sha256": sha256(report.read_bytes()).hexdigest(),
    "checks": [{"name": name, "value": str(actual), "status": "PASS"}
               for name, (actual, _) in checks.items()],
}
encoded = json.dumps(data, indent=2, sort_keys=True) + "\n"
(root / "exact_constant_checks.json").write_text(encoded)
print(encoded, end="")

