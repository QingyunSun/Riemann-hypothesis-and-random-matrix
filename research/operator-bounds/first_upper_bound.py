import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from pathlib import Path
import json
f=lambda u:(np.pi/2)**2*np.sinc(u/2)**2
v=np.linspace(0,1,2001)
B=np.array([4*quad(lambda u:(x+u)*f(u),0,1-x,epsabs=1e-11)[0] for x in v])
C=np.array([8*quad(lambda u:f(u)*quad(f,0,1-x-u,epsabs=1e-11)[0],0,1-x,epsabs=1e-10)[0] for x in v])
def objective(y):return np.max(B+y*C+v*v/(2*y))
r=minimize_scalar(objective,bounds=(.03,.5),method='bounded')
j=np.argmax(B+r.x*C+v*v/(2*r.x))
out={'status':'numerical evaluation of a proposed Cauchy majorant; does not close no-go','y':r.x,'bound':r.fun,'max_v':v[j],'target':np.pi**2/2,'normalized_margin_bound':r.fun/(2*np.pi**2)-.25,'B0':B[0],'C0':C[0]}
print(out);Path(__file__).with_name('first-upper-bound-results.json').write_text(json.dumps(out,indent=2))
