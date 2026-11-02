# Round 23: actual shift completion, local centering and a growing arithmetic residual

Date: 2026-09-05. Status: three ordinary mathematical results with complete independent reviews. They reorganize the actual prime-pair/heat target but do not establish its strict upper bound. No proof of RH, Montgomery's full pair-correlation conjecture, GUE, an AH refutation, a zeta-gap improvement or a prime gap below 186 is claimed.

This checkpoint continues the user's priority: a theorem about actual Riemann zeros and their random-matrix statistics. Every result below uses the actual von Mangoldt sequence or a rigorously compared arithmetic residual. The earlier finite ACUE heat theorems remain separate. The 705-page public and 753-page local PDFs retain their explicit Round 14 scope; this report extends their research history without relabeling those files.

## 1. The precise unsolved target

Retain the fixed nonnegative smooth window and exact kernel
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},\quad
W_T(x)=\omega(\log x/\ell),
\]
\[
b_T(m)=\frac{T}{m^T\ell^2}\int_1^mW_T(x)x^{T-2}\,dx,
\qquad K_T(m,n)=b_T(m)(m/n)^T.
\]
On odd \(m<n\), the reviewed R22 coefficient is
\[
q_2(m,n)=\Lambda(m)\Lambda(n)
-\mathfrak S(n-m)[\Lambda(m)+\Lambda(n)-2].
\]
Put
\[
Q_{2,T}=2\sum_{\substack{m<n\\m,n\ {\rm odd}}}K_T(m,n)q_2(m,n).
\]
The prior RH theorem gives
\[
\overline V_T=M+Q_{2,T}+o(1),\qquad
M\approx0.1851531432653023.
\]
The fixed AH-Pairs hypothesis forces the saturation value
\[
A\approx1.0105877964142522.
\]
Thus the new arithmetic input sought is
\[
\boxed{\liminf_{T\to\infty}Q_{2,T}<A-M.}
\tag{1}
\]
The stronger benchmark \(\liminf Q_{2,T}\le1-M\) would give a deficit of at least \(A-1\approx0.0105877964\). It is a sufficient benchmark, not a necessary condition for excluding AH. Neither bound is proved here. The prior positive-deficit equivalence retains RH and its exact fixed-window assumptions.

The earlier impossible all-shifts sub-square-root prefix hypothesis remains rejected. New centering does not retroactively validate it.

## 2. Completing an actual upper-window prime component

Read the complete [author proof](../dyson/round23/even-pair-dispersion/UPPER_WING_SHIFT_COMPLETION.md) and [Plato's independent review](../dyson/round23/even-pair-dispersion-review/INDEPENDENT_UPPER_WING_REVIEW.md).

Use fixed smooth compact cutoffs \(\chi,V\), supported in \((1,2)\), and set
\[
X=T^\alpha,\quad H=X/T,\quad Q=X^{523/1000},
\qquad 11/5\le\alpha\le9/4.
\]
The weight is the actual kernel with these cutoffs:
\[
F_T(m,h)=b_T(m)\chi(m/X)V(h/H)(m/(m+h))^T.
\]
The selected divisor family is the entire odd part of the fixed R11 canonical complementary family, with each distinct squarefree modulus counted once. Its coefficient is the true \(\mu(d)\), with the exact logarithmic cofactor. The 186 source's owner conditions imply both \(d\le Q\) and
\[
P^+(d)\le X^{501/5000}.
\tag{2}
\]
This statement is about that full owner family. It is not a property of every modulus below \(Q\).

Opening the exact identity
\[
\Lambda(m)=\sum_{d\mid m}\mu(d)\log(m/d)
\]
and switching \(n=m+h\) yields the five-term identity
\[
\mathcal P_{T,X}^{\chi,V}
=\mathcal B_{\mathcal D}+\mathcal A_{\mathcal D}
+\mathcal N_{\mathcal D}+\mathcal C_{\mathcal D}
-\mathcal M_{\mathfrak S}.
\tag{3}
\]
Here \(\mathcal B\) is the primitive centered progression component; \(\mathcal A\) is its exact principal; \(\mathcal N\) is the nonprimitive part; \(\mathcal C\) retains every complementary divisor; and \(\mathcal M_{\mathfrak S}\) retains both original prime marginals, their singular-series weights and the constant two. All five sums and all masks are specified in the author proof. The principal has \(1/\varphi(d)\), not \(1/d\).

The genuinely useful cancellation is in the physical shift before absolute values are taken over primes or moduli. For odd \(d\) and unit \(n\), write \(h=2r\), \(a=2^{-1}n\bmod d\). The primitive kernel is
\[
1_{r\equiv a\pmod d}-1_{(r,d)=1}/\varphi(d),
\]
with exact mean zero. Poisson summation gives the frequency prefactor \(1/(2d)\), and the zero frequency vanishes. The true weight satisfies, for every fixed \(j\),
\[
|\partial_h^j(F_T(n-h,h)\log((n-h)/d))|
\ll_j\frac{\log X}{X\ell^2}H^{-j}.
\tag{4}
\]
This uses the exact primitive representation of \(b_T\); differentiating it does not cost \(T^j\). The Pareto factor is not replaced by an exponential.

Completion and the elementary Chebyshev bound then prove
\[
|\mathcal B_{\mathcal D}|
\ll_J\frac Q{\log X}(Q/H)^J.
\]
Since \(H\ge X^{6/11}\), choosing the fixed order \(J=24\) gives
\[
\boxed{|\mathcal B_{\mathcal D}|
\ll X^{-7/440}/\log X.}
\tag{5}
\]
For the nonprimitive term, a nonzero summand has \(n=p^j\) and \(p\mid d\). The owner guard (2), the divisor bound \(\tau(m)\ll_\eta m^\eta\), and the original logarithmic weights yield
\[
\boxed{|\mathcal N_{\mathcal D}|
\ll X^{-15041/45000}.}
\tag{6}
\]
This is a bound on actual prime powers, not a prime-only replacement.

Consequently the packet has the reviewed reduction
\[
\mathcal P_{T,X}^{\chi,V}
=\mathcal A_{\mathcal D}+\mathcal C_{\mathcal D}
-\mathcal M_{\mathfrak S}+o(1).
\tag{7}
\]
The entire remaining signed expression is unbounded by this proof.

The 186 theorem can also be applied legally per fixed shift: the true modulus is \(2d\), the residues are coherent, the primitive mask is retained, and a fixed positive exponent retreat pays the factor two. After summing shifts, that application gives only \(H\log^{-B}X\) for arbitrary fixed \(B\), which is insufficient. The saving in (5) comes from classical shift completion, not a new distribution exponent in the source.

This packet lies away from \(h=0\) and requires \(H>Q\). It does not cover the full height window or a sharp half-line endpoint. Bounded combinations of \(O(\log T)\) packets preserve the negligible removed error when their relevant smooth seminorms are uniformly bounded; no full partition is asserted.

## 3. A legal fixed-modulus-six normalization

Read the complete [author proof](../dyson/round23/mod3-centering/FIXED_MOD6_CENTERING.md) and [root's independent proof review](../dyson/round23/mod6-root-review/INDEPENDENT_MOD6_REVIEW.md).

Let
\[
A_6(m,h)=1_{(m(m+h),6)=1},\qquad
\nu_6(h)=\#\{a\bmod6:(a(a+h),6)=1\}.
\]
For even shifts \(\nu_6=2\) on \(h\equiv0\pmod6\) and \(1\) on \(h\equiv2,4\pmod6\). Set \(r_6=6A_6/\nu_6\); for odd shifts set \(r_6=0\). Define
\[
q_6(m,h)=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)r_6(m,h)
\left[\frac{\Lambda(m)+\Lambda(m+h)}3-1\right].
\tag{8}
\]
For comparison on the full domain, extend \(q_2\) with baseline \(2\,1_{m\ {\rm odd}}\), as in R22.

The full signed change of normalization is unconditionally negligible:
\[
2\sum_{m,h\ge1}b_T(m)(1+h/m)^{-T}(q_6-q_2)
=O_\omega\left(\eta_6(L)+\frac1{T\ell}+2^{-T}\right)=o(1),
\tag{9}
\]
where \(\eta_6(L)=\sup_{x\ge L}|\sum_{n\le x}\Lambda(n)\chi_6(n)|/x\to0\) by PNT in the two fixed reduced classes modulo six. No GRH or growing-modulus uniformity is assumed.

The central arithmetic point is the signed singular-series progression difference
\[
d_h=\mathfrak S(h)(1_{h\equiv2\pmod6}-1_{h\equiv4\pmod6}).
\]
Its prefix satisfies
\[
\sum_{h\le Y}d_h=O(\log(2+Y)).
\tag{10}
\]
This follows directly from the positive divisor expansion of the singular series and the bounded prefixes of the nonprincipal character modulo three. It supplies smooth forward and backward coefficient bounds before PNT in AP is applied. In the backward derivative, the factor is \(Th/n-2\); splitting the two original derivative terms first would lose the required uniformity.

Forbidden residue classes with one prime endpoint are retained in the character sum. Only terms supported on powers of 2 or 3 are charged as exceptions. The separate estimate
\[
2\sum_{A_6(m,h)=0}b_T(m)(1+h/m)^{-T}|q_6(m,h)|
=O_\omega(T^{-1}+2^{-T}/\ell^2)
\tag{11}
\]
then permits removal of the remaining forbidden product rows. The proof includes both infinite endpoint tails. The periodic baseline tail retains its polynomial factor \(U\) before it is absorbed into the stated vanishing bound.

On the admissible rows the two formulas are
\[
q_6=\begin{cases}
\Lambda(m)\Lambda(m+h)-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-3],
&h\equiv0\pmod6,\\
\Lambda(m)\Lambda(m+h)-2\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-3],
&h\equiv2,4\pmod6.
\end{cases}
\tag{12}
\]
The factor two in the second line is essential. These formulas give another exact asymptotic target under the inherited RH transfer. They do not lower its value.

## 4. A growing wheel in the actual variance and heat energy

Read the complete [author proof](../dyson/round23/growing-wheel-centering/GROWING_WHEEL_CENTERING.md) and [Euclid's independent review](../dyson/round23/growing-wheel-review/INDEPENDENT_GROWING_WHEEL_REVIEW.md).

This result is distinct from the fixed-modulus-six pair normalization. It compares actual interval norms directly and does not infer a growing-modulus pair theorem from fixed-AP PNT.

Let \(\mathcal W\) be any finite squarefree wheel, possibly depending on \(T\), and put
\[
\kappa=\omega(\mathcal W),\quad R=\mathcal W/\varphi(\mathcal W),
\quad D=R2^\kappa,\qquad
r_{\mathcal W}(n)=[\Lambda(n)-R]1_{(n,\mathcal W)=1}.
\]
Here \(\omega(\mathcal W)\) denotes the number of distinct prime factors, not the fixed window function. The author uses separate notation to keep those roles explicit.

For the original positive product measure
\[
d\mu_T=\frac{T}{\ell^2}e^{-\lambda}W_T(x)x^{-2}\,dx\,d\lambda,
\qquad
\mathfrak m_T=\mu_T(\mathbb R^2)\le\frac{\|\omega\|_\infty T}{L\ell^2},
\]
inclusion-exclusion gives the global endpoint discrepancy
\[
\left|\sum_{n\le x}R1_{(n,\mathcal W)=1}-x\right|\le D.
\]
Thus replacement of the continuum center has norm debt at most \(2D\sqrt{\mathfrak m_T}\), uniformly over every positive length \(\lambda\).

All removed powers whose bases divide the wheel have a separate debt
\[
\kappa\left(\frac94\ell+\frac{\sqrt2}{T}\right)\sqrt{\mathfrak m_T}.
\tag{13}
\]
This follows from their actual cumulative staircase, bounded by \(\kappa\log x\), and the second moment of the exponential length law. It includes the first powers and arbitrarily large endpoints.

Reverse triangle inequalities prove the unconditional finite-height comparison of square roots of variances. Under RH, the prior boundedness of the original variance converts it to
\[
\boxed{\overline V_T^{\rm rough}=\overline V_T+o(1)
\quad\text{if}\quad D=o(T^{3/8}\log T).}
\tag{14}
\]
The same condition forces \(\kappa=O(\log T)\), so (13) tends to zero without a second growth hypothesis. There is no assumption \(\mathcal W\le T^C\).

A concrete growing family is
\[
\mathcal W=\prod_{p\le z}p,\qquad
z=c\log T\log\log T,\qquad 0<c<\frac3{8\log2}.
\tag{15}
\]
Ordinary PNT gives \(\kappa=(c+o(1))\log T\); the elementary bound \(R\le\lfloor z\rfloor\) for eventual \(z\ge2\) suffices. Mertens' theorem is not needed. This is a sufficient cutoff range; failure of the displayed budget beyond it does not prove failure of the variance comparison.

The actual cumulative residual defines
\[
g_{T,\mathcal W}(v)=\sqrt{\omega(v/\ell)}e^{-v/2}
\sum_{n\le e^v}r_{\mathcal W}(n).
\]
It differs from the original R21 log-prime profile in \(L^2\) by at most
\[
\sqrt{\|\omega\|_\infty/L}\,[D+\kappa(7\ell/4+\sqrt2)].
\]
The unchanged R21 Fourier multiplier is nonnegative and at most \(7/3\) for \(T\ge4\). Consequently the exact actual heat energy also transfers with an explicit error, uniformly in the allowed wheel. Its semigroup acts in the logarithmic integer coordinate. It is neither Dyson Brownian motion nor de Bruijn–Newman motion of the zeta zeros.

Removing support changes the surviving coefficient to \(\Lambda(n)-R\). Squared energy is not monotone under this operation. AH saturation transfers unchanged; a strict rough-residual energy bound remains a new arithmetic obligation.

## 5. The second reading of 186 and FLT: selected tools and missing objects

The coordinator supplied a complete [second-reading memorandum](../dyson/round23/coordinator-intake/ASTRA_186_FLT_SECOND_READING_TOOLS.md), preserved unchanged with its receipt. Root read the entire 17,120-byte memorandum. The memo separates primary-source results, directly derived general lemmas and applications still missing here.

The actual complementary-modulus construction is used in Section 2 with full gcd, tail, parity and coefficient accounting. The gain is quantified, and the unestimated terms remain explicit. This satisfies an actual source-to-expression mapping rather than relying solely on an exponent comparison.

The memo also supplies an exact finite zero-margin perturbation: if \(Z(m,n)\) has zero row and column sums on odd endpoints, then \(\delta K=Z/\mathfrak S(n-m)\) removes all singleton and constant terms of \(q_2\). This is an auxiliary signed kernel. It still needs an admissible realization, a comparison to the original target and a signed double-prime estimate.

The two-mark positive-measure algebra from the 186 numerical certificate is reserved for a genuine exceptional-factor expansion with correct overlap multiplicities. No independent-Poisson model is substituted for unknown prime-pair correlations.

FLT's generic pointwise-to-dimension theorem and the memo's approximate-fixed-point Hilbert–Schmidt bound are potentially useful tools. The present cutoff heat operator has only an \(O(T\log T)\) dimension budget at heat time \(T^{-2}\). A single profile's energy estimate supplies neither a large independent arithmetic family nor a uniform bound over that family. Those missing objects are required before starting a formalization project. The FLT material concerns formalizing an existing theorem; neither its Lean build nor the entire 186 certificate was rerun here.

The next bounded work tests an additional divisibility restriction on nonprimitive shifts, the exact small-cofactor complement after opening all small odd divisors, and realization of zero-margin directions in the actual kernel family. These are active R24 investigations, not additional accepted claims in this checkpoint.

## 6. Review, preservation and reproducibility

All three full author proofs have full independent ordinary-mathematics reviews: Plato reviewed Euclid's completion; root reviewed Plato's fixed-six normalization; Euclid reviewed Aquinas's growing wheel. Root also read the entire other two manuscripts and their final independent reviews before assembling this report. Author submission headers remain unchanged; final acceptance is recorded beside them rather than rewritten into the historical source.

The fixed-six copied checker replays its entire JSON and stdout byte for byte, including all metadata: 36 residue cases, 8 bounded divisor-prefix cases and 3 derivative/moment cases. The completion checker has five exact groups, including 7,700 primitive-mask identities, 79 even-grid periods, 146 cyclotomic Fourier coefficients and 12 formal-log divisor identities. The growing-wheel checker contains eight exact scalar identities and enumerates no prime heights or wheels. These checks verify their stated finite algebra, not asymptotic prime distribution.

The [intake manifest](../dyson/round23/INTAKE_MANIFEST.json), [source link map](../dyson/round23/SOURCE_LINK_MAP.md) and [integration receipt](../logs/round23-integration/INTEGRATION_RECEIPT.json) record source bytes, local-only primary bodies, checked dependencies and full output comparisons. Ordinary proof review, exact finite algebra, syntax checks, external peer review and formal verification are different statuses; the last two have not occurred.

All 55 originals, totaling 646,019 bytes, are retained in the local Round 23 archive. There are 53 public originals, totaling 366,277 bytes; two complete primary HTML pages remain local with hashes. The integration checks 238 declared dependency records and three complete JSON/stdout replay pairs. Five exact-byte path substitutions are explicitly recorded: two historical R22 output files and three copied-replay input references. They do not omit any output fields.

The coordinator's late [complete R22 singleton review](../dyson/round23/coordinator-r22-review/COORDINATOR_COMPLETE_SINGLETON_REVIEW.md) now closes the coordinator review that was pending at the R22 freeze. It accepts the stronger exponential tails after full proof/source reading, but does not claim another checker execution. The [independent R22 publication verification](../dyson/round23/coordinator-intake/COORDINATOR_R22_PUBLICATION_VERIFICATION.json) separately checks that checkpoint's 55 public originals and 58 local originals. Both are new R23 evidence; the truthful earlier pending record is unchanged.

All 1,375 mathematical expressions and 70 editorial links pass presentation/path checks. Six original EOF blank lines are retained through exact-file attributes rather than edited away. No new prime-height computation, large scan, paid model call, Fable session or PDF rebuild is part of this integration. The ongoing research goal is the strict actual-zeta inequality (1).

## 7. Risks, rollback and postponed work

The principal risk is dropping a signed marginal, nonprimitive mask, sparse-power tail or a uniformity condition when combining otherwise correct reductions. Physical completion requires a smooth shift packet and sufficient room beyond the modulus; it does not treat the full endpoint by fiat. The fixed-six proof cannot be extrapolated to varying progressions, and the growing-wheel norm theorem cannot be read as a strict energy improvement.

This is one research checkpoint. Reverting its commit restores the previous public state; prior and local original files remain preserved. Postpone another complete PDF compilation, larger prime sweeps, arbitrary unconstrained kernel optimization, and formalization without a concrete checked theorem dependency. The next useful step is to estimate the actual surviving signed correlation, or to eliminate a proposed mechanism with an exact counterargument.
