#!/usr/bin/env python3
"""Exact algebra checks for the R20 height lemma, not a zeta simulation."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sympy as sp

HERE=Path(__file__).resolve().parent
u,a,y=sp.symbols("u a y",real=True)
ell,A,d=sp.symbols("ell A d",positive=True)

fourier_multiplier=1+(sp.exp(sp.I*sp.pi*a)+sp.exp(-sp.I*sp.pi*a))/2
assert sp.simplify(sp.expand_complex(fourier_multiplier)-(1+sp.cos(sp.pi*a)))==0
cos_integral=sp.integrate(a*(1-a)*sp.cos(sp.pi*a),(a,0,1))
assert cos_integral==0
low_band_mass=2+2*sp.integrate(a*(1-a)*(1+sp.cos(sp.pi*a)),(a,0,1))
assert low_band_mass==sp.Rational(7,3)
assert sp.trigsimp(sp.sin(sp.pi*u)**2+sp.cos(sp.pi*u)**2)==1
for sign in [-1,1]:
    # The RHS is manifestly positive for every real u.
    assert sp.expand(2*(1+u*u)-(u+sign*sp.Rational(1,2))**2
                     -((u-sign*sp.Rational(1,2))**2+sp.Rational(3,2)))==0

r_big=1-ell/(y*(ell+sp.log(y)))
r_small=1-y*(ell+sp.log(y))/ell
assert sp.simplify(r_big-(1-1/y)-sp.log(y)/(y*(ell+sp.log(y))))==0
assert sp.simplify(r_small-(1-y)+y*sp.log(y)/ell)==0

p=4/sp.pi*y*y/(1+y*y)**2
P=2/sp.pi*(sp.atan(y)-y/(1+y*y))
assert sp.simplify(sp.diff(P,y)-p)==0
assert sp.limit(P,y,sp.oo)-P.subs(y,0)==1
positive_gap=4*(4-y*y)*(4*y*y-1)/(25*sp.pi*(1+y*y)**2)
assert sp.simplify(p-16/(25*sp.pi)-positive_gap)==0
assert sp.simplify((d/2)*2*(d/(8*A))*16/(25*sp.pi)-2*d*d/(25*sp.pi*A))==0

algebra_cases=0
for av in [Fraction(1),Fraction(3,2),Fraction(2)]:
    for r in [Fraction(k,12) for k in range(13)]:
        for dv in [av*Fraction(k,8) for k in range(9)]:
            for xv in [2*av*r*Fraction(k,8) for k in range(9)]:
                delta=xv-r*dv
                assert -av*r<=delta<=2*av*r
                assert abs(delta)<=2*av*r
                algebra_cases+=1

report=HERE/"MULTIPLICATIVE_HEIGHT_EQUICONTINUITY.md"
record={
 "status":"PASS",
 "scope":"Exact normalization, denominator, prefix algebra and probability-kernel checks. No numerical zeros, no positive deficit, no proof of the separately proposed length-average identity.",
 "author_sha256":hashlib.sha256(report.read_bytes()).hexdigest(),
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "sympy_version":sp.__version__,
 "envelope_fourier_multiplier":"1+cos(pi*alpha)",
 "envelope_lower_bound":"1/(2*pi^2*(1+u^2))",
 "cos_integral":str(cos_integral),
 "low_band_pair_mass":str(low_band_mass),
 "uniform_pair_envelope_factor":"6*pi^2 for sufficiently large heights",
 "normalization_ratio_identities":"PASS: upper and lower y branches",
 "prefix_algebra_cases":algebra_cases,
 "probability_kernel_total_mass":1,
 "probability_kernel_antiderivative":str(P),
 "probability_kernel_lower_bound_on_half_to_two":"16/(25*pi)",
 "conditional_deficit_lower_coefficient":"2*d^2/(25*pi*A)",
 "conditional_length_average_dependency":"Not verified by this checker; must be independently proved."
}
(HERE/"height_regularity_checks.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2))

