#!/usr/bin/env python3
"""Fixed symbolic checks of the note; no parameter search or zeta evaluation."""
from pathlib import Path
import hashlib
import json
import platform
import sympy as s

HERE = Path(__file__).resolve().parent
x, y, t, r, z = s.symbols("x y t r z", positive=True)
A = (x**2 - x**-2) / 2
B = (x - x**-1) / 2
a = 2 * (x**2 - 1) / (x**2 + 1)
b = 2 * (x - 1) / (x + 1)
kappa = 2 * b - a
checks = {}


def zero(name, expression):
    checks[name] = s.factor(expression) == 0
    assert checks[name], name


R = a / (1 + y) - 2 * b / (1 + 4 * y)
zero("R_plus_kappa_numerator", R + kappa - y * ((8*b-a) + (8*b-4*a)*y) / ((1+y)*(1+4*y)))
zero("kappa_in_t", kappa.subs(x, (1+t)/(1-t)) - 4*t**3/(1+t**2))
zero("negative_radius_in_t", (kappa/(4*a-2*b)).subs(x, (1+t)/(1-t)) - t**2/(3-t**2))
zero("a_cosh_square", a * (x+x**-1)**2/4 - A)
zero("b_cosh_half_square", b * (x+2+x**-1)/4 - B)
Iminus = (1-(1+r)*s.exp(-r))/r**2
Iplus = ((r-1)*s.exp(r)+1)/r**2
zero("Iminus_integral", s.integrate(z*s.exp(-r*z), (z,0,1)) - Iminus)
zero("Iplus_integral", s.integrate(z*s.exp(r*z), (z,0,1)) - Iplus)
closed = 0
endpoint = 0
for rr, c, d in [(2,A,a), (1,-B,-b)]:
    ep = x**rr
    u = c - d*(s.Rational(1,2) + 1/(4*ep))
    v = -d/(4*ep)
    im = (1-(1+rr)/ep)/rr**2
    ip = ((rr-1)*ep+1)/rr**2
    endpoint += u/ep + v*ep
    closed += u*(1+2*im) + v*(1+2*ip)
zero("ghat_at_plus_one", endpoint)
closed = s.factor(closed - s.Rational(4,3)*kappa - (A-B))
rational_bound = (x-1)*(3*x**6-6*x**5-17*x**4+28*x**3-35*x**2-6*x-15)/(12*x**2*(x+1)*(x**2+1))
zero("closed_bound_rational_form", closed-rational_bound)
zero("triangular_correction_coefficient", 1+2*s.integrate(z*(1-z),(z,0,1))-s.Rational(4,3))
q2 = s.symbols("q2", nonnegative=True)
zero("Palm_pair_normalization", (s.Rational(1,4)-q2)/s.Rational(1,2)-s.Rational(1,2)*(1-4*q2))
period_integral = s.integrate(z*s.exp(-r*z),(z,0,1)) + s.integrate((2-z)*s.exp(-r*z),(z,1,2))
zero("triangle_one_period_integral", period_integral-(1-s.exp(-r))**2/r**2)
V = lambda rr: 2*(x**rr-1)/(x**rr+1)/rr**2 + 2/(x**(2*rr)-1)
WA = x**2/4+s.Rational(5,4)/x**2-x-2/x+s.Rational(3,2)
zero("DPP_two_scale_closed_value", A*V(2)-B*V(1)-WA)

result = {
    "status": "PASS",
    "scope": "Exact algebra and fixed normalizations only; inequalities and Fourier pairing reviewed separately. No parameter scan, outward decimal enclosure, actual-zeta bound, or novelty claim.",
    "note_sha256": hashlib.sha256((HERE/"POSITIVITY_OBLIGATION_NOTE.md").read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "python": platform.python_version(),
    "sympy": s.__version__,
    "checks": checks,
    "exact_bound_with_x_equal_exp_1": str(rational_bound),
    "floating_bound_55_digits_not_enclosure": str(s.N(closed.subs(x,s.E),55)),
    "floating_DPP_W_55_digits_not_enclosure": str(s.N(WA.subs(x,s.E),55)),
}
(HERE/"minorant_symbolic_check.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
