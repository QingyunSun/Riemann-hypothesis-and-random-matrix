# Independent audit of the quantitative eleven-root certificate

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
