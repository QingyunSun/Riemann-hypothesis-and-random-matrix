# Round 10: a power saving for one actual shifted-prime discrepancy

Date: 2026-09-05. **This round proves an unconditional bound for a specified smooth packet of the actual arithmetic discrepancy. It does not prove a new zeta pair-correlation lower bound.** The accompanying source audit explains why two tempting short-interval inputs do not supply the missing precision.

## The bound and how far it remains from the target

Use the complementary squarefree modulus family Q_X from Round 9, with q<=Q=X^.523. Let X=T^alpha, 6/5<=alpha<=7/5, and H=X/T. The discrepancy D_Q^V uses the actual localized prime-covariance sinc kernel, its Mobius–log divisor coefficient, its coprime principal term, and a fixed smooth cutoff V(h/H), supported in 1<h/H<2.

The [complete ordinary proof](../dyson/round10/shift-average/SMOOTH_SHIFT_COMPLETION_BOUND.md) gives

\[
\boxed{|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{HX(X+Q^2)}\,(\log X)^4.}
\tag{1}
\]

The estimate itself is unconditional. RH is used only when inserting it into the earlier actual-zeta correspondence. The proof works for any squarefree modulus subset with this cap; it does not yet exploit triple dense divisibility beyond the selection of the prescribed family. No novelty claim is made for its elementary completion and spacing ingredients.

For H=X^theta, the new exponent is 1.023+theta/2. The previous per-shift estimate, summed by the triangle inequality, had exponent 1+theta with any fixed logarithmic saving.

| H exponent | Previous triangle exponent | New smooth-packet exponent | Power saved, before logarithms |
|---|---:|---:|---:|
| 1/6 | 7/6 | 3319/3000 | 181/3000 = 0.060333... |
| 2/7 | 9/7 | 8161/7000 | 839/7000 = 0.119857... |

This is a power improvement in a genuine arithmetic error bound. Nevertheless, after division by the required X log X fluctuation scale, the estimate still grows as X^.023 sqrt(H) log³X. It does not evaluate this selected component at the precision needed for the compact Fourier test. The whole unsmoothed shift range, complementary divisor remainder, support main terms and continuous centering also remain unresolved.

## Why completing the shift sum helps

First remove prime powers from both terms of the progression discrepancy. Their total contribution is O_eta(H X^(.5+eta) log³X+H sqrt(X) log⁴X), which is o(X log X) for eta=.01 and the stated H range. Every remaining prime exceeds every modulus, so it is a unit modulo each q. This permits exact finite Fourier completion while retaining the principal unit sum.

For a separated amplitude f(p/X)v(h/H), define

\[
S_v(\beta)=\sum_hv(h/H)e(-\beta h),\qquad
A_f(\beta)=\sum_p(\log p)f(p/X)e(\beta p).
\]

Combining repeated rational frequencies before estimating gives the exact pairing

\[
\sum_{d,a}^{*} S_v(a/d)
\left(\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q\right)
\left(A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)\right).
\tag{2}
\]

The star means 2<=d<=Q, 1<=a<d and (a,d)=1. The zero frequency cancels. The principal coefficient mu(d)/phi(d) follows from the exact Ramanujan ratio and is independent of the parent modulus q. Treating all original fractions r/q as distinct would invalidate the subsequent spacing estimate.

The squared norm of the first two factors in (2) is O(H log³Q), or O(H log⁵Q) when a log q coefficient is present. A direct Schur/spacing argument bounds the centered prime sums' squared norm by O(X(X+Q²) log²X). The proof retains the logarithm in the elementary spacing bound. Cauchy–Schwarz then yields (1), after including the logarithmic cofactor.

The original two-variable sinc kernel is not simply replaced by a separated model. With y=m/X, z=h/H and epsilon=H/X=1/T, its phase is

\[
\epsilon^{-1}\log\frac y{y-\epsilon z}
=\int_0^z\frac{du}{y-\epsilon u}.
\]

It and its derivatives are uniformly smooth on the fixed support. A Fourier expansion with uniformly summable derivative-weighted coefficients transfers the separated estimate to the actual kernel, including log(y-epsilon z). The fixed support also keeps both cutoff factors on their correct branch.

Separate reviews cover the [coefficients and spacing](../dyson/round10/shift-average/COEFFICIENT_AND_SPACING_AUDIT.md) and the [actual kernel/prime-power passage](../dyson/round10/shift-average/ACTUAL_KERNEL_AND_PRIME_POWER_REVIEW.md). The root additionally read the complete author argument. The accepted scope is the explicitly defined smooth packet. A possible bounded-variation extension in a review is not silently promoted to a theorem for the full sharp packet.

## What the checked prime-variance sources do not give

The [arithmetic source audit](../dyson/round10/arithmetic-residual/ARITHMETIC_RANGE_AND_MIXED_MOMENT.md), with [independent review](../dyson/round10/arithmetic-residual/INDEPENDENT_REVIEW.md), examines the edge shell X=T^(1+s/b), 1<=s<=2, h=X/T. Its interval-length exponent is s/(b+s), tending to zero.

[Guth–Maynard, arXiv:2405.20552v2](https://arxiv.org/html/2405.20552v2), Corollary 1.4, gives almost-all prime-count asymptotics for h>=X^(2/15+epsilon), with fixed epsilon. Even the corollary's epsilon-zero endpoint misses the whole shell once b>13. The subsequent Remark discusses a slight fixed-epsilon improvement with a worse error; it still does not cover an exponent tending to zero.

Inside the stated range, a direct conversion of the count theorem and its exceptional-set bound gives an error in the squared count far above the fluctuation scale X h log(X/h). Almost-all PNT is therefore not itself a constant-precision variance theorem. The audit does not rule out stronger uses of the underlying methods.

The checked [Carneiro–Chandee–Chirre–Milinovich short-interval comparisons](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf) retain fixed factors approximately 0.9028 and 1.0736, and fixed-endpoint quantifiers. These do not supply the shrinking first correction required by the mesoscopic test. The large-beta statements in that source use beta as the endpoint of the prime range, not the damping b.

## One precise remaining arithmetic mixed moment

Let R_b be the genuine-prime residual at displacement b/(2 log T), with the same cutoff N=floor(T/log^6 T), and put

\[
E_T(b)=\frac{e^b\|R_b\|_2^2}{T\log^2T},\quad
K_b=-R_b-2\partial_bR_b,\quad
M_T(b)=\frac{e^b\operatorname{Re}\langle R_b,K_b\rangle}{T\log^2T}.
\]

Exactly M_T=-E_T'. In the absolutely convergent region, K gives the genuine-prime weight log(p)/log(T)-1; the working-strip object is its centered analytic continuation. Differentiating an unspecified asymptotic error is not part of the argument.

For some fixed epsilon>0, an actual uniform bound

\[
M_T(s)\ge s^{-2}-(2-\epsilon)s^{-3}+o(s^{-3})
\tag{3}
\]

through twice a suitable slow envelope would imply that the Round 9 coupled statistic has lower limit at least -3/4+3epsilon/8, with the required uniform quantifiers. This would contradict AH-Pairs under RH. The implication follows by integrating from b to 2b; the correction integral is exactly 3/(8b²). Reviewed RH upper estimates control the small exponential terms.

**Inequality (3) is not proved.** This formulation identifies one signed, logarithmically weighted genuine-prime correlation; it is not a substitute for estimating it. Neither source checked here supplies a positive epsilon.

## Verification and next mathematical decision

The finite script checks 9,615 exact Ramanujan-ratio cases, reduced-frequency grouping with formal log q coefficients, zero-frequency cancellation and both endpoint exponents. A second exact script checks the prime-range thresholds and mixed-moment normalization. These checks validate algebra; the power bound rests on the written analytic proof and independent reviews.

All 15 original files (1,452,061 bytes) are preserved in the adjacent local `Astra-Local-Archive/round10-originals/`; 14 research files are verbatim public. The third-party Guth–Maynard HTML body stays local, identified by URL/hash. Earlier primary references remain in their pinned local folders. The [intake manifest](../dyson/round10/INTAKE_MANIFEST.json) and [integration replay](../logs/round10-integration/recheck.json) record their exact scope. Both output JSON files reproduce in a separate process. The mixed-moment JSON is identical in full; the completion output differs only in two temporary provenance paths, with source hashes still checked. No new floating optimization, prime-gap sweep, or zeta-data fit was run.

From the repository root, with Python and SymPy:

```text
python3 research/logs/round10-integration/recheck.py --prime-gap-source-dir /path/to/retained/round9-external-sources
python3 tools/verify_manifest.py
```

The next useful arithmetic work is an estimate for the pairing (2) that uses the selected Mobius coefficients together with the centered prime exponential sums, beyond separate norm bounds. A separate possibility is an averaged version of (3) with a strict quantitative gain. Repeating the same completion with different notation or improving only its logarithmic exponent would not close the existing power gap.

The large handoff PDFs retain their stated earlier checkpoints; this compact report is an additional source record. The goal remains active. Reverting this research slice removes its reports and rechecks without altering earlier proofs. New model sessions, generic positivity scans and claims of a solved famous conjecture are outside this checkpoint.
