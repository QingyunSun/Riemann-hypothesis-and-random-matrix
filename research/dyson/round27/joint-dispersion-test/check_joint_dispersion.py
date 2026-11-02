#!/usr/bin/env python3
"""Exact finite coefficient/Gram identities and source parameter margins."""
from fractions import Fraction as F
from collections import defaultdict
from hashlib import sha256
from pathlib import Path
from math import gcd
import json
HERE=Path(__file__).resolve().parent

def factor(n):
    fs={}; p=2
    while p*p<=n:
        while n%p==0: fs[p]=fs.get(p,0)+1; n//=p
        p+=1
    if n>1: fs[n]=1
    return fs

def mu(n):
    f=factor(n)
    return 0 if any(v>1 for v in f.values()) else (-1)**len(f)

def aval(n,D,K):
    ans=defaultdict(int)
    for d in range(D+1,2*D+1):
        if d%2 and n%d==0:
            k=n//d
            if k%2 and K<k<=2*K:
                for p,e in factor(k).items(): ans[p]+=mu(d)*e
    return {p:e for p,e in ans.items() if e}

assert aval(253,10,20)=={23:-1}
assert aval(345,10,20)=={23:1}
counts={"actual_signed_convolution_coefficient_examples":2}

# Formal labels F_dk suffice for exact Gram expansion; no sampled primes.
ds=[3,5,7,9]
ks=[5,7,9]
# Rational arbitrary table stands for actual f(dk); product collisions retained.
f={d*k:F((d*k)%11-5,1+(d*k)%7) for d in ds for k in ks}
C=[[f[d*k] for k in ks] for d in ds]
a=[F(mu(d)) for d in ds]
b=[F(2),F(-3,2),F(7,3)]  # arbitrary vector; identity also holds for log k
Cb=[sum(C[i][j]*b[j] for j in range(len(ks))) for i in range(len(ds))]
direct=sum(x*x for x in Cb)
gram=sum(b[j]*b[k]*sum(C[i][j]*C[i][k] for i in range(len(ds)))
         for j in range(len(ks)) for k in range(len(ks)))
assert direct==gram
pair=sum(a[i]*Cb[i] for i in range(len(ds)))
assert pair*pair<=sum(x*x for x in a)*gram
counts["joint_Gram_and_fixed_vector_Cauchy"] = 2

# Full centered product, including all singleton terms.
n=0
for u in [F(0),F(2),F(7,3)]:
    for v in [F(-1),F(0),F(11,5)]:
        assert (u-2)*(v-2)==u*v-2*u-2*v+4
        n+=1
counts["centered_two_prime_product_expansion"]=n

w,delta,sigma,retreat=F(1,200),F(1,1000),F(1,10),F(1,1000)
source_values=[72*w+24*delta,48*w+16*delta+4*sigma,64*w+20*delta+2*sigma]
assert source_values==[F(48,125),F(82,125),F(27,50)]
assert all(v<1 for v in source_values)
assert F(1,2)+2*w-retreat==F(509,1000)
counts["source_186_exact_parameter_checks"]=4

q1,q2,theta=F(1,3),F(49,100),F(1,2)
eps=F(1,100)
margins={
 "B_order60":60*(theta-q2)-q2,
 "principal_mask":theta-q2,
 "cofactor_grid":2-theta-2*q2,
 "joint_RH":q1*(F(1,2)-eps),
 "nonprimitive":F(1,2)-eps,
}
assert list(margins.values())==[F(11,100),F(1,100),F(13,25),F(49,300),F(49,100)]
assert all(v>0 for v in margins.values())
counts["medium_band_power_margins"]=5

# Dense-support obstruction for actual prime p, with an exact rational allocation.
# These small examples illustrate the same divisor gap; asymptotic PNT is not sampled.
for p,yy,U in [(101,F(2),F(10)),(1009,F(3),F(31))]:
    assert 1<U/yy<U<p
    assert not any(U/yy<=v<=U for v in [1,p])
    assert 2<U/yy
    assert not any(U/yy<=v<=U for v in [1,2,p,2*p])
counts["prime_and_twice_prime_dense_divisor_gap_examples"]=4

out={"status":"PASS","scope":"Exact finite algebra only; no large-prime scan or unproved operator-norm test.",
"author_sha256":sha256((HERE/'JOINT_DISPERSION_TEST.md').read_bytes()).hexdigest(),
"check_groups":counts,"total_scalar_cases":sum(counts.values()),
"medium_band_power_margins":{k:str(v) for k,v in margins.items()},
"source_186_lhs":[str(v) for v in source_values],"source_level":str(F(1,2)+2*w-retreat),
"Frobenius_to_block_power_at_Y_sqrtX":str(F(1,4))}
encoded=json.dumps(out,indent=2,sort_keys=True)+"\n"
(HERE/'exact_check_results.json').write_text(encoded)
print(encoded,end="")

