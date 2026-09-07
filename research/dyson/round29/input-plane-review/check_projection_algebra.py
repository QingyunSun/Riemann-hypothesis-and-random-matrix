"""Small exact algebra checks only; no frequency scan or asymptotic certification."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json
import sympy as s

HERE=Path(__file__).resolve().parent
j,t,T=s.symbols('j t T',positive=True)
phase=t*s.log(2*j+1)/(2*s.pi)
checks=[]


def check(name,condition):
    assert condition,name
    checks.append(name)


check('odd_phase_first_derivative',s.simplify(s.diff(phase,j)-t/(s.pi*(2*j+1)))==0)
check('double_phase_second_derivative',s.simplify(s.diff(2*phase,j,2)+4*t/(s.pi*(2*j+1)**2))==0)
check('first_derivative_lower_using_pi_less_than_22_over_7',F(20,27)/F(22,7)>F(1,5))
check('first_derivative_upper_using_pi_greater_than_3',F(40,21)/3<F(4,5))
check('second_derivative_lower_factor',4/F(27,20)**2==F(1600,729))
check('second_derivative_upper_factor',8/F(21,20)**2==F(3200,441))
check('second_derivative_fixed_ratio',F(3200,441)/F(1600,729)==F(162,49))
N,u,v,z1,z2,lam=s.symbols('N u v z1 z2 lam',real=True)
G=s.Matrix([[N+u,v],[v,N-u]])/2
check('Gram_characteristic_polynomial',s.expand((G-lam*s.eye(2)).det()-((lam-N/2)**2-(u*u+v*v)/4))==0)
z=s.Matrix([z1,z2])
formula=2*((N-u)*z1*z1-2*v*z1*z2+(N+u)*z2*z2)/(N*N-u*u-v*v)
check('exact_inverse_projection_form',s.simplify((z.T*G.inv()*z)[0]-formula)==0)
check('target_power',F(-2)+F(1,2)+F(3,2)-F(1,2)==F(-1,2))
check('target_log_power',-2+1+1==0)
check('X_power_conversion',F(-1,2)/2==F(-1,4))
out={'status':'PASS','scope':'Exact derivative, Gram, range and normalization identities only; no finite threshold or asymptotic estimate is proved by these checks.',
     'sympy_version':s.__version__,'checks':checks,'total':len(checks),
     'coordinator_sha256':sha256((HERE/'COORDINATOR_LOG_VECTOR_MELLIN_INPUT_PROJECTION.md').read_bytes()).hexdigest(),
     'review_sha256':sha256((HERE/'INDEPENDENT_INPUT_PLANE_REVIEW.md').read_bytes()).hexdigest()}
encoded=json.dumps(out,indent=2,sort_keys=True)+'\n'
(HERE/'exact_projection_checks.json').write_text(encoded)
print(encoded,end='')
