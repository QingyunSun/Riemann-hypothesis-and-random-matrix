# Independent review of the finite clipped-Gram bridge

Date: 2026-11-01, America/Los_Angeles; checked 2026-11-02 UTC. Reviewer: stationary-challenge agent. **Verdict: PASS for the precise finite three-mode statement.** No transfer to the actual zeta window is established.

## 1. Matrices, exact spectra, and the determinant sign

Take A={0,1,2,4,7,8}, B={3,5,6,9,10,11} on the twelfth roots of unity, with angles theta_a=2 pi a/12. Define V with rows indexed by the six occupied sites and columns k=0,1,2 by

\[
V_{a,k}=3^{-1/2}e^{ik\theta_a},\qquad
U=VV^*,\qquad M=V^*V.
\]

Thus U is the proposed unit-diagonal six-by-six Gram matrix. Its three nonzero eigenvalues are those of the positive three-by-three matrix M. The remaining three eigenvalues are zero; they must not be silently removed when taking a trace of a function with nonzero value at zero.

Writing p_j=sum exp(ij theta_a), we already have the exact evaluations

\[
p_1(A)=(1+i\sqrt3)/2,\qquad p_2(A)=(1+3i\sqrt3)/2,
\]

and both change sign for B. In particular, |p_1|^2=1, |p_2|^2=7 and T=Re(p_1^2 conjugate(p_2)) is 2 on A and -2 on B. Up to complex conjugation of the whole matrix, which does not change its eigenvalues,

\[
M=\begin{pmatrix}
2&p_1/3&p_2/3\\
\overline{p_1}/3&2&p_1/3\\
\overline{p_2}/3&\overline{p_1}/3&2
\end{pmatrix}.
\]

Direct expansion gives

\[
\operatorname{tr}M=6,\qquad
\operatorname{tr}M^2=12+\frac29(2|p_1|^2+|p_2|^2)=14,
\]

\[
\det M=8-\frac29(2|p_1|^2+|p_2|^2)+\frac{2}{27}T
=6+\frac{2T}{27}.
\]

The determinant values are therefore 166/27 and 158/27. The common second elementary symmetric coefficient is (36-14)/2=11, so the characteristic polynomials are exactly lambda^3-6 lambda^2+11 lambda-det M. Also M_B=4I-M_A, which checks the spectral reflection directly.

Let x_1,x_2,x_3 solve x^3-x-4/27=0. There is one root in (-1,-1/2), one in (-1/2,0), and one a in (1,11/10): the polynomial has signs negative, positive, negative, positive at -1,-1/2,0,11/10, and its value at 1 is negative. These three disjoint intervals exhaust its roots. This is an exact sign certificate, not numerical root selection. The nonzero spectra are {2+x_j} for A and {2-x_j} for B. All six listed values are positive. Vieta gives sum x_j^2=2.

## 2. The clipped trace and the three zero modes

Use precisely

\[
\Psi_1(\lambda)=(\lambda-1)^2-(\lambda-2)_+^2.
\]

The **first square is not clipped**. In particular Psi_1(0)=1. The common untruncated trace for the full six-by-six matrices is

\[
\operatorname{tr}(U-I)^2=14-2\cdot6+6=8.
\]

For A only the eigenvalue 2+a exceeds 2, and its removed square is a^2. For B the two eigenvalues corresponding to the negative x-roots exceed 2; their removed squares sum to 2-a^2. Consequently

\[
\operatorname{tr}\Psi_1(U_A)=8-a^2,\qquad
\operatorname{tr}\Psi_1(U_B)=6+a^2,
\]

\[
\boxed{\operatorname{tr}\Psi_1(U_A)-\operatorname{tr}\Psi_1(U_B)
=2-2a^2<0.}
\]

Equal full pair-difference data therefore do not determine this clipped trace for the specified circular three-mode kernel. The first two spectral moments are equal, but the determinant, and hence a higher spectral statistic, is not. As a further exact consistency check, tr M_A^3-tr M_B^3=8/9 by Newton's identity.

## 3. Probability-law normalization

The prior independent pair review established two disjoint dihedral orbits, each of size 24 and ACUE probability 1/72. The kernel is invariant under rotation of all sites; reflection conjugates its matrix and leaves its spectrum unchanged. Hence the displayed trace is constant on each orbit.

Under the previously defined tilt P_epsilon=P_ACUE(1+epsilon(1_OA-1_OB)), the expectation difference from ACUE is exactly

\[
\frac{\epsilon}{72}(2-2a^2)
=\boxed{\frac{\epsilon(1-a^2)}{36}}.
\]

The joint law of all the original pair-difference data and the sorted gap list remains unchanged, as established in `../pair-matched-flow/AGENT_PAIR_REVIEW.md`. This statement concerns the full law of that summary; its preservation does not preserve the extra clipped-Gram statistic.

## 4. Scope of the external mixed-multiplicity theorem

The definitions and parameter condition were checked directly in [Knausgård, arXiv:2609.33043v2, Theorem 2](https://arxiv.org/html/2609.33043v2): for diagonal multiplicities between 1 and 2, its sufficient condition is c>=max(1+tau,2+tau/2). Thus tau=1 requires c>=5/2. The theorem cannot be cited with c=2 to handle arbitrary mixed multiplicities.

For D=I alone, there is a separate elementary identity, using tr U=6:

\[
\operatorname{tr}\varphi_2(U)-6=\operatorname{tr}\Psi_1(U),
\qquad \varphi_2(x)=x^2-(x-2)_+^2.
\]

This identity requires no mixed-multiplicity theorem and does not extend its permitted parameters. The finite diagnostic also uses a different kernel and a different clipping threshold from the paper's Euclidean probability window and tau=12/5. The separate half-lattice estimate in `ZETA_STATISTICS_SCAN.md` shows that the latter window stays strictly below its clipping threshold, so its trace reduces there to an ordinary pair statistic. Nothing in the present example contradicts that inactivity result.

The exact calculation is accepted as a model-level bridge from a higher phase statistic to an active spectral clipping diagnostic. It supplies no zero-count improvement, no actual-zeta signed correlation estimate, and no global novelty claim. The symbolic replay below verifies its finite algebra only.

## 5. Verification

`CLIPPED_GRAM_CHECK.py` independently builds the exact radical matrices and checks their first three moments, determinants, characteristic polynomials, spectral reflection, rational root sign brackets, trace decomposition and orbit normalization. All **19 exact checks passed**, as recorded in `CLIPPED_GRAM_CHECK_OUTPUT.json`. No floating-point value is used to establish a sign or select a root.

The root's complete `../pair-matched-flow/CLIPPED_GRAM_BRIDGE.md` was read and agrees with this derivation. It explicitly retains all three zero eigenvalues and obtains the common quadratic trace 8. Its inactive-threshold negative control at tau=4 is also correct: the largest eigenvalue is less than 31/10, hence below the threshold 5.

The reviewed snapshot hashes are:

| File in `../pair-matched-flow/` | Bytes | SHA256 |
|---|---:|---|
| `CLIPPED_GRAM_BRIDGE.md` | 6707 | `db79e661b1d4a8ecc1b6b63aeb56d3f758d5a6361f918ba79f1ccb1ea5e6621a` |
| `check_clipped_gram.py` | 3694 | `498a6bbe9b134a747230a4589e2048b49c129b0ef369bfd3532c637a40695279` |
| `CLIPPED_GRAM_CHECKS.json` | 1357 | `5c6f70fa1be9d5feb494ffa27c710e30c7488c46441c0acde4e0098792e213d4` |
