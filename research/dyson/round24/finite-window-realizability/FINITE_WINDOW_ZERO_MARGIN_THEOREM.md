# Exact zero margins for finitely many actual window profiles

Date: 2026-09-05. Author: Plato / residual_gram. Status: ordinary proof submitted for independent review. This note tests a genuine extension of the original kernel family. It proves no strict zeta or prime-correlation inequality.

The root's preceding R24 note excludes one or two full Pareto profiles with arbitrary lower-endpoint coefficients. Here the coefficient class is more restrictive but directly contains every finite combination arising from compactly supported changes of the actual lower-endpoint windows. In this class the exclusion extends to **every finite number of distinct exponents**. The proof uses the actual prime-pair singular series, including its positive divisor expansion and its rational-frequency averages; no arbitrary checkerboard or prime data are substituted.

## 1. Statement and relation to the actual kernel

Fix a positive odd integer \(m_0\), a finite integer \(r\geq1\), and distinct real numbers

\[
2<t_1<t_2<\cdots<t_r.
\]

Let \(c_j(m)\) be complex coefficients on odd \(m\geq m_0\). Suppose that for some finite real \(M\), each coefficient is constant on all odd \(m>M\):

\[
c_j(m)=C_j\quad(m>M).
\tag{1}
\]

Define on the full triangular domain of odd \(m<n\)

\[
\delta K(m,n)=\sum_{j=1}^r c_j(m)n^{-t_j}.
\tag{2}
\]

Write \(S(h)=\mathfrak S(h)\), the ordinary prime-pair singular series. Assume the exact weighted margins

\[
\sum_{\substack{n>m\\n\ {\rm odd}}}S(n-m)\delta K(m,n)=0
\quad(m\geq m_0\ {\rm odd}),
\tag{3}
\]

\[
\sum_{\substack{m_0\leq m<n\\m\ {\rm odd}}}S(n-m)\delta K(m,n)=0
\quad(n>m_0\ {\rm odd}).
\tag{4}
\]

**Theorem.** Under (1)–(4), all coefficients \(c_j(m)\) vanish. In particular the integer kernel \(\delta K\) is zero.

For each fixed exponent \(t>2\), changing the actual smooth window gives precisely

\[
\delta K_t(m,n)
=\left[\frac{t}{(\log t)^2}
\int_1^m\delta W_t(x)x^{t-2}\,dx\right]n^{-t}.
\tag{5}
\]

If \(\delta W_t\) is supported below a finite upper endpoint, the bracket is constant after that endpoint. Thus every finite combination of such genuine window variations belongs to (1)–(2). This remains true when the exponents, supports, or number of profiles depend on an external height: apply the exact theorem separately at each fixed height. No uniform asymptotic constant in that extra parameter is claimed or needed.

Coincident exponents must first be combined. Without that convention, cancellation between duplicate parametrizations would invalidate the assertion that each individual coefficient is zero, though the resulting kernel could still be zero.

## 2. Elementary facts about the actual singular series

For positive integers \(k\), write

\[
S(2k)=2C_2\sum_{d\mid k}g(d),\qquad
g(d)=\frac{\mu^2(d)1_{d\ {\rm odd}}}
{\prod_{p\mid d}(p-2)},
\quad
C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right)>0.
\tag{6}
\]

The empty product gives \(g(1)=1\). Formula (6) follows by multiplying the finitely many local factors for primes dividing \(k\). Its normalization is important here; on the even grid the mean is two, not one.

Positivity and an absolutely convergent Euler product give

\[
\sum_{d\geq1}\frac{g(d)}d
=\prod_{p>2}\left(1+\frac1{p(p-2)}\right)
=C_2^{-1}.
\tag{7}
\]

We will also use, for \(Y\geq1\),

\[
G(Y):=\sum_{d\leq Y}g(d)\ll1+\log(2Y).
\tag{8}
\]

Here is a direct bound retaining every divisor. On odd squarefree \(d\),

\[
g(d)=\frac1d\prod_{p\mid d}\left(1+\frac2{p-2}\right).
\]

Expand the finite product. With
\(r(a)=\mu^2(a)1_{a\ {\rm odd}}2^{\omega(a)}/\prod_{p\mid a}(p-2)\), dropping a squarefree restriction in the remaining positive sum gives

\[
G(Y)\leq(1+\log(2Y))\sum_{a\geq1}\frac{r(a)}a,
\qquad
\sum_{a\geq1}\frac{r(a)}a
=\prod_{p>2}\left(1+\frac2{p(p-2)}\right)<\infty.
\]

This proves (8). Formula (6) and (7) also imply the useful exact bound

\[
\sum_{1\leq h\leq y}S(h)
=2C_2\sum_d g(d)\left\lfloor\frac{y}{2d}\right\rfloor
\leq y.
\tag{9}
\]

Finally, for every fixed \(\eta>0\),

\[
S(2k)\ll_\eta k^\eta.
\tag{10}
\]

Indeed \(S(2k)=2C_2\prod_{p\mid k,p>2}(p-1)/(p-2)\). For all sufficiently large primes the factor is at most \(p^\eta\); the finitely many small primes contribute a fixed constant. This is enough even when two exponents in (2) are very close.

## 3. Row masses determine the eventual constants

For fixed \(t>2\), define

\[
A_t(m)=\sum_{\substack{n>m\\n\ {\rm odd}}}S(n-m)n^{-t}.
\]

As \(m\to\infty\) through odd integers,

\[
\boxed{A_t(m)\sim\frac{m^{1-t}}{t-1}.}
\tag{11}
\]

To prove this with no unproved local prime average, substitute (6) and use positivity:

\[
A_t(m)=2C_2\sum_{d\geq1}g(d)
\sum_{v\geq1}(m+2dv)^{-t}.
\]

For every fixed \(d\), an elementary Riemann sum gives

\[
m^{t-1}\sum_{v\geq1}(m+2dv)^{-t}
\longrightarrow\frac1{2d(t-1)}.
\]

The same expression is at most \(1/(2d(t-1))\) by integral comparison for a decreasing function. Equation (7) therefore permits dominated convergence in \(d\), proving (11) with the displayed constant.

For all sufficiently large odd \(m\), the row condition is

\[
\sum_{j=1}^r C_jA_{t_j}(m)=0.
\]

Divide by \(m^{1-t_1}\) and use (11). The smallest exponent contributes \(C_1/(t_1-1)\), while every other term tends to zero. Hence \(C_1=0\). Repeating with the next exponent gives \(C_j=0\) for every \(j\). Thus all the coefficients are supported on finitely many actual rows.

All sums in the statement are already well-defined before this reduction. The eventual-constant hypothesis makes every coefficient sequence bounded. By (9), for any \(t>2\),

\[
\sum_{\substack{m_0\leq m<n\\m,n\ {\rm odd}}}
S(n-m)n^{-t}
\leq\sum_{n>m_0}n^{1-t}<\infty.
\tag{12}
\]

Consequently the total weighted perturbation is absolutely summable; the proof does not rely on an unregulated infinite-row construction.

## 4. A rational-frequency mean with its tail justified

For any fixed integer \(l\), any odd prime \(q\), and \(1\leq a\leq q-1\), one has

\[
\boxed{
\lim_{N\to\infty}\frac1N
\sum_{\substack{1\leq k\leq N\\k>l}}
S(2(k-l))e(-ak/q)
=\frac{2}{(q-1)^2}e(-al/q),
}
\tag{13}
\]

where \(e(u)=\exp(2\pi i u)\). The condition \(k>l\) avoids assigning a value to the singular series at zero; deleting the finitely many earlier terms does not affect the limit.

For each fixed divisor \(d\), averaging the progression \(k\equiv l\pmod d\) against the indicated phase gives zero unless \(q\mid d\). If \(q\mid d\), its mean is \(e(-al/q)/d\). This follows from a complete geometric progression; no equidistribution of primes is used.

It remains to justify taking the mean term by term in (6). After a divisor cutoff \(D\), the absolute contribution of the omitted terms is at most a fixed multiple of

\[
\sum_{d>D}\frac{g(d)}d
+\frac{G(N+|l|)}N.
\tag{14}
\]

This bound follows by counting at most \(N/d+1\) integers in each progression. Equation (8) makes the second term tend to zero as \(N\to\infty\), and (7) makes the first tend to zero as \(D\to\infty\), in that order. Thus the passage is rigorous even though the pointwise divisor expansion is not a uniformly bounded finite sum.

The resulting Euler product is

\[
2C_2\sum_{q\mid d}\frac{g(d)}d
=2C_2\frac{1}{q(q-2)}
\prod_{\substack{p>2\\p\ne q}}\left(1+\frac1{p(p-2)}\right)
=\frac{2}{(q-1)^2},
\]

which proves (13). The factor two is the actual odd-endpoint/even-shift normalization.

## 5. Finite column combinations cannot tend to zero

Let \(u(l)\) be any finitely supported complex sequence. Suppose

\[
F(k)=\sum_l u(l)S(2(k-l))\longrightarrow0
\quad(k\to\infty),
\tag{15}
\]

where the expression is evaluated only after all the finitely many lower endpoints. Then \(u(l)=0\) for every \(l\).

For each fixed \(q,a\), (15) implies that the Cesaro mean of \(F(k)e(-ak/q)\) is zero. Applying (13) term by term in the finite sum gives

\[
\sum_l u(l)e(-al/q)=0
\quad(1\leq a\leq q-1).
\tag{16}
\]

If the support lies between integers \(l_-\) and \(l_+\), choose an odd prime with \(q-1>l_+-l_-\). The polynomial

\[
P(z)=\sum_l u(l)z^{l-l_-}
\]

has degree less than \(q-1\) and vanishes at all \(q-1\) nontrivial \(q\)-th roots of unity by (16). It is therefore zero. This argument uses all those roots, not irreducibility over the rationals: the coefficients are allowed to be arbitrary complex numbers. This proves the assertion.

## 6. Complete the proof of the theorem

By Section 3, every coefficient is supported on finitely many odd rows. Write those rows as \(m=2l+1\), and put

\[
F_j(k)=\sum_l c_j(2l+1)S(2(k-l)).
\]

For all sufficiently large integers \(k\), the column condition at \(n=2k+1\) reads

\[
\sum_{j=1}^r (2k+1)^{-t_j}F_j(k)=0.
\tag{17}
\]

By (10), each finite translate combination satisfies \(F_j(k)\ll_\eta k^\eta\) for every fixed \(\eta>0\), with constants depending on these fixed coefficients. Multiply (17) by \((2k+1)^{t_1}\). If \(r>1\), choose \(0<\eta<t_2-t_1\). Every term except \(F_1(k)\) tends to zero, so \(F_1(k)\to0\). If \(r=1\), this conclusion follows directly from (17). Section 5 forces all coefficients \(c_1(m)\) to be zero. Repeat with the next exponent. After finitely many steps every coefficient is zero, proving the theorem.

## 7. Meaning for the proposed arithmetic search

This result closes the specific proposed extension from two to three, or any other finite number of, **untruncated Pareto tails generated by compact lower-endpoint windows**. It permits arbitrary complex signs and does not merely exclude positive mixtures. It also allows all possible finite choices of smooth windows; it is not a negative result from a low-dimensional numerical span.

The restriction in (1) matters. With arbitrary growing row-dependent coefficients, the three-profile row and column system has more freedom than the two-profile system; the theorem makes no claim about that larger class. An actual variance application would have to prove its realization and convergence separately. A separate upper-endpoint cutoff also breaks the separated full-tail form (2), so it is not covered here.

The conclusion is about exact singleton-margin cancellation. It does not preclude approximate cancellation with an explicitly bounded error, or a signed perturbation whose margins are evaluated arithmetically instead of forced to zero. Those alternatives would require a quantitative comparison to the actual positive variance or Bragg deficit and an estimate of the residual double-prime sum. Neither comparison nor strict arithmetic bound is obtained in this note.

It would therefore be misleading to interpret this theorem as a new bound on zeta correlations. Its useful consequence is narrower: an exact-zero-margin search over finitely many genuine compact-window Pareto profiles is empty, so such a search should not be launched as a proposed route to a strict deficit.

## Sources and validation scope

The original kernel and the finite-profile question are specified in the root's [R24 realizability note](../kernel-realizability/ZERO_MARGIN_REALIZABILITY_TEST.md), SHA256 `818f0ac7b2952fd05fde28762079aeb94d23c72fbe8171e3298cedeb935bb60c`. The actual positive divisor expansion (6) is also written and used in [the frozen R23 fixed-modulus-6 report](../../research-round23/mod3-centering/FIXED_MOD6_CENTERING.md), SHA256 `ec3c4a258cf1ef2614e0255ee44c7c3a7e04268fe1655f082815f8012133285e`.

All new limits, Fourier means, and polynomial arguments used here are proved above. No external prime-distribution theorem, RH, numerical scan, or finite-height experiment is needed. The adjacent receipt pins the source files and this version. Ordinary independent review, rather than a numerical certificate, is the appropriate validation for the theorem.
