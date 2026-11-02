"""Exact scalar checks only; analytic localization is an ordinary proof."""
from pathlib import Path
import hashlib,json
import sympy as s
T=s.symbols('T',positive=True)
xi,u,v,t=s.symbols('xi u v t',real=True)
a=T-s.Rational(1,2)
raw=T/(T-1)+1-2*T*a/(a*a+xi*xi)
final=(2*T-1)/(T-1)*(xi*xi+s.Rational(1,4))/(a*a+xi*xi)
assert s.factor(raw-final)==0
assert s.expand(a*a-T*(T-1))==s.Rational(1,4)
# These Laplace primitives are valid on the separately stated T>1 range.
primitives=[-T*s.exp(-(T-1)*u)/(T-1),-s.exp(-T*u)]
assert s.simplify(s.diff(primitives[0],u)-T*s.exp(-(T-1)*u))==0
assert s.simplify(s.diff(primitives[1],u)-T*s.exp(-T*u))==0
cos_primitive=T*s.exp(-a*u)*(-a*s.cos(xi*u)+xi*s.sin(xi*u))/(a*a+xi*xi)
assert s.simplify(s.diff(cos_primitive,u)-T*s.exp(-a*u)*s.cos(xi*u))==0
heat_primitive=-(xi*xi+s.Rational(1,4))*s.exp(-(a*a+xi*xi)*t)/(a*a+xi*xi)
assert s.simplify(s.diff(heat_primitive,t)-(xi*xi+s.Rational(1,4))*s.exp(-(a*a+xi*xi)*t))==0
M,w,dw=s.symbols('M w dw',positive=True)
h=-dw/M
assert s.expand(w+h*dw+M*h*h/2)==w-dw*dw/(2*M)
b,L=s.symbols('b L',positive=True)
assert s.expand(u*u*(1+b*L+u)**4-sum(s.binomial(4,k)*(1+b*L)**(4-k)*u**(k+2) for k in range(5)))==0
checks={'multiplier_difference':'0','mass_shift_difference':'1/4','two_real_laplace_primitives':'PASS','cosine_laplace_primitive':'PASS','heat_resolvent_primitive':'PASS','square_root_taylor_bound':'PASS','fourth_power_moment_expansion':'PASS','scalar_assertions':8}
report=Path(__file__).with_name('LOCALIZED_MELLIN_HEAT_ENERGY.md')
out={'status':'PASS','scope':'Eight exact scalar assertions, not analytic uniformity or a numerical arithmetic bound.','sympy_version':s.__version__,'report_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks}
text=json.dumps(out,indent=2,sort_keys=True)+'\n'
Path(__file__).with_name('heat_multiplier_checks.json').write_text(text)
print(text,end='')
