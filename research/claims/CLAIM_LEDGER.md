# Claim ledger

The classifications below apply to the exact stated scope. “Proof with internal review” means a written mathematical proof and a recorded human-readable audit; it does not mean a Lean kernel has checked it or external referees have accepted it. Historical files may use stronger wording than this ledger.

| ID | Claim | Status | Evidence and remaining obligation |
|---|---|---|---|
| AUD-001 | Independent historical audit has 21 passing checks | Reproduced finite checks | `research/logs/audit_results.json`; not a blanket theorem audit |
| AUD-002 | Original verifier has 39 pass, 4 fail, 1 skip | Recorded run | `research/logs/verify-codex-original.log`; zero process exit does not erase failures |
| ALG-001 | Fixed-support approximator is saturated | Exact algebra | `research/reports/residual_gram_round1.md`; says nothing about larger support |
| NEG-001 | Sparse longer tails under the stated coefficient bounds cannot supply constant energy | Proof in report | Same report; hypothesis on coefficients is essential |
| NUM-001 | Degree-14 half-gap trial has margin about -0.01535798 | Numerical optimization | `research/residual-gram/variational-results.json`; no global optimality claim |
| CERT-001 | Fixed rational trial has margin in (-.01467,-.01465) for the stipulated integral | Exact rational certificate | `research/residual-gram/rational-trial-certificate.json`; transfer is separate |
| ARITH-001 | Fixed symmetric-prime family has that arithmetic limiting form | Written proof, independent internal review | `research/reports/symmetric_prime_arithmetic_transfer.md`, `symmetric_prime_transfer_independent_review.md` |
| NUM-002 | Full finite operator remains below pi²/2 through L=10⁷ | Numerical eigenvalue data | `research/operator-bounds/extended-arithmetic-results.json`; no asymptotic upper bound |
| NUM-003 | Structural features nearly recover the L=10⁶ optimum | Numerical fit and full-form evaluation | `research/operator-bounds/eigenvector-feature-results.json`; finite L only |
| NEG-002 | Tested Schur–Volterra majorant is too large to prove the target barrier | Numerical diagnostic of an explicit bound | `research/reports/residual_gram_round2.md`; not a certified optimum over all profiles |
| FOCK-001 | Fixed prime-bin compression provides a constructive limiting lower bound | Proof draft | Same report; not full operator convergence or an upper bound |
| NEG-003 | Centered Gaussian pole term cannot be dropped in a uniform long-support estimate | Analytic counterexample, primary review | `research/reports/centered_gaussian_mixed_moments.md`; RH for the contour identity |
| NEG-004 | Nonnegative Fourier transform cannot coexist with a zero at the origin for a nonzero Schwartz weight | Elementary proof | Same report; does not rule out quantitative subtraction |
| HEAT-001 | Isolated-pair first collision satisfies D ~ δ²/8 under δ²B→0 | Proof draft with internal audits | `research/reports/yau_flow_galilean_refinement.md`; quantitative second-pass audit in `galilean-proof-audit.md`; K=16384, eta0=1/524288 |
| RMT-001 | Circular positive-integer-beta extreme gaps induce the stated first-collision law | Proof draft with internal review | `research/reports/yau_flow.md`; published gap laws are inputs; novelty audit incomplete |
| PRIME-001 | A 39-element admissible tuple has diameter 182 | Exact finite verification | `research/reports/prime186.md`; DHL[39,2] is not proved |
| PRIME-002 | Fixed prime-sieve minorant mass has the saved rational enclosure | Exact rational computation plus separate coverage check | `research/prime-gaps/minorant_mass.json`, `minorant_geometry.json` |
| OPEN-001 | μζ < 1/2 under RH | Open in this programme | No positive applicable certificate |
| OPEN-002 | New fixed-width Montgomery pair-correlation theorem beyond known support | Open in this programme | No new arithmetic mixed-term theorem supplied |
| OPEN-003 | Prime-gap bound below 186 | Open in this programme | No improved admissible-tuple/sieve certificate chain |
| OPEN-004 | RH, full GUE statistics, general-beta depth universality | Open here | Not implied by any local counterexample or finite computation |

All paths are relative to the repository root. The public reports contain the derivations; the JSON files preserve values and parameters. Run logs are snapshots, not machine proofs. Updates should change this ledger and the associated report together.

## Round 3 and incoming collaboration

| ID | Claim | Status | Evidence and remaining obligation |
|---|---|---|---|
| DYN-001 | All protected symmetric trace moments agree under forward deterministic circular flow | Written proof with independent internal review | `research/reports/dynamic_generator.md`; m<=N, all orders and all t>=0, not postcollision attractive dynamics |
| FORCE-001 | Force-square expectations differ by a factor of two, with exact dissipation formulas | Written proof with independent internal review | `research/reports/force_energy.md`; finite CUE/ACUE, singular two-point information |
| BRIDGE-001 | Initial smallest gap need not collide first | Exact rational counterexample and Sturm certificate | `research/bridge-audit/attachment_bridge_checks.json`; lower bound survives; pair-selection correction required |
| BRIDGE-002 | Marked inverse blowup need not force marked-depth derivative blowup | Exact symbolic counterexample | Same certificate; paired isospectral 2x2 matrices, no fixed-norm-along-path claim |
| SOURCE-001 | LR explicitly suggests a .606894 hard-core upper bound | Primary-source correction | `research/reports/new_attachment_bridge_audit.md`; not proved in the cited passage |
| RITZ-001 | Two-dimensional finite residual correction improves the fixed trial | Reproduced finite calculation | `research/operator-bounds/ritz_residual_diagnostic.json`; half-gap margin remains negative; no automatic continuum transfer |
| PRIME-003 | Complementary root predicates yield a finite allocation frontier | Exact algebra and rational feasibility certificates | `research/reports/prime186_structural_frontier.md`; fixed active row/template; not a global sieve obstruction or a new gap |
| FABLE-001 | Earlier FABLE_001 pickup and numerical output exist | Pinned public-source evidence | `fable/PICKUP_RECEIPT.json`; final arithmetic report absent; no receipt inferred for newer packet |

## Round 4: actual restoration credit and finite-family diagnosis

| ID | Claim | Status | Evidence and remaining obligation |
|---|---|---|---|
| PRIME-004 | One true failure rectangle gives positive normalized credit exceeding 1.5058119471 ppm | Outward integral, independent mathematical review and identical separate-process rerun | `research/reports/prime186_round4.md`; k=40 fixed step trial, 53 coherent signed terms; no gap reduction |
| PRIME-005 | Complete fixed-k=40 margin improves from 23.36045 to 24.86626 ppm | Exact scalar combination of new lower credit with inherited published endpoints | Same report and `research/prime-gaps/round4/prime-credit/alpha_credit_margin_replay.json`; original 149 upper forms not recomputed here |
| RESTORE-001 | Exact projected-marginal and signed-residual restoration identities hold | Written proof and independent finite signed diagnostics | `research/prime-gaps/round4/restoration-proof/RESTORATION_PROOF_AUDIT.md`; new weighted residual integrals still needed; alternative lower bounds cannot be added together |
| NUM-004 | Full77 k=39 cap-only Ritz candidate directly evaluates near 0.99439639936 | Floating optimization with matrix/independent scalar comparison | `research/prime-gaps/round4/k39-trial/REPORT.md`; Gram condition number about 2.28e10; no strict family upper bound or restored criterion |
| AUD-003 | Corrected isolated FLINT passes the original signed regression and relevant native suites | Source-built upstream fix and recorded tests | `research/prime-gaps/round4/repro-flint/README.md`; full binding suite has a separate Jacobi contract assertion; no universal library-verification claim |

## Round 5: radius-dependent constants and bounded geometry search

| ID | Claim | Status | Evidence and remaining obligation |
|---|---|---|---|
| PRIME-006 | The original exceptional-square estimate extends to the explicit radius interval with a recomputed constant | Ordinary written derivation and exact rational certificates | `research/prime-gaps/round5/exceptional-radius/EXCEPTIONAL_RADIUS_EXTENSION.md`; canonical fixed-profile class, all roots bounded, original global prime cap, no new distribution theorem |
| PRIME-007 | Twelve of fifteen natural cap templates satisfy the audited source conditions; a one-layer trim repairs the row-39 mesh issue uniformly over [0.272,0.278] | Exact arithmetic and sufficient-template proof | `research/prime-gaps/round5/geometry-audit/GEOMETRY_SOURCE_AUDIT.md`; new failure covers and physical integrals remain uncomputed |
| NUM-005 | Ten coarse radius/plateau trials and two fine refinements give no geometry improvement over the original k=39 point | Saved floating cap-only searches and matrix/vector checks | `research/reports/prime186_round5.md`; untrimmed supports, ill-conditioned matrices, no rigorous family upper bound or global no-go theorem |
| AUD-004 | Three bounded Round 5 replay scripts reproduce their exact outputs, and all twelve saved matrices match their thirty-six candidate witnesses | Independent integration replay | `research/logs/round5-integration/recheck.json`; metadata exclusions stated; no fresh full integral or eigenvalue sweep |

## Round 6: full signed cap operator and a new radial direction

| ID | Claim | Status | Evidence and remaining obligation |
|---|---|---|---|
| PRIME-008 | The fixed cap functional is represented by a bounded self-adjoint signed operator on the actual fragment-measure space | Written derivation and independent internal audit | `research/prime-gaps/round6/operator-proof/FULL_SIGNED_CAP_OPERATOR.md`; true arithmetic support uses a different projected operator and denominator |
| ALG-002 | For h=P_V(I−P_U)Tf and w=(I−P_U)h, the mixed form equals ||h||², with nonnested projections | Exact identity, rational signed-model checks | `research/prime-gaps/round6/residual-audit/SIEVE_RESIDUAL_AUDIT.md`; the normalized coupling is ||h||²/||w|| for unit f; numerical projection errors remain separate |
| CERT-002 | The frozen new radial function is outside the old trial space, whose extension has dimension 78 | Exact rational support checks, polynomial-root argument and modular-rank certificate | `research/prime-gaps/round6/operator-diagnostic/outside_span_certificate.json`; proves independence, not a distance or Rayleigh-value enclosure |
| NUM-006 | The new 78-dimensional cap trial directly evaluates at 0.994467820900683, approximately 71.4215 ppm above the old trial | Floating optimization, tilt/cutoff controls, independent fine replay | `research/reports/prime186_round6.md`; still below one, ill-conditioned Gram, no interval gain certificate or arithmetic restoration |
| AUD-005 | Exact model checks, saved-output checks and one fine-grid radial-residual calculation reproduce their recorded outputs | Independent integration replay | `research/logs/round6-integration/recheck.json`; not a proof of full residual norm, missing-energy bound or smaller prime gap |
