# Evaluating the signed singular-series main term

6 November 2026. Research derivation, with known inputs identified. This completes the main-term calculation left open in the preceding checkpoint. It gives a conditional theorem and a weaker sufficient signed inequality; it does not establish the required prime-pair discrepancy estimate.

## 1. Statement and status

Set \(L=\log T\), \(\gamma=\alpha+\beta\), and choose fixed parameters and packet width with

\[
\beta>\eta>0,\qquad \alpha-\eta>1,\qquad \gamma+\eta<2.
\tag{1}
\]

Take a real, even Schwartz envelope \(\psi\) whose Fourier transform \(q\) is smooth and supported in \((-\eta,\eta)\), with \(c_\psi=\int\psi^3>0\). The previous nonnegative construction is allowed. Let \(\Phi\ge0\) be smooth, supported in \((1,2)\), and normalized by \(\int\Phi=1\). Fourier transforms use \(e^{-2\pi ixy}\). Write

\[
Z_\nu(t)=\sum_{\rho=1/2+i\gamma_j}\psi\left(\frac{L(\gamma_j-t)}{2\pi}\right)
e\left(\nu\frac{L(\gamma_j-t)}{2\pi}\right).
\]

Assume RH, and count all zero ordinates with multiplicity. Define the **raw** alias mean

\[
M_T=\frac1{Tc_\psi}\int\Phi(t/T)\operatorname{Re}
\left[Z_\alpha Z_\beta\overline{Z_\gamma}
-\overline{Z_{2-\alpha}}Z_\beta Z_{2-\gamma}\right]dt.
\tag{2}
\]

This is not the recorded distinct-index Hann statistic. It has the same pointwise half-grid cancellation, and its sine-process expectation is exactly \(\beta\).

**Derived arithmetic identity.** For the signed discrepancy functional \(\mathcal R_T\) defined below,

\[
\boxed{\quad M_T=\beta-\frac{\operatorname{Re}\mathcal R_T}{c_\psi}+o(1).\quad}
\tag{3}
\]

The proof uses a known singular-series average of Fazzari–Gerspach, not their defective full two-sign prime-pair conjecture. Formula (3) itself does not assume a conjectural bound on \(\mathcal R_T\).

Consequences:

- If \(\operatorname{Re}\mathcal R_T=o(1)\), then \(M_T\to\beta\). This is a completed **conditional packet theorem**.
- More weakly, if \(\limsup\operatorname{Re}\mathcal R_T<\beta c_\psi\), then \(\liminf M_T>0\). This already contradicts the full off-half-grid pair-mass concentration hypothesis described in the earlier checkpoint, under RH.
- Even \(\liminf\operatorname{Re}\mathcal R_T<\beta c_\psi\) gives a positive subsequential mean, also incompatible with that pair-AH implication \(M_T\to0\).

Under RH, bounded fixed-window count moments and the Schwartz-tail argument also give \(M_T=O_{\alpha,\beta,\psi,\Phi}(1)\). Formula (3) therefore already implies \(\operatorname{Re}\mathcal R_T=O_{\alpha,\beta,\psi,\Phi}(1)\), without a prime-pair discrepancy conjecture. Full pair-AH would require the specific cancellation \(\operatorname{Re}\mathcal R_T\to\beta c_\psi\). The open task is to beat or exclude that positive threshold; arbitrary smallness is a sufficient but unnecessarily strong objective.

No threshold-beating bound on \(\mathcal R_T\) is proved here. The contribution is an explicit packet calculation and reduction using known arithmetic input. It is not a new general Hardy–Littlewood-to-GUE principle and carries no claim of having solved a famous conjecture.

## 2. Exact arithmetic decomposition and endpoint convention

Abbreviate \(q_\nu(v)=q(\log v/L-\nu)\). For a signed nonzero integer shift \(h\), set

\[
A_{n,h}(y)=\sum_{k\le y}\Lambda(k/n)\Lambda(k+h),\qquad
E_{n,h}(y)=A_{n,h}(y)-\frac{\mathfrak S_n(h)}n(y-\max(0,-h))_+.
\tag{4}
\]

Here \(\Lambda(k/n)=0\) unless \(n\mid k\), and \(\Lambda\) vanishes away from positive prime powers. For \(n=p^a\),

\[
\mathfrak S_n(h)=\mathbf1_{(n,h)=1}\mathfrak S(nh),
\]

where \(\mathfrak S\) is the usual prime-pair singular series, even in its argument. Use

\[
W_{n,h}(x)=\frac{q_\alpha(x/n)q_\gamma(x+h)}{\sqrt{x(x+h)}}
\widehat\Phi\left(\frac{T}{2\pi}\log\frac{x}{x+h}\right)
\tag{5}
\]

on \(x>0,x+h>0\), and zero elsewhere. The smooth cutoffs make each integral compactly supported away from its singular endpoints. Define

\[
\mathcal R_T=\frac1{L^3}\sum_n\Lambda(n)q_\beta(n)
\sum_{h\ne0}\int W_{n,h}(x)\,dE_{n,h}(x),
\tag{6}
\]

and

\[
\mathcal S_T=\frac1{L^3}\sum_n\frac{\Lambda(n)q_\beta(n)}n
\sum_{h\ne0}\mathfrak S_n(h)\int W_{n,h}(x)\,dx.
\tag{7}
\]

The factor \(1/n\) belongs in (7), **not** in (6). It is already present in the discrepancy's subtracted density.

The explicit formula and the substitution \(x=nm, h=r-nm\), established in the preceding checkpoint, give

\[
M_T=-\operatorname{Re}(\mathcal S_T+\mathcal R_T)/c_\psi+o(1).
\tag{8}
\]

The equal-product \(h=0\) term is negligible: all three von Mangoldt factors then arise from powers of a common prime. In the low-frequency raw term, the matched single variable is at most \(T^{2-\alpha+\eta}<T\), with a fixed margin. Near-comparable products are therefore also shorter than \(T\), so unequal integers are suppressed by the height Fourier kernel; non-comparable products have a kernel argument of order \(T\) and are negligible by Schwartz decay. This does not require the entire independently truncated product to be shorter than \(T\). No repeated-zero subtraction is needed.

The overlap-length convention in (4) is consistent for both signs. On the support of (5), the derivative of the subtracted continuous main term is exactly \(\mathfrak S_n(h)/n\). The endpoint error in the original printed global Conjecture 1.8 is therefore not imported into this calculation.

## 3. The known singular-series input

For \(n=p^a\), define \(B_n(y)=\sum_{1\le h\le y}\mathfrak S_n(h)\). Fazzari–Gerspach, Lemma 2.7, equation (2.29), gives, **uniformly in \(y\) and the prime power \(n\)**,

\[
B_n(y)-y=-\frac12\min\{\log p,\log y\}
+O((\log y)^{2/3}).
\tag{9}
\]

We use the harmless bounded extension \(\log^+y\) and error \(O(1+(\log(2+y))^{2/3})\) near zero. This is a singular-series lemma, separate from the prime-pair conjecture; it is stated without an RH assumption. Its proof cites Friedlander–Goldston's singular-series average. [Primary paper, printed pages 17–18](https://arxiv.org/pdf/2412.20099v1#page=17)

One immediate uniform consequence is \(B_n(y)\ll y\) for \(y\ge1\). We use both the signed secondary term and this positive upper bound.

### A smoothed consequence with all constants fixed

Let

\[
K(u)=\operatorname{Re}\widehat\Phi(u/(2\pi))
=\int\Phi(t)\cos(tu)\,dt.
\]

Then \(K\) is real, even, Schwartz, \(K(0)=1\), and

\[
\int_\mathbb R K(u)\,du=2\pi\Phi(0)=0.
\tag{10}
\]

For \(H\ge p\), we claim

\[
\boxed{\quad
\sum_{h\ne0}\mathfrak S_n(h)K(h/H)
=-\log p+O_\Phi\left(1+(\log(2+H))^{2/3}+(p/H)^2\right).
\quad}
\tag{11}
\]

Proof: the two signs give twice the positive sum. Integrate \(K(y/H)\) against \(dB_n(y)\), use (9), and integrate by parts. The density term is zero by (10), and the remaining main integral is

\[
\int_0^\infty\min\{\log p,\log^+(Hu)\}K'(u)\,du.
\tag{12}
\]

Replacing the minimum by \(\log p\) gives \(-\log p\). The replacement is supported on \(u<p/H\). Since \(K'(0)=0\) and \(|K'(u)|\ll u\) there, the error is bounded by

\[
O\left(\frac{\log p}{H^2}
+\int_0^{p/H}u\log\frac{p}{Hu}\,du\right)
=O((p/H)^2).
\]

The error in (9), integrated against \(|K'|\), is \(O(1+(\log(2+H))^{2/3})\). These estimates prove (11). In particular the coefficient is **−1 times \(\log p\)**: the factor one-half in (9) is canceled by the two signs of \(h\).

## 4. Replacing the nonlinear kernel

Write \(H=x/T\). In the comparable region \(|h|\le x/2\), ordinary differentiation and Schwartz bounds give, for any fixed sufficiently large \(A\),

\[
\left|W_{n,h}(x)-\frac{q_\alpha(x/n)q_\gamma(x)}x
\widehat\Phi\left(-\frac{h}{2\pi H}\right)\right|
\ll_A\frac{|h|}{x^2}(1+|h|/H)^{-A}.
\tag{13}
\]

Indeed the logarithmic phase error is \(O(T(h/x)^2)\); the envelope and reciprocal-square-root changes are \(O(|h|/x)\) relative to \(x^{-1}\). Extra powers of \(|h|/H\) are absorbed by increasing the Schwartz decay order.

From \(B_n(y)\ll y\) and partial summation,

\[
\sum_{h\ne0}\mathfrak S_n(h)|h|(1+|h|/H)^{-A}\ll H^2.
\]

Thus summing the error in (13) over shifts gives \(O(T^{-2})\) for each \(x\), uniformly in \(n\). Since the pertinent range has \(x\ll T^{\gamma+\eta}\), the total error in (7) is

\[
O(T^{\gamma+\eta-2}/L^2)=o(1).
\tag{14}
\]

Here \(\sum\Lambda(n)|q_\beta(n)|/n\ll L\). The non-comparable and large-shift tails are smaller than any power of \(T\): the Fourier-kernel argument is then of order \(T\), while the finite packet sums and singular series have polynomial bounds.

The leading linearized sum is real, since opposite shifts are conjugates. Also

\[
\frac Hp=\frac{x/n}{T}\frac np\ge T^{\alpha-\eta-1}
\]

whenever its envelope is nonzero. Thus (11) applies uniformly, and the \((p/H)^2\) error saves a power. Inserting it into (7) yields

\[
\operatorname{Re}\mathcal S_T
=-\frac1{L^3}\sum_n\frac{\Lambda(n)^2q_\beta(n)}n
\int q_\alpha(x/n)q_\gamma(x)\frac{dx}x
+O(L^{-1/3})+o(1).
\tag{15}
\]

The \(O(L^{-1/3})\) comes from a uniform \(O(L^{2/3})\) shift error, an \(O(L)\) weighted twist sum, and an \(O(L)\) logarithmic integral, divided by \(L^3\).

## 5. Prime averaging and the exact packet convolution

Set

\[
J(v)=\int_\mathbb R q(u-\alpha)q(u+v-\gamma)\,du.
\]

Changing variables \(u=\log(x/n)/L\) in (15) makes its main term

\[
-\frac1{L^2}\sum_n\frac{\Lambda(n)^2}{n}
q(\log n/L-\beta)J(\log n/L).
\tag{16}
\]

Higher prime powers contribute \(o(1)\), because their reciprocal weighted tail above \(T^{\beta-\eta}\) is \(O(T^{-(\beta-\eta)/2}\operatorname{polylog}T)\). Partial summation with the prime number theorem gives, for a fixed smooth compactly supported \(F\) away from zero,

\[
\frac1{L^2}\sum_p\frac{(\log p)^2}{p}F(\log p/L)
\longrightarrow\int vF(v)\,dv.
\tag{17}
\]

Therefore the limit of (16) is

\[
-\iint v\,q(v-\beta)q(u-\alpha)q(u+v-\gamma)\,du\,dv.
\]

Put \(a=u-\alpha,b=v-\beta\). Since \(\gamma=\alpha+\beta\), this becomes

\[
-\iint(\beta+b)q(a)q(b)q(a+b)\,da\,db.
\]

The term containing \(b\) is odd under \((a,b)\mapsto(-a,-b)\). The remaining convolution equals
\(\beta\int\psi^3=\beta c_\psi\). Hence

\[
\boxed{\quad\operatorname{Re}\mathcal S_T\longrightarrow-\beta c_\psi.\quad}
\tag{18}
\]

Equations (8) and (18) prove (3). The sign reverses once when passing from the prime packet to the zero statistic, so the predicted zero mean is **+\(\beta\)**.

## 6. A sufficient local discrepancy hypothesis

The previous checkpoint proves that an endpoint-aware estimate
\(E_{n,h}(y)=O_\varepsilon(X^{1/2+\varepsilon})\), uniformly only on the packet-compatible blocks \(n\asymp N,y\asymp X\) and near shifts \(|h|\le(X/T)T^\kappa\), implies \(\mathcal R_T=o(1)\) if

\[
\alpha+3\beta+3\eta<2.
\tag{19}
\]

The resulting error exponent is \(\alpha/2+3\beta/2+3\eta/2-1+\varepsilon\). Conditions (1) and (19) hold for \(\alpha=1.2,\beta=.2\) and every \(0<\eta<.05\). Thus a precise endpoint-consistent localized Hardy–Littlewood assumption now gives the **complete** conclusion \(M_T\to1/5\), rather than merely control of an unevaluated main term.

The averaged absolute discrepancy norm from the earlier checkpoint also suffices. The threshold in Section 1 is weaker still: one only needs an upper bound below \(\beta c_\psi\) for the real signed error, not its full asymptotic vanishing.

These hypotheses remain unproved for the actual primes. The next arithmetic task is therefore to bound that signed error functional; the singular-series main term is no longer an outstanding step.

## 7. Verification and failed approaches

`check_normalizations.py` and `normalizations.json` contain reproducible floating-point diagnostics for the signed shift sum and the two-dimensional packet normalization. They are not interval certificates and do not test the unproved prime-pair discrepancy premise.

A naive Ramanujan expansion produces two separately logarithmically divergent pieces. The special prime's Euler factor must remain coupled to the rest of the expansion. Lemma 2.7 avoids that rearrangement entirely. Likewise, direct truncation of the full numerical shift sum leaves a large oscillatory mean-density tail. The stable diagnostic subtracts density one and restores its exactly known contribution using Poisson summation. These are computational or summation-order issues, not counterexamples to (11).

The known singular-series lemma is credited to its source. The new work here is its precise application to this raw alias packet, the nonlinear-to-linear kernel control, the complete normalization, and the explicit one-sided discrepancy target. Ordinary derivations and independent review are not formal verification.
