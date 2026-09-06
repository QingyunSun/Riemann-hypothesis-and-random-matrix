# A parity-adjusted form of the renormalized pair target

Date: 2026-09-05. Author: root. Status: ordinary proof draft awaiting independent review. No strict correlation bound or novelty claim is made. This note proves two unconditional negligible corrections for the exact R21 kernel. Its final identification with the R21 remainder additionally uses the separately reviewed singleton-renormalization lemma; the transfer to the actual variance uses RH.

## 1. Definitions and statement

Write \(\ell=\log T\), \(L=T^{7/4}\), \(U=T^{9/4}\), and retain
\[
b(m)=\frac{T m^{-T}}{\ell^2}\int_1^m W_T(x)x^{T-2}dx,\quad
k(m,h)=\left(\frac m{m+h}\right)^T,\quad T\ge4.
\]
The fixed smooth weight is nonnegative and supported in \([L,U]\). Its bounds already proved in R21 are
\[
|b(m)|\ll_\omega(m\ell^2)^{-1},\quad
|b'(m)|\ll_\omega(m^2\ell^2)^{-1},\quad b(m)=0\ (m\le L),
\]
and the exact tail bound is
\[
b(m)\ll_\omega U^{T-1}m^{-T}/\ell^2.
\]
Let \(\mathfrak S(h)\) be the prime-pair singular series, zero for odd \(h\). The elementary finite inequality
\[
\sum_{1\le h\le Y}\mathfrak S(h)\le Y
\tag{1}
\]
for every real \(Y\ge0\) follows from the positive divisor expansion in the small-shift note. For even \(h\), \(\mathfrak S(h)\ge2C_2>0\), with the fixed twin-prime Euler product \(C_2\).

Define
\[
q(m,h)=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-1],
\]
and its parity-adjusted counterpart
\[
q_2(m,h)=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2\,1_{\{m\ {\rm odd}\}}].
\]
Every sum below retains prime powers. The asserted negligible corrections are
\[
\boxed{
2\sum_{m,h\ge1}b(m)k(m,h)[q_2(m,h)-q(m,h)]
=O_\omega((T\ell)^{-1}),
}
\tag{2}
\]
and
\[
\boxed{
2\sum_{\substack{m\ {\rm even}\\h\ {\rm even},\ h\ge1}}
b(m)k(m,h)|q_2(m,h)|
=O_\omega((T\ell)^{-1}+2^{-T}/\ell^2).
}
\tag{3}
\]
The constants are unspecified and independent of \(T\). These two conclusions are unconditional. The proof uses only (1), smooth weights and the sparsity of powers of two.

## 2. The parity baseline has negligible weighted sum

The exact difference is
\[
q_2(m,h)-q(m,h)
=\mathfrak S(h)(2\,1_{\{m\ {\rm odd}\}}-1).
\tag{4}
\]
It vanishes when \(h\) is odd. Fix an even shift. The partial sums of \(2\,1_{\{m\ {\rm odd}\}}-1=-(-1)^m\) over any integer interval have absolute value at most one. On a block \(X<m\le2X\), the endpoint and total variation norm of \(b(m)k(m,h)\) is at most
\[
\frac{C_\omega}{X\ell^2}(1+h/(2X))^{-T}.
\]
This follows directly from the derivative bound on \(b\) and the monotonicity of \(k\) in \(m\); it is also valid on a truncated last block. Alternating summation by parts thus bounds the block in (2) by that coefficient times \(\mathfrak S(h)\).

For every decreasing differentiable nonnegative function \(g\) tending to zero, (1) gives
\[
\sum_{h\ge1}\mathfrak S(h)g(h)
=\int_0^\infty A(y)(-g'(y))dy
\le\int_0^\infty g(y)dy,\qquad
A(y)=\sum_{h\le y}\mathfrak S(h).
\tag{5}
\]
Both boundary terms vanish in the uses here. Taking \(g(y)=(1+y/(2X))^{-T}\) yields \(2X/(T-1)\). Hence the complete shift sum on a block is \(O_\omega(1/(T\ell^2))\). There are \(O(\ell)\) blocks covering \((L,2U]\). Their total is \(O_\omega(1/(T\ell))\).

For the infinite \(m>2U\) tail, absolute summation is enough. The same argument gives
\[
\sum_h\mathfrak S(h)k(m,h)\le m/(T-1).
\]
Therefore its absolute mass is bounded by
\[
\frac{C_\omega U^{T-1}}{T\ell^2}
\sum_{m>2U}m^{1-T}
\ll_\omega \frac{U\,2^{-T}}{T^2\ell^2}.
\]
Integral comparison plus the first integer term justifies the last estimate uniformly for \(T\ge4\), since \(2U\ge T\). With \(U=T^{9/4}\), this exponentially small expression is \(O_\omega(1/(T\ell))\). This proves (2). No unproved arithmetic cancellation is used: the cancellation is the exact parity alternation of a smooth weight.

## 3. Even endpoints after the baseline change

For \(m,h\) both even, \(m+h\) is even. A nonzero von Mangoldt value at either endpoint is exactly \(\log2\), at a power of two. Also the baseline in \(q_2\) is zero. Consequently
\[
|q_2(m,h)|\le
\Lambda(m)\Lambda(m+h)+
\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)].
\]
The first term is bounded by a fixed multiple of the second: if both are nonzero, their values are \(\log2\), while \(\mathfrak S(h)\ge2C_2>0\). If either vanishes, the product is zero. Thus it suffices to bound the two nonnegative singleton-power contributions
\[
J_-=\sum_{\substack{r=2^j\\r>L}}b(r)\Lambda(r)
\sum_{h\ge1}\mathfrak S(h)k(r,h),
\]
\[
J_+=\sum_{r=2^j}\Lambda(r)
\sum_{1\le m<r}b(m)(m/r)^T\mathfrak S(r-m).
\tag{6}
\]
Enlarging the sums to all indicated \(m,h\) is legal because every coefficient is nonnegative.

For \(L<r\le2U\), the inner lower-endpoint sum is at most \(r/(T-1)\) by (5). The bound on \(b(r)\) gives \(O_\omega(1/(T\ell^2))\) per power of two. There are \(O(\ell)\) such powers, for a total \(O_\omega(1/(T\ell))\).

For the upper endpoint in the same range, use
\[
b(m)(m/r)^T\le
\frac{C_\omega}{r\ell^2}(1-(r-m)/r)^{T-1}.
\]
Apply (5) to \(g(h)=(1-h/r)_+^{T-1}\), whose integral is \(r/T\). This again gives \(O_\omega(1/(T\ell^2))\) per power, and \(O_\omega(1/(T\ell))\) in total.

If \(r>2U\), the exact tail bound in \(J_-\) gives
\[
b(r)\sum_h\mathfrak S(h)k(r,h)
\ll_\omega U^{T-1}r^{1-T}/(T\ell^2).
\]
Its sum over powers of two is \(O_\omega(2^{-T}/(T\ell^2))\). Indeed the first power \(r_0>2U\) satisfies \(r_0^{1-T}\le(2U)^{1-T}\), and the following powers form a geometric series with ratio \(2^{1-T}\le1/8\).

For the upper-endpoint tail, the exact cancellation of \(m^T\) gives, for every \(m<r\),
\[
b(m)(m/r)^T
=\frac{T}{r^T\ell^2}\int_1^mW_T(x)x^{T-2}dx
\ll_\omega \frac{U^{T-1}}{r^T\ell^2}.
\]
Equation (1) implies \(\sum_{m<r}\mathfrak S(r-m)\le r\), so the row is \(O_\omega(U^{T-1}r^{1-T}/\ell^2)\). The same geometric sum makes its entire power-of-two tail \(O_\omega(2^{-T}/\ell^2)\).

Together these bounds prove (3). They include the true infinite endpoint and every higher power of two.

## 4. Conditional assembly with the separate companion lemmas

The singleton-renormalization identity being proved separately is
\[
\mathcal E_T=2\sum_{m,h\ge1}b(m)k(m,h)q(m,h)+o(1).
\tag{7}
\]
Its ordinary-PNT proof is a separate dependency. It must be reviewed before this assembly is accepted. The odd-primepower-pair companion proves that the entire odd-\(h\) nonnegative \(\Lambda\Lambda\) contribution is \(o(1)\). On those shifts both \(q\) and \(q_2\) equal that product because the singular series vanishes.

Combining those two independently established inputs with (2)–(3) gives
\[
\boxed{
\mathcal E_T=
2\sum_{\substack{m\ {\rm odd}\\h\ge2,\ h\ {\rm even}}}
b(m)k(m,h)
\{\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\}
+o(1).
}
\tag{8}
\]
The inner singleton constants are two because the baseline now conditions on the allowed parity class. Merely dropping the even endpoints in \(q\) with its old constant one would be wrong: those even endpoints have a large nonzero singular-series baseline. The exact alternating correction must be included first.

Equation (8), once its dependencies are accepted, gives the same signed strict target on odd endpoints and even shifts. It does not bound the remaining expression, and does not make the old unweighted all-shifts premise possible. The full original odd-shift contribution to \(\mathcal E_T\) has not been deleted on its own; the global renormalization redistributes singleton terms before the parity reduction.

This is an exact normalization check with controlled errors, closely related to classical removal of a local congruence factor. It is not a new prime-distribution estimate or a solution of the zeta-correlation problem.
