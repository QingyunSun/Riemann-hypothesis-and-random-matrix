# Quantitative ACUE counterexamples and a sharper zeta target

6 November 2026. Incremental checkpoint following [PR #6](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/pull/6). The full 881-page historical handoff remains available there; this packet adds proofs and corrections rather than silently rewriting old records.

## What changed mathematically

**A finite existence result is now quantitative.** At N=11 and scalar-heat time s=log(85/84), an explicitly defined, strictly positive alternative to ACUE preserves the full joint distribution of pair-displacement counts and sorted adjacent gaps, together with all protected trace expectations. Its survival probability increases by more than 0.0175:

| Law | Probability of no collision by s |
|---|---:|
| ACUE | 0.198104310321809... |
| Constructed positive law | between 0.2156294303856491 and 0.2156294309055878 |

The exact law is a cyclotomic linear solve specified by a small dyadic seed. A floating LP locates the seed, but neither a floating residual nor an assumed numerical rank is used as proof. Independent 224-bit replay, separate Fourier-Gram weight checks and the previous independent survivor-classification algorithm support the certificate. See [finite theorem](finite/REPORT.md) and [independent audit](finite/INDEPENDENT_REVIEW.md).

**The periodic-lift route has an exact probability limitation.** A seed atom of mass p lifts to an atom of mass p^r. The mass of the full two-fold lifted support is exactly
\[
M_{n,2}=\frac{(2n)!}{n!(4n)^n}\sim\sqrt2 e^{-n}.
\]
At n=11 it is only 0.00002353051503. This identity uses the classical, already-proved Dyson constant-term theorem. Any static-summary-preserving law that agrees with ACUE outside the lifted support differs in every event probability by at most this support mass. Merely repeating the finite pattern cannot create a nonvanishing asymptotic distinction. See [proof and checks](PERIODIC_LIFT_MASS.md).

**A probabilistic issue in the zeta transfer can be closed under RH.** For every fixed unfolded window and fixed k, existing restricted Rudnick-Sarnak correlations imply a uniform kth-moment bound for its zero count. Hence cubic window scores are uniformly integrable. Full pair-displacement concentration on the half-grid then forces the cubic alias mean to vanish, by an explicit inequality. This corrects the earlier audit's suggestion that an additional unproved occupancy estimate was needed in the fixed-window RH setting. It does not apply to merely matching pair tests in the protected Fourier band.

**The conditional arithmetic packet theorem is now complete.** A raw, Fourier-localized triple variant vanishes on every translated half-grid, has exact sine-process expectation +1/5, and avoids separate high-frequency pair corrections. Its zeta average, under RH, reduces to a signed near-product correlation of
\[
(\Lambda(m)-1)\Lambda(n)(\Lambda(r)-1)
\]
with m near T^(6/5), n near T^(1/5), r near T^(7/5), and an oscillatory kernel around mn=r. A subsequent calculation evaluates the signed singular-series main term using the existing Fazzari-Gerspach Lemma 2.7. Under RH, the exact reduction is
\[
M_T=\frac15-\frac{\operatorname{Re}\mathcal R_T}{c_\psi}+o(1).
\]
Here \(\mathcal R_T\) is the explicitly defined endpoint-aware signed prime-pair discrepancy. A consistent localized Hardy-Littlewood estimate yields \(M_T\to1/5\); that estimate remains unproved. More weakly, any upper bound for the signed error strictly below \(c_\psi/5\) excludes the stated half-grid pair-concentration hypothesis under RH. See the [complete calculation](arithmetic/MAIN_TERM_THEOREM.md), [independent review](arithmetic/MAIN_TERM_INDEPENDENT_REVIEW.md), and [source-input audit](arithmetic/SOURCE_INPUT_AUDIT.md).

**Why a size estimate alone can fail.** For each fixed real \(c\), there are positive, independently assigned surrogate counting measures with integer weights on permitted multiples of \(n\) and signed residual tending to \(c\beta c_\psi\). Their cumulative discrepancies obey \(O_\varepsilon((T/n)T^\varepsilon)\) on the packet, and the occupied sites can avoid small prime factors in both linear forms up to \(K\log T\) for every fixed \(K>0\). Taking \(c=1\) cancels the whole main term. This is a counterexample to inferring a saving from those size and support conditions alone. It does not represent the actual primes by a common von Mangoldt sequence. The central comparison \(T/n=X^{4/7}\) is not uniform over the edges of a fixed-width packet. See the [construction and its limitations](arithmetic/SURROGATE_SHARPNESS.md).

## What the bounded-probe work contributes

[The bounded-probe note](bounded/REPORT.md) gives robust normalized and clipped variants, a rigorous sine-process sign on short windows, and a precise limitation: a finite-degree continuous correlation polynomial uniformly bounded on every finite configuration in a compact interval must be constant.

This explains why clipping cannot generally retain a fixed three-trace arithmetic formula. For actual zeta under RH and fixed window width, clipping is optional because count moments already control uniform integrability. These are structural statements, not a proof of the zeta/GUE conjecture.

## DBM and primary-source update

[The explicit clock example](source_refresh/DBM_BACKWARD_OBSTRUCTION.md) satisfies the Landon-Sosoe-Yau mesoscopic regularity hypotheses and optimal initial rigidity, yet Gaussian regularization changes a compact microscopic two-point statistic by at least \(1-8/\pi^2\) in the limit. This gives a concrete obstruction to inferring the original statistics from the regularized ones. The missing comparison is written as a Duhamel integral; this is an application of the known universality theorem, not a new universality claim.

[The live source audit](source_refresh/SOURCE_REFRESH.md) incorporates a distinct October manuscript claiming a 0.67353820 simple-critical-line proportion, with a new local-certificate architecture and explicit compiled-search trust dependencies. Its full computation was not rerun. Fable/PR 11 and the checked 186/182 source heads were unchanged at the audit snapshot. Better simplicity alone does not establish non-lattice spacing or the missing signed correlation.

## Files and reproduction

- finite/candidate.json: exact dyadic free coordinates and row/column selections; about 89 KB.
- finite/certify.py: reconstructs the selected algebraic system and verifies an interval certificate.
- finite/baseline.py: sums all 16,159 orbit masses and survivor probabilities.
- finite/check_weights.py: independent Fourier-projection determinant check of all 1,489 paired orbit weights.
- check_lift.py: direct lifted-atom identities, the closed purity formula and pair-fibre membership.
- bounded/check.py: supplementary deterministic inequality and combinatorial checks.
- arithmetic/REPORT.md: initial derivations, precise support ranges and primary references.
- arithmetic/MAIN_TERM_THEOREM.md: completed singular-series calculation, conditional theorem and exact cancellation threshold.
- arithmetic/MAIN_TERM_INDEPENDENT_REVIEW.md: independent proof and two multiplicity-safe count-moment arguments.
- arithmetic/SOURCE_INPUT_AUDIT.md: primary-source scope and an independent prime-modulus reduction.
- arithmetic/check_normalizations.py: numerical diagnostics only, not proof of the missing arithmetic premise.
- HANDOFF_ADDENDUM.md and HANDOFF_ADDENDUM.pdf: integrated reading copies.

From this directory, with Python 3.12, NumPy 2.5.4, SciPy 1.18.1 and python-flint 0.8.0:
```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python finite/certify.py
python finite/baseline.py
python finite/check_weights.py
python check_lift.py
python bounded/check.py
python arithmetic/check_normalizations.py
```
These versions were used for the root replay; they are not claimed to be the only compatible versions. The interval verifier may produce slightly different inverse-residual enclosures on another BLAS build, but checks the same explicit lower bound and defines the same exact law.

## Review boundaries and next work

The finite theorem has internal proofs and machine-checkable interval calculations. It is not yet externally reviewed or formalized in Lean. The zeta moment bound is a corollary of an existing theorem with its hypotheses checked. The signed prime discrepancy estimate remains open in this programme. The main-term calculation is now closed, so the packet theorem is conditional on that precise remaining input. No unconditional RH, Montgomery-Dyson, AH-refutation or improved prime-gap theorem is asserted.

The next analytic step is to bound the real signed discrepancy below its exact cancellation threshold. Under RH this functional is already bounded; the stated pair-AH would force it to tend to the specific positive value \(c_\psi/5\). The new calculation therefore identifies the precise cancellation that must be excluded. For a large-N model theorem, a successful perturbation must act outside the exponentially small repeated-pattern support.

[The direct discrepancy calculation](arithmetic/CONDITIONAL_NEXT.md) shows that a consistent localized square-root prime-pair error would be sufficient for the error stage on the central domain \(\alpha+3\beta<2\). The formerly unevaluated main term is now supplied by the complete calculation linked above; the earlier error-stage note is retained as a historical step.

[An endpoint audit](arithmetic/ENDPOINT_CORRECTION.md) identifies a defect in the literal two-sign uniform hypothesis printed in Fazzari-Gerspach v1. The conditional calculation here uses a separately stated, endpoint-aware local assumption. This is a source-formulation correction, not a refutation of classical Hardy-Littlewood.

No infrastructure changes, runtime optimization or performance claim are part of this packet. Postpone a new broad numerical search, a repeated 881-page rebuild, or a claimed famous-conjecture solution without the missing arithmetic estimate.

See [REPRODUCTION.md](REPRODUCTION.md) for exact commands, validation boundaries, PDF rebuilding, and the discovery-data archive.
