#!/usr/bin/env python3
"""Independent bounded checks of COMPACT_POLE_PACKET.md.

Run: python3 check_compact_packet.py [--output-dir DIR]
Requires SymPy and mpmath. Exact symbolic checks are distinguished from
high-precision numerical diagnostics; the latter are not interval certificates.
No zeta integral or zeta-zero statistic is evaluated.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import sympy as s
import mpmath as mp


def exact_checks() -> dict:
    y,b,z=s.symbols('y b z',real=True)
    pieces=[(s.Integer(-2),s.Integer(-1),(2+y)**3/6),
            (s.Integer(-1),s.Integer(0),s.Rational(2,3)-y*y-y**3/2),
            (s.Integer(0),s.Integer(1),s.Rational(2,3)-y*y+y**3/2),
            (s.Integer(1),s.Integer(2),(2-y)**3/6)]
    C2=[]
    for j,t in enumerate([-2,-1,0,1,2]):
        left=s.Integer(0) if j==0 else pieces[j-1][2]
        right=s.Integer(0) if j==4 else pieces[j][2]
        for order in range(3):
            lv=s.diff(left,y,order).subs(y,t)
            rv=s.diff(right,y,order).subs(y,t)
            assert s.simplify(lv-rv)==0
            C2.append({'knot':t,'order':order,'value':str(lv)})
    def norm(order:int):
        total=0
        for lo,hi,B in pieces:
            poly=s.diff(B,y,order)
            roots=[r for r in s.solve(poly,y) if r.is_real and lo<r<hi] if poly!=0 else []
            cuts=[lo]+sorted(roots,key=lambda x:float(x))+[hi]
            for a,c in zip(cuts,cuts[1:]):
                sign=s.sign(poly.subs(y,(a+c)/2))
                total+=sign*s.integrate(poly,(y,a,c))
        return s.simplify(total)
    norms=[norm(i) for i in range(4)]
    assert norms==[s.Integer(1),s.Rational(4,3),s.Rational(8,3),s.Integer(8)]
    mass=sum(s.integrate(B,(y,lo,hi)) for lo,hi,B in pieces)
    assert mass==1
    tilt_checks=[]
    endpoints=0
    for lo,hi,B in pieces:
        K=-s.diff(B,y,2)+b*b*B
        primitive=s.exp(b*y)*(-s.diff(B,y)+b*B)
        difference=s.simplify(s.diff(primitive,y)-s.exp(b*y)*K)
        assert difference==0
        endpoints+=primitive.subs(y,hi)-primitive.subs(y,lo)
        tilt_checks.append({'interval':[str(lo),str(hi)],'difference':str(difference)})
    assert s.simplify(endpoints)==0
    Kouter=-(2-y)+b*b*(2-y)**3/6
    negative_outer=s.simplify(2*s.integrate(-Kouter,(y,1,2)))
    assert negative_outer==1-b*b/12
    ratio=(1-z/12)/(2+2*z/3)
    derivative=s.factor(s.diff(ratio,z))
    assert s.simplify(derivative+s.Rational(5,6)/(2+2*z/3)**2)==0
    assert ratio.subs(z,s.Rational(1,4))==s.Rational(47,104)
    # At b=0, K=-B'' has sign change at |y|=2/3.
    positive_b0=2*s.integrate(2-3*y,(y,0,s.Rational(2,3)))
    negative_b0=2*(s.integrate(3*y-2,(y,s.Rational(2,3),1))+s.integrate(2-y,(y,1,2)))
    assert positive_b0==negative_b0==s.Rational(4,3)
    # Exact inverse-transform calculation for q != 0, followed by the q=0 limit.
    q=s.symbols('q',real=True,nonzero=True)
    transform=s.simplify(2*sum(s.integrate((-s.diff(B,y,2)+b*b*B)*s.cos(q*y),(y,lo,hi))
                               for lo,hi,B in pieces[2:]))
    expected=(q*q+b*b)*(s.sin(q/2)/(q/2))**4
    assert s.trigsimp(s.expand_trig(transform-expected))==0
    assert s.simplify(s.limit(transform,q,0)-b*b)==0
    return {'status':'PASS','C2_matching':C2,'spline_integral':str(mass),
            'L1_derivative_norms':[str(x) for x in norms],
            'tilted_primitive_piece_checks':tilt_checks,'tilted_endpoint_sum':str(s.simplify(endpoints)),
            'outer_negative_mass':str(negative_outer),'normalized_outer_mass_derivative_in_b_squared':str(derivative),
            'normalized_outer_lower_bound':'47/104','full_b0_positive_mass':str(positive_b0),
            'full_b0_negative_mass':str(negative_b0),'normalized_b0_negative_mass':'2/3',
            'inverse_transform_q_nonzero':str(transform),'inverse_transform_q_zero':'b**2'}


def B_mp(y):
    u=abs(y)
    if u<=1:return mp.mpf(2)/3-u*u+u**3/2
    if u<=2:return (2-u)**3/6
    return mp.mpf(0)


def K_mp(y,b):
    u=abs(y)
    if u<=1:return 2-3*u+b*b*B_mp(y)
    if u<=2:return u-2+b*b*B_mp(y)
    return mp.mpf(0)


def numerical_inverse()->list[dict]:
    mp.mp.dps=70
    cases=[]
    for bname,b in [('0',mp.mpf(0)),('1/400',mp.mpf(1)/400),('1/2',mp.mpf(1)/2)]:
        for qname,q in [('0',mp.mpf(0)),('1e-8',mp.mpf('1e-8')),('pi',mp.pi),
                         ('2pi',2*mp.pi),('10',mp.mpf(10)),('25',mp.mpf(25))]:
            value=2*mp.quad(lambda y:K_mp(y,b)*mp.cos(q*y),[0,1,2])
            sinc=mp.mpf(1) if q==0 else mp.sin(q/2)/(q/2)
            expected=(q*q+b*b)*sinc**4
            error=abs(value-expected)
            assert error<mp.mpf('1e-60'),(bname,qname,error)
            cases.append({'b':bname,'q':qname,'quadrature':mp.nstr(value,65),
                          'formula':mp.nstr(expected,65),'absolute_error':mp.nstr(error,8),
                          'status':'PASS','evidence':'70-digit numerical diagnostic, not an enclosure'})
    return cases


def trial_factor(n:int)->dict[int,int]:
    d=2;out={}
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out


def finite_prime_packet()->dict:
    mp.mp.dps=70
    X=10000;W=100;sigma=mp.mpf(3)/4;b=(1-sigma)/W
    lower=X*mp.exp(-mp.mpf(2)/W);upper=X*mp.exp(mp.mpf(2)/W)
    lo=int(mp.floor(lower))+1;hi=int(mp.ceil(upper))-1
    # Route A factors each integer in the support independently by trial division.
    route_a={}
    for n in range(lo,hi+1):
        fac=trial_factor(n)
        if len(fac)==1:
            p,k=next(iter(fac.items()));route_a[n]=(p,k)
    # Route B sieves the primes, then forms every prime power in the support.
    sieve=[True]*(hi+1);sieve[0]=sieve[1]=False
    for p in range(2,int(hi**.5)+1):
        if sieve[p]:
            for n in range(p*p,hi+1,p):sieve[n]=False
    route_b={}
    for p in range(2,hi+1):
        if sieve[p]:
            power=p;k=1
            while power<=hi:
                if power>=lo:route_b[power]=(p,k)
                power*=p;k+=1
    assert route_a==route_b
    assert route_a[101**2]==(101,2)
    def term(n,p):
        return 2*mp.pi*W*mp.log(p)*mp.power(n,-sigma)*K_mp(W*mp.log(mp.mpf(n)/X),b)
    suma=mp.fsum(term(n,p) for n,(p,k) in sorted(route_a.items()))
    sumb=mp.fsum(term(n,p) for n,(p,k) in sorted(route_b.items(),reverse=True))
    assert abs(suma-sumb)<mp.mpf('1e-60')
    powers=[{'n':n,'p':p,'k':k,'weighted_term':mp.nstr(term(n,p),60)} for n,(p,k) in sorted(route_a.items()) if k>=2]
    return {'status':'PASS','X':X,'W':W,'sigma':'3/4','b':'1/400',
            'open_support_endpoints':[mp.nstr(lower,65),mp.nstr(upper,65)],
            'integers_in_support':[lo,hi],'prime_power_count':len(route_a),
            'prime_power_factorizations':[{'n':n,'p':p,'k':k} for n,(p,k) in sorted(route_a.items())],
            'higher_prime_powers':powers,'arithmetic_sum_route_a':mp.nstr(suma,65),
            'arithmetic_sum_route_b':mp.nstr(sumb,65),
            'absolute_difference':mp.nstr(abs(suma-sumb),8),
            'scope':'Finite signed arithmetic sum only. No numerical zeta integral, asymptotic zeta estimate, or RH test.'}


def main()->None:
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--proof',type=Path,default=Path(__file__).with_name('COMPACT_POLE_PACKET.md'))
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    proof_bytes=args.proof.read_bytes()
    result={'status':'PASS','exact':exact_checks(),'numerical_inverse_fourier':numerical_inverse(),
            'finite_prime_packet':finite_prime_packet(),'proof':{'filename':args.proof.name,
               'sha256':hashlib.sha256(proof_bytes).hexdigest()},
            'runtime':{'python':sys.version.split()[0],'sympy':s.__version__,'mpmath':mp.__version__},
            'limitations':['No numerical diagnostic is an outward enclosure.','The finite arithmetic evaluation is not a numerical zeta integral.','These checks do not prove the contour shift or any AH/Montgomery claim.']}
    output=args.output_dir/'compact_packet_checks.json'
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','C2_endpoint_matches':len(result['exact']['C2_matching']),
                     'inverse_fourier_diagnostics':len(result['numerical_inverse_fourier']),
                     'finite_prime_power_count':result['finite_prime_packet']['prime_power_count'],
                     'higher_prime_powers':result['finite_prime_packet']['higher_prime_powers'],
                     'result_sha256':hashlib.sha256(output.read_bytes()).hexdigest()},sort_keys=True))

if __name__=='__main__':main()
