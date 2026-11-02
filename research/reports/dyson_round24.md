# Round 24: unrestricted nonprimitive removal and the exact Möbius–prime complement

Date: 2026-09-06. Status: ordinary mathematical proofs with full internal independent reviews. No RH, Montgomery–Dyson, GUE, AH-refutation, zeta-gap or sub-186 theorem is claimed. Novelty and proof-assistant verification remain separate obligations.

This round removes a restrictive modulus hypothesis from an actual prime-power estimate, identifies the complete complementary covariance with its correct centers, and excludes a specified family of exact zero-margin comparison kernels. The strict arithmetic inequality needed for actual zeta zeros remains open. The earlier 705-page public and 753-page local PDFs retain their Round 14 scope; this report and its complete source manuscripts extend the archive separately.

## 1. The unchanged target

With \(\ell=\log T\), retain the exact kernel
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}\,dx,
\]
where the fixed nonnegative smooth \(\omega\) is supported in \([7/4,9/4]\). On odd \(m\) and positive even \(h\), set
\[
q_2(m,h)=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2].
\]
The full target is
\[
Q_{2,T}=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
b_T(m)(1+h/m)^{-T}q_2(m,h).
\]
Under RH, the earlier reviewed transfer gives
\[
\overline V_T=M+Q_{2,T}+o(1),\qquad
M=\int\omega\approx0.1851531433.
\]
AH-Pairs forces the saturation value \(A\approx1.0105877964\). The desired new input is
\[
\boxed{\liminf_{T\to\infty}Q_{2,T}<A-M.}
\]
The benchmark \(\liminf Q_{2,T}\le1-M\) is stronger than necessary. Neither is proved.

The R24 arithmetic packet uses
\[
X=T^\alpha,\quad H=X/T,\quad Q=X^{523/1000},
\quad 11/5\le\alpha\le9/4,
\]
\[
F(m,h)=b_T(m)\chi(m/X)V(h/H)(m/(m+h))^T,
\]
with fixed smooth cutoffs compactly supported in \((1,2)\). The new nonprimitive lemma has wider hypotheses than this combined packet argument; the other estimates keep their own stated restrictions.

## 2. Nonprimitive removal for every odd divisor subset

The [author proof](../dyson/round24/general-nonprimitive/GENERAL_NONPRIMITIVE_BOUND.md) and [Plato's independent review](../dyson/round24/general-nonprimitive-review/INDEPENDENT_NONPRIMITIVE_REVIEW.md) prove
\[
\boxed{\mathcal N_{\mathcal D}\ll_\eta X^\eta/T}
\]
for every subset of distinct odd divisors \(d\le Q<X\). The earlier largest-prime owner restriction is unnecessary.

The new observation is an extra condition in the actual summand. If \(n=m+h=p^j\) has nonzero prime weight and is nonprimitive modulo \(d\), then
\[
p\mid d,\qquad p\mid h,\qquad j\ge2.
\]
The last assertion follows from \(d\le Q<X<n<3X\). Thus \(p\le\sqrt{3X}\). Writing \(h=2pr\), the support gives the exact count
\[
\#\{r:H/(2p)<r<H/p\}\le H/p.
\]
When \(p>H\), the set is empty. No extra rounding term or assumption \(H\gg\sqrt X\) is needed.

For each actual \(m=n-h\), the full divisor coefficient is bounded by
\[
\sum_{\substack{d\mid m\\d\le Q}}
|\mu(d)|\log(m/d)\le\tau(m)\log(2X)
\ll_\eta X^\eta\log X.
\]
There are at most two powers of each odd prime in \((X,3X)\). Combining the amplitude \(F\ll1/(X\ell^2)\) with the elementary estimate
\[
\sum_{p\le Y}\frac{\log p}{p}\ll\log(2Y)
\]
proves the bound. It uses the complete von Mangoldt sequence, not a prime-only replacement, and needs neither RH nor a distribution theorem in progressions.

At \(\eta=1/100\), the R24 upper-window range gives \(X^{-391/900}\). The mathematical improvement is the divisibility count; six exact scalar checks verify exponent arithmetic only.

Consequently the small-divisor opening may use all odd \(d\le Q\), whenever the separate primitive completion estimate is legal.

## 3. The exact complement and its two centers

The [complete cofactor proof](../dyson/round24/small-cofactor-target/SMALL_COFACTOR_CENTERED_TARGET.md) and [Aquinas's independent review](../dyson/round24/small-cofactor-review/INDEPENDENT_SMALL_COFACTOR_REVIEW.md) keep
\[
c_Q(m)=\sum_{\substack{d\mid m\\d>Q}}\mu(d)\log(m/d)
\]
with its sharp cutoff. Writing \(m=kd\) gives
\[
\mathcal C_Q=
2\sum_{\substack{3\le k<K\\k\ {\rm odd}}}\log k
\sum_{\substack{d>Q\\d\ {\rm odd}}}\mu(d)
\sum_{h\ {\rm even}}F(kd,h)\Lambda(kd+h),
\qquad K=2X/Q.
\]
The \(k=1\) term is zero. The endpoint \(k<K\) is strict, and no condition \((k,d)=1\) is imposed.

For the primitive cofactor mask \((h,k)=1\), the exact prime center is \(2k/\varphi(k)\). Define
\[
\mathcal Z_Q=
2\sum_{\substack{3\le k<K\\k\ {\rm odd}}}\log k
\sum_{\substack{d>Q\\d\ {\rm odd}}}\mu(d)
\sum_{\substack{h\ {\rm even}\\(h,k)=1}}
F(kd,h)\left[\Lambda(kd+h)-\frac{2k}{\varphi(k)}\right].
\]
Every removed raw nonprimitive term is charged using the same \(p\mid h\) restriction. Its entire added-back center completes to
\[
\mathcal L_Q^0=2\sum_{m\ {\rm odd}}c_Q(m)J_-(m),
\qquad J_-(m)=\int F(m,h)\,dh,
\]
with error \(O((K/H)\log^3X)\). The proof retains the physical-shift density \(\varphi(k)/(2k)\) until it cancels the added center. In this range
\[
K/H\le2X^{-753/11000}.
\]

A separate exact flat-centered object is
\[
\mathcal Z_Q^{(2)}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)c_Q(m)[\Lambda(m+h)-2].
\]
After paying all mask and center debts, the proof gives
\[
\mathcal Z_Q=\mathcal Z_Q^{(2)}
+O_\eta\!\left(X^\eta/T+(K/H)\log^3X\right).
\]
One may not replace the primitive center by two before this comparison. Conversely, using the flat object directly in a later proof need not inherit a condition introduced solely for primitive-cofactor completion.

At the R24 freeze, the remaining packet is
\[
\boxed{\mathcal A_Q+\mathcal L_Q^0+\mathcal Z_Q
-\mathcal M_{\mathfrak S}+o(1).}
\]
The original small-divisor principal \(\mathcal A_Q\), both singular-series prime marginals, and the constant two remain. Their joint evaluation is a separate subsequent task.

## 4. A failed source application and the honest analytic bound

Absorbing \(\mu((n-h)/k)\) into a smooth weight does not supply a legal application of the 186 one-prime theorem. The manuscript proves a concrete variation obstruction: squarefree \(d\equiv11\pmod{18}\) have \(|\mu(d)|=1\), but \(9\mid d-2\), so \(\mu(d-2)=0\). A positive-density count with an \(O(\sqrt D)\) error makes the actual odd-grid variation of order \(D\).

This rejects that literal weighted partial-summation application. It does not exclude every alternative representation or a genuinely joint dispersion estimate.

The RH short-interval mean-square estimate at exponent three from [Carneiro–Chandee–Chirre–Milinovich](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), printed page 1 equations (1.1) and (1.3), is valid here. The proof keeps real-to-integer endpoints, powers of two, the discrete odd-grid center and the actual second moment of \(c_Q\). It yields
\[
\boxed{|\mathcal Z_Q^{(2)}|
\ll\sqrt H\,\log^{3/2}X.}
\]
This grows; it is not the needed \(O(1)\) or strict upper bound.

The scale issue is substantive. For a fixed interior \(\alpha\), nonnegative nonzero cutoffs and \(\omega(\alpha)>0\), the packet mass is asymptotic to
\[
\frac{H}{2\ell^2}\omega(\alpha)
\int\!\!\int\frac{\chi(v)}vV(z)e^{-z/v}\,dz\,dv.
\]
Only this mass limit uses the limiting exponential; the arithmetic kernel stays exact. A relative \(o(1)\) error on mass \(H/\ell^2\) need not be small at fluctuation scale. Even an illustrative relative \(X^{-1/2}\log^2X\) leaves \(H/\sqrt X\), which grows with exponent between \(1/22\) and \(1/18\). The large mains must be combined before estimating them.

## 5. Exact zero-margin kernels: the one- and two-profile theorem

The [root proof](../dyson/round24/kernel-realizability/ZERO_MARGIN_REALIZABILITY_TEST.md), [Plato review](../dyson/round24/kernel-realizability-review/INDEPENDENT_REALIZABILITY_REVIEW.md), and [coordinator review](../dyson/round24/coordinator-realizability-review/COORDINATOR_REALIZABILITY_REVIEW.md) examine a proposed exact comparison route.

At one exponent \(t>2\), the actual triangular kernel is \(c(m)n^{-t}\) on odd \(m<n\). Its singular-series row mass
\[
A_t(m)=\sum_{\substack{n>m\\n\ {\rm odd}}}
\mathfrak S(n-m)n^{-t}
\]
is strictly positive. An exact zero row therefore forces \(c(m)=0\).

For two distinct exponents \(t_1>t_2>2\), allow arbitrary row-dependent coefficients. The row relation fixes their ratio through \(A_{t_1}(m)/A_{t_2}(m)\), a strict weighted average of \(n^{-(t_1-t_2)}\). It is strictly below the nearest-column value. The first available column forces the first row coefficients to vanish; induction proves the same for every row.

No growth bound on these two coefficient functions is required. The theorem does require the full triangular tail and exact margins. It does not address an independent upper cutoff or approximate margins.

## 6. The finite compact-window extension

[Plato's complete extension](../dyson/round24/finite-window-realizability/FINITE_WINDOW_ZERO_MARGIN_THEOREM.md), read fully by root and independently accepted in the [coordinator review](../dyson/round24/coordinator-realizability-review/COORDINATOR_REALIZABILITY_REVIEW.md), handles every finite collection of distinct exponents \(t_j>2\) with row coefficients that are eventually constant. This covers the actual compact lower-window primitives under investigation.

The positive divisor expansion gives
\[
A_t(m)\sim m^{1-t}/(t-1).
\]
The row equations first force every eventual constant to vanish, leaving finitely many rows.

The essential independence statement is the rational-frequency mean
\[
\lim_{N\to\infty}\frac1N
\sum_{\substack{k\le N\\k>l}}
\mathfrak S(2(k-l))e(-ak/q)
=\frac{2}{(q-1)^2}e(-al/q)
\]
for every fixed \(l\), odd prime \(q\), and \(a=1,\ldots,q-1\). The divisor tail is explicitly bounded by
\[
\sum_{d>D}\frac{g(d)}d+\frac{G(N+|l|)}N,
\qquad G(Y)\ll\log(2Y),
\]
with \(N\) taken to infinity before \(D\).

If a finite translate combination tends to zero, its coefficient polynomial vanishes at all \(q-1\) nontrivial \(q\)-th roots. Taking \(q-1\) above its degree forces all coefficients to vanish, even for arbitrary complex coefficients. One root alone would not suffice.

A subpower singular-series bound then separates every pair of distinct exponents, however close. Full weighted absolute convergence is proved before the limiting column argument. Hence every exact zero-margin kernel in this finite compact-window family is zero.

The result holds separately at each external height even if the finite profile count depends on that height. It supplies no uniform estimate for approximate margins. It closes this specific exact search; it does not exclude unrelated kernel classes or general arithmetic methods.

## 7. Preserved evidence and checks

All **42 original files, 188,323 bytes**, are preserved verbatim in the public round folder and the adjacent local archive. They include complete proofs, independent reviews, exact outputs, source receipts and the working note's historical review status. Later acceptance is recorded separately rather than rewriting old submission labels.

Additional evidence is kept as distinct files:

- [Late coordinator R23 mod-six review](../dyson/round24/coordinator-r23-review/COORDINATOR_MOD6_REVIEW.md).
- [Coordinator R23 publication check](../dyson/round24/coordinator-intake/COORDINATOR_R23_PUBLICATION_VERIFICATION.json), with its explicit coverage.
- [Updated 186/FLT memo after realizability](../dyson/round24/coordinator-intake/ASTRA_186_FLT_TOOLS_AFTER_REALIZABILITY.md); the previous R23 memo remains unchanged.

Integration verified **196 dependency records**, with zero unresolved hashes, zero path substitutions and zero unresolved historical relative links. The complete author and independent nonprimitive JSON/stdout outputs agree byte for byte. The cofactor review separately records eight exact assertions and source verification. Integration did not repeat these mathematical runs.

See the [intake manifest](../dyson/round24/INTAKE_MANIFEST.json), [source-link map](../dyson/round24/SOURCE_LINK_MAP.md), and [integration receipt](../logs/round24-integration/INTEGRATION_RECEIPT.json). The local originals are in Astra-Local-Archive/round24-originals. The earlier 23-file working ZIP remains an explicitly incomplete historical snapshot.

No new prime-height scan, prime-gap sweep, model call or large PDF build is part of this checkpoint. Scalar checks support exact arithmetic, not formal verification of analytic theorems.

## 8. Next mathematical obligation

Finish the joint evaluation of \(\mathcal A_Q+\mathcal L_Q^0-\mathcal M_{\mathfrak S}\), retaining every mask, center and endpoint. Then bound the actual signed Möbius–prime covariance and justify the scale partition needed for the full variance. A fixed compact packet alone does not imply the full statistic.

Postpone further searches inside the excluded exact kernel family, another prime-gap sweep, and generic RMT simulations without a zeta transfer. Completed stable lemmas may later enter a proof-assistant queue. Reverting this round's research commit restores the preceding publication without rewriting historical sources.
