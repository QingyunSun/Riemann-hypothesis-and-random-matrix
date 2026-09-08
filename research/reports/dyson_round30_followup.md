# Closing central challenge: precise comparisons, no strict signed gain

2026-09-08. This is the last bounded mathematical follow-up of the programme before its 06:15 UTC cutoff. It preserves successful local arguments and the exact failures of the attempted central shortcuts. The major-conjecture objective is not achieved: no RH proof, Montgomery–Dyson/GUE theorem, AH refutation, improved actual-zeta gap, or sub-186 prime-gap theorem has been proved.

## Four supported conclusions

**The upper balanced tail is localized.** R30's argument is uniform down to the bounded endpoint X=T squared. For its stated unmasked balanced blocks,
\[
|Z(X)|\ll T^{-141/800}/\sqrt{\log T}+(T^2/X)^{3/4},
\qquad T^2\le X\le T^{9/4}.
\]
For a specified uniformly controlled dyadic family X_j=2^jT squared,
\[
\limsup_{T\to\infty}\sum_{j\ge J}|Z(X_j)|\ll2^{-3J/4}.
\]
The finitely many central blocks remain. Pointwise vanishing at each fixed exponent above 2 is not permission to declare the complete upper sum zero. [Root derivation and independently checked quantifiers](../dyson/round30/central-followup/ROOT_HEIGHT_LOCALIZATION.md).

**The full periodic central principal is negligible.** For q=2d, the exact model
\[
p_d(n)=\frac q{\varphi(q)}\mathbf1_{(n,q)=1}-2\mathbf1_{n\text{ odd}}
\]
has mean zero and vanishing Fourier coefficients at every multiple of d. The full Ramanujan series, after convolution with the exact smooth prime kernel, has norm O(Y/phi(d)). Projection is retained as an L2 contraction. The complete model contribution to the two-alias central stationary pairing is therefore O(1/log T). No harmonic or parity mode is dropped. [Complete proof and actual error identity](../dyson/round30/central-followup/STATIONARY_CHALLENGE_RAMANUJAN_MAIN.md).

**A separate zero-sampling norm is controlled at critical length.** Under RH, for a fixed smooth carrier window and an arbitrary polynomial on the sharp dyadic interval,
\[
\frac{2\pi}{\log T}\sum_{\gamma>0}w(\gamma/T)|P(\gamma)|^2
=\int w(t/T)|P(t)|^2dt
+O\!\left(\frac{(T+D)\sum|c_d|^2}{\log\log T}\right).
\]
This follows by removing the common phase, applying the existing RH bound for the zero-counting discrepancy, and paying the variation through Montgomery–Vaughan. For the actual central Möbius polynomial the error is additive O(T squared/loglog T). No lower bound for every short-window continuous norm is assumed. The comparison supplies no new signed correlation estimate. The [complete source/applicability review](../dyson/round30/central-followup/zero-moment-review/ZERO_MOMENT_APPLICABILITY.md) also checks the actual length and error terms in the Bui–Florea–Milinovich and Milinovich–Ng statements.

**The actual joint product can also be sampled, with its variation paid.** Let G(t)=w(t/T) fhat(t) M_D(t) B_K(t), with the original prime-error transform and both original sharp polynomials. Root proved, and an independent agent checked,
\[
\frac1{\pi X\log^2T}\int G(t)dt
=\frac2{X\log^3T}\sum_{\gamma>0}G(\gamma)
+O(1/\log\log T),\qquad X=T^2.
\]
After removing the three common phases, their remaining phase derivative is log(DK/X), which is bounded. The derivative of the transformed prime error corresponds to multiplication of its compact physical profile by log(x/X); the other derivatives have bounded relative logarithmic weights. The complete product's L1 variation is O(T squared times log squared), which makes the error vanish after normalization. This is an actual weighted-zero comparison, not a pair-correlation distribution law. [Complete root proof](../dyson/round30/central-followup/ROOT_JOINT_ZERO_SAMPLING.md).

## The exact central estimate still missing

The periodic principal is split separately for every d. Its complementary error is
\[
e_d(n)=\Lambda(n)\mathbf1_{n\text{ odd}}
-\frac{2d}{\varphi(2d)}\mathbf1_{(n,2d)=1}.
\]
Moving the Mellin projection to the dual factor uses its **bilinear transpose P_{-J}**, not P_J. The exact original compact prime kernel then yields a finite weight L_{d,J}(n), supported in X<n<3X, even though the projected dual function is noncompact. The d and J dependence remains. The central stationary band is
\[
Z_J=\frac1{X\log^2T}\sum_{d\sim D,\ d\text{ odd}}\frac{\mu(d)}d
\sum_{X<n<3X}e_d(n)L_{d,J}(n)
+O(1/\log T)+O(T^{-1/2}).
\]
The required o(X log squared T) bound for its numerator is not proved. It is equivalent to an o(1) bound for this specified band. Ordinary PNT or a formal Ramanujan principal calculation does not replace that missing estimate at moduli comparable to square root X and with these projected oscillatory weights.

The joint zero-sampling identity gives another exact target with an error tending to zero. Its zero sum is also unestimated. The same zeros determine the prime-error transform, so independent randomness, a diagonal replacement, and the deletion of a kernel are not justified. In particular, 1/zeta has poles at zeta zeros; a finite Möbius polynomial does not vanish there by a reciprocal identity.

Even a saving for the specified central band would not, by itself, pay all unbalanced, masked and shift-dependent terms in the global R26 aggregate. Its remaining major target is still
\[
\boxed{\liminf_{T\to\infty}Z_T<A-2M.}
\]
The established global identity remains Vbar_T=Z_T+2M+o(1). Neither the missing strict inequality nor the alternative signed-residual lower bound from R8 has been proved.

## Reviews and verification

Root read the complete eight-section periodic-principal proof and checked every normalization, harmonic bound, reciprocal-totient estimate and transpose sign. An independent agent checked the root's uniform endpoint/tail argument and the complete joint-sampling proof. Root read the full zero-moment note and independently checked its Stieltjes proof, absolute-error qualification and the primary Bui–Florea–Milinovich Theorem 3.1 and Carneiro–Chandee–Milinovich Theorem 2 statements. The final notes and receipts distinguish these reads from formal verification.

The finite principal checker uses exact cyclotomic arithmetic and checks 66 Fourier cases, 10 cancelled parity modes, 401 Ramanujan bounds, 50 reciprocal-totient identities and the bilinear transpose sign. A deliberately incorrect same-sign projection is rejected. These checks validate finite algebra, not the asymptotic theorem. Original source bodies stay in the local reference folder; public receipts preserve their hashes and source URLs. No new prime or zero scan was run, and no new external model session was started.

## Recoverable state and assessment

The local working repository is the Dropbox `Riemann zeta RMT/Astra-Research` folder, on `codex/astra-research`; PR 1 in `QingyunSun/Riemann-hypothesis-and-random-matrix` remains the public research branch. The old Alpha-devbox PR 11 has a coordination link. The full 705-page public and 753-page local PDFs remain the earlier compilations through R14; the subsequent complete reports and proof files are Markdown and are not silently represented as already incorporated into those PDFs.

The existing three-day programme's cutoff is 2026-09-08 06:15 UTC. This bounded follow-up is being closed and saved; no new research round is opened near that cutoff. The recoverable mathematical starting point is the exact central finite discrepancy or the exact joint zero sum above, with all remaining global terms retained. Further representations, finite countermodels, internal review counts and archive sizes are not substitutes for the strict arithmetic gain. The [Chinese progress assessment](progress_assessment_2026_09_07.md) states plainly that the user's major-theorem objective remains unmet.
