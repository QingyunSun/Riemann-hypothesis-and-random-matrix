# R30: a vanishing balanced block above the central height

2026-09-07. This checkpoint proves a local estimate under ordinary RH. It does not prove a strict global prime-variance improvement, refute AH, establish Montgomery–Dyson/GUE, or improve a prime-gap record. No external novelty claim or formal proof certification is made.

For fixed smooth profiles, sharp full odd factor intervals, and
\[
X=T^\alpha,\quad Y=X/T,\quad D,K\asymp\sqrt X,
\qquad 2+\delta\le\alpha\le9/4,\quad \delta>0\text{ fixed},
\]
the actual block defined in equation (1) of the [complete proof](../dyson/round30/stationary-challenge/UPPER_HEIGHT_BALANCED_CHECK.md) satisfies
\[
|Z_{D,K}|\ll
\frac{T^{-141/800}}{\sqrt{\log T}}+T^{-3\delta/4}=o(1).
\]
The full unmasked Möbius sequence, the odd center 2, prime powers, and both sharp endpoints are retained. This strengthens the local boundedness mechanism at these upper heights. It does not extend to an arbitrary divisor mask or to the central height \(\alpha=2\).

The arithmetic ingredient is the RH consequence
\[
\sup_{|t|\le D^C}\left|\sum_{D<d\le2D,\ d\ \mathrm{odd}}\mu(d)d^{it}\right|
\ll_{C,\eta}D^{1/2+\eta}.
\]
A sharp Perron argument establishes this from the classical reciprocal-zeta estimate stated in [Bagchi, printed page 4, equation (3)](https://www.isibang.ac.in/~statmath/eprints/2005/isibc200535.pdf). This use of actual Möbius cancellation is absent from R29's mean-value argument for arbitrary bounded coefficients. The reciprocal-zeta estimate itself is classical, not a project discovery.

The general-height energy estimates have squared norms \(Y\log^2T\) and \(X/T^2\). Splitting the nonstationary frequencies at \(L=\sqrt T\log T\) gives the first vanishing term. At the alias frequencies, the fixed second-order estimate supplies the second term over the entire infinite tail. All constants may depend on the fixed profiles, comparison constants and \(\delta\). A limit in which \(\delta\) tends to zero is not covered.

The earlier [sharp odd stationary-phase derivation](../dyson/round30/stationary-challenge/SHARP_ODD_STATIONARY_CHALLENGE.md) is preserved in full. It retains the half-weight endpoint correction, the odd-lattice alias signs, the second endpoint saddle, and the noncompact band-projected prime error. Its vanishing error does not estimate its signed central main term. The upper-height theorem uses frequency separation to avoid that unresolved central obstruction.

The proof's section 6 explains the distinction from R23: that argument removed certain discrepancies for a masked owner family; it did not estimate this whole unmasked balanced block. Conversely, the present reciprocal-zeta argument cannot be inserted into the masked family without an additional theorem.

The [root review](../dyson/round30/ROOT_REVIEW.md) records the analytic checks and limits. Twelve exact algebra groups were replayed independently and reproduce the author's JSON byte for byte. They check exponent and norm identities, not the analytic theorem. The upper-height KaTeX syntax check was unavailable because the existing local package returned empty exports; its recorded error is not a passed syntax check. No new prime scan or external model session was run. The [intake manifest](../dyson/round30/INTAKE_MANIFEST.json) pins the unchanged author files.

The next unresolved object is the actual central alias correlation at \(X=T^2\), followed by the remaining global packets. Another stationary representation or an absolute-value estimate that remains \(O(1)\) does not supply the required strict signed gain. The programme's global threshold remains the one stated in [R26](dyson_round26.md).
