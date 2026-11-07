"""Certify a positive 11-root tilt around a fixed binary64 approximate solution.

All ball calculations use 160-bit Arb. Numerical LP coefficients are treated as
exact dyadic rationals. The final weights are defined by an exact linear solve.
"""
from pathlib import Path
import json,time,hashlib
import numpy as np
from flint import acb,arb,arb_mat,ctx
from scipy.linalg import solve
from base import matching_complements,summary_fibres,is_survivor,sha256_serialized,odd_even_dimension
D=Path(__file__).parent
ctx.prec=160
data=json.loads((D/'candidate.json').read_text())
n=11;m=22
character_traces,dimension=odd_even_dimension(n)
assert character_traces==[3956,106,22,184] and dimension==964
pairs=matching_complements(n,summary_fibres(n))
assert sha256_serialized(pairs)=='9d4eaf8488c59fe8854a610a651912763ed89141bece84d2630ea59302ee902e'
labels=[(tuple(a),tuple(b)) for a,b in data['independent_constraints']]
cols=np.array(data['dependent_coordinates'],dtype=int)
h=np.array([float.fromhex(x) for x in data['candidate_relative_changes_hex']])
scales=[arb(float.fromhex(x)) for x in data['row_scales_hex']]
N=len(labels)
assert all(0<sum(a)==sum(b)<=11 and (len(a)+len(b))%2==1 for a,b in labels)
assert all(j>=1 for a,b in labels for j in a+b)
assert all(scale>0 for scale in scales)
assert np.all(np.isfinite(h))
assert len(set(cols))==N==964 and len(h)==len(pairs)==1489
roots=[acb(arb(k)/n).exp_pi_i() for k in range(m)]
S=[a for a,b in pairs]
trace=[[sum((roots[(j*k)%m] for k in s),acb(0)) for s in S] for j in range(n+1)]
def orbit(s):return len({tuple(sorted((sign*i+j)%m for i in s)) for sign in (-1,1) for j in range(m)})
factors=[4*(arb(k)/m*arb.pi()).sin()**2 for k in range(m)]
weights=[]
for s in S:
 w=arb(orbit(s))/m**n
 for i,x in enumerate(s):
  for y in s[i+1:]:w*=factors[y-x]
 weights.append(w)
assert all(q>0 for q in weights)
print('weights built',flush=True)
parts={p for label in labels for p in label};prod={}
for p in parts:
 v=[acb(1) for _ in S]
 for j in p:v=[x*y for x,y in zip(v,trace[j])]
 prod[p]=v
col_order=list(map(int,cols));hs=list(map(arb,map(float,h)))
C=arb_mat(N,N);res=arb_mat(N,1)
start=time.time()
for ri,(a,b) in enumerate(labels):
 row=[-4*(u*v.conjugate()).real*q/scales[ri] for u,v,q in zip(prod[a],prod[b],weights)]
 for cj,k in enumerate(col_order):C[ri,cj]=row[k]
 res[ri,0]=sum((x*y for x,y in zip(row,hs)),arb(0))
 if ri%200==0:print('rows',ri,time.time()-start,flush=True)
print('matrix filled',time.time()-start,flush=True)
Cmid=np.array([[float(C[i,j].mid()) for j in range(N)] for i in range(N)])
R0=solve(Cmid,np.eye(N),check_finite=False)
R=arb_mat([[arb(float(x)) for x in row] for row in R0])
err=arb_mat(N,N)
for j in range(N):err[j,j]=1
err-=R*C
rho=max(sum((abs(err[i,j]) for j in range(N)),arb(0)).upper() for i in range(N))
assert rho<1,rho
rr=R*res
eta=max(abs(rr[i,0]).upper() for i in range(N))
epsilon=eta/(1-rho)
assert epsilon<arb('0.000001'),epsilon
# Define h* by fixing free dyadics and solving the exact dependent system.
# The pointwise correction on dependent components is bounded by epsilon.
hbound=arb(float(abs(h).max()))+epsilon
assert hbound<1
heat=[(arb(85)/84)**(j*(n-j)) for j in range(n+1)]
d=[is_survivor(b,roots,heat)-is_survivor(a,roots,heat) for a,b in pairs]
assert d==data['survival_differences']
assert sha256_serialized(d)=='cc3db78a40ea6d36b8f21c45ab7394f54612c38986283a043e87f587b8517a5b'
obj=sum((q*arb(int(label))*x for q,label,x in zip(weights,d,hs)),arb(0))
objerr=epsilon*sum((weights[j]*abs(int(d[j])) for j in cols),arb(0))
lower=(obj-objerr).lower()
assert lower>arb('0.0088')
gain=arb(99)/50
assert gain*hbound<1
assert gain*lower>arb('0.0175')
record={
 'certificate':'strict positive probability law with exact moment preservation',
 'precision_bits':ctx.prec,
 'constraint_rank':N,
 'protected_involution_traces':character_traces,
 'pair_count':len(S),
 'rho_upper':str(rho),'preconditioned_residual_upper':str(eta),
 'dependent_correction_linf_upper':str(epsilon.upper()),
 'relative_density_change_linf_upper':str(hbound.upper()),
 'survival_probability_shift_lower':str(lower),
 'survival_probability_shift_upper':str((obj+objerr).upper()),
 'simple_certified_lower_bound':'0.0088',
 'magnification':'99/50',
 'magnified_lower_bound':str((gain*lower).lower()),
 'magnified_upper_bound':str((gain*(obj+objerr)).upper()),
 'magnified_relative_change_bound':str((gain*hbound).upper()),
 'magnified_simple_lower_bound':'0.0175',
 'selected_orbit_mass':str((2*sum(weights,arb(0)))),
 'sample_approximation_sha256':hashlib.sha256((D/'candidate.json').read_bytes()).hexdigest(),
 'elapsed_seconds':time.time()-start,
 'exact_definition':'Keep the free coordinates equal to stored dyadic h; solve selected 964 protected equations for dependent coordinates. Add q_i h_i to B_i and subtract from A_i.'}
(D/'certificate.json').write_text(json.dumps(record,indent=2));print(json.dumps(record,indent=2),flush=True)
