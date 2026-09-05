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
