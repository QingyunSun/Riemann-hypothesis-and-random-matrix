# Coordinator ordinary review of the fixed-modulus-six normalization

Date: 2026-09-05. Verdict: accepted, with the sufficient-target interpretation stated below.

The complete author source FIXED_MOD6_CENTERING.md (17,011 bytes, SHA256 ec3c4a258cf1ef2614e0255ee44c7c3a7e04268fe1655f082815f8012133285e) and the complete owner's independent review (9,883 bytes, SHA256 9e6850f2da9558c9ae068c49e57fbe8b51d931fe96bc72c4044f38a44421b242) were read. I independently checked the following ordinary arguments. Seven primary/programme source pins match the retained bytes. I opened and read the fixed-AP PNT paragraph of [DLMF 27.11](https://dlmf.nist.gov/27.11) live. I did not execute or separately review the finite checker, rebuild Lean, run prime samples, inspect a growing-wheel proof, or verify publication of R23.

## Accepted estimates and source scope

With the author's exact kernels and full coefficients,

\[
2\sum_{m,h\ge1}b(m)k(m,h)(q_6-q_2)
=O_\omega\left(\eta_6(L)+(T\ell)^{-1}+2^{-T}\right)=o(1)
\]

and

\[
2\sum_{A_6(m,h)=0}b(m)k(m,h)|q_6(m,h)|
=O_\omega\left(T^{-1}+2^{-T}/\ell^2\right)=o(1).
\]

These statements are unconditional for fixed modulus 6. The actual-variance assembly inherits RH from the earlier programme. The fixed-character PNT is not a GRH assertion or a statement uniform in growing moduli.

## Local algebra and the non-exceptional forbidden rows

For even h, \(r_6=6A_6/\nu_6\) equals 3 on allowed rows for \(h=0\bmod6\), and 6 on the single allowed row for \(h=2,4\bmod6\). It vanishes on forbidden rows. On odd shifts, both S and d vanish and the no-division convention is consistent.

I checked the residue identities by splitting even endpoints, odd endpoints divisible by 3, and the two reduced classes. In particular:

- \(m=1,h=2\bmod6\): the first endpoint may be genuinely prime, and its coefficient is \(+S(h)\).
- \(m=5,h=2\bmod6\): both endpoints are admissible, and its singleton coefficient in the difference is \(-S(h)\).
- The \(h=4\bmod6\) signs reverse.
- \(h=0\bmod6\): reduced classes give zero character difference, while the non-reduced classes remain in the exceptional term.

Thus the linear difference really is
\[
d_h[\Lambda(m)\chi_6(m)-\Lambda(m+h)\chi_6(m+h)]
+S(h)[e(m)+e(m+h)].
\]
Only e is supported on powers of 2 or 3. The genuinely prime endpoint in a forbidden pair is retained in the character term. This validates the exact normalization, rather than an invalid deletion based only on impossibility of simultaneous primality.

## Logarithmic signed prefix and smoothing

The identity \(d_{2k}=S(2k)\chi_3(k)\), the positive divisor expansion of S, and complete multiplicativity of the fixed character give the author's finite divisor-prefix formula. The inner character prefix is bounded by one at real as well as integer endpoints.

For squarefree d coprime to 6,
\[
g(d)=d^{-1}\prod_{p\mid d}(1+2/(p-2)).
\]
Expanding the finite product, then enlarging the positive harmonic sum over multiples, bounds its total by
\[
(1+\log Z)\prod_{p>3}(1+2/[p(p-2)]).
\]
The product is finite. This proves \(D(Y)=O(\log(2+Y))\) without cancellation over the outer d variable.

The forward Stieltjes transform has derivative kernel
\[
T x^{-2}(1+h/x)^{-T-2}(Th/x-1).
\]
After v=h/x, the two relevant majorant integrals are exactly
\[
\frac{2T}{T+1},\qquad
\frac{2T}{(T-1)(T+1)}+\frac1{T+1}.
\]
They are bounded uniformly for real T≥4. Thus \(K_T=O(\log(2x))\) and \(K_T'=O(\log(2x)/x)\); multiplying by the already established b,b' bounds gives a smooth coefficient on the required scale.

The backward primitive cancels the (n−h) power before differentiation. Differentiating at fixed h combines the two large-looking terms into
\[
W_T'(s)s^{T-2}+W_T(s)s^{T-3}(Th/n-2).
\]
This is the correct sign and constant. Under the normalized Beta(1,T−2) majorant, the mean of Th/n is T/(T−1), uniformly bounded. It proves the derivative bound \(O(\log(2n)/(n^2\ell^2))\). Smooth zero extension removes moving-boundary terms. No relative error near a vanishing b or positivity of D is assumed.

## Applying PNT and treating both infinite ends

The live DLMF paragraph gives asymptotic prime counts in each fixed coprime progression. Partial summation converts these to log-weighted counts; all higher powers cost \(O(\sqrt x\log^2(2x))\). Therefore \(B_6(x)=o(x)\).

Both smooth coefficients satisfy \(|F|\ll1/(x\ell)\), \(|F'|\ll1/(x^2\ell)\) on [L,2U]. Exact endpoint partial summation costs
\[
O\{\eta_6(L)[\ell^{-1}+\ell^{-1}\log(2U/L)]\}=O(\eta_6(L)).
\]
This treats the whole smoothed shift sum before using PNT. No factor equal to the number of shifts is silently omitted.

For the forward far endpoint, the actual b-tail and the signed K bound give
\(U^{T-1}\ell^{-2}\sum_{m>2U}m^{-T}\log^2(2m)=O(2^{-T})\).
For the backward far endpoint, the actual primitive support gives exactly the same tail scale. The U powers cancel; the first discrete term is controlled because 2U≥T. Coarse compact-window derivative bounds are not summed to infinity.

## Periodic baseline and all sparse product exceptions

The period-six baseline has zero mean and bounded interval prefixes. For fixed h, the variation of k across an m-block is bounded by its increment; treating it this way avoids an unnecessary pointwise factor T. The endpoint-plus-variation norm of bk is therefore bounded by \(C(X\ell^2)^{-1}k(2X,h)\). The established positive prefix \(\sum_{h\le Y}S(h)\le Y\) then yields \(O(1/(T\ell^2))\) per dyadic block.

The far baseline retains \(U2^{-T}/(T^2\ell^2)\). It is absorbed in \(O(1/(T\ell))\) for the specified U=T^{9/4}; it is not itself declared \(O(2^{-T}/\ell^2)\).

For e, each near-window power of 2 or 3 contributes \(O(1/(T\ell^2))\), and there are \(O(\ell)\) powers. The forward singular-series and backward compact-Pareto integrals have the stated masses. Far tails sum geometrically with ratio at most \(2^{1-T}\).

On \(A_6=0\), the coefficient really is the nonnegative product \(\Lambda(m)\Lambda(m+h)\). Nonzero products have a 2- or 3-power endpoint; both orientations must be counted, allowing harmless overlap. The extra logarithm for the other endpoint increases the near-window total to \(O(1/T)\). For the upper far endpoint the exact primitive and Chebyshev remove the other endpoint sum. For the lower far endpoint, the first exceptional power lies between 2U and 6U, and the residual logarithmic factor divided by T is bounded; the rest is a geometric series with a linearly growing logarithm. This gives the complete stated \(O(2^{-T}/\ell^2)\) tail.

## Disposition and remaining target

The admissible coefficient is
\[
\Lambda(m)\Lambda(m+h)-S(h)(\Lambda(m)+\Lambda(m+h)-3)
\]
for h=0 mod6, and has singleton multiplier 2S(h) for h=2,4 mod6. The extra factor two is essential. The reviewed R22 inputs plus the two estimates above validate the ordinary arithmetic assembly; RH is still required for its actual-variance interpretation.

The author's inherited benchmark \(1-M\) is a stronger sufficient target. The essential current strict target remains a liminf below \(A-M\). Neither is proved by this normalization.

No amendment to the ordinary estimates is requested. This review accepts a legal fixed-congruence transformation and complete exceptional-product removal. It does not accept a growing-modulus extension, a strict bound on the remaining prime-pair correlation, AH refutation or any famous-conjecture solution. Preserve it as a new coordinator review without changing previously frozen author or owner-review files.

