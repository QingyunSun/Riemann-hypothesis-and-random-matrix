# Riemann zeros and random matrices

Research workspace for Bill (Qingyun) Sun, GPT-6 Astra and Claude Code/Fable.

The main target is a genuine theorem about the relationship between Riemann zeta zeros and Montgomery–Dyson random-matrix statistics. Arithmetic resonance/correlation is the main route; deterministic heat-flow and finite counterexamples provide supporting results and adversarial tests.

Historical research and current collaboration remain available in [Alpha-devbox PR #11](https://github.com/galpha-ai/Alpha-devbox/pull/11). New results will be added through reviewable research branches and pull requests here. No proof of RH, GUE, AH refutation, or a sub-186 prime gap is claimed by this repository.

Every result must state its assumptions, proof status, primary references, reproducible evidence and remaining arithmetic gap. Historical instructions inside archived sources are records, not current execution instructions.

## Read the research

* [Current state](RESEARCH_STATE.md), [research log](research/RESEARCH_LOG.md), and [claim ledger](research/claims/CLAIM_LEDGER.md).
* **[Complete takeover Markdown through Round 14](docs/handoff/ASTRA_COMPLETE_RESEARCH_CONTEXT_2026_09_05.md)** and **[705-page public PDF](output/pdf/ASTRA_COMPLETE_RESEARCH_CONTEXT_2026_09_05.pdf)**. The latest audited programme comes first, followed by the complete earlier archive and Rounds 4–5 supplement. The separate local edition has 753 pages and includes supplied private context.
* [313-page Rounds 6–14 supplement](output/pdf/ASTRA_ROUNDS_6_14_HANDOFF.pdf), [Markdown](docs/handoff/ASTRA_ROUNDS_6_14_HANDOFF.md), and [source index](docs/handoff/ROUNDS_6_14_ARCHIVE_INDEX.json): 69 complete reports and 297 individually verified source objects at checkpoint `2a9ec81`, including proofs, failed routes, independent reviews and precise next research obligations.
* [Round 26: the full actual-variance reduction and its accumulated constant](research/reports/dyson_round26.md). Under ordinary RH, the complete fixed variance is Z_T+2M+o(1), with a finite exact shift-dependent Mobius-prime covariance, both infinite tails and all scale errors paid. The global O(1) bound is inherited from the known variance bound; the strict improvement remains open. Complete independent derivations and reviews are preserved.
* [Round 25: joint main cancellation at the central scale and the actual Fourier remainder](research/reports/dyson_round25.md). Under ordinary RH, the fixed compact packet equals its exact Mobius-prime covariance plus o(1), including X=T²; the genuine zero core and remote Fourier tails are negligible. The intervening signed integral and strict variance target remain open. Complete independent proofs and primary-source audits are preserved.
* [Round 24: unrestricted nonprimitive removal, the exact Mobius-prime complement, and an excluded kernel family](research/reports/dyson_round24.md). The actual prime-power bound no longer needs the owner restriction; full cofactor centers and independent reviews retain the unbounded signed covariance. Exact zero margins are impossible throughout the specified finite compact-window family.
* [Round 23: actual shift completion, fixed-six centering and a growing arithmetic residual](research/reports/dyson_round23.md). Two true prime-packet components vanish in a specified upper-window range; fixed-modulus-six normalization is unconditional; a growing wheel preserves the actual variance and log-prime heat target under RH with explicit norm debts. Full independent reviews retain the unresolved strict signed correlation.
* [Round 22: remove linear and parity terms from the actual pair target](research/reports/dyson_round22.md). Ordinary PNT makes the full singleton correction negligible; unconditional odd-pair and parity estimates leave a precise signed expression on odd endpoints and even shifts. The inherited variance transfer uses RH, and its strict quadratic estimate remains open. Complete independent derivations and source reviews are preserved.
* [Round 21: exact arithmetic, Tauberian and log-prime heat targets](research/reports/dyson_round21.md). An unconditional finite truncation bound, RH full-height fixed-test equivalence and an actual-prime heat-energy formula lead to a precise signed prime-pair remainder. Its strict upper bound remains open. A substantive review correction proves the proposed all-shifts sub-square-root shortcut impossible; old versions and reviews remain preserved.
* [Round 20: an actual length-averaged variance and equivalent Bragg target](research/reports/dyson_round20.md). Under RH, a positive exponential length average is a probability average of the fixed actual-zero spectral bump, with upper limit A. Height regularity makes a strict variance deficit equivalent to a positive Bragg limsup; either would exclude AH, but neither is proved. Three separate single-length prime variances and all per-bin data are preserved as finite floating diagnostics.
* [Round 19: positive prime variance and uniform finite ACUE heat](research/reports/dyson_round19.md). A fully centered prime variance has an exact AH prediction and a conditional strict-deficit implication. A separate finite ACUE theorem produces a local Bragg deficit of order s² on a time interval independent of N. Complete reviews retain the missing actual-prime inequality and the missing initial-zeta flow transfer. A source-valid shift-dispersion audit leaves the full RH aggregate unchanged.
* [Round 18: the reflected trace and exact modulus normalization](research/reports/dyson_round18.md). The carrier-one gamma term is an explicit small trivial-zero correction, while nontrivial residues retain the unknown quadratic energy; the proposed large-carrier series actually diverges. Dense-factor support lemmas give a polylog completed coefficient norm at level X^.525, but exact inversion restores the original arithmetic weights. Independent reviews and a complete algebra replay are preserved.
* [Round 17: the sieve fluctuation loss and an exact quadratic packet](research/reports/dyson_round17.md). A fully centered short-interval cap still loses the needed scale. A double-zero compact packet gives an exact positive real-square/modulus-energy relation; reflected-zero residues and nonzero weight-derivative terms remain explicit. Neither yields the strict Bragg deficit.
* [Round 16: the frequency-two AH atom and an exactly finite prime packet](research/reports/dyson_round16.md). RH supplies a sharp translated-bump upper bound that AH saturates; a strict deficit would exclude AH. The actual centered prime kernel is valid around logarithmic scale T². A separate nonnegative time packet has exact compact Fourier support and a finite signed prime sum. Complete proofs and independent reviews retain the missing strict inequality.
* [Round 15: an exact signed arithmetic target and a pole-canceling packet](research/reports/dyson_round15.md). The actual Vaughan remainder has a proved untwisted SW coefficient and explicit uncovered ranges. A nonnegative Gaussian time packet cancels the zeta simple pole, with its leading signed Fourier cost and all endpoint terms retained. Both are independently reviewed; the full zeta inequality remains open.
* [Round 14: an actual Type I removal and a quantitative CUE heat theorem](research/reports/dyson_round14.md). The specified short-divisor component is o(X log X) unconditionally; a finite CUE background bound yields relative heat-depth error O_p(N^(-2/3)). Both have complete proofs and independent reviews, with no zeta transfer.
* [Round 13: extract a rational core and retain the signed remainder](research/reports/dyson_round13.md). Ordinary RH gives an actual rational-core replacement error X^.923 log²X; its main term remains. A real-prime positive subsum and an exact CRT norm identity identify where cancellation is still needed.
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
* [Fable 2073028 repair audit](fable/reviews/pr11-2073028/INTAKE_REVIEW.md): corrected F1 coefficient and cutoff scaling; a proved finite mass-cutoff Fock bound; remaining general-beta and arithmetic-limit gaps. A separate 160-file source snapshot remains verbatim.
* [Pinned Fable mirror and provenance](fable/README.md).
* [One Fable computation packet](tasks/FABLE_SINGLE_SESSION_COMPUTE_TASK.md), prepared for manual delivery to the user's existing session. The earlier task was acknowledged and has F2 outputs; the newer packet has separate, unconfirmed receipt status.

The earlier public handoff combines 48 source documents at checkpoint `055a4a0`. The complete archive adds the ten-report Rounds 4–5 supplement and the 69-report Rounds 6–14 supplement, preserving each volume's source checkpoint and pagination. The historical papers retain known errors, explicitly corrected by the current audit. Neither their filenames nor their earlier status labels supersede the claim ledger.

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

To rebuild the later supplement and the public complete archive, run:

```text
python3 tools/build_round6_14_handoff.py
python3 research/logs/round6-14-handoff/check_source_coverage_euclid.py
node tools/render_handoff.cjs docs/handoff/ASTRA_ROUNDS_6_14_HANDOFF.md output/pdf/ASTRA_ROUNDS_6_14_HANDOFF.pdf
python3 tools/build_complete_handoff.py
```

`build_complete_handoff.py --include-local` additionally combines the private edition when its earlier local source files are present. `inspect_pdf_pages.py` renders every page and screens blank bodies and bounds; it requires human visual review. `check_merged_pdf.py` compares every merged page with its indexed source image and records even single-pixel differences for review. The final receipt, source coverage check and visual reviews are in `research/logs/round6-14-handoff/`.

## Scope, limitations and rollback

This is a research archive with reproducible experiments, not a formally verified theorem library. Numerical eigenvalues are not rigorous upper bounds. Written proofs with internal review are labelled separately from exact finite certificates and open conjectures. No new prime-gap or zeta-gap record is claimed.

The prior sources remain pinned in `historical/`; new work stays on a research branch. Reverting the snapshot commits restores the bootstrap without rewriting history. Postponed work includes a proof-assistant formalization of completed lemmas, external novelty review, a positive half-gap certificate, and complete infinite-dimensional operator transfer. See [the architecture](docs/architecture.md) for file ownership and data flow.
