# Round 21: exact arithmetic and heat targets for one zeta-correlation deficit

Date: 2026-09-05. This checkpoint develops four ordinary mathematical results around the actual positive length-averaged prime variance introduced in Round 20. It supplies an absolutely convergent arithmetic kernel with a finite truncation bound, a full-height fixed-test Tauberian equivalence, a localized heat-energy representation of the actual prime error, and a centered prime-pair remainder whose strict upper bound would exclude AH-Pairs. The required strict upper bound remains unproved.

A coordinator review also found a substantive obstruction in one proposed route: a uniform sub-square-root estimate for every centered shift is impossible already at shift one. The author revision and independent review preserve that correction explicitly. The signed weighted target survives. None of these results proves RH, the GUE conjecture for zeta zeros, the full Montgomery pair-correlation conjecture, a new zero-gap bound, or a prime-gap improvement below 186. No global novelty claim is made for the identities or the classical obstruction.

## 1. One fixed actual object, with all centers retained

Keep precisely the fixed nonnegative autocorrelation bump from [Round 20](dyson_round20.md):
\[
\varepsilon=\tfrac14,\qquad
\omega(\alpha)=\psi((\alpha-2)/\varepsilon),\qquad
a=\tfrac74,\quad b=\tfrac94.
\]
Its support is \([a,b]\), its height is at most one, and
\[
M=\int_{\mathbb R}\omega(\alpha)\,d\alpha
=\varepsilon\int_{\mathbb R}\psi(v)\,dv,\qquad
A=1+\varepsilon^2\int_{\mathbb R}|v|\psi(v)\,dv.
\]
The inherited finite quadrature diagnostics give \(M\approx0.1851531433\) and \(A\approx1.0105877964\). Those decimals are descriptive approximations to the exact integrals, not new certified interval computations.

Let \(\Lambda(n)\) denote the von Mangoldt function, with every prime power retained, and put
\[
\Psi(x)=\sum_{n\le x}\Lambda(n),\qquad E(x)=\Psi(x)-x,
\qquad W_T(x)=\omega(\log x/\log T).
\]
The statistic is
\[
\overline V_T=\frac{T}{\log^2T}\int_1^\infty
W_T(x)\frac{dx}{x^2}
\int_0^\infty e^{-\lambda}
[E(xe^{\lambda/T})-E(x)]^2\,d\lambda.
\tag{1}
\]
The prime coordinate ranges from \(L_T=T^{7/4}\) to \(U_T=T^{9/4}\). The length parameter runs over its full positive range. Continuous subtraction is exact.

Round 20 proves under RH that
\[
\overline V_T=\int_0^\infty
\frac{4y^2}{\pi(1+y^2)^2}C_{Ty}\,dy+o(1),\qquad
C_{0,T}\longrightarrow A,\qquad D_T=C_{0,T}-C_T\ge0,
\tag{2}
\]
and
\[
\liminf_T\overline V_T<A
\quad\Longleftrightarrow\quad
\limsup_TD_T>0.
\tag{3}
\]
Here \(C_T\) is the fixed bump centered at spectral frequency two in the actual finite zeta-pair measure. Either strict statement excludes the precise full AH-Pairs hypothesis. Failure of AH-Pairs is not proved to imply a deficit for this particular bump. This logical distinction remains in force throughout this checkpoint.

## 2. Exact all-length arithmetic kernel and a finite positive truncation

Define
\[
F_T(x)=T x^T\int_x^\infty [E(y)-E(x)]^2y^{-T-1}\,dy.
\]
The substitution \(y=xe^{\lambda/T}\) makes (1) exactly
\[
\overline V_T=\frac{T}{\log^2T}
\int_{L_T}^{U_T}W_T(x)x^{-2}F_T(x)\,dx.
\]
For every real \(T>2\), without RH, the following three expanded terms converge absolutely:
\[
\begin{aligned}
F_T(x)
={}&\sum_{m,n>x}\Lambda(m)\Lambda(n)
\left(\frac{x}{\max(m,n)}\right)^T\\
&-2x\sum_{n>x}\Lambda(n)
\left[\frac{T}{T-1}\left(\frac xn\right)^{T-1}
-\left(\frac xn\right)^T\right]
+\frac{2x^2}{(T-1)(T-2)}.
\end{aligned}
\tag{4}
\]
The two mixed terms and the continuous square are essential. Dropping them changes a centered variance into a different large positive quantity. The full proof justifies expansion using \(\Psi(y)\le y\log y\) and absolute total-variation estimates.

With
\[
J_s(z)=\int_{L_T}^{\min(U_T,z)}
W_T(x)x^{s-2}\,dx,
\]
where the integral is zero when \(z\le L_T\), the pair part after the outer integration has coefficient
\[
\frac{J_T(\min(m,n))}{\max(m,n)^T}.
\]
The author gives the complete mixed and continuous coefficients and an equivalent single-index formula. Thus the full arithmetic object can be evaluated using finite Mellin integrals once its tail is controlled.

For \(N\ge U_T\), define the genuinely positive truncation
\[
F_{T,N}(x)=T x^T\int_x^N[E(y)-E(x)]^2y^{-T-1}\,dy
\]
and define \(\overline V_{T,N}\) by the same outer integral. This truncates the positive integral itself. Each resulting finite prime-pair, mixed and continuous coefficient includes its endpoint correction. In particular, the pair survival factor becomes
\[
\left(\frac{x}{\max(m,n)}\right)^T-\left(\frac xN\right)^T.
\]
It would be incorrect to obtain this finite object by merely discarding the large indices in (4).

The complete explicit tail estimate yields the unconditional bound
\[
\boxed{
0\le\overline V_T-\overline V_{T,N}
\le2048\,T^{9/4}2^{-T},
\qquad T\ge3,\quad N=\lceil2T^{9/4}\rceil.
}
\tag{5}
\]
The proof first uses the integral tail at \(2U_T\); rounding its endpoint upward can only decrease the remainder. Every strict limiting target in (3) can therefore be formulated using this finite positive functional. Equation (5) controls the mathematical truncation, not floating-point evaluation of its highly canceling expanded terms.

The endpoint \(T=2\) is handled separately. Under RH the centered integral converges, although the separated positive infinite pieces in (4) diverge. Finite Stieltjes integration retains the boundary
\[
-\left(\frac xN\right)^T[E(N)-E(x)]^2.
\]
A centered signed limiting formula at \(T=2\), including the Euler constant contribution, follows from
\[
\int_x^\infty\frac{E(y)-E(x)}{y^2}\,dy
=\log x-\gamma-\sum_{n\le x}\frac{\Lambda(n)}n.
\]
This is an endpoint repair inside the exact object, not permission to cancel divergent uncentered series.

Read the [complete kernel and endpoint proof](../dyson/round21/length-arithmetic-kernel/EXACT_LENGTH_ARITHMETIC_KERNEL.md) and [root review of the kernel and Tauberian arguments](../dyson/round21/root-review/ROOT_KERNEL_AND_TAUBERIAN_REVIEW.md).

## 3. What the length average determines about one zeta test

Equation (2) is a multiplicative convolution. Set \(f(x)=C_{e^x}\), with a bounded extension below the original height range. Its kernel in logarithmic coordinates is
\[
q(u)=\frac4\pi\frac{e^{3u}}{(1+e^{2u})^2},
\qquad K(u)=q(-u).
\]
With the angular Fourier transform convention, direct beta integration gives
\[
\boxed{\widehat K(\tau)=
\frac{1+i\tau}{\cosh(\pi\tau/2)}\ne0
\quad(\tau\in\mathbb R).}
\tag{6}
\]
The gamma recurrence and reflection identities determine both the sign in the numerator and the normalization.

Round 20's actual-height regularity, together with \(C_{0,T}\to A\), implies the asymptotic modulus
\[
\limsup_{x\to\infty}\sup_{|h|\le\delta}
|f(x+h)-f(x)|
\le2A(1-e^{-\delta}).
\tag{7}
\]
Finite sums can jump at individual zero heights; (7) is the needed asymptotic statement, not an assertion of finite-height continuity.

Wiener's classical translation-density theorem applies to the nowhere-zero transform (6). If \(K*f\to c\), first approximate any fixed \(L^1\) kernel by a finite sum of fixed translates of \(K\). Then apply that conclusion to a fixed narrow averaging kernel, use (7), take the height limit, and only afterward let the averaging width shrink. This proves
\[
\boxed{
\overline V_T\longrightarrow c
\quad\Longleftrightarrow\quad
C_T\longrightarrow c
\quad\Longleftrightarrow\quad
D_T\longrightarrow A-c
}
\tag{8}
\]
under RH, along all real heights tending to infinity.

Equation (8) does not establish existence of any of these limits. It does not give a converse along an arbitrary isolated subsequence: the Wiener argument needs the limits of all fixed translates. Nor does it invert the smoothing stably in a bounded linear \(L^\infty\) norm; (6) decays exponentially at high frequency. The author's explicit wave examples record this limitation. This is a fixed-test application of classical Tauberian machinery, situated within the classical prime-variance/pair-correlation programme, without a claim to a new general Montgomery equivalence.

Read the [complete fixed-bump Tauberian proof](../dyson/round21/tauberian-information/FIXED_BUMP_TAUBERIAN_EQUIVALENCE.md). The primary Wiener statement is Theorem 1 in the [van Neerven preprint](https://fa.ewi.tudelft.nl/~neerven/publications/papers/RIMUT_97.pdf); the retained local source and page receipt identify the exact statement used.

## 4. Heat flow acting on the actual log-prime error

There is now an analytic heat formulation of (1) that starts from actual primes. Put \(\ell=\log T\) and
\[
F(v)=e^{-v/2}E(e^v),\qquad
\eta=\sqrt\omega,\qquad
g_T(v)=\eta(v/\ell)F(v).
\]
Under RH, \(|F(v)|\ll(1+\max(v,0))^2\). The localized function \(g_T\) is compactly supported in \(L^2\), with the genuine prime-power jumps retained.

The square root of this nonnegative smooth bump is globally Lipschitz and in \(H^1\). Indeed the Glaeser estimate
\[
|\omega'|^2\le2\|\omega''\|_\infty\omega
\]
bounds its derivative on each positive component and extends across the zero set. Smoothness of the square root is unnecessary. Its all-shift translation estimate is
\[
\|\eta(\,\cdot/\ell-u/\ell)-\eta(\,\cdot/\ell)\|_2^2
\le\frac{u^2}{\ell}\|\eta'\|_2^2.
\]

Changing variables \(x=e^v\) and \(u=\lambda/T\) in the centered arithmetic integral gives the exact increment
\[
e^{u/2}F(v+u)-F(v).
\]
Moving the cutoff inside this translation incurs a commutator. Its squared product-space norm is bounded by
\[
R_T\ll_\omega\frac1\ell\int_0^\infty
T e^{-(T-1)u}u^2(1+b\ell+u)^4du
=O_\omega(\ell^3/T^2).
\]
This estimate covers all positive shifts, including the region where only the translated cutoff is nonzero. The separately established Round 20 RH arithmetic bound, obtained before any new heat representation, then gives the normalized localization error \(O_\omega(\sqrt{\ell/T})\).

Plancherel and elementary Laplace integration now prove
\[
\boxed{
\overline V_T=
\frac{T}{2\pi\ell^2}
\int_{\mathbb R}
\frac{2T-1}{T-1}
\frac{\xi^2+1/4}{(T-1/2)^2+\xi^2}
|\widehat g_T(\xi)|^2\,d\xi
+O_\omega(\sqrt{\ell/T}).
}
\tag{9}
\]
The positive \(1/4\) and the factors of two are fixed by the exact exponential centering; they are not adjustable model constants.

For the ordinary heat semigroup \(H_t=\exp(t\partial_v^2/2)\), define
\[
\mathcal H_T=\int_0^\infty e^{-(T-1/2)^2t}
\left(\|\partial_vH_tg_T\|_2^2+
\tfrac14\|H_tg_T\|_2^2\right)dt.
\]
Then
\[
\boxed{
\overline V_T=\frac{T(2T-1)}{(T-1)\ell^2}\mathcal H_T
+O_\omega(\sqrt{\ell/T}).
}
\tag{10}
\]
The integrated Fourier multiplier is bounded, so Tonelli justifies this energy even though the unsmoothed arithmetic staircase need not have an \(L^2\) derivative.

Consequently a sufficient strict research target is
\[
\liminf_T\frac{2T}{\ell^2}\mathcal H_T<A.
\tag{11}
\]
Replacing the prefactor by two in this limiting criterion uses the inherited bound on the normalized energy. It is not a pointwise finite-height equality.

The flow here acts on the log-prime coordinate \(v\). It is distinct from moving zeta zeros under the de Bruijn–Newman deformation or eigenvalues under Dyson Brownian motion. A theorem for either of those dynamics does not automatically imply (11). The crude RH pointwise bound alone gives an unusable normalized estimate of order \(T\ell^3\). The missing strict gain must come from more information about the actual arithmetic function.

Read the [full heat-energy proof](../dyson/round21/log-prime-heat/LOCALIZED_MELLIN_HEAT_ENERGY.md) and [independent Aquinas review](../dyson/round21/log-prime-heat-review/INDEPENDENT_LOG_PRIME_HEAT_REVIEW.md).

## 5. An exact signed prime-pair error carries the missing gain

The all-length kernel also isolates a concrete centered two-point remainder. Let
\[
a_n=\Lambda(n)-1,\qquad
c_h=\mathfrak S(h)-1,
\]
where \(\mathfrak S(h)\) is the classical prime-pair singular series, zero for odd \(h\). Define the nonnegative weight
\[
b_T(m)=\frac{T m^{-T}}{\log^2T}
\int_1^m W_T(x)x^{T-2}\,dx.
\]
For \(T\ge4\), put
\[
\boxed{
\mathcal E_T=
2\sum_m b_T(m)\sum_{h\ge1}
(1+h/m)^{-T}\,[a_ma_{m+h}-c_h].
}
\tag{12}
\]
The full sum converges absolutely at each such \(T\). Its value may have either sign. Under RH the complete reduction is
\[
\boxed{\overline V_T=M+\mathcal E_T+o(1).}
\tag{13}
\]
Thus
\[
\boxed{\liminf_T\mathcal E_T\le1-M}
\tag{14}
\]
would imply the sufficient bound \(\liminf\overline V_T\le1<A\). Numerically its right side is approximately \(0.8148468567\). The existing RH upper information reaches only \(A-M\approx0.8254346531\). The required gain is the exact positive constant \(A-1\), approximately \(0.0105877964\). No bound (14) is proved here, and (14) is weaker than proving \(\mathcal E_T\to0\).

There are two substantial cancellation checks behind (13). First, replacing the exact continuous mean by the discrete centered sum retains the floor discrepancy:
\[
E(qx)-E(x)=\sum_{x<n\le qx}a_n+\{x\}-\{qx\}.
\]
Its squared norm in the normalized positive measure is at most \(T^{-3/4}/\log^2T\). Cauchy–Schwarz with the known RH variance bound makes its effect \(O(T^{-3/8}/\log T)\). The singleton terms inside \(a_ma_{m+h}\) are not discarded.

Second, the unconditional singular-series result of Montgomery–Soundararajan gives
\[
2\sum_{1\le h<k}(k-h)c_h=-k\log k+O(k).
\]
Twice integrating the exact Pareto kernel against this triangular sum yields, uniformly for \(T\ge4,m\ge T\),
\[
\sum_{h\ge1}c_h(1+h/m)^{-T}
=-\tfrac12\log(m/T)+O(1).
\tag{15}
\]
The logarithmic moment is controlled uniformly through a beta-prime probability density. Replacing the Pareto kernel by an exponential inside an absolute uncentered bound would introduce a growing error in the upper part of the prime window.

Finally the RH prime-number estimate for the diagonal, including higher prime powers, gives
\[
\sum_m b_T(m)a_m^2\longrightarrow
\int\alpha\omega(\alpha)\,d\alpha,
\]
whereas twice the singular-series comparison sum tends to
\[
-\int(\alpha-1)\omega(\alpha)\,d\alpha.
\]
Their sum is exactly \(M\). The manuscript also controls the \(m>2U_T\) tail and all errors in the slowly varying outer weight.

Read the [complete centered pair-error proof and revised range audit](../dyson/round21/strict-arithmetic-target/CENTERED_PAIR_ERROR_TARGET.md). The unconditional singular-series input is equation (16) of the [Montgomery–Soundararajan paper](https://arxiv.org/abs/math/0409258). Their stronger prime-moment theorems require extra conjectural prime-tuple estimates; the [Chan refinement](https://arxiv.org/abs/math/0503441) also states its additional mean-square hypothesis explicitly. Neither is an RH-only solution of (14).

## 6. A failed absolute-bound route and the exact obstruction

Write the centered partial error on a dyadic block as
\[
E_X(z,h)=\sum_{X<m\le z}[a_ma_{m+h}-c_h].
\]
Abel summation turns its contribution into a bound of the form
\[
\frac1{X\log^2T}\sum_{h\le X}
(1+h/(2X))^{-T}
\sup_{X<z\le2X}|E_X(z,h)|.
\tag{16}
\]
The effective shift scale is \(H=X/T\). Formally inserting a uniform estimate \(X^\beta\log^B X\) yields a block budget \(H X^{\beta-1}\log^{B-2}X\). Across \(X=T^\alpha\), \(\alpha\in[7/4,9/4]\), the formal threshold would be \(\beta<4/9\). The square-root budget still loses \(X^{1/18}\) at the upper endpoint, before logarithms.

The original draft described that sub-\(4/9\) all-shifts premise as an unproved possible stronger input. Coordinator review showed it is impossible, a substantive correction now retained in the record.

For integer \(X<z\le2X\), let
\[
P_X(z)=\sum_{X<m\le z}\Lambda(m)\Lambda(m+1).
\]
Any nonzero product has an even member which is a power of two. There are only \(O(\log X)\) candidates, each of weight \(O(\log X)\), so \(P_X(z)=O(\log^2X)\). Because \(c_1=-1\), exact expansion gives
\[
E_X(z,1)=P_X(z)-2[E(z)-E(X)]
-\Lambda(z+1)+\Lambda(X+1).
\tag{17}
\]
A uniform all-block bound with any fixed \(\beta<1/2\), including all sufficiently large \(T\) in the proposed window, would therefore imply
\[
E(x)=O(x^\theta)\qquad\text{for some }\theta<1/2
\]
by dyadic telescoping and extension from integers to real \(x\). The window condition covers every sufficiently large \(X\) by taking \(T=\sqrt X\); a sparse-subsequence premise would be different.

But
\[
\int_1^\infty E(y)y^{-s-1}\,dy
=\frac{-\zeta'/\zeta(s)}s-\frac1{s-1}
\]
initially for \(\Re s>1\). The proposed error estimate makes the integral holomorphic for \(\Re s>\theta\), contradicting the nonzero residue \(-m_\rho/\rho\) at any critical-line zero \(\rho\). Such zeros exist unconditionally, so RH is not needed for this obstruction. The classical inputs are the [Euler product](https://dlmf.nist.gov/25.2.E11) and [existence of critical-line zeros](https://dlmf.nist.gov/25.10).

This rules out the particular uniform absolute premise, not signed cancellation in (12), averaged estimates, or separately specified restricted shift ranges. In fact, under RH, (17) and (16) bound the single \(h=1\) contribution on each block by \(O_\omega(X^{-1/2})\), so its total in the current window is \(o(1)\). The bad pointwise premise does not itself obstruct the actual weighted target. A hypothetical gain \(H^\rho\) in signed aggregation would overcome the displayed square-root power loss if \(\rho>1/10\), with room for small exponent losses. A mean-square bound alone cannot simply be relabeled as that signed gain.

The original author draft, initial accepting review, coordinator objection, revised proof and later review are preserved with distinct hashes. The [root pair and heat review](../dyson/round21/root-review/ROOT_CENTERED_PAIR_AND_HEAT_REVIEW.md) records the missed feasibility issue and the complete delta review. This is a record of a corrected proposed route; it does not silently promote the old review to approval of the corrected version. Read the [coordinator's complete obstruction](../dyson/round21/coordinator-review/COORDINATOR_H1_OBSTRUCTION.md) and [updated independent pair review](../dyson/round21/strict-arithmetic-review/INDEPENDENT_CENTERED_PAIR_REVIEW.md).

## 7. What this changes for the next attempt

The current narrow objective is a strict estimate for the actual signed functional (12), or equivalently for the heat energy (10), sufficient to cross \(A\). The arithmetic and heat formulations expose different terms but contain the same missing information. Neither may assume the desired zeta-correlation asymptotic as input.

The useful next questions are whether small obstructing shifts can be bounded separately inside the actual weighted aggregate; whether an applicable signed dispersion or moment estimate survives the entire range \(H=X/T\); and whether the positive heat resolvent supports an energy inequality using arithmetic structure beyond the pointwise RH error estimate. Each proposal needs an exact normalization, a full range audit and a proof that its gain remains after centers and endpoints are restored.

The prime-gap 186 source's complementary factorization conditions concern a specific weighted one-prime progression theorem. They do not directly give the centered two-prime remainder or signed shift cancellation in (12). In the present window \(H\) ranges from \(X^{3/7}\) to \(X^{5/9}\); the earlier small-\(H\) transfer calculation does not cover it. The manuscript records a possible complete-residue opportunity where \(H>X^{0.523}\), together with the remaining half-line, endpoint and coefficient obstacles. No improvement of that source theorem is claimed.

This checkpoint adds no new prime-height scan and no new finite-RMT simulation. The tiny symbolic checkers test finite kernel algebra, exact transform identities, floor centers, exponent budgets and the explicitly stated endpoint cases. Independent copies reproduce their complete recorded outputs. Full ordinary proofs and source-page reviews handle the analytic limits; these are not Lean or other proof-assistant certifications.

The [intake manifest](../dyson/round21/INTAKE_MANIFEST.json), [source-link map](../dyson/round21/SOURCE_LINK_MAP.md) and [integration receipt](../logs/round21-integration/INTEGRATION_RECEIPT.json) separate original bytes, later reviews, public copies and local-only primary-source bodies. All research conclusions and verifiable calculations are preserved. The 705-page public and 753-page local handoffs remain the complete through-Round-14 compilations; this full later report and its source package extend the audit trail without relabeling those PDFs.

Broad numerical scans, another large PDF rebuild, general software frameworks, a supposed uniform sub-square-root pair theorem, and claims that deterministic ACUE flow automatically describes actual zeta zeros are postponed or excluded for the reasons above. Publication is a review checkpoint while the strict arithmetic research remains active.
