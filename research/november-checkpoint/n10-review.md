# Independent audit of the ten-particle extension

## Even-particle signs and the rank bound

The complement action retains sign +1 at even N. In the unitary-DFT proof from the eleven-particle audit, the Jacobi minor sign is (-1)^(sum E − sum B), equal to +1 for a balanced exponent set modulo the even integer 2N. After conjugation, multiplying every row in numerator and denominator by the same root of unity turns the negative exponents into 2N−1−E^c and 2N−1−B^c. Both lists reverse, and their reversal signs cancel. This proof works for both parities.

Reflection of the site set acts on E through N−1−E modulo 2N with sign (-1)^(h(N−h)). At N=10 this sign is (-1)^h. Complement preserves the number h of upper-half exponent indices. Thus RC carries the **same** sign as R at its starting E, and the projector (I+R)(I−C)/4 still applies.

The independent residue-lift enumeration traversed all 184756 ten-element exponent subsets and returned signed traces (1957,87,19,129), hence upper rank 474. It uses possible unwrapped signed highest weights rather than the author's bipartition implementation. In addition, 375 literal determinant-ratio comparisons of R,C and RC passed modulo 101 with primitive twentieth root 32. They include negative reflection factors. The exact sign argument and exhaustive count support the characteristic-zero upper bound. The determinant samples are a diagnostic only.

## Size minimality has a precise scope

I independently enumerated dihedral orbit classes using cyclic gap words rather than binary rotations, grouped them by all displacement counts and the sorted consecutive gaps, then evaluated protected trace polynomials directly in splitting fields. The results are

| N | Dihedral orbits | Static fibres | Full static-law freedom | Protected rank |
|--:|--:|--:|--:|--:|
| 1 | 1 | 1 | 0 | 0 |
| 2 | 2 | 2 | 0 | 0 |
| 3 | 3 | 3 | 0 | 0 |
| 4 | 8 | 8 | 0 | 0 |
| 5 | 16 | 16 | 0 | 0 |
| 6 | 50 | 47 | 3 | 3 |
| 7 | 133 | 123 | 10 | 10 |
| 8 | 440 | 396 | 44 | 44 |
| 9 | 1387 | 1179 | 208 | 208 |

The finite-field primes used for N=6,7,8,9 were 13,29,17,19, different from the author tests. A full-column minor proves injectivity in characteristic zero. These are **all** orbit-mass changes within the static-summary fibres, so this obstruction extends beyond complement-only tilts. An arbitrary law on N distinct sites of a rotated 2N-grid may first be averaged under rotations and reflection. This keeps its survival distribution and static-summary law, and keeps the protected moment identities when compared with ACUE. The resulting orbit law is subject to the injectivity above. Thus the minimality claim concerns all such grid-supported laws, including initially nonsymmetric laws and random global rotations.

The calculation does not address arbitrary continuous configurations, changed lattice spacing, repeated roots, or a different collection of preserved statistics. Say “smallest N on the 2N-site model with these stated constraints.”

## Complement graph at N=10

An independent gap-word enumeration gave 2234 complement edges and 462 self-loops. Counting connected components of the summary graph gives circulation dimension 496. Its cycle space preserves the entire joint static-summary distribution, even when an individual edge connects different summaries. Because each edge connects distinct complementary dihedral orbits, orbit-mass changes on distinct edges have disjoint support, so mapping edge flows to signed orbit laws is injective.

For the numerical event part, the source reports protected rank 473 and rank 475 after appending the two separately certified survival rows. The upper bound 474 means at least one of the two events lies outside the characteristic-zero protected span. It does not choose which time. A modular rank deficit by itself cannot identify the exact characteristic-zero protected rank as 473. The proof need only the matching algebraic upper bound and the augmented lower bound. My independent contribution here verifies the signs, exhaustive upper bound, full smaller-size rigidity, and cycle dimension. The author or a separate flow reviewer must certify the two survival rows and the modular 475 computation.

Replays are n10_symmetry_replay.py, n10_small_minimality.py and n10_cycles_independent.py, with their JSON outputs.

## Additional survival replay

The event computation was then rerun at **176-bit** Arb precision, and protected/augmented matrix ranks recomputed over three splitting primes. This rerun uses the author's event and feature functions, independently rebuilding the arrays and choosing additional fields.

| Prime | Primitive twentieth root | Protected rank | With first event only | With second event only | With both events |
|--:|--:|--:|--:|--:|--:|
| 101 | 32 | 473 | 474 | 474 | 475 |
| 241 | 6 | 473 | 474 | 474 | 475 |
| 401 | 22 | 473 | 474 | 474 | 475 |

All pivot classifications were decisive. Thus the numerical premises for the two-time assertion were reproduced beyond the 144-bit source run. This does not choose one event or turn the modular rank 473 into a characteristic-zero upper bound. See n10_new_primes.py and n10_new_primes.json.
