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

## Round 7: actual-zeta reductions and arithmetic/dynamical tests

| ID | Claim | Status | Evidence and remaining obligation |
|---|---|---|---|
| ZETA-RED-001 | RH+AH-Pairs implies the stated two-scale zeta logarithmic-derivative mean square tends to W_AH=0.0623924179764985... | Ordinary reduction with two internal reviews | `research/dyson/round7/poisson-resolvent/TWO_SCALE_ZETA_TARGET.md`; handles nonconvergent P_0(T), endpoints, tails and Gamma/holomorphic-square terms; no actual arithmetic lower bound or novelty claim |
| CERT-003 | W_AH<0.06240<1/16, with certified strict gap greater than 0.00010 | Exact Fraction enclosure and separate coordinator certificate | Same folder, `two_scale_certificate.json` and `coordinator_threshold_1_16_check.json`; an RH-dependent liminf bound of 1/16 would refute AH-Pairs, but is not proved |
| ZETA-RED-002 | The fixed compact Fourier bump has AH target 7/10; its centered prime-covariance remainder has AH target -3/5 | Source-backed reduction and exact kernel expansion | `research/dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md`; the new covariance estimate remains open; finite kernel normalization is not an asymptotic theorem |
| ARITH-002 | The fixed binary large-prime mark has the stated arithmetic limiting forms for fixed polynomial coefficients | Ordinary arithmetic proof with independent internal review | `research/dyson/round7/arithmetic-resonator/DERIVATION.md` and `INDEPENDENT_REVIEW.md`; full n>=1 measure before restriction, short-background limit and same-prime insertion specified; no growing-family uniformity |
| NUM-007 | One new 30-feature trial has limiting half-gap margin about -0.01465492379421; its fixed rational vector is also negative on finite integer operators through L=10^6 | Floating quadrature and integer-operator evaluation, independently replayed | Same folder; three quadrature orders agree but no interval enclosure, finite-family upper bound or actual zero data is supplied |
| FLOW-001 | Ordered repulsive systems with the stated decreasing common field have gap-independent contraction; a bounded-discrepancy deterministic half-grid family retains hard core 1/2 under forward flow | Ordinary derivation, exact algebra and force calibration | `research/dyson/round7/true-zeta-flow/FORWARD_FLOW_OBSTRUCTION.md`; actual H_t boundary propagation and removal of stochastic smoothing are missing |
| AUD-006 | Nine Round 7 output files and the order-40 matrix arrays reproduce in an isolated replay | Separate-process integration check | `research/logs/round7-integration/recheck.json`; excludes timing fields only, original evidence unchanged; does not certify either missing zeta inequality |

## Round 8: actual short-prime projection and centered residual

| ID | Claim | Status | Evidence and remaining obligation |
|---|---|---|---|
| ZETA-RED-003 | Under RH, the actual logarithmic-derivative mean square equals its short-prime diagonal plus residual norm squared and O_c(N log^4 T), with N=floor(T/log^6 T) | Ordinary analytic proof and independent review of final draft | `research/dyson/round8/resolvent-arithmetic/SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md`; fixed c>0, all sufficiently large T, no growing-c uniformity or new zeta lower bound |
| ARITH-003 | The residual has the displayed absolutely convergent centered-psi continuation; its pole may be removed from normalized energy with O_c(log^-3 T) error | Ordinary RH-dependent continuation and norm bounds, independently reviewed | Same folder; exact endpoint includes the atom at N; both scales use one common arithmetic error function; the signed comparison is unproved |
| CERT-004 | The short-prime two-scale main term B lies strictly in (0.45609397932923,0.45609397932924) | Exact rational scalar enclosure | Same folder, `check_centered_tail.json`; the sufficient target liminf E_T>=1/16-B remains open |
| POS-001 | The displayed band-limited minorant gives the exact weak bound near -0.208674513 under the stated pair-measure assumptions | Ordinary proof, independent Fourier-pairing review and thirteen exact symbolic checks | `research/dyson/round8/spectral-positivity/`; optimum only in the specified one-parameter family; does not reach 1/16 or claim a new actual-zeta estimate |
| AUD-007 | Both Round 8 result JSON files reproduce exactly, and eight rational cutoff cases verify the Stieltjes endpoint convention | Isolated integration replay | `research/logs/round8-integration/recheck.json`; no excluded fields, parameter scan or large-T zeta computation |


## Round 9: complementary moduli, genuine primes and the first edge correction

| ID | Claim | Status | Evidence and remaining obligation |
|---|---|---|---|
| ARITH-004 | Selected Mobius–log divisor correlations on complementary moduli up to X^.523 have per-shift error O_A(X log^(-A)X) | Application of the cited ordinary distribution theorem, independently reviewed | `research/dyson/round9/factorization-covariance/`; uniform coherent residues and smooth weights; full H-shift packet is not controlled at scale X log X |
| ARITH-005 | Under RH the selected aggregate equals its explicit progression discrepancy plus O(H sqrt(X) log^4 X) | Ordinary proof with independent review | Same folder, Eq22; error is o(X log X) on H<=X^(2/7), but the discrepancy, complementary divisors and other covariance terms remain open |
| ARITH-006 | The fixed two-large-prime interaction has the stated arithmetic moment and insertion limit | Ordinary fixed-family extension with independent root review | `research/dyson/round9/multiplicative-profile/DERIVATION.md` and `INDEPENDENT_REVIEW.md`; relies on reviewed fixed-moment/Schur inputs, not a general Fock limit |
| NUM-008 | The new 30-feature interaction has floating margin -0.0146549114371551; the frozen L=100000 integer trial is also negative | Deterministic quadrature, finite checks and independent exact-array replay | Same folder; small matched-baseline gain is not interval-certified, and the trial is worse than the historical 48-feature best |
| ARITH-007 | Prime-power tail energy is at most O(T N^(-1/3) log^4(2N)+delta^(-4)); replacing the RH residual by its genuine-prime continuation changes normalized energy by o(1) | Elementary ordinary proof and independent review, with growing-width corollary | `research/dyson/round9/prime-power-removal/`; uniform amplified error O(b² e^(2b) a_T)=o(1) on b=o(log log T); no lower-bound gain |
| ZETA-RED-004 | The coupled mesoscopic residual has sine target zero and AH target -3/4; a stated uniform strict lower bound would refute AH-Pairs under RH | Source/rate audit, exact algebra and independent quantifier review | `research/dyson/round9/mesoscopic-edge/`; existential slow diagonal only, no prescribed AH convergence rate or proved arithmetic edge estimate |
| AUD-008 | Five Round 9 output JSON files and the fresh q32 full M/G arrays reproduce | Separate-process bounded integration replay | `research/logs/round9-integration/recheck.json`; excludes timing and temporary source paths only; q20 retained matrices are checked but not recomputed |


## Round 10: smooth completion of the actual shift sum

| ID | Claim | Status | Evidence and remaining obligation |
|---|---|---|---|
| ARITH-008 | A specified smooth shift packet of the actual selected discrepancy is O(sqrt(H X (X+Q²)) log^4 X), Q=X^.523 | Unconditional ordinary proof with separate coefficient/spacing and actual-kernel reviews | `research/dyson/round10/shift-average/`; saves a power over accumulating the source per-shift estimate, but remains above X log X; full sharp packet and complementary terms are not evaluated |
| AUD-009 | The checked Guth–Maynard count range and RH variance comparisons do not directly supply shrinking-edge fluctuation precision | Bounded primary-source audit with independent review | `research/dyson/round10/arithmetic-residual/`; includes the source's fixed-epsilon improvement remark; not a universal literature or method obstruction |
| ZETA-RED-005 | A stated uniform genuine-prime logarithmic mixed-moment bound with deficit coefficient below two implies a strict gap above -3/4 in the coupled statistic | Conditional calculus lemma with reviewed actual-residual differentiation and quantifiers | Same folder; M_T>=s^-2-(2-epsilon)s^-3+o(s^-3) remains unproved |
| AUD-010 | Both Round 10 exact-check JSON outputs reproduce | Separate-process integration check | `research/logs/round10-integration/recheck.json`; 9615 Ramanujan cases and scalar implications, with only two temporary source paths excluded; not a numerical proof of the analytic bound |


## Fable intake at 89393d5: source receipt and review status

- **Verified provenance:** 141 public research files preserved verbatim; older 81-file mirror unchanged.
- **Exact correction:** Pi4 leading coefficient is 6a, hence m4=a^2+6a. The source refuter's -zz3 probe has the wrong sign; this was reproduced and corrected separately.
- **Bounded numerical replay:** ten refuter flags match, including three failed narrative assertions. Insertion values agree within 8.33e-17; this is floating verification, not a formal certificate.
- **Not accepted as written:** CUE uniform constants 1054/1055; general-beta BB-LD scaling and its claimed consequences; one-point-to-selected-pair density inference; unconditional periodized-zeta gap inference. See the separate review for the limited possible constant repair and missing hypotheses.
- **Still conditional:** a depth conclusion needing flow-window stability or H_C; arithmetic rate extrapolations from finite drift.
- **Unchanged:** the independently reviewed Astra fixed-family arithmetic limit remains valid and its certified trial margin negative. No new zeta-gap, AH-refutation, GUE or prime-gap theorem follows.


## Round 11: RH component estimate and exact remaining arithmetic scope

- **Ordinary proof under RH, independently reviewed:** the specified actual smooth discrepancy satisfies O(sqrt(X(X+Q^2)) log^5 X), Q=X^.523. This removes sqrt(H) from Round 10. The assumption change is explicit; no novelty claim for classical small-arc methods.
- **Ordinary PNT construction, independently reviewed:** on the full canonical complementary family, fixed nonnegative V gives completed coefficient squared mass >=c_V H/log^348 X (log-weight version log^-346). All actual squarefree prime products satisfy the guards. This excludes a fixed-power saving for that coefficient norm only.
- **Ordinary RH identity, independently reviewed:** M_T(b)=b^(-2)+2b^(-3)+B_T(b)+o(b^(-3)) uniformly on the stated slow range, with all centered terms combined. The pole and cutoff errors are quantified.
- **Exact finite checks:** rational exponents/counting constants, 384 arc counts and 2901 unique frequency memberships reproduce. They do not prove RH, PNT or the analytic source lemma.
- **Open:** an arithmetic bound at X log X, full sharp covariance, joint prime/coefficient cancellation and the strict lower bound on B_T. No new actual-zeta pair-correlation, gap, AH-refutation, GUE or sub-186 theorem.

Evidence: `reports/dyson_round11.md`, the complete author/reviewer records in `dyson/round11/`, and `logs/round11-integration/`.


## Round 12: specific arithmetic shortcuts fail

- **Ordinary proof, independently reviewed:** actual canonical support forces positive local sampling constant >=c Q^2/log^348 X, even for artificial integer-frequency packets obeying the known arc envelopes. The analogous specified absolute-weight operator has its stated lower bound. This is not a lower bound for actual prime concentration or the full signed functional.
- **Ordinary prime-arithmetic counterexample, independently reviewed:** at legal source scales and conductors, an additive twist of a prime-interval SW coefficient has modulus-3 discrepancy (i sqrt(3)/4+o(1))N/log N. Therefore direct phase absorption does not inherit SW. The source theorem is not contradicted; averaged phase treatment remains open.
- **Ordinary support count, independently reviewed:** the primitive-filtered shift interval has full local unit images, so the product-local residue lift costs phi(d)~d on the constructed family. Also H is below the source's permitted short-factor scale. These are failed applications, not a general dispersion impossibility.
- **Insufficient RH estimate, independently reviewed:** centered Selberg--Gallagher gives only the recorded weak one-sided mixed bound; stronger known global estimates are retained separately and still do not supply the required signed shrinking-shell coefficient in the proposed use. No optimality of RH norm bounds is claimed.
- **Exact replay:** 60 signed-kernel identities, rational constants/source inequalities and six modular-selection cases pass. No large numerical prime realization.
- **Unchanged:** strongest actual component bound X^1.023 log^5 X under RH; all target zeta/RMT lower inequalities and famous conjectures remain open.

Evidence: `reports/dyson_round12.md`, `dyson/round12/INDEPENDENT_ROOT_REVIEW.md`, and `logs/round12-integration/`.
