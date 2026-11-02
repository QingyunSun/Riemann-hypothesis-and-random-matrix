# Independent audit of the pole-annihilating actual-zeta packet

Reviewer: Aquinas (`yau_flow`), independently of author `prime186`. Date: 2026-09-05.

Status: **accepted within its stated scope; final frozen author version and independent replay checked.** The final hashes and bounded-check receipt are recorded below. This is a proof and artifact review, not evidence for a new pair-correlation bound.

The result is a legitimate linear logarithmic-derivative contour identity with a nonnegative real time weight, an explicitly signed arithmetic kernel, exact continuous-density cancellation, and a uniform but weak RH bound. It does not establish the old sharp-time two-width target or a sign for the new mixed moment.

## 1. Contour, pole and exact normalization

Write `a=1-sigma`, with `1/2 < sigma < 1`. The weight

\[
w(t)=\frac{t^2+a^2}{W^2}e^{-t^2/(2W^2)}
\]

is strictly positive for real `t` and has simple zeros at `t=+ia` and `t=-ia`. In the variable `s=sigma+it`, the pole at `s=1` corresponds to **`t=-ia`**, as the author states.

The residue of `-zeta'/zeta` at 1 is `+1`. Orienting both vertical lines upwards gives “right integral minus left integral equals `2 pi i` times the residue.” Since `ds=i dt`, the resulting formula on the left has pole term **`-2 pi X^a w(-ia)`**. This fixes both the sign and the factor `2 pi` independently of a Fourier convention guess.

Under RH, the strip from `sigma` to a fixed `beta>1` contains no nontrivial zero poles; trivial zero poles are to its left. The only possible pole is 1, which this weight cancels. The logarithmic derivative on the distant horizontal segments has a standard polynomial logarithmic bound with a constant permitted to depend on `sigma-1/2`; Gaussian decay on a fixed horizontal strip dominates it. Thus those integrals vanish for each fixed choice of the theorem's parameters.

On the right line, the Dirichlet series is absolutely convergent. With `v=beta-sigma`, shifting the entire weight from `t-iv` to the real line supplies `(n/X)^v`, cancelling the apparent factor `X^v n^{-beta}` down to exactly `n^{-sigma}`. The final Gaussian in `log(n/X)` dominates the exponential counting density of the integers for every fixed `W>0`, so its prime-power series converges absolutely. No critical-strip Dirichlet series is assumed.

The Fourier kernel follows from minus the second derivative of the Gaussian transform:

\[
K(\lambda)=\sqrt{2\pi}W
\left(1+\frac{a^2}{W^2}-W^2\lambda^2\right)
e^{-W^2\lambda^2/2}.
\]

The conjugation symmetry on the real line proves that the stated mixed moment is real.

This proof moves a contour for **one** logarithmic derivative. Moving a contour for `H(s)H(2 sigma-s)` would cross reflected zero poles at real part `2 sigma-1/2`; the present weight does not eliminate those. The authored norm identity instead uses ordinary Plancherel and has no such contour. Likewise, a simple weight zero does not automatically cancel a double pole in a derivative or squared logarithmic derivative.

## 2. Exact density cancellation and its signed cost

For `b=a/W`, `r=sqrt(1+b^2)` and `G_b(z)=(1+b^2-z^2)exp(-z^2/2)`, the substitution `y=X exp(z/W)` retains the factor `X^a exp(bz)`. The derivative identity

\[
\frac{d}{dz}\left[(z+b)e^{-z^2/2+bz}\right]
=(1+b^2-z^2)e^{-z^2/2+bz}
\]

is exact. Both endpoint values vanish. It proves the zero integral of the complete continuous density and the equality of its positive and negative masses. Evaluation at `z=+r` and `z=-r` gives exactly the author's factor

\[
2\sqrt{2\pi}X^a e^{-r^2/2}
\{r\cosh(br)+b\sinh(br)\}.
\]

The continuum Gaussian saddle is `log(y/X)=a/W^2`, not `aW^2`. Thus there is no remote exponential saddle under this time-width convention, but the negative-frequency contribution still has leading mass.

The unweighted positive mass is `2r exp(-r^2/2)+2b^2 int_0^r exp(-z^2/2) dz`; subtracting the total mass `b^2 sqrt(2 pi)` gives the negative mass. Both tend to `2 exp(-1/2)`. Restoring the Fourier scaling yields equal limiting one-sided kernel masses `2 sqrt(2 pi/e)`, with net mass only `2 pi a^2/W^2`.

Because the prime coefficients are nonnegative, removing the negative part gives an **upper** bound for the arithmetic sum. Positivity of the time weight is not positivity of each arithmetic kernel entry. The report preserves this distinction.

## 3. Centering, lower endpoint and finite-window tails

With the right-continuous prime-power counting function and `E(y)=psi(y)-y`, subtracting the entire continuous density yields `M=int_0^infty f dE`. Integration by parts gives `M=-int_0^infty E f'`. At zero, `E(y)=-y` and the logarithmic Gaussian makes `E(y)f(y)` vanish; the upper boundary vanishes as well. Absolute convergence follows from the same Gaussian decay.

If the integral begins at 1, its exact correction is `f(1)-int_0^1 f(y)dy`, since `E(1)=-1`. Both terms in the author's equation (18) have the correct signs. The interval below the first prime is not silently dropped.

**Finite-cutoff distinction:** equation (21) bounds the tails of the integrated-by-parts expression `-int E f'`. A finite centered Stieltjes sum has additional endpoint terms. For endpoints `y_minus=X exp(-R/W)` and `y_plus=X exp(R/W)` avoiding atoms, its two outside pieces equal

\[
E(y_-)f(y_-)-E(y_+)f(y_+)
-\int_{(0,y_-)\cup(y_+,\infty)}E(y)f'(y)\,dy.
\]

At atoms, the interval convention must determine the corresponding one-sided endpoint value. Thus the IBP-tail estimate alone must not be relabelled a raw prime-series-tail estimate. This does not invalidate the author's stated theorem, which identifies the particular integral whose tails are bounded.

As a check on quantitative endpoint control in the stated uniform range, the same inequalities give, for `R>=1`,

\[
|E(y_-)f(y_-)|+|E(y_+)f(y_+)|
\le 450\,W X^{1/2-\sigma}(1+\log X)^2
R^4e^{-R^2/4}.
\]

Indeed `(1+R)^2(5/4+R^2)<=9R^4`, and the remaining two-endpoint constant is `162 sqrt(2 pi) exp(1/16)<450`. This bounds precisely the additional boundary terms; it is not a new sign estimate for the prime packet.

## 4. Primary RH input and uniform constants

I checked the retained primary text and visually read printed page 337 of Lowell Schoenfeld, *Sharper bounds for the Chebyshev functions theta(x) and psi(x). II*. Theorem 10, equation (6.2), states the ordinary-RH bound for `psi(x)-x` with coefficient `1/(8 pi)` and threshold **73.2**. The theta threshold 599 is a different equation and is not used here.

Primary [AMS PDF](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), SHA-256 `8c3cac1ee52eb05af05ec410adc587a18505a46aacdde41ae097038b0e7c3897`.

For `1<=y<=74`, `psi(y)<=y log y` and `sqrt(74)<9` justify the chosen coarse global constant; for `0<y<1`, `E(y)=-y`. Hence the displayed global estimate with coefficient 9 is valid. No Dirichlet-L-function GRH is involved.

After differentiating the kernel and substituting the logarithmic variable, the expression in (22) has exactly one eventual factor `W`; there is no omitted Jacobian. In the range `1/2<sigma<=3/4`, `W>=1`, the polynomial majorant is

\[
P(z)=15/16+13z/4+3z^2/4+z^3.
\]

I independently multiplied by `(1+z)^2`. Its coefficients are `15/16, 41/8, 131/16, 23/4, 11/4, 1`. Integrating the Gaussian moments gives `(805/16)sqrt(pi)+481/4`. The rational comparison in (23) is `120784/105<1200`; multiplication by the global coefficient 9 proves **10800**.

For the tails, `P(z)(1+z)^2 <= (95/4)z^5` for `z>=1`, and

\[
\int_R^\infty z^5e^{-z^2/4}\,dz
=2(R^4+8R^2+32)e^{-R^2/4}.
\]

Including both tails leaves the prefactor `95 sqrt(2 pi) exp(1/16)<270`. Multiplying by 9 proves **2430**. The elementary rational comparisons for the square roots and exponential are in the safe direction.

For fixed `c>0`, `sigma=1/2+c/log T`, `W` comparable to `T` and `X=T^alpha` in the stated compact alpha range, `X^{1/2-sigma}=exp(-c alpha)` is retained and the bound is uniformly `O_c(T log^2 T)`. With `R=4 sqrt(log T)`, the IBP tail is `O_c(T^{-3} log^4 T)`; the finite-window endpoint terms above obey the same negligible order. These are weak absolute estimates, not a variance constant or a useful signed lower bound.

## 5. Hilbert-space identities and target-transfer limits

The finite-polynomial mixed formula and full Gram matrix have the correct conjugates and Fourier arguments. The Gram matrix is positive semidefinite because it integrates against the positive measure `w(t)dt`, despite its potentially negative off-diagonal entries. A diagonal coefficient norm cannot replace it without proof.

Writing `X=exp(lambda)`, the mixed moment is the positive-sign Fourier transform of `H_sigma(t)w(t)`. Plancherel therefore gives factor **`2 pi`** and time weight **`w^2`**, exactly as in (27). Gaussian decay makes the relevant function square-integrable; no norm contour or critical-strip prime-series expansion is needed.

The continuum comparison for a dense coefficient window has two separately equal signed masses of order `M`, while the stated diagonal component is of order `W`. Their ratio is `2 M/(sqrt(e) log(2) W)`. This is a continuum-kernel/diagonal-normalization calculation only, as the author explicitly says; it is not an asymptotic for the actual short-interval prime pieces or for the full Gram norm.

The original target uses a different sharp time cutoff and a signed difference of two sigma values. Neither this positive-weight projection nor its `w^2` energy identity transfers to that target automatically. Moreover the packet itself depends on sigma, so parameter differentiation introduces an extra derivative-of-weight term. The final manuscript retains that caution. No inequality for the old target or exclusion of the ACUE prediction is accepted from the present calculation.

No mathematical correction to the stated analytic theorems is required by this review. Acceptance concerns the linear packet identity, signed cancellation formulas, uniform absolute bounds and Hilbert-space identities, with all the limits just stated.

## 6. Final delta, script inspection and independent replay

Accepted final `POLE_ANNIHILATING_PACKET.md` SHA-256:

`3213cf34d3a5521260b48ebbeebbf12522afd04c92075c30e6e0434478bb908a`.

The final version explicitly retains the finite-window endpoint qualification after (21), the simple-pole versus higher-pole distinction, reflected-zero warnings for a different norm contour, and the derivative-of-weight term. I checked these additions. Using the primary bound only for `y>73.2` is safe, and the elementary small-height argument overlaps that range.

I read `check_pole_packet.py` before running it. The finite-atom calculation differentiates `f(y(z))` with the correct logarithmic Jacobian and splits integration at every atom. Its finite polynomial is expressly a finite normalization test, not a truncated zeta Dirichlet series. Exact `Fraction` arithmetic verifies the polynomial coefficients and rational constant comparisons; the integral comparisons use mpmath at 70 decimal digits and are diagnostics, not interval enclosures.

For the independent replay, I copied the unchanged final report and script into this review's `replay` subdirectory and ran that copy with the local Python/mpmath runtime. Author files and their result were not modified. The run passed:

- nine direct Fourier-transform comparisons;
- three pole-value evaluations;
- three positive/negative mass cases, both tilted and untilted;
- one finite-Dirichlet mixed normalization;
- three finite-atom centered Stieltjes identities;
- the exact polynomial, Gaussian-moment and rational constant checks.

The independent JSON is byte-identical to the authored JSON. This proves reproducibility of the stated bounded checks, not the mathematical conclusions that require the written contour and RH arguments.

Final evidence hashes:

- Script: `25a20d5946dd6e973cd18cc52a1031f47cc4b2fe82cca236c32de0332ad40a04`.
- Authored and independent result JSON: `1cf9ae8467e35c1413a7c809ccc2daeb7757c4701a457356ffae25cd6672daf9`.
- Source manifest: `84cd4a5f31145cf596708b93933c1dee600bfa87569896d3d9acc8dcaf362243`.

I independently recomputed all eight retained source-file hashes and byte counts: the Schoenfeld PDF/text and six prior programme reports. All match the manifest. The Inoue HTML is a historical reference rather than an input to this theorem; no local HTML hash is claimed. The separately reported coordinator Gaussian cross-check was not used as proof or replay evidence here.

The review, replay output and receipt are frozen. No author report, original source, renderer or repository file was edited, and no new parameter scan or external model call was performed.
