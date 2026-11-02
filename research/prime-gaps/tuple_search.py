"""Exploratory HiGHS admissible tuple search; exact-check every returned witness.
An infeasibility status is a solver result, not a portable proof certificate.
All feasible sets of >=3 entries occupy one parity; translate and divide by two.
"""
import json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
from pathlib import Path

def primes(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]

def exact_check(a,k):
    assert len(a)==k and len(set(a))==k
    omitted={p: sorted(set(range(p))-{n%p for n in a}) for p in primes(k)}
    assert all(omitted.values())
    return {'tuple':a,'cardinality':k,'diameter':max(a)-min(a),'omitted_residues':omitted}

def search(k,diameter,seconds=60):
    n=diameter//2+1
    ps=[p for p in primes(k) if p!=2]
    nv=n+sum(ps)
    nr=len(ps)*n+len(ps)+1
    a=lil_matrix((nr,nv),dtype=float)
    lo=np.full(nr,-np.inf);hi=np.ones(nr)
    j=n;r=0
    for p in ps:
        for i in range(n):
            a[r,i]=1;a[r,j+i%p]=1;r+=1
        a[r,j:j+p]=1;lo[r]=hi[r]=1;r+=1;j+=p
    a[r,:n]=1;lo[r]=hi[r]=k
    t=time.monotonic()
    result=milp(np.r_[np.arange(n)*1e-8,np.zeros(nv-n)],integrality=np.ones(nv),bounds=Bounds(np.zeros(nv),np.ones(nv)),constraints=LinearConstraint(a.tocsc(),lo,hi),options={'time_limit':seconds,'mip_rel_gap':0,'presolve':True})
    out={'k':k,'diameter_bound':diameter,'seconds':time.monotonic()-t,'status':int(result.status),'message':result.message}
    if result.x is not None:
        a=[2*i for i in range(n) if result.x[i]>.5]
        if len(a)==k:
            out['witness']=exact_check(a,k)
    return out

if __name__=='__main__':
    published=[0,2,6,12,20,26,30,32,36,42,48,50,56,60,68,72,78,86,90,92,98,102,110,116,120,126,132,138,140,146,152,156,158,162,168,170,176,180,182,186]
    results={'published':exact_check(published,40),'drop_two':exact_check(published[2:],38),'runs':[]}
    for k,d in [(39,180),(40,184),(39,178),(38,176)]:
        out=search(k,d,90);results['runs'].append(out);print(json.dumps(out),flush=True)
        Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2))
