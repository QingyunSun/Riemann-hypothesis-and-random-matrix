# Actual prime-window matrices: the declared leading-mode test did not falsify the operator route

Date: 2026-09-05. Author: Aquinas. Status: deterministic floating diagnostic, submitted for independent review. All three cases were declared in `EXPERIMENT_PLAN.md` before implementation. No RH assumption is needed to compute these finite matrices. There is no interval certificate, asymptotic estimate, fitted exponent, random-matrix replacement, or claim about the sign of the full global covariance.

The three matrices have no isolated dominant leading singular mode on the declared grid. Their top singular values are close to the second values, and the top mode carries only 2.61%, 1.34%, and 0.68% of squared Frobenius mass. Its constant, log, and Möbius overlaps are small. A subsequently requested high-frequency Mellin-template check finds maximum squared projections of 13.16%, 12.29%, and 5.72%, larger than the initial low-frequency overlaps but still not majority projections in those tested two-dimensional spans. The fixed Möbius/log contraction is also substantially smaller than its operator Cauchy bound. Therefore this particular attempt to falsify the uniform operator strategy by exposing a dominant coherent leading mode **did not succeed**. This does not exclude untested or weighted coherent modes, establish the proposed operator estimate, or make it preferable to a vector-specific estimate.

## 1. Exact matrix definition and frozen inputs

The source is Euclid's R27 `JOINT_DISPERSION_TEST.md`, Sections 3–4, read in full, SHA256 `c7012e375b62263ec472dcb45e362caebca6d8719fe5080c7476a1f4b0d94e5b`. For each declared central height, set
\[
X=T^2,\qquad Y=T,\qquad \ell=\log T,
\]
\[
C_{d,k}=X\ell^2 b_T(dk)\chi(dk/X)
\sum_{h\ {\rm even}}V(h/T)
(1+h/(dk))^{-T}[\Lambda(dk+h)-2].
\tag{1}
\]
Every odd integer \(d,k\) in \((1.05T,1.35T]\) is used. Their products satisfy \(1.1025X<dk<1.8225X\), hence lie inside \((X,2X)\). No product is removed according to its factorization. The matrix is symmetric because the same row and column sets are used and its entry depends only on their product.

The fixed smooth profiles are
\[
\chi(t)=V(t)=
\exp\!\left(1-\frac1{1-((t-1.5)/0.45)^2}\right)
1_{|t-1.5|<0.45}.
\tag{2}
\]
Their maximum is one. The exact continuum weight is retained:
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}\,dx,
\]
\[
\omega(u)=\psi(4(u-2)),\qquad
\psi(v)=\frac{\int f(x)f(x-v)\,dx}{\int f(x)^2\,dx},
\quad f(x)=e^{-1/(1-4x^2)}1_{|x|<1/2}.
\tag{3}
\]
This is the actual R16 bump, not a replacement polynomial or Gaussian. The zero extension of each smooth profile is used at its endpoints.

The finite von Mangoldt array includes every prime power, with value \(\log p\) at \(p^a\). The flat center is the exact number \(2\), appropriate to odd endpoints. There is no empirical centering, fitted mean, removal of the constant mode, or subtraction of any singular vector.

## 2. Declared cases and preserved arithmetic data

| X | T | Matrix dimension | Row/column integers | Distinct products | Nonzero even shifts | Direct product/shift terms |
|---:|---:|---:|---|---:|---:|---:|
| 1,000,000 | 1000 | 150 | odd 1051–1349 | 11,238 | 449 | 5,045,862 |
| 4,000,000 | 2000 | 300 | odd 2101–2699 | 44,552 | 899 | 40,052,248 |
| 16,000,000 | 4000 | 600 | odd 4201–5399 | 177,130 | 1799 | 318,656,870 |

The shift sums include all even integers where (2) is nonzero, respectively 1052–1948, 2102–3898, and 4202–7798. The genuine prime-coefficient array was constructed through 29,157,201. Its 1,809,625 nonzero entries, including powers, are retained as integer indices and float64 values in `arrays/lambda_coefficients.npz`; zero coefficients are reconstructed as zero. The entire Möbius prefix through 5399 is also saved.

Each `arrays/case_X.npz` contains the raw matrix, row integers, unique products, inverse product map, full even shifts, profile values, both quadrature prefactors, centered window sums, separate prime and exact-flat-center sums, the Möbius/log vectors, complete signed eigenvalues and eigenvectors, and the two predeclared test-subspace bases. Product deduplication only avoids repeating identical finite sums; the inverse map restores every original matrix multiplicity.

The algorithm uses deterministic symmetric eigendecomposition. Since \(C=C^{\mathsf T}\), the singular values are the absolute eigenvalues. The left singular vector associated to an eigenvector differs from its right vector by the eigenvalue sign; all squared overlaps below are unaffected. The full signed spectra are retained. No random seed or randomized SVD is used.

## 3. Raw norms and spectral concentration

All displayed decimals are rounded floating outputs. `results.json` retains the full recorded precision.

| X | Operator norm | Frobenius norm | Top squared-energy fraction | Stable rank | Second/first singular value |
|---:|---:|---:|---:|---:|---:|
| 1,000,000 | 217.960376 | 1349.992893 | 0.0260671 | 38.3626 | 0.980830 |
| 4,000,000 | 457.171547 | 3956.269734 | 0.0133532 | 74.8882 | 0.993398 |
| 16,000,000 | 1017.331212 | 12308.018421 | 0.00683201 | 146.370 | 0.986952 |

Here the top squared-energy fraction is \(\|C\|_{\rm op}^2/\|C\|_{\rm F}^2\); stable rank is its reciprocal. The leading eigenvalue is positive in all three cases. None of these spectra has a large isolated top singular value. This is a finite statement about these arrays, not a claim about a limiting spectral distribution.

For reference, the unmodified squared norm divided by the scale appearing in the proposed R27 bound is

| X | op² / [X (log X)²] | op² / [X log X] |
|---:|---:|---:|
| 1,000,000 | 0.000248897893 | 0.00343865147 |
| 4,000,000 | 0.000226103916 | 0.00343718763 |
| 16,000,000 | 0.000235077738 | 0.00389949286 |

The normalizations are recorded for reproducibility, not used to fit a power or logarithmic exponent. A bounded ratio at three finite values supplies no uniform estimate. Its magnitude also depends on the declared fixed profiles and block width.

## 4. Coherent-vector checks, without changing the matrix

The table gives squared Euclidean projection of the unit top eigenvector onto each normalized vector or declared subspace. The smooth subspace consists of the constant and sine/cosine modes of frequencies 1 through 4 on the proportional row coordinate. The arithmetic subspace is spanned by all residue indicators modulo 3, 5 and 7; its numerical rank is 13. These spaces were chosen before the experiment and were never subtracted from the matrix.

| X | Constant | log d | Centered log d | μ(d) | Smooth 9-dimensional space | Residues mod 3,5,7 |
|---:|---:|---:|---:|---:|---:|---:|
| 1,000,000 | 0.000211723 | 0.000211648 | 0.0000000311 | 0.000469250 | 0.00204311 | 0.169172 |
| 4,000,000 | 0.000108828 | 0.000107726 | 0.0000318139 | 0.000753525 | 0.00401363 | 0.0771862 |
| 16,000,000 | 0.00106876 | 0.00111417 | 0.00648687 | 0.000612397 | 0.00993281 | 0.0187872 |

The constant and uncentered log vectors are nearly parallel on the narrow proportional block, which is why both are supplemented by centered log. The declared smooth space captures less than one percent of the top-vector squared mass in each case. The small-modulus arithmetic projection is appreciable in the first case, but it is not a dominant projection, and the later two values do not reveal a persistent dominant mode in that same space. These initial checks do not test rapidly oscillating Mellin modes; the requested follow-up below addresses that separate question.

The absolute constant-vector Rayleigh quotient divided by the full operator norm is 0.032885, 0.088691, and 0.056079. Restricting only the **input** to the declared smooth subspace gives operator-norm ratios 0.534282, 0.543319, and 0.575913; the arithmetic-input ratios are 0.683103, 0.605439, and 0.562860. The latter numbers are not top-vector overlaps: they optimize over the specified input space and may collect contributions from many singular modes. Neither statistic uses a mode-subtracted target.

### Requested Mellin-template follow-up on the same saved arrays

After the initial results, the coordinator requested this additional check before freeze. Its exact grid was recorded in `MELLIN_FOLLOWUP_PLAN.md` before calculation. No prime coefficients or matrices were recomputed. For a dimension-n case, exactly 4n uniformly spaced frequencies, including zero, run through
\[
t_{\max}=\frac\pi{\min_j(\log d_{j+1}-\log d_j)}.
\tag{3a}
\]
This reaches the largest **local** Nyquist scale; nonuniform log samples do not have a unique global alias-free Nyquist frequency. The minimum-local and average-spacing versions are also recorded in `mellin_results.json`.

At each frequency, the top vector is projected onto
\(\operatorname{span}\{\cos(t\log d),\sin(t\log d)\}\).
The implementation uses the equivalent rotated basis in \(\log(d/d_{\rm mid})\) to avoid unnecessarily large phases. The full two-by-two Gram inverse is used, and zero frequency is treated as the one-dimensional constant span. The winning projection is checked independently by QR.

| X | Frequencies | Largest tested t | Winning t | Winning t/T | Maximum squared projection |
|---:|---:|---:|---:|---:|---:|
| 1,000,000 | 600 | 2117.433060 | 1756.868499 | 1.75686850 | 0.131635577 |
| 4,000,000 | 1200 | 4238.008296 | 3046.841660 | 1.52342083 | 0.122876204 |
| 16,000,000 | 2400 | 8479.158475 | 4760.911407 | 1.19022785 | 0.057238142 |

The frequency spacings are approximately 3.535. Every positive-frequency Gram matrix passes the rank check. Left and right squared projections agree exactly in the stored floating calculation, as expected from symmetry and the sign relation for its singular vectors. The winning Gram and QR values agree within \(2\cdot10^{-16}\).

This reveals some high-frequency template overlap that the original low modes missed. It does not exhibit a dominant single tested Mellin span. It also does not optimize over continuous frequency, rule out log-dependent amplitude envelopes or combinations of several modes, prove an aliasing statement, or give an asymptotic operator lower bound. All frequencies, left/right projection arrays and Gram entries are saved in `arrays/mellin_X.npz`; no selected mode is removed from C.

## 5. The actual fixed Möbius/log contraction

Let \(a_d=\mu(d)\) and \(b_k=\log k\), with no centering of either vector. The exact block normalization from R27 is
\[
Z_{D,K}=\frac{2}{X\ell^2}a^{\mathsf T}Cb,
\qquad
|Z_{D,K}|\le\frac{2}{X\ell^2}\|a\|_2\|C\|_{\rm op}\|b\|_2.
\tag{4}
\]

| X | Actual normalized block contraction | Normalized operator Cauchy bound | Signed fraction of that bound |
|---:|---:|---:|---:|
| 1,000,000 | −0.000424820654 | 0.00883086935 | −0.0481063 |
| 4,000,000 | −0.000634172575 | 0.00829505977 | −0.0764518 |
| 16,000,000 | −0.000446876958 | 0.00845040204 | −0.0528823 |

The fixed contraction is about 4.8%–7.6% of its operator bound in magnitude. It therefore benefits from vector-specific cancellation on this grid. This does not mean that its asymptotic order is smaller, and these three negative values do not estimate the sign of the full \(\mathcal Z_T\). The full target includes all other balanced blocks, unbalanced cofactors, physical shift scales, and height blocks.

The leading eigenmode alone contributes signed fractions −0.006551, +0.003727, and −0.015620 of the full contraction. Thus the recorded fixed contraction is not produced predominantly by the single top mode either. Opposing signs and the rest of the spectrum remain in the original sum.

## 6. Numerical implementation and verification

The actual integral for the prefactor is evaluated after the exact substitution \(r=-(T-1)\log(x/m)\):
\[
X\ell^2b_T(m)=\frac Xm\frac T{T-1}
\int_0^\infty e^{-r}
\omega\!\left(\frac{\log m}{\ell}-\frac{r}{(T-1)\ell}\right)dr.
\tag{5}
\]
No approximation \(b_T(m)=\omega(\log m/\ell)/(m\ell^2)\) is substituted. The production prefactor uses 64-node Gauss–Laguerre quadrature and the 16,385-node autocorrelation table calculated with 256-node Gauss–Legendre quadrature. Every required product is compared with 32 Laguerre nodes and an 8193-node table with 128 inner nodes. Tables, inner quadrature nodes and weights, and both product prefactors are retained.

The finite shift sum uses the exact floating expression `exp(-T*log1p(h/m))`, including every nonzero even shift. Selected entries are independently recomputed with Python `math.fsum`, direct autocorrelation quadrature, and adaptive integration in \(r\) over \([0,48]\). Since \(0\le\omega\le1\), the omitted transformed integral is mathematically at most \(e^{-48}\), times the prefactor in (5). This tail bound does **not** turn the other floating quadratures into an interval certificate.

All checks passed:

* Prime/power/composite fixtures include Λ(4)=Λ(8)=log 2, Λ(9)=Λ(27)=log 3, Λ(25)=Λ(125)=log 5, and Λ(6)=Λ(45)=0.
* Every row, product, shift and endpoint mask is checked. Every matrix is bitwise symmetric.
* Across all required products, the maximum relative 32/64 quadrature difference is at most \(1.43\cdot10^{-15}\). The corresponding raw-matrix Frobenius differences are approximately \(2.49\cdot10^{-13}\), \(7.33\cdot10^{-13}\), and \(8.79\cdot10^{-12}\).
* Twenty-seven predetermined entry checks have maximum absolute discrepancy \(1.78\cdot10^{-14}\). The adaptive integrator reports errors up to about \(2\cdot10^{-12}\); these are numerical diagnostics, not outward enclosures.
* The top-eight eigen-residual divided by Frobenius norm is below \(6.5\cdot10^{-16}\). The Frobenius/eigenvalue sum-of-squares discrepancy is below \(4\cdot10^{-16}\) relatively.
* The Möbius/log contraction agrees with an independently grouped product-index contraction to relative error below \(6\cdot10^{-16}\).

The exact assertions, tolerances and observed discrepancies are in `run_matrix_test.py` and `results.json`. Floating summation and quadrature remain limitations even when these comparisons agree near machine precision.

## 7. Reproduction, resource record and limits

Run from any directory with the existing NumPy/SciPy environment:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 '/Users/qingyunsun/Library/CloudStorage/Dropbox/Research/ACUE-Astra-Handoff-2026-09-04/research-round28/actual-prime-matrix-test/run_matrix_test.py'
```

Then run the adjacent `check_mellin_templates.py` with the same environment for the saved-array follow-up. It reads the three matrices rather than computing primes again. Its stdout is retained in `mellin_run.log`.

The retained execution used Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1 on macOS arm64, with the three thread variables set to one. Full stdout is `run.log`. The three measured case times were 0.131, 0.561 and 3.428 seconds; total reported time, including setup and sparse coefficient storage, was 5.336 seconds. These are one-run resource observations, not a performance benchmark. The predeclared omission rule was never triggered. Retained data and code occupied about 32.8 MB before the final report/receipts. Peak resident memory was not measured; the largest dense Lambda array alone occupies about 233 MB, with chunked work arrays in addition.

The source and artifact receipts bind the predeclared plan, implementation, actual outputs, three raw matrices, coefficient tables and source definitions. The one explicitly labelled follow-up scans only the requested fixed Mellin-frequency grids on existing arrays. There was no profile or block optimization, new prime height, random replacement, or empirical mode removal.

The result leaves both mathematical options open. An operator theorem remains unproved, but this finite test did not identify the proposed coherent-mode reason to abandon it. A bound using the fixed Möbius/log vectors can exploit more structure than a uniform operator bound; the observed additional cancellation is a property of these three finite arrays only. The next mathematical input still has to estimate the genuine centered affine-prime Gram correlations, or the fixed signed contraction, in the required uniform asymptotic range.
