# Independent review of the two-scale actual-zeta reduction

Date: 2026-09-05. Reviewer: the residual/arithmetic lane, independently of the authoring lane.

**Verdict: accepted as an ordinary RH-dependent reduction, with no remaining mathematical obstruction found in the reviewed argument.** The review accepts `RH + AH-Pairs => W_T -> W_AH`, including cancellation without a limit for P_0(T), and accepts both proposed sufficient arithmetic lower bounds. It does **not** prove either lower bound for actual zeta mean squares, refute AH, establish a new zeta-spacing theorem, certify novelty, or constitute proof-assistant verification.

One minor truncation issue was identified and corrected by the author during review: the fixed physical pair cutoff must avoid limiting half-lattice atoms. The current text explicitly takes M=j+1/4. The transfer proof and model formulas were otherwise unchanged. The subsequent addition of the weaker sufficient threshold 1/16 has also been checked.

The reviewed report and script hashes, temporary-copy replay details, and final metadata-only status change are pinned in `independent_review_receipt.json`.

## 1. Acceptance coverage

| component | result | reason |
|---|---|---|
| Exact source AH formulation and RH dependence | accepted | The source's AH0, (1.12), (1.14), (1.15) supply exactly the stated pair concentration, tail bound and finite-T masses. |
| Near-diagonal nuisance cancellation | accepted | The alternating comb includes k=0 and contributes 2(P_0(T)-1)/sinh(b); the two coefficients cancel at the same T. No limit for P_0(T) is used. |
| Noncompact pair test | accepted after the endpoint clarification | Uniform O(1/M) tails allow fixed-M asymptotics first; M=j+1/4 avoids atomic truncation endpoints. |
| Completed-zeta normalization | accepted | Pairing positive and negative zeros removes the possible exponential constant; the real logarithmic derivative has the required absolutely convergent Poisson sum. |
| Finite-zero endpoints and gamma centering | accepted | Width T/log^4(T), unit-interval zero counts and the pair bound control all normalized square tails; the gamma discrepancy has normalized L2 norm O(1/log T). |
| Real square to modulus square | accepted | Under RH, the square of zeta'/zeta has no poles in the chosen rectangle; the holomorphic-square vertical integral is negligible for every large T. |
| Constants and sufficient thresholds | accepted | Exact rational enclosures separate W_AH from both 7/100 and 1/16; independent symbolic checks link the closed constants to the variance formulas. |
| Script scope | accepted | The scripts prove/check constants and finite-model identities. They do not compute an actual-zeta mean square. |

## 2. Primary source check and the role of P_0(T)

The primary paper was read directly at [Goldston–Lee–Schettler–Suriajaya, arXiv:2507.06823v1](https://arxiv.org/html/2507.06823v1). Its AH-Pairs formulation uses the high interval T/log^2(T)<gamma,gamma'<=T. The RH-dependent fixed-k formulas and bounded P_0(T) are available there; its Section 2 explains removal of the excluded early range. The reduction correctly keeps these inputs separate from the paper's additional AH-Weak Density hypotheses.

Only additive o(1) accuracy for each fixed k is required. Since only finitely many k occur before the truncation limit, those errors may be combined without imposing uniform asymptotics for k growing with T. The near-zero bin may include multiplicity and near-coincident distinct zeros. It is therefore correct to preserve P_0(T), rather than silently replacing it by one.

Relative to the p_0=1 half-lattice pair measure, the finite-T mass change is

    (P_0(T)-1) sum_k (-1)^k delta_(k/2).

Its Fourier transform has mass 2 at every odd integer. Therefore its Poisson variance contribution is

    2(P_0(T)-1) sum_(m in Z) exp(-b |2m+1|)
      = 2(P_0(T)-1)/sinh(b).

The coefficient two and the inclusion of the diagonal are both necessary. The same formula follows in physical space from the classical alternating Cauchy-kernel sum. The combination at b=2 and b=1 cancels the entire nuisance parameter at each T, after the noncompact-test approximation has been justified.

## 3. Pair tails and the corrected cutoff

The source pair bound gives normalized mass O(1+h) for differences of size at most h, for 0<=h<=T. Since K_b(x)=O_b((1+x^2)^-1), a dyadic decomposition between M and T contributes O_b(1/M). Beyond T, the total normalized pair mass is O(T log T), whereas the kernel is O_b(T^-2), giving O_b(log T/T). These estimates are uniform in T for fixed b.

For the model family, bounded P_0(T) gives uniformly bounded absolute atomic weights, hence another O_b(1/M) tail. Positivity of every finite-T approximate model weight is not needed for that latter absolute bound.

A hard cutoff at a half integer would not by itself have a determined limit: an AH cluster could approach that endpoint from either side. The author's repair M=j+1/4 eliminates this ambiguity. The early-range discrepancy is o(1) for each such fixed cutoff, and the limiting bin concentration then evaluates the finite sum. Sending T to infinity first and M to infinity second proves the stated expansion uniformly for the bounded nuisance parameter. It is legitimate that Q_T(b) need not itself converge when P_0(T) oscillates; only the two-scale combination is asserted to converge.

## 4. Completed-zeta identity and endpoints

With L=log(T)/(2pi), a=b/(4pi), and eta=a/L, a single Poisson term satisfies

    P_a(L(t-gamma))
      = 1/(pi L) * eta/[eta^2+(t-gamma)^2].

Under RH, the paired canonical product about 1/2 has factors `1+(s-1/2)^2/gamma^2`. The function is even about 1/2 and has order one; no nonconstant exponential prefactor remains after pairing. Its logarithmic derivative consequently gives exactly the sum over both positive and negative ordinates, with multiplicities. The real-part series converges absolutely. There is no missing factor of two: summing over both signs already supplies the two linear factors of each paired zero.

The finite convolution identity uses `P_a*P_a=P_(2a)` and a change of variable dt=dx/L. Its normalization is therefore exactly the report's `(TL)^-1` pair measure. The kernel evaluates to

    K_b(x)=2b/(b^2+4pi^2 x^2).

The unit-interval zero count is sufficient for the stated endpoint estimates. On the two strips of width w=T/log^4(T), both finite and completed sums are O_b(log T), so their normalized squared integrals are O_b(log^-2 T). On the interior, omitted negative and above-T zeros have total Poisson contribution O_b(log T/(L^2 w)). The pair bound provides a bounded normalized square integral for the finite sum, so Cauchy–Schwarz controls the interior replacement.

The far exterior estimate O_b(log T/(L^2 d)) has an integrable square for d>=w. The full integral of a finite Poisson sum is N(T)/L; the loss from interior zero tails is bounded by summing the displayed reciprocal distances, and the boundary zero count gives a vanishing normalized contribution. Thus the mean tends to one and the subtraction of one in the centered square is correctly normalized. No exact stationarity of finite zeta zeros is assumed.

## 5. Gamma centering and the holomorphic-square rectangle

The extra real terms in xi'/xi equal one half of log(t/(2pi)), with the stated uniform lower-order error. Since pi L=log(T)/2, dividing by pi L and subtracting one leaves

    [log(t/T)-log(2pi)]/log(T) + lower-order terms.

Its normalized L2 norm is O(1/log T): the integral of |log(t/T)|^2 divided by T stays bounded, and the fixed initial interval causes no difficulty. The bounded normalized L2 norm supplied by the pair statistic justifies removal of this centering discrepancy by Cauchy–Schwarz. This yields the factor four in front of the real-square mean.

For F=zeta'/zeta, RH places every nontrivial zero strictly to the left of the rectangle whose left side is 1/2+eta. The pole at one is below its bottom side t=1. Thus F^2 is analytic in the rectangle. On Re(s)=2, its absolutely convergent Dirichlet series has no constant coefficient, so its vertical integral is O(1). On the top side, the local zero count and distance eta from the critical line give the uniform bound F=O_b(log^2 T), hence an O_b(log^4 T) horizontal integral. This works even if T is exactly a zero ordinate: the positive real displacement eta prevents a pole. The bottom and the initial segment are harmless.

Consequently the holomorphic-square integral is o(T log^2 T). Applying

    2(Re F)^2 = |F|^2 + Re(F^2)

is now justified, rather than merely assumed. Finally eta=b/(2log T), so the modulus integral is exactly I_T(b/2), giving

    Q_T(b)=2 I_T(b/2)/(T log^2 T)+o(1).

This argument is unweighted. An arbitrary arithmetic weight would change the contour problem and cannot inherit this vanishing without a separate proof.

## 6. Model spectra and exact constants

The half-lattice pair measure has diagonal mass one and the correct nonzero half-lattice masses. Fourier transformation gives the triangular periodic density plus atoms at the nonzero even integers. Those atoms are essential. The nuisance modification instead adds atoms at odd integers. The reported spectra and their Poisson integrals are consistent with these two different combs.

The variance formulas were checked independently against the closed W expressions as exact rational-function identities in x=exp(1). This closes a small verification gap that a script evaluating only the closed constants would leave: the constants really are the stated two-variance combination, not merely two separated numbers.

The rational exponential enclosure uses the sum through degree 40 and bounds the remaining factorial series by a geometric majorant. Its interval arithmetic is valid even though it repeats the same exponential variable, because independent interval multiplication only enlarges the enclosure. The certified inequalities imply both

    W_AH < .06240 < .07,
    W_AH < .06240 < 1/16,

and `1/16-W_AH > .00010`. Therefore either RH-conditional lower bound on the corresponding liminf would contradict AH-Pairs. The number .07 is a convenient stronger target, not a logically necessary threshold. Neither arithmetic lower bound follows from the constant calculation.

## 7. Replay, scope and remaining obligation

Both check scripts were copied to a fresh temporary directory and run there. Their generated JSON matched the author's files after ignoring the elapsed-time field. The exact constant script was replayed again after addition of the 1/16 assertions. Original mathematical files were not altered by the reviewer. The only authorized final report edit is the first paragraph's review-status metadata and link to this review; the receipt verifies that distinction and pins the final files.

The finite subset enumerations are floating-point calibration, while the symbolic identities and Fraction arithmetic establish their stated algebraic and constant assertions. A rational finite canonical-product example checks a normalization; it does not by itself prove the infinite xi-product statement, which is instead justified analytically above.

The unresolved work is the actual signed mean-square inequality. The half-lattice model already matches the known interior Fourier band and satisfies spectral positivity, so those facts alone cannot force a value above W_AH. The reviewed reduction makes the missing arithmetic statement precise; it does not supply the out-of-band information or control the negative tail by a new prime-correlation estimate. Acceptance of this reduction must not be described as a proof of such an inequality or as a refutation of AH.
