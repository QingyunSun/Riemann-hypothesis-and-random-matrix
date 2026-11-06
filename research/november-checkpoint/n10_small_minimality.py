"""Independent small-size rigidity using cyclic gap-word canonicalization."""
from collections import defaultdict
from itertools import combinations
from math import comb
from flint import nmod_mat
import json


def partitions(n, ceiling=None):
    if n==0:
        yield ()
        return
    for j in range(min(ceiling or n,n),0,-1):
        for tail in partitions(n-j,j):
            yield (j,)+tail


def classes(n):
    size=2*n
    seen=set()
    for rest in combinations(range(1,size),n-1):
        sites=(0,)+rest
        gap=tuple(sites[i+1]-sites[i] for i in range(n-1))+(size-sites[-1],)
        candidates=[]
        for seq in (gap,gap[::-1]):
            candidates.extend(seq[i:]+seq[:i] for i in range(n))
        canonical=min(candidates)
        if canonical not in seen:
            seen.add(canonical)
            loc=[0]
            for d in canonical[:-1]:
                loc.append(loc[-1]+d)
            yield tuple(loc),canonical


def replay(n):
    size=2*n
    groups=defaultdict(list)
    orbits=0
    for sites,gaps in classes(n):
        delta=tuple(sum(1 for a in sites for b in sites if (a-b)%size==r)
                    for r in range(1,n+1))
        groups[(delta,tuple(sorted(gaps)))].append(sites)
        orbits+=1
    pairs=[(cls[0],c) for cls in groups.values() for c in cls[1:]]
    if not pairs:
        return dict(n=n,orbits=orbits,fibres=len(groups),free_parameters=0,rank=0)
    p=next(a for a in range(size+1,1000) if (a-1)%size==0 and all(a%d for d in range(2,a)))
    omega=next(a for a in range(2,p) if pow(a,size,p)==1
               and all(pow(a,j,p)!=1 for j in range(1,size)))
    table=[]
    pos=[[sum(pow(omega,j*x%size,p) for x in s)%p for j in range(size)]
         for pair in pairs for s in pair]
    def trace(s,lam,sign):
        a=1
        for j in lam:
            a=a*s[sign*j]%p
        return a
    for k in range(n+1):
        ps=list(partitions(k))
        for a in ps:
            for b in ps:
                v=[(trace(s,a,1)*trace(s,b,-1)+trace(s,b,1)*trace(s,a,-1))%p
                   for s in pos]
                table.append([(v[i+1]-v[i])%p for i in range(0,len(v),2)])
    rank=nmod_mat(table,p).rank()
    assert rank==len(pairs)
    return dict(n=n,orbits=orbits,fibres=len(groups),free_parameters=len(pairs),
                rank=rank,prime=p,primitive_root=omega)


if __name__=='__main__':
    print(json.dumps([replay(n) for n in range(1,10)],indent=2))
