# Independent review of the actual prime-power tail estimate

Date: 2026-09-05. Reviewer: `yau_flow`, separately from the authoring coordinator.

Reviewed final author artifact: `PRIME_POWER_TAIL_ESTIMATE.md`, SHA-256 `e7fff21fa21285a20968c218e99b17b3bc634bf28b88268c002f406a0fdd6cd0`. The initial complete review covered the corrected six-section version `b28cc13877d38d7cc83956127ace275df1f87585df8f2905fc309e77ae6d2349`; the final appended uniform corollary and corrected formula markup were subsequently read and accepted. Section 7 below records the independent derivation of that corollary.

**Verdict:** the tail estimate, residual-energy replacement, and exact genuine-prime continuation are accepted as ordinary mathematical arguments. No missing endpoint, square-frequency factor, or uncontrolled infinite off-diagonal sum was found. The author has corrected the minor provenance sentence to acknowledge the RH prime-counting-error estimate as well as the logarithmic-derivative estimate. No numerical scan or new experiment was run.

## 1. Scope of the unconditional estimate

For \(0<\delta\leq1/4\), \(\sigma=1/2+\delta\), \(N\geq4\), and \(T>0\), the series
\[
U(t)=\sum_{p^k>N,\ k\geq2}(\log p)p^{-k\sigma-ikt\log p}
\]
converges absolutely and uniformly in real \(t\) for each fixed \(\delta>0\). The sum over squares is majorized by \(\sum_{n\geq2}(\log n)n^{-1-2\delta}\); the higher powers converge even at \(\delta=0\). The claimed uniform estimate
\[
\|U\|_{L^2(0,T)}^2
\ll T N^{-1/3}\log^4(2N)+\delta^{-4}
\tag{1}
\]
does not use RH. Uniformity means the implied constant is independent of \(\delta,N,T\) in the displayed range, not that the second term remains bounded as \(\delta\downarrow0\).

## 2. Squares: frequency and infinite near-diagonal terms

For prime squares, the coefficients are
\(a_p=(\log p)p^{-1-2\delta}\), and the time phase is \(e^{-2it\log p}\). Therefore
\[
\left|\int_0^T e^{2it\log(m/n)}dt\right|
\leq\frac1{|\log(m/n)|}
\]
for \(m\ne n\). The factor one, rather than two, is correct because of the square frequency.

If \(n/2\leq m\leq2n\), then
\(|\log(m/n)|\geq|m-n|/(2n)\). Uniformly in the allowed \(\delta\),
\[
\frac{|a_ma_n|}{|\log(m/n)|}
\ll\frac{\log^2(2n)}{n^{1+4\delta}|m-n|}.
\]
The remaining harmonic sum costs \(O(\log(2n))\), giving
\[
\sum_{n\geq2}\frac{\log^3(2n)}{n^{1+4\delta}}
\ll\delta^{-4}.
\]
The comparison follows directly from integrals of \((\log x)^j x^{-1-4\delta}\), \(0\leq j\leq3\). Their powers \(\delta^{-j-1}\) are all absorbed by \(\delta^{-4}\) on \(0<\delta\leq1/4\). This checks the deliberate fourth power of the error.

For noncomparable pairs the denominator is bounded below by \(\log2\). The product majorant is
\[
\left(\sum_{n\geq2}\frac{\log n}{n^{1+2\delta}}\right)^2
\ll\delta^{-4}.
\]
Both estimates legitimately enlarge prime sums to integer sums and remove the cutoff. Every resulting series converges for each positive \(\delta\). Finite partial sums can consequently be passed to the infinite series without invoking a mean-value theorem with divergent error.

The diagonal is bounded by
\[
T\sum_{p>\sqrt N}\frac{(\log p)^2}{p^{2+4\delta}}
\ll T N^{-1/2}\log^2(2N).
\]
This proves the square part of the author's estimate, including its normalization and uniformity.

## 3. Higher powers and the endpoint sign

For \(A_3(x)=\sum_{p^k\leq x,k\geq3}\log p\), the elementary bound
\(A_3(x)\ll x^{1/3}\log^2(2x)\) is valid: there are at most \(O(\log x)\) exponents, at most \(x^{1/3}\) bases for each, and each weight is \(O(\log x)\). No prime-counting asymptotic is assumed.

The exact partial-summation formula for the strict tail is
\[
\sum_{p^k>N,k\geq3}(\log p)p^{-k\sigma}
=-A_3(N)N^{-\sigma}
 +\sigma\int_N^\infty A_3(x)x^{-\sigma-1}dx.
\]
The endpoint term is nonpositive and can be discarded in this upper bound. This remains correct when \(N\) itself is a prime power, provided \(A_3(N)\) includes that atom, as the definition does.

Since \(\sigma-1/3\geq1/6\), the integral is
\(O(N^{-1/6}\log^2(2N))\) uniformly for \(\sigma\in(1/2,3/4]\). Squaring the resulting uniform-in-time bound gives
\(O(TN^{-1/3}\log^4(2N))\). Combining the square and higher-power estimates with \(|u+v|^2\leq2|u|^2+2|v|^2\) proves (1). Prime powers have a unique prime base; there is no duplicate counting between the \(k=2\) and \(k\geq3\) pieces.

## 4. Replacement in the actual residual

Now set \(\delta=c/\log T\), with fixed \(c>0\), and \(N=\lfloor T/\log^6T\rfloor\). Under RH, the already proved bound
\(\|R\|_2\ll_c\sqrt T\log^2T\) applies. Taking a square root in (1) gives
\[
\frac{\|U\|_2}{\sqrt T}
\ll_c a_T:=N^{-1/6}\log^2(2N)+\frac{\log^2T}{\sqrt T}.
\]
The exact norm expansion and Cauchy–Schwarz yield
\[
\frac{|\|R-U\|_2^2-\|R\|_2^2|}{T\log^2T}
\ll_c a_T+\frac{a_T^2}{\log^2T}.
\]
At the stated cutoff \(a_T\to0\), so its quadratic term is absorbed into \(O_c(a_T)\) for all sufficiently large \(T\). This proves the author's displayed error. The dependence on \(c\), including the factor from \(\delta^{-2}\), is correctly contained in \(\ll_c\). Applying the estimate separately at the two fixed widths preserves an \(o(1)\) replacement error; it does not improve the signed target's limiting constant.

## 5. The exact genuine-prime identity

Let \(U_{\rm all}(s)=\sum_{p,k\geq2}(\log p)p^{-ks}\), which is absolutely convergent on \(\Re s>1/2\). Decompose the finite von Mangoldt polynomial as
\[
P_N=P_N^{\rm prime}+P_N^{\rm power},\qquad
U_{\rm tail}=U_{\rm all}-P_N^{\rm power}.
\]
Then exactly
\[
R-U_{\rm tail}=H-U_{\rm all}-P_N^{\rm prime}.
\]
This checks that powers \(p^k\leq N\) cancel once, and the strict tail \(p^k>N\) removes precisely the remaining powers. In particular, there is no off-by-one correction at a prime-power cutoff.

For \(\theta(x)=\sum_{p\leq x}\log p\), the Stieltjes continuation of the prime-only function gives
\[
R-U_{\rm tail}
=\frac{N^{1-s}}{s-1}-(\theta(N)-N)N^{-s}
 +s\int_N^\infty(\theta(x)-x)x^{-s-1}dx.
\]
The endpoint includes a prime equal to \(N\). Under RH,
\(\psi(x)-x=O(\sqrt x\log^2(2x))\), and the elementary sum of powers \(k\geq2\) is \(O(\sqrt x\log^2(2x))\), so the same bound holds for \(\theta(x)-x\). The integral is absolutely convergent for \(\Re s>1/2\). These facts verify the exact continuation and its analytic domain.

The only requested editorial clarification concerned §6 of the initial author draft: its phrase “the only RH input” needed to acknowledge both the logarithmic-derivative bound used for the norm and the RH prime-counting-error bound used for this representation. The revised §6 does so. Both inputs were already present in Round 8; this correction does not change the result.

## 6. Review scope

The entire six-section author draft was inspected. The review checked the infinite sums directly and did not replace them with finite numerical evidence. No numerical check is needed to establish their convergence or endpoint signs, and none was run. The result is an arithmetic simplification of the unresolved covariance problem. It neither supplies the missing positive constant nor certifies the desired residual lower bound.

## 7. Independently checked uniform mesoscopic corollary

Write \(L=\log T\). The same proof makes the residual-energy replacement uniform for
\[
1\leq c\leq L/4.
\]
Indeed, the RH logarithmic-derivative estimate used in the edge audit is
\(O(L^2/c+L)=O(L^2)\) uniformly on this range. The finite-polynomial bound is also uniform there. Thus \(\|R\|_2\ll\sqrt T L^2\) with an absolute implied constant. Moreover, \(\delta^{-2}=(L/c)^2\leq L^2\), so the unconditional bound (1) gives the same \(a_T\), with an absolute constant. Consequently
\[
\sup_{1\leq c\leq L/4}
\frac{|\|R_c-U_{c,N}\|_2^2-\|R_c\|_2^2|}{TL^2}
\ll a_T.
\tag{2}
\]

At \(N=\lfloor T/L^6\rfloor\),
\[
a_T\ll T^{-1/6}L^3+T^{-1/2}L^2.
\]
If \(b=b(T)\to\infty\) and \(b=o(\log L)\), both widths \(c=b/2\) and \(c=b\) eventually lie in the uniform range. Applying (2) to the coupled statistic
\[
b^2\{2\sinh(b)r_T(b)-2\sinh(2b)r_T(2b)\}
\]
changes it by at most \(O(b^2e^{2b}a_T)=o(1)\). The last limit follows because \(e^{2b}=L^{o(1)}\), whereas \(a_T\) contains a negative power of \(T\). Prime-power removal therefore remains justified at this mesoscopic edge scale. It still supplies no new arithmetic covariance estimate and does not choose an AH convergence rate.

The final author §7 is accepted, including its uniformity on every range \(2\leq b\leq G(T)\) with \(G(T)=o(\log L)\). Its statement that decreasing polynomial coefficients preserve the elementary bound refers to the positive coefficient majorants in that bound; no monotonicity of the exact finite-time polynomial norm is required or claimed. The author's historical draft-status sentence is retained as provenance; the present independent review supplies the current ordinary-proof verdict. This is not a formal machine-checked proof or a numerical gain enclosure.
