# Round 15: an exact signed arithmetic target and a legal pole-canceling packet

Date: 2026-09-05. The first result identifies the precise Möbius–von Mangoldt bilinear form left after the actual Type I removal, and verifies a genuine untwisted distribution property of its second coefficient. The second constructs a nonnegative time weight that exactly cancels the actual zeta pole in a linear logarithmic-derivative pairing. Both have complete proofs, independent reviews, root review and bounded replays. Neither improves the current full-discrepancy bound or proves an actual-zeta conjecture.

## 1. The arithmetic remainder now has explicit coefficients

Keep the original smooth discrepancy, including Q=X^.523, the full sinc/log-cofactor kernel, the smooth shift range H in [X^(1/6),X^(2/7)], signed Möbius modulus weights and the same primitive principal subtraction. Define

\[
\beta_B(m)=\sum_{d\mid m,\ d>B}\Lambda(d),\qquad
R_{A,B}=\mu_{>A}*\beta_B.
\]

The exact Vaughan identity and a second smooth-cofactor Poisson estimate give

\[
\mathcal D[\Lambda]=\mathcal D[R_{A,B}]
+O_J\left(HX(ABQ/X)^J\log^2X\right),
\quad ABQ\le X/2.
\]

The same explicit form replaces R14's divisor-cutoff remainder with its separately stated small error. For A=B=X^(1/5) and J=4, the error is O(X^(1711/1750)log²X), below X log X. Thus a uniform o(X) estimate for each of the O(log X) surviving dyadic bilinear blocks would suffice for the selected discrepancy at its target scale. That block estimate is unproved.

The coefficient satisfies 0<=beta_B(m)<=log m and, when B is at least a fixed positive power of X, the full untwisted Siegel–Walfisz condition with arbitrary auxiliary coprimality modulus and fixed divisor exponent one. The proof opens actual prime divisors, uses the primary prime-interval theorem, sums the cofactor harmonically and removes the remaining prime powers with an explicit negligible bound. It is not a blanket assertion that convolutions inherit distribution.

There are two essential limitations. First, the actual coefficient R remains signed: legal-support integer witnesses give both signs, and R vanishes on primes. Second, the source's admissible short-factor scales are only [X^.399,X^.5] at the fixed checked parameters. Asymmetric cutoffs can remove one short-factor corner, but leave a larger unbalanced corner; a factor swap is not assumed. The cutoff budget below .477 cannot force both factors above the limiting edge .398. Even on legitimate blocks, a per-shift logarithmic saving does not remove the polynomial H summation loss.

The full RH discrepancy bound remains O(X^1.023 log^5 X). The new result fixes a concrete signed analytic obligation; it is not an improvement of that bound or of W_T.

Full evidence: [author proof](../dyson/round15/signed-arithmetic/VAUGHAN_SIGNED_REMAINDER.md), [independent review](../dyson/round15/signed-arithmetic-review/INDEPENDENT_VAUGHAN_REVIEW.md), [root review](../dyson/round15/root-review/ROOT_VAUGHAN_REVIEW.md), and the adjacent exact script/JSON.

## 2. A nonnegative time packet can cancel the actual simple pole

For 1/2<sigma<1, a=1-sigma and W>0, define

\[
w_{\sigma,W}(t)=\frac{t^2+a^2}{W^2}e^{-t^2/(2W^2)}.
\]

It is strictly positive for real t and vanishes at t=±ia. Under RH a one-factor contour shift proves, for actual H=-zeta'/zeta,

\[
\int_{\mathbb R}H(\sigma+it)X^{it}w_{\sigma,W}(t)dt
=\sum_{n\ge2}\Lambda(n)n^{-\sigma}K_{\sigma,W}(\log(n/X)),
\]
\[
K_{\sigma,W}(\lambda)=\sqrt{2\pi}W
\left[1+\frac{a^2}{W^2}-W^2\lambda^2\right]
e^{-W^2\lambda^2/2}.
\]

The usual pole residue is exactly zero. The prime-side series is absolutely convergent, but its Fourier kernel has a leading negative part. The continuous-density integral is exactly zero through equal positive and negative masses, each asymptotic to 2sqrt(2pi/e) X^(1-sigma). Those continuum masses are not asserted to be prime short-interval asymptotics.

Using E=psi-x, the actual expression equals -integral E f'. All zero/infinity and finite-window endpoint conventions are retained. A convenient global Schoenfeld-based RH estimate yields the explicit bound

\[
|M_{\sigma,W}(X)|\le10800\,W X^{1/2-\sigma}(1+\log X)^2
\]

for 1/2<sigma<=3/4, W>=1 and X>=2. The report also gives a Gaussian centered-tail bound; the independent review adds an explicit bound for the finite-window Ef terms. This is useful convergence control, not a sharp signed lower bound.

The nonnegative time measure supplies a valid full Gram matrix and projection inequality, despite signed Fourier entries. Plancherel supplies an exact positive arithmetic energy with weight w². It does not replace w² by w or by the original sharp interval. A derivative of the parameter-dependent weight produces an extra term, and its simple zeros do not cancel double poles. No reflected-H contour is used.

Full evidence: [author proof](../dyson/round15/dyson-bridge/POLE_ANNIHILATING_PACKET.md), [independent review](../dyson/round15/pole-packet-review/INDEPENDENT_POLE_PACKET_REVIEW.md), [root review](../dyson/round15/root-review/ROOT_POLE_PACKET_REVIEW.md), and the bounded check script.

## 3. Exact checks, archive and next research test

The arithmetic check uses formal symbols for log p and exact rational cutoffs: 49,152 identities through n=4096, independent grouping of the bilinear coefficient, prime-input zeros, two opposite-sign actual support witnesses and all source parameter inequalities pass. The packet check verifies exact rational constants and high-precision Fourier, mass and finite Dirichlet-polynomial identities. The floating quadratures are labelled diagnostics, not interval certificates or observations of the true large-height zeta statistic. Both complete output JSON files replay byte for byte, with no excluded fields.

All originals are retained in the adjacent local `round15-originals` folder. The [intake manifest](../dyson/round15/INTAKE_MANIFEST.json) records two public omissions that are merely duplicate copies of an author's report and script in an independent replay directory. Every published source is verbatim. The [integration receipt](../logs/round15-integration/INTEGRATION_RECEIPT.json) records the bounded replays. No new third-party model session was invoked.

The next analytic work is an aggregate estimate using actual Möbius coefficients and the proved beta_B property, or a weighted covariance identity that makes the new packet useful for a sufficient zeta inequality. A separate R16 attempt examines AH's forced spectral atom at frequency two and an exactly finite compact arithmetic packet; their eventual results require their own reviews. The complete 705/753-page handoff stays pinned through Round 14, with this smaller report serving as the later update.

Postponed: broad prime-gap scans, another large PDF rebuild, a factor swap or phase-twisted SW premise without proof, and any conjecture/novelty claim from a component identity. The main risk is losing signed terms or source ranges during a subsequent application. Reverting this checkpoint removes the new slice without altering the archived sources or earlier proofs.
