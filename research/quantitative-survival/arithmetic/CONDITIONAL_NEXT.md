# Direct Hardy–Littlewood error control for the raw alias packet

> Historical stage note: the singular-series main term left open below has since been evaluated in [MAIN_TERM_THEOREM.md](MAIN_TERM_THEOREM.md), with [independent review](MAIN_TERM_INDEPENDENT_REVIEW.md). The required estimate for the actual prime-pair discrepancy remains unproved. This chapter is retained to document the derivation and the earlier boundary of knowledge.

6 November 2026. Bounded analytical continuation of `REPORT.md`. This note proves an error-transfer bound conditional on an independent, endpoint-aware prime-pair discrepancy estimate confined to the required near shifts. The printed two-sign uniform Conjecture 1.8 has an endpoint defect explained in `ENDPOINT_CORRECTION.md`; it is not assumed literally here. It does **not** evaluate the remaining singular-series main term or claim Hardy–Littlewood implies the exact +1/5 statistic without that calculation.

## 1. Setup and exact change of variables

Use the notation and Fourier convention of `REPORT.md`. More generally let

\[
1<\alpha<2-\beta,\quad 0<\beta<1,
\quad q_\nu(v)=q(\log v/L-\nu),\quad L=\log T,
\]

where \(q\in C_c^\infty((-\eta,\eta))\). Require \(\alpha-\eta>1\), \(\beta>\eta\), and narrow enough packets to preserve the sine-process chambers. Put \(\gamma=\alpha+\beta\); this \(\gamma\) is a frequency parameter, not a zero ordinate. The normalized high prime packet before taking a real part is

\[
P_T=\frac1{L^3}\sum_{m,n,r}
\frac{\Lambda(m)\Lambda(n)\Lambda(r)}{\sqrt{mnr}}
q_\alpha(m)q_\beta(n)q_\gamma(r)
\widehat\Phi\left(\frac{T}{2\pi}\log\frac{mn}{r}\right).
\tag{1}
\]

The raw zero statistic satisfies \(M_T=-\operatorname{Re}P_T/c_\psi+o(1)\). Write \(x=nm\) and \(h=r-nm\). For fixed \(n,h\ne0\), define

\[
A_{n,h}(y)=\sum_{k\le y}\Lambda(k/n)\Lambda(k+h),\qquad
E_{n,h}(y)=A_{n,h}(y)-\frac{\mathfrak S_n(h)}n (y-\max(0,-h))_+,
\tag{2}
\]

where \(\Lambda(k/n)=0\) unless \(n\mid k\), and terms with \(k+h\le0\) are omitted. The endpoint-aware main term retains the positive overlap length. The singular series is the one in Fazzari–Gerspach Conjecture 1.8, \(\mathfrak S_n(h)=\mathbf1_{(n,h)=1}\mathfrak S(nh)\); it is even in \(h\).

Apart from a smooth dyadic cutoff in \(x\), the weight against \(dA_{n,h}(x)\) is exactly

\[
W_{n,h}(x)=\frac{q_\alpha(x/n)q_\gamma(x+h)}{\sqrt{x(x+h)}}
\widehat\Phi\left(\frac{T}{2\pi}\log\frac{x}{x+h}\right).
\tag{3}
\]

In particular, **there is no additional factor \(n\)** in this weight: \(mn=x\), so \(\sqrt{mnr}=\sqrt{x(x+h)}\). The factor \(1/n\) enters only through the Hardy–Littlewood main density in (2).

## 2. The variation estimate and summed error

Localize \(x\asymp X\) smoothly and take \(|h|\le cX\), for a fixed sufficiently small \(c\). For each fixed \(A>0\),

\[
\|W_{n,h}\|_\infty+\int|W'_{n,h}(x)|\,dx
\ll_A X^{-1}(1+T|h|/X)^{-A}.
\tag{4}
\]

To check this, the argument \(u=T\log(x/(x+h))/(2\pi)\) has size comparable to \(T|h|/X\), and \(xu'(x)=O(u)\). The prefactor is \(O(X^{-1})\); its logarithmic derivative and those of the smooth packet cutoffs are \(O(X^{-1})\), with the packet derivatives carrying an additional \(1/L\). Schwartz bounds on \(\widehat\Phi\) and its derivative prove (4), including the derivative of the dyadic cutoff.

Consequently partial summation gives

\[
\left|\int W_{n,h}\,dE_{n,h}\right|
\ll_A \frac{\sup_{y\asymp X}|E_{n,h}(y)|}{X}
(1+T|h|/X)^{-A}.
\tag{5}
\]

Suppose first that the pointwise discrepancy bound is \(E_{n,h}(y)=O_\varepsilon(X^{\theta+\varepsilon})\) uniformly on the needed range. On a dyadic block \(n\asymp N\), using \(\sum_{n\asymp N}\Lambda(n)\ll N\) and
\(\sum_{h\ne0}(1+T|h|/X)^{-A}\ll X/T\) when \(X/T\gg1\), the normalized error in (1) is

\[
\boxed{\quad
O_{\varepsilon,A}\left(\frac{NX^{\theta+\varepsilon}}{TL^3}\right)
\quad}
\tag{6}
\]

per block. The finitely many logarithmic numbers of blocks can be absorbed into \(T^\varepsilon\). In the central exponent notation this gives a power saving whenever

\[
\boxed{\ \beta+\theta(\alpha+\beta)<1.\ }
\tag{7}
\]

For an independently assumed localized square-root discrepancy, \(\theta=1/2\), the domain is

\[
\boxed{\ \alpha+3\beta<2.\ }
\tag{8}
\]

At \((\alpha,\beta)=(1.2,.2)\), the central error exponent is \(-.1+\varepsilon\). Equivalently, a pointwise discrepancy exponent strictly below \(4/7\), with suitable margins, would suffice for the error step. This says nothing yet about the main term.

### Packet widths, diagonals, and tails

The logarithmic packet width must be included. On the relevant near-product support, \(n\le T^{\beta+\eta}\), while \(x+h\le T^{\alpha+\beta+\eta}\) and \(x\asymp x+h\). Thus (6), summed over the blocks, is

\[
O_\varepsilon\left(T^{\beta+\eta+\theta(\alpha+\beta+\eta)-1+\varepsilon}\right).
\tag{9}
\]

For \(\theta=1/2\), this exponent is
\(\alpha/2+3\beta/2+3\eta/2-1+\varepsilon\).
At the current frequencies any \(\eta<.05\) leaves a margin exceeding .025 before choosing \(\varepsilon\). The weaker estimate obtained by ignoring the upper cutoff on \(r\) replaces \(3\eta/2\) by \(2\eta\), and still saves a power for every fixed \(\eta<.05\).

The \(h=0\) term is handled separately. All three nonzero von Mangoldt factors then come from powers of the same prime. The positive lower packet cutoffs give a power-saving bound; for example the number of possible prime bases is at most \(T^{\beta+\eta}\), and the denominator \(mn\) is at least \(T^{\alpha+\beta-\eta}\), leaving \(O(T^{-\alpha+2\eta}\operatorname{polylog}T)\).

The region \(|h|\asymp X\), or non-comparable \(x,x+h\), is negligible by arbitrary decay of \(\widehat\Phi\), against polynomially bounded sums. It is enough to assume the discrepancy estimate for \(0<|h|\le (X/T)T^\kappa\), with a fixed small \(\kappa>0\). Outside this range the kernel argument exceeds a constant times \(T^\kappa\); arbitrary decay controls both the actual prime sum and the singular-series expression. Choose \(\kappa\) small enough that \((X/T)T^\kappa<X^{1/2-\delta}\) for some \(\delta>0\), which is possible here because the maximum \(X\) exponent is below two. Hence the whole required assumption concerns shifts smaller than the square-root scale. The difference between the endpoint-aware main term and the uncorrected \(\mathfrak S_n(h)y/n\) is at most \(\mathfrak S_n(h)|h|/n\), which is absorbed in \(O_\varepsilon(X^{1/2+\varepsilon})\) on this local range. In the integration region \(x\asymp X\gg|h|\), their derivatives are exactly equal, so (12) remains unchanged.

## 3. A weaker, localized averaged discrepancy hypothesis

Pointwise uniform Hardy–Littlewood over all twists and shifts is more than the error proof uses. For dyadic blocks compatible with the packets, the following weighted discrepancy norm suffices:

\[
\mathfrak D_T(A)=\frac1{L^3}\sum_{N,X}\sum_{n\asymp N}
\Lambda(n)|q_\beta(n)|\sum_{h\ne0}
\frac{\sup_{y\asymp X}|E_{n,h}(y)|}{X}
(1+T|h|/X)^{-A}=o(1).
\tag{10}
\]

All terms here are restricted to the comparable near-product region just treated; its complement is independently negligible. Equation (5) proves that (10) is sufficient. It requires control only for prime-power twists in this short packet, shifts concentrated near \(X/T\), and the indicated local ranges of \(y\). It can hold even with exceptional twists or shifts violating a pointwise bound.

An even weaker, signed condition is

\[
\operatorname{Re}\left\{
\frac1{L^3}\sum_n\Lambda(n)q_\beta(n)
\sum_{h\ne0}\int W_{n,h}(x)\,dE_{n,h}(x)
\right\}=o(1).
\tag{11}
\]

This condition permits cancellation between discrepancies and is exactly the error functional needed for the real observable. Equation (10) is a transparent sufficient norm for (11), not an assertion that (11) has been established. Neither condition requires all the uniformity in the original pointwise conjecture.

## 4. The main term that is still unevaluated

Under an error hypothesis above, (1) becomes

\[
P_T=\mathcal S_T+o(1),
\quad
\mathcal S_T=\frac1{L^3}\sum_n\frac{\Lambda(n)q_\beta(n)}n
\sum_{h\ne0}\mathfrak S_n(h)
\int_0^\infty W_{n,h}(x)\,dx.
\tag{12}
\]

The further required conclusion is

\[
\operatorname{Re}\mathcal S_T\longrightarrow-\beta c_\psi
\tag{13}
\]

(or any nonzero limiting or subsequential value sufficient to exclude the specified pair-AH). **This note does not prove (13).** The phase, nonlinear change of variables, prime-power averaging, packet widths, and the surviving arithmetic fluctuations of the singular series must all be retained in evaluating it.

A first-average replacement of the singular series is inadequate: \(\int\widehat\Phi=\Phi(0)=0\), with analogous vanishing for every polynomial moment. Thus a continuous mean-density approximation loses the main signal. A sharp signed singular-series calculation is a separate substantive step, not an error estimate that can be bundled into (6).

Centering the two long prime weights by replacing \(\Lambda(m),\Lambda(r)\) with \(\Lambda(m)-1,\Lambda(r)-1\) is legitimate for the **whole packet** by the nonstationary Poisson argument in `REPORT.md`. The proof above deliberately first applies Hardy–Littlewood to the uncentered prime pair. One must not replace \(\mathfrak S_n(h)\) by a guessed centered version term by term without computing the corresponding background sums.

## Source and interpretation

The independent local square-root discrepancy has the error scale proposed in Conjecture 1.8 in Fazzari–Gerspach, *The third moment of the logarithm of zeta and a twisted pair correlation conjecture*. [Versioned primary paper](https://arxiv.org/abs/2412.20099v1)

Their Theorem 1.9 has a different smoothed observable and the conservative range \(1-\beta\le\alpha\le2-48\beta\). The calculation here does not improve that theorem. It establishes that **for our specific packet, its error-transfer stage alone** allows the broader domain (8), conditional on the consistent localized discrepancy estimate defined here, not on the defective full two-sign formulation as printed. The singular-series asymptotic needed to turn this into a complete conditional theorem remains open in this note.
