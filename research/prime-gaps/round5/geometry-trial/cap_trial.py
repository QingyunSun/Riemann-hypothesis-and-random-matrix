#!/usr/bin/env python3
"""Exploratory cap-only evaluation of the published rational profile at k=39.

Independent FFT implementation with the actual NumPy dtype recorded. No Arb enclosure, no support
restoration, no FLINT import, and no replacement of the published runtime.
The source file is read only to parse the two literal coefficient tables.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import time
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve
from scipy.special import spence

HERE = Path(__file__).resolve().parent
SOURCE = Path(os.environ.get("PRIME186_SOURCE", str(HERE.parents[1] / "research-round1/prime186-work/PrimeGaps186/prime_gap_186_certificate.py")))


def read_coefficients():
    wanted = {"COEFFICIENT_SIGNATURES", "COEFFICIENT_INTEGER_MATRIX"}
    values = {}
    for node in ast.parse(SOURCE.read_text()).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            name = getattr(node.targets[0], "id", "")
            if name in wanted:
                values[name] = ast.literal_eval(node.value)
    return tuple(map(tuple, values["COEFFICIENT_SIGNATURES"])), values["COEFFICIENT_INTEGER_MATRIX"]


def geometry(config=None):
    config = config or {}
    rho, gap = Q(262499, 10**6), Q(1, 10**7)
    rs = rho - gap
    physical_S = Q(config.get("physical_S", ".2742997"))
    S, T1 = physical_S / rs, (Q(".5252997")-physical_S) / rs
    T0 = Q(1997, 1000) - S
    epsilon = gap / rho
    zeta = Q(19037, 100000) / rho
    sigma0, sigmam = Q(100001, 10**6), Q(1, 2) - Q(40481, 100000) + Q(1, 10**10)
    def ladder(T, eps, maximum, parameters):
        previous, rows = Q(0), []
        E = rho*(S+T)-Q(1, 2)
        for index in range(100):
            degree = min(index//12, 2)
            c, slope = parameters[degree]
            omega = min(maximum, (c-eps-E+2*previous-gap)/slope)
            B = (Q(1, 2)+2*previous)/rho
            rows.append({"a": B-T, "b": B-S})
            if omega == maximum:
                break
            previous = omega
        return rows
    old = ladder(T0, Q(1,10**6), Q(12499,10**6),
                 [((1-5*sigma0)/15,Q(18,5)),((1-4*sigma0)/16,Q(7,2)),(Q(3,80),Q(3))])
    new = ladder(T1, Q(1,10**7), Q(253,20000),
                 [((1-5*sigmam)/15,Q(18,5)),((1-4*sigmam)/16,Q(7,2)),((1-2*sigmam)/20,Q(16,5))])
    assert len(old) == 29 and len(new) == 43
    A, C0, C1 = S+epsilon/2, T0+epsilon/2, T1+epsilon/2
    mode = config.get("plateau", "original")
    if mode == "original":
        L0, L1 = Q(23,40)*C0, Q(23,40)*C1
    elif mode == "common_max":
        L0 = L1 = Q(3,5)*C0
    elif mode == "common_min":
        L0 = L1 = (3*A-C0)/4
    else:
        raise ValueError("unknown plateau mode")
    assert A > C1 > C0 > 0
    for C,L in [(C0,L0),(C1,L1)]:
        assert (3*A-C)/4 <= L <= 3*C/5
        assert L >= 3*A/7
    assert (C0+L0)/4 <= (C1+L1)/4
    outer_cap = min(A-L0,A-L1)
    pair_constant = Q(config.get("pair_constant", ".34"))
    metadata = {"physical_S": str(physical_S), "physical_T0": str(rs*T0),
                "physical_T1": str(rs*T1), "plateau_mode": mode,
                "L0": str(L0), "L1": str(L1), "q0": str(L0/C0), "q1": str(L1/C1),
                "pair_constant": str(pair_constant), "outer_cap": str(outer_cap),
                "frontier_slacks": [str(L-(3*A-C)/4) for C,L in [(C0,L0),(C1,L1)]],
                "plateau_upper_slacks": [str(3*C/5-L) for C,L in [(C0,L0),(C1,L1)]],
                "constraints": "exact rational plateau and nesting checks pass; full source audit separate"}
    shells = {
        "outer": [(new[0]["a"], zeta), (new[24]["a"], (S+epsilon)/2),
                  (S, outer_cap)],
        "base": [(old[12]["b"], zeta), (old[24]["b"], (T0+epsilon)/2),
                 (T0, (C0+L0)/4)],
        "enlarged": [(new[12]["b"], zeta), (new[24]["b"], (T1+epsilon)/2),
                     (T1, (C1+L1)/4)],
        "full": [(S, zeta)],
    }
    return {"rho": rho, "rho_star": rs, "S": S, "T0": T0, "T1": T1, "shells": shells, "pair_constant": pair_constant, "metadata": metadata}


@lru_cache(None)
def block_partitions(signature):
    if not signature:
        return (((), 1),)
    output = defaultdict(int)
    q = signature[-1]
    for blocks, mult in block_partitions(signature[:-1]):
        output[tuple(sorted(blocks+(q,)))] += mult
        for value, copies in Counter(blocks).items():
            new = list(blocks); new.remove(value); new.append(value+q)
            output[tuple(sorted(new))] += mult*copies
    return tuple(output.items())


def fiber_splits(signature):
    counter = sorted(Counter(signature).items())
    for chosen in product(*(range(count+1) for _, count in counter)):
        rem, exponent, mult = [], 0, 1
        for (q, count), selected in zip(counter, chosen):
            rem.extend([q]*(count-selected))
            exponent += q*selected
            mult *= math.comb(count, selected)
        yield tuple(rem), exponent, mult


def dickman_under_three(x):
    """Exact analytic expression for 0<=x<=3, evaluated in float64."""
    x = np.asarray(x, dtype=float)
    assert x.min() >= 0 and x.max() <= 3
    y = np.ones_like(x)
    mask = x > 1
    y[mask] -= np.log(x[mask])
    mask = x > 2
    z = x[mask]
    y[mask] += np.log(z-1)*np.log(z)+spence(z)+np.pi**2/12
    return y


class Trial:
    def __init__(self, k, intervals, tilt, dtype="longdouble", config=None):
        self.start = time.monotonic()
        self.k, self.N, self.n = k, intervals, intervals-k
        self.dtype = np.dtype(dtype).type
        self.geo = geometry(config)
        self.hq = self.geo["S"]/intervals
        self.h = self.dtype(self.hq.numerator)/self.hq.denominator
        self.tilt = self.dtype(tilt)
        self.mid = (np.arange(self.n, dtype=self.dtype)+self.dtype(".5"))*self.h
        self.radial = (np.arange(self.n, dtype=self.dtype)+self.dtype(k)/2)*self.h
        self.background_radial = self.radial-self.h/2
        self.centered = self.radial-self.dtype(".9")
        self.g = self.dtype(".105")/(1+self.mid/100)+self.dtype(".895")/(1+self.dtype("181.4")*self.mid)
        self.Zoriginal = np.sum(self.g*self.g)
        self.Z = np.sum(self.g*self.g*np.exp(-self.tilt*self.mid))
        self.weights = self.g*self.g*np.exp(-self.tilt*self.mid)/self.Z
        self.normalization = self.dtype(k)*self.h/self.Z
        signatures, integer_rows = read_coefficients()
        self.coefficients = {sig: np.asarray(row,dtype=self.dtype)/10**10
                             for sig,row in zip(signatures,integer_rows)}
        self.shells = {}
        for role, rows in self.geo["shells"].items():
            lower, output = Q(0), []
            count = k if role == "outer" else k-1
            for upper, cap in rows:
                cap_index = int(cap//self.hq)
                j = np.arange(self.n)+count
                mask = (j > int(lower//self.hq)) & (j <= int(upper//self.hq))
                output.append((cap_index, mask))
                lower = upper
            self.shells[role] = output
        self.caps = sorted({cap for rows in self.shells.values() for cap,_ in rows})
        self.survivals, self.weighted_cache, self.power_cache = {}, {}, {}
        self.block_cache, self.moment_cache = {}, {}
        self.conv_count = 0

    def conv(self, a, b):
        self.conv_count += 1
        return fftconvolve(a,b)[:self.n].astype(self.dtype,copy=False)

    def survival(self, cap):
        if cap not in self.survivals:
            nodes, weights = np.polynomial.legendre.leggauss(8)
            indices = np.arange(self.n,dtype=float)
            values = np.zeros(self.n)
            for x,w in zip((nodes+1)/2,weights/2):
                values += w*dickman_under_three((indices+x)/cap)
            self.survivals[cap] = values.astype(self.dtype)
        return self.survivals[cap]

    def weighted(self, cap, exponent):
        key = cap, exponent
        if key not in self.weighted_cache:
            self.weighted_cache[key] = self.weights*self.survival(cap)*self.mid**exponent
        return self.weighted_cache[key]

    def power(self, cap, count):
        key = cap,count
        if key not in self.power_cache:
            if count==0:
                a=np.zeros(self.n,dtype=self.dtype);a[0]=1
            elif count==1:
                a=self.weighted(cap,0)
            else:
                half=self.power(cap,count//2);a=self.conv(half,half)
                if count%2:a=self.conv(a,self.weighted(cap,0))
            self.power_cache[key]=a
        return self.power_cache[key]

    def blocks(self, cap, blocks):
        key=cap,blocks
        if key not in self.block_cache:
            self.block_cache[key]=(self.power(cap,0) if not blocks else self.weighted(cap,blocks[0])
                                   if len(blocks)==1 else self.conv(self.blocks(cap,blocks[:-1]),self.weighted(cap,blocks[-1])))
        return self.block_cache[key]

    def moment(self, cap, count, signature):
        key=cap,count,signature
        if key not in self.moment_cache:
            a=np.zeros(self.n,dtype=self.dtype)
            for blocks,mult in block_partitions(signature):
                falling=math.prod(range(count-len(blocks)+1,count+1))
                a+=mult*falling*self.conv(self.power(cap,count-len(blocks)),self.blocks(cap,blocks))
            self.moment_cache[key]=a
        return self.moment_cache[key]

    def clear(self):
        self.weighted_cache.clear();self.power_cache.clear()
        self.block_cache.clear();self.moment_cache.clear()

    def square_groups(self):
        entries=list(self.coefficients.items());out={}
        for i,(sig,c) in enumerate(entries):
            for j in range(i,len(entries)):
                eta,d=entries[j]
                key=tuple(sorted(sig+eta))
                arr=np.convolve(c,d)*(1 if i==j else 2)
                out[key]=out.get(key,0)+arr
        return out

    def denominator(self):
        total=self.dtype(0);absolute=self.dtype(0)
        for cap,mask in self.shells["outer"]:
            shell=self.dtype(0)
            for sig,c in self.square_groups().items():
                radial=np.polynomial.polynomial.polyval(self.centered,c)*np.exp(self.tilt*self.radial)
                terms=radial*self.moment(cap,self.k,sig)
                shell+=np.sum(terms[mask])
                absolute+=np.sum(np.abs(terms[mask]))
            total+=shell
            self.clear()
        return total,absolute

    def affine(self):
        grouped={}
        for sig,c in self.coefficients.items():
            for rem,exponent,mult in fiber_splits(sig):
                key=rem,exponent
                grouped[key]=grouped.get(key,0)+mult*c
        rows=[]
        for cap,mask in self.shells["outer"]:
            result={}
            for (rem,exponent),c in grouped.items():
                radial=np.polynomial.polynomial.polyval(self.centered,c)*mask
                fiber=self.g*self.survival(cap)*self.mid**exponent
                corr=fftconvolve(radial,fiber[::-1])[self.n-1:2*self.n-1]
                result[rem]=result.get(rem,0)+corr
            rows.append(result)
        return rows

    def forms(self):
        denominator,den_abs=self.denominator()
        affine=self.affine()
        regions=np.zeros(3,dtype=self.dtype)
        regions_abs=np.zeros(3,dtype=self.dtype)
        previous_moments={}
        for layer,cap in enumerate(self.caps):
            masks=[]
            for role in ("base","enlarged","full"):
                mask=np.zeros(self.n,dtype=bool)
                for inner_cap,inner_mask in self.shells[role]:
                    if cap<=inner_cap:mask |= inner_mask
                masks.append(mask)
            regions_mask=(masks[0],masks[1]&~masks[0],masks[2]&~masks[1])
            rows={}
            for (outer_cap,_),part in zip(self.shells["outer"],affine):
                if cap<=outer_cap:
                    for sig,arr in part.items():rows[sig]=rows.get(sig,0)+arr
            if not rows:
                continue
            keys=sorted(rows)
            integrand=np.zeros(self.n,dtype=self.dtype)
            abs_integrand=np.zeros(self.n,dtype=self.dtype)
            next_moments={}
            for i,sig in enumerate(keys):
                for j in range(i,len(keys)):
                    eta=tuple(sorted(sig+keys[j]))
                    moment=self.moment(cap,self.k-1,eta)
                    next_moments[eta]=moment.copy()
                    diff=moment if layer==0 else moment-previous_moments[eta]
                    term=rows[sig]*rows[keys[j]]*diff*(1 if i==j else 2)
                    integrand+=term;abs_integrand+=abs(term)
            scale=self.normalization*np.exp(self.tilt*self.background_radial)
            for i,mask in enumerate(regions_mask):
                regions[i]+=np.sum((integrand*scale)[mask])
                regions_abs[i]+=np.sum((abs_integrand*scale)[mask])
            previous_moments=next_moments
            self.clear()
        mass,pair,lam=self.dtype(".99998"),self.dtype(str(float(self.geo["pair_constant"]))),self.dtype(".008")
        a=mass*mass-mass*lam;b=(1-mass/lam)*(1-mass)*pair
        numerator=regions[0]+(a+b)*regions[1]+b*regions[2]
        rho=self.dtype(self.geo["rho_star"].numerator)/self.geo["rho_star"].denominator
        quotient=rho*numerator/denominator
        # Return to the source's common normalization for same-grid comparisons.
        normalization_conversion=(self.Z/self.Zoriginal)**self.k
        out={"status":"exploratory cap-only; no outward enclosure or support restoration",
             "geometry": self.geo["metadata"],
             "k":self.k,"inner_dimension":self.k-1,"intervals":self.N,"convolution_length":self.n,
             "dtype":str(np.dtype(self.dtype)),"tilt":float(self.tilt),
             "denominator_tilted_normalization":float(denominator),
             "denominator_original_normalization":float(denominator*normalization_conversion),
             "J_regions_over_I":dict(zip(("base","plus","tail"),map(float,regions/denominator))),
             "rho_J_over_I":float(quotient),"cap_gap_to_one":float(1-quotient),
             "denominator_absolute_contraction_ratio":float(den_abs/abs(denominator)),
             "face_absolute_contraction_ratios":list(map(float,regions_abs/np.maximum(abs(regions),self.dtype("1e-300")))),
             "fft_convolutions":self.conv_count,"seconds":time.monotonic()-self.start,
             "aligned_cap_indices":self.caps,
             "source_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest()}
        return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--k",type=int,default=39)
    ap.add_argument("--intervals",type=int,default=4096)
    ap.add_argument("--tilt",type=float,default=20)
    ap.add_argument("--dtype",choices=("float64","longdouble"),default="longdouble")
    ap.add_argument("--out",type=Path)
    args=ap.parse_args()
    out=Trial(args.k,args.intervals,args.tilt,args.dtype).forms()
    path=args.out or HERE/f"k{args.k}_n{args.intervals}_tilt{args.tilt:g}_{args.dtype}.json"
    path.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2),flush=True)


if __name__=="__main__":
    main()
