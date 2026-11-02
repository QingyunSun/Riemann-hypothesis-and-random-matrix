# Removing the nonprimitive packet for every odd divisor subset

Date: 2026-09-05. Author: Aquinas. Status: complete ordinary unconditional proof, submitted for independent review. This note strengthens the nonprimitive estimate of R23 without changing its frozen manuscript. It neither estimates the surviving signed prime correlation nor proves a strict zeta-variance bound.

## 1. Exact statement and unchanged normalization

Let
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},\quad
X=T^\alpha,\quad H=X/T,\quad Q=X^{523/1000},
\qquad 11/5\le\alpha\le9/4,
\tag{1}
\]
where \(T\ge4\) is real. Fix a smooth nonnegative function \(\omega\) supported on \([7/4,9/4]\), extended by zero, and fixed real \(\chi,V\in C_c^\infty((1,2))\). Define the actual continuum-window weight
\[
b_T(m)=\frac{T m^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}\,dx,
\quad
F_T(m,h)=b_T(m)\chi(m/X)V(h/H)
\left(\frac m{m+h}\right)^T.
\tag{2}
\]
No exponential approximation to the last factor is made.

Let \(\mathcal D\) be **any set of distinct odd positive integers** at most \(Q\). The set may depend arbitrarily on \(T,\alpha\). Squarefreeness need not be imposed because its coefficient below is exactly \(\mu(d)\). Define
\[
\mathcal N_{\mathcal D}
=2\sum_{d\in\mathcal D}\mu(d)
\sum_{\substack{n\ge1\text{ odd}\\h\text{ even}}}
\Lambda(n)F_T(n-h,h)\log((n-h)/d)
1_{(h,d)>1}1_{n\equiv h\pmod d}.
\tag{3}
\]
Only points with \(X<n-h<2X\) and \(H<h<2H\) contribute; elsewhere the summand is defined to be zero. Thus its logarithm is evaluated only at a positive argument greater than one, and every sum is finite. Equation (3) is exactly the term (18) in R23, with its divisor family generalized and its original factor two retained.

**Theorem.** For every fixed \(\eta>0\), uniformly in (1) and in the choice of \(\mathcal D\),
\[
\boxed{\left|\mathcal N_{\mathcal D}\right|
\ll_{\eta,\omega,\chi,V}\frac{X^\eta}{T}.}
\tag{4}
\]
In particular, choosing the fixed value \(\eta=1/100\),
\[
\boxed{|\mathcal N_{\mathcal D}|
\ll_{\omega,\chi,V}X^{-391/900}=o(1).}
\tag{5}
\]
The proof actually uses only \(d\le Q<X\), rather than the specific exponent of \(Q\), for this nonprimitive term. No restriction on the largest prime factor of \(d\), owner factorization, prime distribution in progressions, PNT, or RH is required.

## 2. Support and the forced divisibility of the shift

Write \(m=n-h\). The exact support gives
\[
X<m<2X,\qquad H<h<2H,\qquad
X<n<2X+2H\le\tfrac52X<3X.
\tag{6}
\]
The displayed weak inequality uses only \(T\ge4\). The fixed continuum window remains \([L,U]\); in particular we do not truncate \(b_T(m)\) at \(m=U\). Its global bound is
\[
0\le b_T(m)\le
\frac{T\|\omega\|_\infty}{(T-1)m\ell^2},
\qquad
|F_T(m,h)|\ll_{\omega,\chi,V}\frac1{X\ell^2}.
\tag{7}
\]
This follows by integrating \(\|\omega\|_\infty x^{T-2}\) in (2), bounding the exact Pareto factor by one, and using \(m>X\). It applies throughout the packet, including where \(m>U\).

If a summand in (3) is nonzero, then \(\Lambda(n)\ne0\), so \(n=p^j\) for a unique prime \(p\). The masks give
\[
d\mid n-h,\qquad (h,d)>1,
\qquad\text{hence }p\mid d\text{ and }p\mid h.
\tag{8}
\]
Indeed every prime dividing \((h,d)\) divides \(n\), whose only prime factor is \(p\). The prime \(p\) is odd because \(n\) is odd. Also \(j\ge2\): otherwise \(p=n>X>d\), contradicting \(p\mid d\). Consequently
\[
p\le\sqrt n<\sqrt{3X}.
\tag{9}
\]
All higher powers remain present, with their correct weight
\(\Lambda(p^j)=\log p\), not \(\log(p^j)\).

Since \(p\) is odd and \(h\) is even, (8) gives \(h=2pr\) for a positive integer \(r\). Therefore the exact open-interval count satisfies
\[
\#\{h\in2\mathbb Z:H<h<2H,\ p\mid h\}
\le\#\{r\in\mathbb Z:0<r<H/p\}\le H/p.
\tag{10}
\]
This argument has no discarded rounding term: if \(p\ge H\), the count is zero. Independently, the assigned height range has
\[
\frac{H}{\sqrt{3X}}
=\frac{X^{1/2-1/\alpha}}{\sqrt3}
\ge\frac{X^{1/22}}{\sqrt3}\longrightarrow\infty
\tag{11}
\]
uniformly. Thus even the usual interval-length bound with a rounding term would suffice, but (10) is simpler and exact.

## 3. Divisor coefficients and the harmonic prime sum

For fixed \(n,h\), each divisor in \(\mathcal D\) occurs at most once. Since \(d\le Q<X<m<2X\),
\[
\sum_{\substack{d\in\mathcal D\\d\mid m}}
|\mu(d)|\,|\log(m/d)|
\le\tau(m)\log(2X)
\ll_\eta X^\eta\log(2X).
\tag{12}
\]
Additional masks can only decrease this absolute bound. There is no factor \(|\mathcal D|\) or \(Q\) in (12). For completeness, the elementary divisor bound follows by choosing a prime cutoff such that \(p^\eta\ge2\) above it, using \(e+1\le2^e\le p^{\eta e}\), and absorbing the finite product of \(\sup_{e\ge0}(e+1)p^{-\eta e}\) for smaller primes into the constant.

For each odd prime \(p\), there are at most two powers in \((X,3X)\). Three distinct powers would have largest-to-smallest ratio at least \(p^2\ge9\), impossible in this interval. This deliberately loose bound includes every exponent \(j\ge2\) admitted by (9).

Only the elementary Chebyshev estimate is needed for summing their prime bases. Write \(\vartheta(y)=\sum_{p\le y}\log p\). One may use
\(\vartheta(y)\le\Psi(y)\le4(\log2)y\) for real \(y\ge1\). To see the last bound, the valuations of \({2n\choose n}\) majorize the prime-power terms in \(\Psi(2n)-\Psi(n)\); then use \(\log{2n\choose n}\le2n\log2\), telescope on powers of two, and use monotonicity. Partial summation, with \(\vartheta(t)=0\) for \(t<2\), gives
\[
\sum_{p\le Y}\frac{\log p}{p}
=\frac{\vartheta(Y)}Y+
\int_1^Y\frac{\vartheta(t)}{t^2}\,dt
\ll1+\log Y.
\tag{13}
\]
This is not a prime asymptotic in a short interval or an arithmetic progression.

Combining the original factor two in (3), (7), (10), (12), and the bound on the number of powers yields
\[
\begin{aligned}
|\mathcal N_{\mathcal D}|
&\ll_{\eta,\omega,\chi,V}
\frac{X^\eta\log(2X)}{X\ell^2}
\sum_{p\le\sqrt{3X}}
\sum_{\substack{j\ge2\\X<p^j<3X}}
(\log p)\frac Hp\\
&\ll_{\eta,\omega,\chi,V}
\frac{HX^\eta}{X}
\frac{\log(2X)(1+\log(\sqrt{3X}))}{\ell^2}
\ll_{\eta,\omega,\chi,V}\frac{X^\eta}{T}.
\end{aligned}
\tag{14}
\]
The last constant is uniform because \(\log X=\alpha\ell\) with \(\alpha\) in a fixed compact interval. Finally
\[
\frac{X^{1/100}}T=X^{1/100-1/\alpha}
\le X^{1/100-4/9}=X^{-391/900},
\tag{15}
\]
proving (4)–(5).

There are no unestimated endpoints or infinite tails in (14): both physical cutoffs are compact and vanish outside the open intervals in (6). The real endpoints of the original continuum integral were retained in (2); the proof uses its global majorant rather than replacing its moving endpoint by \(X\) or \(U\).

## 4. The exact opening that this permits

The primitive completion proof in R23 Sections 4–5 also uses no owner guard. Its parity kernel is
\[
K_{d,h}(n)=1_{(n,d)=1}
\left(1_{n\equiv h\pmod d}-
\frac{1_{(h,d)=1}}{\varphi(d)}\right).
\tag{16}
\]
For any odd \(d\), its sum over a complete period of the even shifts is zero. The smooth Poisson proof, with \(H\ge Q\), bounds the resulting term by
\[
|\mathcal B_{\mathcal D}|
\ll_J\frac{Q}{\log X}(Q/H)^J.
\tag{17}
\]
Its hypotheses are precisely the fixed smooth cutoffs, the derivative bound for the actual (2), odd \(d\le Q\), and the elementary prime-power-inclusive Chebyshev bound. Restricting or enlarging the set of odd divisors below \(Q\) does not affect any of them. Taking the same fixed \(J=24\) gives
\[
24\left(\frac6{11}-\frac{523}{1000}\right)
-\frac{523}{1000}=\frac7{440},\qquad
|\mathcal B_{\mathcal D}|\ll
X^{-7/440}/\log X.
\tag{18}
\]
Here (17) is the already proved R23 completion estimate applied within its verified scope; the new argument of this note is (14).

The finite algebra \(\Lambda(m)=\sum_{d\mid m}\mu(d)\log(m/d)\) and the exact primitive/nonprimitive congruence split hold for any divisor subset. Consequently R23's same packet obeys
\[
\mathcal P_{T,X}^{\chi,V}
=\mathcal A_{\mathcal D}+\mathcal C_{\mathcal D}
-\mathcal M_{\mathfrak S}
+O_{\omega,\chi,V}\left(
\frac{X^{-7/440}}{\log X}+X^{-391/900}\right),
\tag{19}
\]
where \(\mathcal A_{\mathcal D}\), \(\mathcal C_{\mathcal D}\), and \(\mathcal M_{\mathfrak S}\) retain exactly R23 (17), (19), and (20), with the chosen \(\mathcal D\). In particular the full primitive masks, the coefficients \(\mu(d)/\varphi(d)\), the logarithmic cofactors, and both singular-series-weighted prime marginals remain unchanged.

One may now choose all odd integers \(d\le Q\). The remaining complementary divisors then satisfy \(d>Q\), hence their integer cofactors satisfy \(k=m/d<2X/Q\). This is a genuine simplification of the exact arithmetic organization; it is not an upper bound for the remaining signed expression. No estimate of its sign, cancellation, or identification with the singular-series marginals follows from (19).

The arbitrary divisor family in this corollary is not asserted to satisfy the 186 paper's distribution hypotheses. That theorem is not used in (14) or (17). This result concerns the stated smooth positive-shift packet and height range, not every shift or the entire original variance. In particular no strict Bragg deficit, AH refutation, or improved prime gap is claimed.

## 5. Provenance and bounded checks

The adjacent receipt pins the unchanged R23 [packet and primitive completion proof](../../research-round23/even-pair-dispersion/UPPER_WING_SHIFT_COMPLETION.md), its author receipt, and the R22 [prime-power-inclusive Chebyshev proof](../../research-round22/odd-primepower-pairs/ALL_ODD_PRIMEPOWER_PAIRS.md), Section 2. All elementary arithmetic ingredients used above are proved in this note as well; no new distributional source is being imported.

The tiny adjacent checker verifies only exact rational exponent and normalization identities. It does not enumerate factors, prime powers, divisor families, or prime heights, and it does not replace the ordinary proof. Frozen source bytes are not changed by this companion.
