#!/usr/bin/env python3
"""Bounded structural checks; no genuine-zeta heat integration is performed.

The contraction and external-field algebra use exact fractions. The explicit
circle trajectory uses float64 trigonometry and is labelled a numerical check.
"""
from __future__ import annotations

import json
import math
import random
from fractions import Fraction as F
from pathlib import Path


def line_force(x):
    return [sum((F(2)/(a-b) for j,b in enumerate(x) if j!=i),F(0)) for i,a in enumerate(x)]


def exact_contraction_checks():
    rng=random.Random(7072026)
    external=list(map(F,[-30,-20,20,30]))
    for _ in range(200):
        x=[];y=[]
        a=F(-4);b=F(-4)
        for i in range(6):
            a+=F(rng.randint(2,10),10)
            b+=F(rng.randint(2,10),10)
            x.append(a);y.append(b)
        w=[a-b for a,b in zip(x,y)]
        fx,fy=line_force(x),line_force(y)
        for i in range(6):
            rhs=-sum((F(2)*(w[i]-w[j])/((x[i]-x[j])*(y[i]-y[j])) for j in range(6) if j!=i),F(0))
            assert fx[i]-fy[i]==rhs
        imax=max(range(6),key=lambda i:w[i]);imin=min(range(6),key=lambda i:w[i])
        assert fx[imax]-fy[imax]<=0
        assert fx[imin]-fy[imin]>=0
        field=lambda z:sum((F(2)/(z-d) for d in external),F(0))
        if w[imax]>=0:assert field(x[imax])-field(y[imax])<=0
        if w[imin]<=0:assert field(x[imin])-field(y[imin])>=0
    return {"trials":200,"arithmetic":"exact fractions","all_passed":True}


def exact_far_field_checks():
    roots=list(map(F,[-19,-11,-7,5,9,13]))
    B2=sum((d**-2 for d in roots),F(0))
    B3=sum((abs(d)**-3 for d in roots),F(0))
    field=lambda z:sum((F(2)/(z-d) for d in roots),F(0))
    for j in range(-40,41):
        z=F(j,20);R=abs(z)
        assert R<=F(5,2)
        assert abs(field(z)-field(0))<=4*R*B2
        assert abs(field(z)-field(0)+2*B2*z)<=4*R**2*B3
    return {"points":81,"B2":str(B2),"B3":str(B3),"all_passed":True}


def circle_checks():
    rows=[]
    max_rel_error=0.0
    rng=random.Random(277)
    for N in [4,8,16,32,64]:
        M=N//2
        for s in [0.0,0.001,0.01,0.1,1.0]:
            c=math.sqrt(0.5)*math.exp(-math.pi**2*s)
            alpha=math.acos(c)
            points=[]
            for j in range(M):
                for sign in [-1,1]:
                    angle=(2*math.pi*j+sign*alpha)/M
                    angle%=2*math.pi
                    velocity=sign*M*c/math.sqrt(1-c*c)
                    points.append((angle,velocity))
            points.sort()
            force=[sum(1/math.tan((x-y)/2) for j,(y,_) in enumerate(points) if j!=i)
                   for i,(x,_) in enumerate(points)]
            error=max(abs(v-f) for (_,v),f in zip(points,force))
            relative=error/(1+max(abs(v) for _,v in points))
            max_rel_error=max(max_rel_error,relative)
            assert relative<1e-9
            gaps=[((points[(i+1)%N][0]-points[i][0])%(2*math.pi))*N/(2*math.pi) for i in range(N)]
            predicted=2*alpha/math.pi
            assert abs(min(gaps)-predicted)<1e-12
            assert min(gaps)>0.5-1e-12
            assert max(gaps)<1.5+1e-12
            # Unfolded period-two configuration: two atoms at 2j +/- alpha/pi.
            offset=alpha/math.pi
            for _ in range(20):
                a=rng.uniform(-8,8);b=a+rng.uniform(0.01,20)
                count=sum(a<2*j+sign*offset<=b for j in range(-20,30) for sign in [-1,1])
                assert abs(count-(b-a))<=2+1e-12
            if N==16:
                rows.append({"microscopic_time":s,"small_gap":predicted,"large_gap":2-predicted,
                             "force_max_abs_error":error})
    return {"type":"float64 analytic-trajectory versus cotangent-ODE check",
            "N_values":[4,8,16,32,64],"max_relative_force_error":max_rel_error,
            "gap_evolution_example_N16":rows,"sine_pair_test_lower_bound":1-8/math.pi**2}


def generator_checks():
    rows=[]
    for N in [4,8,16,32,64,128]:
        m=N//2
        alpha=F(m,N)
        coefficient=8*alpha**2*(1-alpha)
        clock_coefficient=8*alpha**2
        assert coefficient==1 and clock_coefficient==2
        rows.append({"N":N,"m":m,"CUE_omitted_diffusion_slope_over_pi_squared":str(coefficient),
                     "CUE_deterministic_slope_over_pi_squared":str(-coefficient),
                     "clock_diffusion_slope_over_pi_squared":str(clock_coefficient)})
    # Signed trace merging never increases either protected Fourier weight.
    for m in range(-12,13):
        for n in range(-12,13):
            if not m or not n:continue
            before=(max(m,0)+max(n,0),max(-m,0)+max(-n,0))
            after=(max(m+n,0),max(-m-n,0))
            assert after[0]<=before[0] and after[1]<=before[1]
    return {"arithmetic":"exact fractions and integers","rows":rows,
            "signed_merge_filtration_checks":24**2}


if __name__=="__main__":
    result={"status":"all bounded checks passed; no zeta spacing theorem asserted",
            "contraction":exact_contraction_checks(),"external_field":exact_far_field_checks(),
            "two_periodic_circle":circle_checks(),"generator":generator_checks()}
    output=Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
