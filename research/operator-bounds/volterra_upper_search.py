"""Numerical search for a variable Schur majorant of K.
No rigorous grid, quadrature, or arithmetic remainder certification.
"""
import numpy as np,json
from scipy.special import roots_legendre
from pathlib import Path

def compute(N):
    v=np.linspace(0,1,N+1);h=1/N;x,w=roots_legendre(48);x=(x+1)/2;w=w/2
    f=lambda u:(np.pi/2)**2*np.sinc(u/2)**2
    U=(1-v[:,None])*x
    B=4*(1-v)*(((v[:,None]+U)*f(U))@w)
    S=v[:,None];U=S*x
    C=8*v*((f(U)*f(S-U))@w)
    def trial(lam,ret=False):
        Y=np.zeros(N+1);den=np.zeros(N+1)
        for j in range(N,-1,-1):
            n=N-j
            tail=h*np.dot(C[1:n+1],Y[j+1:])
            if n:tail-=.5*h*C[n]*Y[-1]
            den[j]=lam-B[j]-tail
            if den[j]<=0:return False, Y,den
            Y[j]=v[j]**2/(2*den[j])
        return True,Y,den
    lo=4.;hi=6.
    for _ in range(42):
        mid=(lo+hi)/2
        if trial(mid)[0]:hi=mid
        else:lo=mid
    ok,Y,den=trial(hi+1e-7)
    return {'N':N,'numerical_critical_lambda':hi,'normalized_margin_bound':hi/(2*np.pi**2)-.25,'min_denominator':float(den.min()),'max_Y':float(Y.max())},v,Y,B,C
if __name__=='__main__':
    out=[]
    for n in (250,500,1000,2000,4000):
        row,v,Y,B,C=compute(n);out.append(row);print(json.dumps(row),flush=True)
    Path(__file__).with_name('volterra-upper-results.json').write_text(json.dumps(out,indent=2))
    np.savez(Path(__file__).with_name('volterra-upper-profile.npz'),v=v,Y=Y,B=B,C=C)
