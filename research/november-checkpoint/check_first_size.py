"""Check minimal size through N=10. Requires the companion check_protected_survival.py."""
from collections import defaultdict, deque
import json

import numpy as np
from flint import acb, arb, ctx, nmod_mat
from check_protected_survival import (
    is_survivor, modular_rows, partitions, sha256_serialized, summary_fibres,
)


def complement_cycles(n, groups):
    key = {s:summary for summary,fibre in groups.items() for s in fibre}
    pool = set(range(2*n))
    edges, cycles = [], []
    parent, tree = {}, defaultdict(list)

    def root(s):
        while s in parent:
            s = parent[s]
        return s

    for a,u in key.items():
        b = min(tuple(sorted((sign*i+j)%(2*n) for i in pool-set(a)))
                for sign in (1,-1) for j in range(2*n))
        if b<=a:
            continue
        v = key[b]
        j = len(edges)
        edges.append((a,b))
        if u==v:
            cycles.append([(j,1)])
            continue
        uroot, vroot = root(u),root(v)
        if uroot!=vroot:
            parent[uroot]=vroot
            tree[u].append((v,j,1))
            tree[v].append((u,j,-1))
            continue
        q,seen = deque([(v,[])]), {v}
        while q:
            t,path=q.popleft()
            if t==u:
                cycles.append([(j,1)]+path)
                break
            for w,other,sgn in tree[t]:
                if w not in seen:
                    seen.add(w)
                    q.append((w,path+[(other,sgn)]))
    # Check conservation directly on the true summary bins.
    for cycle in cycles:
        div=defaultdict(int)
        for j,sgn in cycle:
            a,b=edges[j];div[key[a]]-=sgn;div[key[b]]+=sgn
        assert not any(div.values())
    return edges,cycles


def even_n_signed_character_traces(n):
    size=2*n
    pool=set(range(size)); sets=set()
    for k in range(n+1):
        for a in partitions(k):
            for b in partitions(k):
                if len(a)+len(b)>n:continue
                nu=a+(0,)*(n-len(a)-len(b))+tuple(-j for j in reversed(b))
                e=tuple(sorted((j+n-1-i)%size for i,j in enumerate(nu)))
                if len(e)==len(set(e)):sets.add(e)
    traces=[0]*4
    for e in sets:
        h=sum(i>=n for i in e)
        sign=(-1)**(h*(n-h))
        reflect=lambda t:tuple(sorted((n-1-j)%size for j in t))
        c=tuple(sorted(size-1-j for j in pool-set(e)))
        for j,(v,sgn) in enumerate([(e,1),(reflect(e),sign),(c,1),(reflect(c),sign)]):
            assert v in sets
            if e==v:traces[j]+=sgn
    return traces


def main():
    out={}
    for n,p,r in [(1,3,2),(2,5,2),(3,7,3),(4,17,2),(5,11,2),
                  (6,109,101),(7,113,7),(8,113,40),(9,109,4)]:
        groups=summary_fibres(n)
        transfers=[(v[0],b) for v in groups.values() for b in v[1:]]
        if transfers:
            rows=[row.tolist() for _,_,row in modular_rows(n,transfers,p,r)]
            rank=nmod_mat(rows,p).rank()
        else:
            rank=0
        assert rank==len(transfers)
        out[str(n)]={'summary_degrees_of_freedom':len(transfers),'rank':rank,'prime':p}

    n=10; prime=101; root=32
    traces=even_n_signed_character_traces(n)
    assert traces==[1957,87,19,129]
    dim=(traces[0]+traces[1]-traces[2]-traces[3])//4
    edges,cycles=complement_cycles(n,summary_fibres(n))
    ids=sorted({j for cyc in cycles for j,_ in cyc})
    loc={j:i for i,j in enumerate(ids)}
    gs=[edges[j] for j in ids]
    D=np.zeros((len(gs),len(cycles)),dtype=np.int64)
    for i,cyc in enumerate(cycles):
        for j,sgn in cyc:D[loc[j],i]=sgn
    coefficients = np.array([row for _,_,row in modular_rows(n,gs,prime,root)])
    tableau = (coefficients@D)%prime
    rank0=nmod_mat(tableau.tolist(),prime).rank()
    assert rank0==473
    ctx.prec=144
    roots=[acb(arb(j)/n).exp_pi_i() for j in range(2*n)]
    evidence={}
    for t in (72,70):
        heat=[(arb(t+1)/t)**(j*(n-j)) for j in range(n+1)]
        d=np.array([is_survivor(b,roots,heat)-is_survivor(a,roots,heat) for a,b in gs])@D
        tableau=np.vstack((tableau,d%prime))
        evidence[f'{t+1}/{t}']={'combined_augmented_rank':nmod_mat(tableau.tolist(),prime).rank(),
                               'sha256_signed_cycle_events':sha256_serialized(d.tolist())}
    assert evidence['71/70']['combined_augmented_rank']>dim
    out['10']={'edges':len(edges),'cycles':len(cycles),'selfloops':sum(len(c)==1 for c in cycles),
               'edges_used':len(gs),'involution_traces':traces,'odd_upper_bound':dim,
               'rank_mod_101':rank0,'two_events':evidence}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
