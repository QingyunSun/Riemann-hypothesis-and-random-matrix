# Independent R22 derivation: the full singleton correction is negligible

Date: 2026-09-05. Author/reviewer: residual_gram / Astra. Status: independent ordinary derivation submitted for cross-review. This checks the proposed renormalization independently of Euclid's author report. No author source has been changed. The requested conclusion holds under RH; in fact, the linear correction needs only the ordinary prime number theorem. The inherited transfer from the variance to prime pairs still assumes RH. No strict variance bound or AH refutation follows.

## 1. Precise statement and inputs

Put ell=log T, L=T^{7/4}, U=T^{9/4}, with real T≥4, and use the fixed smooth weight omega supported in [7/4,9/4]. Its zero extension is smooth. Write
\[
W(x)=\omega(\log x/\ell),\qquad
b(x)=\frac{T x^{-T}}{\ell^2}\int_1^xW(y)y^{T-2}\,dy,
\qquad k(m,h)=\left(\frac m{m+h}\right)^T.
\tag{1}
\]
Define b(x)=0 for x≤L, including x≤0. In integrals below, the primitive in (1) is likewise defined to be zero below L. Every value of the actual von Mangoldt function is retained, including prime powers. Set
\[
a_n=\Lambda(n)-1,\qquad
c_h=\mathfrak S(h)-1.
\]
The correction in question is
\[
\mathcal L_T=2\sum_{m,h\ge1}b(m)k(m,h)c_h(a_m+a_{m+h}).
\tag{2}
\]
All sums are absolutely convergent for each T≥4 before signed identities are applied; the tail bounds below also verify this.

**Conclusion.** With constants depending only on the fixed weight,
\[
\mathcal L_T
=-2\sum_{L<n\le2U}b(n)a_n\log(n/T)
+O_\omega(1/\ell)
+O_\omega\!\left(U^{3/2}(1+\log U)2^{-T}/\ell^2\right).
\tag{3}
\]
Under RH this gives
\[
\mathcal L_T=O_\omega\!\left(\frac1\ell+\frac{\ell}{\sqrt L}
+\frac{U^{3/2}(1+\log U)2^{-T}}{\ell^2}\right)=o(1).
\tag{4}
\]
The ordinary PNT also suffices for o(1), as proved in section 6.

The only singular-series input is the unconditional triangular average already checked in R21:
\[
A_2(y):=\sum_{h\ge1}(y-h)_+c_h
=-\frac12y\log y+O(y),\qquad y\ge1,
\quad A_2(y)=0\quad(0\le y\le1).
\tag{5}
\]
Its source is Montgomery–Soundararajan, arXiv:math/0409258v1, printed p.4 equation (16), after division by two and linear interpolation. We also use the elementary bound |c_h|≪h^{1/2}; any fixed small positive divisor exponent would suffice. The R21 proof, primary PDF and first corrected review are pinned in the receipt.

## 2. Why the backward marginal has an exact cancellation

For the forward marginal, R21 already proved uniformly for m≥T that
\[
\sum_{h\ge1}c_h k(m,h)
=-\frac12\log(m/T)+O(1).
\tag{6}
\]
The backward marginal is different. After n=m+h, its exact weight is
\[
f_n(h)=b(n-h)\left(\frac{n-h}{n}\right)^T
=\frac{T}{n^T\ell^2}\int_1^{n-h}W(x)x^{T-2}\,dx.
\tag{7}
\]
Set this to zero when n−h≤L. This is an identity, not a local approximation of b or of the Pareto factor. On h≥0, it is smooth, supported inside [0,n−L], and f_n(0)=b(n). For s=n−h in the support,
\[
\begin{aligned}
f_n'(h)&=-\frac{T}{n^T\ell^2}W(s)s^{T-2},\\
f_n''(h)&=\frac{T}{n^T\ell^2}
\left[W'(s)s^{T-2}+(T-2)W(s)s^{T-3}\right].
\end{aligned}
\tag{8}
\]
Both derivatives vanish where s lies outside [L,U]. The W-prime term can have either sign. No positivity of f_n'' is assumed.

Integration by parts on [0,infinity) gives exactly
\[
\int_0^\infty h f_n''(h)\,dh=f_n(0)=b(n).
\tag{9}
\]
The boundary at infinity vanishes because of support. The h=0 boundary in h f_n' vanishes, whereas the subsequent f_n endpoint is retained. This is the source of the coefficient b(n), even when n lies close to L or U.

## 3. Uniform logarithmic moment, including the moving endpoint

Let C_omega be a fixed sufficiently large constant. Since
\(|W'(s)|\le\|\omega'\|_\infty/(s\ell)\), equation (8) implies, for n>L and 0<h<n,
\[
|f_n''(h)|
\le\frac{C_\omega T(T-1)}{n^3\ell^2}
(1-h/n)^{T-3}.
\tag{10}
\]
Off the derivative support the left side is zero. Enlarging the right side to the full interval (0,n) is legal. In particular
\[
\int_0^\infty h|f_n''(h)|\,dh
\le\frac{C_\omega}{n\ell^2}\frac{T}{T-2}
\le\frac{2C_\omega}{n\ell^2}.
\tag{11}
\]
This bound is absolute rather than relative to b(n); we never divide by a possibly tiny b(n).

For the logarithmic moment, let v=h/n and u=Tv. The normalized beta density
\[
p_T(v)=(T-1)(T-2)v(1-v)^{T-3},\qquad0<v<1,
\tag{12}
\]
has total mass one. Its u-variable has mean 2. On 0<u<1 its density is
\[
\frac{(T-1)(T-2)}{T^2}u(1-u/T)^{T-3}\le u.
\]
Consequently
\[
\mathbb E_{p_T}|\log u|
\le\int_0^1u|\log u|du+\mathbb E_{p_T}u
\le\frac14+2=\frac94.
\tag{13}
\]
Combining (10)–(13) yields
\[
\int_0^\infty h\left|\log\frac{Th}{n}\right||f_n''(h)|dh
\ll_\omega\frac1{n\ell^2}.
\tag{14}
\]
This estimate is uniform for every n>L. In particular it holds for n arbitrarily close to L, at U, and at 2U. Near the upper boundary the actual derivative may live far from n/T and be exponentially small; the absolute beta envelope still proves (14). No assertion that the actual derivative mass is a positive probability measure, or is concentrated uniformly relative to b(n), is needed.

Using (9) and (14),
\[
\int_0^\infty h\log h\,f_n''(h)dh
=b(n)\log(n/T)+O_\omega(1/(n\ell^2)).
\tag{15}
\]
This preserves all signs in f_n'' while estimating only its error absolutely.

## 4. The backward singular-series transform

For fixed n, only finitely many h contribute. Integrating each hinge gives
\[
\sum_{h\ge1}c_h f_n(h)=\int_0^\infty A_2(y)f_n''(y)dy.
\tag{16}
\]
Indeed, \(\int_h^\infty(y-h)f_n''(y)dy=f_n(h)\). Thus no differentiability or unproved first-derivative estimate of A_2 is assumed.

The O(y) term in (5) contributes O_omega(1/(n ell²)) by (11). On 0<y<1, A_2(y)=0. Extending the logarithmic main term into this short range costs at most
\[
\frac{C_\omega T(T-1)}{n^3\ell^2}
\int_0^1y|\log y|dy
\ll_\omega\frac1{n\ell^2},
\tag{17}
\]
because n>L>T. Therefore (15)–(17) prove the uniform exact-kernel estimate
\[
\boxed{\sum_{h\ge1}c_h b(n-h)\left(\frac{n-h}{n}\right)^T
=-\frac12b(n)\log(n/T)+O_\omega(1/(n\ell^2))}
\tag{18}
\]
for n>L. For n≤L the left side and b(n) both vanish. We use the error in (18) only up to 2U; it must not be summed to infinity in absolute value.

## 5. Absolute convergence, prime-weighted errors and both tails

The elementary Chebyshev bound Ψ(x)≪x gives
\[
\sum_{L<n\le2U}\frac{|a_n|}{n}
\le\sum_{L<n\le2U}\frac{\Lambda(n)+1}{n}
\ll1+\log(2U/L)\ll\ell.
\tag{19}
\]
This step is essential. The crude pointwise bound |a_n|≤1+log n would only give O(1) after summing the error in (18), rather than the needed o(1). Partial summation of Chebyshev supplies the logarithmic improvement without any short-interval prime estimate.

From the exact zero-extended integral form,
\[
b(x)\ll_\omega\frac1{x\ell^2},\qquad
|b'(x)|\ll_\omega\frac1{x^2\ell^2}.
\tag{20}
\]
Thus the O(1) in the forward transform (6) contributes O(1/ell) on [L,2U], by (19); the error in (18) does so too.

For x>U, the original primitive bounds b(x) by
\[
b(x)\ll_\omega U^{T-1}x^{-T}/\ell^2.
\tag{21}
\]
Using |c_h|≪h^{1/2}, T≥4 and (1+h/m)^{-T}≤(1+h/m)^{-4},
\[
\sum_{h\ge1}|c_h|k(m,h)\ll m^{3/2}.
\]
Together with |a_m|≤1+log m, the forward part with m>2U is bounded by
\[
\frac{C_\omega U^{T-1}}{\ell^2}
\sum_{m>2U}m^{3/2-T}(1+\log m)
\ll_\omega\frac{U^{3/2}(1+\log U)2^{-T}}{\ell^2}.
\tag{22}
\]
All constants here can be uniform for T≥4; the smallest denominator in the elementary tail integral is T−5/2≥3/2.

For the backward part with n>2U, equation (7) directly gives
\[
0\le f_n(h)\ll_\omega U^{T-1}n^{-T}/\ell^2
\quad(1\le h<n),
\]
for the actual nonnegative weight omega; the corresponding absolute bound holds without that sign. Since \(\sum_{h<n}|c_h|\ll n^{3/2}\), the same bound (22) applies after multiplication by |a_n| and summation in n. This also includes the range m=n−h>U, where the primitive has saturated but has not vanished. No missing region is discarded.

For fixed T≥4 these estimates prove all required absolute convergence. Equations (6), (18), (19) and (22), with the factor two in (2), now give exactly (3): the two main marginals each contribute minus one half of the same smooth prime sum.

## 6. The remaining smooth prime sum

Let
\[
A(x)=\sum_{n\le x}a_n=\Psi(x)-\lfloor x\rfloor,
\qquad g(x)=b(x)\log(x/T).
\]
On [L,2U], equation (20) implies
\[
|g(x)|\ll_\omega\frac1{x\ell},\qquad
|g'(x)|\ll_\omega\frac1{x^2\ell}.
\tag{23}
\]
Partial summation with the exact half-open endpoint convention gives
\[
\sum_{L<n\le2U}g(n)a_n
=g(2U)A(2U)-g(L)A(L)-\int_L^{2U}A(x)g'(x)dx.
\tag{24}
\]
Here g(L)=0, even when L happens to be an integer. Under RH, A(x)=O(√x log²(2x)), and log x is comparable to ell on this window. Hence (24) is O_omega(ell/√L), proving (4).

There is a modest strengthening. Put
\[
\eta(L)=\sup_{x\ge L}\frac{|\Psi(x)-\lfloor x\rfloor|}{x}.
\]
The ordinary PNT gives eta(L)→0. Using |A(x)|≤eta(L)x in (24) and (23) gives
\[
\left|\sum_{L<n\le2U}g(n)a_n\right|
\ll_\omega\eta(L)\left(\frac1\ell+\frac{\log(2U/L)}\ell\right)
\ll_\omega\eta(L)=o(1).
\tag{25}
\]
Thus the linear renormalization itself is unconditional. This does not remove RH from the inherited R21 variance identity. The source statement Ψ(x)=x+o(x), equivalent to PNT, was checked directly at [DLMF 25.16.3](https://dlmf.nist.gov/25.16.E3). The floor correction is at most one. No quantitative PNT rate is asserted in (25).

## 7. What the renormalization does and does not achieve

Define
\[
q_{m,h}=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)\bigl(\Lambda(m)+\Lambda(m+h)-1\bigr).
\tag{26}
\]
The algebraic identity is exact:
\[
a_ma_{m+h}-c_h=q_{m,h}+c_h(a_m+a_{m+h}).
\tag{27}
\]
Consequently, with the same fixed weight and all prime powers,
\[
\mathcal Q_T:=2\sum_{m,h\ge1}b(m)k(m,h)q_{m,h}
=\mathcal E_T+o(1).
\tag{28}
\]
Under the existing RH variance transfer,
\[
\overline V_T=M+\mathcal Q_T+o(1).
\tag{29}
\]
Thus the unchanged meaningful target can be written \(\liminf\mathcal Q_T\le1-M\). The old h=1 singleton obstruction no longer applies verbatim: when h is odd, q_{m,h}=Λ(m)Λ(m+h), with no singleton prime-error terms. This observation does not prove any improved bound for even shifts or for the complete signed aggregate. It does not establish that a new uniform sub-square-root hypothesis for q is attainable.

The result is a legal removal of the identified linear nuisance, using a proved signed singular-series average and ordinary one-prime information. It is not a strict arithmetic gain, and no new famous theorem is claimed. The next missing estimate remains genuinely quadratic in the actual primes.

## 8. Small checks and provenance

A separate small exact checker verifies the renormalization algebra, the beta normalization and scaled mean at a few integer T, and the hinge/integration endpoint identities for polynomial compact weights, including n close to the lower edge and beyond twice the upper edge. These are finite algebra checks, not numerical heights or evidence for the unresolved pair estimate. The ordinary proof supplies uniformity in real T and the asymptotic bounds. The receipt pins this report, its exact checks and the already retained R21 sources. No author file, historical round or Git state was edited.
