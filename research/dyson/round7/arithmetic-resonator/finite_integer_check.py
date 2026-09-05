#!/usr/bin/env python3
"""Evaluate the frozen rational marked resonator on actual integers.
No finite-L value is an asymptotic or zeta-zero theorem.
"""
from pathlib import Path
import json,time,math
import numpy as np
from numpy.polynomial.legendre import legval
from scipy.sparse import csr_matrix
HERE=Path(__file__).resolve().parent

def arithmetic_data(L,ell):
    spf=np.zeros(L+1,dtype=np.int32)
    for p in range(2,L+1):
        if spf[p]==0:
            view=spf[p::p];view[view==0]=p
    primes=np.flatnonzero(spf==np.arange(L+1));primes=primes[primes>=2]
    d=np.ones(L+1);s2=np.zeros(L+1);s3=np.zeros(L+1);C=np.zeros(L+1)
    exponent=np.zeros(L+1,dtype=np.int8);u=np.log(np.arange(1,L+1))/np.log(L)
    for n in range(2,L+1):
        p=int(spf[n]);m=n//p;repeat=m%p==0
        e=int(exponent[m])+1 if repeat else 1;exponent[n]=e
        d[n]=d[m]*(ell+e-1)/e
        t=math.log(p)/math.log(L)
        s2[n]=s2[m]+(0 if repeat else t*t)
        s3[n]=s3[m]+(0 if repeat else t*t*t)
        C[n]=C[m]+(0 if repeat else int(p*p>L))
    assert np.all((C==0)|(C==1))
    return primes,u,d[1:],s2[1:],s3[1:],C[1:]

def operator(L,primes):
    rows=[];cols=[];values=[]
    for p in primes:
        q=int(p);e=1
        while q<=L:
            m=np.arange(1,L//q+1);rows.append(q*m-1);cols.append(m-1)
            values.append(np.full(len(m),2*np.sin(np.pi/2*np.log(q)/np.log(L))/(e*np.sqrt(q))))
            if q>L//int(p):break
            q*=int(p);e+=1
    return csr_matrix((np.concatenate(values),(np.concatenate(rows),np.concatenate(cols))),shape=(L,L))

def amplitude(features,coeffs,v,s2,s3,C):
    H=np.zeros(len(v));powers={2:s2,3:s3}
    for (degree,ks,marked),coefficient in zip(features,coeffs):
        term=legval((4*v-3) if marked else (2*v-1),[0]*degree+[1])
        if marked:term*=C
        for k in ks:term*=powers[k]
        H+=coefficient*term
    return H

def main():
    source=json.loads((HERE/'large_prime_sector_d4_q40.json').read_text())
    integers=np.rint(np.asarray(source['enlarged']['coefficients'])*10**8).astype(np.int64)
    coeffs=integers/10**8;mat=np.load(HERE/'large_prime_sector_d4_q40.npz')
    norm=float(coeffs@mat['G']@coeffs);margin=float(coeffs@mat['M']@coeffs/norm-.25)
    rational={'ell_exact':'27/25','denominator':10**8,'coefficient_integers':integers.tolist(),
              'features':source['features'],'continuum_quadrature_norm':norm,
              'continuum_quadrature_margin':margin,'status':'fixed rational coefficients; integrals not outward enclosed'}
    (HERE/'fixed_rational_vector.json').write_text(json.dumps(rational,indent=2)+'\n')
    rows=[]
    for L in (10000,100000,1000000):
        start=time.monotonic();ps,v,d,s2,s3,C=arithmetic_data(L,27/25);A=operator(L,ps)
        H=amplitude(source['features'],coeffs,v,s2,s3,C);x=d*H/np.sqrt(np.arange(1,L+1))
        ax=A@x;aa=A@ax;norm=float(x@x)
        row={'L':L,'theta':1,'norm':norm,'AstarA':float(ax@ax/norm),
             'A2':float(x@aa/norm),'margin':float((ax@ax+x@aa)/(2*np.pi**2*norm)-.25),
             'number_with_large_prime':int(C.sum()),'prime_power_nnz':A.nnz,'seconds':time.monotonic()-start}
        rows.append(row);print(json.dumps(row),flush=True)
    (HERE/'finite_integer_results.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
