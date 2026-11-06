# Independent check of the protected rank at eleven particles

The rank upper bound **964** survives both the characteristic-zero symmetry audit and an independent enumeration. This supplies the upper bound needed to interpret a modular increase after appending the survival test. A modular deficit in the protected matrix alone would give only a lower bound on its characteristic-zero rank.

## Alternants and the two symmetries

Put m=2n, B={0,…,n−1}, and let F be the unitary discrete Fourier transform matrix with entries proportional to ω^(ij), where ω has order m. For any n-set S of sites and n-set E of exponents, put φ_E(S)=det F[S,E]/det F[S,B], using increasing row and column orders. The denominator is a nonzero Vandermonde. The functions φ_E are linearly independent on all n-sets: the matrix of their numerators is an exterior power of F, and division rescales each row by a nonzero scalar.

A balanced product of trace monomials of positive and negative weight w≤n is a linear combination of U(n) characters with signed highest weights λ of total zero whose positive part has sum at most w. This follows by regarding each monomial as a class function in the w-fold tensor powers of the defining representation and its dual: power sums are integer combinations of polynomial characters, each weight of their product is a sum of w positive unit vectors and w negative unit vectors, and each constituent's highest weight is among those weights. Thus the finite residue sets of the Weyl numerator (with coincident exponents giving a zero determinant) bound the span from above. The upper bound below only needs containment. Since the protected span is closed under the real involutions that matter here, all its reflection-averaged complement contrasts land within the projected space described below. Alternatively project the larger Weyl span directly; no equality of the spans is required. The per-sign weight limit makes unbalanced moments vanish for rotation-invariant measures by rotation through one lattice step.

**Complement.** Jacobi’s complementary-minor identity on F and unitarity give φ_E(Sᶜ)=(-1)^(ΣE−ΣB) conjugate(det F[S,Eᶜ]/det F[S,Bᶜ]). The sign is +1 since our balanced exponents have ΣE≡ΣB modulo the even integer m. The common row factor ω^(−s) may be inserted in both determinants to turn conjugated columns into m−1−j. Both column lists reverse, so their sorting signs cancel. Bᶜ maps to B. The resulting transformation is C(E)={m−1−j : j∉E} with coefficient +1.

**Reflection.** Negate all sites in the numerator and denominator. The common row factors ω^((n−1)s) transform their exponents by j↦n−1−j mod m, giving R(E). With h elements in [n,m), the sorting signs of the two descending sublists relative to the fully reversed B list give (-1)^(h(n−h)). C preserves h. At n=11 this sign is always +1. Reflection on arguments is a complex-linear pullback; it also conjugates each individual alternant value. Hence its even projection is appropriately applied to the dihedral-orbit averages.

## Independent exact enumeration

The companion script enumerates all 705432 eleven-element residue sets. It checks each by lifting raw shifted exponents, independently of the bipartition-based author calculation. In increasing convention the lift has entries j+λ_j for 0≤j<n. Each lies in [−n,2n−1]. Only residues in the upper half can wrap negatively. Their required number is fixed by (ΣE−ΣB)/(2n), so testing the possible subsets finds precisely the sets with a zero-sum, nondecreasing signed highest weight of positive mass ≤n. Closure under R,C and RC is checked explicitly. The resulting traces are

| identity | R | C | RC | reflection even, complement odd |
|--:|--:|--:|--:|--:|
| 3956 | 106 | 22 | 184 | (3956+106−22−184)/4 = 964 |

The two commuting involutions give the last expression by the projector (I+R)(I−C)/4. Averaging a test on the dihedral orbit removes its reflection-odd part. Subtracting its averages on complementary orbits removes its complement-even part. Restricting the set of complement pairs to a common gap histogram cannot raise the rank. Complexification preserves rank for the resulting real-valued rows.

As a separate diagnostic, literal finite-field determinant ratios using a primitive 22nd root 11 modulo 89 passed 375 deterministic R/C/RC identities on 125 sample pairs of site/exponent sets. These sample checks corroborate the argument; they do not establish the character identity on their own. Run `python n11_symmetry_replay.py` with python-flint to regenerate the JSON receipt.

## Scope

Together with a verified augmented modular rank at least 965 modulo a splitting prime, this upper bound implies characteristic-zero separation of the survival statistic from the protected test rows on the selected pair transfers. The rank result concerns finite-model laws. Its conversion to a statement about genuine zeta zeros requires a separate arithmetic argument.
