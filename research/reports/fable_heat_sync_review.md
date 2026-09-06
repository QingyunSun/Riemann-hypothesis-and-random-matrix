# Pinned Fable intake: heat flow, function fields, and LR hard cores

2026-09-05. This review reads the existing public Fable work at **a408e7050fffc74459b3c83fafa5ac03c8b7dea6** in galpha-ai/Alpha-devbox, the PR #11 head supplied for this intake. It uses git ls-tree and git show at that exact commit. No Claude session was started, no task was sent to Fable, and none of its experiments was rerun.

Companion evidence file: fable_heat_sync_inventory.json. It records the pinned revision, source hashes, line numbers, expected-report presence, and public journal event counts. The main coordinator is mirroring the source folder separately.

## 1. Main conclusion

This public snapshot contains useful new mathematical formulations and experimental scripts, but **no completed heat-flow, function-field, or LR proof report and no committed output dataset for those scripts**. They must not be merged into the theorem ledger as completed proofs or completed numerical results.

Three concrete defects were found in the available source:

1. The explicit CUE-background constant assembly reverses an inequality in its second regime. A limited repair is possible, but the displayed global constant is not certified by the committed argument.
2. The pair-LP ansatz assumes a compactly supported correction whose Fourier transform vanishes on an interval. In the exact continuum problem this forces the correction to vanish identically. Its numerical feasibility boundary therefore cannot be treated as a general LR upper bound.
3. The function-field support code assigns the wrong Weyl density to the negative-determinant component of the even orthogonal group. Its matrix sampler and claimed reference rejection sampler target different laws.

There is no new evidence here contradicting our audited finite-CUE isolated-pair depth theorem, the all-forward-time protected-trace obstruction, or the force-energy identities. The correct SO(odd) three-body example instead illustrates why an isolated-pair assumption is necessary.

## 2. What is actually present

The [claims ledger at the pinned commit](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/CLAIMS.md) has seven claim rows, all from the prime-certificate cluster D1. It has no completed A-cluster heat claim or B-cluster LR/function-field claim.

The [coordination file](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/FABLE_COORDINATION.md) acknowledges the old endpoint-bound error, the Lean collision-time gap, the distinction between strong and density-tolerant AH, and the need for outward-rounded prime certificates. These acknowledgements agree with Astra's audit.

However, the coordination text refers to a repaired theorem report as though its argument were already available; the referenced report is absent from this commit. The same issue applies to the future files in the [round-two plan](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/ROUND2_PLAN.md).

The following planned reports are absent:

- r1_theoremB_repair.md, r1_cue_background.md, r1_cbe_background.md;
- r1_levelB_barrier.md, r1_small_gaps.md, r1_zeta_numerics.md, r1_structure_review.md;
- r2_dynamic_universality.md, r2_marked_depth_proof.md, r2_acue_rho_bound.md;
- r2_lr_hardcore_lp.md, r2_function_field.md, r2_dbm_relaxation.md.

There are corresponding background, function-field, and LR scripts. Their declared output paths under overnight/fable/data are not present in this commit. This is an observation about committed evidence, not a statement that no computation happened in Fable's private running environment.

The public harness export has six workflow journals. Five contain only two “started” entries each. The remaining journal contains three “started” entries and one result: the completed H2 prime-certificate report. The agent metadata files contain agent type and spawn depth, while the index leaves labels, status, and model columns blank. These exports do not provide an independent-refuter completion record for heat/FF/LR at this head.

The substantive completed report visible here is r1_h2_interval_cert.md, which belongs to the prime-audit intake rather than this heat review. Its stated H3 result is an \(M_k\) certificate, while the large H3 tuple is explicitly not reverified in the claims ledger. Preserve that distinction.

## 3. CUE background work: useful local structure, uncertified global constant

### 3.1 What agrees with the audited repair

The [Theorem-B check script](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r1_theoremB_check.py#L1) uses the correct attractive coefficient flow and root ODE. It replaces the erroneous single-endpoint csc-squared bound with the maximum of both endpoint values.

Its exact bracket

$$
\cot(x_b/2)-\cot(x_a/2)
=\frac{\sin(g/2)}{\sin(x_b/2)\sin(x_a/2)},\qquad x_a=x_b+g,
$$

is correct. Since both sine factors are positive for the chosen representatives,

$$
B=2\sin(g/2)S_{\rm exact}
\le gS_{\rm exact}\le gS_{\rm avg}\le gS_*.
$$

The middle comparison is the arithmetic-geometric-mean inequality applied to the endpoint reciprocal sine values. These are valid local algebraic repairs. They do not themselves control a moving background up to collision.

The script explicitly probes a three-cluster configuration where the background grows by more than a factor two; this is a useful adversarial test, not a proof that all other configurations satisfy a window bound. Its “ACUE-type” random subsets are uniformly sampled non-clock subsets, not Vandermonde-weighted ACUE samples. That is acceptable for deterministic stress testing, but their sample frequencies are not ACUE probabilities.

### 3.2 The exact three-point constant is a useful route

The [background-constant script](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r1_cue_background_constants.py) formulates a global determinantal three-point bound using alternants and the inequality \(|s_\lambda(z)|\le s_\lambda(1,1,1)\) on the torus. The coefficient

$$
A_3(N)=\sum_{0\le m_1<m_2<m_3<N}
[(m_2-m_1)(m_3-m_1)(m_3-m_2)]^2
=\frac{N^3(N^2-1)^2(N^2-4)}{2160}
$$

leads to

$$
\rho_3(\theta_1,\theta_2,\theta_3)
\le \frac{A_3(N)}{4(2\pi)^3}
\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^2.
$$

The factor \(1/4\) comes from the denominator \(2\) in the three-variable Weyl dimension formula, squared. This agrees with the \(N^9\) three-point Vandermonde structure used in our audited CUE transfer. It is a promising explicit refinement rather than evidence of a different heat-flow mechanism.

The script's polynomial identity tests and sampled determinant comparisons should be described as checks until accompanied by its missing written report. Polynomial interpolation through finitely many values is not an all-\(N\) proof unless the degree bound is also justified.

### 3.3 Definite sign error in the second-regime tail assembly

At [line 159](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r1_cue_background_constants.py#L159), the code reasons

$$
N<(L/4)^3\quad\Longrightarrow\quad \frac1N<\frac{64}{L^3}.
$$

The conclusion is reversed: reciprocation gives \(1/N>64/L^3\). Thus a bound \(C/N\) from a cutoff gap \(4/N\) cannot be converted to \(64C/L^3\) by that step.

A possible repair of this single step uses the deterministic fact \(\delta_{\min}\le2\pi/N\). In the nontrivial remaining regime

$$
4N^{1/3}<L\le2\pi N^{1/3},
$$

one has \(L^3\le(2\pi)^3N\), hence

$$
\frac CN\le\frac{(2\pi)^3C}{L^3}.
$$

For \(L>2\pi N^{1/3}\), the event \(\delta_{\min}>LN^{-4/3}\) is empty. This suggests replacing 64 by \((2\pi)^3\) in the indicated regime conversion. It does not validate every other missing step in the announced background-tail theorem.

The script assigns “pass=True” to assembled constants rather than verifying their probability derivation. Its displayed bounds \(P(S_*>MN^2)\le C M^{-3/8}\) and the refinement with exponent \(-1/2\) must remain unproved in this intake. A software pass flag is not a mathematical certificate of that tail argument.

Our audited Galilean isolated-pair proof does not depend on this constant assembly: it obtains \(\delta^2B\to0\) from a triple-free packing event. Therefore this defect does not invalidate our finite-CUE result.

## 4. Function-field support: correct identities, wrong orthogonal reference law

### 4.1 Valid finite polynomial identities

The [function-field depth core](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r2_ff_depth_core.py) implements the same attractive coefficient flow

$$
P_s(z)=\sum_j a_j e^{sj(M-j)}z^j.
$$

At a double root \(z_0\), it has

$$
\partial_sP_s(z_0)=-z_0^2P_s''(z_0),
$$

because the operator is \((M-1)z\partial_z-z^2\partial_z^2\) and \(P_s'(z_0)=0\). For a simple double root this supplies a nonzero transverse parameter derivative. It does not, by itself, settle all multiple or symmetry-forced collision strata needed for a general almost-everywhere continuity theorem.

The genus-two palindromic reduction is also correct:

$$
P_s(z)=z^4+A e^{3s}z^3+B e^{4s}z^2+A e^{3s}z+1
$$

reduces, after division by \(z^2\), to

$$
Q_s(x)=x^2+A e^{3s}x+B e^{4s}-2,\qquad x=z+z^{-1}.
$$

Bulk and edge collisions are detected algebraically by its discriminant and the equations \(Q_s(2)=0\), \(Q_s(-2)=0\). The numerical implementation uses a finite sign grid and a time cap; those are numerical detection choices, not a certified first-root solver.

### 4.2 The forced-root three-body example is real and informative

For the configuration \(\{1,e^{i\theta},e^{-i\theta}\}\), put \(A=1+2\cos\theta\). Then

$$
P_s(z)=z^3-Ae^{2s}z^2+Ae^{2s}z-1
=(z-1)(z^2+(1-Ae^{2s})z+1).
$$

If \(0<\theta<2\pi/3\), so \(A>0\), the first collision occurs at \(z=1\) when \(Ae^{2s}=3\). Consequently

$$
D=\frac12\log\frac3{1+2\cos\theta}
=\frac{\theta^2}{6}+O(\theta^4).
$$

This matches the formula in the [hard-edge routine](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r2_ff_depth_core.py#L317). The routine does not explicitly enforce the domain \(0<\theta<2\pi/3\); the small-angle calls shown in the check script lie inside it. At \(\theta=2\pi/3\) the configuration is a stationary clock. For \(2\pi/3<\theta<\pi\), the first collision is at \(-1\), and the different expression is \(D=\frac12\log(-1/A)\).

For \(\theta\downarrow0\), the minimum gap is \(\delta=\theta\) and \(D/(\delta^2/8)\to4/3\). This is not a counterexample to our theorem: a third root is only a gap-scale distance from the chosen pair, so \(\delta^2B\) does not tend to zero. It is a clean explanation of why forced symmetry and three-point clustering must be handled separately in orthogonal models.

### 4.3 Definite Weyl-density mismatch for the even negative component

The code defines O_minus as \(O^-(2N+2)\), with both forced eigenvalues \(+1\) and \(-1\). Yet [lines 367–368](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r2_ff_depth_core.py#L367) and the rejection sampler at lines 388–389 multiply the free-angle density by

$$
\prod_j\cos^2(\theta_j/2).
$$

For \(O^-(2N+2)\), the correct factor is

$$
\prod_j\sin^2\theta_j,
$$

the same free-angle factor as \(USp(2N)\). The half-angle cosine factor belongs instead to \(O^-(2N+1)\). This is explicitly distinguished in [Meckes, The Random Matrix Theory of the Classical Compact Groups, Theorem 3.5, printed page 76](https://case.edu/artsci/math/mwmeckes/elizabeth/Haar_book.pdf#page=76).

There is also an elementary diagnostic independent of the formula table. In even dimension, \(U\mapsto-U\) preserves the negative-determinant component and its Haar measure. For rank \(N=1\), this maps the free angle \(\theta\) to \(\pi-\theta\), so its density must be reflection symmetric. The claimed \(\cos^2(\theta/2)\) density is not. It would give

$$
\mathbb E\cos\theta
=\frac{\int_0^\pi\cos\theta\cos^2(\theta/2)\,d\theta}
{\int_0^\pi\cos^2(\theta/2)\,d\theta}
=\frac12,
$$

whereas reflection symmetry requires zero. Thus the matrix Haar sampler and the coded rejection sampler cannot both pass as implementations of the same law. No rerun is needed to establish the mismatch.

### 4.4 What remains unproved for function fields

No curve-family equidistribution theorem with its hypotheses, exceptional set, order of limits, or uniformity is written out in the available snapshot. The fixed-rank continuous-mapping route is plausible only after establishing the required almost-everywhere continuity of the chosen depth functional. Passing subsequently to growing rank needs the relevant group-specific extreme-gap law and separate hard-edge/forced-root analysis.

The pointwise continuity demonstration in the check script is a numerical path through a few configurations, not an almost-everywhere theorem. Equality of two initial gaps also does not by itself prove that they collide simultaneously under different backgrounds. These missing steps remain exactly the kind of obligations recorded in our earlier audit.

## 5. LR work: valid test families versus an invalid continuum ansatz

### 5.1 A precise obstruction in the pair-LP parametrization

The [pair-LP script](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r2_lr_pair_lp.py#L11) writes

$$
g=g_{\rm sine}+u,\qquad u=0\text{ outside }[-X,X],
$$

and aims to impose \(\widehat u(\alpha)=0\) throughout \((-1,1)\). For a compactly supported integrable function or finite signed measure, \(\widehat u(z)\) is entire in the complex variable \(z\). If it vanishes on a real open interval, the identity theorem forces it to vanish identically, and Fourier uniqueness gives \(u=0\).

But a positive hard core requires \(u=-g_{\rm sine}\) on a nonempty interval around zero. Since \(g_{\rm sine}(x)>0\) for nonzero sufficiently small \(x\), that is impossible. Thus the exact continuum version of this compact-correction ansatz is infeasible for every \(c>0\), including the known half-lattice model that motivated the programme.

Sampling Fourier constraints at finitely many frequencies avoids the analytic contradiction only by no longer imposing the exact mimicry condition. This does not turn the finite-support family into an outer relaxation containing all admissible stationary processes. Therefore an infeasibility threshold from this code is not a rigorous general upper bound on LR \(\mu\), and shrinking the grids alone cannot repair the logical direction.

There is an additional implementation-level overstatement at line 54: the “minimum over a cell” is approximated using nine sample points. A sampled minimum is at least the true minimum. Its negative is therefore not a certified conservative lower constraint on \(u\) that guarantees \(g\ge0\) throughout the cell.

### 5.2 The count-variance and test-function formulations are useful

The [triangle certificate](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r2_lr_triangle_cert.py) has a valid underlying necessary condition. For a stationary intensity-one process with hard core \(c\), an interval of length \(L\le c\) contains at most one point almost surely, modulo irrelevant endpoint events. Hence

$$
\operatorname{Var}N[0,L]=L-L^2.
$$

If its spectral measure agrees with the sine structure factor \(|\alpha|\) on the unit band and is nonnegative outside, then

$$
L-L^2\ge
2\int_0^1\frac{\sin^2(\pi L\alpha)}{\pi^2\alpha}\,d\alpha.
$$

This is a genuine analytic necessary inequality under the stated process hypotheses. The committed file computes a root numerically, but its numerical output is not committed here; this intake does not claim a new bound.

The [weighted-window eigenvalue formulation](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r2_lr_pd_window_eig.py) extends the same variance argument to real weights on an interval. The [Selberg-type formulation](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r2_lr_selberg_eig.py) instead uses \(T(x)=(c^2-x^2)|F(x)|^2\) with band-limited \(F\). Their continuum inequalities are sensible test families; the numerical eigenvalue computations still require certified quadrature and discretization error bounds before they become numerical certificates.

The [general band-limited LP](https://github.com/galpha-ai/Alpha-devbox/blob/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/scripts/r2_lr_bandlimited_lp.py) itself acknowledges that rational-knot piecewise-linear Fourier profiles create a periodic \(x^2T(x)\), obstructing a global sign certificate in that finite family. A tail penalty does not by itself certify the sign between the sampled spatial grid points. Any claimed improvement from that script would need a complete continuum certificate, not just a positive floating LP objective.

## 6. Conflict matrix and recommended handoff classification

| Fable item at the pinned head | Relation to audited Astra work | Handoff status |
|---|---|---|
| Endpoint maximum repair and exact cotangent bracket | Agrees | Preserve as valid local algebra |
| Claimed explicit CUE-background tail constant | Contains a reversed inequality; written proof absent | Unproved, with exact defect and partial repair recorded |
| CUE three-point Vandermonde bound structure | Agrees with our triple-free route | Useful independent formulation; no new theorem claim |
| SO(odd) three-body depth \(\theta^2/6\) | Outside isolated-pair hypotheses | Valid finite example, with domain restriction |
| Even \(O^-\) Weyl reference density | Wrong group factor | Repair before interpreting group-specific diagnostics |
| Function-field universality | Missing continuity/equidistribution/limit-order proof | Open |
| Compact-correction LR pair LP | Does not contain the target continuum models | Invalid as a general upper-bound certificate |
| LR window/Selberg analytic inequalities | Plausible and directly checkable under stated hypotheses | Valid formulations; numerical certification absent |
| Proposed DBM relaxation experiment | Only a planned report at this head | No completed evidence to compare |
| Protected trace equality and force-energy separation | No contradicting result in this snapshot | Our independent audited conclusions unchanged |

The archive should preserve the original source verbatim, attach this pinned review, and avoid upgrading planned filenames, printed PASS labels, or uncommitted output paths into completed discoveries. A later Fable commit may supply repairs or full reports; it should receive a new pinned intake rather than silently replacing this record.
