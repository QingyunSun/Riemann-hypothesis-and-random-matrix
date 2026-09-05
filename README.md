# Riemann zeros and random matrices

Research workspace for Bill (Qingyun) Sun, GPT-6 Astra and Claude Code/Fable.

The main target is a genuine theorem about the relationship between Riemann zeta zeros and Montgomery–Dyson random-matrix statistics. Arithmetic resonance/correlation is the main route; deterministic heat-flow and finite counterexamples provide supporting results and adversarial tests.

Historical research and current collaboration remain available in [Alpha-devbox PR #11](https://github.com/galpha-ai/Alpha-devbox/pull/11). New results will be added through reviewable research branches and pull requests here. No proof of RH, GUE, AH refutation, or a sub-186 prime gap is claimed by this repository.

Every result must state its assumptions, proof status, primary references, reproducible evidence and remaining arithmetic gap. Historical instructions inside archived sources are records, not current execution instructions.

## Read the research

* [Current state](RESEARCH_STATE.md), [research log](research/RESEARCH_LOG.md), and [claim ledger](research/claims/CLAIM_LEDGER.md).
* [Round 12: test the remaining arithmetic gap](research/reports/dyson_round12.md). Actual-support positive sampling is sharp up to logarithms, a real-prime phase twist violates the 186 theorem's SW hypothesis, and centered Selberg upper norms leave the needed sign/precision open. These rule out specific shortcuts; no stronger prime bound is claimed.
* [Round 11: remove the shift-length loss under RH](research/reports/dyson_round11.md). The actual smooth discrepancy improves to X^1.023 log^5 X, with an independent source/proof audit. An explicit prime-modulus construction rules out a coefficient-only power saving for the full chosen family; the joint prime pairing remains open.
* [Round 10: a power saving for one actual shifted-prime discrepancy](research/reports/dyson_round10.md). Completing a fixed smooth shift packet saves at least X^.060333 over the per-shift triangle bound, with a complete proof and separate coefficient/kernel reviews. The resulting estimate still exceeds the zeta covariance scale. A primary-source variance audit identifies the remaining mixed-moment obligation.
* [Round 9: actual prime arithmetic and a failed two-prime interaction](research/reports/dyson_round9.md). Complementary moduli up to X^.523 control one selected divisor component; its sum across all shifts remains unestimated at the needed scale. Prime powers are removed with a uniform error bound, and the mesoscopic target is stated with explicit quantifiers. A new double-large-prime trial remains negative. All proofs, reviews and bounded replay results are retained.
* [Round 8: isolate the actual arithmetic remainder](research/reports/dyson_round8.md). An independently reviewed RH contour identity separates the two-scale target into an exactly evaluated short-prime main term and a signed energy of the same centered prime-counting error. The required residual lower bound remains unproved; exact scalar, endpoint and symbolic checks are preserved.
* [Round 7: two explicit actual-zeta targets for Dyson–Montgomery](research/reports/dyson_round7.md). A two-scale logarithmic-derivative mean square cancels AH's unknown diagonal parameter; a lower limit of at least 1/16 would refute AH-Pairs under RH. A separate compact Fourier test has an exact centered prime-covariance kernel. The required arithmetic inequalities remain open. Independent proof reviews, a negative large-prime-mark trial and a forward-flow obstruction are preserved together.
* [Detailed handoff and public historical archive](docs/handoff/ASTRA_PUBLIC_RESEARCH_HANDOFF.md) and [PDF](output/pdf/ASTRA_PUBLIC_RESEARCH_HANDOFF.pdf).
* [Fixed symmetric-prime arithmetic transfer](research/reports/symmetric_prime_arithmetic_transfer.md) and [independent review](research/reports/symmetric_prime_transfer_independent_review.md). The proof validates a fixed family; its currently certified margin remains negative.
* [Centered Gaussian pole correction and counterexample](research/reports/centered_gaussian_mixed_moments.md).
* [Complete finite arithmetic-operator experiments](research/reports/residual_gram_round2.md).
* [Scalar heat-flow proof](research/reports/yau_flow.md) and [quantitative audit](research/reports/galilean-proof-audit.md).
* [Protected dynamic trace theorem](research/reports/dynamic_generator.md) and [independent review](research/reports/dynamic_generator_independent_review.md).
* [Force-energy formulas](research/reports/force_energy.md) and [independent exact review](research/reports/force_energy_independent_review.md).
* [Collision/marked counterexamples and source correction](research/reports/new_attachment_bridge_audit.md).
* [Prime-gap certificate audit](research/reports/prime186.md) and [complementary-factorization frontier](research/reports/prime186_structural_frontier.md).
* [New certified positive restoration credit and k=39 optimization](research/reports/prime186_round4.md): the fixed k=40 margin improves to 24.86626 ppm using inherited baseline bounds; the gap remains 186. Optimized k=39 cap-only data remain below one.
* [Variable-radius exceptional bound and geometry search](research/reports/prime186_round5.md): exact source conditions and a uniform one-layer mesh repair accompany ten coarse trials and two refinements. No radius/plateau improvement was found; full restoration remains unevaluated.
* [Full signed cap operator and a direction beyond the old 77-dimensional space](research/reports/prime186_round6.md): an exact independence certificate accompanies a numerical gain of 71.42 ppm, to 0.99446782090. A separate process reproduces the fine-grid calculation; the quotient remains below one and arithmetic support restoration is outstanding.
* [Detailed Rounds 4-5 supplement](docs/handoff/ASTRA_ROUNDS_4_5_HANDOFF.md) and [59-page PDF](output/pdf/ASTRA_ROUNDS_4_5_HANDOFF.pdf): ten complete reports, including proof reviews, runtime validation, exact constants and failed searches, pinned to source checkpoint `c74b326`.
* [Pinned Fable mirror and provenance](fable/README.md).
* [One Fable computation packet](tasks/FABLE_SINGLE_SESSION_COMPUTE_TASK.md), prepared for manual delivery to the user's existing session. The earlier task was acknowledged and has F2 outputs; the newer packet has separate, unconfirmed receipt status.

The public handoff combines 48 source documents at checkpoint `055a4a0`; subsequent research is linked above and recorded in the current state and ledger. The historical papers retain known errors, explicitly corrected by the current audit. Neither their filenames nor their earlier status labels supersede the claim ledger.

## Reproduce and verify

The numerical scripts use Python with `numpy`, `scipy`, `sympy`, and `mpmath`. Some optional historical solvers need additional packages; they are not part of the bounded checks. The independent arithmetic identities and the rational certificate do not need a model API.

```text
python3 tools/verify_manifest.py
python3 tools/build_handoff.py
```

The following checks were run successfully in a **copy** of the research and historical folders. Most original experiment scripts write adjacent JSON files, so use a copy or isolated checkout when rerunning them; retain the original output before a new run.

```text
OPENBLAS_NUM_THREADS=1 python3 research/logs/audit_research.py
OPENBLAS_NUM_THREADS=1 python3 research/residual-gram/check_algebra.py
python3 research/residual-gram/rational_trial_certificate.py
python3 research/heat-flow/yau_flow_checks.py
python3 research/heat-flow/galilean_audit_constants.py
python3 research/centered-gaussian/centered_gaussian_pole_checks.py
python3 research/prime-gaps/minorant_geometry.py
python3 research/dynamic-generator/generator_audit.py
python3 research/dynamic-generator/dynamic_generator_independent_review.py
python3 research/force-energy/force_energy.py
python3 research/force-energy/force_energy_review.py
python3 research/bridge-audit/attachment_bridge_checks.py
python3 research/prime-gaps/prime186_frontier_checks.py
```

Original execution logs and the separate integration recheck logs are retained in `research/logs/`. Full eigensolver runs are optional and explicitly sized; they are not silently launched by these checks. The saved million-dimensional eigenvector supports the feature-fit reproduction. The optional ten-million-dimensional vector is retained in the adjacent local archive; its spectrum, residual, parameters and regeneration script are public.

To build the PDF, install the pinned Markdown/KaTeX dependencies with `npm ci --prefix tools/document-renderer`, and provide Playwright and Chromium. Then run:

```text
node tools/render_handoff.cjs
```

`PLAYWRIGHT_MODULE` may specify an installed Playwright module path; `PLAYWRIGHT_CHROMIUM_EXECUTABLE` may specify a browser binary. Otherwise the renderer uses ordinary module resolution and Playwright's installed browser. Input Markdown and output PDF can be supplied as its two positional arguments. The renderer saves math/overflow diagnostics under `tmp/`; final PDF validation is recorded with the research logs.

## Scope, limitations and rollback

This is a research archive with reproducible experiments, not a formally verified theorem library. Numerical eigenvalues are not rigorous upper bounds. Written proofs with internal review are labelled separately from exact finite certificates and open conjectures. No new prime-gap or zeta-gap record is claimed.

The prior sources remain pinned in `historical/`; new work stays on a research branch. Reverting the snapshot commits restores the bootstrap without rewriting history. Postponed work includes a proof-assistant formalization of completed lemmas, external novelty review, a positive half-gap certificate, and complete infinite-dimensional operator transfer. See [the architecture](docs/architecture.md) for file ownership and data flow.
