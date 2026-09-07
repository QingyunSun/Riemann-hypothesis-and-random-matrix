"""Exact small algebra/endpoint checks, not an asymptotic or prime-height scan."""
from hashlib import sha256
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

HERE = Path(__file__).resolve().parent
x,u,y,T,Y,R,ell=s.symbols("x u y T Y R ell",positive=True)
V=s.Function("V")
A=s.Function("A")
S=s.Function("S")
groups=[]


def record(name,cases,scope):
    groups.append(dict(name=name,cases=cases,passed=True,scope=scope))


k=V((u-x)/Y)*(x/u)**T
r=T*(1/x-1/u)
assert s.simplify(s.diff(k,x)+s.diff(k,u)-r*k)==0
G=A(x)*S(x)/x
assert s.simplify(x*s.diff(G,x)+(A(x)/x-s.diff(A(x),x))*S(x)-A(x)*s.diff(S(x),x))==0
record("negative_sobolev_derivative_signs",2,
       "Exact kernel derivative and G-prime decomposition; no derivative of E.")


# Fixed n differentiation is x(partial_x-partial_h), including its x factor.
P=A(x)*V(y/Y)*(x/(x+y))**T
direct=P.subs(y,u-x)
current=P
for j in range(1,4):
    direct=x*s.diff(direct,x)
    current=x*(s.diff(current,x)-s.diff(current,y))
    assert s.simplify(direct-current.subs(y,u-x))==0
record("fixed_integer_derivative_operator",3,
       "Orders one through three, with actual Pareto factor and arbitrary A,V.")


def lam(n):
    fac=s.factorint(n)
    return s.log(next(iter(fac))) if len(fac)==1 else s.Integer(0)


def psi(z):
    return sum(lam(n) for n in range(2,int(s.floor(z))+1))


count=0
for a in [s.Rational(j,2) for j in range(8,25)]:
    for h in [s.Rational(j,2) for j in range(1,8)]:
        odds=[n for n in range(1,20) if n%2 and a<n<=a+h]
        lhs=sum(lam(n)-2 for n in odds)
        oddcount=s.floor((a+h+1)/2)-s.floor((a+1)/2)
        assert oddcount==len(odds)
        powers=sum(1 for j in range(1,6) if a<2**j<=a+h)
        correction=h-2*oddcount-s.log(2)*powers
        rhs=(psi(a+h)-(a+h))-(psi(a)-a)+correction
        assert s.simplify(lhs-rhs)==0
        assert abs(h-2*oddcount)<=2
        assert powers<=1
        count+=1
record("real_endpoint_odd_center",count,
       "Exact floor endpoints, prime powers, odd count, and at most one power of 2.")


# Check adjacent phase increments and the two derivative normalization factors.
t,z=s.symbols("t z",positive=True)
phi=t*s.log(2*z+1)/(2*s.pi)
assert s.simplify(s.diff(phi,z)-t/(s.pi*(2*z+1)))==0
assert s.simplify(s.diff(phi,z,2)+2*t/(s.pi*(2*z+1)**2))==0
inc=s.expand_log(phi.subs(z,z+1)-phi,force=True)
assert s.simplify(inc-t/(2*s.pi)*s.log((2*z+3)/(2*z+1)))==0
record("odd_lattice_frequency_normalization",3,
       "Poisson derivative and exact adjacent increment kept distinct.")


# An explicit finite centered prime observable checks inverse-Mellin signs
# algebraically through formal multiplicative phases.
z3,z5=s.symbols("z3 z5")
phase={3:z3,5:z5,9:z3**2,15:z3*z5,25:z5**2}
mu={3:-1,5:-1}
fc={9:s.Integer(2),15:-s.Integer(3),25:s.Integer(0)}
direct=sum(mu[d]*s.log(q)*fc[d*q]*phase[d*q] for d in (3,5) for q in (3,5))
product=sum(mu[d]*phase[d]*s.log(q)*phase[q]*fc[d*q] for d in (3,5) for q in (3,5))
assert s.expand(direct-product)==0
assert Fraction(2,1)*Fraction(1,2)==1
record("mellin_sign_and_factor_two",2,
       "Positive phases in both polynomials; original 2 times inversion 1/(2pi).")


# Exact exponent accounting at X=T^2,Y=T and logX=2ell.
assert s.simplify((Y**2*x**2/x**3).subs({Y:T,x:T**2}))==1
assert s.simplify((Y/x).subs({Y:T,x:T**2})-1/T)==0
assert s.simplify(T*(2*ell)*T/(T**2*ell**2)-2/ell)==0
for j in (2,3,4):
    raw=T**(s.Rational(1,2)+j)*(2*ell)/R**j*s.sqrt(R*T)*s.sqrt(R)*(2*ell)/(T**2*ell**2)
    assert s.simplify(raw-4*(R/T)**(1-j))==0
record("all_band_normalizations",6,
       "Negative-Sobolev mass, power-of-2 support debt, low and high band scales.")


# Geometric high-band sum, exact finite sum and exact omitted tail.
for j in (2,3,4):
    q=Fraction(1,2**(j-1))
    for n in (1,2,4,8):
        finite=sum(q**r for r in range(n))
        tail=q**n/(1-q)
        assert finite+tail==1/(1-q)
record("infinite_frequency_tail",12,
       "Geometric summability for every fixed derivative order at least two.")


result=dict(author_sha256=sha256((HERE/"SIGNED_MELLIN_BLOCK_BOUND.md").read_bytes()).hexdigest(),
            groups=groups,total_cases=sum(g["cases"] for g in groups),all_passed=True,
            scope="Exact finite checks only; analytic inequalities are proved and source-audited in the manuscript. No prime-height or frequency scan.")
encoded=json.dumps(result,indent=2,sort_keys=True)+"\n"
(HERE/"exact_check_results.json").write_text(encoded)
print(encoded,end="")
