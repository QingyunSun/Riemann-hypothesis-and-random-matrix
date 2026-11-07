"""Independent checks for lift atom identities and the exact Dyson mass."""
import itertools
import json
from fractions import Fraction
from math import factorial
from pathlib import Path
from flint import arb, acb, acb_mat, ctx

ctx.prec = 192

def atom(sites, size):
    n = len(sites)
    value = arb(1) / size**n
    for i, a in enumerate(sites):
        for b in sites[i+1:]:
            value *= 4 * (arb(b-a)/size*arb.pi()).sin()**2
    return value

def overlaps(x, y):
    return (x-y).contains(0)

def main():
    identities = 0
    mass_records = []
    for n in range(1, 9):
        total, purity = arb(0), arb(0)
        clock_bound = arb(1)/2**n
        for s in itertools.combinations(range(2*n), n):
            p = atom(s, 2*n)
            assert p > 0
            assert p.lower() <= clock_bound.upper()
            total += p
            purity += p*p
            if n <= 6:
                for r in (2, 3):
                    lifted = tuple(sorted(a+2*n*j for a in s for j in range(r)))
                    assert overlaps(atom(lifted, 2*n*r), p**r)
                    identities += 1
        exact = Fraction(factorial(2*n), factorial(n)*(4*n)**n)
        rational = arb(exact.numerator)/exact.denominator
        assert total.contains(1)
        assert overlaps(purity, rational)
        assert overlaps(atom(tuple(range(0, 2*n, 2)), 2*n), clock_bound)
        mass_records.append({"n": n, "purity_exact": str(exact), "purity_ball": str(purity)})
    fibre_checks = 0
    for n, r in ((1, 2), (2, 2), (2, 3), (3, 2)):
        N, M = n*r, 2*n*r
        for sites in itertools.combinations(range(M), N):
            s = set(sites)
            pair_count = len(s & {(x+2*n) % M for x in s})
            seed = {x % (2*n) for x in s}
            actual_lift = {a+2*n*j for a in seed for j in range(r)}
            is_lift = len(seed) == n and actual_lift == s
            assert (pair_count == N) == is_lift
            fibre_checks += 1
    n = 11
    exact11 = Fraction(factorial(2*n), factorial(n)*(4*n)**n)
    record = {
        "precision_bits": ctx.prec,
        "direct_lift_atom_checks": identities,
        "full_pair_fibre_membership_checks": fibre_checks,
        "purity_formulas_checked": mass_records,
        "N11_twofold_lift_mass_exact": str(exact11),
        "N11_twofold_lift_mass_decimal": str(arb(exact11.numerator)/exact11.denominator),
        "scope": "Numerical interval checks supplement the general algebraic proofs."
    }
    out = Path(__file__).with_name("LIFT_CHECKS.json")
    out.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps(record, indent=2))

if __name__ == "__main__":
    main()
