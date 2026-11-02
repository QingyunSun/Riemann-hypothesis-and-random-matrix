# Independent review of the R21 centered prime-pair target

Date: 2026-09-05. Reviewer: residual_gram / Astra. **Accepted as an ordinary conditional reduction and unconditional singular-series lemma, within the stated scopes.** No mathematical amendment is requested. The review does not accept the unproved strict pair-error estimate, an AH refutation, or a new Montgomery–Dyson theorem.

The complete reviewed author file is [CENTERED_PAIR_ERROR_TARGET.md](../strict-arithmetic-target/CENTERED_PAIR_ERROR_TARGET.md), SHA256 `81a676d68836bff15a50ba6190bf2c1eab7cd54f0d3ae85d604a48fc36a7e54e`, 17,025 bytes. I read its full proof and final checker. I also read the relevant primary-source text and visually inspected Montgomery–Soundararajan printed pp.4–5 and Chan printed p.2. The author files were not edited.

## 1. The actual center and exact kernel

The definition a_n=Λ(n)−1 preserves both singleton prime terms. At arbitrary real endpoints, the number of integers in (x,qx] is floor(qx)−floor(x), so
\[
\Delta=S+r,\qquad
r=\lfloor qx\rfloor-\lfloor x\rfloor-(q-1)x.
\]
The remainder is the difference of two fractional parts and has absolute value at most one. It is not a neglected average prime error.

The total positive measure of the x window is at most T/(L log²T), since the exponential length measure has mass one. Hence the squared norm of r is O(T^{-3/4}/log²T). R20 supplies a bounded squared norm of the actual continuously centered count under RH. Applying the norm triangle inequality and then the difference-of-squares bound gives O(T^{-3/8}/log T) for the replacement by the discretely centered square. No independent short-interval first-moment assertion is required.

The all-length indicator survival is exactly (x/max(m,n))^T. The x integral stops at min(m,n), and for m<n=m+h the resulting coefficient is
\[
b_T(m)\left(\frac{m}{m+h}\right)^T.
\]
The diagonal and the two ordered off-diagonal orientations therefore give (14), with the factor two exactly as written. The lower integration endpoint 1 in b_T is harmless because the actual weight vanishes below L. No approximation of the Pareto factor by an exponential occurs.

The centered error in (4) really contains
\[
a_ma_{m+h}-(\mathfrak S(h)-1)
=\Lambda(m)\Lambda(m+h)-\Lambda(m)-\Lambda(m+h)+2-\mathfrak S(h).
\]
Thus both singleton discrepancies and the discrete integer center remain present. A source estimate for an uncentered prime-pair sum would have to control these additional terms before it could imply the author's error estimate.

## 2. The singular-series source and its uniform Pareto transform

Montgomery–Soundararajan define their centered singular series by inclusion–exclusion. For a two-point set it is S({d₁,d₂})−1. Their R₂(k) sums over ordered distinct shifts in {1,…,k}; translation invariance gives exactly
\[
R_2(k)=2\sum_{1\le h<k}(k-h)(\mathfrak S(h)-1).
\]
This verifies both the factor two and the sign in the triangular average. On printed p.4, equation (16) is the unconditional formula −k log k+A k+O(k^{1/2+η}). Choosing one fixed η<1/2 gives the author's weaker O(k) form with an absolute fixed constant. The sharp error is not needed.

The hinge sum is linear on each interval between consecutive integers. Its real interpolation consequently satisfies A₂(y)=−(1/2)y log y+O(y) for y≥1. Below one it vanishes, and the author separately accounts for that range rather than claiming y log y=O(y) there.

For k(y)=(1+y/m)^{-T}, the identity Σc_h k(h)=∫A₂(y)k″(y)dy is legal. One especially direct justification is to integrate each hinge: its integral against k″ is k(h). Absolute interchange follows from |c_h|≪h^η and T≥4. Thus there is no hidden assumption on differentiability of the staircase A₂ or on its unknown signed first derivative.

The density yk″(y)dy has mass one. Under u=Ty/m it becomes exactly (1+1/T)u(1+u/T)^{-T-2}du. Its mean u is 2T/(T−1)≤8/3, while on (0,1) its density is at most 5u/4. In particular
\[
\mathbb E|\log u|\le\frac5{16}+\frac83.
\]
The error in A₂ contributes O(1), and the correction from 0<y<1 is also O(1), because m≥T. This proves the uniform −(1/2)log(m/T)+O(1) conclusion without a varying-test asymptotic or an unproved individual estimate for c_h. The optional exact digamma expression and the integer harmonic-number specialization have the correct parameters: the beta-prime law has parameters 2 and T.

Every m with b_T(m)≠0 satisfies m>L=T^{7/4}>T for T≥4. Thus the lemma covers the entire coefficient support; there is no missing small-m region.

## 3. Weight approximation, tails and the full prime-power diagonal

The substitution x=mu gives (22) exactly. The zero extension of the smooth compact weight allows differentiation through this integral. The integral of |log u|u^{T-2} is (T−1)^{-2}, giving the stated uniform error O(1/(mT log³T)) in (23). No derivative of an asymptotic prime formula is used.

This error is summed only on L<m≤2U. Summing it against a_m²≪log²(2m) gives O(1/T). The main weight has total mass O(1/log T). The author correctly switches to the original integral for m>2U; using the pointwise approximation error on the entire infinite tail instead would not suffice.

Here is an explicit justification of the asserted exponential tail. With the harmless fixed choice |c_h|≪h^{1/2}+1, the absolutely summed comparison inner kernel is O(m^{3/2}) uniformly for T≥4. The actual inner kernel is O(m(1+log m)²), using |a_n|≤1+log n and the integrability of powers and logarithms against (1+h/m)^{-4}. Multiplying by b_T(m)≪U^{T-1}m^{-T}/log²T and summing m>2U gives a fixed polynomial in U and log U times 2^{-T}. Since U=T^{9/4}, this is o(1). These estimates also justify the full absolute convergence claimed before the centered comparison is subtracted.

For the diagonal, partial summation of the RH bound for Ψ gives ΣΛ(n)log n=z log z−z+O(√z log³(2z)). At n=p^k,
\[
\Lambda(n)\log n-\Lambda(n)^2=(k-1)(\log p)^2.
\]
This vanishes on primes but must be retained on higher powers. Its total through z is O(√z log³(2z)), so Σa_n²=z log z+O(z) follows. The report includes this correction explicitly.

Partial summation against W_T(z)/z now gives the diagonal main term ∫αω(α)dα. The O(z) cumulative error contributes O(1/log T), and the extra derivative of z log z contributes only another lower-order term. The singular-series main term is −∫(α−1)ω(α)dα, with its uniform O(1) error multiplied by Σb_T=O(1/log T). Their difference is exactly M=∫ω. This cancellation does not require replacing primes by a random model or assuming that a marginal prime average is uniform over the short shifts.

Together with the floor estimate, these facts prove Vbar_T=M+E_T+o(1) under RH. Therefore liminf E_T≤1−M is equivalent to the proposed liminf Vbar_T≤1 target. It remains unproved. The existing RH upper A only gives limsup E_T≤A−M, as the author states.

## 4. Abel norm, finite support and the hypothetical exponent budget

Differentiating the exact representation (22) gives |b_T′(m)|≪1/(m²log²T), with no extra factor T. The derivative has one term from 1/m and one from the smooth logarithmic weight; integrating u^{T-2} supplies the factor (T−1)^{-1}. This verifies (30).

For fixed h, the Pareto factor is increasing with m. Its total variation on [X,2X] is at most its upper endpoint. The product variation is therefore at most a constant times (X log²T)^{-1}(1+h/(2X))^{-T}. Abel summation against the centered prefix error gives (29). No differentiation of the arithmetic error is being assumed.

The h>X tail is exponentially small uniformly for X in the window: the kernel is at most a decaying Pareto tail starting at 1+h/(2X)>3/2, while the coefficient majorants have only polynomial growth. The previously discussed m>2U tail is independently negligible.

There is no hidden extension of the proposed X-range in the dyadic decomposition. One may cover (L,U] by truncated dyadic intervals whose base points lie in [L,U], and handle (U,2U] with the block based at X=U. Abel summation on a subinterval uses differences of the same prefix errors and changes only an absolute constant. Thus the hypothesis in (31), if actually established uniformly throughout the stated window, is sufficient for this bookkeeping.

The bound Σ_{h≥1}(1+h/(2X))^{-T}≤2X/(T−1) gives the displayed factor H=X/T. A uniform exponent β<4/9 therefore beats the largest power X≈T^{9/4}, even after O(log T) blocks and a fixed logarithmic loss. The square-root error budget has the exact X exponents −1/14, 0 and 1/18 at the three marked alpha values. The additional formal H^ρ saving would need ρ>1/10 to overcome the worst power. These are valid sufficient-budget calculations; they do not assert the required estimates or a lower bound for their actual errors. A mean square over shifts alone does not justify a signed-cancellation saving.

## 5. Primary-source ranges and what is not imported

I checked Montgomery–Soundararajan printed p.5 visually and against the extracted text. Theorem 3 assumes uniform prime-tuple errors for every relevant k and distinct shifts. For K=2 its conclusion has H≤N^{1/2} and retains the H²N^{1/2+η} error. The k=1 part is related to RH, but the k=2 hypothesis is not supplied by RH. The author's distinction is accurate.

Chan printed p.2 explicitly labels the mean-square tuple input Conjecture 2 and obtains the moment conclusion under that hypothesis. It is not an unconditional theorem furnishing the centered shift-aggregate needed here. No such conditional result is used to prove the main reduction; only the unconditional singular-series average is imported from these papers.

I also read the retained 186 primary text around Proposition 2.3 and Corollary 2.19. The latter is an absolute sum of allowed one-prime progression discrepancies, uniform on subintervals. It is not the prime-pair error (28), and applying a per-shift estimate in absolute value leaves the shift count. The author correctly preserves the distinction between legal uses for individual divisor pieces and an unproved bound for the full von Mangoldt pair.

The new scale H ranges from X^{3/7} to X^{5/9}; it does not equal the older X^{1/6} to X^{2/7} range. The crossing H>X^{523/1000} occurs at alpha>1000/477, with the stated direction. The report does not silently import the old discrepancy estimate into this different complete pair statistic. The earlier phase-twist/Siegel–Walfisz obstruction is used only as a limitation on that direct inference, not as a proof that every different dispersion approach is impossible. Reproving that prior obstruction is outside this review; its pinned dependency hash was verified unchanged.

## 6. Independent replay and final scope

I read `check_centered_pair_target.py`, SHA256 `51f9178f5035e285005ddd27ec88773f03253ddc1d7dee85a8d5c2114e136129`, then copied only that file and the frozen author report into a temporary directory and ran the small checker there. The independently retained JSON and log are byte-identical to the author's, each with SHA256 `52a481cad73b2c26de39ce2607097ba0f99fe590c510fd35fd10a74d553dfdc2`.

The replay covers twelve exact finite signed kernel cases, twenty-five floor cases, four beta/harmonic-moment cases, twelve formal prime-power corrections and the rational exponent thresholds. The bump decimals are embedded inherited diagnostics and are labeled accordingly. The exact arithmetic performed on those decimals does not turn them into interval-certified bump moments. No prime scan, numerical height, zeta-zero calculation or additional parameter search was performed.

Every entry of the author's source manifest was checked against the retained bytes; the results are saved in `source_hash_checks.json`. The three source-page images were also inspected directly. The separate receipt pins the author, checker, source manifest, this review and the replay outputs.

No amendment is requested. The accepted result is an explicit actual centered arithmetic target and its proved normalization. The required upper estimate for E_T remains open.
