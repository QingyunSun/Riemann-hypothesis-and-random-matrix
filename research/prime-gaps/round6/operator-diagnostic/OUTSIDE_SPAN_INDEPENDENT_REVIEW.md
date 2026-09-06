# Independent review of the frozen radial profile outside the old span

**Verdict: the outside-span argument is valid.** This note records the independent review already completed by the Yau-flow audit agent. It certifies a new direction in the true cap Hilbert space, not an enclosure of a numerical Rayleigh gain.

## Evidence independently checked

The reviewed witness is ../residual-trial/radial_residual_n98304_cut1e-09_tilt20_compact.npz. Its SHA256 is b283cab182b0b32091f24ac898def31cc263fa6af1a4540b30721e8122b80c77. A read-only hash comparison confirmed that this public checkpoint is byte-identical to the staged witness used in the independent review.

The h.npy member was decoded independently with Python's standard-library ZIP, NPY-header and binary-structure handling, rather than through the certificate's NumPy loading path. The stored array is little-endian binary64. Its entries at indices 0 through 12 are exactly zero, and its first nonzero entry is at index 18422, with exact dyadic value

\[
h_{18422}=-\frac{6264072493613325}{4611686018427387904}\ne0.
\]

This interprets the frozen stored value as an exact rational definition of the new step profile. It does not assert that the floating computation producing that value exactly evaluated an operator residual.

The 11 official coefficient signatures were separately read from the preserved source using its literal syntax tree. Their maximum exponent sum is 6. The old basis combines these signatures with radial powers of degrees 0 through 6. On the product cell with indices

\[
(j_1,j_2,\ldots,j_{39})=(r,0,\ldots,0),
\]

division by the common strictly positive product factor G leaves a polynomial in r of degree at most 12. The midpoint representatives are affine in r, the radial shift is affine in r, and each power-sum signature has degree at most its exponent sum. This degree assertion is for the actual frozen midpoint-step basis.

## Whole-cell support and positive measure

The argument uses whole product cells, not isolated representative points, which would not by themselves establish an L² assertion. The mesh is

\[
\Delta=\frac{2742997}{258046918656}>0.
\]

For the largest selected index, the maximum coordinate-total endpoint and maximum whole-cell total are respectively

\[
18423\Delta=0.1958335096353804\ldots,
\qquad
(18422+39)\Delta=0.19623744348796382\ldots.
\]

These were checked with exact rational arithmetic. The whole-cell total is strictly below the first outer-shell boundary

\[
\frac{653622010000}{689056987511}
=0.9485746779246842\ldots.
\]

Every selected coordinate cell is also strictly below the retained fragment cap. The companion certificate uses the sufficient conservative cap

\[
\frac{41328816845772771}{110249118001760000},
\]

which exceeds 18423 Delta. The independently reconstructed final outer cap was larger still, approximately 0.4951438701; using the smaller common cap is therefore harmless.

All 14 selected product cells consequently lie inside the same first outer shell and satisfy its cap automatically. On these small coordinate-total intervals, the unscaled fragment measure has total-size density one. Each selected product cell has mass Delta^39, which is strictly positive. The common factor G is strictly positive on them.

## Proof of nonmembership

Suppose the frozen cap-supported radial profile G h belongs to the old span U in L². The old profiles and the new profile are constant after the prescribed midpoint evaluation on each selected product cell. Equality almost everywhere therefore forces equality of their values on each such positive-mass cell.

After dividing by G, an old-span representation would give a polynomial p(r) of degree at most 12 satisfying

\[
p(0)=p(1)=\cdots=p(12)=0,
\qquad
p(18422)=h_{18422}\ne0.
\]

Thirteen distinct roots force p to vanish identically, a contradiction. Hence G h is outside U. Equivalently, its orthogonal projection onto U-perp has strictly positive true Hilbert norm. This conclusion is independent of inverse-Gram conditioning and of the accuracy of the computed projection norm.

## Scope of this review

The implementation certify_outside_span.py and its outside_span_certificate.json receipt were read when preparing this record. They additionally contain a modular rank-77 witness for the old basis and an augmented-rank-78 conclusion. This reviewer did not independently rerun that modular rank computation. The 13-zero argument above does not need it; dimension exactly 78 additionally uses independence of the 77 old basis vectors.

No fine integral, optimization, or existing certificate was rerun or modified for this note. The result proves nonmembership for the frozen dyadic step profile. It supplies no quantitative lower bound for the outside-space norm, no outward enclosure of the new quotient or its gain, and no certification of the fully restored arithmetic support. Those remain separate obligations.
