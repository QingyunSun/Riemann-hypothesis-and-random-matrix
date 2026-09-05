# Research log: recoverable mathematical work

This log records problems, mathematical arguments, calculations, corrections, and evidence. It is a public research record, not a transcript of private model deliberation. Detailed proofs and counterexamples live in the linked reports. Timestamps record checkpoints; they do not imply continuous computation between checkpoints.

## 2026-09-05: source recovery and independent audit

**Question.** Which statements in the earlier ACUE, Newman-depth, zeta and prime-gap programme survive direct checking?

**Input.** Historical base `ee61fba38925190916e556f87bc1ea83a502413e`; Fable handoff update `0f86c31d847178f0a774f70073ddc44206b32f98`; user-provided mathematical context and original Inoue probe. The public historical source is preserved in `historical/riemann-rmt/`; private supplied context and conversation exports remain in the adjacent local archive.

**Outcome.** The original verification script reports 39 PASS, 4 FAIL, 1 SKIP even though its exit status is zero. The independent audit has 21 passing checks. Those passing checks verify specified algebraic/numerical facts; they do not validate every historical theorem.

**Corrections worth preserving.** The Galerkin angle needs `acos(1-1/(n*n*a))`; the Wilson trace identity requires the stated boundary geometry; COM null dimensions in the tested sizes are not the earlier claimed pattern; a near-endpoint background example refutes an old uniform upper bound. Clock mass does not disappear at fixed N. The Lean development has actual unfinished obligations, and a conclusion-free depth comparison is not a depth theorem. See the [full audit narrative](../docs/handoff/ASTRA_RESEARCH_HANDOFF_MAIN.md) and [reproduction](logs/audit_research.py).

**Decision.** Keep corrected statements, archive failed claims verbatim with warnings, and require an explicit arithmetic transfer before assigning consequences to real zeta zeros.

## 2026-09-05 05:56:56 UTC: first autonomous research milestone begins

The initial authorized milestone is eight hours. The user's coordination task subsequently relayed a 72-hour recoverable programme. This log makes no guarantee of uninterrupted execution or of solving an open conjecture. The active priority is a genuine RH-conditional zeta half-gap result or an explicit out-of-band correlation theorem. Matrix-model distinctions are supporting results.

Three internal research lanes were assigned: scalar heat-flow proof and Yau comparison; residual Gram and arithmetic resonators; prime-gap certificate audit and transferable positivity methods. Their reports preserve failures as well as successes.

## Round 1: the saturated approximator and the new resonator direction

**Question.** Can another approximator inside the same accessible product support recover the missing half-gap energy?

**Exact answer.** Completion of squares gives `2 Re<ba,bg>-||ba||^2=||bg||^2-||ba-bg||^2`. Thus the selected coefficient-space approximator is already saturated for a fixed resonator and fixed product support. This does not optimize the resonator, prove a global method barrier, or allow replacement of finite-height Gram matrices by diagonal matrices without an error theorem.

**Independent computations.** The published linear Inoue trial is reproduced. A degree-14 one-variable trial has half-gap margin about `-0.01535798170385`. A fixed rational symmetric-prime trial improves this to a certified continuum value about `-0.014662375473369`; richer exploratory trials reach about `-0.01465473` but have ill-conditioned numerical Gram problems. These are distinct candidates, all negative.

**Failure with information.** Sparse support beyond the usual cutoff cannot provide a fixed amount of missing energy under the stated subpolynomial coefficient bounds. Sparse orthogonality alone is insufficient; dense correlations or different coefficient concentration would need a new estimate.

**Evidence.** [Round 1 report](reports/residual_gram_round1.md), [exact rational certificate](residual-gram/rational_trial_certificate.py), [certificate output](residual-gram/rational-trial-certificate.json).

## Round 1: scalar heat flow and extreme circular gaps

**Question.** Does a tiny isolated pair determine the first collision of the actual coefficient heat flow?

**Mathematical output.** A deterministic proof draft uses a scalar heat normal form. Removing the background linear drift by exact heat conjugation reduces the sufficient isolation condition to `delta^2 B -> 0`. Its probability application uses triple-cluster exclusion and published extreme-gap laws for CUE and positive integer beta circular ensembles.

**Scope.** This is a proposed full RMT theorem with internal audits, not a zeta-zero theorem and not a proof of universality for every beta. Its initial-background method overlaps classical Lehmer-pair theory; priority and formal verification remain separate obligations.

**Evidence.** [Heat report](reports/yau_flow.md), [Galilean refinement](reports/yau_flow_galilean_refinement.md), [independent first review](reports/prime186-yau-independent-review.md), [numerical checks](heat-flow/yau_flow_checks.json).

## Round 1: what the prime-gap 186 calculation actually contributes

**Question.** Can exact positivity and certificate methods from the public 186 project provide a smaller prime-gap bound or a transferable tool?

**Output.** A 39-element admissible tuple of diameter 182 was found, but no `DHL[39,2]` certificate was established. This is not a prime-gap improvement. An exact-rational convex-simplex enclosure independently bounds a fixed minorant mass. Separate exact geometry checks address the published triangulation's coverage. Numerical infeasibility searches are not portable impossibility proofs.

**Failure with information.** The official numerical verifier hit a FLINT convolution regression in the installed environment. No step was bypassed and no successful official certificate rerun was claimed. The public Lean project retains stated assumptions; it is not an assumption-free formalization of every analytic ingredient.

**Decision.** Stop broad prime-gap tuning until there is a definite path to a new analytic or certificate threshold. Transfer support accounting and exact positivity methods to the zeta lane.

**Evidence.** [Prime report](reports/prime186.md), [exact minorant calculation](prime-gaps/minorant_mass.py), [coverage verification](prime-gaps/minorant_geometry.py), [margin ledger](prime-gaps/margin_ledger.json).

## Round 2: ten-million-dimensional operator and a failed upper bound

**Question.** Is there a large unused coefficient direction hidden outside the one-variable trial family?

**Computation.** At `L=10^7`, the full sparse arithmetic operator has computed largest eigenvalue `4.324089558989538`, below the half-gap threshold `pi^2/2`. At `L=10^6`, 20 symmetric-prime features nearly reproduce the full finite optimum; 40 features reduce the remaining difference to about `0.0004437`. A 40-bin bosonic model with 215,308 states is also below threshold.

**Analytic attempt.** Separate Cauchy bounds lead to a scalar Schur–Volterra majorant. Its tested threshold is approximately `5.2074`, above `pi^2/2`; it cannot establish a universal half-gap obstruction. More grid precision does not fix that mathematical loss.

**Decision.** Preserve the full spectra, fit residuals and failed majorant. Investigate compatibility of extremizers or new arithmetic products, rather than presenting rising finite spectra as an asymptotic proof.

**Evidence.** [Round 2 report](reports/residual_gram_round2.md), [spectra](operator-bounds/extended-arithmetic-results.json), [fits](operator-bounds/eigenvector-feature-results.json), [Fock data](operator-bounds/boson-cutoff-results.json), [majorant data](operator-bounds/volterra-upper-results.json).

## Round 2: centered Gaussian positivity has an explicit pole correction

**Question.** Can a centered Gaussian make all Fourier kernels positive and therefore extend the accessible mixed-product support for free?

**Exact negative result.** In the critical-line contour identity, centering leaves an explicit pole-cut integral. For the intended longer-tail supports its phase is opposite to the retained prime contribution. A dense coefficient example with bounded diagonal norms has a negative pole correction of order `M/log M`; for `M=T^(1+eta)` this exceeds the presumed height normalization. The exact long-support Gram penalty also contains substantial off-diagonal mass.

**Related obstruction.** A nonzero Schwartz weight with nonnegative Fourier transform cannot vanish at the origin. Removing low-height coherent mass while keeping all those Fourier signs is not a free operation. This does not exclude all centered-packet methods: they must pay the pole term and control the density-subtracted mixed moment.

**Evidence.** [Full derivation and counterexample](reports/centered_gaussian_mixed_moments.md), [80-digit checks](centered-gaussian/centered_gaussian_pole_checks.json). The primary agent checked the source contour identity, the phase multiplication, and the dense-tail scaling. These are mathematical checks, not formal proof-assistant verification.

## Round 2: arithmetic transfer of the fixed symmetric-prime trial

**Question.** Were the proposed prime-factor moments merely an assumed Poisson–Dirichlet model?

**New proof draft.** A positive-measure Laplace limit for `d_ell(n)^2/n`, marked reciprocal-prime measures, exact divisor convolution, and weighted Schur truncation together give a proposed complete derivation of the fixed family's continuum form. The argument distinguishes the same-prime contribution that survives in `A* A` from the repeated prime in `A^2` that vanishes. It explicitly handles short backgrounds and signed polynomial coefficients.

**Status.** Independent adversarial audit requested. Do not upgrade this entry to an accepted theorem before reading that review. A successful audit would validate the family, while leaving the negative margin unchanged.

**Evidence.** [Proof draft](reports/symmetric_prime_arithmetic_transfer.md).

## Coordination and next decisions

Only the user's existing Fable session is to receive [one manually delivered audit packet](../tasks/FABLE_SINGLE_SESSION_COMPUTE_TASK.md). It independently checks a fixed vector and then stops. No receipt or completion is assumed. Astra owns the broader proof programme.

Next decisions depend on evidence: accept or repair the arithmetic transfer; finish the scalar-heat audit; identify a precise new estimate for density-subtracted mixed products or a compatibility-preserving upper bound. No parameter search, formalization attempt, or failed route should silently overwrite its earlier data. Git history and the source manifest are part of the evidence.

## 2026-09-05: arithmetic transfer audit resolved

The separately assigned residual-Gram agent accepted the fixed-family arithmetic transfer as a complete ordinary written proof after checking all six requested points. The primary author added the three requested explicit estimates. The result is unconditional as an arithmetic operator limit; RH is required only for its insertion into Inoue's zeta inequality. The fixed negative margin, full-operator limit, and half-gap target are unchanged. [Independent review](reports/symmetric_prime_transfer_independent_review.md).

The heat-flow author also completed a second-pass quantitative audit with K=16384 and eta0=1/524288, supported by exact symbolic checks. This is separate from the earlier independent prime-agent review. The true-Ht discussion identifies isolated small-gap arithmetic information as the missing input; it does not turn a circular model result into a zeta theorem. [Second-pass audit](reports/galilean-proof-audit.md).
