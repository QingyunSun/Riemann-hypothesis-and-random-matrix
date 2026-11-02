#!/usr/bin/env python3
"""Exact Sturm certificate and symbolic marked-depth counterexample.

Run with Python 3 and SymPy; writes JSON next to this file. No numerical
integration or critical-line Dirichlet expansion occurs in this check.
"""
from __future__ import annotations

import json
from pathlib import Path
from time import perf_counter

import sympy as sp


def main() -> None:
    start = perf_counter()
    x, s = sp.symbols("x s")
    initial = sp.expand(x * (x*x-1) * ((x-100)**2-sp.Rational(121,400)))
    heat = sp.expand(sum(s**j*sp.diff(initial,x,2*j)/sp.factorial(j) for j in range(3)))
    disc = sp.Poly(sp.discriminant(heat,x),s)
    lo, hi = sp.Rational(151,1000), sp.Rational(19,125)
    narrow_lo, narrow_hi = sp.Rational(12999,85936), sp.Rational(53965,356761)
    assert disc.count_roots(0,lo) == 0
    assert disc.count_roots(lo,hi) == 1
    assert disc.count_roots(narrow_lo,narrow_hi) == 1
    assert lo < narrow_lo < narrow_hi < hi
    assert sp.gcd(disc,disc.diff()).degree() == 0
    assert all(disc.eval(t) != 0 for t in (0,lo,hi,narrow_lo,narrow_hi))
    boundary_counts = {
        str(b): int(sp.Poly(heat.subs(x,b),s).count_roots(0,hi))
        for b in (-2,2,98,102)
    }
    assert all(value == 0 for value in boundary_counts.values())
    root_counts = []
    for t, expected in ((0,(3,2,5)),(lo,(3,2,5)),(hi,(3,0,3))):
        poly = sp.Poly(heat.subs(s,t),x)
        counts = tuple(int(poly.count_roots(a,b)) for a,b in
                       ((-2,2),(98,102),(-sp.oo,sp.oo)))
        assert counts == expected
        root_counts.append({"s":str(t),"cluster":counts[0],
                            "isolated_pair":counts[1],"all_real":counts[2]})

    # N=2 Cayley phases have half-separation atan(b)-atan(a).
    # Lambda(a,b)=log((1+a*b)/sqrt((1+a*a)*(1+b*b))) for 0<a<b.
    a,b,e = sp.symbols("a b e",positive=True)
    lam = sp.log((1+a*b)/sp.sqrt((1+a*a)*(1+b*b)))
    chi_small = (b-a)/((1+a*b)*(1+a*a))
    chi_large = -(b-a)/((1+a*b)*(1+b*b))
    assert sp.simplify(sp.diff(lam,a)-chi_small) == 0
    assert sp.simplify(sp.diff(lam,b)-chi_large) == 0
    cs,cl = [sp.factor(v.subs({a:e,b:1-e})) for v in (chi_small,chi_large)]
    assert sp.limit(cs,e,0,dir="+") == 1
    assert sp.limit(cl,e,0,dir="+") == -sp.Rational(1,2)
    marked_rows = []
    for eps in (sp.Rational(1,10),sp.Rational(1,100),sp.Rational(1,10**6)):
        marked_rows.append({"epsilon":str(eps),"inverse_small":str(1/eps),
                            "chi_small":str(sp.N(cs.subs(e,eps),30)),
                            "chi_large":str(sp.N(cl.subs(e,eps),30))})
    result = {
        "status":"exact rational Sturm and exact symbolic checks passed",
        "sympy_version":sp.__version__,
        "flow":"H_s=exp(s*d_x^2)P, s >= 0 is attractive root motion",
        "initial_polynomial":str(initial),"heat_polynomial":str(heat),
        "discriminant_coefficients_descending":[str(c) for c in disc.all_coeffs()],
        "discriminant_squarefree":True,
        "first_collision_interval":[str(narrow_lo),str(narrow_hi)],
        "interval_decimals":[str(sp.N(t,30)) for t in (narrow_lo,narrow_hi)],
        "sturm_counts":{"zero_to_lo":0,"lo_to_hi":1,"narrow_interval":1},
        "boundary_root_counts":boundary_counts,"real_root_counts":root_counts,
        "minimum_initial_gap":"1","first_colliding_initial_gap":"11/10",
        "missing_gap_correction":"21/800",
        "marked_lambda":str(lam),"marked_chi_small":str(cs),"marked_chi_large":str(cl),
        "marked_limits":{"chi_small":"1","chi_large":"-1/2","inverse_small":"+infinity"},
        "marked_examples":marked_rows,
        "elapsed_seconds":perf_counter()-start,
        "limitations":"Exact CAS arithmetic certificate, not a Lean/Isabelle formal proof. No global zeta conclusion."
    }
    output=Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":result["status"],"output":str(output),
                      "elapsed_seconds":result["elapsed_seconds"]},indent=2))


if __name__ == "__main__":
    main()
