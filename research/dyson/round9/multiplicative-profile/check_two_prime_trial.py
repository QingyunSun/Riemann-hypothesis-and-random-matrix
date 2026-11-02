#!/usr/bin/env python3
"""Fixed exact integer identities, independent quadratures, and one frozen trial."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import math
import time
import numpy as np
from numpy.polynomial.legendre import legval
from scipy.integrate import quad
from scipy.sparse import csr_matrix
from two_large_prime_sector import marked_values, choose_two, PRIOR_SHA

HERE = Path(__file__).resolve().parent
ell, a, cutoff = F(27,25), F(27,25)**2, 120


def factors(n):
    fs = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            fs[p] = fs.get(p,0)+1
            n //= p
        p += 1
    if n > 1:
        fs[n] = 1
    return fs


fs = {n:factors(n) for n in range(1,cutoff+1)}
primes = [n for n in range(2,cutoff+1) if fs[n] == {n:1}]
labels = {p:F(p,cutoff) for p in primes}
divisor = {}
for n in fs:
    d = F(1)
    for e in fs[n].values():
        for j in range(e):
            d *= (ell+j)/(j+1)
    divisor[n] = d
counts = {n:sum(p**3>cutoff for p in fs[n]) for n in fs}
mark = {n:counts[n]*(counts[n]-1)//2 for n in fs}
V = {n:sum((e*labels[p] for p,e in fs[n].items()),F(0)) for n in fs}
S2 = {n:sum((labels[p]**2 for p in fs[n]),F(0)) for n in fs}
S3 = {n:sum((labels[p]**3 for p in fs[n]),F(0)) for n in fs}
phi = lambda v,s2,s3: 1+v+s2*s2+s3
assert all(c in (0,1,2) for c in counts.values())
lhs = sum((divisor[n]**2*mark[n]*phi(V[n],S2[n],S3[n])/n for n in fs),F(0))
rhs, pairs = F(0), 0
for p in primes:
    for q in primes:
        if p >= q or p**3 <= cutoff or q**3 <= cutoff:
            continue
        for m in range(1,cutoff//(p*q)+1):
            assert m**3 < cutoff and m < min(p,q)
            assert p not in fs[m] and q not in fs[m]
            assert divisor[p*q*m]**2 == a*a*divisor[m]**2
            rhs += a*a*divisor[m]**2/(p*q*m)*phi(V[m]+labels[p]+labels[q],S2[m]+labels[p]**2+labels[q]**2,S3[m]+labels[p]**3+labels[q]**3)
            pairs += 1
assert lhs == rhs
triples = 0
for p,q in product(primes,repeat=2):
    if p == q:
        continue
    for m in range(1,cutoff//(p*q)+1):
        if p in fs[m] or q in fs[m]:
            continue
        ip, iq, c = int(p**3>cutoff), int(q**3>cutoff), counts[m]
        assert mark[m*p] == mark[m]+c*ip
        assert mark[m*p*q] == mark[m]+c*(ip+iq)+ip*iq
        assert divisor[m*p]*divisor[m*q] == a*divisor[m]**2
        assert divisor[m]*divisor[m*p*q] == a*divisor[m]**2
        triples += 1
newton = 0
for ci,cj,dl,dr in product((0,1),(0,1),range(3),range(3)):
    def value(c):
        return (F((c+dl)*(c+dl-1),2) if ci else F(1))*(F((c+dr)*(c+dr-1),2) if cj else F(1))
    q0,q1,q2 = [value(c) for c in (0,1,2)]
    for c in (0,1,2):
        assert value(c) == q0+(q1-q0)*c+(q2-2*q1+q0)*F(c*(c-1),2)
        newton += 1

# Independent nested adaptive integration at one interior point. This uses the
# raw marked-prime formula, not the Jacobi substitutions in the trial code.
aa, v, tau = float(a), .91, 1/3
quad_checks = []
for ks in ((),(2,)):
    def outer(p):
        def inner(q):
            rem = max(0.,v-p-q)
            polynomial = 1 if not ks else p*p+q*q+rem*rem/(aa+1)
            return rem**(aa-1)*polynomial/(p*q)
        return quad(inner,tau,v-p,epsabs=2e-13,epsrel=2e-13)[0]
    independent = aa*aa/2*v**(1-aa)*quad(outer,tau,v-tau,epsabs=2e-13,epsrel=2e-13)[0]
    gaussian = float(marked_values(aa,ks,(v,),2,40)[0])*(v-2*tau)**(aa+1)
    assert abs(independent-gaussian) < 2e-12
    quad_checks.append({'powers':ks,'independent_adaptive':independent,'gauss':gaussian,'absolute_difference':abs(independent-gaussian)})

source = json.loads((HERE/'two_large_prime_d4_q32.json').read_text())
mat = np.load(HERE/'two_large_prime_d4_q32.npz')
integers = np.rint(np.asarray(source['enlarged']['coefficients'])*10**8).astype(np.int64)
coeff = integers/10**8
norm = float(coeff@mat['G']@coeff)
frozen = {'ell_exact':'27/25','threshold_exact':'1/3','denominator':10**8,
          'coefficient_integers':integers.tolist(),'features':source['features'],
          'radial_basis':source['radial_basis'],'continuum_quadrature_norm':norm,
          'continuum_quadrature_margin':float(coeff@mat['M']@coeff/norm-.25),
          'status':'fixed rational vector; integrals are floating, not outward enclosed'}
(HERE/'fixed_rational_vector.json').write_text(json.dumps(frozen,indent=2)+'\n')

# Single actual-integer evaluation, including all prime powers of A_L.
L = 100000
started = time.monotonic()
spf = np.zeros(L+1,dtype=np.int32)
for p in range(2,L+1):
    if spf[p] == 0:
        values = spf[p::p]
        values[values == 0] = p
ps = np.flatnonzero(spf == np.arange(L+1)); ps = ps[ps >= 2]
d = np.ones(L+1); s2 = np.zeros(L+1); s3 = np.zeros(L+1); C = np.zeros(L+1,dtype=np.int8); exponent = np.zeros(L+1,dtype=np.int8)
for n in range(2,L+1):
    p, m = int(spf[n]), n//int(spf[n])
    repeat = m%p == 0
    e = int(exponent[m])+1 if repeat else 1
    exponent[n] = e
    d[n] = d[m]*(float(ell)+e-1)/e
    u = math.log(p)/math.log(L)
    s2[n] = s2[m]+(0 if repeat else u*u)
    s3[n] = s3[m]+(0 if repeat else u*u*u)
    C[n] = C[m]+(0 if repeat else int(p**3>L))
assert np.all((C>=0)&(C<=2))
D = C[1:]*(C[1:]-1)/2
v = np.log(np.arange(1,L+1))/np.log(L)
H = np.zeros(L)
for (degree,ks,marked),c in zip(source['features'],coeff):
    term = legval(6*v-5 if marked else 2*v-1,[0]*degree+[1])
    if marked:
        term *= D
    for k in ks:
        term *= s2[1:] if k == 2 else s3[1:]
    H += c*term
rows,cols,data = [],[],[]
for p in ps:
    q,e = int(p),1
    while q <= L:
        m = np.arange(1,L//q+1)
        rows.append(q*m-1); cols.append(m-1)
        data.append(np.full(len(m),2*np.sin(np.pi/2*np.log(q)/np.log(L))/(e*np.sqrt(q))))
        if q > L//int(p):
            break
        q *= int(p); e += 1
operator = csr_matrix((np.concatenate(data),(np.concatenate(rows),np.concatenate(cols))),shape=(L,L))
x = d[1:]*H/np.sqrt(np.arange(1,L+1)); ax = operator@x; aax = operator@ax
xn = float(x@x)
finite = {'L':L,'theta':1,'norm':xn,'AstarA':float(ax@ax/xn),'A2':float(x@aax/xn),
          'margin':float((ax@ax+x@aax)/(2*np.pi**2*xn)-.25),
          'number_with_D_equal_one':int(D.sum()),'prime_power_nnz':operator.nnz,'seconds':time.monotonic()-started,
          'scope':'fixed rational coefficients on actual integers; not an asymptotic theorem or zero sample'}
result = {'status':'PASS','exact_integer_cutoff':cutoff,'ell_exact':str(ell),
          'unique_unordered_double_large_prime_decompositions':pairs,
          'coprime_ordered_insertion_triples':triples,'Newton_exact_state_checks':newton,
          'exact_marked_Fraction_identity':lhs == rhs,'adaptive_moment_checks':quad_checks,
          'finite_integer_evaluation':finite,'prior_source_sha256':PRIOR_SHA,
          'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
