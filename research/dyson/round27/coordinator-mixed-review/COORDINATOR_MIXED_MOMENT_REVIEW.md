# Independent review of the R27 mixed-moment test

Status: ordinary mathematical review accepted after a derivative-order correction. This is a feasibility and inequality-direction result, not a strict covariance upper bound. I read the complete author manuscript and checked the corrected Poisson passage in the live version. The receipt records and freezes that version.

Author manuscript: `research-round27/mixed-moment-test/MIXED_MOMENT_DIRECTION_TEST.md`, 21,089 bytes, SHA-256 `b338a3210061055f6ad5899fd168175ba2c85d6225f80f71e6cd48098923cdc5`. While review was underway, the author added Lemma 2 and clarified the composite sign family and parity removal in the GY comparison. I subsequently reread the complete expanded manuscript and reviewed those additions; the acceptance below applies to this frozen expanded version.

## Correction made and verified

The original passage described the remainder `O(A_f*(d/X)^2)` as following from two derivatives. I sent a targeted correction to the owning task; the current author file now specifies **three derivatives**. For clarity, the complete calculation is

\[
\sum_{m\equiv d\ (2d)}f(m)-\frac1{2d}\int f
=\frac1{2d}\sum_{k\ne0}(-1)^k\widehat f(k/(2d)).
\]

If `||f'''||_1 << A_f/X^2`, three integrations by parts bound the right side by `O(A_f*d^2/X^2)`. Two derivatives alone only yield `O(A_f*d/X)`. The actual smooth packet has uniform derivatives of every fixed order, so the corrected argument retains the original error `Y*Q^3/(X^3*ell)`. No mathematical conclusion needs weakening.

## Other substantive checks

- The primitive progression is modulo **2d**, and its prime density is `1/phi(d)` for odd d. The flat odd-cofactor lattice has density `1/(2d)`. The outer factors 2 and -4 therefore give exactly the finite coefficient K_Q displayed in Lemma 1.
- Splitting the weight into the two common functions `F(n-h,h)*log(n-h)` and `F(n-h,h)`, with scalar `-log d` on the latter, makes weighted partial summation legal. The uniform cutoff `2Q<X^(2/5)` lies strictly below the ordinary Bombieri--Vinogradov range. I reopened the primary short-gaps paper's Proposition 2.15, including its below-one-half prime case and interval uniformity; no stronger 186 distribution exponent is required here.
- Nonprimitive classes retain actual prime powers, the exact factor log p, and the condition p|h. The positive-integer count for h=2pr is O(Y/p), including its empty range. The divisor coefficient is charged once before summing p. This validates the stated nonprimitive cost.
- The exact identity `A_Q=Lambda_Q+log(m/Q)*B_Q` preserves vanishing of c_Q on primes. The two finite composite examples have the stated opposite signs. They show failure of a pointwise sign inference, without claiming to model the global asymptotic covariance.
- The available per-shift logarithmic error, multiplied by the actual number of shifts and amplitude, does not yield a vanishing error in the natural power-length range. This is a limitation of that available estimate, not a lower bound on the true error. The stated pure and mixed GY comparisons retain their distinct approximants and parameter restrictions.
- The **new Lemma 2 improves the pure-divisor part** beyond its earlier crude estimate. Compatible divisor pairs select one odd class modulo `2D`, with `D=lcm(d1,d2)<=Q^2`; the original outer factor two leaves exactly the coefficient `1/D`. The product of logarithms cancels the `ell^-2` normalization at the level of its amplitude, giving `A_f=O(1/X)` and `||f'''||_1=O(X^-3)`. Three integrations by parts therefore give `O(D^2/X^3)` for each pair and shift. Summing at most Q^2 pairs and O(Y) shifts gives `O(Y*Q^6/X^3)=O(Y^5/X^3)`. Both subsequent sums are geometric: the Y sum is dominated by `(ell*X/T)^5`, and the height sum by U^2. The result is exactly `O(ell^5*T^(-1/2))`. I accept this unconditional reduction to the explicit finite divisor main. It does not evaluate that main to a new upper-bound constant and introduces no genuine prime factor into Poisson summation.
- The positive measure in (18), the real interval endpoints, and the continuum center give the original variance norm exactly. For each fixed T>2 the interval features are square-integrable. Polarization gives the lower projection bound and leaves an unknown nonnegative residual. The pseudoinverse and range condition are legitimate for an exact Gram matrix.
- The kernel in (23) follows by integrating lambda from `T*log(max(m,n)/x)` to infinity, then integrating x up to min(m,n). This reproduces the exact b_T(min) times Pareto kernel. A separation-localized off-diagonal packet has zero diagonal and is not a positive Gram form merely because its edge weights are nonnegative. Cross-scale features therefore require their own actual Gram terms.

## Global boundedness and the real remaining target

I separately reopened R20 `length-averaged-variance/EXPONENTIAL_LENGTH_AVERAGE.md`, equations (5)--(7), to locate the inherited ordinary-RH bound `0<=liminf Vbar<=limsup Vbar<=A`. Combining it with the already reviewed R26 identity yields

\[
-2M\le\liminf\mathcal Z_T\le\limsup\mathcal Z_T\le A-2M.
\]

Thus the **global** Z_T is already O(1). Growing bounds for separate packets or for a particular attempted mixed-moment error do not negate that fact. The open objective is a strict improvement below A-2M along an unbounded sequence. The explicit threshold 1-2M is sufficient and stronger; reaching exactly that threshold is not necessary for every possible exclusion of AH.

I accept the corrected Lemma 1, the expanded Lemma 2, and the manuscript's limited feasibility conclusion. The pure-divisor completion error is now globally vanishing and must not continue to be described as an obstruction. The genuine-prime mixed moment still leaves the shifted prime-prime term in (13), and neither that estimate nor projection positivity supplies the missing strict upper bound. Returning to the weaker per-shift genuine-prime calculation would not improve the already established R26 joint-main cancellation.

## Verification limits

The author checker was not run, and this review does not claim formal verification, a numerical asymptotic experiment, an exhaustive literature search, or a new audit of all inherited R20/R26 source proofs. GY definitions, theorem conditions and selected proof steps were checked in the separate coordinator source-intake note. The new source reopening here was [short-gaps Proposition 2.15](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), printed page 10. The mathematical correction and its effect were checked directly as above.
