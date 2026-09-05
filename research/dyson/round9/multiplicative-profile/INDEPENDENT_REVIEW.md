# Independent review: the fixed two-large-prime interaction

Date: 2026-09-05. Reviewer: the root research lane, independently of the author. **Accepted as an ordinary fixed-family arithmetic extension and a negative floating experiment.** No interval certification, external novelty claim, or new zeta theorem is accepted or implied.

Reviewed author files:

- `DERIVATION.md`: SHA256 `0b717ee45e31abcd399ba48d58069b47bab6b1d9ea5086afed42ca9df6438438`.
- `two_large_prime_sector.py`: SHA256 `ed6fa274593a04d8a168a8597c76a994ad0595edb337995a7904a93b6a845de0`.
- `check_two_prime_trial.py`: SHA256 `61c4c5c92b5d502670fbf469fe61d422f69778369125ff569a28418aa3dab9ff`.

The root read the complete derivation, report, and two scripts. The review uses the previously independently reviewed Round 7 fixed-moment and weighted Schur estimates as inputs; it does not supply a new proof of those inherited results or a general Fock-space limit.

## Arithmetic checks independent of the optimizer

1. For two distinct prime divisors exceeding L^(1/3), their product leaves a cofactor less than either prime. The unordered double-mark decomposition, the coefficient a², and the factor 1/2 in the ordered limiting integral are correct. Three such distinct primes cannot divide n<=L.
2. A *single* designated prime at this threshold need not be coprime to the cofactor. The author handles this explicitly. For ell>=1, the ratio d_ell(p^(e+1))/d_ell(p^e)=(ell+e)/(e+1) is at most ell. Hence the background repeat estimate has an extra 1/p, and summing designated primes supplies sum p^(-2)=O(L^(-1/3)). Bounded fixed marks preserve this estimate. No automatic-coprimality claim is imported from the older threshold 1/2.
3. C is three-valued, while D is binary. The identities C²=C+2D, CD=2D, D²=D and the three-state Newton interpolation are correct. The two insertion rules include the mixed term from one old and one new large prime, as well as the event with two newly inserted large primes. Infeasible states disappear through total mass, not an artificial truncation of C.
4. The measure used before the Laplace limit is on all n>=1. Restriction to total mass at most one follows the weak limit. Fixed threshold planes have zero limiting measure, and the locally integrable residual density controls the small-cofactor strip. This avoids a false pointwise uniform asymptotic at a cofactor cutoff near one.
5. The bounded, fixed coefficient family permits the inherited signed operator truncations. The distinct-prime terms produce H0 Huw and Hu Hw. The A*A same-prime term survives with uninserted H0²; the repeated-prime term in A² has the extra reciprocal-prime factor and vanishes. The displayed M2/M3 constants agree with the actual creation matrix normalization.

## Implementation and interpretation

The two-mark substitution has Jacobian delta²(1-z), residual density (delta z)^(a-1), and denominator tw, giving exactly delta^(a+1) z^(a-1)(1-z)/(tw). The one-mark endpoint exponent is a. The code divides the total-mass and insertion domains at each fixed threshold and uses the corresponding Jacobi factors. Its coefficient interpolation keeps all three background count states.

The rational frozen vector is nonzero without appealing to a numerical Gram matrix: its unmarked value at the origin is 155237743/100000000. Continuity then gives a positive limiting norm on a sufficiently small unmarked interval.

The reported margin is approximately -0.0146549114371551. The observed 2.66e-8 improvement over the matched baseline is not certified, especially with a diagonally scaled Gram condition near 5.36e7. The full negative deficit is about 0.01465. The new span does not contain the earlier best 48-feature span, and its value is worse than that historical result. Thus this fixed trial supplies no small-gap or AH consequence. It also does not rule out a different interaction, a larger coefficient space, or the resonance method.

Finite exact checks validate the stated identities and cutoff conventions; quadrature agreement and the finite-integer experiment validate specific implementations. They do not prove the asymptotic transfer. Independent integration replay and full-array comparisons are recorded separately when this folder is published.

The author files retain their historical “review pending” wording. This separately hashed review records their later acceptance without silently rewriting the original research record.
