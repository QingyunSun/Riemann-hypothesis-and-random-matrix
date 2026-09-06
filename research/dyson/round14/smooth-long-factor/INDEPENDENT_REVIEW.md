# Independent review: smooth long-factor removal

Date: 2026-09-05. **Accepted as an unconditional ordinary proof of the stated component bound.** No mathematical correction is requested. This is an independent check of the complete authored note, with special attention to the exact kernel, primitive restrictions, Poisson normalization, uniform derivatives, and total error. It does not claim an estimate for the remaining signed discrepancy or the zeta covariance.

The reviewed author file is `SMOOTH_LONG_FACTOR_REMOVAL.md`, SHA-256 **d6143f19ddf006a1acc833ecd2e5265bffb35817930cfeaa4f4e4b973af7c849**. The author file and its existing outputs were left unchanged. The proof was compared with the frozen R9 discrepancy definition and R11 kernel formula. The bounded author script was inspected and replayed in a temporary copy; its certificate agrees after normalizing only the temporary source path. Replay details are in `INDEPENDENT_REPLAY.json`, and hashes of the reviewed dependencies and review artifacts are in `INDEPENDENT_REVIEW_RECEIPT.json`.

## Acceptance coverage

| Item | Author location | Finding |
|---|---|---|
| Actual discrepancy and log-cofactor weight | Equations (4)–(6) | Matches R9/R11; no weight or primitive principal term is dropped. |
| Periodic phase mean and Fourier sign | Equations (7)–(11) | Correct, including nonprimitive numerators and nonsquarefree moduli. |
| Exact profile and uniform derivatives | Equations (12)–(15) | Correct in the full stated parameter range. |
| Progression Poisson formula and zero mode | Equations (16)–(17) | Correct sign, factor L/q, and exact principal cancellation. |
| Sum over every r,h,q | Equations (18)–(20a) | Correct bound HX(UQ/X)^J log²X and exponent thresholds. |
| Exact signed remainder and HB identity | Equations (6), (21)–(22) | Correct; the criterion requires an individual smooth long variable. |
| Validation scope | Adjacent script/certificate | Small exact algebra and floating Gaussian diagnostic only; not a computational proof of the analytic estimate. |

## 1. Kernel and parameter uniformity

For n=rs, L_r=X/r, u=s/L_r, δ=H/X=1/T, and z=h/H, the exact identities are rs=Xu and rs−h=X(u−δz). Because χ is supported inside (1,3/2), both arguments of the a-factors lie above X on the nonzero support. Thus both use the power −3/2. The two logarithms become precisely

\[
\log s=\log(X/r)+\log u,\qquad
\log((rs-h)/q)=\log(X/q)+\log(u-\delta z).
\]

The sinc argument has no hidden large derivative:

\[
\delta^{-1}\log\frac{u}{u-\delta z}
=\int_0^z\frac{dt}{u-\delta t},\qquad
\partial_u^j\int_0^z\frac{dt}{u-\delta t}
=(-1)^j j!\int_0^z\frac{dt}{(u-\delta t)^{j+1}}.
\]

Here z lies in a fixed compact subset of (1,2). On the support, u−δt≥u−δz is bounded away from zero for 0≤t≤z. Also δ≤X^{-5/7} in the stated range. The profile therefore has a fixed positive compact support for all sufficiently large X, and every fixed u derivative of the nonlogarithmic factors is uniformly bounded. The only growth is from the two logarithms, each O(log X), since 1≤r≤U<X and 1≤q≤Q<X. This proves the uniform O_J(log²X) seminorm bound. Smooth zero extension is legitimate because χ is compactly supported strictly inside its open interval.

The needed derivatives are derivatives in the normalized summation variable u, **uniformly in** r,h,q,T; the proof does not require differentiating an arithmetic cutoff with respect to r or q. There is no missing r^J factor: the rescaling to L_r already accounts for it. The exact joint kernel is retained throughout.

## 2. Primitive masks and Poisson cancellation

If (r,q)>1 and (h,q)=1, rs≡h mod q has no solutions, and the primitive principal sum has no terms because (rs,q)>1. Such terms vanish in both parts, rather than contributing an exceptional error. If (r,q)=1, multiplication by r gives

\[
rs\equiv h\pmod q\iff s\equiv h\bar r\pmod q,
\qquad (rs,q)=1\iff(s,q)=1.
\]

The resulting class b=h r̄ is a unit. For the Fourier convention \(\widehat\Phi(t)=\int\Phi(u)e(-tu)du\), the progression formula is

\[
\sum_{s\equiv b\ (q)}\Phi(s/L)
=\frac Lq\sum_k\widehat\Phi(kL/q)e(kb/q).
\]

Averaging this formula over all unit b produces exactly c_q(k)/φ(q). The k=0 terms cancel since c_q(0)=φ(q). The sign in author equation (16) is consequently correct. The bounds |c_q(k)|≤φ(q) and |Φ̂(t)|≪_J log²X |t|^{-J}, together with J≥2 and L≥2q, give equation (17), including its factor L/q.

The auxiliary periodic identity in §2 is also correct: a unit inner n permutes the units, so the period mean of R is zero. With R(m)=Σ_ℓ R̂(ℓ)e(ℓm/q), Poisson yields the coefficient R̂(−ν mod q) in equation (9). Multiples of q vanish as well. The shift bound Σ_{1≤a<q}|S_{V,H}(a/q)|≪q follows by summing the stated decay, both when q≥H and when q<H. This auxiliary explanation is not substituted for the direct progression proof of the actual kernel.

## 3. Total error and numerical exponents

The bound for one retained r,h,q is

\[
\ll_J q^{J-1}(X/r)^{1-J}\log^2X.
\]

Taking absolute values of the Möbius coefficients, summing the actual shifts with Σ_h|V(h/H)|≪H, and enlarging the permitted moduli to every q≤Q gives

\[
\ll_J HX^{1-J}\log^2X
\left(\sum_{r\le U}r^{J-1}\right)
\left(\sum_{q\le Q}q^{J-1}\right)
\ll_J HX(UQ/X)^J\log^2X.
\]

No extra q, H, or divisor-count factor is omitted. The q=1 discrepancy is identically zero, so including it in this upper sum causes no issue. Real U≥1 with the stated integer cutoff also causes no endpoint term.

For U=X^{2/5}, Q=X^{523/1000}, H≤X^{2/7}, and J=4, the exponent is 1711/1750, with margin 39/1750 below 1. For U≤X^{477/1000−η}, fixed η>0 ensures UQ≤X/2 for sufficiently large X. Any fixed integer J≥2 satisfying Jη>2/7 gives o(X log X), despite the remaining logarithmic square. The dependence of constants on η and J is properly stated; no claim uniform as η↓0 is needed.

## 4. Signed remainder and Heath–Brown scope

The identities Λ=μ*log and Λ=Λ_{≤U}+Λ_{>U} hold pointwise, including n=1, and the discrepancy is linear. Therefore equation (6) is exact before estimation. Neither sign nor cancellation properties of the untreated divisor portion are inferred from the small estimate for the retained portion. Prime powers have not been removed, so there is no missing prime-power exception here.

For the displayed Heath–Brown identity, E=ε−μ_{≤Y}*1=μ_{>Y}*1 is supported on integers greater than Y. Thus E^{*k}*Λ vanishes for n≤Y^k. Expanding ε−E^{*k} and using 1*Λ=log gives equation (21) with its displayed binomial coefficients and signs. Taking Y^k beyond the support covers all terms.

After a smooth multiplicative partition, an individual unrestricted 1 or log variable of scale L≥QX^η admits exactly the same progression argument. The other variables may be grouped into a short arithmetic coefficient c(r); no smoothness is assigned to c(r). For fixed identity order, divisor multiplicities cost at most X^ε and fixed logarithmic factors, which a larger fixed J absorbs. The criterion does not apply merely because a product of several rough variables is long. This limitation, the possibility of an unbalanced Λ_{>U}, and the absence of a bound for the whole remaining discrepancy are all stated correctly in the author report.

## 5. Replay and final scope

The inspected script checks 63 exact periodic-centering cases, the formal-logarithm divisor and HB identities through n=125, the real short cutoff 9/2, and exact rational exponent arithmetic. Its two Gaussian progression comparisons have the correct Poisson sign and agree within the stated binary64 tolerance; these are diagnostics, not rigorous enclosures. The temporary replay passed every assertion and reproduced the certificate modulo its temporary source path. Original report, script, certificate, and log were not changed.

This review accepts the displayed unconditional removal of a definite short-divisor component. It does not upgrade the R13 positive restricted-core claim into a full signed lower bound, establish cancellation for an arithmetic long coefficient, estimate the remaining Λ_{>U} discrepancy, or imply AH/RH/Montgomery progress beyond the explicit component reduction. No additional scan, literature claim, or author edit is required for acceptance of the result as stated.
