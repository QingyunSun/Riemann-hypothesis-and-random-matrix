# Exponential averaging removes the envelope loss for an actual prime variance

Date: 2026-09-05. Status: ordinary proof submitted for independent review. Assumption: RH. This is an application of the classical weighted prime/zero Plancherel formula and the RH Selberg bound. No novelty claim, strict Bragg deficit, AH refutation, or Montgomery–Dyson theorem is made.

The result concerns **one actual statistic at each finite height**, with an integral over all positive logarithmic interval lengths. It is not merely an iterated limit of formally averaged zero kernels. Reparameterization supplies the needed uniformity on compact length ranges; a separate arithmetic argument controls the infinite length tail.

## 1. The statistic and the bound

Retain the Round 16 autocorrelation bump \(\psi\), with \(\psi(0)=1\), both \(\psi\) and \(\widehat\psi\) nonnegative, and support \([-1,1]\). Fix \(\varepsilon=1/4\), and set
\[
\omega(\alpha)=\psi((\alpha-2)/\varepsilon),\qquad
m_1=\int |u|\psi(u)du,\qquad
A_\varepsilon=1+\varepsilon^2m_1.
\tag{1}
\]
Write \(\Psi(x)=\sum_{n\le x}\Lambda(n)\), keeping all prime powers. For \(T\ge2\) and \(\lambda>0\), define
\[
\Delta_{\lambda,T}(x)=\Psi(e^{\lambda/T}x)-\Psi(x)
-(e^{\lambda/T}-1)x,
\tag{2}
\]
\[
V_{\lambda,T}(\omega)=\frac{T}{\log^2T}\int_1^\infty
\Delta_{\lambda,T}(x)^2\,
\omega\!\left(\frac{\log x}{\log T}\right)\frac{dx}{x^2},
\qquad
\overline V_T=\int_0^\infty e^{-\lambda}V_{\lambda,T}(\omega)d\lambda.
\tag{3}
\]
The center in (2) is exact, not \(\lambda x/T\). The \(x\)-window is exactly \([T^{7/4},T^{9/4}]\); its logarithmic weight is independent of \(\lambda\). For every fixed \(\lambda\), the interval includes \(x<n\le e^{\lambda/T}x\). Endpoint conventions on the jumps of \(\Psi\) change neither Lebesgue integral.

Let \(F_U\) be the Round 16 Montgomery form factor, normalized by \(U\log U/(2\pi)\), and write
\[
C_U=\int\omega(\alpha)F_U(\alpha)d\alpha,
\qquad D_U=C_{\varepsilon,U}(0)-C_U\ge0.
\tag{4}
\]
For harmless notation in integrals below, put \(C_U=D_U=0\) when \(U<2\). Their actual values for \(U\ge2\) remain unchanged.

**Theorem.** Under RH, (3) is finite for every \(T\ge2\), and
\[
\boxed{\overline V_T=\int_0^\infty p(y)C_{Ty}dy+o(1),\qquad
p(y)=\frac4\pi\frac{y^2}{(1+y^2)^2},\quad
\int_0^\infty p(y)dy=1.}
\tag{5}
\]
Consequently,
\[
\boxed{0\le\liminf_T\overline V_T\le\limsup_T\overline V_T
\le A_\varepsilon,}
\tag{6}
\]
and
\[
\boxed{A_\varepsilon-\overline V_T
=\int_0^\infty p(y)D_{Ty}dy+o(1).}
\tag{7}
\]
In particular RH plus the precise AH-Pairs hypothesis of Round 16 implies
\(\overline V_T\to A_\varepsilon\).
There is no factor \(L^+\approx1.0736\) in (6). The bound reaches, but does not beat, the AH value.

More generally, (5) implies
\[
\liminf_U C_U\le\liminf_T\overline V_T
\le\limsup_T\overline V_T\le\limsup_U C_U.
\tag{8}
\]
For \(d=\limsup_U D_U\), one therefore obtains the quantitative sufficient implication
\[
d\ge A_\varepsilon-\liminf_T\overline V_T.
\tag{9}
\]
A reverse strict-subsequence implication would additionally need persistence of a deficit across a nonvanishing interval of multiplicative heights. That separate estimate is not assumed in this proof.

## 2. Verified primary inputs and their scope

The primary source is Carneiro–Chandee–Chirre–Milinovich (CCCC), *On Montgomery's pair correlation conjecture: a tale of three integrals*. We use only the following already checked statements:

1. The RH Selberg estimate, source equation (1.3): for every fixed \(B>1\),
\[
J(B,S):=\int_1^{S^B}
\left(\Psi((1+1/S)x)-\Psi(x)-x/S\right)^2\frac{dx}{x^2}
\ll_B\frac{\log^2S}{S}
\quad(S\to\infty).
\tag{10}
\]
2. For one fixed \(g\) with \(\widehat g\in C_c^\infty((0,\infty))\), put \(\omega_g=|\widehat g|^2\),
\[
f_S(t)=\left|\sum_\gamma g((t-\gamma)\log S/(2\pi))\right|^2
+\left|\sum_\gamma g((\gamma-t)\log S/(2\pi))\right|^2,
\quad K_S(Y)=\int_0^Yf_S(t)dt.
\tag{11}
\]
The sums include every nontrivial zero ordinate, with multiplicity and both signs. CCCC equation (3.8), printed p.25, gives
\[
V_{1,S}^{\rm lin}(\omega_g)
=\frac{2S}{\pi}\int_0^\infty
\left(\frac{\sin(\kappa_St)}t\right)^2f_S(t)dt
+O_g(\log^{-2}S),
\quad \kappa_S=\tfrac12\log(1+1/S).
\tag{12}
\]
Here \(V_{1,S}^{\rm lin}\) uses the interval \((x,(1+1/S)x]\), center \(x/S\), normalization \(S/\log^2S\), and weight \(\omega_g(\log x/\log S)\), as in Round 19.
3. In the same source, the equality immediately before (3.9) gives
\[
K_S(Y)=2Y\int\omega_g(\alpha)F_Y(\alpha)d\alpha+o_g(Y),
\quad S\log^{-3}S\le Y\le S\log^3S,
\tag{13}
\]
uniformly in this range. Also \(f_S(t)\ll_g\log^2(t+2)\), uniformly for sufficiently large \(S\). The source's later plateau assumptions on \(\widehat g\) are used to bound characteristic intervals, not required by (12)–(13).

All uses of (12)–(13) below keep **one fixed \(g\)**. We do not posit a uniform source error for a family of varying test functions. The local spectral mass bounds needed below are the positive-pair comparison from Round 16, or the equivalent bounded fixed-window mass bounds used in Round 19.

## 3. The all-length arithmetic tail is controlled before any zero transfer

The following bounds hold for any fixed bounded nonnegative \(\omega\) supported in \([a,b]\subset(0,\infty)\), and in particular for (1). Constants may depend on this fixed window and its sup norm.

Define exactly
\[
S=S(T,\lambda)=\frac1{e^{\lambda/T}-1},\qquad
r=\frac{\log S}{\log T},\qquad
\omega_{T,\lambda}(\alpha)=\omega(r\alpha).
\tag{14}
\]
For \(S>1\), a direct change of normalization, with no approximation, gives
\[
V_{\lambda,T}(\omega)
=\frac TSr^2 V_{1,S}^{\rm lin}(\omega_{T,\lambda}).
\tag{15}
\]
For \(0<\lambda\le\sqrt T\), one has \(S\gg\sqrt T\) and
\(\log S\ge(1/2-o(1))\log T\). Thus \(T^b\le S^B\) for a fixed choice such as \(B=3b+3\), once \(T\) is large. Apply (10), directly on the original nonnegative \(x\)-integral, to obtain
\[
V_{\lambda,T}(\omega)\ll_\omega
\frac TS\frac{\log^2S}{\log^2T}.
\tag{16}
\]
For \(1\le\lambda\le\sqrt T\), \(\log S\le\log T\), and
\(T/S=T(e^{\lambda/T}-1)\ll\lambda\). For \(0<\lambda\le1\),
\(\log S\le\log T+\log(1/\lambda)\). Consequently,
\[
V_{\lambda,T}(\omega)\ll_\omega
\begin{cases}
\lambda(1+|\log\lambda|)^2,&0<\lambda\le1,\\
\lambda,&1\le\lambda\le\sqrt T.
\end{cases}
\tag{17}
\]
The constants here are independent of \(T\) and \(\lambda\). This is a use of (10) at a fixed \(B\), not an unproved uniformity of a theorem in a moving prime window.

For \(\lambda>\sqrt T\), use the classical RH consequence
\(E(x):=\Psi(x)-x\ll\sqrt x\log^2(2x)\). The exact center in (2) gives
\(\Delta_{\lambda,T}(x)=E(e^{\lambda/T}x)-E(x)\). On the fixed logarithmic window,
\[
V_{\lambda,T}(\omega)
\ll_\omega \frac T{\log T}
e^{\lambda/T}(\log T+\lambda/T+1)^4.
\tag{18}
\]
For \(T\ge2\), the weight \(e^{-\lambda}\) dominates this expression by an integrable exponential times a polynomial. This proves finite-\(T\) existence. Moreover its integral over \(\lambda>\sqrt T\) is
\(O_\omega(T^C e^{-\sqrt T/2})=o(1)\) for some absolute fixed \(C\); no useful optimization of that harmless polynomial is needed.

Equations (17)–(18) yield the quantitative tail statements
\[
\limsup_{T\to\infty}\int_L^\infty e^{-\lambda}V_{\lambda,T}(\omega)d\lambda
\ll_\omega(L+1)e^{-L}\qquad(L\ge1),
\tag{19}
\]
\[
\limsup_{T\to\infty}\int_0^a e^{-\lambda}V_{\lambda,T}(\omega)d\lambda
\ll_\omega a^2(1+|\log a|)^2\qquad(0<a\le1).
\tag{20}
\]
The same argument gives a uniform bound for the total average in (3) for all sufficiently large \(T\). It also bounds the mass of any fixed enlarged logarithmic window. Those facts will justify approximation of the test function at the end.

## 4. Legal fixed-test transfer on compact length and zero-height ranges

First take \(\omega=\omega_g\) from (11), and fix
\(0<a<L<\infty\). Uniformly for \(a\le\lambda\le L\),
\[
S=\frac T\lambda(1+O_L(T^{-1})),\quad
r=1+O_{a,L}(\log^{-1}T),\quad
T/S=\lambda+O_L(T^{-1}).
\tag{21}
\]
All weights \(\omega_{T,\lambda}\) are supported in one fixed compact subinterval of \((0,\infty)\), and
\(\|\omega_{T,\lambda}-\omega\|_\infty=O_{g,a,L}(1/\log T)\).
The nonnegative Selberg mass bound (10), on that enlarged window, therefore permits replacing \(\omega_{T,\lambda}\) by the **fixed** \(\omega\) in (15), with an error \(o_{g,a,L}(1)\) uniform in \(\lambda\). Apply (12) with this fixed \(g\). The exact relation
\(\kappa_S=\lambda/(2T)\), followed by \(t=Ty\), gives
\[
V_{\lambda,T}(\omega)
=\frac2\pi r^2\int_0^\infty k_\lambda(y)
\,d\!\left(\frac{K_S(Ty)}T\right)+o_{g,a,L}(1),
\quad k_\lambda(y)=\frac{\sin^2(\lambda y/2)}{y^2}.
\tag{22}
\]
The measures in (22) do depend on \(\lambda\) through \(S\). We do not identify them with one common smoothed zero process.

Nevertheless, for fixed \(0<\eta<R<\infty\), (13) implies
\[
\frac{K_S(Ty)}T=2y C_{Ty}+o_{g,a,L,\eta,R}(1)
\quad(\eta\le y\le R),
\tag{23}
\]
uniformly in both \(\lambda\) and \(y\). Indeed \(S\asymp_{a,L}T\), and the ratio \(Ty/S\) remains in a fixed compact subset of \((0,\infty)\), strictly inside the source's logarithmic range for large \(T\). The two-parameter uniformity in (13) with fixed \(g\) is exactly the one being used. The right side of (23) is independent of \(S\) to the stated accuracy.

Integration by parts on \([\eta,R]\) in (22) is now legitimate. It differentiates the explicit kernel, **not** \(C_U\) and not an unknown error term. After replacing \(r^2\) by one, its contribution is
\[
\frac4\pi\left[
Rk_\lambda(R)C_{TR}-\eta k_\lambda(\eta)C_{T\eta}
-\int_\eta^R yk_\lambda'(y)C_{Ty}dy\right]+o(1),
\tag{24}
\]
uniformly on the fixed length range. Even if \(C_U\) jumps when the height passes a zero, the displayed expression is well defined; no differentiability of \(C_U\) has been used.

For completeness the discarded \(y\) ends in (22) have bounds
\[
\limsup_T\int_0^\eta k_\lambda(y)
\,d(K_S(Ty)/T)\ll_g\lambda^2\eta,
\qquad
\limsup_T\int_R^\infty k_\lambda(y)
\,d(K_S(Ty)/T)\ll_g R^{-1},
\tag{25}
\]
uniformly for \(\lambda\in[a,L]\). Here is the needed justification. In the source range, (13) and the bounded fixed-window spectral mass give \(K_S(Ty)/T\ll_g y\). Use \(k_\lambda\le\lambda^2/4\) at the lower end and \(k_\lambda\le y^{-2}\) at the upper end, with Stieltjes integration by parts for the latter. Below \(S\log^{-3}S\) and above \(S\log^3S\), the pointwise logarithmic bound on \(f_S\) gives errors tending to zero, uniformly at fixed \([a,L]\). The intermediate-range constants in the limsup in (25) can be chosen independently of this compact length range: they use the fixed-test spectral mass bound and the limiting ratio \(\log S/\log T\to1\). Thus, after multiplication by \(e^{-\lambda}\), the lower-end bound is \(O_g(\eta\int_a^L\lambda^2e^{-\lambda}d\lambda)=O_g(\eta)\), and the upper-end bound is \(O_g(1/R)\).

## 5. Averaging the kernels and removing every cutoff

On fixed \([a,L]\) and \([\eta,R]\), average (24) using ordinary Fubini. Put
\(k_{a,L}(y)=\int_a^L e^{-\lambda}k_\lambda(y)d\lambda\).
The elementary Laplace transform is
\[
\begin{aligned}
k_\infty(y)
&:=\int_0^\infty e^{-\lambda}
\frac{\sin^2(\lambda y/2)}{y^2}d\lambda\\
&=\frac1{2y^2}\left(1-\frac1{1+y^2}\right)
=\frac1{2(1+y^2)}.
\end{aligned}
\tag{26}
\]
At zero the same value follows from \(\int e^{-\lambda}\lambda^2/4=1/2\). Both \(k_{a,L}\) and its derivative converge uniformly to \(k_\infty\) on a fixed compact \(y\)-interval as \(a\downarrow0,L\uparrow\infty\). Differentiation here is of an absolutely convergent elementary integral; it is unrelated to differentiating an asymptotic formula for zeta.

The order of the proof is as follows:

1. Fix \(a,L,\eta,R\), use (22)–(24), and let \(T\to\infty\) in the error bounds, without presuming a limit for \(C_T\).
2. At fixed \(\eta,R\), send \(a\downarrow0,L\uparrow\infty\). Equations (19)–(20) control the actual prime-variance lengths discarded on the left. Uniform kernel convergence controls the compact-\(y\) expression on the right. The integrated bounds in (25) are \(O_g(\eta+1/R)\).
3. Send \(\eta\downarrow0,R\uparrow\infty\). The final decreasing kernel has derivative
\(k_\infty'(y)=-y/(1+y^2)^2\). The boundary terms in (24) tend to zero because \(C_U\) is bounded for \(U\ge2\), while \(yk_\infty(y)=O(y)\) near zero and \(O(1/y)\) at infinity.

These estimates prove that the difference between the two sides of (5) tends to zero. They concern the original all-length statistic (3); the length cutoffs are auxiliary proof devices. Equivalently, for any prescribed error tolerance one first chooses the fixed auxiliary cutoffs sufficiently far out, then takes \(T\) sufficiently large. No prescribed growing cutoff or rate for the source's \(o(Y)\) is claimed.

Finally,
\[
-\frac4\pi yk_\infty'(y)=p(y),\qquad
\int_0^\infty\frac{y^2}{(1+y^2)^2}dy=\frac\pi4,
\tag{27}
\]
which gives precisely the probability density in (5). The upper constant one arises because the averaged kernel itself is decreasing. Replacing an oscillating squared-sinc kernel by a decreasing majorant is no longer needed.

## 6. Extension to the exact autocorrelation bump and the AH value

The proof so far assumes \(\omega=|\widehat g|^2\) with one fixed smooth compactly supported \(\widehat g\). To recover (1), approximate the continuous square root of \(\omega\) uniformly by smooth functions supported in a common compact interval \(J\subset(0,\infty)\), and square them. Write the resulting nonnegative weights as \(\omega_j\), with \(\|\omega_j-\omega\|_\infty\to0\).

The arithmetic bound in Section 3, applied to the characteristic mass on \(J\), gives
\[
\limsup_T|\overline V_T(\omega_j)-\overline V_T(\omega)|
\ll_J\|\omega_j-\omega\|_\infty.
\tag{28}
\]
The fixed-window spectral mass bound similarly controls
\(|C_U(\omega_j)-C_U(\omega)|\) uniformly for large \(U\), hence its average against \(p\). The finite-height portion \(Ty\) below a fixed threshold has vanishing \(p\)-mass. Apply (5) at each fixed \(j\), take \(T\to\infty\), then \(j\to\infty\). No Schwartz-seminorm constants are required to remain bounded in \(j\).

Round 16 gives \(C_{\varepsilon,U}(0)=A_\varepsilon+o(1)\), \(0\le C_U\le C_{\varepsilon,U}(0)\), and \(D_U\ge0\). Averaging these statements against the probability density proves (6)–(9). Under RH+AH-Pairs, Round 16 proves \(C_U\to A_\varepsilon\), without an additional simplicity assumption or a limit for a near-zero clustering parameter. Dominated convergence in (5) gives equality at the AH value.

For later use, in logarithmic height \(u=\log y\), the averaging density is
\[
q(u)=p(e^u)e^u=\frac4\pi\frac{e^{3u}}{(1+e^{2u})^2}>0.
\tag{29}
\]
Thus the transfer averages over multiplicative zero heights, with positive mass on every fixed open height-ratio interval. It is not an identity at one common height.

## 7. Arithmetic content, relation to logarithmic derivatives, and limitations

This is a real bound for the positive, exactly centered prime variance (3). All prime powers and the continuous density subtraction remain inside its square. Nothing has replaced the arithmetic coefficients by generic point-process data. The only arithmetic estimates used are already known under RH: the fixed-window Selberg bound, the classical \(\Psi(x)-x\) bound for the far length tail, and the verified weighted prime/zero formula.

The proof is an elementary Laplace averaging of that classical formula. It should be regarded as a useful choice of smoothing, with no assertion of priority. The Poisson factor in (26) acts on the **rescaled zero-height variable** \(t/T\) of a smoothed zero sum. CCCC Section 4's usual logarithmic-derivative moment instead produces a Poisson kernel in the **difference of two zero ordinates** and retains a gamma/mean term. These are related transform methods, but (5) has the fixed logarithmic prime window \(\omega\) and is not identified here with an unweighted one-parameter integral of \(|\zeta'/\zeta|^2\). Establishing such an additional exact representation would require its own localization and centering calculation; it is not needed for (5).

The genuine improvement in this bounded exercise is from the available transfer constant \(L^+A_\varepsilon\) for an unsmoothed single interval length to the bound \(A_\varepsilon\) for the explicitly different length-averaged statistic. It is not a strict improvement below the saturation value, and it does not improve the original unsmoothed variance by implication. No existing theorem cited here proves \(\liminf\overline V_T<A_\varepsilon\). Producing that strict arithmetic loss remains the essential research problem.

## 8. Sources and verification record

- [CCCC author-hosted primary paper](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), equations (1.3), (3.8), equality before (3.9), and Section 4; the previously retained PDF/text are pinned in the adjacent receipt. The present proof uses these fixed-test statements, not a new uniform-in-length version of them.
- [Schoenfeld, *Sharper bounds for the Chebyshev functions*, II](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), Theorem 10, equation (6.2), printed p.337: under RH, the explicit \(\sqrt x\log^2x/(8\pi)\) bound for \(|\Psi(x)-x|\) holds for \(x>73.2\). Enlarging its constant on a bounded initial interval supplies the elementary global bound used in (18); the explicit constant is not needed here.
- [Round 19 weighted variance proof](../../research-round19/bragg-variance-literature/BRAGG_WEIGHTED_SELBERG_VARIANCE.md) and its independent review: normalization, fixed-test source ranges and the former \(L^+\) loss.
- [Round 16 Bragg target](../../research-round16/bragg-atom/BRAGG_ATOM_TARGET.md): the exact bump, positive-pair upper bound, compact spectral mass, AH saturation and treatment of early/near-zero pairs.

During source exploration I located indexed text of Goldston–Gonek (1990), printed p.616, displaying a general interval-length formula. The AMS download returned HTTP 403; the older DigiZeitschriften link for Goldston (1988) redirected to its service-closure page. Those inaccessible formulas are **not used as additional proof inputs**. Reparameterization (14)–(24) avoids needing a new source claim about their uniformity.

This is an analytic proof, not a numerical parameter scan. The adjacent symbolic check verifies only the elementary Laplace kernel, its derivative, total mass and the exact reparameterization algebra. It is not a verification of the analytic error estimates or a certified numerical zeta result. The full source and proof checks are recorded separately.
