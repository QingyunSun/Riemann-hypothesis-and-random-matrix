# Root integration review: counterexamples and the November literature scan

Date: 2026-11-01 Pacific / 2026-11-02 UTC. Historical base: `ab174153a443ac747d7cb34a5352ce0441f6f895`. This is one bounded continuation on the existing research branch and PR. The previous September deadline is retained as historical context; the user explicitly renewed research.

## 1. Mathematical review boundary

The root read the complete pair-matched heat argument and its independent review, the rare-defect coupling proof, the stochastic filtration/character proof, the convolution-DPP examples and rigidity proof, and the three primary-source applicability audits. The clipped-Gram bridge was developed after the literature scan and separately challenged by the independent reviewer. These are ordinary mathematical arguments with internal reviews. They have not been checked by a proof assistant or externally refereed.

The principal mathematical scope controls are:

- Full finite pair matching does not determine scalar heat response, collision depth or every nonlinear Gram statistic. The positive ACUE perturbation preserves the complete pair/gap-summary law, but changes a protected mixed cubic moment. It therefore does not answer the all-order AH mimicry problem.
- The DBM theorem uses one positive/negative frequency budget across all times and the stated beta=2 generator. It does not protect an entire continuously observed path or identify stochastic flow with the deterministic zeta Newman flow.
- Sparse insertion preserves all fixed local sine limits but can change global extreme gaps. The construction does not prove a depth law or apply itself to actual zeta zeros.
- Full sine pair rigidity is restricted to the specified Hermitian convolution-DPP class. Its determinantal premise cannot be assumed from pair data.
- The active finite clipped-Gram kernel differs from the external zeta paper's Euclidean window. The latter's clipping is inactive on distinct half-lattice points at its chosen threshold. The two calculations are compatible.
- The exact cubic target lies outside the protected frequency range; its CUE value is not automatically the value of a localized zeta statistic.

The pinned external QRH, Chowla, GOE and local-smoothing statements are attributed to their manuscripts. The scan examined theorem hypotheses, selected proof mechanisms and the advertised Lean scope; it did not rebuild full external formalizations. The distinct-zero improvement has an imported computational certificate and analytic assumptions beyond the formalized finite layer. This record does not claim a new world record, a refutation of RH/AH/GUE, or a central signed arithmetic saving.

## 2. Reproduction actually completed

| Check | Recorded outcome | Scope |
|---|---|---|
| `pair-matched-flow/check_pair_matched_heat.py` | 4,704 small complement cases, exact witnesses, weights, root isolation and controls passed | Finite algebra and exact identities |
| Independent `AGENT_PAIR_CHECK.py` | 49 checks; root replay JSON equals saved output | Finite heat, orbit and DPP calculations |
| `stochastic-protection/check_stochastic_protection.py` | Six character eigenfunction identities passed | Exact finite Laurent identities; not the full analytic semigroup argument |
| `pair-matched-flow/check_clipped_gram.py` | Exact matrices, characteristic polynomials, root counts and negative control passed | Finite active/inactive clipping example |
| Independent `CLIPPED_GRAM_CHECK.py` | 19 checks; root replay JSON equals saved output | Independent exact Gram normalization |
| `CUBIC_TARGET_CHECK.py` | 80 mode cases and six target cases; root replay JSON equals saved output | Projection intersection counts |
| `verify_package.py` | Python parsing, local Markdown links, math syntax, receipt hashes and replay equality passed | Publication integrity; see `PACKAGE_CHECKS.json` for current counts |

The scripts use the repository's existing Python/SymPy and Node/KaTeX tools. No Rust code, benchmark, full historical archive rebuild, new Monte Carlo study or paid model harness was introduced. There is no speed or scaling claim to benchmark.

Two implementation-only failures were corrected before recording passing output. SymPy expression objects with different canonical forms initially failed structural equality despite algebraic equality; the checker now simplifies Hermitian differences and compares exact characteristic coefficients. The initial math-syntax check omitted display mode and rejected otherwise valid equation tags; it now preserves inline/display mode. Neither issue required changing the mathematical theorem or loosening numerical tolerances.

## 3. Source and review provenance

OpenAI materials are pinned to commit `4eaee87548250b2682affda7d05d947c05554bae`. The root's Exa search returned 23 candidate results across three targeted search requests; this number is not a count of independently verified theorems or the combined agents' entire search coverage. Each source audit records what was actually read.

Full third-party PDFs and source files remain in the adjacent local archive; public JSON receipts retain their URLs, byte counts and hashes. The RMT PDF/text relocation was checked byte for byte. The independent RMT audit's source-location sentence was updated after that move; its mathematical text was unchanged.

`REVIEW_ROOT_SYNTHESIS.md` pins the pre-expansion synthesis. Root subsequently applied its scope corrections and added the final literature findings and clipped-Gram bridge; the earlier review is not represented as covering that later entire text. The separate clipped-Gram review pins the final mathematical bridge and its checker. Earlier unpublished notes carrying a stale September date were corrected to the actual November audit date; historical published records were preserved.

The public repository manifest is refreshed only for the changed/new files in this slice, preserving all historical entries from the base manifest. This is a targeted hash update, not a claim of re-reading every large archived PDF from Dropbox. The delta receipt records the exact file set.

## 4. Delivery, risks and rollback

The changes consist of the new `research/counterexamples/` package, brief current-state/index/claim-log updates, and the targeted manifest delta. There is no production behavior or infrastructure migration. Ordinary proof review and exact finite checks leave the analytic-transfer and external novelty questions open.

Rollback consists of reverting this slice's commit. All prior research remains in the parent commit. Do not roll back unrelated later collaborator changes.

The next research slice should test an analytically admissible active Gram correction, a restricted signed small-prime graph transfer, or the explicitly normalized unprotected cubic statistic. Postponed work includes external seven-point interval-certificate replay, full Lean builds, a new complete PDF compilation, prime-gap parameter sweeps, and any global-conjecture claim unsupported by the missing arithmetic estimate.
