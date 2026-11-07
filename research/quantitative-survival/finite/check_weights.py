"""Check orbit weights by Fourier Gram determinants, independent of sine products."""
import json
from pathlib import Path
from flint import acb, arb, acb_mat, ctx
from base import summary_fibres, matching_complements

def main():
    ctx.prec = 192
    n, size = 11, 22
    roots = [acb(arb(k)/n).exp_pi_i() for k in range(size)]
    kernel = [sum((roots[(j*d) % size] for j in range(n)), acb(0))/size
              for d in range(size)]
    pairs = matching_complements(n, summary_fibres(n))
    total = arb(0)
    for a, b in pairs:
        def gram(s):
            value = acb_mat([[kernel[(x-y) % size] for y in s] for x in s]).det()
            assert value.imag.contains(0) and value.real > 0
            return value.real
        pa, pb = gram(a), gram(b)
        assert (pa-pb).contains(0)
        product = arb(1)/size**n
        for i, x in enumerate(a):
            for y in a[i+1:]:
                product *= 4*(arb(y-x)/size*arb.pi()).sin()**2
        assert (product-pa).contains(0)
        def orbit(s):
            return len({tuple(sorted((sign*x+j) % size for x in s))
                        for sign in (-1, 1) for j in range(size)})
        oa, ob = orbit(a), orbit(b)
        assert oa == ob
        total += oa*(pa+pb)
    out = {"precision_bits": ctx.prec, "matched_pairs_checked": len(pairs),
           "method": "independent Fourier-projection Gram determinants versus sine-product weights",
           "total_paired_mass": str(total),
           "positive_atom_and_equal_complement_weights": True}
    Path(__file__).with_name("ROOT_WEIGHT_REVIEW.json").write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
