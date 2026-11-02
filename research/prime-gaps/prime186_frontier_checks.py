#!/usr/bin/env python3
"""Exact complementary-support frontier checks; no FLINT or paid services.

This checks finite arithmetic/geometry, not prime distribution or sieve integrals.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
import json
from math import gcd, isqrt
from pathlib import Path
from time import perf_counter


@lru_cache(None)
def divisors(n: int) -> tuple[int, ...]:
    small = [d for d in range(1,isqrt(n)+1) if n%d == 0]
    return tuple(sorted(set(small+[n//d for d in small])))


@lru_cache(None)
def dense(m: int, order: int, y: int) -> bool:
    """Definition 2.1 via exact coverage of target intervals [v,Yv]."""
    if order == 0:
        return True
    for j in range(order):
        reach = 1
        for v in divisors(m):
            if dense(m//v,j,y) and dense(v,order-1-j,y):
                if v > reach:
                    return False
                reach = max(reach,y*v)
        if reach < y*m:
            return False
    return True


def allocation_envelope(knots: list[F], lower: list[F], upper: list[F]) -> dict:
    """Exact feasibility of nondecreasing 3-Lipschitz phi with pointwise bounds.

    Knots include zero, whose lower and upper bounds both equal zero.
    A failed (i,j) is an explicit two-bound plus Lipschitz contradiction.
    """
    assert knots[0] == lower[0] == upper[0] == 0
    assert all(a < b for a,b in zip(knots,knots[1:]))
    envelope = [max(lower[j]-3*max(knots[j]-u,F(0))
                    for j in range(len(knots))) for u in knots]
    for i,value in enumerate(envelope):
        if value > upper[i]:
            j=max(range(len(knots)),key=lambda j:lower[j]-3*max(knots[j]-knots[i],F(0)))
            return {"feasible":False,"upper_index":i,"lower_index":j,
                    "positive_violation":str(value-upper[i])}
    assert all(F(0) <= b-a <= 3*(v-u)
               for u,v,a,b in zip(knots,knots[1:],envelope,envelope[1:]))
    return {"feasible":True,"knots":[str(u) for u in knots],
            "phi_values":[str(a) for a in envelope]}


def cap_feasibility(A: F,C: F,u: F,v: F) -> dict:
    assert u > v > 0
    # Inner root at v: 4v-phi(v)<=C and phi(v)<=A.
    # Outer root at u: u+phi(u)<=A and 3u-phi(u)<=C.
    return allocation_envelope([F(0),v,u],
        [F(0),max(F(0),4*v-C),max(F(0),3*u-C)],
        [F(0),min(3*v,A),min(3*u,A-u)])


def main() -> None:
    start=perf_counter()
    D,E,Y,X=330,455,10,27000
    Q=D*E//gcd(D,E); A_int,C_int=121,2197
    assert Q == 30030 and gcd(D,E) == 5
    assert A_int*C_int <= X*Y and Q > X
    # f(p)=p, g(p)=p^2. Only activated primes: 11 in D, 13 in E.
    assert 11*11 <= A_int and 11**2 <= C_int
    assert 13**2*13 <= C_int and 13 <= A_int
    primes=(2,3,5,7,11,13)
    prefix=1; prime_rows=[]
    for p in primes:
        if p>Y:
            assert p**3 <= Y*prefix
            prime_rows.append({"p":p,"p_cubed":p**3,"Y_prefix":Y*prefix})
        prefix*=p
    assert dense(Q,3,Y) and not dense(E,3,Y)
    assert not any(F(11,Y) <= v <= 11 and dense(E//v,2,Y)
                   for v in divisors(E))

    rho=F(262499,10**6); gap=F(1,10**7); rs=rho-gap
    S=F(2742997,10**7)/rs; T1=F(251,1000)/rs
    T0=2-F(3,1000)-S; eps=gap/rho; h=S/98304
    rows=[]
    for name,T in (("old",T0),("new",T1)):
        A,C=S+eps/2,T+eps/2
        L0=F(23,40)*C; Lmin=(3*A-C)/4; Lmax=3*C/5
        assert 0<Lmin<L0<Lmax and Lmin>=3*A/7
        for label,L in (("extreme_outer",Lmin),("midway",(Lmin+L0)/2),
                        ("published",L0),("earlier_3_over_5",Lmax)):
            u,v=A-L,(C+L)/4
            assert u>v and u>=2*L/3 and v>=2*L/3
            assert 4*u<=A+C and u+4*v==A+C
            assert 3*u-L<=C and L<=A
            feasible=cap_feasibility(A,C,u,v); assert feasible["feasible"]
            impossible=cap_feasibility(A,C,u+h,v+h)
            assert not impossible["feasible"]
            ur,vr=(u//h)*h,(v//h)*h
            rounding_slack=A+C-ur-4*vr
            assert 0<=rounding_slack<5*h
            rows.append({"ladder":name,"point":label,"A":str(A),"C":str(C),
                "L":str(L),"L_over_C":str(L/C),"outer_cap":str(u),"inner_cap":str(v),
                "physical_outer_cap":float(rs*u),"physical_inner_cap":float(rs*v),
                "frontier_slack":"0","cross_cap_slack":str(A+C-4*u),
                "rounded_frontier_slack":str(rounding_slack),
                "outer_gain_vs_published":float(rs*(L0-L)),
                "inner_loss_vs_published":float(rs*(L0-L)/4),
                "allocation_certificate":feasible,"joint_one_cell_increase":impossible})
    out={"status":"all exact checks passed","runtime_seconds":perf_counter()-start,
         "integer_example":{"D":D,"E":E,"gcd":gcd(D,E),"Q":Q,"Y":Y,"X":X,
            "A":A_int,"C":C_int,"cubic_checks":prime_rows,"Q_triply_dense":True,
            "E_triply_dense":False,"E_failure":{"j":2,"k":0,"target_U":11}},
         "frontier_dual_identities":[
             "A+C-u-4v=(A-u-phi(u))+(C-4v+phi(v))+(phi(u)-phi(v))",
             "A+C-4u=(A-u-phi(u))+(C-3u+phi(u))"],
         "rho_star":str(rs),"mesh":str(h),"frontier_points":rows,
         "limitations":["No physical source integral recomputed","No k=39 Rayleigh quotient computed",
                        "Largest-fragment frontier is not the entire hereditary support",
                        "No new prime-gap bound"]}
    path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({"status":out['status'],"runtime_seconds":out['runtime_seconds'],
                      "output":str(path)},indent=2))


if __name__=='__main__':
    main()
