# Round 11: remove the shift-length loss using actual RH prime input

Date: 2026-09-05. **Under RH, this round improves the same actual smooth shifted-prime discrepancy to X^1.023 log^5 X.** It also proves a narrow arithmetic obstruction to coefficient-only power savings and makes the log-weighted residual's positive diagonal explicit. None of these results proves the required new zeta pair-correlation lower bound.

## The component improvement

Keep the Round 10 discrepancy, with Q=X^(523/1000), X=T^alpha, 6/5<=alpha<=7/5 and H=X/T. It is the actual Mobius-log weighted progression discrepancy selected by the Round 9 complementary conditions, with its original sinc kernel and fixed smooth cutoffs V in C_c^infinity(1,2) and chi in C_c^infinity(1,3/2). The [full proof](../dyson/round11/prime-frequency/CENTERED_SMALL_ARC_BOUND.md) establishes

\[
\boxed{|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{X(X+Q^2)}\,(\log X)^5
\ll X^{1.023}(\log X)^5\qquad\text{under RH}.}
\]

This removes sqrt(H) from Round 10. The additional RH assumption is material; the earlier bound was unconditional. The saving in powers of X is 1/12 at H=X^(1/6), and 1/7 at H=X^(2/7). The bound applies to any squarefree subfamily with the specified cap and therefore does not claim a new dense-divisibility theorem.

After division by the required X log X covariance scale, the estimate is still O(X^.023 log^4 X). The full sharp shift packet, complementary divisor piece, support main terms and final signed covariance remain outside this bound. In particular, the compact Fourier target greater than -3/5 and the two-scale target 1/16 remain unproved.

## Where the arithmetic gain comes from

[Bhowmik–Schlage-Puchta, Lemma 3](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/Goldbach4.2.10.pdf), printed page 3, proves under RH

\[
\int_{-1/y}^{1/y}\left|\sum_{n\le x}(\Lambda(n)-1)e(\beta n)\right|^2d\beta
\ll (x/y)\log^4 x,\qquad 1\le y\le x.
\]

Its proof includes the cutoff errors in the Selberg/Gallagher passage. Partial summation transfers it to a smooth genuine-prime polynomial minus its integer mean, E_f=A_f-B_f. Prime powers cost no more than the same bound. The frequency derivative is another such polynomial, E_f'=2pi i X E_(u f), so its norm is controlled without differentiating an asymptotic error.

The exact Round 10 pairing has coefficients C_(a/d)=S_v(a/d)M_d, with

\[
M_d=\sum_{q\in\mathcal Q,\ d\mid q}\frac{\mu(q)}q,
\qquad S_v(\beta)=\sum_h v(h/H)e(-\beta h).
\]

Equal rational frequencies are already merged. Sampling on disjoint intervals of length comparable to Q^-2 and retaining only the local arc gives a squared prime norm O(X(X+Q^2)rho log^4 X). The coefficient mass on the jth dyadic band is O(H 2^((1-2J)j) log^3 Q), while rho is at most 2^j/H. These factors cancel H before summation. J=2 suffices to sum all frequency tails.

Both remaining mean terms are retained: the smooth integer mean is handled by Poisson summation, and the primitive Ramanujan mean by a first-power shift bound and the reciprocal-totient sum. Neither introduces a new H loss. The two-variable Fourier separation includes derivative costs in both indices; its rapid decay handles the actual sinc kernel and log cofactor. The original progression prime-power error and the later centered-polynomial prime-power subtraction are distinct, and both are included.

The [independent review](../dyson/round11/prime-frequency/SMALL_ARC_INDEPENDENT_REVIEW.md) checks the primary source, weighted prefixes, derivatives, local sampling, every tail band, both means and the full kernel. Root also read the complete argument. This is an internally reviewed ordinary proof, not formal verification or a novelty claim for the classical ingredients.

## Actual prime moduli prevent a coefficient-only shortcut

The [conductor construction](../dyson/round11/conductor-arithmetic/CONDUCTOR_MASS_LOWER_BOUND.md), with [independent review](../dyson/round11/conductor-arithmetic/INDEPENDENT_REVIEW.md), fixes the full canonical family of all distinct q=[D,E] satisfying the Round 9 balanced complementary predicates and coefficient mu(q). For fixed nonnegative nonzero V it proves

\[
\sum_{d,a}^{*}|S_v(a/d)M_d|^2\gg_V H/(\log X)^{348}.
\]

The construction uses two primes in a fixed-ratio interval of exponent .09 and 346 primes in one of exponent 343/346000. All factors are distinct. Their product is in (Q/2,Q], has positive Mobius sign, and splits into two roots within the exact radius .2615. Only the large prime in each root triggers its guard, leaving a strict margin .0255. PNT and unique factorization give a positive constant times Q/log^348 X different moduli, for every sufficiently large X.

At a terminal conductor d=q>Q/2 no other multiple is at most Q, so its full signed coefficient is exactly 1/d. Enough primitive low numerators have a shift transform bounded below by a positive multiple of H. Summing their squares proves the lower bound. An additional log q improves its logarithmic power to log^-346 X.

This excludes an O(H X^(-eta)) coefficient-norm bound for any fixed eta>0 on this full family. It does not exclude a specially pruned family, different weights, frequency localization, or cancellation between the actual prime polynomial and these coefficients. It is entirely compatible with the small-arc improvement above. No numerical prime realization or claim of an effective threshold is involved.

## The exact positive diagonal leaves a signed arithmetic remainder

The [mixed-tail note](../dyson/round11/log-weighted-tail/ARITHMETIC_DIAGONAL_AND_SOURCE_GAP.md), with [independent review](../dyson/round11/log-weighted-tail/INDEPENDENT_REVIEW.md), starts from the genuine-prime residual R_b at displacement b/(2 log T), with N=floor(T/log^6 T). Define K_b=-R_b-(log T)^(-1)partial_s R_b and

\[
M_T(b)=\frac{e^b}{T\log^2T}\operatorname{Re}\langle R_b,K_b\rangle.
\]

The finite centered measure uses prime atoms of mass log p minus Lebesgue measure on (N,Y]. RH gives an explicit uniform cutoff error for it and its log-weighted companion. The pole is then removed at O(e^b log^-3 T), retaining the endpoint correction. On 2<=b<=2G(T), G=o(log log T), the result is

\[
M_T(b)=\frac1{b^2}+\frac2{b^3}+\mathcal B_T(b)+o(b^{-3}).
\]

Here B_T is the combined centered off-diagonal remainder, including both prime-continuum terms and the continuum square. Only their combined limit is justified. The explicit diagonal comes from prime lengths T^(1+O(1/b)); the accessible slice below T is nonpositive and negligible.

A uniform bound B_T(s)>=-(4-epsilon)/s^3-o(s^-3), or the stated strict integrated improvement, would supply the earlier AH-excluding criterion. **Neither bound is proved.** Chirre's checked derivative identity leaves the unknown out-of-band form-factor integral; its fixed-width asymptotic does not supply this arithmetic estimate. The valid but enormous analytic cutoff is not presented as a practical computation.

## Verification, provenance and next step

All 18 original files, 536,670 bytes, are retained locally under `Astra-Local-Archive/round11-originals/`; 15 research files are public verbatim. Three third-party PDF/text/HTML bodies stay local with URL/hash receipts. The [intake manifest](../dyson/round11/INTAKE_MANIFEST.json) records each file. The [separate replay](../logs/round11-integration/recheck.json) checks both bounded scripts in a copy, excluding only the temporary primary-source path from the conductor certificate. The complete small-arc JSON is identical. Exact checks cover rational exponents, counting constants, 384 finite arc counts and 2,901 unique frequency memberships; they are not tests of RH itself.

```text
python3 research/logs/round11-integration/recheck.py --prime-gap-source /path/to/openai-short-gaps.pdf
python3 tools/verify_manifest.py
```

The next useful attempt must use signed joint prime/modulus cancellation beyond positive sampling, or prove a one-sided estimate for the combined mixed remainder. The coefficient construction alone cannot rule these out. A generic positive-sampling improvement, an unqualified import of the 186 dispersion theorem, and short-interval upper bounds are being checked against their exact hypotheses before further computation.

The long PDFs retain their previously stated checkpoints; this report adds a new source record. Rollback is a revert of this slice. Formalization, a full covariance theorem, and a solved famous conjecture remain outstanding. No new external-model session, large scan, or infrastructure layer was added.
