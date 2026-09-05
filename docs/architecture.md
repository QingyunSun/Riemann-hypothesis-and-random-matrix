# Research archive architecture

This repository preserves a checkable mathematical programme with small, independently runnable experiments. It does not implement the Alpha-devbox agent controller.

* `RESEARCH_STATE.md`: the current objective, assignments and synchronization state.
* `research/RESEARCH_LOG.md`: chronological questions, results, failures and decisions supported by evidence.
* `research/claims/CLAIM_LEDGER.md`: authoritative claim scope and proof status.
* `research/reports/`: complete mathematical arguments and independent reviews.
* `research/prime-gaps/round4/`: outward lower-credit integrals, independent kernel/projection audits, k=39 cap matrices and coefficients, and the isolated corrected arithmetic-runtime record. Its external primary source paths are configurable; the full third-party numerical paper text is not duplicated.
* `research/residual-gram/`, `operator-bounds/`, `heat-flow/`, `centered-gaussian/`, `prime-gaps/`, `dynamic-generator/`, `force-energy/`, `bridge-audit/`: focused Python experiments with JSON outputs and original execution logs.
* `fable/overnight-2026-09-05/`: byte-for-byte public Fable snapshot, with its own provenance manifest and separate Astra intake reviews.
* `historical/riemann-rmt/`: pinned earlier public sources, preserved even when corrected by later audit.
* `docs/handoff/`: the detailed audited handoff and its current supplement.
* `output/pdf/`: the public rendered handoff.
* `tools/`: manifest validation and document assembly/rendering.
* `tasks/`: one bounded task for the user's existing Fable session.

The adjacent local folder `Astra-Local-Archive` contains user-supplied full context and optional large data. It is separate from Git. New mathematical reports, important results, scripts and hashes belong here; credentials and unrelated private conversations do not.

Python handles arithmetic and experiment orchestration; JavaScript handles Markdown/KaTeX PDF rendering. No Rust kernel is needed for this slice. A test of a computation is evidence about that computation, not an automatic formalization of its mathematical theorem.

The portable acceptance surface is: verify hashes; run the bounded algebra/certificate checks in a copy; rebuild the handoff; inspect PDF math and layout. Full eigenvalue sweeps are optional and explicitly sized. No dashboard, distributed orchestration, model-calling service or new paid session is introduced.
