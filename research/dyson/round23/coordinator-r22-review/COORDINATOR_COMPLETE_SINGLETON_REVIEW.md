# Coordinator review: R22 complete singleton-renormalization author proof

Date: 2026-09-05. Status: accepted as an ordinary proof, with the target-scope clarification below. This closes the coordinator review that was pending at the R22 publication freeze. It does not retrospectively change that freeze.

Author file: SINGLETON_RENORMALIZATION.md, 13,005 bytes, SHA256 3adcc1e15799a6b9b4a6af4dfeec6854ce8185959c12b41c3cb5703297255f67.
Separate full-author review: INDEPENDENT_AUTHOR_REVIEW.md, 9,114 bytes, SHA256 1bba960d5fde26320847349934eab63dc074595ac42d07f79cf879d23c32fd72.

I read both complete texts and the complete 3,139-byte exact checker. I independently checked the algebra and estimates below. Seven retained primary-source/programme-dependency files match the author's source manifest byte count and SHA256. The author proof, reviewer proof, source manifest, author receipt and checker are frozen beside this review. I did not execute the checker again, rebuild Lean, rerun prime computations, or re-audit the entire research repository.

## 1. Accepted conclusion and assumptions

For the author's unchanged exact Pareto weight, all positive integer shifts and all prime powers retained,

\[
\mathcal E_T=\mathcal Q_T+\mathcal L_T,\qquad
\mathcal L_T=O_\omega(\ell^{-1}+\eta(L)+2^{-T})=o(1),
\]

where \(L=T^{7/4}\), \(\ell=\log T\), and
\(\eta(L)=\sup_{y\ge L}|\Psi(y)-\lfloor y\rfloor|/y\).
This conclusion uses the ordinary PNT and the unconditional triangular singular-series estimate. Under RH the stated rate
\(O_\omega(\ell^{-1}+\ell T^{-7/8}+2^{-T})\)
also follows. RH remains required for the programme's inherited transfer to the actual variance. The renormalization alone does not establish that transfer unconditionally.

The source manifest's assumptions correctly distinguish PNT, ordinary RH and the absence of a conjectural pair-error input. No GRH is being imported.

## 2. Exact identity, convergence and weight differentiation

Writing \(l=\Lambda(m)\), \(r=\Lambda(m+h)\), \(S=\mathfrak S(h)\), subtraction gives

\[
(l-1)(r-1)-(S-1)-[lr-S(l+r-1)]
=(S-1)(l+r-2).
\]

Thus both singleton coefficients and the constant have the author's signs. At each fixed real \(T\ge4\), the bound \(|S(h)-1|\ll h^{1/2}\) and logarithmic bounds on \(\Lambda\) give an inner absolute sum \(O_T(m^{3/2}\log^2(2m))\). Combined with the actual weight tail \(O_\omega(U^{T-1}m^{-T}/\ell^2)\), this is summable in \(m\). Fixed-\(T\) absolute convergence is established before either marginal is regrouped. It is not confused with a uniform asymptotic estimate.

The representation
\[
b_T(m)=\frac{T}{m\ell^2}\int_0^1
\omega((\log m+\log u)/\ell)u^{T-2}\,du
\]
gives \(b=O(1/(m\ell^2))\), \(b'=O(1/(m^2\ell^2))\). The factor \(T\) is cancelled by the integral mass \(1/(T-1)\). The smooth zero extension handles \(m=L\) without an atom. No unwanted derivative loss in \(T\) occurs.

## 3. Backward transform, signed curvature and endpoints

After \(n=m+h\), the factor \((n-h)^T\) cancels exactly. Thus
\(f_n(h)=T I_T(n-h)/(n^T\ell^2)\), and its second derivative is

\[
f_n''(h)=\frac{T}{n^T\ell^2}
\{W_T'(n-h)(n-h)^{T-2}
 +(T-2)W_T(n-h)(n-h)^{T-3}\}.
\]

The \(W_T'\) term is retained with its sign. The function may be constant initially if \(n>U\); the argument does not remove that segment. Its endpoint value is \(f_n(0)=b_T(n)\). Smooth vanishing at \(n-h=L\) licenses extension by zero.

For \(A_2(y)=\sum_{h\ge1}(y-h)_+c_h\), the exact identities are

\[
\sum_h c_hf_n(h)=\int_0^\infty A_2(h)f_n''(h)\,dh,\qquad
\int_0^\infty hf_n''(h)\,dh=b_T(n).
\]

The second formula retains the nonzero value at zero; \(hf_n'\) vanishes there, but \(f_n(0)\) does not. The first identity follows by integrating each hinge and involves no unjustified derivative of a signed staircase.

The derivative envelope is bounded by
\(C_\omega T(T-1)(1-h/n)^{T-3}/(n^3\ell^2)\).
Multiplying by \(h\,dh\) and changing to \(t=h/n\) produces a uniformly bounded multiple of the Beta(2,T−2) probability measure. Under \(u=Tt\), its mean is exactly 2; its density for \(u<1\) is at most \(u\). Therefore
\[
\mathbb E|\log u|\le \int_0^1u|\log u|\,du+\mathbb E u=9/4.
\]
The excess normalization is \(T/(T-2)\le2\), so the absolute first and logarithmic moments have the claimed \(O(1/(n\ell^2))\) size for every real \(T\ge4\).

The \(0<h<1\) segment is treated separately because \(A_2\) vanishes there. Its replacement cost is \(O(T^2/(n^3\ell^2))\), within the required bound since \(n>L\ge T\). These steps prove the author's backward approximation uniformly on \(L<n\le2U\), including near the support endpoints where the main term may be tiny. No relative-error claim is needed.

## 4. Both infinite tails really are O(2^{-T})

This is the portion not covered by the coordinator's earlier acceptance of the separate derivation's weaker polynomial-times-exponential tail bound.

For the forward tail \(m>2U\), the already justified signed Pareto transform bounds the whole inner row by \(O(\log(2m))\). Consequently the remaining bound is

\[
\frac{U^{T-1}}{\ell^2}
\sum_{m>2U}m^{-T}\log^2(2m)=O(2^{-T}).
\]

This does not claim that the row of absolute values of \(c_h\) is logarithmic. The integral has scale \((2U)^{1-T}/(T-1)\), and the powers of \(U\) cancel.

For the backward tail \(n>2U\), the support of \(f_n''\) is contained in \([n-U,n-L]\subset[n/2,n]\). Hence \(|A_2(h)|\ll n\log(2n)\) there. Integrating the actual derivative over \(m\in[L,U]\) gives

\[
\int|f_n''|\ll_\omega
\frac{T U^{T-2}}{n^T\ell^2},
\quad
|C_T(n)|\ll_\omega
\frac{T U^{T-2} n^{1-T}\log(2n)}{\ell^2}.
\]

The \((T-2)\) factor in the \(W_T\) term is cancelled by integrating \(m^{T-3}\); the \(W_T'\) term is smaller at this scale. The exact tail integral of \(y^{1-T}\log^2(2y)\) has the author's three positive logarithmic terms, denominators \(T-2,(T-2)^2,(T-2)^3\), and factor \((2U)^{2-T}\). Multiplication cancels \(U^{T-2}\); \(T/(T-2)\) remains bounded and \(\log(4U)\asymp\ell\). The result is \(O(2^{-T})\).

For both sums, monotonicity on the tail and \(2U\ge T\) control the first possible integer term by a constant times the integral. No integer-endpoint gap or extra positive power of \(U\) remains. Crucially, the finite-range \(O(1/(n\ell^2))\) error is never summed to infinity.

## 5. Finite-range summation and the PNT input

Chebyshev partial summation yields
\(\sum_{L<n\le2U}|a_n|/n=O(\ell)\).
This gives \(O(1/\ell)\) for the forward and backward transform errors. Replacing it by a pointwise \(\log n\) bound would lose this saving; the proof uses the correct aggregate bound.

Both marginal main terms equal \(-M_T\), where
\(M_T=\sum_{L<n\le2U}a_nb_T(n)\log(n/T)\).
The factor of two in their original definitions is already consumed by the \(-1/2\) transform. Thus
\(\mathcal L_T=-2M_T+O(1/\ell+2^{-T})\).

For \(g=b\log(y/T)\), \(|g|\ll1/(y\ell)\) and \(|g'|\ll1/(y^2\ell)\). Abel summation with the right-continuous function \(A(y)=\Psi(y)-\lfloor y\rfloor\), including both real endpoints, gives \(M_T=O(\eta(L))\). Under RH it gives \(O(\ell/\sqrt L)\). PNT controls only this singleton aggregate; it does not estimate the remaining two-prime term.

## 6. Primary sources and finite-check scope

I re-read the retained Montgomery–Soundararajan printed p.4 equation (16) and the retained Schoenfeld equation (6.2) context. The former's \(R_2\) is twice the triangular sum used here; interpolation gives the real-variable version with \(O(y)\) error. The latter bounds \(\Psi-x\) under RH, retaining prime powers. The PNT formulation is DLMF 25.16.3, already read live during this review programme; no fresh quantitative rate is inferred from PNT.

Five primary files and two programme dependencies were verified against the author manifest in this review. This is a byte/provenance check for the retained files, not a fresh full-paper audit.

The exact checker genuinely checks the residual identity, backward cancellation and signed derivative in three integer examples, beta moments in those examples, a compact polynomial endpoint identity, and a symbolic tail primitive. It does not establish the uniform real-\(T\) analytic estimates or convergence. Those are justified by the ordinary proof above. I read the checker but did not run it; the earlier author's and independent reviewer's runs are not presented as a coordinator execution.

## 7. Target clarification and disposition

Author equation (9), \(\liminf\mathcal Q_T\le1-\varepsilon m_0\), is a stronger sufficient benchmark inherited from an earlier target. Renormalization makes this particular benchmark equivalent for \(\mathcal E_T\) and \(\mathcal Q_T\). It is not necessary for every strict variance deficit: the current strict target is \(\liminf Q_{2,T}<A-M\), while \(\le1-M\) is stronger. The coordinator's second-reading tool packet and the owner's receipt already preserve that distinction.

Accepted: the full author singleton-renormalization theorem, the sharper exponential tails, PNT-only scope of the renormalization, RH quantitative rate, and legitimate replacement inside the complete weighted signed remainder.

Not established: a strict quadratic prime-pair estimate, a uniform short-prefix statement, removal of the new singular-series-weighted singletons individually, AH refutation, RH, or GUE. No correction to the ordinary estimates is requested. This late review should be recorded as R23-or-later evidence; keep the truthful R22 freeze record that coordinator review was pending.

