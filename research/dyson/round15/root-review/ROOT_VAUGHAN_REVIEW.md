# Root review of the exact R15 arithmetic reduction

Date: 2026-09-05. Reviewed final author SHA-256 `227179985368ea9a8c961b21dee9474d1440c1c5a3b7d04958a1e28b3e11d22a` and the complete independent Aquinas audit, SHA-256 `96a203248c4235c497d177793de501703af7c81d48a1361e1a863183ec294532`.

Status: accepted for the exact full-kernel reduction, untwisted coefficient lemma and quantified limitations. No improved bound for the full discrepancy is obtained.

## Checks on the proof

The identity is a pointwise arithmetic convolution identity, not an approximation to a random prime model. Splitting the Möbius factor in `mu*log` and the von Mangoldt value inside `1*Lambda` gives the four signed terms. The distinction between a value cutoff and R14's divisor cutoff is maintained. In particular the displayed formula relating the two different remainders includes the entire missing smooth term.

The actual weight forces `n>X>B`, so the small von Mangoldt value vanishes exactly. If the combined short factor `ad` is nonunit modulo q, neither the progression nor primitive principal term contributes. For a unit short factor both retain the same mask and the correct inverse residue. The remaining profile has one logarithmic factor, not the two in R14's `mu*log` term. Summing its Poisson bound with the actual `Lambda(d)` coefficient supplies the second logarithm in the final error. Thus

\[
\mathcal D[\Lambda]-\mathfrak B_{A,B}
\ll_J HX(ABQ/X)^J\log^2X
\]

has the asserted powers and all original weights. The ratio condition, fixed derivative order and failure of uniform constants as the margin tends to zero are explicitly stated. The two rational exponents are correct; a small positive exponent margin is not a numerically effective constant claim.

For the coefficient `beta_B`, opening each prime divisor as `m=kp` keeps `(k,rs)=1` on both sides of the source discrepancy. The inner prime interval may be sharply cut at B; the primary interval property and partial summation allow this. Harmonic summation in k consumes logarithms but does not change the fixed divisor exponent. Prime powers give the stated `M/sqrt(B)` error after absolute summation. The all-modulus statement is consistent with a direct large-modulus estimate using the progression count and `r/phi(r)<=tau(r)`. This is genuine untwisted Siegel–Walfisz, with the usual ineffective constants; it does not imply the phase-twisted statement excluded in R12.

The number of dyadic factor blocks meeting `X<am<2X` is `O(log X)`, not `O(log^2 X)`, because the sum of the two block indices lies in a bounded-width interval. Consequently a uniform `o(X)` block estimate suffices; no such estimate is proved.

## Adversarial checks and their resolution

I explicitly challenged the asymmetric-cutoff proposal: a lower bound on the beta variable does not ensure that it is the source theorem's shorter variable. The final report retains the `m>X^.5` corner, does not assume a Möbius-factor swap, and notes that even such a swap cannot cover the far unbalanced corner. Its cutoff budget below `.477` cannot force both factors above the strict source edge `.398`. This is an obstruction to the specified direct decomposition-and-source application, not to every dispersion argument.

I also challenged whether the nonnegative beta coefficient gives a sign. The final report gives exact opposite-sign actual integer witnesses and records that its remaining coefficient vanishes at prime inputs. The reduction reorganizes prime/composite cancellation. Neither witness determines the sign of the full progression-minus-principal form.

Finally the source per-shift estimate loses a factor H upon absolute summation. No sequence of merely algebraic rewritings removes that factor or provides the required covariance sign. The retained `mathfrak B` is a concrete next analytic problem. The R11 full-discrepancy bound remains `O(X^1.023 log^5 X)` under RH.

## Acceptance and reproducibility scope

The final standard-library script was inspected before the integration replay. Its exact formal-log representation, independently grouped divisor sums, integer/noninteger cutoffs, prime-input zeros, signed support witnesses and rational inequalities test the finite algebra. Neither this script nor its 49,152 equalities proves an asymptotic distribution theorem by computation. That theorem's hypotheses and proof are checked in the separate written reviews.

No RH/GUE/AH-refutation or new prime/zeta gap result follows. The public handoff through Round 14 remains a fixed historical checkpoint; this additional proof belongs in the next small research slice without rebuilding the large PDFs.
