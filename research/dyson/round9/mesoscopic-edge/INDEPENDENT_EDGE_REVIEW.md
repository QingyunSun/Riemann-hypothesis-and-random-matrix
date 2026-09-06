# Independent review of the mesoscopic edge obligation

Date: 2026-09-05. Reviewer: the root research lane, independently of the source-audit author. **Accepted as a bounded analytic/source audit, without a new arithmetic edge estimate.**

I read the complete `EDGE_RATE_AUDIT.md`, its small algebra script, and the saved primary source at Theorem 5, Lemma 16 and Section 4.2. The following points were checked directly rather than inferred from the script's PASS status.

1. The source uses c where the report uses b/2. Substitution gives exactly the displayed lower and upper functions. The absolute proof error for c>=1 contains the square root of log(log T)/log T, the c/log T term, and log²(T)/(T c²). Keeping this error instead of the theorem's compressed relative error is legitimate. It can be below the exponential edge signal on a sufficiently slow diagonal.
2. The limiting lower bound's deficit is asymptotic to e^(-b)/b, while sine minus base ACUE is asymptotic to e^(-b)/b² in normalized I. The failure therefore persists even after the finite-height error is removed. The upper deficit is larger by order b². These are statements about the checked bounds, not every consequence of RH.
3. The RH estimate for sum Lambda(n)² has the stated main terms x log x-x. Partial summation cancels the log x terms and leaves (1/2)log²x+O(1) for the sum divided by n. A decreasing exponential weight has bounded total variation, so the bounded primitive error stays O(1) uniformly in b. The missing interval between log N/log T and one gives the displayed endpoint error. All normalized errors vanish relative to e^(-b)/b² for b=o(log log T), including the second scale.
4. The factors two in the residual statistic are correct. Substituting r_S(b)=e^(-b)/b gives -b e^(-2b)+(b/2)e^(-4b). The difference from ACUE is b²[H(b)-H(2b)], tending to 3/4. The additive AH parameter contributes exactly equal constants with opposite signs, so a limit for p_0(T) is unnecessary.
5. The fixed-width AH errors permit an existential stepwise increasing diagonal. Choosing their errors at widths j and 2j below e^(-2j)/j³ makes the amplified error O(1/j). This does not justify a predetermined formula for b(T).

## An explicit sufficient uniform quantifier

To avoid ambiguity in the phrase “a selectable increasing range”, the following is one precise sufficient arithmetic target. Find an increasing G(T) tending to infinity with G(T)=o(log log T), for which

\[
\lim_{B\to\infty}\liminf_{T\to\infty}
\inf_{B\le b\le G(T)}\mathcal C_T(b)>-\frac34.
\tag{R}
\]

The intervals are nonempty for every fixed B once T is sufficiently large. If (R) holds, choose the AH diagonal under the envelope G(T). Along that diagonal the statistic tends to -3/4 by the reviewed argument, contradicting (R). The outer limit in (R) exists as an extended monotone limit of the inner lower bounds. Equivalently, one may supply a strict uniform gap for all sufficiently large lower cutoffs B.

This condition does not assert an exact GUE law at each fixed b. It is stronger than a statement at a single predetermined growing b(T), because such a statement might be incompatible with the unknown AH convergence rate. It is weaker than proving both individual residual asymptotics (AE). None of these arithmetic conditions is proved in the report or this review.

The source audit and model algebra are useful because they identify the required first correction and rule out two incorrect rate objections. They supply no positive improvement in the current lower bound. No additional numerical experiment, parameter scan or formal verification was performed for this review.
