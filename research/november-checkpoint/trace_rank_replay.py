"""Independent ACUE protected-rank replay: Weyl alternants and direct trace tests.

Needs python-flint (nmod_mat). The exact alternant count gives the upper bound.
Reduction in a splitting prime, evaluated at sites with literal power sums,
supplies the matching lower bound for each row of the output.
"""
from itertools import combinations
import json
from flint import nmod_mat


def partitions(n, ceiling=None):
    if n == 0:
        yield ()
    else:
        for j in range(min(ceiling or n, n), 0, -1):
            for tail in partitions(n - j, j):
                yield (j, *tail)


def orbits(n):
    m = 2*n
    seen = set()
    reps = []
    for e in combinations(range(m), n):
        if e not in seen:
            reps.append(e)
            for t in range(m):
                seen.add(tuple(sorted((j+t) % m for j in e)))
    return reps


def alternants(n, ps):
    m = 2*n
    counts = set()
    weights = 0
    vanishing = 0
    for group in ps:
        for a in group:
            for b in group:
                if len(a) + len(b) > n:
                    continue
                weights += 1
                ell = [-x for x in a]
                ell += [0]*(n-len(a)-len(b)) + list(reversed(b))
                residues = tuple(sorted((j+x) % m for j,x in enumerate(ell)))
                if len(set(residues)) == n:
                    counts.add(residues)
                else:
                    vanishing += 1
    return len(counts), weights, vanishing


def prime_order_root(p, m):
    return next(x for x in range(2,p) if pow(x,m,p)==1 and
                all(pow(x,k,p)!=1 for k in range(1,m)))


def test_rank(n, p):
    m = 2*n
    r = prime_order_root(p,m)
    ps = [list(partitions(w)) for w in range(n+1)]
    roots = [pow(r,i,p) for i in range(m)]
    reps = orbits(n)
    rows = []
    # Columns in nmod_mat correspond to tests, rows to orbits.
    for cells in reps:
        sums = [sum(roots[(i*k)%m] for i in cells) % p for k in range(m)]
        vals = []
        for group in ps:
            pos, neg = [], []
            for lam in group:
                a=b=1
                for k in lam:
                    a = a*sums[k] % p
                    b = b*sums[-k] % p
                pos.append(a)
                neg.append(b)
            vals.extend(a*b % p for a in pos for b in neg)
        rows.append(vals)
    rk = nmod_mat(rows,p).rank()
    count,w,zeros = alternants(n,ps)
    assert rk == count
    return dict(n=n, prime=p, root=r, orbits=len(reps), tests=len(rows[0]),
                modular_rank=rk, admissible_highest_weights=w,
                vanishing_alternants=zeros, distinct_weyl_residues=count,
                affine_tilt_dimension=len(reps)-rk)


if __name__=='__main__':
    cases = [(n, next(p for p in [97,109,113,127,193,211,241,257]
                      if (p-1)%(2*n)==0)) for n in range(2,9)]
    cases.append((8,257))
    print(json.dumps([test_rank(n,p) for n,p in cases], indent=2))
