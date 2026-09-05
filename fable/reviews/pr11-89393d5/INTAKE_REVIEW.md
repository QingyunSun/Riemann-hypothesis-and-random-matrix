# Fable PR11 snapshot 89393d5: separate intake and two-sided arithmetic audit

Date: 2026-09-05. Source: [Alpha-devbox commit 89393d5da61a45561ed199330c5b836f47fcd629](https://github.com/galpha-ai/Alpha-devbox/commit/89393d5da61a45561ed199330c5b836f47fcd629). This review accepts a source snapshot and reports specific checks. It does not approve every mathematical claim in that snapshot or establish a new zeta-gap result.

## What arrived

The [new snapshot](../../snapshots/89393d5/files/) contains 141 files, 1,062,904 bytes, preserved verbatim. Its [manifest](../../snapshots/89393d5/SOURCE_MANIFEST.json) pins every file. The earlier 81-file a408e705 mirror remains unchanged. The retained local source tarball has 3,104,082 bytes and SHA256 `9ca9fd9c7b907512db107a59e8f2d8caf5489887a532a55b4d6503bea42f1976`.

Three source commits recovered six proposer reports, added the C-beta-E background and F1 arithmetic-transfer drafts, then added two F1 refuters. The recovered claims include Theorem B repair, CUE background, Level B, structure, H2 and finite-sum diagnostics. These reports are now present; the earlier snapshot's absent-file assessment must not be applied to them. Presence is not proof acceptance. The source's own claim ledger describes several as awaiting refutation, and its last commit message says an F1 repair is in progress. That message is not a completed repair receipt.

This bounded intake examines F1/F2 arithmetic and reproduces the two F1 refuters. The [separate background and boundary audit](BACKGROUND_AND_BOUNDARY_REVIEW.md) records additional specific objections; neither review is a full acceptance audit of the heat-flow drafts. No new Claude session, model request, automated next task, or large prime computation was launched.

## The valid F1 objection, and the refuter's own sign error

The proposer text gives the leading coefficient of Pi_4 as 6a^2, then concludes m4=a^2+6a after adding Pi_2^2. The two expressions are inconsistent. The correct leading terms are

\[
\Pi_2^2\sim a^2\varepsilon^{-4},\qquad
\Pi_4\sim 6a\varepsilon^{-4},\qquad
m_4=a^2+6a.
\]

To see the second coefficient, the local inclusion probability has rho_p=a p^(-s)+O(p^(-2s)). Thus rho_p(1-rho_p) has the same leading a p^(-s). The sum of (log p)^4 p^(-s) has leading 6/(s-1)^4; prime powers and local quadratic errors are analytic near s=1. This supplies a single factor a. The proposer's script assigns the correct final m4 as a literal; that assignment does not verify its incorrect written intermediate coefficient. The resulting conditional moment expression (a+6)v^4/((a+1)(a+2)(a+3)) is consistent with the corrected coefficient.

However, the refuter's numerical probe also has an error. Its function zz3 is the third derivative of zeta'/zeta. Since zeta'/zeta(1+eps)=-1/eps+analytic, zz3 has leading **+6/eps^4**. The script evaluates **-zz3*eps^4** and labels it as tending to +6. All three saved values are actually -6. The subsequent coefficient is separately assigned as 6a and does not depend on this bad probe.

The [independent correction](check_pole_coefficient.py) differentiates the pole using exact rational algebra and separately runs the correctly signed high-precision diagnostic. The exact pole algebra supplies the coefficient; the numerical probe is a secondary sign check. This correction preserves the refuter's valid objection to the proposer while rejecting its faulty numerical verification. The original scripts and outputs are untouched.

## The quoted normalization table mixes different v values

For fixed v=1, the stored two-term normalization ratios are:

| L | Actual v=1 ratio |
|---:|---:|
| 10^4 | 1.0001888352957300 |
| 10^5 | 1.0001190371666680 |
| 10^6 | 1.0000833930992132 |
| 10^7 | 1.0000616581233717 |

The proposer's first two quoted values, 1.002005 and 1.000396, come from other v rows at L=10^4, not this fixed-v sequence. The last two entries were correctly transcribed. The refuter detects this mismatch and the bounded replay confirms it.

The [replay receipt](recheck.json) records ten checks with three expected narrative failures. All pass/fail flags match the saved refuter. The rigour output matches exactly, including its sign bug. The insertion calculation at L=1000 agrees to less than 10^-12; small platform-level floating differences are explicitly retained in the receipt and log. A receipt labelled successful replay does not turn the three failed assertions into passes. The check based only on a literal source formula string is a source-presence check, not an independent proof of the operator contract.

## What the finite drift does and does not establish

F2's stored fixed-vector margins remain negative, from about -0.05199 at L=10^3 to -0.03124 at L=10^7. Its continuum value is approximately -0.014662375473371, consistent with Astra's independently certified fixed-vector limit. The finite data were received as diagnostics; this intake does not rerun the large computations or upgrade them to interval certificates.

Slow prime-discreteness drift, even through 10^8 in a semi-continuum diagnostic, does not refute an asymptotic O(1/log L) bound without a proved constant and threshold. Nor can a few competing curve fits establish the rate. Large finite differences between full and clean operators do not contradict a proved vanishing difference in a fixed-family limit.

F1/F2 were working from the earlier Astra input checkpoint 97df092. Subsequent Astra work supplies a [fixed-family arithmetic transfer proof](../../../research/reports/symmetric_prime_arithmetic_transfer.md) and [independent review](../../../research/reports/symmetric_prime_transfer_independent_review.md), with joint weak limits and bounded-operator control. For that fixed family an o(1) limit suffices; an explicit O(1/log L) rate is not logically required. The F1 prose cannot be used to reopen that specific gap solely because its own rate proof is unfinished. Conversely, the fixed-family proof does not validate arbitrary growing feature families or claim that this negative trial refutes AH.

## Reproduction and next use

From the public repository root:

```text
OPENBLAS_NUM_THREADS=1 python3 fable/reviews/pr11-89393d5/recheck.py
```

This verifies all source hashes, copies the complete snapshot to a temporary directory, runs only the two named refuters (bounded at L<=10^6), and runs the separate pole check. Logs and the structured receipt remain beside this review. The code was read before execution; no model call or network access is part of these checks. Imported proposers' large main blocks are not executed.

For collaboration, the useful corrections are the Pi_4 coefficient, the refuter sign, the fixed-v table, and the distinction between fixed-family convergence and a quantitative rate. A repaired draft needs its own new commit and review. Remaining RMT/heat-flow proposer reports require separate mathematical audits; this intake gives no blanket endorsement.
