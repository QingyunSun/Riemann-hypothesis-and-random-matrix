"""Replay the six-orbit rigidity and 11-particle protected survival certificates.

Requirements: Python >=3.10, numpy, python-flint (tested with 0.9.0).
All survivor tests use real/complex Arb balls via python-flint. No floats.
"""
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from functools import lru_cache

import numpy as np
from flint import acb, arb, ctx, nmod_mat


@lru_cache(None)
def partitions(k, cap=None):
    if k == 0:
        return [()]
    return [(j,) + v for j in range(min(k, cap or k), 0, -1)
            for v in partitions(k - j, j)]


def summary_fibres(n):
    size, mask = 2*n, (1 << (2*n))-1
    seen, groups = set(), defaultdict(list)
    for sites in itertools.combinations(range(size), n):
        word = sum(1 << j for j in sites)
        if word in seen:
            continue
        mirror = int(f'{word:0{size}b}'[::-1], 2)
        for b in (word, mirror):
            seen.update(((b << j) | (b >> (size-j))) & mask for j in range(size))
        gaps = tuple(sorted((sites[(i+1) % n] - j) % size for i, j in enumerate(sites)))
        pairs = tuple((word & (((word << j) | (word >> (size-j))) & mask)).bit_count()
                      for j in range(1, n+1))
        groups[pairs, gaps].append(sites)
    return groups


def matching_complements(n, groups):
    size = 2*n
    pool = set(range(size))
    out = []
    for family in groups.values():
        if len(family) < 2:
            continue
        for a in family:
            sites = pool-set(a)
            b = min(tuple(sorted((sign*i+j) % size for i in sites))
                    for sign in (1, -1) for j in range(size))
            if a < b and b in family:
                out.append((a, b))
    return out


def odd_even_dimension(n):
    size = 2*n
    if n % 2 != 1:
        raise ValueError("the unsigned involution formula here requires odd N")
    index_sets = set()
    for k in range(n+1):
        for a, b in itertools.product(partitions(k), repeat=2):
            if len(a)+len(b) > n:
                continue
            nu = a+(0,)*(n-len(a)-len(b))+tuple(-q for q in reversed(b))
            e = tuple(sorted((u+n-1-j) % size for j, u in enumerate(nu)))
            if len(set(e)) == n:
                index_sets.add(e)
    pool, counts = set(range(size)), [0]*4
    def reflect(e):
        return tuple(sorted((n-1-j) % size for j in e))
    for e in index_sets:
        c = tuple(sorted(size-1-j for j in pool-set(e)))
        images = (e, reflect(e), c, reflect(c))
        assert set(images) <= index_sets
        for j, target in enumerate(images):
            counts[j] += (e == target)
    return counts, (counts[0]+counts[1]-counts[2]-counts[3])//4


def is_survivor(sites, roots, heat):
    n = len(sites)
    coeffs = [acb(1)]
    for j in sites:
        z = roots[j]
        coeffs = ([-z*coeffs[0]] +
                  [a-z*b for a,b in zip(coeffs, coeffs[1:])] + [coeffs[-1]])
    coeffs = [a*h for a,h in zip(coeffs, heat)]
    power = [acb(n)]
    for k in range(1, n):
        power.append(-(k*coeffs[n-k] + sum(coeffs[n-j]*power[k-j] for j in range(1,k))))
    lower = [[acb(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        pivot = (power[0]-sum(lower[i][k]*lower[i][k].conjugate()*pivots[k]
                               for k in range(i))).real
        if pivot < 0:
            return 0
        if not pivot > 0:
            raise ArithmeticError(f'Uncertified pivot at {sites}, {i}: {pivot}')
        pivots.append(pivot)
        for j in range(i+1,n):
            lower[j][i] = (power[j-i] - sum(lower[j][k]*lower[i][k].conjugate()*pivots[k]
                                            for k in range(i))) / pivot
    return 1


def modular_rows(n, transfers, p, root):
    size = 2*n
    assert pow(root,size,p) == 1 and all(pow(root,j,p) != 1 for j in range(1,size))
    sites = [s for transfer in transfers for s in transfer]
    root_powers = [pow(root,j,p) for j in range(size)]
    values = np.array([[sum(root_powers[(i*j)%size] for i in s) % p for s in sites]
                       for j in range(size)], dtype=np.int64)
    def trace(part, sign):
        out = np.ones(len(sites), dtype=np.int64)
        for j in part:
            out = out * values[sign*j] % p
        return out
    for k in range(1,n+1):
        parts = partitions(k)
        plus = [trace(part,1) for part in parts]
        minus = [trace(part,-1) for part in parts]
        for i, a in enumerate(parts):
            for j, b in enumerate(parts[i:], i):
                both = plus[i]*minus[j] + plus[j]*minus[i]
                diff = (both[1::2]-both[::2]) % p
                if np.any(diff):
                    yield a,b,diff


def sha256_serialized(obj):
    buf = json.dumps(obj, separators=(',', ':')).encode()
    return hashlib.sha256(buf).hexdigest()


def main():
    six = summary_fibres(6)
    blocks = [tuple(f) for f in six.values() if len(f) > 1]
    rows = {}
    for a,b,row in modular_rows(6, blocks, 109, 101):
        if sorted((len(a),len(b))) == [1,2] and (a,b) in [
                ((2,), (1,1)), ((3,), (2,1)), ((4,), (3,1))]:
            rows[sum(a)] = row.tolist()
    rq = nmod_mat([rows[k] for k in (2,3,4)], 109).rank()
    assert (sum(map(len,six.values())),len(six),len(blocks),rq) == (50,47,3,3)
    n, prime, root = 11, 199, 181
    groups = summary_fibres(n)
    transfers = matching_complements(n, groups)
    assert len(transfers) == 1489
    counts, bound = odd_even_dimension(n)
    assert counts == [3956,106,22,184] and bound == 964
    ctx.prec = 144
    roots = [acb(arb(j)/n).exp_pi_i() for j in range(2*n)]
    heat = [(arb(85)/84)**(j*(n-j)) for j in range(n+1)]
    outcomes = [[is_survivor(s,roots,heat) for s in pair] for pair in transfers]
    d = [b-a for a,b in outcomes]
    table = [row.tolist() for _,_,row in modular_rows(n, transfers, prime, root)]
    base = nmod_mat(table,prime).rank()
    aug = nmod_mat(table+[[v%prime for v in d]],prime).rank()
    assert (base,aug) == (964,965)
    print(json.dumps({
        'N6': {'orbits':50,'summary_fibres':47,'three_double_fibres':blocks,
               'three_cubic_rank_mod_109':rq},
        'N11': {'transfers':len(transfers),'dihedral_orbits':sum(map(len,groups.values())),
                'involution_traces':counts,'protected_rank_upper_bound':bound,
                'modulus':prime,'primitive_root_of_unity':root,
                'nonzero_rows_mod_prime':len(table),'protected_rank_mod_prime':base,
                'augmented_rank_mod_prime':aug, 'exp_elapsed_time':'85/84',
                'arb_precision_bits':ctx.prec, 'surviving_each_side':list(map(sum,zip(*outcomes))),
                'signed_counts':dict(sorted(Counter(d).items())),
                'sha256_transfer_order':sha256_serialized(transfers),
                'sha256_survival_differences':sha256_serialized(d)}},indent=2))


if __name__ == '__main__':
    main()
