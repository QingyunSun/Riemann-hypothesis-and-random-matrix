# Bounded review of the research synthesis

Date: 2026-11-01 America/Los_Angeles / 2026-11-02 UTC. Reviewer: `r29_close`.

**Disposition: PASS within the stated scope; no material mathematical correction identified.** This is an applicability and claim-scope review, not an independent certification of the complete external papers or their Lean dependency closures. The stochastic report was written by this reviewer: the check of that report below is an author self-check, not an independent review. Root separately reported replaying all six symbolic checks successfully; this pass did not repeat them.

## 1. Findings

1. **QRH and zero statistics.** The synthesis correctly orders the numerical bounds: a smaller right boundary excludes a larger half-plane. A fixed zero-free half-plane restricts real parts and does not supply out-of-band pair or triple correlation, local repulsion, or RH. The distinction between original-paper statements, formalization scope, and this project's actual checks is retained. Cubic Gauss/theta structure is not identified with three-point zero correlation.

2. **No Siegel zero does not imply no AH.** The synthesis does not reverse the relevant one-way implication. Excluding a possible source or motivation for AH does not exclude the statistical hypothesis itself. Suggested editorial precision: replace “实际零点数据” with “关于真实零点的新解析输入,” so the sentence does not sound as though numerical observations are required for a proof.

3. **R30 hypothetical exponent test.** The source bound in `UPPER_HEIGHT_BALANCED_CHECK.md`, §§3–4, is indeed
   \[
   D^{1/2+\eta}/\bigl(T^{3/4}\sqrt{\log T}\bigr).
   \]
   Its sharp odd Möbius estimate is uniform over a specified polynomial-height range under RH. At the central scale \(D\asymp T\), replacing that input *hypothetically* by an equally uniform \(D^{B+\eta}\) gives \(T^{B-3/4+\eta}/\sqrt{\log T}\). For \(B=0.874957\ldots\), this particular upper bound does not tend to zero. The synthesis correctly calls this a test of one existing estimate. It neither establishes the proposed replacement from QRH nor transfers the other RH-dependent inputs to an unconditional setting, and it does not claim the actual quantity must grow.

4. **Finite residue comparison.** The quoted depth, size, prime-size, interval-length and indicator-error bounds agree with the exact commit-pinned source. Offsets really are uniform in this intermediate lemma; this does not make the final fixed-form Chowla theorem a theorem about arbitrary growing shifts. Every translate uses the same residue coordinate at a given prime, as the synthesis requires. The distinction between truncated small-prime tests and the actual central arithmetic term is essential and preserved.

   For the next application, add the two source details that the prose currently abbreviates: the auxiliary modulus \(l\) is fixed, the selected primes do not divide \(l\), and the sufficiently-large-\(L\) threshold may depend on \(l\). Moreover, the scalar-expansion corollary assumes total coefficient mass at most \(\exp(C L^5)\) and gives error \(\exp(-L^9)\). The indicator error \(\exp(-L^{10})\) cannot be silently retained after an arbitrary weighted expansion. The current synthesis does not make that mistake; it correctly lists coefficient control as unfinished work.

5. **Finite models and stochastic protection.** Author self-check confirms the \(\beta=2\) radial generator \((\Delta+V\cdot\nabla)/(2N)\), the product correction \(-mn p_{m+n}/N\), and filtration by separate positive/negative weights. The multitime theorem uses one shared budget across all observations. The balanced character at weight \((N+1,N+1)\) has discrepancy \(-\exp(-2(N+1)t)\) under this normalization. This establishes a sharp obstruction to enlarging the universal rectangular budget, not a classification of every minimal distinguishing observation. The full continuous-path reconstruction is outside that budget and has no claimed finite-data stability. No deterministic Newman-flow identification or actual-zeta theorem is asserted.

6. **Other model conclusions.** The pair-matched perturbation is explicitly acknowledged to change a mixed moment already in the protected range, so it is not advertised as matching the entire AH moment input. The sparse-defect argument separates all fixed-order local correlation limits from global extreme gaps and does not derive a Newman depth law. The sine rigidity conclusion is restricted to Hermitian convolution-kernel DPPs with spectral density in \([0,1]\); it is not asserted for arbitrary stationary point processes.

The proposed signed graph moments, out-of-band triple test and cubic-theta detector remain research targets. None is presented as a proven arithmetic transfer or a famous-conjecture result.

## 2. Exact source and review boundary

The finite-residue source was read from the already identified URL, without a new literature search:

<https://raw.githubusercontent.com/openai/math/4eaee87548250b2682affda7d05d947c05554bae/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/02-finite-law.tex>

Its SHA-256 is `473761422e03b4a185af34a2ec8aaf5cececff9d04fcf8d05a95f7e052757952`, matching the public source receipt. The circuit encoding, low-order Fourier correction, and scalar-expansion statement were inspected. This check does not independently reprove Braverman's theorem or the complete ordinary-Chowla argument. The QRH proof audit was already completed in this lane and was not restarted.

Files reviewed, with the exact versions before any subsequent editorial changes:

| File | SHA-256 |
|---|---|
| `latest-literature-2026-11-01/CHOWLA_TRANSFER_AND_RESEARCH_DECISIONS.md` | `50ab411aa6221467f38647ff908ce088c0fe3ab4c3269707491e11085cf44ac8` |
| `latest-literature-2026-11-01/QRH_METHOD_AUDIT.md` | `6e3397e0d482dc3479fbb1809885f561b6e01ee149a6d35edcf06f41fb22f638` |
| `stochastic-protection/AGENT_STOCHASTIC_PROTECTION.md` | `90c5d88bc938f8410550d337f5689c30726efb614b29a6bf80f75c94671e14f3` |
| `research/dyson/round30/stationary-challenge/UPPER_HEIGHT_BALANCED_CHECK.md` | `53aa1b19cd28094248efe2ac5d3f88859e27f1751ebb1ffbbaa6c6e38213d5f2` |
| `pair-matched-flow/AGENT_PAIR_REVIEW.md` | `54e1233b31ca01f48c6889543d3eb04624ef65884d71ad7f9b71b0833eb5e4e2` |
| `pair-matched-flow/RARE_DEFECT_LOCAL_UNIVERSALITY.md` | `97187d986208b85963b359764a1fc470238b6116f29ce50e470777194e160063` |

Except for the explicitly repository-relative R30 path, table paths are relative to `research/counterexamples/`. No historical file was edited, no scan or symbolic replay was repeated, and no Git operation was performed in this review.
