# Round 13 — Genuine-prime minor arcs and a fixed-inner-interval averaging audit

Status: completed ordinary mathematical source/proof audit, not a numerical enclosure or a theorem about zeta pair correlation. This note records the source theorem, the necessary major-arc coverage correction, and exactly what the current arithmetic packet permits. No new parameter scan was run.

## 1. Objects and the primary minor-arc theorem

Write \(e(u)=\exp(2\pi i u)\), and let
\[
P_N(\alpha)=\sum_{N\le p<2N}(\log p)e(\alpha p),
\qquad M\asymp X^{3/5},\quad N\asymp X^{2/5},\quad Q=X^{523/1000}.
\]
The inner support is fixed independently of the integer \(m\in I_M\), where \(I_M\) is an interval containing \(M+O(1)\) consecutive integers. The current outer coefficients initially satisfy \(|\alpha_m|\le1\). Extra divisor/logarithmic weights must be charged through their actual norms.

**Source theorem.** Montgomery and Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, author-hosted manuscript, Theorem 17.1, equation (17.29), printed page 65 (PDF page 77, zero-based index 76), states that, for coprime integers \(a,q\), \(q\ge1\), and
\[
|\alpha-a/q|\le q^{-2},
\]
\[
\left|\sum_{n\le Y}\Lambda(n)e(\alpha n)\right|
\ll \left(Yq^{-1/2}+Y^{4/5}+Y^{1/2}q^{1/2}\right)(\log Y)^{5/2}.
\tag{1}
\]
Definition (17.28) is explicitly the von Mangoldt prefix, not an arbitrarily twisted coefficient sequence. The proof on printed pages 65–66 chooses the Vaughan parameters \(U=V=Y^{2/5}\). It explicitly says that \(q>Y\) gives a bound weaker than the trivial estimate. Thus no usable \(q\le Y\) restriction should be silently imported into an application whose exact denominator exceeds \(Y\).

Primary source: [author-hosted Montgomery–Vaughan manuscript](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf). The version and local SHA256 are recorded in `sources/receipt.json`; this is a manuscript source, not a claim about publication status or the strongest possible modern estimate.

Taking two prefixes, and subtracting the prime powers, gives
\[
|P_N(\alpha)|\ll B_N(q),\qquad
B_N(q)=\left(Nq^{-1/2}+N^{4/5}+\sqrt{Nq}\right)(\log(2N))^{5/2}.
\tag{2}
\]
Indeed, the discarded powers contribute at most
\(\sum_{k\ge2,p^k\le2N}\log p\ll\sqrt N\log^2(2N)\), which is absorbed by (2). No RH is used here.

If \(w\) is of bounded variation on \([N,2N]\), partial summation gives the uniform weighted version
\[
\left|\sum_{N\le p<2N}(\log p)w(p)e(\alpha p)\right|
\ll \bigl(\|w\|_\infty+\operatorname{Var}(w)\bigr)B_N(q).
\tag{3}
\]
The same rational approximation applies to every prefix with endpoint between \(N\) and \(2N\), so there is no interval-uniformity gap. Smooth scaled weights \(w(p/N)\) have a constant depending on their fixed variation norm. Unweighted prime sums follow by replacing \(w(x)\) with \(w(x)/\log x\), which costs \(O(1/\log N)\). Uniform variation suffices for this pointwise statement even if the weight depends on \(m\); it does not, by itself, establish the fixed-coefficient orthogonality argument in Section 3.

## 2. The required major arcs, and an obstruction to narrower coverage

Let \(R=(\log X)^B\), with fixed \(B>0\), and take \(X\) large enough that \(2\le R\le\sqrt N\). Put
\[
\mathfrak M_R=\bigcup_{1\le q\le R}\ \bigcup_{(a,q)=1}
\left\{\alpha\pmod1:\left\|\alpha-a/q\right\|\le\frac{2R}{qN}\right\}.
\tag{4}
\]
The harmless factor 2 accommodates floors. Dirichlet approximation with denominator cap \(K=\lfloor N/R\rfloor\) gives coprime \(a,q\), \(q\le K\), and
\[
|\alpha-a/q|\le\frac1{qK}\le\frac{2R}{qN},
\qquad |\alpha-a/q|\le q^{-2}.
\]
Consequently, outside (4), \(R<q\le N/R\). Applying (2),
\[
|P_N(\alpha)|\ll
\left(NR^{-1/2}+N^{4/5}\right)(\log(2N))^{5/2}.
\tag{5}
\]
For any fixed desired logarithmic saving, a sufficiently large fixed \(B\) supplies it in this pointwise estimate.

It is incorrect to deduce this denominator range after deleting only neighborhoods \(|\alpha-a/q|\le C/N\), with fixed \(C\), for \(q\le R\). The available Dirichlet error is \(O(R/(qN))\), which is larger for small \(q\). A concrete obstruction is \(\alpha=K_0/N\), where \(K_0>C\) is a fixed nonintegral number. For large \(N\), this is outside all those fixed-width cores: for \(q\ge2\), \(a/q\) is separated from zero by at least \(1/R\), much larger than \(1/N\). But the ordinary PNT and partial summation give
\[
P_N(K_0/N)=N\int_1^2e(K_0u)\,du+o(N),
\]
with nonzero integral. It is therefore not a minor arc with arbitrary logarithmic cancellation. Grid phases with denominator \(d\gg N\) approximate such a point within \(1/d=o(1/N)\), so the issue also occurs in the sampled setting.

The coverage repair does **not** worsen the coarse bad-point count already contemplated. The total length of (4) is
\[
\ll\frac R N\sum_{q\le R}\frac{\varphi(q)}q\ll\frac{R^2}N,
\]
and the number of constituent circular intervals is \(O(R^2)\). For any reduced \(a/d\), multiplication by \(a\) permutes the grid of \(d\) residues. Counting complete periods and enlarging the final incomplete period yields
\[
\#\{m\in I_M:am/d\in\mathfrak M_R\}
\ll(M+d)\left(\frac{R^2}N+\frac{R^2}d\right).
\tag{6}
\]
Restriction to \((m,d)=1\) only decreases this count. The interval-count term in (6) must be retained before using the actual \(d>N\) range.

## 3. A stronger exact average at \(a=1\), including the natural centering

Let \(d>N\), and let \(b_n\) be any fixed coefficients supported in an integer interval of diameter less than \(d\). Orthogonality gives the exact identity
\[
\sum_{r\bmod d}\left|\sum_n b_ne(rn/d)\right|^2=d\sum_n|b_n|^2.
\tag{7}
\]
Completing successive periods of an arbitrary interval \(I_M\), using nonnegativity for its incomplete period, gives
\[
\sum_{m\in I_M}\left|\sum_n b_ne(mn/d)\right|^2
\le (\lfloor |I_M|/d\rfloor+1)d\sum_n|b_n|^2
\ll(M+d)\sum_n|b_n|^2.
\tag{8}
\]
For log-prime coefficients, Chebyshev's estimate gives
\(\sum_{N\le p<2N}(\log p)^2\ll N\log N\). Hence
\[
\sum_{m\in I_M}|P_N(m/d)|\ll\sqrt{M(M+d)N\log N}.
\tag{9}
\]
Here \(M>d\), so this is \(\ll M\sqrt{N\log N}\), with power \(X^{4/5}\). No minor-arc theorem is needed for this average. For general outer coefficients replace (9) by
\[
\left|\sum_m\alpha_mP_N(m/d)\right|
\ll\|\alpha\|_2\sqrt{(M+d)N\log N}.
\tag{10}
\]
This remains valid for every \((a,d)=1\) in place of 1.

The actual terminal expression has a unit mask and a principal centering. Suppose \(d\) is squarefree and all supported \(n\) are coprime to \(d\). Then the Ramanujan identity gives
\[
\frac1{\varphi(d)}\sum_{r\bmod d}^{*}\sum_n b_ne(rn/d)
=\frac{\mu(d)}{\varphi(d)}\sum_n b_n.
\]
Subtracting this exact unit-average constant decreases the unit mean square:
\[
\sum_{r\bmod d}^{*}\left|\sum_n b_ne(rn/d)-
\frac{\mu(d)}{\varphi(d)}\sum_n b_n\right|^2
=\sum_{r\bmod d}^{*}\left|\sum_n b_ne(rn/d)\right|^2
-\frac{|\sum_n b_n|^2}{\varphi(d)}
\le d\sum_n|b_n|^2.
\tag{11}
\]
Thus (8)–(10) also control the centered terminal sum restricted to \((m,d)=1\), without an added centering debt. In the current canonical conductor family every prime factor of \(d\) is \(\le X^{0.2615}<N\), so the required unit condition holds for every inner prime.

This calculation is strictly about fixed inner coefficients/support. A smooth product weight may be transferred through an explicitly summable separable expansion, with the sum of its coefficient norms charged. It is not permission to absorb \(e(amn/d)\) into arbitrary coefficients and then invoke Siegel–Walfisz. Arbitrary \(m\)-dependent phase absorption invalidates that inference.

For the top-conductor packet \(Q/2<d\le Q\), its exact conductor coefficient is \(M_d=\mu(d)/d\), the low reduced numerators satisfy \(a\le d/(16H)\), and \(|S_V(a/d)|\ll_V H\). Summing (9) absolutely over these indices gives only
\[
\sum_{d\asymp Q}\frac H d\frac d H\,
O\bigl(M\sqrt{N\log N}\bigr)
\ll Q M\sqrt{N\log N}=X^{1.323}(\log X)^{1/2}.
\tag{12}
\]
The coarse enlarged-major-arc count (6), followed by the trivial prime-sum bound, instead gives \(\ll QM R^2\) on those arcs. Neither bound is \(o(X\log X)\). There is a genuine averaging improvement for each fixed conductor/frequency; it does not yet give the required full arithmetic pairing improvement.

## 4. The \(q=1\) core has an RH square-root remainder

Schoenfeld's *Sharper bounds for the Chebyshev functions \(\theta(x)\) and \(\psi(x)\). II*, Theorem 10, equation (6.3), printed page 337, proves under RH
\[
|\theta(x)-x|<\frac1{8\pi}\sqrt x\log^2x\qquad(x\ge599).
\tag{13}
\]
Primary source: [AMS original paper](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf). The publisher PDF was downloaded directly and its first page read. Endpoint changes in the chosen half-open prime interval contribute at most \(O(\log N)\), already absorbed below.

Let \(\beta\) be the representative of \(am/d\pmod1\) with \(|\beta|\le C/N\), for fixed \(C\). Partial summation of (13) gives
\[
P_N(\beta)=J_N(\beta)+O\bigl((1+N|\beta|)\sqrt N\log^2N\bigr),
\qquad J_N(\beta)=\int_N^{2N}e(\beta u)\,du.
\tag{14}
\]
The error follows from two endpoint errors and
\(2\pi|\beta|\int_N^{2N}|\theta(u)-u|\,du\); this states the precise frequency uniformity. Fixed BV weights have the analogous variation cost.

For the centered terminal sum one can keep
\[
J_N(\beta)-\frac{\mu(d)}{\varphi(d)}P_N(0)
\]
as the explicit main term, retaining the principal term exactly. Alternatively \(P_N(0)=N+O(\sqrt N\log^2N)\) by RH, with a smaller additional error after division by \(\varphi(d)\).

The number of core \(m\)'s is
\[
\ll_C(M+d)(1/N+1/d).
\]
Combining this count with the same low-numerator and conductor weights as in (12), the total absolute remainder in (14) is at most
\[
\ll_{C,V}Q(M+Q)\sqrt N(1/N+1/Q)\log^2N
\ll_{C,V}\frac{QM}{\sqrt N}\log^2X
=X^{0.923}\,O_{C,V}(\log^2X).
\tag{15}
\]
This is a valid power-saving extraction for this identifiable component, initially with \(|\alpha_m|\le1\). It does not bound the explicit major main term, does not cover the enlarged \(q=1\) core uniformly in a growing \(C\) without paying the factor in (14), and does not transfer automatically to small \(q>1\). Square-root prime-AP errors at those other rationals require corresponding Dirichlet-L information; ordinary zeta RH does not provide it.

## 5. Accepted result and remaining obligation

The exact minor-arc theorem is applicable after the enlarged rational neighborhoods (4) are used. The fixed-inner-interval average is stronger than its pointwise application here, and the true unit mask/principal centering cause no loss by (11). The \(q=1\) component admits the rigorously small remainder (15), with its main term retained.

The missing step is cancellation in the actual weighted sum over conductors, reduced numerators, and the extracted arithmetic main terms. The estimates above neither prove such cancellation nor a zeta pair-correlation improvement. No claim is made for a coefficient sequence with an absorbed oscillatory phase, for unspecified product-weight separation, for arbitrary outer divisor coefficients at unit cost, or for the whole unsmoothed arithmetic packet.
