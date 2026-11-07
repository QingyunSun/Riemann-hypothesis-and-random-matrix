import numpy as np,json,time
from scipy.linalg import qr,solve
from pathlib import Path
D=Path(__file__).parent; a=np.load(D/'floating.npz');B=a['B'];q=a['q'];h=a['h']*.5
_,_,rows=qr(B.T,pivoting=True,mode='economic',check_finite=False);rows=rows[:964]
_,_,cols=qr(B[rows],pivoting=True,mode='economic',check_finite=False);cols=cols[:964]
free=np.array(sorted(set(range(1489))-set(cols)))
M=B[rows][:,cols]
R=solve(M,np.eye(964),check_finite=False)
res=B[rows]@h
corr=R@res
h[cols]-=corr
rho=np.linalg.norm(np.eye(964)-R@M,ord=np.inf)
print('cond',np.linalg.cond(M),'rho',rho,'corrmax',abs(corr).max(),'invnorm',np.linalg.norm(R,np.inf),'hmax',abs(h).max(),'obj',a['q']@ (a['d']*h),flush=True)
np.savez(D/'pivots.npz',rows=rows,cols=cols,free=free,R=R,h=h)
