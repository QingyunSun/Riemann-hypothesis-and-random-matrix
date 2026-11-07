# Research addendum: quantitative survival and a conditional zeta theorem

6 November 2026. This addendum supplements the full historical handoff in PR #6. The singular-series main term has now been evaluated; the required actual-prime discrepancy estimate remains open. Earlier intermediate records are retained and explicitly labelled as historical stages. Finite certificates, conditional theorems, numerical diagnostics and external source claims are distinguished.


---

# Quantitative ACUE counterexamples and a sharper zeta target

_Source: README.md_

6 November 2026. Incremental checkpoint following [PR #6](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/pull/6). The full 881-page historical handoff remains available there; this packet adds proofs and corrections rather than silently rewriting old records.

## What changed mathematically

**A finite existence result is now quantitative.** At N=11 and scalar-heat time s=log(85/84), an explicitly defined, strictly positive alternative to ACUE preserves the full joint distribution of pair-displacement counts and sorted adjacent gaps, together with all protected trace expectations. Its survival probability increases by more than 0.0175:

| Law | Probability of no collision by s |
|---|---:|
| ACUE | 0.198104310321809... |
| Constructed positive law | between 0.2156294303856491 and 0.2156294309055878 |

The exact law is a cyclotomic linear solve specified by a small dyadic seed. A floating LP locates the seed, but neither a floating residual nor an assumed numerical rank is used as proof. Independent 224-bit replay, separate Fourier-Gram weight checks and the previous independent survivor-classification algorithm support the certificate. See [finite theorem](finite/REPORT.md) and [independent audit](finite/INDEPENDENT_REVIEW.md).

**The periodic-lift route has an exact probability limitation.** A seed atom of mass p lifts to an atom of mass p^r. The mass of the full two-fold lifted support is exactly
\[
M_{n,2}=\frac{(2n)!}{n!(4n)^n}\sim\sqrt2 e^{-n}.
\]
At n=11 it is only 0.00002353051503. This identity uses the classical, already-proved Dyson constant-term theorem. Any static-summary-preserving law that agrees with ACUE outside the lifted support differs in every event probability by at most this support mass. Merely repeating the finite pattern cannot create a nonvanishing asymptotic distinction. See [proof and checks](PERIODIC_LIFT_MASS.md).

**A probabilistic issue in the zeta transfer can be closed under RH.** For every fixed unfolded window and fixed k, existing restricted Rudnick-Sarnak correlations imply a uniform kth-moment bound for its zero count. Hence cubic window scores are uniformly integrable. Full pair-displacement concentration on the half-grid then forces the cubic alias mean to vanish, by an explicit inequality. This corrects the earlier audit's suggestion that an additional unproved occupancy estimate was needed in the fixed-window RH setting. It does not apply to merely matching pair tests in the protected Fourier band.

**The conditional arithmetic packet theorem is now complete.** A raw, Fourier-localized triple variant vanishes on every translated half-grid, has exact sine-process expectation +1/5, and avoids separate high-frequency pair corrections. Its zeta average, under RH, reduces to a signed near-product correlation of
\[
(\Lambda(m)-1)\Lambda(n)(\Lambda(r)-1)
\]
with m near T^(6/5), n near T^(1/5), r near T^(7/5), and an oscillatory kernel around mn=r. A subsequent calculation evaluates the signed singular-series main term using the existing Fazzari-Gerspach Lemma 2.7. Under RH, the exact reduction is
\[
M_T=\frac15-\frac{\operatorname{Re}\mathcal R_T}{c_\psi}+o(1).
\]
Here \(\mathcal R_T\) is the explicitly defined endpoint-aware signed prime-pair discrepancy. A consistent localized Hardy-Littlewood estimate yields \(M_T\to1/5\); that estimate remains unproved. More weakly, any upper bound for the signed error strictly below \(c_\psi/5\) excludes the stated half-grid pair-concentration hypothesis under RH. See the [complete calculation](arithmetic/MAIN_TERM_THEOREM.md), [independent review](arithmetic/MAIN_TERM_INDEPENDENT_REVIEW.md), and [source-input audit](arithmetic/SOURCE_INPUT_AUDIT.md).

**Why a size estimate alone can fail.** For each fixed real \(c\), there are positive, independently assigned surrogate counting measures with integer weights on permitted multiples of \(n\) and signed residual tending to \(c\beta c_\psi\). Their cumulative discrepancies obey \(O_\varepsilon((T/n)T^\varepsilon)\) on the packet, and the occupied sites can avoid small prime factors in both linear forms up to \(K\log T\) for every fixed \(K>0\). Taking \(c=1\) cancels the whole main term. This is a counterexample to inferring a saving from those size and support conditions alone. It does not represent the actual primes by a common von Mangoldt sequence. The central comparison \(T/n=X^{4/7}\) is not uniform over the edges of a fixed-width packet. See the [construction and its limitations](arithmetic/SURROGATE_SHARPNESS.md).

## What the bounded-probe work contributes

[The bounded-probe note](bounded/REPORT.md) gives robust normalized and clipped variants, a rigorous sine-process sign on short windows, and a precise limitation: a finite-degree continuous correlation polynomial uniformly bounded on every finite configuration in a compact interval must be constant.

This explains why clipping cannot generally retain a fixed three-trace arithmetic formula. For actual zeta under RH and fixed window width, clipping is optional because count moments already control uniform integrability. These are structural statements, not a proof of the zeta/GUE conjecture.

## DBM and primary-source update

[The explicit clock example](source_refresh/DBM_BACKWARD_OBSTRUCTION.md) satisfies the Landon-Sosoe-Yau mesoscopic regularity hypotheses and optimal initial rigidity, yet Gaussian regularization changes a compact microscopic two-point statistic by at least \(1-8/\pi^2\) in the limit. This gives a concrete obstruction to inferring the original statistics from the regularized ones. The missing comparison is written as a Duhamel integral; this is an application of the known universality theorem, not a new universality claim.

[The live source audit](source_refresh/SOURCE_REFRESH.md) incorporates a distinct October manuscript claiming a 0.67353820 simple-critical-line proportion, with a new local-certificate architecture and explicit compiled-search trust dependencies. Its full computation was not rerun. Fable/PR 11 and the checked 186/182 source heads were unchanged at the audit snapshot. Better simplicity alone does not establish non-lattice spacing or the missing signed correlation.

## Files and reproduction

- finite/candidate.json: exact dyadic free coordinates and row/column selections; about 89 KB.
- finite/certify.py: reconstructs the selected algebraic system and verifies an interval certificate.
- finite/baseline.py: sums all 16,159 orbit masses and survivor probabilities.
- finite/check_weights.py: independent Fourier-projection determinant check of all 1,489 paired orbit weights.
- check_lift.py: direct lifted-atom identities, the closed purity formula and pair-fibre membership.
- bounded/check.py: supplementary deterministic inequality and combinatorial checks.
- arithmetic/REPORT.md: initial derivations, precise support ranges and primary references.
- arithmetic/MAIN_TERM_THEOREM.md: completed singular-series calculation, conditional theorem and exact cancellation threshold.
- arithmetic/MAIN_TERM_INDEPENDENT_REVIEW.md: independent proof and two multiplicity-safe count-moment arguments.
- arithmetic/SOURCE_INPUT_AUDIT.md: primary-source scope and an independent prime-modulus reduction.
- arithmetic/check_normalizations.py: numerical diagnostics only, not proof of the missing arithmetic premise.
- HANDOFF_ADDENDUM.md and HANDOFF_ADDENDUM.pdf: integrated reading copies.

From this directory, with Python 3.12, NumPy 2.5.4, SciPy 1.18.1 and python-flint 0.8.0:
```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python finite/certify.py
python finite/baseline.py
python finite/check_weights.py
python check_lift.py
python bounded/check.py
python arithmetic/check_normalizations.py
```
These versions were used for the root replay; they are not claimed to be the only compatible versions. The interval verifier may produce slightly different inverse-residual enclosures on another BLAS build, but checks the same explicit lower bound and defines the same exact law.

## Review boundaries and next work

The finite theorem has internal proofs and machine-checkable interval calculations. It is not yet externally reviewed or formalized in Lean. The zeta moment bound is a corollary of an existing theorem with its hypotheses checked. The signed prime discrepancy estimate remains open in this programme. The main-term calculation is now closed, so the packet theorem is conditional on that precise remaining input. No unconditional RH, Montgomery-Dyson, AH-refutation or improved prime-gap theorem is asserted.

The next analytic step is to bound the real signed discrepancy below its exact cancellation threshold. Under RH this functional is already bounded; the stated pair-AH would force it to tend to the specific positive value \(c_\psi/5\). The new calculation therefore identifies the precise cancellation that must be excluded. For a large-N model theorem, a successful perturbation must act outside the exponentially small repeated-pattern support.

[The direct discrepancy calculation](arithmetic/CONDITIONAL_NEXT.md) shows that a consistent localized square-root prime-pair error would be sufficient for the error stage on the central domain \(\alpha+3\beta<2\). The formerly unevaluated main term is now supplied by the complete calculation linked above; the earlier error-stage note is retained as a historical step.

[An endpoint audit](arithmetic/ENDPOINT_CORRECTION.md) identifies a defect in the literal two-sign uniform hypothesis printed in Fazzari-Gerspach v1. The conditional calculation here uses a separately stated, endpoint-aware local assumption. This is a source-formulation correction, not a refutation of classical Hardy-Littlewood.

No infrastructure changes, runtime optimization or performance claim are part of this packet. Postpone a new broad numerical search, a repeated 881-page rebuild, or a claimed famous-conjecture solution without the missing arithmetic estimate.

See [REPRODUCTION.md](REPRODUCTION.md) for exact commands, validation boundaries, PDF rebuilding, and the discovery-data archive.


---

# A quantitative protected-survival counterexample

_Source: finite/REPORT.md_

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


---

# Independent audit of the quantitative eleven-root certificate

_Source: finite/INDEPENDENT_REVIEW.md_

6 November 2026. Internal mathematical and numerical review; not external peer review or formal verification.

## Finding

The quantitative certificate is valid on the stated finite-model hypotheses. I found no error in the exact-law construction, the complementary-orbit moment equations, the 964-dimensional span argument, the Neumann-series enclosure, or the signed survival objective. An isolated replay at 224-bit Arb precision, with a different floating inverse routine, verifies a survival-probability increase exceeding 0.0175 while every probability remains strictly positive.

This audit does not establish a zeta theorem, an infinite-volume separation, or LP optimality. The original ACUE baseline and periodic-lift mass calculation are being audited separately by the root investigator.

## Source and replay identity

Reviewed files: `REPORT.md`, `certify.py`, `candidate.json`, and `base.py` in this directory. Also reviewed the checkpoint's `ELEVEN_POINT_PROTECTED_SURVIVAL.md` and `n11-rank-review.md` for the characteristic-zero span argument.

The candidate bytes have SHA-256

`879a342d7c9a79aed72dae2bf72bd79c1fc7ad670a8f25124429237eb5edd76c`.

The replay was made in the separate directory `/private/tmp/astra-zeta-nov06-quant/finite-independent-224`, without changing the author's source files. The only numerical changes to the copied certificate were:

- Arb precision 224 instead of 160 bits;
- `scipy.linalg.inv(Cmid)` instead of solving `Cmid R = I` using `scipy.linalg.solve`.

The candidate has 964 distinct dependent coordinates, all in the valid range 0,...,1488. Its 1,489 stored survival differences have counts (-1,0,+1)=(137,1096,256). Both the ordered orbit-pair hash and the recomputed survivor hash pass the original assertions.

## 1. The moment equations have the correct sign and meaning

For every frequency 1<=j<=11, complementation on the 22-site grid sends p_j to -p_j, because the full-grid trace is zero. For a balanced trace product p_a conjugate(p_b) with an odd total number of factors, the real part therefore changes sign. For the test f=2 Re(p_a conjugate(p_b)), its complement difference is precisely -4 Re(p_a conjugate(p_b)), which is the formula reconstructed in the certificate.

Canonicalizing the complement by a rotation or reflection does not change this real balanced test. Rotation multiplies the product by a phase of total exponent zero. Reflection conjugates it and leaves its real part unchanged.

The selected labels are positive partitions with equal weight at most 11. Even-factor products have zero complementary difference, so their absence does not omit a constraint. Imaginary parts vanish under the preserved reflection symmetry. All required unbalanced expectations vanish under grid rotation because their nonzero total exponent has absolute value at most 11 and hence is not divisible by 22; an additional continuous common rotation is also permissible.

The q_i factors are orbit masses. Multiplying the i-th transfer by q_i and applying nonzero row scalings does not change the dimension of the constraint space. The matrix describes mass transferred from A_i to B_i, so the objective q_i h_i [survive(B_i)-survive(A_i)] has the correct sign.

## 2. Why 964 independent equations enforce all protected moments

This conclusion needs both a lower and an upper rank bound; a modular rank alone would not suffice. The present interval certificate proves an actual 964-by-964 submatrix invertible in characteristic zero. The checkpoint supplies the independent upper bound 964 as follows.

A balanced trace polynomial of each-sign weight at most 11 is a linear combination of U(11) characters whose highest weights have total zero and positive mass at most 11. On the grid, each character is a Fourier minor divided by a nonzero Vandermonde minor. Reducing the alternant exponents gives the enumerated 3,956 residue sets; repeated exponents vanish.

Reflection and particle-hole complementation act by commuting involutions on this span. For odd N=11 the reflection reordering sign (-1)^[h(N-h)] is +1. The complement sign is +1 by the balanced exponent sum and Jacobi's complementary-minor identity. Their fixed-set counts are

`3956, 106, 22, 184`.

The reflection-even, complement-odd projector therefore has rank

(3956+106-22-184)/4 = 964.

Taking complementary differences of dihedral orbit averages lands in this projected space. Restricting the columns to pairs that share a gap histogram cannot increase its dimension. Thus the verified 964 independent rows span every protected constraint on these transfers. No assumed equality between the entire character span and the protected trace span is needed; containment gives the upper bound.

I checked this argument rather than treating the integer 964 as a numerical observation. The current replay re-enumerates the residue sets and fixed counts, but uses the author's enumeration function. The prior checkpoint's alternative residue-lift enumeration is separate corroborating evidence; it was read, not rerun in this audit.

## 3. The dyadic candidate defines an exact law

Every stored hexadecimal float is an exact binary64 dyadic rational, not an intended unknown decimal real. At precision at least 53, constructing `arb(float_value)` represents that dyadic exactly; a separate conversion check against the integer numerator and denominator confirmed zero radius.

All row scales are strictly positive dyadics. Every root-of-unity trace and every q_i is evaluated with outward-rounded balls containing its exact algebraic value. Hence the matrix entries and residual balls enclose one exactly defined real-algebraic system.

Fixing the 525 free coordinates to their stored dyadics and solving the remaining 964 equations defines h* exactly. The certificate does not declare a floating residual to be zero.

## 4. The preconditioned error estimate is valid

Let r=B h0, let C be the dependent-coordinate submatrix, and let R be the computed floating inverse interpreted entrywise as an exact dyadic matrix. With E=I-RC, the certificate establishes ||E||_infinity<=rho<1. Thus RC and C are invertible. The exact dependent correction is

delta=-(RC)^(-1) R r,

and

||delta||_infinity <= ||Rr||_infinity/(1-rho).

The proof does not assume R itself is already a valid inverse. Nor does it require a condition-number estimate or an unverified floating solve.

The row-sum quantities use outward upper endpoints. The stored upper endpoints have zero Arb radius; their maximum is therefore legitimate. Propagating the correction bound through the objective with the sum of q_i |d_i| over dependent coordinates gives a valid worst-case enclosure. Unchanged free coordinates contribute no correction error.

## 5. Independent replay results

The 224-bit replay, using the alternate inverse routine, yielded:

| Quantity | Certified bound |
|---|---:|
| ||I-RC||_infinity | < 0.000004584921 |
| ||R B h0||_infinity | < 0.000000003919400 |
| ||h*-h0||_infinity | < 0.000000003919418 |
| ||h*||_infinity | < 0.500000006777886 |
| Unmagnified survival increase | > 0.00885107073931318 |
| Unmagnified survival increase | < 0.00885107100190835 |
| Increase after multiplying h* by 99/50 | > 0.01752512006384011 |
| Increase after multiplying h* by 99/50 | < 0.01752512058377852 |
| Magnified relative density change | < 0.990000013420213 |

Thus every altered density is greater than 0.009999986579787 times its original positive density. The untouched densities remain unchanged. The exact moment equations are homogeneous, so multiplying h* by 99/50 preserves them.

The slightly changed inverse affects the enclosure radius, not the exact law: the defining free dyadics and exact selected equations remain identical. The exact law does not depend on the preconditioner.

## 6. Survival classification and scope of independence

The replay recomputes all survivor bits at the rational heat multiplier 85/84 using the original Hermitian Newton-sum/LDL classifier, now at 224 bits. It certifies strict signs and matches the stored vector.

The mathematical criterion is appropriate: self-inversiveness is preserved by the symmetric heat multipliers; the Newton Toeplitz matrix is positive definite exactly for distinct unit-circle roots. A negative certified pivot detects failure of that condition. A simple all-unit-circle configuration at the final time cannot have undergone an earlier collision, since the reverse repulsive root flow has a positive nondecreasing Vandermonde modulus and extends back without collision.

This is a higher-precision replay of the same classifier, not a new independent classification algorithm. The checkpoint's earlier Cayley/Sturm replay is the independent-method evidence. That distinction should remain explicit in publication descriptions.

## Conclusion

The claimed finite probability separation greater than 1.75 percentage points is certified by an exact-law definition and rigorous error bounds. The strongest remaining limitations are external verification and the arithmetic/infinite-volume transfer, not a residual-sized numerical loophole in this certificate.


---

# The exact probability cost of periodic lifting

_Source: PERIODIC_LIFT_MASS.md_

This is a limitation on the present finite-model construction, not a no-go theorem for all possible countermodels.

Let \(P_n\) be ACUE on \(n\)-subsets \(S\) of the \(2n\)-th roots of unity. Write
\[
p_n(S)=(2n)^{-n}|\Delta(S)|^2.
\]
For \(r\ge2\), take every \(r\)-th root of every point of \(S\); denote the resulting \(nr\)-point configuration by \(L_r(S)\).

## 1. Exact atom identity

\[
p_{nr}(L_r(S))=p_n(S)^r.
\]

To prove this, set \(Q(z)=P_S(z^r)\). For every root \(z\) of \(Q\),
\[
|Q'(z)|=r|P'_S(z^r)|.
\]
Multiplying over all \(nr\) roots gives
\[
|\Delta(L_r(S))|^2
=r^{nr}|\Delta(S)|^{2r}.
\]
Divide by \((2nr)^{nr}\). The lift is injective on seed configurations. Its dihedral orbit size equals that of the seed, since rotations by \(2n\) grid sites stabilize the lift.

Consequently the ACUE probability of the entire lifted support is
\[
M_{n,r}=\sum_{|S|=n}p_n(S)^r.
\]
This sum runs over all seed subsets, not just the matched pairs used by our construction.

## 2. A closed formula from the classical Dyson constant-term identity

For \(r=2\),
\[
\boxed{M_{n,2}=\frac{(2n)!}{n!(4n)^n}.}
\]

Indeed, on the unit torus \(|\Delta|^4\) is the Dyson Laurent product with all parameters equal to 2. Its exponent in each variable lies between \(-2(n-1)\) and \(2(n-1)\), strictly inside the aliasing length \(2n\). Averaging it on the full \((2n)^n\) grid therefore extracts only its ordinary constant term. Repeated coordinates contribute zero. Dividing the ordered sum by \(n!\) gives
\[
M_{n,2}=\frac{1}{n!(2n)^n}
 \operatorname{CT}|\Delta|^4
=\frac{1}{n!(2n)^n}\frac{(2n)!}{2^n}.
\]
The constant-term theorem is classical; this application does not establish a new famous Dyson conjecture. See [Good, Short Proof of a Conjecture by Dyson, J. Math. Phys. 11 (1970), 1884](https://sites.math.rutgers.edu/~zeilberg/akherim/good1970.pdf).

At \(n=11\),
\[
M_{11,2}=\frac{1249937325}{53119845582848}
=0.00002353051503228758\ldots .
\]

Stirling's formula gives \(M_{n,2}\sim\sqrt2 e^{-n}\). This is a probability estimate, not a runtime claim.

## 3. All lift factors

The ACUE atom \(p_n(S)\) is the principal minor of the rank-\(n\) Fourier projection on \(2n\) sites. Its diagonal entries equal \(1/2\), so Hadamard's inequality gives \(p_n(S)\le2^{-n}\). The two alternating clock subsets attain equality. Hence
\[
M_{n,r}\le 2^{-n(r-2)}\frac{(2n)!}{n!(4n)^n}
\quad (r\ge2).
\]
This strengthens the simpler \(M_{n,r}\le2^{-n(r-1)}\).

## 4. The full pair data already determine membership in the lifted support

Write \(c_S(a)=|S\cap(S+a)|\) for the pair-displacement count on the \(2nr\)-site grid. Then
\[
S\in L_r\quad\Longleftrightarrow\quad c_S(2n)=nr.
\]
The right-hand condition says that translating the set by \(2n\) sites leaves every point in the set. Its translation cycles have length \(r\), so \(S\) is precisely the lift of an \(n\)-subset of the \(2n\)-site grid.

Thus the lifted support is a union of fibres of the full pair-data map. Any probability law \(Q\) with the same full pair-summary distribution as ACUE has
\[
Q(L_r)=P_{nr}(L_r)=M_{n,r}.
\]
If \(Q\) additionally agrees with \(P_{nr}\) outside that support, then, in the convention \(\operatorname{TV}(Q,P)=\sup_A|Q(A)-P(A)|\),
\[
\operatorname{TV}(Q,P_{nr})\le M_{n,r}.
\]
Every event probability, including survival under heat, differs by at most that amount. No bound on the density ratio is needed.

## Consequence for the research programme

The eleven-root theorem now gives an explicitly certified survival shift exceeding 0.0175. Its periodic copies cannot sustain a comparable macroscopic shift: at size 22, even redistributing the entire two-fold lifted support can change a probability by at most 0.0000235305151. A nonvanishing large-size separation requires perturbations affecting configurations outside this repeated-pattern support.

This result does not exclude an extensive construction, a stationary infinite-volume countermodel, or a different arithmetic route. It identifies exactly why the existing periodic-lift argument is insufficient.


---

# Bounded local probes: a rigorous transfer lemma and the arithmetic price

_Source: bounded/REPORT.md_

6 November 2026. Internal research note; not a zeta theorem or an external-priority claim.

## 1. Question and outcome

The PR5 audit identifies an actual logical requirement: the unnormalized signed triple statistic grows like the cube of window occupancy. An asymptotic half-grid approximation requires uniform integrability to transfer to its mean. For arbitrary point processes that is additional information. **For actual zeta zeros under RH, at fixed window width, it is available:** the companion arithmetic audit derives every fixed count moment from restricted Rudnick-Sarnak correlations and a positive bandlimited majorant. Thus fixed-window uniform integrability is not a remaining arithmetic unknown in that conditional setting.

There is a clean remedy at the level of probability: normalize by the number of ordered distinct triples. This gives a bounded local statistic, with explicit stability under approximate lattice locations, sparse bad points, and exceptional windows. It has a rigorously nonzero sine-process expectation on sufficiently short windows. For general windows, a hard occupancy cutoff preserves any proved nonzero unnormalized expectation once a determinantal tail bound is small enough.

There is an equally precise limitation. No nonconstant finite-degree correlation polynomial with continuous kernels can be uniformly bounded over arbitrary finite simple configurations in a compact window. Normalization or clipping necessarily leaves the finite three-trace algebra, unless one restricts the configuration class. Pointwise boundedness is stronger than the moment bounds available for a specified process. Consequently the theorem does not obstruct the under-RH zeta uniform-integrability argument, and the original signed three-trace statistic remains the simpler arithmetic target.

## 2. The original phase difference and a bounded normalization

Put

\[
a=(6/5,1/5,-7/5),\qquad b=(-4/5,1/5,3/5),
\]

and

\[
h(x_1,x_2,x_3)=\cos(2\pi a\cdot x)-\cos(2\pi b\cdot x).
\]

These are exactly PR5's two frequency triples. For a finite simple configuration X in a window I, let K=|X| and

\[
V(X)=\sum_{i,j,k\ \mathrm{distinct}}h(x_i,x_j,x_k),\qquad
U(X)=\begin{cases}V(X)/(K)_3,&K\ge3,\\0,&K<3.\end{cases}
\]

Here (K)_r=K(K-1)...(K-r+1). Then |U|<=2 uniformly in K. The same conclusions below hold with any attached triple weights in [0,1], including Hann product weights, while retaining the denominator (K)_3. Claims about strict sign in section 5 use unweighted triples, or positive symmetric weights.

The two complex phases have ratio exp(4 pi i(x_i-x_k)). Consequently h=0 termwise on every translated half-grid, regardless of thinning and weights.

## 3. Quantitative approximate-AH transfer, without occupancy tails

Suppose at least (1-epsilon)K points in a window are within eta of one common translate of (1/2)Z. For every entirely good triple,

\[
|h|\le |e^{4\pi i(x_i-x_k)}-1|\le8\pi\eta.
\]

At most 3 epsilon of uniformly sampled ordered distinct triples contain a bad point, by the union bound on their three uniform marginals. As |h|<=2,

\[
\boxed{|U(X)|\le8\pi\eta+6\epsilon.}
\]

No factor involving K remains. If a fraction q of windows is entirely exceptional, the absolute mean is at most

\[
\boxed{8\pi\eta+6\epsilon+2q.}
\]

These bounds may be replaced by their minimum with 2. They concern a local common lattice translate; an unrelated nearest-half-integer phase for each point would not suffice.

### Sparse deletion measured globally

There is also a useful spatial-average form, avoiding local bad-point fractions. Let B be a stationary set of bad points of intensity rho_B, and use sliding windows of fixed length L. Suppose every window with no B point is eta-close to a translated half-grid. Campbell's formula and Markov's inequality give

\[
\Pr\{B\cap I\ne\varnothing\}\le L\rho_B,
\qquad
\boxed{|\mathbb E U|\le8\pi\eta+2L\rho_B.}
\]

An additional exceptional-window fraction q costs 2q. The same statement holds deterministically for long spatial averages, up to the endpoint contribution, by integrating the number of deleted points in a sliding interval. For a unit-intensity process, deletion of a point-intensity fraction epsilon means rho_B=epsilon. This is stronger than assuming a small fraction of bad points separately in every window.

For comparison of the statistic before and after deleting b points of a particular configuration,

\[
|U(X)-U(X\setminus B)|\le\min(4,12b/K)
\]

when K>0; the conventions for occupancies below 3 make the bound valid there too. In particular this difference is at most 4b, giving a spatial-average change at most 4L rho_B without any lattice hypothesis.

## 4. Normalization does not automatically preserve the signed mean

A negative E V does not imply a negative E[V/(K)_3]: the denominator is correlated with the signed numerator. The PR5 finite-window means therefore cannot simply be relabelled as means of U. They must be recomputed or proved separately.

This is not a technicality. A two-outcome random variable can have a large negative V on high-occupancy outcomes and a small positive V on low-occupancy outcomes; dividing by a cubic occupancy can reverse its mean.

## 5. A rigorous nonzero sine-process expectation for the same normalized triple kernel

Let all three coordinates lie in an interval of length L<=1/4. Define the symmetrized kernel

\[
\bar h(x)=\frac16\sum_{\sigma\in S_3}h(x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)}),
\qquad v=\sum_{j=1}^3(x_j-\bar x)^2.
\]

Since both frequency vectors sum to zero, centering x does not change the phases. Permutation averaging gives

\[
\frac16\sum_\sigma(a\cdot x_\sigma)^2=\frac{43}{25}v,
\qquad
\frac16\sum_\sigma(b\cdot x_\sigma)^2=\frac{13}{25}v.
\]

Also |a dot x|<=7L/5 and |b dot x|<=4L/5. The elementary Taylor bound

\[
|\cos z-1+z^2/2|\le |z|^4/24
\]

therefore gives

\[
\bar h(x)\le-
\left(\frac{12\pi^2}{5}-\frac{926\pi^4}{375}L^2\right)v.
\]

For L<=1/4 the bracket is greater than pi^2/2 (use pi^2<10). Thus

\[
\boxed{\bar h(x)\le-\frac{\pi^2}{2}v<0}
\]

for every nonconstant triple. Consequently U(X)<0 whenever K>=3, and U(X)=0 otherwise, for a simple configuration in such a window.

For the unit-intensity sine process, rho_3(x)=det[sinc(pi(x_i-x_j))] is strictly positive at every distinct triple: it is the Gram determinant of three linearly independent exponentials in L^2[-1/2,1/2]. Its integral on I^3 is positive, so P(K>=3)>0. Hence

\[
\boxed{\mathbb E_{\rm sine} U<0\quad(0<L\le1/4).}
\]

This is a proof, not a Monte Carlo sign inference. It combines with section 3 to give an explicit logical separator between a sine process and an approximate half-grid process with vanishing contamination.

The same strict-sign conclusion holds for unfolded Haar CUE of every rank N>=3: the three-point density is the Gram determinant of three distinct Fourier evaluation vectors, hence is strictly positive on distinct triples in this short interval. This is a fixed-window finite-CUE statement, not a claimed zeta transfer.

### An explicit positive integral lower bound

Write c=pi^2/2 and

\[
J_L=\int_{I^3}\!\left[\sum_j(x_j-\bar x)^2\right]\rho_3(x)\,dx>0.
\]

The triple variance is at most 2L^2/3. Hadamard's inequality gives rho_r<=1 for this unit-intensity determinantal process. By Cauchy-Schwarz and

\[
(K)_3^2=(K)_6+9(K)_5+18(K)_4+6(K)_3,
\]

one obtains the completely explicit, albeit small, lower bound

\[
-\mathbb E U\ge
\frac{3c J_L^2}{2L^2(L^6+9L^5+18L^4+6L^3)}>0.
\]

The remaining integral is over a compact cube with a specified elementary nonnegative integrand; positivity does not depend on a numerical quadrature.

### Why this is not an arithmetic breakthrough

On such a short interval the probe is effectively detecting the presence of three close points. A translated half-grid has at most one point in an interval of length 1/4. Proving positive limiting frequency of three actual zeta zeros in such windows is itself a strong, currently unproved input in this programme. Boundedness removes an approximation-transfer obstacle, not the arithmetic difficulty. This local theorem should not be described as a new zeta distribution result.

## 6. A large-window cutoff preserving any proved nonzero mean

Let V have triple weights bounded by 1 and suppose a sine or unfolded CUE calculation rigorously gives E V=-m<0 in an interval of length L. Define

\[
H_M(X)=\frac{V(X)\,1_{K\le M}}{2(M)_3},\qquad M\ge3.
\]

Then |H_M|<=1, and H_M vanishes on half-grids. If K>M and 1<=r<=M-2,

\[
(K)_3\le\frac{(K)_{3+r}}{(M-2)_r}.
\]

For a unit-intensity determinantal process, E(K)_j<=L^j, so

\[
|\mathbb E[V1_{K>M}]|\le
\boxed{\frac{2L^{3+r}}{(M-2)_r}}=:R_{L,M,r}.
\]

Therefore if R<m,

\[
\mathbb E H_M\le-\frac{m-R}{2(M)_3}<0.
\]

For illustration only, L=40, M=100, r=40 gives an extremely small explicit tail bound, computable using integer powers and products. Applying this to PR5 requires a rigorous lower bound m for that precise finite-window mean; the checked-in floating expectation is not by itself an interval certificate. No such certificate is claimed here.

On a regular window H_M obeys |H_M|<=4 pi eta+3 epsilon, and exceptional windows cost at most q. The hard cutoff can be discontinuous under deletion across K=M; the pointwise lattice-transfer bound remains valid because it never compares two different occupancies.

### A smooth alternative

For R>0, let H_R=V/[2(K+R)^3]. Then |H_R|<=1 and

\[
|\mathbb E V-2R^3\mathbb E H_R|
\le\frac6R(L^4+3L^3).
\]

Indeed 1-(1+u)^(-3)<=3u and K(K)_3=(K)_4+3(K)_3. Thus sufficiently large R preserves every nonzero E V, with an explicit condition. Its generic bound is usually much weaker than the hard-cutoff tail bound. It also requires higher information in its arithmetic expectation.

## 7. The exact arithmetic price: a finite-order boundedness theorem

**Theorem.** Let I be a compact interval with nonempty interior. Suppose

\[
F(X)=c+\sum_{r=1}^d\sum_{i_1,\ldots,i_r\ \mathrm{distinct}}
f_r(x_{i_1},\ldots,x_{i_r}),
\]

where every f_r is continuous and symmetric on I^r. If |F(X)| is bounded by one constant for every finite simple configuration X in I, then all f_r vanish and F is constant.

**Proof.** Sample n iid points from an arbitrary nonatomic probability measure mu on I. They are distinct almost surely. The expectation is

\[
c+\sum_{r=1}^d(n)_r\int f_r\,d\mu^r.
\]

It is a polynomial in n bounded for all positive integers n. Each coefficient in the falling-factorial basis is zero, so the integral of each f_r against mu^r is zero. Approximate arbitrary probability measures by nonatomic ones; continuity preserves this identity. Polarize the resulting homogeneous polynomial in finite mixtures of Dirac measures to conclude f_r=0 at every tuple. QED.

The theorem covers fixed finite sums of ordinary weighted trace products after repeated-index terms are expanded. It does not cover ratios, adaptive sampling, clipping, discontinuous order statistics, or a class of processes with a deterministic occupancy bound.

Thus an arbitrary-occupancy bounded nontrivial local probe cannot remain a fixed finite-order correlation polynomial. This is why simply asking for both boundedness and the old three-trace explicit-formula calculation is incompatible on that class.

## 8. Exact representations exist, but they require more information

For K>=3,

\[
\frac1{(K)_3}=\frac12\int_0^1 t^{K-3}(1-t)^2\,dt.
\]

Hence U has an exact generating-functional representation. For a determinantal process with reduced Palm kernel K^x_I,

\[
\mathbb E U=\frac12\int_0^1(1-t)^2
\int_{I^3}h(x)\rho_3(x)
\det(1-(1-t)K^x_I)\,dx\,dt.
\]

The reduced Palm Fredholm determinant records all further points in the window. Similarly, 1/(K+R)^3=(1/2) integral_0^infinity u^2 exp[-u(K+R)] du yields a Laplace-functional representation for the soft normalization.

For actual zeta zeros, inserting an explicit formula into each linear trace does not remove these random denominators or occupancy indicators. Estimating the normalized expectation directly would require joint count/phase information. At fixed window width under RH, however, one can keep the unnormalized finite-order statistic: the required occupancy moment bound is already obtainable, so the unresolved input is the signed mean beyond the protected correlation range.

Here is the count-control mechanism. Choose a nonnegative Schwartz majorant of the fixed interval with sufficiently small compact Fourier support. For each fixed k, choose that support so that the k-fold product and every repeated-index partition remain in the restricted k-level correlation region. Applying the correlation theorem yields a bounded kth moment of the local zero count. In particular a fixed moment above degree three gives uniform integrability of a cubic statistic by Holder's inequality. The permitted cutoff in the macroscopic height average is supported by the interval-cutoff extension on p.1030 of [Rudnick-Sarnak, *The n-level correlations of zeros of the zeta function* (1994)](https://www.math.tau.ac.il/~rudnick/papers/RudnickSarnakCRAS1994.pdf). This is a consequence of existing restricted correlations, not a new unprotected correlation theorem.

## 9. A simpler bounded positive alternative

For K>=1 put

\[
Q(X)=1-\left|K^{-1}\sum_{x\in X}e^{4\pi i x}\right|^2,
\]

and Q(empty)=0. Then 0<=Q<=1. It vanishes exactly when all point phases e^(4 pi i x) agree, equivalently when the configuration lies in a translated half-grid. With eta-close good points and bad fraction epsilon,

\[
Q\le32\pi^2\eta^2+4\epsilon.
\]

For any interval of positive length, the sine-process expectation is strictly positive: its second correlation density is positive off the diagonal, and almost surely distinct points do not differ by a half-integer. This illustrates that finding a bounded statistical separator is easy; proving its positive limiting zeta expectation remains the substantive issue. Its denominator again leaves the finite pair-trace algebra.

## 10. Recommended next step

1. Keep the original unnormalized PR5 statistic for a direct three-trace arithmetic target.
2. Add U as an empirical robustness diagnostic, reporting its own means rather than reusing the original means.
3. If one wants a rigorous finite-model sign at widths 10,20,40, interval-certify E V, choose an explicit occupancy cutoff M using section 6, and then compute the bounded diagnostic.
4. State the missing zeta input exactly: **under RH and at fixed window width, it is the signed three-trace mean beyond the protected range.** Count moments provide the necessary uniform integrability. A nonzero bounded-probe mean is an alternative target, but its normalization adds joint-law complexity and is unnecessary solely to obtain uniform integrability in this setting.

## Sources and verification scope

- Local source: `../../november-checkpoint/CONCURRENT_PR5.md`, audited against PR5 commit `3b7687eb4a6be68c9093d997c473ebcf1331947e`.
- Local original statistic and finite CUE controls: `PR #5 statistic.py at the pinned commit` and `controls.py`.
- The elementary inequalities and identities above are proved in this note. The accompanying deterministic check script tests the phase cancellation, stability constants, symmetrized-kernel inequality, deletion bound, and factorial identities. Numerical testing is supplementary to the stated proofs.
- No zeta data were reprocessed, no arithmetic asymptotic established, and no external novelty or formal verification claim made.


---

# Arithmetic audit of the half-grid triple probe

_Source: arithmetic/REPORT.md_

> Historical stage note: the singular-series main term left open below has since been evaluated in [MAIN_TERM_THEOREM.md](arithmetic/MAIN_TERM_THEOREM.md), with [independent review](arithmetic/MAIN_TERM_INDEPENDENT_REVIEW.md). The required estimate for the actual prime-pair discrepancy remains unproved. This chapter is retained to document the derivation and the earlier boundary of knowledge.

6 November 2026. Research derivations and primary-source audit; integrated into this checkpoint after independent review.

PR #5 remains at `3b7687eb4a6be68c9093d997c473ebcf1331947e` (`feat/windowed-zeta-triples`), verified through GitHub during this audit. The [pinned statistic](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/3b7687eb4a6be68c9093d997c473ebcf1331947e/research/experiments/windowed-triples/statistic.py) uses the distinct ordered triples

\[
a=(1.2,0.2,-1.4),\qquad b=(-0.8,0.2,0.6).
\]

The full empirical experiment was not rerun. This note derives an alternative observable, closes a conditional uniform-integrability issue, and identifies a specific arithmetic estimate still missing. It does **not** prove a nonzero limiting zeta statistic or refute the Alternative Hypothesis.

## 1. A cleaner raw triple observable

Let \(e(x)=e^{2\pi ix}\). For arbitrary real locations and product weights, the difference of the two phases is

\[
e(a\cdot(x_i,x_j,x_k))-e(b\cdot(x_i,x_j,x_k))
=e(b\cdot(x_i,x_j,x_k))[e(2(x_i-x_k))-1].
\]

Consequently the difference vanishes term by term on every translate of \(\tfrac12\mathbb Z\), including arbitrary thinning and multiplicities. **Distinctness of the indices is unnecessary.** The raw product is therefore an equally valid half-grid detector and avoids estimating the high-frequency pair terms introduced by distinct-index subtraction.

For a precise Fourier-localized version, choose a nonzero, nonnegative, real even Schwartz function \(\psi\) with \(q=\widehat\psi\in C_c^\infty((-\eta,\eta))\), where \(0<\eta<0.05\). Such functions exist: square a real even Schwartz function with sufficiently narrow smooth compact Fourier support. Put

\[
c_\psi=\int_\mathbb R\psi(x)^3\,dx>0,\qquad
Z_\alpha(t)=\sum_\gamma\psi\left(\frac{L(\gamma-t)}{2\pi}\right)
e\left(\alpha\frac{L(\gamma-t)}{2\pi}\right),\quad L=\log T.
\]

Here RH is assumed, zeros are counted with multiplicity, and the sum includes all nontrivial ordinates. Let \(\Phi\ge0\) be smooth, supported inside \((1,2)\), with integral one. Define

\[
M_T=\frac1{Tc_\psi}\int\Phi(t/T)\operatorname{Re}
\{Z_{1.2}Z_{0.2}\overline{Z_{1.4}}
-\overline{Z_{0.8}}Z_{0.2}Z_{0.6}\}\,dt.
\tag{1}
\]

This is a proposed mathematical variant, **not** a relabeling of the recorded Hann/distinct-index measurements.

### Its sine-process expectation is exactly +1/5

Away from the three zero-coordinate axes, the full third moment of the unit-density sine process has spectral density

\[
C_3(\xi)=1-\sum_{j=1}^3(1-|\xi_j|)_+
+2\left(1-\sum_j\xi_j^+\right)_+,
\qquad \sum_j\xi_j=0.
\tag{2}
\]

This follows by expanding the determinantal three-point density and adding the coincidence partitions; away from the axes it also equals the third cumulant density. In the entire support packet around \(a\), (2) is \(\xi_2\). In the packet around \(b\), it is zero. The packets miss all coordinate axes. Writing \(\xi=a+u\), integration against \(\prod_jq(u_j)\delta(\sum u_j)\) gives

\[
\int \xi_2\prod_jq(u_j)\delta(\sum u_j)\,du
=0.2\,c_\psi:
\]

the term containing \(u_2\) is odd under simultaneous sign reversal. Thus the normalized expected raw difference is exactly **+0.2 for this fixed envelope**, rather than merely an infinite-window limit. The distinct-index sine limit is a different number, −0.4.

The same construction works for
\[
(\alpha,\beta,-\alpha-\beta),\quad
(\alpha-2,\beta,2-\alpha-\beta),\qquad
0<\beta<1,\quad1<\alpha<2-\beta,
\]
with packets narrow enough to stay in the indicated chambers. Its raw sine expectation is \(\beta\). Shrinking \(\beta\) gives a shorter prime variable, at the price of a smaller signal.

## 2. Occupancy and the precise meaning of pair-AH

### Fixed-window moments are already bounded under RH

For fixed \(W,k\), set
\[
K_W(t)=\#\{\gamma:|L(\gamma-t)/(2\pi)|\le W\}.
\]
Then
\[
\frac1T\int_T^{2T}K_W(t)^k\,dt=O_{W,k}(1).
\tag{3}
\]

Here is a direct corollary argument, including the required support check. Choose \(\varphi\ge0\), Schwartz and bandlimited to \((-\delta,\delta)\), with \(\varphi\ge1\) on \([-2W-1,2W+1]\) and \(k\delta<2\). For \(1\le r\le k\), put
\[
F_r(x)=\int_\mathbb R\prod_{j=1}^r\varphi(x_j-u)\,du.
\]
It is symmetric, translation invariant, and Schwartz transverse to the diagonal. Its Fourier measure is supported on \(\sum\xi_j=0\), with \(|\xi_j|<\delta\), hence \(\sum|\xi_j|<2\). Also \(F_r\ge1\) whenever the configuration has diameter at most \(2W\): integrate over an interval of length one near any one of the points.

The restricted correlation theorem gives an \(O(TL)\) bound for the distinct-index sum of \(F_r(L\gamma_1/(2\pi),\ldots)\) with all ordinates in \([T/2,3T]\). In the expansion of the integral of \(K_W^k\), group repeated indices by their partitions into \(r\) distinct indices. Any tuple that can lie in one window has diameter at most \(2W\), and the set of eligible centers has length at most \(4\pi W/L\). Multiply these two bounds and sum the finitely many partitions to obtain (3).

The exact primary input is Rudnick–Sarnak, *The n-level correlations of zeros of the zeta function*, Theorem 1.1, pp.1029–1030; immediately after that theorem the authors explicitly allow an interval characteristic cutoff under RH. Their test conditions TF1–TF3 and strict Fourier support \(\sum|\xi_j|<2\) are precisely the conditions checked above. This argument uses the height-localized theorem with \(L=\log T\), not an unexamined interchange with the index normalization. [Original paper](https://www.math.tau.ac.il/~rudnick/papers/RudnickSarnakCRAS1994.pdf)

Thus the earlier PR audit's occupancy caveat can be sharpened: **under RH, uniform integrability for fixed compact-window cubic scores is a known-theorem consequence, not an additional conjecture.** This does not make an empirical deletion test a proof; it supplies a separate analytic bound.

### Full pair concentration suffices; protected-band matching does not

Let \(R\) denote the unnormalized raw or distinct phase difference in a compact window, with absolute weights at most one. Let \(B_\eta\) be the number of ordered pairs in that window whose displacement has distance greater than \(\eta\) from \(\tfrac12\mathbb Z\). The phase factorization gives
\[
|R|\le4\pi\eta K^3+2KB_\eta.
\]
If \(\mathbb E K^j\le C_j\), split at \(K\le M\), using the crude \(|R|\le2K^3\) on the tail. Then
\[
\mathbb E|R|\le4\pi\eta C_3+2M\mathbb E B_\eta+\frac{2C_4}{M}
\le4\pi\eta C_3+4\sqrt{C_4\mathbb E B_\eta}.
\tag{4}
\]
The last display chooses \(M=\sqrt{C_4/\mathbb E B_\eta}\); the zero case follows by a limit. Divide by the positive normalization for the normalized score.

Therefore a **full local pair-displacement hypothesis** asserting \(\mathbb E B_\eta\to0\) for every fixed window and every fixed \(\eta>0\) implies that these cubic means tend to zero: first let \(T\to\infty\), then \(\eta\downarrow0\). The same conclusion follows from convergence of the full local pair measures to a measure supported on the half-grid, using nonnegative off-lattice majorants. Distinct labels at the same zero cause no problem. No coupling of entire configurations, or separate three-point AH, is needed.

This implication does **not** follow just from agreement with pair tests whose Fourier support lies in the Montgomery range. Those tests do not establish vanishing off-lattice pair mass. The formulation of “AH” must say which assertion is assumed.

The conclusion extends to the Schwartz envelope in (1). Partition the unfolded line into unit cells, apply (3) uniformly to shifted centers whose heights stay in \([T/2,3T]\), and use Minkowski's inequality to bound the fourth norm of the tail by a constant times \(\sum_{|j|>A}\sup_{[j,j+1]}|\psi|\). This tends to zero. Cells farther than a constant times \(T\log T\) are handled by the elementary local zero-count bound \(O(\log(2+T+|j|))\) and arbitrarily rapid decay of \(\psi\). Hölder bounds the difference of the cubic products after truncation. Thus full pair-AH plus RH implies \(M_T\to0\).

## 3. Exact reduction to a signed near-product prime correlation

Use \(\widehat\Phi(y)=\int\Phi(u)e^{-2\pi iyu}\,du\), and write
\[
q_\alpha(n)=q(\log n/L-\alpha).
\]
The explicit formula, for positive \(\alpha>\eta\), gives uniformly on the support of the height average
\[
Z_\alpha(t)=-\frac1L\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
q_\alpha(n)n^{-it}+O_B(T^{-B})
\tag{5}
\]
for every fixed \(B\). All sums are finite, supported on \(T^{\alpha-\eta}<n<T^{\alpha+\eta}\). The gamma-density contribution has no surviving Taylor moments because the Fourier packet misses zero; smoothness and Schwartz decay control its remainder. The explicit pole terms are also rapidly small, using the compact Fourier support and the large real displacement of their arguments. Negative-frequency values are complex conjugates.

The low packet \((-.8,.2,.6)\) contributes \(o(1)\). One can see this directly: the product of the two positive prime variables is at most \(T^{.8+2\eta}<T\), so unequal integer products are killed by arbitrary decay of \(\widehat\Phi\). Exact equality forces all three nonzero von Mangoldt factors to be powers of the same prime; since every variable has a positive power-of-\(T\) lower cutoff, the weighted diagonal tends to zero. This also agrees with the restricted-correlation theorem.

Consequently (1) is
\[
M_T=-\frac1{c_\psi L^3}\operatorname{Re}\sum_{m,n,r\ge1}
\frac{\Lambda(m)\Lambda(n)\Lambda(r)}{\sqrt{mnr}}
q_{1.2}(m)q_{.2}(n)q_{1.4}(r)
\widehat\Phi\!\left(\frac{T}{2\pi}\log\frac{mn}{r}\right)+o(1).
\tag{6}
\]

This identifies an exact asymptotic target. The central scales are
\[
m\asymp T^{1.2},\quad n\asymp T^{.2},\quad r\asymp T^{1.4},
\quad |r-mn|\asymp T^{.4},
\]
with the stated small exponent-width packets, rather than literal fixed-factor dyadic windows. The final relation describes the kernel's natural scale; its rapidly decaying tails remain in (6).

There is a useful centering improvement. For any fixed \(\alpha-\eta>1\),
\[
\sum_{n\ge1}n^{-1/2}q_\alpha(n)n^{-it}=O_B(T^{-B})
\]
uniformly for \(t\) comparable to \(T\). Poisson summation has no stationary integer frequency because \(n\gg T\); repeated integration by parts controls the zero Fourier mode as well. Therefore in (6) **both** long prime factors can be replaced by \(\Lambda-1\), leaving the same main term:
\[
\boxed{\quad
M_T=-\frac{\operatorname{Re}\mathcal C_T}{c_\psi L^3}+o(1),\quad
\mathcal C_T=\sum_{m,n,r}
\frac{(\Lambda(m)-1)\Lambda(n)(\Lambda(r)-1)}{\sqrt{mnr}}
q_{1.2}(m)q_{.2}(n)q_{1.4}(r)
\widehat\Phi\!\left(\frac{T}{2\pi}\log\frac{mn}{r}\right).
\quad}
\tag{7}
\]

The sine prediction is \(\operatorname{Re}\mathcal C_T/L^3\to-c_\psi/5\). Proving merely that the left side does not tend to zero would already contradict full pair-AH, conditional on RH. No such estimate is proved here.

**A first-moment prime-density approximation is insufficient.** Because \(\Phi\) is supported away from zero, \(\int\widehat\Phi=\Phi(0)=0\), and all polynomial moments of this kernel vanish. Replacing the long prime factors by their mean density erases the signal. A positive prime count in a short interval, without the necessary signed covariance, does not evaluate (7).

## 4. Which existing theorems actually reach this target?

### Restricted n-level correlations

For balanced three frequencies, \(\sum|\xi_j|<2\) is equivalent to total positive frequency less than one. The low packet lies inside; the high packet has total positive frequency 1.4 and lies outside. Any balanced triple beyond that boundary has at least one coordinate of absolute value greater than one, which explains why distinct-index subtraction imports unknown high-frequency pair terms. Formula (1) removes those pair subtractions, but does not remove the genuine support obstruction.

The compact physical Hann taper in PR #5 has unbounded Fourier support. It cannot be inserted unchanged into the restricted theorem at fixed width. The Fourier-compact envelope above is a separate observable deliberately chosen to make support statements exact.

### Fazzari–Gerspach: the closest matching arithmetic theorem

The primary paper is Alessandro Fazzari and Maxim Gerspach, *The third moment of the logarithm of zeta and a twisted pair correlation conjecture*, arXiv:2412.20099v1, submitted 28 December 2024. [Versioned primary source](https://arxiv.org/abs/2412.20099v1)

Its Proposition 1.7, assuming RH, treats a prime-power twist \(n\le T^{1-\varepsilon}\). With \(\beta=\log n/\log T\) and \(\delta_T=10\log\log T/\log T\), the range, including symmetry, is
\[
-1+\delta_T<\alpha<1-\beta-\delta_T.
\]
Thus \(\alpha=1.2,\beta=.2\) is excluded. Theorem 1.9 is stated under RH **and** their uniform Hardy–Littlewood Conjecture 1.8, and gives the displayed range
\[
1-\beta\le\alpha\le2-48\beta.
\]
At \(\beta=.2\) this interval is empty. At \(\beta=.01,\alpha=1.2\), it is nonempty and includes the corresponding alias probe, whose sine signal is .01.

The printed additional conjecture asks, uniformly for \(1\le h,n\le x^{1-\varepsilon}\),
\[
\sum_{m\le x}\Lambda(m/n)\Lambda(m\pm h)
=\mathfrak S_n(h)x/n+O_\varepsilon(x^{1/2+\varepsilon}),
\]
with zero contribution unless \(n\mid m\). **Endpoint correction:** as literally printed with both signs, this common \(x\) main term cannot hold throughout the stated uniform range: already at \(n=1\), the minus sum equals the plus sum with upper endpoint \(x-h\). See `ENDPOINT_CORRECTION.md` for the exact check. Our continuation therefore uses an independent, endpoint-aware discrepancy assumption restricted to the much smaller near-product shifts, not the full printed assertion. This audit does not establish the paper's theorem under a repaired global assumption. The theorem uses a particular smoothed Cauchy pair kernel and a height cutoff with derivatives controlled by powers of \(U=(\log T)^B\); transporting it to arbitrary packets is additional work. Its third-logarithm-moment theorem assumes triple and twisted-pair conjectures, so cannot be used to prove those assumptions.

The structural relevance is direct: after holding the short prime variable fixed, (7) asks about primes \(m\) and \(nm+h\), with a signed smooth shift average. The paper supplies a concrete conditional template, with the endpoint convention requiring repair. It does not provide an RH-only evaluation of our packet.

### Twisted moments do not automatically supply von Mangoldt correlations

Bettin–Chandee–Radziwiłł prove a mean-square formula for \(|\zeta|^2\) times a squared arbitrary Dirichlet polynomial of length below \(T^{1/2+1/66}\), with the coefficient and smoothness conditions in their theorem. That is not a formula for (7). [Primary paper](https://arxiv.org/abs/1411.7764)

Bettin–Bui–Li–Radziwiłł treat the twisted fourth moment with polynomial length below \(T^{1/4}\). Their associated quadratic divisor theorem averages \(am_1m_2-bn_1n_2=h\) smoothly in the long variables and allows arbitrary weights in the short variables \(a,b\). The long von Mangoldt weights in (7) do not meet those hypotheses. Differentiating zeta moments produces derivatives in the numerator, whereas the explicit formula concerns logarithmic derivatives; introducing reciprocal zeta factors requires a new ratios/mollification estimate. [Primary paper](https://arxiv.org/abs/1609.02539)

Unrestricted zeta correlations derived by Conrey–Snaith use the ratios conjecture as input. They are predictions for this purpose, not an available unconditional or RH-only bridge. [Primary paper](https://arxiv.org/abs/0803.2795)

## 5. Concrete next slice and limitations

The useful reduction is now:

1. Under RH, restricted correlations already control all fixed local count moments.
2. Actual off-half-grid pair-mass concentration forces the alias score to vanish; equation (4) makes this quantitative.
3. A raw packet eliminates separate high-frequency pair corrections and has exact sine expectation +1/5.
4. Its zeta mean is equivalent to the explicit signed centered prime sum (7).

The next tractable mathematical task is to adapt the Fazzari–Gerspach smoothed calculation to a narrow small-\(\beta\) packet, keeping a consistent localized Hardy–Littlewood assumption explicit, and identify the weakest **averaged signed** replacement for that assumption actually used. This could yield an honest conditional implication and a sharply stated new analytic target. It would not by itself be an RH-only refutation of AH.

Postpone a claim that general twisted-moment technology already proves the needed estimate; an unrestricted-conjecture conclusion; and a new empirical run advertised as closing the arithmetic gap. The sources inspected here do not provide a theorem evaluating (7) under RH alone. This is a bounded primary-source audit, not a claim that every possible recent paper has been ruled out.


---

# Direct Hardy–Littlewood error control for the raw alias packet

_Source: arithmetic/CONDITIONAL_NEXT.md_

> Historical stage note: the singular-series main term left open below has since been evaluated in [MAIN_TERM_THEOREM.md](arithmetic/MAIN_TERM_THEOREM.md), with [independent review](arithmetic/MAIN_TERM_INDEPENDENT_REVIEW.md). The required estimate for the actual prime-pair discrepancy remains unproved. This chapter is retained to document the derivation and the earlier boundary of knowledge.

6 November 2026. Bounded analytical continuation of `REPORT.md`. This note proves an error-transfer bound conditional on an independent, endpoint-aware prime-pair discrepancy estimate confined to the required near shifts. The printed two-sign uniform Conjecture 1.8 has an endpoint defect explained in `ENDPOINT_CORRECTION.md`; it is not assumed literally here. It does **not** evaluate the remaining singular-series main term or claim Hardy–Littlewood implies the exact +1/5 statistic without that calculation.

## 1. Setup and exact change of variables

Use the notation and Fourier convention of `REPORT.md`. More generally let

\[
1<\alpha<2-\beta,\quad 0<\beta<1,
\quad q_\nu(v)=q(\log v/L-\nu),\quad L=\log T,
\]

where \(q\in C_c^\infty((-\eta,\eta))\). Require \(\alpha-\eta>1\), \(\beta>\eta\), and narrow enough packets to preserve the sine-process chambers. Put \(\gamma=\alpha+\beta\); this \(\gamma\) is a frequency parameter, not a zero ordinate. The normalized high prime packet before taking a real part is

\[
P_T=\frac1{L^3}\sum_{m,n,r}
\frac{\Lambda(m)\Lambda(n)\Lambda(r)}{\sqrt{mnr}}
q_\alpha(m)q_\beta(n)q_\gamma(r)
\widehat\Phi\left(\frac{T}{2\pi}\log\frac{mn}{r}\right).
\tag{1}
\]

The raw zero statistic satisfies \(M_T=-\operatorname{Re}P_T/c_\psi+o(1)\). Write \(x=nm\) and \(h=r-nm\). For fixed \(n,h\ne0\), define

\[
A_{n,h}(y)=\sum_{k\le y}\Lambda(k/n)\Lambda(k+h),\qquad
E_{n,h}(y)=A_{n,h}(y)-\frac{\mathfrak S_n(h)}n (y-\max(0,-h))_+,
\tag{2}
\]

where \(\Lambda(k/n)=0\) unless \(n\mid k\), and terms with \(k+h\le0\) are omitted. The endpoint-aware main term retains the positive overlap length. The singular series is the one in Fazzari–Gerspach Conjecture 1.8, \(\mathfrak S_n(h)=\mathbf1_{(n,h)=1}\mathfrak S(nh)\); it is even in \(h\).

Apart from a smooth dyadic cutoff in \(x\), the weight against \(dA_{n,h}(x)\) is exactly

\[
W_{n,h}(x)=\frac{q_\alpha(x/n)q_\gamma(x+h)}{\sqrt{x(x+h)}}
\widehat\Phi\left(\frac{T}{2\pi}\log\frac{x}{x+h}\right).
\tag{3}
\]

In particular, **there is no additional factor \(n\)** in this weight: \(mn=x\), so \(\sqrt{mnr}=\sqrt{x(x+h)}\). The factor \(1/n\) enters only through the Hardy–Littlewood main density in (2).

## 2. The variation estimate and summed error

Localize \(x\asymp X\) smoothly and take \(|h|\le cX\), for a fixed sufficiently small \(c\). For each fixed \(A>0\),

\[
\|W_{n,h}\|_\infty+\int|W'_{n,h}(x)|\,dx
\ll_A X^{-1}(1+T|h|/X)^{-A}.
\tag{4}
\]

To check this, the argument \(u=T\log(x/(x+h))/(2\pi)\) has size comparable to \(T|h|/X\), and \(xu'(x)=O(u)\). The prefactor is \(O(X^{-1})\); its logarithmic derivative and those of the smooth packet cutoffs are \(O(X^{-1})\), with the packet derivatives carrying an additional \(1/L\). Schwartz bounds on \(\widehat\Phi\) and its derivative prove (4), including the derivative of the dyadic cutoff.

Consequently partial summation gives

\[
\left|\int W_{n,h}\,dE_{n,h}\right|
\ll_A \frac{\sup_{y\asymp X}|E_{n,h}(y)|}{X}
(1+T|h|/X)^{-A}.
\tag{5}
\]

Suppose first that the pointwise discrepancy bound is \(E_{n,h}(y)=O_\varepsilon(X^{\theta+\varepsilon})\) uniformly on the needed range. On a dyadic block \(n\asymp N\), using \(\sum_{n\asymp N}\Lambda(n)\ll N\) and
\(\sum_{h\ne0}(1+T|h|/X)^{-A}\ll X/T\) when \(X/T\gg1\), the normalized error in (1) is

\[
\boxed{\quad
O_{\varepsilon,A}\left(\frac{NX^{\theta+\varepsilon}}{TL^3}\right)
\quad}
\tag{6}
\]

per block. The finitely many logarithmic numbers of blocks can be absorbed into \(T^\varepsilon\). In the central exponent notation this gives a power saving whenever

\[
\boxed{\ \beta+\theta(\alpha+\beta)<1.\ }
\tag{7}
\]

For an independently assumed localized square-root discrepancy, \(\theta=1/2\), the domain is

\[
\boxed{\ \alpha+3\beta<2.\ }
\tag{8}
\]

At \((\alpha,\beta)=(1.2,.2)\), the central error exponent is \(-.1+\varepsilon\). Equivalently, a pointwise discrepancy exponent strictly below \(4/7\), with suitable margins, would suffice for the error step. This says nothing yet about the main term.

### Packet widths, diagonals, and tails

The logarithmic packet width must be included. On the relevant near-product support, \(n\le T^{\beta+\eta}\), while \(x+h\le T^{\alpha+\beta+\eta}\) and \(x\asymp x+h\). Thus (6), summed over the blocks, is

\[
O_\varepsilon\left(T^{\beta+\eta+\theta(\alpha+\beta+\eta)-1+\varepsilon}\right).
\tag{9}
\]

For \(\theta=1/2\), this exponent is
\(\alpha/2+3\beta/2+3\eta/2-1+\varepsilon\).
At the current frequencies any \(\eta<.05\) leaves a margin exceeding .025 before choosing \(\varepsilon\). The weaker estimate obtained by ignoring the upper cutoff on \(r\) replaces \(3\eta/2\) by \(2\eta\), and still saves a power for every fixed \(\eta<.05\).

The \(h=0\) term is handled separately. All three nonzero von Mangoldt factors then come from powers of the same prime. The positive lower packet cutoffs give a power-saving bound; for example the number of possible prime bases is at most \(T^{\beta+\eta}\), and the denominator \(mn\) is at least \(T^{\alpha+\beta-\eta}\), leaving \(O(T^{-\alpha+2\eta}\operatorname{polylog}T)\).

The region \(|h|\asymp X\), or non-comparable \(x,x+h\), is negligible by arbitrary decay of \(\widehat\Phi\), against polynomially bounded sums. It is enough to assume the discrepancy estimate for \(0<|h|\le (X/T)T^\kappa\), with a fixed small \(\kappa>0\). Outside this range the kernel argument exceeds a constant times \(T^\kappa\); arbitrary decay controls both the actual prime sum and the singular-series expression. Choose \(\kappa\) small enough that \((X/T)T^\kappa<X^{1/2-\delta}\) for some \(\delta>0\), which is possible here because the maximum \(X\) exponent is below two. Hence the whole required assumption concerns shifts smaller than the square-root scale. The difference between the endpoint-aware main term and the uncorrected \(\mathfrak S_n(h)y/n\) is at most \(\mathfrak S_n(h)|h|/n\), which is absorbed in \(O_\varepsilon(X^{1/2+\varepsilon})\) on this local range. In the integration region \(x\asymp X\gg|h|\), their derivatives are exactly equal, so (12) remains unchanged.

## 3. A weaker, localized averaged discrepancy hypothesis

Pointwise uniform Hardy–Littlewood over all twists and shifts is more than the error proof uses. For dyadic blocks compatible with the packets, the following weighted discrepancy norm suffices:

\[
\mathfrak D_T(A)=\frac1{L^3}\sum_{N,X}\sum_{n\asymp N}
\Lambda(n)|q_\beta(n)|\sum_{h\ne0}
\frac{\sup_{y\asymp X}|E_{n,h}(y)|}{X}
(1+T|h|/X)^{-A}=o(1).
\tag{10}
\]

All terms here are restricted to the comparable near-product region just treated; its complement is independently negligible. Equation (5) proves that (10) is sufficient. It requires control only for prime-power twists in this short packet, shifts concentrated near \(X/T\), and the indicated local ranges of \(y\). It can hold even with exceptional twists or shifts violating a pointwise bound.

An even weaker, signed condition is

\[
\operatorname{Re}\left\{
\frac1{L^3}\sum_n\Lambda(n)q_\beta(n)
\sum_{h\ne0}\int W_{n,h}(x)\,dE_{n,h}(x)
\right\}=o(1).
\tag{11}
\]

This condition permits cancellation between discrepancies and is exactly the error functional needed for the real observable. Equation (10) is a transparent sufficient norm for (11), not an assertion that (11) has been established. Neither condition requires all the uniformity in the original pointwise conjecture.

## 4. The main term that is still unevaluated

Under an error hypothesis above, (1) becomes

\[
P_T=\mathcal S_T+o(1),
\quad
\mathcal S_T=\frac1{L^3}\sum_n\frac{\Lambda(n)q_\beta(n)}n
\sum_{h\ne0}\mathfrak S_n(h)
\int_0^\infty W_{n,h}(x)\,dx.
\tag{12}
\]

The further required conclusion is

\[
\operatorname{Re}\mathcal S_T\longrightarrow-\beta c_\psi
\tag{13}
\]

(or any nonzero limiting or subsequential value sufficient to exclude the specified pair-AH). **This note does not prove (13).** The phase, nonlinear change of variables, prime-power averaging, packet widths, and the surviving arithmetic fluctuations of the singular series must all be retained in evaluating it.

A first-average replacement of the singular series is inadequate: \(\int\widehat\Phi=\Phi(0)=0\), with analogous vanishing for every polynomial moment. Thus a continuous mean-density approximation loses the main signal. A sharp signed singular-series calculation is a separate substantive step, not an error estimate that can be bundled into (6).

Centering the two long prime weights by replacing \(\Lambda(m),\Lambda(r)\) with \(\Lambda(m)-1,\Lambda(r)-1\) is legitimate for the **whole packet** by the nonstationary Poisson argument in `REPORT.md`. The proof above deliberately first applies Hardy–Littlewood to the uncentered prime pair. One must not replace \(\mathfrak S_n(h)\) by a guessed centered version term by term without computing the corresponding background sums.

## Source and interpretation

The independent local square-root discrepancy has the error scale proposed in Conjecture 1.8 in Fazzari–Gerspach, *The third moment of the logarithm of zeta and a twisted pair correlation conjecture*. [Versioned primary paper](https://arxiv.org/abs/2412.20099v1)

Their Theorem 1.9 has a different smoothed observable and the conservative range \(1-\beta\le\alpha\le2-48\beta\). The calculation here does not improve that theorem. It establishes that **for our specific packet, its error-transfer stage alone** allows the broader domain (8), conditional on the consistent localized discrepancy estimate defined here, not on the defective full two-sign formulation as printed. The singular-series asymptotic needed to turn this into a complete conditional theorem remains open in this note.


---

# Endpoint correction to a cited two-sign prime-pair formulation

_Source: arithmetic/ENDPOINT_CORRECTION.md_

6 November 2026. Independently checked against the rendered original PDF, printed page 7, Conjecture 1.8 of Fazzari–Gerspach, *The third moment of the logarithm of zeta and a twisted pair correlation conjecture*, arXiv:2412.20099v1. [Primary PDF, page 7](https://arxiv.org/pdf/2412.20099v1#page=7)

## What is printed, and the exact endpoint check

The displayed formula uses the same main term for both signs:

\[
\sum_{m\le x}\Lambda(m/n)\Lambda(m\pm h)
=\frac{\mathfrak S_n(h)}n x+O_\varepsilon(x^{1/2+\varepsilon}),
\qquad 1\le h,n\le x^{1-\varepsilon}.
\tag{1}
\]

This is visible in the original PDF, not an OCR substitution. Under the usual convention that the von Mangoldt function vanishes away from positive prime powers, set \(n=1\) and define

\[
A_+(x,h)=\sum_{1\le m\le x}\Lambda(m)\Lambda(m+h),\qquad
A_-(x,h)=\sum_{h<m\le x}\Lambda(m)\Lambda(m-h).
\]

Changing variables gives the exact identity

\[
A_-(x,h)=A_+(x-h,h).
\tag{2}
\]

Choose \(\varepsilon=1/10\), and take an even integer \(h\sim x^{3/4}\). Both \(h\le x^{9/10}\) and \(h\le(x-h)^{9/10}\) hold for large \(x\). Applying the two printed estimates to (2) would force

\[
\mathfrak S(h)h=O(x^{3/5}).
\]

For even \(h\), the singular series defined immediately above (1) is bounded below by the fixed positive twin-prime constant \(2\prod_{p>2}(1-(p-1)^{-2})\). Thus the left side is bounded below by a positive constant times \(x^{3/4}\), a contradiction.

The two signs cannot simultaneously have the printed common main term throughout that stated range. A source interpretation using an unstated even extension of \(\Lambda\) to negative integers would change the sum and would not be the conventional prime-pair assertion; our work uses only positive prime powers.

## Consistent formulation and relevance to our packet

The ordinary endpoint-aware main term for a signed shift \(h\) is

\[
\frac{\mathfrak S_n(h)}n\,(x-\max(0,-h))_+.
\tag{3}
\]

In particular the minus-sign main term at \(n=1\) is \(\mathfrak S(h)(x-h)_+\). This restores consistency with the exact identity. No claim is made here that the square-root remainder in this repaired global formulation is proved, or that every theorem in the cited paper has now been checked with it.

For our near-product packet the needed scales are

\[
x\asymp X,\qquad |h|\asymp X/T,\qquad
X\le T^{1.4+\eta},\quad \eta<.05.
\]

They satisfy \(X/T\ll X^{1/2}\) with a fixed power margin. Even allowing a small power enlargement of the effective shift range preserves this inequality. The endpoint difference is at most \(\mathfrak S_n(h)|h|/n\), which is absorbed by a localized \(O_\varepsilon(X^{1/2+\varepsilon})\) discrepancy bound. On the actual integration region \(x\asymp X\gg |h|\), the derivative of (3) is exactly \(\mathfrak S_n(h)/n\), so the partial-summation main integral is unchanged.

Accordingly, `CONDITIONAL_NEXT.md` now defines discrepancy against (3) and assumes a consistent **independent local estimate** only on the needed near shifts. It does not adopt the full printed assertion (1). The conditional error exponent and the unevaluated signed singular-series main term are unchanged.

## Scope of this correction

This is an endpoint defect in a particular written uniform two-sign formulation. It is **not a refutation of the Hardy–Littlewood prime-pair conjecture**, not a new prime-distribution result, and not a claim that the paper's intended conditional conclusions are false. The correction removes an inconsistent premise from our own research notes and makes their remaining assumptions explicit.

Updated companion files: `REPORT.md` and `CONDITIONAL_NEXT.md`.


---

# Evaluating the signed singular-series main term

_Source: arithmetic/MAIN_TERM_THEOREM.md_

6 November 2026. Research derivation, with known inputs identified. This completes the main-term calculation left open in the preceding checkpoint. It gives a conditional theorem and a weaker sufficient signed inequality; it does not establish the required prime-pair discrepancy estimate.

## 1. Statement and status

Set \(L=\log T\), \(\gamma=\alpha+\beta\), and choose fixed parameters and packet width with

\[
\beta>\eta>0,\qquad \alpha-\eta>1,\qquad \gamma+\eta<2.
\tag{1}
\]

Take a real, even Schwartz envelope \(\psi\) whose Fourier transform \(q\) is smooth and supported in \((-\eta,\eta)\), with \(c_\psi=\int\psi^3>0\). The previous nonnegative construction is allowed. Let \(\Phi\ge0\) be smooth, supported in \((1,2)\), and normalized by \(\int\Phi=1\). Fourier transforms use \(e^{-2\pi ixy}\). Write

\[
Z_\nu(t)=\sum_{\rho=1/2+i\gamma_j}\psi\left(\frac{L(\gamma_j-t)}{2\pi}\right)
e\left(\nu\frac{L(\gamma_j-t)}{2\pi}\right).
\]

Assume RH, and count all zero ordinates with multiplicity. Define the **raw** alias mean

\[
M_T=\frac1{Tc_\psi}\int\Phi(t/T)\operatorname{Re}
\left[Z_\alpha Z_\beta\overline{Z_\gamma}
-\overline{Z_{2-\alpha}}Z_\beta Z_{2-\gamma}\right]dt.
\tag{2}
\]

This is not the recorded distinct-index Hann statistic. It has the same pointwise half-grid cancellation, and its sine-process expectation is exactly \(\beta\).

**Derived arithmetic identity.** For the signed discrepancy functional \(\mathcal R_T\) defined below,

\[
\boxed{\quad M_T=\beta-\frac{\operatorname{Re}\mathcal R_T}{c_\psi}+o(1).\quad}
\tag{3}
\]

The proof uses a known singular-series average of Fazzari–Gerspach, not their defective full two-sign prime-pair conjecture. Formula (3) itself does not assume a conjectural bound on \(\mathcal R_T\).

Consequences:

- If \(\operatorname{Re}\mathcal R_T=o(1)\), then \(M_T\to\beta\). This is a completed **conditional packet theorem**.
- More weakly, if \(\limsup\operatorname{Re}\mathcal R_T<\beta c_\psi\), then \(\liminf M_T>0\). This already contradicts the full off-half-grid pair-mass concentration hypothesis described in the earlier checkpoint, under RH.
- Even \(\liminf\operatorname{Re}\mathcal R_T<\beta c_\psi\) gives a positive subsequential mean, also incompatible with that pair-AH implication \(M_T\to0\).

Under RH, bounded fixed-window count moments and the Schwartz-tail argument also give \(M_T=O_{\alpha,\beta,\psi,\Phi}(1)\). Formula (3) therefore already implies \(\operatorname{Re}\mathcal R_T=O_{\alpha,\beta,\psi,\Phi}(1)\), without a prime-pair discrepancy conjecture. Full pair-AH would require the specific cancellation \(\operatorname{Re}\mathcal R_T\to\beta c_\psi\). The open task is to beat or exclude that positive threshold; arbitrary smallness is a sufficient but unnecessarily strong objective.

No threshold-beating bound on \(\mathcal R_T\) is proved here. The contribution is an explicit packet calculation and reduction using known arithmetic input. It is not a new general Hardy–Littlewood-to-GUE principle and carries no claim of having solved a famous conjecture.

## 2. Exact arithmetic decomposition and endpoint convention

Abbreviate \(q_\nu(v)=q(\log v/L-\nu)\). For a signed nonzero integer shift \(h\), set

\[
A_{n,h}(y)=\sum_{k\le y}\Lambda(k/n)\Lambda(k+h),\qquad
E_{n,h}(y)=A_{n,h}(y)-\frac{\mathfrak S_n(h)}n(y-\max(0,-h))_+.
\tag{4}
\]

Here \(\Lambda(k/n)=0\) unless \(n\mid k\), and \(\Lambda\) vanishes away from positive prime powers. For \(n=p^a\),

\[
\mathfrak S_n(h)=\mathbf1_{(n,h)=1}\mathfrak S(nh),
\]

where \(\mathfrak S\) is the usual prime-pair singular series, even in its argument. Use

\[
W_{n,h}(x)=\frac{q_\alpha(x/n)q_\gamma(x+h)}{\sqrt{x(x+h)}}
\widehat\Phi\left(\frac{T}{2\pi}\log\frac{x}{x+h}\right)
\tag{5}
\]

on \(x>0,x+h>0\), and zero elsewhere. The smooth cutoffs make each integral compactly supported away from its singular endpoints. Define

\[
\mathcal R_T=\frac1{L^3}\sum_n\Lambda(n)q_\beta(n)
\sum_{h\ne0}\int W_{n,h}(x)\,dE_{n,h}(x),
\tag{6}
\]

and

\[
\mathcal S_T=\frac1{L^3}\sum_n\frac{\Lambda(n)q_\beta(n)}n
\sum_{h\ne0}\mathfrak S_n(h)\int W_{n,h}(x)\,dx.
\tag{7}
\]

The factor \(1/n\) belongs in (7), **not** in (6). It is already present in the discrepancy's subtracted density.

The explicit formula and the substitution \(x=nm, h=r-nm\), established in the preceding checkpoint, give

\[
M_T=-\operatorname{Re}(\mathcal S_T+\mathcal R_T)/c_\psi+o(1).
\tag{8}
\]

The equal-product \(h=0\) term is negligible: all three von Mangoldt factors then arise from powers of a common prime. In the low-frequency raw term, the matched single variable is at most \(T^{2-\alpha+\eta}<T\), with a fixed margin. Near-comparable products are therefore also shorter than \(T\), so unequal integers are suppressed by the height Fourier kernel; non-comparable products have a kernel argument of order \(T\) and are negligible by Schwartz decay. This does not require the entire independently truncated product to be shorter than \(T\). No repeated-zero subtraction is needed.

The overlap-length convention in (4) is consistent for both signs. On the support of (5), the derivative of the subtracted continuous main term is exactly \(\mathfrak S_n(h)/n\). The endpoint error in the original printed global Conjecture 1.8 is therefore not imported into this calculation.

## 3. The known singular-series input

For \(n=p^a\), define \(B_n(y)=\sum_{1\le h\le y}\mathfrak S_n(h)\). Fazzari–Gerspach, Lemma 2.7, equation (2.29), gives, **uniformly in \(y\) and the prime power \(n\)**,

\[
B_n(y)-y=-\frac12\min\{\log p,\log y\}
+O((\log y)^{2/3}).
\tag{9}
\]

We use the harmless bounded extension \(\log^+y\) and error \(O(1+(\log(2+y))^{2/3})\) near zero. This is a singular-series lemma, separate from the prime-pair conjecture; it is stated without an RH assumption. Its proof cites Friedlander–Goldston's singular-series average. [Primary paper, printed pages 17–18](https://arxiv.org/pdf/2412.20099v1#page=17)

One immediate uniform consequence is \(B_n(y)\ll y\) for \(y\ge1\). We use both the signed secondary term and this positive upper bound.

### A smoothed consequence with all constants fixed

Let

\[
K(u)=\operatorname{Re}\widehat\Phi(u/(2\pi))
=\int\Phi(t)\cos(tu)\,dt.
\]

Then \(K\) is real, even, Schwartz, \(K(0)=1\), and

\[
\int_\mathbb R K(u)\,du=2\pi\Phi(0)=0.
\tag{10}
\]

For \(H\ge p\), we claim

\[
\boxed{\quad
\sum_{h\ne0}\mathfrak S_n(h)K(h/H)
=-\log p+O_\Phi\left(1+(\log(2+H))^{2/3}+(p/H)^2\right).
\quad}
\tag{11}
\]

Proof: the two signs give twice the positive sum. Integrate \(K(y/H)\) against \(dB_n(y)\), use (9), and integrate by parts. The density term is zero by (10), and the remaining main integral is

\[
\int_0^\infty\min\{\log p,\log^+(Hu)\}K'(u)\,du.
\tag{12}
\]

Replacing the minimum by \(\log p\) gives \(-\log p\). The replacement is supported on \(u<p/H\). Since \(K'(0)=0\) and \(|K'(u)|\ll u\) there, the error is bounded by

\[
O\left(\frac{\log p}{H^2}
+\int_0^{p/H}u\log\frac{p}{Hu}\,du\right)
=O((p/H)^2).
\]

The error in (9), integrated against \(|K'|\), is \(O(1+(\log(2+H))^{2/3})\). These estimates prove (11). In particular the coefficient is **−1 times \(\log p\)**: the factor one-half in (9) is canceled by the two signs of \(h\).

## 4. Replacing the nonlinear kernel

Write \(H=x/T\). In the comparable region \(|h|\le x/2\), ordinary differentiation and Schwartz bounds give, for any fixed sufficiently large \(A\),

\[
\left|W_{n,h}(x)-\frac{q_\alpha(x/n)q_\gamma(x)}x
\widehat\Phi\left(-\frac{h}{2\pi H}\right)\right|
\ll_A\frac{|h|}{x^2}(1+|h|/H)^{-A}.
\tag{13}
\]

Indeed the logarithmic phase error is \(O(T(h/x)^2)\); the envelope and reciprocal-square-root changes are \(O(|h|/x)\) relative to \(x^{-1}\). Extra powers of \(|h|/H\) are absorbed by increasing the Schwartz decay order.

From \(B_n(y)\ll y\) and partial summation,

\[
\sum_{h\ne0}\mathfrak S_n(h)|h|(1+|h|/H)^{-A}\ll H^2.
\]

Thus summing the error in (13) over shifts gives \(O(T^{-2})\) for each \(x\), uniformly in \(n\). Since the pertinent range has \(x\ll T^{\gamma+\eta}\), the total error in (7) is

\[
O(T^{\gamma+\eta-2}/L^2)=o(1).
\tag{14}
\]

Here \(\sum\Lambda(n)|q_\beta(n)|/n\ll L\). The non-comparable and large-shift tails are smaller than any power of \(T\): the Fourier-kernel argument is then of order \(T\), while the finite packet sums and singular series have polynomial bounds.

The leading linearized sum is real, since opposite shifts are conjugates. Also

\[
\frac Hp=\frac{x/n}{T}\frac np\ge T^{\alpha-\eta-1}
\]

whenever its envelope is nonzero. Thus (11) applies uniformly, and the \((p/H)^2\) error saves a power. Inserting it into (7) yields

\[
\operatorname{Re}\mathcal S_T
=-\frac1{L^3}\sum_n\frac{\Lambda(n)^2q_\beta(n)}n
\int q_\alpha(x/n)q_\gamma(x)\frac{dx}x
+O(L^{-1/3})+o(1).
\tag{15}
\]

The \(O(L^{-1/3})\) comes from a uniform \(O(L^{2/3})\) shift error, an \(O(L)\) weighted twist sum, and an \(O(L)\) logarithmic integral, divided by \(L^3\).

## 5. Prime averaging and the exact packet convolution

Set

\[
J(v)=\int_\mathbb R q(u-\alpha)q(u+v-\gamma)\,du.
\]

Changing variables \(u=\log(x/n)/L\) in (15) makes its main term

\[
-\frac1{L^2}\sum_n\frac{\Lambda(n)^2}{n}
q(\log n/L-\beta)J(\log n/L).
\tag{16}
\]

Higher prime powers contribute \(o(1)\), because their reciprocal weighted tail above \(T^{\beta-\eta}\) is \(O(T^{-(\beta-\eta)/2}\operatorname{polylog}T)\). Partial summation with the prime number theorem gives, for a fixed smooth compactly supported \(F\) away from zero,

\[
\frac1{L^2}\sum_p\frac{(\log p)^2}{p}F(\log p/L)
\longrightarrow\int vF(v)\,dv.
\tag{17}
\]

Therefore the limit of (16) is

\[
-\iint v\,q(v-\beta)q(u-\alpha)q(u+v-\gamma)\,du\,dv.
\]

Put \(a=u-\alpha,b=v-\beta\). Since \(\gamma=\alpha+\beta\), this becomes

\[
-\iint(\beta+b)q(a)q(b)q(a+b)\,da\,db.
\]

The term containing \(b\) is odd under \((a,b)\mapsto(-a,-b)\). The remaining convolution equals
\(\beta\int\psi^3=\beta c_\psi\). Hence

\[
\boxed{\quad\operatorname{Re}\mathcal S_T\longrightarrow-\beta c_\psi.\quad}
\tag{18}
\]

Equations (8) and (18) prove (3). The sign reverses once when passing from the prime packet to the zero statistic, so the predicted zero mean is **+\(\beta\)**.

## 6. A sufficient local discrepancy hypothesis

The previous checkpoint proves that an endpoint-aware estimate
\(E_{n,h}(y)=O_\varepsilon(X^{1/2+\varepsilon})\), uniformly only on the packet-compatible blocks \(n\asymp N,y\asymp X\) and near shifts \(|h|\le(X/T)T^\kappa\), implies \(\mathcal R_T=o(1)\) if

\[
\alpha+3\beta+3\eta<2.
\tag{19}
\]

The resulting error exponent is \(\alpha/2+3\beta/2+3\eta/2-1+\varepsilon\). Conditions (1) and (19) hold for \(\alpha=1.2,\beta=.2\) and every \(0<\eta<.05\). Thus a precise endpoint-consistent localized Hardy–Littlewood assumption now gives the **complete** conclusion \(M_T\to1/5\), rather than merely control of an unevaluated main term.

The averaged absolute discrepancy norm from the earlier checkpoint also suffices. The threshold in Section 1 is weaker still: one only needs an upper bound below \(\beta c_\psi\) for the real signed error, not its full asymptotic vanishing.

These hypotheses remain unproved for the actual primes. The next arithmetic task is therefore to bound that signed error functional; the singular-series main term is no longer an outstanding step.

## 7. Verification and failed approaches

`check_normalizations.py` and `normalizations.json` contain reproducible floating-point diagnostics for the signed shift sum and the two-dimensional packet normalization. They are not interval certificates and do not test the unproved prime-pair discrepancy premise.

A naive Ramanujan expansion produces two separately logarithmically divergent pieces. The special prime's Euler factor must remain coupled to the rest of the expansion. Lemma 2.7 avoids that rearrangement entirely. Likewise, direct truncation of the full numerical shift sum leaves a large oscillatory mean-density tail. The stable diagnostic subtracts density one and restores its exactly known contribution using Poisson summation. These are computational or summation-order issues, not counterexamples to (11).

The known singular-series lemma is credited to its source. The new work here is its precise application to this raw alias packet, the nonlinear-to-linear kernel control, the complete normalization, and the explicit one-sided discrepancy target. Ordinary derivations and independent review are not formal verification.


---

# Independent audit and completion of the singular-series main term

_Source: arithmetic/MAIN_TERM_INDEPENDENT_REVIEW.md_

6 November 2026. This note audits the arithmetic packet and proves the remaining singular-series asymptotic using an existing uniform singular-series lemma. It does not prove the required prime-pair discrepancy estimate, and hence does not prove an RH-only zeta correlation result.

## 1. Result and dependencies

Let q, psi, Phi, L, alpha, beta and gamma=alpha+beta be as in the arithmetic packet. In particular q is real, even and smooth with compact support in (-eta,eta), psi is its inverse Fourier transform, c_psi=integral psi^3>0, and Phi is real smooth, supported in (1,2), with integral one. Assume

\[
\alpha-\eta>1,\qquad \beta>\eta,\qquad
\gamma+\eta<2,
\]

and the remaining stated packet-chamber margins. Write S_T for equation (12) of `CONDITIONAL_NEXT.md`. Then

\[
\boxed{\operatorname{Re}S_T=-\beta c_\psi+o(1).}
\]

The proof uses Fazzari-Gerspach Lemma 2.7, equation (2.29), and the prime number theorem. That lemma is a singular-series average, not their defective two-sign uniform prime-pair conjecture. Thus the main-term calculation does not inherit the endpoint defect in Conjecture 1.8.

Combined with the signed discrepancy hypothesis (11) of `CONDITIONAL_NEXT.md`, the raw prime packet has real part tending to -beta c_psi. Combined additionally with the packet's RH explicit-formula reduction, the proposed raw zero observable tends to +beta. Full local pair-AH would instead force it to zero by the count-moment argument. The unproved discrepancy hypothesis is therefore indispensable in the conditional conclusion.

The pointwise local square-root discrepancy is one sufficient input when alpha+3 beta+3 eta<2, with a strict margin. The weaker averaged signed discrepancy condition remains sufficient outside the pointwise error-transfer discussion.

## 2. Primary-source check

The local primary PDF is `/private/tmp/astra-zeta-nov06-quant/arithmetic/twisted.pdf`. I extracted its text and visually inspected printed p.17; the rendering is `fg-lemma-2-7.png` in this directory. Lemma 2.7 states, uniformly for the prime-power twist n=p^a and y in its large-y range,

\[
A_n(y):=\sum_{1\le h\le y}\mathfrak S_n(h)
=y-\frac12\min\{\log p,\log y\}
 +O((\log y)^{2/3}).
\tag{A}
\]

Replacing the error by O((1+log y)^(2/3)) handles all y>=1. Its proof refers to a prior singular-series estimate, not to the prime-pair conjecture. The section treats odd p in detail and explicitly says p=2 is obtainable with minor modification. The displayed lemma is uniform in n and y. [Versioned primary source](https://arxiv.org/abs/2412.20099v1)

No Ramanujan-series rearrangement is needed below. In particular, convergence issues in interchanging a conditionally convergent Ramanujan expansion with a shrinking-frequency kernel are avoided.

## 3. A uniform signed smoothing lemma

Let f be a fixed real even Schwartz function with integral over R equal to zero. Let H>=p>=2. Then (A) implies

\[
\boxed{
\sum_{h\ne0}\mathfrak S_{p^a}(h)f(h/H)
=-(\log p)f(0)
 +O_f\left((1+\log H)^{2/3}+(p/H)^2\right).
}
\tag{B}
\]

Here the sum excludes h=0. The singular series is even, so the left side is twice its positive-h part. Partial summation gives

\[
2\sum_{h\ge1}\mathfrak S_n(h)f(h/H)
=-2\int_0^\infty A_n(y)H^{-1}f'(y/H)\,dy.
\]

The term A_n(y)=y contributes 2H integral_0^infinity f=0. After writing y=Hu, the logarithmic term contributes

\[
\int_0^\infty
\min\{\log p,\log^+(Hu)\}\,f'(u)\,du.
\]

For u>=p/H this is the constant log p. Integrating that constant over the full half-line gives -(log p)f(0). The difference is supported on 0<=u<p/H. Since f is even, f'(0)=0 and |f'(u)|<=C_f u for u<=1. Consequently the transition contributes O_f((p/H)^2); the small interval Hu<1 is included in this bound. Finally, the error in (A) contributes at most

\[
C\int_0^\infty (1+\log(2+Hu))^{2/3}|f'(u)|\,du
\ll_f(1+\log H)^{2/3}.
\]

This proves (B), with its sign, factor of two, and exclusion of the diagonal explicit.

For our height kernel set

\[
f(u)=\operatorname{Re}\widehat\Phi(u/(2\pi)).
\]

It is even because Phi is real. Moreover f(0)=1 and integral_R f=2 pi Phi(0)=0, because Phi is supported away from zero. Thus the main term in (B) is exactly -log p, with no missing 2 pi factor.

## 4. Removing the nonlinear shift weight

The exact weight in the source packet is

\[
W_{n,h}(x)=\frac{q_\alpha(x/n)q_\gamma(x+h)}{\sqrt{x(x+h)}}
\widehat\Phi\left(\frac{T}{2\pi}\log\frac{x}{x+h}\right).
\]

Put H=x/T and define

\[
W^0_{n,h}(x)=\frac{q_\alpha(x/n)q_\gamma(x)}x
\widehat\Phi\left(-\frac{h}{2\pi H}\right).
\]

For |h|<=x/2, smoothness and Schwartz decay imply, for every fixed A,

\[
\boxed{|W_{n,h}(x)-W^0_{n,h}(x)|
\ll_A\frac{|h|}{x^2}(1+|h|/H)^{-A}.}
\tag{C}
\]

Indeed the denominator and q_gamma change by O(|h|/x) relatively at the amplitude scale 1/x. The two Fourier arguments differ by O(T(h/x)^2). Their intervening arguments remain comparable to h/H in absolute value. Multiplying the latter difference by a Schwartz derivative gives a term bounded by |h|/x^2 times (|h|/H), which is absorbed by increasing A before applying the bound.

The singular series is nonnegative. Formula (A) implies uniformly A_n(Y)<<Y for Y>=1, so partial summation gives

\[
\sum_{h\ne0}\mathfrak S_n(h)|h|(1+|h|/H)^{-A}\ll_A H^2
\]

when H>=1 and A>2. Hence the h-sum of the error in (C) is O(T^-2), uniformly in n and x.

On the comparable part of the original packet, x is at most 2 T^(gamma+eta). Also sum_n Lambda(n)|q_beta(n)|/n=O(L). After the x integral and normalization L^-3, the whole nonlinear-weight error is therefore

\[
O\left(T^{\gamma+\eta-2}/L^2\right)=o(1).
\tag{D}
\]

The region |h|>x/2, including nonpositive x+h and noncomparable positive variables, is handled before the linearization. The exact kernel there has a Fourier argument of size at least cT whenever both positive variables are comparable to their prescribed packets; outside comparable packets it is no smaller. The smooth packet supports bound all sums and integrals by fixed powers of T. Arbitrary Schwartz decay therefore makes this region negligible. The corresponding tails of the extended W^0 sum have |h|/H>T/2 and are likewise negligible. This justifies extending the linearized sum over every nonzero integer h.

## 5. Applying the signed smoothing lemma uniformly through the packet

For a prime-power n=p^a on the support, H/p is bounded below by

\[
\frac{x}{Tp}\ge\frac{x}{Tn}
\ge T^{\alpha-\eta-1}.
\]

Thus H>=p and p/H tends to zero by a fixed power, uniformly in every contributing n and x. Also log H=O(L). Applying (B) to the real part of W^0 gives

\[
\operatorname{Re}S_T
=-\frac1{L^3}\sum_n\frac{\Lambda(n)^2q_\beta(n)}n
\int_0^\infty q_\alpha(x/n)q_\gamma(x)\frac{dx}x
+o(1).
\tag{E}
\]

The smoothing error O(L^(2/3)) contributes O(L^(-1/3)) after the two logarithmic integrations. The transition error contributes O(T^(-2(alpha-eta-1))/L). These bounds, together with (D), justify the o(1) in (E).

The second Lambda factor in (E) is log p from the singular-series smoothing, equal to Lambda(n) for n=p^a. It is not log n when a>1. This distinction is necessary before discarding higher prime powers.

## 6. PNT convolution and exact coefficient

Set u=log(x/n)/L and v=log n/L. The x integral in (E) is

\[
L\int q(u-\alpha)q(u+v-\gamma)\,du.
\]

Higher powers p^a with a>=2 contribute o(1): on n>=T^(beta-eta), their sum of (log p)^2/n is power-small up to powers of L. For the prime terms, partial summation with the prime number theorem yields

\[
\operatorname{Re}S_T\longrightarrow
-\int\!\int v\,q(v-\beta)q(u-\alpha)
q(u+v-\gamma)\,du\,dv.
\]

Writing a=u-alpha and b=v-beta turns this into

\[
-\int\!\int(\beta+b)q(a)q(b)q(a+b)\,da\,db.
\]

The b term vanishes under (a,b)->(-a,-b), since q is even. Fourier inversion gives integral q(a)q(b)q(a+b)=integral psi^3=c_psi. The limit is therefore exactly -beta c_psi. In the original frequencies beta=1/5, the raw zero statistic has conditional limit +1/5.

## 7. Audit of the preceding reductions

### Raw versus distinct-index observables

The raw difference vanishes termwise on translated half-grids even with repeated labels: its complex phase ratio is exp(4 pi i(x_i-x_k)). Removing repeated-index subtraction is legitimate for this newly defined observable. It does change the sine prediction: the original distinct-index statistic and the raw statistic are not interchangeable.

Away from coordinate axes, the raw sine spectral density is

\[
1-\sum_j(1-|\xi_j|)_+
+2(1-\sum_j\xi_j^+)_+.
\]

In the high chamber it equals xi_2; in the low chamber it is zero. The even envelope cancels the first-order packet displacement, giving precisely beta c_psi. Thus the +1/5 coefficient and the prime-packet sign agree independently.

### Explicit formula and centering

With e(x)=exp(2 pi i x), each positive-frequency zero trace has prime term -L^-1 sum Lambda(n)n^-1/2 q(log n/L-alpha)n^-it. Multiplication of the three trace terms gives a minus sign. Height averaging produces Phi-hat(T log(mn/r)/(2 pi)), exactly the source convention.

The Fourier packet misses zero. All gamma-density Taylor moments consequently vanish; rapid decay handles the tail and the explicit pole evaluations. The claimed rapidly small remainders require fixed packet parameters, which are the parameters used here.

For alpha-eta>1, the unweighted long Dirichlet polynomial is rapidly small by Poisson summation: the phase has no stationary integer frequency on n>>T. Therefore replacing each long Lambda factor by Lambda-1 is valid for the complete packet. It is not a license to center the Hardy-Littlewood singular series term by term. The main-term proof above correctly starts from the uncentered pair correlation.

### Diagonal and short low packet

The h=0 prime-product diagonal forces all three von Mangoldt factors to be powers of one prime. Their positive lower packet cutoffs make its normalized contribution power-small. It is correctly excluded from the singular-series smoothing lemma.

The low packet is inside the restricted-correlation region. Its direct prime proof also works: near a product equality the target integer remains below T by a fixed power, so unequal integers are killed by the height Fourier kernel; exact equality is the negligible common-prime-power diagonal. In a general packet one should use this near-comparable argument, rather than require unnecessarily that the product of the two independent upper cutoffs be below T. The concrete eta<0.05 packet satisfies even that stronger easy condition.

### Fixed-window count moments

The positive bandlimited majorant construction in the source packet satisfies the Rudnick-Sarnak support restriction: for the \(r\)-fold convolution test, each frequency lies in \((-\delta,\delta)\) and their sum is zero, giving \(\sum_j|\xi_j|<r\delta\le k\delta<2\). It majorizes every cluster of diameter at most \(2W\). The height-localized distinct-tuple bound is \(O(T\log T)\); each tuple contributes at most \(4\pi W/\log T\) to the center integral. Repeated-index partitions then give all fixed local count moments. This uses the RH interval-cutoff extension stated after Rudnick-Sarnak Theorem 1.1. I found no missing occupancy hypothesis in this argument.

**Multiplicity convention checked explicitly.** Printed p.1028 says the ordinates are counted with multiplicities. Printed p.1029, directly after equation (1.4), specifies summation over distinct indices. Thus equal ordinate values carrying different zero indices are included in the starred correlation sum. The paper does not silently assume simplicity here. I checked the extracted source and visually inspected printed p.1029; `rs-distinct-indices.png` records the latter.

**Direct proof, also including multiplicities.** The root investigator proposed this alternative, and its coefficient and mean-square bounds were independently checked here. Fix an integer \(k\ge1\) and choose a nonnegative even Schwartz majorant \(\phi\ge1\) on \([-W,W]\), with smooth Fourier support in \((-\delta,\delta)\), where \(k\delta<1\). Such a majorant exists at arbitrarily small positive bandwidth, with constants depending on W,k. Under RH the explicit formula gives, uniformly for \(t\in[T,2T]\),

\[
0\le K_W(t)\le\sum_\gamma\phi(L(\gamma-t)/(2\pi))
\le C_{W,k}+2|D(t)|,
\]

where the zero sum includes multiplicity and

\[
D(t)=\sum_{p\le T^\delta}a_p p^{-it},\qquad
a_p=\frac{\log p}{L\sqrt p}\widehat\phi(\log p/L).
\]

The bounded gamma-density term and pole terms are absorbed into C. Prime powers \(p^a\) with \(a\ge2\) also contribute \(O(1)\) in absolute value: the squares use \(\sum_{p\le T^{\delta/2}}\log p/p\ll L\), and the contributions from \(a\ge3\) are absolutely summable before division by \(L\).

Chebyshev's prime bound and partial summation give \(\sum_p|a_p|^2=O_{W,k}(1)\). Write \(D(t)^k=\sum_{m\le N}b_m m^{-it}\), where \(N\le T^{k\delta}\). Unique prime factorization and Cauchy-Schwarz over at most k! ordered representations give

\[
\sum_m|b_m|^2\le k!\left(\sum_p|a_p|^2\right)^k.
\]

For m!=n, the elementary integral bound is

\[
\left|\int_T^{2T}(m/n)^{-it}dt\right|
\le\frac{2N}{|m-n|}.
\]

Using \(2|b_mb_n|\le|b_m|^2+|b_n|^2\) and the harmonic sum \(H_N\),

\[
\frac1T\int_T^{2T}|D(t)|^{2k}dt
\le\left(1+\frac{4NH_N}{T}\right)\sum_m|b_m|^2
=O_{W,k}(1).
\]

The strict inequality \(k\delta<1\) makes \(NH_N/T\) tend to zero. It follows that the \(2k\)-th local count moment is bounded, and therefore every fixed count moment is bounded. This direct proof requires RH for positivity of the zero majorant but no simplicity assumption and no convention about factorial correlations. It independently confirms the Rudnick-Sarnak argument.

The source's quantitative pair-AH bound is also valid: the off-half-grid pair count B_eta gives |R|<=4 pi eta K^3+2K B_eta, followed by a fourth-moment tail split. Schwartz tails are controlled by the same fixed moments and rapid envelope decay. This concerns full local off-lattice pair concentration, not protected-band pair matching.

### The localized discrepancy exponent

After x=nm the exact weight is 1/sqrt(x(x+h)); there is no additional n factor. A local discrepancy O(X^(theta+epsilon)), a weight variation O(X^-1), approximately X/T relevant shifts, and sum_{n~N} Lambda(n)=O(N) give error NX^theta/(T L^3), up to epsilon factors. Thus beta+theta(alpha+beta)<1 is correct. For theta=1/2 it is alpha+3 beta<2. Including packet widths gives the sufficient strict inequality alpha+3 beta+3 eta<2. No improvement to the source paper's different observable is claimed by this accounting.

## 8. Scope and the remaining obstacle

This completes the singular-series calculation that the earlier continuation had deliberately left open. The resulting theorem is conditional on a specified near-product prime-pair discrepancy functional; it is not an unconditional or RH-only exclusion of AH. The exact main term is consistent with the source paper's twisted-correlation mechanism and requires no claim of external novelty.

The meaningful next problem is now sharper: prove the signed discrepancy functional is o(1), or bound it away from the precise cancellation that would erase the -beta c_psi singular-series contribution. Standard first-order prime density cannot do that. The phase kernel has zero integral, so its mean-density term cancels and the secondary singular-series term survives.


---

# Audit of the singular-series input to the signed main term

_Source: arithmetic/SOURCE_INPUT_AUDIT.md_

6 November 2026. This note audits the source of the singular-series mean used in MAIN_TERM_THEOREM.md. It does not prove the localized prime-pair discrepancy hypothesis.

## Source and exact scope

Fazzari–Gerspach, *The third moment of the logarithm of zeta*, arXiv:2412.20099v1, Lemma 2.7, equation (2.29), printed pp.17–18, states uniformly in y and n that
\[
\sum_{1\le h\le y}\mathfrak S_n(h)-y
=-\frac12\min\{\Lambda(n),\log y\}
+O((\log y)^{2/3}).
\]
Here the surrounding section takes n=q^a, a prime power. Its opening paragraph explicitly treats odd q>2 in the proofs and says the q=2 case follows by modification. Use y≥2, or write log(2y) in the error if the integration reaches bounded y.

This is an unconditional singular-series statement. The preceding Lemma 2.6 assumes RH, but Lemma 2.7 does not inherit that hypothesis implicitly: its proof invokes Friedlander–Goldston's unconditional singular-series mean. This is independent of the endpoint defect in the paper's Conjecture 1.8.

Primary sources:
- [FG Lemma 2.7](https://arxiv.org/pdf/2412.20099v1#page=17).
- [Friedlander–Goldston (1995), DOI 10.1215/ijm/1255986635](https://doi.org/10.1215/ijm/1255986635).
- [Author-uploaded copy](https://www.researchgate.net/publication/254209041_Some_singular_series_averages_and_the_distribution_of_Goldbach_numbers_in_short_intervals).

The FG v1 PDF text and its section context were read directly. The publisher's FG95 PDF endpoint returned a security interstitial in this audit; the author-uploaded text was readable. Its Proposition 1 includes an x≥r condition and discusses an extra factor for removing that restriction. Therefore one should not claim that an arbitrary-r uniform estimate was independently re-proved here.

## A separate prime-modulus check

Let S(h) denote the ordinary two-prime singular series, extended by zero to odd h. Write
\[
A(y)=\sum_{1\le h\le y}S(h).
\]
The ordinary Friedlander–Goldston estimate is
\[
A(y)=y-\tfrac12\log y+O((\log(2y))^{2/3})\quad(y\ge1).
\]
For an odd prime q define
\[
a_q=\frac{q-1}{q-2},\quad r_q=a_q-1=\frac1{q-2},\quad
B_q(y)=\sum_{\substack{h\le y\\q\nmid h}}S(h).
\]
Then the local factors give S_{q^a}(h)=a_q S(h)1_{q∤h}. Grouping h by its q-adic valuation gives the exact recurrence
\[
A(y)-A(y/q)=B_q(y)+r_q B_q(y/q).
\]
This uses S(q^v u)=a_q S(u) for q∤u and v≥1.

Put D_q(y)=a_qB_q(y)-y. For y≥q,
\[
D_q(y)=-\frac{a_q}{2}\log q-r_qD_q(y/q)
 +O((\log(2y))^{2/3}),
\]
where the coefficient of y cancels exactly:
\[
a_q(1-1/q)-1-r_q/q=0.
\]

If y<q, then B_q(y)=A(y), so
\[
D_q(y)=-\tfrac12\log y+O((\log(2y))^{2/3}),
\]
uniformly q≥5: the additional errors y/(q−2) and log(y)/(q−2) are bounded.

For q≤y<q², substitution of this base case yields
\[
D_q(y)+\tfrac12\log q
=-\frac{r_q}{2}\log(q^2/y)+O((\log(2y))^{2/3}),
\]
and r_q log q is uniformly bounded. For y≥q² the residual
D_q(y)+½log q recurs with multiplier −r_q. When q≥5, |r_q|≤1/3, so its error is bounded by a geometric series. This independently derives
\[
D_q(y)=-\tfrac12\min(\log q,\log y)
 +O((\log(2y))^{2/3})
\]
uniformly over odd primes q≥5 from the ordinary mean A(y). It avoids applying FG95 at an auxiliary argument y/q below q.

The q=3 recurrence has |r_q|=1, so this geometric-error proof does not establish the sharp cited q=3 remainder. The weaker argument below shows that this sharp fixed-prime remainder is unnecessary for the packet theorem.

## The q=2 case has an elementary reduction

For h odd, S_{2^a}(h)=S(2h), and for h even it is zero. Since S(4k)=S(2k),
\[
\sum_{h\le y}S_{2^a}(h)=A(2y)-A(y)
=y-\tfrac12\log2+O((\log(2y))^{2/3})
\]
for y≥2. This supplies the missing even-prime modification without introducing a new prime-pair hypothesis.

## A weaker q=3 bound is enough for the packet

At q=3 the exact recurrence and the ordinary singular-series mean give, for y≥3,
\[
D_3(y)=-\log3-D_3(y/3)+O((\log(2y))^{2/3}).
\]
Iterate until the argument lies in [1,3). There are O(log(2y)) steps, the terminal value is bounded, and the sum of absolute errors is
\[
\ll\sum_{0\le j\le\log_3 y}(\log(2y/3^j))^{2/3}
\ll(\log(2y))^{5/3}.
\]
The constant terms are bounded by an alternating geometric sum (even the cruder O(log y) bound suffices). Thus
\[
D_3(y)=O((\log(2y))^{5/3}).
\tag{A1}
\]
This is weaker than the cited sharp lemma but follows from the ordinary mean and the exact recurrence alone.

For the even Schwartz kernel K in MAIN_TERM_THEOREM.md, with integral zero, integration by parts now yields
\[
\sum_{h\ne0}\mathfrak S_{3^a}(h)K(h/H)
=-\frac2H\int_0^\infty D_3(y)K'(y/H)\,dy
=O_K((\log(2+H))^{5/3}).
\tag{A2}
\]
The extension for y<1 is bounded and causes no problem. All integrals converge by Schwartz decay.

The packet only contains n=3^a≥R=T^{\beta-\eta}, so
\[
\sum_{\substack{a\ge1\\3^a\ge R}}\frac1{3^a}=O(R^{-1}).
\]
Using (A2), the logarithmic x-integral O(L), and the factor L^{-3} in the main term, all such twists contribute
\[
O\big(T^{-(\beta-\eta)}L^{-1/3}\big)=o(1)
\]
to its linearized singular-series packet. The nonlinear replacement error was already controlled uniformly in n. Replacing these terms by the formal −log3 main expression changes the result by a still smaller power-saving quantity.

Consequently the packet theorem can be based on the independently derived uniform q≥5 estimate, the elementary q=2 reduction, and this weak q=3 bound. It does not need the unexpanded sharp q=3 case of FG Lemma 2.7. This does not amount to an independent proof of that sharper fixed-prime statement.

## Implication for the packet argument

The packet n≈T^β contains prime powers; the singular series depends on their underlying prime q. In the central contributing region the shift scale H≈T^(α+β−1) exceeds n≈T^β because α>1. The uniform version is nevertheless useful when smoothing through smaller h.

The critical point is the secondary logarithmic term, not merely the leading mean y. Replacing S_n by its mean loses exactly the signed signal the packet calculation is designed to retain. The audit supports using the cited lemma with its stated prime-power scope. It does not convert the unproved localized Λ-pair estimate into a theorem.


---

# A size obstruction at the critical discrepancy scale

_Source: arithmetic/SURROGATE_SHARPNESS.md_

For the raw triple packet, a signed error of order one is compatible with positivity, the divisibility condition on the counting variable, the singular-series support condition on shifts, and a cumulative discrepancy of order \((T/n)T^\varepsilon\) on polynomially bounded shifts. The example below uses a separately assigned measure for each prime-power twist and shift. The prime problem imposes a further requirement on all these measures, since their weights must factor through one von Mangoldt sequence. This is a limitation on arguments that use only the listed hypotheses, not a counterexample for the actual primes.

## Statement

Set \(L=\log T\), \(\gamma=\alpha+\beta\), with fixed exponents satisfying \(\alpha-\eta>1,\ \beta>\eta>0,\ \gamma+\eta<2\). Take the real even packet \(q=\widehat\psi\in C_c^\infty(-\eta,\eta)\), \(c_\psi=\int\psi^3>0\), and write \(q_\nu(x)=q(\log x/L-\nu)\). Let \(s_{n,h}=\mathbf 1_{(n,h)=1}\mathfrak S(nh)\), the even nonnegative singular series. This construction applies to prime powers \(n=p^a\) in \(T^{\beta-\eta}<n<T^{\beta+\eta}\) and signed \(h\ne0\). Denote the overlap-length reference measure by
\[
dA^0_{n,h}(x)=\frac{s_{n,h}}n\mathbf1_{x>\max(0,-h)}dx.
\]
We take the real part of the residual formed with the complex packet weight
\[
W_{n,h}(x)=\frac{q_\alpha(x/n) q_\gamma(x+h)}{\sqrt{x(x+h)}}
\widehat\Phi\!\left(\frac{T}{2\pi}\log\frac{x}{x+h}\right).
\]
Here \(\Phi\in C_c^\infty(1,2)\) is real, with integral one. Define
\[
R_T[A]=\frac1{L^3}\sum_n\Lambda(n)q_\beta(n)\sum_{h\ne0}
\int W_{n,h}(x)\,d(A_{n,h}-A^0_{n,h})(x).
\]

For each fixed real \(c\), there are nonnegative counting measures \(A^*_{n,h}\), with integer weights supported on \(n\mathbb Z_{>0}\cap\{x+h>0\}\), such that
\[
\sup_y|A^*_{n,h}((0,y])-A^0_{n,h}((0,y])|
\ll_c 1+s_{n,h}\left(1+\frac{T\log p}{n}\right),\qquad
\operatorname{Re}R_T[A^*]\longrightarrow c\beta c_\psi .
\]
The measures work simultaneously for every fixed allowed \(q\) and \(\Phi\); error constants may depend on the fixed tests. The model assigns zero mass whenever \(s_{n,h}=0\). At \(c=1\) the residual cancels the singular-series main term of the raw packet at leading order. The actual primes would have to satisfy an additional estimate to exclude that value. After discretizing and flooring, the small bound is on the **cumulative** discrepancy; the total variation of an atomic measure minus a continuous reference need not be small.

## Construction and calculation

Choose an even real \(f\in C_c^\infty(\mathbb R)\) which equals one on \([1,2]\), vanishes near zero and has integral zero. For example start with an even plateau on \([1,2]\) supported on the union of \((1/2,5/2)\) with its reflection, then subtract two half-weighted translates to distant disjoint intervals. Write
\[
B(u)=\frac1{2\pi}\int f(t)e^{itu}dt,\qquad
K_\Phi(u)=\operatorname{Re}\widehat\Phi(u/(2\pi)).
\]
The function \(B\) is even, real, Schwartz, and \(B(0)=0\). In particular \(\int_0^\infty |B(u)|du/u<\infty\). Fourier inversion gives
\[
\int_\mathbb R B(u)K_\Phi(u)\,du=\int\Phi(t)f(t)dt=1.
\]

Choose fixed \(d>0\) with \(\gamma-\eta-d>1\), and \(0\le\chi\le1\) smooth, supported on \((\gamma-\eta-d,\gamma+\eta+d)\) and equal to one on \([\gamma-\eta,\gamma+\eta]\). Put \(H=x/T\). On positive overlap define the absolutely continuous measure
\[
dA_{n,h}(x)=dA^0_{n,h}(x)
\left[1+c\chi(\log x/L)\frac{\log p}{H}B(h/H)\right].
\]
The absolute size of the relative change on the support of \(\chi\) is \(O_c(L T^{-(\gamma-\eta-d-1)})=o(1)\), uniformly over these twists. The measure is positive on permitted rows for all sufficiently large \(T\). For every endpoint \(y\) the change in its cumulative weight is at most
\[
\frac{|c|s_{n,h}T\log p}{n}\int_{0}^\infty
\left|B(|h|T/x)\right|\frac{dx}{x}
\ll_c s_{n,h}\frac{T\log p}{n}.
\]

The estimate \(\sum_{1\le h\le y}s_{n,h}=y+O(1+\log(2+y))\) follows uniformly from Lemma 2.7 of Fazzari–Gerspach. Partial summation, with \(g=B K_\Phi\) even and Schwartz, gives
\[
\sum_{h\ne0}s_{n,h}g(h/H)
= H\int_\mathbb R g(u)du+O_g(1+\log(2+H))
=H+O_g(1+\log(2+H)).
\]
[Source for the singular-series estimate](https://arxiv.org/html/2412.20099v1#S2.L7)

In the linearized weight, the real phase is \(K_\Phi(h/H)\). On \(|h|\le x/2\) the pointwise error in replacing \(W\) by \(q_\alpha(x/n)q_\gamma(x)\widehat\Phi(-h/(2\pi H))/x\) is
\[
O_A\!\left(\frac{|h|}{x^2}(1+|h|/H)^{-A}\right).
\]
This follows by Taylor expansion of the logarithm and the smooth envelopes. Since \(\sum_{h\ne0}s_{n,h}|h|(1+|h|/H)^{-A}\ll H^2\), the shift-summed weight error is \(O(T^{-2})\). The perturbation multiplier is uniformly bounded here. In the comparable region the support of either envelope restricts \(x\ll T^{\gamma+\eta}\). After integration and twist summation the resulting error is \(O(T^{\gamma+\eta-2}L^{-2})=o(1)\). Outside this region the original Fourier kernel has argument of order at least \(T\), and the linearized kernel has arbitrary decay for \(|h|/H\gg T\). Polynomial support for the original packet, and partial summation for the linearized tail, give \(o(1)\).

On the linearized support \(H\ge T^{\gamma-\eta-1}\), and \(\chi=1\). Using the preceding shift average, the residual becomes
\[
\frac{c}{L^3}\sum_n\frac{\Lambda(n)\log p}{n}q_\beta(n)
\int q_\alpha(x/n)q_\gamma(x)\frac{dx}{x} +o(1).
\]
Indeed the relative kernel error from \(O(1+\log H)/H\) is uniformly small in absolute value, and the same expression with all envelopes replaced by their absolute values is \(O(1)\). Prime powers with exponent at least two contribute \(o(1)\) by their reciprocal tail. Partial summation of the prime number theorem in the variable \(v=\log p/L\) gives the limit
\[
c\iint(\beta+b)q(a)q(b)q(a+b)\,da\,db=c\beta c_\psi .
\]
The integral with the factor \(b\) vanishes by evenness.

For the integer version, write \(F(y)=A_{n,h}((0,y])\), and use the cumulative function \(F^*(y)=\lfloor F(n\lfloor y/n\rfloor)\rfloor\) on \(y\ge0\). It is increasing and \(0\le F(y)-F^*(y)\le 1+2s_{n,h}\) for large \(T\). Each atom has the required support. On a smooth dyadic block \(x\asymp X\), \(n\asymp N\), integrate by parts. The localized weight satisfies
\[
\|W\|_\infty+\|W'\|_1\ll_A X^{-1}(1+T|h|/X)^{-A}
\]
for \(|h|\le c_0X\) with a fixed small constant \(c_0\). The sum of \((1+s_{n,h})(1+T|h|/X)^{-A}\) is \(O(X/T)\). Thus the rounding changes the residual by \(O(N/(TL^3))\) per such block. Comparable shifts outside the small range have arbitrarily strong Fourier decay, as do all non-comparable contributing shifts. Their derivatives and the number of terms grow at most polynomially on packet supports. Summing the logarithmically many blocks gives \(o(1)\), since \(N\ll T^{\beta+\eta}\) and \(\beta+\eta<1\).

## Both linear forms can pass a growing small-prime sieve

The example can additionally require every occupied site \(x=nm\) to satisfy
\[
\gcd(m(nm+h),Q)=1,\qquad Q=\prod_{\ell\le z}\ell\le T^\kappa,
\qquad 0<\kappa<1-\beta-\eta .
\]
Here \(\ell\) ranges over primes. One may take \(z\) to be a sufficiently small positive constant times \(\log T\), by the prime number theorem. For \(s_{n,h}>0\), each prime permits at least one residue class for \(m\). At odd primes at most two classes are excluded. At two, positivity of \(s_{n,h}\) ensures that a class survives. By the Chinese remainder theorem and Mertens' product estimate the admissible fraction \(d=d_{n,h}(Q)\) of residues modulo \(Q\) satisfies \(d\gg (\log(2+z))^{-2}\).

On each allowed \(m\) with positive overlap put weight \(s_{n,h}/d\) times the multiplier in square brackets in the construction above, evaluated at \(x=nm\). Counting admissible residues up to an arbitrary endpoint gives \(d y+O(Q)\) for the integer argument \(m\le y\). The square-bracket multiplier has supremum and total variation \(O_c(1)\), uniformly in \(n,h\). Indeed its nonconstant derivative is bounded by \(C L T/x^2\) on \(x\ge T^{\gamma-\eta-d_0}\), where \(d_0\) is the fixed cutoff margin called \(d\) above. This uses boundedness of \(B\) and \(uB'(u)\). Partial summation on the positive overlap therefore shows that this sieve-supported cumulative measure differs from the continuous \(F(y)\) by \(O_c(s_{n,h}Q/d)\), uniformly in the endpoint. Flooring its cumulative function changes it by at most one and retains the sieve support.

Since \(Q/d\le T^{\kappa+o(1)}=o(T/n)\), the stated cumulative discrepancy bound still holds. The per-block rounding estimate becomes \(O(N Q (\log(2+z))^2/(T L^3))\), which tends to zero after summing blocks. The limiting residual is still \(c\beta c_\psi\). Each integer atom has weight at most \(1+2s_{n,h}/d\). On polynomially bounded \(n,h\) this is \((\log\log T)^{O(1)}\), since the elementary Euler product for \(s_{n,h}\) is \((\log\log(10+n|h|))^{O(1)}\). To see the last bound, split prime divisors at \(\log(10+n|h|)\), use Mertens' estimate below that point, and bound the number of larger prime divisors by \(\log(n|h|)/\log\log(10+n|h|)\).

**A larger sieve cutoff.** The period argument already gives a bound \(Q\), without dividing it by \(d\), for the discrepancy of the normalized residue count: every complete period has exactly \(dQ\) allowed sites, and the contribution and expected count of a remaining prefix both lie in \([0,Q]\) after normalization. A different elementary bound is useful for larger \(Q\). Let \(\nu_\ell\in\{1,2\}\) count the forbidden residue classes at \(\ell\) in an admissible row. Expand the product of the local indicators by inclusion–exclusion. By the Chinese remainder theorem each selected list of forbidden classes mod distinct primes gives one residue class modulo their product, whose count up to any real endpoint differs from its density times that endpoint by at most one. Thus the **unnormalized** count differs from its mean by at most \(\prod_{\ell\le z}(1+\nu_\ell)\le3^{\pi(z)}\). After normalization the cumulative error bound in the partial summation above may use \(\min\{Q,3^{\pi(z)}/d\}\) in place of \(Q/d\). In particular for every fixed \(K>0\) we may use \(z=K\log T\): then \(3^{\pi(z)}/d=T^{o(1)}\), regardless of the exponent of the resulting primorial. This extension still uses separately assigned rows, with no common prime weights.

## Scope of the obstruction

At the central scales \(n=T^{1/5}\) and \(X=T^{7/5}\) the critical factor is \(T/n=X^{4/7}\). Standard Euler-factor bounds give \(s_{n,h}\ll_\varepsilon (n|h|)^\varepsilon\) on nonzero shifts. Thus the cumulative error stays within \((T/n)T^\varepsilon\) throughout polynomially bounded packet ranges. On a packet of fixed positive width the precise comparator is \(T/n\) on each twist block. A uniform \(X^{4/7+o(1)}\) for every edge block would require a separate bandwidth analysis.

The displayed construction is a family indexed by \(T\). A single system of measures also realizes the limits along any prescribed sufficiently lacunary sequence of heights whose twist intervals are disjoint. Assign the construction at \(T_j\) to the twists in its interval and use the reference measure on remaining twists. Only assigned twists contribute at each \(T_j\). A global integer version can use the rounded reference measure on the remaining rows. This last statement controls the specified subsequence, not all intermediate heights for that same system.

The example isolates which information discarded by a magnitude estimate could matter. The same \(\Lambda\) values must determine the weights at every twist and shift for actual prime pairs. Our measures assign these weights row by row. They establish a limitation on deductions from the listed size and positivity constraints. The signed discrepancy of the actual primes remains open.

[Exact finite sieve checks](arithmetic/check_sieve_rows.py) and their [receipt](arithmetic/sieve_checks.json) test the residue densities, floor support and primitive bounds for both shift signs. They use a rational test multiplier, not actual primes or a numerical certification of the limiting residual.


---

# A concrete obstruction to inferring original zeta statistics from DBM regularization

_Source: source_refresh/DBM_BACKWARD_OBSTRUCTION.md_

6 November 2026. This is a direct application of an existing universality theorem, with an explicit clock example. It is a methodological obstruction, not a new universality theorem or an actual-zeta result.

## Source theorem and scale conventions

Landon–Sosoe–Yau, [arXiv:1609.09011v4](https://arxiv.org/abs/1609.09011v4), Definition 2.1 and Theorem 2.2, consider the real-line Gaussian-divisible ensemble \(H_t=V+\sqrt{t}W\). The Hermitian/GUE version is stated in the remark following the theorem. The initial diagonal V must have polynomially bounded norm and
\[
c\le \operatorname{Im}m_V(E+i\eta)\le C
\quad (|E|\le G,\ g\le\eta\le10).
\]
The time range is \(gN^\sigma\le t\le N^{-\sigma}G^2\). The local scaling uses the free-convolution density \(\rho_{\mathrm{fc},t}(E)\). It is not the same process as circular DBM or deterministic scalar heat.

The v4 PDF was compared directly with v3: the displayed v4 correlation statement has density prefactors, and its following remark explicitly addresses the Hermitian case. Definition 2.1 and the main time constraints agree in the compared passages. Appendix F already exists in v3. The weakened-regularity universality theorem F.1 requires \(s=N^{\omega-1}\) with \(\omega>2/3\); the local-law theorem F.2 does not require this stronger time restriction. This is not an assertion that every line of the revisions was compared.

## Proposition: even a perfectly rigid clock defeats generic backward inference

Let
\[
v_j=\frac{j-(N+1)/2}{N},\quad 1\le j\le N.
\]
Choose
\[
g=N^{-9/10},\quad G=N^{-1/10},\quad
t=N^{-4/5},\quad \sigma=1/20.
\]
These parameters satisfy the source's scale requirements for large N: one may take δ=1/20 in its auxiliary assumptions \(N^{\delta-1}\le g\le N^{-\delta},\ G\le N^{-\delta}\). In particular,
\[
gN^\sigma=N^{-17/20}\le t,\qquad
t\le N^{-\sigma}G^2=N^{-1/4}.
\]
The points are the exact midpoint quantiles for the uniform density on [-1/2,1/2]: their error from those quantiles is zero (and from the alternative j/N quantile convention it is exactly 1/(2N)). Thus they satisfy optimal microscopic rigidity.

Fix nonnegative smooth bumps h,φ of integral one, with h compactly supported and supp φ contained in (1/4,1/3). Set
\[
O(a,b)=h((a+b)/2)\phi(a-b).
\]
Let ρ_N=ρ_fc,t(0), and define the ordered, distinct two-point statistic
\[
F_{N,t}(\lambda)=\sum_{i\ne j}O(N\rho_N\lambda_i,N\rho_N\lambda_j).
\]
The subscript t in F fixes the final density scaling; this same function is used at both initial and final times. Then
\[
F_{N,t}(v)=0
\]
for all sufficiently large N, but for Hermitian DBM
\[
\lim_{N\to\infty}\mathbb E F_{N,t}(\lambda(t))
=\iint O(a,b)\left[1-\left(\frac{\sin\pi(a-b)}{\pi(a-b)}\right)^2\right]\,da\,db
\ge 1-\frac8{\pi^2}>0.
\]

### Verification of the regularity premise

The v_j are midpoints of N equal intervals. For f(v)=η/((v−E)²+η²), its total variation on the real line is 2/η. Thus
\[
\left|\frac1N\sum_j f(v_j)-\int_{-1/2}^{1/2}f(v)\,dv\right|
\le\frac{2}{N\eta}.
\]
For |E|≤G≤1/4 the integral is
\[
\arctan((1/2-E)/\eta)+\arctan((1/2+E)/\eta),
\]
between 2 arctan(1/40) and π for g≤η≤10. The error is at most 2N^(-1/10)=o(1). The required positive lower and finite upper bounds follow uniformly. Also \(\|V\|\le1/2\).

### The t-dependent density causes no loophole

By symmetry the boundary Stieltjes transform of the free convolution at zero is i b_N, with b_N bounded above and below by the source's regularity conclusions. Its fixed-point equation gives
\[
b_N=\frac1N\sum_j\frac{t b_N}{v_j^2+(t b_N)^2}
=2\arctan\frac{1}{2t b_N}+O((Nt)^{-1}).
\]
Since t→0 and Nt→∞, b_N→π, hence ρ_N=b_N/π→1. Every nonzero initial unfolded separation is therefore ρ_N times a positive integer in absolute value. It cannot enter (1/4,1/3) for large N.

### Observable normalization and positive limiting difference

If \(p_t^{(2)}\) denotes the symmetrized two-coordinate marginal density used in the paper, then
\[
\mathbb E F_{N,t}
=\frac{N-1}{N}\frac1{\rho_N^2}
\iint O(a,b)\,
p_t^{(2)}\left(\frac a{N\rho_N},\frac b{N\rho_N}\right)\,da\,db.
\]
Thus the normalization is precisely the one to which the corrected density-prefactor version of Theorem 2.2 applies. The GUE limit is the unit-intensity sine two-point function.

With u=(a+b)/2 and v=a−b the Jacobian has absolute value one. On (1/4,1/3), sin(πv)/(πv) is positive and decreasing, so its square is at most 8/π². Since both bumps integrate to one, the lower bound follows.

This proves that mesoscopic resolvent regularity, even supplemented by perfect initial rigidity, cannot imply
\[
\mathbb E F_{N,t}(\lambda(t))-F_{N,t}(v)=o(1).
\]
The theorem itself supplies the counterexample to such a proposed backward inference.

## The missing estimate in Duhamel form

For real-line Hermitian DBM, in the normalization \(d\lambda_i=N^{-1/2}dB_i+N^{-1}\sum_{j\ne i}(\lambda_i-\lambda_j)^{-1}ds\), the generator is
\[
\mathcal L_N
=\frac1{2N}\sum_i\partial_i^2+
 \frac1N\sum_{i\ne j}\frac{1}{\lambda_i-\lambda_j}\partial_i.
\]
For the smooth symmetric \(F_{N,t}\), localization of Itô's formula gives
\[
\mathbb E F_{N,t}(\lambda(t))-F_{N,t}(\lambda(0))
=\int_0^t\mathbb E[(\mathcal L_NF_{N,t})(\lambda(s))]\,ds.
\]
The pair singularities cancel on smooth symmetric functions, or one can first stop away from collisions and then pass to the limit. In the clock example this integral has a positive order-one limit.

Consequently, adding DBM to a finite window of zeta zeros could prove universality for the *regularized* window once its hypotheses are checked. Returning to the original zeros requires a separate, observable-specific smallness estimate for this integral, or a comparison principle of equivalent strength. No such estimate is established here from RH, a zero-count moment bound or a local density law. The clock rules out deducing it from generic regularity and rigidity alone. This identifies where an actual-zeta comparison would need additional, plausibly arithmetic information.

The programme's [circular DBM protected-multitime theorem](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/codex/astra-research/research/counterexamples/stochastic-protection/AGENT_STOCHASTIC_PROTECTION.md) is a separate result: it preserves agreement of low-weight expectations between two initial laws. It does not establish this backward comparison for unprotected microscopic observables. The finite scalar-heat collision results use a third flow with attractive deterministic root dynamics.


---

# Primary-source refresh: zeta, DBM and prime gaps

_Source: source_refresh/SOURCE_REFRESH.md_

6 November 2026. This is a bounded source audit, not a claim to exhaust the current literature. Read together with `DBM_BACKWARD_OBSTRUCTION.md` and `SOURCE_RECEIPT.json`. Full third-party papers and source trees remain in scratch storage; this directory contains only our analysis and compact provenance.

## What changed, and what did not

| Source | Version/date checked | Finding and review status |
|---|---|---|
| [Alpha-devbox PR 11](https://github.com/galpha-ai/Alpha-devbox/pull/11) | Head `0edc027d25b604c97588f7432ee5bac51452b912`; 49 commits; updated 6 Nov 2026, 10:40:07 UTC | Open. Latest comment at the beginning of this audit, `6682930107`, is our checkpoint, not new independent Fable review. Prior Fable comment inspected: 2 Nov, `6568092545`. No new collaborator result established. |
| [OpenAI PrimeGaps186](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330) | Main `61340d0b74163003b32756bb16e91d9209a5e330`, 2 Sep 2026 | Same checked head. Public support exists for the 186 project. Its Lean README explicitly identifies three assumed input results; this is not a fresh end-to-end formal verification by us. |
| [Sharifi prime-gaps Lean](https://github.com/romyar1/prime-gaps-lean/tree/b77bf175bdedc5123027b3fcf0abc38427975770), [author's 182 bundle](https://www.math.ucla.edu/~sharifi/AI/prime_gaps_182_expository_bundle.pdf) | Main `b77bf175bdedc5123027b3fcf0abc38427975770`, 4 Oct 2026 | Same head and identical PDF SHA-256 as prior checkpoint. No newly smaller prime-gap bound verified. |
| [Inoue, arXiv:2604.05733](https://arxiv.org/abs/2604.05733v1) | v1, 7 Apr 2026 | Unchanged checked version. RH-conditional normalized small-gap bound below 0.50895; not a critical-line proportion. |
| [Durkan–Pearce-Crump, arXiv:2610.28527](https://arxiv.org/abs/2610.28527v2) | v2, 23 Oct 2026 | Unchanged checked version. Half-spacing endpoint result; the RH positive-proportion statement is below 1/2+epsilon. It does not supply a strict below-1/2 zeta-gap theorem. |
| [Knausgård, arXiv:2610.08965](https://arxiv.org/abs/2610.08965v1) | v1, 6 Oct 2026; one author, Kristian Muri Knausgård | Newly incorporated in this audit: distinct from the earlier `2609.33043v2` paper in our scan. Landing, PDF theorem and public repository agree on the claimed stronger bounds. Computation not independently rerun. |
| [Wang, arXiv:2609.24167](https://arxiv.org/abs/2609.24167v2) | v2, 6 Oct 2026 | Withdrawn. Do not list the earlier numerical improvement as a presently established new theorem on this evidence. |
| [Arias de Reyna, arXiv:2610.24612](https://arxiv.org/abs/2610.24612v1) | v1, 17 Oct 2026 | Expository context; no new zeta local-distribution theorem was extracted from it. |
| [Landon–Sosoe–Yau, arXiv:1609.09011](https://arxiv.org/abs/1609.09011v4) | v4, 30 Sep 2026, compared with v3, 14 Jan 2019 | Checked actual regularity definition and universality theorem, not appendix titles. The usable obstruction is written out separately. Appendix F already occurs in v3. |
| [Fazzari–Gerspach, arXiv:2412.20099](https://arxiv.org/pdf/2412.20099v1#page=17) | v1, Lemma 2.7, equation (2.29) | Unconditional uniform prime-power singular-series mean supports the signed main-term argument. The localized arithmetic discrepancy remains an additional hypothesis. See the separate analytic source audit. |

## What the new Knausgård source actually claims

The exact title is *More than 83.9% of the zeros of the Riemann zeta function are distinct and more than 67.35% are simple and on the critical line.* Theorem 1.3 states

\[
\liminf_{T\to\infty}\frac{N_{0,s}(T)}{N(T)}
\ge \frac{1669159}{2478195}=0.67353820\ldots.
\]

The distinct-zero constant is `1645064/1960733 = 0.83900459675...`. These are the paper's claimed theorems; this audit does not certify the full proof.

Its architecture differs from the earlier unlabelled clipped-Gram inequality: multiplicity-labelled seven-point inequalities for distinctness, and an unlabelled eight-point inequality for simplicity on the line, combined with telescoping storage functions and a large-sieve bound on separated subsets. Proposition 5.2 requires a unit-diagonal Hermitian matrix, entrywise kernel approximation, and `U_SS <= 2 I` on every 0.85-separated subset. The critical-line constants are `x=.008722`, `b=.004389`, `C<1.3279474`, giving `(2-C-b)/(1-x)`. Proposition 7.3 bounds this particular certificate scheme: below `.67357` for index range at most seven, and below `.67383` for all pairs. These ceilings are not universal limits on zeta methods. [Paper, §§5 and 7](https://arxiv.org/pdf/2610.08965v1).

## Exactly what was checked about the computation

The [public repository](https://github.com/kristianmk/839/tree/b280d51bef5ab32b3280b0955d040085ed522d59) was pinned at `b280d51bef5ab32b3280b0955d040085ed522d59` (9 Oct 2026). Twelve selected files were downloaded; eleven files listed in its manifest matched their published hashes. The twelfth was the manifest itself.

The three added computational axioms are named:

```
Distinct839.Local.check_passes._native.native_decide.ax_1_1
Simple673.Local.check_passes._native.native_decide.ax_1_1
Line889.Local.check_passes._native.native_decide.ax_1_1
```

Each records acceptance of its branch-and-bound checker, evaluated by compiled `native_decide`. They are separate runs; the simple-critical-line theorem uses the second. Its declaration is `checkAllPar kTabArray 32 96 = true`, for root box `[13926,262143]^7`. The reported run visits 535,332,163 boxes. `axioms.txt` and the explanatory README agree on this trust boundary. [Pinned RunAll source](https://github.com/kristianmk/839/blob/b280d51bef5ab32b3280b0955d040085ed522d59/lean/Simple673/Local/RunAll.lean), [pinned Lean README](https://github.com/kristianmk/839/blob/b280d51bef5ab32b3280b0955d040085ed522d59/lean/README.md).

**Review limitation:** no complete Lean build, compiled search, table regeneration, or kernel-only replay was performed here. Matching hashes and reading a reported successful run verify provenance, not that run's correctness. The result has a public computational proof claim with an explicit compiler/runtime trust dependency; describing it as independently verified by this programme would be false.

## Consequences for AH and actual zeta: our assessment

An improvement in the proportion of simple zeros alone does not refute the Alternative Hypothesis. A simple process supported on a half-lattice can have 100% simple points while still retaining its lattice spacing obstruction. A new simplicity constant therefore does not imply sine-kernel correlations, non-lattice spacings or a strict below-half gap.

The potentially useful transfer is structural. To exploit the new certificates, one must identify a zeta-derived observable retaining the required local labels, index ordering and joint cluster geometry, prove its separated-subset matrix bound with the actual window, and show its arithmetic average contradicts every relevant half-lattice model. For the critical-line theorem the certificate is unlabelled, so multiplicity labels must not be silently imported into that conclusion. For a dynamical extension, the needed marks would additionally encode which neighbours act on the same root, and their coupling to the prime-weighted statistic.

Our older half-grid operator-norm counterexample does not automatically disprove the new certificate: the window, threshold and local assumptions changed. Conversely, the new certificate does not supply the missing prime-weighted correlation estimate. The first useful next step is to evaluate the new window and local functional on explicit AH examples and locate exactly which hypothesis, if any, excludes them.

The separate clock/DBM note makes another obstruction precise: mesoscopic regularity and even perfect initial rigidity do not control the difference between original microscopic statistics and those after adding Gaussian noise. A positive order-one Duhamel integral occurs in an explicit example. A zeta transfer needs arithmetic control of that integral, not only another local law.

## Publication scope

No famous conjecture was proved or refuted by this source refresh. The new contributions to this packet are an explicit backward-transfer obstruction, a stronger provenance audit, and an independent check of the singular-series input to a conditional signed main-term theorem. Further certificate reruns, a full novelty review, an actual-zeta discrepancy estimate, and stronger prime-gap claims are postponed.


---

# Reproduction and review receipt

_Source: REPRODUCTION.md_

6 November 2026. This packet contains mathematical derivations, internally checked finite certificates, numerical diagnostics, and source audits. They have different evidential roles.

## Exact finite law and interval checks

The fixed input is finite/candidate.json, SHA-256:

`879a342d7c9a79aed72dae2bf72bd79c1fc7ad670a8f25124429237eb5edd76c`

Its hexadecimal floats define exact dyadic rationals. The probability law is defined by an exact cyclotomic linear solve. The interval computation proves that this solve exists, stays strictly positive, preserves the stated moments, and changes survival by more than 0.0175.

Root replay environment: Python 3.12, NumPy 2.5.4, SciPy 1.18.1, python-flint 0.8.0, with one BLAS thread. Independent replay used 224-bit interval precision and a different numerical inverse call. The 160-bit verifier's numerical inverse is only a preconditioner; its validity is checked with outward-rounded intervals.

Run from this directory:


```sh
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export PYTHONDONTWRITEBYTECODE=1
python finite/certify.py
python finite/baseline.py
python finite/check_weights.py
python check_lift.py
python bounded/check.py
python arithmetic/check_normalizations.py
```


The first five commands passed in the root replay, and all six commands passed again in an isolated-copy review immediately before publication. The regenerated JSON receipts matched after excluding elapsed-time fields:

- 964 selected constraints, the independently derived dimension bound, positivity and survival shift were certified.
- All 16,159 ACUE dihedral orbits were included in the probability baseline.
- All 1,489 selected orbit-pair weights were independently checked by Fourier-projection Gram determinants.
- 2,548 direct lift identities and 1,924 pair-fibre membership cases were checked; the general statements are proved in the accompanying note.
- 1,356 deterministic supplementary checks support the bounded-probe derivations.

In `finite/certificate.json`, `exact_definition` describes the base perturbation. The reported strongest law uses that perturbation multiplied by the separately recorded `magnification` factor \(99/50\). Its positivity and survival gain are the `magnified_*` fields; no magnification of the base ACUE probabilities themselves is intended.

The last command gives floating diagnostics of a known singular-series average and the packet convolution. It is not an interval proof, a prime-pair experiment, or verification of the missing arithmetic hypothesis. Quadrature orders 128 and 256 were compared; finite-cutoff differences are retained in the receipt rather than suppressed.

For the additional artificial counting-measure example, run `python arithmetic/check_sieve_rows.py` and compare its standard output to `arithmetic/sieve_checks.json`. The standard-library checker uses exact rational arithmetic and a piecewise-linear test density. It checks 576 twist/shift/modulus rows, 71,424 integer jumps and 142,848 primitive endpoint values. These finite tests support the discretization and local sieve argument, not the limiting prime-number-theorem calculation. An independent review checked that flooring preserves the primitive bound rather than a total-variation bound and that the same surrogate works for each fixed height test, without uniformity in varying tests.

## Optional discovery reproduction

The files finite/quantify.py, finite/pivot.py and finite/export_candidate.py record how the compact seed was obtained. Running them sequentially creates floating.npz and pivots.npz and exports candidate.reconstructed.json. These are a floating search, not the proof.

The exporter was checked against the original search matrices and reconstructs the committed seed object exactly. A new LP/QR run may select different coordinates on another numerical-library build. It must undergo its own interval verification before supporting a theorem.

The original approximately 57 MiB of search matrices are retained in the local Dropbox checkpoint's discovery-data folder, with hashes. They are deliberately excluded from Git because the 89 KB seed is sufficient for the independent certificate replay. This is a size decision, not a mathematical dependency omitted from the verifier.

## Analytical review

Two independent agents derived the signed singular-series main term. The root checked Fourier signs, the two shift signs, the 1/n density factor, packet support margins, the nonlinear-kernel replacement and the PNT convolution. The result uses Fazzari-Gerspach Lemma 2.7, not the endpoint-defective full two-sign formulation of Conjecture 1.8.

A further adversarial review checked the general support conditions and corrected the low-packet wording: the matched single variable is shorter than \(T\); near-comparable products inherit that bound, while non-comparable products are handled by Fourier decay. The concrete \((1.2,0.2)\) packet was unaffected. These reviews are internal AI-assisted checks, not external peer review.

The count-moment step was checked in two ways. Rudnick-Sarnak counts multiplicities and its starred sum uses distinct indices; a separate positive-majorant and Dirichlet-polynomial argument also proves the required fixed moments under RH.

The source refresh is a provenance and hypothesis audit. The external 0.67353820 calculation, complete Lean builds and the prime-gap projects were not independently rerun here. See source_refresh/SOURCE_RECEIPT.json for exact pins and limitations.

## Rebuild the integrated Markdown and PDF


```sh
python build_handoff.py
node render_pdf.cjs
```


The renderer uses the repository's existing tools/document-renderer packages (markdown-it and KaTeX), plus Playwright. Install the existing lockfile with npm ci in tools/document-renderer if needed. DOCUMENT_NODE_MODULES can point to an installed node_modules directory; PLAYWRIGHT_MODULE can point to the Playwright module; PLAYWRIGHT_CHROMIUM_EXECUTABLE can specify an existing Chrome/Chromium binary.

PDF generation fails on KaTeX errors or detected horizontal overflow. RENDER_QA.json records these checks. Structural page checks and rendered-page inspection are recorded separately in VALIDATION.json. The integrated Markdown preserves historical stages and marks the subsequent completion explicitly.

## Scope, risks and rollback

No runtime speed or memory-efficiency improvement is claimed; these are not benchmark results. Application npm/Rust infrastructure is unchanged.

The finite results have internal ordinary proofs and interval certificates, not an external peer review or a Lean formalization. The zeta conclusion remains conditional on a precise arithmetic input. The source papers' bounds and computational claims retain their own dependencies. The phase convention is ordinary attractive scalar heat throughout the finite certificate; circular DBM and real-line Gaussian regularization are separate processes.

Reverting this research-directory addition is the rollback. A full external proof review, formalization, an actual bound on the signed prime error, a large-N perturbation of positive mass, and a new prime-gap theorem remain future work.
