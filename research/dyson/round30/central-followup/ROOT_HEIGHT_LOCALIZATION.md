# The upper balanced tail localizes at the central multiplicative scale

2026-09-08. Root derivation; independently checked by the r29-close agent against every estimate in sections 2–5 of the final R30 upper-height proof. This is a summation corollary for a specified family of blocks, not a strict global variance theorem.

## Uniform endpoint statement

Let the block and all normalizations be exactly those of R30, with ordinary RH, full sharp odd factor intervals, fixed smooth profiles and fixed comparison bounds for D/sqrt(X) and K/sqrt(X). The proof of [UPPER_HEIGHT_BALANCED_CHECK](../stationary-challenge/UPPER_HEIGHT_BALANCED_CHECK.md), SHA256 `53aa1b19cd28094248efe2ac5d3f88859e27f1751ebb1ffbbaa6c6e38213d5f2`, actually gives the bounded estimate
\[
|Z(X)|\ll\frac{T^{-141/800}}{\sqrt{\log T}}
+\left(\frac{T^2}{X}\right)^{3/4},
\qquad T^2\le X\le T^{9/4}.
\tag{1}
\]
Its constants are uniform over this entire closed interval. A fixed positive delta is needed only to conclude that the second term tends to zero at every height X at least T to the power 2+delta.

To check the endpoint, write Y=X/T. The positive energy is bounded by Y times log squared and the negative energy by X/T squared, including at X=T squared. The fixed-beta Selberg interval containment, localized Schur kernel estimates, odd-lattice correction and powers-of-2 correction remain valid there. The sharp Perron estimate is used only for |t| at most a fixed multiple of K, which is less than D squared uniformly for large T. The split L=sqrt(T)log(T) remains below the first alias threshold. The second-order high-frequency estimate is (T/D) to the power three-halves, giving the second term of (1). No constant in these steps needs an inverse power of delta. At the endpoint this is an O(1) bound, consistent with R29.

## A summable upper-height tail

Fix one such uniformly controlled balanced block at each
\[
X_j=2^jT^2,\qquad
0\le j\le j_{\max}:=\left\lfloor\frac{\log T}{4\log2}\right\rfloor.
\]
The profiles may be fixed, or drawn from a specified family whose required derivative bounds and support separations are uniform. Let Z_j be these blocks, and let J be a fixed nonnegative integer. Equation (1) and the geometric series yield
\[
\sum_{j=J}^{j_{\max}}|Z_j|
\ll T^{-141/800}\sqrt{\log T}
+2^{-3J/4}.
\tag{2}
\]
For an empty sum the assertion is immediate. Otherwise there are O(log T) summands in the first term, and
\[
\sum_{j\ge J}2^{-3j/4}
=\frac{2^{-3J/4}}{1-2^{-3/4}}.
\]
In particular,
\[
\lim_{J\to\infty}\limsup_{T\to\infty}
\sum_{j=J}^{j_{\max}}|Z_j|=0.
\tag{3}
\]
Thus the upper balanced tail is uniformly small outside a sufficiently large fixed multiplicative neighbourhood of T squared. Fixed bounded weights on these blocks preserve (2), as does a fixed finite number of block families with uniform constants.

## What this does not prove

The order of limits in (3) matters. For any fixed J, the blocks j=0 through J-1 are not estimated by a quantity tending to zero. It would be false to infer that the entire upper contribution vanishes merely because each fixed exponent alpha greater than 2 has a vanishing block. The abstract array a_0(T)=1 and a_j(T)=0 for j>0 illustrates this logical distinction: it has an identically zero remote tail and a nonzero total. This array is only an illustration of the limiting inference, not a model of actual primes.

Nor has this note identified the stipulated balanced dyadic family with the complete R26 sum. Arbitrary owner masks, all factor ratios, all physical shift profiles and their multiplicities require their own estimates and summation bookkeeping. The genuine central signed correlation, and ultimately the strict inequality liminf Z_T < A-2M, remain unproved.

No new prime computation, formal verification or external novelty claim accompanies this corollary. The independent review confirmed the uniform alpha=2 endpoint and both summations above; it did not upgrade their scope to the global programme.
