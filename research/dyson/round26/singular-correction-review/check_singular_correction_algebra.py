"""Small exact symbolic checks; no prime or singular-series samples."""

from pathlib import Path
from hashlib import sha256
import json
import sympy as s

root = Path(__file__).resolve().parent
y, x = s.symbols('y x', positive=True)
T = s.symbols('T', positive=True)
B, M0, M1, ell, logY = s.symbols('B M0 M1 ell logY')
g = y**2/2-y*s.log(y)/2+B*y/2
assert s.simplify(s.diff(g,y,2)-(1-1/(2*y))) == 0
assert s.diff(B*y,y,2) == 0
tail_mass = x**(1-T)/(T-1)
tail_log = x**(1-T)*(s.log(x)/(T-1)+1/(T-1)**2)
assert s.simplify(s.diff(tail_mass,x)+x**(-T)) == 0
assert s.simplify(s.diff(tail_log,x)+x**(-T)*s.log(x)) == 0
mass = T/(T-1)*M0/ell
logmoment = T/(T-1)*(M1+M0)+T*M0/((T-1)**2*ell)
combined = logmoment-(ell+logY)*mass
expected = T/(T-1)*(M1-logY*M0/ell)+T*M0/((T-1)**2*ell)
assert s.simplify(combined-expected) == 0
assert s.Rational(2)-1 == 1
assert -1+s.Rational(1,2)*(-s.Rational(1,2)+s.Rational(1,8)) == -s.Rational(19,16)
assert s.Rational(7,4)*(-s.Rational(1,2)) == -s.Rational(7,8)
data = {
    'status':'PASS',
    'exact_checks':8,
    'scope':'Second derivative sign, linear-term cancellation, two endpoint moment primitives, exact moment combination, density factor and two rational decay exponents only.',
    'report_sha256':sha256((root/'REFINED_SINGULAR_CORRECTION.md').read_bytes()).hexdigest(),
    'values':{'hinge_second_derivative':str(s.diff(g,y,2)), 'total_prime_minus_lattice_factor':1, 'summed_transform_log_power_at_epsilon_1_8':'-19/16','RH_height_tail_power':'-7/8'},
}
encoded=json.dumps(data,indent=2,sort_keys=True)+'\n'
(root/'singular_correction_checks.json').write_text(encoded)
print(encoded,end='')
