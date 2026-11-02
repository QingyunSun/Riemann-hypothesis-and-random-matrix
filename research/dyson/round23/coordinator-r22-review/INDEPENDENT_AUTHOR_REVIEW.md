# Independent review of the complete R22 singleton-renormalization proof

Date: 2026-09-05. Reviewer: residual_gram / Astra. **The complete ordinary proof is accepted.** The singleton renormalization is unconditional by PNT; its stated quantitative rate uses RH, as does the inherited variance transfer. No strict quadratic prime-pair bound is accepted or proved.

Reviewed author: [SINGLETON_RENORMALIZATION.md](../singleton-renormalization/SINGLETON_RENORMALIZATION.md), final SHA256 `3adcc1e15799a6b9b4a6af4dfeec6854ce8185959c12b41c3cb5703297255f67`. I independently derived the two marginals before reading this complete author report; that separate frozen derivation is [INDEPENDENT_SINGLETON_DERIVATION.md](INDEPENDENT_SINGLETON_DERIVATION.md), SHA256 `33b28a289e504973bd75800099e9758869a550f5f116b29798b2b3ffa2451aea`. This review covers the complete author text, including its sharper signed tail bounds. No author file was edited.

## Exact coefficient and legitimate rearrangement

The identity in author equation (3) has the correct sign and constant. Subtracting q from the old coefficient leaves exactly (S(h)−1)(Λ(m)+Λ(m+h)−2). Both prime-power marginals remain in this identity; neither is replaced by a heuristic expectation.

The fixed-T absolute-convergence argument precedes use of any signed cancellation. With |c_h|≪h^{1/2} and the logarithmic majorants for Λ, summing the h-tail at fixed m costs at most C_T m^{3/2}log²(2m). The remaining tail is bounded by m^{3/2−T}log²(2m), hence converges for T≥4. Thus changing n=m+h and separating the two marginal sums is justified independently of the subsequent sharper estimates.

The exact weight representation (13) and its zero extension give b and b-prime bounds without an extra factor of T. Differentiating the u-integral introduces only the derivative of omega divided by ell and the derivative of 1/m. Its mass 1/(T−1) offsets the numerator T. This also proves the endpoint b(L)=0.

## Both weighted marginal estimates

The forward transform (11) is the previously proved unconditional R21 lemma for m≥T. All nonzero b(m) have m>L>T, so there is no uncovered lower range. Its O(1) remainder is multiplied by b(m)|a_m|. Chebyshev partial summation gives sum_{L<n≤2U}|a_n|/n=O(ell), making the error O(1/ell). Using the pointwise logarithmic bound here would lose the needed saving; the author correctly avoids that step.

For the backward transform, the powers of n−h cancel exactly in (24). Its second derivative (25), including the W-prime term and the factor T−2, agrees with direct differentiation. The resulting f_n is smooth on the half-line, with f_n(0)=b(n) and support ending at n−L. It can have a constant initial portion when n>U, because its primitive is then saturated; this portion is retained.

The two identities in (27) follow by integrating individual hinges and by retaining the f_n(0) endpoint. There is no need to differentiate the unknown signed staircase of c_h. The factor h makes the h f_n-prime boundary vanish at zero; the subsequent f_n boundary equals b(n), not zero.

The absolute envelope in (28) is correct. After normalization it is the Beta(2,T−2) density. With u=Tt, its mean is 2, and its density below u=1 is bounded by u. Therefore the bound E|log u|≤9/4 is uniform for all real T≥4. The additional factor T/(T−2) is at most 2. This controls the logarithmic error while allowing the true second derivative to change sign.

This is an absolute error estimate, not a relative approximation to b(n). It remains valid arbitrarily close to L, at U and at 2U, even where b(n) is tiny. The correction from h<1 is bounded separately by T²/(n³ell²) times the integrable h|log h|; since n>L>T it is within O(1/(n ell²)). Thus the backward transform (26) is valid with precisely the main coefficient claimed. Its error is summed only on the finite main range.

## Sharper infinite tails

The author's O(2^{-T}) tail bounds are stronger than the elementary polynomial(U) times 2^{-T} bound in my independent derivation, and they are valid.

For the forward tail, the already justified signed transform (11) bounds the complete inner row by O(log(2m)). Multiplication by |a_m| and the actual b-tail leaves U^{T−1}/ell² times sum_{m>2U}m^{-T}log²(2m). Its integral has the stated (2U)^{1−T} scale and denominator T−1; the U powers cancel. The sum is controlled by its first term plus the integral. Since 2U≥T and the integrand is decreasing there, the first term is absorbed uniformly. This proves (22) without claiming an absolute sum over c_h of logarithmic size.

For the backward tail n>2U, the actual second-derivative support lies in [n−U,n−L]⊂[n/2,n]. Thus A_2(h)=O(n log(2n)) on that support. In (25), integrate |W-prime|m^{T−2}+(T−2)|W|m^{T−3} over m∈[L,U]. The second integral cancels the factor T−2; the first is smaller by a bounded factor. This gives exactly
\[
\int|f_n''(h)|dh\ll_\omega T U^{T-2}/(\ell^2 n^T).
\]
The resulting C_T(n) bound in (35) has exponent n^{1−T}. Equation (37) is the exact elementary tail antiderivative, with all three logarithmic terms and positive signs correct. Multiplying by T U^{T−2}/ell² cancels the powers of U and leaves bounded T/(T−2) and comparable logarithms. The first discrete term is again controlled because 2U≥T. Hence the outer sum of |a_n C_T(n)| is O(2^{-T}).

The use of the signed triangular estimate inside each row is legitimate after the fixed-T absolute convergence has been established. Neither proof declares f_n'' positive or sums the O(1/n) approximation over an infinite interval. The saturated-primitive region m>U is automatically included by the hinge identity.

## PNT, RH and source scopes

The two finite main terms are both −M_T, including their factors of two. Thus (39) has the correct coefficient −2M_T. Abel summation uses A(y)=Ψ(y)−floor(y), with both endpoint values retained. From |g|≪1/(y ell) and |g-prime|≪1/(y²ell), the ordinary PNT modulus eta(L) bounds the integral by eta(L)log(2U/L)/ell=O(eta(L)); the endpoints are smaller. This proves unconditional o(1), rather than importing RH into a one-prime estimate unnecessarily.

Under RH, A(y)=O(√y log²(2y)) gives O(ell/√L), including the exact real endpoints. The floor correction costs at most one. These facts prove the quantitative rate in (7). They do not remove RH from R21's transfer of the actual variance.

I verified the relevant source scopes independently:

- Montgomery–Soundararajan, arXiv:math/0409258v1, printed p.4 equation (16), supplies the unconditional triangular singular-series average. The factor of two and real interpolation were already checked in the corrected R21 review and used again here.
- [DLMF 25.16.3](https://dlmf.nist.gov/25.16.E3), checked live, states the ordinary PNT formulation Ψ(y)=y+o(y). No quantitative rate is inferred from that statement.
- Schoenfeld, Theorem 10, printed p.337 equation (6.2), was read in the retained text and visually checked on its retained page image. It gives the RH bound for Ψ, including higher prime powers. Equation (6.3), with its different threshold for theta, is not substituted. The author uses only the large-y O(√y log²y) consequence; a larger constant handles any bounded initial range. The live AMS PDF fetch returned 403, so the already retained primary PDF/page was used instead.

## Verification and final scope

I read the complete author checker, then copied only that unchanged Python file and the frozen author report to a temporary directory and ran it there. All fourteen exact checks pass. The independent JSON and log are byte-identical to the author outputs, SHA256 `85c5cdc46588bde67d0e858e8325c9ae472e8f82b08b60c279a18733291233ce`. They cover the residual coefficient algebra, exact backward power cancellation and signed derivatives, beta normalization/log moments, a compact polynomial hinge identity, the exact tail antiderivative and the RH endpoint exponent. My separate derivation also has its own exact compact-weight endpoint tests; its original frozen files remain unchanged. No numerical heights, prime scans or parameter sweep were run.

All five primary-source files and both programme dependencies in the author source manifest were checked against retained bytes. The source manifest, author receipt, current author/checker, independent replay outputs, visual Schoenfeld page and this review are pinned in the separate receipt. The finite checks corroborate algebra; the ordinary arguments establish uniformity, convergence and the limiting statement.

No further amendment is requested. The exact new q keeps its singular-series-weighted linear terms; the theorem licenses replacement of the complete signed weighted remainder, not removal of each of those terms separately. The old h=1 singleton obstruction no longer transfers verbatim to this coefficient. Nothing here proves an all-shifts sub-square-root estimate for q, an even-shift upper estimate, or a strict upper bound for the full quadratic aggregate. The remaining target and its constant are unchanged.
