#!/usr/bin/env python3
"""Lower-bound region for the *official step trial*; randomized QMC is diagnostic.

Reads only literal data and exact geometry functions from the preserving official
source. It does not import CapEngine, run the official certificate, or circumvent
its mandatory signed-FLINT regression. See report for measure and subset proof.
"""
from __future__ import annotations
import argparse, ast, hashlib, json, math, time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

BASE=Path('/Users/qingyunsun/Library/CloudStorage/Dropbox/Research/ACUE-Astra-Handoff-2026-09-04')
import os
SOURCE = Path(os.environ.get("PRIME186_SOURCE", '/Users/qingyunsun/Library/CloudStorage/Dropbox/Research/ACUE-Astra-Handoff-2026-09-04/research-round1/prime186-work/PrimeGaps186/prime_gap_186_certificate.py'))
OUT=Path(__file__).resolve().parent


def exact_inputs():
    tree=ast.parse(SOURCE.read_text())
    names={'COEFFICIENT_SIGNATURES','COEFFICIENT_INTEGER_MATRIX','YOUNG_Q'}
    ns={'F':F,'math':math}
    for node in tree.body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in names:
            ns[node.targets[0].id]=ast.literal_eval(node.value)
    fs={'_ladder','_shells','_cells','_event_cells','_group','_schedule','build_inputs'}
    for node in tree.body:
        if isinstance(node,ast.FunctionDef) and node.name in fs:
            exec(compile(ast.Module(body=[node],type_ignores=[]),str(SOURCE),'exec'),ns)
    return ns['build_inputs'](),ns['COEFFICIENT_INTEGER_MATRIX'],ns['COEFFICIENT_SIGNATURES']


def json_exact(obj):
    if isinstance(obj,F):return str(obj)
    if isinstance(obj,dict):return {k:json_exact(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [json_exact(v) for v in obj]
    return obj


def profile(x):return .105/(1+x/100)+.895/(1+181.4*x)


class Prototype:
    def __init__(self,cutoff_cells=18800,tilt=45.,region="triangle"):
        self.region=region
        self.inputs,cmat,self.sigs=exact_inputs()
        self.c=np.array(cmat,dtype=np.float64)/1e10
        self.k=40
        self.hq=F(self.inputs['layout']['grid_step']);self.h=float(self.hq)
        self.bq=cutoff_cells*self.hq;self.b=float(self.bq)
        self.row=self.inputs['source_ladders']['new'][24]
        self.A=float(self.row['A']);self.L=float(self.row['owner_plateau'])
        self.a=float(self.row['a']);self.xi=float(self.row['xi'])
        self.capq=46580*self.hq;self.cap=float(self.capq)
        self.pminq=(self.row['A']-self.capq)/F(5,2)
        self.pmin=float(self.pminq)
        assert self.bq < self.pminq and self.row['xi']<self.pminq
        assert F(3,2)*self.pminq<self.row['owner_plateau']
        self.tilt=tilt
        mids=(np.arange(98264)+.5)*self.h
        self.g=profile(mids)
        self.physical_norm=self.h*np.sum(self.g**2)
        weights=self.g[:cutoff_cells]**2*np.exp(-tilt*np.arange(cutoff_cells)*self.h)
        self.seed_mass=self.h*np.sum(weights)
        self.probs=weights/np.sum(weights)
        self.cdf=np.cumsum(self.probs);self.cdf[-1]=1.
        self.exp_mass=-math.expm1(-tilt*self.b)/tilt
        self.I_upper=23685317890e-24
        self.I_lower=23685317816e-24
        self.rho=float(F(self.inputs['trial']['source_geometry']['parameters']['rho_star']))
        self.bh=float(F(self.inputs['hybrid']['b']))
        self.credit_coefficient=1-4*self.rho*abs(self.bh)

    def evaluate_polynomial(self,mids):
        s=mids.sum(axis=1)-.9
        powers={j:np.sum(mids**j,axis=1) for j in range(2,7)}
        acc=np.zeros(mids.shape[0])
        for row,sig in zip(self.c,self.sigs):
            val=np.full(mids.shape[0],row[-1])
            for cc in row[-2::-1]:val=val*s+cc
            for j in sig:val*=powers[j]
            acc+=val
        return acc

    def estimate(self,power,seed,owner):
        from scipy.stats import qmc
        distinct=owner=='distinct'
        marked=2 if distinct else 1
        unmarked=self.k-marked
        factor=self.k*(self.k-1) if distinct else self.k
        # p,q are ordered. Ordered-owner factor creates disjoint configurations.
        pwidth=(29100-26400)*self.h if self.region=="rectangle_lower" else self.cap-self.pmin
        prefactor=factor*pwidth*self.seed_mass**unmarked*self.exp_mass**marked/self.physical_norm**self.k
        sob=qmc.Sobol(d=42,scramble=True,seed=seed)
        values=[];accepted=0;weighted_s=0.;weighted_p=0.;weighted_q=0.
        count=1<<power;chunk=min(count,1<<14)
        for offset in range(0,count,chunk):
            u=sob.random(chunk)
            if self.region=="rectangle_lower":
                p=(26400+2700*u[:,0])*self.h
                qlo=np.full(chunk,32400*self.h)
                qv=(32400+4300*u[:,1])*self.h
                pair_kernel=np.full(chunk,4300*self.h/(29100*36700*self.h**2))
            else:
                p=self.pmin+(self.cap-self.pmin)*u[:,0]
                qlo=np.maximum(p,self.A-p-np.minimum(1.5*p,self.L))
                qv=qlo+(self.cap-qlo)*u[:,1]
                pair_kernel=(self.cap-qlo)/(p*qv)
            xs=np.empty((chunk,40))
            # True continuous exponentials for marked seeds.
            xs[:,:marked]=-np.log1p(-u[:,2:2+marked]*(1-math.exp(-self.tilt*self.b)))/self.tilt
            z=u[:,2+marked:]
            jj=np.searchsorted(self.cdf,z,side='right')
            prev=np.where(jj==0,0.,self.cdf[np.maximum(jj-1,0)])
            xs[:,marked:]=self.h*(jj+(z-prev)/self.probs[jj])
            totals=xs.copy()
            totals[:,0]+=p
            totals[:,1 if distinct else 0]+=qv
            indices=np.floor(totals/self.h).astype(np.int64)
            r=indices.sum(axis=1)
            s=totals.sum(axis=1)
            good=(r<98264)&(s>self.a)&(qlo<self.cap)
            if self.region=="rectangle_lower":good &= r*self.h>self.a
            accepted+=int(good.sum())
            w=np.zeros(chunk)
            if np.any(good):
                idx=indices[good]
                mid=(idx+.5)*self.h
                polynomial=self.evaluate_polynomial(mid)
                # g^2 cancels proposal exactly on every unmarked coordinate.
                gs=np.prod(self.g[idx[:,:marked]]**2,axis=1)
                exponent=self.tilt*(xs[good,:marked].sum(axis=1)+self.h*jj[good].sum(axis=1))
                w[good]=prefactor*pair_kernel[good]*np.exp(exponent)*gs*polynomial**2
            values.append(w)
            weighted_s+=float(np.dot(w,s));weighted_p+=float(np.dot(w,p));weighted_q+=float(np.dot(w,qv))
        allv=np.concatenate(values)
        mean=float(allv.mean())
        return {'owner':owner,'power':power,'seed':seed,'samples':count,'accepted':accepted,
                'alpha_normalized_estimate':mean,'alpha_over_I_upper_estimate':mean/self.I_upper,
                'credit_over_I_upper_estimate':self.credit_coefficient*mean/self.I_upper,
                'iid_se_diagnostic_only':float(allv.std(ddof=1)/math.sqrt(count)),
                'weighted_total':weighted_s/allv.sum(),'weighted_p':weighted_p/allv.sum(),'weighted_q':weighted_q/allv.sum(),
                'max_weight':float(allv.max())}

    def metadata(self):
        return {'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                'cutoff':str(self.bq),'cutoff_cells':int(self.bq/self.hq),'tilt':self.tilt,'region':self.region,
                'large_fragment_cap':str(self.capq),'p_min':str(self.pminq),
                'row':json_exact(self.row),'normalization_hZ_float':self.physical_norm,
                'published_normalized_I_interval':[self.I_lower,self.I_upper],
                'alpha_credit_coefficient':self.credit_coefficient,
                'status':'Randomized QMC of an exact lower-bound integral, not a certified numeric lower endpoint.'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--power',type=int,default=18);ap.add_argument('--repeats',type=int,default=4)
    ap.add_argument('--cutoff-cells',type=int,default=18800);ap.add_argument('--tilt',type=float,default=45.)
    ap.add_argument('--region',choices=['triangle','rectangle_lower'],default='triangle')
    ap.add_argument('--output',type=Path,default=OUT/'alpha_credit_qmc.json')
    args=ap.parse_args();start=time.monotonic();p=Prototype(args.cutoff_cells,args.tilt,args.region)
    runs=[]
    for owner in ['distinct','same']:
        for seed in range(args.repeats):
            row=p.estimate(args.power,240905+seed,owner);runs.append(row)
            print(json.dumps(row),flush=True)
    result=p.metadata();result['runs']=runs
    result['summary']={}
    for owner in ['distinct','same']:
        vals=np.array([r['alpha_over_I_upper_estimate'] for r in runs if r['owner']==owner])
        result['summary'][owner]={'mean_alpha_over_I_upper':float(vals.mean()),'across_scrambles_se':float(vals.std(ddof=1)/math.sqrt(len(vals))) if len(vals)>1 else None}
    result['summary']['combined_alpha_over_I_upper_estimate']=sum(x['mean_alpha_over_I_upper'] for x in result['summary'].values())
    result['elapsed_seconds']=time.monotonic()-start
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary'],indent=2));print('elapsed',result['elapsed_seconds'])

if __name__=='__main__':main()
