"""Exploratory resummed symmetric prime-factor profiles for the Inoue diagonal form.
No arithmetic asymptotic transfer or outward numerical certificate is claimed.
r(n) ~ d_ell(n) prod_p g(logp/logL) f(logn/logL), g=exp(sum c_k u^k).
The density factor H(v)=E_PD exp(2 sum c_k S_k) is computed by exact formal
power-series recurrence evaluated in floating arithmetic; truncation is checked.
"""
from pathlib import Path
import sys,json,time
import numpy as np
from scipy.special import roots_jacobi,eval_jacobi,beta
from scipy.linalg import eigh
from scipy.optimize import differential_evolution,minimize
from functools import lru_cache


def basis(x,d,a):
 x=np.asarray(x).ravel()
 return np.array([np.sqrt(2*n+a)*eval_jacobi(n,0,a-1,2*x-1) for n in range(d+1)]).T

@lru_cache(256)
def density_coeffs(a,cs,nmax=100):
 # g^2=exp(2 sum c_k u^k), series d_n.
 d=np.zeros(nmax+1);d[0]=1
 for n in range(1,nmax+1):
  d[n]=sum(2*k*c*d[n-k] for k,c in enumerate(cs,2) if k<=n)/n
 h=np.zeros(nmax+1);h[0]=1
 for n in range(1,nmax+1):
  k=np.arange(1,n+1)
  h[n]=a/n*np.dot(k*d[1:n+1]*beta(k,a+n-k),h[n-1::-1])
 return h

def density(v,a,cs):
 h=density_coeffs(a,tuple(cs));out=np.polynomial.polynomial.polyval(v,h)
 low=np.polynomial.polynomial.polyval(v,h[:81])
 if np.any(out<=0) or np.max(np.abs(out-low)/(1+np.abs(out)))>1e-7:
  raise ArithmeticError('Unstable/truncated density series')
 return out

def profile(u,cs):return np.exp(sum(c*u**k for k,c in enumerate(cs,2)))

def matrices(ell,cs,degree=5,order=24,phi=.5):
 a=ell**2
 vx,vw=roots_jacobi(order,0,a-1);v=(vx+1)/2;vw=vw/2**a
 vw=vw*density(v,a,cs)
 zx,zw=roots_jacobi(order,0,0);z=(zx+1)/2;zw=zw/2
 F=basis(v,degree,a);G=F.T@(vw[:,None]*F)
 V,X,Y=np.meshgrid(v,z,z,indexing='ij');Wv,Wx,Wy=np.meshgrid(vw,zw,zw,indexing='ij')
 U=(1-V)*X;W=(1-V)*(1-X)*Y
 wt=(Wv*Wx*Wy*(1-V)**2*(1-X)*np.pi**2*phi**2*np.sinc(phi*U)*np.sinc(phi*W)*profile(U,cs)*profile(W,cs)).ravel()
 F0=basis(V,degree,a);F1=basis(V+U,degree,a);F2=basis(V+W,degree,a);F12=basis(V+U+W,degree,a)
 M2=(F0.T@(wt[:,None]*F12)+F1.T@(wt[:,None]*F2))*2*a/np.pi**2
 V,Z=np.meshgrid(v,z,indexing='ij');Wv,Wz=np.meshgrid(vw,zw,indexing='ij');U=(1-V)*Z;wt=Wv*Wz*(1-V)
 F0=basis(V,degree,a);F1=basis(V+U,degree,a)
 M1=F0.T@((wt*np.pi*phi*np.sinc(phi*U)*profile(U,cs)).ravel()[:,None]*F1)*(abs(1-2*phi)*2*ell/np.pi)
 M3=F0.T@((wt*(np.pi*phi)**2*U*np.sinc(phi*U)**2).ravel()[:,None]*F0)*2/np.pi**2
 M=M1+M2+M3;return (M+M.T)/2,(G+G.T)/2

def solve(p,degree=5,order=24):
 ell=p[0];cs=p[1:]
 M,G=matrices(ell,cs,degree,order)
 ev,vec=eigh(M,G,subset_by_index=(degree,degree))
 return float(ev[-1]-.25),vec[:,-1],float(np.linalg.cond(G))

def objective(p,degree=5,order=20):
 try:return -solve(p,degree,order)[0]
 except (ArithmeticError,np.linalg.LinAlgError,ValueError):return 1e3

if __name__=='__main__':
 start=time.monotonic();out={'status':'exploratory continuum variational trial, not arithmetic theorem','results':[]}
 baseline=solve([1.1762950386,0.0],degree=6,order=32)[0];assert abs(baseline+.01535798218167)<1e-9
 out['baseline']=baseline;print('baseline',baseline,flush=True)
 for dim in [1,2,3,5]:
  if dim==1:seeds=[[1.07,-2],[1.07,2],[1.2,0],[.8,5]]
  else:
   prev=out['results'][-1]['parameters'];seeds=[prev+[0]*(dim+1-len(prev)),[1.08]+[0]*dim]
  best=None
  bounds=[(.45,2.2)]+[(-15,15)]*dim
  for seed in seeds:
   res=minimize(objective,seed,args=(5,20),method='Nelder-Mead',bounds=bounds,options={'maxiter':250,'xatol':2e-4,'fatol':1e-10})
   if best is None or res.fun<best.fun:best=res
  params=best.x.tolist();m,vec,cond=solve(params,degree=7,order=32)
  entry={'prime_log_profile_degree':dim+1,'parameters':params,'optimized_degree5_order20_margin':float(-best.fun),'validated_degree7_order32_margin':m,'norm_gram_condition':cond,'radial_jacobi_coefficients':vec.tolist(),'optimizer_success':bool(best.success),'iterations':int(best.nit),'seconds_total':time.monotonic()-start}
  out['results'].append(entry);print(json.dumps(entry),flush=True);Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
