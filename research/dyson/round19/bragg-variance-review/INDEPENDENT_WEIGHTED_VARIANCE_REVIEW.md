# Independent review: weighted Selberg variance and the Bragg deficit

Reviewer: Euclid / prime186. Date: 2026-09-05. Verdict: **accepted within the stated RH-conditional scope**. No mathematical correction to the frozen author report is required.

Reviewed author file: BRAGG_WEIGHTED_SELBERG_VARIANCE.md, 21,201 bytes, SHA256
0c5323ac5a983148a9ec433ea1196fb0fd538f00872ac73e9de3ae105c7a2502.

I read the complete report and checker, checked the primary statements and relevant source ranges, visually inspected CCCC printed p.25, and replayed a copied checker independently. This acceptance concerns the reduction and its conditional consequences. It does not certify a variance deficit, an AH refutation, a new bound for actual primes, or a best-possible literature bound.

## 1. Source identity, normalization, and prefix uniformity

The retained CCCC PDF has SHA256
38dfbdd9f11dd435fde98b0e70466c53bb281f584cbb7debceb6521c8a4c58ac.
Printed p.25 is also PDF page 25. Direct visual reading confirms that its equation (3.8) has the unnormalized factor
\[
\frac2\pi\log^2T,
\qquad e^{2\kappa}=1+1/T,
\]
and two squared zero sums. Multiplication by \(T/\log^2T\) gives the author's \(2T/\pi\), and its source error \(O_g(1/T)\) becomes \(O_g(\log^{-2}T)\).

The unnumbered equality immediately before source (3.9) is crucial:
\[
\int_0^Y f(t,\eta)\,dt
=2Y\int_0^\infty F(\alpha,Y)|\widehat g(\alpha)|^2\,d\alpha+o_g(Y),
\]
uniformly for \(\eta\log^{-3}\eta\le Y\le\eta\log^3\eta\).
With \(\eta=T\), this is exactly the needed prefix comparison. It is stronger than the interval upper/lower inequalities subsequently labeled (3.9). In particular, the report has not mistaken those inequalities for an equality.

The two sums account for the factor two. The source uses all zero ordinates in this intermediate expression. No simplicity assumption, removed early-zero block, or change from \(Y\) to \(T^\beta\) is introduced. The bounded logarithmic ratio is a necessary part of the cited uniformity.

The support/plateau conditions on \(\widehat g\) used to majorize characteristic intervals enter the source comparison (3.7) and the inequalities in (3.9), not the underlying weighted Plancherel identity. The application to a fixed smooth compactly supported Fourier test is appropriate. Positive compact support avoids the pole/low-frequency endpoint concerns relevant in earlier packet work.

## 2. Full-limit transfer and tail bounds

Let
\[
G_T(y)=K_T(Ty)/T,\qquad c_T=T\kappa_T\longrightarrow\tfrac12.
\]
Direct substitution in the normalized source identity gives
\[
V_T=\frac2\pi\int_0^\infty
\frac{\sin^2(c_Ty)}{y^2}\,dG_T(y)+o(1).
\]
Thus the limiting kernel is \(k(y)=\sin^2(y/2)/y^2\), and
\[
\frac2\pi\int_0^\infty k(y)\,2A\,dy
=\frac{4A}{\pi}\frac{\pi}{4}=A.
\]
No extra factor \(T\), \(2\), \(\pi\), or \(\varepsilon^{-1}\) is missing.

I checked the four endpoint regimes independently.

* For \(0<y<\log^{-3}T\), the pointwise bound \(f_T(t)\ll_g\log^2(t+2)\), multiplied by the bounded small-\(y\) kernel, gives \(O_g(1/\log T)\).
* On the intermediate height range, the uniform prefix formula and compact spectral mass bound give \(G_T(y)\ll_g y\). Positivity then gives \(O_g(\eta)\) for \(0<y<\eta\).
* For \(R<y<\log^3T\), the kernel is at most \(y^{-2}\). Integration by parts with \(G_T(y)\ll_g y\) gives \(O_g(1/R)\), including both boundary terms.
* For \(y>\log^3T\), the pointwise bound gives
\[
\int_{\log^3T}^\infty \frac{\log^2(Ty+2)}{y^2}\,dy
=O(1/\log T).
\]
This is after the rescaled measure normalization.

These estimates are uniform for \(c_T\) in a fixed compact positive interval, so replacement by its limit is justified on a fixed central interval followed by removal of its ends. The conclusion concerns a full limit, not equality of the two statistics at a common height.

### Explicit completion of the smooth-square approximation argument

The original bump is smooth and nonnegative, but the report correctly does not assume its square root is a smooth compactly supported Fourier transform. Choose all approximants on one compact interval \(J\Subset(1,3)\) containing \([2-\varepsilon,2+\varepsilon]\). This is possible because \(\varepsilon<1\), and also keeps the AH discussion away from odd-frequency endpoints.

Let \(\omega_j=|\widehat g_j|^2\), with
\(\delta_j=\|\omega_j-\omega\|_\infty\to0\), common support in \(J\), and uniformly bounded sup norms. The compact spectral mass bound and the RH Selberg bound, source (1.3), imply
\[
\limsup_T|C_T(\omega_j)-C_T(\omega)|\le M_J\delta_j,
\quad
\limsup_T|V_T(\omega_j)-V_T(\omega)|\le N_J\delta_j.
\]

There is no need to assume \(C_T(\omega_j)\) itself has a full limit when only \(C_T(\omega)\to A\) is known. At fixed \(j\), on a fixed interval \([\eta,R]\), the prefix formula gives
\[
G_{j,T}(y)=2Ay+O(M_J\delta_j y)+o_j(1).
\]
Integration by parts against \(k\) bounds the corresponding central-integral error by a constant times
\[
\delta_j\left(Rk(R)+\eta k(\eta)+\int_\eta^R y|k'(y)|\,dy\right)+o_j(1).
\]
After taking the height limit at fixed \(j\), the intermediate-range tail constant is uniform in \(j\): it uses only the common compact spectral mass and uniform \(\|\omega_j\|_\infty\). The extreme-range errors may depend on Schwartz seminorms of \(g_j\), but vanish in that first height limit.

One may therefore take \(T\to\infty\), then \(j\to\infty\) for fixed \(\eta,R\), and finally \(\eta\downarrow0,\ R\uparrow\infty\). This proves the claimed full-limit extension without an unjustified uniform Schwartz bound or a hidden compatible-subsequence premise. This paragraph makes explicit a valid order already allowed by the report.

## 3. AH implication and the finite-\(R\) deficit conversion

The inherited R16 statements are \(D_T\ge0\),
\(C_{\varepsilon,T}(0)=A_\varepsilon+o(1)\), and AH-Pairs forcing
\(C_T\to A_\varepsilon\). The full-limit transfer therefore gives
\(V_{\varepsilon,T}\to A_\varepsilon\) under RH and AH-Pairs.

If \(\limsup D_T=0\), nonnegativity forces \(D_T\to0\), and hence the **full** limit \(C_T\to A_\varepsilon\). This proves the contrapositive variance-deficit implication without comparing the two statistics on the same subsequence. That logical distinction is correctly retained.

For the quantitative assertion, positivity permits discarding the \(y>R\) part before integration by parts. At fixed \(R\),
\[
V_T\ge\frac4\pi
\left(Rk(R)C_{TR}-\int_0^R yk'(y)C_{Ty}\,dy\right)+o(1).
\]
The small-height argument and smooth-square approximation justify the zero endpoint. With \(d=\limsup D_T\), every fixed compact \(y\)-interval away from zero eventually satisfies \(D_{Ty}\le d+o(1)\), uniformly. This is exactly the ordinary definition of limsup at all sufficiently large heights.

The derivative is
\[
yk'(y)=\frac{\sin y}{2y}-\frac{1-\cos y}{y^2}.
\]
For \(y\le1\), its absolute value is at most one. For \(y\ge1\), it is at most \(1/(2y)+2/y^2\). Consequently
\[
Rk(R)\le1/R,\quad
\int_0^R|yk'(y)|\,dy\le3+\tfrac12\log R,\quad
\int_R^\infty k(y)\,dy\le1/R.
\]
These give the author's exact bound
\[
A_\varepsilon-v_*
\le\frac{4A_\varepsilon}{\pi R}
+\frac{4d}{\pi}\left(3+R^{-1}+\tfrac12\log R\right).
\]
The choice \(R\ge8A_\varepsilon/(\pi\delta)\) makes the first term at most \(\delta/2\), and the resulting lower bound for \(d\) has the stated factor \(\pi/8\).

It is essential that \(R\) is finite here. The integral of the absolute oscillatory derivative on the entire half-line diverges, so the report correctly avoids a false global integration-by-parts estimate.

## 4. Finite arithmetic expansion, endpoints, and atomic diagonal

With \(q_T=1+1/T\), an integer \(n\) occurs in
\(\Psi(q_Tx)-\Psi(x)\) exactly on \([n/q_T,n)\), apart from irrelevant integration endpoints. The intersection for \(m,n\) is
\[
[\max(m,n)/q_T,\ \min(m,n)).
\]
This proves the author's \(B_T(m,n)\), with zero value when the interval is empty. The kernel is nonnegative and has finite support. It gives a factor two when the double sum is expressed using \(m<n\).

Multiplying
\[
\left(\sum_{x<n\le q_Tx}\Lambda(n)-x/T\right)^2
\]
by \(T W_T(x)/(x^2\log^2T)\) gives exactly:

* the \(B_T\) diagonal and pair terms;
* the negative cross coefficient \(-2\Lambda(n)/\log^2T\) times \(\int W_T(x)\,dx/x\);
* the continuous square \(\int W_T(x)\,dx/(T\log^2T)\).

No prime power is omitted. In particular the mean cross term has no extra \(T\), and the continuous term has one inverse \(T\). Support below \(x=1\) is irrelevant because the given logarithmic bump lies strictly above frequency one.

For the atomic diagonal,
\[
\int_{n/q_T}^n x^{-2}\,dx=\frac1{Tn}.
\]
The variation of \(W_T\) over this cell is \(O_\varepsilon(1/(T\log T))\). Uniform PNT partial summation of \(\sum_{n\le z}\Lambda(n)^2\sim z\log z\), over the fixed positive power window, therefore yields
\[
\frac1{\log^2T}\sum_n\frac{\Lambda(n)^2}{n}
\omega\!\left(\frac{\log n}{\log T}\right)
\longrightarrow\int\alpha\omega(\alpha)\,d\alpha
=2\varepsilon m_0.
\]
The symmetry of the bump removes its odd first moment. Smooth endpoint cells are covered by the same variation estimate.

Thus the threshold for the remaining three terms is precisely
\(1+\varepsilon^2m_1-2\varepsilon m_0\). This is a condition on their **signed sum**. Positivity of the pair kernel gives no upper bound for that centered remainder.

## 5. Local variance premise and its uniformity

For fixed \(\eta>0\), the hypothesis
\[
\nu_T([X,e^\eta X])
\le(B\eta+o(1))\frac{\log T}{T}
\]
must hold uniformly over all \(X\) in the required enlarged power window. Divide the log-\(x\) window into \(O(\log T/\eta)\) cells. After multiplication by \(T/\log^2T\), the accumulated error is
\(O(o(1)/\eta)=o(1)\), because \(\eta\) is fixed. The upper Riemann sums have mesh \(\eta/\log T\), tending to zero.

This proves \(\limsup V\le B\varepsilon m_0\) and the sufficient threshold
\[
B<\frac{1+\varepsilon^2m_1}{\varepsilon m_0}.
\]
The premise is not supplied by a two-log RH bound, and an additive fixed-\(h\) variance theorem needs a uniform conversion before use with \(h=x/T\). These limitations are correctly stated.

## 6. Primary-source range audit

I read the precise statements used for every row of the literature table, not just their abstracts.

* CCCC source pp.22–25 confirms the sunrise-envelope factors and their use for liminf/limsup bounds. Lemma 13 combined with the weighted prefix bound gives \(\limsup V\le L^+A_\varepsilon\). It does not force a strict deficit.
* CCCC Theorem 9, equation (2.25), contains the first finite-interval candidate tested at length \(1/2\). The checker obtains \(57/32\) for that candidate; it does not assert that this is the minimum of all candidates or a bound for the tailored weighted bump.
* CCCC's introductory (1.3) supplies the fixed-logarithmic-window RH mass bound required in the approximation. Its large-window \(1.4283\) comparison does not license subtraction of upper bounds.
* Carneiro–Milinovich–Ramos v2, Theorem 1 and Corollary 2, explicitly require sufficiently large interval length. The GRH Theorem 3/Corollary 4 has both the stronger hypothesis and the same long-length restriction.
* The retained Das–Ismoilov–Ramos HTML Theorem 1 and Corollary 7 explicitly state their respective \(\ell_0\) quantifiers. Those are not removed by introductory prose.
* LPZ 1308.3934, printed p.4, distinguishes the RH two-log variance bound from the one-log bound needing a pair-correlation hypothesis.
* LPZ 1311.0597v4, Theorem 1 and its Corollary, has the explicit growth condition \(TS(X,\tau)/X\to\infty\) and the corollary's \(X\le T/\log T\). At \(\tau=1,\ X\asymp T^2\), the former ratio tends to zero. Its later theorem invokes an extra conjecture.
* The Rudnick HTML Theorems 1.1–1.2 concern, respectively, a large-genus average and degree \(d>1\) early-time behavior. The displayed normalization \(X=T^{d\alpha}\), \(0<\alpha<1/d\), gives \(X<T\), not the actual-zeta \(T^2\) regime.

These checks support the bounded source audit. I do not independently certify all proofs in those papers or claim this list exhausts available literature.

## 7. Reproduction and acceptance record

The entire 5,052-byte checker was reviewed. Its rational-log canonicalization is legitimate because the interval endpoints are positive rationals; prime factorization expands those logarithms exactly. It does not use numerical tolerance to declare the kernel identity zero.

A temporary copied script ran with SymPy 1.14.0 and exit status zero, with no stderr. The complete regenerated JSON and stdout log are byte-identical to the author artifacts:

* JSON SHA256: e2a6154e2d531a542178bf4bc60ac69fcd11346937cb15292dbbb1478cbfb28f.
* Log SHA256: 3f888f00c4b3dc5c9420cb36fde053f3d949141e19b8b918bc0fc65f1cbbb989.

The first interval test uses 18 actual prime-power logarithm coefficients, 20 integration cells, \(T=7\), and \(10\le x\le30\). The second uses 23 signed rational coefficients, 31 cells, \(T=3\), and \(5/2\le x\le18\). Both complete centered expansions are exactly equal. The kernel derivative, its origin limit, the Dirichlet integral, the Abelian factor, and the finite-tail budget also pass.

The adjacent receipt preserves **all** replay JSON fields, four author artifact hashes, thirteen source/dependency file hashes, and the source-page visual check. The source download receipt was separately hash-checked. No author file, earlier round, canonical repository, or source file was modified.

Acceptance is limited to the ordinary RH reduction, exact arithmetic identity, and conditional quantitative deficit conversion. The missing prime-variance inequality remains missing.

