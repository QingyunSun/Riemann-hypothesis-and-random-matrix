# What the pair-matched heat counterexamples do and do not settle

Date: 2026-11-01 America/Los_Angeles (2026-11-02 UTC). Status: bounded primary-source literature audit and exact scope check. This note does not independently certify the numerical or algebraic heat-depth certificates in the companion report. No claim of a solved zeta conjecture or established novelty is made.

## 1. The defensible conclusion

The finite constructions in `PAIR_MATCHED_HEAT_COUNTEREXAMPLES.md` target a precise model implication: complete static two-point data, even supplemented by a nearest-neighbor gap histogram, determine a chosen observable's deterministic heat-flow response or backward collision depth. A certified counterexample disproves that implication. It does not disprove Montgomery's conjecture about actual zeta zeros, and it does not establish that the full sine two-point function can be realized by a different stationary infinite process.

There are three separate distinctions:

1. Complete two-point data are weaker than all protected mixed trace moments or all higher correlation functions.
2. Convergence of every fixed local correlation function is weaker than control of rare events in an increasing observation region at an additional shrinking gap scale.
3. An artificial unitary spectrum is not automatically an admissible model for the arithmetic constraints on zeta zeros, nor does its deterministic scalar heat flow automatically inherit Dyson Brownian motion universality.

The new proof obligation of this lane is the exact dynamical separation and the positivity of any perturbed ACUE law. The underlying homometric complements are classical.

One arithmetic distinction is essential: the **full** n=2 GUE/pair-correlation conjecture already implies a positive proportion of normalized gaps below every fixed epsilon>0, and would rule out AH. Lagarias–Rodgers state this explicitly in §2.2. AH survives the available restricted test data, not that full conjecture. [Precise statement](https://academic.oup.com/qjmath/article/71/1/257/5714711).

## 2. Static homometry and its novelty limit

For a subset A of a finite cyclic group, its full difference-count function is encoded by A(x)A(x^{-1}) modulo x^M-1. Different sets with equal such functions are called homometric or Z-related. Jedrzejewski and Johnson, *The structure of Z-related sets*, §2, attribute complement homometry to Patterson (1944); in particular every half-filled subset of a regular even polygon is homometric to its complement. Their Theorem 2 also gives a periodic union construction. Thus neither the complement identity nor replication alone is a new result. The earlier Patterson paper was not independently read in this audit. [Primary exposition](https://arxiv.org/html/1304.6608v1).

The broader inverse problem is also classical: identical autocorrelation or diffraction need not determine the underlying object. Grimm and Baake discuss deterministic and random weighted-comb constructions with shared diffraction and differing entropy. Those examples are not, by themselves, alternative realizations of the exact sine two-point function or models of zeta zeros. [*Homometric point sets and inverse problems*](https://arxiv.org/abs/0808.0094).

Kuna, Lebowitz and Speer study realizing finitely many prescribed correlation functions; their constructions include nonuniqueness under stated hypotheses. Their general realizability results cannot be substituted without checking hypotheses for a unit-intensity sine-kernel two-point realization. [*Realizability of point processes*](https://arxiv.org/abs/math-ph/0612075).

## 3. An exact mixed-moment obstruction

Use the normalization already derived in the project report `research/reports/dynamic_generator.md`:

\[
p_m=\sum_{j=1}^N e^{im\theta_j},\qquad
L=\sum_k\left(\sum_{j\ne k}\cot\frac{\theta_k-\theta_j}{2}\right)\partial_{\theta_k}.
\]

It gives

\[
Lp_m=-m\left((N-m)p_m+\sum_{a=1}^{m-1}p_a p_{m-a}\right).
\]

Since L is a first-order real derivation, the product rule gives the exact identity

\[
\boxed{L|p_2|^2=-4(N-2)|p_2|^2-4\operatorname{Re}(p_1^2\overline{p_2}).}
\]

Consequently, two laws with equal E|p_2|² but unequal E L|p_2|² have unequal E Re(p_1² conjugate(p_2)). In the supplied N=6 example, a derivative difference of -16 would force a mixed-moment difference of +4 when the pair observable agrees. This implication is exact algebra; the supplied derivative values themselves are certified in the companion construction, not by this literature audit.

The mixed moment p_1² conjugate(p_2) is balanced and has positive Fourier weight 2. It belongs to Tao's protected CUE/ACUE low-moment class when N≥2. Tao's Proposition 1 concerns weighted trace moments, a larger collection than the diagonal quantities E|p_m|². His matrix-to-zeta discussion is explicitly heuristic. Therefore a perturbation detected by the displayed derivative cannot simultaneously preserve the entire protected moment class. [Tao, *The alternative hypothesis for unitary matrices*, 8 May 2019](https://terrytao.wordpress.com/2019/05/08/the-alternative-hypothesis-for-unitary-matrices/).

This is a useful obstruction to a stronger proposed construction, not a defect in a theorem explicitly limited to pair data. Preserving an entire gap-histogram law does not remove it.

## 4. The genuine published AH nonuniqueness question

Lagarias and Rodgers construct a stationary shifted half-lattice point process compatible with the higher-order bandlimited zeta tests in their Theorem 4.7. In §6 they ask whether the process is unique among processes with half-integer separations and the same correlations against every K_n; they expect nonuniqueness. Appendix B also distinguishes their model's gap probabilities from a uniqueness assertion. This is a precise published research question to target. A pair-only perturbation does not answer it. A bounded search found no resolution, but this is not an exhaustive claim about its current status. [*Higher correlations and the alternative hypothesis*, QJM 71 (2020), 257–280, §6](https://academic.oup.com/qjmath/article/71/1/257/5714711).

Their separate *Bandlimited mimicry of point processes* defines mimicry using **all orders** and a Fourier-support box. Theorem 1.4 gives uniqueness of the mimicker's correlation measures on aZ when B>1/(2a), under its hypotheses. It is not a pair-correlation uniqueness theorem. At a=1/2, Theorem 1.8 allows sine mimicry at B=1 and excludes B>1. The strict inequality in the uniqueness theorem matters; the critical boundary cannot be discarded. Its box condition must also be distinguished from the K_n test class in the other paper. [Theorems 1.4 and 1.8](https://arxiv.org/html/1907.03391v3).

To attack the published AH question with a finite ACUE tilt, one must first exhibit a positive law annihilating every required higher-order test, then construct and verify a stationary infinite limit. A derivative difference already visible in a protected moment rules out that specific route to such a tilt.

## 5. Full local GUE versus extreme gaps

Arias de Reyna and Rodgers prove an equivalence, in their zeta setting, between all-order GUE correlation convergence, point-process distribution convergence, and suitable joint spacing convergence. Their proof uses moment control. “Correlation convergence” there means all orders; it cannot be replaced by the pair conjecture alone. Conversely, their theorem prevents an overstatement that all-order local convergence fails to determine ordinary fixed local spacing distributions. [*On convergence of points to limiting processes, with an application to zeta zeros*, Theorem 2](https://arxiv.org/html/2311.13441v2).

Extreme-gap laws ask for additional control. Ben Arous and Bourgade prove the CUE/GUE smallest-gap laws through a thinned close-pair process and its factorial moments; uniform estimates are needed at the angular N^{-4/3} scale. This is stronger input than ordinary fixed-window pair convergence. Their paper does not prove a logical nonimplication theorem about actual zeta zeros. [*Extreme gaps between eigenvalues of random matrices*, Theorem 1.1 and §2](https://math.nyu.edu/~bourgade/papers/ExtremeGaps.pdf).

The companion `RARE_DEFECT_LOCAL_UNIVERSALITY.md` supplies an elementary model counterexample: one randomly located close-pair insertion preserves the complete fixed local sine limit, with a direct total-variation coupling estimate, but forces a much smaller global minimum gap. This sparse modification argument should be presented as a transparent obstruction, not as a claimed new major theorem.

## 6. Precise targets and exclusions

| Proposed target | What this lane supports | Remaining requirement |
|---|---|---|
| Complete finite pair data determine scalar-heat response/depth | Explicit counterexample, conditional on companion certificates | Exact algebra, positivity, and chosen flow normalization |
| Pair data plus full gap-histogram law determine that response | Sharper finite model counterexample | Verify the law-level tilt and derivative separation |
| All protected ACUE moments determine the same response | The displayed first derivative cannot separate such laws | Seek an observable/time derivative outside the protected algebra |
| The published Lagarias–Rodgers AH process is unique | A precise published question, not answered here | Preserve every relevant higher-order test; verify infinite limit |
| Exact full sine two-point function determines all higher correlations | No specialized counterexample established by this audit | Construct the exact stationary realization, with realizability proof |
| Full local sine universality forces the global CUE minimum-gap law | False for general model sequences; companion proof | Arithmetic or uniform rare-event assumptions for any zeta application |
| Montgomery–Dyson/GUE conjecture for actual zeta zeros | No proof or disproof obtained | New information about actual zeros beyond artificial models |

A targeted search did not locate the exact finite homometry-to-heat-depth separation in prior literature. That absence is insufficient to certify novelty. No claim about Wigner/Dyson Brownian motion universality is contradicted: those theorems carry stochastic dynamics and matrix hypotheses that these artificial deterministic spectra need not satisfy.

Postponed: exhaustive novelty search; all-order AH nonuniqueness; arithmetic embedding; infinite-volume heat-flow transport; any heat-depth conclusion from the rare-defect construction without a proved isolation/background estimate.
