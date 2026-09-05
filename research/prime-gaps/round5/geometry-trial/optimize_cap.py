#!/usr/bin/env python3
"""Exploratory 77-dimensional cap Gram assembly and conditioned Ritz search."""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.signal import fftconvolve

from cap_trial import HERE, Trial, fiber_splits


def denominator_matrix(trial, descriptors):
    size = len(descriptors)
    result = np.zeros((size,size),dtype=trial.dtype)
    # All entries with identical joined signature and total radial degree share an integral.
    groups = {}
    for i,(sig,d) in enumerate(descriptors):
        for j in range(i,size):
            eta,e=descriptors[j]
            key=tuple(sorted(sig+eta))
            groups.setdefault(key,[]).append((i,j,d+e))
    radial_powers=np.asarray([trial.centered**j*np.exp(trial.tilt*trial.radial) for j in range(13)])
    for cap,mask in trial.shells["outer"]:
        for sig,entries in groups.items():
            moment=trial.moment(cap,trial.k,sig)
            values=radial_powers[:,mask] @ moment[mask]
            for i,j,degree in entries:
                result[i,j]+=values[degree]
        trial.clear()
    return result+result.T-np.diag(result.diagonal())


def face_matrix(trial, descriptors):
    size=len(descriptors)
    radials=np.asarray([trial.centered**degree for degree in range(7)])
    splits={}
    exponents=set()
    for i,(sig,degree) in enumerate(descriptors):
        for rem,exponent,mult in fiber_splits(sig):
            splits.setdefault(rem,[]).append((i,exponent,degree,mult))
            exponents.add(exponent)
    affine=[]
    for cap,mask in trial.shells["outer"]:
        kernels={}
        for exponent in sorted(exponents):
            fiber=trial.g*trial.survival(cap)*trial.mid**exponent
            for degree in range(7):
                kernels[exponent,degree]=fftconvolve(radials[degree]*mask,fiber[::-1])[trial.n-1:2*trial.n-1]
        affine.append(kernels)
    matrix=np.zeros((size,size),dtype=trial.dtype)
    mass,lam,pair=trial.dtype(".99998"),trial.dtype(".008"),trial.dtype(str(float(trial.geo["pair_constant"])))
    a=mass*mass-mass*lam
    b=(1-mass/lam)*(1-mass)*pair
    prefactor=trial.normalization*np.exp(trial.tilt*trial.background_radial)
    previous_moments={}
    for layer,cap in enumerate(trial.caps):
        masks=[]
        for role in ("base","enlarged","full"):
            mask=np.zeros(trial.n,dtype=bool)
            for inner_cap,inner_mask in trial.shells[role]:
                if cap<=inner_cap:mask |= inner_mask
            masks.append(mask)
        signed_mask=masks[0].astype(trial.dtype)+(a+b)*(masks[1]&~masks[0])+b*(masks[2]&~masks[1])
        combined={}
        for (outer_cap,_),kernels in zip(trial.shells["outer"],affine):
            if cap<=outer_cap:
                for key,arr in kernels.items():
                    combined[key]=combined.get(key,0)+arr
        if not combined:
            continue
        rows={}
        for rem,terms in splits.items():
            columns=[x[0] for x in terms]
            assert len(columns)==len(set(columns))
            values=np.asarray([mult*combined[exponent,degree] for _,exponent,degree,mult in terms])
            rows[rem]=(columns,values)
        keys=sorted(rows)
        next_moments={}
        for i,sig in enumerate(keys):
            col_a,A=rows[sig]
            for j in range(i,len(keys)):
                eta=tuple(sorted(sig+keys[j]))
                moment=trial.moment(cap,trial.k-1,eta)
                next_moments[eta]=moment.copy()
                difference=moment if layer==0 else moment-previous_moments[eta]
                weight=difference*prefactor*signed_mask
                col_b,B=rows[keys[j]]
                local=A @ (B*weight).T
                matrix[np.ix_(col_a,col_b)]+=local
                if i!=j:
                    matrix[np.ix_(col_b,col_a)]+=local.T
        previous_moments=next_moments
        trial.clear()
        print(json.dumps({"stage":"face_layer","layer":layer,"cap":cap}),flush=True)
    return (matrix+matrix.T)/2


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--k",type=int,default=39)
    parser.add_argument("--intervals",type=int,default=98304)
    parser.add_argument("--tilt",type=float,default=20)
    parser.add_argument("--validate",action="store_true")
    parser.add_argument("--config",type=Path,required=True)
    args=parser.parse_args()
    start=time.monotonic()
    config=json.loads(args.config.read_text())
    trial=Trial(args.k,args.intervals,args.tilt,config=config)
    descriptors=[(sig,d) for sig in trial.coefficients for d in range(7)]
    fixed=np.concatenate(list(trial.coefficients.values()))
    gram=denominator_matrix(trial,descriptors)
    print(json.dumps({"stage":"denominator_complete","seconds":time.monotonic()-start}),flush=True)
    face=face_matrix(trial,descriptors)
    rho=float(trial.geo["rho_star"])
    numerator=rho*face
    diagonal=np.sqrt(gram.diagonal())
    assert np.all(diagonal>0)
    G=gram/diagonal[:,None]/diagonal[None,:]
    B=numerator/diagonal[:,None]/diagonal[None,:]
    G=(G+G.T)/2;B=(B+B.T)/2
    values,vectors=eigh(G)
    results=[]
    fixed_I=float(fixed@gram@fixed)
    fixed_ratio=float((fixed@numerator@fixed)/fixed_I)
    out={"status":"exploratory finite-family Ritz search; no outward cap bound or support restoration",
         "config":config, "geometry":trial.geo["metadata"],
         "k":args.k,"intervals":args.intervals,"tilt":args.tilt,
         "dimension":len(descriptors),"dtype":str(gram.dtype),
         "fixed_vector_matrix_denominator":fixed_I,"fixed_vector_matrix_quotient":fixed_ratio,
         "scaled_gram_eigenvalues":list(map(float,values)),
         "scaled_gram_min_eigenvalue":float(values[0]),
         "trials":results}
    for cutoff in (1e-8,1e-10,1e-12):
        keep=values>cutoff*values[-1]
        U=vectors[:,keep]/np.sqrt(values[keep])
        reduced=U.T@B@U
        ev,evec=eigh((reduced+reduced.T)/2)
        v=U@evec[:,-1]
        c=v/diagonal
        c/=math_sqrt(float(c@gram@c))
        quotient=float(c@numerator@c)
        residual=B@v-quotient*G@v
        norm_bound=np.linalg.norm(B,2)*np.linalg.norm(v)+abs(quotient)*np.linalg.norm(G,2)*np.linalg.norm(v)
        record={"relative_gram_cutoff":cutoff,"retained_dimension":int(keep.sum()),
                "retained_scaled_gram_condition":float(values[-1]/values[keep][0]),
                "rho_J_over_I":quotient,"gap_to_one":1-quotient,
                "projected_eigen_residual":float(np.linalg.norm(reduced@evec[:,-1]-ev[-1]*evec[:,-1])),
                "full_scaled_pencil_relative_residual":float(np.linalg.norm(residual)/norm_bound),
                "coefficients_float":[float(x) for x in c]}
        if args.validate:
            independent=Trial(args.k,args.intervals,args.tilt,config=config)
            independent.coefficients={sig:np.array(c[7*i:7*(i+1)],dtype=independent.dtype)
                                      for i,sig in enumerate(trial.coefficients)}
            check=independent.forms()
            record["direct_candidate_evaluation"]=check
            record["matrix_vs_direct_quotient_difference"]=quotient-check["rho_J_over_I"]
        results.append(record)
        print(json.dumps({k:v for k,v in record.items() if k not in ("coefficients_float","direct_candidate_evaluation")}),flush=True)
    out["seconds"]=time.monotonic()-start
    prefix=HERE/f"{config['tag']}_k{args.k}_n{args.intervals}"
    np.savez_compressed(prefix.with_suffix(".npz"),gram=gram,numerator=numerator,fixed=fixed)
    prefix.with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({"output":str(prefix.with_suffix(".json")),"seconds":out["seconds"]}),flush=True)


def math_sqrt(value):
    assert value>0
    return value**.5


if __name__=="__main__":
    main()
