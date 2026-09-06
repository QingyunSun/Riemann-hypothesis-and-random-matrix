#!/usr/bin/env python3
"""Bounded exact checks of R19 formulas; no large-prime or zeta experiment.

Run: python3 check_weighted_variance.py [--output-dir DIR]
The finite support test uses a flat test window, not the R16 smooth seed.
Its purpose is to check the universal interval geometry and every mean factor.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s


def canonical(expr):
    expanded = s.expand_log(s.expand(expr), force=True)
    replacements = {}
    for logarithm in expanded.atoms(s.log):
        value = logarithm.args[0]
        if value.is_Rational and value > 0:
            numerator, denominator = value.as_numer_denom()
            replacements[logarithm] = (
                sum((power*s.log(prime) for prime,power in s.factorint(numerator).items()),s.S.Zero)
                - sum((power*s.log(prime) for prime,power in s.factorint(denominator).items()),s.S.Zero)
            )
    return s.expand(expanded.xreplace(replacements))


def interval_test(T, low, high, coefficients):
    q = 1 + 1/T
    points = {low, high}
    for n in coefficients:
        for point in (s.Rational(n), s.Rational(n)/q):
            if low < point < high:
                points.add(point)
    points = sorted(points)
    direct = s.S.Zero
    for left, right in zip(points, points[1:]):
        mid = (left + right)/2
        total = sum((c for n, c in coefficients.items() if mid < n <= q*mid), s.S.Zero)
        direct += total**2*(1/left-1/right) - 2*total/T*s.log(right/left) + (right-left)/T**2

    def kernel(m, n):
        left = max(low, s.Rational(max(m,n))/q)
        right = min(high, s.Rational(min(m,n)))
        return 1/left-1/right if left < right else s.S.Zero

    diagonal = sum((c*c*kernel(n,n) for n,c in coefficients.items()), s.S.Zero)
    cross = sum((2*coefficients[m]*coefficients[n]*kernel(m,n)
                 for m in coefficients for n in coefficients if m<n), s.S.Zero)
    mean = s.S.Zero
    for n,c in coefficients.items():
        left, right = max(low,s.Rational(n)/q), min(high,s.Rational(n))
        if left < right:
            mean += -2*c/T*s.log(right/left)
    continuous = (high-low)/T**2
    expanded = diagonal+cross+mean+continuous
    difference = canonical(direct-expanded)
    assert difference == 0, difference
    return {
        'T':str(T),'x_low':str(low),'x_high':str(high),'coefficient_count':len(coefficients),
        'integration_cells':len(points)-1,'coefficients':{str(n):str(c) for n,c in coefficients.items()},
        'normalization':'Both expressions omit the same positive T/log(T)^2 factor.',
        'direct_minus_full_kernel':'0',
        'expression_sha256':hashlib.sha256(str(canonical(direct)).encode()).hexdigest(),
        'status':'PASS'
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    y=s.symbols('y',positive=True);A,delta=s.symbols('A delta',positive=True)
    k=s.sin(y/2)**2/y**2
    derivative=s.sin(y)/(2*y)-(1-s.cos(y))/y**2
    assert s.trigsimp(y*s.diff(k,y)-derivative)==0
    assert s.limit(k,y,0)==s.Rational(1,4)
    assert s.limit(derivative/y**2,y,0)==-s.Rational(1,24)
    integral=s.integrate(k,(y,0,s.oo))
    assert integral==s.pi/4
    assert s.simplify((2/s.pi)*2*A*integral-A)==0
    assert s.simplify(4*A/(s.pi*(8*A/(s.pi*delta)))-delta/2)==0
    ell=s.Rational(1,2)
    upper=s.Rational(4,3)*(1+ell)+ell**3/12-ell/3-s.Rational(1,4)*max(0,1-ell-ell**2)
    assert upper==s.Rational(57,32)
    prime_coeffs={}
    for n in range(2,35):
        f=s.factorint(n)
        if len(f)==1:prime_coeffs[n]=s.log(next(iter(f)))
    tests=[interval_test(s.Rational(7),s.Rational(10),s.Rational(30),prime_coeffs),
           interval_test(s.Rational(3),s.Rational(5,2),s.Rational(18),
                         {n:s.Rational(n%5-2,n%3+1) for n in range(2,25)})]
    record={'status':'PASS','scope':'Exact finite algebra and kernel normalization only. No actual asymptotic variance bound or Bragg deficit is evaluated.',
            'sympy_version':s.__version__,'kernel_derivative':str(derivative),
            'kernel_at_zero':'1/4','kernel_derivative_second_order':'-1/24',
            'integral_k':'pi/4','Abelian_normalization':'A',
            'finite_interval_candidate_length_half':str(upper),
            'quantitative_tail_budget_at_R_8A_over_pi_delta':'delta/2',
            'interval_tests':tests}
    target=args.output_dir/'weighted_variance_checks.json'
    target.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print('PASS: kernel derivative, Dirichlet integral, Abelian constants, tail budget, rational interval bound.')
    print('PASS: exact full interval-kernel expansion for prime-power logarithms and independent signed rational data.')
    print('No asymptotic arithmetic inequality or numerical zero statistic is claimed.')

if __name__=='__main__':main()
