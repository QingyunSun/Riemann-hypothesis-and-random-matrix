# Riemann zeros and random matrices

Research workspace for Bill (Qingyun) Sun, GPT-6 Astra and Claude Code/Fable.

The main target is a genuine theorem about the relationship between Riemann zeta zeros and Montgomery–Dyson random-matrix statistics. Arithmetic resonance/correlation is the main route; deterministic heat-flow and finite counterexamples provide supporting results and adversarial tests.

Historical research and current collaboration remain available in [Alpha-devbox PR #11](https://github.com/galpha-ai/Alpha-devbox/pull/11). New results will be added through reviewable research branches and pull requests here. No proof of RH, GUE, AH refutation, or a sub-186 prime gap is claimed by this repository.

Every result must state its assumptions, proof status, primary references, reproducible evidence and remaining arithmetic gap. Historical instructions inside archived sources are records, not current execution instructions.

## Read the research

* [Current state](RESEARCH_STATE.md), [research log](research/RESEARCH_LOG.md), and [claim ledger](research/claims/CLAIM_LEDGER.md).
* [Detailed handoff and public historical archive](docs/handoff/ASTRA_PUBLIC_RESEARCH_HANDOFF.md) and [PDF](output/pdf/ASTRA_PUBLIC_RESEARCH_HANDOFF.pdf).
* [Fixed symmetric-prime arithmetic transfer](research/reports/symmetric_prime_arithmetic_transfer.md) and [independent review](research/reports/symmetric_prime_transfer_independent_review.md). The proof validates a fixed family; its currently certified margin remains negative.
* [Centered Gaussian pole correction and counterexample](research/reports/centered_gaussian_mixed_moments.md).
* [Complete finite arithmetic-operator experiments](research/reports/residual_gram_round2.md).
* [Scalar heat-flow proof](research/reports/yau_flow.md) and [quantitative audit](research/reports/galilean-proof-audit.md).
* [Prime-gap certificate audit](research/reports/prime186.md).
* [One Fable computation packet](tasks/FABLE_SINGLE_SESSION_COMPUTE_TASK.md), prepared for manual delivery to the user's existing session. No receipt or completion is assumed.

The public handoff combines 32 source documents. The historical papers retain known errors, explicitly corrected by the current audit. Neither their filenames nor their earlier status labels supersede the claim ledger.

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
