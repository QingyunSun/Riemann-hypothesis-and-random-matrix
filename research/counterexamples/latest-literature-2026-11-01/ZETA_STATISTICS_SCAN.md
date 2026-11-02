# Zeta statistics: bounded source audit and comparison with our counterexamples

Audit date: 2026-11-01 America/Los_Angeles / 2026-11-02 UTC.

Scope: primary-paper statements and the exact implications for our programme. This is not a full independent verification of the cited analytic arguments, interval computations, or Lean builds. No new record is asserted by this project. Historical files were read, not revised. The companion pair-matched notes' dates were corrected to the present audit date.

## 1. Conclusions for the next research decision

The Lamzouri constant is exactly the old Montgomery–Taylor constant already present in our historical calculations. Reoptimizing the same scalar energy and retaining the same decoding inequality cannot improve it. This does **not** establish a ceiling for all arguments using restricted pair data. Our historical synthesis explicitly retracted that broader claim.

The most relevant later structure found here is a mixed-multiplicity, clipped Gram-matrix correction in Knausgård's October revision. It attempts to improve what one extracts from a second-moment estimate by retaining unavoidable local overlap. That is a different mathematical operation from lowering the optimal Montgomery–Taylor energy. Its headline remains a preprint claim with stated analytic and computational dependencies; this audit has not replayed those dependencies.

A useful additional diagnostic is proved in §5: on distinct points of a shifted half-integer lattice, the clipping used in that paper is inactive for its stated window. The correction then reduces to an ordinary pair-energy statistic. This prevents a premature claim that the correction itself separates all pair-matched AH models.

## 2. Lamzouri: precise source capsule

Source: [arXiv:2609.02882v2](https://arxiv.org/html/2609.02882v2), submitted September 2, revised September 8, 2026; Proposition 2.1, Lemmas 3.1–3.2, Remark 3.4, Theorem 1.1.

The unconditional proportions are

\[
C_0=2-C_{\rm MT},\quad C_1=(1+C_0)/2,\quad
C_2=(1+2\sqrt2+2C_0)/(3+2\sqrt2):
\]

simple-and-critical ≥ C0; distinct ≥ C1; simple-or-critical ≥ C2; average(simple, critical) ≥ C1.

For a nonempty finite conjugation-invariant multiset Z, real even compactly supported eta in L², and integral eta²=1, put K=Fourier(eta²). Proposition 2.1 gives

\[
\#\{\text{simple real elements}\}\ge 2|Z|-\sum_{z,s\in Z}K(z-s)^2.
\]

This is a square, not an absolute square. The Hilbert-space argument does not require entrywise positivity. Lemma 3.1 uses real even L¹ tests supported in [-1,1], Lipschitz at zero. Lemma 3.2 takes smooth eta supported inside (-1/2,1/2); applying the formula separately to Q=eta²*eta² and Q'' removes the rational weight. Remark 3.4 proves optimality **within this method**, citing the Montgomery–Taylor extremal problem.

Numerical evaluations of these displayed constants, independently recomputed with elementary arithmetic here, are C0=0.672500703679412, C1=0.836250351839706, C2=0.887620008173354.

## 3. Exact comparison with our historical energy and Galerkin calculation

Local sources inspected:

- `historical/riemann-rmt/final_verified_paper.md`, §§2.1–2.2 and 7.2–7.3.
- `historical/riemann-rmt/verify_codex.py`, introductory energy and Galerkin definitions. This old script was not executed in this audit.
- `research/dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md`, source-comparison table.
- `research/reports/dyson_round28.md`, source-recheck paragraph.

The historical variational object is, on I=[-1/2,1/2],

\[
E(f)=\int_I f(s)^2\,ds+\int_I\int_I|s-t|f(s)f(t)\,ds\,dt,
\qquad \int_I f=1.
\]

Its recorded optimizer and value are

\[
f_*(s)=\frac{\cos(\sqrt2s)}{\sqrt2\sin(1/\sqrt2)},\qquad
q_*=E(f_*)=\frac12+\frac1{\sqrt2}\cot(1/\sqrt2).
\]

Thus the dictionary is exact: our q* is C_MT, our delta_MT is C0, and Lamzouri's probability profile eta² corresponds to f. The normalization is not a different random-matrix ensemble or a new decimal coincidence.

Here is a short direct check of the limited optimality claim. Define Tf(s)=integral_I |s-t|f(t)dt and A=Id+T. Since

\[
\sup_{s\in I}\int_I|s-t|dt=1/2,
\]

the Schur bound gives operator norm ||T||≤1/2 and hence

\[
\langle h,Ah\rangle\ge\tfrac12\|h\|_2^2.
\]

The equation f*''+2f*=0 implies (Af*)''=0. Evenness makes Af* constant; evaluation at an endpoint gives Af*=q*. For any real f with integral one, set h=f-f*. Then integral h=0, so the cross term vanishes:

\[
\boxed{E(f)-q_*=\langle h,Ah\rangle\ge\tfrac12\|f-f_*\|_2^2.}
\]

This proves the minimum for the entire normalized real L² profile class, therefore also for its nonnegative even subclass. Smooth interior cutoffs approximate f*, so restricting to the smooth profiles does not change the infimum. This elementary check is included for transparency, not claimed as a new extremal theorem.

Every exactly integrated Galerkin profile lies in that same L² class. Increasing its dimension can only approach q* from above. If the final count is still decoded as 2-E(f), it cannot exceed C0. An alleged improvement from that unchanged optimization must involve a normalization error, an altered admissible class, or an altered decoding step.

The distinction between these possibilities matters. The historical `final_verified_paper.md` §7.2 retracts an earlier assertion that C0 was the optimum over every bandwidth-one configurationwise certificate. It distinguishes the profile problem, the marked open-Nyquist problem, and the binary ACUE moment fiber. Section 7.3 also records an unresolved witness/replay boundary for the broader claimed PairCeiling number. Lamzouri's method-specific optimality does not repair or license those stronger claims.

## 4. Knausgård: the later structural candidate

Source: [arXiv:2609.33043v2](https://arxiv.org/html/2609.33043v2), submitted September 27, revised October 7, 2026; Theorems 1–2, Proposition 6, §4.

The preprint claims the distinct-zero proportion 16260119298029/19426831050000=0.83699288145242…. Define

\[
\varphi_c(x)=x^2-(x-c)_+^2,\qquad
\Psi_\tau(x)=(x-1)^2-(x-1-\tau)_+^2.
\]

For Hermitian unit-diagonal U, D=diag(d_i), 1≤d_i≤2, G=D^(1/2)UD^(1/2), tau≥0 and c≥max(1+tau,2+tau/2), its matrix inequality is

\[
\operatorname{tr}\varphi_c(G)-\operatorname{tr}D^2\ge\operatorname{tr}\Psi_\tau(U).
\]

The proof retains overlap contributions from distinct on-line zeros of multiplicity one **or two**. Its seven-point input is an imported computer-assisted inequality. Section 4 says the operator transport, energy asymptotic, local certificate, pinching/block averaging, and smoothing are not formalized; they enter as hypotheses. It reports an independent computational replay but no line-by-line verifier audit, and a remaining tangent-pruner dependency. This audit performed neither replay nor Lean build.

Interpretation for us: this changes the counting inequality and uses geometric spread information. It does not beat the scalar energy minimum and does not contradict §3. No correlation beyond the known support is supplied merely by the improved distinct-zero claim.

## 5. New diagnostic calculation: clipping is inactive on the half-lattice

The following elementary bound is independently proved here. It is a model calculation; its novelty is not asserted.

Let f be any nonnegative probability density supported in I=[-1/2,1/2], K=Fourier(f), and let y_j=a+n_j/2 with distinct integers n_j. The finite Gram matrix U_ij=K(y_i-y_j) satisfies

\[
\boxed{0\preceq U\preceq 2\|f\|_\infty I.}
\]

Indeed, for coefficients b_j, extending the nonnegative integral from I to [-1,1] and using orthogonality of the exponentials gives

\[
\begin{aligned}
b^*Ub
&=\int_I f(u)\left|\sum_j b_j e^{\pi i n_j u}\right|^2du\\
&\le\|f\|_\infty\int_{-1}^{1}\left|\sum_j b_j e^{\pi i n_j u}\right|^2du
=2\|f\|_\infty\sum_j|b_j|^2.
\end{aligned}
\]

For the Montgomery–Taylor density this upper bound is sqrt(2)/sin(1/sqrt(2))=2.176929108088795.

The window explicitly specified in Knausgård's §3 is

\[
v(u)=\cos(\sqrt2u)+10^{-9}\sum_{j=1}^6\kappa_j\cos(2\pi ju),\quad
\kappa=(3322500,-7609135,1190194,-731476,-1680572,1141360),
\quad f=v/\int_Iv.
\]

The integer-frequency corrections integrate to zero. Their absolute coefficients sum to 15675237. Using sin(x)>x-x³/6 at x=1/sqrt(2),

\[
2\|f\|_\infty
\le\frac{2(1+15675237/10^9)}{\sqrt2\sin(1/\sqrt2)}
<\frac{24}{11}(1+15675237/10^9)<2.217.
\]

Positivity also follows from cos(sqrt(2)u)≥3/4 on I and 15675237/10^9<3/4. Hence no unverified decimal minimization is used in this bound.

At the paper's choice tau=12/5, the clipping threshold is 1+tau=17/5=3.4. Every eigenvalue of U is below it. Therefore

\[
\operatorname{tr}\Psi_{12/5}(U)=\operatorname{tr}(U-I)^2
=\sum_{i\ne j}|K(y_i-y_j)|^2.
\]

Thus this particular statistic is entirely determined by full Euclidean pair-difference data on such half-lattice configurations. It can be positive and useful for zero counts without distinguishing pair-matched models. This does not refute the clipped Gram inequality, whose statement is much broader than half-lattice configurations.

The proof uses distinct support points; multiplicities belong separately in D. It uses ordinary real-line differences. Our finite circular homometry certificates cannot silently be substituted: a periodized circular kernel needs its own corresponding spectral estimate. Smooth cutoffs also require tracking their renormalization, although sufficiently close standard cutoffs preserve the strict bound below 3.4.

Research implication: before proposing a new AH discriminator based on a clipped Gram trace, first verify that its spectrum can actually reach the clipping threshold. Otherwise the supposedly nonlinear statistic collapses to an already known pair observable.

## 6. Wang: short-interval localization, with narrower available support

Source: [arXiv:2609.07918v2](https://arxiv.org/html/2609.07918v2), submitted September 7, revised October 6, 2026. Theorems 1.1–1.2 state unconditional short-interval bounds for H=T^theta. Set C_theta=theta/2+cot(theta/sqrt(2))/sqrt(2). The simple-critical lower fraction is 2-C_theta>0 for theta>theta_0=0.5501…, and the distinct lower fraction is (2q+1-C_theta)/(q(q+1)), q=floor(C_theta), for every fixed 0<theta<1. The proof fixes 0<lambda<theta, so this is localization in height, not an extension beyond unit Fourier support. The full analytic proof was not independently verified here. Search-result criticism concerning v1 was not treated as evidence against v2.

For our programme, a controlled height window could help formulate a local energy target. It still contains approximately T^theta log(T)/(2 pi) zeros: this is not a microscopic nearest-neighbor window. No small-gap, shrinking-scale extreme-gap, or inverse-heat stability estimate follows from those counting proportions alone.

## 7. Counterexample compatibility and practical next step

Our historical positive-form and determinant-tail counterexamples address inference from insufficient observations: a compression can miss a negative direction; a few self-moments need not control a determinant or mixed cutoffs. Neither a structured counting inequality nor an improved positive proportion excludes every hidden defect. Thus the new papers do not invalidate those counterexamples, and the counterexamples do not invalidate the papers.

The constructive opportunity is to retain a quantitatively positive remainder that the baseline count discarded. To promote this to a zeta or AH advance, specify the exact target and prove its necessary new ingredient:

| Target | Required ingredient beyond the checked material |
|---|---|
| Improve a zero-count proportion | An audited local overlap inequality and correct global counting/analytic assembly |
| Distinguish pair-matched AH models | A statistic that remains genuinely outside the preserved pair algebra on those models |
| Refute AH using actual zeta | Arithmetic or dynamical information incompatible with all admissible AH models, not simply a positive overlap budget |
| Prove a minimum-gap or Newman-depth law | Uniform shrinking-scale or collision-background estimates; ordinary local universality does not suffice |

A bounded next slice is to isolate and independently verify the mixed-multiplicity matrix inequality, then decide whether its retained remainder measures the specific missing phenomenon. Repeating the old scalar profile optimization is not that slice. Replaying the external seven-point verifier is a separate, explicit task, not something this literature note has completed.

## 8. Search coverage and verification limits

The targeted search covered Lamzouri, September/October 2026 arXiv zeta-zero/pair-correlation entries, and the directly relevant references discovered above. It found no verified extension of the full zeta pair-correlation plateau or higher-correlation support that resolves our arithmetic gap. This is a bounded-search outcome, not a claim of an exhaustive November 1 literature census or a declaration of the current world record.

Version dates were checked on arXiv abstract pages. Theorem statements were checked in the corresponding v2 full texts. The mathematical comparison in §3 and half-lattice bound in §5 are explicit hand derivations; their scalar constants were recomputed. No new Monte Carlo run, interval-certificate replay, formal build, or global Galerkin audit was performed. No historical source was changed.
