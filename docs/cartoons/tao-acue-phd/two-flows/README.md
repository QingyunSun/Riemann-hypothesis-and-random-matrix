# Pair data, two flows, and the missing arithmetic bridge

Two English comic pages for mathematics PhD readers, expanding the project's 5 November 2026 discussion note for Terence Tao.

[Two-page printable PDF](Tao-ACUE-two-flows-cartoon.pdf) · [Page 1 PNG](01-pair-data.png) · [Page 2 PNG](02-two-flows.png) · [Generation prompts](generation-prompts.md)

- **Page 1:** the exact finite counterexamples and the cubic mechanism.
- **Page 2:** Tao's motivation, scalar heat versus circular Dyson Brownian motion, extreme gaps, and the open zeta transfer.

The images are explanatory artwork. Particle motions and tangent drawings are schematic, not numerical trajectories. The two eight-site circles, their occupied sites, and the stated numerical quantities are exact examples or stated approximations.

## The essential mathematical point

The full unlabelled pair-displacement measure is equivalent to the collection of Fourier powers |p_k|² for **all** k. One Fourier coefficient alone is not sufficient. A labelled distance matrix is different information.

At half filling, complementary occupied sets have the same pair counts:
\[
c_{S^c}(r)=2N-2N+c_S(r)=c_S(r).
\]
Yet the arrangements of neighbours around individual zeros may differ, and nonlinear observables of moving zeros can detect that difference.

For S={0,1,3,4} and C={2,5,6,7} in Z/8, both shorter-arc distance multisets are (1,1,2,3,3,4). Under ordinary scalar heat, their first collision times are
\[
\tau_S=-\frac12\log y_* \approx0.0886279433,\quad
4y_*^3-4y_*+1=0,\quad y_*\in(4/5,1);
\qquad
\tau_C=\frac{\log2}{6}\approx0.1155245301.
\]
These are two deterministic grid configurations. They are not a CUE/ACUE sample comparison.

For A={0,1,2,4,7,8}, B=A^c in Z/12, the sorted cyclic gaps also agree. Write p_k=Σ_j exp(ikθ_j). At the initial time,
\[
|p_2|^2=7,\qquad
T=\operatorname{Re}(p_1^2\overline{p_2})=
\begin{cases}2& A,\\-2&B.\end{cases}
\]
For the attractive scalar-heat time s,
\[
\frac{d}{ds}|p_2|^2=4(N-2)|p_2|^2+4T,
\]
giving 120 and 104 at N=6. Small ACUE probability transfers between the symmetry orbits preserve the joint law of static pair data and sorted gaps, but change a protected cubic. This simple construction does **not** preserve all protected trace moments.

## Two different flows

**Scalar heat** evolves a trigonometric polynomial:
\[
\partial_s F=\partial_x^2F,\qquad
F_0(x)=\prod_j\sin((x-\theta_j)/2).
\]
Before collisions, its zeros satisfy the deterministic attractive equation
\[
\dot\theta_j=-\sum_{k\ne j}\cot((\theta_j-\theta_k)/2).
\]
This is the convention used throughout both comic pages.

**Circular Dyson Brownian motion** instead has noise and repulsive drift. In the normalization of the project proof,
\[
d\theta_i=N^{-1/2}dB_i+
\frac1{2N}\sum_{j\ne i}\cot((\theta_i-\theta_j)/2)\,dt.
\]
A trace monomial has positive weight Σ k a_k and negative weight Σ k b_k. For products of such observables at deterministic times, CUE-started and ACUE-started flows agree when the **sum across all times** of each weight is at most N. This is not N independently at every time. Unrotated ACUE also satisfies the theorem.

The source supplies a balanced weight-(N+1) witness. The theorem does not cover arbitrary nonlinear observables, collision stopping times, or adaptive sampling. Thus adding dynamics does not automatically bypass a protected moment range.

## CUE and ACUE collision scales

The internally reviewed project argument gives finite Haar-CUE first collision scale N^(-8/3), using the minimum-gap law and a background estimate. This is a probabilistic scale, not a universal limiting constant. ACUE obeys the deterministic lattice bound τ≥π²/(8N²); this is not an equality and some clock configurations never collide.

The heuristic τ≈gap²/8 applies to a sufficiently isolated close pair, with control of surrounding zeros. Fixed-window local convergence does not by itself control the globally closest pair.

## What is and is not concluded

The finite constructions refute reconstruction from particular static summaries. They do not refute the Montgomery pair-correlation conjecture, the full zeta/GUE conjecture, or RH.

The cartoons explain the scope of the supplied meeting note. They do not attempt to catalogue subsequent project results.

An actual-zeta application still requires an arithmetic estimate for a suitable higher-order statistic or for the environment of a close pair, at the required scales. The finite periodic scalar heat flow is not itself the zeta/Newman flow.

The question on the final panel is:

> Which prime statistic detects a close pair AND its surrounding zeros?

## Source map

- [Tao meeting note source](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/feat/tao-acue-meeting-note/docs/Tao-ACUE-meeting.tex).
- [Exact pair-matched scalar-heat examples](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/codex/astra-research/research/counterexamples/pair-matched-flow/PAIR_MATCHED_HEAT_COUNTEREXAMPLES.md).
- [Protected multitime DBM moments](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/codex/astra-research/research/counterexamples/stochastic-protection/AGENT_STOCHASTIC_PROTECTION.md): §§1–4, especially shared multitime weight budgets.
- [Selected CUE background estimate](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/codex/astra-research/research/dyson/round14/cue-selected-background/SELECTED_CUE_BACKGROUND.md) and its adjacent independent review.

The input PDF, local source paths, image hashes, and validation results are recorded in VALIDATION.json. Source references are internal project proofs, not claims of external peer review or formal verification.

## Rebuild and validation

Run:

```sh
python3 verify_examples.py
python3 build_pdf.py
```

The example checks use only Python's standard library. The PDF builder needs ReportLab and pypdf. It places the unchanged generated PNGs on two pages; it does not redraw or edit the artwork.

The scope is documentation only: two images, their PDF, exact captions, generation prompts, and numerical checks of the illustrated quantities. No performance claim is made. New theorem searches, formal proof verification, and arithmetic transfer are postponed. Reverting this documentation addition is the rollback.
