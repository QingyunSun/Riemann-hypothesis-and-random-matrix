# Round 7: an arithmetic large-prime sector for zeta's half-gap problem

**Result:** a fixed, discontinuous arithmetic feature beyond every finite polynomial in the old power sums was added and tested. The enlarged resonator's limiting half-gap margin is numerically approximately **-0.01465492379421**. The added feature improves the matched baseline by only **1.429e-8**, so this concrete route does not cross the half-gap threshold. Three quadrature orders agree to about 1.4e-15, and direct evaluation of a frozen rational coefficient vector on actual integers is also negative.

The useful output is the explicit large-prime-sector arithmetic transfer, its mixed insertion formulas, a complete rational test vector, and a bounded negative decision. This is not a new theorem about zeta zeros or an impossibility theorem for the full resonance-correlation method.

## 1. Why this family was selected

The initial suggestion to add S3 or S2^2 was corrected after checking the existing archive. Round 1 had already tested these features, and a 48-term, twelve-group power-sum family had reached approximately -0.01465472564383. Repeating that sweep would not be a new research direction. That old number remains slightly better than the new trial below; differences in the finite spans and ell values must not be concealed.

The genuinely new mark is

    C_L(n) = 1_(there is a prime p|n with p>sqrt(L)).

For n<=L it is a binary mark. It cuts the prime-factor configurations into a large-prime sector and its complement. This sharp fixed threshold is not represented by a finite polynomial in S2,S3,..., although sufficiently large polynomial spaces could approximate it in a suitable mass norm.

The exact identity n=pm with p>sqrt(L), m<p gives a simple arithmetic proof route, rather than an unsupported identification with a limiting Fock operator. No physical prime-gap k39 matrices, heat-flow matrices, or model-only random-matrix distribution were used in this computation.

## 2. The precise 30-dimensional experiment

Fix ell=27/25 and a=729/625. Use the coefficient family

    r_L(n)=d_ell(n) H(v_n,S2(n),S3(n),C_L(n)),

with v_n=log(n)/log(L) and the same distinct-prime power sums as the previous arithmetic transfer proof.

The matched unmarked space has twenty features:

    {1,S2,S3,S2^2} times Legendre_d(2v-1), 0<=d<=4.

The enlarged space adds ten features:

    C times {1,S2} times Legendre_d(4v-3), 0<=d<=4.

The second radial basis is centered on the marked support 1/2<v<=1, avoiding needless conditioning loss from monomials on a short interval. This is only a basis choice: it does not restrict the five radial degrees available in either marked group.

All thirty coefficients are optimized together at the one fixed ell. There is no ell scan, threshold scan, degree scan, or new eigenvalue scan of the full integer operator. The basis and threshold remain fixed as L tends to infinity.

## 3. Arithmetic derivation and its review status

[DERIVATION.md](DERIVATION.md) gives the ordinary proof extension in full. The main new identity is

    E_v[C product S_(k_i)]
      = a v^(1-a) sum_(A subset of labeled factors) m_(I\A)(a)
          integral_(1/2)^v t^(sum_A k_i-1)
             (v-t)^(a-1+sum_(I\A) k_i) dt,

with zero value when v<=1/2. It follows from an exact unique-large-prime integer decomposition and the prime number theorem, together with the already established finite marked-prime moments. The background factor is automatically coprime to the large prime. A fixed threshold's boundary has zero limiting measure.

The insertion changes are C -> C+1_(u>1/2). The off-diagonal M2 terms use H0 Huw and Hu Hw. The same-prime A^*A term survives as M3 with H0^2; it must not be given an inserted mark. The repeated-prime A^2 term vanishes after the usual truncations. The previous weighted Schur estimates are valid for arbitrary signed coefficient vectors and remove small-prime/prime-power operator pieces without assuming a positive H.

The full fixed-family transfer now has a separate [independent internal review](INDEPENDENT_REVIEW.md), including the short background, fixed-threshold boundary and signed-vector truncations. This is not formal verification or external peer review. Numerical agreement is not used as a substitute for the proof review. The source interface remains [Inoue's RH-conditional resonance-correlation theorem](https://arxiv.org/html/2604.05733v1#S3), with its stated product cutoff and error terms.

## 4. Limiting-form numerical results

The quantity displayed is

    margin = (M2+M3)/I - 1/4,

with the normalization fixed in DERIVATION.md. A positive number is required for the intended half-gap attack.

| quadrature order | 20-dimensional baseline | enlarged 30-dimensional family |
|---:|---:|---:|
| 20 | -.0146549380840022 | -.0146549237942085 |
| 28 | -.0146549380840022 | -.0146549237942086 |
| 40 | -.0146549380840038 | -.0146549237942099 |

The order-40 scaled mass-Gram condition numbers are approximately 5.17e7 for the baseline and 1.20e8 for the enlarged family. Every direction survives the stated relative eigenvalue cutoff. The enlarged pencil's residual norm is near 2e-16. These are diagnostics for floating matrices; they do not certify integration or eigenvalue errors.

The quadrature is specifically split at the mark discontinuities. Marked M2 blocks are supported only in three disjoint sectors: a background total greater than 1/2, an inserted u greater than 1/2, or an inserted w greater than 1/2. The background-sector Jacobi weight absorbs the exact (v-1/2)^a endpoint factor. Consequently no integration cell crosses an unresolved step in the mark.

The enlarged value is still about .01465 below zero, vastly larger than the tiny observed gain. It is therefore a useful negative test of this particular sector feature, not evidence of a new record. Nor does it rule out other thresholds, richer occupation functions, or an altogether different resonator.

## 5. Complete frozen rational vector

The order-40 optimizing coefficients were rounded to denominator 100,000,000 and then evaluated again as one fixed vector. In each row below the five integers multiply the radial Legendre degrees 0,1,2,3,4. The first four rows use Legendre_d(2v-1); the last two use Legendre_d(4v-3). Divide every integer by 100,000,000.

| factor | five coefficient numerators |
|---|---|
| 1 | -117846152, 38918251, 1078497, -33600, 411449 |
| S2 | 46899554, -54583075, 43523183, -40218573, 12782032 |
| S3 | 295982141, -383374116, 290083532, -105264757, 17704774 |
| S2^2 | -109987670, 186525942, -226829807, 150959435, -47011938 |
| C | 87192, -72400, 513184, -115799, -690461 |
| C S2 | -361789, 437850, -2512958, 557662, 2084511 |

Its quadrature norm is `1.0000000030188823` and margin is `-0.014654923794209879`. Rational coefficients do not make the integral evaluation an interval certificate. `fixed_rational_vector.json` stores the exact integers, basis labels and denominator so that no coefficient must be reconstructed from a screenshot or rounded prose.

## 6. Direct finite-integer check

The same frozen rational vector was evaluated on actual integers, using the full finite prime-power creation matrix

    A_(p^e m,m)=2 sin(pi log(p^e)/(2log L))/(e sqrt(p^e)).

These are direct Rayleigh evaluations, not optimized eigenvalues. The distinct-prime mark is tested by the exact integer comparison p*p>L. The divisor coefficients include all prime exponents, and the finite operator includes all prime-power multipliers.

| L | ||Ax||^2/||x||^2 | x^T A^2 x/||x||^2 | finite margin |
|---:|---:|---:|---:|
| 10,000 | 2.98343331577942 | 1.10733089333213 | -.04275946416555 |
| 100,000 | 3.02158248945693 | 1.17479313763796 | -.03740912722744 |
| 1,000,000 | 3.04668220745756 | 1.22147565861788 | -.03377259651844 |

The finite evaluations set theta=log L/log T to its limiting value one. They do not assert that a literal finite T already satisfies that equality under the source cutoff. Their slow approach toward a limiting form is not extrapolated to an asymptotic certificate. These data concern resonator coefficients and the arithmetic operator; they are not measurements of actual zeta zeros.

## 7. Independent numerical checks

`validate_sector.py` performs checks that use different formulas or representations:

- The unmarked Gram and numerator blocks are compared with the previous independent monomial implementation after an explicit Legendre-to-monomial change of basis. Maximum absolute discrepancies are about 1.92e-13 and 9.07e-13.
- At a=1, the marked moments are checked against closed formulas `E_v C=log(2v)` and `E_v(C S2)=.75(v^2-.25)-v(v-.5)+.5v^2 log(2v)`.
- For noninteger a=729/625, direct integration in the marked-prime variable t is compared with the implemented scaled Jacobi formula, including repeated labeled factors S2^2 and S2^3. Observed differences are at most about 1e-15.
- The sampled marked moments satisfy 0<=E(C product S_k)<=E(product S_k), and three quadrature orders give an enlarged-margin spread of 1.36e-15.
- The finite integer construction asserts C in {0,1} for every integer evaluated.

The numerical integration routines' reported errors and matrix residuals are not outward enclosures. The report deliberately distinguishes the ordinary arithmetic derivation, the finite matrix model, the numerical tests, and the actual zeta theorem.

## 8. Files and reproduction

All new files are confined to this directory. No Git operation, Claude call, paid API, prime-gap matrix run, or PDF build was used.

```sh
OPENBLAS_NUM_THREADS=1 python3 large_prime_sector.py --order 20
OPENBLAS_NUM_THREADS=1 python3 large_prime_sector.py --order 28
OPENBLAS_NUM_THREADS=1 python3 large_prime_sector.py --order 40
OPENBLAS_NUM_THREADS=1 python3 finite_integer_check.py
OPENBLAS_NUM_THREADS=1 python3 validate_sector.py
```

`large_prime_sector.py` is self-contained apart from NumPy/SciPy. Each quadrature order has JSON containing every coefficient, basis label, Gram spectrum and diagnostic, plus an NPZ with the full numerator and mass matrices. `finite_integer_check.py` records the frozen rational vector and the actual integer values. `validate_sector.py` uses the older `general_prime_features.py` only for its independent unmarked normalization comparison; its SHA is pinned in `validation.json`. The validation script's input location is the existing common BASE layout.

`DERIVATION.md` supplies all additional marked moments and insertion rules. `manifest.json` pins the new code/data and environment. The normal public export is small; no large eigenvector or omitted private service is required.

## 9. Decision and remaining work

This fixed half-threshold sector is now a tested arithmetic family with a concrete transfer argument. Its tiny numerical improvement does not justify further tuning of the same degree-four coefficients. A materially different occupation structure or a new estimate connecting the resonator to arithmetic correlations remains necessary for a serious chance of crossing the half-gap threshold.

No implication for Montgomery-Dyson pair correlation or a refutation of general AH follows from this negative result. Even a future positive small-gap result would need care about multiplicity and the zero atom allowed in some AH formulations. The current run ends with this specific negative decision and preserves all formulas and coefficients for independent review.
