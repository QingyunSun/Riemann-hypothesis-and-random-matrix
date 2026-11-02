#!/usr/bin/env python3
"""Small exact symbolic controls; no numerical height or prime scan.

Toy exponents 2,3,4 and finite rational intervals test the algebra only.
They do not evaluate Vbar, zeta zeros, an asymptotic limit, or an RH claim.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s


def formal_log(q):
    a,b=s.Rational(q).as_numer_denom()
    return sum((k*s.Symbol(f'L_{p}') for p,k in s.factorint(a).items()),s.S.Zero)-sum((k*s.Symbol(f'L_{p}') for p,k in s.factorint(b).items()),s.S.Zero)


def power_integral(exponent,left,right):
    if exponent == -1:
        return formal_log(right/left)
    return (right**(exponent+1)-left**(exponent+1))/(exponent+1)


def finite_control(T,x,N,coefficients):
    T=s.Integer(T);x=s.Rational(x);N=s.Rational(N)
    coeff={s.Integer(n):c for n,c in coefficients.items() if x<n<=N}
    points=sorted({x,N}|{n for n in coeff if x<n<N})
    direct=s.S.Zero
    continuous_stieltjes=s.S.Zero
    for left,right in zip(points,points[1:]):
        mid=(left+right)/2
        A=sum((c for n,c in coeff.items() if n<=mid),s.S.Zero)
        C=A+x
        direct+=T*x**T*(C*C*power_integral(-T-1,left,right)-2*C*power_integral(-T,left,right)+power_integral(1-T,left,right))
        continuous_stieltjes+=x**T*(C*power_integral(-T,left,right)-power_integral(1-T,left,right))
    z=x/N
    B=lambda r:T*r**(T-1)/(T-1)-r**T
    if T==2:
        center=2*formal_log(N/x)+4*z-z*z-3
    else:
        center=2/((T-1)*(T-2))-T/(T-2)*z**(T-2)+2*T/(T-1)*z**(T-1)-z**T
    pair=sum((cm*cn*((x/max(m,n))**T-z**T) for m,cm in coeff.items() for n,cn in coeff.items()),s.S.Zero)
    mixed=-2*x*sum((c*(B(x/n)-B(z)) for n,c in coeff.items()),s.S.Zero)
    expanded=pair+mixed+x*x*center
    jump=s.S.Zero
    for n,c in coeff.items():
        G=sum((cm for m,cm in coeff.items() if m<=n),s.S.Zero)-(n-x)
        jump+=c*(x/n)**T*(2*G-c)
    G_N=sum(coeff.values(),s.S.Zero)-(N-x)
    boundary=-(x/N)**T*G_N*G_N
    stieltjes=jump-2*continuous_stieltjes+boundary
    assert s.expand(direct-expanded)==0
    assert s.expand(direct-stieltjes)==0
    assert s.expand(boundary)!=0
    # Dropping the cutoff boundary is demonstrably incorrect in these controls.
    omitted_boundary_difference=s.expand(direct-(jump-2*continuous_stieltjes))
    assert s.expand(omitted_boundary_difference-boundary)==0
    return {'toy_exponent':str(T),'interval':[str(x),str(N)],
            'coefficients':{str(n):str(c) for n,c in coeff.items()},'cell_count':len(points)-1,
            'direct_minus_pair_mixed_continuous':'0','direct_minus_stieltjes_with_boundary':'0',
            'cutoff_is_occupied':N in coeff,'required_boundary':str(s.factor(boundary)),
            'omitting_boundary_fails':True,
            'scope':'Exact toy finite functional only; not a numerical height evaluation.'}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    T,q,z,N=s.symbols('T q z N',positive=True)
    survival=q**(-T)
    assert s.simplify(s.diff(survival,q)+T*q**(-T-1))==0
    B=lambda r:T*r**(T-1)/(T-1)-r**T
    assert s.simplify(s.diff(B(1/q),q)+T*(q-1)*q**(-T-1))==0
    moment=T/(T-2)-2*T/(T-1)+1
    assert s.factor(moment-2/((T-1)*(T-2)))==0
    C=2/((T-1)*(T-2))-T/(T-2)*q**(2-T)+2*T/(T-1)*q**(1-T)-q**(-T)
    assert s.simplify(s.diff(C,q)-T*(q-1)**2*q**(-T-1))==0
    assert s.simplify(C.subs(q,1))==0
    limit=s.simplify(s.limit(C,T,2))
    assert s.simplify(limit-(2*s.log(q)+4/q-q**(-2)-3))==0
    assert s.simplify(B(1)-1/(T-1))==0
    a,b=s.symbols('a b',positive=True)
    P2=lambda a,b:b*b/a+2*b/a**2+2/a**3
    P4=lambda a,b:b**4/a+4*b**3/a**2+12*b*b/a**3+24*b/a**4+24/a**5
    tail2=N**(2-T)*P2(T-2,1+s.log(N))
    tail4=N**(1-T)*P4(T-1,s.log(2*N))
    assert s.simplify(s.diff(tail2,N)+N**(1-T)*(1+s.log(N))**2)==0
    assert s.simplify(s.diff(tail4,N)+N**(-T)*s.log(2*N)**4)==0
    constant=s.Rational(9,2)*5*s.Rational(17,4)**2*4
    assert constant==s.Rational(13005,8)<2048
    assert s.expand(9*(T-1)*(T-2)-2*T*T-(T-3)*(7*T-6))==0
    # Check the large-index regrouping for arbitrary formal arithmetic values.
    n,x,En,Ex,Ln=s.symbols('n x En Ex Ln')
    assert s.cancel(2*((En+n)-(Ex+x))-Ln+2*x-2*T*n/(T-1)-(2*(En-Ex)-Ln-2*n/(T-1)))==0
    # The Laurent constant and finite-prefix cancellation are formal identities.
    h=s.symbols('h');gamma=s.symbols('gamma')
    assert s.limit((1/h-gamma)/(1+h)-1/h,h,0)==-gamma-1
    P,H=s.symbols('P H')
    full=-gamma-1-(H-P/x-s.log(x))-(P-x)/x
    assert s.simplify(full-(s.log(x)-gamma-H))==0
    prime_coeff={}
    for n in range(2,14):
        factors=s.factorint(n)
        if len(factors)==1:prime_coeff[n]=s.Symbol(f'L_{next(iter(factors))}')
    controls=[finite_control(3,s.Rational(5,2),12,prime_coeff),
              finite_control(2,s.Rational(7,3),13,prime_coeff),
              finite_control(4,s.Rational(11,4),9,{n:s.Rational(n%5-2,n%3+1) for n in range(2,14)})]
    record={'status':'PASS','sympy_version':s.__version__,
            'survival_and_mixed_antiderivatives':'PASS','continuous_moment':'2/((T-1)(T-2))',
            'finite_T2_continuous_coefficient':str(limit),'unconditional_tail_derivative':'0','RH_tail_derivative':'0',
            'finite_cutoff_constant_before_rounding':str(constant),'stated_safe_constant':2048,
            'T_ratio_inequality_factor':'(T-3)*(7*T-6)',
            'larger_prime_power_regrouping':'0','Laurent_and_finite_prefix_constants':'PASS',
            'finite_controls':controls,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Small exact symbolic checks only. Analytic convergence and RH statements require the written proof; no numerical heights, scans or asymptotic inference.'}
    (args.output_dir/'length_arithmetic_checks.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps(record,indent=2,sort_keys=True))

if __name__=='__main__':main()
