"""Assemble complete R6--14 proof/review texts from a verified Git checkpoint.

Only the generated Markdown and JSON index are written. Every source and associated
artifact is byte-compared with its pinned Git blob before it is accepted.
"""
from pathlib import Path
import hashlib
import json
import posixpath
import re
import subprocess
from urllib.parse import quote, unquote, urlsplit

from build_handoff import cleaned

ROOT = Path(__file__).resolve().parents[1]
PIN = "2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba"
REPOSITORY = "https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix"
WEB = f"{REPOSITORY}/blob/{PIN}/"
RAW_WEB = f"https://raw.githubusercontent.com/QingyunSun/Riemann-hypothesis-and-random-matrix/{PIN}/"
OUT = ROOT / "docs/handoff/ASTRA_ROUNDS_6_14_HANDOFF.md"
INDEX = OUT.with_name("ROUNDS_6_14_ARCHIVE_INDEX.json")

# Author proofs precede their independent reviews. README summaries are indexed
# as repository artifacts rather than duplicating their shorter text in the book.
GROUPS = [
    ("R6 — full signed prime-sieve operator and residual direction", [
        "research/reports/prime186_round6.md",
        "research/prime-gaps/round6/operator-proof/FULL_SIGNED_CAP_OPERATOR.md",
        "research/prime-gaps/round6/residual-audit/SIEVE_RESIDUAL_AUDIT.md",
        "research/prime-gaps/round6/operator-diagnostic/FINITE_MARKED_OPERATOR_AUDIT.md",
        "research/prime-gaps/round6/residual-trial/REPORT.md",
        "research/prime-gaps/round6/residual-trial/PROVENANCE.md",
        "research/prime-gaps/round6/operator-diagnostic/OUTSIDE_SPAN_INDEPENDENT_REVIEW.md",
    ]),
    ("R7 — actual-zeta targets, arithmetic mark, and flow obstruction", [
        "research/reports/dyson_round7.md",
        "research/dyson/round7/poisson-resolvent/TWO_SCALE_ZETA_TARGET.md",
        "research/dyson/round7/poisson-resolvent/INDEPENDENT_REVIEW.md",
        "research/dyson/round7/dyson-frontier/POISSON_TRANSFER_REVIEW.md",
        "research/dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md",
        "research/dyson/round7/true-zeta-flow/FORWARD_FLOW_OBSTRUCTION.md",
        "research/dyson/round7/arithmetic-resonator/DERIVATION.md",
        "research/dyson/round7/arithmetic-resonator/REPORT.md",
        "research/dyson/round7/arithmetic-resonator/INDEPENDENT_REVIEW.md",
    ]),
    ("R8 — short-prime projection and signed residual", [
        "research/reports/dyson_round8.md",
        "research/dyson/round8/resolvent-arithmetic/SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md",
        "research/dyson/round8/resolvent-arithmetic/INDEPENDENT_IDENTITY_AUDIT.md",
        "research/dyson/round8/spectral-positivity/POSITIVITY_OBLIGATION_NOTE.md",
        "research/dyson/round8/spectral-positivity/MINORANT_REVIEW.md",
    ]),
    ("R9 — complementary moduli, genuine-prime tails, and the edge", [
        "research/reports/dyson_round9.md",
        "research/dyson/round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md",
        "research/dyson/round9/factorization-covariance/INDEPENDENT_BRIDGE_REVIEW.md",
        "research/dyson/round9/multiplicative-profile/DERIVATION.md",
        "research/dyson/round9/multiplicative-profile/REPORT.md",
        "research/dyson/round9/multiplicative-profile/INDEPENDENT_REVIEW.md",
        "research/dyson/round9/prime-power-removal/PRIME_POWER_TAIL_ESTIMATE.md",
        "research/dyson/round9/prime-power-removal/INDEPENDENT_REVIEW.md",
        "research/dyson/round9/mesoscopic-edge/EDGE_RATE_AUDIT.md",
        "research/dyson/round9/mesoscopic-edge/INDEPENDENT_EDGE_REVIEW.md",
    ]),
    ("R10 — complete the actual shift packet", [
        "research/reports/dyson_round10.md",
        "research/dyson/round10/shift-average/SMOOTH_SHIFT_COMPLETION_BOUND.md",
        "research/dyson/round10/shift-average/COEFFICIENT_AND_SPACING_AUDIT.md",
        "research/dyson/round10/shift-average/ACTUAL_KERNEL_AND_PRIME_POWER_REVIEW.md",
        "research/dyson/round10/arithmetic-residual/ARITHMETIC_RANGE_AND_MIXED_MOMENT.md",
        "research/dyson/round10/arithmetic-residual/INDEPENDENT_REVIEW.md",
    ]),
    ("R11 — RH small arcs and actual conductor structure", [
        "research/reports/dyson_round11.md",
        "research/dyson/round11/prime-frequency/CENTERED_SMALL_ARC_BOUND.md",
        "research/dyson/round11/prime-frequency/SMALL_ARC_INDEPENDENT_REVIEW.md",
        "research/dyson/round11/conductor-arithmetic/CONDUCTOR_MASS_LOWER_BOUND.md",
        "research/dyson/round11/conductor-arithmetic/INDEPENDENT_REVIEW.md",
        "research/dyson/round11/log-weighted-tail/ARITHMETIC_DIAGONAL_AND_SOURCE_GAP.md",
        "research/dyson/round11/log-weighted-tail/INDEPENDENT_REVIEW.md",
    ]),
    ("R12 — exact limits of sampling and dispersion transfers", [
        "research/reports/dyson_round12.md",
        "research/dyson/round12/sampling-geometry/ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md",
        "research/dyson/round12/sampling-geometry/COUNTING_REVIEW.md",
        "research/dyson/round12/dispersion-transfer/DISPERSION_HYPOTHESIS_OBSTRUCTION.md",
        "research/dyson/round12/mixed-arithmetic/SELBERG_MIXED_REMAINDER_AUDIT.md",
        "research/dyson/round12/INDEPENDENT_ROOT_REVIEW.md",
    ]),
    ("R13 — rational-core extraction and the signed CRT remainder", [
        "research/reports/dyson_round13.md",
        "research/dyson/round13/phase-resonance/AVERAGED_RATIONAL_PHASE_TEST.md",
        "research/dyson/round13/minor-arc-source/MINOR_ARC_AND_FIXED_INTERVAL_AUDIT.md",
        "research/dyson/round13/signed-kernel/SMOOTH_SIGNED_KERNEL_NORM.md",
        "research/dyson/round13/signed-kernel/INDEPENDENT_AUDIT.md",
        "research/dyson/round13/INDEPENDENT_ROOT_REVIEW.md",
    ]),
    ("R14 — smooth Type I removal and quantitative finite CUE heat", [
        "research/reports/dyson_round14.md",
        "research/dyson/round14/smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md",
        "research/dyson/round14/smooth-long-factor/INDEPENDENT_REVIEW.md",
        "research/dyson/round14/cue-selected-background/SELECTED_CUE_BACKGROUND.md",
        "research/dyson/round14/cue-selected-background/INDEPENDENT_REVIEW_EUCLID.md",
        "research/dyson/round14/INDEPENDENT_ROOT_REVIEW.md",
    ]),
    ("Fable intake — 89393d5 and 2073028, separate reviewed corrections", [
        "fable/reviews/pr11-89393d5/INTAKE_REVIEW.md",
        "fable/reviews/pr11-89393d5/BACKGROUND_AND_BOUNDARY_REVIEW.md",
        "fable/reviews/pr11-2073028/INTAKE_REVIEW.md",
        "fable/reviews/pr11-2073028/F1_F3_INDEPENDENT_AUDIT.md",
        "fable/reviews/pr11-2073028/F1_REPAIR_AND_CUTOFF_REVIEW.md",
        "fable/reviews/pr11-2073028/F3_MASS_CUTOFF_BOUND.md",
        "fable/reviews/pr11-2073028/CBETA_REPAIR_REVIEW.md",
    ]),
]

SOURCE_PREFIXES = ["research/prime-gaps/round6/"] + [
    f"research/dyson/round{i}/" for i in range(7, 15)
] + ["fable/reviews/pr11-89393d5/", "fable/reviews/pr11-2073028/"]
EVIDENCE_PREFIXES = SOURCE_PREFIXES + [
    f"research/logs/round{i}-integration/" for i in range(6, 15)
]

FRONT = r"""# Riemann zeros, random matrices and actual prime arithmetic

## Rounds 6–14: complete takeover supplement / 第 6–14 轮完整接棒补编

**Source checkpoint: `2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba`, 2026-09-05.** This book follows the earlier main handoff and Rounds 4–5 supplement. It prints the complete substantial reports and independent reviews from the subsequent work, including the final R14 proofs and both later Fable intakes. It is a faithful research archive, not an announcement that a famous conjecture has been solved.

**当前结论：没有证明 RH、Montgomery/GUE 猜想、AH-Pairs 的反驳、新的 ζ 半间隙定理或小于 186 的素数间隙。** 已完成的工作包括：真实算术误差项的两次改进、一个可在所需尺度下消去的精确 Type I 分量、有限 CUE 热流的定量误差、具有精确假设的反例与障碍，以及完整保留的负向变分实验。数值增益、普通证明、独立内部审查与形式验证在本文中始终分开。

The intended next researcher is GPT-6 Astra or a human analyst taking over without access to the live conversation. Read this synthesis first, then the integrated report for the chosen lane, then its full proof and independent review. The main earlier archive remains necessary for the original ACUE constructions, fixed-family arithmetic-transfer proof, Galilean heat lemma, force-energy identities, and Rounds 1–5 prime-gap certificates. Those earlier documents are linked by pinned source paths rather than silently reproduced under a new date.

## 1. What the programme is trying to prove

The main target is a substantive theorem about **actual zeta zeros** and the Montgomery–Dyson connection. Random-matrix examples and heat flow are tools for isolating missing hypotheses, not substitutes for the arithmetic explicit formula. The most concrete accepted reductions concern the precise AH-Pairs formulation, including its possible near-diagonal mass. General AH must not be replaced by a simple hard-core process with gap at least one half. Multiplicity or near-coincident pairs can occupy the zero lattice point. An arbitrarily small gap, or a positive proportion of gaps below one half, need not by itself refute the full hypothesis unless the statistic also excludes that near-zero freedom.

There are three explicit formulations of the arithmetic target. Each is sufficient under its recorded RH and limiting hypotheses; none has been proved here.

**Notation warning / 记号须按章节理解.** N denotes the CUE matrix dimension in the heat-flow reports, the Dirichlet cutoff floor(T/log⁶T) in the resolvent reports, and a short factor of size X^.4 in the R13 Type II discussion. These are different objects. D_N is finite polynomial heat depth, while \(\mathcal D_{\mathcal Q}^V\) is an arithmetic progression discrepancy. The resonator length L, a smooth long-factor length, and the L used to truncate the minimum-gap tail also have separate local meanings. Each full report resets its definitions. Exceptional close pairs in an RMT model do not by themselves refute a density-version AH statement for zeta.

### 1.1 The fixed two-width resolvent target

For fixed c>0 define

\[
I_T(c)=\int_0^T\left|\frac{\zeta'}{\zeta}
\left(\frac12+\frac c{\log T}+it\right)\right|^2dt,
\qquad
W_T=\frac{2[\sinh(2)I_T(1)-\sinh(1)I_T(1/2)]}{T\log^2T}.
\]

Under RH and AH-Pairs, the reviewed reduction gives

\[
W_T\longrightarrow W_{\rm AH},\qquad
0.06239<W_{\rm AH}<0.06240<\frac1{16}.
\]

The sine-kernel prediction is approximately 0.0822714431214773. Therefore

\[
\boxed{\liminf_{T\to\infty}W_T\ge\frac1{16}}
\]

would refute AH-Pairs under RH. The previously discussed target 0.07 is also sufficient, but unnecessarily strong. The two widths were chosen to cancel the bounded near-diagonal parameter P₀(T) exactly; no convergence of that parameter is assumed. Tail truncation, finite-height endpoints, the Gamma factor, ξ′/ξ normalization and the holomorphic-square passage are part of the printed proof and reviews. The reduction itself is established; the displayed actual-zeta lower bound is not.

### 1.2 A compact out-of-band Fourier test

Fix the recorded nonnegative smooth bump φ, integral one, supported on [6/5,7/5] and symmetric about 13/10. For the normalized form factor F_T,

| Observable | RH + AH-Pairs prediction | Sine-kernel prediction |
|---|---:|---:|
| ∫φ(α)F_T(α)dα | 7/10 | 1 |
| Centered prime-covariance remainder | −3/5 | −3/10 |

An actual lower limit strictly above 7/10 for the first observable, or strictly above −3/5 for the corresponding centered remainder, would exclude AH-Pairs. The limit 1 would establish this one smooth Montgomery prediction. It would not automatically prove the entire pair-correlation conjecture or RH. The full prime-prime term, prime-continuum cross terms, continuous mean square and diagonal must remain present.

### 1.3 A shrinking mesoscopic correction

The residual route uses N=floor(T/log⁶T) and

\[
R_c(t)=-\frac{\zeta'}{\zeta}\left(\frac12+\frac c{\log T}+it\right)
-\sum_{n\le N}\Lambda(n)n^{-1/2-c/\log T-it}.
\]

Round 8 proves under RH that W_T=B+\(\mathcal E_T\)+o(1), where B≈0.4560939793292317 and

\[
\mathcal E_T=
\frac{2[\sinh(2)\|R_1\|_2^2-\sinh(1)\|R_{1/2}\|_2^2]}{T\log^2T}.
\]

The fixed-width sufficient target is therefore liminf \(\mathcal E_T\)≥−0.3935939793292317…. The residual combination is signed and of leading order. Positivity of its two individual energies does not prove the target.

For b=2c set r_T(b)=\(\|R_{b/2}\|_2^2/(T\log^2T)\). The coupled statistic

\[
\mathcal C_T(b)=b^2\left[
2\sinh b\,r_T(b)-2\sinh(2b)\,r_T(2b)-\frac1{2b}\right]
\]

has sine prediction 0 and AH prediction −3/4 after the same nuisance cancellation. The sufficient lower bound has uniform quantifiers on a slowly growing envelope G(T)=o(log log T), followed by B→∞:

\[
\lim_{B\to\infty}\liminf_{T\to\infty}
\inf_{B\le b\le G(T)}\mathcal C_T(b)>-\frac34.
\]

A fixed-width limit does not authorize a prescribed growing rate. The needed error is a first correction of relative order 1/b, not merely a leading relative o(1) estimate. The reports state an equivalent sufficient signed logarithmic mixed-moment bound. Its positive diagonal is explicit, but its centered off-diagonal remainder remains open.

## 2. The strongest arithmetic results at this checkpoint

Write X=T^α with 6/5≤α≤7/5, H=X/T, and Q=X^(523/1000). Thus H ranges from X^(1/6) to X^(2/7). The selected complementary squarefree modulus family is inherited from the 186 paper's verified ordinary analytic input. Repeated representations of one modulus are counted only once. These numbers belong to a particular arithmetic component; 0.523 is not a zero-distribution exponent or a new prime-gap record.

The exact smooth discrepancy retains a fixed V(h/H), the original sinc kernel, μ(q) log((m−h)/q), and the primitive principal sum. Its useful bounds progress as follows.

| Stage | Proved bound for the specified discrepancy | Assumptions and remaining limitation |
|---|---|---|
| R9 source transfer, summed absolutely over h | O_A(HX log^(−A)X) | Ordinary source theorem; fixed logarithmic saving cannot absorb polynomial H. |
| R10 shift completion | O(√(HX(X+Q²)) log⁴X) | Unconditional; original smooth joint kernel restored after separation. |
| R11 centered small arcs | O(√(X(X+Q²)) log⁵X)=O(X^1.023 log⁵X) | Under RH; removes √H, but remains above X log X. |
| R14 short Möbius divisor portion | O_J(HX(UQ/X)^J log²X) | Unconditional for UQ≤X/2 and fixed J≥2; the exact signed remainder is retained. |

Round 11 uses an actual RH centered-prime small-arc estimate, including its derivative version, before sampling at the rational frequencies. Equal fractions are merged first. Its coefficient band mass and local arc length cancel H. The integer mean and primitive Ramanujan mean are treated separately and both remain accounted for. This is a genuine improvement of a defined arithmetic error bound. It still leaves a factor X^.023, apart from logarithms, above the required covariance scale. It is not a proof that this factor is necessary for primes.

Round 14 makes a further exact reduction. Define

\[
\Lambda_{\le U}(n)=\sum_{r\mid n,\ r\le U}\mu(r)\log(n/r),
\qquad \Lambda=\Lambda_{\le U}+\Lambda_{>U}.
\]

For U=X^.4 and J=4, the bound for the first portion is O(X^(1711/1750)log²X)=o(X log X). More generally every fixed η>0 with η<.477 permits U≤X^(.477−η), choosing fixed J with Jη>2/7. This follows from exact progression Poisson summation in the genuinely smooth long cofactor. Its zero mode cancels the actual primitive principal term. The normalized joint kernel has uniform derivatives; no regularity is assigned to the short Möbius sequence. A product of several rough long factors does not satisfy this hypothesis merely because its total length exceeds Q. The remaining Λ_{>U} discrepancy is an exact signed arithmetic object and is unestimated.

The strongest full selected smooth-packet bound is consequently still the R11 RH estimate. The short-divisor removal identifies a smaller residual problem; it is not a bound for every remaining piece. The complete covariance additionally requires complementary moduli, support main terms, other ranges and continuous centering. None may be suppressed because the selected component is attractive to calculate.

## 3. The finite CUE theorem that is now on firm ground

For Haar CUE(N), let δ_min be the smallest angular gap, and B_N the inverse-square circular background at that gap's midpoint. Round 14 proves directly from the exact finite-N three-point Gram determinant that

\[
\mathbb E\sum_{i:\delta_i\le\varepsilon} B_i
\le\frac{N^6\varepsilon^3}{18},\qquad 0<\varepsilon\le\pi.
\]

The endpoint zeros in the determinant cancel the singular endpoint weight. The proof enlarges an endpoint-weighted count to all short ordered pairs only after that cancellation; enlarging a midpoint-weighted count directly would be invalid. Circular ordering includes the wrap gap. No conditional density of a selected minimum is assumed. Combining the estimate with the classical CUE minimum-gap law gives B_N/N²=O_p(1), with an explicit truncation-tail bound.

For the specified scalar-heat evolution of the characteristic polynomial, with D_N its first positive discriminant time, the existing deterministic Galilean lemma then yields

\[
\frac{8D_N}{\delta_{\min}^2}-1=O_{\mathbb P}(N^{-2/3}),
\qquad D_N-\delta_{\min}^2/8=O_{\mathbb P}(N^{-10/3}).
\]

This is a quantitative approximation in probability for finite CUE. It is not a rate for convergence of the entire depth distribution, a theorem for general β, a stochastic Dyson Brownian motion theorem, or an established property of actual zeta zeros. The earlier qualitative ratio and deterministic lemma are explicitly credited in the new proof. No global literature novelty claim is made.

The distinction matters for the original research aspiration. RMT supplies a rigorous reference law and precise mechanisms. A zeta theorem needs the arithmetic hypothesis that forces the corresponding local behavior. Reusing the RMT conclusion under a name such as “alternative COE” cannot supply that missing hypothesis.

## 4. Failed approaches that materially changed the programme

### 4.1 More fixed resonator features did not cross the half-gap threshold

The original request to enlarge S₂/S₃ polynomials was checked against the archive before computation; it duplicated an earlier sweep. The replacement in R7 was the sharp integer mark for a prime divisor above √L. The fixed family has a direct unique-large-prime decomposition and a reviewed limiting arithmetic transfer. Its 30-dimensional half-gap margin is about −0.01465492379421, improving its matched baseline by only 1.429×10⁻⁸. It remains worse than the older 48-feature value near −0.0146547256.

A later proposed multiplicative profile also duplicated an already resummed experiment. R9 instead used the nonmultiplicative event of two distinct prime divisors above L^(1/3). Its unique unordered double-prime decomposition is exactly coprime; its singly marked formula requires an explicit repeated-prime error. The new fixed 30-dimensional margin is −0.0146549114371551 versus −0.0146549380840028 for its matched baseline, a floating gain of about 2.66×10⁻⁸ at scaled Gram condition about 5.36×10⁷. Its actual finite-integer frozen-vector test at L=100000 has margin −0.0374094621535042.

These are new concrete arithmetic families and useful transfer checks. The numerical gains are not interval-certified and are far from crossing zero. Their spans do not contain the entire older 48-feature space. They prove no global no-go for resonators, and do not justify another blind coefficient sweep. All coefficients and matrices remain in the repository with hashes.

### 4.2 Generic positivity does not deliver the arithmetic gain

The explicit R8 minorant gives a valid bound around −0.208674513 for W, far below 1/16. Optimality was proved only inside that fixed one-parameter family. A realized stationary half-grid determinantal process satisfies the available low-band information and positivity yet attains W_AH<1/16. This blocks an inference from those hypotheses alone. It does not describe actual primes or rule out an arithmetic theorem.

The two residuals do arise from the same centered arithmetic function ψ(x)−x, and after the justified prime-power removal from θ(x)−x. Their common origin is useful structure. Its mere existence, or the positivity of each residual norm, does not fix the sign of their weighted difference. The pole and endpoint terms must first be bounded; an unregularized infinite prime series in the critical strip is not a legal replacement.

### 4.3 Deterministic heat and protected traces do not force GUE

The R7 flow report supplies a deterministic contraction bound under its stated external-field condition, but leaves an actual-zeta boundary-propagation estimate open. Its exact finite polynomial family begins on a half-grid up to rotation and retains all normalized gaps at least one half under forward flow, tending toward a clock. This defeats a proposed implication from those dynamical hypotheses. It is not a counterexample obeying the full zeta explicit formula.

The protected trace algebra also remains matched under the recorded full DBM comparison. At a protected frequency m=N/2 the stochastic microscopic generator contribution at CUE is π². Thus a deterministic calculation cannot simply discard stochastic smoothing because a collection of low moments agrees. The original AH definition and the distinction between actual and artificial wrap gaps remain essential.

### 4.4 Actual conductor geometry obstructs norm-only shortcuts

R11 constructs an admissible terminal complementary family using two primes of exponent .09 and 346 distinct smaller primes of exponent 343/346000. It has ≫Q/log^348X moduli near Q. At terminal d=q>Q/2, no other permitted multiple exists, so the full Möbius coefficient is exactly 1/d. The coefficient squared mass is at least a constant times H/log^348X. This rules out a fixed-power coefficient-norm improvement for that full family. It does not rule out pruning, different weights, or cancellation with genuine prime sums.

R12 uses the same actual frequencies to prove sharpness up to logarithms for a positive sampling step, including its known local energy and derivative envelopes. The saturating polynomial is artificial. This is an obstruction to that general sampling argument, not a lower bound for the actual centered-prime functional and not evidence that X^.023 is unavoidable for primes.

### 4.5 Direct import of the 186 dispersion theorem fails specific premises

An additive twist of a genuine-prime short coefficient can lose the required Siegel–Walfisz property. The explicit modulus-3 example, at legal source scales M=X^.6 and N=X^.4, gives a discrepancy of leading size N/log N. The source theorem remains true; the transformed coefficient does not satisfy its hypothesis. The coherent shift interval also cannot be replaced by the Cartesian product of all its local residue images without an enormous class cost. Taking H itself as the short convolution length falls below the checked source range.

These failures identify what an averaged replacement must preserve: the joint m,a,d,h phases and cross-prime coherence. They do not prove that every averaged use of dispersion fails.

### 4.6 Short-interval theorems miss the needed scale or correction

The checked Guth–Maynard corollary concerns h≥X^(2/15+ε), with fixed ε. The mesoscopic shell here has exponent s/(b+s)→0. Even the corollary's ε-zero endpoint misses that shell for b>13; the following remark's slight fixed improvement does not resolve a vanishing exponent. Almost-all PNT counts also do not by themselves provide a variance constant.

The checked three-integral comparisons have constant losses larger than the shrinking sine-versus-AH signal. Their finite-T errors can be made small on a sufficiently slow diagonal, so it would be wrong to blame only height errors. The limiting lower bound misses a first correction. R12's actual Selberg audit retains both cutoff crossings and the joint mean, yet does not supply the necessary sign or b⁻³ precision in the mixed moment. These are source-specific quantitative failures, not a claim that all existing analytic methods are exhausted.

### 4.7 A positive rational core does not lower-bound the signed whole

R13 extracts the zero-rational Type II core with total RH replacement error O(X^.923 log²X), retaining the explicit integral main term. An admissible restricted positive block can have size at least a constant times X^1.123/log^348X. Other phases and the actual long coefficients may cancel it. R14 gives a constructive instance of such complete cancellation when a long factor is smooth.

The exact signed-kernel norm has a CRT/Poisson main term and an explicit remainder. Large original common divisors give short enough CRT periods for smooth decay. The small-gcd long-period terms remain. A coherent positive off-diagonal subsum of size at least a constant times Q²H/log^696X is not a lower bound for the complete signed remainder. Reduced denominator gcd and original modulus gcd are different quantities. Even an ideal unrestricted integer norm of order XH would not alone give the desired prime-specific bound.

## 5. The R6 prime-gap work that had not reached the earlier PDFs

R6 constructs the full signed cap operator, rather than defining an operator only through a 77×77 matrix. Its finite fragment measure is not a probability measure conditioned on the outer domain. The erased-coordinate adjoint is an unweighted lift with outer support. On product amplitudes the single erased g factor must not become a g² conditional expectation. The face multiplier can be negative; positive-semidefinite assumptions are invalid.

For the old mass-orthogonal projection P and a radial projection P_V that need not commute with it, the useful direction is

\[
r=(I-P)Tf,\qquad h=P_Vr,\qquad w=(I-P)h,
\qquad \langle f,Tw\rangle=\|h\|^2.
\]

For unit f, its normalized mixed entry is \(\|h\|^2/\|w\|\), not simply \(\|w\|\). The actual mass projection of Tf is used, without assuming an exact Ritz vector. The active radial cells are frozen and define the chosen subspace; small excluded mass is not a bound for omitted residual energy.

The fixed k=39 direct cap quotient rises from 0.9943963993644909 to 0.9944678209006830, about 71.4215 ppm. An exact dyadic-rational/polynomial-root certificate proves the stored direction is genuinely outside the old 77-space on positive-measure cells. That exact independence certificate does not certify the numerical gain. The Gram condition is large, the quotient is still about 5532.18 ppm below one, and arithmetic support restoration remains unproved for the candidate. The actual 2×2 plane supplies only about 1.26% of its crossing requirement, without estimating the full residual.

Four public compact NPZ witnesses retain all candidate and projection arrays except the regenerable 77×N density cache. The four original full archives remain local with hashes and array-by-array compaction receipts. This is explicit storage compaction, not deletion of adverse outputs. The prime-gap bound remains 186; the prior R4 rigorous margin gain and R5 geometry constraints should be read in their separate earlier supplement. Prime-gap broad sweeps were paused when the user redirected the main lane to actual zeta and Dyson–Montgomery.

## 6. Fable corrections must travel with their source snapshots

The 89393d5 intake repaired the moment coefficient to Π₄∼6aε⁻⁴, while also finding a sign error in the refuter's own derivative probe and a table mixing different v values. A successful replay of a refuter reproduces its failures; it does not certify every assertion in it. Finite drift does not disprove an asymptotic fixed-family limit without a proved constant and threshold. The later Astra fixed-family transfer remains separate from Fable's unfinished quantitative-rate discussion.

At 2073028 the corrected F1 coefficient and fixed-v table are accepted. The finite prime-sum cutoff is explained by the reviewed incomplete-gamma limit. The F3 assertion of an infinite field norm on the mass cutoff is false. A complete weighted sector proof gives, for g(u)=2sin(πu/2),

\[
\|K\|\le2\int_0^1\frac{|g(u)|^2}{u^2}du
=4\pi\operatorname{Si}(\pi)-8\approx15.27212735.
\]

This proves finite boundedness for the stipulated idealized operator and uniformly for the literal discrete grids. It lies above π²/2, so it proves no sharp spectral wall. The first interval has infinite du/u measure, and a nonzero constant there is not a normalized Galerkin basis vector. Numerical extrapolations near 4.6456 remain numerical evidence, with no proved full arithmetic-to-Fock transfer.

The general-β background repair is still only partial. Its purported exact finite-N CUE formula is a sine limit; its comparator vanishes at q=2π while the true normalized two-point density is one. Its uniform replacement v′=v(1+O(ε/w)) fails near an endpoint. A direct conditional triple integral restores the intended L^(β+1)c^(2β+1) exponents, but does not prove general-β density control. Uniform one-point intensity alone cannot control the background of a selected smallest pair: a randomly rotated clustered configuration is a counterexample to that inference. The independent R14 finite-CUE argument uses the needed higher correlation structure and does not rely on these uncorrected general-β claims.

Both intake reviews are printed in full below. The 141-file and 160-file Fable snapshots remain separately pinned in the repository; their complete duplicated source texts are not printed again in this supplement. This separation preserves original errors and later corrections without rewriting history.

## 7. Prioritized next work, with concrete success criteria

These are research proposals, not claims that any famous conjecture is now within a guaranteed final step. Prefer one bounded calculation or lemma with a falsifiable acceptance condition before a larger search.

1. **Estimate the actual remaining arithmetic term after R14 removal.** Start with the exact Λ_{>U} discrepancy, fixed U≤X^(.477−η), and the original joint sinc/log kernel. Use a stated Heath–Brown decomposition and preserve the primitive mean. Identify one remaining factor pattern and prove an aggregate bound strictly below X log X, or exhibit the exact source hypothesis that fails. A smooth long variable is already handled; relabeling that case is not new progress.
2. **Keep signed phase information through the long-variable average.** R12 forbids a blanket SW inheritance claim for twisted coefficients. R13 isolates rational cores and their main terms. A useful next theorem must estimate their full signed combination with the actual coefficients, not only a positive subblock or a norm for arbitrary integer polynomials. Record every denominator, numerator and gcd range. Success requires a power improvement over the X^1.023 bound or a directly useful signed covariance estimate, not a logarithmic cosmetic gain.
3. **Attack the mixed genuine-prime remainder at the exact first correction.** Use the finite centered measure and logarithmic companion already proved in R11. The positive diagonal is b⁻²+2b⁻³. A strict one-sided improvement for the combined off-diagonal remainder, or its integrated version, could imply the mesoscopic AH-excluding criterion. State uniformity through twice a valid slow envelope; keep the two prime-continuum terms and continuum square together. A mere O(1) energy bound is not the requested result.
4. **Use the CUE theorem as a precise reference theorem.** Any zeta heat-flow transfer must supply an actual local arithmetic hypothesis strong enough to control selected near-pair backgrounds and true boundaries. Test it against the half-grid, rotated-cluster and artificial-wrap examples before trying to prove it. A general-β extension would require a correct finite-N n=3 bound with the stated domain; it cannot be imported from weak process convergence alone.
5. **If returning to variational search, demand a structural reason for a gain.** The simple power-sum, resummed multiplicative, single-large-prime and double-large-prime directions are already archived. Choose a genuinely different fixed integer feature or a proved extension of the available mixed arithmetic form. Give exact coefficient meaning and a controlled transfer before treating a continuum model as a zeta test. A negative finite span is not a global barrier.
6. **Formalize selected stable components after proof review.** Good bounded candidates are the primitive Poisson cancellation, the exact mass-cutoff Fock inequality, the finite-N CUE Gram/singular-weight estimate, and the finite rational outside-span witness. The FLT formalization work motivates careful decomposition and proof checking; it supplies no unproved analytic input. A proof-assistant certificate must be reported separately from Python checks and internal reviews.

暂缓：同一负向系数空间的重复扫描、把普通 PSD 或点过程正性再包装成算术输入、忽略 ζ 的 pole/mean 交叉项、以假设缺失的 periodization 推出真实小间隙、重复开启 Fable 会话，以及把数值外推或程序复算称为已证明的历史级定理。研究主线应以“缺少的真实算术估计是否推进”为进度标准，而不是文件数或模型轮数。

## 8. 中文接棒判断与阅读顺序

最值得继续的变化，不是又找到了一个更像随机矩阵的模型，而是已经把若干模糊目标改写为可核查的真实算术不等式。第 7 轮消除了 AH 中可能不收敛的近零质量；第 8–11 轮把两个 resolvent 的能量差写成同一个中心化素数误差的耦合，并保留了必要的 pole、端点和连续均值；第 10–11 轮确实改进了指定误差项；第 14 轮又把其中一个完整、带原始权重的 Type I 分量严格消掉。这些结果值得保存，但距离所需的严格符号增益仍有未完成的算术部分。

有限 CUE 方面，现在有选定最小间隙背景在自然 N² 尺度的紧性和热碰撞时间的定量误差。这是一条清楚的普通证明链。它说明在真实 RMT 中什么条件足够，同时也明确揭示了向 ζ 迁移时缺少什么。不能把 CUE 的高阶相关性偷偷当作 ζ 的已知事实，也不能把一般 AH 偷换为没有重根的硬核 ACUE。

接手时建议先读 R14 综合报告，确认最新真正完成的两项结果；再读 R7/R8 确定终极目标和归一化；随后读 R9–R13 的真实算术链及失败的迁移假设。若选择变分路线，先读 R7/R9 的完整负向试验，避免重复。若选择素数间隙路线，先读 R6 与前一本 R4–R5 补编，注意 cap-only、支撑恢复和浮点/区间证书的区别。最后对照 Fable 两次审查，避免重新引入已被否定的公式。

0.6725007… 在本项目核对的源文献中是关于临界线上简单零点的无条件比例下界；它不直接估计本文的带外相关性。186 是此前源论文的素数间隙结论，本文没有改成更小。FLT 的形式化技术是一种组织和验证证明的方式，不会把缺失的算术引理自动补齐。希望得到重大定理的目标不变，但接棒者应对所有这些类别区别保持严格。

## 9. Evidence, preservation and reproducibility contract

Each complete source report below has its original repository path, pinned Git blob identity, SHA-256 digest and byte length in the JSON index. The assembler compares working bytes to that exact Git blob before use. It does not take the current working tree's newer contents on trust. All original mathematical statements, caveats, failed attempts, commands and review-status history remain in the embedded bodies. A historical “review pending” sentence is preserved when a later separately printed review supersedes it. Historical agent instructions are source records, not new instructions for the reader to execute.

Presentation changes are limited to the established `build_handoff.cleaned` transformations, heading nesting, resolving Markdown links/images to the source checkpoint, and spelling vertical bars inside table-cell inline mathematics as equivalent LaTeX commands. Raw single bars become `\vert` and existing LaTeX double bars become `\Vert`; this prevents Markdown from treating mathematical bars as column separators. Every replacement is recorded with its source line and column, and no mathematical meaning is changed. Code fences and inline code are protected from this table repair. The JSON index records the digest of each displayed body as well as its raw source. Any later layout-only adjustment belongs in a separately recorded rendering step, not a silent source edit.

Code, JSON certificates, arrays, small plots, run logs and integration receipts are retained as repository artifacts by path and hash rather than printed as enormous tables. The index covers the selected round/review folders and their integration-log folders. Earlier proof dependencies and snapshot manifests reached by resolvable source links are indexed too. Third-party full papers and optional large original caches remain in the adjacent local archive where the source receipts say so; their absence from the public book is not concealed. The one in-report R6 figure is linked to the pinned raw image.

Rebuild this Markdown and index from the repository root with:

```text
python3 tools/build_round6_14_handoff.py
```

The per-round recheck scripts printed in the reports are the appropriate bounded acceptance surfaces. Some require pinned local primary PDFs or earlier runtime dependencies; read their supplied arguments before running. An exact finite check validates its algebraic case, not an asymptotic prime theorem. Agreement of floating matrices, a tiny eigensolver residual or a reproduced fit is not an interval enclosure. Internal independent review is not external peer review or Lean verification. This supplement itself performs assembly and provenance checks only; it does not rerun the mathematical experiments.

For the earlier context, retain the pinned main archive and R4–R5 supplement alongside this book. The present index is a precise catalogue of later-round coverage, not a claim to include private conversations or every earlier source document for a second time.
"""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def tree() -> dict[str, dict]:
    result = {}
    for entry in git("ls-tree", "-rz", PIN).split(b"\0"):
        if not entry:
            continue
        metadata, path = entry.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split()
        if kind == "blob":
            result[path.decode()] = {"git_blob": oid, "mode": mode}
    return result


def table_math_presentation(raw: str) -> tuple[str, list[dict]]:
    """Escape table-cell math bars without changing separators or code spans.

    Locations refer to one-based Unicode character positions in the raw source.
    A trailing space terminates each TeX control word and has no rendered width.
    """
    lines = raw.splitlines(keepends=True)
    eligible = []
    fence = None
    for line in lines:
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif marker[1][0] == fence:
                fence = None
            eligible.append(False)
        else:
            eligible.append(fence is None)
    divider = re.compile(r"^\s{0,3}\|?\s*:?-+:?\s*(?:\|\s*:?-+:?\s*)+\|?\s*$")
    rows = set()
    for i, line in enumerate(lines):
        if i and eligible[i] and eligible[i-1] and divider.fullmatch(line.strip()) and "|" in lines[i-1]:
            rows.add(i-1)
            j = i+1
            while j < len(lines) and eligible[j] and lines[j].strip() and "|" in lines[j]:
                rows.add(j)
                j += 1

    def escaped(text: str, at: int) -> bool:
        preceding = 0
        at -= 1
        while at >= 0 and text[at] == "\\":
            preceding += 1
            at -= 1
        return preceding % 2 == 1

    changes = []
    for row in sorted(rows):
        original = lines[row]
        edits = []
        pos = 0
        while pos < len(original):
            if original[pos] == "`":
                end_ticks = pos
                while end_ticks < len(original) and original[end_ticks] == "`":
                    end_ticks += 1
                close = original.find(original[pos:end_ticks], end_ticks)
                pos = len(original) if close < 0 else close + end_ticks-pos
                continue
            if original.startswith(r"\(", pos) and not escaped(original, pos):
                opener, closer = r"\(", r"\)"
            elif original[pos] == "$" and not escaped(original, pos) and not original.startswith("$$", pos) and (pos == 0 or original[pos-1] != "$"):
                opener, closer = "$", "$"
            else:
                pos += 1
                continue
            end = original.find(closer, pos+len(opener))
            while end >= 0 and (escaped(original, end) or (closer == "$" and original.startswith("$$", end))):
                end = original.find(closer, end+len(closer))
            if end < 0:
                pos += len(opener)
                continue
            start = pos+len(opener)
            cursor = start
            while cursor < end:
                if original.startswith(r"\|", cursor) and not escaped(original, cursor):
                    old, new = r"\|", r"\Vert "
                elif original[cursor] == "|" and not escaped(original, cursor):
                    old, new = "|", r"\vert "
                else:
                    cursor += 1
                    continue
                edits.append((cursor, old, new))
                changes.append({
                    "source_line": row+1, "source_character_column": cursor+1,
                    "old": old, "new": new, "inline_math_delimiter": opener,
                    "source_inline_math": original[pos:end+len(closer)],
                    "reason": "Equivalent TeX bar command prevents Markdown table-column splitting",
                })
                cursor += len(old)
            pos = end+len(closer)
        updated = original
        for at, old, new in reversed(edits):
            assert updated[at:at+len(old)] == old
            updated = updated[:at] + new + updated[at+len(old):]
        lines[row] = updated
    return "".join(lines), changes


def check_table_math_presentation() -> None:
    sample = (
        "Outside $|x|$ and \\(\\|y\\|\\) stay unchanged.\n\n"
        "| $|h|$ | Value |\n|---|---|\n"
        "| $|x|+\\|y\\|$ | \\(|z|+\\|w\\|\\), `$|code|$` |\n\n"
        "```text\n| $|code|$ | b |\n|---|---|\n| a | $|code|$ |\n```\n"
    )
    actual, changes = table_math_presentation(sample)
    assert len(changes) == 10
    assert actual.startswith("Outside $|x|$ and \\(\\|y\\|\\) stay unchanged.")
    assert "| $\\vert h\\vert $ | Value |" in actual
    assert r"$\vert x\vert +\Vert y\Vert $" in actual
    assert r"\(\vert z\vert +\Vert w\Vert \), `$|code|$`" in actual
    assert actual.split("```text", 1)[1] == sample.split("```text", 1)[1]
    assert table_math_presentation(actual) == (actual, [])


def main() -> None:
    check_table_math_presentation()
    pinned = tree()
    verified: dict[str, dict] = {}

    def source(rel: str) -> tuple[bytes, dict]:
        if rel not in pinned:
            raise ValueError(f"Source absent from checkpoint {PIN}: {rel}")
        raw = (ROOT / rel).read_bytes()
        expected = git("cat-file", "blob", pinned[rel]["git_blob"])
        if raw != expected:
            raise ValueError(f"Working source differs from pinned Git blob: {rel}")
        record = {"path": rel, **pinned[rel], "sha256": digest(raw), "bytes": len(raw)}
        verified[rel] = record
        return raw, record

    _, helper_record = source("tools/build_handoff.py")
    selected = [rel for _, reports in GROUPS for rel in reports]
    if len(selected) != len(set(selected)):
        raise ValueError("Duplicate included report")
    expected_md = {
        rel for rel in pinned if any(rel.startswith(p) for p in SOURCE_PREFIXES)
        and rel.endswith(".md") and Path(rel).name != "README.md"
    }
    if expected_md - set(selected):
        raise ValueError(f"Uncovered substantive Markdown: {sorted(expected_md-set(selected))}")

    # Resolve only repository objects or known original staging paths. Unknown
    # references are preserved and disclosed, never guessed from a similar title.
    directories = {posixpath.dirname(rel) for rel in pinned}
    directories |= {"/".join(rel.split("/")[:i]) for rel in pinned for i in range(1, len(rel.split("/")))}
    link_dependencies: set[str] = set()
    unresolved = []

    def resolve_link(report: str, target: str) -> tuple[str | None, str]:
        target = target.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if target.startswith(("http:", "https:", "mailto:", "data:", "app:", "codex:")):
            return None, "external"
        if target.startswith("#"):
            return WEB + quote(report, safe="/") + target, "source_fragment"
        split = urlsplit(target)
        filepart = unquote(split.path)
        candidates = []
        if not filepart.startswith("/"):
            candidates.append(posixpath.normpath(posixpath.join(posixpath.dirname(report), filepart)))
        else:
            root_marker = "/Astra-Research/"
            if root_marker in filepart:
                candidates.append(filepart.split(root_marker, 1)[1])
            match = re.search(r"/research-round(\d+)/(.*)", filepart)
            if match:
                number, suffix = int(match[1]), match[2]
                if number == 6:
                    candidates.append("research/prime-gaps/round6/" + suffix)
                elif 7 <= number <= 14:
                    candidates.append(f"research/dyson/round{number}/" + suffix)
        for rel in candidates:
            if rel in pinned or rel in directories:
                if rel in pinned:
                    link_dependencies.add(rel)
                suffix = ("?" + split.query if split.query else "") + ("#" + split.fragment if split.fragment else "")
                urlbase = WEB if rel in pinned else WEB.replace("/blob/", "/tree/")
                return urlbase + quote(rel, safe="/") + suffix, rel
        return None, "unresolved"

    pattern = re.compile(r"(?P<image>!?)(?P<label>\[[^\]\n]*\])\((?P<target><[^>\n]+>|[^)\n]+)\)")

    def display_body(report: str, raw: str) -> tuple[str, list[dict], list[str], list[dict]]:
        rewrites = []
        lines = []
        fence = None
        table_safe, table_changes = table_math_presentation(raw)
        for line in table_safe.splitlines(keepends=True):
            marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
            if marker:
                if fence is None:
                    fence = marker[1][0]
                elif marker[1][0] == fence:
                    fence = None
                lines.append(line)
                continue
            if fence:
                lines.append(line)
                continue

            def replace(match):
                target = match["target"]
                updated, disposition = resolve_link(report, target)
                if disposition == "unresolved":
                    unresolved.append({"report": report, "target": target})
                if updated is None:
                    return match[0]
                if match["image"] and disposition in pinned:
                    updated = RAW_WEB + quote(disposition, safe="/")
                rewrites.append({"old": target, "new": updated, "resolved_path_or_kind": disposition})
                return match["image"] + match["label"] + "(" + updated + ")"

            lines.append(pattern.sub(replace, line))
        linked = "".join(lines)
        display = cleaned(linked)
        transformations = []
        if table_changes:
            transformations.append("Table rows only: equivalent inline-math bar spelling; every replacement recorded with original source position")
        if rewrites:
            transformations.append("Markdown links/images resolved to the exact source checkpoint outside code fences")
        if display != linked:
            transformations.append("Existing build_handoff.cleaned: nest headings and preserve recorded metadata/reference presentation")
        return display, rewrites, transformations, table_changes

    reports = []
    bodies = []
    toc = ["## Complete source texts / 完整原文目录", "", "| No. | Group | Source report |", "|---:|---|---|"]
    for group, members in GROUPS:
        for rel in members:
            raw_bytes, record = source(rel)
            raw = raw_bytes.decode("utf-8")
            display, rewrites, transformations, table_changes = display_body(rel, raw)
            number = len(reports) + 1
            first_title = re.search(r"^# +(.+)$", raw, flags=re.M)
            title = first_title[1] if first_title else Path(rel).stem
            anchor = f"report-{number:02d}"
            toc.append(f"| {number:02d} | {group.split(' — ')[0]} | [{title.replace('|', '/')}](#{anchor}) |")
            bodies.append(
                f'<a id="{anchor}"></a>\n\n# Current report {number:02d}: {title}\n\n'
                f"**Collection:** {group}.\n\n"
                f"**Source:** [{rel}]({WEB}{quote(rel, safe='/')}).\n\n"
                f"**SHA-256:** `{record['sha256']}`. **Git blob:** `{record['git_blob']}`. "
                f"**Original bytes:** {record['bytes']}.\n\n" + display
            )
            reports.append({
                "number": number, "group": group, "title": title, **record,
                "source_lines": len(raw.splitlines()), "full_text_included": True,
                "display_body_sha256": digest(display.encode()),
                "presentation_transformations": transformations, "link_rewrites": rewrites,
                "table_math_replacements": table_changes,
            })

    artifacts = set(selected) | link_dependencies
    artifacts |= {rel for rel in pinned if any(rel.startswith(prefix) for prefix in EVIDENCE_PREFIXES)}
    for snapshot in ("89393d5", "2073028"):
        manifest = f"fable/snapshots/{snapshot}/SOURCE_MANIFEST.json"
        if manifest in pinned:
            artifacts.add(manifest)
    for rel in sorted(artifacts):
        if rel not in verified:
            source(rel)

    front = FRONT.strip() + "\n\n" + "\n".join(toc)
    appendix = (
        "# Source index and artifact receipt\n\n"
        f"This supplement includes **{len(reports)} complete source reports**. "
        f"Its companion JSON index verifies **{len(artifacts)} associated repository objects** "
        "against the pinned Git tree. Code, arrays, logs, shorter READMEs and receipts are catalogued "
        "there without printing their complete machine data. The embedded proof/review text is not abridged.\n\n"
        f"Source checkpoint: `{PIN}`. Builder: `tools/build_round6_14_handoff.py`. "
        "Index: `docs/handoff/ROUNDS_6_14_ARCHIVE_INDEX.json`.\n\n"
        "The source reports and their earlier checks determine the scope of every mathematical claim. "
        "This assembly verifies preservation and provenance; it supplies no new mathematical experiment.\n"
    )
    assembled = "\n\n".join([front, *bodies, appendix]) + "\n"
    if any(ord(char) < 32 and char not in "\n\t\r" for char in assembled):
        raise ValueError("Unexpected control byte in assembled report")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(assembled)
    included = set(selected)
    index = {
        "title": "Astra Rounds 6–14 complete proof and research supplement",
        "source_commit": PIN, "repository": REPOSITORY,
        "assembly_date": "2026-09-05", "complete_report_count": len(reports),
        "source_policy": "Every source/artifact was byte-compared against the pinned Git blob; no source file edited.",
        "selection_policy": "All integrated R6–14 reports; every non-README Markdown in the round/review folders; R6 provenance retained; seven separate later Fable reviews; no duplicated Fable source snapshots.",
        "presentation_policy": "Existing cleaned helper, recorded link/image resolution, and recorded equivalent inline-math bar spelling on table rows only. Full proof/review bodies retained, including historical status and commands. No mathematical-content edits.",
        "builder": {"path": str(Path(__file__).relative_to(ROOT)), "sha256": digest(Path(__file__).read_bytes()), "new_derived_artifact_not_in_source_commit": True},
        "cleaned_helper": helper_record,
        "assembled_markdown": {"path": str(OUT.relative_to(ROOT)), "sha256": digest(assembled.encode()), "bytes": len(assembled.encode()), "lines": len(assembled.splitlines())},
        "reports": reports,
        "repository_artifacts": [
            {**verified[rel], "full_text_included": rel in included,
             "role": "complete report" if rel in included else "code/data/log/receipt/linked dependency; retained in repository"}
            for rel in sorted(artifacts)
        ],
        "unresolved_local_markdown_links_preserved": unresolved,
        "not_included_as_full_text": "Duplicate READMEs, arrays/code/log bodies, the complete duplicated Fable snapshots, earlier-round archive texts and locally retained third-party sources. Their paths/hashes remain in the repository and its receipts.",
        "validation": {"pinned_blob_comparison": "PASS", "substantive_markdown_coverage": "PASS", "duplicate_sources": "none", "table_math_repair_unit_checks": "PASS: table headers/rows, both math delimiters, single/double bars, code protection, non-table preservation, idempotence", "source_report_mutations": "none", "mathematical_experiments_run": "none"},
    }
    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "source_commit": PIN, "reports": len(reports), "verified_artifacts": len(artifacts),
        "bytes": OUT.stat().st_size, "lines": len(assembled.splitlines()),
        "unresolved_local_links": len(unresolved), "output": str(OUT),
        "table_math_replacements": sum(len(r["table_math_replacements"]) for r in reports),
        "output_sha256": index["assembled_markdown"]["sha256"],
    }, indent=2))


if __name__ == "__main__":
    main()
