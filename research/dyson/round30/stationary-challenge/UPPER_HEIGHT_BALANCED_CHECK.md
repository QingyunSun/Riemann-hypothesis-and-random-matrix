# Independent check: a vanishing balanced block strictly above height T squared

Date: 2026-09-07. Author: stationary-challenge agent, independently checking the root investigator's proposed extension. Status: ordinary proof submitted for review. This is an application of classical consequences of RH to a local arithmetic block. No novelty, global variance deficit, AH contradiction, or Montgomery–Dyson theorem is claimed.

## 1. Verdict and exact statement

The proposed extension is valid with the genuine unmasked Möbius coefficients. A fixed second-order Sobolev estimate already handles every high Mellin frequency, so no growing derivative order or pointwise Möbius bound outside a polynomial frequency range is required.

Fix \(0<\delta\le1/4\), let

\[
X=T^\alpha,\quad 2+\delta\le\alpha\le9/4,\quad
Y=X/T,\quad \ell=\log T,\quad D,K\asymp\sqrt X,
\]

where the comparison constants lie in fixed compact subsets of \((0,\infty)\). Keep the actual \(b_T\), fixed smooth \(\chi,V\in C_c^\infty((1,2))\), and the sharp odd intervals \(D<d\le2D\), \(K<k\le2K\). Define

\[
F(x,h)=b_T(x)\chi(x/X)V(h/Y)(1+h/x)^{-T},
\]

\[
Z_{D,K}=2\sum_{d,k\text{ in these sharp odd intervals}}
\mu(d)\log k\sum_{h\text{ even}}F(dk,h)[\Lambda(dk+h)-2].
\tag{1}
\]

Under ordinary RH,

\[
\boxed{
Z_{D,K}\ll
\frac{T^{-141/800}}{\sqrt{\log T}}+T^{-3\delta/4}=o(1),}
\tag{2}
\]

uniformly in the stated closed height range and fixed comparison constants. The exponent in the first term is a convenient choice, not an optimized exponent. The result preserves the odd center 2, all prime powers at odd endpoints, the exact smooth product/shift cutoffs, and both sharp factor endpoints.

It is a result for the whole fixed balanced block (1), not just its primitive progression discrepancy. It does not allow an arbitrary mask on the d interval, does not include \(\alpha=2\), and does not settle the noncentral shift or unbalanced blocks of the global variance.

## 2. The exact extension and the two inherited energies

Put

\[
A(x)=X\ell^2b_T(x)\chi(x/X),\qquad
k(x,u)=V((u-x)/Y)(x/u)^T,
\]

\[
f(x)=A(x)\sum_{n\text{ odd}}k(x,n)[\Lambda(n)-2].
\tag{3}
\]

The integer prime variable \(n\) stays fixed under differentiation. The function \(f\) is supported compactly inside \((X,2X)\), and at odd integers \(m\),

\[
f(m)=X\ell^2\sum_{h\text{ even}}F(m,h)[\Lambda(m+h)-2].
\]

Consequently the R29 Mellin identity remains exact:

\[
Z_{D,K}=\frac1{\pi X\ell^2}\int_{\mathbb R}
\widehat f(t)M_D(t)B_K(t)\,dt,
\tag{4}
\]

with the same positive phases in the two Dirichlet polynomials. For each fixed nonnegative integer \(j\), the R29 proof generalizes to

\[
\int_{\mathbb R}(1+(t/T)^2)^j|\widehat f(t)|^2dt
\ll_j Y\ell^2,
\tag{5}
\]

\[
\int_{\mathbb R}\frac{|\widehat f(t)|^2}{1+t^2}dt
\ll\frac X{T^2}.
\tag{6}
\]

Here are the scale checks needed for this extension; they must not be inferred from the special identity \(X=T^2\).

The fixed-order derivatives of \(A\) in \(x\partial_x\) remain bounded uniformly. The exact primitive expression for \(b_T\) has mass \(1/(T-1)\) and only differentiates the fixed \(\omega\). In the fixed-prime-variable derivative recurrence, \(x/Y\asymp T\), so the kernel bounds are still \(O_j(T^j)\) and \(O_j(T^j/Y)\) after one additional shift derivative.

For the prime increment, retain the R29 change of variables \(\lambda=Ty/x\). The relevant enclosing interval is the fixed \([1/2,2]\), and \(dy=(x/T)d\lambda\). For \(S=T/\lambda\), the full x range \([X,2X]\) lies in \([1,S^3]\), uniformly for all sufficiently large \(T\) and \(\alpha\le9/4\). Thus the fixed-parameter Selberg integral with \(\beta=3\) gives

\[
\int_X^{2X}\int_Y^{2Y}|E(x+y)-E(x)|^2dy\,dx
\ll\frac{X^3\ell^2}{T^2}=XY^2\ell^2.
\]

Combining this with fixed-prime-variable partial summation proves (5). The lambda integration is retained. No uniform theorem with a growing beta or a growing derivative order is invoked.

For (6), the exact R29 decomposition is \(f(e^v)=G'(v)+R(v)\), with

\[
S(x)=\int E(u)k(x,u)du,\qquad G(v)=A(x)S(x)/x.
\]

Restrict x to \([X,2X]\) when applying Schur. Cramér's RH mean square and the two kernel sections of length \(O(Y)\) give

\[
\int_X^{2X}|S(x)|^2dx\ll Y^2X^2.
\]

The squared logarithmic-coordinate norms of \(G\) and the main terms of \(R\) are therefore \(O(Y^2/X)=O(X/T^2)\). The identity

\[
\partial_xk+\partial_uk=T(1/x-1/u)k
\]

still has the multiplier \(O(1/X)\), since \(u-x\asymp X/T\). The odd-lattice correction has squared norm \(O(Y^{-2})\), and the powers-of-2 correction has squared norm \(O(Y/X)=O(1/T)\). Both are bounded by \(O(X/T^2)\) in the present range. The original prime powers are consequently not discarded. Plancherel proves (6).

All constants in (5), (6) are uniform over the stated alpha interval. In what follows only \(j=0\), \(j=2\), and (6) are needed.

## 3. Genuine Möbius twist: source and sharp Perron check

The primary statement independently read is Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann Hypothesis*, printed page 4 (PDF page index 5), equation (3): under RH the reciprocal zeta function is subpolynomial in height uniformly a fixed positive distance to the right of the critical line. The paper cites Titchmarsh, Theorem 14.2. [Author-hosted PDF](https://www.isibang.ac.in/~statmath/eprints/2005/isibc200535.pdf).

Only that reciprocal-zeta estimate is imported here. The following sharp Perron consequence is derived independently, avoiding the parameter notation in the sketch of its Lemma 3:

\[
\boxed{
|M_D(t)|\ll_{C,\eta}D^{1/2+\eta}
\quad\text{for}\quad |t|\le D^C,}
\tag{7}
\]

for each fixed \(C>0\) and sufficiently small fixed \(\eta>0\).

For an endpoint \(u\asymp D\), choose \(x=\lfloor u\rfloor+1/2\), so \(n<x\) is exactly \(n\le u\) for integral n. Set \(c=1+1/\log x\), \(p=C+2\), and choose \(H\asymp D^p\). On \(\Re s>1\), the exact odd twisted Dirichlet series is

\[
Q_t(s)=\sum_{n\text{ odd}}\mu(n)n^{it-s}
=\frac1{(1-2^{-s+it})\zeta(s-it)}.
\tag{8}
\]

The half-integer truncated Perron formula gives

\[
\sum_{n\le u,\ n\text{ odd}}\mu(n)n^{it}
=\frac1{2\pi i}\int_{c-iH}^{c+iH}Q_t(s)\frac{x^s}{s}ds
+O(x\log(xH)/H).
\tag{9}
\]

The error is uniform in t because the coefficients have absolute value at most one. The half-integer distance controls the near-endpoint terms in the usual truncated indicator estimate.

Shift to \(\sigma_0=1/2+\eta/4\). Under RH no pole of \(Q_t\) lies in this rectangle. The zeta pole produces a reciprocal zero, not a residue, and the odd Euler factor has poles only at real part zero. On the rectangle the odd factor is bounded by \((1-2^{-\sigma_0})^{-1}\). Choose the reciprocal-zeta exponent \(\varepsilon=\eta/(4p)\). Since \(|t|\le D^C\) and \(H\asymp D^p\),

\[
|Q_t(s)|\ll_{C,\eta}H^\varepsilon.
\]

The new vertical integral is

\[
O(x^{1/2+\eta/4}H^\varepsilon\log H)
=O(D^{1/2+3\eta/4}),
\]

after absorbing \(\log H\ll D^{\eta/4}\). The horizontal integrals are \(O(xH^{\varepsilon-1})\), and the Perron error is smaller. Subtracting the two exact endpoint sums proves (7).

It is useful to specify \(H\) comparable to the declared fixed power, rather than merely impose an unrestricted lower bound on \(H\), because the reciprocal-zeta exponent allocation uses that power. No gamma factor, exceptional zero assumption, GRH, or residue at the critical line enters this argument. The contour stays a fixed positive distance to its right.

## 4. Low and middle frequencies

Put

\[
L=\sqrt T\,\ell,\qquad R_0=\pi K/2.
\]

For large T, \(1<L<R_0\). The sharp odd first-derivative bound from R29 is

\[
|B_K(t)|\ll\frac{K\ell}{1+|t|},\qquad |t|\le R_0.
\tag{10}
\]

All frequencies in this range satisfy \(|t|\le D^2\) for large T, uniformly in the comparison constants. Thus use (7) with the fixed value \(C=2\).

On \(|t|\le L\), combine (6), (7), (10), and Cauchy with the interval's length. Its normalized contribution is at most

\[
\frac{KD^{1/2+\eta}\ell}{X\ell^2}
\frac{\sqrt X}{T}\sqrt L
\ll\frac{D^{1/2+\eta}\sqrt L}{T\ell}.
\tag{11}
\]

The factor comparing \(\sqrt{1+t^2}\) with \(1+|t|\) is bounded. On \(L<|t|\le R_0\), use (5) with \(j=0\), and \(\int_{|t|>L}t^{-2}dt\ll1/L\). This contribution is at most

\[
\frac{KD^{1/2+\eta}\ell}{X\ell^2}
(\sqrt Y\ell)L^{-1/2}
\ll\frac{D^{1/2+\eta}}{\sqrt{TL}}.
\tag{12}
\]

At the displayed choice of L, (11), (12) are both

\[
\ll\frac{D^{1/2+\eta}}{T^{3/4}\sqrt\ell}
\ll\frac{T^{(\alpha-3)/4+\alpha\eta/2}}{\sqrt\ell}.
\tag{13}
\]

Taking \(\eta=1/100\), the maximum exponent for \(\alpha\le9/4\) is

\[
-\frac3{16}+\frac9{800}=-\frac{141}{800}.
\]

The actual reciprocal-zeta input matters here. Replacing \(\mu(d)\) by arbitrary bounded coefficients would invalidate (7) and the low/middle saving. Direct partial summation of an untwisted Mertens bound would also lose a factor of order t; that weaker route is not being used.

## 5. All high frequencies, with no Perron range restriction

For dyadic \(R\ge R_0\asymp K\asymp D\), R29's unconditional mean-value and second-derivative estimates give

\[
\|M_D\|_{L^2(R<|t|\le2R)}\ll\sqrt{RD},
\qquad
\|B_K\|_{L^\infty(R<|t|\le2R)}\ll\sqrt R\,\ell.
\tag{14}
\]

Both are valid for arbitrarily high R. The latter is allowed to be weaker than the trivial bound for very large R; it remains an upper bound. No pointwise Möbius estimate is used here.

Equation (5) gives

\[
\|\widehat f\|_{L^2(R<|t|\le2R)}
\ll_j\sqrt Y\,\ell(T/R)^j.
\]

The normalized contribution on one such band is therefore

\[
\ll_j\frac{R\sqrt{YD}}{X}(T/R)^j
\asymp_j\frac{R}{\sqrt{DT}}(T/R)^j.
\tag{15}
\]

The constants implicit in the last comparison depend only on the fixed bounds for \(D/\sqrt X\). With \(j=2\), sum the geometric series starting at \(R_0\). The complete high-frequency contribution is

\[
\ll (T/D)^{3/2}
\ll T^{-3(\alpha-2)/4}
\le T^{-3\delta/4}.
\tag{16}
\]

This proves (2), including both signs and frequencies beyond every fixed polynomial range of t. The fixed separation \(\alpha\ge2+\delta\) is essential: at \(\alpha=2\), the right side of (16) is only bounded, reproducing the R29 carrier obstruction.

## 6. Comparison with the full R23 proof

I read all of `research-round23/even-pair-dispersion/UPPER_WING_SHIFT_COMPLETION.md`, SHA256 `2ff5ea968ea2adc76d40fc81a65c23cba5b143593e61c71bbc5c5f30ffc0a1a5`, not just its checkpoint summary.

R23 proves that a primitive progression discrepancy and a nonprimitive component vanish for its specified complementary-modulus owner family. It retains the exact primitive principal and complementary divisor terms. Its unresolved expression is explicitly \(\mathcal A_{\mathcal D}+\mathcal C_{\mathcal D}-\mathcal M_{\mathfrak S}\). Consequently R23 does not already prove the complete sharp balanced block (1) is \(o(1)\).

Conversely, (7) uses the full odd Möbius Dirichlet series. It cannot simply be applied to the owner-masked polynomial in R23. The two results are different local eliminations; this proof is not a bound on each piece of the R23 decomposition separately. Their overlap in physical height is not a reason to identify their arithmetic coefficients or their conclusions.

## 7. Remaining scope and reproducibility

The result removes the full balanced packet at heights separated by a fixed power from \(T^2\). It does not improve the \(T^2\) carrier correlation, settle the union of all height/shift/cofactor packets, identify a signed global constant, or contradict AH. Those are separate missing steps.

Programme source: corrected R29 `SIGNED_MELLIN_BLOCK_BOUND.md`, SHA256 `753f116b8ebc5d6cc7d7a4e148c98e9b8ef9df97d4327efe2fa094507aa13492`, read in full. The R29 source chain supplies the fixed-beta Selberg bound, Cramér mean square, Montgomery–Vaughan mean-value theorem, and sharp odd cofactor estimates. Bagchi equation (3) was independently read from its author-hosted PDF during this check. No other part of that paper is used as an unexamined black box.

The adjacent finite checker passed 12 exact exponent, norm-scale, and odd Euler-factor identities. It does not certify the analytic contour shift, prove RH, estimate numerical asymptotic constants, or run a new prime calculation. A KaTeX syntax check was attempted but is unavailable: the existing Dropbox-hosted module returned an empty export object, so no mathematical syntax acceptance is claimed for this note. The runtime failure is recorded separately and is not a mathematical test failure.
