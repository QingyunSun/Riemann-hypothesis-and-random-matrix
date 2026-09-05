#!/usr/bin/env python3
"""Exact positive failure rectangle + outward official-grid contraction.

Default --self-test uses integers/Fractions only and never imports FLINT.
--certify requires the official signed convolution regression to pass. All writes
are beside this file; the official source is imported read-only without changes.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json, math, sys, time
from fractions import Fraction as F
from pathlib import Path
from alpha_credit import SOURCE, OUT, exact_inputs, json_exact

B=18800
P=(26400,29100)
Q=(32400,36700)
N=98264


def box_cell_numerators(offset:int,widths:tuple[int,...],length:int):
    """d! times volume of {0≤x_i≤w_i: j≤offset+Σx_i<j+1}."""
    d=len(widths)
    shifts=[(offset+sum(w for bit,w in zip(bits,widths) if bit),(-1)**sum(bits))
            for bits in itertools.product((0,1),repeat=d)]
    def cumulative(j):return sum(sign*max(0,j-shift)**d for shift,sign in shifts)
    prev=cumulative(0);out=[]
    for j in range(length):
        nxt=cumulative(j+1);out.append(nxt-prev);prev=nxt
    return out


def kernels():
    # Arrays are the cell mass / h, with constant densities 1/p_upper,1/q_upper.
    u=[1 if j<B else 0 for j in range(N)]
    vp=box_cell_numerators(P[0],(P[1]-P[0],B),N)
    vq=box_cell_numerators(Q[0],(Q[1]-Q[0],B),N)
    vpq=box_cell_numerators(P[0]+Q[0],(P[1]-P[0],Q[1]-Q[0],B),N)
    return (u,vp,vq,vpq),(1,2*P[1],2*Q[1],6*P[1]*Q[1])


def self_test():
    inputs,_,_=exact_inputs();h=F(inputs['layout']['grid_step']);row=inputs['source_ladders']['new'][24]
    assert 0<B<P[0]<P[1]<Q[0]<Q[1]<=46580
    assert P[0]*h>row['xi']
    assert F(3,2)*P[1]*h<row['owner_plateau']
    assert (Q[0]+F(5,2)*P[0])*h>row['A']
    assert row['index']==24 and row['source_order']==3
    first_r=row['a']//h+1
    assert (first_r-1)*h<=row['a']<first_r*h
    arrays,den=kernels()
    for a in arrays:assert min(a)>=0 and len(a)==N
    expected=[B,2*B*(P[1]-P[0]),2*B*(Q[1]-Q[0]),6*B*(P[1]-P[0])*(Q[1]-Q[0])]
    assert [sum(a) for a in arrays]==expected
    # Independent small-volume check: known sum-of-two-unit-uniform cell masses.
    assert box_cell_numerators(0,(1,1),4)==[1,1,0,0]
    assert box_cell_numerators(0,(1,1,1),5)==[1,4,1,0,0]
    # Total marking-ring coefficient = k same-owner + k(k-1) distinct-owner.
    masses=[F(sum(a),d) for a,d in zip(arrays,den)]
    ordinary,first,second,both=masses
    assert both==first*second/ordinary
    ring=[F(1),F(0),F(0),F(0)]
    for _ in range(40):
        a,x,y,xy=ring;u,v,w,vw=masses
        ring=[a*u,x*u+a*v,y*u+a*w,xy*u+a*vw+x*w+y*v]
    expected_both=40*both*ordinary**39+40*39*first*second*ordinary**38
    assert ring[3]==expected_both
    result={'status':'integer geometry and kernel invariants passed','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'grid_step':str(h),'B':B,'P':P,'Q':Q,'first_accepted_radial_index':int(first_r),'last_accepted_radial_index':N-1,
            'failure_margin':str((Q[0]+F(5,2)*P[0])*h-row['A']),
            'kernel_denominators':den,'kernel_numerator_sums':expected,
            'kernel_nonnegative':True,'exact_mass_conservation':True,'owner_factor_test':True,
            'kernel_sha256':[hashlib.sha256(','.join(map(str,a)).encode()).hexdigest() for a in arrays]}
    return result,arrays,den


def certify(bits=224,threads=1):
    start=time.monotonic();check,arrays,den=self_test()
    spec=importlib.util.spec_from_file_location('official_prime186',SOURCE)
    official=importlib.util.module_from_spec(spec);sys.modules[spec.name]=official;spec.loader.exec_module(official)
    # CapEngine executes the unmodified mandatory signed-FFT check on entry.
    engine=official.CapEngine(intervals=98304,precision=160,fixed_bits=bits,arb_threads=threads)
    print(json.dumps({'event':'signed_regression_passed','elapsed_seconds':time.monotonic()-start}),flush=True)
    raw=[]
    for a,d in zip(arrays,den):
        raw.append(tuple(weight*official.rational(F(v,d)) for v,weight in zip(a,engine.coordinate_weights)))
    jets=official.SourceJets(tuple(raw),engine.midpoints,bits=bits,ring='palm')
    mask=official.np.zeros(engine.n,dtype=bool)
    mask[check['first_accepted_radial_index']:]=True
    answer=official.arb(0);parts=[]
    for signature,polynomial in engine.square_groups:
        signed=official.float_interval(engine.radial_polynomial(polynomial))
        moment=jets.rows(40,signature,channel='both').binary64_intervals()
        term=official.outward_sum(official.interval_multiply(signed,moment),mask)
        answer+=term
        part={'signature':signature,'term_interval':official._driver_interval(term),'running_interval':official._driver_interval(answer)}
        parts.append(part)
        print(json.dumps({'event':'signature_completed','signature':signature,'running':str(answer),'elapsed_seconds':time.monotonic()-start}),flush=True)
    # The signed sum is the nonnegative square of one coherent lower measure.
    # Never declare an approximate positive value to be an outward lower bound.
    interval=official._driver_interval(answer)
    lower=F(interval['lower']);upper=F(interval['upper'])
    assert lower<=upper
    I_upper=F(23685317890,10**24)
    hybrid=engine.rho_star*4*abs(F(official.DERIVED_INPUTS['hybrid']['b']))
    coefficient=1-hybrid
    result={'status':'certified positive alpha lower endpoint' if lower>0 else 'outward contraction inconclusive',
            'geometry':check,'signed_regression_passed':True,'fixed_bits':bits,'arb_precision_bits':160,'threads':threads,
            'alpha_rectangle_normalized_interval':interval,'alpha_over_published_I_upper_lower':str(max(F(0),lower)/I_upper),
            'credit_over_published_I_upper_lower':str(coefficient*max(F(0),lower)/I_upper),
            'alpha_credit_coefficient':str(coefficient),'parts':parts,'elapsed_seconds':time.monotonic()-start,
            'scope':'New lower-bound rectangle for published k40 trial. Published cap/loss endpoints are source-inherited, not recomputed here.'}
    (OUT/'alpha_rectangle_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('parts','geometry')},indent=2))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--certify',action='store_true');ap.add_argument('--bits',type=int,default=224);ap.add_argument('--threads',type=int,default=1)
    args=ap.parse_args()
    if args.certify:certify(args.bits,args.threads)
    else:
        result,_,_=self_test();(OUT/'alpha_rectangle_kernel_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
