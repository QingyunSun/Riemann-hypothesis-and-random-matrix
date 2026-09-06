# Independent review of the exponential length-average identity

Reviewer: Euclid / prime186. Date: 2026-09-05.
Verdict: **accepted under RH, within the author's stated scope**. No correction to the frozen author report is required.

Reviewed file: EXPONENTIAL_LENGTH_AVERAGE.md, 18,644 bytes, SHA256
cd8c2f7dc48530ed02f915dd202c8aedaaaadb1096cafc019beeb595b9beebbe.

I read the whole report and its symbolic checker, checked every change of variables and cutoff argument, and replayed the thirteen elementary checks in a temporary copy. The identity concerns an explicitly different all-length prime statistic. It establishes no strict deficit below the AH value.

## 1. Exact arithmetic reparameterization

The decisive identity is
\[
S=\frac1{e^{\lambda/T}-1},\qquad
1+\frac1S=e^{\lambda/T}.
\]
Thus the actual interval and its center agree **exactly** with the source's linear-length interval at parameter \(S\). If
\(r=\log S/\log T\), then
\[
\omega_{T,\lambda}(\alpha)=\omega(r\alpha)
\]
satisfies
\[
\omega_{T,\lambda}(\log x/\log S)=\omega(\log x/\log T).
\]
The prime window has not moved. The normalization identity is likewise exact:
\[
\frac TSr^2\frac S{\log^2S}=\frac T{\log^2T}.
\]
This proves the author's equation (15) whenever \(S>1\), without replacing the mean by \(\lambda x/T\).

The restriction \(S>1\) is respected. In the asymptotic near/intermediate length range \(0<\lambda\le\sqrt T\), one has \(S\gg\sqrt T>1\). Large lengths, including those for which \(S\le1\), are handled directly by the RH Chebyshev error bound and never fed into this reparameterized source formula.

## 2. Actual arithmetic tails, including finite-height existence

For \(0<\lambda\le\sqrt T\),
\[
\log S\ge(\tfrac12-o(1))\log T.
\]
For a fixed support window \([a,b]\), a fixed exponent such as \(B=3b+3\) therefore gives \(T^b\le S^B\), uniformly in this entire length range. The nonnegative integral is bounded directly by the fixed-\(B\) Selberg integral. This proves
\[
V_{\lambda,T}\ll \frac TS\frac{\log^2S}{\log^2T}.
\]
It does not ask for uniformity of a smooth-test Plancherel formula as the test changes.

The inequalities
\[
T/S\ll\lambda,\qquad
\log S\le\log T+\log(1/\lambda)\quad(0<\lambda\le1)
\]
and \(\log S\le\log T\) for \(1\le\lambda\le\sqrt T\) give the stated
\(\lambda(1+|\log\lambda|)^2\) and \(\lambda\) bounds, with constants independent of \(T,\lambda\) once \(T\) is sufficiently large.

For the far tail, retain the exact mean:
\[
\Delta_{\lambda,T}(x)
=E(e^{\lambda/T}x)-E(x),\qquad E(x)=\Psi(x)-x.
\]
The RH bound \(E(z)\ll\sqrt z\log^2(2z)\) yields
\[
|\Delta_{\lambda,T}(x)|^2
\ll e^{\lambda/T}x\,
(\log T+\lambda/T+1)^4
\]
on the fixed logarithmic prime window. Since its integral of \(dx/x\) is \(O(\log T)\), this gives exactly
\[
V_{\lambda,T}\ll
\frac T{\log T}e^{\lambda/T}
(\log T+\lambda/T+1)^4.
\]
The exponential is \(e^{\lambda/T}\), not \(e^{2\lambda/T}\). That distinction depends on retaining the center and using RH.

For every \(T\ge2\), multiplication by \(e^{-\lambda}\) gives decay at least \(e^{-\lambda/2}\) times a polynomial. This proves integrability at infinity even at \(T=2\). On a compact length interval, the same RH bound, or local boundedness of the finite-range Chebyshev function, proves finite-height integrability. Thus the all-length statistic exists for every stated height, not merely asymptotically.

Finally,
\[
\int_L^\infty\lambda e^{-\lambda}\,d\lambda=(L+1)e^{-L},
\quad
\int_0^a\lambda(1+|\log\lambda|)^2\,d\lambda
\ll a^2(1+|\log a|)^2.
\]
Combined with the \(o(1)\) far tail above \(\sqrt T\), these prove the author's equations (19)–(20) and the uniform mass bound for any fixed enlarged logarithmic window. No infinite prime-series expansion or formal tail cancellation has been substituted for these bounds.

## 3. Fixed-test use of the classical prime/zero formula

On a fixed compact length range \([a,L]\),
\[
S=T/\lambda\,(1+O_L(T^{-1})),\qquad
r=1+O_{a,L}(1/\log T).
\]
The moving weight differs from the fixed smooth weight in sup norm by \(O_{g,a,L}(1/\log T)\), with support in one fixed compact interval. Positivity and the Selberg mass bound control the change in the original prime integral. This legitimately removes the moving test **before** using CCCC.

The CCCC input consequently uses one fixed \(g\). The author's source constants need not be uniform in a family of Schwartz functions. For this fixed test, the source remainder tends uniformly to zero as \(S\asymp_{a,L}T\to\infty\).

The exact relation
\[
\kappa_S=\tfrac12\log(1+1/S)=\lambda/(2T)
\]
and \(t=Ty\) give
\[
V_{\lambda,T}
=\frac2\pi r^2\int_0^\infty
\frac{\sin^2(\lambda y/2)}{y^2}\,
d\!\left(K_S(Ty)/T\right)+o(1).
\]
I checked all \(T,S,\log S\) and \(\pi\) factors. The rescaled prefix measures still depend on \(\lambda\); the proof does not identify them as one common zero process.

On a fixed \(\eta\le y\le R\), the ratio \(Ty/S\) stays in a fixed compact subset of \((0,\infty)\). It therefore lies inside the source's logarithmic uniformity range for all large \(T\). The equality immediately before CCCC (3.9), not merely the inequalities labeled (3.9), gives
\[
K_S(Ty)/T=2yC_{Ty}+o(1)
\]
uniformly in both compact parameters. This is the legal reason the principal expression becomes independent of \(S\).

Stieltjes integration by parts differentiates only the explicit kernel. It does not differentiate \(C_U\), which may jump at zero heights, or the unknown source error. The resulting boundary and integral terms are exactly the author's equation (24).

## 4. Zero-height tails and the order of all limits

The positive rescaled prefix measure has \(K_S(Ty)/T\ll_g y\) in the source's intermediate range. The lower kernel estimate is
\(k_\lambda(y)\le\lambda^2/4\), and the upper one is \(k_\lambda(y)\le y^{-2}\). These prove
\[
O_g(\lambda^2\eta),\qquad O_g(1/R)
\]
for the two intermediate tails after taking the large-\(T\) limsup.

At the extreme ranges, the pointwise \(f_S(t)\ll_g\log^2(t+2)\) bound gives vanishing errors. More explicitly, the relevant source endpoints are
\[
y_{\rm low}=S/(T\log^3S),\qquad
y_{\rm high}=S\log^3S/T.
\]
At fixed \([a,L]\), the lower extreme error is of order
\(\lambda^2(S/T)/\log S\), and the upper is of order
\((T/S)/\log S\); both vanish uniformly. Their constants may depend on the fixed compact length range without harming the proof.

The **intermediate** limsup tail constants can be chosen independently of \([a,L]\): they use only the fixed-test spectral mass bound and the fact that the source prefix error has vanished in the first height limit. Consequently their length integrals are bounded by
\[
O_g\!\left(\eta\int_a^L\lambda^2e^{-\lambda}d\lambda\right)=O_g(\eta),
\quad O_g(1/R).
\]
This is the important distinction that permits removal of the length cutoffs before the \(y\)-cutoffs. It is explicitly accounted for in the final author version.

The valid order is therefore:

1. Fix all four auxiliary cutoffs and take the height limit in the **difference/error estimates**, without assuming \(C_T\) converges.
2. Remove the length cutoffs using actual arithmetic tail bounds on the left and uniform elementary kernel convergence on the fixed \(y\)-interval on the right.
3. Remove the \(y\)-cutoffs using the integrated tail bounds and bounded \(C_U\).

This proves an \(o(1)\) difference for the original all-length statistic. It is not an assertion of a source error rate for prescribed growing cutoffs.

## 5. The averaged kernel and its exact probability density

The elementary transform is
\[
\int_0^\infty e^{-\lambda}
\frac{\sin^2(\lambda y/2)}{y^2}\,d\lambda
=\frac1{2(1+y^2)}=:k_\infty(y).
\]
On a fixed compact \(y\)-interval, differentiating the length integral is legitimate by an integrable exponential times a polynomial in \(\lambda\). It has no connection to differentiating an asymptotic zeta formula.

The boundary term \(yk_\infty(y)C_{Ty}\) tends to zero at both ends because \(C_U\) is bounded for \(U\ge2\), with the declared bounded extension below that threshold. Hence
\[
-\frac4\pi yk_\infty'(y)
=\frac4\pi\frac{y^2}{(1+y^2)^2}=p(y),
\quad \int_0^\infty p(y)\,dy=1.
\]
The author's principal identity follows. The constant one is a consequence of this exact decreasing averaged kernel. It does not improve the single-length statistic by implication.

## 6. Exact bump, bounded-height convention, and consequences

Approximate the square root of the exact bump uniformly on a common compact positive-frequency interval, then square the smooth approximants. Section 3 supplies a uniform bound for the **all-length arithmetic mass** on that common support. The compact spectral mass bound controls the right side against \(p\).

Apply the identity at one fixed approximation, take the height limit, and then remove the approximation. No uniform Schwartz seminorm is required. Unlike a full-limit Abelian argument, this identity compares two height-dependent expressions directly and never needs a full limit for any approximating spectral statistic.

The convention \(C_U=D_U=0\) for \(U<2\) is harmless: the affected \(p\)-mass tends to zero as \(T\to\infty\), and all remaining finite heights form a bounded portion of the actual finite zero sums. Combining \(C_{\varepsilon,U}(0)\to A_\varepsilon\), nonnegativity, and the probability identity proves the non-strict upper bound, the averaged deficit identity, and the stated liminf/limsup interval.

Under AH-Pairs, the inherited full limit \(C_U\to A_\varepsilon\) gives equality at saturation by dominated convergence. No near-zero clustering parameter limit or simplicity assumption enters.

The report appropriately leaves reverse strict-subsequence transfer to a separate height-persistence argument. My independently authored R20 height lemma supplies such an argument, but it is not used to validate the present proof and creates no circular dependency.

## 7. Primary-source and replay record

The CCCC equation (1.3), weighted equation (3.8), and uniform equality before (3.9) were checked directly against the pinned source text. Its printed p.25 was already visually checked in my independently frozen R19 review; the same PDF hash is retained here. I also reread and visually checked Schoenfeld printed p.337, Theorem 10, equation (6.2), confirming the RH bound for \(\Psi(x)-x\) and the threshold \(73.2\). Extending the constant over a bounded initial interval is valid.

The inaccessible Goldston–Gonek/Goldston pages mentioned in the report are not extra assumptions. The exact reparameterization makes those unverified general-length formulas unnecessary.

I read the complete 3,012-byte symbolic checker. A temporary copy of both the checker and its pinned author report ran with SymPy 1.14.0. All thirteen symbolic assertions passed; stdout and the regenerated JSON are each byte-identical to the original:
7262ab47eb028f0e2453ca2139a16bd0f78b478e57bc7a80e3680e3eb6f2bf8e.

The receipt retains every symbolic field, including the normalized kernel, density, cumulative function, interval-length identity, exact \(\kappa\), length-tail factor and endpoint values. Fifteen author/dependency pins were checked for both size and SHA256. The separate syntax checker was hash-verified but not rerun, as requested; no numerical zero or prime scan was performed.

The companion receipt pins this review and all checked source/artifact versions. No author, source, earlier-round or Git file was modified.

**Accepted conclusion:** under RH the actual positive, exactly centered all-length variance is a probability average of the same fixed spectral bump over multiplicative heights, up to \(o(1)\), and has upper limit at most the AH value. No strict actual arithmetic deficit is established.

