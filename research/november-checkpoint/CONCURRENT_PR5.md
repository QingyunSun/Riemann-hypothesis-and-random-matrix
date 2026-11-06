# Read-only audit of the concurrent zeta triple experiment

Audited 6 November 2026 against PR #5 in QingyunSun/Riemann-hypothesis-and-random-matrix, pinned at commit `3b7687eb4a6be68c9093d997c473ebcf1331947e`. The branch is `feat/windowed-zeta-triples`, based on `codex/astra-research`. This is a separate concurrent experiment from the protected-survival counterexamples in PR #6.

## What the experiment adds

The experiment evaluates a specified distinct, ordered triple statistic on 2,031,052 published zeta ordinates. The two frequencies in unfolded coordinates are (1.2, 0.2, −1.4) and (−0.8, 0.2, 0.6). Their real triple sums are subtracted, with a Hann product weight on each spatial window and denominator ∫w³=5W/16. The difference has a pointwise zero identity on any translated exact half-grid. Thus it supplies an actual-zeta numerical observation of a statistic designed to separate lattice points from unitary correlations. It complements the finite-model existence theorem but does not measure heat collision times or exhibit an arithmetic estimate for them. [PR](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/pull/5)

The checked-in CSV contains 18 primary zeta means, all negative. For indices 1,000,001–2,001,052 they are approximately −0.441729, −0.443849 and −0.422252 at widths 10,20,40. The corresponding finite-rank CUE theoretical expectations are approximately −0.4. Near index 10²¹, the width-40 result changes from −0.580264 to −0.029794 when the window origin moves by half a width; the reported descriptive standard errors are 0.151727 and 0.134204. The CUE sampled width-40 mean is −0.351061 with SE 0.032417, within two SE of the theoretical control. These finite samples support a negative empirical sign much more directly than a limiting magnitude. [Pinned CSV](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/3b7687eb4a6be68c9093d997c473ebcf1331947e/research/experiments/windowed-triples/measurements.csv)

## Checks of the statistic and controls

The implementation correctly removes repeated indices. For a balanced triple with frequencies a+b+c=0, the coincidence i=j subtracts the second-power-weight trace at −c multiplied by the first-power-weight trace at c, with analogous terms for the other two coincidences. The +2∑w³ correction cancels between the two triples. The included test enumerates all ordered distinct triples and agrees with this fast formula.

The half-grid cancellation is termwise. The ratio of the two triple phases is exp(4πi(x_i−x_k)), which equals one when all coordinates belong to a common translate of ½Z. Arbitrary thinning and arbitrary weights attached to each ordered triple preserve this identity. This is stronger than a statement about the ACUE mean. The included thinning/translation test passes. [Pinned statistic](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/3b7687eb4a6be68c9093d997c473ebcf1331947e/research/experiments/windowed-triples/statistic.py)

The underlying phase is translation invariant because each frequency triple sums to zero. A change of window origin changes membership and weights, so the observed origin sensitivity is compatible with correct phase handling. The implementation shifts zeta window origins by W/2 and rotates each simulated matrix separately to avoid adjoining independent realizations.

The CUE expectation includes the same window weights and the finite rank 120. For these widths and modes the singleton integrals vanish, leaving the two oriented three-cycles of the determinantal correlation. The independent three-dimensional quadrature test agrees with the Fourier trace computation. The ACUE sampler uses the rank-120 projection kernel on 240 sites with iterative conditional projection; the real kernel is a gauge of the Fourier projection. Both control constructions are consistent with the stated finite models. [Pinned controls](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/3b7687eb4a6be68c9093d997c473ebcf1331947e/research/experiments/windowed-triples/controls.py)

## What windowing and AH still require

Before tapering, the first triple has total positive frequency 1.4 and the second 0.8. The first lies outside the usual protected budget of one. The compact physical-space Hann taper has unbounded Fourier support. At the fixed widths used here its tails persist, so a theorem restricted to the low-frequency region cannot simply be applied to the windowed statistic. The README states this limitation accurately.

The triple statistic also has size controlled by a third power of window occupancy. Passing from an asymptotic half-grid hypothesis to a zero expected score requires control of approximation errors and exceptional windows, with a suitable uniform-integrability or quantitative occupancy estimate. Removing the specified 1% of gap endpoints, the densest 5% of windows, and windows containing the flagged endpoints are useful checks of those particular finite deletions. They do not control an arbitrary asymptotic exceptional set. The README makes this distinction.

For a completely regular window containing K points within η of a translated half-grid, the phase identity and Lipschitz bound give |S_W| ≤ 128πη K(K−1)(K−2)/(5W). This elementary bound shows explicitly why a microscopic lattice-approximation estimate must be combined with occupancy control. It does not supply either estimate for zeta.

## Work actually performed

Read the six source/data files `statistic.py`, `test_statistic.py`, `controls.py`, `run.py`, `README.md` and `measurements.csv` from the pinned remote commit into a temporary audit directory. Ran all five existing unittest cases successfully in 0.017 seconds with single-thread numerical-library settings. Read the CSV independently to check the counts, means and reported origin sensitivity. No implementation discrepancy was found in this bounded inspection.

This audit did not download and rehash the raw Odlyzko data, repeat the full 2,400-matrix CUE Monte Carlo run, certify individual ordinates, or rerender the chart. It relies on the checked-in CSV for the empirical magnitudes. The tests validate the local statistic, theoretical control and specific invariants, rather than the provenance of the full recorded run. [Pinned tests](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/3b7687eb4a6be68c9093d997c473ebcf1331947e/research/experiments/windowed-triples/test_statistic.py)
