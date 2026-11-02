#!/usr/bin/env python3
"""Exact algebra for the singleton renormalization; no prime or zero samples."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent
def pin(p):
    b=p.read_bytes()
    return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}

def main():
    checks=[]
    def zero(name,expr):
        assert s.simplify(expr)==0,name
        checks.append({"name":name,"status":"PASS"})

    lm,ln,S=s.symbols("Lambda_m Lambda_n S")
    old=(lm-1)*(ln-1)-(S-1)
    q=lm*ln-S*(lm+ln-1)
    zero("exact old minus new singleton identity",old-q-(S-1)*(lm+ln-2))

    m,n,h,ell=s.symbols("m n h ell",positive=True)
    I=s.Function("I")
    W=s.Function("W")
    for T in (4,5,9):
        zero("backward power cancellation T="+str(T),
             T*I(m)/(m**T*ell**2)*(m/n)**T-T*I(m)/(n**T*ell**2))
        fprime=-T/(n**T*ell**2)*W(n-h)*(n-h)**(T-2)
        expected=T/(n**T*ell**2)*(s.diff(W(m),m).subs(m,n-h)*(n-h)**(T-2)
                  +(T-2)*W(n-h)*(n-h)**(T-3))
        zero("exact signed backward second derivative T="+str(T),
             s.diff(fprime,h)-expected)

    t=s.symbols("t")
    beta=[]
    for T in (4,5,9):
        density=s.expand((T-2)*(T-1)*t*(1-t)**(T-3))
        mass=s.integrate(density,(t,0,1))
        mean=s.integrate(T*t*density,(t,0,1))
        assert mass==1 and mean==2
        poly=s.Poly(density,t)
        log_t=sum(-c/s.Rational((k+1)**2) for (k,),c in poly.terms())
        zero("beta log moment T="+str(T),log_t-(1-s.harmonic(T-1)))
        beta.append({"T":T,"mass":str(mass),"mean_scaled_u":str(mean),
                     "log_u_expectation":str(s.log(T)+log_t)})
    checks.append({"name":"beta probability mass and scaled mean in three cases","status":"PASS"})

    # Exact compact polynomial example. W and W' vanish at both endpoints.
    x=s.symbols("x")
    Wpoly=(x-1)**3*(2-x)**3
    T=4
    n0=s.Rational(5,2)
    Ipoly=s.integrate(s.expand(Wpoly*x**(T-2)),x)
    b0=T/n0**T*(Ipoly.subs(x,2)-Ipoly.subs(x,1))
    fsecond=T/n0**T*(s.diff(Wpoly,x)*x**(T-2)+(T-2)*Wpoly*x**(T-3))
    hinge=s.integrate(s.expand((n0-x)*fsecond),(x,1,2))
    zero("compact signed derivative first-moment identity",hinge-b0)

    y,Tr=s.symbols("y Tr",positive=True)
    tail=y**(2-Tr)*(s.log(2*y)**2/(Tr-2)
         +2*s.log(2*y)/(Tr-2)**2+2/(Tr-2)**3)
    zero("exact backward tail antiderivative",s.diff(tail,y)+y**(1-Tr)*s.log(2*y)**2)
    assert s.Rational(7,4)/2==s.Rational(7,8)
    checks.append({"name":"RH lower endpoint exponent 7/8","status":"PASS"})

    result={"status":"PASS","scope":"Exact residual algebra, signed derivatives, beta moments, compact hinge identity and tail primitive only; no strict arithmetic bound.",
            "author":pin(HERE/"SINGLETON_RENORMALIZATION.md"),
            "checker":pin(Path(__file__)),"sympy_version":s.__version__,
            "number_of_checks":len(checks),"checks":checks,"beta_moments":beta}
    data=json.dumps(result,indent=2,sort_keys=True)+"\n"
    (HERE/"singleton_renormalization_checks.json").write_text(data)
    print(data,end="")

if __name__=="__main__":
    main()

