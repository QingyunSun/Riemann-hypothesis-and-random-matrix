#!/usr/bin/env python3
"""Independent exact geometry, derivative bounds and bounded high-precision checks.

The T=100 precision control repeats one requested value with the same frozen
piecewise-constant weight. It is not a fourth T value or an interval certificate.
"""
from __future__ import annotations
import argparse
import bisect
import csv
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as s


def log_rational(q):
    a,b=s.Rational(q).as_numer_denom()
    return sum((power*s.Symbol(f'L_{p}') for p,power in s.factorint(a).items()),s.S.Zero)-sum((power*s.Symbol(f'L_{p}') for p,power in s.factorint(b).items()),s.S.Zero)


def exact_control(T,low,high,coeffs):
    T,low,high=map(s.Rational,(T,low,high));q=1+1/T
    events={low,high}
    for n in coeffs:
        for x in [s.Rational(n)/q,s.Rational(n)]:
            if low<x<high:events.add(x)
    events=sorted(events)
    direct=s.S.Zero
    for left,right in zip(events,events[1:]):
        mid=(left+right)/2
        a=sum((value for n,value in coeffs.items() if mid<n<=q*mid),s.S.Zero)
        direct+=a*a*(1/left-1/right)-2*a/T*log_rational(right/left)+(right-left)/T**2
    pair=s.S.Zero
    for m,cm in coeffs.items():
        for n,cn in coeffs.items():
            left=max(low,s.Rational(max(m,n))/q);right=min(high,s.Rational(min(m,n)))
            if left<right:pair+=cm*cn*(1/left-1/right)
    center=s.S.Zero
    for n,c in coeffs.items():
        left=max(low,s.Rational(n)/q);right=min(high,s.Rational(n))
        if left<right:center-=2*c/T*log_rational(right/left)
    center+=(high-low)/T**2
    difference=s.expand(direct-pair-center)
    assert difference==0
    return {'T':str(T),'window':[str(low),str(high)],'coefficient_count':len(coeffs),
            'coefficients':{str(n):str(c) for n,c in coeffs.items()},'event_cells':len(events)-1,
            'direct_minus_full_pair_and_both_centers':'0'}


def exact_analytic_checks():
    z=s.symbols('z');p=s.Integer(1);polynomials=[];norms=[]
    for j in range(5):
        polynomials.append(str(p));norms.append(sum(abs(c) for c in s.Poly(p,z).all_coeffs()))
        p=s.expand((1-z*z)**2*s.diff(p,z)+(4*j*z*(1-z*z)-2*z)*p)
    assert norms==[1,2,8,88,1096]
    # The rational base 27/10 < e follows already from sum_{k=0}^5 1/k!.
    assert sum(s.Rational(1,s.factorial(k)) for k in range(6))>s.Rational(27,10)
    assert s.Rational(27,10)**7>1000
    assert s.Rational(27,10)**16>5629037
    assert s.Rational(7,32761)<s.Rational(1,4096)
    u=s.symbols('u',positive=True)
    i0=u/(1+u);i1=s.log(1+u)-u/(1+u);i2=u-2*s.log(1+u)+u/(1+u)
    for integral,power in [(i0,0),(i1,1),(i2,2)]:
        assert s.simplify(s.diff(integral,u)-u**power/(1+u)**2)==0
        assert s.limit(integral,u,0)==0
    for degree in range(2,13):
        assert s.expand(s.series(i1,u,0,13).removeO()).coeff(u,degree)==s.Rational((-1)**degree*(degree-1),degree)
    for degree in range(3,13):
        assert s.expand(s.series(i2,u,0,13).removeO()).coeff(u,degree)==s.Rational((-1)**(degree+1)*(degree-2),degree)
    T,L,B=s.symbols('T L B',positive=True)
    expression=B*B/L*i0-2*B/T*i1+L/T**2*i2
    assert s.simplify(s.diff(expression,u)-(B-L*u/T)**2/(L*(1+u)**2))==0
    coeffs={}
    for n in range(2,55):
        factors=s.factorint(n)
        if len(factors)==1:coeffs[n]=s.Symbol(f'L_{next(iter(factors))}')
    controls=[exact_control(5,10,45,coeffs),
              exact_control(4,s.Rational(11,2),23,{n:s.Rational(n%7-3,n%4+1) for n in range(2,30)})]
    return {'derivative_polynomials_P0_to_P4':polynomials,'coefficient_l1_norms':[int(a) for a in norms],
            'stable_integral_derivative_identity':'0','I1_I2_series_coefficients':'Exact through degree 12',
            'uniform_cell_relative_width_upper':'7/32761 < 1/4096',
            'log_bounds':'log(T)<7, log(integer cutoff)<16 proved from e>27/10',
            'finite_kernel_controls':controls}


def precision_control(source: Path):
    mp.mp.dps=70
    T=100;q=mp.mpf(101)/100
    arrays=np.load(source/'prime_powers.npz')
    mask=arrays['n']<=31939
    positions=[int(x) for x in arrays['n'][mask]]
    bases=[int(x) for x in arrays['prime_base'][mask]]
    prefix=[mp.mpf(0)]
    for p in bases:prefix.append(prefix[-1]+mp.log(p))
    boundaries=[mp.power(T,mp.mpf(7)/4+mp.mpf(j)/(2*16384)) for j in range(16385)]
    low,high=boundaries[0],boundaries[-1]
    points=set(boundaries)
    for n in positions:
        for x in [mp.mpf(n)/q,mp.mpf(n)]:
            if low<x<high:points.add(x)
    points=sorted(points)
    with (source/'variance_T100_bins.csv').open() as f:
        rows=list(csv.DictReader(f))
    weights=[(mp.mpf(r['psi_left_simpson'])+mp.mpf(r['psi_right_simpson']))/2 for r in rows]
    bins=[mp.mpf(0) for _ in weights]
    for left,right in zip(points,points[1:]):
        mid=(left+right)/2
        total=prefix[bisect.bisect_right(positions,q*mid)]-prefix[bisect.bisect_right(positions,mid)]
        # Independent direct antiderivative at 70 decimal digits, no small-u series.
        cell=total**2*(1/left-1/right)-2*total/T*mp.log(right/left)+(right-left)/T**2
        assert cell>=0
        index=bisect.bisect_right(boundaries,left)-1
        bins[index]+=T/mp.log(T)**2*cell
    result=mp.fsum(x*w for x,w in zip(bins,weights))
    original=json.loads((source/'actual_prime_variance.json').read_text())['results'][0]
    difference=abs(result-mp.mpf(original['positive_variance_midpoint_diagnostic']))
    bin_difference=max(abs(a-mp.mpf(r['unweighted_positive_mass'])) for a,r in zip(bins,rows))
    assert difference<mp.mpf('1e-11')
    assert bin_difference<mp.mpf('1e-11')
    # Independent arbitrary-precision adaptive integration of the actual seed at fixed v.
    def f(x):
        return mp.exp(-1/(1-4*x*x)) if abs(x)<mp.mpf('.5') else mp.mpf(0)
    den=mp.quad(lambda x:f(x)**2,[-mp.mpf('.5'),0,mp.mpf('.5')])
    samples=[]
    table=[]
    with (source/'seed_autocorrelation.csv').open() as h:
        table=list(csv.DictReader(h))
    for index in [0,1024,4096,6144,7168,8192]:
        v=mp.mpf(index)/8192
        val=mp.quad(lambda x:f(x)*f(x-v),[v-mp.mpf('.5'),v/2,mp.mpf('.5')])/den if v<1 else mp.mpf(0)
        error=abs(val-mp.mpf(table[index]['psi_fine']))
        assert error<mp.mpf('1e-12')
        samples.append({'v':str(v),'adaptive_70digit_psi':str(val),'absolute_difference_from_simpson':str(error)})
    return {'scope':'High-precision diagnostics, not directed-rounding certificates.',
            'T':T,'decimal_precision':70,'cell_count':len(points)-1,
            'independent_formula':'Direct uncentered antiderivative; active Lambda from prefix differences at the cell midpoint.',
            'same_frozen_piecewise_constant_weight_result':str(result),
            'absolute_total_difference':str(difference),'max_unweighted_bin_difference':str(bin_difference),
            'adaptive_seed_controls':samples}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--data-dir',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    exact=exact_analytic_checks()
    data=np.load(args.data_dir/'prime_powers.npz')
    # Independent exact factorization through 1000 includes non-prime-power exclusions.
    lookup={int(n):(int(p),int(k)) for n,p,k in zip(data['n'],data['prime_base'],data['exponent']) if n<=1000}
    for n in range(2,1001):
        factors=s.factorint(n)
        if len(factors)==1:assert lookup[n]==next(iter(factors.items()))
        else:assert n not in lookup
    assert np.all(np.array([int(p)**int(k)==int(n) for n,p,k in zip(data['n'],data['prime_base'],data['exponent'])]))
    high=precision_control(args.data_dir)
    output={'status':'PASS','exact':exact,'prime_power_integer_identity_count':len(data['n']),
            'independent_factorization_range':[2,1000],'high_precision':high,
            'sympy_version':s.__version__,'mpmath_version':mp.__version__,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact finite algebra plus bounded high-precision diagnostics. No asymptotic inference or interval certificate.'}
    (args.output_dir/'prime_variance_checks.json').write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print(json.dumps(output,indent=2,sort_keys=True))

if __name__=='__main__':main()
