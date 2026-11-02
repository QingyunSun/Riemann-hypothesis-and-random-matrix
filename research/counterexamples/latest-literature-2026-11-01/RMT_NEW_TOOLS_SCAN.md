# Latest analytic and random-matrix tools: bounded primary-source audit

Date: 2026-11-01, America/Los_Angeles; retrieval completed 2026-11-02 UTC. Author: stationary-challenge agent. Repository snapshot: OpenAI `math`, commit `4eaee87548250b2682affda7d05d947c05554bae`.

This note audits statements and possible applicability. It is not an independent verification of the complete new proofs. The date in the earlier pair-review draft was corrected from stale inherited context; its mathematical contents were unchanged.

## 1. What was actually inspected

The [official catalogue at the pinned commit](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/overview.tex) was searched for random matrices, Dyson, eigenvalues, zeta, zero spacing, pair correlation, Dirichlet polynomials, restriction and smoothing. The directly relevant random-matrix family found was **219**, fixed-degree random regular graph universality and its weak-disorder extension. The main new general analytic family was **079**, Euclidean local smoothing; family **077** is the earlier three-dimensional positively curved restriction result.

No directly stated theorem on zeta GUE statistics, zeta ratios, higher zeta correlations or their Dyson evolution was identified in this bounded catalogue scan. This is a statement about the inspected catalogue summaries, not an exhaustive assertion about every lemma in its manuscripts.

The [official history](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/history.md) records the local-smoothing addition on October 26 and a separate Hodge formalization correction on October 29. The accompanying [October 26 announcement](https://openai.com/index/building-scientific-understanding-with-academic-communities/) describes the release as model-produced research material to be examined by mathematicians. Source PDFs and extracted text for the three manuscripts inspected here were moved, with byte verification, to the adjacent `Astra-Local-Archive/latest-literature-2026-11-01/rmt_sources/`. Public `rmt_sources/SOURCE_RECEIPT.json` records the exact source URLs and PDF hashes; `LOCAL_SOURCE_LOCATION.json` also records the extracted-text hashes. This source-location sentence was updated by root after the author's scan. The actual PDFs, rather than only their abstracts, supplied the theorem and method details below.

QRH and ordinary two-point Chowla are covered by the parallel `QRH_METHOD_AUDIT.md` and `CHOWLA_TRANSFER_AND_RESEARCH_DECISIONS.md`; they are not re-audited here.

## 2. The closest genuinely relevant RMT input: family 219

The [clean-model paper](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/paper.pdf), Theorem 1.1, states fixed-energy GOE convergence for uniform simple labelled d-regular graphs, for each fixed d at least 3 and energy strictly inside the Kesten–McKay band. It identifies the complete microscopic point-process law through Laplace functionals, with unfolding n times the Kesten–McKay density.

Sections 1.3 and 3–6 describe a useful mechanism: quantitative Gaussian moments of sampled eigenvector coordinates, controlled microscopic resolvent tails, reversible edge switches, continuous identities on a marked limiting process, Gaussian insertion, and fixed-energy Dyson Brownian relaxation. The order of limits is explicit: first graph size with a fixed number of marks, then increasingly many weak switches inside the limiting law. The Gaussian information is joint higher-order information, not merely pair correlation.

The [weak Anderson companion](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/fixed-energy-universality-weak-anderson-disorder-random-regular-graphs.pdf), Theorem 1.1, allows independent uniform diagonal potentials of sufficiently small fixed positive strength. The permissible strength depends on degree and distance from the clean spectral edges. Unfolding uses the positive density of states of the random infinite-tree operator. Its Sections 1.2 and 4–8 retain the environment-conditioned variance of Gaussian eigenvector marks, use potential resampling and finite-rank identities, and obtain GOE insertion only after averaging the sampled environments.

**What can transfer, and what cannot — our assessment.** The plausible reusable object is a marked point-process identity with a genuinely distribution-preserving finite-rank perturbation. Our pair-matched heat counterexamples explain why the required extra marks cannot be reconstructed from the complete pair law. A zeta transfer would require an arithmetic construction providing the relevant higher joint moments, a valid resampling identity, controlled resolvent tails, and correct normalization. No such construction is supplied by our existing notes or by the graph theorem. Moreover these papers have real-symmetric GOE symmetry; a zeta GUE argument needs the appropriate complex-symmetry version. Calling the zero evolution “Dyson-like” does not establish any of these hypotheses.

The pinned formalization manifest had no match for either family-219 manuscript title/path, and the guessed `lean/docs/219.md` did not exist. This supports only “no corresponding formalization identified in this scan”; it is not a proof that no relevant Lean result exists anywhere.

## 3. October 26 local smoothing: exact useful bounds and the transfer gap

The [October 25 manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf), released October 26, states in Theorem 1.1, for n at least 2, finite p at least 2 and epsilon positive,

\[
\|e^{-it|D|}f\|_{L^p(\mathbb R^n\times[1,2])}
\le C\|f\|_{W^{s,p}},\qquad
s=\max\{0,(n-1)/2-n/p\}+\epsilon.
\]

At p=2, epsilon can be zero. Theorem 1.2 gives the sharper annular form, with \(p_c=2n/(n-1)\),

\[
\|e^{-it|D|}\phi(D/N)f\|_{L^{p_c}}
\lesssim [\log(2+N)]^{2/p_c}\|f\|_{p_c}.
\]

Corollaries 9.3 and 12.1 give strict-range spherical/conic and paraboloid extension, respectively. Appendix E, Theorem E.1, treats a simple largest eigenvalue of a real symmetric matrix pencil with positive transverse Hessian, on a compact angular patch. This is a specified phase class, not an arbitrary oscillatory phase theorem. The method retains interference before taking a square and constructs a conserved current and auxiliary determinant energy.

The [official Lean scope](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/079.md) lists wave local smoothing and several consequences. Comparator challenges intentionally contain unproved reference statements; their `sorry` markers are not evidence that the separate solution contains those holes. We did not replay the Lean build or audit that complete development.

**Our assessment of arithmetic applicability.** A Dirichlet polynomial \(\sum a_n e^{it\log n}\) is not already a wave extension operator on a curved hypersurface. Its single-parameter logarithmic phases do not supply the dimension, transverse curvature, input norm, or spacetime averaging in these theorems. A legitimate reduction must exhibit these objects and account for discretization, interval lengths, cutoffs, and coefficient norms. No power saving for our signed Möbius/prime correlation follows merely by citing local smoothing.

The most plausible role is to improve an error bound after an arithmetic-to-curved-extension reduction has been proved. It cannot by itself identify the sign or nonzero main term of a cubic correlation. Even the stronger logarithmic annular estimate needs a quantitative transfer calculation; treating its logarithmic loss as an automatic gain over the R29/R30 bounds would be invalid. The previous family-077 restriction result need not be separately developed before this newer, more general wave input is tested against a concrete reduction.

## 4. Independent check of the proposed out-of-band cubic target

This is an exact finite RMT calculation, independently derived here from the projection-DPP determinant identity; no novelty claim is made. Let CUE have size N and ACUE occupy N of the 2N equally spaced sites with its usual rank-N Fourier projection law. Write

\[
p_k=\sum_j e^{ik\theta_j},\qquad I=\{0,\ldots,N-1\}.
\]

For CUE the frequency space is \(\mathbb Z\); for ACUE it is \(\mathbb Z/(2N)\). Let \(L(q)=|I\cap(I+q)|\). Expanding the logarithm of the DPP generating determinant to degree three gives, for \(a+b+c=0\), the third joint cumulant

\[
N-L(a)-L(b)-L(c)+J(a,b)+J(a,c),
\]

where \(J(a,b)=|I\cap(I+a)\cap(I+a+b)|\); changing all shift signs has no effect on the required counts. This is the three negative two-block traces plus the two oriented three-block traces. For \((a,b,c)=(m,m,-2m)\), all one-mode expectations vanish, so this cumulant equals the ordinary expectation \(\mathbb E[p_m^2\overline{p_{2m}}]\).

In fact, throughout the integer range \(N/2<m<N\), both triple intersections vanish. On the integer line their three translates span 2m>N. On the 2N-cycle the three successive gaps are m,m,2N-2m, all strictly smaller than N; hence the three marked sites cannot lie in an arc of length N-1. The pair counts are

| Projection space | L(m) | L(2m) | Cubic expectation |
|---|---:|---:|---:|
| Integers, CUE | N-m | 0 | 2m-N |
| 2N-cycle, ACUE | N-m | 2m-N | 0 |

Consequently, for N divisible by 5 and \(m=3N/5\),

\[
\boxed{\mathbb E_{\rm CUE}\frac1N\Re(p_m^2\overline{p_{2m}})=\frac15,
\qquad
\mathbb E_{\rm ACUE}\frac1N\Re(p_m^2\overline{p_{2m}})=0.}
\]

The normalization and signs proposed by the root investigator are correct. The positive and negative total frequency weights are both 2m=6N/5, outside the protected weight-N sector. Thus the precise frequency triple is (0.6,0.6,-1.2), not an unspecified “higher correlation.” Rotation averaging leaves it unchanged because the total frequency is zero.

This makes a clear arithmetic target: derive a suitably centered, localized and normalized zeta analogue of this cubic and prove the CUE value or another value incompatible with the half-grid model. One must retain repeated-index diagonals and window/centering terms in the explicit-formula translation; the raw finite trace is not automatically a factorial three-point statistic. None of the external papers inspected here proves that arithmetic identity. Pair-matched model counterexamples are useful for defining the missing information, while this target specifies information that actually lies beyond the protected range.

## 5. Definite outcome

The independent cubic normalization check is positive. The graph papers give a concrete example of obtaining universality from **higher marked information plus distribution-preserving perturbations**, which is more informative for the proposed Dyson route than a generic heat analogy. The local-smoothing paper provides stronger analytic bounds worth testing only after an explicit reduction is written. The scan supplied no theorem that closes our current actual-zeta signed-correlation gap, and no new zeta theorem is claimed.

`CUBIC_TARGET_CHECK.py` and its JSON output provide bounded exact count checks for the finite target. The analytic literature statements above are attributed published claims with stated hypotheses, not conclusions certified by that checker.
