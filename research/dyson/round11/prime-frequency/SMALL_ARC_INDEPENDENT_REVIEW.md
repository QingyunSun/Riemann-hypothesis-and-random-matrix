# Independent review of the RH centered-small-arc improvement

Date: 2026-09-05. Reviewer: `yau_flow`, separately from the author `residual_gram`.

**Verdict:** the written proof of
\[
|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{X(X+Q^2)}\log^5X,
\qquad Q=X^{523/1000},
\]
is accepted under RH for the fixed smooth packet and modulus family specified in the author report. The removal of the previous \(\sqrt H\) factor is supported by actual centered-prime input. No lost tail band, undeclared GRH assumption, or omitted mean term was found. The bound remains larger than the required \(X\log X\) covariance scale. This is an ordinary independent proof audit, not formal verification or a claim of novelty.

## 1. Primary source and its exact applicability

I read Lemma 3 and its proof on printed page 3 of Bhowmik–Schlage-Puchta, [Mean representation number of integers as the sum of primes](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/Goldbach4.2.10.pdf), together with the preceding definitions and Lemmas 1–2. The PDF SHA-256 is `6cf48524eb9473cca93c1ce0ea97e00fc7dab7c49a3db4e01a490cc165296607`.

The polynomial is exactly the finite prefix with coefficients \(\Lambda(n)-1\). The centered interval is \([-1/y,1/y]\), and the upper bound is \((x/y)\log^4x\) under RH. The source states \(y\leq x\); the application uses the unproblematic subrange \(1\leq y\leq x\). Its proof includes the two prefix-edge regions, so no unproved endpoint cancellation is being imported. The source's separate discussion of GRH near general rational arcs is not needed here: this proof uses its RH arc around zero, then a local sampling inequality at points within that arc.

## 2. Weighted prefixes, genuine primes, and frequency derivatives

Let \(f\) have fixed compact support in \([c,C]\subset(0,\infty)\). Stieltjes partial summation expresses the weighted \(\Lambda-1\) polynomial as an integral of prefix polynomials with endpoints \(x\in[cX,CX]\), plus any endpoint terms. Minkowski's inequality gives a factor controlled by \(\|f\|_\infty+\int|f'|\). On the needed arcs, \(\rho\geq1/H\), so \(y=1/\rho\leq H=o(X)\), eventually below every prefix endpoint. The source therefore applies uniformly, yielding
\[
\int_{\|\alpha\|\leq\rho}|E_f(\alpha)|^2\,d\alpha
\ll_f X\rho\log^4X.
\tag{1}
\]
Here \(E_f=A_f-B_f\), with \(A_f\) genuinely prime-supported and \(B_f\) the integer polynomial. Replacing the von Mangoldt coefficients by prime coefficients subtracts a finite prime-power polynomial. Its sup norm is \(O_f(\sqrt X\log^2X)\), so its squared integral is \(O_f(X\rho\log^4X)\). This proves (1) for exactly the polynomial used later.

The derivative identity
\[
E_f'(\alpha)=2\pi iX E_{u f(u)}(\alpha)
\]
is exact coefficient by coefficient. Applying (1) with the new fixed weight \(u f(u)\) gives
\[
\int_{\|\alpha\|\leq\rho}|E_f'(\alpha)|^2\,d\alpha
\ll_f X^3\rho\log^4X.
\tag{2}
\]
Thus no estimate has been formally differentiated. The needed seminorms of both \(f\) and \(u f\) are accounted for.

## 3. Local sampling retains the original Farey spacing

All distinct reduced fractions with \(2\leq d\leq Q\) have circular separation at least \(Q^{-2}\). Take disjoint intervals of length, for example, \(Q^{-2}/2\), centered at the selected fractions. For each continuously differentiable \(F\), the fundamental theorem applied to \(|F|^2\) gives at each center
\[
|F(\beta)|^2\leq |I_\beta|^{-1}\int_{I_\beta}|F|^2
+2\int_{I_\beta}|F F'|.
\]
Summing preserves disjointness. If the centers satisfy \(\|\beta\|\leq\rho\), their intervals lie in the enlarged arc of radius \(\rho+Q^{-2}/4\). Because \(\rho\geq1/H\) and \(Q^2\gg H\), this enlargement is at most a constant times \(\rho\). Combining (1)–(2) and Cauchy–Schwarz only in the derivative integral yields
\[
\sum_{\|a/d\|\leq\rho}^{*}|E_f(a/d)|^2
\ll_f X(Q^2+X)\rho\log^4X.
\tag{3}
\]
For a band reaching the whole circle, Parseval for the polynomial and its derivative gives the same bound with \(\rho\asymp1\). This handles wraparound and the final band. The argument neither improves the spacing to \(1/(HQ)\) nor assumes each small interval is a new arithmetic major arc.

## 4. Coefficient bands and their summation

The exact Round 10 completion has coefficients
\[
C_{a/d}=S_v(a/d)M_d,
\quad
M_d=\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q.
\]
The bound \(|M_d|\leq(1+\log(Q/d))/d\) and smooth finite-difference estimate
\(|S_v(\alpha)|\ll_{v,J}H(1+H\|\alpha\|)^{-J}\) do not require Möbius cancellation.

For any denominator \(d\), at most \(2\rho d\) nonzero residues satisfy \(\|a/d\|\leq\rho\); if \(\rho d<1\), there are none. Hence, for the central arc \(j=0\) and the annuli with upper radius \(2^j/H\),
\[
\sum_{\beta\in I_j}|C_\beta|^2
\ll_{v,J}H2^{(1-2J)j}\log^3(2Q).
\tag{4}
\]
This counts every reduced denominator from 2 through \(Q\), including divisors much smaller than the original moduli. There is no inherited cutoff \(d>\sqrt X\). The last clipped annulus obeys the same estimate since its upper radius is only enlarged for this upper bound.

Combining (3)–(4) on each band gives
\[
\left|\sum_{\beta\in I_j}C_\beta E_f(\beta)\right|
\ll_{f,v,J}\sqrt{X(Q^2+X)}\,
2^{(1-J)j}\log^{7/2}X.
\]
The \(H\) factors cancel. The geometric series converges for \(J=2\), independently of the number of bands. Thus no hidden \(\log H\) or discarded high-frequency tail is needed. A \(\log q\) factor in the conductor coefficient contributes one extra logarithm, giving \(\log^{9/2}X\).

## 5. The integer mean and the primitive mean are both present

The decomposition being bounded is exactly
\[
A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)
=E_f(a/d)+B_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0).
\]
The two terms after \(E_f\) must be handled separately.

For smooth compact \(f\), Poisson summation gives
\(|B_f(\alpha)|\ll_{f,A}X(1+X\|\alpha\|)^{-A}\). Since every nonzero fraction has distance at least \(1/Q\) from the integers, and
\(\sum_{a=1}^{d-1}|S_v(a/d)|\ll_v d\), one has
\(\sum_\beta|C_\beta|\ll_v Q\log(2Q)\). The resulting integer-mean error is
\(O_{f,v,A}(XQ\log(2Q)(X/Q)^{-A})\). A fixed sufficiently large \(A\) makes it negligible. The estimate is on the discrete integer mean itself.

For the primitive mean, the same first-power shift bound gives
\[
|A_f(0)|\sum_{d\leq Q}
\frac{|M_d\mu(d)|}{\varphi(d)}
\sum_{(a,d)=1}|S_v(a/d)|
\ll_{f,v}X\log^2(2Q).
\]
This uses Chebyshev and \(\sum_{d\leq Q}1/\varphi(d)\ll\log(2Q)\). It introduces no \(H\) loss and claims no unproved cancellation. The denominator-one term is identically zero in the original completion; it was not discarded during this later decomposition.

## 6. Actual kernel, the two prime-power uses, and scope

The smooth kernel is the exact Round 10 kernel in the variables \(y=m/X\), \(z=h/H\), \(\epsilon=1/T\), and its phase equals
\(\int_0^z(y-\epsilon u)^{-1}du\). The compact support stays away from the denominator singularity. All fixed mixed derivatives, including those after multiplication by \(\log(y-\epsilon z)\), remain uniformly bounded as \(\epsilon\to0\).

In the Fourier separation with fixed outer cutoffs, the constants in (1)–(3) grow polynomially with the m-frequency through the variations of \(f\) and \(u f\). The Poisson bound also costs a fixed number of m-derivatives. Smooth shift bounds cost a fixed number of h-derivatives. Uniform rapid decay of the two-variable Fourier coefficients absorbs all of these costs. The author explicitly includes both m- and h-frequency dependence. The logarithmic identity \(\log((m-h)/q)=\log X-\log q+\log(y-\epsilon z)\) is exact. Rounding the resulting \(\log^{9/2}\) to \(\log^5\) is legitimate.

There are two distinct prime-power steps. The local polynomial replacement proving (1) was checked in Section 2 above. Separately, replacing \(\Lambda\) inside the original progression discrepancy is needed to make every remaining prime a unit modulo every modulus. Its progression error is bounded by the divisor count of \(m-h\); its principal error uses the reciprocal-totient sum. Both are at most the displayed Round 10 error
\[
O_\eta(HX^{1/2+\eta}\log^3X+H\sqrt X\log^4X).
\]
For \(\eta=1/100\) and \(H\leq X^{2/7}\), this is \(o(X\log X)\) and below the new bound. It is not the same operation as the local prime-power replacement, and neither step is omitted.

The accepted statement is restricted to the fixed smooth packet \(V\in C_c^\infty(1,2)\), the actual stated kernel, and the chosen squarefree family. It is conditional on RH. At \(Q=X^{.523}\), it leaves \(X^{.023}\log^4X\) after covariance normalization. No bound for the entire sharp packet, complementary divisor piece, or desired conjecture follows from this audit.

## 7. Evidence and final version

The final author artifact is **CENTERED_SMALL_ARC_BOUND.md**, SHA-256 `9ebf2d8daaac37702302f5a798611e6a6152e352e5b7dd680c319ba76b3f6e29`. The full mathematical draft and primary source were read; the final status paragraph and its link to this review were checked after the author froze the mathematical text. No numerical experiment was necessary, and the author's finite exact-check script was not independently rerun. The acceptance concerns the ordinary analytical proof and its stated scope, not the status of any unreviewed later revision.
