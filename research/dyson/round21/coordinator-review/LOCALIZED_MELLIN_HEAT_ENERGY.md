# The actual length-averaged prime variance as localized heat energy

Round 21, 2026-09-05. Author: root. Status: complete ordinary proof submitted for independent review. Assumption: RH. No novelty claim or strict arithmetic bound is made.

This result supplies an analytic representation of the exact R20 arithmetic target. The heat acts on the logarithmic prime coordinate, not on moving zeta zeros. It is neither Dyson Brownian motion nor the de Bruijn–Newman zero flow.

## 1. Definitions and statement

Let \(E(x)=\Psi(x)-x\), where \(\Psi(x)=\sum_{n\le x}\Lambda(n)\) includes all prime powers. Define on the whole real line
\[
F(v)=e^{-v/2}E(e^v).
\tag{1}
\]
For \(v<0\), this is simply \(-e^{v/2}\). Under RH, the classical Chebyshev estimate gives
\[
|F(v)|\le C(1+v_+)^2
\tag{2}
\]
for one fixed constant and all real \(v\).

Use exactly the R20 fixed nonnegative smooth weight \(\omega\), supported on \([a,b]=[7/4,9/4]\), and put
\[
\eta=\sqrt\omega,\qquad L=\log T,\qquad
g_T(v)=\eta(v/L)F(v),\qquad T\ge2.
\tag{3}
\]
The square root is in \(H^1(\mathbb R)\), as proved below. The function \(g_T\) is compactly supported and in \(L^2\); it is not assumed differentiable across prime-power jumps.

Adopt the angular Fourier convention
\(\widehat g(\xi)=\int_{\mathbb R}g(v)e^{-i\xi v}dv\).
Write
\[
a_T=T-\tfrac12,\qquad
M_T(\xi)=\frac{2T-1}{T-1}
 \frac{\xi^2+1/4}{a_T^2+\xi^2}.
\tag{4}
\]

**Theorem.** For the actual exactly centered all-length variance of R20,
\[
\boxed{
\overline V_T
=\frac{T}{2\pi L^2}
 \int_{\mathbb R}M_T(\xi)|\widehat g_T(\xi)|^2d\xi
+O_\omega\!\left(\sqrt{\frac LT}\right).
}
\tag{5}
\]
The implied constant can depend on the fixed weight and a valid RH Chebyshev/Selberg bound; no numerical value is asserted.

Equivalently, if \(H_t=e^{t\partial_v^2/2}\) is the ordinary heat semigroup on the real \(v\)-line, put
\[
\mathcal E_T=
\int_0^\infty e^{-a_T^2t}
\left(\|\partial_v H_tg_T\|_2^2+
 \tfrac14\|H_tg_T\|_2^2\right)dt.
\tag{6}
\]
Then
\[
\boxed{
\overline V_T
=\frac{T(2T-1)}{(T-1)L^2}\mathcal E_T
+O_\omega\!\left(\sqrt{\frac LT}\right).
}
\tag{7}
\]
The integral exists even though \(g_T\) may have jumps. The derivative acts only after positive heat time, and the time integral is justified by a bounded Fourier multiplier.

A sufficient condition for exclusion of full AH-Pairs under RH is consequently
\[
\liminf_{T\to\infty}\frac{2T}{L^2}\mathcal E_T<A,
\tag{8}
\]
where \(A=1+\varepsilon^2m_1\) is the R20 saturation value. Condition (8) is not proved. The inherited non-strict upper bound supplies only a limiting upper bound \(A\) for the same normalized energy.

## 2. The actual square-root cutoff has enough regularity

A nonnegative \(C^2\) function \(\omega\) on \(\mathbb R\), with bounded second derivative \(M=\|\omega''\|_\infty\), satisfies
\[
|\omega'(x)|^2\le2M\omega(x).
\tag{9}
\]
If \(M=0\), a compactly supported such function vanishes identically, a trivial case. Otherwise Taylor's upper bound at \(h=-\omega'(x)/M\) gives
\[
0\le\omega(x+h)\le
\omega(x)-\frac{|\omega'(x)|^2}{2M}.
\]
On each component where \(\omega>0\), the derivative of its square root therefore obeys
\[
|\eta'(x)|=\frac{|\omega'(x)|}{2\sqrt{\omega(x)}}
\le\sqrt{M/2}.
\]
Continuity at the zeros extends this Lipschitz bound across components. Since the support is compact, \(\eta\in H^1\cap L^\infty\). No extra smoothness assumption on \(\sqrt\omega\) is needed.

For \(\eta_L(v)=\eta(v/L)\), the standard translation estimate follows directly by integrating its weak derivative and applying Cauchy–Schwarz:
\[
\|\eta_L(\,\cdot-u)-\eta_L\|_2^2
\le u^2\|\eta_L'\|_2^2
=\frac{u^2}{L}\|\eta'\|_2^2.
\tag{10}
\]
It holds for every real \(u\), not just a small translation.

## 3. Convert the exactly centered prime square

Put \(x=e^v\) and \(u=\lambda/T\). The continuous center retained in R20 gives exactly
\[
\Psi(e^ux)-\Psi(x)-(e^u-1)x
=E(e^{v+u})-E(e^v)
=e^{v/2}\bigl(e^{u/2}F(v+u)-F(v)\bigr).
\tag{11}
\]
Since \(dx/x^2=e^{-v}dv\), the two exponential factors cancel. Therefore, with the measure
\[
d\mu_T(u)=T e^{-Tu}du,\qquad u\ge0,
\]
the exact variance is
\[
\overline V_T=\frac{T}{L^2}B_T,\qquad
B_T=\int_0^\infty\int_{\mathbb R}
\left|\eta_L(v)
 [e^{u/2}F(v+u)-F(v)]\right|^2dv\,d\mu_T(u).
\tag{12}
\]
This identity does not split separately divergent prime/mean series and is valid at \(T=2\) under the centered RH integrability result.

Consider instead the genuine translation quadratic form
\[
Q_T(g)=\int_0^\infty
 \|e^{u/2}g(\,\cdot+u)-g\|_2^2\,d\mu_T(u).
\tag{13}
\]
It is finite for every \(g\in L^2\) and every \(T>1\): the triangle bound reduces it to a constant times
\(\|g\|_2^2\int T e^{-Tu}(e^u+1)du\).

The two vectors inside (12) and \(Q_T(g_T)\) differ by
\[
e^{u/2}\bigl(\eta_L(v+u)-\eta_L(v)\bigr)F(v+u).
\tag{14}
\]
This is the localization commutator. Discarding it without a bound would incorrectly assume that the moving arithmetic endpoint leaves the cutoff unchanged.

## 4. A quantitative localization error

Let \(R_T\) be the squared norm of (14) in the product space \(dv\,d\mu_T(u)\). Substitute \(w=v+u\). When the cutoff difference is nonzero, \(w\) lies in the union of \([aL,bL]\) and \([aL+u,bL+u]\), hence between \(aL\) and \(bL+u\). Equations (2) and (10) imply
\[
R_T\le
\frac{C^2\|\eta'\|_2^2}{L}
\int_0^\infty T e^{-(T-1)u}
u^2(1+bL+u)^4du.
\tag{15}
\]
This is finite even at \(T=2\). Expanding the fourth power evaluates its upper bound explicitly:
\[
R_T\le
\frac{C^2\|\eta'\|_2^2}{L}
\sum_{k=0}^4 {4\choose k}(1+bL)^{4-k}
\frac{(k+2)!\,T}{(T-1)^{k+3}}
=O_\omega(L^3/T^2).
\tag{16}
\]
The final estimate is asymptotic as \(T\to\infty\); the preceding expression covers every \(T\ge2\).

The already proved RH Selberg/length-tail estimates in R20 give a uniform bound on \(\overline V_T\), so (12) yields
\(B_T=O_\omega(L^2/T)\).
This bound was proved from the actual arithmetic integral and does not use the new heat representation.

The elementary Hilbert-space inequality
\[
|Q_T(g_T)-B_T|\le2\sqrt{B_TR_T}+R_T
\tag{17}
\]
now gives
\[
\frac{T}{L^2}|Q_T(g_T)-B_T|
=O_\omega\!\left(\sqrt{\frac LT}+\frac LT\right)
=O_\omega\!\left(\sqrt{\frac LT}\right).
\tag{18}
\]
This proves a quantitative localization error with the fixed, actual bump. No changing test-function constants or asymptotic approximation of a square root is involved.

## 5. Exact Fourier and heat calculation

For fixed \(u\), Plancherel gives the multiplier
\(\left|e^{u/2+i\xi u}-1\right|^2\).
Its integral against \(d\mu_T\), for \(T>1\), is
\[
\begin{aligned}
\int_0^\infty T e^{-Tu}
 |e^{u/2+i\xi u}-1|^2du
&=\frac{T}{T-1}+1
-\frac{2T(T-1/2)}{(T-1/2)^2+\xi^2}\\
&=\frac{2T-1}{T-1}
 \frac{\xi^2+1/4}{(T-1/2)^2+\xi^2}
=M_T(\xi).
\end{aligned}
\tag{19}
\]
Tonelli applies to the original nonnegative integrand. Thus
\[
Q_T(g)=\frac1{2\pi}\int M_T(\xi)|\widehat g(\xi)|^2d\xi.
\tag{20}
\]
Combining this exact formula with (18) proves (5).

In operator notation the multiplier is
\[
\frac{2T-1}{T-1}
(-\partial_v^2+1/4)(-\partial_v^2+a_T^2)^{-1}.
\tag{21}
\]
This denotes a bounded nonnegative operator on \(L^2\). It is not an assertion that the unsmoothed distributional derivative of the staircase is square integrable.

Finally,
\[
\frac{\xi^2+1/4}{a_T^2+\xi^2}
=\int_0^\infty e^{-a_T^2t}
(\xi^2+1/4)e^{-t\xi^2}dt.
\tag{22}
\]
Nonnegative integration and Plancherel identify the right side with the integrated heat energy (6). Since the ratio on the left is bounded for fixed \(T>1\), the time-integrated energy exists for all \(g\in L^2\), even at its jump discontinuities. This proves (7).

As \(T\to\infty\), the extra factor \((2T-1)/(T-1)\) tends to two. The inherited bound on \(\overline V_T\), together with (18), bounds the correspondingly normalized \(\mathcal E_T\). Consequently replacing that factor by two introduces only \(o(1)\), which justifies the limiting sufficient condition (8).

## 6. What this representation adds and what it does not

The logarithmic-coordinate RH error \(F\) contains the actual prime-power staircase and its exact continuous subtraction. Its localized Fourier energy is measured by an explicit positive resolvent multiplier. The same quantity is an integrated ordinary heat-gradient energy. Thus one may try estimates for this specific arithmetic function using analytic operator methods without inventing a stochastic law or transferring a matrix model to zeta.

This representation by itself supplies no better arithmetic estimate. The crude bound (2) implies only \(\|g_T\|_2^2=O(L^5)\); using the supremum of the multiplier would give an unusable bound of order \(TL^3\) for the normalized energy. The useful non-strict constant \(A\) still comes from the existing low-band information and prime/zero transfer. A strict improvement must exploit additional structure in the actual localized error, beyond a generic \(L^2\) norm or the elementary positivity of the heat operator.

The heat parameter here scales as \(T^{-2}\) in the logarithmic prime variable. This is not the \(H_t\) deformation of zeta zeros. No statement about zero trajectories, collision time, ACUE-to-zeta transport or the de Bruijn–Newman constant follows from (7).

All assertions concern a fixed weight and asymptotic height with a proved error bound. The numerical constant in that error is not evaluated; no finite-height zero-pair certificate is claimed. Priority and broader equivalence with classical variance formulas require a separate literature audit.

## Inputs and check scope

- R20 EXPONENTIAL_LENGTH_AVERAGE.md, final SHA256 cd8c2f7dc48530ed02f915dd202c8aedaaaadb1096cafc019beeb595b9beebbe: exact centered statistic, RH existence, fixed-window Selberg/length-tail bound and saturation value.
- R20 MULTIPLICATIVE_HEIGHT_EQUICONTINUITY.md, final SHA256 6048b8792084d1523212ddd5f0c05dcc5b54fb158c3dab37762675e91a1072fe: the separate strict-deficit implication, used only to state the consequence of (8).
- Schoenfeld Theorem 10 (6.2), in the already retained primary paper: the RH Chebyshev error bound used in (2). No explicit numerical constant is needed.
- The rest is the displayed translation, Taylor, Plancherel and Laplace calculation. A separate tiny symbolic checker will verify only these elementary identities. Independent ordinary proof review is still required.
