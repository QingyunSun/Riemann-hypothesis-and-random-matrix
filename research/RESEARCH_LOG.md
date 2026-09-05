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


## 2026-09-05: dynamic proposals audited, including our own source correction

The low-mode degree-growth hypothesis fails: deterministic circular Coulomb evolution preserves positive and negative trace weights separately. A Schur/Cauchy-Binet proof gives ACUE/CUE equality for all derivative orders and all forward times in the protected symmetric-polynomial algebra. There are 234 exact protected comparisons; the nine out-of-band comparisons already differ at time zero. Independent cross-review is recorded separately.

The force square does separate the models, but collapses to a singular two-point statistic. Its CUE expectation is N(N²−1)/3 and its ACUE expectation is half that value. The expected initial dissipative slope is negative infinity for CUE and exactly −2N(N⁴−1)/15 for ACUE. The proof checks integrability and uses Fatou, rather than exchanging an invalid derivative and expectation. Complete float64 subset enumeration through N=10 supports the formulas.

Exact rational Sturm analysis provides a five-root counterexample to the minimum-gap-first premise. A symbolic 2x2 calculation disproves a proposed implication from marked inverse divergence to divergent depth susceptibility. The valid hard-core lower bounds remain useful; a universal exact identity requires the gap of the pair that actually collides.

We also corrected our own earlier Lagarias–Rodgers source judgment. The companion paper explicitly suggests adapting existing methods to a .606894 hard-core upper bound, but supplies no proof there. The earlier criticism that the literature never connects those objects was unjustified. Historical originals remain intact; the current main handoff and audit state the correction.

Evidence: `reports/dynamic_generator.md`, `reports/force_energy.md`, `reports/new_attachment_bridge_audit.md`, and their adjacent focused script/data folders. These finite-model results are not a zeta AH refutation.

## 2026-09-05: 186 transfer tools and finite Ritz decision

The two-dimensional residual Ritz correction for the L=100000 fixed arithmetic vector raises the half-gap margin by approximately 0.000488512, from −0.0376302 to −0.0371417. It validates a finite self-adjoint residual calculation, not an asymptotic fixed-family theorem. The report records a signed-residual lemma and the actual combined-product kernel that needs arithmetic control.

The user's Weijie Su link returns HTTP403 in this session. Its supplied structural description is checked against the primary 186 manuscript: complementary factorization controls the actual lcm divisor and triply dense divisibility, then permits wider sieve supports. No scalar exponent is imported into the unrelated zeta mixed-moment problem. The next decision is a new valid support/correlation estimate, not extra digits of the same negative vector. Evidence: `reports/transferable_tools_ritz_decision.md` and the structural frontier report.


## 2026-09-05: Fable pickup evidence recovered from the existing public session

A live PR11 check found source head `a408e7050fffc74459b3c83fafa5ac03c8b7dea6`. Its coordination note acknowledges the earlier FABLE_001 task from Astra commit 97df092, and F2 continuum/finite-sum files are present. The intended final task001_report.md is absent at this source head. The newer bounded packet has a separate receipt status; no complete execution of it is inferred.

The 81 existing public files are mirrored byte-for-byte under `fable/overnight-2026-09-05/`, with SHA-256 provenance. Most proposed heat/function-field/LR report filenames are not yet present. Their scripts and plans are evidence of work, not completed proofs. Independent Astra intake reviews record their exact scope and any issues. This synchronization starts no Claude session, agent or follow-up task. Historical instructions in the mirror remain source data.

## 2026-09-05: a new certified positive deletion credit

The next experiment addressed an actual omitted positive term in Proposition4.6. A disjoint, ordered two-fragment event violates a retained source row and lies inside the official cap domain. Restricting residual coordinate totals below the fragment cutoff removes Dickman uncertainty. Constant lower reciprocal-mark densities turn the new cell kernels into exact rational box volumes; both same-coordinate and different-coordinate owners are retained.

A corrected source-built FLINT runtime passed the unchanged mandatory regression. The 53-term outward square contraction proves a normalized credit exceeding1.5058119471ppm. Independent integer-cell/Eulerian kernel reconstruction and the measure/geometry proof audit pass. A separate process reproduces all53 interval terms and final rational endpoints exactly. Combining with the original published bounds increases the same k40 margin from23.36045 to24.86626ppm. No sub186 bound follows.

The runtime record preserves the previously failing wheel, upstream fix, source hashes, successful native/binding checks and a separately diagnosed full binding-suite Jacobi assertion. No checks were disabled and the official certificate was unchanged. Evidence: `reports/prime186_round4.md` and `prime-gaps/round4/`.

## 2026-09-05: finite k39 optimization identifies the next deficit

An independent cap engine, calibrated against the official k40 denominator interval, evaluates the original vector at k39 with quotient0.994361581476018. All77 coefficients were then optimized on the same official grid and physical caps. Independent scalar reevaluation of the returned vector gives0.994396399364491, leaving5603.60ppm below one. The matrix is ill-conditioned, so this remains a numerical candidate search and does not prove a family-wide upper bound.

The measured scale rules out treating the demonstrated few-ppm k40 credit as a solution for the inherited k39 vector. It does not cap all possible credit or support changes. The next bounded investigation changes radius/plateau geometry and recomputes affected source constants, rather than rescanning the same fixed vector. Exact signed projection identities also reveal that a generic completed-square estimate is worse than the current Young loss without certified cancellation; the separate inner-overlap correction is quantitatively tiny for the published trial.

The Fable hand-delivery packet received the coordinator's reuse-evidence prefix. The existing public mathematical task body and prior receipt note remain unchanged. No new Fable session, dispatch or receipt is inferred. The 333-page handoff remains an immutable earlier checkpoint; this new research is a separately linked update.

## 2026-09-05: variable-radius exceptional proof and bounded geometry decision

The completed Round 5 separates an analytic extension from a numerical search. The original exceptional-square counting argument works with a variable bound on all coefficient-root radii, with positive auxiliary exponents and unchanged CRT slack on an explicit open interval. Two independent exact implementations reproduce the primary fraction at radius 0.275 and agree on five changed-radius constants. A separate lower bound on the actual bin sum exceeds 0.34 at radius 0.276, proving that this particular counting mechanism cannot retain the old constant there.

The source audit examined fifteen natural radius/plateau templates and accepted twelve. The original plateau fraction fails its unchanged largest-cap formulas at the three largest radii, whereas valid common-height choices preserve both source constraints and inner nesting. A common replacement inner-square source works throughout the interval. Actual grid endpoints can retain new row 39, whose activation is narrower than two cells. A uniform one-outer-layer inward restriction removes that row while preserving row 38 and its guard. These are sufficient analytic/source results; the new failure schedule and physical upper integrals remain outstanding.

Ten coarse cap trials and two official-grid refinements reoptimized all 77 coefficients with their actual exceptional constants. Neither refined geometry change improves the original k39 value: the two quotients are 0.9943734016224463 and 0.9943501891039260, compared with 0.9943963993644909. They are untrimmed cap-only trials. No finite-family upper bound, global obstruction or smaller prime gap is inferred. Rebuilding full restoration for these negative candidates is postponed in favor of a materially different profile/support idea or a rigorous finite-family bound.

The integration replay preserves all original outputs, runs three bounded scripts in a temporary copy, and checks twelve saved matrix archives with thirty-six candidate vectors. Exact exceptional constants, fifteen source cases and twenty mask nestings agree. Only timing and optional source-text metadata are excluded from exact comparisons. The 53-file intake records all original hashes and two publication edits that make external source paths configurable. Evidence: `reports/prime186_round5.md`, `prime-gaps/round5/`, and `logs/round5-integration/`.

## 2026-09-05: detailed Rounds 4-5 handoff supplement

A separate 59-page PDF and 142 KB Markdown supplement collect ten complete proof, audit, runtime and search reports pinned to source commit c74b326. All source hashes match that commit. Every final page was rendered and visually reviewed across the primary and independent reviewers; one long display, a missing table separator and accidental prose emphasis were repaired only in assembly. Final checks report zero math errors, overflow or replacement characters. The original 333-page public and 381-page full local PDFs remain unchanged; the new supplement is available in both the public checkout and the adjacent local archive. No conjecture-completion claim follows from this document release.

## 2026-09-05: full signed operator generates a function beyond the old sieve space

The bounded Round 6 addressed the actual operator, rather than defining it by the old 77-dimensional matrix. Erased-coordinate integrals use the finite fragment measure; their adjoints restore the outer indicator. The hybrid face multiplier includes a negative region, so positivity is not assumed. A separate proof identifies exactly which total-cell/fragment-layer atoms are invariant for the cap operator, and why the true prefix/tail support requires more information.

The first new compression projects the full residual into arbitrary radial functions multiplied by the fixed product profile. Its subspace is not nested with the polynomial trial space. Independent review corrects a tempting projection-order mistake: with h=P_VQTf and w=Qh, the mixed form equals ||h||², while ||w||²=||h||²−||P_Uh||². The implementation uses the mass projection of Tf, without assuming the approximate candidate is an exact Ritz vector. Eighty rational signed examples and a separate 38-state nonuniform marked model verify the identities and retain a negative quadratic witness.

The official-grid radial construction raises the direct cap quotient from 0.9943963993644909 to 0.9944678209006830, a gain of 71.4215 ppm. The simple two-dimensional plane captures 71.0202 ppm; reoptimizing the remaining coefficients adds about 0.40155 ppm. Tilt and cutoff controls are stable at the stated tolerances. The realized plane's coupling squared is only about 1.26% of its threshold-crossing requirement. This is not a bound on the full uncomputed residual. The quotient remains 5532.18 ppm below one and its actual arithmetic support has not been restored.

A separate exact certificate proves that the frozen radial function leaves the old space. On positive-measure product cells, the old basis restricts to degree at most twelve in one cell index. The frozen radial column has thirteen exact zeros and a later exact nonzero dyadic value. A modular rank-77 witness plus that extra cell also proves dimension 78 over the rationals. An independent reviewer decoded the stored binary array and checked the whole-cell rational support inequalities. Independence is exact; the numerical distance and gain are not interval-certified.

One separate root process reproduces the fine radial profile and all selected reported values exactly, after replaying the independent algebra and saved-output checks. The full 183 MB of source arrays remain local; four compact public witnesses omit only the regenerable D cache, with file hashes and unchanged-array checks. The radial-energy plot is computed from saved arrays and suggests inspecting inner-cutoff transitions, without claiming causality or full residual localization. The next useful decision is a larger effective compression or a new product/support structure, not another run of the unchanged polynomial family. Evidence: `reports/prime186_round6.md`, `prime-gaps/round6/`, and `logs/round6-integration/`.

## 2026-09-05: two explicit actual-zeta targets for Dyson–Montgomery

The user's latest steering made Dyson–Montgomery and actual zeta zeros the priority, and paused prime-gap coefficient searches. Four bounded lines of work produced a two-scale logarithmic-derivative target, a compact Fourier/prime-covariance target, a new fixed arithmetic feature, and an explicit dynamical obstruction. No required new arithmetic inequality was proved.

The Poisson-resolvent comparison initially distinguishes CUE and the half-grid ACUE process, with the nonzero even Bragg atoms retained. General AH-Pairs has an extra near-diagonal mass P_0(T), which need not converge. Its Poisson variance contribution is exactly 2(P_0(T)-1)/sinh(b). Taking sinh(2)V(2)-sinh(1)V(1) cancels this freedom at the same height. The resulting AH value is 0.0623924179764985..., while the sine-kernel prediction is 0.0822714431214773.... Exact rational enclosures and a separate coordinator certificate show that an actual-zeta liminf of at least 1/16 would suffice to contradict AH-Pairs under RH. The earlier 0.07 target is optional and stronger than necessary.

The actual-zeta reduction controls noncompact pair tails, the early-zero removal, finite-height endpoints, the paired xi product, the Gamma drift and the holomorphic square needed to change a real-square mean into a modulus-square mean. Independent review identified a truncation-endpoint issue; the author fixed it by taking physical pair cutoffs j+1/4, away from half-grid atoms. Two reviews accept the corrected ordinary reduction. They do not establish the missing signed mean-square bound or assert novelty.

A separate compact bump supported on [6/5,7/5] avoids all integer atoms and gives an AH form-factor target 7/10, compared with the sine target one. Its exact prime kernel retains the continuous pole mean, the prime/mean cross term and the mean square. After removing the atomic diagonal of size 13/10, the AH covariance remainder is -3/5 and the sine target is -3/10. A high-precision finite identity confirms the normalization and demonstrates that omitting the mean materially changes the calculation. The new signed prime covariance remains unestimated.

The first suggested S3/S2^2 extension was rejected as a duplicate of the earlier archive. The replacement was the binary mark for a prime factor greater than sqrt(L). The exact unique-large-prime factorization gives an arithmetic moment and insertion calculus, now independently reviewed with explicit full-measure and short-background limits. One 30-feature trial at ell=27/25 improves its matched 20-feature baseline by only about 1.429e-8, reaching a negative margin -0.01465492379421. This is still worse than the earlier best larger polynomial family. All coefficients, matrices and the fixed rational vector were retained; the latter stays negative in direct integer-operator evaluations through L=10^6. No further sweep of this feature is justified by this result.

The forward-flow report gives a gap-independent contraction estimate, but also identifies the retained-block boundary propagation that a true H_t comparison must control. An exact deterministic polynomial family has bounded counting discrepancy and keeps hard core 1/2 at all forward times. The DBM diffusion contribution remains order one on a protected microscopic trace, even though ACUE and CUE continue to match the entire protected trace filtration under DBM. These results identify missing inputs; they do not transfer universality to zeta.

The integration replay in a temporary copy reproduces nine output files after excluding only timing, including identical order-40 matrices and the fixed rational integer trial. All 57 original files (3,392,974 bytes) are also preserved in the adjacent local archive; 14 third-party PDF/text references stay local with public hashes. Three publication edits make the old arithmetic source path portable and update/clarify completed proof review. The next bounded analysis seeks an actual centered-psi/cutoff identity for the signed mean square. The weight changes sign beyond log(2 cosh 1); ACUE itself rules out deriving the target from low-band identities and generic positivity alone. Evidence: `reports/dyson_round7.md`, `dyson/round7/`, and `logs/round7-integration/`.

## 2026-09-05: the actual arithmetic residual is isolated

The follow-up targeted the missing arithmetic term. Under RH, a contour shift of the actual logarithmic derivative against its finite prime polynomial gives a diagonal main term and O_c(N log^3 T) mixed error. The infinite right-line sum is split into near and far integer pairs with explicit bounds. Completing the square yields I_T(c)=T D_N+||R_c||²+O_c(N log^4 T). With N=floor(T/log^6 T), PNT evaluates the two-scale diagonal as B=0.4560939793292317..., so the prior 1/16 target is exactly a signed-residual lower bound of 1/16-B=-0.3935939793292317.... That lower bound remains unproved.

An exact Stieltjes continuation writes R_c using psi(x)-x, its endpoint at N and the pole counterterm. RH makes the integral absolutely convergent, but the straightforward absolute-value estimate is of order T log³ T and is much too large after squaring. Two scales act on the same centered arithmetic function; their coupling is retained explicitly. The pole can be removed from normalized energy using only the pointwise RH bound already in the proof, with O_c(log^-3 T) error. Independent review supplied this simplification and replaced an unnecessary low-zero-table assumption with a compact RH estimate. The final author hash is accepted in the review.

The companion positivity audit closes a tempting shortcut. An explicit band-limited minorant has a valid exact weak bound near -0.208674513, with a one-parameter optimum only in its stated correction family. A second reviewer checks its nonnegativity, Fourier endpoint regularization and half-grid determinantal process. That actual process satisfies the known band and positivity constraints while lying below 1/16. Formal spectra with arbitrarily large negative-weight atoms are explicitly separated from this realized countermodel. No generic positivity argument supplies the missing arithmetic lower bound.

The ten received files (66,313 bytes) are preserved verbatim publicly and locally. Two complete JSON outputs reproduce in a temporary copy, without metadata exclusions. An additional eight exact rational cases check prime-power and prime endpoints in the finite Stieltjes formula. Actual-zeta checks occur only in the absolutely convergent half-plane; critical-strip regularized sums are labeled low-height diagnostics, not an asymptotic estimate or W_T computation. There is no new parameter scan, novel prime-gap result or completed famous conjecture. The next obligation is the shared centered-prime energy estimate or the compact covariance target. Evidence: `reports/dyson_round8.md`, `dyson/round8/`, and `logs/round8-integration/`.


## 2026-09-05: actual complementary-modulus component and a failed two-prime interaction

Round 9 used the 186 paper's complementary factorization conditions in a definite part of the centered-prime covariance. Parameters omega=.012, delta=.001 and epsilon=.001 give 240 omega+80 delta=2.96 and a full-prime distribution level .523. An exact Mobius–log decomposition selects moduli in that family. For each shift, coherent primitive residues and two common smooth weights permit the source estimate with O_A(X log^(-A)X) error. The original nonprimitive terms and principal-term prime-power deletions are separately bounded. This is a valid arithmetic transfer beyond the square-root divisor level, but arbitrary logarithmic savings do not survive the H polynomially many shifts at the required fluctuation scale.

A further RH identity leaves only O(H sqrt(X) log^4 X) in the summed principal/exceptional terms, which is negligible throughout the compact Fourier test's H range. The missing signed progression discrepancy D_Q is now explicit, as is the untouched shifted bilinear remainder. The proof does not substitute the source's multiplicative convolution theorem into Lambda(qm+h). An independent reviewer accepts the bounded transfer and its precise limitations. The next attempted estimate completes the smooth h sum before applying a large-sieve bound; that is ongoing Round 10, not a completed result here.

A proposed exponential prime profile was found to duplicate earlier work, so no repeat scan was run. Instead one fixed double-large-prime indicator D=count(count-1)/2 was added. Its exact unordered factorization and three-state insertion calculus were reviewed, including the necessary repeated-prime error for a single designated prime above L^(1/3). The 30-feature continuum margin is -0.0146549114371551: a small unverified floating gain over its matched baseline, still worse than the older 48-feature trial and far below zero. Its fixed rational vector is also negative on an actual integer operator at L=100000. This failure does not exclude a different coefficient family.

The root proved an elementary prime-power tail estimate, independently checked by the flow/source lane. Prime squares require an infinite mean-square argument with a convergent delta^(-4) error; higher powers permit absolute summation. The resulting replacement error is uniform for growing widths, including the b² e^(2b) amplification in the mesoscopic statistic. The open residual now uses genuine primes without changing its limiting target.

The mesoscopic source audit corrects a possible rate objection: the proof-level finite-height error of the published three-integrals bounds can be negligible on a sufficiently slow diagonal. The limiting lower bound itself remains weaker by a factor of order b than the first sine-versus-ACUE correction. Coupling widths b and 2b removes the nonconvergent AH diagonal mass and gives targets zero versus -3/4. Its sufficient lower bound must be uniform on a selectable range; fixed-width AH alone does not supply a prescribed growing rate. Neither that lower bound nor a leading-plus-correction prime variance asymptotic is proved.

All 28 original files, including later independent reviews, are retained verbatim locally; 26 research files are public. The two third-party reference bodies stay local with URL/hash receipts, alongside an extra copy of the 186 source pair. An isolated replay reproduces five JSON outputs after excluding only timing and temporary source paths, and both fresh order-32 matrices agree exactly. The earlier PDFs were not rebuilt for this bounded negative trial. Evidence: `reports/dyson_round9.md`, `dyson/round9/`, and `logs/round9-integration/`.


## 2026-09-05: completion improves an actual shifted-prime discrepancy by a power

Round 10 addressed the polynomial H loss left by the previous source application. Completing a fixed smooth packet in h and grouping equal rational frequencies gives the exact Ramanujan-centered pairing of selected Mobius coefficients and genuine-prime exponential sums. The conductor principal term is mu(d)/phi(d), independent of the parent modulus. Its zero-frequency term cancels; duplicated r/q frequencies are merged before a spacing estimate. A coefficient squared norm O(H log^3 Q), together with a direct finite-spacing bound for the centered prime sums, yields O(sqrt(H X (X+Q²)) log^4 X) for the actual packet, including its log cofactor and original sinc kernel.

The passage to the actual two-variable weight is justified by uniform smooth derivatives and an absolutely summable Fourier separation. Both terms of the progression discrepancy are included in the prime-power removal. Two independent reviewers split the coefficient/spacing and full-kernel/exception duties, and the root read the complete final argument. The bound itself is unconditional and works for any squarefree family with the stated cap; it does not claim a new dense-divisibility distribution theorem. At Q=X^.523, the error exponent is 1.023+theta/2 for H=X^theta. The saving over the per-shift triangle exponent is at least 181/3000. The estimate remains above the required X log X scale, and its scope stays the fixed smooth packet.

A parallel actual-prime source audit found that Guth–Maynard v2 Corollary 1.4, including its subsequent slight fixed-epsilon improvement remark, does not reach the interval exponent s/(b+s) tending to zero. Even where the stated count theorem applies, its immediate squared-error consequence is too large for the needed variance precision. Checked RH short-interval comparisons also retain fixed constant losses and endpoint quantifiers. A specifically log-weighted genuine-prime mixed moment M=-E' would be sufficient if its deficit coefficient were strictly below two; integration over [b,2b] gives the exact gap 3epsilon/8 above -3/4. That hypothesis remains unproved and is recorded as an obligation, not a new zeta estimate.

All 15 original files (1,452,061 bytes) remain local and 14 research files are verbatim public; the third-party HTML stays local. Both exact output JSON files reproduce, with only two temporary provenance paths excluded from one output. The 9615 Ramanujan checks and scalar tests verify algebra, while ordinary proofs and independent reviews support the analytic claim. No floating search, prime-gap sweep, or new model session was used. The next substantive step must exploit arithmetic cancellation in the completed pairing or prove a mixed-moment gain; lowering only logarithmic losses cannot close the remaining power gap. Evidence: `reports/dyson_round10.md`, `dyson/round10/`, and `logs/round10-integration/`.


## 2026-09-05: later Fable snapshot and independent two-sided review

PR11 commit 89393d5 supplies 141 files (1,062,904 bytes), including previously absent proposer reports, C-beta-E/F1 drafts and two F1 refuters. A new verbatim snapshot preserves the old mirror unchanged. The proposer has an incorrect Pi4 coefficient 6a^2 and a table mixing different v values. The correct coefficient is 6a and the fixed-v table is reconstructed from its stored rows. The refuter's objection is valid, but its numerical third-derivative probe has an additional sign error: saved -6 values are labelled as tending to +6. Root independently checks the pole algebra and reproduces that bug without editing the originals.

The two bounded refuters replay in a copy: all ten check flags match, including three expected failures of narrative assertions. The insertion computation differs from saved values by at most 8.33e-17. Fixed negative finite margins and slow drift do not negate the independently reviewed fixed-family o(1) transfer or establish a rate. The source's claimed need for a quantitative rate is not a requirement for that particular fixed limit.

The coordination task separately identifies a reversed CUE tail inequality, a dimensionally false general-beta local-density hypothesis, a wrong unused partition function, an invalid inference from one-point intensity to selected-pair density, an undischarged flow-window condition, and a periodization wrap-gap issue. Root checks the cited passages and elementary counterexamples. These are precise repair obligations, not rejection of every candidate lemma. No new Fable session or automatic follow-on task was launched. Evidence: `fable/reviews/pr11-89393d5/`, with both source snapshots separately pinned.


## 2026-09-05: RH small-arc input removes the actual shift-length loss

The Round 11 arithmetic lane uses the primary Bhowmik--Schlage-Puchta centered small-arc estimate under RH. Weighted prefixes and an exact derivative polynomial provide local energy and derivative bounds. Disjoint Farey sampling then retains the arc length factor rho, and dyadic pairing with the smooth h coefficients cancels H. Every tail band, the smooth integer mean and the distinct primitive Ramanujan mean are treated; Fourier costs in both kernel variables and both prime-power operations are included. Independent review accepts O(X^1.023 log^5 X) for the actual smooth discrepancy. It saves a power between 1/12 and 1/7 over Round 10, at the explicit additional RH assumption, but leaves X^.023 after covariance normalization.

A separate arithmetic construction places 348 distinct prime factors into two valid complementary roots. Fixed-ratio PNT gives at least c Q/log^348 X terminal conductors above Q/2. Their full signed coefficient is exactly 1/d; no other parent multiple can cancel it. Primitive low numerators retain shift transform of order H. The coefficient norm therefore cannot improve by a fixed power on this full family. This is not an obstruction to the new localized bound, different supports, or signed joint cancellation with actual primes.

The mixed-tail lane verifies Chirre's fixed-width derivative identity, including its remaining unknown form-factor integral. A centered finite prime measure converges with an explicit RH tail bound; the pole is negligible and the endpoint is retained. Its diagonal is b^(-2)+2b^(-3), with a joint off-diagonal remainder whose needed sign and coefficient remain unproved. The mathematical cutoff exp((log T)^3) is acknowledged as computationally infeasible, and the failed long-polynomial majorant is not confused with the true error.

All 18 originals (536,670 bytes) are preserved locally; 15 research files are public verbatim. Two exact checks replay successfully, with only one temporary reference path excluded. Primary third-party PDF/text/HTML bodies remain local with receipts. The next bounded investigations test sampling sharpness on the actual support, legal use of the 186 distribution theorem, and the precision of centered prime-interval upper bounds. No large scan, PDF rebuild, or external-model session was launched.


## 2026-09-05: close three false shortcuts while preserving joint arithmetic

The actual terminal conductors already constructed contain enough reduced low frequencies to force a microscopic cluster by pigeonhole. A finite integer-band Dirichlet packet proves Q^2/log^348 X lower sampling scale and the corresponding absolute-weight bound. It meets the known small-arc and derivative envelopes but is explicitly not an actual prime polynomial. The exact signed Gram and residue kernel are retained as possible routes; positive sampling does not decide their cancellation.

The source-transfer lane keeps the genuine complementary moduli and legal bilinear scales. A permitted phase twist approaches a cubic root of unity on the prime interval, causing an explicit modulus-3 discrepancy of order N/log N and violating SW with logarithmic exponent two. The global primitive-filtered shift interval still projects to all local unit classes, making the product CRT hull cost phi(d) rather than a divisor weight. Treating H as the short convolution factor also falls below the source range. These close specific direct substitutions, not a new dispersion argument preserving the extra variables.

The mixed-arithmetic lane applies Saffari--Vaughan's genuine-theta RH theorem directly to the jointly centered measure. Mellin Gallagher, both cutoff crossings and weighted dyadic sums give a valid but insufficient estimate. The stronger global bound on the same source page and earlier E=O(1) control are explicitly retained; the weak local calculation is not advertised as best possible. The actual smoothed kernel has negative lobes, which only defeats a termwise positivity shortcut, not general PSD. No needed one-sided fluctuation coefficient is obtained.

Root independently reads and accepts all three proofs within these scopes. All 18 originals (1,904,996 bytes) are kept locally; 15 research files are public verbatim. Both exact scripts replay; only four temporary provenance paths are omitted from one certificate. The existing Fable manual packet receives its updated source-status prefix, preserving the canonical packet's prior body and receipt. No new session or covered large computation is requested. Subsequent bounded work tests whether averaging sparse rationally resonant phases, and retaining the exact signed CRT kernel, can improve the actual prime estimate.


### 2026-09-05 — Fable 2073028 repair intake

Preserved the next 160-file PR11 revision separately. Accepted the repaired F1 coefficient and fixed-v rows while retaining the refuter-sign correction. Proved and independently reviewed the joint-cutoff incomplete-gamma diagnosis. Replaced F3's claimed infinite field norm by a complete mass-weighted sector bound, also uniform for its literal grids; this remains above the sharp threshold. Checked M=6,8,10 only and recorded general-beta repair gaps separately. No new Fable session, large prime sum or spectrum sweep was run. Next work remains the actual signed zeta arithmetic and a separately checked finite-RMT background estimate.


### 2026-09-05 — Round 13 rational-core extraction

A fixed rational core can be extracted with total RH error X^.923 log²X after retaining the true conductor/shift weights and primitive means. Its main term can be large on a real-prime admissible subsum. Completed the exact CRT norm decomposition and isolated the unresolved small-gcd nonzero modes. Positive coherent contributions remain only subsums of the signed expression. Two inspected exact scripts replay in a copy; independent reviews distinguish these component results from the unresolved actual prime pairing. Follow-up tests the smooth-long-factor cancellation directly inside the original kernel.
