#!/usr/bin/env python3
"""Independent normalization and marked-moment checks; floating, not enclosures."""
from pathlib import Path
import hashlib,importlib.util,json,os,sys
import numpy as np
from numpy.polynomial import Polynomial
from numpy.polynomial.legendre import leg2poly
from scipy.integrate import quad
from large_prime_sector import moment,marked_moment_scaled,partitions
HERE=Path(__file__).resolve().parent
old=Path(os.environ.get('ASTRA_PRIME_FEATURES_SOURCE',
    HERE.parents[2]/'residual-gram/general_prime_features.py'))
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('old_power_forms',old);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
M0,G0,features=module.forms(27/25,4,[(),(2,),(3,),(2,2)],order=32)
transform=np.zeros((20,20))
for group in range(4):
    for degree in range(5):
        p=Polynomial(leg2poly([0]*degree+[1]))(Polynomial([-1,2]))
        transform[group*5:group*5+len(p.coef),group*5+degree]=p.coef
now=np.load(HERE/'large_prime_sector_d4_q40.npz')
Gdiff=float(np.max(abs(now['G'][:20,:20]-transform.T@G0@transform)))
Mdiff=float(np.max(abs(now['M'][:20,:20]-transform.T@M0@transform)))
assert Gdiff<1e-10 and Mdiff<1e-10
# Independent explicit a=1 formulas: E C=log(2v), and the S2 mixed mark.
cases=[]
for v in (.50001,.6,.9,1.):
    first=float(marked_moment_scaled(1.,(),np.array([v]),48)[0]*(v-.5))
    second=float(marked_moment_scaled(1.,(2,),np.array([v]),48)[0]*(v-.5))
    exact0=np.log(2*v)
    exact2=.75*(v*v-.25)-v*(v-.5)+.5*v*v*np.log(2*v)
    assert abs(first-exact0)<1e-13 and abs(second-exact2)<1e-13
    cases.append({'a':1,'v':v,'mark_error':first-exact0,'mark_S2_error':second-exact2})
# Independently integrate t directly, without the Jacobi substitution or cached
# scaled formula. This tests a noninteger exponent and repeated labeled factors.
a=(27/25)**2
for ks in ((),(2,),(3,),(2,2),(2,2,2)):
    v=.9
    def integrand(t):
        total=0.
        for bits in range(1<<len(ks)):
            inserted=sum(k for j,k in enumerate(ks) if (bits>>j)&1)
            remaining=tuple(k for j,k in enumerate(ks) if not (bits>>j)&1)
            total+=t**inserted*moment(a,remaining)*(v-t)**sum(remaining)
        return a*v**(1-a)*(v-t)**(a-1)*total/t
    direct,error=quad(integrand,.5,v,epsabs=2e-13,epsrel=2e-13)
    jac=float(marked_moment_scaled(a,ks,np.array([v]),48)[0]*(v-.5)**a)
    assert abs(jac-direct)<2e-12
    cases.append({'a':a,'v':v,'powers':ks,'direct_t_integral':direct,'jacobi_integral':jac,
                  'difference':jac-direct,'quad_reported_error':error})
# Matrix Cauchy and nonnegative marked moment bounds on each sampled v.
for v in np.linspace(.5001,1,25):
    for ks in ((),(2,),(3,),(2,2)):
        mark=float(marked_moment_scaled(a,ks,np.array([v]),40)[0]*(v-.5)**a)
        assert -1e-14<=mark<=moment(a,ks)*v**sum(ks)+1e-13
rows=[json.loads((HERE/f'large_prime_sector_d4_q{order}.json').read_text()) for order in (20,28,40)]
spread=max(r['enlarged']['margin'] for r in rows)-min(r['enlarged']['margin'] for r in rows)
assert spread<1e-10
out={'status':'independent numerical normalization checks pass; not rigorous quadrature enclosures',
     'base_Gram_max_abs_difference':Gdiff,'base_numerator_max_abs_difference':Mdiff,
     'old_source_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),
     'marked_moment_checks':cases,'enlarged_margin_order_spread':spread}
(HERE/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
