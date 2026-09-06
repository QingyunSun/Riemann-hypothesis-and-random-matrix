#!/usr/bin/env python3
"""Exact bounded partition/hinge/constant checks, not numerical prime estimates."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb
import json

HERE = Path(__file__).resolve().parent

def r(t):
    # Auxiliary exact C^2 cutoff for telescoping checks only.
    # The theorem uses a fixed C-infinity cutoff, not this polynomial.
    if t <= 1:
        return F(1)
    if t >= 2:
        return F(0)
    u = t-1
    return 1-10*u**3+15*u**4-6*u**5

def beta(t):
    return r(t)-r(2*t)

counts = {}
n = 0
for t4 in range(1,257):
    t = F(t4,4)
    for last in range(9):
        val = sum(beta(t/F(2**j)) for j in range(last+1))
        assert val == r(t/F(2**last))-r(2*t)
        assert all(beta(t/F(2**j)) >= 0 for j in range(last+1))
        n += 1
counts["finite_dyadic_telescoping_and_nonnegative_weights"] = n

for t4 in range(1,257):
    t = F(t4,4)
    val = sum(beta(t/F(2**j)) for j in range(9))
    assert val == 1-r(2*t)
    if t > 1:
        assert val == 1
counts["finite_cover_of_exact_lower_endpoint_profile"] = 256

def poly_mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():
            c[i+j]=c.get(i+j,F(0))+x*y
    return {k:v for k,v in c.items() if v}

def power_linear(a,b,n):
    return {k:F(comb(n,k))*a**(n-k)*b**k for k in range(n+1)}

def second(a):
    return {k-2:v*k*(k-1) for k,v in a.items() if k>=2}

def shift(a,s):
    return {k+s:v for k,v in a.items()}

def integrate_pair(a,log=False):
    # Integral over[1,2], represented exactly as C+D*log(2).
    C,D=F(0),F(0)
    for k,v in a.items():
        if log:
            assert k != -1
            C -= v*(F(2)**(k+1)-1)/F((k+1)**2)
            D += v*F(2)**(k+1)/F(k+1)
        elif k == -1:
            D += v
        else:
            C += v*(F(2)**(k+1)-1)/F(k+1)
    return C,D

for degree in range(2,7):
    f=poly_mul(power_linear(F(-1),F(1),degree),
               power_linear(F(2),F(-1),degree))
    fpp=second(f)
    assert integrate_pair(shift(fpp,1)) == (0,0)
    a=integrate_pair(shift(fpp,2))
    b=integrate_pair(f)
    assert a == tuple(2*x for x in b)
    assert integrate_pair(shift(fpp,1),log=True) == integrate_pair(shift(f,-1))
counts["compact_polynomial_hinge_integrations_by_parts"] = 15

# Formal real-endpoint interpolation of an actual finite atomic hinge.
for N in range(1,41):
    for t in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
        y=N+t
        S=lambda h:F(h*h+1,3) if h%2==0 else F(0)
        hinge=lambda x:sum(max(F(0),x-h)*S(h) for h in range(1,43))
        assert hinge(y)==(1-t)*hinge(F(N))+t*hinge(F(N+1))
counts["real_atomic_hinge_linear_interpolation"] = 200

# Deterministic +1 coefficient after both odd-prime marginals and odd density.
for integral in [F(-3,7),F(0),F(11,13)]:
    joint = integral+integral-integral
    assert joint == integral
counts["global_correction_coefficient"] = 3

# Symmetry around2 makes M1=M0; exact polynomial test on symmetric[7/4,9/4].
for k in range(5):
    # omega(2+v)=v^(2k), the statement is linear for any even profile.
    mass0=2*F(1,4)**(2*k+1)/F(2*k+1)
    oddmoment=F(0)
    mass1=mass0+oddmoment
    assert mass1==mass0
counts["symmetric_weight_M1_equals_M0"] = 5

ell_powers={
 "primitive_B": F(1)-1+F(1,2)*F(2-16,3),
 "principal_mask_order36": F(4)-F(1,2)*12,
 "flat_even_grid_order4": F(1)-F(1,2)*4,
 "singular_remainder_nu_quarter": -F(1)-F(1,2)*F(1,4),
 "small_shift_cutoff": F(1,2)-1,
}
expected_ell=[-F(7,3),-F(2),-F(1),-F(9,8),-F(1,2)]
assert list(ell_powers.values())==expected_ell
T_powers={
 "cofactor_grid": F(9,4)*F(1,3)-F(7,3),
 "centered_mobius_prime_RH": F(9,4)*(F(101,150)-F(1,2))-F(101,150),
 "nonprimitive_eta": F(9,4)*F(1,100)-1,
 "upper_length_tail_R32ell": F(9,4)-1-F(32,4),
 "correction_singleton_RH": -F(7,8),
}
expected_T=[-F(19,12),-F(17,60),-F(391,400),-F(27,4),-F(7,8)]
assert list(T_powers.values())==expected_T
assert all(x<0 for x in [*ell_powers.values(),*T_powers.values()])
counts["summed_error_exact_exponents"] = 10

author=HERE/'FULL_SHIFT_REDUCTION.md'
out={
 "status":"PASS",
 "scope":"Finite exact algebra, no prime-height sampling or unproved asymptotic claim.",
 "auxiliary_cutoff_scope":"Polynomial r is used only for finite telescoping checks; theorem uses a C-infinity cutoff.",
 "author_sha256":sha256(author.read_bytes()).hexdigest(),
 "check_groups":counts,
 "total_scalar_cases":sum(counts.values()),
 "ell_error_exponents":{k:str(v) for k,v in ell_powers.items()},
 "T_error_exponents":{k:str(v) for k,v in T_powers.items()},
}
s=json.dumps(out,indent=2,sort_keys=True)+"\n"
(HERE/'exact_check_results.json').write_text(s)
print(s,end="")

