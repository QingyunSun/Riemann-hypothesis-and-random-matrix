#!/usr/bin/env python3
"""Exact range and normalization checks for one bounded arithmetic audit."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
b, u, epsilon = s.symbols('b u epsilon', positive=True)
leading = s.integrate(u**-2, (u,b,2*b))
correction = s.integrate(u**-3, (u,b,2*b))
assert s.simplify(leading-1/(2*b)) == 0
assert s.simplify(correction-3/(8*b*b)) == 0
bound = s.simplify(b*b*(leading-(2-epsilon)*correction-1/(2*b)))
assert s.simplify(bound-(-s.Rational(3,4)+3*epsilon/8)) == 0
q, E1, E2 = s.symbols('q E1 E2', real=True)
exact = b*b*((1-q*q)*E1-(1-q**4)*E2-1/(2*b))
integrated = b*b*(E1-E2-1/(2*b)-q*q*E1+q**4*E2)
assert s.expand(exact-integrated) == 0
theta0 = F(2,15)
alpha0 = 1/(1-theta0)
assert alpha0 == F(15,13)
rows=[]
for shell_s in (F(1), F(2)):
    threshold=(1/theta0-1)*shell_s
    exponent= shell_s/(14+shell_s)
    assert threshold == F(13,2)*shell_s
    assert exponent < theta0
    rows.append({'shell_s':str(shell_s),'largest_b_even_at_epsilon_zero':str(threshold),
                 'fixed_b':14,'h_exponent_at_b14':str(exponent),
                 'below_Corollary_1_4_range':True})
out={'status':'PASS','scope':'Exact scalar implications and theorem-range checks only; no new arithmetic mixed-moment inequality, covariance estimate or parameter search',
     'integral_s_minus_2':str(leading),'integral_s_minus_3':str(correction),
     'conditional_C_lower_limit':str(bound),'hyperbolic_correction_identity':True,
     'Guth_Maynard_lower_h_exponent':'2/15 + fixed epsilon',
     'minimum_X_exponent_at_epsilon_zero':str(alpha0),'edge_range_checks':rows,
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'sympy_version':s.__version__}
(HERE/'check_edge_mixed_moment.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
