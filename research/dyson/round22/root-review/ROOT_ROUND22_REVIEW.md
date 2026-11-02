# Root review and assembly of Round 22

Date: 2026-09-05. Verdict: the small-shift estimates, complete singleton renormalization, all-odd pair bound and parity-adjusted assembly are accepted as ordinary proofs at the precise scopes below. No strict actual-zeta estimate is accepted or claimed. The root authored the parity note, so its independent audit is Aquinas's separate review.

## 1. Full texts and independence

The root read the complete small-shift author manuscript, SHA256 290c1ba8e80ab64074cfe0c4ad9d2609d4930b4bf52d789ffa156f9090731a9b, and Euclid's complete independent review, SHA256 614cd44518df86e4712c6ec38d503a5f3f5706e96dd020075ca1a28648bfd975.

The root also read Plato's full independent singleton derivation, SHA256 33b28a289e504973bd75800099e9758869a550f5f116b29798b2b3ffa2451aea; Euclid's complete final author manuscript, SHA256 3adcc1e15799a6b9b4a6af4dfeec6854ce8185959c12b41c3cb5703297255f67; and Plato's complete final-source review, SHA256 1bba960d5fde26320847349934eab63dc074595ac42d07f79cf879d23c32fd72. The two derivations share the exact kernel insight discussed among the agents but were written and checked independently; they are not presented as independent external peer review.

The all-odd manuscript was read in full at SHA256 6db0484a4ad3b3fdb63284a23138063971b350d8cc39f8d96bde1c26a2166e30, including both displayed explicit constants. Its entire small checker was read and replayed by the root in a temporary copy.

Finally the root read Aquinas's complete independent parity review, SHA256 700a7e9c194f685fbcecbcbd6116bc606bd95a77cd8ed7494e4c2957b2533de4, of the root's source SHA256 36a995c9852e95d6c29e44f2c5dd5815d27318fbabe0a94770e9f21a59c3bb6b. That review accepts the two unconditional corrections and the assembly as an implication from separately reviewed dependencies. This root note supplies the final dependency assembly after the other complete proofs have been accepted.

## 2. Small shifts: exact norms and uniform sieve input

The exact integral for \(b_T\) gives \(b_T\ll1/(m\ell^2)\), \(b_T'\ll1/(m^2\ell^2)\), without a derivative factor \(T\). The increasing Pareto factor has total variation bounded by its endpoint. Consequently the Abel norm is the stated \(1/(X\ell^2)\) times the upper-endpoint kernel.

The root checked the finite singular-series average directly: the nonnegative divisor expansion and \(\lfloor K/(2d)\rfloor\le K/(2d)\) give
\[
\sum_{h\le K}\mathfrak S(h)\le
KC_2\prod_{p>2}\left(1+\frac1{p(p-2)}\right)=K.
\]
The Euler product is absolutely convergent. This is a finite upper inequality; no asymptotic in growing shifts is assumed.

For even \(h\), the sieve's local densities have one forbidden class at primes dividing \(h\), two otherwise, and stay below \(2/3\). CRT errors are bounded by \(\nu_h(d)\le\tau(d)\). The full independent source audit verifies the upper fundamental lemma with one dimension-two constant for every \(h\le X\), rather than extending a fixed-pattern theorem beyond its stated scope. The root accessed the primary Tao notes and read the detailed author and independent hypothesis verification; the independent and coordinator receipts give the full equation22/Lemma17/Corollary19 source checks. No new prime-distribution assertion is hidden in the elementary CRT remainder.

The higher-prime-power count is retained with the deliberately loose \(O(\sqrt X\log X)\) count and logarithmic weights. For odd \(h\), the power-of-two argument is uniform in the whole real block because both endpoints lie in \([X,3X]\), containing only \(O(1)\) powers of two. Exact real singleton endpoints give the floor correction, which is harmless but cannot be omitted algebraically.

The geometric sum of \(X^{-1/2}\) starts at \(L\) and introduces no extra logarithm. The leading absolute all-shift term does sum over \(O(\ell)\) blocks. This distinction gives precisely \(K/\ell+K\ell T^{-7/8}\) in the unconditional estimate and \(K T^{-7/8}\) in the RH odd signed estimate. The exact tail weight, not a local approximation of \(b_T\), gives the \(K2^{-T}\) remainder. The stated small-o ranges and subset version follow.

## 3. Complete linear correction: the signed backward derivative

The new coefficient differs from the old one by exactly
\[
(\mathfrak S(h)-1)(\Lambda(m)+\Lambda(m+h)-2).
\]
Both singleton coefficients and their factors are retained. At fixed \(T\ge4\), the polynomial singular-series majorant and the actual \(m^{-T}\) tail prove absolute convergence before the discrete indices are rearranged.

The root independently checked the main structural identity
\[
b_T(n-h)(1-h/n)^T
=\frac{T}{n^T\ell^2}\int_1^{n-h}W_T(x)x^{T-2}dx.
\]
This cancellation of powers is exact. Its second derivative contains both \(W_T'\) and \((T-2)W_T\), is supported where \(n-h\in[L,U]\), and may change sign. The primitive's constant part for \(n-h>U\) remains part of the function even though its derivatives vanish there.

Integrating the hinge kernel twice gives the exact backward singular-series transform. The endpoint identity \(\int h f_n''=f_n(0)=b_T(n)\) retains the lower boundary. The absolute envelope is Beta\((2,T-2)\), whose variable \(u=Th/n\) has mean two and density at most \(u\) below one. Hence its absolute logarithmic moment is at most \(1/4+2\), with an additional normalization factor \(T/(T-2)\le2\). This controls the error without dividing by a small value of the bump or treating a signed derivative as positive.

The same bound works arbitrarily close to each support endpoint. The extension of the triangular main term below \(h=1\) costs at most \(T^2/(n^3\ell^2)\) times an integrable logarithmic moment; \(n>L>T\) makes it small enough. The result is the uniform backward main term \(-b_T(n)\log(n/T)/2\), with error \(O(1/(n\ell^2))\) on the finite main range.

Chebyshev partial summation gives \(\sum |a_n|/n=O(\ell)\), making both marginal error sums \(O(1/\ell)\). A pointwise logarithmic bound would be too weak here. The two marginals, including their outer factor two, have total smooth main \(-2\sum b_T(n)a_n\log(n/T)\). Partial summation with \(\Psi-\lfloor\cdot\rfloor\) gives \(O(\eta(L))\) from ordinary PNT and \(O(\ell/\sqrt L)\) under RH.

The root checked the sharper tail proof in the main author separately from Plato's looser independent tail. For the forward tail, the already justified signed inner transform is only logarithmic; the powers of \(U\) cancel in the exact integral. For the backward tail, \(f_n''\) is supported at \(h\asymp n\), and \(\int|f_n''|\ll T U^{T-2}/(\ell^2 n^T)\). Multiplying by the triangular estimate \(O(n\log n)\), then summing the outer prime-error majorant, leaves the exact \(n^{1-T}\log^2n\) tail. Its antiderivative cancels \(U^{T-2}\), with \(T/(T-2)\) uniformly bounded. The first integer terms are controlled by the integral because \(2U\ge T\). Thus the author's pure \(O(2^{-T})\) tails are valid.

The ordinary PNT statement was checked live at DLMF25.16.E3. The separate retained Schoenfeld primary/source-page review supplies the RH quantitative consequence for \(\Psi\), with prime powers included. The live AMS403 is not a missing mathematical input: the retained exact primary PDF was independently read. This root pass does not claim another page rendering.

The full linear correction is therefore \(o(1)\) unconditionally. The RH assumption in the inherited variance transfer remains unchanged.

## 4. All odd pairs: independent constant and tail check

At odd shift exactly one endpoint is even, so every nonzero product has a power of two with weight \(\log2\). The exact split into lower and upper power endpoints keeps the original ordered-pair factor two.

For the lower endpoint in \((L,2U]\), monotonicity of \((r/x)^T\log x\) on \([r,\infty)\) gives the displayed tail integral beginning at the integer \(r\). For the upper endpoint, the increasing power sum is at most \(r^T/T\). The root checked the power count \(N\le3\ell/(2\log2)\) and \(\log r\le11\ell/4\). The combined rational main bound is
\[
\frac{33}{4}\left(\frac{16}{9}+\frac43\right)+\frac{16}{9}
=\frac{247}{9}<32.
\]

The explicit Chebyshev constant \(4\log2\) follows from binomial valuations at dyadic integers and monotonicity. The strict endpoint in its Stieltjes use contributes \(-\Psi(r)\), correctly discarded only in an upper bound. In the upper-endpoint tail, the displayed Fubini equality applies to the enlarged all-integer nonnegative sum, not to an odd sum whose parity was silently erased.

For the first power \(r_0>2U\), the geometric factor is at most \((16/7)2^{-T}\). The two tail constants sum to
\[
8\left(\frac{16}{9}+\frac43\right)\frac{16}{7}
=\frac{512}{9}<64,
\]
using \((\log2)^2<1\). Both infinite tails are included. This proves the complete explicit bound for every real \(T\ge4\), unconditionally.

The copied scalar replay passes all seven assertions and its complete JSON/stdout are byte-identical, SHA256 bd6a9629c9e495c33456b61eb7f96b3df08584c82a8d9b86cb497e33da966343. The checker corroborates algebra and constants; this ordinary review checks convergence, support, prime powers and inequalities. No prime-height data was generated.

## 5. Parity adjustment and final logical order

The root's parity proof has the independent full audit noted in Section1. I read that review completely. It verifies the sign \(q_2-q=-\mathfrak S(h)(-1)^m\); the alternating partial-sum norm; full shift summation from \(\sum_{h\le y}\mathfrak S(h)\le y\); the distinction between the all-integer \(m>2U\) tail, which retains a factor \(U\), and sparse power-of-two tails, which do not; and the compact-kernel integral \(r/T\).

The new local baseline is zero at even \(m\), even \(h\). All its remaining nonzero singleton endpoints are powers of two. Their lower and upper row bounds are \(O(1/(T\ell^2))\) per power in the window, plus the separately controlled geometric tails. The old baseline one would not allow those rows to be discarded. This is why the transformation must precede endpoint restriction.

All dependencies of the conditional assembly are now separately reviewed. Its legitimate sequence is: globally replace the old residual by the full singular-series-centered \(q\)-sum; make the controlled parity-baseline change; remove odd shifts using the complete odd-pair lemma; remove even endpoints using the absolute power-of-two row bound. The surviving expression has odd \(m\), even \(h\ge2\), and singleton constant two. Combining with the inherited RH transfer yields exactly the reported actual-variance representation.

This does not delete the original residual's entire odd portion independently, does not prove any new uniform pointwise error bound, and does not give a sign or strict upper constant for the remaining even-shift quadratic expression. Those distinctions belong in the current ledger and integrated report.

## 6. Acceptance and what remains

The complete Round22 assembly is accepted as an ordinary reduction under RH, with its component unconditional/PNT/RH assumptions separated as above. It legally removes the specific linear obstruction discovered in Round21. It does not prove the sufficient strict bound, AH failure, Montgomery pair correlation, or the sine-kernel limit.

All proof sources and independent reviews remain unchanged. Existing separate checker replays and source hashes are pinned in their own receipts; publication need not rerun them. No numerical scan, large PDF build, external model session, formal proof kernel or novelty certification is part of this review. The next actual mathematical obligation is a strict estimate for the remaining signed quadratic prime term.
