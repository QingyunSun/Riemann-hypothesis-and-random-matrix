# Round 8: isolate the actual arithmetic remainder

The two-scale target from [Round 7](dyson_round7.md) can be written as a computable short-prime main term plus one signed difference of residual energies. The residuals have an exact convergent representation using the same centered prime-counting error. This round proves that decomposition under RH and identifies why two tempting lower-bound arguments fail. **It does not prove the required residual inequality or refute AH-Pairs.**

## 1. A short-prime projection identity for actual zeta

Fix c>0 and put

\[
N=\left\lfloor\frac{T}{\log^6T}\right\rfloor,
\quad s_c(t)=\frac12+\frac c{\log T}+it,
\quad H_c(t)=-\frac{\zeta'}{\zeta}(s_c(t)),
\]
\[
P_c(t)=\sum_{n\le N}\Lambda(n)n^{-s_c(t)},
\qquad R_c(t)=H_c(t)-P_c(t).
\]

The [ordinary analytic proof](../dyson/round8/resolvent-arithmetic/SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md) establishes, under RH,

\[
\int_0^T|H_c(t)|^2dt
=T\sum_{n\le N}\frac{\Lambda(n)^2}{n^{1+2c/\log T}}
+\|R_c\|_{L^2(0,T)}^2+O_c(N\log^4T).
\tag{1}
\]

The mixed product is evaluated by a contour shift to the absolutely convergent Dirichlet-series half-plane. The contour avoids the pole at one; RH controls the shrinking horizontal distance from the zeros. The infinite right-line off-diagonal sum, the top edge and the initially removed short interval all receive explicit bounds. A finite-polynomial mean-value estimate and completion of the square give (1). Exact finite-height orthogonality is not assumed.

An [independent audit](../dyson/round8/resolvent-arithmetic/INDEPENDENT_IDENTITY_AUDIT.md) checks the contour orientation, diagonal coefficient, near-diagonal summation, infinite tail, T-dependent error and continuation signs. No novelty claim or proof-assistant certification accompanies this ordinary reduction.

## 2. The precise remaining inequality

For the Round 7 statistic

\[
W_T=\frac{2}{T\log^2T}
\left[\sinh(2)\|H_1\|_2^2-\sinh(1)\|H_{1/2}\|_2^2\right],
\]

(1) and PNT imply

\[
W_T=B+\mathcal E_T+o(1),
\quad B=2\int_0^1u[\sinh(2)e^{-2u}-\sinh(1)e^{-u}]du
=0.4560939793292317\ldots,
\]
\[
\mathcal E_T=\frac{2}{T\log^2T}
\left[\sinh(2)\|R_1\|_2^2-\sinh(1)\|R_{1/2}\|_2^2\right].
\]

Thus the sufficient AH-refutation target is precisely

\[
\boxed{\liminf_{T\to\infty}\mathcal E_T\ge\frac1{16}-B
=-0.3935939793292317\ldots.}
\tag{2}
\]

The positive short-prime main term does not prove (2). The residual combination is signed and of leading order. The sine prediction would make it about -0.3738225362077544, but that value has not been obtained for actual zeta.

## 3. The two residuals come from the same arithmetic function

Set E(x)=psi(x)-x with psi(N) including the atom at N. For Re(s)>1/2, s≠1, RH gives the exact identity

\[
-\frac{\zeta'}{\zeta}(s)-\sum_{n\le N}\Lambda(n)n^{-s}
=\frac{N^{1-s}}{s-1}-E(N)N^{-s}
+s\int_N^\infty E(x)x^{-s-1}dx.
\tag{3}
\]

The integral converges absolutely under RH. The formula is obtained in the original convergence half-plane and then continued; no unregularized critical-strip prime series is used. The pole and endpoint subtraction have fixed signs.

At the chosen cutoff, the pole term can be removed from the normalized residual energy using its L2 estimate and the pointwise RH bound already proved in the same argument. The normalized cross-term error is O_c(log^-3 T); the decomposition needs no stronger pair-correlation input. Writing e_N(v)=E(Ne^v)/(Ne^v)^(1/2), the remaining residual is

\[
N^{-c/\log T-it}\left[-e_N(0)+s_c(t)
\int_0^\infty e_N(v)e^{-(c/\log T)v-itv}dv\right].
\]

The two damping widths therefore act on one actual arithmetic function. This coupling is a concrete structure for the next estimate. Replacing the two energies by independent nonnegative variables loses that structure; assuming it forces (2) without a proof would also be an error.

Using only |E(x)|≪sqrt(x) log²(x) and absolute values gives a residual bound of order T log³(T) for a power-of-T cutoff. Its squared integral is far too large. This is a documented failure of that particular estimate, not a proof that RH or all analytic approaches are insufficient.

## 4. Positivity gives a valid weak bound, but cannot reach the target

The [bounded positivity note](../dyson/round8/spectral-positivity/POSITIVITY_OBLIGATION_NOTE.md) gives an explicit band-limited minorant, using the known interior Montgomery band and positivity of the pair measure. Its resulting exact expression is approximately -0.208674513 for W, far below 1/16. The minorant is optimal only within the one-parameter correction family written there. Its [independent review](../dyson/round8/spectral-positivity/MINORANT_REVIEW.md) checks the Fourier support, endpoint pairing and realizable point-process obstruction.

The decisive obstruction remains the actual stationary half-grid determinantal process. It matches the known low band, satisfies the stated point-process positivity constraints, and attains W_AH<1/16. Thus neither generic positivity nor merely changing two smoothing widths supplies the required arithmetic input. The frequency weight changes sign above log(2 cosh 1); even a one-term positive-coefficient polynomial disproves a universal positive-coefficient quadratic-form claim.

## 5. Verification and next scope

The accompanying checks verify exact scalar enclosures, a finite-step integration-by-parts identity and an absolutely convergent comparison with zeta'/zeta. Low-height regularized-prime sums are explicitly labeled diagnostics. They are not evaluations of the large-T target, and no convergence rate in the critical strip is inferred from them. Intake hashes and an isolated integration replay preserve the received evidence.

The next mathematical obligation is (2), exploiting the common centered prime error in (3), or the alternative compact prime-covariance target in Round 7. Repeating a positive-coefficient argument, dropping the pole before bounding its cross term, and scanning generic random-matrix models are postponed. The famous conjecture remains open in this programme.
