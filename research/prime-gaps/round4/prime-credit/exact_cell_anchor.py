#!/usr/bin/env python3
"""Small, rigorous nonzero alpha anchor. No floating-point proof steps.

This intentionally weak bound is a normalization/ownership check, not the ppm
certificate sought by the full positive-kernel contraction.
"""
from fractions import Fraction as F
from pathlib import Path
import json,math,time,hashlib
from alpha_credit import exact_inputs,OUT


def g(t):return F(21,200)/(1+t/100)+F(179,200)/(1+F(907,5)*t)

def ceiling(q):return -((-q.numerator)//q.denominator)

def power10(e):return F(10**e) if e>=0 else F(1,10**(-e))

def main():
    start=time.monotonic();inputs,mat,sigs=exact_inputs();h=F(inputs['layout']['grid_step']);row=inputs['source_ladders']['new'][24]
    S=F(inputs['trial']['source_geometry']['parameters']['S'])
    # Since g^2 decreases, h Z ≤ h + integral_0^S g(t)^2 dt.
    M=4096;scale=10**24
    riemann=h+S/M*sum(ceiling(g(j*S/M)**2*scale) for j in range(M))/scale
    norm_upper=F(22,1000)
    assert riemann<norm_upper
    seed,pl,ql=900,27500,34000
    width=h/10
    assert seed*h+width<18800*h<pl*h
    assert (pl+ql+F(3,2)*pl)*h>row['A']
    assert F(3,2)*(pl*h+width)<row['owner_plateau']
    assert pl*h>row['xi']
    assert 40*seed+pl+ql<98264
    assert (40*seed+pl+ql)*h>row['a']
    # Each owner total remains in one official cell, so F is exactly constant.
    assert 3*width<h
    raw=[]
    for owner in ('distinct','same'):
        indices=[seed]*40;indices[0]+=pl;indices[1 if owner=='distinct' else 0]+=ql
        mids=[(F(j)+F(1,2))*h for j in indices]
        radial=sum(mids)-F(9,10)
        powers={p:sum(t**p for t in mids) for p in range(2,7)}
        poly=F(0)
        for cs,sig in zip(mat,sigs):
            val=F(cs[-1],10**10)
            for c in reversed(cs[:-1]):val=val*radial+F(c,10**10)
            for p in sig:val*=powers[p]
            poly+=val
        assert poly!=0
        value=poly*math.prod(g(t) for t in mids)
        count=40*39 if owner=='distinct' else 40
        lower=count*value**2*width**40/F(10*pl+1)/F(10*ql+1)
        raw.append(lower)
    Iupper=F(23685317890,10**24)
    ratio=sum(raw)/(norm_upper**40*Iupper)
    exponent=-1
    while power10(exponent)>ratio:exponent-=1
    assert power10(exponent)<=ratio<power10(exponent+1)
    out={'status':'exact rational positive lower bound proved',
         'alpha_over_published_I_upper_lower':str(power10(exponent)),
         'scientific_lower':f'1e{exponent}',
         'purpose':'Strict positivity and normalization anchor only; far too small to improve a useful sieve margin.',
         'hZ_upper':str(norm_upper),'hZ_rational_Riemann_upper':str(riemann),
         'official_grid_step':str(h),'seed_interval_cells':[str(seed),str(F(seed)+F(1,10))],
         'p_interval_cells':[str(pl),str(F(pl)+F(1,10))],'q_interval_cells':[str(ql),str(F(ql)+F(1,10))],
         'radial_index_sum':40*seed+pl+ql,'owner_counts':[1560,40],
         'elapsed_seconds':time.monotonic()-start}
    (OUT/'exact_cell_anchor.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
