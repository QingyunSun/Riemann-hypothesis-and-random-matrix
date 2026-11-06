"""Cycle dimension via independent cyclic gap-word orbit keys."""
import json
from collections import defaultdict
from n10_small_minimality import classes


def key(sites,size):
    t=sorted(sites); n=len(t)
    gap=tuple(t[i+1]-t[i] for i in range(n-1))+(size+t[0]-t[-1],)
    return min(g[i:]+g[:i] for g in (gap,gap[::-1]) for i in range(n))


def summary(sites,gap,n):
    size=2*n
    return tuple(sum(1 for a in sites for b in sites if (a-b)%size==r)
                 for r in range(1,n+1)),tuple(sorted(gap))


n=10
pool=set(range(2*n))
orbits={gap:sites for sites,gap in classes(n)}
vertices={gap:summary(sites,gap,n) for gap,sites in orbits.items()}
edges=[]
for gap,sites in orbits.items():
    other=key(pool.difference(sites),2*n)
    if gap<other:
        edges.append((vertices[gap],vertices[other]))

adj=defaultdict(set)
loops=0
for u,v in edges:
    if u==v:
        loops+=1
    adj[u].add(v);adj[v].add(u)
seen=set();components=0
for s in adj:
    if s in seen:continue
    components+=1
    todo=[s];seen.add(s)
    while todo:
        u=todo.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v);todo.append(v)
dim=len(edges)-len(adj)+components
assert len(edges)==2234 and loops==462 and dim==496
print(json.dumps(dict(dihedral_orbits=len(orbits),static_fibres=len(set(vertices.values())),
                     complement_edges=len(edges),self_loops=loops,
                     incident_vertices=len(adj),components=components,
                     circulation_dimension=dim),indent=2))
