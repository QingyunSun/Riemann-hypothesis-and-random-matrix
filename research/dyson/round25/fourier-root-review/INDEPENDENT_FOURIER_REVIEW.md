# Independent review of the actual Möbius–prime Fourier reduction

Date: 2026-09-06. Reviewer: root. Reviewed author: Aquinas. Frozen manuscript: ACTUAL_MOBIUS_FOURIER_TEST.md, 15,958 bytes, SHA256 00343ddd2edd35410bfd6b1a5cd29baa4024a0e074820881d568e0490730e0b5.

**Decision:** the complete ordinary proof is accepted in its stated scope. The finite Fourier identity is unconditional; its useful zero-core estimate and the displayed prime norm bounds use ordinary RH. No \(O(1)\) bound, sign, global shift partition, AH refutation or formal verification follows. This review independently checks the mathematics and primary statements; it does not treat scalar tests as analytic proofs.

## 1. The identity keeps the actual kernel

I read the whole frozen manuscript, including both parameter ranges and the exact sharp divisor complement. The rescaled weight has uniformly bounded mixed derivatives: the primitive integral defining \(b_T\) absorbs the apparent \(T\)-dependence, and the Pareto factor is \((1+z/(Tv))^{-T}\) on a fixed compact support.

The period-four expansion in the lower endpoint variable is exact. Smooth zero extension gives summable decay in its mode index \(j\), also after any fixed number of derivatives in the shift variable. Enforcing the original interval \(X<kd<2X\) separately is valid because the reconstructed weight vanishes at every omitted endpoint.

In the author's convention the product of phases is
\[
e(-kd\theta+jkd/(4X))\,e(n\theta)\,e(-h\theta).
\]
Integrating over a full unit period imposes precisely \(n=kd+h\), with the remaining phase reconstructing the lower endpoint Fourier mode. The auxiliary prime cutoff equals one on every contributing endpoint. Thus the coefficient, the sharp \(d>Q\) condition and every prime power are unchanged.

Since \(kd,n\) are odd and \(h\) is even, the Möbius and prime factors each change sign under a half-period shift, while the shift factor is unchanged. Their product has period \(1/2\). The prefactor is therefore \(2/(X\ell^2)\) on the unit circle and \(4/(X\ell^2)\) on \([-1/4,1/4]\). No independent half-integer major arc is counted twice.

Poisson summation gives decay away from the half-integer lattice. On the stated half-period cell, the nearest alias is zero, with the other aliases bounded by the same summable tail. The bound
\[
|W_j(\theta)|\ll_{B,J}(1+|j|)^{-B}
H(1+H|\theta|)^{-J}
\]
is valid for fixed \(B,J\). It asserts decay, not compact Fourier support.

## 2. Primary inputs and the weighted prime norm

I independently opened the author sources with the web tool:

- [Tao, Notes 8](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/), Theorem 8, states the uniform Davenport bound for the actual Möbius function with arbitrary fixed logarithmic saving and ineffective constants.
- [Bhowmik–Schlage-Puchta](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/Goldbach4.2.10.pdf), printed page 3, Lemma 3, bounds the centered prime transform under RH. Its definition is \(R=S-T\), so the coefficient is \(\Lambda(n)-1\).
- [Ng](https://www.cs.uleth.ca/~nathanng/RESEARCH/mobius2b.pdf), printed pages 5–6, records ordinary-RH bounds for the Möbius prefix and \(\Psi(x)-x\). The stronger Theorem 1 on the following discussion has an additional negative-moment hypothesis and is not used.

The odd Möbius restriction in Davenport's estimate is an exact difference of two phases. A difference of two prefixes handles the real sharp interval and \(d>Q\); each nonempty row has \(D_k\ge Q/2\), so its logarithm is comparable to \(\log X\) in both fixed-power ranges.

For the prime factor, the coefficient correction is exactly
\[
1_{n\ {\rm odd}}(\Lambda(n)-2)-(\Lambda(n)-1)
=(-1)^n-1_{n\ {\rm even}}\Lambda(n).
\]
The first term is a smooth alternating integer sum, rapidly small on the zero cell. The second is supported on powers of two; only boundedly many lie in the fixed-ratio prime cutoff. Their total is \(O(\log X)\).

Weighted partial summation can use the centered source inequality for prefix lengths between \(X/2\) and \(4X\). At the smallest frequency radius, enlarging to \(2/X\) keeps the required source parameter below every prefix length. The manuscript's bound
\[
\int_{-r}^{r}|P(\theta)|^2\,d\theta
\ll Xr\log^4X,\qquad X^{-1}\le r\le1/4,
\]
therefore has the correct range and center. Dyadic integration against \(W_j\), including the innermost interval, gives the stated weighted \(L^2\) bound and then its \(L^1\) consequence.

The cofactor sum satisfies
\[
\sum_{k<K}\log k\,D_k\ll X\log^2X.
\]
Consequently factorwise Davenport and Cauchy yield only
\[
|Z_Q^{(2)}|\ll_A\sqrt X\,\log^{-A}X.
\]
This is weaker than the inherited \(\sqrt H\log^{3/2}X\) bound. The latter's parity-centered proof does not require \(K<H\), and its fixed exponent-three Selberg input remains legal across the new height range. No stronger result is hidden in the change of Fourier representation.

## 3. Independent zero-core calculation

Under ordinary RH the odd Möbius prefix has the same square-root-plus-epsilon bound, by
\[
M_{\rm odd}(y)=\sum_{a\ge0}M(y/2^a).
\]
For a phase varying over a \(d\)-interval of length \(D_k=X/k\), its total variation costs
\[
D_k k|\theta|+O(|j|)=X|\theta|+O(|j|).
\]
This factor is essential; replacing it by \(D_k|\theta|\) would give an invalid saving.

Abel summation with both sharp endpoints gives
\[
|M_{k,j}(\theta)|
\ll_\eta D_k^{1/2+\eta}(1+X|\theta|+|j|).
\]
The actual odd prime prefix, including its bounded grid discrepancy and powers-of-two correction, similarly gives
\[
|P(\theta)|\ll\sqrt X\log^2X(1+X|\theta|).
\]

For \(|\theta|\le R/X\), multiply these bounds by \(H\), the frequency length \(O(R/X)\), the exact normalization \(4/(X\ell^2)\), and the full cofactor sum
\[
\sum_{k<K}\log k\,D_k^{1/2+\eta}
\ll_\eta X^{1/2+\eta}\sqrt K\log X.
\]
This independently reproduces
\[
|Z_{\rm core}(R)|\ll_\eta
\frac{\sqrt K}{T}X^\eta R(1+R)^2\log X.
\]
The polynomial mode cost is summable. Taking \(R\) to be any fixed power of \(\log X\) makes the core negligible, since the worst power of \(\sqrt K/T\) is \(-3707/18000\) in the old range and \(-13/90\) in the new range. This calculation controls the genuine zero core only.

## 4. Tail, resonances and the precise surviving region

The global bounds \(|P|\ll X\) and \(|M|\ll D_k\), combined with the fixed derivative order \(J=202\), yield
\[
|Z_{\rm tail}(U)|\ll XU^{1-J}.
\]
For \(U=X^{1/100}\), this is \(X^{-101/100}\). All logarithmic cofactor costs are absorbed by the original normalization. This is a paid tail bound with a fixed derivative order.

The exact remaining signed integral is therefore on
\[
(\log X)^B/X<|\theta|\le X^{1/100}/H
\]
inside the half-period cell. The author retains every Fourier mode and cofactor coefficient in that expression.

In the new range, \(K/H\) grows. Cofactor phases can resonate at \(\theta=1/k\) within the physical mean-scale band. Ordinary RH controls the Möbius factor at its integer phase, but does not turn the accompanying prime transform at \(1/k\) into a zero-frequency transform. Other rational phases also introduce character information not supplied by ordinary RH. This is a valid limitation of the proposed estimate; it is not a lower bound showing that these arcs dominate.

The all-factor square-root thought experiment still leaves a growing \(\sqrt K\) loss. It is explicitly hypothetical, and it only diagnoses this factorwise Cauchy inequality. It does not rule out cancellation across cofactor rows, a more suitable bilinear estimate, or a different jointly centered formulation.

## 5. Verification and subsequent scope

The adjacent receipt records the author/source hash checks and a separate-process replay of the nine exact rational assertions in a copied directory. The analytic conclusions rest on the arguments above and the full author proof, not on those assertions. No prime-height or frequency-grid search is part of this review.

The separately reviewed R25 joint-main theorem now identifies a fixed compact actual packet with \(Z_Q^{(2)}+o(1)\). Combining it with this Fourier theorem leaves the same unresolved annulus for that packet. Both are still fixed-window results. Extending to all physical shifts must retain the accumulated singular-series correction; no such extension or strict bound is certified by this review.
