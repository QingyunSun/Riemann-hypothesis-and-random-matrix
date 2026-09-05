#!/usr/bin/env python3
"""Exact finite tests for the R19 norm/CRT argument; no asymptotic claim is tested."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import hashlib
import json

HERE = Path(__file__).resolve().parent
REPORT = HERE / "SHORT_RESIDUE_DISPERSION_TEST.md"

def mu(n):
    ans, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            ans = -ans
            if n % p == 0:
                return 0
        p += 1
    return -ans if n > 1 else ans

def units(q):
    return [a for a in range(q) if gcd(a,q) == 1]

records = []
for H in (3,4,5):
    qs = (30,35,42,55,70,77)
    norm = F(0)
    pair = F(0)
    e_norm = F(0)
    for q in qs:
        assert q > 2*H
        us = units(q)
        v = {a: F((a-H)*(2*H-a),H*H) if H < a < 2*H else F(0)
             for a in us}
        mean = sum(v.values()) / len(us)
        centered = {a:v[a]-mean for a in us}
        sq = sum(z*z for z in centered.values())
        raw = sum(z*z for z in v.values()) - sum(v.values())**2/len(us)
        assert sq == raw and sum(centered.values()) == 0
        # Arbitrary integral factor models a modulus multiplier; no floating log.
        weight = F(mu(q)*(1+q%4))
        e = {a:weight*centered[a] for a in us}
        norm += weight*weight*sq
        pair += weight*sum(v[a]*e[a] for a in us)
        e_norm += sum(z*z for z in e.values())
    assert pair == norm == e_norm
    records.append({"H":H,"norm":str(norm),"sharp_pairing":str(pair)})

crt_count = product_count = off_diagonal_examples = 0
for q,r1,r2 in ((3,5,7),(5,3,7)):
    l1,l2,L = q*r1,q*r2,q*r1*r2
    for n1 in units(l1)[:4]:
        for n2 in units(l2)[:4]:
            for h1 in [h for h in range(1,8) if gcd(h,l1)==1]:
                for h2 in [h for h in range(1,8) if gcd(h,l2)==1]:
                    compatible = (h1*n2-h2*n1)%q == 0
                    sols = [m for m in range(L)
                            if (m*n1-h1)%l1 == 0 and (m*n2-h2)%l2 == 0]
                    assert len(sols) == int(compatible)
                    crt_count += 1
                    if compatible and (n1-n2)%q != 0:
                        off_diagonal_examples += 1
                    for m in range(L):
                        i1 = F((m*n1-h1)%l1 == 0)
                        i2 = F((m*n2-h2)%l2 == 0)
                        u1 = F(gcd(m*n1,l1)==1 and gcd(h1,l1)==1)
                        u2 = F(gcd(m*n2,l2)==1 and gcd(h2,l2)==1)
                        ph1,ph2 = len(units(l1)),len(units(l2))
                        lhs=(i1-u1/ph1)*(i2-u2/ph2)
                        rhs=i1*i2-i1*u2/ph2-u1*i2/ph1+u1*u2/(ph1*ph2)
                        assert lhs == rhs
                        product_count += 1
assert off_diagonal_examples > 0

rho,kappa,ds=F(523,1000),F(343,346000),F(3,125)
s1=28*kappa
s2=rho-s1
assert s1 < F(1,10)-3*ds
assert s2 < F(4,10)+4*ds
n,q1,q2,q3=F(2,5),F(19,50),F(3,25),F(1,40)
margins=[n-q1,1-(2*n+q2+2*q3),
         2-(2*n+q1+4*q2+3*q3),2-(n+q1+5*q2+2*q3)]
assert margins == [F(1,50),F(3,100),F(53,200),F(57,100)]
assert q1+q2+q3 == F(21,40)
eps=F(1,1000)
assert all(a>b*eps for a,b in zip(margins,[1,8,15,15]))
theta=F(1-rho,2)
assert theta == F(477,2000)
assert F(1,6) < theta < F(2,7)
assert rho+F(1,2)+F(1,12) == F(3319,3000)
assert rho+F(1,2)+F(1,7) == F(8161,7000)
assert 1/(1-theta) == F(2000,1523)
payload={
 "status":"PASS",
 "scope":"Exact finite identities and rational exponent comparisons only; no new prime estimate, PNT-family threshold, localized variance, or zeta claim.",
 "author_sha256":hashlib.sha256(REPORT.read_bytes()).hexdigest(),
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "primitive_projection_sharpness":records,
 "crt_cases":crt_count,
 "retained_principal_product_cases":product_count,
 "compatible_cases_not_reducible_to_n1_equals_n2_mod_q":off_diagonal_examples,
 "maynard_III_allocation":{"delta":str(ds),"q1_exponent":str(s1),"q2_exponent":str(s2)},
 "maynard_II_margins":[str(a) for a in margins],
 "localized_variance_theta_threshold":str(theta),
 "old_compact_alpha_threshold":str(1/(1-theta))
}
(HERE/"shift_dispersion_checks.json").write_text(json.dumps(payload,indent=2)+"\n")
print(json.dumps(payload,indent=2))

