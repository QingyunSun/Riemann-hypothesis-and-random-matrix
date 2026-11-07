# A quantitative protected-survival counterexample

This note strengthens the eleven-root construction from the November checkpoint. At elapsed scalar-heat time

\[
s_0=\log(85/84),
\]

there is a strictly positive law on the ACUE support with the same complete pair/gap-summary law and all the same protected balanced trace expectations, whose survival probability exceeds that of ACUE by **more than 0.0175**. The original ACUE probability is approximately 0.1981043103. The new probability lies between 0.2156294303856491 and 0.2156294309055878. Thus the difference is at least 1.75 percentage points, while all configured weights remain positive.

A milder version keeps every density between 0.499999993 and 1.500000007 times its original ACUE density and changes survival by more than 0.0088. The stronger version scales this exact perturbation by 99/50. Its density stays between 0.0099999865 and 1.9900000135 times the original density. These are finite, explicitly specified laws.

## The probability coordinates

Use the 1,489 pairs of complementary dihedral orbits from `base.py`, copied from the checked-in eleven-point verifier. In each pair choose canonical representatives \(A_i,B_i\). The pair shares both the full ordered difference counts and the sorted adjacent gaps. The original ACUE mass of each orbit in the pair is the same number

\[
q_i=\frac{|\operatorname{Orb}(A_i)|}{22^{11}}
\prod_{x<y\in A_i}4\sin^2\frac{\pi(y-x)}{22}.
\]

Together, the paired orbits carry 0.4326384603063366 of the original ACUE mass. Let \(d_i\) be the certified survival indicator of \(B_i\) minus that of \(A_i\). Transfer \(q_i h_i\) from \(A_i\) to \(B_i\), uniformly within the orbits. This preserves the static-summary distribution exactly, and is strictly positive whenever \(|h_i|<1\).

For each protected trace test \(f_j\), the moment constraint is

\[
\sum_i q_i\bigl(f_j(B_i)-f_j(A_i)\bigr)h_i=0.
\]

Every selected row is twice the real part of a balanced trace product of degree at most eleven, with an odd number of trace factors. For a complementary orbit pair, its difference is therefore minus four times the real product at \(A_i\). Rotation and reflection preserve this real test. The previous Weyl/Jacobi argument bounds the entire space of these constraint rows by 964. The matrix used below contains 964 independent rows, so enforcing them enforces every protected balanced test. Uniform rotation by a grid site, already included in the dihedral averaging, also sets every protected unbalanced expectation to zero: its nonzero weight difference has absolute value at most eleven, below the grid period twenty-two. No continuous rotation or enlargement of the support is needed.

## Search and the exact law

The floating search solves a box-constrained linear program in \(h\), with \(|h_i|\le1\) and objective \(\sum_i q_i d_i h_i\). It gives a value approximately 0.01770214175. This search value is a numerical optimization result; no optimality claim is needed for the certificate.

The reproducible certificate uses the dyadic coordinates in `candidate.json`. It records 964 protected trace rows, 964 dependent coordinates, their dyadic row scales, and an approximate vector \(h^0\). Each hexadecimal float string denotes its exact dyadic rational. Fix the remaining 525 coordinates to the recorded values and solve the 964 selected protected equations exactly for the dependent coordinates. This uniquely defines a vector \(h^*\) over the real cyclotomic field. It is this exact vector that defines the probability law. The original floating LP solution is only a way of locating it. The optional `export_candidate.py` reconstructs the seed object from the saved search matrices; it writes a separate filename so the committed certificate input cannot be overwritten by a new floating search.

Let \(B\) denote the selected weighted and scaled matrix, and \(C\) its square submatrix on the dependent coordinates. Compute a binary64 approximate inverse \(R\), then treat each entry of \(R\) as an exact dyadic rational. The outward-rounded 160-bit Arb calculation verifies

\[
\|I-RC\|_\infty<4.989\times10^{-6},\qquad
\|R Bh^0\|_\infty<3.920\times10^{-9}.
\]

The Neumann-series argument proves that \(C\) is invertible and that the exact correction obeys

\[
\|h^*-h^0\|_\infty<3.920\times10^{-9},
\]

with the correction supported only on the dependent coordinates. The same certificate encloses the objective directly, allowing for this correction. It gives

\[
0.0088510707393131
<\sum_i q_i d_i h_i^*
<0.0088510710019084.
\]

Moreover \(\|h^*\|_\infty<0.5000000068\). Scaling by 99/50 preserves strict positivity and gives the stated probability increase above 0.0175. Both constructions satisfy all moment equalities exactly; their rigor does not depend on treating a small floating residual as zero.

The survivor indicators are recomputed with the certified Hermitian Newton-sum criterion in the parent verifier. The candidate's stored indicator list must match the recomputation and the previously pinned SHA-256. The total original probability is independently summed over all 16,159 dihedral orbits and encloses one. That enumeration also gives the original survival probability.

## What periodic lifting does to the available mass

For a seed configuration with \(n\) roots, lift it to the full preimage under \(z\mapsto z^r\), giving \(N=nr\). If \(p_n(S)\) is its individual ACUE atom mass, the lifted atom has mass

\[
p_{nr}(\operatorname{lift}_r S)=p_n(S)^r.
\]

Indeed, differentiating \(P_S(z^r)\) and multiplying the derivative moduli over its \(nr\) roots gives \(r^{nr}|\Delta(S)|^{2r}\). Division by \((2nr)^{nr}\) yields the identity. The dihedral orbit cardinality is preserved by the lift. The whole lifted support has total mass

\[
M_r=\sum_{|S|=n}p_n(S)^r
\le \bigl(\max_S p_n(S)\bigr)^{r-1}
\le 2^{-n(r-1)}.
\]

The last inequality follows from the rank-n projection kernel's diagonal n/(2n)=1/2 and Hadamard's determinant bound; a clock configuration attains the atom bound. In the constructed lift perturbations the total mass on the lifted support remains \(M_r\). Thus their total variation distance and every survival-probability difference are at most \(M_r\), even when the redistribution within that support is large.

For the eleven-point seed, summing all atom powers with Arb gives

| Lift factor r | Total ACUE mass of the entire lifted support |
|---|---|
| 2 | 0.00002353051503228758 |
| 3 | 0.000000001689923184198222 |
| 4 | 0.0000000000002703540711351132 |

This exposes a quantitative limitation of the current lifting argument. It supplies examples at arbitrarily large sizes, but the available mass decays quickly. A macroscopic limiting survival separation would need probability changes on a much larger portion of the support.

## Reproduction

`base.py` is the copied checkpoint verifier. `candidate.json` is the compact numerical seed, approximately 89 KB. `certify.py` is the interval certificate, and `baseline.py` computes the full ACUE baseline and lift-support masses. The numerical search scripts `quantify.py` and `pivot.py` record how the seed was found; their large intermediate NPZ files are unnecessary for certificate replay.

Use Python with NumPy, SciPy and python-flint. Run `python certify.py` and `python baseline.py` in this directory. `certificate.json` and `baseline.json` are the output receipts. Float inverse computation may change slightly between numerical-library versions, but its validity and the final explicit lower bounds are checked by Arb on every run. Every source, candidate and matrix is reconstructed locally; no external data or API is required.

This result concerns the finite deterministic scalar heat flow. Its protected-moment and static-summary equalities do not evaluate any statistic of the true zeta zeros, and the construction by periodic lifting supplies no stationary infinite-volume discrepancy of positive size.
