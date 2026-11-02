# A direct k=39 cap-only trial with the published physical geometry

2026-09-05. **Exploratory numerical result; no interval certificate, support-restored criterion, or new prime-gap bound.**

**Completed finite-family optimization:** after optimizing all 77 polynomial coefficients at the same frozen geometry, the best directly re-evaluated \(k=39\) candidate has cap quotient approximately **0.99439639936**, still **0.00560360064** below one. The full scaled Gram condition number is \(2.28\times10^{10}\); the matrix and direct scalar evaluations agree within \(1.74\times10^{-10}\). This is numerical evidence about the fixed family, not a certified upper bound. The corresponding \(k=40\) optimized positive control is approximately **1.00021374364**. Details and the retained-dimension checks are below.

The complete published 77-coefficient rational polynomial, evaluated in **39 outer coordinates and 38 retained coordinates** with the original physical radii, fragment caps and 98,304-cell grid, gives
\[
\frac{\rho_*J_{\rm cap}}I=0.994361581476018.
\]
The cap-only shortfall is approximately **0.005638418524**, or **5,638 parts per million**. This is a concrete fixed-trial deficit, not a bound on all 77-dimensional coefficients.

The independent \(k=40\) control gives
\[
\rho_*J_{\rm cap}/I=1.000206086776951,\qquad
I=2.36853178533315\times10^{-14},
\]
with \(I\) inside the published interval
\[
[2.3685317816,\;2.3685317890]\times10^{-14}.
\]
The published cap quotient lower endpoint is \(1.0002060794024186\ldots\), consistent with the independent value. No official FLINT check was bypassed; the program does not import FLINT or execute the official certificate.

## Fixed input and dimension changes

Source: [OpenAI PrimeGaps186, commit 61340d0b74163003b32756bb16e91d9209a5e330](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330), especially the companion numerical paper §§1.1–1.2 and the two literal coefficient tables in the certificate.

The source script SHA256 is **7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4**. Only its literal signatures and integer coefficients are parsed as data. The exploratory implementation independently reconstructs the rational ladder and cap geometry.

The parameters retained are
\[
\rho_*=\frac{2624989}{10^7},\quad
S=\frac{2742997}{2624989},\quad
T_0=\frac{2499106033}{2624989000},\quad
T_1=\frac{2510000}{2624989}.
\]
Thus the physical outer/base/enlarged radii remain \(0.2742997\), \(0.2499106033\), \(0.251\). The fragment-cap indices at the official mesh remain
\[
35265,\ 35419,\ 44781,\ 44976,\ 46580,\ 49152,\ 68225.
\]
These are fragment caps; coordinate totals above a cap are retained with their Dickman density.

For \(k=39\), the convolution length is \(98304-39=98265\), outer cell assignment uses \((r+39)h\), the retained-face assignment uses \((r+38)h\), and the radial midpoint is \((r+39/2)h\). The erased-coordinate normalization is **\(39h/Z\)**, not \(40h/Z\). Moment falling factorials use 39 or 38 as appropriate. No \(k=40\) denominator, source-loss bound or alpha estimate is inherited.

The fixed profile is
\[
g(t)=\frac{21/200}{1+t/100}+\frac{179/200}{1+(907/5)t},
\]
and the polynomial is the published rational linear combination of
\[
(s-9/10)^d P_\sigma(t),\quad0\le d\le6,\quad
\sigma\in\{\varnothing,2,3,4,5,6,22,23,24,33,222\}.
\]
The same outer trial is used in every face form.

## Independent numerical method

Conditional on a largest-fragment cap \(z\), the total-size measure is \(\rho_D(t/z)\,dt\). All needed arguments satisfy \(t/z<3\). The implementation uses
\[
\rho_D(x)=1\ (x\le1),\qquad \rho_D(x)=1-\log x\ (1<x\le2),
\]
\[
\rho_D(x)=1-\log x+\log(x-1)\log x+\operatorname{Li}_2(1-x)+\pi^2/12
\quad(2<x\le3).
\]
Eight-point Gauss integration computes each cell mass. The rational midpoint profile and polynomial are constant within each cell, as in the official trial.

Power-sum products are reduced by set partitions to convolutions of coordinate measures with monomial weights. Erasing a coordinate uses the exact expansion
\[
P_\sigma(t_1,\ldots,t_{k-1},u)
=\prod_{q\in\sigma}(P_q(t_1,\ldots,t_{k-1})+u^q).
\]
The two erased-coordinate copies are integrated independently before squaring and integrating the retained configuration. Nested fragment-cap layers are handled by differences of the corresponding retained-coordinate moments.

An explicit exponential change of numerical normalization prevents the extremely small original denominator from being swamped by FFT roundoff. Put
\[
Z_\tau=\sum_jg(t_j)^2e^{-\tau t_j},\qquad
w_j=\frac{g(t_j)^2e^{-\tau t_j}}{Z_\tau}.
\]
Every denominator contraction restores \(e^{\tau s}\); every retained-face contraction restores \(e^{\tau s_{\rm face}}\), with normalization \(kh/Z_\tau\). The erased fiber still uses the original \(g\). Thus the trial and geometry are unchanged. To return to the published normalization multiply every form by \((Z_\tau/Z_0)^k\), which cancels from the quotient.

The code requests NumPy longdouble but records the actual dtype. On this macOS runtime it is **float64**, so no extra-precision claim is made.

## Completed values

| \(k\) | cells | tilt \(\tau\) | \(\rho_*J/I\) |
|---:|---:|---:|---:|
| 40 | 4,096 | 20 | 0.995271191907594 |
| 40 | 16,384 | 20 | 0.999149113371267 |
| 40 | 98,304 | 20 | 1.000206086776951 |
| 39 | 16,384 | 20 | 0.993352220411709 |
| 39 | 98,304 | 20 | 0.994361581476018 |
| 39 | 98,304 | 25 | 0.994361581476014 |

Coarse rows change the step grid and its inward rounding; they are diagnostics, not the official fixed-grid certificate. The final two \(k=39\) rows retain the official grid and differ only in an algebraically cancelling numerical normalization. Their difference is \(4.22\times10^{-15}\).

At \(k=39,N=98304,\tau=20\), the separated face values are
\[
J_0/I=3.780455375344233,\quad
J_+/I=0.007728822713122185,\quad
J_t/I=0.06588020236568319.
\]
The signed cap form uses the published minorant parameters
\[
\text{mass}=49999/50000,\quad K=17/50,\quad\lambda=1/125,
\]
\[
a=\text{mass}^2-\text{mass}\lambda,\qquad
b=(1-\text{mass}/\lambda)(1-\text{mass})K,
\qquad J_{\rm cap}=J_0+(a+b)J_++bJ_t.
\]
The ratio of absolute contraction sums to the final denominator is about 183; the corresponding ratios for the face pieces are about 93, 530 and 1033. These measure cancellation in the chosen representation, not rigorous error bounds.

## Interpretation and earliest proof debt

The fixed \(k=39\) profile requires a change on the order of \(0.00564\) in the normalized criterion before it reaches one. The currently demonstrated \(k=40\) alpha-credit region is on the order of ten parts per million, roughly hundreds of times smaller. That comparison is a scale diagnostic only: a \(k=40\) alpha estimate is not a \(k=39\) bound, and a lower bound for one alpha region is not an upper bound for all possible alpha credit.

The remaining obligations are:

1. A genuine outward enclosure for this \(k=39\) cap form; current quadrature and FFT arithmetic are floating.
2. Separate treatment of the actual \(k=39\) rootwise support predicates and all restoration terms, including any credit attached to removal of failed outer roots.
3. An optimization or certified upper bound for the finite polynomial family before interpreting this fixed-vector deficit as a family-wide limitation.
4. The complete arithmetic sieve criterion, rather than a cap-only inequality, before any DHL[39,2] or prime-gap conclusion.

No restored \(k=39\) margin is asserted. Even a positive optimized cap-only quotient would not prove DHL[39,2].

## Files and reproduction

- **cap_trial.py**: independently implemented cap-only computation; only coefficient literals are read from the preserved official clone.
- **k39_n98304_tilt20_longdouble.json**, **k39_n98304_tilt25_longdouble.json**: final fixed-grid \(k=39\) trials. Despite the requested-type filename, each JSON records the actual dtype as float64.
- **k40_n98304_tilt20_longdouble.json**: official-grid positive control.
- Other JSON files: coarse-grid diagnostics.
- **official_numerics.txt**: local pdftotext extraction of the unchanged official companion PDF, for equation review.

Run:

    OPENBLAS_NUM_THREADS=1 python3 cap_trial.py --k 39 --intervals 98304 --tilt 20

The official-grid fixed-vector run took about 10.5 seconds in the observed concurrent run; this is a local observation, not a general performance claim.

## Completed 77-dimensional optimization at frozen geometry

**optimize_cap.py** assembles the denominator Gram \(G\) and the numerator matrix \(B=\rho_*J_{\rm cap}\) directly, without searching coefficients during integration. All coefficients vary in the same 77-dimensional polynomial space; the physical support and coordinate profile \(g\) remain frozen.

For the denominator, entries with the same joined power-sum signature and summed radial degree share one moment contraction. For the numerator, the exact erased-coordinate expansion expresses each basis function as a finite sum of retained power-sum signatures times one-dimensional fiber kernels. Weighted matrix products assemble their shared retained-coordinate integrals. This is a different contraction order from evaluating one fixed coefficient vector.

The matrices are diagonally scaled by \(\sqrt{G_{ii}}\). Three relative eigenvalue thresholds are applied to the scaled Gram before whitening: \(10^{-8},10^{-10},10^{-12}\). At the last threshold all 77 dimensions survive. Each resulting candidate is then passed to the separate scalar-form implementation in **cap_trial.py**.

At \(N=98304\), the results are:

| \(k\) | retained dimension | scaled Gram condition | matrix quotient | direct candidate quotient |
|---:|---:|---:|---:|---:|
| 39 | 62 | \(9.01\times10^7\) | 0.994371194303 | 0.994371194271 |
| 39 | 75 | \(3.65\times10^9\) | 0.994396034484 | 0.994396034594 |
| 39 | 77 | \(2.28\times10^{10}\) | 0.994396399191 | 0.994396399364 |
| 40 | 62 | \(9.49\times10^7\) | 1.000188112833 | 1.000188112844 |
| 40 | 75 | \(3.86\times10^9\) | 1.000213094616 | 1.000213094394 |
| 40 | 77 | \(2.42\times10^{10}\) | 1.000213743635 | 1.000213743640 |

For \(k=39\), the scaled Gram eigenvalues range from \(2.30246\times10^{-9}\) to \(52.4410\). The full-dimensional projected eigen-residual is \(1.24\times10^{-12}\); the residual of the scaled generalized pencil, divided by the documented matrix-norm bound, is \(7.36\times10^{-17}\). These residuals concern the assembled numerical matrices, not unknown integration errors.

The separate scalar evaluation of the 77-dimensional candidate has an absolute denominator-contraction ratio around 368 and face-contraction ratios around 180, 1194 and 1805. It differs from the matrix quotient by \(1.74\times10^{-10}\), far below the observed shortfall of \(0.00560\), but this discrepancy is not itself a rigorous error enclosure.

The optimization recovers only approximately **34.82 parts per million** relative to the published coefficients transplanted to \(k=39\). It leaves approximately **5603.60 parts per million** of cap-only shortfall. The 75-to-77-dimensional change is under one part per million. On this frozen geometry the existing polynomial coefficients are numerically close to the best found value.

The \(k=40\) control is positive in every retained subspace, and the full-family optimization improves its existing cap value by approximately 7.66 parts per million. Thus the experiment is not globally misnormalized so that every trial fails.

The complete matrix-plus-three-validation run took about 58 seconds for each dimension in the observed concurrent run. Files:

- **optimize_cap.py**
- **ritz_k39_n98304.json**, **ritz_k39_n98304.npz**
- **ritz_k40_n98304.json**, **ritz_k40_n98304.npz**
- **ritz_k39_n16384.json**, **ritz_k39_n16384.npz**: initial coarse-grid assembly check.

The JSON retains floating coefficient vectors, all scaled Gram eigenvalues, thresholds, residuals and direct candidate evaluations. The NPZ retains the raw denominator and numerator matrices and original coefficient vector.

Reproduce:

    OPENBLAS_NUM_THREADS=1 python3 optimize_cap.py --k 39 --intervals 98304 --validate

## Structural checks and next decision

**check_structure.py** checks the set-partition moment expansion against exhaustive three-coordinate summation on a four-point measure, and checks the erased-coordinate polynomial identity for all 11 signatures. Errors are below \(3\times10^{-17}\). It also verifies the exact \(k=40\) cap-index ranges against the companion paper's table and compares the closed Dickman expression at \(3\) against an independent integral. Results are in **structural_check_results.json**.

The official clone's git status remains clean. No official certificate code, dependency or assertion was modified. All three local scripts pass Python compilation.

The appropriate next mathematical decision is to stop repeated scans of these 77 coefficients at the frozen geometry. A rigorous finite-family upper bound would require outward enclosures for the two matrices and a certified positive-definiteness test for \(cG-B\), for some explicit \(c<1\), after a numerically suitable basis change. The current float64 matrices and eigensolver output do not supply that certificate.

A different radius/owner-support allocation may change the cap form substantially. Such a proposal must recompute its source-dependent caps and support restoration; it cannot simply retain the current cap arrays while changing \(S\) or \(T\). No radius scan or new support claim is included here.
