# Round 26: a full actual-variance reduction with its nonzero singular-series correction

Date: 2026-09-06. Status: complete ordinary mathematical proof with independent full reviews. The main theorem assumes ordinary RH. It covers the whole height and length range of the fixed actual prime variance. It does not prove a strict improvement of that variance, exclude AH, establish Montgomery–Dyson/GUE, or prove RH. External novelty assessment and proof-assistant verification remain open.

The key change from Round 25 is that the physical shift cutoff now varies by scale. This permits a full partition, but the small singular-series correction in each packet accumulates to a nonzero constant. The proof computes that constant and pays every discarded endpoint and tail.

Read the [complete author proof](../dyson/round26/full-shift-reduction/FULL_SHIFT_REDUCTION.md), [Plato's independent full review](../dyson/round26/global-reduction-review/INDEPENDENT_GLOBAL_REDUCTION_REVIEW.md), [independent correction derivation](../dyson/round26/singular-correction-review/REFINED_SINGULAR_CORRECTION.md), and [coordinator full review](../dyson/round26/coordinator-global-review/COORDINATOR_GLOBAL_REDUCTION_REVIEW.md).

## 1. Exact statement

Keep
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},
\quad W_T(x)=\omega(\log x/\ell),
\]
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}\int_1^mW_T(x)x^{T-2}\,dx,
\qquad k_T(m,h)=(m/(m+h))^T.
\]
The weight \(\omega\) is fixed, smooth and nonnegative, supported in \([7/4,9/4]\). Initially distinguish
\[
M_0=\int\omega(u)\,du,\qquad
M_1=\int(u-1)\omega(u)\,du.
\]
For the actual symmetric bump about two, \(M_1=M_0=M\), with the previously computed diagnostic \(M\approx0.1851531433\).

The full parity-adjusted target remains
\[
Q_{2,T}=2\sum_{\substack{m\ {\rm odd}\\h\ge2,\ h\ {\rm even}}}
b_T(m)k_T(m,h)
\{\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\}.
\]
The inherited R21/R22 theorem assumes RH and says
\[
\overline V_T=M_0+Q_{2,T}+o(1).
\]
It includes the full continuous center and every prime power.

Choose one fixed smooth nonincreasing \(r\), equal to one on \([0,1]\) and zero on \([2,\infty)\), with values in \([0,1]\). Set
\[
\beta(t)=r(t)-r(2t),\qquad
Y_0=\sqrt\ell,\quad R=32\ell,\quad Y_j=2^jY_0,
\quad Q_j=Y_j^{2/3}.
\]
For odd \(m\), put
\[
c_{Q_j}(m)=\sum_{\substack{d\mid m\\d>Q_j}}
\mu(d)\log(m/d),\qquad
c_T(m,h)=\sum_{j\ge0}\beta(h/Y_j)c_{Q_j}(m).
\]
The sharp divisor threshold is part of the definition. Now define the finite actual covariance
\[
\boxed{
Z_T=2\sum_{\substack{m\ {\rm odd}\\h\ge2,\ h\ {\rm even}}}
b_T(m)r(m/(2U))r(Th/(Rm))k_T(m,h)
c_T(m,h)[\Lambda(m+h)-2].}
\]
The support has \(m<4U\), \(h<2Rm/T\), and only finitely many shift scales. No \((k,d)=1\) condition or generic replacement sequence is introduced.

The new theorem is
\[
\boxed{Q_{2,T}=Z_T+M_1+O((\log T)^{-1/2})}
\]
under ordinary RH. Consequently, for the actual symmetric weight,
\[
\boxed{\overline V_T=Z_T+2M+o(1).}
\]
The last \(o(1)\) also includes the separately established variance transfer. This is a full reduction, not a strict bound for the covariance.

## 2. Why the constant is present

The unconditional singular-series input is [Montgomery–Soundararajan, equation (47), printed page 16](https://arxiv.org/pdf/math/0409258v1):
\[
2\sum_{h\ge1}(N-h)_+\mathfrak S(h)
=N^2-N\log N+B N+O_\nu(N^{1/2+\nu})
\]
for integers \(N\), with fixed \(B\). This statement concerns the singular series itself; it does not assume the paper's conjectural prime-pair asymptotics.

The hinge sum interpolates linearly between integer endpoints. The smooth main has bounded second derivative on \([1,\infty)\), so the same asymptotic holds for real endpoints with only an additional \(O(1)\) error.

For a smooth function \(f\) supported on \((Y/2,2Y)\), with amplitude \(A_f\) and derivative scale \(Y\), the exact hinge identity and two integrations by parts give
\[
\boxed{
\sum_{h\ {\rm even}}\mathfrak S(h)f(h)
=\int f(h)\,dh-\frac12\int\frac{f(h)}h\,dh
+O_\nu(A_fY^{-1/2+\nu}).}
\]
The linear term is killed because \(\int y f''(y)\,dy=0\). The remainder is integrated against \(|f''|\); it is never differentiated.

For one fixed natural-scale packet, the displayed correction was \(O(\ell^{-2})\) after summing endpoints, hence negligible in R25. Across all height and shift scales it has a finite total. Treating every such contribution as an error would lose that constant.

## 3. An exact finite partition

Set \(X_i=2^iL\). The actual packet is
\[
F_{ij}(m,h)=b_T(m)\beta(m/X_i)\beta(h/Y_j)
r(m/(2U))r(Th/(Rm))k_T(m,h).
\]
The telescoping identities are
\[
\sum_i\beta(m/X_i)=1\quad(m>L),\qquad
\sum_j\beta(h/Y_j)=1-r(2h/Y_0).
\]
Only
\[
X_i<8U,\qquad Y_j<8RX_i/T
\]
can contribute. There are \(O(\ell)\) height blocks and \(O(\ell)\) shift blocks at each height. The fixed-ratio support is \((1/2,2)\), and the small endpoint enlargements beyond the old fixed-\(\alpha\) range are retained.

For every fixed pair of derivative orders,
\[
|\partial_m^a\partial_h^bF_{ij}|
\ll_{a,b}(X_i\ell^2)^{-1}X_i^{-a}Y_j^{-b}.
\]
These constants are uniform. Although \(Y_j/(X_i/T)\) can grow like \(\ell\), its fixed polynomial derivative costs are absorbed by the actual Pareto decay. The two moving upper cutoffs are differentiated on their genuine scales. No growing derivative order or hidden logarithmic seminorm is used.

The direct \(q_2\) small-shift estimate gives
\[
\sum_{h\le K}\text{absolute weighted }q_2
\ll K/\ell+K\ell L^{-1/2}+K2^{-T}.
\]
Its proof applies the inherited uniform upper sieve to the actual prime product and Chebyshev to both singular-series marginals. It does not infer a bound for \(q_2\) merely from an earlier bound for a different centered coefficient. Taking \(K=\lceil\sqrt\ell\rceil\) removes the low shift cutoff at cost \(O(\ell^{-1/2})\).

The actual height tail beyond \(2U\) is \(O(U2^{-T})\). The removed length tail is \(O((RU/T)e^{-R/4})\), hence \(O(\ell T^{-27/4})\). Both follow from the exact tail of \(b_T\), monotone integral comparison, and the elementary bound \(\sum_{h\le y}\mathfrak S(h)\le y\). Absolute convergence is justified before the partition is summed.

## 4. All local errors are summable

In each nonzero packet write \(X=X_i\), \(Y=Y_j\), \(Q=Y^{2/3}\). The R25 five-term divisor identity remains exact. The changed scale is handled directly; a theorem requiring fixed-power \(Q\) is not silently extended to \(Q\asymp\ell^{1/3}\).

Use fixed completion orders \(16\) for the primitive discrepancy, \(36\) for the principal's primitive mask, and \(4\) for the complementary flat center. The nonprimitive prime-power count again uses \(p\mid h\), with \(O(Y/p)\) shifts and no \(Y\gg\sqrt X\) requirement.

Under ordinary RH, the same centered Möbius argument works uniformly down to \(Q=\ell^{1/3}\). Its error is
\[
\frac{Y}{\sqrt X}Q^{-1/2+\epsilon}\log X.
\]
The parameter \(Q\) is fixed within each packet when derivatives and Abel summation are performed.

The complete local identity is
\[
\mathcal P_{ij}=\mathcal Z_{ij}^{(2)}+\mathcal D_{ij}
+\mathcal R_{ij}.
\]
With fixed \(\epsilon=\eta=1/100\) and singular-series exponent \(\nu=1/4\), the nine errors sum as follows:

| Source of error | Bound after summing all packets |
|---|---|
| Primitive discrepancy | \(O(\ell^{-7/3})\) |
| Nonprimitive prime powers | \(O(R\ell U^{1/100}/T)\) |
| Principal-mask completion | \(O(\ell^{-2})\) |
| Nonunit principal mean | \(O(R\ell^2/T)\) |
| Complementary flat-center grid | \(O(\ell^{-1})\) |
| Odd-cofactor completion | \(O(R^{7/3}T^{-19/12}/\ell)\) |
| Joint centered RH remainder | \(O(R^{101/150}\ell T^{-17/60})\) |
| Refined singular-series remainder | \(O(\ell^{-9/8})\) |
| Final odd endpoint grid | \(O(R/(TL\ell^2))\) |

Negative powers of \(Y\) are summed geometrically from \(Y_0\), and positive powers from the last allowed scale. The two nontrivial height sums are geometric in \(X^{1/3}\) and \(X^{13/75}\), respectively. The table is a proved uniform error ledger, not a set of finite numerical observations.

## 5. Evaluation of both marginal corrections

Write
\[
I_-(m)=\int F_{ij}(m,h)\frac{dh}{h},\qquad
I_+(n)=\int F_{ij}(n-h,h)\frac{dh}{h}.
\]
The refined transform produces exactly
\[
\mathcal D_{ij}
=\sum_{m\ {\rm odd}}\Lambda(m)I_-(m)
+\sum_{n\ {\rm odd}}\Lambda(n)I_+(n)
-2\sum_{m\ {\rm odd}}I_-(m).
\]
The sign is positive in \(\mathcal P-\mathcal Z\), because the negative singular-series correction is subtracted in the original target.

Ordinary RH replaces both prime marginals by their continuous integrals, with total error \(O(\ell L^{-1/2})\). The odd integer measure has density one half. The two continuous prime integrals agree by Fubini, leaving one copy of
\[
\mathcal I_T=\iint b_T(m)r(m/(2U))r(Th/(Rm))k_T(m,h)
[1-r(2h/Y_0)]\,\frac{dh\,dm}{h}.
\]
For \(H_m=m/T\), its inner integral is
\[
\log(H_m/Y_0)+O(1)
\]
uniformly on the full retained height range. The lower transition costs at most a fixed logarithm; the true Pareto tail is bounded directly.

The two independent proofs evaluate the outer integral in complementary ways. The author uses a uniform approximation of \(b_T\) by \(W_T(m)/(m\ell^2)\) with a paid \(O(T^{-1})\) integrated error. The independent companion computes the exact moments
\[
\int b_T(m)\,dm=\frac{T}{T-1}\frac{M_0}{\ell},
\]
\[
\int b_T(m)\log m\,dm
=\frac{T}{T-1}\int u\omega(u)\,du
+\frac{TM_0}{(T-1)^2\ell}.
\]
Both give
\[
\mathcal I_T=M_1-\frac{\log Y_0}{\ell}M_0
+O(\ell^{-1})=M_1+O(\log\ell/\ell).
\]
Combining this with the paid small-shift error proves the full theorem.

## 6. What is now bounded, and what remains open

The global \(Z_T\) is different from an individual fixed R25 packet. The inherited RH facts
\[
0\le\overline V_T,\qquad\limsup_T\overline V_T\le A
\]
and the new exact reduction immediately imply
\[
-2M\le\liminf_T Z_T\le\limsup_T Z_T\le A-2M.
\]
Thus the global covariance is already \(O(1)\) under RH by the existing variance bound. This is inherited information, not a new improvement. Individual packet and matrix estimates can still grow.

The actual desired improvement is
\[
\boxed{\liminf_T Z_T<A-2M.}
\]
The stronger sufficient benchmark is \(\liminf Z_T\le1-2M\). Neither is proved. The fixed AH-Pairs prediction would give \(Z_T\to A-2M\), whereas the full GUE prediction would give \(Z_T\to-M\). These remain predictions, not established limits. Expecting this newly defined covariance to tend to zero would discard its deterministic correction.

The R25 Fourier estimate cannot be applied globally unchanged. At the lowest scale \(Q=\ell^{1/3}\), the Möbius summation length may be only polylogarithmic, so \(\log D\asymp\log X\) is false. A proposed remote frequency cutoff may also exceed the whole half-period cell. Any global Fourier argument must rebuild these ranges with the actual weights.

## 7. Evidence and the next research question

The author proof, 22,834 bytes with SHA256 c0d413f2eead98cfc97de09cd5b4f8ffaa0df7a6b81249df576ccff61a0cadd6, has complete Plato and coordinator reviews. Root read the entire proof. The independent correction manuscript is 14,577 bytes with SHA256 b6a6211db21df5e5d10031027863eb4764bdab820f60ab4befb63c8dc9caeffe.

Seven groups comprising 2,793 exact finite checks were independently replayed with complete JSON and stdout bytes identical. The companion has eight symbolic checks. The coordinator also independently checked ten rational exponents, with its narrower replay scope stated explicitly. These are not Lean proofs or numerical evidence for an unproved sign.

The [intake manifest](../dyson/round26/INTAKE_MANIFEST.json), [source-link map](../dyson/round26/SOURCE_LINK_MAP.md), and [integration receipt](../logs/round26-integration/INTEGRATION_RECEIPT.json) preserve complete original proofs, reviews, outputs and source hashes. Full third-party source bodies remain local. Historical submission labels are not rewritten.

The next substantive question is whether joint cofactor dispersion or mixed moments of an actual divisor approximant can establish the strict upper bound. A positive residual norm often supplies only a lower bound, and the cutoff here depends on the shift separation. Both points must be checked before invoking a projection or sieve theorem. Postpone factorwise numerical scans, another exact-kernel search in the excluded family, and claims of a famous-conjecture breakthrough. Reverting this round's research commit restores the preceding publication without rewriting source history.
