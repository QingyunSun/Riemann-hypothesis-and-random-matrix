# Independent audit of the half-threshold arithmetic transfer

Date: 2026-09-05. Reviewer: the separate `yau_flow` research agent.

**Verdict:** the fixed-family arithmetic limit in `DERIVATION.md` is accepted as an ordinary mathematical argument, with the full-measure clarification and explicit limiting procedure below. I found no missing large-prime sector, extra factor of two, erroneous same-prime insertion, or unjustified extension of the Schur estimate to signed coefficients. This is independent internal review, not formal verification or external peer review. It does not certify the floating numerical optimum or prove a zero-spacing result.

I read the complete derivation, report, `large_prime_sector.py`, `finite_integer_check.py`, and the preceding `symmetric_prime_arithmetic_transfer.md`, including its explicit collision and operator-error estimates. I also checked the primary source's Theorems 3 and 4. The filename `threshold_model.py` in the review request is stale; the implementation in this checkpoint is `large_prime_sector.py`.

## 1. Precise scope of the accepted statement

Fix \(\ell\geq1\), \(a=\ell^2\), and one real polynomial
\[
H(v,S,C)=F(v,S)+C J(v,S),
\]
where only finitely many distinct-prime power sums \(S_k\), with \(k\geq2\), occur. The polynomial, its degree, its coefficients, and the threshold \(1/2\) remain fixed as \(L\to\infty\). With \(I>0\), the proposed arithmetic quotient converges to
\[
\frac{M_2+M_3}{I}-\frac14.
\]
The statement is unconditional as an assertion about weighted integer sums and the specified finite arithmetic matrices. RH enters only in its separate application to the zeta theorem. No uniformity in a growing basis, a moving threshold, \(\ell\), or optimizing coefficients depending on \(L\) has been proved. The frozen rational coefficient vector is within the accepted fixed-family scope.

## 2. Exact large-prime decomposition and mixed moments

For \(n\leq L\), two distinct prime divisors greater than \(\sqrt L\) are impossible, as is the square of such a prime. Thus
\[
C_L(n)=\mathbf1_{P^+(n)>\sqrt L}\in\{0,1\},
\]
where \(C_L(1)=0\). If this mark is one, there is exactly one decomposition \(n=pm\) with \(p>\sqrt L\), and \(m\leq L/p<p\). Consequently the coprimality in this decomposition is exact, not asymptotic:
\[
d_\ell(pm)^2=a d_\ell(m)^2,
\qquad S_k(pm)=S_k(m)+u_p^k.
\]
The identity in DERIVATION §3 therefore holds for every test function for which its finite sums are defined. No prime-density approximation is involved at this stage.

The unmarked moment for a labeled list \(I=(k_1,\ldots,k_j)\), of total weight \(K\), is
\[
m_I(a)=\frac{1}{(a)_K}
 \sum_{\pi}a^{|\pi|}\prod_{B\in\pi}\Gamma\!\left(\sum_{i\in B}k_i\right).
\]
Each block denotes one distinct prime shared by precisely those marks. The factor \(\Gamma(\sum_B k_i)\), rather than \(\Gamma(1+\sum_B k_i)\), is correct because the prime-size measure is \(du/u\). There is no factorial for ordering blocks: each labeled set partition appears once. In particular,
\[
m_{(2)}=\frac1{a+1},\quad
m_{(3)}=\frac2{(a+1)(a+2)},\quad
m_{(2,2)}=\frac{a+6}{(a+1)(a+2)(a+3)}.
\]

Disintegrating the exact large-prime identity by total size \(v\), and dividing by the unmarked density \(v^{a-1}\), gives
\[
\mathbb E_v\!\left[C\prod_{i\in I}S_{k_i}\right]
=a v^{1-a}\sum_{A\subseteq I}m_{I\setminus A}(a)
\int_{1/2}^{v}t^{\sum_{i\in A}k_i-1}
 (v-t)^{a-1+\sum_{i\notin A}k_i}\,dt
\]
for \(v>1/2\), and zero otherwise. The subset notation is over labeled positions. For example, the \(C S_2^2\) integrand has exactly the three contributions
\[
t^3(v-t)^{a-1}
 +2m_{(2)}t(v-t)^{a+1}
 +m_{(2,2)}t^{-1}(v-t)^{a+3}.
\]
The middle factor two is necessary and is retained by the implementation's bit-subset expansion. All higher powers of \(C\) reduce to the same marked moment. These formulas check for the mixed \(S_2,S_3\) features and their products appearing in both numerator and norm.

## 3. Measure convergence, discontinuities, and short backgrounds

One wording clarification is needed in DERIVATION §2: the measure whose Laplace transform tends to \(C_\ell t^{-a}\) must be
\[
\nu_L=(\log L)^{-a}\sum_{n\geq1}\frac{d_\ell(n)^2}{n}
 \delta_{\log n/\log L},
\]
with the sum over **all** positive integers. The measure truncated to \(n\leq L\) does not have that Laplace transform. The preceding transfer proof correctly uses the full measure and then restricts to compact intervals, so this is a clarification of the new note's abbreviated notation, not a failure of its argument.

The full positive measures converge locally to
\[
\nu(dv)=\frac{C_\ell}{\Gamma(a)}v^{a-1}\,dv.
\]
The Laplace bound also gives uniformly bounded mass on \([0,1]\). This supplies all total-mass control needed here. To make the new limit argument explicit:

1. Fix \(\varepsilon>0\), and restrict the finitely many ordinary marked primes and operator primes to \(p\geq L^\varepsilon\). The threshold prime already lies in \((L^{1/2},L]\).
2. Expand a fixed polynomial into finitely many labeled-prime terms. After discarding coincidences as below, each is a product of the background measure and finitely many reciprocal-prime measures on compact logarithmic intervals bounded away from zero. PNT and partial summation identify the latter as \(du/u\).
3. Take the product-measure weak limit, restricted by the relevant simplex. Its limiting measure is absolutely continuous in the continuous prime sizes and background size. The hyperplanes \(u=1/2\), \(w=1/2\), the large-prime threshold \(t=1/2\), and each total-size cutoff have zero mass. Bounded piecewise polynomial test functions are therefore legitimate.
4. Finally let \(\varepsilon\downarrow0\). For \(k\geq2\), deleting small ordinary marks changes \(S_k\) by at most \(\varepsilon^{k-1}\), uniformly for \(n\leq L\). Fixed polynomial products change by \(O_H(\varepsilon)\). The threshold mark is never deleted in this step.

This is not an appeal to pointwise uniform Selberg–Delange estimates at each prime tuple. For an explicit short-background check, after the prime cutoffs are fixed, the part with remaining background size \(v\leq\eta\) is bounded by a fixed constant depending on \(H,\ell,\varepsilon\) times \(\nu_L([0,\eta])\). For each fixed \(\eta>0\),
\[
\nu_L([0,\eta])\longrightarrow
\frac{C_\ell}{\Gamma(a+1)}\eta^a.
\]
Taking \(L\to\infty\), then \(\eta\downarrow0\), controls this portion. The background atom \(m=1\) has normalized mass \((\log L)^{-a}\to0\). The large-prime endpoint \(p\) near \(L\) causes no new atom or missing boundary term. These observations close the short-background and discontinuity obligations for this fixed family.

## 4. Coincidences and signed coefficient bounds

For \(\ell\geq1\), the decreasing ratios \((\ell+e)/(e+1)\) give
\[
d_\ell(p^{b+c})\leq d_\ell(p^b)d_\ell(p^c).
\]
In particular,
\[
\sum_{m\leq L:p\mid m}\frac{d_\ell(m)^2}{m}
\leq\frac{\ell^2}{p}\sum_{k\leq L}\frac{d_\ell(k)^2}{k}.
\]
An external reciprocal-prime factor then makes an operator/background coincidence cost \(p^{-2}\). At \(p\geq L^\varepsilon\), the sum of these costs is \(O(L^{-\varepsilon})\). Other retained prime measures have bounded mass for fixed \(\varepsilon\); using a weaker power of \(\log\log L\) bound would also suffice. There are only finitely many coincidence patterns.

The jump of \(C\) does not invalidate this estimate. A coincidence can change an amplitude discontinuously, but both amplitudes are bounded by a constant times \(d_\ell\); the contribution of the exceptional integer set still has the same vanishing upper bound. One does not need differentiability or positivity of \(H\).

## 5. Operator normalization and the two diagonal mechanisms

For the retained prime operator, put \(\alpha_p=2\sin(\pi u_p/2)\). Direct multiplication gives
\[
(Ax)_n=\frac1{\sqrt n}\sum_{p\mid n}\alpha_p r(n/p).
\]
Squaring this expression gives the stated ordered \((p,q)\) sum for \(A^*A\). Multiplying a second time gives the stated ordered sum for \(A^2\). For distinct primes coprime to the background, the coefficient factors are
\[
r(mp)r(mq)=\ell^2d(m)^2H_uH_w,
\quad r(m)r(mpq)=\ell^2d(m)^2H_0H_{uw}.
\]
The four sine factors from \(\alpha_p\alpha_q\), divided by \(2\pi^2\), give \(2\ell^2/\pi^2\). Both discrete and continuous prime pairs are ordered, so another factor of two would be an error.

For \(A^*A\), the same-prime term is exactly
\[
\sum_{mp\leq L}\frac{\alpha_p^2}{mp}r(m)^2.
\]
Its amplitude is evaluated at \(m\). Thus \(M_3\) uses \(H_0^2\), without adding the prime's mark, its power sums, or its size to \(H\). There is no extra \(\ell^2\) here. In contrast, the same-prime term in \(A^2\) contains \(p^{-2}\) and vanishes after the fixed lower prime cutoff. I independently checked this distinction directly from matrix multiplication; it is essential and correctly implemented.

The positive Schur weight \(d_\ell(n)/\sqrt n\) from the preceding proof gives the uniform operator bounds used in the new derivation. For \(A=A_0+E\),
\[
\|A^*A-A_0^*A_0\|,\ \|A^2-A_0^2\|
\leq(\|A\|+\|A_0\|)\|E\|.
\]
Thus the errors \(O_\ell(\sqrt\varepsilon+(\log L)^{-1/2})\) hold after division by \(\|x\|^2\), for every nonzero signed vector. The denominator's asymptotic follows separately from \(I>0\). No positivity or positive-semidefinite assumption on the entire numerator is being used.

## 6. Insertion sectors and implementation audit

On \(v+u+w\leq1\), at most one of the background's large prime, the inserted \(u\)-prime, and the inserted \(w\)-prime can exceed the global half threshold. Insertion must use \(\chi(u)=\mathbf1_{u>1/2}\), not a threshold relative to the new total size. The code uses the correct global threshold.

For two feature factors with inserted indicators \(d_l,d_r\), the code's marked product is the exact identity
\[
(C+d_l)(C+d_r)=C(1+d_l+d_r)+d_l d_r.
\]
The `expand` routine retains labeled multiplicities, including repeated \(S_2\) factors. The `partitions` routine may return equal-looking blocks when numerical labels repeat; their multiplicities correctly represent different partitions of the labeled positions.

For a matrix block containing at least one marked feature, the three integration domains are disjoint, up to zero-measure boundaries:

| Domain | Source of the possible mark | Treatment in the code |
|---|---|---|
| \(v>1/2\) | Background prime | Marked background moment; both inserted primes below half |
| \(u>1/2\) | First inserted prime | Background mark zero; explicit insertion indicator |
| \(w>1/2\) | Second inserted prime | Symmetric insertion sector |

The first domain contains configurations with and without a background large prime; the marked moment, rather than the condition \(v>1/2\) alone, supplies the correct weight. The code respects this distinction. \(M_3\)'s marked blocks use only the first domain because its amplitude is uninserted.

Writing \(\delta=v-1/2\) and \(t=v-\delta z\) in a marked moment extracts \(\delta^a\). The remaining integrand is smooth up to \(\delta=0\), since \(t\geq1/2\). Its background-size factor is \(z^{a-1}\), with additional integer powers of \(z\) for unassigned marks. The scaled Jacobi implementation is correct. The outer Gram factor is \((v-1/2)^a v^{a-1}\), and the marked \(M_2\) background domain has this factor times \((1-v)^2(1-x)\). In an inserted-prime domain, the Jacobian is \((1/2-v)^2(1-x)\). These are exactly the weights used by `forms()`.

The sine-kernel replacements using NumPy's normalized `sinc` also have the correct constants. Symmetrizing the final real matrix preserves its quadratic form. The finite-integer implementation uses distinct prime factors for the marks, the full divisor coefficients for prime powers, and the exact integer condition \(p^2>L\). I found no disagreement between the formulas and the inspected implementation.

## 7. Primary-source interface and the limits of the result

[Inoue, arXiv:2604.05733v1, Theorems 3 and 4](https://arxiv.org/html/2604.05733v1#S3) allow arbitrary arithmetic resonator coefficients under RH, with \(L\leq T/(\log T)^2\). Choosing the approximator equal to the logarithmic increment coefficients yields the specified two quadratic forms; at \(\phi=1/2\) the linear term cancels. The earlier Schur argument controls the remaining normalized errors and the replacement \(\log L/\log T\to1\). The new mark does not introduce a new source restriction.

This confirms the **interface**, not a favorable sign. A strictly positive limiting margin would still have to be exhibited, and a strict improvement below half would use continuity in \(\phi\) for a fixed vector. The present negative numerical trial proves neither a new zeta theorem nor a refutation of AH. A statement about zeros counted with multiplicity cannot silently become a statement about positive pair distances bounded away from zero.

## 8. What the numerical evidence does and does not establish

The reported values at quadrature orders 20, 28, and 40 are consistent with the inspected implementation and each other. I inspected the stored validation data but did **not** rerun the integrations, finite-\(L\) million-integer evaluations, or any eigenvalue optimization. No new scan was performed.

Agreement of quadrature orders is not an outward enclosure. A small pencil residual does not bound integration error. The scaled Gram condition number near \(1.2\times10^8\) must remain visible when interpreting extremely small improvements. The rational vector is genuinely fixed, but rational coefficients do not make its transcendental limiting integrals exact. Accordingly:

- Accepted: a numerically negative test of this particular 30-dimensional family, with all inputs preserved.
- Not established: a rigorous negative upper bound over the whole 30-dimensional space.
- Not established: a certified gain of \(1.429\times10^{-8}\), despite its stable floating estimate.
- Rejected as an inference: a structural impossibility theorem for larger occupation families or the full resonance-correlation method.

These are scope boundaries, not objections to the authors' present negative decision.

## 9. Independent exact checks and pinned evidence

`independent_identity_checks.py` is a separate, standard-library-only check at the single fixed cutoff \(L=120\), with \(\ell=27/25\). It uses exact integer and `Fraction` arithmetic. Rational formal prime labels and kernels replace logarithms and sines only to check their algebraic roles; this is expressly not an asymptotic or numerical-margin test. It checked all 120 integers, the 70 unique-large-prime pairs, 132 coprime ordered distinct-prime insertion triples, both exact quadratic-form expansions, the surviving uninserted diagonal, and all eight Boolean product assignments. Every assertion passed. The results are in `independent_identity_checks.json`.

Run the bounded algebra check with:

```sh
python3 independent_identity_checks.py
```

The reviewed author-file SHA-256 values are:

| File | SHA-256 |
|---|---|
| DERIVATION.md | `62970c91f2ff757eabc5d9a364d189fb7a42494c0f188713b2974003df4833b0` |
| REPORT.md | `439e08210143acf4adfae7918f8e8ca92e5ce6d66080ce8a8858cc62bbe35d06` |
| large_prime_sector.py | `255ad9a2f29e086eca01b3823bd9ece3ecbfa47b431259a6af3fee260c9afa8d` |
| finite_integer_check.py | `2126542d6b75822fb79e0910d43e4e5639be5455e079be3095c534c60a171295` |
| validate_sector.py | `72a286b477034a3f3aae63aeaba479d5de5640a1e13fe8043f37b3f918b07d26` |
| fixed_rational_vector.json | `1858e8c2ec1effa0f51e93ff28561057d1e1c5d8c9d9c08b50d099ab71e9943f` |
| validation.json | `cf8970966bcbdb9d65cde8043461466a9633c3ad74de624d2a84b1f7c2e0bc2a` |

No author file, source repository, or existing experiment output was modified. This review and its small algebra-check files are the only new outputs.
