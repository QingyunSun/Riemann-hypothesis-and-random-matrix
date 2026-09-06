# A stronger isolated-pair lemma after removing the background drift

2026-09-05. This is a proposed refinement of `yau_flow.md`, independently derived in the same research round. It has not yet received the other agents' full review. It overlaps conceptually with classical Lehmer-pair criteria and should not be advertised as a new principle without a priority check.

The reciprocal-chord condition δA→0 in the first draft can be replaced by the weaker inverse-square condition δ²B→0. The improvement removes the effect of a large common background velocity by an exact Galilean transformation of scalar heat flow.

## Statement

Let δ be the smallest angular gap in a circle-rooted degree-N polynomial. Center its endpoints at ±δ/2 and write

\[
Q_0(x)=p_\delta(x)H(x),\qquad
p_\delta(x)=\sin\frac{x-\delta/2}{2}\sin\frac{x+\delta/2}{2},\qquad
H(x)=\prod_{k\ne\pm}\sin\frac{x-\theta_k}{2}.
\]

Define

\[
L=\frac{H'(0)}{H(0)}=-\frac12\sum_{k\ne\pm}\cot\frac{\theta_k}{2},\qquad
B=\frac14\sum_{k\ne\pm}\csc^2\frac{\theta_k}{2}.
\]

If δ→0 and δ²B→0 along a sequence of configurations, then the global first collision time of the coefficient flow exp(sj(N−j)) satisfies

\[
D=\frac{\delta^2}{8}(1+o(1)).
\]

In fact, there are absolute constants C and ε₀>0 such that, when δ²(B+1)≤ε₀,

\[
\frac{\delta^2}{8}\le D\le
\delta^2\left[\frac18+C\delta^2(B+1)\right].
\]

No numerical value of C or ε₀ is claimed. The lower bound is the existing deterministic two-body comparison. The following argument gives the upper bound.

## 1. A global centered sine-factor estimate

For all real c and v,

\[
|\cos v-c\sin v|e^{cv}\le e^{4(1+c^2)v^2}.
\tag{S}
\]

Put w=|v|√(1+c²). If w≥1/2, use
\[
\log|\cos v-c\sin v|+cv
\le\log(1+|c||v|)+|c||v|
\le2w\le4w^2.
\]
The inequality is automatic if the factor vanishes. If w≤1/2, the function r(u)=cos u−c sin u is positive between 0 and v: throughout that segment,
\[
r(u)\ge1-u^2/2-|c||u|\ge1-1/8-1/2>0.
\]
Its centered logarithm f(u)=log r(u)+cu has f(0)=f′(0)=0 and
\[
f''(u)=-\frac{1+c^2}{r(u)^2}<0.
\]
Thus f(v)≤0, proving (S) also in this case.

Now put
\[
R(y)=e^{-Ly}\frac{H(y)}{H(0)}.
\]
Each sine ratio is cos(y/2)−cot(θk/2)sin(y/2). Applying (S) factor by factor gives the **global real-line bound**
\[
|R(y)|\le e^{4By^2},\qquad y\in\mathbb R.
\tag{G}
\]

When By²≤1/16, every uncentered sine ratio remains at least 3/4 along the segment from 0 to y. Consequently H has constant sign on that segment and
\[
-\frac{16}{9}B\le (\log |H|)''\le0.
\]
After subtracting the linear term Ly and integrating twice,
\[
-By^2\le\log R(y)\le0,
\qquad |R(y)-1|\le By^2.
\]
When By²>1/16, (G) gives |R(y)−1|≤e^{4By²}+1≤32By²e^{4By²}. Combining both regions,
\[
|R(y)-1|\le32By^2e^{4By^2},\qquad y\in\mathbb R.
\tag{E}
\]
The case B=0 is immediate: H is constant.

## 2. Exact heat conjugation and the moving frame

For any real L for which the Gaussian integrals converge,
\[
e^{s\partial_x^2}(e^{Lx}f(x))
=e^{Lx+L^2s}(e^{s\partial_x^2}f)(x+2Ls).
\tag{C}
\]
This is a direct completion of the square in the Gaussian convolution. Here the original trigonometric polynomial is bounded on the real axis; the transformed integrals converge at the times used below because δ²B is small.

Set s=τδ² and use the moving coordinate x=δξ−2Ls. With Z standard normal and Y=ξ+√(2τ)Z, formula (C) yields
\[
\frac{4e^{-L\delta\xi+L^2s}}{\delta^2H(0)}
Q_s(\delta\xi-2Ls)
=\mathbb E\left[
\frac4{\delta^2}p_\delta(\delta Y)R(\delta Y)
\right].
\tag{M}
\]
The multiplier on the left is real and nonzero, so it does not alter the roots or their signs relative to the constant H(0).

The right side converges uniformly on compact ξ,τ sets to
\[
\mathbb E(Y^2-1/4)=\xi^2-1/4+2\tau.
\]
More precisely, (E), the elementary sine Taylor remainder, and Gaussian integrability give
\[
\sup_{|\xi|\le R_0,\,0\le\tau\le T}
\left|\frac{4e^{-L\delta\xi+L^2s}}{\delta^2H(0)}
Q_s(\delta\xi-2Ls)-(\xi^2-1/4+2\tau)\right|
\le C_{R_0,T}\delta^2(B+1),
\tag{U}
\]
once δ²B is sufficiently small depending on T. Indeed the error is bounded by a constant times
\(\delta^2(B+1)(1+|Y|^6)e^{4B\delta^2Y^2}\), and its expectation is uniformly bounded after choosing δ²B small enough. This is why a quadratic global bound was necessary; a merely local Taylor expansion would not justify the heat integral.

## 3. Collision tracking with moving boundaries

Use the interval
\[
[-2\delta-2Ls,\,2\delta-2Ls]
\]
on the real cover of the circle. At time zero it contains exactly the selected pair, since δ²B→0 excludes any third point at distance O(δ). The normal form (U) shows that both boundary values stay nonzero for all times up to (1/8+ε)δ², and the whole interval contains no real root at that final time.

If no global multiple root had occurred, the initially simple circle roots would remain on the circle and vary continuously. The leading and constant polynomial coefficients are fixed and nonzero, so no root can escape via zero or infinity. Simple self-inversive roots cannot leave the circle without colliding with their reciprocal-conjugate partners. The two roots in the moving interval therefore cannot disappear without a multiple root, and cannot leave through its nonvanishing moving boundaries. This contradiction gives D≤(1/8+ε)δ².

Taking ε to be a sufficiently large constant times δ²(B+1) gives the quantitative upper bound. Pair identity after the first global collision is irrelevant: an earlier collision already establishes the desired upper bound.

## 4. Consequences and scope

On a triple-free event at length r, the packing argument now gives B≤Cr⁻², with no harmonic logarithm. Therefore the circular-beta proof in `yau_flow.md` works with δ²B=Oₚ((δ/r)²), which tends to zero at the same admissible r scales. The limiting laws and constants do not change.

The transformation also explains why a large common drift need not obstruct collision localization. The right structural quantity is curvature of the logarithm of the background product, not the absolute sum of its first derivatives. This connects naturally with classical Lehmer-pair inverse-square criteria. For an infinite canonical product one must separately justify convergence, the exponential normalization, and its true heat evolution; this note does not claim that those steps, or the arithmetic small-gap input, have been completed for ζ.

The stronger criterion is strictly weaker. Take δ=N⁻², put the selected pair at ±δ/2, and place the remaining N−2 points at angles (M+k)δ, k=0,…,N−3, with M=⌈√logN⌉. Every gap is at least δ. Direct harmonic-sum estimates give δ²B asymptotic to 1/M, tending to zero, while δA is of order log(N/M), tending to infinity. The Galilean argument therefore applies even though the first proof's absolute first-derivative bound fails. The moving interval may travel across many *initial* gaps; its all-time nonvanishing boundaries still make the tracking argument valid.

The root agent independently checked the centered-factor bound and the moving-frame mechanism. Numerical checks in `yau_flow_checks.py` include cases with δA between 1.09 and 5.31 but δ²B near 0.02. The selected local double-root times are close to δ²/8. Those configurations have many equal-size gaps, so the script deliberately does not label their computed local double-root time as the first global collision.
