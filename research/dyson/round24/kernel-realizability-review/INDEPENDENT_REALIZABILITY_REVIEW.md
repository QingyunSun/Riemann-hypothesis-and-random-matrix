# Independent review of the one- and two-profile realizability test

Reviewer: Plato / residual_gram, 2026-09-05. Status: **accepted as an ordinary proof on the stated endpoint domain**. No author amendment is requested. No numerical test or scan was needed.

Reviewed report: [ZERO_MARGIN_REALIZABILITY_TEST.md](../kernel-realizability/ZERO_MARGIN_REALIZABILITY_TEST.md), 7,052 bytes, SHA256 `818f0ac7b2952fd05fde28762079aeb94d23c72fbe8171e3298cedeb935bb60c`. Its statement is a negative result for two explicitly specified kernel families, not for general arithmetic perturbations or the Dyson–Montgomery problem.

## 1. Exact domain and convergence

The domain consists of all positive odd lower endpoints \(m\geq m_0\) and all odd upper endpoints \(n>m\), with one fixed positive odd \(m_0\). In particular every row contains its nearest endpoint \(m+2\) and infinitely many later endpoints. Every column contains only finitely many rows. These hypotheses are used in the proof and must remain in any quotation of the result.

For fixed \(m\), the stated elementary estimate \(S(n-m)\ll(n-m)^{1/2}\) bounds the tail of \(A_t(m)\) by a constant times \(\sum_{n>m}n^{1/2-t}\). Hence \(t>2\) more than suffices for absolute convergence. Positivity of \(S(h)\) for each positive even shift implies \(0<A_t(m)<\infty\). Each coefficient at a fixed row is a finite real or complex number; no uniform growth restriction on coefficients is needed for these separate row sums.

The proof never exchanges an infinite sum over rows with an infinite sum over columns. The argument consequently remains valid even for row-coefficient sequences for which a globally weighted double sum would not converge. Such convergence would be an additional requirement for using a surviving direction in the original arithmetic statistic, but it is not a gap in this nonexistence theorem.

## 2. One exponent and the exact original kernel

The original definitions give, for the actual exponent \(T>2\),

\[
b_T(m)(m/n)^T
=\frac{T}{(\log T)^2}
\left(\int_1^m W_T(x)x^{T-2}\,dx\right)n^{-T}.
\]

Thus a change of the lower-endpoint window at fixed \(T\) has exactly the separated form \(c(m)n^{-T}\). Allowing arbitrary coefficients \(c(m)\) only enlarges that family. Its weighted row sum is \(c(m)A_T(m)\), so exact zero row margins force every actual row coefficient to vanish. Column cancellation is unnecessary in this case.

The author correctly distinguishes the integer kernel from its continuum parametrization. This proof does not imply that every continuum window with zero sampled primitive is the zero function. It establishes that such a window gives no nonzero perturbation on the actual integer endpoint set.

## 3. The strict ratio and finite-column induction

For two exponents \(t_1>t_2>2\), the row condition first gives

\[
c_2(m)=-c_1(m)R_m,
\qquad R_m=A_{t_1}(m)/A_{t_2}(m).
\]

After division by \(A_{t_2}(m)\), the positive weights
\(S(n-m)n^{-t_2}\) form a probability distribution on the row. Accordingly \(R_m\) is the expectation of the strictly decreasing function \(n^{-(t_1-t_2)}\). The nearest endpoint has positive mass, but the distribution is not concentrated there: every later odd endpoint also has positive mass. It follows strictly that

\[
0<R_m<(m+2)^{-(t_1-t_2)}.
\]

There is no appeal to an asymptotic singular-series mean or to prime distribution in this step. The positive bracket in author equation (10) is therefore nonzero for each fixed row, even though no uniform quantitative lower bound for the bracket is asserted or needed.

The first column, \(n=m_0+2\), has only one entry. Its zero column margin and \(S(2)>0\) force that row's nearest entry to vanish, and the strict bracket forces \(c_1(m_0)=c_2(m_0)=0\). If all preceding rows vanish, the column \(n=m+2\) has only the current row left. The same argument eliminates it. Ordinary induction through the odd integers proves the result. Every induction step contains only a finite sum. This checks both the infinite-domain quantifier and the absence of an unstated global limiting argument.

The proof also works for complex coefficients: the nonzero bracket is real, but the equation multiplying it is a scalar linear equation. For coincident exponents the separate coefficient conclusion would fail through redundant representations; the author explicitly assumes distinct exponents.

## 4. Relation to the motivating finite identity

I checked the motivating memorandum's Section 2.1 and the exact parity-adjusted coefficient from the cited R22 report. For a finite matrix \(Z(m,n)\) on odd \(m<n\), define \(\delta K=Z/S(n-m)\). Then

\[
\sum_{m<n}\delta K(m,n)q_2(m,n)
=\sum_{m<n}\delta K(m,n)\Lambda(m)\Lambda(n)
\]

when the rows and columns of \(Z\) both sum to zero. Indeed the two singleton sums vanish separately by the respective margins, and the total sum of \(Z\) is zero as well, cancelling the constant two. Thus the motivating algebra is correct.

It does not contradict the present result. A finite checkerboard has independent upper-endpoint truncations and is zero at early columns. In the two full-tail family, a row satisfying its own zero-margin condition has a nonzero nearest entry whenever its coefficients are nonzero. That specific constraint is what starts and sustains the induction.

The hypotheses cannot silently be changed to a rectangle with a common upper-endpoint starting point, to arbitrary endpoint cutoffs, or to approximate margin cancellation. The report explicitly leaves those variants open. Its conclusion also does not provide a quantitative lower bound on the error of approximate cancellation: a qualitative nonzero bracket alone would not establish such a bound.

## 5. Accepted scope and the next unresolved comparison

The exact original kernel and the enlarged two-tail family cannot realize a nonzero perturbation with the stated exact weighted margins. The report properly does not conclude that all zero-margin probes fail. With three profiles there is already extra linear freedom at one row after imposing its row margin and nearest-entry value; this observation alone does not settle the full column system, global convergence, realization by smooth actual windows, or a comparison with the original positive variance.

In particular zero margins do not grant a sign for the remaining double-prime sum. An auxiliary perturbation would still need an admissibility/comparison theorem and a genuine arithmetic estimate with the direction and size needed for the strict target. The stated target \(\liminf Q_{2,T}<A-M\), and the stronger sufficient benchmark \(\liminf Q_{2,T}\leq1-M\), agree with the cited programme definitions. Neither follows from the present negative test.

This review accepts the two direct proofs and their limitations. It introduces no strict Bragg deficit, new prime-correlation bound, or general no-go theorem. The adjacent review receipt verifies the author and cited dependency hashes. Author files were left unchanged.
