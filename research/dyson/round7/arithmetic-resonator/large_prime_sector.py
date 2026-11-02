#!/usr/bin/env python3
"""Fixed arithmetic >sqrt(L) prime sector for the Inoue half-gap form.

New family: Legendre radial coefficients of {1,S2,S3,S2^2}, plus
C=1_{P+(n)>sqrt(L)} times Legendre radial coefficients of {1,S2}.
All integrations below are deterministic floating quadrature, not enclosures.
"""
from __future__ import annotations
import argparse,json,math,time,hashlib
from functools import lru_cache
from pathlib import Path
import numpy as np
from scipy.special import roots_jacobi,gammaln
from scipy.linalg import eigh
from numpy.polynomial.legendre import legval

HERE=Path(__file__).resolve().parent
BASE_GROUPS=((),(2,),(3,),(2,2))
MARK_GROUPS=((),(2,))

@lru_cache(None)
def partitions(xs):
    if not xs:return ((),)
    a,*rest=xs;out=[]
    for blocks in partitions(tuple(rest)):
        out.append(((a,),)+blocks)
        for i in range(len(blocks)):
            out.append(blocks[:i]+((a,)+blocks[i],)+blocks[i+1:])
    return tuple(out)

@lru_cache(None)
def moment(a,ks):
    if not ks:return 1.
    return sum(a**len(bs)*math.prod(math.gamma(sum(b)) for b in bs) for bs in partitions(ks))*math.exp(gammaln(a)-gammaln(a+sum(ks)))

def expand(ks,insertions,n):
    out={}
    for bits in range(1<<len(ks)):
        remain=[];coefficient=np.ones(n)
        for j,k in enumerate(ks):
            if (bits>>j)&1:coefficient*=sum(u**k for u in insertions)
            else:remain.append(k)
        key=tuple(sorted(remain));out[key]=out.get(key,0)+coefficient
    return out


def gauss(order,power,lo=0.,hi=1.):
    x,w=roots_jacobi(order,0,power)
    return lo+(hi-lo)*(x+1)/2,w*((hi-lo)/2)**(power+1)


def marked_moment_scaled(a,ks,v,order):
    """E_v[C prod S_k]/(v-1/2)^a, valid v>=1/2.

C in {0,1}; one designated large prime contributes a dt/t, the remaining
unmarked background contributes its usual beta-density moments.
"""
    unique,inverse=np.unique(v,return_inverse=True)
    z,w=gauss(order,a-1)
    delta=unique-.5;t=unique[:,None]-delta[:,None]*z[None,:]
    out=np.zeros(len(unique))
    for bits in range(1<<len(ks)):
        marked=sum(k for j,k in enumerate(ks) if (bits>>j)&1)
        remaining=tuple(k for j,k in enumerate(ks) if not (bits>>j)&1)
        r=sum(remaining)
        value=np.sum(t**(marked-1)*z[None,:]**r*w,axis=1)
        out+=moment(a,remaining)*delta**r*value
    out*=a*unique**(1-a)
    return out[inverse]


class FormBuilder:
    def __init__(self,ell,degree,order):
        self.ell,self.a,self.degree,self.order=ell,ell*ell,degree,order
        self.groups=[(sig,0) for sig in BASE_GROUPS]+[(sig,1) for sig in MARK_GROUPS]
        self.features=[(d,sig,c) for sig,c in self.groups for d in range(degree+1)]
        self.marked_order=max(32,order)
    def cross(self,v,left,right,weight,mode,scaled_mark=False):
        v=np.ravel(v);left=[np.ravel(u) for u in left];right=[np.ravel(u) for u in right]
        weight=np.ravel(weight);n=len(v);D=self.degree+1
        ml=v+sum(left);mr=v+sum(right)
        dl=sum((u>.5).astype(float) for u in left) if left else np.zeros(n)
        dr=sum((u>.5).astype(float) for u in right) if right else np.zeros(n)
        radial_l={c:np.asarray([legval((2*ml-1) if c==0 else (4*ml-3),[0]*d+[1]) for d in range(D)]).T for c in (0,1)}
        radial_r={c:np.asarray([legval((2*mr-1) if c==0 else (4*mr-3),[0]*d+[1]) for d in range(D)]).T for c in (0,1)}
        expansions_l={sig:expand(sig,left,n) for sig,_ in self.groups}
        expansions_r={sig:expand(sig,right,n) for sig,_ in self.groups}
        cache={};result=np.zeros((len(self.features),len(self.features)))
        for i,(sig,ci) in enumerate(self.groups):
            for j,(eta,cj) in enumerate(self.groups):
                if mode=='base' and (ci or cj):continue
                if mode=='marked' and not (ci or cj):continue
                value=np.zeros(n)
                for kl,cl in expansions_l[sig].items():
                    for kr,cr in expansions_r[eta].items():
                        ks=tuple(sorted(kl+kr))
                        if ks not in cache:
                            base=moment(self.a,ks)*v**sum(ks)
                            marked=marked_moment_scaled(self.a,ks,v,self.marked_order) if scaled_mark else np.zeros(n)
                            cache[ks]=base,marked
                        base,marked=cache[ks]
                        if ci==cj==0:m=base
                        elif ci==1 and cj==0:m=marked+dl*base
                        elif ci==0 and cj==1:m=marked+dr*base
                        else:m=(1+dl+dr)*marked+dl*dr*base
                        value+=cl*cr*m
                result[i*D:(i+1)*D,j*D:(j+1)*D]=radial_l[ci].T@((weight*value)[:,None]*radial_r[cj])
        return result
    def forms(self):
        a=self.a;n=self.order
        v,vw=gauss(n,a-1);z,zw=gauss(n,0)
        G=self.cross(v,[],[],vw,'base')
        v,vw=gauss(n,a,.5,1)
        G+=self.cross(v,[],[],vw*v**(a-1),'marked',True)
        # The unmarked block uses the ordinary smooth simplex quadrature.
        v,vw=gauss(n,a-1)
        V,X,Y=np.meshgrid(v,z,z,indexing='ij');Wv,Wx,Wy=np.meshgrid(vw,zw,zw,indexing='ij')
        U=(1-V)*X;W=(1-V)*(1-X)*Y;weights=Wv*Wx*Wy*(1-V)**2*(1-X)
        M=self.m2_region(V,U,W,weights,'base')
        # Background contains the unique >1/2 prime: Jacobi factor (v-1/2)^a.
        v,vw=gauss(n,a,.5,1)
        V,X,Y=np.meshgrid(v,z,z,indexing='ij');Wv,Wx,Wy=np.meshgrid(vw,zw,zw,indexing='ij')
        U=(1-V)*X;W=(1-V)*(1-X)*Y
        weights=Wv*Wx*Wy*V**(a-1)*(1-V)**2*(1-X)
        M+=self.m2_region(V,U,W,weights,'marked',True)
        # One inserted prime exceeds1/2. These two sectors are disjoint and
        # v<1/2 forces the background large-prime indicator to vanish.
        v,vw=gauss(n,a-1,0,.5)
        V,X,Y=np.meshgrid(v,z,z,indexing='ij');Wv,Wx,Wy=np.meshgrid(vw,zw,zw,indexing='ij')
        U=.5+(.5-V)*X;W=(.5-V)*(1-X)*Y
        weights=Wv*Wx*Wy*(.5-V)**2*(1-X)
        M+=self.m2_region(V,U,W,weights,'marked')
        M+=self.m2_region(V,W,U,weights,'marked')
        # Same-prime A*A term survives, with H0 squared and no inserted mark.
        v,vw=gauss(n,a-1)
        V,Z=np.meshgrid(v,z,indexing='ij');Wv,Wz=np.meshgrid(vw,zw,indexing='ij');U=(1-V)*Z
        weights=Wv*Wz*(1-V)*np.pi**2/4*U*np.sinc(U/2)**2*2/np.pi**2
        M+=self.cross(V,[],[],weights,'base')
        v,vw=gauss(n,a,.5,1)
        V,Z=np.meshgrid(v,z,indexing='ij');Wv,Wz=np.meshgrid(vw,zw,indexing='ij');U=(1-V)*Z
        weights=Wv*Wz*V**(a-1)*(1-V)*np.pi**2/4*U*np.sinc(U/2)**2*2/np.pi**2
        M+=self.cross(V,[],[],weights,'marked',True)
        return (M+M.T)/2,(G+G.T)/2
    def m2_region(self,V,U,W,weights,mode,scaled_mark=False):
        weights=weights*np.pi**2/4*np.sinc(U/2)*np.sinc(W/2)*2*self.ell**2/np.pi**2
        return self.cross(V,[],[U,W],weights,mode,scaled_mark)+self.cross(V,[U],[W],weights,mode,scaled_mark)


def solve(M,G,indices=None):
    if indices is None:indices=np.arange(len(G))
    G=G[np.ix_(indices,indices)];M=M[np.ix_(indices,indices)]
    diag=np.sqrt(G.diagonal());Gs=G/diag[:,None]/diag[None,:];Ms=M/diag[:,None]/diag[None,:]
    vals,U=eigh(Gs);keep=vals>vals[-1]*1e-11
    W=U[:,keep]/np.sqrt(vals[keep]);K=W.T@Ms@W
    ev,evec=eigh((K+K.T)/2);c=W@evec[:,-1]/diag
    c/=float(c@G@c)**.5
    residual=M@c-float(c@M@c)*G@c
    return {'margin':float(c@M@c-.25),'quotient':float(c@M@c),
            'coefficients':c.tolist(),'retained_dimension':int(keep.sum()),
            'dimension':len(G),'gram_scaled_eigenvalues':vals.tolist(),
            'retained_scaled_condition':float(vals[-1]/vals[keep][0]),
            'pencil_residual_norm':float(np.linalg.norm(residual)),
            'norm':float(c@G@c)}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--order',type=int,default=24)
    ap.add_argument('--degree',type=int,default=4);args=ap.parse_args()
    ell=27/25;start=time.monotonic();fb=FormBuilder(ell,args.degree,args.order);M,G=fb.forms()
    base_count=len(BASE_GROUPS)*(args.degree+1)
    result={'status':'fixed arithmetic marked-family continuum numerical trial; not interval certified',
            'ell_exact':'27/25','mark':'C_L(n)=1 if a distinct prime p|n satisfies p>sqrt(L), else0',
            'phi':.5,'degree':args.degree,'order':args.order,'features':fb.features,
            'radial_basis':'Legendre_d(2v-1) unmarked; Legendre_d(4v-3) marked',
            'base':solve(M,G,np.arange(base_count)),'enlarged':solve(M,G),
            'seconds':time.monotonic()-start,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    prefix=HERE/f'large_prime_sector_d{args.degree}_q{args.order}'
    prefix.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    np.savez_compressed(prefix.with_suffix('.npz'),M=M,G=G)
    print(json.dumps({k:v for k,v in result.items() if k not in ('features','base','enlarged')},indent=2))
    print(json.dumps({key:{k:v for k,v in result[key].items() if k not in ('coefficients','gram_scaled_eigenvalues')} for key in ('base','enlarged')},indent=2))
if __name__=='__main__':main()
