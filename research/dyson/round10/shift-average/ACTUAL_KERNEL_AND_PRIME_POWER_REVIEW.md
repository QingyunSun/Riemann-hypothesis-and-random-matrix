# Independent review: actual shift kernel and genuine-prime replacement

Date: 2026-09-05. **Accepted for the stated smooth packet.** This is a narrow ordinary-proof review of Sections 1–2 and 6 of `SMOOTH_SHIFT_COMPLETION_BOUND.md`, pinned to SHA256 `7b52e4d82dc40bf90183331d548b7fffe5545d1928d7cb93223223b5b71c1d78`. The reduced-fraction coefficients and finite-spacing bounds are independently covered by `COEFFICIENT_AND_SPACING_AUDIT.md`; this review does not present that other review as its own work.

No fatal gap was found in the object identification, prime-power deletion, coprime completion prerequisites, or exact separation of the actual two-variable weight. This acceptance does not upgrade the resulting discrepancy estimate to the required zeta covariance scale.

## 1. The object really is the localized Round 9 discrepancy

Author equation (3) is precisely the Round 9 equation (21) with the additional scalar shift weight V(h/H). The convention for Delta includes both a progression sum and the coprime principal sum. The residue is h; the shifted argument is m-h; the logarithm is log((m-h)/q). These remain in their correct places. The smooth packet has H<h<2H, and therefore is contained in the earlier hard shift cutoff provided its fixed constant is at least two, as explicitly assumed.

The source modulus family is squarefree and has q<=X^.523. No new source-distribution conclusion is being imported: the subsequent completion only uses squarefreeness and this cap. The claimed power improvement concerns this one identified smooth discrepancy component. The unsmoothed full shift range, other divisor components, and continuous covariance centering are not estimated here.

## 2. Both prime-power portions have been bounded

Write theta_*(m)=log m on primes and zero otherwise. On the fixed support, m and m-h are comparable to X, the a-factors and sinc are bounded, and the extra logarithm is O(log X). For each h and each prime power m=p^j with j>=2, the progression contribution only involves q dividing m-h. Hence the number of possible q is at most tau(m-h), independently of the detailed selected family. The bound tau(n)<<_eta X^eta together with the prime-power von Mangoldt mass O(sqrt(X) log^2 X) gives the first term of the author's (4):

    O_eta(H X^(1/2+eta) log^3 X).

The principal portion is a different sum and cannot be omitted. Bound its prime-power mass absolutely, multiply by the O(log X) logarithmic weight and by sum_(q<=Q)1/phi(q)=O(log X), then sum the O(H) shifts. This gives

    O(H sqrt(X) log^4 X).

Retaining or dropping the principal coprimality restrictions by an absolute upper bound is valid. In particular this step accounts for prime powers with primes dividing q as well as those not dividing q; it does not confuse these with primes dividing h. At eta=1/100 and H<=X^(2/7), the largest displayed power is X^(557/700), which is strictly smaller than X. Both nuisance terms are therefore o(X log X), and also smaller than the claimed completion bound.

Only after this replacement is every surviving m a genuine prime exceeding Q. Then m is a unit modulo every q. In the progression sum, h congruent to m modulo q forces (h,q)=1 automatically, so the h-coprimality restriction may be removed there. It must remain in the principal term, where it becomes the exact unit-residue projector. The order of operations in the draft is correct. Performing this extension before prime-power removal would need extra terms, and the draft does not do that.

All these estimates are unconditional. RH is only needed in the previously stated conversion from this discrepancy to the relevant aggregate zeta covariance component.

## 3. Uniform smooth separation of the actual kernel

Put epsilon=H/X=1/T, y=m/X and z=h/H. On the support, y-epsilon z lies in a fixed compact subset of (1,3/2), and z lies in a fixed compact subset of (1,2). Thus both original a-factors take their inverse-three-halves branch. Their product is exactly

    y^(-3/2) (y-epsilon z)^(-3/2).

The sinc phase is exactly

    epsilon^(-1) log(y/(y-epsilon z))
       = integral_0^z du/(y-epsilon u).

This integral representation also proves the removable epsilon=0 limit z/y and gives uniform bounds for every fixed mixed y,z derivative on a slightly larger fixed rectangle, for all sufficiently small epsilon. It avoids differentiating the misleading 1/epsilon factor separately. The sinc function is smooth at zero, so there is no hidden singularity. The support stays away from y-epsilon z=0 and from the a-factor branch corner; the minimum definition of a therefore introduces no derivative defect.

The same derivative bounds hold after multiplication by log(y-epsilon z). On a larger fixed rectangle, use fixed compact cutoffs and the two-variable Fourier series of the smooth amplitude. Its coefficients decay faster than any fixed power in both frequency indices, uniformly in epsilon. Each term becomes f_k(m/X)v_l(h/H). The prime-factor estimate used later depends only on the bounded sup norm of f_k, not on its derivatives; the finite-difference estimate for v_l costs at most a fixed polynomial in l. Uniform rapid coefficient decay absorbs that polynomial, so the separated estimates sum absolutely with a uniform constant. No approximation remainder is left unestimated.

Finally the exact cofactor identity is

    log((m-h)/q)=log X-log q+log(y-epsilon z).

The constant log X factor, the log q conductor coefficient, and the additional smooth logarithmic amplitude are the three legitimate cases treated in the author proof. The resulting log^(7/2) bound from the first two cases is harmlessly relaxed to log^4. A q-dependent function has not been silently included in a common smooth amplitude.

## 4. Scope and acceptance

The actual sinc kernel is retained, including its sign. No positivity, variance asymptotic, RH, or convergent critical-strip prime series is used in this component estimate. The completed bound remains larger than X log X throughout the displayed alpha interval. The draft says so explicitly.

This review accepts the fixed smooth packet only. A bounded-variation extension of the separated coefficient estimate may be possible, but the full sharp packet is not claimed or required here. No endpoint extension, parameter search, or new numerical prime experiment was performed. The attached receipt pins the reviewed author report, Round 9 source convention, and this review; its exact fraction checks verify the nuisance exponent and the support cap inequality, not asymptotic prime distribution.
