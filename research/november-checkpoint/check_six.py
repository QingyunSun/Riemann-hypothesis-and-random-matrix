"""Independent exact six-of-twelve verification using integer pairs for 2 cos(kπ/6)."""
from collections import defaultdict
from itertools import combinations, product
from math import comb

# The pair (u, v) represents u + sqrt(3)*v.
COS2 = ((2, 0), (0, 1), (1, 0), (0, 0), (-1, 0), (0, -1),
        (-2, 0), (0, -1), (-1, 0), (0, 0), (1, 0), (0, 1))


def representative(sites):
    return min(tuple(sorted((sign*x+r) % 12 for x in sites))
               for sign in (1, -1) for r in range(12))


def summary(sites):
    counts = tuple(sum((x+r) % 12 in sites for x in sites) for r in range(12))
    gaps = tuple(sorted((sites[(j+1) % 6]-x) % 12 for j,x in enumerate(sites)))
    return counts, gaps


def doubled_cubic(sites, k):
    terms = [COS2[(a+(k-1)*b-k*c) % 12] for a,b,c in product(sites, repeat=3)]
    return tuple(map(sum, zip(*terms)))


def main():
    subsets = list(combinations(range(12),6))
    assert len(subsets) == comb(12,6) == 924
    orbits = sorted({representative(s) for s in subsets})
    fibres = defaultdict(list)
    for s in orbits:
        fibres[summary(s)].append(s)
    pairs = sorted(group for group in fibres.values() if len(group)>1)
    assert (len(orbits),len(fibres),[len(g) for g in pairs]) == (50,47,[2]*3)
    rows = []
    for k in (2,3,4):
        row = []
        for a,b in pairs:
            delta = tuple(x-y for x,y in zip(doubled_cubic(a,k),doubled_cubic(b,k)))
            assert all(x % 2 == 0 for x in delta)
            row.append(tuple(x//2 for x in delta))
        rows.append(row)
    expected = [[(4,0),(2,0),(-6,4)], [(-8,0),(-4,0),(-6,2)],
                [(0,0),(12,0),(6,-6)]]
    assert rows == expected
    # Nonzero determinant modulo 13, reducing sqrt(3) to 4.
    (a,b,c),(d,e,f),(g,h,i) = [[(u+4*v)%13 for u,v in row] for row in rows]
    det = (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%13
    assert det == (864-480*4)%13 != 0
    print(dict(subsets=len(subsets),orbits=len(orbits),summaries=len(fibres),
               difference_matrix=rows,determinant_mod_13=det))


if __name__ == "__main__":
    main()
