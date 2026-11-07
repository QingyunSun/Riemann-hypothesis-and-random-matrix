# Primary-source refresh: zeta, DBM and prime gaps

6 November 2026. This is a bounded source audit, not a claim to exhaust the current literature. Read together with `DBM_BACKWARD_OBSTRUCTION.md` and `SOURCE_RECEIPT.json`. Full third-party papers and source trees remain in scratch storage; this directory contains only our analysis and compact provenance.

## What changed, and what did not

| Source | Version/date checked | Finding and review status |
|---|---|---|
| [Alpha-devbox PR 11](https://github.com/galpha-ai/Alpha-devbox/pull/11) | Head `0edc027d25b604c97588f7432ee5bac51452b912`; 49 commits; updated 6 Nov 2026, 10:40:07 UTC | Open. Latest comment at the beginning of this audit, `6682930107`, is our checkpoint, not new independent Fable review. Prior Fable comment inspected: 2 Nov, `6568092545`. No new collaborator result established. |
| [OpenAI PrimeGaps186](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330) | Main `61340d0b74163003b32756bb16e91d9209a5e330`, 2 Sep 2026 | Same checked head. Public support exists for the 186 project. Its Lean README explicitly identifies three assumed input results; this is not a fresh end-to-end formal verification by us. |
| [Sharifi prime-gaps Lean](https://github.com/romyar1/prime-gaps-lean/tree/b77bf175bdedc5123027b3fcf0abc38427975770), [author's 182 bundle](https://www.math.ucla.edu/~sharifi/AI/prime_gaps_182_expository_bundle.pdf) | Main `b77bf175bdedc5123027b3fcf0abc38427975770`, 4 Oct 2026 | Same head and identical PDF SHA-256 as prior checkpoint. No newly smaller prime-gap bound verified. |
| [Inoue, arXiv:2604.05733](https://arxiv.org/abs/2604.05733v1) | v1, 7 Apr 2026 | Unchanged checked version. RH-conditional normalized small-gap bound below 0.50895; not a critical-line proportion. |
| [Durkan–Pearce-Crump, arXiv:2610.28527](https://arxiv.org/abs/2610.28527v2) | v2, 23 Oct 2026 | Unchanged checked version. Half-spacing endpoint result; the RH positive-proportion statement is below 1/2+epsilon. It does not supply a strict below-1/2 zeta-gap theorem. |
| [Knausgård, arXiv:2610.08965](https://arxiv.org/abs/2610.08965v1) | v1, 6 Oct 2026; one author, Kristian Muri Knausgård | Newly incorporated in this audit: distinct from the earlier `2609.33043v2` paper in our scan. Landing, PDF theorem and public repository agree on the claimed stronger bounds. Computation not independently rerun. |
| [Wang, arXiv:2609.24167](https://arxiv.org/abs/2609.24167v2) | v2, 6 Oct 2026 | Withdrawn. Do not list the earlier numerical improvement as a presently established new theorem on this evidence. |
| [Arias de Reyna, arXiv:2610.24612](https://arxiv.org/abs/2610.24612v1) | v1, 17 Oct 2026 | Expository context; no new zeta local-distribution theorem was extracted from it. |
| [Landon–Sosoe–Yau, arXiv:1609.09011](https://arxiv.org/abs/1609.09011v4) | v4, 30 Sep 2026, compared with v3, 14 Jan 2019 | Checked actual regularity definition and universality theorem, not appendix titles. The usable obstruction is written out separately. Appendix F already occurs in v3. |
| [Fazzari–Gerspach, arXiv:2412.20099](https://arxiv.org/pdf/2412.20099v1#page=17) | v1, Lemma 2.7, equation (2.29) | Unconditional uniform prime-power singular-series mean supports the signed main-term argument. The localized arithmetic discrepancy remains an additional hypothesis. See the separate analytic source audit. |

## What the new Knausgård source actually claims

The exact title is *More than 83.9% of the zeros of the Riemann zeta function are distinct and more than 67.35% are simple and on the critical line.* Theorem 1.3 states

\[
\liminf_{T\to\infty}\frac{N_{0,s}(T)}{N(T)}
\ge \frac{1669159}{2478195}=0.67353820\ldots.
\]

The distinct-zero constant is `1645064/1960733 = 0.83900459675...`. These are the paper's claimed theorems; this audit does not certify the full proof.

Its architecture differs from the earlier unlabelled clipped-Gram inequality: multiplicity-labelled seven-point inequalities for distinctness, and an unlabelled eight-point inequality for simplicity on the line, combined with telescoping storage functions and a large-sieve bound on separated subsets. Proposition 5.2 requires a unit-diagonal Hermitian matrix, entrywise kernel approximation, and `U_SS <= 2 I` on every 0.85-separated subset. The critical-line constants are `x=.008722`, `b=.004389`, `C<1.3279474`, giving `(2-C-b)/(1-x)`. Proposition 7.3 bounds this particular certificate scheme: below `.67357` for index range at most seven, and below `.67383` for all pairs. These ceilings are not universal limits on zeta methods. [Paper, §§5 and 7](https://arxiv.org/pdf/2610.08965v1).

## Exactly what was checked about the computation

The [public repository](https://github.com/kristianmk/839/tree/b280d51bef5ab32b3280b0955d040085ed522d59) was pinned at `b280d51bef5ab32b3280b0955d040085ed522d59` (9 Oct 2026). Twelve selected files were downloaded; eleven files listed in its manifest matched their published hashes. The twelfth was the manifest itself.

The three added computational axioms are named:

```
Distinct839.Local.check_passes._native.native_decide.ax_1_1
Simple673.Local.check_passes._native.native_decide.ax_1_1
Line889.Local.check_passes._native.native_decide.ax_1_1
```

Each records acceptance of its branch-and-bound checker, evaluated by compiled `native_decide`. They are separate runs; the simple-critical-line theorem uses the second. Its declaration is `checkAllPar kTabArray 32 96 = true`, for root box `[13926,262143]^7`. The reported run visits 535,332,163 boxes. `axioms.txt` and the explanatory README agree on this trust boundary. [Pinned RunAll source](https://github.com/kristianmk/839/blob/b280d51bef5ab32b3280b0955d040085ed522d59/lean/Simple673/Local/RunAll.lean), [pinned Lean README](https://github.com/kristianmk/839/blob/b280d51bef5ab32b3280b0955d040085ed522d59/lean/README.md).

**Review limitation:** no complete Lean build, compiled search, table regeneration, or kernel-only replay was performed here. Matching hashes and reading a reported successful run verify provenance, not that run's correctness. The result has a public computational proof claim with an explicit compiler/runtime trust dependency; describing it as independently verified by this programme would be false.

## Consequences for AH and actual zeta: our assessment

An improvement in the proportion of simple zeros alone does not refute the Alternative Hypothesis. A simple process supported on a half-lattice can have 100% simple points while still retaining its lattice spacing obstruction. A new simplicity constant therefore does not imply sine-kernel correlations, non-lattice spacings or a strict below-half gap.

The potentially useful transfer is structural. To exploit the new certificates, one must identify a zeta-derived observable retaining the required local labels, index ordering and joint cluster geometry, prove its separated-subset matrix bound with the actual window, and show its arithmetic average contradicts every relevant half-lattice model. For the critical-line theorem the certificate is unlabelled, so multiplicity labels must not be silently imported into that conclusion. For a dynamical extension, the needed marks would additionally encode which neighbours act on the same root, and their coupling to the prime-weighted statistic.

Our older half-grid operator-norm counterexample does not automatically disprove the new certificate: the window, threshold and local assumptions changed. Conversely, the new certificate does not supply the missing prime-weighted correlation estimate. The first useful next step is to evaluate the new window and local functional on explicit AH examples and locate exactly which hypothesis, if any, excludes them.

The separate clock/DBM note makes another obstruction precise: mesoscopic regularity and even perfect initial rigidity do not control the difference between original microscopic statistics and those after adding Gaussian noise. A positive order-one Duhamel integral occurs in an explicit example. A zeta transfer needs arithmetic control of that integral, not only another local law.

## Publication scope

No famous conjecture was proved or refuted by this source refresh. The new contributions to this packet are an explicit backward-transfer obstruction, a stronger provenance audit, and an independent check of the singular-series input to a conditional signed main-term theorem. Further certificate reruns, a full novelty review, an actual-zeta discrepancy estimate, and stronger prime-gap claims are postponed.
