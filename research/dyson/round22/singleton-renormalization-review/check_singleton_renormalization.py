#!/usr/bin/env python3
"""Small exact algebra checks; no prime scan or asymptotic numerical test."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent

def pin(path):
    data=path.read_bytes()
    return {"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}

def main():
    lm,ln,S=s.symbols('lambda_m lambda_n singular_series')
    old=(lm-1)*(ln-1)-(S-1)
    new=lm*ln-S*(lm+ln-1)
    correction=(S-1)*(lm+ln-2)
    assert s.expand(old-new-correction)==0
    assert s.expand(new.subs(S,0))==lm*ln

    v=s.symbols('v',real=True)
    beta=[]
    for T in (4,5,8,12):
        density=(T-1)*(T-2)*v*(1-v)**(T-3)
        mass=s.integrate(density,(v,0,1))
        mean=s.integrate(T*v*density,(v,0,1))
        envelope=s.integrate(T*(T-1)*v*(1-v)**(T-3),(v,0,1))
        assert mass==1 and mean==2
        assert envelope==s.Rational(T,T-2)
        beta.append({"T":T,"mass":str(mass),"scaled_mean":str(mean),
                     "absolute_envelope_mass":str(envelope)})
    assert s.integrate(-v*s.log(v),(v,0,1))==s.Rational(1,4)

    x,h=s.symbols('x h',real=True)
    A,B=s.Rational(2),s.Rational(5)
    W=(x-A)**2*(B-x)**2
    assert W.subs(x,A)==W.subs(x,B)==0
    assert s.diff(W,x).subs(x,A)==s.diff(W,x).subs(x,B)==0
    ell=s.Rational(3)
    sites=(A-s.Rational(1,10),A+s.Rational(1,10),A+1,
           B-s.Rational(1,10),B+1,2*B+1)
    cases=[]
    for T in (4,6):
        J=s.integrate(W*x**(T-2),x)
        J=s.expand(J-J.subs(x,A))
        full=s.simplify(J.subs(x,B))
        def primitive(y):
            if y<=A:return s.Integer(0)
            if y>=B:return full
            return s.simplify(J.subs(x,y))
        for n in sites:
            pref=s.Rational(T)/(ell**2*n**T)
            f=lambda t:s.simplify(pref*primitive(n-t))
            lo=max(s.Integer(0),n-B)
            hi=max(s.Integer(0),n-A)
            fpp=s.expand(pref*((s.diff(W,x)*x**(T-2)
                           +(T-2)*W*x**(T-3)).subs(x,n-h)))
            # On the actual derivative support this is d²/dh² of the exact primitive.
            assert s.expand(s.diff(pref*J.subs(x,n-h),h,2)-fpp)==0
            moment=s.integrate(h*fpp,(h,lo,hi)) if hi>lo else s.Integer(0)
            assert s.simplify(moment-f(0))==0
            direct=s.Integer(0);hinge=s.Integer(0);count=0
            for j in range(1,int(s.ceiling(n))+1):
                c=s.Rational((-1)**j*(j+1),j+2)
                direct+=c*f(j)
                lower=max(s.Integer(j),lo)
                if lower<hi:
                    hinge+=c*s.integrate((h-j)*fpp,(h,lower,hi))
                count+=1
            assert s.simplify(direct-hinge)==0
            cases.append({"T":T,"n":str(n),"derivative_support":[str(lo),str(hi)],
                          "b_n":str(f(0)),"h_fpp_integral":str(s.simplify(moment)),
                          "finite_signed_hinge_sum":str(s.simplify(direct)),
                          "checked_integer_h":count})
    out={"status":"PASS","scope":"Exact finite algebra/hinge checks only; uniform asymptotics are supplied by ordinary proof.",
         "coefficient_identity":str(s.expand(old-new-correction)),
         "odd_shift_q":str(s.expand(new.subs(S,0))),
         "beta_moments":beta,"small_u_log_moment":"1/4","uniform_log_moment_bound":"9/4",
         "compact_weight":"(x-2)^2(5-x)^2 on [2,5], zero elsewhere; C1 endpoints",
         "formal_ell":str(ell),"hinge_cases":cases,
         "report":pin(HERE/'INDEPENDENT_SINGLETON_DERIVATION.md'),
         "checker":pin(Path(__file__)),"new_prime_heights":False}
    data=json.dumps(out,indent=2,sort_keys=True)+'\n'
    (HERE/'singleton_renormalization_checks.json').write_text(data)
    print(data,end='')

if __name__=='__main__':main()
