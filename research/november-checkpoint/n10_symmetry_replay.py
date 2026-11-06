"""Enumerate Weyl residue sets by lifting residues, independently of partitions."""
from itertools import combinations
from math import comb
from random import Random
import json


def has_balanced_lift(e, n):
    """Lift sorted shifted weights e_j=j+lambda_j, lambda nondecreasing."""
    m = 2*n
    excess = sum(e) - n*(n-1)//2
    if excess < 0 or excess % m:
        return False
    wraps = excess // m
    high = [x for x in e if x >= n]
    # Every possible lift lies in [-n,2n-1]. High residues may wrap once.
    for shifted in combinations(high, wraps):
        w = set(shifted)
        lift = sorted(x-m if x in w else x for x in e)
        pos = sum(max(0, x-j) for j,x in enumerate(lift))
        if pos <= n:
            return True
    return False


def permuted(e, n):
    all_sites = set(range(2*n))
    r = lambda s: tuple(sorted((n-1-x) % (2*n) for x in s))
    c = tuple(sorted(2*n-1-x for x in all_sites.difference(e)))
    return (r(e),c,r(c))


def replay(n):
    m=2*n
    sites=set(range(m))
    weight={e for e in combinations(range(m),n) if has_balanced_lift(e,n)}
    trace = [len(weight),0,0,0]
    for e in weight:
        r,c,rc=permuted(e,n)
        h=sum(x>=n for x in e)
        sign=(-1)**(h*(n-h))
        assert {r,c,rc}<=weight
        trace[1] += sign*(r==e)
        trace[2] += c==e
        trace[3] += sign*(rc==e)

    # Verify the full Jacobi/sorting transformations on actual minors modulo 101.
    # This field has an order-20 primitive root (the code checks its order).
    from flint import nmod_mat
    p=101
    root=next(a for a in range(2,p) if pow(a,m,p)==1 and
              all(pow(a,j,p)!=1 for j in range(1,m)))
    powers=[pow(root,j,p) for j in range(m)]
    def phi(s,e):
        def minor(t):
            return int(nmod_mat([[powers[(i*j)%m] for j in t] for i in s],p).det())
        return minor(e)*pow(minor(range(n)),-1,p)%p
    rng=Random(18211)
    pool=sorted(weight)
    direct=0
    for _ in range(125):
        s=tuple(sorted(rng.sample(range(m),n)))
        e=rng.choice(pool)
        r,c,rc=permuted(e,n)
        sr=tuple(sorted(-i%m for i in s))
        sc=tuple(sorted(sites.difference(s)))
        src=tuple(sorted(-i%m for i in sc))
        h=sum(x>=n for x in e)
        sign=(-1)**(h*(n-h))
        assert phi(sr,e)==sign*phi(s,r)%p
        assert phi(sc,e)==phi(s,c)
        assert phi(src,e)==sign*phi(s,rc)%p
        direct+=3
    return {"n":n,"all_subsets":comb(m,n),"traces":trace,
            "even_R_odd_C":(trace[0]+trace[1]-trace[2]-trace[3])//4,
            "field":p,"primitive_root":root,"individual_minor_equalities":direct}

if __name__=='__main__':
    if not __debug__:
        raise RuntimeError("Run with assertions enabled.")
    print(json.dumps(replay(10),indent=2))
