# Round 5: bounded radius and plateau search at k = 39

**Status:** completed exploratory cap-only search. Ten configurations were screened at 16,384 intervals; only two were refined at the published 98,304 intervals. Every configuration reassembled and optimized all 77 polynomial coefficients. No improved cap candidate was found from the radius/plateau changes. No support-restored certificate, DHL(39,2), smaller prime gap, or global variational upper bound is asserted.

The best original-geometry Round 4 value remains `0.9943963993644909`. At the fine grid, the two nearby Round 5 geometry choices gave `0.9943734016224463` and `0.9943501891039260`. Their deficits from one remain about 5,627 and 5,650 parts per million. This is substantially larger than the approximately 1.5 ppm rigorously recovered alpha credit in Round 4.

## 1. Exact scope and objects

The starting point is the official [PrimeGaps186 repository](https://github.com/openai/PrimeGaps186), pinned in our preserved clone to `61340d0b74163003b32756bb16e91d9209a5e330`. The independent engine reads only the two literal coefficient tables from `prime_gap_186_certificate.py`; it neither imports nor changes the official runtime. The source SHA256 is `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`.

We vary the physical outer radius r while imposing the exact constraints

    rho = 0.262499, rho_star = 0.2624989,
    S = r / rho_star,
    T1 = (0.5252997 - r) / rho_star,
    T0 = 1.997 - S.

Thus both `rho_star*(S+T1)=0.5252997` and `S+T0=1.997` are fixed. The radial sums governing the two distribution ladders stay fixed, so the nominal omega/delta ladder values remain unchanged. The actual mesh, all radial masks, cap indices, Gram matrices, erased-coordinate integrals and optimized vectors are recomputed for each configuration. In particular, an invariant nominal ladder does not imply an invariant retained-row list or support-repair schedule.

The trial retains the published product weight g and the 77-dimensional polynomial span: eleven symmetric signatures, each multiplied by radial powers zero through six about 0.9. It changes neither k=39 nor the analytic structure of that finite span. The success criterion for this bounded search was a material increase of the fine-grid cap quotient toward one, followed by a separately valid support-repair calculation. The first criterion was not met.

## 2. Plateau geometry and a reduced parameter choice

Write `epsilon=10^-7/rho`, `A=S+epsilon/2` and `Cnu=Tnu+epsilon/2`. For a source with plateau height L, the core decomposition is

    phi_D(u) = min(3u/2, L),
    phi_E(u) = 3u - phi_D(u).

In the tested regime A>C1>C0, the active largest-tail conditions allow

    (3A-Cnu)/4 <= Lnu <= 3Cnu/5.

The additional 5/2 tail-reduction guard `Lnu >= 3A/7` also holds. The corresponding final-shell caps are

    outer cap = min(A-L0, A-L1),
    old inner cap = (C0+L0)/4,
    new inner cap = (C1+L1)/4.

The old/new inner regions must be nested. The original equal fraction `Lnu=.575*Cnu` is one option. Two other useful choices share the *height* of the plateau rather than its fraction:

    common_min: L0=L1=(3A-C0)/4,
    common_max: L0=L1=.6*C0.

Both preserve the required interval for each source and give nested inner caps automatically. Equal heights avoid spending extra outer-cap width merely because the new source has larger C1. This exact geometric simplification is valid even though the numerical search did not benefit from the tested endpoints.

Every rational radius, L, L/C, frontier slack, cap, and integer shell range at both meshes is saved in `geometry_checks.json`. `validate_geometry.py` verifies the fixed sums, both plateau frontiers and guards, and actual old/new/full mask nesting on all twenty configuration/grid pairs. These checks are necessary structural checks; the separate source-geometry audit supplies the remaining distribution and repair constraints.

## 3. Exceptional square constant must change with physical radius

The original exceptional-square statement uses radius at most 11/40 and the convenient bound K=17/50. It is incorrect to reuse that constant at r=.276 or .278 without a new calculation.

The independent exact rational computation in `../exceptional-radius/certify_exceptional_radius.py` repeats the original 1,024-bin, 21-term alternating-logarithm upper certificate. It reproduces the published baseline rational sum exactly and gives safe rounded-up constants:

| r | K used here | certified upper bound, approximately |
|---|---:|---:|
| .272 | .301405 | .301404153485181623 |
| .2742997 | .327323 | .327322538111366366 |
| .275 | .34 | .336133604027290568 |
| .276 | .349580 | .349579996894903756 |
| .278 | .380026 | .380025921565620058 |

The `.275` trial intentionally retains the still-valid conservative `.34`; the exact calculation would also allow `.336134`. The original-geometry baseline likewise retains `.34` to check agreement with Round 4.

Both matrix and direct evaluation use the changed K in the signed hybrid:

    m=.99998, lambda=.008,
    a=m*m-m*lambda,
    b=(1-m/lambda)*(1-m)*K,
    Jcap=Jbase+(a+b)*Jplus+b*Jtail.

Thus higher-radius trials do not inherit an unjustified exceptional constant. Reducing K at the original radius improves the coarse optimized cap value by only about 0.6183 ppm. This calculation concerns the cap form; it is not a new fully certified prime-gap margin.

## 4. Bounded numerical results

All entries below are the direct scalar reevaluation of the optimized 77-vector. The independent matrix value, vector, conditioning, residuals, and three whitening-cutoff results are retained in each JSON file. Corresponding NPZ files hold the full Gram matrix, numerator matrix and original coefficient vector.

| tag | physical r | plateau | K | grid | rho_star Jcap/I |
| baseline | .2742997 | original | .34 | 16384 | 0.993379352892581 |
| r272_min | .272 | common_min | .301405 | 16384 | 0.992837127339583 |
| r272_original | .272 | original | .301405 | 16384 | 0.992825152057240 |
| r274_max | .2742997 | common_max | .327323 | 16384 | 0.993356576365699 |
| r274_original | .2742997 | original | .327323 | 16384 | 0.993379971225379 |
| r275_max | .275 | common_max | .34 | 16384 | 0.993324871060043 |
| r276_max | .276 | common_max | .349580 | 16384 | 0.993147338997495 |
| r276_min | .276 | common_min | .349580 | 16384 | 0.993160475207861 |
| r278_max | .278 | common_max | .380026 | 16384 | 0.992272698494233 |
| r278_min | .278 | common_min | .380026 | 16384 | 0.992274861882488 |
| r274_max | .2742997 | common_max | .327323 | 98304 | 0.994373401622446 |
| r275_max | .275 | common_max | .34 | 98304 | 0.994350189103926 |

The original-geometry coarse matrix value agrees bit for bit with the unchanged Round 4 program. Against that coarse control, the other tested radii all lose: approximately 542 ppm at .272, 54 ppm at .275, 219 ppm at .276, and 1,104 ppm at .278, using the better of the tested plateau choices at each radius.

The two most competitive nearby alternatives were refined. At the fine grid, original radius/common_max loses 22.9977 ppm relative to the Round 4 optimized original geometry; .275/common_max loses 46.2103 ppm. The ordering agrees with the coarse evidence. The search stopped at these ten configurations and two refinements. There is no extrapolation from these values to every plateau height, every radius, every product weight, or every finite family.

## 5. Numerical audit and its limits

The engine uses a positive exponential tilt of 20 in convolution weights and restores the exact balancing factors. This avoids evaluating the tiny un-tilted convolution left tail by cancellation. It is the same independent cap engine developed and checked in Round 4. `numpy.longdouble` on this host is actually 64 bits; no extra precision or outward enclosure is claimed.

Across all twelve computations:

- all 77 dimensions were retained at the smallest tested scaled-Gram cutoff;
- the maximum full scaled-Gram condition number was about 4.307e10;
- matrix versus direct candidate quotient disagreement was at most 2.884e-10;
- full scaled-pencil relative residual was at most 5.30e-16;
- the summed recorded compute time was 175.3 seconds on this host, excluding orchestration.

These checks give meaningful numerical evidence at the tens-of-ppm scale at issue, but they are not interval-arithmetic error bounds. The generalized eigenvalue is an observed numerical optimum of the assembled finite matrix. We do not label it a certified upper bound or a no-go theorem. Direct reevaluation uses a different contraction order but shares the cap model and one-dimensional moment primitives; it does not independently prove that model.

## 6. Support and source obligations discovered during this search

The following are substantive constraints, not bookkeeping details.

1. **The inner-square auxiliary source must be updated at smaller r.** At r=.272, the published omega=.0031 gives a level smaller than twice the new physical inner radius. The separate exact source audit supplies a common replacement `omega_s=.0035`, `delta_s=.025`, which passes the tested source and row-12 containment inequalities. Those source facts do not by themselves evaluate the cap's support losses.

2. **A new retained row can violate the original low-witness mesh guard.** At the fine grid, r=.272,.275,.276,.278 can retain new-ladder row 39. Its activation coordinate is about 1.886625e-5, which is less than two mesh cells for these cases. The original low-witness implementation requires at least two cells. The source theorem does not fail, but the original support-repair engine cannot be inherited unchanged.

3. **An explicit inward restriction can remove that extra row.** With `h=S/98304`, `J1=floor(T1/h)`, define

       Jo=min(98303, floor(B_new39/h)-J1).

   Restrict the outer sum of coordinate indices to `r_total <= Jo-k`. In the affected tested cases Jo=98302, one layer less than the ordinary Jo=98303; this restores the retained range 0 through 38. Keep h, nominal S, convolution length and Z fixed, but recompute every face from the trimmed F. The current reported trials are **not trimmed**. No numerical loss estimate for that modification is included here.

4. **Every schedule still needs rebuilding.** Even after trimming, actual integer thresholds, caps, source-specific masks, failure forms and outward quadrature bounds must be regenerated. The approximately 1.5 ppm alpha rectangle proved for the fixed published k40 profile cannot simply be transferred to these optimized k39 vectors or these radii.

Since none of the screened geometry changes gave a promising cap value, a full repaired certificate for these particular vectors is postponed. This is a prioritization decision based on the observed finite trials, not a proof that repair or a different profile cannot succeed.

## 7. Reproducibility and archive contents

Run from this directory:

```sh
OPENBLAS_NUM_THREADS=1 python3 validate_geometry.py
OPENBLAS_NUM_THREADS=1 python3 run_bounded_screen.py
OPENBLAS_NUM_THREADS=1 python3 run_bounded_screen.py --refine
```

Dependencies are recorded in `manifest.json`: Python, NumPy and SciPy, platform, actual long-double bit count, and SHA256 of all computation inputs and outputs. The parser's only upstream file dependency is

    ../../research-round1/prime186-work/PrimeGaps186/prime_gap_186_certificate.py

relative to this directory. That file provides the literal published coefficient signatures and integer coefficient matrix. An exported archive must preserve this relative layout or set `SOURCE` to the pinned copy. The two distribution-ladder recurrences and geometry are independently implemented in `cap_trial.py`; no FLINT module is imported and no official regression guard is disabled. The preserved upstream clone remained clean after all computations.

Files are intentionally small-purpose: `cap_trial.py` evaluates a vector; `optimize_cap.py` builds and solves the finite pencil; `validate_geometry.py` checks exact parameters and actual masks; `run_bounded_screen.py` replays the declared finite list. Ten `*.config.json` files contain every parameter choice. Each computed point has JSON evidence and a compressed NPZ matrix archive. `summary.json` is the compact comparison surface.

## 8. Conclusion for the next research step

The tested radius/plateau degrees of freedom do not erase the k39 cap deficit. The useful output is a fully recomputed negative trial, a simpler common-height plateau parameterization, a valid radius-dependent exceptional constant, and an explicit identification of the new mesh obstruction. A more serious search should change a mathematically justified larger component, such as the product profile or support geometry, or derive a certified finite-family upper bound before expending effort on full support restoration. Arbitrary radius scans and inherited k40 constants are not justified by these results.
