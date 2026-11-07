# Arithmetic audit of the half-grid triple probe

> Historical stage note: the singular-series main term left open below has since been evaluated in [MAIN_TERM_THEOREM.md](MAIN_TERM_THEOREM.md), with [independent review](MAIN_TERM_INDEPENDENT_REVIEW.md). The required estimate for the actual prime-pair discrepancy remains unproved. This chapter is retained to document the derivation and the earlier boundary of knowledge.

6 November 2026. Research derivations and primary-source audit; integrated into this checkpoint after independent review.

PR #5 remains at `3b7687eb4a6be68c9093d997c473ebcf1331947e` (`feat/windowed-zeta-triples`), verified through GitHub during this audit. The [pinned statistic](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/3b7687eb4a6be68c9093d997c473ebcf1331947e/research/experiments/windowed-triples/statistic.py) uses the distinct ordered triples

\[
a=(1.2,0.2,-1.4),\qquad b=(-0.8,0.2,0.6).
\]

The full empirical experiment was not rerun. This note derives an alternative observable, closes a conditional uniform-integrability issue, and identifies a specific arithmetic estimate still missing. It does **not** prove a nonzero limiting zeta statistic or refute the Alternative Hypothesis.

## 1. A cleaner raw triple observable

Let \(e(x)=e^{2\pi ix}\). For arbitrary real locations and product weights, the difference of the two phases is

\[
e(a\cdot(x_i,x_j,x_k))-e(b\cdot(x_i,x_j,x_k))
=e(b\cdot(x_i,x_j,x_k))[e(2(x_i-x_k))-1].
\]

Consequently the difference vanishes term by term on every translate of \(\tfrac12\mathbb Z\), including arbitrary thinning and multiplicities. **Distinctness of the indices is unnecessary.** The raw product is therefore an equally valid half-grid detector and avoids estimating the high-frequency pair terms introduced by distinct-index subtraction.

For a precise Fourier-localized version, choose a nonzero, nonnegative, real even Schwartz function \(\psi\) with \(q=\widehat\psi\in C_c^\infty((-\eta,\eta))\), where \(0<\eta<0.05\). Such functions exist: square a real even Schwartz function with sufficiently narrow smooth compact Fourier support. Put

\[
c_\psi=\int_\mathbb R\psi(x)^3\,dx>0,\qquad
Z_\alpha(t)=\sum_\gamma\psi\left(\frac{L(\gamma-t)}{2\pi}\right)
e\left(\alpha\frac{L(\gamma-t)}{2\pi}\right),\quad L=\log T.
\]

Here RH is assumed, zeros are counted with multiplicity, and the sum includes all nontrivial ordinates. Let \(\Phi\ge0\) be smooth, supported inside \((1,2)\), with integral one. Define

\[
M_T=\frac1{Tc_\psi}\int\Phi(t/T)\operatorname{Re}
\{Z_{1.2}Z_{0.2}\overline{Z_{1.4}}
-\overline{Z_{0.8}}Z_{0.2}Z_{0.6}\}\,dt.
\tag{1}
\]

This is a proposed mathematical variant, **not** a relabeling of the recorded Hann/distinct-index measurements.

### Its sine-process expectation is exactly +1/5

Away from the three zero-coordinate axes, the full third moment of the unit-density sine process has spectral density

\[
C_3(\xi)=1-\sum_{j=1}^3(1-|\xi_j|)_+
+2\left(1-\sum_j\xi_j^+\right)_+,
\qquad \sum_j\xi_j=0.
\tag{2}
\]

This follows by expanding the determinantal three-point density and adding the coincidence partitions; away from the axes it also equals the third cumulant density. In the entire support packet around \(a\), (2) is \(\xi_2\). In the packet around \(b\), it is zero. The packets miss all coordinate axes. Writing \(\xi=a+u\), integration against \(\prod_jq(u_j)\delta(\sum u_j)\) gives

\[
\int \xi_2\prod_jq(u_j)\delta(\sum u_j)\,du
=0.2\,c_\psi:
\]

the term containing \(u_2\) is odd under simultaneous sign reversal. Thus the normalized expected raw difference is exactly **+0.2 for this fixed envelope**, rather than merely an infinite-window limit. The distinct-index sine limit is a different number, −0.4.

The same construction works for
\[
(\alpha,\beta,-\alpha-\beta),\quad
(\alpha-2,\beta,2-\alpha-\beta),\qquad
0<\beta<1,\quad1<\alpha<2-\beta,
\]
with packets narrow enough to stay in the indicated chambers. Its raw sine expectation is \(\beta\). Shrinking \(\beta\) gives a shorter prime variable, at the price of a smaller signal.

## 2. Occupancy and the precise meaning of pair-AH

### Fixed-window moments are already bounded under RH

For fixed \(W,k\), set
\[
K_W(t)=\#\{\gamma:|L(\gamma-t)/(2\pi)|\le W\}.
\]
Then
\[
\frac1T\int_T^{2T}K_W(t)^k\,dt=O_{W,k}(1).
\tag{3}
\]

Here is a direct corollary argument, including the required support check. Choose \(\varphi\ge0\), Schwartz and bandlimited to \((-\delta,\delta)\), with \(\varphi\ge1\) on \([-2W-1,2W+1]\) and \(k\delta<2\). For \(1\le r\le k\), put
\[
F_r(x)=\int_\mathbb R\prod_{j=1}^r\varphi(x_j-u)\,du.
\]
It is symmetric, translation invariant, and Schwartz transverse to the diagonal. Its Fourier measure is supported on \(\sum\xi_j=0\), with \(|\xi_j|<\delta\), hence \(\sum|\xi_j|<2\). Also \(F_r\ge1\) whenever the configuration has diameter at most \(2W\): integrate over an interval of length one near any one of the points.

The restricted correlation theorem gives an \(O(TL)\) bound for the distinct-index sum of \(F_r(L\gamma_1/(2\pi),\ldots)\) with all ordinates in \([T/2,3T]\). In the expansion of the integral of \(K_W^k\), group repeated indices by their partitions into \(r\) distinct indices. Any tuple that can lie in one window has diameter at most \(2W\), and the set of eligible centers has length at most \(4\pi W/L\). Multiply these two bounds and sum the finitely many partitions to obtain (3).

The exact primary input is Rudnick–Sarnak, *The n-level correlations of zeros of the zeta function*, Theorem 1.1, pp.1029–1030; immediately after that theorem the authors explicitly allow an interval characteristic cutoff under RH. Their test conditions TF1–TF3 and strict Fourier support \(\sum|\xi_j|<2\) are precisely the conditions checked above. This argument uses the height-localized theorem with \(L=\log T\), not an unexamined interchange with the index normalization. [Original paper](https://www.math.tau.ac.il/~rudnick/papers/RudnickSarnakCRAS1994.pdf)

Thus the earlier PR audit's occupancy caveat can be sharpened: **under RH, uniform integrability for fixed compact-window cubic scores is a known-theorem consequence, not an additional conjecture.** This does not make an empirical deletion test a proof; it supplies a separate analytic bound.

### Full pair concentration suffices; protected-band matching does not

Let \(R\) denote the unnormalized raw or distinct phase difference in a compact window, with absolute weights at most one. Let \(B_\eta\) be the number of ordered pairs in that window whose displacement has distance greater than \(\eta\) from \(\tfrac12\mathbb Z\). The phase factorization gives
\[
|R|\le4\pi\eta K^3+2KB_\eta.
\]
If \(\mathbb E K^j\le C_j\), split at \(K\le M\), using the crude \(|R|\le2K^3\) on the tail. Then
\[
\mathbb E|R|\le4\pi\eta C_3+2M\mathbb E B_\eta+\frac{2C_4}{M}
\le4\pi\eta C_3+4\sqrt{C_4\mathbb E B_\eta}.
\tag{4}
\]
The last display chooses \(M=\sqrt{C_4/\mathbb E B_\eta}\); the zero case follows by a limit. Divide by the positive normalization for the normalized score.

Therefore a **full local pair-displacement hypothesis** asserting \(\mathbb E B_\eta\to0\) for every fixed window and every fixed \(\eta>0\) implies that these cubic means tend to zero: first let \(T\to\infty\), then \(\eta\downarrow0\). The same conclusion follows from convergence of the full local pair measures to a measure supported on the half-grid, using nonnegative off-lattice majorants. Distinct labels at the same zero cause no problem. No coupling of entire configurations, or separate three-point AH, is needed.

This implication does **not** follow just from agreement with pair tests whose Fourier support lies in the Montgomery range. Those tests do not establish vanishing off-lattice pair mass. The formulation of “AH” must say which assertion is assumed.

The conclusion extends to the Schwartz envelope in (1). Partition the unfolded line into unit cells, apply (3) uniformly to shifted centers whose heights stay in \([T/2,3T]\), and use Minkowski's inequality to bound the fourth norm of the tail by a constant times \(\sum_{|j|>A}\sup_{[j,j+1]}|\psi|\). This tends to zero. Cells farther than a constant times \(T\log T\) are handled by the elementary local zero-count bound \(O(\log(2+T+|j|))\) and arbitrarily rapid decay of \(\psi\). Hölder bounds the difference of the cubic products after truncation. Thus full pair-AH plus RH implies \(M_T\to0\).

## 3. Exact reduction to a signed near-product prime correlation

Use \(\widehat\Phi(y)=\int\Phi(u)e^{-2\pi iyu}\,du\), and write
\[
q_\alpha(n)=q(\log n/L-\alpha).
\]
The explicit formula, for positive \(\alpha>\eta\), gives uniformly on the support of the height average
\[
Z_\alpha(t)=-\frac1L\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
q_\alpha(n)n^{-it}+O_B(T^{-B})
\tag{5}
\]
for every fixed \(B\). All sums are finite, supported on \(T^{\alpha-\eta}<n<T^{\alpha+\eta}\). The gamma-density contribution has no surviving Taylor moments because the Fourier packet misses zero; smoothness and Schwartz decay control its remainder. The explicit pole terms are also rapidly small, using the compact Fourier support and the large real displacement of their arguments. Negative-frequency values are complex conjugates.

The low packet \((-.8,.2,.6)\) contributes \(o(1)\). One can see this directly: the product of the two positive prime variables is at most \(T^{.8+2\eta}<T\), so unequal integer products are killed by arbitrary decay of \(\widehat\Phi\). Exact equality forces all three nonzero von Mangoldt factors to be powers of the same prime; since every variable has a positive power-of-\(T\) lower cutoff, the weighted diagonal tends to zero. This also agrees with the restricted-correlation theorem.

Consequently (1) is
\[
M_T=-\frac1{c_\psi L^3}\operatorname{Re}\sum_{m,n,r\ge1}
\frac{\Lambda(m)\Lambda(n)\Lambda(r)}{\sqrt{mnr}}
q_{1.2}(m)q_{.2}(n)q_{1.4}(r)
\widehat\Phi\!\left(\frac{T}{2\pi}\log\frac{mn}{r}\right)+o(1).
\tag{6}
\]

This identifies an exact asymptotic target. The central scales are
\[
m\asymp T^{1.2},\quad n\asymp T^{.2},\quad r\asymp T^{1.4},
\quad |r-mn|\asymp T^{.4},
\]
with the stated small exponent-width packets, rather than literal fixed-factor dyadic windows. The final relation describes the kernel's natural scale; its rapidly decaying tails remain in (6).

There is a useful centering improvement. For any fixed \(\alpha-\eta>1\),
\[
\sum_{n\ge1}n^{-1/2}q_\alpha(n)n^{-it}=O_B(T^{-B})
\]
uniformly for \(t\) comparable to \(T\). Poisson summation has no stationary integer frequency because \(n\gg T\); repeated integration by parts controls the zero Fourier mode as well. Therefore in (6) **both** long prime factors can be replaced by \(\Lambda-1\), leaving the same main term:
\[
\boxed{\quad
M_T=-\frac{\operatorname{Re}\mathcal C_T}{c_\psi L^3}+o(1),\quad
\mathcal C_T=\sum_{m,n,r}
\frac{(\Lambda(m)-1)\Lambda(n)(\Lambda(r)-1)}{\sqrt{mnr}}
q_{1.2}(m)q_{.2}(n)q_{1.4}(r)
\widehat\Phi\!\left(\frac{T}{2\pi}\log\frac{mn}{r}\right).
\quad}
\tag{7}
\]

The sine prediction is \(\operatorname{Re}\mathcal C_T/L^3\to-c_\psi/5\). Proving merely that the left side does not tend to zero would already contradict full pair-AH, conditional on RH. No such estimate is proved here.

**A first-moment prime-density approximation is insufficient.** Because \(\Phi\) is supported away from zero, \(\int\widehat\Phi=\Phi(0)=0\), and all polynomial moments of this kernel vanish. Replacing the long prime factors by their mean density erases the signal. A positive prime count in a short interval, without the necessary signed covariance, does not evaluate (7).

## 4. Which existing theorems actually reach this target?

### Restricted n-level correlations

For balanced three frequencies, \(\sum|\xi_j|<2\) is equivalent to total positive frequency less than one. The low packet lies inside; the high packet has total positive frequency 1.4 and lies outside. Any balanced triple beyond that boundary has at least one coordinate of absolute value greater than one, which explains why distinct-index subtraction imports unknown high-frequency pair terms. Formula (1) removes those pair subtractions, but does not remove the genuine support obstruction.

The compact physical Hann taper in PR #5 has unbounded Fourier support. It cannot be inserted unchanged into the restricted theorem at fixed width. The Fourier-compact envelope above is a separate observable deliberately chosen to make support statements exact.

### Fazzari–Gerspach: the closest matching arithmetic theorem

The primary paper is Alessandro Fazzari and Maxim Gerspach, *The third moment of the logarithm of zeta and a twisted pair correlation conjecture*, arXiv:2412.20099v1, submitted 28 December 2024. [Versioned primary source](https://arxiv.org/abs/2412.20099v1)

Its Proposition 1.7, assuming RH, treats a prime-power twist \(n\le T^{1-\varepsilon}\). With \(\beta=\log n/\log T\) and \(\delta_T=10\log\log T/\log T\), the range, including symmetry, is
\[
-1+\delta_T<\alpha<1-\beta-\delta_T.
\]
Thus \(\alpha=1.2,\beta=.2\) is excluded. Theorem 1.9 is stated under RH **and** their uniform Hardy–Littlewood Conjecture 1.8, and gives the displayed range
\[
1-\beta\le\alpha\le2-48\beta.
\]
At \(\beta=.2\) this interval is empty. At \(\beta=.01,\alpha=1.2\), it is nonempty and includes the corresponding alias probe, whose sine signal is .01.

The printed additional conjecture asks, uniformly for \(1\le h,n\le x^{1-\varepsilon}\),
\[
\sum_{m\le x}\Lambda(m/n)\Lambda(m\pm h)
=\mathfrak S_n(h)x/n+O_\varepsilon(x^{1/2+\varepsilon}),
\]
with zero contribution unless \(n\mid m\). **Endpoint correction:** as literally printed with both signs, this common \(x\) main term cannot hold throughout the stated uniform range: already at \(n=1\), the minus sum equals the plus sum with upper endpoint \(x-h\). See `ENDPOINT_CORRECTION.md` for the exact check. Our continuation therefore uses an independent, endpoint-aware discrepancy assumption restricted to the much smaller near-product shifts, not the full printed assertion. This audit does not establish the paper's theorem under a repaired global assumption. The theorem uses a particular smoothed Cauchy pair kernel and a height cutoff with derivatives controlled by powers of \(U=(\log T)^B\); transporting it to arbitrary packets is additional work. Its third-logarithm-moment theorem assumes triple and twisted-pair conjectures, so cannot be used to prove those assumptions.

The structural relevance is direct: after holding the short prime variable fixed, (7) asks about primes \(m\) and \(nm+h\), with a signed smooth shift average. The paper supplies a concrete conditional template, with the endpoint convention requiring repair. It does not provide an RH-only evaluation of our packet.

### Twisted moments do not automatically supply von Mangoldt correlations

Bettin–Chandee–Radziwiłł prove a mean-square formula for \(|\zeta|^2\) times a squared arbitrary Dirichlet polynomial of length below \(T^{1/2+1/66}\), with the coefficient and smoothness conditions in their theorem. That is not a formula for (7). [Primary paper](https://arxiv.org/abs/1411.7764)

Bettin–Bui–Li–Radziwiłł treat the twisted fourth moment with polynomial length below \(T^{1/4}\). Their associated quadratic divisor theorem averages \(am_1m_2-bn_1n_2=h\) smoothly in the long variables and allows arbitrary weights in the short variables \(a,b\). The long von Mangoldt weights in (7) do not meet those hypotheses. Differentiating zeta moments produces derivatives in the numerator, whereas the explicit formula concerns logarithmic derivatives; introducing reciprocal zeta factors requires a new ratios/mollification estimate. [Primary paper](https://arxiv.org/abs/1609.02539)

Unrestricted zeta correlations derived by Conrey–Snaith use the ratios conjecture as input. They are predictions for this purpose, not an available unconditional or RH-only bridge. [Primary paper](https://arxiv.org/abs/0803.2795)

## 5. Concrete next slice and limitations

The useful reduction is now:

1. Under RH, restricted correlations already control all fixed local count moments.
2. Actual off-half-grid pair-mass concentration forces the alias score to vanish; equation (4) makes this quantitative.
3. A raw packet eliminates separate high-frequency pair corrections and has exact sine expectation +1/5.
4. Its zeta mean is equivalent to the explicit signed centered prime sum (7).

The next tractable mathematical task is to adapt the Fazzari–Gerspach smoothed calculation to a narrow small-\(\beta\) packet, keeping a consistent localized Hardy–Littlewood assumption explicit, and identify the weakest **averaged signed** replacement for that assumption actually used. This could yield an honest conditional implication and a sharply stated new analytic target. It would not by itself be an RH-only refutation of AH.

Postpone a claim that general twisted-moment technology already proves the needed estimate; an unrestricted-conjecture conclusion; and a new empirical run advertised as closing the arithmetic gap. The sources inspected here do not provide a theorem evaluating (7) under RH alone. This is a bounded primary-source audit, not a claim that every possible recent paper has been ruled out.
