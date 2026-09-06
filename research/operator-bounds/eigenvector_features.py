"""Fit finite arithmetic Perron vector with transparent symmetric features.
No asymptotic inference; held coefficients measured by exact finite operator.
"""
import sys,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import lstsq
sys.path.insert(0,str(Path(__file__).parents[2]/'research/residual-gram'))
from arithmetic_operator import prime_powers,make_A

base=Path(__file__).parents[2]
z=np.load(base/'research/residual-gram/arithmetic-eigenvector.npz');L=int(z['L']);x=z['x'];x*=np.sign(x[0]);n=np.arange(1,L+1);v=np.log(n)/np.log(L)
pp=list(prime_powers(L));S2=np.zeros(L);S3=np.zeros(L);S4=np.zeros(L);largest=np.zeros(L);omega=np.zeros(L)
for p,e in pp:
    if e==1:
        u=np.log(p)/np.log(L);S2[p-1::p]+=u*u;S3[p-1::p]+=u**3;S4[p-1::p]+=u**4;largest[p-1::p]=u;omega[p-1::p]+=1
A=make_A(L);At=A.T
def K(y):
    ay=A@y;aty=At@y
    return At@ay+.5*(A@ay+At@aty)
true=float(x@K(x));results=[]
for ell in (1.,1.08,1.1763):
    d=np.ones(L)
    for p,e in pp:d[p-1::p]*=(ell+e-1)/e
    wt=d/np.sqrt(n)
    for label,features in [('mass_only',[np.ones(L)]),('symmetric_powers',[np.ones(L),S2,S3,S4]),('plus_largest',[np.ones(L),S2,S3,S4,largest,largest**2]),('plus_omega',[np.ones(L),S2,S3,S4,largest,largest**2,omega,omega**2])]:
        F=np.column_stack([wt*feature*v**i for feature in features for i in range(5)])
        coef,_,rank,_=lstsq(F,x,cond=1e-11,lapack_driver='gelsd');y=F@coef
        row={'ell':ell,'features':label,'rank':int(rank),'l2_error':float(np.linalg.norm(x-y)),'rayleigh':float(y@K(y)/(y@y)),'deficit_from_finite_max':float(true-y@K(y)/(y@y))}
        results.append(row);print(json.dumps(row),flush=True)
        del F
Path(__file__).with_name('eigenvector-feature-results.json').write_text(json.dumps({'L':L,'true_eigenvalue':true,'fits':results},indent=2))
