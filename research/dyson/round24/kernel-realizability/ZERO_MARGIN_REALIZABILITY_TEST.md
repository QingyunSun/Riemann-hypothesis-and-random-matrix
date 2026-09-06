# A realizability test for zero-margin perturbations of the actual Pareto kernel

Date: 2026-09-05. Author: root / Astra. Status: bounded ordinary proof submitted for independent review. This is a negative test of two specific kernel families, not a no-go theorem for arithmetic correlation estimates.

## Problem and actual objects

The coordinator's second reading of the 186 work supplies a useful exact identity: for odd endpoints \(m<n\), any finite matrix \(Z(m,n)\) whose row and column sums vanish gives a perturbation \(\delta K=Z/\mathfrak S(n-m)\) that cancels the singleton and constant terms of \(q_2\). The identity is correct. Its next obligation is to realize such a perturbation in an admissible family of actual kernels, or to prove a comparison to that family.

This note tests the existing single Pareto exponent, and a deliberately enlarged family allowing two distinct exponents with arbitrary coefficients in the lower endpoint. Both tests can be decided exactly without prime data or a matrix optimizer.

Fix a positive odd lower endpoint \(m_0\), and let both endpoints range over odd integers, with \(m\ge m_0\) and \(n>m\). Write \(S(h)=\mathfrak S(h)\). Only two established facts about the singular series are used:
\[
S(h)>0\quad(h>0\text{ even}),\qquad S(h)\ll h^{1/2}.
\]
The second crude bound ensures the row sums below converge. The first is the essential structural assumption.

For each \(t>2\), define the positive row mass
\[
A_t(m)=\sum_{\substack{n>m\\n\ {\rm odd}}}S(n-m)n^{-t}.
\tag{1}
\]
It is finite and strictly positive. A zero-margin perturbation in the present notation means
\[
\sum_{\substack{n>m\\n\ {\rm odd}}}S(n-m)\delta K(m,n)=0
\quad\text{for every }m,
\tag{2}
\]
\[
\sum_{\substack{m_0\le m<n\\m\ {\rm odd}}}S(n-m)\delta K(m,n)=0
\quad\text{for every odd }n>m_0.
\tag{3}
\]
Each column sum is finite. No global interchange of a double sum is needed for the results below.

## 1. Varying the logarithmic window at one exponent cannot give such a direction

At the actual exponent \(T\), the exact kernel separates:
\[
K_T(m,n)=b_T(m)(m/n)^T
=\left[\frac{T}{(\log T)^2}
\int_1^mW_T(x)x^{T-2}\,dx\right]n^{-T}.
\tag{4}
\]
A change in the lower-endpoint window therefore has the form
\[
\delta K(m,n)=c(m)n^{-T}
\tag{5}
\]
on the same endpoint domain. This statement also holds if arbitrary lower-endpoint coefficients are allowed, which is a larger family than changes of a fixed smooth window.

Substitution of (5) into the row condition (2) gives \(c(m)A_T(m)=0\). Positivity of (1) forces \(c(m)=0\) for every actual row. Thus \(\delta K\) is identically zero. The column condition is not even needed.

This conclusion concerns the kernel evaluated on the integer endpoint set. It does not assert injectivity of the map from arbitrary continuum window functions to finitely sampled primitives. Window variations that vanish on every actual row simply produce the zero perturbation in the statistic.

## 2. Two distinct Pareto exponents still do not supply a nonzero direction

**Proposition.** Let \(t_1>t_2>2\). Suppose
\[
\delta K(m,n)=c_1(m)n^{-t_1}+c_2(m)n^{-t_2},
\tag{6}
\]
where the two coefficients can be arbitrary real numbers at each odd lower endpoint. If (2) and (3) hold on the full domain specified above, then \(\delta K=0\). In fact \(c_1(m)=c_2(m)=0\) for all rows.

**Proof.** The row condition gives
\[
c_2(m)=-c_1(m)\frac{A_{t_1}(m)}{A_{t_2}(m)}.
\tag{7}
\]
Put \(d=t_1-t_2>0\). The ratio in (7) is a positive weighted average:
\[
\frac{A_{t_1}(m)}{A_{t_2}(m)}
=
\frac{\sum_{n>m,\ n\ {\rm odd}}S(n-m)n^{-t_2}n^{-d}}
{\sum_{n>m,\ n\ {\rm odd}}S(n-m)n^{-t_2}}.
\tag{8}
\]
All weights are positive, and at least two endpoints have positive weights. The strictly decreasing function \(n^{-d}\) therefore gives
\[
\frac{A_{t_1}(m)}{A_{t_2}(m)}<(m+2)^{-d}.
\tag{9}
\]
In particular the nearest permitted entry in this row is
\[
\delta K(m,m+2)
=c_1(m)(m+2)^{-t_2}
\left[(m+2)^{-d}-\frac{A_{t_1}(m)}{A_{t_2}(m)}\right],
\tag{10}
\]
whose bracket is strictly positive.

For the first column \(n=m_0+2\), equation (3) contains only the row \(m=m_0\). Since \(S(2)>0\), it forces (10) to vanish, and hence \(c_1(m_0)=c_2(m_0)=0\). Assume the preceding rows have zero coefficients. In the column \(n=m+2\), every earlier row contributes zero, so (3) again forces (10) to vanish. Induction over the odd lower endpoints proves the claim. Each step uses a finite column sum, so no convergence or limiting induction issue is hidden. \(\square\)

The argument does not use prime distribution, RH, the sign of \(c_1,c_2\), or a bound on their growth. Row convergence follows from \(t_2>2\). It remains valid for complex coefficients, although real coefficients suffice for the proposed signed perturbations.

## 3. What this does and does not rule out

The genuine single-window family is contained in (5). Even allowing arbitrary coefficients in \(m\) at each of two distinct exponents, as in (6), does not realize an exact zero-row-and-column perturbation on the full triangular endpoint domain. Thus the coordinator's finite checkerboard identity cannot be imported by merely changing the logarithmic window or combining two untruncated Pareto tails.

There is no contradiction with a finite \(2\times2\) checkerboard. Such a perturbation has a separate upper-endpoint support cutoff and independent entries, and belongs to neither (5) nor (6). For example, a checkerboard supported on \(m_1,m_2<n_1,n_2\) has zero entries at early columns; in (6), a nonzero row that has been balanced by (7) is forced by (10) to have a nonzero nearest entry. It is this specific realization constraint that drives the induction.

The following remain open:

- Three or more independent tail profiles, or profiles with separate upper-endpoint cutoffs.
- Approximate margin cancellation with a quantified weighted error rather than (2)–(3) exactly.
- A comparison theorem that imports a finite auxiliary checkerboard into the original positive variance or nonnegative Bragg deficit.
- The signed double-prime estimate on any nontrivial admissible perturbation.

No lower bound for \(q_2\) is substituted for the required upper bound. No loss-free replacement of the original kernel is asserted. The strict target remains
\[
\liminf Q_{2,T}<A-M,
\]
with \(\liminf Q_{2,T}\le1-M\) a stronger sufficient benchmark.

## Provenance and validation scope

The motivating identity and research priority are in the coordinator's frozen second-reading memorandum, SHA256 331e923f508fe05f88491cb0b0992930323c2b095fe48a4083dd427c02ffa9da. The exact original kernel and parity-adjusted coefficient are from the reviewed R22 target, SHA256 36a995c9852e95d6c29e44f2c5dd5815d27318fbabe0a94770e9f21a59c3bb6b.

The two statements above are direct ordinary proofs. They require no numerical certificate and are not formalized in Lean. Their value is to reject a concrete proposed realization before a computation is built around it. They do not rule out the general zero-margin idea, heat methods, or a major conjecture.
