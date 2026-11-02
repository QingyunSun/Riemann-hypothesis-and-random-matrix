# Round 28: actual prime matrices, significant Mellin pairings, and the cost of a uniform operator target

Date: 2026-09-06. Status: complete ordinary Mellin derivation with independent review, and a separately reviewed finite floating experiment. The Gaussian comparison is an exact theorem about its defined finite model. No actual-prime operator asymptotic, strict global covariance estimate, AH refutation, RH proof, Montgomery–Dyson/GUE theorem, or new prime-gap result is established.

The main experimental finding is that selected Mellin transpose pairings reach about 35%, 47% and 55% of the three actual finite matrix norms. A modest projection of one leading eigenvector had not revealed this contribution. The separate analytic result identifies these transpose pairings exactly as centered prime and zeta-zero observables. The fixed Möbius/logarithmic pairing remains a different, weaker target than a bound for the whole operator.

## 1. Complete sources and review scope

- [Predeclared matrix experiment](../dyson/round28/actual-prime-matrix-test/EXPERIMENT_PLAN.md), [initial report](../dyson/round28/actual-prime-matrix-test/RESULTS.md), and [complete original output](../dyson/round28/actual-prime-matrix-test/results.json).
- [Separately declared Mellin grid follow-up](../dyson/round28/actual-prime-matrix-test/MELLIN_FOLLOWUP_PLAN.md) and [complete grid output](../dyson/round28/actual-prime-matrix-test/mellin_results.json).
- [Separate transpose-pairing follow-up](../dyson/round28/actual-prime-matrix-test/FOLLOWUP_TRANSPOSE_PAIRING.md) and [all six results](../dyson/round28/actual-prime-matrix-test/transpose_pairing_results.json).
- [Independent full numerical review](../dyson/round28/actual-prime-matrix-review/INDEPENDENT_MATRIX_REVIEW.md) and the coordinator's [standard-library transpose replay](../dyson/round28/coordinator-transpose/COORDINATOR_TRANSPOSE_REPLAY.json).
- [Complete ordinary Mellin proof and finite Gaussian theorem](../dyson/round28/mellin-operator-audit/MELLIN_OPERATOR_AUDIT.md) and [root's independent full review](../dyson/round28/mellin-operator-review/INDEPENDENT_MELLIN_OPERATOR_REVIEW.md).

Original reports, their later qualifications, all scripts, raw arrays and receipts remain separate and unchanged. The initial frequency projection test was not the direct transpose test; the latter was requested and performed after that distinction was identified.

## 2. The matrices use actual prime powers and the original center

For \(T=1000,2000,4000\), set \(X=T^2\), \(\ell=\log T\). Both matrix indices run over every odd integer in
\[
I_T=(1.05T,1.35T].
\]
The unchanged central expression is
\[
C_{d,k}=f_T(dk),
\]
\[
f_T(m)=X\ell^2b_T(m)\chi(m/X)
\sum_{h\ {\rm even}}V(h/T)
\left(1+\frac hm\right)^{-T}[\Lambda(m+h)-2].
\]
The two profiles are the fixed smooth exponential bump centered at \(1.5\), supported in \((1.05,1.95)\). The mass weight \(b_T\) is the actual R21/R26 integral, with the fixed R16 autocorrelation \(\omega\). Its transformed integral is evaluated numerically, rather than replaced by its leading asymptotic.

Every required even shift is included. The von Mangoldt sequence contains prime powers with coefficient \(\log p\), and the parity center is exactly two. All ordered factor pairs are retained, including equal products; grouping them only avoids repeating identical computations. The array is real symmetric because entries depend on the product, but can have eigenvalues of both signs.

The relevant fixed arithmetic contraction is
\[
Z_{I_T}=\frac{2}{X\ell^2}\mu^{\mathsf T}C\log,
\qquad \mu_d=\mu(d),\quad(\log)_k=\log k.
\]
It is one balanced block, not the full R26 \(\mathcal Z_T\).

## 3. Original finite results

All three predeclared cases completed. The displayed figures below are rounded floating values; the complete precision, profiles and source parameters are in the original outputs.

| \(X\) | Dimension | Operator norm | Frobenius norm | Fixed normalized \(Z_{I_T}\) |
|---:|---:|---:|---:|---:|
| 1,000,000 | 150 | 217.9604 | 1349.9929 | -0.0004248207 |
| 4,000,000 | 300 | 457.1715 | 3956.2697 | -0.0006341726 |
| 16,000,000 | 600 | 1017.3312 | 12308.018 | -0.0004468770 |

The magnitude of the fixed contraction is approximately 4.8%, 7.6% and 5.3% of its respective operator Cauchy bound. The three signs do not establish a limiting sign, a global negative covariance, or any asymptotic exponent.

The leading singular value carries about 2.61%, 1.34% and 0.683% of total squared Frobenius mass. The next singular value is respectively 98.1%, 99.3% and 98.7% as large. There is no isolated mode carrying a majority of the matrix energy in these arrays. This narrow observation does not rule out a family of coherent modes.

## 4. The Mellin projection grid and the essential correction

The follow-up uses the existing arrays only. For each matrix it samples exactly four times the matrix dimension in frequencies through the declared maximum-local Nyquist scale of the unequal logarithmic spacings. At positive \(t\), it computes the exact two-dimensional projection onto
\[
\operatorname{span}\{\cos(t\log d),\sin(t\log d)\},
\]
using the full two-by-two Gram matrix. Zero frequency is handled as rank one. The selected winners are independently checked by QR.

| \(X\) | Selected \(t/T\) | Squared projection of top vector |
|---:|---:|---:|
| 1,000,000 | 1.7568685 | 0.1316356 |
| 4,000,000 | 1.5234208 | 0.1228762 |
| 16,000,000 | 1.1902279 | 0.0572381 |

These are maxima on the stated grid for that projection statistic. They do not maximize a matrix pairing, optimize continuous frequency, or test all possible envelopes and combinations of modes.

The important correction is that plane overlap does not determine the actual Mellin operator test. With
\[
w_t(d)=d^{it}/\sqrt{|I_T|},
\]
that test is the complex **transpose** contraction
\[
B_C(t)=w_t^{\mathsf T}Cw_t.
\]
It is not \(w_t^*Cw_t\). Even complete projection onto a plane can coexist with a zero transpose pairing: on a real orthonormal cosine/sine plane, take \(C=I\) and \(w=(q_c+iq_s)/\sqrt2\).

The subsequent calculation evaluated only zero and each already selected winning frequency. It did not add heights, change profiles, or search for a new maximum. Its positive-frequency results are:

| \(X\) | \(|B_C(t)|\) | \(|B_C(t)|/\|C\|_{\rm op}\) |
|---:|---:|---:|
| 1,000,000 | 76.88797 | 0.3527612 |
| 4,000,000 | 216.43681 | 0.4734258 |
| 16,000,000 | 557.85252 | 0.5483490 |

Thus the finite Mellin pairings are substantial despite the much smaller projection of one top vector. The plane compression retains sizable eigenvalues of both signs. Interpreting the initial top-vector result as absence of Mellin structure would be incorrect.

At zero frequency the three norm ratios are only about 3.29%, 8.87% and 5.61%. The nonzero-frequency observation is consequently more informative than a test of the constant vector alone. It still supplies no asymptotic lower bound for the exact continuum-defined matrix.

## 5. An exact actual-prime Mellin test

For any of the finite balanced rectangles, let
\[
r(m)=\#\{(d,k):dk=m\},\qquad N_d=|\mathcal D|,\quad N_k=|\mathcal K|.
\]
The ordinary proof gives
\[
\mathcal M_T(t)=
\frac1{\sqrt{N_dN_k}}\sum_m r(m)f_T(m)m^{it},
\qquad
\boxed{\|C\|_{\rm op}\ge\sup_{t\in\mathbb R}|\mathcal M_T(t)|.}
\]
This is a transpose pairing of two unit vectors. Neither continuum replacement of the indices nor a smooth approximation to \(r(m)\) occurs.

For fixed \(X\), its exact Cesaro diagonal identity is
\[
\lim_{R\to\infty}\frac1{2R}\int_{-R}^R|\mathcal M_T(t)|^2dt
=\frac1{N_dN_k}\sum_m r(m)^2|f_T(m)|^2.
\]
This identity is not a numerical enclosure of the all-real supremum.

Set
\[
a_t(x)=\sum_{m\ {\rm odd}}r(m)m^{it}F(m,x-m),
\qquad P_X=\frac{X\ell^2}{\sqrt{N_dN_k}}.
\]
Then
\[
\mathcal M_T(t)=P_X\sum_{n\ {\rm odd}}a_t(n)[\Lambda(n)-2].
\]
For \(E(x)=\Psi(x)-x\), the exact form retaining both corrections is
\[
\boxed{\mathcal M_T(t)
=P_X\left[-\int E(x)a_t'(x)\,dx+L_t-P_{2,t}\right],}
\]
\[
L_t=\int a_t-2\sum_{n\ {\rm odd}}a_t(n),\qquad
P_{2,t}=(\log2)\sum_{j\ge1}a_t(2^j).
\]
All support is compact. No pole or continuous centering term has been omitted.

Changing variables to logarithmic height gives an exact pairing with the R21 carrier \(e^{-v/2}E(e^v)\), and with its cutoff version where the fixed central weight is positive. The existing heat energy does not bound all these arithmetic tests without their dual multiplier norms.

## 6. The actual zero representation and its remaining obligation

For \(\widetilde a_t(s)=\int a_t(x)x^{s-1}dx\), the smooth explicit formula yields
\[
\mathcal M_T(t)=P_X\left[
L_t-P_{2,t}-\sum_\rho\widetilde a_t(\rho)
-\sum_{j\ge1}\widetilde a_t(-2j)\right].
\]
The zeta pole is canceled by the original center through \(L_t\). The powers of two and trivial zeros remain explicit. The zero sums converge absolutely for each compact smooth test.

Uniformly over real \(t\), the displayed corrections satisfy
\[
P_XL_t=O(X^{-1/2}),\qquad
P_XP_{2,t}=O_\eta(X^\eta),\qquad
P_X\sum_{j\ge1}|\widetilde a_t(-2j)|=O(X^{-2}).
\]
The middle estimate is deliberately coarse but smaller than the proposed norm scale for fixed \(\eta<1/2\).

In particular the proposed uniform norm saving
\[
\|C\|_{\rm op}^2\ll X(\log X)^{2-\delta}
\]
would require the unproved actual-zero estimate
\[
\boxed{\sup_t\left|\sum_\rho\widetilde a_t(\rho)\right|
\ll(\log X)^{-1-\delta/2}.}
\]
The exact transform displays \(m^{i(t+\gamma)}\) under RH, but this does not by itself justify localization near \(t=-\gamma\). The sampled product multiplicities and possible aliases remain.

## 7. A precise extra-logarithm warning in a separate finite model

Let \(N\) be odd, let \(\xi_j\) be independent real Gaussians of variance \(\sigma^2\), and set
\[
H_{jk}=\xi_{j+k\pmod N}.
\]
Reflection turns this cyclic Hankel matrix into a circulant. Its exact norm distribution is
\[
\Pr\{\|H\|_{\rm op}^2\le N\sigma^2z\}
=\operatorname{erf}(\sqrt{z/2})(1-e^{-z})^{(N-1)/2}.
\]
Its mean is bracketed by \(N\sigma^2H_{(N-1)/2}\) and that quantity plus \(N\sigma^2\).

At \(X=N^2\), \(Y=N\), \(\sigma^2=Y\log X\), the ordinary model theorem gives
\[
\frac{\|H\|_{\rm op}^2}{X(\log X)^2}\longrightarrow\frac12
\quad\text{in probability}.
\]
Yet any deterministic sample-independent unit-vector contraction has mean square at most \(N\sigma^2=X\log X\). Thus a fixed normalized pairing can vanish while the corresponding normalized uniform operator norm does not.

This model includes independent Gaussian cells, a cyclic wrap and special index geometry. No comparison with the actual prime matrix has been proved. Its theorem does not refute the actual operator route; it explains why that route can be more demanding than the fixed arithmetic-vector target.

## 8. Independent validation and preserved data

Plato independently computed nine entries by factoring all 9,441 participating integer endpoints and using a separate nested adaptive autocorrelation integral. Those samples include the explicit higher powers \(1201^2\), \(2411^2\), \(4801^2\). The maximum entry discrepancy was about \(1.25\times10^{-14}\). Every stored eigenpair, full spectral reconstruction, matrix symmetry, product map and the relevant vector normalizations were checked.

The six transpose values were checked independently through the real cosine/sine expansion, the full signed eigendecomposition and the grouped product formula. The coordinator additionally read the saved array payloads with Python's standard library and recomputed the six values without NumPy. These different numerical paths agree at the recorded floating tolerances. They are not interval certificates; observed quadrature agreement does not prove a rigorous absolute rounding enclosure.

Root independently reviewed the full Mellin derivation and repeated the unchanged 56-case exact checker. Its JSON and stdout match in full. Those finite identities do not mechanize the analytic contour proof.

All 59 originals, totaling 33,610,266 bytes, are retained locally. The public copy preserves 56 files / 33,281,840 bytes verbatim, including all 11 numerical archives with 115 arrays. Three full primary HTML bodies remain local with public hashes. The 124 dependency checks include 36 explicit exact-byte path relocations. Array schema and finite-value checks pass. The original and follow-up computations remain separately dated; no arrays or reports are silently rewritten.

The source experiment records a single-run elapsed time, not a performance comparison. Peak RSS was not measured, so the proposed memory guard is not claimed to have been monitored. No full numerical experiment, new height or frequency search was rerun for publication.

## 9. Research decision

The substantial finite Mellin tests make it worthwhile to analyze how the fixed logarithmic cofactor vector couples to those directions. Controlling its particular input contribution may be easier than controlling every vector. This is a next analytic task, not a conclusion proved by the three matrices.

The literature recheck did not add a new source breakthrough: Lamzouri's arXiv:2609.02882 had already been assessed in the [R7 source frontier](../dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md). Its fixed-support tools do not furnish the missing high-band arithmetic upper bound. The current programme therefore continues on the actual signed pairing and its exact analytic estimates.

The R26 global covariance remains \(O(1)\) under RH by the inherited variance bound. The strict improvement below \(A-2M\), the actual-zero distribution theorem, and any famous-conjecture conclusion remain open.
