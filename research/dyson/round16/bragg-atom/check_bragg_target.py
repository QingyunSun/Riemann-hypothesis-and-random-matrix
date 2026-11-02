#!/usr/bin/env python3
"""Bounded R16 normalization checks, not a computation of actual zeta zeros.
Run: python3 check_bragg_target.py
Requires NumPy and SymPy. Seed quadrature is floating, not an enclosure.
"""
from __future__ import annotations
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
import sympy as s


def exact_checks() -> dict:
    ell = F(1,4)
    triangle = F(4,3)*(1+ell)+ell**3/12-ell/3-F(1,4)*(1-ell-ell**2)
    assert triangle == F(1085,768)
    eps = F(1,4)
    exponents = [1-1/(2-eps),1-1/(2+eps)]
    assert exponents == [F(3,7),F(5,9)]
    nuisance = [F(1,2)-1/(2-eps),F(0),F(1,2)-1/(2+eps)]
    assert nuisance == [-F(1,14),F(0),F(1,18)]
    # Independent exact autocorrelation check, using a polynomial seed only as
    # an algebraic regression. It is NOT substituted for the C-infinity seed.
    x,v=s.symbols('x v',real=True)
    f=(1-4*x*x)**2
    s2=s.integrate(f*f,(x,-s.Rational(1,2),s.Rational(1,2)))
    psi=s.expand(s.integrate(f*(1-4*(x-v)**2)**2,(x,v-s.Rational(1,2),s.Rational(1,2)))/s2)
    assert s.simplify(psi.subs(v,0)-1)==0
    assert s.simplify(psi.subs(v,1))==0
    m0=s.integrate(2*psi,(v,0,1))
    m1=s.integrate(2*v*psi,(v,0,1))
    assert m0==s.integrate(f,(x,-s.Rational(1,2),s.Rational(1,2)))**2/s2
    assert 0<m1<m0<1
    z=s.symbols("z",positive=True)
    leading_mass=s.integrate(z,(z,0,1))+s.integrate(z**-3,(z,1,s.oo))
    log_correction=s.integrate(z*s.log(z),(z,0,1))+s.integrate(z**-3*s.log(z),(z,1,s.oo))
    assert leading_mass==1 and log_correction==0
    tt=s.symbols("tt",real=True)
    assert s.simplify(1/(s.Rational(3,2)-s.I*tt)+1/(s.Rational(1,2)+s.I*tt)
        -2/((s.Rational(3,2)-s.I*tt)*(s.Rational(1,2)+s.I*tt)))==0
    for k in range(-20,21):
        assert s.cos(4*s.pi*s.Rational(k,2))==1
    assert 1-s.cos(4*s.pi*s.Rational(1,4))==2
    return {'triangle_candidate_ell_1_over_4':str(triangle),
            'shift_exponents_epsilon_1_over_4':[str(t) for t in exponents],
            'nuisance_power_relative_to_X':[str(t) for t in nuisance],
            'polynomial_seed_regression':{'seed':'(1-4*x^2)^2 on [-1/2,1/2]',
              'scope':'Algebra check only; main theorem uses the fixed C-infinity seed.',
              's2':str(s2),'psi_on_0_1':str(psi),'m0':str(m0),'m1':str(m1)},
            'diagonal_leading_weight_mass':str(leading_mass),
            'diagonal_log_correction':str(log_correction),
            'continuous_mean_denominator_identity':'PASS',
            'half_lattice_cosine_exact_cases':41,'status':'PASS'}


def floating_seed(order:int)->dict:
    z,w=leggauss(order)
    x=z/2; w=w/2
    f=np.exp(-1/(1-4*x*x))
    norm=float(np.dot(w,f*f)); m0=float(np.dot(w,f)**2/norm)
    # Triangular x,y domain avoids the |x-y| kink in quadrature.
    y=-.5+(x[:,None]+.5)*(z[None,:]+1)/2
    wy=(x[:,None]+.5)*w[None,:]
    fy=np.exp(-1/(1-4*y*y))
    m1=float(2*np.dot(w*f,np.sum(wy*(x[:,None]-y)*fy,axis=1))/norm)
    # A deliberately finite synthetic zero configuration tests both normalizations.
    # It is not a zeta dataset or asymptotic model for zeta.
    T=100.; L=np.log(T)/(2*np.pi); N=T*L
    ordinates=1+np.array([0,1/3,7/6,9/4])/L
    du=L*(ordinates[:,None]-ordinates[None,:])
    pairweight=4/(4+(ordinates[:,None]-ordinates[None,:])**2)/N
    eps=.25; b=2.
    alpha=b+eps*(x[:,None]-x[None,:])
    direct=np.zeros_like(alpha)
    for i in range(len(ordinates)):
        for j in range(len(ordinates)):
            direct += pairweight[i,j]*np.cos(2*np.pi*alpha*du[i,j])
    cb_direct=float(eps*np.sum((w*f)[:,None]*(w*f)[None,:]*direct)/norm)
    hatf=np.sum((w*f)[:,None,None]*np.exp(-2j*np.pi*x[:,None,None]*eps*du[None,:,:]),axis=0)
    kernel=eps*np.abs(hatf)**2/norm
    cb_pair=float(np.sum(pairweight*kernel*np.cos(2*np.pi*b*du)))
    c0=float(np.sum(pairweight*kernel))
    defect=float(np.sum(pairweight*kernel*(1-np.cos(4*np.pi*du))))
    assert abs(cb_direct-cb_pair)<1e-13
    assert abs(c0-cb_pair-defect)<1e-13
    assert defect>=0 and cb_pair>=-1e-14
    return {'order':order,'s2':norm,'m0':m0,'m1':m1,
            'epsilon_1_over_4':{'AH_and_RH_upper':1+m1/16,
                'sine_prediction':m0/4,'atomic_prime_diagonal':m0/2,
                'strict_deficit_required_for_bound_below_one':m1/16,
                'centered_prime_remainder_upper_target':1-m0/2},
            'synthetic_finite_sum_check':{'T':T,'normalized_offsets':[0,1/3,7/6,9/4],
                'cb_direct_double_integral':cb_direct,'cb_fourier_pair':cb_pair,
                'c0':c0,'defect':defect,'absolute_identity_error':abs(cb_direct-cb_pair)},
            'status':'PASS','certification':'floating quadrature only; no interval enclosure'}


def main()->None:
    out={'exact':exact_checks(),'floating':[floating_seed(n) for n in (64,128,192)],
         'status':'PASS','scope':'Normalization and exact rational source checks only. No zeta upper target is tested or proved.'}
    for key in ('m0','m1'):
        err=abs(out['floating'][-1][key]-out['floating'][-2][key])
        assert err<1e-12
    out['floating_refinement_max_change']=max(abs(out['floating'][-1][k]-out['floating'][-2][k]) for k in ('m0','m1'))
    p=Path(__file__).with_name('bragg_checks.json');p.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS','exact_triangle_bound':out['exact']['triangle_candidate_ell_1_over_4'],
                     'm0_floating':out['floating'][-1]['m0'],'m1_floating':out['floating'][-1]['m1'],
                     'refinement_change':out['floating_refinement_max_change']},sort_keys=True))

if __name__=='__main__':
    main()
