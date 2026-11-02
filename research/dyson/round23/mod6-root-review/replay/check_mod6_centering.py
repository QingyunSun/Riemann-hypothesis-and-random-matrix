#!/usr/bin/env python3
"""Exact fixed-modulus local identities; no prime-height diagnostic or scan."""
from pathlib import Path
from math import gcd
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent

def pin(p):
    data=p.read_bytes()
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def chi3(n):return {0:0,1:1,2:-1}[int(n)%3]
def chi6(n):return {0:0,1:1,2:0,3:0,4:0,5:-1}[int(n)%6]
def g(d):
    factors=s.factorint(d)
    if any(v>1 for v in factors.values()):return s.Integer(0)
    return s.prod(s.Rational(1,int(p)-2) for p in factors)
def ss_over_2C2(h):
    if h%2:return s.Integer(0)
    return sum((g(int(d)) for d in s.divisors(h//2) if int(d)%2),s.Integer(0))

def main():
    lm,ln,S=s.symbols('Lambda_m Lambda_n S_h')
    rows=[];baseline=[]
    for h in range(6):
        nu=sum(gcd(a*(a+h),6)==1 for a in range(6))
        assert nu==(0 if h%2 else 2 if h==0 else 1)
        baseline_sum=s.Integer(0)
        for m in range(6):
            n=(m+h)%6
            A=int(gcd(m*n,6)==1)
            r=s.Rational(6*A,nu) if nu else s.Integer(0)
            Sh=S if h%2==0 else s.Integer(0)
            d=Sh*(int(h==2)-int(h==4))
            left=Sh*(1-r/3)
            first=chi6(m)*d+Sh*int(gcd(m,6)>1)
            second=-chi6(n)*d+Sh*int(gcd(n,6)>1)
            assert s.expand(left-first)==0
            assert s.expand(left-second)==0
            q2=lm*ln-Sh*(lm+ln-2*(m%2))
            q6=lm*ln-Sh*r*((lm+ln)/3-1)
            decomp=d*(chi6(m)*lm-chi6(n)*ln)+Sh*(lm*int(gcd(m,6)>1)+ln*int(gcd(n,6)>1))+Sh*(r-2*(m%2))
            assert s.expand(q6-q2-decomp)==0
            if not A:assert s.expand(q6-lm*ln)==0
            if h%2==0:baseline_sum+=r-2*(m%2)
            rows.append({'m_mod6':m,'h_mod6':h,'n_mod6':n,'nu':nu,'admissible':A,'r6':str(r),'q6':str(s.expand(q6)),'difference_decomposition':'PASS'})
        if h%2==0:
            assert baseline_sum==0
            baseline.append({'h_mod6':h,'period_sum':str(baseline_sum)})
    divisor_cases=[]
    for Y in (s.Rational(0),s.Rational(1),s.Rational(3,2),s.Rational(2),s.Rational(5),s.Rational(19,2),s.Rational(18),s.Rational(25)):
        direct=sum((ss_over_2C2(h)*(int(h%6==2)-int(h%6==4)) for h in range(1,int(s.floor(Y))+1)),s.Integer(0))
        via_divisors=s.Integer(0)
        abs_bound=s.Integer(0)
        for d in range(1,int(s.floor(Y/2))+1):
            if gcd(d,6)>1:continue
            inner=sum(chi3(j) for j in range(1,int(s.floor(Y/(2*d)))+1))
            assert abs(inner)<=1
            via_divisors+=g(d)*chi3(d)*inner
            abs_bound+=g(d)
        assert s.simplify(direct-via_divisors)==0
        assert abs(direct)<=abs_bound
        divisor_cases.append({'Y':str(Y),'D_over_2C2':str(direct),'positive_divisor_majorant':str(abs_bound)})

    x,h,n,ell=s.symbols('x h n ell',positive=True)
    v=s.symbols('v',nonnegative=True)
    W=s.Function('W')
    derivatives=[]
    for T in (4,5,8):
        fk=T/x*(1+h/x)**(-T-1)
        expected=T/x**2*(1+h/x)**(-T-2)*(T*h/x-1)
        assert s.simplify(s.diff(fk,x)-expected)==0
        integrand=T/n**T/ell**2*W(n-h)*(n-h)**(T-2)
        back=T/n**T/ell**2*(s.diff(W(x),x).subs(x,n-h)*(n-h)**(T-2)+W(n-h)*(n-h)**(T-3)*(T*h/n-2))
        assert s.simplify(s.diff(integrand,n)-back)==0
        mass=s.integrate(T*(1+v)**(-T-2)*(T*v+1),(v,0,s.oo))
        log_majorant=s.integrate(T*v*(1+v)**(-T-2)*(T*v+1),(v,0,s.oo))
        back_mean=s.integrate((T-2)*(1-v)**(T-3)*T*v,(v,0,1))
        assert mass==s.Rational(2*T,T+1)
        assert log_majorant==s.Rational(2*T,(T-1)*(T+1))+s.Rational(1,T+1)
        assert back_mean==s.Rational(T,T-1)
        derivatives.append({'T':T,'forward_derivative_identity':'PASS','backward_combined_derivative_identity':'PASS','forward_absolute_mass':str(mass),'forward_log_majorant':str(log_majorant),'backward_scaled_beta_mean':str(back_mean)})
    out={'status':'PASS','scope':'36 exact residue identities, fixed finite divisor sums and symbolic kernel derivatives; not prime data or an asymptotic estimate.',
         'residue_cases':rows,'baseline_period_sums':baseline,'divisor_prefix_cases':divisor_cases,'derivative_cases':derivatives,
         'prime_height_runs':False,'modulus':6,'report':pin(HERE/'FIXED_MOD6_CENTERING.md'),'checker':pin(Path(__file__)),'sympy_version':s.__version__}
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    (HERE/'mod6_centering_checks.json').write_text(text)
    print(text,end='')

if __name__=='__main__':main()
