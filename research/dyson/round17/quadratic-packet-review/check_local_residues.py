"""Independent exact Laurent and compact-kernel normalization checks.

This does not check the Riemann hypothesis or a contour estimate numerically.
Output is saved only beside this independent review script.
"""
from pathlib import Path
import json
import sympy as s

u, a, W, S0, S1, h0, h1 = s.symbols("u a W S0 S1 h0 h1", nonzero=True)
H = 1 / (s.I * u) + h0 + h1 * s.I * u
Hp = -1 / (s.I * u) ** 2 + h1
weight = ((u - s.I * a) ** 2 + a * a) ** 2 * (S0 + S1 * u) / W**4
weight_sigma = -4 * a * ((u - s.I * a) ** 2 + a * a) * (S0 + S1 * u) / W**4
res = {
    "H_squared_weight": s.residue(H**2 * weight, u, 0),
    "two_H_Hprime_weight": s.residue(2 * H * Hp * weight, u, 0),
    "H_squared_sigma_weight": s.residue(H**2 * weight_sigma, u, 0),
}
assert res["H_squared_weight"] == 0
assert s.simplify(res["two_H_Hprime_weight"] - 8 * s.I * S0 * a**2 / W**4) == 0
assert s.simplify(res["H_squared_sigma_weight"] + 8 * s.I * S0 * a**2 / W**4) == 0

# B6(z)=(1/5!) sum_k (-1)^k C(6,k)(z+3-k)_+^5.
# At zero, all derivatives through order four are continuous.
central = {
    order: sum((-1) ** k * s.binomial(6, k) * (3 - k) ** (5 - order)
               / s.factorial(5 - order) for k in range(3))
    for order in (0, 2, 4)
}
assert central == {0: s.Rational(11, 20), 2: -1, 4: 6}
record = {
    "status": "PASS",
    "scope": "Exact local Laurent identities and B6 central derivatives only; not a zeta-data or contour-proof computation.",
    "t_residues": {key: str(value) for key, value in res.items()},
    "real_to_lower_line_residue_factor": "-2*pi*I",
    "B6_central_even_derivatives": {str(key): str(value) for key, value in central.items()},
}
Path(__file__).with_suffix(".json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps(record, sort_keys=True))
