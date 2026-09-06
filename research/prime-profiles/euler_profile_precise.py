"""Higher-precision density evaluation for the exploratory Euler-profile search.
The scalar density power series uses 55 digits; final Rayleigh matrices still
use floating quadrature, so this is not a certified arithmetic result.
"""
from pathlib import Path
import json,time
from functools import lru_cache
import numpy as np
import mpmath as mp
from scipy.optimize import minimize
import euler_profile as ep
mp.mp.dps=55
@lru_cache(128)
def coeff(a,cs,N=140):
 a=mp.mpf(a);cs=list(map(mp.mpf,cs));d=[mp.mpf(0)]*(N+1);d[0]=1
 for n in range(1,N+1):d[n]=sum(2*k*c*d[n-k] for k,c in enumerate(cs,2) if k<=n)/n
 H=[mp.mpf(0)]*(N+1);H[0]=1
 for n in range(1,N+1):
  B=1/(a+n-1);total=mp.mpf(0)
  for k in range(1,n+1):
   total+=k*d[k]*B*H[n-k]
   if k<n:B*=mp.mpf(k)/(a+n-k-1)
  H[n]=a*total/n
 return tuple(H)
def density(v,a,cs):
 H=coeff(a,tuple(cs));values=[]
 for x in list(v)+[1.0]:
  y=mp.polyval(H[::-1],mp.mpf(x));short=mp.polyval(H[:111][::-1],mp.mpf(x))
  if y<=0 or abs(y-short)>mp.mpf('1e-11')*(1+abs(y)):raise ArithmeticError('Power-series truncation unresolved')
  values.append(float(y))
 return np.array(values[:-1])
ep.density=density

def main():
 start=time.monotonic();out={'status':'exploratory continuum search, high-precision density, floating Rayleigh quadrature','results':[]}
 seed=[1.0906269411552656,.6070329368880861,-2.1906991585666895]
 for dim in [2,3,5]:
  seed=seed+[0]*(dim+1-len(seed))
  result=minimize(ep.objective,seed,args=(5,20),method='Nelder-Mead',bounds=[(.7,1.5)]+[(-8,8)]*dim,options={'maxiter':160,'xatol':2e-4,'fatol':1e-9})
  seed=result.x.tolist();checks=[]
  for degree,order in [(5,24),(7,32),(9,40)]:
   margin,vec,cond=ep.solve(seed,degree,order);checks.append({'radial_degree':degree,'quadrature_order':order,'margin':margin,'gram_condition':cond,'radial_coefficients':vec.tolist()})
  row={'parameters':seed,'profile_degree':dim+1,'optimizer_success':bool(result.success),'iterations':int(result.nit),'checks':checks,'elapsed':time.monotonic()-start};out['results'].append(row)
  print(json.dumps(row),flush=True);Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
if __name__=='__main__':main()
