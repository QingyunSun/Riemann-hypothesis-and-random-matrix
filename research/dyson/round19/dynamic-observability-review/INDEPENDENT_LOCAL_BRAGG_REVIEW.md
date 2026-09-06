# Independent review: a uniform local Bragg deficit under circular scalar heat

Date: 2026-09-05. Reviewer: residual_gram / Astra. **Accepted as an ordinary finite-model theorem with constants uniform in N.** No mathematical amendment is requested. This acceptance excludes a true-zeta transfer, a refutation of AH, a stochastic Dyson Brownian-motion claim, and any claim of research priority.

The complete reviewed author file is [LOCAL_BRAGG_PRODUCTION.md](../dynamic-observability/LOCAL_BRAGG_PRODUCTION.md), SHA256 `e87f858bbc39a592e1b2e557f0bcb83e05f685706b14586563b3c317ce651735`, 18,586 bytes. I read the complete proof and checker, checked the final presentation delta, and reran the unchanged bounded checker in a temporary directory. No author file was edited.

## 1. Exact normalization and observable

The polynomial evolution has coefficient multiplier exp[−k(N−k)t]. The root equation follows from the logarithmic derivative at a simple root: z_i/(z_i−z_j)=1/2−(i/2)cot((θ_i−θ_j)/2). Its constants cancel the (N−1) term, leaving θ_i′=Σcot((θ_i−θ_j)/2). With q_i=Nθ_i/(2π) and s=N²t/(4π²), the q equation has exactly K_N(x)=(2π/N)cot(πx/N). Centering the polynomial yields ∂_t Q=−∂_θ²Q. This is the deterministic repulsive root flow. The odd-N antiperiodic convention is harmless for the root argument.

For the stated Fourier convention, k_ε(u)=ε ψ̂(εu) has Fourier transform ψ(ξ/ε). Its N-periodization therefore has Fourier coefficients N⁻¹ψ(m/(Nε)). Including the outer 1/N in the pair statistic gives the spectral normalization **1/N²**. Multiplication by cos(4πu) shifts the frequency index by ±2N; evenness and |p_{−m}|²=|p_m|² identify the two translated sums. Thus D=C(0)−C(2) exactly. Every spatial summand is nonnegative, and half-grid initial data give D=0 term by term.

For the rank-N projection on 2N sites, the frequency intersection for 0<|m|≤N has size N−|m|. The variance trace identity gives E|p_m|²=|m|, including the boundary |m|=N. Equation (14) and its limit 1+ε²m₁ follow with the stated normalization. These are initial expectations, not a stationarity assertion.

## 2. The cyclic comparison and global existence

Lemma 1 is valid in the lifted chamber q₁<⋯<q_N<q₁+N. This chamber is convex. The vector y_i=q_{i+1}−h is in the same chamber as x_i=q_i: its internal inequalities are shifted original inequalities, and its last seam inequality is q₁+N−h<q₂−h+N. Periodicity of K_N makes y solve the same indexed equation, including the last coordinate.

The off-diagonal derivatives are −K_N′>0. Integrating the Jacobian on the segment from x to y gives a cooperative linear equation for y−x on each compact collision-free time interval. Positivity of this linear system preserves y−x≥0, including the seam gap. This avoids assuming that the initial minimum gap has a unique location or a differentiable minimizing index. Conserved center and the positive hard core give compactness of the relative configuration away from all kernel poles, and hence global existence.

## 3. Relative velocity, wrap handling and acceleration

The bounds |K_N|≤2/d and |K_N′|≤π²/(2d²) use intrinsic circular distance d≤N/2. Directional packing gives at most two k-th neighbors at distance at least kh; an antipodal particle can be assigned to either direction once. The counting estimate 2R/h remains an upper bound beyond the antipode. Stieltjes integration yields the tail 4/(hR), while the harmonic estimate yields the stated local inverse-distance sum.

In Lemma 2, all particles within 2d of i are within 3d of j. Including the mutual pair terms and omitting only each self-term bounds the two near force sums by the first term in (17). For a far point at distance r>2d from i, every point along a shortest arc from i to j has distance at least r−d>r/2 from it. Thus the interpolating arc never meets a kernel pole. The periodic kernel can be lifted along that arc, and the mean-value bound is 2π²d/r². This reasoning is valid across a coordinate seam and also when there are no far points.

For h=1/2, F(r)/r² is decreasing: rF′(r)<16 whereas 2F(r)>32+16π². The two directional neighbor sums and the derivative constant give precisely
\[
|q_i''|\le 4\pi^2\sum_{k\ge1}\frac{F(k/2)}{k^2}.
\]
The factor is 2 directions times π²/2 times 4 from (k/2)⁻². The elementary bounds in the report give
\[
|q_i''|<40(128\cdot2+16\cdot3)=12160<12288.
\]
This is uniform in N, configuration and time. No N-uniform bound for the individual velocities is assumed or needed. The corresponding inverse-square background bound is also valid. These estimates supply the uniform remainder control absent from a fixed-N curvature computation alone.

## 4. Event probability and opening speed

The determinant formula gives the adjacent occupation probability exactly. N sin(π/(2N))≥√2 for N≥2 proves p_N≥1/8. For N≥8, the sixteen selected grid labels in the event are distinct modulo 2N. Their occupation count has mean 8 and variance at most 4 by the negative off-diagonal DPP covariances. Chebyshev bounds the event that all sixteen are occupied by 1/16; subtracting it from the adjacent-occupation event yields probability at least 1/16. No independence is used. At N=8 the sixteen labels are the whole grid and the total occupation is deterministically 8, which is consistent with the argument.

The complete half-grid force vanishes. Subtracting the hole forces gives the sign and coefficient of (24): for a hole at h/2, the relevant cotangent difference is cot((h−1)π/(2N))−cot(hπ/(2N)), which is positive. A hole with 2≤h≤15 gives
\[
g'(0)\ge\frac8{\pi h(h-1)}\ge\frac4{105\pi}>\frac1{84}.
\]
The endpoint sine inequalities hold for every N≥8, including holes close to the antipode or beyond it. The sine factors themselves are positive for all h in the full hole sum.

With |g″|≤2A_* and s_*=β/(4A_*), the lower derivative β/2 and gap increment βs/2 follow uniformly. The upper relative-velocity bound F(1/2)<128 yields g≤1/2+128s+A_*s²<3/4 throughout this interval. The pair remains consecutive, and its lifted gap remains below N/2. This covers the original seam bonds without changing the event count.

## 5. Local deficit and fixed-time conclusion

On [1/2,3/4], nonnegativity of the seed and its support in [−1/2,1/2] give f̂(εg)≥cos(3πε/4)∫f. Squaring and applying the definition of ψ̂ gives k_{ε,N}(g)≥κ_ε. For Δ=g−1/2∈[0,1/4], the elementary sine chord bound gives 1−cos(4πg)≥32Δ²≥8β²s².

There are 2N positive grid bonds, each producing a distinct unordered pair on its good event. Their expected number is at least N/8. The pair statistic counts both orders, giving N/4 expected ordered contributions. Its normalization 1/N then gives exactly
\[
\mathbb E\mathfrak D_{\varepsilon,N}(q(s))\ge
2\kappa_\varepsilon\beta^2s^2
\quad(N\ge8,\ 0<s\le s_*).
\]
Overlapping events are harmless because expectation is linear and every other pair contribution is nonnegative. The proof needs no infinite-process construction or exchange of a Taylor expansion with N→∞. The lower bound is tiny but strictly positive for each fixed allowed s.

## 6. Actual-zeta limitations and verification receipt

The theorem demonstrates that deterministic scalar heat can create this localized Bragg deficit from ACUE initial data while retaining a half-unit hard core. It therefore disproves the claimed general transfer bound (30) under only the listed model hypotheses. It does not identify actual zeta's initial law with ACUE. General AH-Pairs permits near-zero clusters and multiplicities, and the actual H_t evolution requires additional principal-value, density, window and tail comparisons. Positive-time model separation supplies no initial-time arithmetic deficit. The report correctly states that an O(s) transfer error cannot justify a lower bound of order s², and that the Round 18 static reflection identities do not supply that missing estimate.

I read and replayed `check_local_bragg.py`, SHA256 `83807e566506c778fbc9a6903293e94158c557c1c1fe73e06f7f6d3157b2f549`. The unchanged N=8 exhaustive calculation visits 12,870 configurations and checks 48,048 good bonds. The independent JSON and log are byte-identical to the author's, both with SHA256 `b9272cb9512e0bea0551308a1d495a16adc2ba80e7c3a7bac9c1ae908055942d`. Its probability, hole-formula, acceleration and global-curvature calculations are floating diagnostics, not interval certificates. Its time, probability and envelope constants are checked separately with exact rational arithmetic. No numerical ODE evolution, additional N scan, zeta computation or source modification was performed.

The separate [coherent-mode review](../root-bragg-curvature/INDEPENDENT_CURVATURE_REVIEW.md) accepts the exact initial-curvature identity, but that identity is not used as a substitute for this theorem's uniform acceleration argument. The review receipt pins the author, checker, author receipt and independent outputs.
