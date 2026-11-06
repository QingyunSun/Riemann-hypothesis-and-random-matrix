# What pair correlations forget

A six-panel English cartoon for mathematics PhD readers, based on the 5 November 2026 Tao meeting note. This is an explanation of the finite-model results in that note, not an announcement of a new zeta theorem.

- [Full cartoon](Tao-ACUE-PhD-cartoon.png)
- [PDF: overview plus three enlarged reading spreads](Tao-ACUE-PhD-cartoon.pdf)
- [Exact image-generation prompts](generation-prompts.md)

## The central point

The collection of all pair separations does not necessarily tell us which separations share a common endpoint. Those relationships matter when zeros move. The counterexamples make this loss of information explicit: identical complete pair data can give different scalar-heat dynamics.

This challenges a proposed reconstruction principle. It is not a counterexample to Montgomery's pair-correlation conjecture or the full zeta/GUE conjecture.

## 1. Why Tao introduced ACUE

CUE consists of eigenangles of a Haar unitary matrix. ACUE selects N sites from a regular 2N-site circle with Vandermonde-squared weights; it is not uniform subset sampling. In particular, its smallest possible angular separation is pi/N, half the mean separation.

Writing p_k = tr(U^k), its mixed trace moments match those of CUE in the protected range
\[
\sum_{k\ge1}k a_k\le N,\qquad \sum_{k\ge1}k b_k\le N,
\quad
\mathbb E\prod_k p_k^{a_k}\overline{p_k}^{\,b_k}.
\]
Thus low moment agreement does not by itself establish the desired point-process law. The two schematic rings in panel 1 illustrate the same N=7.

## 2. One time convention throughout

For angles theta_j, choose
\[
F_0(x)=\prod_{j=1}^N\sin((x-\theta_j)/2),\qquad
F_s=e^{s\partial_x^2}F_0.
\]
Up to the first collision, a simple zero obeys
\[
\dot\theta_j=-\frac{F_s''(\theta_j)}{F_s'(\theta_j)}
=-\sum_{k\ne j}\cot\frac{\theta_j-\theta_k}{2}.
\]
This is deterministic attractive scalar heat. The source repository also uses a reverse parameter t=-s; its derivative signs must therefore be reversed here. Dyson Brownian motion has noise and repulsive drift and is a different process.

The curve pictures in panel 2 are conceptual illustrations, not numerical solution plots.

## 3. The exact four-point counterexample

For a half-filled cyclic group with K=2N sites, let C be the complement of S and set
\[
c_S(r)=\sum_x1_S(x)1_S(x+r).
\]
Then
\[
c_C(r)=K-2N+c_S(r)=c_S(r).
\]
Consequently the full pair-displacement measures agree, equivalently every |p_k|^2 agrees. This is unlabelled pair information, not a labelled distance matrix.

For S={0,1,3,4} and C={2,5,6,7} in Z/8, the six shorter-arc distances are 1,1,2,3,3,4. After a common rotation, use
\[
F(x)=\cos2x-\sqrt2\cos x+1,\qquad
G(x)=\sin2x+\sqrt2\sin x.
\]
Their exact first collision times are
\[
\tau_S=-\tfrac12\log y_* =0.0886279433267\ldots,\qquad
4y_*^3-4y_*+1=0,\quad y_*\in(4/5,1),
\]
\[
\tau_C=\frac{\log2}{6}=0.1155245300933\ldots.
\]
F has two simultaneous double collisions; G has a triple collision. Both initial configurations lie on the same grid. They are not a CUE/ACUE sample pair.

## 4. The missing information appears already in a cubic

For A={0,1,2,4,7,8} and B=A^c in Z/12, full pair data and sorted consecutive gaps (1,1,1,2,3,4) agree. But
\[
|p_2|^2=7,\qquad
T=\Re(p_1^2\overline{p_2})=2\ \text{on A},\quad -2\ \text{on B}.
\]
Under the attractive s-flow,
\[
\frac{d}{ds}|p_2|^2=4(N-2)|p_2|^2+4T.
\]
At N=6 this yields 120 and 104. The small graph shows initial tangent slopes from the common value 7, not entire time trajectories.

Moving a sufficiently small amount of ACUE mass between these two symmetry orbits preserves the joint law of the full static pair measure and gap histogram, while changing the mean heat response. It changes the protected weight-two cubic T. It does not preserve all of Tao's protected mixed moments.

The cubic contains repeated-index contributions as well as genuine three-point information. The meaningful distinction here survives because the pair contributions are already matched; a zeta experiment would need to remove them explicitly.

## 5. Why extremes require more information

In the finite Haar-CUE model, the angular minimum gap has probabilistic order N^(-4/3). The project's collision analysis, including control of the surrounding zeros, gives first-collision order N^(-8/3). The small-gap heuristic is tau approximately delta^2/8; the required background estimates are part of the argument.

For ACUE, the lattice yields the deterministic lower bound
\[
\tau\ge\frac{\pi^2}{8N^2}.
\]
This is not a universal asymptotic equality. Some configurations, including equally spaced clock configurations, never collide.

A first collision depends on the rarest close pair. Convergence in a fixed local window alone does not control such a global extreme.

## 6. What would constitute progress for actual zeta zeros?

The finite counterexamples identify missing information. To use it for zeta, one still needs arithmetic control of an appropriate higher correlation or the local environment of a close pair, with the correct scales and hypotheses.

The explicit formula connects prime sums to zero statistics, but does not automatically provide the needed estimate. The final bridge in the cartoon is intentionally unfinished.

The question to carry forward is:

**Which prime-based statistic detects how a close pair interacts with its surrounding zeros?**

## Sources and verification

- [Tao, The alternative hypothesis for unitary matrices (2019)](https://terrytao.wordpress.com/2019/05/08/the-alternative-hypothesis-for-unitary-matrices/): motivation, ensemble weights and protected moment range.
- [Meeting note source](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/feat/tao-acue-meeting-note/docs/Tao-ACUE-meeting.tex).
- [Exact finite-model derivations and checks](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/codex/astra-research/research/counterexamples/pair-matched-flow/PAIR_MATCHED_HEAT_COUNTEREXAMPLES.md).
- [Collision-scale and normalization audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/codex/astra-research/research/reports/new_attachment_bridge_audit.md).

The source PDF was read and visually inspected. A separate mathematical reviewer checked the configurations, collision times, conjugation, cubic values, heat-time signs and slopes. The image was reviewed separately; schematic particle counts and the graph's starting value were corrected. This is explanatory artwork with internal mathematical checks, not an external peer review or a formal proof.

## Rebuild and scope

Run: python build_pdf.py

Requires ReportLab. The PDF embeds the unchanged final raster, then presents clipped, enlarged page views without altering its pixels. The full poster is 1024 by 1536 pixels; enlarged views improve reading layout, not source resolution.

No numerical performance claim is made. No repository infrastructure or research theorem was changed. Further proof formalization, new counterexample searches and actual-zeta estimates are outside this illustration task.
