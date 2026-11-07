# A common sieve sequence at the cancellation threshold

The explicit formula turns one test of zeta zeros into a question about primes. If the zero spacings concentrate on multiples of half the mean spacing, a signed error in counts of prime pairs must approach a particular positive value. Can the fact that every pair count uses the same primes exclude this value?

We construct a single nonnegative weight sequence at each height that attains the required value. It retains the true von Mangoldt weights for the twist and satisfies a growing small-prime sieve at both endpoints of each pair. Its pair count at shift two has a discrepancy much larger than the critical size. Conversely, the separately assigned rows in the previous study attained the same limit while satisfying a critical-size bound. Whether both constraints together control the signed error remains open, as does the bound for the true von Mangoldt sequence. [Previous construction](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/f28ca3e9376f45336100295fa130cb75e6a5b415/research/quantitative-survival/arithmetic/SURROGATE_SHARPNESS.md)

## The construction

Use the conventions and real part of the discrepancy in [the packet calculation](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/f28ca3e9376f45336100295fa130cb75e6a5b415/research/quantitative-survival/arithmetic/MAIN_TERM_THEOREM.md). Fix \(\alpha=1.2,\ \beta=.2,\ \gamma=\alpha+\beta,\ 0<\eta<.05\). The bands for the twist, left endpoint, and right endpoint are disjoint. Fix \(0<\kappa<\gamma-\eta-1\). Choose \(z\) a sufficiently small fixed positive multiple of \(\log T\) so \(Q=\prod_{p\le z}p\le T^\kappa\) for large \(T\). Define one nonnegative sequence \(b_T\) by assigning \(b_T(n)=\Lambda(n)\) throughout the twist band \(T^{\beta-\eta}\le n\le T^{\beta+\eta}\). At all other positive integers put
\[
\omega(k)=D\mathbf1_{(k,Q)=1},\qquad D=Q/\varphi(Q)\ll\log(2z),\qquad b_T(k)=\omega(k).
\]
The wheel has exactly mean one over each period. At every active site \(x=nm,\ r=x+h\), the row mass is the product \(b_T(m)b_T(r)\). Both endpoints avoid all primes up to \(z\) whenever this mass is positive. The factors at the two endpoints are bounded by \(D\). The twist still carries its actual von Mangoldt weight. All following limits are for fixed tests. We calculate a signed functional of this one family of weights.

Let \(q_\nu(u)=q(\log u/\log T-\nu)\), \(L=\log T\), \(H=x/T\), and let \(W_{n,h}(x)\) be the packet weight in the cited calculation. The unsubtracted, off-diagonal sum is
\[
P_T= L^{-3}\sum_n \Lambda(n)q_\beta(n)
\sum_{m\ge1}\omega(m)\sum_{h\ne0,\,nm+h>0}\omega(nm+h)W_{n,h}(nm).
\]
We have \(\operatorname{Re}P_T=o(1)\). To prove this, linearize the real part of the weight as
\[
\widetilde W_{n,h}(x)=\frac{q_\alpha(m)q_\gamma(x)}x K_\Phi(h/H),\qquad
K_\Phi(u)=\int\Phi(t)\cos(tu)\,dt.
\]
On \(|h|\le x/2\) the error in one summand is at most \(C_A |h|x^{-2}(1+|h|/H)^{-A}\). Its sum over \(h\), with the two endpoint weights included, is \(O(D^2 T^{-2})\). Whenever one of the envelopes is nonzero in that comparable region, \(x\ll T^{\gamma+\eta}\). For each twist the number of possible \(m\) is \(O(T^{\gamma+\eta}/n+1)\). After summing the twists with \(\sum_{n}\Lambda(n)|q_\beta(n)|/n\ll L\), the error tends to zero because \(\gamma+\eta<2\). Non-comparable original pairs lie in polynomial ranges and have Schwartz decay at an argument of order at least \(T\). The linearized tail for \(|h|>x/2\) has arbitrary power saving by the same decay. We can therefore extend the periodic function \(\omega\) in the linearized sum to all integers.

For every residue class \(a\bmod Q\), Poisson summation gives
\[
\sum_{h\equiv a\bmod Q}K_\Phi(h/H)=0
\quad\text{when}\quad 2\pi H/Q>2.
\]
Indeed the Fourier samples correspond to \(t=2\pi jH/Q\), \(j\in\mathbb Z\), whereas the angular spectrum of \(K_\Phi\) lies in \((-2,-1)\cup(1,2)\). On the linearized support \(H\ge T^{\gamma-\eta-1}\), so the condition holds for every active \(x\). The complete periodic sum over \(h\) vanishes. Removing \(h=0\) leaves at most
\[
\frac{C D^2}{L^3}\sum_{n\in I_\beta}\frac{\Lambda(n)}n
\sum_{m\in I_\alpha}\frac1m\ll D^2/L=o(1).
\]
Here \(I_\nu=[T^{\nu-\eta},T^{\nu+\eta}]\). This proves the claimed limit for \(P_T\). The reference singular-series sum has real limit \(-\beta c_\psi\), so the signed discrepancy of these common weights satisfies
\[
\operatorname{Re}\mathcal R_T[b_T]\longrightarrow\beta c_\psi.
\]
The conclusion uses the known singular-series average together with the already derived normalization. [Fazzari–Gerspach, Lemma 2.7](https://arxiv.org/html/2412.20099v1#S2.E29)

## Where its uniform row discrepancy fails

Take a sequence of odd prime twists \(p\to\infty\), \(T=p^5\), \(n=p\), \(X=T^\gamma\), and \(h=2\). Throughout \(X\le x=pm\le2X\) the two endpoints lie outside the twist band. For \(p>z\) the average of \(\omega(m)\omega(pm+2)\) in one period equals
\[
2C_{2,z}=2\prod_{2<\ell\le z}\left(1-\frac{1}{(\ell-1)^2}\right),
\]
with the product over primes. At 2 one residue is excluded, and at each odd prime up to \(z\) two residues are excluded. The full singular series is \(s_{p,2}=2C_2(p-1)/(p-2)\), where \(C_2\) uses all odd primes. There are \(\gg z/\log z\) primes in \((z,2z]\), so the omitted Euler factors give \(C_{2,z}-C_2\gg1/(z\log z)\). For example, \(1-\prod(1-u_\ell)\ge1-e^{-\sum u_\ell}\), applied just to this interval, gives this lower bound. The extra factor at \(p\) changes the result by \(O(1/p)\). Thus for large \(p\) the wheel mean exceeds \(s_{p,2}\) by \(\gg1/(z\log z)\).

Complete-period counting on the interval has a remainder \(O(D^2 Q)\). Its row-discrepancy increment therefore exceeds a fixed positive multiple of \(X/(p z\log z)\) for large \(p\). Since \(X/T=T^{\gamma-1}\), this exceeds \((T/p)T^\varepsilon\) for any fixed \(0<\varepsilon<\gamma-1\). At least one endpoint has absolute primitive discrepancy at least half the increment. This is a failure on the same twist and spatial scales as the packet. The construction supplies a common sequence and the desired scalar cancellation. The full row discrepancy imposes an additional arithmetic requirement.

## Exact consistency of shared atom weights

For specified positive endpoint bands with disjoint supports, record admissible sites as edges \((m,r)\) of a bipartite graph. Observed edges with the same endpoints must have identical weight. On a graph with positive edge labels \(w\), a representation \(w(m,r)=u_m v_r\) exists exactly when the alternating products agree around every even cycle. Choose one positive value in each connected component and propagate the other values by division along a spanning tree. Equality of the remaining edge labels is equivalent to the fundamental cycle conditions. With some zero edges, an observed zero edge cannot have both endpoints incident to positive edges. When this property holds, the positive subgraph takes the preceding factorization, and vertices incident only to zero edges may be set to zero. This is the usual rank-one partial-matrix completion criterion. Disjoint endpoint bands allow the two arrays to be viewed as one arithmetic sequence. The inferences here concern prescribed atomic labels. [Hadwin, Harrison and Ward, rank-one completions](https://doi.org/10.1090/S0002-9939-06-08094-4)

On a positive four-cell rectangle write \(D_4=\log(w_{11}w_{22}/(w_{12}w_{21}))\). Its distance to additive row and column potentials in log sup norm is exactly \(|D_4|/4\). The triangle inequality supplies the lower bound. Subtract \(D_4/4\) on each diagonal log entry and add it on each off-diagonal log entry to obtain a zero alternating sum. This gives equality.

Two rectangles quantify the distinction for the separately assigned surrogate at \(c=0\), with \(Q=210\) and \(T=n^5\). The checker certifies all four endpoint integers are prime in each example by trial division. Every shift is permitted, nonzero, and has magnitude below \(nm/T\). These finite sites lie in the indicated bands, for example with \(\eta=.02\) and a test positive at the indicated frequencies. This calculation uses the surrogate's finite weights directly. The preceding limit for common periodic weights uses the additional asymptotic inequality \(Q\ll H\).

- At \(n=11\), take \(m=(1771387,1771397)\) and \(r=(19485283,19485341)\). The shifts are \(((26,84),(-84,-26))\). The sieve-supported, pre-floor weights \(s_{n,h}/d_{n,h}(Q)\) are in the ratio \(((12/11,1),(1,12/11))\) times a common scalar. The prime 13 divides the two diagonal shifts. Factors belonging to primes at most 7 cancel against the sieve normalization. The resulting cross ratio is \(144/121\).
- At \(n=5\), take \(m=(15329,15331)\) and \(r=(76631,76649)\). The shifts are \(((-14,4),(-24,-6))\). All four pre-floor weights equal \(28C_2\). The cumulative counts of allowed sites in the overlap at these endpoints are \(((1752,1460),(2920,2920))\). Flooring the cumulative weights produces integer jumps \(((18,19),(18,18))\), giving determinant \(-18\). A common sequence gives determinant zero. For an exact floor certificate, compute the finite Euler product up to \(Y=10^6\) by rational outward rounding. The remaining tail is between \((Y-1)/Y\) and one, since the product over all integers beyond \(Y\) telescopes. These bounds uniquely determine every floor used here.

Atomic cycle failures can be invisible to linear averages. For a finite graph, the conic hull of the restrictions of nonnegative products \(u_m v_r\) is the entire cone of nonnegative edge tables. A sequence supported on just the two endpoints of one edge spans its coordinate ray. Thus a mixture of common sequences can match arbitrary nonnegative edge weights in expectation, after duplicate edges are identified. This observation imposes no size or primitive bounds on its individual sequences. The wheel above gives the cancellation for a single deterministic sequence at each height, with a quantified violation of the full singular-series discrepancy.

`python3 check_common.py` reproduces `receipt.json` using only standard-library integer and rational arithmetic. The 120 additional local-product checks verify finite wheel averages. The packet limit and the size of the large primitive error follow from the analysis above.

## Guide to the full research handoff

The 881-page historical handoff contains 280,578 whitespace-delimited words. It preserves the original research rounds, including failed attempts and later corrections. Its opening chapters report the finite Newman-depth constructions, the role of the surrounding zeros at a Lehmer pair, the Fable and Inoue audit, and the prime-gap sieve investigation. The residual Gram chapter records the computed saturation, the independent replay, and the unsuccessful attempts to transfer the finite bound to primes. [Full Markdown](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/b7e68548e809b6be8626ea7019357f7dc07311fd/docs/handoff/HANDOFF_2026-11-06.md) · [Full PDF](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/b7e68548e809b6be8626ea7019357f7dc07311fd/output/pdf/HANDOFF_2026-11-06.pdf)

The 65-page quantitative addendum gives the interval certificate at \(N=11\). At scalar heat time \(\log(85/84)\), survival rises from approximately 19.8104% to 21.5629% while the full joint pair-displacement and sorted-gap law and all protected trace expectations agree. The addendum also evaluates the signed prime main term under RH, identifies the precise residual threshold, and applies the Landon–Sosoe–Yau theorem to a rigid clock to test backward inference from DBM. [Addendum and reproduction files](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/tree/f28ca3e9376f45336100295fa130cb75e6a5b415/research/quantitative-survival)

For prime gaps, the project replay recovered admissible-tuple minima of 176, 182, and 186 at 38, 39, and 40 shifts. The examined 39-coordinate sieve trial attained 0.994467820900683 before restoring arithmetic support, below its required threshold of one. The 186 and 182 bounds belong to the cited external projects. The formalizations list their imported hypotheses. For zero gaps, Inoue's bound is conditional on RH and gives \(\mu<0.50895\). The later half-spacing endpoint result allows arbitrarily small positive slack above one half. A fixed improvement below one half for actual zeta zeros remains a research target. [Prime-gap audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/b7e68548e809b6be8626ea7019357f7dc07311fd/research/november-checkpoint/prime-review.md) · [Inoue](https://arxiv.org/abs/2604.05733) · [Durkan–Pearce-Crump](https://arxiv.org/abs/2610.28527v2)

Internal reviewers checked the packet reduction, the shared sequence calculation and its shift-two discrepancy independently. The final verification compared both earlier Markdown/PDF pairs to the public GitHub files, checked all 42 files in the historical PR and all 43 public manifest entries in the quantitative addendum, and verified the 18 locally archived discovery files. External proof review and formal verification of the project's conclusions remain open. The latest checked Fable revision is recorded in the older collaboration thread, which also contains the handoff for review. [Fable revision](https://github.com/galpha-ai/Alpha-devbox/pull/11#issuecomment-6568092545) · [Review handoff](https://github.com/galpha-ai/Alpha-devbox/pull/11#issuecomment-6703030951)
