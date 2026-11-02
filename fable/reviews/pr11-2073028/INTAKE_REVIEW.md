# Fable 2073028: repaired arithmetic, finite Fock bound and retained gaps

Date: 2026-09-05. Source: Alpha-devbox PR11 commit `20730285c8f9a81539e0662c6e015023c2ed107a`. The 160 received public research files are a separate verbatim snapshot. Earlier snapshots and their reviews remain unchanged.

Two previous F1 objections are repaired: the leading coefficient is now Pi4~6a epsilon^-4 and the fixed-v table now uses its actual v=1 rows. The unchanged refuter still tests the negative of the derivative that tends to positive six. The new finite prime sum is honestly inconclusive; its cutoff is explained by the independently reviewed incomplete-gamma limit in `F1_REPAIR_AND_CUTOFF_REVIEW.md`.

The F3 claim that the field norm is infinite is false for the stipulated g and mass cutoff. `F3_MASS_CUTOFF_BOUND.md` gives a direct, independently checked sector proof: ||K||<=2 integral_0^1 |g(u)|²/u² du. For g=2sin(pi u/2), this is 4pi Si(pi)-8, approximately 15.2721. It also uniformly bounds every literal finite grid. This finite upper bound is above the desired pi²/2 threshold; it supplies no spectral-wall or arithmetic-transfer theorem. The first-bin constant-basis normalization in the source is not defined in L²(du/u).

The bounded local check imports only the source matrix builder and checks grids M=6,8,10, every occupation coefficient, the finite mass inequality and the scalar integral. It uses floating arithmetic and is not a rigorous eigenvalue enclosure. It does not rerun the large source/refuter sweeps. The source's memory check occurs after matrix allocation, and its ru_maxrss/1024 conversion assumes Linux units; on macOS that is not an MB conversion. No runtime or memory claim is inferred from those old numbers.

The source script and JSON model description also omit 1/sqrt(j) from their opening formula, although the actual builder correctly includes it. All comparisons here use the builder's literal coefficients. Source bytes are preserved rather than silently corrected.

The general-beta background repair is reviewed separately in `CBETA_REPAIR_REVIEW.md`; its unresolved finite-N formulas and conditional flow assumptions must not be treated as a proved CbetaE-to-depth theorem. The older CUE and periodized-zeta objections remain applicable where their source files did not change.

The new contribution is a finite boundedness theorem for the idealized operator and a precise cutoff diagnosis. The separate Astra fixed-family arithmetic transfer remains valid with its currently negative certified margin. Full arithmetic-to-Fock convergence, a sharp spectral threshold and the actual-zeta signed covariance gain remain open.
