# Testing a short-interval sieve cap against the actual Bragg target

Round 17, 2026-09-05. Author: Euclid. Status: ordinary proof and a narrowly scoped method-bound calculation, submitted for independent review.

We obtain a legal upper estimate for the actual centered prime expression in the R16 Bragg target. It uses a positive time majorant, an exact moving-interval identity, and a primary-source Brun–Titchmarsh bound. Every prime–continuum cross term is retained. The resulting upper bound grows like \(x/(T\log T)\), so this application does not break the known saturation bound near \(\alpha=2\).

This is a failure of the specified short-interval cap/moment argument. It is not an obstruction for genuine primes, all sieve arguments, stronger averaged covariance estimates, or the desired zeta theorem. No novelty claim or prime-data experiment is made.

## 1. The precise target and the same centered signal

Use the frozen R16 notation, with \(x=T^\alpha\) and, for the specified bump of width \(\varepsilon=1/4\),

\[
\frac74\le\alpha\le\frac94,\qquad
a_u(x)=\min\{(u/x)^{1/2},(x/u)^{3/2}\},
\]

\[
P_x(t)=\sum_{n\ge2}\Lambda(n)a_n(x)n^{-it}
-\int_0^\infty a_u(x)u^{-it}du.
\tag{1}
\]

All prime powers remain. The sum and integral are absolutely convergent. Under RH the R16 reduction states, uniformly on this interval of exponents,

\[
F_T(\alpha)=\frac{\int_0^T|P_x(t)|^2dt}{xT\log T}+o(1).
\tag{2}
\]

For the nonnegative bump \(\psi_\varepsilon(\alpha)=\psi((\alpha-2)/\varepsilon)\),

\[
C_{\varepsilon,T}(2)=\int\psi_\varepsilon(\alpha)F_T(\alpha)d\alpha.
\]

The established upper bound is \(1+\varepsilon^2m_1\), exactly attained by the AH-Pairs prediction. A strict deficit below this number, or the stronger bound below one, remains unproved.

## 2. A legal positive majorant of the actual centered quadratic kernel

Put \(\ell=1/T\), and define the moving interval quantities on the logarithmic coordinate \(v\):

\[
A_x(v)=\sum_{e^v<n\le e^{v+\ell}}\Lambda(n)a_n(x),\qquad
m_x(v)=\int_{e^v}^{e^{v+\ell}}a_u(x)du,
\]

\[
J_x(T)=\int_{\mathbb R}|A_x(v)-m_x(v)|^2dv.
\tag{3}
\]

Use

\[
g_T(t)=\left(\frac{\sin(t/(2T))}{t/(2T)}\right)^2,\qquad
c_*=\left(\frac{\sin(1/2)}{1/2}\right)^2>0.
\]

The sinc function is decreasing and positive between zero and \(1/2\), so \(g_T(t)\ge c_*\) on \([-T,T]\). Plancherel gives the exact identity

\[
\boxed{\int_{\mathbb R}|P_x(t)|^2g_T(t)dt=2\pi T^2J_x(T).}
\tag{4}
\]

For normalization, introduce the finite signed measure on the log coordinate
\[
d\eta_x(v)=\sum_n\Lambda(n)a_n(x)\delta_{\log n}
-a_{e^v}(x)e^v\,dv.
\]
Its Fourier transform, using \(e^{-itv}\), is \(P_x(t)\). The convolution of this measure with \(1_{[-\ell,0]}\) is \(A_x-m_x\) up to endpoint conventions on a null set. The squared modulus of the interval's Fourier transform is \(\ell^2g_T(t)\). The \(1/(2\pi)\) Plancherel constant proves (4).

The finite total variation of \(\eta_x\), and convolution with the interval, also justify the \(L^2\) statements directly. Both \(A_x\) and \(m_x\) are integrable and bounded for fixed \(x,T\).

Since the signal is the Fourier transform of a real signed measure, its squared modulus is even. Therefore

\[
\boxed{
\frac1{xT\log T}\int_0^T|P_x(t)|^2dt
\le\frac{\pi T}{c_*x\log T}J_x(T).
}
\tag{5}
\]

This is a time-measure inequality for the complete centered signal. It is not an entrywise comparison between the oscillating sine kernel in R16 and a positive kernel. Its center has not been dropped:

\[
J_x(T)=\int A_x^2\,dv-2\int A_xm_x\,dv+\int m_x^2\,dv.
\tag{6}
\]

## 3. The primary sieve input and all prime powers

Yamada, arXiv:2312.16090v1, Theorem 2, equation (13), printed p.3, proves for every real \(u>0\), \(h>1\), at modulus one,

\[
\pi(u+h)-\pi(u)<\frac{2h}{\log h+0.8601}.
\tag{7}
\]

The theorem is unconditional and uniform in the starting point. We use the theorem as stated, without claiming to have audited its numerical proof or that it is the best possible bound in every power range. Its additive denominator improvement is retained below; it does not change the leading ratio when \(h\) is a fixed positive power.

For \(h=u(e^{1/T}-1)\) with \(T\) large, every prime in the interval has weight at most \(\log(u+h)\). The remaining prime powers satisfy the elementary uniform upper bound

\[
\sum_{\substack{u<p^k\le u+h\\k\ge2}}\log p
\ll \frac{h\log^2(2u)}{\sqrt u}+\log^2(2u).
\tag{8}
\]

To prove (8), allow every integer base for each \(2\le k\le\log_2(2u)\). The number is at most
\((h/k)u^{1/k-1}+1\), and each weight is at most \(\log(2u)\). Summing these bounds proves the displayed estimate. We have not discarded a prime-power error in the Bragg quadratic expression.

The weight \(a_u(x)\) is positive and satisfies the global log-Lipschitz bound

\[
e^{-3|z|/2}\le\frac{a_{ue^z}(x)}{a_u(x)}\le e^{3|z|/2}.
\tag{9}
\]

Consequently (7)–(9) imply, uniformly for \(u/x\) in any fixed compact subset of \((0,\infty)\), with \(x=T^\alpha\), \(7/4\le\alpha\le9/4\),

\[
A_x(\log u)\le
\left(\frac{2\alpha}{\alpha-1}+o(1)\right)m_x(\log u).
\tag{10}
\]

Indeed the principal cap ratio is
\[
e^{O(1/T)}
\frac{2\log(u+h)}{\log h+0.8601}
\longrightarrow c(\alpha):=\frac{2\alpha}{\alpha-1}.
\]
The error (8), divided by \(h\), tends to zero. In particular the central \(\alpha=2\) cap is \(4+o(1)\), not \(2+o(1)\): the von Mangoldt weight supplies \(\log x\), while the sieve denominator supplies \(\log(x/T)\).

## 4. Exact size of the retained center and cross term

The weight's elementary moments are

\[
\int_0^\infty u\,a_u(x)^2du
=\frac1x\int_0^x u^2du+x^3\int_x^\infty u^{-2}du
=\frac43x^2.
\tag{11}
\]

By (9), uniformly over all \(u>0\),
\[
m_x(\log u)=\frac{u\,a_u(x)}T(1+O(1/T)).
\]
It follows that

\[
\int_{\mathbb R}m_x(v)^2dv
=\left(\frac43+O(1/T)\right)\frac{x^2}{T^2}.
\tag{12}
\]

Fubini applied to the nonnegative cross term gives
\[
\int A_x(v)m_x(v)dv
=\sum_n\Lambda(n)a_n(x)
\int_{\log n-\ell}^{\log n}m_x(v)dv
=\frac{1+O(1/T)}{T^2}
\sum_n\Lambda(n)n a_n(x)^2.
\]

Under ordinary RH, partial summation of
\(\psi(y)=y+O(\sqrt y\log^2(2y))\) yields

\[
\sum_n\Lambda(n)n a_n(x)^2
=\frac43x^2+O(x^{3/2}\log^2(2x)).
\]

The two weights are \(n^2/x\) below \(x\) and \(x^3/n^2\) above \(x\); their derivatives and the RH error give the displayed bound separately, with the common endpoint retained. Thus

\[
\boxed{\int A_xm_x=
\left(\frac43+o(1)\right)\frac{x^2}{T^2}.}
\tag{13}
\]

These are global, smoothly weighted means. They require no short-interval prime asymptotic. The error in (13) is relative to the large mean \(x^2/T^2\); it is not silently asserted to be \(o(1)\) after the final Bragg normalization.

## 5. A proved capped-moment estimate, including both tails

**Proposition.** Under RH, uniformly for \(x=T^\alpha\), \(7/4\le\alpha\le9/4\),

\[
\boxed{
J_x(T)\le
\left[\frac43\frac{\alpha+1}{\alpha-1}+o(1)\right]
\frac{x^2}{T^2}.
}
\tag{14}
\]

The only arithmetic inputs are (7), the elementary power count (8), and the ordinary RH global prime estimate used in (13).

**Proof.** On any fixed range \(e^{-R}\le u/x\le e^R\), (10) and \(A_x\ge0\) give
\(A_x^2\le(c(\alpha)+o(1))A_xm_x\).
We justify extending this inequality in the integral before applying (6).

Set \(Q=T^{5/4}\). For \(1\le u\le Q\), the crude integer count and \(\Lambda(n)\le\log n\), together with \(u+h<x\) for large \(T\), give
\[
\int_{\log u:\,u\le Q} A_x(v)^2dv
\ll\frac{\log^2(2Q)}x
\left(\frac{Q^3}{T^2}+\frac{Q^2}T+Q\right)
=o(x^2/T^2).
\tag{15}
\]
There are no atoms for \(u<2e^{-1/T}\); this handles the lower endpoint. At the smallest admitted \(\alpha=7/4\), the three relative powers of \(T\) in (15) are \(-3/2,-7/4,-2\), respectively, before logarithms. The analogous \(m_x^2\) contribution is negligible, and Cauchy–Schwarz handles \(A_xm_x\) there.

For all \(u\ge Q\), (7)–(9) give the uniform bound \(A_x\le11m_x\) for sufficiently large \(T\). Indeed the prime cap ratio is at most \(10+o(1)\), and the ratio from (8) is
\[
O\!\left(\frac{\log^2(2u)}{\sqrt u}
+\frac{T\log^2(2u)}u\right)=o(1)
\]
uniformly in that range. Hence \(A_x^2\le11A_xm_x\).

Fubini as in (13), or partial summation with \(\psi(y)\ll y\), bounds the \(A_xm_x\) mass on \(u/x\notin[e^{-R},e^R]\) by
\[
O((e^{-3R}+e^{-R})x^2/T^2).
\tag{16}
\]
The continuous \(m_x^2\) tail has the same bound by (11). The powers are those of the lower moment \(u^2/x\) and the upper moment \(x^3/u^2\). First let \(T\) tend to infinity, uniformly in \(\alpha\), and then let \(R\) tend to infinity. Equations (10), (15) and (16) prove
\[
\int A_x^2\le(c(\alpha)+o(1))\frac43\frac{x^2}{T^2}.
\]

Now substitute this inequality, (12), and (13) into the exact centered expansion (6). The leading coefficient is
\[
\frac43[c(\alpha)-2+1]
=\frac43\frac{\alpha+1}{\alpha-1}.
\]
The \(-2\) is the retained prime–continuum contribution. This proves (14). No lower bound was substituted in place of an unknown signed correlation. ∎

## 6. What this actually gives for the Bragg test

Combining (2), (5) and (14) yields the valid but weak upper estimate

\[
F_T(\alpha)\le
\left[\frac{4\pi}{3c_*}\frac{\alpha+1}{\alpha-1}+o(1)\right]
\frac{T^{\alpha-1}}{\log T}+o(1),
\tag{17}
\]

uniformly on the admitted interval. At \(\alpha=2\) its coefficient is \(4\pi/c_*\), and its size is \(T/\log T\).

Because \(\psi_\varepsilon\ge0\), this is a legal majorant for the exact centered quadratic expression of the original target:

\[
C_{\varepsilon,T}(2)\le
\frac1{\log T}\int\psi_\varepsilon(\alpha)
\left[\frac{4\pi}{3c_*}\frac{\alpha+1}{\alpha-1}+o(1)\right]
T^{\alpha-1}d\alpha+o(1).
\tag{18}
\]

The right side of this available estimate diverges. For example, on the fixed interval \(2\le\alpha\le2+\varepsilon/2\), the bump has a positive lower bound and \(T^{\alpha-1}\ge T\). Thus the bound supplied by (18), not the actual \(C_{\varepsilon,T}(2)\), grows at least proportionally to \(T/\log T\). The already established upper bound \(1+\varepsilon^2m_1\) is much stronger.

The loss is visible even after exact centering: a fixed cap \(A_x\le c\,m_x\), together with its first moment, bounds the centered second moment at scale \((c-1)m_x^2\). Here \(m_x\) is of order \(x/T\). The required quadratic scale is of order \(m_x\log T\), smaller by \(x/(T\log T)\). Replacing the fixed cap constant by another number greater than one does not repair this power loss.

Within this particular cap-times-first-moment step, reaching a bounded Bragg estimate would require an excess cap of order \(T\log T/x\), with a suitably controlled constant, or an independent averaged centered second-moment estimate. This is a diagnosis of that inequality step, not a necessary condition for every proof strategy. An oscillatory or genuinely averaged sieve argument may use information that the cap step loses.

No negative prime–continuum term was removed: it supplies the \(-2\) in (14). No prime powers were deleted. The failure is therefore not explained by a forgotten pole term; it persists in this explicit legal application after the means are handled correctly.

## 7. Scope, source pins and reproducibility

This bounded test proves (4), (5), and (14)–(18) for the actual weighted von Mangoldt signal. It finds no strict deficit at the AH atom. The calculation does not exhaust published short-interval or sieve techniques and makes no claim that a stronger joint prime estimate is impossible.

Primary inputs:

- Tomohiro Yamada, [Explicit improvements of the Brun–Titchmarsh theorem for arbitrary intervals](https://arxiv.org/pdf/2312.16090v1), Theorem 2, equation (13), printed p.3. We use only its modulus-one case and keep its precise range \(u>0,h>1\). The paper's PDF/text are retained locally with hashes, not copied into the canonical repository by this task.
- D. A. Goldston, [Notes on Pair Correlation of Zeros and Prime Numbers](https://arxiv.org/pdf/math/0412313), equation (3.4), printed p.4, gives the ordinary RH global prime-error input. The actual-signal reduction is pinned through the R16 report, which records its own explicit-formula provenance.

The adjacent exact checker verifies the weight-moment constant, the centered cap coefficients at the endpoint and central exponents, and the three low-tail power margins. It performs no prime scan and does not turn this weak upper bound into evidence about the actual Bragg limit.
