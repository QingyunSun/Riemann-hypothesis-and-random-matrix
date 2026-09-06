"""Energy-binned bosonic model of prime-factor creation.
Upper endpoints for logarithmic bins give restricted-support lower experiments.
Numerics do not themselves prove arithmetic convergence or spectral enclosures.
"""
from __future__ import annotations
import json,time,argparse
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import LinearOperator,eigsh

def states(N):
    base=N+1;powers=[base**j for j in range(N)]
    out=[];energy=[]
    def rec(j,remain,key,used):
        if j==0:out.append(key);energy.append(used);return
        for n in range(remain//j+1):rec(j-1,remain-j*n,key+n*powers[j-1],used+j*n)
    rec(N,N,0,0)
    return out,np.asarray(energy,dtype=np.int16),powers,base

def solve(N,phi=.5):
    t=time.time();keys,E,powers,base=states(N);index={key:i for i,key in enumerate(keys)}
    x,w=roots_legendre(32);x=(x+1)/2;w=w/2
    coeff=[]
    for j in range(1,N+1):
        u=(j-1+x)/N
        coeff.append(np.sqrt(np.dot(w,4*(np.pi*phi)**2*u*np.sinc(phi*u)**2)/N))
    row=[];col=[];val=[]
    for i,key in enumerate(keys):
        for j in range(1,N-int(E[i])+1):
            nj=(key//powers[j-1])%base
            row.append(index[key+powers[j-1]]);col.append(i);val.append(coeff[j-1]*np.sqrt(nj+1))
    A=csr_matrix((val,(row,col)),shape=(len(keys),len(keys)));At=A.T
    def mv(x):
        ax=A@x;atx=At@x
        return At@ax+.5*(A@ax+At@atx)+np.pi*abs(1-2*phi)*(ax+atx)
    K=LinearOperator(A.shape,matvec=mv,dtype=float)
    eig,vec=eigsh(K,k=1,which='LA',v0=np.ones(len(keys)),tol=1e-11)
    z=vec[:,0];ev=eig[0]
    return {'N':N,'phi':phi,'dimension':len(keys),'A_nnz':A.nnz,'eigenvalue':float(ev),'margin':float(ev/(2*np.pi**2)-phi*(1-phi)),'residual':float(np.linalg.norm(mv(z)-ev*z)),'seconds':time.time()-t}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--sizes',default='12,16,20,24,28,32,36,40');a=p.parse_args();out=[]
    for n in map(int,a.sizes.split(',')):
        r=solve(n);print(json.dumps(r),flush=True);out.append(r)
    Path(__file__).with_name('boson-cutoff-results.json').write_text(json.dumps(out,indent=2))
