# Round 7: two explicit actual-zeta targets for Dyson–Montgomery

The user's direction is now the main lane: actual Riemann-zeta pair correlations and the Alternative Hypothesis, with random matrices and heat flow used to find precise tests. The prime-gap parameter search is paused. This round has two rigorous reductions to explicit arithmetic inequalities, a new arithmetic resonator with a negative test result, and a forward-flow obstruction. **Neither required new zeta inequality is proved.**

## 1. The most concrete target: two logarithmic-derivative mean squares

For fixed c>0 write

\[
I_T(c)=\int_0^T\left|\frac{\zeta'}{\zeta}
\left(\frac12+\frac c{\log T}+it\right)\right|^2dt,
\quad
W_T=\frac{2[\sinh(2)I_T(1)-\sinh(1)I_T(1/2)]}{T\log^2T}.
\]

The [complete reduction](../dyson/round7/poisson-resolvent/TWO_SCALE_ZETA_TARGET.md) gives, under RH and the precise AH-Pairs formulation in the cited primary paper,

\[
W_T\to W_{\rm AH},\qquad
0.06239<W_{\rm AH}<0.06240.
\]

The sine-kernel prediction is 0.0822714431214773…. Therefore a proof under RH that

\[
\boxed{\liminf_{T\to\infty}W_T\ge1/16}
\]

would already refute AH-Pairs under RH. The easier-to-remember 0.07 target is sufficient but unnecessarily strong as an acceptance threshold. Every lower limit strictly exceeding W_AH would suffice.

The construction fixes a genuine issue with comparing only ACUE to CUE. General AH-Pairs leaves a bounded near-diagonal parameter P_0(T), which need not converge. For a Poisson smoothing width b/(4π), that freedom contributes exactly 2(P_0(T)−1)/sinh(b) to the limiting variance formula. The displayed two-scale combination cancels it. The argument does not assume simple zeros or replace the full AH class by one example.

The proof explicitly controls the noncompact pair-kernel tails, the removed low-zero interval, finite-height endpoints, the Gamma factor, and the holomorphic-square term required to pass from squared real part to squared modulus. The truncations avoid half-lattice boundary atoms. [One independent review](../dyson/round7/dyson-frontier/POISSON_TRANSFER_REVIEW.md) checks these conversions; a [second review](../dyson/round7/poisson-resolvent/INDEPENDENT_REVIEW.md) also reruns the scalar and finite-model checks. The constant enclosure is exact rational arithmetic. These facts establish the reduction, not the missing lower bound for W_T.

## 2. A compact Fourier target and its exact prime covariance

The [primary-source frontier report](../dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md) chooses one nonnegative smooth bump φ with integral one, supported on [6/5,7/5] and symmetric about 13/10. For Montgomery's normalized form factor F_T, the two predictions are

| Statistic | RH + AH-Pairs | Montgomery sine-kernel target |
|---|---:|---:|
| Integral φ(α) F_T(α) dα | 7/10 | 1 |
| Centered prime-covariance remainder E_T | −3/5 | −3/10 |

The AH conclusion follows from half-lattice support and the known low band: the limiting pair Fourier distribution is 2-periodic, so its density on (1,2) must be 2−α. The chosen test avoids the integer atoms and all dependence on the unknown near-diagonal mass. Uniform pair-tail bounds justify this statement without assuming a full limiting process exists.

The report then gives an exact prime kernel for E_T. It retains both von Mangoldt sums and the continuous mean from the pole. An independently checked finite expansion demonstrates why omitting that mean changes the problem. A proof that liminf E_T>−3/5 would suffice to refute AH-Pairs under RH; the stronger limit −3/10 would prove this one smoothed Montgomery prediction. Both remain open here.

These are alternative precise targets. Neither comes from reinterpreting the distribution exponent of the 186 prime-gap proof. The missing quantity is a signed two-prime covariance, at the accuracy displayed in the report.

## 3. A genuinely different arithmetic resonator was tried and did not cross

The first proposed S2/S3 polynomial extension had already been tested in the earlier archive. The agent identified that duplication and instead used the sharp arithmetic mark

\[
C_L(n)=1_{\{P^+(n)>\sqrt L\}},\qquad n\le L.
\]

There is an exact unique-large-prime decomposition n=pm with p>√L and m<p. It gives the new marked moments and insertion rules directly from integers. The [derivation](../dyson/round7/arithmetic-resonator/DERIVATION.md) and [independent audit](../dyson/round7/arithmetic-resonator/INDEPENDENT_REVIEW.md) explain the small-prime truncation, threshold boundary, short background and surviving same-prime term.

A complete 30-dimensional trial was optimized at one fixed ell=27/25. Its limiting half-gap margin is numerically −0.01465492379421, a gain of only about 1.429×10^−8 over its matched 20-dimensional baseline. It remains slightly worse than the older 48-feature best trial, which the report states explicitly. Three split quadrature orders agree, and a frozen rational vector has negative directly evaluated integer-operator margins through L=10^6. These are numerical checks, not interval enclosures or actual zero samples. This particular feature does not justify another coefficient sweep.

The [full report and data](../dyson/round7/arithmetic-resonator/REPORT.md) retain the fixed coefficients, full matrices and failed trial. The failure does not prove that every discontinuous prime-factor feature or the full resonance method is incapable of crossing the threshold.

## 4. Forward heat flow: a useful comparison, with two missing estimates

The [forward-flow report](../dyson/round7/true-zeta-flow/FORWARD_FLOW_OBSTRUCTION.md) proves a contraction estimate for ordered real repulsive systems with a decreasing common external field. Its constant does not deteriorate as an internal gap becomes small. However, a remote-field approximation valid at the central particles need not be valid at the retained block's boundary; a specific boundary-propagation integral remains to be controlled for actual H_t.

Even perfect deterministic localization is insufficient for GUE. The exact family

\[
P_t(z)=z^{2M}-2\cos(\pi/4)e^{-M^2t}z^M+1
\]

starts on the ACUE half-grid up to rotation, has bounded counting discrepancy, and keeps all normalized gaps at least 1/2 throughout forward flow. It approaches the unit clock. This is a counterexample to insufficient dynamical hypotheses, not a model satisfying the full arithmetic explicit formula.

The missing stochastic term is quantitatively visible: for a protected trace frequency m=N/2, its expected microscopic generator contribution at CUE is exactly π². Moreover, the entire protected trace filtration remains matched between ACUE and CUE under full DBM. Thus unchanged low moments cannot justify removing stochastic smoothing. The report states the exact Duhamel and boundary estimates a genuine zeta comparison would need.

## 5. What the recent 0.6725 result contributes

The source audit identifies 0.6725007… as an unconditional lower proportion of zeros that are both simple and on the critical line, with the separate distinct-zero consequence stated in the primary papers. It does not evaluate the out-of-band covariance used here. The checked new proof still uses its stated support-one input. The report records exact source URLs, dates and hashes; it does not infer that a percentage-of-zeros theorem supplies a Montgomery plateau.

## 6. Verification and the next decision

The focused folders preserve source provenance, ordinary proofs, independent reviews, exact scalar certificates, complete numerical witnesses and execution logs. Third-party primary PDFs stay in the local reference archive; their URLs and hashes are public. The independent integration receipt is under `research/logs/round7-integration/`.

The next mathematical step is to prove a nontrivial lower bound for the signed mean square W_T or the centered prime covariance E_T using additional arithmetic structure. The two-scale spectral weight is sinh(2)exp(-2|u|)-sinh(1)exp(-|u|); it changes sign at |u|=log(2 cosh 1). Dropping the unknown high-frequency contribution therefore gives no lower bound. More decisively, the actual stationary ACUE comparison process matches the known low band and satisfies point-process positivity while attaining W_AH<1/16. Those inputs alone cannot prove the desired inequality. A bounded continuation examines exactly where additional arithmetic information enters a centered-psi representation.

Numerical model separation and the present reductions do not estimate either required arithmetic quantity. A complete GUE theorem, a new prime-gap sweep, and proof-assistant formalization of an unclosed argument are postponed. The long research goal remains active.
