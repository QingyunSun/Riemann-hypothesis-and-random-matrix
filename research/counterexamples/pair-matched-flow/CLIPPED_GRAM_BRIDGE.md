# A clipped Gram statistic separates the pair-matched ACUE example

Date: 2026-11-01 Pacific / 2026-11-02 UTC. Author: Astra root.

This is an exact finite-model calculation connecting our counterexample to a structure found in the recent literature. It is not a new theorem about zeta zeros or a claim of historical novelty. The ordinary proof below and the accompanying exact algebra check have different roles: the proof establishes the claim; the script checks its finite algebra and root locations.

## 1. Precise question

Can two configurations with the same complete pair measure and the same entire nearest-neighbour gap histogram have different clipped Gram spectra? Yes, even on the support of the same finite ACUE law.

Use the six-point configurations on the twelve roots of unity

\[
A=\{0,1,2,4,7,8\},\qquad B=\{3,5,6,9,10,11\}.
\]

Their complete ordered cyclic pair counts agree, and their sorted cyclic gaps are both \((1,1,1,2,3,4)\). The proof and the probability normalization are in [PAIR_MATCHED_HEAT_COUNTEREXAMPLES.md](PAIR_MATCHED_HEAT_COUNTEREXAMPLES.md). Put \(\theta_j=2\pi j/12\) and define the three-mode Gram matrix on the six occupied sites by

\[
U_{ab}=\frac13\sum_{k=0}^2e^{ik(\theta_a-\theta_b)}.
\]

It is Hermitian positive semidefinite, has diagonal one, and has rank three. It is covariant under global rotation and reflection; its eigenvalue statistics therefore define observables of the dihedral orbit. It is a circular three-mode kernel, not the Euclidean window of the zeta paper discussed below.

## 2. Exact spectra from the mixed cubic

Write \(V_{ak}=e^{ik\theta_a}/\sqrt3\), so \(U=VV^*\). Its three nonzero eigenvalues are those of \(M=V^*V\), whose diagonal entries are two. The trace formulas give

\[
\operatorname{tr}U=6,\qquad
\operatorname{tr}U^2=\frac{3\cdot6^2+4|p_1|^2+2|p_2|^2}{9}=14.
\]

For A we have

\[
p_1=\frac{1+i\sqrt3}{2},\quad
p_2=\frac{1+3i\sqrt3}{2},\quad
T=\Re(p_1^2\overline{p_2})=2.
\]

For B, both displayed traces change sign and T becomes −2. Consequently

\[
\det M=\frac{6^3-6(2|p_1|^2+|p_2|^2)+2T}{27}
=\begin{cases}166/27&A,\\158/27&B.\end{cases}
\]

The two nonzero characteristic polynomials are

\[
\lambda^3-6\lambda^2+11\lambda-166/27,
\qquad
\lambda^3-6\lambda^2+11\lambda-158/27.
\]

Let \(x_1,x_2,a\) be the three roots of \(x^3-x-4/27=0\). There is one root in each of \((-1,-4/5)\), \((-1/5,0)\), and \((1,11/10)\). This follows from the opposite endpoint signs on these disjoint intervals and the degree-three bound on the number of roots; the checker also certifies it by exact root counting. The A eigenvalues are \(2+x_1,2+x_2,2+a\), the B eigenvalues are \(2-x_1,2-x_2,2-a\), and both matrices have three additional zero eigenvalues. Vieta gives

\[
x_1^2+x_2^2+a^2=2,\qquad a>1.
\]

In particular, the Gram matrices have the same trace and squared trace, but different spectra. Also \(\operatorname{tr}U_A^3-\operatorname{tr}U_B^3=8/9\), which makes the missing joint information explicit.

## 3. The clipped difference and a positive-law perturbation

Define

\[
\Psi_1(\lambda)=(\lambda-1)^2-(\lambda-2)_+^2.
\]

The untruncated squared terms have the same trace for A and B. The positive parts for A contribute \(a^2\), whereas those for B contribute \(x_1^2+x_2^2=2-a^2\). Thus

\[
\boxed{\operatorname{tr}\Psi_1(U_A)-\operatorname{tr}\Psi_1(U_B)
=2-2a^2<0.}
\]

This is an exact separation despite matching all pair data and the complete gap histogram. It does not depend on floating eigenvalue calculations.

For the actual ACUE law at N=6, each of the two disjoint dihedral orbits has mass \(1/72\). With the positive perturbation \(P_\varepsilon=P_{\rm ACUE}(1+\varepsilon h)\), where h is +1 on A's orbit, −1 on B's orbit and zero elsewhere, \(|\varepsilon|\le1\), we therefore get

\[
\mathbb E_\varepsilon\operatorname{tr}\Psi_1(U)
-\mathbb E_0\operatorname{tr}\Psi_1(U)
=\frac{\varepsilon(1-a^2)}{36}.
\]

The full joint law of the static pair measure and gap histogram remains unchanged. As in the original construction, the law changes the protected cubic moment T. It does **not** preserve every Tao low-bandwidth mixed moment and is not a counterexample to full AH mimicry.

## 4. What this says about the new clipped-Gram method

The inspiration is the spectral defect \(\operatorname{tr}\Psi_\tau(U)\) in [Knausgård, arXiv:2609.33043v2](https://arxiv.org/html/2609.33043v2). This example proves that such a nonlinear spectral statistic can retain information discarded by a pair-energy summary. It does not verify that paper's seven-point certificate, analytic assembly, or zeta proportion.

There are two essential qualifications.

1. **Thresholds matter.** The paper's mixed-multiplicity theorem requires \(c\ge\max(1+\tau,2+\tau/2)\); for \(\tau=1\), one needs \(c\ge5/2\). Our calculation only evaluates \(\Psi_1\). It does not apply that theorem with an inadmissible choice c=2.
2. **The kernel matters.** For the paper's actual Euclidean window on distinct half-lattice points, the separate [source audit](../latest-literature-2026-11-01/ZETA_STATISTICS_SCAN.md) proves \(\|U\|<2.217\), below the paper's threshold \(1+\tau=3.4\). Its clipping is then inactive and the defect is pair-based. Our different three-mode kernel and threshold genuinely activate the clipping. Substituting them in the analytic zeta argument would require a new admissibility, energy and counting proof.

An internal negative control makes the issue visible even here: set \(\tau=4\), so the clipping threshold is five, above both spectra. Then both defects equal \(\operatorname{tr}(U-I)^2=8\), and the distinction disappears.

The resulting research question is precise: can one find an analytically admissible kernel and counting inequality whose retained nonlinear defect is active on the relevant AH models, and can one evaluate that defect for actual zeta zeros? This file completes the finite separation, not those two arithmetic/analytic steps.

## 5. Reproduction and scope

Run `python3 research/counterexamples/pair-matched-flow/check_clipped_gram.py` from the repository root with SymPy installed. Saved output is [CLIPPED_GRAM_CHECKS.json](CLIPPED_GRAM_CHECKS.json). The checker reconstructs both matrices from the occupied sites, checks pair/gap matching, exact characteristic polynomials, rational root isolation, the cubic trace difference and the inactive-threshold control.

No performance claim or benchmark is made. No Monte Carlo samples, external-paper interval certificate, Lean build, zeta-zero dataset, or prime-gap computation is used. Independent mathematical review is recorded separately in [CLIPPED_GRAM_REVIEW.md](../latest-literature-2026-11-01/CLIPPED_GRAM_REVIEW.md).
