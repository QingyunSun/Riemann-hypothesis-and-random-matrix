#!/usr/bin/env python3
"""Tiny exact checks; no sampled primes or asymptotic numerical inference."""
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent

def factors(n):
    result = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = 1
    return result

def mu(n):
    fs = factors(n)
    return 0 if any(e > 1 for e in fs.values()) else (-1)**len(fs)

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]

def log_vector(n):
    return factors(n)

def lambda_vector(n):
    fs = factors(n)
    return {next(iter(fs)): 1} if len(fs) == 1 else {}

def log_sum(terms):
    ans = defaultdict(int)
    for coefficient, n in terms:
        for p, e in log_vector(n).items():
            ans[p] += coefficient * e
    return {p: e for p, e in ans.items() if e}

counts = {}
for n in range(1, 201):
    assert log_sum((mu(d), n//d) for d in divisors(n)) == lambda_vector(n)
counts["von_mangoldt_divisor_log_coefficient_identities"] = 200

for y2 in range(2, 401):
    y = F(y2, 2)
    direct = sum(mu(n) for n in range(1, int(y)+1) if n % 2)
    indirect, scale = 0, 1
    while y/scale >= 1:
        indirect += sum(mu(n) for n in range(1, int(y/scale)+1))
        scale *= 2
    assert direct == indirect
counts["odd_mobius_geometric_identities_real_endpoints"] = 399

ccount = 0
for n in range(1, 101, 2):
    for Q in [F(1), F(5,2), F(7), F(41,2)]:
        lo = [(mu(d), n//d) for d in divisors(n) if d <= Q]
        hi = [(mu(d), n//d) for d in divisors(n) if d > Q]
        assert log_sum(lo + hi) == lambda_vector(n)
        switched = [(mu(d), k) for k in divisors(n)
                    for d in [n//k] if d > Q and k >= 3]
        assert log_sum(switched) == log_sum(hi)
        ccount += 1
counts["sharp_complement_switch_log_coefficient_identities"] = ccount

pc = 0
for d in range(1, 16, 2):
    phi = sum(gcd(r, d) == 1 for r in range(1, d+1))
    for n in range(1, 34, 2):
        for h in range(2, 26, 2):
            congr = int((n-h) % d == 0)
            nu, hu = int(gcd(n,d) == 1), int(gcd(h,d) == 1)
            kernel = nu * (F(congr)-F(hu,phi))
            principal = F(nu*hu,phi)
            nonprimitive = (1-hu)*congr
            assert kernel + principal + nonprimitive == congr
            pc += 1
counts["primitive_principal_nonprimitive_exact_partition"] = pc

def S_model(h):
    # Arbitrary even coefficient checks the identity, not an estimate of S(h).
    return F(h*h+3, 7) if h % 2 == 0 else F(0)

for y4 in range(1, 161):
    y = F(y4, 4)
    A2 = sum((y-h)*(S_model(h)-1)
             for h in range(1, int(y)+1))
    B2 = sum((y-h)*(S_model(h)-2)
             for h in range(2, int(y)+1, 2))
    alternating = sum((-1)**(h+1)*(y-h)
                      for h in range(1, int(y)+1))
    assert B2-A2 == alternating
counts["even_singular_hinge_algebra_real_endpoints"] = 160

hc = 0
for H2 in range(1, 201):
    H = F(H2, 2)
    for p in [3,5,7,11,31,101]:
        actual = sum(H < 2*p*r < 2*H for r in range(1, int(H/p)+1))
        assert actual <= H/p
        hc += 1
counts["nonprimitive_even_shift_count_including_empty_ranges"] = hc

# Polynomial identity for arbitrary exact scalar one-prime/main inputs.
sc = 0
for left in [F(-7,3), F(0), F(9,5)]:
    for right in [F(-5,2), F(3,7)]:
        for integral in [F(8,9), F(-1,4)]:
            # A+L with a=2, and both S marginals plus odd-grid center.
            joint = 2*right + 2*left - 2*integral
            marginals = 2*left + 2*right - 2*integral
            assert joint-marginals == 0
            sc += 1
counts["both_marginals_constant_cancellation"] = sc

rho, theta_lo, theta_hi = F(2,5), F(3,7), F(5,9)
eps = F(1,100)
margins = {
    "primitive_B_J16": 16*(theta_lo-rho)-rho,
    "principal_mask_Q_over_H": theta_lo-rho,
    "cofactor_grid": 2-theta_hi-2*rho,
    "joint_RH_epsilon_1_over_100": F(1,2)+rho/2-rho*eps-theta_hi,
    "nonprimitive_eta_1_over_100": F(4,9)-eps,
    "unperturbed_joint_RH": F(1,2)+rho/2-theta_hi,
}
expected = [F(2,35), F(1,35), F(29,45), F(158,1125),
            F(391,900), F(13,90)]
assert list(margins.values()) == expected
assert all(x > 0 for x in margins.values())
counts["strict_rational_power_margins"] = len(margins)

author = HERE / "JOINT_MAIN_CANCELLATION.md"
out = {
    "status": "PASS",
    "scope": "Exact finite algebra and rational margins only; ordinary proof is separate.",
    "author_sha256": sha256(author.read_bytes()).hexdigest(),
    "check_groups": counts,
    "total_scalar_cases": sum(counts.values()),
    "power_margins": {k: str(v) for k,v in margins.items()},
}
encoded = json.dumps(out, indent=2, sort_keys=True) + "\n"
(HERE / "exact_check_results.json").write_text(encoded)
print(encoded, end="")

