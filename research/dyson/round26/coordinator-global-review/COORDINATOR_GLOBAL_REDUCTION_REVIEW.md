# R26 global reduction: independent coordinator review

Status: accepted as an ordinary RH reduction, with the inherited R21/R22 inputs explicitly retained. This review does not establish novelty, a strict covariance bound, or a major conjecture. No Lean build or asymptotic numerical validation was performed.

## Material read

I read the complete nine-section Euclid manuscript `FULL_SHIFT_REDUCTION.md` and the complete seven-section Aquinas manuscript `REFINED_SINGULAR_CORRECTION.md`. The frozen versions are recorded in `AUTHOR_BYTES_READ.json`:

- Euclid: 22,834 bytes, SHA-256 `c0d413f2eead98cfc97de09cd5b4f8ffaa0df7a6b81249df576ccff61a0cadd6`.
- Aquinas: 14,577 bytes, SHA-256 `b6a6211db21df5e5d10031027863eb4764bdab820f60ab4befb63c8dc9caeffe`.

This review follows the coordinator's complete R25 review and direct reopening of Montgomery--Soundararajan (47). It does not re-audit all R21/R22 source proofs, the R22 dimension-two upper sieve input, the authors' small checkers, or Plato's final review. In particular the inherited actual variance transfer and the stated uniform upper sieve remain explicit mathematical dependencies, not results newly proved by this review.

## Verdict and exact content

The partition, scale-dependent divisor completion, global error ledger, and constant evaluation support

\[
\mathcal Q_{2,T}=\mathcal Z_T+M_1+O_\omega((\log T)^{-1/2}),
\quad M_1=\int(u-1)\omega(u)\,du.
\]

Here Z_T is exactly the finite expression in Euclid (7), including the actual Pareto weight, smooth upper height and length cutoffs, the lower length partition, all von Mangoldt prime powers, and complementary divisors `d>Q_j` with `Q_j=Y_j^(2/3)`. It is not an old fixed-Q covariance renamed. Inserting the independently inherited variance identity gives, for the actual symmetric weight,

\[
\overline V_T=\mathcal Z_T+2M+o(1).
\]

I found no substantive gap in these two supplied manuscripts. The proof's small- and large-shift coverage is substantially stronger than the frozen R25 fixed-packet statement.

## Independent checks of the critical steps

1. **Partition and finiteness.** The beta sums telescope to `1-r(2m/L)` and `1-r(2h/Y_0)`. Since b vanishes for m<=L, the height factor is exactly one wherever needed. The two upper cutoffs restrict m<4U and h<2Rm/T. They leave a finite collection of packets with X_i<8U and Y_j<8RX_i/T. No growing packet count is absorbed into an unspecified little-oh term.

2. **Uniform derivatives.** The scaled Pareto derivatives are bounded by a fixed polynomial in Y/H times exponential decay, uniformly even when Y/H is as large as a constant times log T. Fixed derivative orders 16, 36, and 4 therefore do not introduce powers of log T through their seminorms. The shifted n=m+h endpoints preserve the X-scale derivatives, and h/X=O(log T/T).

3. **Omitted arithmetic terms.** The direct absolute bound for the new q2 uses Lambda(m)Lambda(m+h) plus the singular-series weighted prime marginals and constant. It therefore legitimately applies the inherited upper sieve to this coefficient, rather than relying on a bound for an older coefficient. Taking K=ceil(sqrt(log T)) makes the small-shift contribution O((log T)^(-1/2)). The m>2U tail retains the exact b(m) decay; integral comparison includes the first integer term. The upper length tail retains the endpoint `a*g(a)` from singular-series partial summation. With R=32 log T, its displayed power is T^(-27/4) times log T.

4. **Polylogarithmic divisor cutoffs.** Q_j grows from (log T)^(1/3), so a fixed-power-in-X argument alone would not suffice. The actual ledger instead has Q/Y=Y^(-1/3). The order-16 discrepancy is Y^(-14/3)/log X; the order-36 principal-mask error is Y^(-12) log^3 X. The nonunit mean is charged separately. The exact positive-integer count for h=2pr is O(Y/p), including the empty p>Y case. It does not require Y much larger than sqrt X.

5. **Joint RH error.** Although `a_Q-2` need not be small in absolute value at the first polylogarithmic Q, the relevant statistic is centered before estimation. Its bound is `Y*Q^(-1/2+epsilon)*log X/sqrt X`. With epsilon=1/100 and Q=Y^(2/3), the Y power is exactly 101/150. This is uniformly summable up to the last allowed physical length. Q remains fixed in each packet when differentiating m.

6. **All nine errors.** Negative Y powers sum geometrically from Y_0. The potentially largest positive-power terms have endpoint powers T^(-19/12) and T^(-17/60), after using the geometric height sums in X^(1/3) and X^(13/75), respectively. The two explicitly loose height sums still decay. The purely logarithmic bounds in Euclid (32) are at worst O((log T)^(-1)). The missing-small-shift bound determines the weaker overall O((log T)^(-1/2)).

7. **Singular-series correction and sign.** The real-endpoint extension of MS (47) uses linear interpolation, costing O(1), and never differentiates a remainder. The resulting transform is `int f - (1/2) int f/h` with remainder bounded by `int h^(1/2+nu)|f''|`. Summing the actual transforms at nu=1/4 costs O((log T)^(-9/8)). Both prime marginals have ambient density one; twice the odd integer lattice also has density one. Thus their correction leaves one positive continuum integral in P-Z, with no missing parity factor.

8. **Constant by two independent evaluations.** Euclid's uniform approximation to b(m) has integrated error O(1/T) against the logarithmic inner integral. Aquinas instead evaluates the exact two moments of b by Tonelli, including the `T/(T-1)^2` endpoint term in the log moment. Both give `M_1-(log Y_0)/(log T)*M_0+O(1/log T)`. The height-cutoff tail is exponentially small. Symmetry gives M_1=M_0=M exactly, without numerical quadrature.

## Research consequence and remaining task

The previously missing all-shift constant is now accounted for. For the programme's sufficient variance target `liminf Vbar<=1`, the corresponding target is

\[
\liminf_{T\to\infty}\mathcal Z_T\le1-2M.
\]

This is a sufficient target, not a necessary characterization of every possible contradiction to AH. A proof that Z_T tends to zero is not required. The full GUE prediction would instead give Z_T tending to -M; that prediction remains unproved for the actual arithmetic object.

The next mathematical work must bound the exact global, scale-dependent signed covariance. The R25 natural-length Fourier representation cannot simply be summed unchanged: the new family reaches down to Y_0=sqrt(log T), uses Q=Y^(2/3), and has O((log T)^2) possible packets. Any next Fourier estimate must preserve these weights and provide a summable error ledger for this range. This is a substantive new scope requirement, not a request for another publication-manifest review or a new numerical scan.
