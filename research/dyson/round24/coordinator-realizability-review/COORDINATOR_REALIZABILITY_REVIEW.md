# Coordinator review: exact zero-margin realizability in actual Pareto families

Date: 2026-09-05. Verdict: both the one/two-profile result and the finite compact-window extension are accepted as ordinary proofs on their stated domains.

I read the complete 7,052-byte original note (SHA256 818f0ac7b2952fd05fde28762079aeb94d23c72fbe8171e3298cedeb935bb60c), its complete 6,993-byte independent review (5b2b0acf98e08b11091e9a342f5b420773443d2ef31f8ebc9f88b001d9b98054), and the complete 11,658-byte finite-window proof (c857d22a766099049bcdc95cdb12bf876d87deb6d83f9e9654c154d4dc2a6a7d). The three complete texts and three cited programme inputs are frozen and hash-verified beside this review. I independently checked the arguments below. No checker, optimizer, prime data, external model or Lean build was used.

## 1. What the negative result actually excludes

For odd endpoints \(m\ge m_0\), \(n>m\), the exact weighted row and column margins are those of \(S(n-m)\delta K(m,n)\), not of \(\delta K\) alone. The positive singular series is evaluated only at positive even shifts.

The existing window variation at exponent t has the separated form \(c(m)n^{-t}\). A nonzero finite checkerboard, by contrast, prescribes individual entries and a separate upper-endpoint support. Both statements can be true: the finite checkerboard cancellation identity is valid, but that checkerboard is not realizable in the tested actual families.

Accepted conclusions:

- At one exponent, even arbitrary lower-endpoint coefficients cannot give nonzero exact zero row margins.
- At two distinct full-tail exponents, arbitrary lower-endpoint coefficients cannot give nonzero exact zero row and column margins on this entire triangular endpoint set.
- At any finite number of distinct full-tail exponents, the same exclusion holds if every coefficient sequence is eventually constant. This class contains finite sums arising from compactly supported changes of the actual lower-endpoint windows.

These statements do not cover separate upper-endpoint truncations, approximate cancellation, or unrestricted non-eventually-constant coefficient sequences at three or more exponents.

## 2. One and two exponents

For t>2, positivity and \(S(h)\ll h^{1/2}\) prove \(0<A_t(m)<\infty\), where
\[
A_t(m)=\sum_{n>m,\ n\ {\rm odd}}S(n-m)n^{-t}.
\]
The one-profile row equation is \(c(m)A_t(m)=0\).

For \(t_1>t_2>2\), the row equation gives
\(c_2=-c_1 A_{t_1}/A_{t_2}\). The ratio is the average of the strictly decreasing function \(n^{-(t_1-t_2)}\) under positive row weights. Since there are positive weights beyond the nearest endpoint, it is strictly below \((m+2)^{-(t_1-t_2)}\). Thus a nonzero balanced row has a nonzero nearest entry.

The first column has one possible lower endpoint and forces that row to vanish. After the preceding rows vanish, the next column again has one remaining possible row. Induction is legitimate because each column contains finitely many earlier endpoints. No double-sum interchange or uniform positive lower bound on the strict bracket is needed. Complex coefficients cause no change. Distinct exponents are essential if the conclusion is stated for individual coefficients.

## 3. Finite compact windows: eventual constants vanish first

The finite-profile extension uses the actual positive divisor expansion
\[
S(2k)=2C_2\sum_{d\mid k}g(d),\qquad
\sum_dg(d)/d=C_2^{-1}.
\]
Its derivation and normalization agree with the already reviewed R23 source. The auxiliary bound \(G(Y)=\sum_{d\le Y}g(d)=O(\log(2Y))\) follows by expanding \(g(d)=d^{-1}\prod_{p\mid d}(1+2/(p-2))\) on squarefree odd d and enlarging a positive harmonic sum. The product \(\prod_{p>2}(1+2/[p(p-2)])\) converges. The prime 3 causes no divergence.

The row mass satisfies
\[
A_t(m)=2C_2\sum_dg(d)\sum_{v\ge1}(m+2dv)^{-t}
\sim \frac{m^{1-t}}{t-1}.
\]
For each fixed d, the inner Riemann sum has normalized limit \(1/[2d(t-1)]\), and decreasing integral comparison gives that same upper bound uniformly in m. Summability of \(g(d)/d\) permits dominated convergence. The factor 2 from the even-grid singular-series mean and the endpoint lattice spacing cancel correctly.

For rows beyond the common finite support endpoint, the row equation is \(\sum_j C_jA_{t_j}(m)=0\). Order the distinct exponents increasingly. Dividing by \(m^{1-t_1}\) isolates \(C_1/(t_1-1)\); then inductively every eventual constant is zero. Hence only finitely many actual rows remain.

Eventual constancy also makes each coefficient sequence bounded. The full absolute double sum is controlled by \(\sum_n n^{1-t}\), using \(\sum_{h\le n}S(h)\le n\). This converges for t>2. No unregulated infinite coefficient construction is hidden.

## 4. Rational-frequency means of the actual singular series

For fixed integer l, odd prime q and \(1\le a<q\), the claimed mean is
\[
\lim_{N\to\infty}\frac1N\sum_{\substack{k\le N\\k>l}}
S(2(k-l))e(-ak/q)
=\frac{2}{(q-1)^2}e(-al/q).
\]

For a fixed d in the positive divisor expansion, the progression \(k=l\bmod d\) has zero phased mean unless q divides d. If q divides d, its phase is fixed and its density is \(1/d\). This is an elementary geometric-progression calculation, not a prime equidistribution input.

The omitted divisor tail after a cutoff D has absolute normalized bound
\[
O\left(\sum_{d>D}g(d)/d+G(N+|l|)/N\right).
\]
Counting at most \(N/d+1\) points in each progression proves the bound, including negative l. First let N grow with D fixed; then let D grow. The first term is an absolutely summable tail and the second tends to zero. This justifies the limit without assuming a uniformly finite divisor expansion.

Finally
\[
2C_2\sum_{q\mid d}g(d)/d
=2\frac{1/[q(q-2)]}{1+1/[q(q-2)]}
=\frac2{(q-1)^2}.
\]
The phase and normalization are correct. This proof works at each fixed q; it neither needs nor asserts uniformity as q grows with N.

## 5. Finite translates cannot converge to zero nontrivially

For finitely supported complex u(l), suppose
\(F(k)=\sum_lu(l)S(2(k-l))\to0\).
The phased Cesaro mean then tends to zero for every fixed q,a. Applying the proved mean to the finite sum yields
\(\sum_lu(l)e(-al/q)=0\) for every \(1\le a<q\).

Choose an odd prime with q−1 greater than the finite support diameter. The polynomial \(\sum_lu(l)z^{l-l_-}\) has lower degree than the number q−1 of distinct nontrivial q-th roots at which it vanishes. It is zero. This is valid for arbitrary complex coefficients; no incorrect rational irreducibility argument is used. An empty support is trivial.

Values at finitely many early k, where a shifted singular series has not yet been defined, do not matter; the proof uses only the eventual sequence and may omit those finitely many terms.

## 6. Separate the finite exponents in the column equations

After the row reduction, each
\(F_j(k)=\sum_lc_j(2l+1)S(2(k-l))\)
is a finite translate combination. The elementary subpower bound \(S(2k)\ll_\eta k^\eta\) is valid for every fixed \(\eta>0\): large local prime factors are at most \(p^\eta\), while finitely many small primes contribute a constant. It applies to the fixed finite translates as well.

Multiply the exact column equation by \((2k+1)^{t_1}\). Choosing \(0<\eta<t_2-t_1\), all other terms vanish as k grows, so \(F_1(k)\to0\). The preceding finite-translate argument eliminates every coefficient in the first profile. Repeating proves the theorem. When only one exponent remains, the column equation directly gives its vanishing.

Arbitrarily close but distinct exponents are allowed: at each fixed external height the positive gap permits a choice of eta. Constants need not be uniform in that height for this exact pointwise-in-height nonexistence statement. The proof must not be repurposed as a quantitative stability bound for approximate margins.

## 7. Consequence for the research task

The kernel produced by a compact lower-window variation has an eventually constant primitive coefficient. Thus an exact-zero-margin search over finitely many such complete Pareto tails is empty, even with complex signs, arbitrary finite windows and any finite number of distinct exponents at each height. This is a structural exclusion of that entire class, not a failed finite-basis numerical experiment.

The original continuum windows themselves need not be zero: different functions may have the same primitive at every sampled integer endpoint. The conclusion is about the actual coefficient sequences and integer kernel.

No amendment to either proof is requested. Stop considering additional finite complete-tail window profiles as a way to realize the coordinator's checkerboard. Keep separate the possibilities of quantitative approximate margins, explicit upper-endpoint cutoffs, or a different comparison theorem, each of which still needs a genuine arithmetic estimate. The strict \(Q_{2,T}\) target remains unproved.

This is an internal ordinary-proof acceptance, not formal verification, external peer review, a global no-go result for all zero-margin kernels, or a theorem about the truth of RH, AH or GUE.

