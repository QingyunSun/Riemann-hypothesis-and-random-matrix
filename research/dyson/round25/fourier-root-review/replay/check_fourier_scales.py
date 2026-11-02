"""Rational scale checks only; no prime data, frequency scan, or factorization."""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

root = Path(__file__).resolve().parent
checks = {
    "old_core_decay": (F(4, 9) - (1 - F(523, 1000)) / 2, F(3707, 18000)),
    "new_core_decay": (F(4, 9) - (1 - F(2, 5)) / 2, F(13, 90)),
    "new_K_over_H_min": (F(4, 9) - F(2, 5), F(2, 45)),
    "new_K_over_H_max": (F(4, 7) - F(2, 5), F(6, 35)),
    "old_H_over_K_min": (F(6, 11) - F(477, 1000), F(753, 11000)),
    "new_Selberg_min_power": ((1 - F(4, 7)) / 2, F(3, 14)),
    "new_Selberg_max_power": ((1 - F(4, 9)) / 2, F(5, 18)),
    "tail_power": (1 + (1 - 202) * F(1, 100), F(-101, 100)),
    "U_over_H_max_power": (F(1, 100) - (1 - F(4, 7)), F(-293, 700)),
}
for actual, expected in checks.values():
    assert actual == expected
data = {
    "status": "PASS",
    "scope": "Nine exact rational scale identities only; the analytic proof requires independent review.",
    "report_sha256": sha256((root / "ACTUAL_MOBIUS_FOURIER_TEST.md").read_bytes()).hexdigest(),
    "checks": [{"name": name, "value": str(value), "status": "PASS"}
               for name, (value, _) in checks.items()],
}
encoded = json.dumps(data, indent=2, sort_keys=True) + "\n"
(root / "fourier_scale_checks.json").write_text(encoded)
print(encoded, end="")
