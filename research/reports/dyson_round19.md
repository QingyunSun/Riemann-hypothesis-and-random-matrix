# Round 19: a positive prime-variance test and a uniform finite heat-flow theorem

Date: 2026-09-05. The programme now has a positive arithmetic statistic with an exact AH prediction and a finite ACUE heat theorem valid on a time interval independent of matrix size. Both have complete ordinary proofs and independent reviews. The missing strict inequality for actual primes remains unproved; the finite heat theorem supplies no initial-zeta transfer. No RH, GUE, AH-refutation, zeta-gap or sub-186 theorem is claimed.

## 1. A concrete positive arithmetic target

Assume RH. Retain the fixed smooth autocorrelation bump \(\psi\) from Round 16, with \(\psi(0)=1\), support \([-1,1]\), and both \(\psi\) and its Fourier transform nonnegative. Put
\[
m_0=\int\psi(u)\,du,\qquad m_1=\int |u|\psi(u)\,du,
\quad \omega(\alpha)=\psi((\alpha-2)/\varepsilon),
\quad A_\varepsilon=1+\varepsilon^2m_1.
\]
Here \(0<\varepsilon<1\) is fixed. The principal concrete choice is \(\varepsilon=1/4\). Let \(\Psi(x)=\sum_{n\le x}\Lambda(n)\), and define
\[
\Delta_T(x)=\Psi((1+1/T)x)-\Psi(x)-x/T,
\]
\[
\boxed{V_{\varepsilon,T}=\frac{T}{\log^2T}
\int_1^\infty\Delta_T(x)^2
\omega\!\left(\frac{\log x}{\log T}\right)\frac{dx}{x^2}.}
\]
This is a nonnegative, completely centered prime-power variance. The prime variable ranges over the logarithmic window \(T^{2-\varepsilon}\le x\le T^{2+\varepsilon}\), not a constant-factor window about \(T^2\). Its interval length is \(x/T\), including the square-root length at the central scale.

Write \(D_T=C_{\varepsilon,T}(0)-C_{\varepsilon,T}(2)\ge0\) for the exact Round 16 actual-zeta Bragg deficit. The proved implications are
\[
\mathrm{RH+AH\text{-}Pairs}\quad\Longrightarrow\quad
V_{\varepsilon,T}\longrightarrow A_\varepsilon,
\]
\[
\boxed{\liminf_{T\to\infty}V_{\varepsilon,T}<A_\varepsilon
\quad\Longrightarrow\quad\limsup_{T\to\infty}D_T>0.}
\]
The latter implication would exclude full AH-Pairs under RH. It does not require that the two deficits occur along the same subsequence, and it does not identify the two statistics at the same height. A proof of \(\liminf V_{1/4,T}\le1\) would suffice. No such bound has been proved here.

The [full variance proof](../dyson/round19/bragg-variance-literature/BRAGG_WEIGHTED_SELBERG_VARIANCE.md), [independent review](../dyson/round19/bragg-variance-review/INDEPENDENT_WEIGHTED_VARIANCE_REVIEW.md), and [root review](../dyson/round19/root-review/ROOT_VARIANCE_REVIEW.md) retain all constants and the order of limits.

## 2. Why the variance implication is valid

The primary CCCC weighted Plancherel identity expresses this prime variance through a nonnegative squared zero-sum signal. Its prefix integral satisfies
\[
K_T(Y)=2Y C_Y+o(Y)
\]
uniformly on \(T/\log^3T\le Y\le T\log^3T\). The rescaled time kernel is
\[
k(y)=\frac{\sin^2(y/2)}{y^2},\qquad
\int_0^\infty k(y)\,dy=\frac\pi4.
\]
The source prefactor and the two squared zero sums give exactly the AH value above. Small-height and remote-height tails are bounded separately. No infinite-interval weak-convergence assertion replaces those estimates.

For \(d=\limsup D_T\) and \(v_* =\liminf V_{\varepsilon,T}\), the proof gives, for every fixed \(R\ge1\),
\[
A_\varepsilon-v_*
\le\frac{4A_\varepsilon}{\pi R}
+\frac{4d}{\pi}\left(3+R^{-1}+\tfrac12\log R\right).
\]
This supplies an explicit positive lower bound on \(d\) conditional on a positive variance deficit. The finite cutoff matters: the absolute derivative envelope of the sinc-square kernel is not integrable over the full half-line.

The exact bump is approximated by smooth squares on one fixed compact subinterval of \((1,3)\). At a fixed cutoff, the finite integration-by-parts formula is first applied to an approximation. The compact spectral and positive variance mass bounds then control replacement by the original bump. Height limits precede removal of the approximation error; the cutoff is removed last. This does not assume that each approximant has its own full spectral limit merely because the original bump does. The independent review makes this point explicit.

## 3. A finite nonnegative prime-pair kernel with all centers

Put \(q_T=1+1/T\) and \(W_T(x)=\omega(\log x/\log T)\). Define
\[
B_T(m,n)=\frac{T}{\log^2T}
\int_{\max(m,n)/q_T}^{\min(m,n)}W_T(x)\frac{dx}{x^2},
\]
with zero value for an empty interval, and
\[
L_T(n)=\frac1{\log^2T}\int_{n/q_T}^{n}W_T(x)\frac{dx}{x},
\qquad M_T=\frac1{T\log^2T}\int W_T(x)\,dx.
\]
Then the exact finite expansion is
\[
V_{\varepsilon,T}=\sum_n\Lambda(n)^2B_T(n,n)
+2\sum_{m<n}\Lambda(m)\Lambda(n)B_T(m,n)
-2\sum_n\Lambda(n)L_T(n)+M_T.
\]
The kernel \(B_T\) is nonnegative and its off-diagonal support has \(n/m<1+1/T\). The prime powers and both continuous-centering terms are retained. The diagonal tends to \(2\varepsilon m_0\). Thus a sufficient assertion for the combined remaining terms \(E_T^{\mathrm{SI}}\) is
\[
\liminf E_T^{\mathrm{SI}}
<1+\varepsilon^2m_1-2\varepsilon m_0.
\]
At \(\varepsilon=1/4\), the inherited diagnostic constants give approximately \(A_\varepsilon=1.01059\) and remaining-term threshold \(0.64028\). The sine prediction for the whole variance is approximately \(0.18515\). These are conditional predictions and evaluations of formulas, not measurements of high zeros or a numerical proof about primes.

One stronger sufficient local premise is a single-log variance bound, uniform over fixed multiplicative cells in the full required power window. A coefficient \(B<A_\varepsilon/(\varepsilon m_0)\), approximately \(5.458\) at the selected epsilon, would suffice. Ordinary RH's extra-log estimate does not supply any fixed such coefficient.

The bounded primary-source audit distinguishes narrow fixed windows from long frequency averages. The recent 1.3208-type long-average constants retain a lower bound on interval length; they cannot be multiplied by the width of this bump. Other cited results retain additional pair-correlation hypotheses or ranges such as \(x<T\). The current CCCC upper transfer yields \(L^+A_\varepsilon\), with \(L^+\approx1.0736\), which still exceeds the AH prediction. The full source restrictions and coordinator range guards are preserved.

## 4. A finite ACUE theorem at a time independent of N

On a circle of circumference \(N\), start with the rank-\(N\) ACUE determinantal process on the \(2N\) half-grid sites. Evolve by deterministic repulsive scalar heat,
\[
q_i'(s)=\sum_{j\ne i}\frac{2\pi}{N}
\cot\frac{\pi(q_i-q_j)}N,
\qquad s=\frac{N^2t}{4\pi^2}.
\]
This is not stochastic Dyson Brownian motion. Periodize the Round 16 spatial kernel:
\[
k_{\varepsilon,N}(u)=\sum_{\ell\in\mathbb Z}
\varepsilon\widehat\psi(\varepsilon(u+\ell N)),
\]
\[
D_{\varepsilon,N}(q)=\frac1N\sum_{i,j}
k_{\varepsilon,N}(q_i-q_j)
\bigl(1-\cos(4\pi(q_i-q_j))\bigr).
\]
Fix \(\varepsilon=1/4\) and
\[
\kappa_\varepsilon=\varepsilon m_0\cos^2(3\pi\varepsilon/4)>0.
\]
The complete ordinary theorem is
\[
D_{\varepsilon,N}(q(0))=0,
\qquad
\boxed{\mathbb E D_{\varepsilon,N}(q(s))
\ge\frac{\kappa_\varepsilon}{3528}s^2}
\]
for every \(N\ge8\) and every \(0<s\le\frac{1}{4\,128\,768}\). The lower bound and allowed time interval are independent of \(N\).

The proof preserves the minimum cyclic gap \(1/2\) by cooperative ODE comparison. A logarithmic relative-velocity estimate gives the uniform acceleration bound \(|q_i''|<12160<12288\). The determinantal two-point formula and a sixteen-site variance estimate give a positive density of occupied adjacent bonds with a nearby hole. Their gaps open at speed at least \(1/84\), remain below \(3/4\) for the stated time, and contribute a positive amount to the kernel. The proof explicitly counts both orientations and includes circular seam cases.

This is a finite-time theorem, not an inference from an initial derivative. Read the [full proof](../dyson/round19/dynamic-observability/LOCAL_BRAGG_PRODUCTION.md), [independent review](../dyson/round19/dynamic-observability-review/INDEPENDENT_LOCAL_BRAGG_REVIEW.md), and [root review](../dyson/round19/root-review/ROOT_DYNAMIC_REVIEW.md). All 168 mathematical expressions pass the author's KaTeX syntax check; this is separate from proof validation.

## 5. An exact curvature check and the actual-zeta limitation

A separate root proof evaluates the global coherent mode
\[
\mathcal B_N(s)=N^{-2}\left|\sum_j e^{4\pi i q_j(s)}\right|^2.
\]
It gives the exact finite-\(N\) identity
\[
\mathbb E_{\mathrm{ACUE}}\mathcal B_N''(0)
=-\frac{64\pi^4}{3}(1-N^{-2}).
\]
The force-energy expectation is independently recovered from the ACUE projection kernel and elementary cotangent sums. This checks the microscopic normalization. Its fixed-\(N\) Taylor expansion has no asserted uniform remainder and does not replace the localized theorem's acceleration argument. Both [the derivation](../dyson/round19/root-bragg-curvature/EXACT_COHERENT_MODE_CURVATURE.md) and [its independent review](../dyson/round19/root-bragg-curvature/INDEPENDENT_CURVATURE_REVIEW.md) are preserved.

The finite model breaks exact half-lattice phase saturation while preserving its half-unit hard core. It therefore rules out a generic assertion that a positive-time deficit is bounded by a constant times the initial deficit plus an error tending to zero in \(N\), under only the listed model assumptions. AH-Pairs does not identify the actual local law as ACUE and permits clusters or multiplicities. Applying the finite theorem to true \(H_t\) requires an additional trajectory/background comparison and an arithmetic estimate connecting positive time to the initial zero statistic. A generic \(O(s)\) error cannot establish a signal of order \(s^2\). None of those missing actual-zeta inputs is supplied here.

## 6. The shift-dispersion trial keeps its original normalization

The separate arithmetic route starts from the actual canonical moduli \(q\asymp Q=X^{.523}\), after the exact Round 18 inverse has restored \(\mu(q)(\log q)^j\). A short primitive-residue packet has exact projected squared norm
\[
\sum_{(h,q)=1}|V(h/H)|^2
-\frac{|\sum_{(h,q)=1}V(h/H)|^2}{\varphi(q)}.
\]
On the admitted real-prime terminal family this is asymptotic to \(H\int|V|^2\). Complete-residue variance therefore supplies no automatic \(H/Q\) saving. Even a hypothetical full variance \(XQ\) up to logarithms gives a weaker power than the current RH bound.

A new localized variance bound \(\sum_{q,h}|\Delta_q(h)|^2\ll HX\) up to logarithms would yield \(H\sqrt{XQ}\). It would cover \(H\le X^{477/2000-\eta}\), equivalently the older compact-test range \(\alpha<2000/1523\), with a fixed margin. The premise is unproved and this range does not reach the frequency-two Bragg window.

Maynard's weaker variable-residue theorem admits one explicit allocation of 28 small prime factors on the terminal family, but its output still carries the shift-length cost. The full logarithmic packet additionally retains \((\log X)^j\). Keeping the physical shifts inside Cauchy–Schwarz creates the exact CRT condition
\[
h_1n_2\equiv h_2n_1\pmod q,
\]
with switched scale \(HN/q\). It cannot be replaced by the fixed-residue condition \(n_1\equiv n_2\pmod q\). The Fourier-dual variable introduced by completion is different from the physical shift. Legal factor-size margins alone do not estimate this joint centered kernel.

The [final author proof](../dyson/round19/shift-dispersion/SHORT_RESIDUE_DISPERSION_TEST.md), [full root review](../dyson/round19/shift-dispersion-review/ROOT_SHIFT_DISPERSION_REVIEW.md), and [final logarithmic clarification receipt](../dyson/round19/shift-dispersion-review/final-log-clarification/ROOT_DELTA_REPLAY_RECEIPT.json) preserve the complete argument and source ranges. The inherited full bound remains \(O(X^{1.023}\log^5X)\) under RH.

## 7. Validation, provenance and next work

The bounded exact interval checker evaluates the complete variance kernel in two independent ways, once with actual prime-power logarithms and once with signed rational coefficients. All means and endpoints agree symbolically. Its full output and stdout replay identically. The shift checker passes 576 CRT cases, 60,480 complete centered-product identities, three sharp projection norms and all rational exponent margins; its final complete replay also matches. The finite ACUE diagnostic enumerates all 12,870 subsets at \(N=8\), with 48,048 good-pair checks, and independently replays byte for byte. Its floating values are diagnostics; exact rational checks and ordinary proofs are distinct evidence.

Author source files remain verbatim. Historical variance/shift review pins and their final deltas remain separate, as do the pre-clarification shift outputs. The [intake manifest](../dyson/round19/INTAKE_MANIFEST.json) records all originals and local-only primary paper bodies/page images. The integrated links above use public repository paths; archived authors' source-relative links refer to their original staging layout and are indexed separately. The existing 705-page public and 753-page local complete PDFs keep their explicit through-Round-14 checkpoint.

The implementation remains a small research archive slice: ordinary proofs, bounded Python checks, source receipts and a syntax check. There is no new performance claim requiring a benchmark, model service or Rust subsystem. A checkpoint can be reverted independently without rewriting earlier sources.

Two next bounded investigations are active: actual-prime evaluation of this positive variance at only three stated finite heights, retaining every prime power and center; and an exponential interval-length average intended to replace the oscillatory transfer kernel by a decreasing one. A separate height-regularity lemma is being challenged. These are ongoing tests, not accepted results of this checkpoint. Optimizing the tiny finite-flow constants, enlarging numerical scans and claiming a famous-conjecture solution are postponed. The immediate unresolved objective remains a strict actual-prime inequality sufficient for the initial-zeta Bragg deficit.
