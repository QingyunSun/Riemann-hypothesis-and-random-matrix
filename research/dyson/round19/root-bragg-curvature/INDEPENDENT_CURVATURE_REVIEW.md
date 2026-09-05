# Independent review of the coherent ACUE-mode curvature

Date: 2026-09-05. Reviewer: residual_gram / Astra. Acceptance: the complete fixed-N ordinary identity is correct. This review does not accept a uniform positive-time conclusion or an actual-zeta transfer, neither of which the author claims.

Reviewed source: `EXACT_COHERENT_MODE_CURVATURE.md`, SHA256 `d8ae40d3442564644b2fe9e647f8ac6061b13f6b8ae4eedfbb618dd7036d9a76`. The author file was read in full and was not edited.

## Time, angular frequency and the derivative

With radian angles, s=N²t/(4π²), q_i=Nθ_i/(2π), and u_i=4πq_i=2Nθ_i, the exact chain rule gives
\[
q_i'(s)=\frac{2\pi}{N}V_i,\qquad
u_i'(s)=\frac{8\pi^2}{N}V_i.
\]
Pairwise antisymmetry of cotangent makes ΣV_i=0 identically. Its s derivative vanishes as well, so Σu_i′=Σu_i″=0 at every collision-free time.

At a rotated 2N-grid subset all e^{iu_i} agree. For Z=N⁻¹Σe^{iu_i}, one therefore has Z′=0 and Z″=−Z N⁻¹Σ(u_i′)². Differentiating |Z|² gives
\[
B_N''(0)=-\frac{128\pi^4}{N^3}\sum_iV_i^2.
\]
The sign and every power of N follow without an ensemble or an approximation. In particular this is an s derivative, not a derivative in the original t variable.

## Ensemble expectation and pair-counting factor

Expanding the force squares yields the cotangent triple sum −1 for each unordered triple. Including its factor two and replacing cot² by csc² gives exactly
\[
\sum_iV_i^2=2\sum_{i<j}\csc^2((\theta_i-\theta_j)/2)-\frac{N(N^2-1)}3.
\]
For the projection DPP on 2N sites, the source's p_d=1/4−sin²(πd/2)/(4N²sin²(πd/(2N))) is det of the two-by-two kernel. The expectation of twice the unordered pair sum is the ordered-pair sum, hence the factor **2N** multiplying Σ_d p_d csc². The odd csc⁴ sum is obtained by subtracting the N-site sum from the 2N-site sum and equals N²(N²+2)/3. Substitution gives
\[
\mathbb E\sum_iV_i^2=\frac{N(N^2-1)}6,
\quad
\mathbb E B_N''(0)=-\frac{64\pi^4}3(1-N^{-2}).
\]
These algebraic reductions require N≥2 and include that endpoint.

An independent N=2 angular check agrees. For an adjacent pair its separation Δ initially equals π/2, and dΔ/dt=2cot(Δ/2)=2. Thus dΔ/ds=2π². The coherent mode is cos²(2Δ), whose second s derivative at the initial point is −8(2π²)²=−32π⁴. Adjacent subsets have probability 1/2; opposite subsets have zero force. The expectation is −16π⁴, exactly the N=2 specialization above.

## Scope

The finite ensemble permits differentiation at a fixed N. It supplies no bound on the N dependence of the Taylor remainder. A nonzero limiting initial curvature cannot be promoted to a fixed microscopic-time separation without an independent uniform acceleration/remainder estimate. The global coherent mode also differs from the localized R16 decaying-kernel deficit. The author states both limitations correctly.

No amendment is requested. No floating calculation, large enumeration, source modification or Git action was used in this review.
