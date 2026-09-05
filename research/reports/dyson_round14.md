# Dyson--Montgomery round 14: an actual Type I removal and a quantitative CUE heat theorem

Date: 2026-09-05. Two bounded results now have complete ordinary proofs, independent reviews and reproducible checks. One removes an exact portion of the actual arithmetic discrepancy. The other strengthens the finite CUE scalar-heat comparison. Neither proves a theorem about the full zeta pair correlation.

## 1. A specified arithmetic component is below the required scale

For the exact smooth discrepancy already defined in Rounds 9--13, retain its original sinc kernel, both logarithmic weights, all permitted moduli q<=Q=X^.523 and the primitive principal subtraction. Split the von Mangoldt coefficient by the exact identity

\[
\Lambda=\Lambda_{\le U}+\Lambda_{>U},\qquad
\Lambda_{\le U}(n)=\sum_{r\mid n,\ r\le U}\mu(r)\log(n/r).
\]

The [complete unconditional proof](../dyson/round14/smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md) establishes

\[
|\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le U}]|
\ll_{J,V,\chi} HX(UQ/X)^J\log^2X
\quad(J\ge2,\ UQ\le X/2).
\]

For U=X^.4, J=4 and H<=X^(2/7), this is O(X^(1711/1750)log²X)=o(X log X). More generally, for every fixed 0<eta<.477, all divisors below U<=X^(.477-eta) are covered by choosing a fixed J with J eta>2/7. The constants may depend on eta and J. No uniform limit as eta tends to zero is claimed.

The reason is exact progression Poisson summation in the smooth long cofactor n/r. Its zero mode cancels the actual primitive principal mean, and its nonzero modes decay because that cofactor exceeds q by a fixed power. The original joint kernel has uniform derivatives after the displayed integral representation removes its apparent singular phase. No smoothness is assigned to the shorter Möbius coefficients, and no dense-divisibility or RH estimate is needed for this portion.

This is a classical method applied and checked for the programme's actual kernel, not a novelty claim for Poisson summation. It also explains constructively how the large positive restricted rational cores from Round 13 can cancel when the actual longer factor is smooth. The signed Lambda_{>U} discrepancy remains exactly in the formula and is unestimated. Its cofactor need not be large or balanced. The full original discrepancy still has only the previously recorded RH bound, above X log X.

The [independent Type I review](../dyson/round14/smooth-long-factor/INDEPENDENT_REVIEW.md) checks every primitive mask, normalized derivative, frequency sign, summation factor and the precise individual-variable criterion for a Heath--Brown component.

## 2. A finite CUE heat-flow approximation has an explicit error scale

Let delta_min be the minimum circular angular gap of Haar CUE(N). At its midpoint define

\[
B_N=\sum_{k\text{ outside the pair}}
\frac1{4\sin^2((\theta_k-c)/2)}.
\]

The [complete CUE proof](../dyson/round14/cue-selected-background/SELECTED_CUE_BACKGROUND.md) establishes the finite-N estimate

\[
\mathbb E\sum_{i:\delta_i\le\varepsilon}B_i
\le N^6\varepsilon^3/18
\qquad(0<\varepsilon\le\pi).
\]

The proof uses the exact finite CUE three-point Gram determinant. Its simultaneous short-pair and endpoint vanishing factors control the singular inverse-square weights. Endpoint weights are used before enlarging to nonconsecutive pairs; directly enlarging a midpoint-weighted sum would be invalid. Circular ordering includes the wrap gap.

The classical minimum-gap law and Markov then give B_N/N²=O_p(1), without assigning a conditional density to the selected pair. For each fixed L,K>0 the proof supplies the explicit bound

\[
\limsup_N\Pr(B_N/N^2>K)
\le e^{-L^3/(72\pi)}+L^3/(18K).
\]

For the finite scalar-heat polynomial

\[
P_{N,s}(z)=\sum_{j=0}^N a_j e^{sj(N-j)}z^j,
\quad P_N(z)=\det(zI-U_N),
\]

let D_N be the first positive discriminant time. Applying the already quantified Galilean lemma with its verified uniform constants yields

\[
\frac{8D_N}{\delta_{\min}^2}-1=O_{\mathbb P}(N^{-2/3}),
\qquad
D_N-\delta_{\min}^2/8=O_{\mathbb P}(N^{-10/3}).
\]

This strengthens the programme's prior qualitative CUE comparison. It is an approximation error in probability, not a convergence rate for the limiting depth distribution. It is not a stochastic Dyson Brownian motion result or an available identity for true zeta zeros. General-beta analogues and global novelty remain outside this proof.

The [independent CUE review](../dyson/round14/cue-selected-background/INDEPENDENT_REVIEW_EUCLID.md) and [root review of both results](../dyson/round14/INDEPENDENT_ROOT_REVIEW.md) accept the proofs with these restrictions.

## 3. Preserved evidence

Seventeen original files totaling 548,013 bytes are preserved in the adjacent local `Astra-Local-Archive/round14-originals`. Fifteen research, review and receipt files are public and verbatim. The full Feng--Wei PDF/text remain local with public source hashes and precise source locations.

The [separate-process replay](../logs/round14-integration/recheck.json) passes both bounded scripts. It checks the symbolic N=3 CUE determinant and singular-weight cancellation, the constant 1/18, 63 complete-period centering cases, exact divisor/HB identities through n=125, rational exponent arithmetic and two fixed floating Gaussian Poisson diagnostics. One temporary source path is excluded from the Type I certificate comparison; the CUE JSON matches every field. These tests supplement ordinary proofs; they do not replace them or provide interval-certified stochastic estimates.

The integration receipt also records the earlier Galilean publication edit: only its title and reviewer attribution differ from the original hash cited by the CUE author. Root compared the complete mathematical bodies and found them identical. Both hashes remain visible; the original proof provenance is not silently rewritten.

## 4. What is still needed for the famous-conjecture target

The actual-zeta route still requires a signed estimate for the retained arithmetic remainder, with all covariance cross terms and principal means present. The CUE theorem supplies a rigorous RMT reference statement and exposes the missing zeta input: isolated close pairs and their background control cannot be assumed from low-band correlation data.

The sufficient two-scale W_T lower limit 1/16, compact Fourier test above 7/10, positive-density violation of AH-Pairs, sub-half normalized zeta gap and sub-186 prime gap remain unproved. No famous conjecture is reported solved. Broad numerical sweeps, another Fable session and a claim of full arithmetic-to-Fock convergence are postponed; the next arithmetic work concerns the exact remaining signed terms.
