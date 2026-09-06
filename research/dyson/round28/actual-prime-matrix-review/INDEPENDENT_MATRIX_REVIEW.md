# Independent review of the R28 actual-prime matrices and Mellin transpose follow-up

Date: 2026-09-05. Reviewer: Plato (`residual_gram`), independent of author Aquinas. Status: accepted as a reproducible, bounded **floating diagnostic**, with the interpretation and limitations below. This is not an interval certificate, an asymptotic operator bound, a strict prime-covariance estimate, or a theorem about AH.

Frozen reviewed inputs:

- `../actual-prime-matrix-test/RESULTS.md`, SHA256 `acf1ec31909cda5ef788778d10e152d9813eaee97095d9f34adcb2c2b731a722`.
- Its `AUTHOR_RECEIPT.json`, SHA256 `c29d6feaeaee0f1f643ee8849c8fef7a77b09d111999c1aa60ecdb6ef3f86121`.
- The separate `FOLLOWUP_TRANSPOSE_PAIRING.md`, SHA256 `858009c2dd603ad8e6956a51a43263d30dc592fb09331c9d44762475c4734ee0`.
- Its `FOLLOWUP_TRANSPOSE_RECEIPT.json`, SHA256 `d030c8f423424683515cdf09e0ec08fe2091fc1f8c681d75f65ce284b5697a5b`.

I read both complete reports, all three numerical scripts, both declared plans, both artifact receipts, the source receipt, and the actual R27 definition. I independently checked saved-array identities, every stored eigenpair, nine matrix entries using independent factorization and independent nested quadrature, and the six selected complex transpose pairings. No broad prime sieve, new height, new frequency grid, or full eigensolver was run in this review. No author input was edited.

## 1. Verdict: faithful matrices, with a material follow-up interpretation

The saved matrices implement the stated genuine-prime expression, including higher prime powers, parity, the flat center two, the unchanged autocorrelation bump and the exact continuum mass kernel evaluated numerically. Their normalizations and saved matrix/eigenvector data pass the independent checks below.

The original leading-vector tests do not show an isolated dominant singular mode in these three matrices. That narrow statement is consistent with the recorded spectra. It must not be read as absence of a coherent Mellin contribution to the operator norm. The separate follow-up directly demonstrates why: at the selected frequencies, the actual unconjugated pairings have magnitudes approximately 35.3%, 47.3% and 54.8% of the full operator norm, despite considerably smaller projection of the single top eigenvector into the corresponding cosine/sine plane.

Thus the follow-up is part of the current interpretation, rather than an optional footnote to a claim of “no coherent mode.” It does not, however, give an asymptotic lower bound or show that the proposed R27 uniform estimate fails. Nor does it estimate the full fixed Möbius/log covariance. Both reports keep those distinctions explicit, and I accept the combined diagnostic on that basis.

## 2. Exact mathematical definition and its implementation

For the three declared values \(T=1000,2000,4000\), put \(X=T^2\), \(\ell=\log T\). Every odd integer in \((1.05T,1.35T]\) occurs as both a row and a column. The implemented matrix is
\[
C_{d,k}=X\ell^2 b_T(dk)\chi(dk/X)
\sum_{h\ \mathrm{even}}V(h/T)
\left(1+\frac h{dk}\right)^{-T}
[\Lambda(dk+h)-2].
\]
Its entry depends only on \(dk\), so symmetry is exact even though the matrix can have eigenvalues of both signs. The source is the actual arithmetic R27 matrix; no synthetic random ensemble is used.

The row bounds and the strict smooth-support bounds are correctly implemented for the declared integer heights. All products lie in \((X,2X)\), with no removal based on factorization. All nonzero even shifts are included. Deduplicating products merely avoids repeating an identical shift sum; the inverse product map restores every ordered matrix position. I verified that inverse map against the full outer product of the saved integer rows, and verified exact equality between the saved matrix and the reconstructed product-value array.

The two compact profiles are exactly the displayed exponential bump with center 1.5 and half-width 0.45. The source autocorrelation is
\[
\psi(v)=\frac{\int f(x)f(x-v)dx}{\int f(x)^2dx},
\qquad
f(x)=e^{-1/(1-4x^2)}1_{|x|<1/2},
\qquad \omega(u)=\psi(4(u-2)).
\]
For \(v\ge0\), the numerator integration interval is \([v-1/2,1/2]\), with midpoint \(v/2\) and half-width \((1-v)/2\). These are exactly the author's Gauss–Legendre change of variables. The denominator has the required additional factor one-half when quadrature on \([-1,1]\) is rescaled. The even extension and the zero extension at \(|v|\ge1\) are correct. The clamped spline derivatives at zero and one match the exact symmetry and compact smooth support.

The source integral is
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}dx.
\]
With \(r=-(T-1)\log(x/m)\), direct differentiation gives
\[
X\ell^2 b_T(m)
=\frac Xm\frac T{T-1}
\int_0^\infty e^{-r}
\omega\left(\frac{\log m}{\ell}-\frac{r}{(T-1)\ell}\right)dr.
\]
Extending the upper transformed endpoint to infinity is exact because the zero-extended \(\omega\) vanishes below its logarithmic support. The code retains this integral rather than replacing it by its leading large-\(T\) approximation. The prefactor in the code is consequently correct: neither \(X\), \(\ell^2\), nor \(T/(T-1)\) is missing or counted twice.

The shift exponent uses `exp(-T*log1p(h/m))`, which evaluates the original Pareto factor. The separate prime, flat-center and directly centered window arrays allow the center to be checked independently; the center is exactly two, not an empirical average.

## 3. Genuine von Mangoldt coefficients and prime powers

The author's finite sieve correctly marks primes and then fills every power \(p^a\), \(a\ge2\), by \(\log p\). A prime-power coefficient is not \(\log(p^a)\). The saved sparse array has positive values at its strictly increasing integer support and reconstructs zero at all other integers. The declared limit exceeds every used product-plus-shift endpoint. The separate Möbius sieve correctly changes sign at multiples of each prime and sets square-divisible arguments to zero; it does not impose coprimality between row and column factors.

For independent arithmetic verification I generated trial primes only through 5499, sufficient to factor any of the sampled endpoints below the declared 29.2-million limit. I did **not** rerun the large sieve. At each independently chosen sample entry, every participating odd integer \(m+h\) was factored, and its von Mangoldt coefficient was computed directly from that factorization. Across the nine sample entries this checks 9,441 shift terms. Every sampled coefficient agrees with the saved sparse array; the maximum difference is zero in the retained floating log evaluations.

The sample rule was fixed before evaluating those entries: the lower corner, a non-diagonal interior position, and the first product window containing the square of the first prime at least \(1.2T\). The last selection is an explicit coverage test of higher prime powers, not a choice made to favor an operator statistic. It includes
\[
1201^2=1442401,\qquad
2411^2=5812921,\qquad
4801^2=23049601.
\]
The independent fixtures also include ordinary primes, powers of two, odd squares, higher powers and non-prime-power composites. I separately factored every saved row integer to verify all three Möbius vectors and their agreement with the saved prefix. These are bounded independent checks of the implementation, not an assertion that every one of the 1.8 million saved nonzero coefficients was independently factored.

## 4. Independent entry integration and the error scope

The reviewer entry calculation does not import the author's `Omega`, its spline tables, its Gauss–Legendre nodes, its Gauss–Laguerre quadrature, or its prime sieve. It uses scalar seed/profile functions, adaptive integration for the denominator and the overlapping autocorrelation interval, adaptive integration in \(r\in[0,48]\), independently factored coefficients, and `math.fsum` for the physical shift sums. This gives a genuinely different numerical path for the selected entries.

The largest observed independent entry discrepancy in each case was:

| X | Independently factored shift terms | Maximum absolute entry difference |
|---:|---:|---:|
| 1,000,000 | 1,347 | \(1.25\times10^{-14}\) |
| 4,000,000 | 2,697 | \(7.11\times10^{-15}\) |
| 16,000,000 | 5,397 | \(1.07\times10^{-14}\) |

The individual products, indices, higher-power hits, separate prime and center sums, prefactor comparisons, and reported quadrature errors are retained in `independent_matrix_checks.json`. These are observed floating comparisons, not outward enclosures.

The rigorous analytic tail fact is narrower: nonnegativity and Cauchy–Schwarz give \(0\le\omega\le1\), so discarding \(r>48\) changes the exact transformed prefactor by at most
\[
\frac Xm\frac T{T-1}e^{-48}.
\]
For an entry, this bound must additionally be multiplied by the absolute value of its profile and centered finite shift sum. This analytic truncation bound says nothing by itself about rounding, adaptive quadrature error estimates, spline error, or the Gauss quadrature error.

The stored 32/64 Laguerre and coarse/fine autocorrelation-table comparisons are also faithful to the code and saved arrays. Agreement near machine precision across all required products is useful numerical stability evidence. It is not a rigorous absolute-error certificate, since both constructions use floating arithmetic and no interval remainder theorem is supplied. The author's direct checks use the same fine autocorrelation quadrature; our additional nested adaptive integration reduces that shared-algorithm concern but still remains floating.

## 5. Stored spectra, projections and fixed contraction

I verified bitwise matrix symmetry, every stored eigenvalue/eigenvector pair through the full residual matrix, orthonormality of the full stored eigenvector matrix, and reconstruction from its complete signed spectrum. No new eigensolver was run. The largest relative Frobenius residuals were:

| X | Full stored-eigenpair residual / Frobenius norm | Maximum entry of orthogonality error |
|---:|---:|---:|
| 1,000,000 | \(2.04\times10^{-15}\) | \(2.56\times10^{-15}\) |
| 4,000,000 | \(2.47\times10^{-15}\) | \(2.45\times10^{-15}\) |
| 16,000,000 | \(3.18\times10^{-15}\) | \(3.11\times10^{-15}\) |

These full-spectrum checks are a little different from the author's top-eight residual statistic and need not have identical values. Both are consistent with the stated floating precision. The author correctly orders singular values by absolute eigenvalue; the left singular vector has the eigenvalue sign relative to the right vector, leaving squared projection values unchanged.

The operator/Frobenius norms, stable ranks, top energy fractions, singular-value gaps and normalized norm ratios all recompute from the saved arrays. The second singular value is close to the first in every case; the largest mode carries only the displayed small fraction of total squared Frobenius mass. This supports the limited statement about lack of a single isolated dominant leading mode in these arrays. It does not assert a limiting spectral law or independence of the many closely spaced modes.

The original fixed-vector contraction is correctly normalized as
\[
Z_{D,K}=\frac{2}{X\ell^2}\mu^{\mathsf T}C\log,
\]
where the logarithmic vector is not centered. Its operator Cauchy bound uses the same factor. I recomputed both from the saved matrix and independently factored Möbius rows, and checked all displayed norm normalizations against `results.json`. The three negative finite contractions do not imply a sign for the global \(\mathcal Z_T\); these matrices cover only three specific blocks.

The low-dimensional overlaps in the original report are squared projections of the top vector, whereas the restricted-input norms are norms of \(CQ\). These are different quantities; the latter does not require the output to lie in the test subspace. The code and report correctly distinguish them. Similarly, centering the logarithmic **test vector** in one overlap calculation does not recenter the matrix or change the original fixed logarithmic contraction.

## 6. The Mellin grid is a projection grid, not an operator test by itself

I read the complete Mellin-template implementation. Its two-dimensional projection formula uses the full cosine/sine Gram matrix, including the cross term; it is not a sum of independently normalized overlaps. Zero frequency is handled as a one-dimensional constant subspace. Translating the logarithmic coordinate by \(\log d_{\mathrm{mid}}\) rotates the same real plane and does not change its projection.

The stored frequency grid has exactly \(4N\) points through the displayed maximum-local Nyquist scale. I checked the exact grid formula against the saved rows, and independently used QR at the winning frequency and five other fixed indices in each case. All selected QR projections agree with the stored projection values within the recorded small floating errors. The full stored projection arrays and code identify the reported maximum on that finite grid; the review did not perform a new frequency search.

The source report correctly warns that unequal logarithmic spacings do not have one universal alias-free Nyquist frequency. This finite grid does not optimize continuous frequency, weighted Mellin envelopes or multimode combinations. Its maximum projection is not a uniform upper bound over those larger classes. The frequencies were chosen after the initial matrix data, and that history is explicitly recorded rather than presented as part of the original predeclared experiment.

## 7. Independent audit of the separate transpose-pairing follow-up

The follow-up keeps the matrices unchanged and evaluates only zero and each previously selected positive frequency. For
\[
w_t(d)=N^{-1/2}d^{it},
\]
the relevant expression is
\[
B_C(t)=w_t^{\mathsf T}Cw_t,
\]
without complex conjugation. The bound
\[
|B_C(t)|=|\langle\overline{w_t},Cw_t\rangle|
\le\|C\|_{\mathrm{op}}
\]
is correct. The exact multiplicative identity is
\[
B_C(t)=\frac1N\sum_m r_I(m)f_T(m)m^{it},
\]
where \(r_I\) counts ordered row/column pairs. There is no Möbius/log weight in this operator test, and it is not the original fixed contraction.

Writing \(w=c+is\), real symmetry gives
\[
B_C(t)=c^{\mathsf T}Cc-s^{\mathsf T}Cs
+2i\,c^{\mathsf T}Cs.
\]
The author's code uses this formula and unconjugated matrix multiplication correctly. Restoring a centered logarithmic phase requires \(e^{2it\log d_{\mathrm{mid}}}\), also correctly included. The grouped-product calculation retains every ordered multiplicity. Its larger floating discrepancy relative to direct matrix multiplication is expected from the distinct large-phase reductions; the author records that discrepancy and does not call it an interval bound.

For an additional independent calculation, I formed the complex test vectors from scalar sine/cosine evaluation, recomputed the real expansion, and also used the **complete signed eigendecomposition**:
\[
B_C(t)=\sum_j\lambda_j(v_j^{\mathsf T}w_t)^2.
\]
The squares here are unconjugated, not absolute squares. I separately reconstructed the pairing from its real-plane compression. Across the six cases the scalar direct calculation agrees with the saved pairings to at most \(1.14\times10^{-13}\), and the full signed spectral expansion to at most \(6.36\times10^{-14}\). The stored compression eigenvalues and ratios also agree.

The independently recomputed positive-frequency ratios are
\[
0.3527612227141845,\quad
0.47342581272882445,\quad
0.5483489690346304.
\]
For clarity, I also calculated the different Hermitian quantity \(w_t^*Cw_t\) as a control: its real values are approximately 32.85, 4.57 and 1.91, very different from the reported complex transpose pairings. This check rules out accidentally replacing the intended statistic by the Hermitian Rayleigh quotient in the independent path.

The two-dimensional compression has opposite-sign eigenvalues of substantial magnitude in the latter two cases. This explains why a transpose pairing can be significant without majority projection of a single leading vector. In general, top-vector plane overlap alone determines neither the transpose pairing nor its absence. The follow-up correctly revises the interpretation of the earlier statistic rather than silently editing its frozen numerical history.

These values are legitimate lower-bound witnesses for the norm of each **saved finite matrix**, up to their explicitly unenclosed floating errors. They do not yield an asymptotic contradiction to \(\|C\|_{\mathrm{op}}^2\ll X(\log X)^{2-\delta}\). Three finite cases cannot supply an asymptotic exponent, a uniform constant, or the required error control on the exact continuum-defined matrices.

## 8. Provenance, reproducibility and minor scope qualifications

The independent main audit checked all 21 entries in the author's original artifact receipt and all three source pins. The separate follow-up audit checked all nine new files and all six explicitly unchanged inputs in its receipt. These are 39 checked receipt entries, including overlap between the two lists; they are not 39 distinct files. The raw NPZ byte hashes bind the data actually inspected. No raw matrix, vector or frequency array was modified.

The original numerical report names the earlier R27 SHA `c7012e...` as the version read, while its final source receipt pins `c7ac888d...`. Our preceding R27 review verified the entire difference: the latter merely corrects the Definition 2.5/2.6 coefficient-sequence terminology. The actual matrix formulas are byte-identical across that source change. This historical metadata distinction has no effect on the experiment, and the final source receipt correctly matches the current file.

The predeclared profiles, heights and core measurements are present in the preserved plan. The running code has the declared time-based omission guard. It does not measure peak RSS or implement a measured one-GiB memory guard; the report explicitly records peak RSS as unmeasured. Consequently the memory cap cannot be claimed to have been independently monitored. The largest dense Lambda array's approximate storage size is a direct shape calculation, not a peak-memory benchmark. This is a resource-reporting limitation, not a numerical defect in the matrices.

The measured runtimes are one-run observations only. Our review neither repeats the whole experiment to compare timing nor claims byte-identical regenerated compressed containers across environments. Reproduction should compare numerical values and invariants with stated tolerances, retain software/BLAS versions, and exclude timing fields from identity comparisons. The source hashes here verify the frozen containers as supplied.

Review outputs are `check_saved_matrix.py`, `independent_matrix_checks.json` and its matching log, `check_saved_transpose.py`, `independent_transpose_checks.json` and its matching log, and the final review receipt. The scripts use the preserved arrays read-only. Their analytic truncation statement is separated from floating quadrature and linear-algebra diagnostics. A syntax/control-byte check of this review is also retained, without claiming that syntax validation proves mathematics.

I accept the experiment and its separate transpose follow-up as bounded actual-arithmetic numerical evidence. The current mathematical conclusion remains open: the operator norm or the fixed signed prime covariance still needs a valid uniform asymptotic estimate. No new famous theorem is established by this numerical checkpoint.
