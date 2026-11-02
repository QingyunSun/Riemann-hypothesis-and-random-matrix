# Predeclared actual prime-window matrix diagnostic

Date: 2026-09-05. This plan is written before implementing or running the experiment. Numerical evidence only; no symbolic, interval, RH, or asymptotic certification is intended.

## Concept layer

Test the actual R27 matrix from Euclid's `joint-dispersion-test/JOINT_DISPERSION_TEST.md`, Sections 3–4, read in full. Set X=T², Y=T, ell=log T and

    C[d,k] = X ell² b_T(dk) chi(dk/X)
             sum_{h even} V(h/T) (1+h/(dk))^(-T) (Lambda(dk+h)-2).

Use the actual R16 seed f(x)=exp(-1/(1-4x²)) on |x|<1/2, its normalized autocorrelation psi, and omega(u)=psi(4(u-2)). The b_T integral is unchanged. Lambda includes all prime powers. The center is exactly 2 on odd endpoints. No empirical recentering or mode subtraction is permitted.

The fixed profiles are chi(t)=V(t)=exp(1-1/(1-((t-1.5)/0.45)²)) on |t-1.5|<0.45, and zero elsewhere. These are fixed smooth functions with maximum one. The square uses every odd integer d,k in (1.05 T,1.35 T]. Products lie strictly inside (X,2X) and inside the positive chi region.

Predeclared X values: 1,000,000; 4,000,000; 16,000,000. Their T values are 1000, 2000, 4000; matrix dimensions are 150, 300, 600. There is no random seed and no randomized linear algebra. If the first two completed cases imply more than ten minutes for the third, or memory exceeds about 1 GiB, omit the third with an explicit resource note. Do not replace any case by an adaptively selected prime location.

Measure the operator norm, Frobenius norm, complete signed eigenvalues, fixed mu/log contraction with its exact prefactor 2/(X ell²), and its fraction of the Cauchy operator bound. Report top-vector squared overlaps with constant, log, centered log, and Mobius vectors. Also predeclare two small test subspaces: trigonometric modes 1, cos(2 pi j t), sin(2 pi j t), j=1..4 on the fixed row coordinate; and residue indicators modulo 3,5,7. These are overlap diagnostics only. They are not subtracted from C. Report the top singular-value energy fraction and gap, rather than calling any overlap 'dominance' without its magnitude.

## System layer

One Python script uses existing NumPy/SciPy; no packages are installed and no Rust module is needed. A sieve creates the genuine finite Lambda array through the largest used endpoint. Only distinct products need window evaluation; all multiplicities are restored in C. Chunked direct sums over the complete even shift set avoid large temporary arrays. Symmetry permits deterministic symmetric eigendecomposition; singular values are absolute eigenvalues, with the sign relating left/right vectors retained.

The stable exact transformation for b_T is

    X ell² b_T(m) = (X/m) T/(T-1)
      integral_0^infinity exp(-r)
      omega(log(m)/ell - r/((T-1)ell)) dr.

Evaluate psi by Gauss–Legendre quadrature plus a recorded spline table; evaluate this integral by Gauss–Laguerre quadrature. Compare 32/64 outer nodes and 8193/16385 psi table sizes with 128/256 inner nodes on every required product. On fixed representative products, independently compare with adaptive integration using direct autocorrelation quadrature. These comparisons are floating convergence checks, not certified error enclosures.

## Code layer

Create `run_matrix_test.py`, `RESULTS.md`, `results.json`, the full stdout log, and `arrays/` containing each raw matrix, row integers, unique products, window sums, b prefactors, Mobius/log vectors, eigenvalues/eigenvectors, and the sparse genuine Lambda coefficient list used. Save all profile/quadrature tables and the software/platform versions. Hash sources, scripts, outputs and arrays in a receipt.

Verification: check selected Lambda prime/power/composite values; all product and even-shift endpoint masks; exact matrix symmetry; finite direct-sum agreement at nine predetermined entries per case; b quadrature convergence; Frobenius/eigenvalue identity; eigen-residuals; and the bilinear form computed both as matrix multiplication and grouped product contraction. All numerical tolerances are recorded with actual discrepancies. If a check fails, investigate it before interpreting norms.

No performance claim is being made. Record timings and storage to make the bounded resource decision auditable. The acceptance criterion is a reproducible faithful matrix and a candid answer about this finite operator strategy, not a small value of the target.

## Postpone

No new heights beyond the three declared values; no profile, block-width, residue, or frequency optimization; no fake ensembles; no fitted asymptotic exponent; no mode-subtracted matrix; no inference from finite data to RH, AH, or an operator theorem; no Git, publication, external model API, package installation or PDF work.
