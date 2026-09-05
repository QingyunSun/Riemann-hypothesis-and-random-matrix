#!/usr/bin/env python3
"""One operator-induced radial residual beyond the fixed 77-dimensional cap span.

All arithmetic is exploratory float64. T includes rho_star and the signed hybrid.
The adjoint is with respect to the full product fragment measure, not coefficient
Euclidean mass. No support-restored or positive-semidefinite claim is made.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import time
import numpy as np
from scipy.linalg import eigh,cho_factor,cho_solve
from scipy.signal import fftconvolve
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
os.environ.setdefault('PRIME186_SOURCE',str(BASE/'research-round1/prime186-work/PrimeGaps186/prime_gap_186_certificate.py'))
from cap_trial import Trial,fiber_splits,SOURCE


def signed_mask(trial,cap):
    masks=[]
    for role in ('base','enlarged','full'):
        mask=np.zeros(trial.n,dtype=bool)
        for c,m in trial.shells[role]:
            if cap<=c:mask |= m
        masks.append(mask)
    mass,lam,K=.99998,.008,.34
    a=mass*mass-mass*lam;b=(1-mass/lam)*(1-mass)*K
    return masks[0].astype(float)+(a+b)*(masks[1]&~masks[0])+b*(masks[2]&~masks[1])


def set_coefficients(trial,c):
    trial.coefficients={sig:np.asarray(c[i*7:(i+1)*7]) for i,sig in enumerate(trial.coefficients)}


def radial_mass(trial,descriptors):
    """q(s) and D_i(s) with <radial h,u_i>=sum h(s) D_i(s)."""
    D=np.zeros((len(descriptors),trial.n));q=np.zeros(trial.n)
    radial=np.asarray([trial.centered**d*np.exp(trial.tilt*trial.radial) for d in range(7)])
    for cap,mask in trial.shells['outer']:
        q+=mask*radial[0]*trial.moment(cap,trial.k,())
        for i,(sig,d) in enumerate(descriptors):
            D[i]+=mask*radial[d]*trial.moment(cap,trial.k,sig)
        trial.clear()
    return q,D


def radial_adjoint(trial):
    """Density b_f(s): <radial h,T f>=sum h(s)b_f(s)."""
    aff=trial.affine();sums=[np.zeros(trial.n) for _ in aff]
    previous={};factor=float(trial.geo['rho_star'])*trial.normalization*np.exp(trial.tilt*trial.background_radial)
    for layer,cap in enumerate(trial.caps):
        rows={}
        for (oc,_),part in zip(trial.shells['outer'],aff):
            if cap<=oc:
                for sig,arr in part.items():rows[sig]=rows.get(sig,0)+arr
        if not rows:continue
        density=np.zeros(trial.n);next_moments={}
        for sig,arr in rows.items():
            moment=trial.moment(cap,trial.k-1,sig)
            difference=moment if layer==0 else moment-previous[sig]
            next_moments[sig]=moment.copy()
            density+=arr*difference
        W=factor*signed_mask(trial,cap)*density
        for j,(oc,_) in enumerate(trial.shells['outer']):
            if cap<=oc:sums[j]+=W
        previous=next_moments;trial.clear()
    result=np.zeros(trial.n)
    for (cap,mask),W in zip(trial.shells['outer'],sums):
        result+=mask*fftconvolve(W,trial.g*trial.survival(cap))[:trial.n]
    return result


def radial_mixed(trial,descriptors,h):
    """All B(u_i,h), B(h,h), independently of radial_adjoint's contraction."""
    aff=[];h_aff=[]
    powers=np.asarray([trial.centered**d for d in range(7)])
    exponents={ex for sig,_ in descriptors for _,ex,_ in fiber_splits(sig)}
    for cap,mask in trial.shells['outer']:
        kernels={}
        for ex in exponents:
            fiber=trial.g*trial.survival(cap)*trial.mid**ex
            for d in range(7):
                kernels[ex,d]=fftconvolve(powers[d]*mask,fiber[::-1])[trial.n-1:2*trial.n-1]
        aff.append(kernels)
        fiber=trial.g*trial.survival(cap)
        h_aff.append(fftconvolve(h*mask,fiber[::-1])[trial.n-1:2*trial.n-1])
    mixed=np.zeros(len(descriptors));hh=0.;previous={}
    sigs={rem for sig,_ in descriptors for rem,_,_ in fiber_splits(sig)}
    factor=float(trial.geo['rho_star'])*trial.normalization*np.exp(trial.tilt*trial.background_radial)
    for layer,cap in enumerate(trial.caps):
        combined={};H=np.zeros(trial.n)
        for (oc,_),part,ha in zip(trial.shells['outer'],aff,h_aff):
            if cap<=oc:
                H+=ha
                for key,arr in part.items():combined[key]=combined.get(key,0)+arr
        if not combined:continue
        diff={};next_moments={}
        for sig in sigs:
            moment=trial.moment(cap,trial.k-1,sig)
            diff[sig]=moment if layer==0 else moment-previous[sig]
            next_moments[sig]=moment.copy()
        W=factor*signed_mask(trial,cap)
        hh+=np.sum(W*H*H*diff[()])
        for i,(sig,d) in enumerate(descriptors):
            mixed[i]+=sum(mult*np.sum(W*H*combined[ex,d]*diff[rem]) for rem,ex,mult in fiber_splits(sig))
        previous=next_moments;trial.clear()
    return mixed,float(hh)


class SampledTrial(Trial):
    """Same cap model, direct arbitrary radial coefficient profile evaluation."""
    def set_profile(self,c,h,beta):
        self.profiles={sig:np.polynomial.polynomial.polyval(self.centered,c[7*i:7*(i+1)])
                       for i,sig in enumerate(self.coefficients)}
        self.profiles[()]+=beta*h
    def denominator(self):
        grouped={};entries=list(self.profiles.items())
        for i,(sig,a) in enumerate(entries):
            for j in range(i,len(entries)):
                eta,b=entries[j];key=tuple(sorted(sig+eta))
                grouped[key]=grouped.get(key,0)+(1 if i==j else 2)*a*b
        total=0.;absolute=0.
        for cap,mask in self.shells['outer']:
            for sig,a in grouped.items():
                term=a*trial_exp(self)*self.moment(cap,self.k,sig)
                total+=np.sum(term[mask]);absolute+=np.sum(abs(term[mask]))
            self.clear()
        return total,absolute
    def affine(self):
        grouped={}
        for sig,a in self.profiles.items():
            for rem,ex,mult in fiber_splits(sig):
                key=rem,ex;grouped[key]=grouped.get(key,0)+mult*a
        output=[]
        for cap,mask in self.shells['outer']:
            part={}
            for (rem,ex),a in grouped.items():
                fiber=self.g*self.survival(cap)*self.mid**ex
                corr=fftconvolve(a*mask,fiber[::-1])[self.n-1:2*self.n-1]
                part[rem]=part.get(rem,0)+corr
            output.append(part)
        return output

def trial_exp(trial):return np.exp(trial.tilt*trial.radial)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--intervals',type=int,default=16384)
    ap.add_argument('--density-cutoff',type=float,default=1e-9)
    ap.add_argument('--tilt',type=float,default=20)
    args=ap.parse_args();start=time.monotonic();N=args.intervals
    trial_root=Path(os.environ.get('PRIME186_TRIAL_ROOT',str(BASE/'research-round4/k39-trial')))
    old=trial_root/f'ritz_k39_n{N}'
    raw=json.loads(old.with_suffix('.json').read_text());data=np.load(old.with_suffix('.npz'))
    G,B=data['gram'],data['numerator'];c=np.asarray(raw['trials'][-1]['coefficients_float'])
    trial=Trial(39,N,args.tilt);set_coefficients(trial,c)
    descriptors=[(sig,d) for sig in trial.coefficients for d in range(7)]
    diag=np.sqrt(G.diagonal());Gs=G/diag[:,None]/diag[None,:]
    factor=cho_factor((Gs+Gs.T)/2,lower=True)
    def solve_mass(v):return cho_solve(factor,v/diag)/diag
    # Use P_U T f itself, not the scalar Ritz approximation lambda*f.
    projected=solve_mass(B@c)
    q,D=radial_mass(trial,descriptors);bf=radial_adjoint(trial)
    # Stored G,B use the old run's tilt. Convert every newly integrated form to
    # that common normalization before any projection, including cross forms.
    reference_tilt=float(raw['tilt'])
    Zreference=np.sum(trial.g*trial.g*np.exp(-reference_tilt*trial.mid))
    mass_scale=float((trial.Z/Zreference)**trial.k)
    q*=mass_scale;D*=mass_scale;bf*=mass_scale
    active=q>args.density_cutoff*max(q);h=np.zeros(trial.n)
    h[active]=(bf-D.T@projected)[active]/q[active]
    print(json.dumps({'stage':'radial_residual','active':int(active.sum()),'h_norm2':float(np.sum(q*h*h))}),flush=True)
    g=D@h;ghh=float(np.sum(q*h*h));bh,bhh=radial_mixed(trial,descriptors,h)
    bh*=mass_scale;bhh*=mass_scale
    p=solve_mass(g);gamma=ghh-float(g@p)
    ev,U=eigh((Gs+Gs.T)/2);W=(U/np.sqrt(ev))/diag[:,None]
    cross=W.T@(bh-B@p)
    zBz=bhh-2*float(p@bh)+float(p@B@p)
    assert gamma>0
    K=np.zeros((78,78));K[:77,:77]=W.T@B@W
    K[:77,77]=cross/gamma**.5;K[77,:77]=K[:77,77];K[77,77]=zBz/gamma
    vals,vec=eigh((K+K.T)/2);coeff=vec[:77,-1];beta=float(vec[77,-1]/gamma**.5)
    newc=W@coeff-beta*p
    check=SampledTrial(39,N,args.tilt);check.set_profile(newc,h,beta);direct=check.forms()
    # Genuine outside-U direction audit: true mass norm and signed mixed pairing.
    coupling=float(c@bh-(c@B)@p)
    original=float(c@B@c/(c@G@c))
    out={'status':'exploratory full cap-operator radial residual; no support restoration',
         'N':N,'density_cutoff':args.density_cutoff,'tilt':args.tilt,
         'stored_matrix_tilt':reference_tilt,'mass_normalization_conversion':mass_scale,
         'normalized_residual_T_expectation':zBz/gamma,
         'original_77_quotient':original,'new_78_matrix_quotient':float(vals[-1]),
         'new_78_direct_evaluation':direct,'gain_matrix':float(vals[-1]-original),
         'radial_norm_squared':ghh,'outside_77_norm_squared':gamma,
         'radial_norm_fraction_outside_77':gamma/ghh,'coupling_f_Tz':coupling,
         'coupling_expected_h_norm_squared':ghh,'coupling_identity_relative_error':(coupling-ghh)/ghh,
         'mixed_adjoint_check':float(c@bh-h@bf),'mixed_adjoint_relative_check':float((c@bh-h@bf)/max(abs(c@bh),abs(h@bf),1e-300)),
         'active_radial_cells':int(active.sum()),'radial_cells':trial.n,
         'excluded_mass_positive_fraction':float(np.sum(np.maximum(q[~active],0))/np.sum(np.maximum(q,0))),
         'negative_radial_mass_absolute_fraction':float(-np.sum(np.minimum(q,0))/np.sum(np.maximum(q,0))),
         'orthogonal_complement_coupling':coupling/gamma**.5,
         'new_vector_beta':beta,'new_vector_coefficients':newc.tolist(),
         'matrix_direct_difference':float(vals[-1]-direct['rho_J_over_I']),
         'dtype':str(q.dtype),'seconds':time.monotonic()-start,
         'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
         'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'engine_sha256':hashlib.sha256((HERE/'cap_trial.py').read_bytes()).hexdigest(),
         'old_npz_sha256':hashlib.sha256(old.with_suffix('.npz').read_bytes()).hexdigest(),
         'old_json_sha256':hashlib.sha256(old.with_suffix('.json').read_bytes()).hexdigest()}
    prefix=HERE/f'radial_residual_n{N}_cut{args.density_cutoff:g}_tilt{args.tilt:g}'
    prefix.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(str(prefix)+'.npz',q=q,D=D,bf=bf,h=h,projected=projected,
                        mass_cross=g,numerator_cross=bh,orthogonal_projection=p,newc=newc,K=K,
                        active=active,radial=trial.radial)
    print(json.dumps({k:v for k,v in out.items() if k not in ('new_vector_coefficients','new_78_direct_evaluation')},indent=2),flush=True)
if __name__=='__main__':main()
