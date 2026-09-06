# The actual-zeta two-scale target: short-prime projection and a centered tail

Date: 2026-09-05. Status: ordinary analytic identities and an explicit remaining inequality. The requested lower bound \(1/16\) is **not proved**. This note does not claim a new theorem about zeta zeros. Round 7 is unchanged.

The useful outcome is a precise arithmetic decomposition. The part supplied by short primes is positive and completely evaluable. The remaining term is one **signed difference of actual residual energies**, with an absolutely convergent representation involving ψ(x)−x under RH. Positivity of the von Mangoldt coefficients does not control that signed difference.

## 1. Definitions and the resulting obligation

Write

\[
s_c(t)=\frac12+\frac{c}{\log T}+it,
\qquad H_c(t)=-\frac{\zeta'}{\zeta}(s_c(t)),
\qquad I_T(c)=\int_0^T|H_c(t)|^2dt,
\]

where c>0 is fixed, and

\[
W_T=\frac2{T\log^2T}
\left(\sinh(2)I_T(1)-\sinh(1)I_T(1/2)\right).
\tag{1}
\]

Set \(N=\lfloor T/\log^6T\rfloor\), for sufficiently large T, and define the genuine finite polynomials

\[
P_c(t)=\sum_{n\le N}\frac{\Lambda(n)}{n^{s_c(t)}},
\qquad R_c(t)=H_c(t)-P_c(t).
\tag{2}
\]

Under RH, the contour calculation below proves

\[
\boxed{
W_T=B+\mathcal E_T+o(1),
\quad
\mathcal E_T=\frac2{T\log^2T}
\left(\sinh(2)\|R_1\|_2^2-
\sinh(1)\|R_{1/2}\|_2^2\right),}
\tag{3}
\]

where all norms are over [0,T] and

\[
\begin{aligned}
B&=2\int_0^1u\left(\sinh(2)e^{-2u}-\sinh(1)e^{-u}\right)du\\
&=\frac{e^2}{4}-e+\frac54+\frac1e
-\frac9{4e^2}+\frac3{4e^4}\\
&=0.4560939793292317215\ldots.
\end{aligned}
\tag{4}
\]

Thus the precise remaining task is

\[
\boxed{\liminf_{T\to\infty}\mathcal E_T
\ge\frac1{16}-B
=-0.3935939793292317215\ldots.}
\tag{5}
\]

By (3), (5) is equivalent to the requested lower bound for W_T. Equation (5) is not deduced here from RH. The existing Round 7 AH calculation gives a limiting W below 1/16, so treating (5) as a consequence of formal coefficient positivity would be circular progress.

## 2. An exact continuation from centered prime counting

Put \(E(x)=\psi(x)-x\), with \(\psi(x)=\sum_{n\le x}\Lambda(n)\). At an integer cutoff, ψ includes the atom at that integer. Assuming RH, the classical bound

\[
E(x)=O\!\left(x^{1/2}\log^2(2x)\right)
\tag{6}
\]

implies that, for every s with Re(s)>1/2 and s≠1,

\[
\boxed{-\frac{\zeta'}{\zeta}(s)
=\frac{s}{s-1}
+s\int_1^\infty E(x)x^{-s-1}dx.}
\tag{7}
\]

The integral in (7) is absolutely convergent. To prove it, first take Re(s)>1, use Stieltjes integration by parts in the absolutely convergent von Mangoldt series, and subtract the integral of x. Both sides then continue meromorphically to Re(s)>1/2. RH excludes logarithmic-derivative poles from this open region except the pole at s=1. The residue of the right side at s=1 is +1, as required for −ζ′/ζ. No critical-strip Dirichlet series has been expanded.

For any real X≥1, finite summation by parts gives

\[
\boxed{
-\frac{\zeta'}{\zeta}(s)
=\sum_{n\le X}\Lambda(n)n^{-s}
+\frac{X^{1-s}}{s-1}
-E(X)X^{-s}
+s\int_X^\infty E(x)x^{-s-1}dx.}
\tag{8}
\]

Consequently the residual in (2) is **exactly**

\[
R_c(t)=\frac{N^{1-s_c(t)}}{s_c(t)-1}
-E(N)N^{-s_c(t)}
+s_c(t)\int_N^\infty E(x)x^{-s_c(t)-1}dx.
\tag{9}
\]

The positive prime coefficients have therefore been replaced in the tail by a centered, signed arithmetic error. The pole term is part of the identity; it cannot be discarded before estimating it at the chosen scale.

Equivalently, for fixed Re(s)>1/2 and s≠1,

\[
-\frac{\zeta'}{\zeta}(s)
=\lim_{M\to\infty}\left(
\sum_{n\le M}\Lambda(n)n^{-s}
+\frac{M^{1-s}}{s-1}\right).
\tag{10}
\]

For a fixed T the convergence is uniform on the two compact vertical segments used in (1). It is not an assertion that the unregularized Dirichlet series converges there. The order of limits in (10), followed by any T asymptotic, must be retained unless a uniform remainder is proved.

## 3. A quantitative bound that exposes the limitation of pointwise RH

Write δ=Re(s)−1/2>0 and ℓ=log X, with X≥2. Formula (6) implies

\[
\left|-E(X)X^{-s}+s\int_X^\infty E(x)x^{-s-1}dx\right|
\ll X^{-\delta}\left[
(\ell+1)^2+|s|\left(
\frac{(\ell+1)^2}{\delta}
+\frac{2(\ell+1)}{\delta^2}
+\frac2{\delta^3}\right)\right].
\tag{11}
\]

This follows by integrating \(x^{-1-\delta}(\log x+1)^2\) explicitly; the implied constant is the one in (6), up to an absolute factor. At δ=c/log T, X=T^θ with fixed θ>0, and t≤T, (11) supplies only

\[
O_{c,\theta}(T\log^3T),
\tag{12}
\]

which is far larger than the natural mean-square scale. Integrating the square of this estimate gives O(T³ log⁶T), whereas (1) is normalized by T log²T. This explicitly identifies a failure of the **pointwise RH estimate used in (6)**, not a proof that every possible consequence of RH is insufficient.

Trying to repair this particular absolute-value bound by making \(X^{-\delta}\) as small as a negative power of T forces log X to be of order (log T)². Such a cutoff destroys the short-polynomial mean-value regime. It is not a support extension obtained for free.

## 4. The actual mixed-integral lemma

For fixed c>0, T sufficiently large, \(3\le N\le T\), and

\[
\sigma=\frac12+\frac c{\log T},\quad
P(t)=\sum_{n\le N}\Lambda(n)n^{-\sigma-it},\quad
D=\sum_{n\le N}\Lambda(n)^2n^{-2\sigma},
\]

assume σ≤3/4 and \(\beta=1+1/\log N\le2\). Under RH,

\[
\int_0^T\left(-\frac{\zeta'}{\zeta}(\sigma+it)\right)
\overline{P(t)}dt
=TD+O_c(N\log^3T).
\tag{13}
\]

This is a complex identity with a bounded complex error. In particular its real part has the same main term.

**Contour and pole control.** Use

\[
F(s)=\left(-\frac{\zeta'}{\zeta}(s)\right)
\sum_{n\le N}\Lambda(n)n^{s-2\sigma}
\tag{14}
\]

on the rectangle from σ+i to β+iT. On the left side the finite sum is exactly \(\overline{P(t)}\). The pole at s=1 is below the rectangle, and RH places every nontrivial zero strictly to its left. The standard local partial-fraction estimate for the logarithmic derivative, together with O(log T) zeros in a unit interval, gives

\[
\frac{\zeta'}{\zeta}(u+iT)=O_c(\log^2T)
\quad(\sigma\le u\le\beta).
\]

Also

\[
\left|\sum_{n\le N}\Lambda(n)n^{u-2\sigma+iT}\right|
\le\sum_{n\le N}\log n\,n^{\beta-2\sigma}
\le eN\log N.
\]

The top integral is therefore O_c(N log³T). On the compact bottom segment, RH and finiteness of the number of nearby zeros give the sufficient bound \(O_c(\log T)\) for the logarithmic derivative: its distance to any nontrivial zero is at least c/log T, and the pole at s=1 has height zero. The bottom integral is thus \(O_c(N\log N\log T)\). The same compact RH bound on the initially omitted left interval \(0\le t\le1\), together with \(\sum_{n\le N}\Lambda(n)n^{-\sigma}\ll\sqrt N\log N\), bounds that interval by \(O_c(\sqrt N\log N\log T)\). These errors are absorbed by \(O_c(N\log^3T)\). No assumption that T avoids a zero ordinate, and no separately verified low-zero table, is needed.

**The right line is an honest absolutely convergent series.** At Re(s)=β>1,

\[
-\frac{\zeta'}{\zeta}(s)=\sum_{m\ge2}\Lambda(m)m^{-s}.
\]

The m=n terms of the vertical integral give (T−1)D. The absolute value of all other integrated terms is at most twice

\[
\sum_{n\le N}\Lambda(n)n^{\beta-2\sigma}
\sum_{\substack{m\ge2\\m\ne n}}
\frac{\Lambda(m)m^{-\beta}}{|\log(m/n)|}.
\tag{15}
\]

For n/2≤m≤2n, m≠n, the inner sum is

\[
O\!\left(n^{1-\beta}\log^2(2N)\right),
\]

by Λ(m)≤log m and the harmonic sum over |m−n|. After the outer factor is applied, summing over n costs O(N log³N), because \(n^{1-2\sigma}\le1\).

Outside that range the denominator is at least log 2, and

\[
\sum_{m\ge2}(\log m)m^{-\beta}
\ll(\beta-1)^{-2}\ll\log^2N.
\]

The remaining outer sum is O(N log N), since \(n^{\beta-2\sigma}\le N^{1/\log N}=e\). Thus the infinite right-line off-diagonal sum is O(N log³N). This completes (13). Neither an unproved long-polynomial mean value nor a critical-strip Dirichlet expansion has been used.

## 5. Orthogonal decomposition to leading order

An elementary finite-polynomial mean-value bound gives

\[
\|P\|_2^2=TD+O(N\log^4T).
\tag{16}
\]

For completeness, bound each non-diagonal integral by \(2/|\log(m/n)|\), use \(|\log(m/n)|\ge|m-n|/N\), then \(2|a_ma_n|\le|a_m|^2+|a_n|^2\), and sum the resulting harmonic series. This gives O(N log N Σ|a_n|²). Here \(\sum|a_n|^2\le\sum_{n\le N}(\log n)^2/n=O(\log^3N)\), proving the stated error. Sharper standard mean-value estimates are unnecessary.

Combining (13) and (16) gives

\[
\boxed{I_T(c)=TD+\|R_c\|_2^2+O_c(N\log^4T).}
\tag{17}
\]

This is an asymptotic projection identity for these specific coefficients, not a claim that the finite functions \(n^{-it}\) are exactly orthogonal on [0,T]. In particular, the cross term \(\langle R_c,P_c\rangle\) is O_c(N log⁴T), rather than identically zero.

With \(N=\lfloor T/\log^6T\rfloor\), the error in (17), divided by T log²T, is O_c(log⁻⁴T). The prime number theorem and partial summation give

\[
\frac D{\log^2T}\longrightarrow\int_0^1u e^{-2cu}du.
\tag{18}
\]

One may obtain (18) from Σ_{n≤x}Λ(n)²∼x log x; the contribution of prime powers of exponent at least two is negligible. Equations (17)–(18) prove (3). All leading constants and both values of c use the same cutoff N.

## 6. What the residual condition measures

The pole term in (9) is individually negligible in the normalized L² scale at this N:

\[
\int_0^T\left|\frac{N^{1-s_c(t)}}{s_c(t)-1}\right|^2dt
\ll_c N^{1-2c/\log T}\ll_c N.
\tag{19}
\]

Its denominator has real part bounded away from zero for sufficiently large T. Dropping it from **the residual energy** also requires a bound on the other factor in the cross term. The same RH partial-fraction estimate used in Section 4 gives the sufficient pointwise bound \(H_c(t)=O_c(\log^2T)\) on [0,T]. Equation (16) also gives \(\|P_c\|_2^2=O_c(T\log^4T)\). Thus \(\|R_c\|_2^2=O_c(T\log^4T)\), and Cauchy–Schwarz with (19) bounds the change of residual energy, divided by T log²T, by

\[
O_c\!\left(\sqrt{\frac NT}+\frac{N}{T\log^2T}\right)
=O_c(\log^{-3}T)=o(1).
\]

This weaker estimate is sufficient and makes the removal independent of the sharper Round 7 pair/resolvent bound.

Accordingly (5) can also be stated with

\[
\widetilde R_c(t)=-E(N)N^{-s_c(t)}
+s_c(t)\int_N^\infty E(x)x^{-s_c(t)-1}dx
\tag{20}
\]

in place of R_c. This version pinpoints the missing arithmetic information: a comparison of two Laplace-damped Fourier energies of the **same centered prime error**.

More explicitly, put \(e_N(v)=E(Ne^v)/(Ne^v)^{1/2}\), v≥0, and δ_c=c/log T. Then

\[
\widetilde R_c(t)=N^{-\delta_c-it}
\left[-e_N(0)+s_c(t)\int_0^\infty
e_N(v)e^{-\delta_cv-itv}dv\right].
\tag{21}
\]

The two copies of e_N are coupled. Replacing their energies by two unrelated nonnegative numbers loses actual analytic structure; asserting that the coupling forces (5) without proof is equally unjustified. A new usable estimate must exploit that common arithmetic function at precision sufficient for (5).

For orientation only, under the full sine/GUE prediction the normalized residual energy would be

\[
\frac{\|R_c\|_2^2}{T\log^2T}\longrightarrow\frac{e^{-2c}}{2c}.
\tag{22}
\]

Its signed contribution to (3) would be −0.3738225362077544… . Thus these residuals are leading-order objects, not errors tending to zero. Formula (22) is a model prediction, not an additional result of the contour lemma.

## 7. Why positive coefficients do not close the argument

For a finite polynomial with nonnegative coefficients, the diagonal coefficient in the two-scale difference is

\[
g(u)=\sinh(2)e^{-2u}-\sinh(1)e^{-u},
\quad u=\frac{\log n}{\log T}.
\]

It is negative for \(u>\log(2\cosh1)=1.126928011\ldots\). Even the one-term polynomial \(\Lambda(p)p^{-s}\), with \(T=p^{1/2}\) and p a sufficiently large prime, has a strictly negative two-scale squared-norm difference because g(2)<0. This is a counterexample to a **universal positive-coefficient quadratic-form assertion**, not a counterexample to the target for actual ζ.

Moreover, (10) has a mandatory continuous counterterm. At a real point s between 1/2 and 1 the finite positive prime sum grows, while (M^{1-s}/(s-1)) is negative and cancels that growth. Removing the counterterm changes the analytic function. These two obstacles survive before any sophisticated arithmetic estimate is attempted.

## 8. Verification and scope

The accompanying `check_centered_tail.py` records:

- exact rational enclosures for B and 1/16−B, obtained by enclosing e with its Taylor series and a geometric remainder;
- an independent finite-step integration-by-parts check of (8), with a finitely supported von Mangoldt measure and a completely evaluated tail, in its absolute-convergence half-plane;
- a comparison with actual ζ′/ζ at Re(s)=3, with an explicit bound on the omitted absolutely convergent von Mangoldt tail;
- small, labeled diagnostic evaluations of the **regularized** sum (10) at s=3/4, showing the size and sign of the mandatory counterterm. These finite diagnostics do not certify convergence rates in the critical strip.

The analytic proof, rather than the numerical checks, supplies continuation and the large-T statements. No numerical value of W_T has been inferred from the low-height examples.

Source inputs for the decomposition are standard RH consequences and the prime number theorem. Relevant primary background is [Goldston, *Notes on Pair Correlation of Zeros and Prime Numbers*](https://arxiv.org/abs/math/0412313), particularly the explicit-formula and mean-value discussion. The significance of the 1/16 threshold comes from the separate, independently reviewed Round 7 reduction using [Goldston–Lee–Schettler–Suriajaya, *Pair Correlation Conjecture II: The Alternative Hypothesis*](https://arxiv.org/abs/2507.06823). The full mixed-integral proof needed here is written in Section 4; neither the decomposition nor the removal of the pole term requires the stronger pair/resolvent estimate.

**Conclusion of this bounded test:** the short-prime main term can be rigorously isolated, and the actual arithmetic term that must improve is (5), equivalently (20)–(21). No lower bound beyond the existing information has been established. Further work should address this signed centered-prime energy rather than reusing coefficient positivity or omitting the pole subtraction.
