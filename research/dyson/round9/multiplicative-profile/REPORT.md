# Round 9: duplicate profile avoided, two-prime interaction tested

Date: 2026-09-05. This directory keeps its initially assigned `multiplicative-profile` name so the task history and dependency paths remain traceable. The actual new experiment is a nonmultiplicative interaction between two distinct large prime divisors.

**Outcome:** the fixed 30-dimensional interaction trial has floating half-gap margin **−0.0146549114371551**. It does not cross zero and remains worse than the old 48-feature best value, approximately −0.0146547256. The written arithmetic extension is in [DERIVATION.md](DERIVATION.md); separate independent review is pending. There is no new zeta theorem, no certified optimizer, and no global obstruction theorem.

## 1. The archive check changed the task before computation

The initial suggestion was a multiplicative prime-size profile such as a product of exp(sum c_k u_p^k), summing all mark orders. The public Round 2 report `research/reports/resummed_prime_profiles.md` and scripts `research/prime-profiles/euler_profile_precise.py/.json` already implement precisely that mechanism. Their convolution-density recurrence resums all powers, rather than merely taking the old finite S2/S3 span. Recorded cases include one, two, three and five exponent coefficients, through u^6. The best validated local continuation was approximately −0.0146638632200778, with radial degree 9 and quadrature order 40; it was a continuum calculation with 110/140-term density comparison, not a completed all-orders arithmetic remainder theorem.

The literal product of (1+eta u_p^2) was not located as an executed trial. It would be inaccurate to claim that every such parameter was already tested. But its multiplicative one-prime mechanism is not new relative to the existing resummed Euler-profile approach. Under the task's stop-on-duplication instruction, no new exponential-profile or eta scan was run.

The old Fock report contains broad bin-occupation states, but explicitly keeps its general operator-transfer issue separate. That is not a prior fixed-integer test of the new D mark below. Searches of the existing research reports and Round 7 arithmetic derivation found no earlier implementation of this fixed two-large-prime interaction. This is an archive-coverage statement, not a mathematical novelty claim.

## 2. What was actually added

For n<=L set

    D_L(n)=1 if at least two DISTINCT prime divisors p of n satisfy p^3>L,
           0 otherwise.

There are at most two. When D=1, the unique unordered pair p<q gives n=pqm with m<L^(1/3)<min(p,q), so the new double-mark starting identity is exact and automatically coprime. The singly marked background count C also occurs in mixed insertions; its one-third-threshold formula needs the explicit repeated-prime error in the derivation and is not mislabeled exact.

The new span has ell=27/25, radial degree four, the same 20 unmarked features as the matched Round 7 baseline, and ten D-marked features: D times 1 or S2, with radial basis P_j(6v-5). The mark is an interaction: adding the first large prime leaves it zero, while adding a second switches it on. A three-state interpolation in the background count C supplies the mixed insertion forms. All thresholds and coefficient counts stay fixed in the arithmetic limit.

The matrices are newly integrated for this mark. Only generic labeled-partition moments, polynomial insertion expansion, Gauss-Jacobi nodes and the generalized-eigenvalue helper are imported from the pinned Round 7 script. The old marked matrices and the prime-gap 77-dimensional problem are not reused.

## 3. The bounded numerical decision

| Fixed trial | Order 20 margin | Order 32 margin |
|---|---:|---:|
| Matched 20 unmarked features | −0.0146549380840023 | −0.0146549380840028 |
| New 30-feature D interaction | −0.0146549114371546 | −0.0146549114371551 |

At order 32 the observed gain over its matched baseline is about 2.66468477e−8. The new value is still roughly 1.858e−7 below the old 48-feature best, and about 0.01465 short of the required zero margin. Those comparisons are numerical only; the larger historical span is not nested in this new 30-dimensional span.

The diagonally scaled mass Gram condition is approximately 5.35731565e7 for the enlarged span. All 30 directions survive the fixed 1e−11 relative eigenvalue cutoff. The final floating pencil residual norm is approximately 2.52e−16 and the mass norm is 1 to rounding. A tiny residual verifies a floating solve, not the correctness of its quadrature or an enclosure of the top eigenvalue. In particular the 2.66e−8 gain is not advertised as certified. The negative main deficit is much larger than that gain.

The baseline M/G blocks independently agree with the existing Round 7 order-40 unmarked blocks to maximum absolute differences 8.33e−16 and 2.22e−15. The two new quadrature orders agree in the enlarged margin to about 5.6e−16. No further degree increase, threshold change, parameter sweep or optimization of ell was performed.

## 4. Fixed vector and independent checks

[fixed_rational_vector.json](fixed_rational_vector.json) contains all 30 integer coefficients with denominator 100000000, the exact ell and threshold, the complete ordered feature list and radial conventions. Its continuum quadrature margin is −0.0146549114371553. Its polynomial value at v=S=D=0 is exactly 155237743/100000000, so it is nonzero; positivity of the limiting mass follows already on a sufficiently small unmarked total-mass interval. The nonzero norm is not based solely on the numerical Gram matrix.

[check_two_prime_trial.py](check_two_prime_trial.py) records the following in [validation.json](validation.json):

- At integer cutoff 120, an exact Fraction identity matches all 12 unique unordered two-large-prime decompositions and their coefficient factor a^2.
- The two insertion identities and divisor factors pass on 132 ordered coprime insertion triples.
- The Newton interpolation in {1,C,D} passes 108 exact state checks, keeping C=2 distinct from C=1.
- At a=(27/25)^2 and total mass v=.91, two independent nested adaptive integrations of the raw E[D] and E[D S2] formulas agree with the substituted Jacobi expressions within 1.11e−16 and 5.56e−17. These are floating checks of different integration formulas, not interval certificates.
- A single actual-integer calculation at L=100000 uses the frozen vector and every prime-power entry of A_L. It has 11109 integers with D=1, 343614 matrix nonzeros, norm about 20.46127, A*A/norm about 3.02145870, A^2/norm about 1.17491031 and margin **−0.0374094621535042**. It is a finite arithmetic calculation at theta=1, not a zeta-zero sample or proof of an asymptotic rate.

The exact checks deliberately use rational formal prime labels for polynomial identities. They do not claim that log(p)/log(L) is rational or replace the actual logarithms used by the final finite-integer evaluation.

## 5. Files, reproduction and limitations

The two computation files are [two_large_prime_sector.py](two_large_prime_sector.py) and [check_two_prime_trial.py](check_two_prime_trial.py). The former produces complete `two_large_prime_d4_q20.json/.npz` and `two_large_prime_d4_q32.json/.npz`; each NPZ retains the full symmetric numerator M and mass G. The latter freezes the rational vector and writes the validation record. A small [manifest.json](manifest.json) pins the new outputs and the relevant archived source files.

From this directory, with Python, NumPy and SciPy:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 two_large_prime_sector.py --order 20
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 two_large_prime_sector.py --order 32
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 check_two_prime_trial.py
```

The environment variable `ASTRA_LARGE_PRIME_SOURCE` can point to the pinned Round 7 `large_prime_sector.py`. Its expected SHA256 is checked before import. The current default is the local public-repository path; a publication copy may replace that default with a portable repository-relative path and must record that change explicitly. The old imported file is not edited. The only output fields expected to vary on replay are recorded run times, runtime/version metadata if added, and environment-dependent floating differences; an identical environment can demand exact arrays as a stronger diagnostic. No speed claim is made from these small local run times.

The arithmetic-transfer argument uses existing fixed-moment asymptotics and uniform operator truncations, plus the explicit new count identities. It does not assume a global Fock limit or an unsupported all-orders coefficient limit. The optimization and the finite-integer sine calculations remain ordinary floating arithmetic. Review of the new proof and code is separate from numerical agreement, and no external novelty or formal verification claim is made.

This round is closed at a useful negative decision. It rules out neither other nonmultiplicative arithmetic features nor the full resonance method. Repeating the old exponential profile, adding more digits to this small gain, or treating it as evidence toward a historic conjecture is postponed. Further work needs a quantitatively different arithmetic direction or a new estimate for the actual out-of-band covariance.
