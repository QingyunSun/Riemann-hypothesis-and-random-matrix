import json,time
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from scipy.optimize import linprog
from flint import arb,acb,ctx
from base import summary_fibres,matching_complements,partitions,is_survivor
OUT=Path(__file__).parent
N=11; M=22
pairs=matching_complements(N,summary_fibres(N));configs=np.array(pairs).reshape(-1,N)
z=np.exp(2j*np.pi*np.arange(M)/M)
power=np.array([np.sum(z[(k*configs)%M],axis=1) for k in range(M)])
rows=[];labels=[]
for k in range(1,N+1):
 ps=partitions(k)
 prod=np.array([np.prod(power[list(part)],axis=0) for part in ps])
 for j,a in enumerate(ps):
  for t,b in enumerate(ps[j:],j):
   if (len(a)+len(b))%2==0:continue
   val=2*(prod[j]*prod[t].conj()).real
   rows.append(val[1::2]-val[::2]);labels.append((a,b))
A=np.array(rows);print('matrix',A.shape,flush=True)

def orbit(s):return len({tuple(sorted((f*i+j)%M for i in s)) for f in (1,-1) for j in range(M)})
q=np.array([orbit(a)*np.prod([abs(z[x]-z[y])**2 for x in a for y in a if x<y])/M**N for a,b in pairs])
ctx.prec=144
rr=[acb(arb(j)/N).exp_pi_i() for j in range(M)]
heat=[(arb(85)/84)**(j*(N-j)) for j in range(N+1)]
d=np.array([is_survivor(b,rr,heat)-is_survivor(a,rr,heat) for a,b in pairs],float)
print('mass total',2*q.sum(),'min',q.min(),'max',q.max(),flush=True)
B=A*q
scale=np.linalg.norm(B,axis=1);B=B/scale[:,None]
t=time.time();u,s,vt=svd(B,full_matrices=False,check_finite=False,lapack_driver='gesdd')
print('svd seconds',time.time()-t,'singular',s[[0,963,964,-1]].tolist(),flush=True)
E=vt[:964];c=q*d
sol=linprog(-c,A_eq=E,b_eq=np.zeros(964),bounds=(-1,1),method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
print('LP',sol.success,sol.message,'obj',-sol.fun if sol.success else None,flush=True)
if sol.success:
 h=sol.x
 report={'status':'floating optimization, awaiting certification','paired_orbit_mass':float(2*q.sum()),'min_orbit_mass':float(q.min()),'max_orbit_mass':float(q.max()),'singular_values':[float(s[i]) for i in [0,963,964,-1]],'survival_probability_shift':float(c@h),'max_scaled_constraint_residual':float(abs(B@h).max()),'box_min':float(h.min()),'box_max':float(h.max()),'original_matrix_rows':len(A),'number_variables':len(q)}
 np.savez(OUT/'floating.npz',q=q,d=d,A=A,B=B,E=E,h=h,s=s,configs=configs,labels=np.array([str(x) for x in labels]))
 (OUT/'floating.json').write_text(json.dumps(report,indent=2));print(report,flush=True)
