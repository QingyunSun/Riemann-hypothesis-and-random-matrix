# Independent root review: two bounded R14 advances

Date: 2026-09-05. Reviewer: root Astra. Both complete author reports were read and their proofs checked independently. This review is not formal verification, a global novelty assessment or a claim about the full zeta covariance.

## Actual Type I component

Reviewed `smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md`, SHA-256 `d6143f19ddf006a1acc833ecd2e5265bffb35817930cfeaa4f4e4b973af7c849`.

The identity Lambda=mu*log, including n=1, makes the split at a real cutoff U exact. After n=rs, a nonunit r contributes to neither a primitive residue progression nor its principal sum. For a unit r the required residue is h times its inverse. No discarded nonunit main term remains.

The profile displayed in equation (13) uses the actual n-h kernel. Both a-factors have the negative-three-halves branch because the compact chi support forces n-h>X and n>X. The integral representation in (14) removes the apparent small-denominator phase singularity. Its derivatives, the compact support and the two logarithms give the claimed uniform O_J(log²X) seminorms for all retained r,h,q. Constants can depend on fixed derivative order and cutoff separation; they do not silently depend on T.

Poisson summation has the positive progression phase e(kb/q) for the stipulated negative-sign Fourier transform. Its zero frequency cancels exactly against the primitive mean, including c_q(0)=phi(q). The nonzero modes are bounded by (L/q)(q/L)^J log²X. Summing q^(J-1) and r^(J-1), and the actual h weights, gives HX(UQ/X)^J log²X without any omitted factor of q or H.

The explicit choice U=X^.4,J=4 has exponent 1711/1750 and margin 39/1750 below one. More generally the uniform proof applies to every fixed positive separation U<=X^(.477-eta), with fixed J eta>2/7. There is no uniform assertion as eta tends to zero. The proof of the recalled Heath--Brown identity is algebraically valid, and the criterion concerns an individual smooth unrestricted variable; a long product does not automatically satisfy it.

Accepted as an unconditional classical Poisson application to this programme's exact discrepancy. The signed Lambda_{>U} term remains exact and unestimated. Its cofactor can be small. Removing this component supplies neither an inequality for the full Lambda sum nor a solution of Montgomery's conjecture.

## Selected CUE background and finite heat-depth error

Reviewed `cue-selected-background/SELECTED_CUE_BACKGROUND.md`, SHA-256 `fbc67828d13534d8d0b4ac1f742a639b282dd93a3f7cb635291f8cdbb651c0a5`, and reread Sections 1--5 of the existing quantified Galilean audit.

For the exact finite CUE Gram representation, ||phi||²=N/(2pi) and ||phi'||²<=N³/(6pi). The two-point determinant is bounded by AD d². Projecting the third vector off the first two gives both A and D r(z)² bounds. Their minimum yields precisely the stated rho3 upper bound N^5 d²/(24pi³) min(1,N²r(z)²).

The singular endpoint integral is finite because the retained r(z)² factor cancels it. The elementary bound q(z)<=pi²/(4r(z)²) and the split r=1/N give an integral at most pi²N. Two endpoints, the 2pi anchor integral and integration of d² from zero to epsilon give N^6 epsilon³/18. These are ordered factorial correlations, so there is no extra half factor. The periodic orientation includes the wrap gap.

The midpoint comparison is made only for consecutive pairs: every third point is outside the open short arc and is at least as close to one endpoint as to the midpoint. Dropping consecutiveness only after replacing by endpoint weights avoids a divergent midpoint integral. The selected minimum requires no conditional density: on delta_min<=L N^(-4/3), its nonnegative background is one of the counted summands. Markov followed by the fixed-L minimum-gap tail gives B_min/N² tightness. The order of limits is valid and does not assume a uniform finite-N tail estimate.

The pinned deterministic lemma uses exactly this midpoint B and controls the heat product after its Galilean conjugation, with constants independent of N and drift. Since delta_min=N^(-4/3) times a tight variable, eta=delta_min²(B+1)=O_p(N^(-2/3)). The lemma's small-eta event has probability tending to one. This proves 8D/delta_min²-1=O_p(N^(-2/3)), and multiplication by the tight squared gap gives absolute difference O_p(N^(-10/3)). No independence between the gap and background is required.

The scalar minimum-gap lower comparison is available without the small-eta condition when delta_min<pi, which holds almost surely for CUE N>=2. Thus the stated nonnegativity is consistent. Finiteness of D for almost every CUE polynomial follows from growth of an interior coefficient and self-inversive root tracking before a collision, as stated in the report.

Accepted as an ordinary finite-CUE result based on the checked classical extreme-gap input and the existing audited deterministic lemma. This is an approximation error in probability, not a rate of convergence to the limiting depth distribution. It is not a stochastic DBM theorem, a general-beta result or an identity available for zeta zeros.

## Remaining work

Both results are appropriate to preserve as concrete progress: one removes an exact actual arithmetic component, and the other strengthens a finite random-matrix heat-flow comparison. The full signed arithmetic remainder, the desired out-of-band zeta correlation inequality and all famous-conjecture targets remain open. Separate agent reviews and bounded algebra replays are retained alongside this review.
