# Independent review of the inherited count and sampling constants

Date: 2026-09-05. Reviewer: the conductor-arithmetic/dispersion-transfer agent.
Scope: Sections 1–3 of ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md only.

Reviewed report SHA-256:
cb52d72f6068c3030968209d8aa028439ea4dc309aa5584d216a1d7d30a1a59d.
This hash was recomputed from the frozen file. The inherited Round 11 conductor
report was also checked at its pinned SHA-256
46347799005bb0f53af25c2a7e8ffb2b2217d92688c7651327dde3562f114b92.

**Accepted within the stated scope.** The following calculations were checked
independently against the actual arithmetic support proof.

- The count \(c_0Q/(2\log^{348}X)\), denominator bound \(d>Q/2\), and
  \(d/(32H)\) primitive numerators give at least
  \(c_0Q^2/(128H\log^{348}X)\) distinct reduced frequencies. No duplicate
  rational frequencies or permutation counts enter.
- Partition into at most \(8X/H\) intervals gives a cell containing at least
  \(c_0Q^2/(1024X\log^{348}X)\) frequencies. This only uses the proved total
  count; no distribution theorem within short intervals is assumed.
- With \(N=\lceil X\rceil\), \(M=\lfloor X/10\rfloor\), the integer support
  really is inside \([X,1.1X]\). Factoring out the carrier on a cell of width
  at most \(1/(100X)\) leaves phase spread at most \(\pi/1000\).
- The lower pointwise bound \(M/(2\sqrt H)\), Parseval norm \(M/H\), and
  \(M\ge X/20\) give the stated sampling ratio
  \(c_0Q^2/(81920\log^{348}X)\).
- The actual coefficient lower bound
  \(|C_\beta|^2\ge m_v^2H^2/(8Q^2)\) then gives precisely the weighted
  denominator 655360 in equation (10).

The constants and their directions are correct for all sufficiently large real
\(X\), uniformly in the stated \(H\)-range. The asymptotic threshold is not
claimed effective or numerically reached.

This review does not turn the artificial sampling packet into a prime
polynomial, and does not establish a lower bound for the full signed pairing.
The final wording correctly keeps the positive unweighted and fixed
absolute-coefficient sampling statements separate from other possible
reweightings or signed arguments. Sections 4–6 and the finite script are
outside this narrow review; the coordinator conducts the wider review.
