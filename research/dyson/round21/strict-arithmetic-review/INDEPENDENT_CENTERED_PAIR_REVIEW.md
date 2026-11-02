# Independent review of the R21 centered prime-pair target, corrected after the h=1 obstruction

Date: 2026-09-05. Reviewer: residual_gram / Astra. **The revised ordinary reduction and unconditional singular-series lemma are accepted; the proposed uniform all-shifts exponent below one half is proved impossible.** No strict aggregate estimate, AH refutation or new Montgomery–Dyson theorem is accepted.

This review supersedes my original acceptance, SHA256 `5a0de0ac42401897b4e417be4ce8804867ede2b937ff6ebc85a9711df02728e4`. I missed a substantive feasibility defect: the original report treated its uniform all-shifts premise with beta below 4/9 as merely unproved. The originating coordinator found the h=1 obstruction. My original review, receipt and replay files are preserved byte-for-byte under [superseded-before-h1-obstruction/prior-independent-review](../strict-arithmetic-target/superseded-before-h1-obstruction/prior-independent-review/INDEPENDENT_CENTERED_PAIR_REVIEW.md); they are historical evidence, not current acceptance of that premise. The corrected proof keeps the valid main identity and signed aggregate target.

The current reviewed author file is [CENTERED_PAIR_ERROR_TARGET.md](../strict-arithmetic-target/CENTERED_PAIR_ERROR_TARGET.md), SHA256 `d7e73b8379e1adadd1fba79e3dc6141252c796502ba793030a500a8c5a6fc15e`, 21,504 bytes. The full original proof and primary-source material were read in the first review. For this revision I independently read every changed mathematical passage, the coordinator's complete obstruction, the new checker and the unchanged-block comparison. I verified both DLMF inputs live. The author files were not edited.

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

## 4. Abel norm, finite support and the formal exponent budget

Differentiating the exact representation (22) gives |b_T′(m)|≪1/(m²log²T), with no extra factor T. The derivative has one term from 1/m and one from the smooth logarithmic weight; integrating u^{T-2} supplies the factor (T−1)^{-1}. This verifies (30).

For fixed h, the Pareto factor is increasing with m. Its total variation on [X,2X] is at most its upper endpoint. The product variation is therefore at most a constant times (X log²T)^{-1}(1+h/(2X))^{-T}. Abel summation against the centered prefix error gives (29). No differentiation of the arithmetic error is being assumed.

The h>X tail is exponentially small uniformly for X in the window: the kernel is at most a decaying Pareto tail starting at 1+h/(2X)>3/2, while the coefficient majorants have only polynomial growth. The previously discussed m>2U tail is independently negligible.

There is no hidden extension of the proposed X-range in the dyadic decomposition. One may cover (L,U] by truncated dyadic intervals whose base points lie in [L,U], and handle (U,2U] with the block based at X=U. Abel summation on a subinterval uses differences of the same prefix errors and changes only an absolute constant. Thus the hypothesis in (31), if actually established uniformly throughout the stated window, is sufficient for this bookkeeping.

The bound Σ_{h≥1}(1+h/(2X))^{-T}≤2X/(T−1) gives the displayed factor H=X/T. As exponent arithmetic, a uniform beta below 4/9 would beat X≈T^{9/4}, even after O(log T) blocks and a fixed logarithmic loss. But the actual all-shifts premise is impossible for every beta below 1/2, as proved in the next section. Therefore the formal 4/9 implication is vacuous as a proposed arithmetic strategy. My first review failed to make this essential distinction.

The square-root error budget still has the exact X exponents −1/14, 0 and 1/18 at the three marked alpha values. A hypothetical signed-aggregation saving H^rho would need rho>1/10 to overcome the worst power. This is a budget for a different, genuinely open signed estimate, not a way to revive the impossible pointwise premise. A mean square over shifts alone does not justify that signed saving.

## 5. Independent review of the coordinator's h=1 obstruction

I read the full [COORDINATOR_H1_OBSTRUCTION.md](../strict-arithmetic-target/sources/COORDINATOR_H1_OBSTRUCTION.md), SHA256 `5270e51de9df32aecee7fd63e569c5f3cdcd743107fc1c7f7be69cf6df587d34`, 4,963 bytes, and the originating `COORDINATOR_CENTERED_PAIR_REVIEW.json`. I checked the local retained copy against the originating note. The ordinary argument is accepted, including its unconditional scope. The revised author equations (32a)–(32e) correctly incorporate it.

For integer X<z≤2X, the h=1 singular series vanishes and direct expansion gives
\[
\begin{aligned}
E_X(z,1)
&=\sum_{X<m\le z}\bigl[\Lambda(m)\Lambda(m+1)-\Lambda(m)-\Lambda(m+1)+2\bigr]\\
&=P_X(z)-2[E(z)-E(X)]-\Lambda(z+1)+\Lambda(X+1).
\end{aligned}
\]
Both singleton endpoint signs are correct. In every nonzero product one of two consecutive prime powers is even and hence a power of two. Counting the possible even members gives the uniform bound P_X(z)=O(log²X). This argument keeps all prime powers and makes no assumption about Mersenne or Fermat primes.

The integer restriction causes no gap: those endpoints already suffice for the dyadic contradiction. For clarity, a direct check at arbitrary real endpoints adds the fractional-part correction and yields
\[
E_X(z,1)=P_X(z)-2[E(z)-E(X)]
-\Lambda(\lfloor z\rfloor+1)+\Lambda(\lfloor X\rfloor+1)
+2(\{X\}-\{z\}).
\]
This is only an explanatory endpoint identity; the author's proof uses integer endpoints.

Uniformity in all sufficiently large real T and every X in [T^{7/4},T^{9/4}] includes every sufficiently large integer X by T=√X. Thus a fixed beta<1/2 and fixed logarithmic loss give |E(z)−E(X)|≪X^theta for any fixed max(beta,0)<theta<1/2. The powers-of-two increments form a geometric series because theta>0. One final block reaches any large integer N. The extension E(y)=E(floor y)−{y} supplies E(y)=O(y^theta) for all real y. No conclusion of this kind is inferred from a premise valid only along a sparse sequence of T.

For Re s>1, logarithmic differentiation of the absolutely convergent Euler product and integration of each indicator n≤y give
\[
\int_1^\infty E(y)y^{-s-1}\,dy
=\frac{-\zeta'/\zeta(s)}s-\frac1{s-1}.
\]
An O(y^theta) bound makes the integral holomorphic on Re s>theta by locally uniform absolute convergence, including after multiplying by any fixed power of log y for differentiation. At a critical-line zero rho of multiplicity m_rho, the meromorphic expression has residue −m_rho/rho, which is nonzero. The subtraction at s=1 cannot cancel it. The uniqueness theorem for meromorphic continuation therefore gives the contradiction.

I checked [DLMF 25.2.11](https://dlmf.nist.gov/25.2.E11), which states the Euler product in Re s>1, and [DLMF 25.10(i)](https://dlmf.nist.gov/25.10), specifically its paragraph after equation 25.10.2 stating that there are infinitely many critical-line zeros. Only one such zero is needed. The obstruction is unconditional; it does not depend on RH or an assumed location of an unverified zero. These standard source facts are separate from the new report's derived contradiction.

The correction has a narrow but decisive scope. The actual signed target liminf E_T≤1−M, the Pareto identity, the singular-series transform and the Abel inequality survive. Under RH, the same h=1 identity gives a prefix bound O(√X log²X). Substitution into the single-shift Abel norm gives O(X^{-1/2}) on each block, since log X and log T are comparable; its sum over the present window is o(1). Thus this pointwise impossibility does not itself obstruct the weighted aggregate. Estimates on specified restricted shifts, averaged estimates, or a treatment separating odd or small shifts need their own full error budget and are not ruled out here.

## 6. Primary-source ranges and what is not imported

I checked Montgomery–Soundararajan printed p.5 visually and against the extracted text. Theorem 3 assumes uniform prime-tuple errors for every relevant k and distinct shifts. For K=2 its conclusion has H≤N^{1/2} and retains the H²N^{1/2+η} error. The k=1 part is related to RH, but the k=2 hypothesis is not supplied by RH. The author's distinction is accurate.

Chan printed p.2 explicitly labels the mean-square tuple input Conjecture 2 and obtains the moment conclusion under that hypothesis. It is not an unconditional theorem furnishing the centered shift-aggregate needed here. No such conditional result is used to prove the main reduction; only the unconditional singular-series average is imported from these papers.

I also read the retained 186 primary text around Proposition 2.3 and Corollary 2.19. The latter is an absolute sum of allowed one-prime progression discrepancies, uniform on subintervals. It is not the prime-pair error (28), and applying a per-shift estimate in absolute value leaves the shift count. The author correctly preserves the distinction between legal uses for individual divisor pieces and an unproved bound for the full von Mangoldt pair.

The new scale H ranges from X^{3/7} to X^{5/9}; it does not equal the older X^{1/6} to X^{2/7} range. The crossing H>X^{523/1000} occurs at alpha>1000/477, with the stated direction. The report does not silently import the old discrepancy estimate into this different complete pair statistic. The earlier phase-twist/Siegel–Walfisz obstruction is used only as a limitation on that direct inference, not as a proof that every different dispersion approach is impossible. Reproving that prior obstruction is outside this review; its pinned dependency hash was verified unchanged.

## 7. Independent replay, preservation and final scope

The original `check_centered_pair_target.py` remains unchanged, SHA256 `51f9178f5035e285005ddd27ec88773f03253ddc1d7dee85a8d5c2114e136129`. Its previously replayed JSON/log remain byte-identical to the original author outputs, SHA256 `52a481cad73b2c26de39ce2607097ba0f99fe590c510fd35fd10a74d553dfdc2`. They pin the superseded original author and are preserved as that original verification record. I did not rerun them against the changed author or relabel their provenance.

That initial replay covered twelve exact finite signed kernel cases, twenty-five floor cases, four beta/harmonic-moment cases, twelve formal prime-power corrections and rational exponent arithmetic. It did not establish that the hypothetical all-shifts exponent premise was mathematically possible. The inherited bump decimals are diagnostics, not interval-certified bump moments.

For the correction I read `check_h1_correction.py`, SHA256 `879c35d3efed14e5c0d2108de3bad078616c0259a4406f9669ffc92944573f4f`. I copied its exact necessary inputs into a temporary directory and replayed only this tiny addendum. The independent JSON and log are byte-identical to the author's new outputs, each SHA256 `e868183e0dcc78ea4a6021d7cbd65d5abae5d7150993fc369de3bb5012c6340e`.

This replay checks the formal h=1 expansion, twenty-two exact singleton-endpoint cases, the symbolic Mellin residue, six geometric-sum identities and the rational window/exponent comparisons. It also verifies that original sections 1–4, equations (28)–(30), the square-root budget (33)–(34), and the primary-source audit are unchanged. All original checker/output bytes are checked against their preserved copies. The analytic impossibility follows from the ordinary argument, not the finite tests.

All entries of the current author source manifest and all referenced correction/preservation hashes were checked against retained bytes. The initial source-page visual review remains applicable to the unchanged primary-source sections. No numerical height, prime scan, parameter sweep or author-file change was made. The separate receipt pins the revised author, coordinator note, new checker and outputs, current review, and original superseded acceptance.

No further amendment is requested to the frozen revised author. The accepted work is the actual centered arithmetic reduction, unconditional Pareto singular-series lemma and unconditional rejection of the uniform sub-square-root all-shifts shortcut. The strict signed upper estimate for E_T remains open.
