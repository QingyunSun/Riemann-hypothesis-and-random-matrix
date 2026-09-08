"""Finite exact identities only; no prime scan or asymptotic certification."""

import json
from pathlib import Path

import sympy as s

z = s.symbols("z")
fourier_cases = 0
parity_cases = 0
ramanujan_bound_cases = 0
totient_cases = 0


def ramanujan(q, l):
    return sum(a * s.mobius(q // a) for a in s.divisors(s.gcd(q, l)))


for d in (1, 3, 5, 9, 15):
    q = 2 * d
    phi = s.totient(q)
    period = [s.Rational(q, phi) * int(s.gcd(n, q) == 1) - 2 * (n % 2) for n in range(q)]
    assert sum(period) == 0
    cyclotomic = s.Poly(s.cyclotomic_poly(q, z), z)
    for l in range(q):
        expected = ramanujan(q, l) / phi - (s.Integer(-1) ** (l // d) if l % d == 0 else 0)
        polynomial = sum(period[n] * z ** ((-l * n) % q) / q for n in range(q)) - expected
        assert s.rem(s.Poly(polynomial, z), cyclotomic).is_zero
        fourier_cases += 1
        if l % d == 0:
            assert expected == 0
            parity_cases += 1
    for l in range(-3 * q, 3 * q + 1):
        assert abs(ramanujan(q, l)) <= s.gcd(q, l)
        ramanujan_bound_cases += 1

for n in range(1, 51):
    assert s.Rational(n, s.totient(n)) == sum(s.mobius(a) ** 2 / s.totient(a) for a in s.divisors(n))
    totient_cases += 1

frequencies = range(-3, 4)
J = {1, 2}
negative_J = {-t for t in J}
f = {t: s.Integer(t + 4) + s.I * (2 * t - 1) for t in frequencies}
g = {t: s.Integer(t * t + 2) + s.I * (3 - t) for t in frequencies}
left = sum(f[t] * g[-t] for t in J)
right = sum(f[t] * g[-t] for t in frequencies if -t in negative_J)
wrong_same_sign = sum(f[t] * g[-t] for t in frequencies if -t in J)
assert s.simplify(left - right) == 0
assert s.simplify(left - wrong_same_sign) != 0

result = {
    "status": "passed",
    "scope": "Exact finite Fourier, arithmetic-identity and transpose-sign checks only; no asymptotic proof certification or prime calculation.",
    "fourier_cases": fourier_cases,
    "cancelled_parity_modes": parity_cases,
    "ramanujan_bound_cases": ramanujan_bound_cases,
    "totient_identity_cases": totient_cases,
    "transpose_identity_cases": 1,
    "incorrect_same_sign_control_rejected": True,
}
serialized = json.dumps(result, indent=2, sort_keys=True) + "\n"
Path(__file__).with_name("stationary_challenge_ramanujan_checks.json").write_text(serialized)
print(serialized, end="")
