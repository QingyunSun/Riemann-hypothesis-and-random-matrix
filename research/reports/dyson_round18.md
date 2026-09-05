# Round 18: evaluate the reflection term and audit the arithmetic normalization

Date: 2026-09-05. The main target remains an actual-zeta Dyson–Montgomery theorem. This checkpoint proves two bounded sets of identities and support lemmas, with independent ordinary-proof reviews. It does not prove the strict frequency-two deficit from Round 16, refute AH, improve the full prime discrepancy, or establish a new famous-conjecture result. Novelty relative to all literature has not been established.

## 1. What was tested

The first question was whether the positive quadratic packet from Round 17 could be evaluated through the zeta functional equation in a way that removes its unknown zero correlations. The gamma term can indeed be evaluated more explicitly. At carrier one it becomes a small positive trivial-zero correction with a negative sign. The nontrivial-zero residues still encode the entire unknown quadratic energy. Extending the resulting positive series to the carrier needed for frequency two fails an actual term test.

The second question was whether the complementary dense factorization behind the 186 prime-gap source makes the current completed conductor coefficients directly usable in a stronger well-factorable progression theorem. A constructive representation exists at a slightly enlarged level and has genuinely small total coefficient norm. The exact inverse transform, however, restores the original modulus coefficients in the progression functional. This distinguishes a useful structural lemma from an unproved arithmetic saving.

The implementation slice preserves authors, proof reviews, source receipts and one copied exact-algebra replay. Python is sufficient; no new Rust kernel, optimizer, model-calling service or PDF build is needed. Acceptance requires complete source hashes, unchanged original records, explicit assumptions and all mathematical replay fields matching. Broader numerical searches, higher-pole packet variants and new conjecture claims are postponed until a relevant inequality is available.

## 2. The functional equation with all residue terms

Assume RH and fix \(1/2<\sigma<1\), \(a=1-\sigma\), \(W\ge1\). Put
\[
H(s)=-\frac{\zeta'}{\zeta}(s),\qquad
w(t)=\frac{(t^2+a^2)^2}{W^4}
\left(\frac{\sin(t/(2W))}{t/(2W)}\right)^6.
\]
The continuous value is used at zero. With the Fourier convention of the complete author report, \(\widehat w(\lambda)=2\pi W K(W\lambda)\), where \(K=(D^2-(a/W)^2)^2B_6\) is supported on \([-3,3]\). The weight is nonnegative on the real line, but its Fourier transform is signed.

The functional equation gives
\[
H(z)=A(z)-H(1-z),\qquad
A(z)=-\log\pi+\tfrac12\psi(z/2)+\tfrac12\psi((1-z)/2).
\]
For \(2\sigma<c<2\sigma+1\), the two logarithmic derivatives in the reflected product have absolutely convergent Dirichlet series. Define
\[
C_\sigma(n)=\sum_{uv=n}\Lambda(u)\Lambda(v)v^{2\sigma-1},
\quad
P_{\sigma,W}(X)=2\pi W\sum_n C_\sigma(n)n^{-\sigma}
K\bigl(W\log(n/X)\bigr).
\]
This is an exactly finite multiplicative prime-power convolution. Let
\[
I_{\sigma,W}(X)=\int_{\mathbb R}|H(\sigma+it)|^2X^{it}w(t)\,dt,
\]
\[
R_{\sigma,W}(X)=\sum_{\rho\ {\mathrm{distinct}}}m_\rho H(2\sigma-\rho)
X^{\sigma-\rho}w\bigl(-i(\sigma-\rho)\bigr).
\]
Multiplicity appears once in this distinct-zero sum. The finite-contour identity is
\[
I_{\sigma,W}(X)=G_c(X)-P_{\sigma,W}(X)-2\pi R_{\sigma,W}(X),
\]
where
\[
G_c(X)=X^{c-\sigma}\int_{\mathbb R}
H(c+it)A(2\sigma-c-it)X^{it}w(t-i(c-\sigma))\,dt.
\]
Although \(I(X)\) is real by symmetry, positivity is used only at \(X=1\). Both unsigned split products have the same artificial pole at \(s=2\sigma\), with full residue
\[
B(X)=H(2\sigma)X^\sigma w(-i\sigma).
\]
The residues cancel in their difference; the packet does not vanish there. Omitting this residue in only one piece gives a wrong identity.

The complete derivation evaluates \(G_c\) using an explicit rational prime sum and a convergent digamma integral with both scale branches. Its combined numerator must remain intact at the lower endpoint. Local Lipschitz regularity comes from the finite spline packet, not from an unjustified derivative of a conditionally integrable time expression. See the [author proof](../dyson/round18/functional-reflection/FUNCTIONAL_REFLECTION_IDENTITY.md), [independent review](../dyson/round18/functional-reflection-review/INDEPENDENT_FUNCTIONAL_REVIEW.md), and [root review](../dyson/round18/root-review/ROOT_FUNCTIONAL_REVIEW.md).

## 3. An exact trace at carrier one, and its limitation

If \(X=1\) and \(W>3/\log2\), compact support makes the finite product and relevant linear/rational prime packets empty. The remaining gamma contribution is
\[
G_c(1)=-2\pi\mathcal T_{\sigma,W},\qquad
\mathcal T_{\sigma,W}=\sum_{k\ge1}H(2\sigma+2k)
w\bigl(-i(\sigma+2k)\bigr)>0.
\]
This series converges absolutely. Uniformly in \(1/2<\sigma<1\) and \(W\ge6\),
\[
0<\mathcal T_{\sigma,W}\ll W^{-4}.
\]
Hence the positive energy satisfies the exact trace
\[
\int_{\mathbb R}|H(\sigma+it)|^2w(t)\,dt
=-2\pi\bigl(R_{\sigma,W}(1)+\mathcal T_{\sigma,W}\bigr).
\]
The sign of the combined nontrivial residue sum follows, but a small upper bound on that sum does not. In fact, a fixed zero of multiplicity \(m\) contributes a \(-m^2/(2(\sigma-1/2))\) singularity times its limiting packet weight as \(\sigma\downarrow1/2\). The quadratic information is still present. No such fixed-zero limit is exchanged through the infinite sum or a coupled height limit.

A separate [root contour proof](../dyson/round18/root-contour-proof/ROOT_INFINITE_CONTOUR_TRACE.md), independently checked by Aquinas and the coordinator, reaches the same formula. It first takes horizontal-height limits at each fixed contour and then sends the right boundary to infinity. Its sufficient strict range is not claimed necessary.

There is a stronger obstruction at the target carrier \(X=T^2,W=T\). For fixed parameters, the proposed kth carrier-weighted trivial residue is asymptotic to
\[
\frac{(\log2)2^{-2\sigma}X^\sigma W^2e^{3\sigma/W}}
{(\sigma+2k)^2}
\left(\frac{X^2e^{6/W}}4\right)^k.
\]
When \(Xe^{3/W}>2\), these positive summands fail to approach zero. This includes every fixed \(T\ge2\) at \(X=T^2,W=T\). Thus that particular infinite-series extension actually diverges; the finite-contour formula remains valid. The ordinary fixed-\(\sigma\) bounds for the surviving prime product have no power gain at this carrier and are not uniform as \(\sigma-1/2\) shrinks.

The coordinator's [original functional review](../dyson/round18/coordinator-review/COORDINATOR_FUNCTIONAL_REVIEW.json) applies to its preserved earlier source snapshot. Its [separate delta review](../dyson/round18/coordinator-review/COORDINATOR_FUNCTIONAL_DELTA_REVIEW.json) independently checks the final divergence paragraph. The two receipts together cover the final author; neither historical source pin is silently replaced.

## 4. Dense moduli and well-factorable weights

Use the previously fixed canonical squarefree moduli with
\[
Q=X^{523/1000},\qquad Y=X^{1/1000},\qquad
X^{1/6}\le H\le X^{2/7}.
\]
The 186 source's complementary-factor guards place them in its strong triply \(Y\)-densely divisible family. For \(j=0,1\), keep the original and completed coefficients distinct:
\[
\lambda_j(q)=\mu(q)(\log q)^j1_{\mathcal Q_X}(q),
\qquad M_d^{(j)}=\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}
\frac{\mu(q)(\log q)^j}{q}.
\]
The following ordinary lemmas are unconditional properties of these coefficients and factor allocations:

1. If a triply well-factorable weight of level \(R\ge1\) is nonzero at \(n>1\), then \(R\ge nP^-(n)^2\). Allocating two factor levels just below the least prime factor proves the support restriction.
2. The actual terminal 348-prime family from Round 11 has nonzero original and completed coefficients where every weight of level at most \(Q(\log X)^B\) vanishes, for each fixed \(B\) and sufficiently large \(X\). No number or size of summands can fix that support mismatch.
3. If \(q\le Q\) is triply \(Y\)-densely divisible, its point mass is triply well-factorable at level \(QY^2\). For squarefree \(q\), each divisor's point mass inherits the constructed allocation. This does not assert that arbitrary divisors inherit the same dense-divisibility parameter.
4. The completed sequence therefore has a constructive common-level decomposition with
\[
\sum_d|M_d^{(j)}|\le(\log Q)^j(1+\log Q)^2.
\]

The necessary exponent supplied by the terminal family is \(45411/86500=.5249826589\ldots\); the sufficient exponent is \(21/40=.525\). Their difference is \(3/173000\). Both lie within the exponent range of the specific fixed-residue Maynard theorem audited here. The same-level obstruction is consequently not a blanket rejection of enlarged levels. A cheaper compressed decomposition of the original signed sequence remains open; the report's large original point-mass cost applies only to that displayed representation.

## 5. Why the small completed norm is insufficient

For a smooth genuine-prime signal supported on primes larger than \(Q\), define the correctly centered progression discrepancy
\[
\Delta_r(h)=\sum_{p\equiv h\pmod r}(\log p)f(p/X)
-\frac{1_{(h,r)=1}}{\varphi(r)}\sum_p(\log p)f(p/X).
\]
The exact Ramanujan expansion of the completed reduced-numerator functional is a sum of \(r\mu(d/r)\Delta_r(h)\) over \(r\mid d\). The primitive indicator in the principal term is indispensable. Inserting the completed coefficients gives
\[
\sum_{d:r\mid d}r\mu(d/r)M_d^{(j)}=\lambda_j(r).
\]
Thus the actual functional is exactly
\[
\mathfrak B_j=\sum_hV(h/H)\sum_r\lambda_j(r)\Delta_r(h).
\]
It is not the differently normalized sum with \(M_r^{(j)}\) in place of \(\lambda_j(r)\). The full inverse restores the original coefficients, including the modulus multiplier. No triangle-bound heuristic is needed for this conclusion.

The [complete proof](../dyson/round18/modulus-weights/MODULUS_WEIGHT_LEVEL_AND_NORMALIZATION.md), [root review](../dyson/round18/root-review/ROOT_MODULUS_REVIEW.md) and [coordinator review](../dyson/round18/coordinator-review/COORDINATOR_MODULUS_REVIEW.json) retain the source hypotheses. Maynard's specifically cited theorem fixes the residue and permits constants depending on it. The 186 absolute dense-modulus theorem already handles its admitted coherent primitive class per shift. Neither cited statement supplies the needed growing shift aggregate. The inherited full bound remains **under RH**, \(O(X^{1.023}\log^5X)\); no improvement is proved here.

## 6. Verification, preservation and the next target

Root executed the exact checker in a separate copy: 320 formal-log coefficient inversions, 2,183 primitive-principal identities and 4,366 complete genuine-prime kernel identities passed, together with exact support/exponent/norm checks. Every mathematical field agrees. The final author JSON also records the documentation-only addition of the RH qualifier; that provenance object is explicitly distinguished from fresh execution output. The unmodified historical stdout pins its earlier report hash. The [replay receipt](../dyson/round18/root-review/ROOT_MODULUS_REPLAY_RECEIPT.json) records both comparisons. These finite checks do not prove the asymptotic real-prime-family statement or an arithmetic estimate.

The [intake manifest](../dyson/round18/INTAKE_MANIFEST.json) identifies every original and its hash. Full primary paper bodies stay in the adjacent local archive; public sources and receipts retain their URLs and hashes. Existing proof files are verbatim. The 705-page public and 753-page local complete PDFs continue to describe their explicit through-Round-14 checkpoint; this report and its linked sources supply the later update.

The next useful work is an actual average correlation estimate: a strict deficit for the fixed frequency-two Bragg test, a sharp centered short-interval second moment at its exact logarithmic smoothing scale, or a source-valid signed shift-dispersion gain. Deterministic heat-flow arguments must identify an input that excludes the previously constructed half-grid models. These directions are being challenged independently. Further identities without a new inequality, large sieve-parameter sweeps, and a claim that a famous conjecture has been solved are postponed.
