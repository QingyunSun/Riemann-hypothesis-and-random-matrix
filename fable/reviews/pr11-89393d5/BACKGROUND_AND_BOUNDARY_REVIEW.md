# Independent background and boundary objections to the same Fable snapshot

Date: 2026-09-05. These findings came from the existing Astra coordination task's independent mathematical intake of commit `89393d5da61a45561ed199330c5b836f47fcd629`. Root checked the quoted source passages and the elementary algebra/counterexamples below. The original proposer files remain unchanged. This is a negative scope audit, not a complete acceptance review of every earlier constant or lemma.

## 1. A reversed inequality in the uniform CUE gap tail

In `r1_cue_background.md`, Proposition 3.3 regime 2 has L>4N^(1/3) and a preceding bound 16.47/N. Its next step replaces this by 16.47*64/L^3 as an upper bound. The inequality goes in the opposite direction: L^3>64N implies 1/N>64/L^3. The displayed uniform constant 1054, and the downstream constants 1055 derived from it, are not established by this proof as written.

A possible elementary repair is to use the deterministic fact delta_min<=2pi/N for N points on a circle of circumference 2pi. The event is empty for L>=2pi N^(1/3). In the remaining part of regime 2, 1/N<(2pi)^3/L^3, so the preceding bound implies a constant below 4100 in place of 1054. If all earlier estimates are accepted, a conservative 4101 can propagate through the stated stiffness tails. This repair preserves the qualitative tightness route. This review has not certified all the preceding numerical constants, and does not silently edit the source or label 1055 verified.

## 2. The C-beta-E local density hypothesis has the wrong scaling

The displayed BB-LD compares the n-point correlation density to N^n times the unscaled angular Vandermonde to power beta with constants independent of N. It is already false for beta=2, n=2. The exact CUE formula is

\[
\rho_2(\theta,\theta+d)
=\frac1{4\pi^2}\left[N^2-\left(\frac{\sin(Nd/2)}{\sin(d/2)}\right)^2\right]
=\frac{N^2(N^2-1)}{48\pi^2}d^2+O_N(d^4).
\]

Hence rho_2/(N^2 d^2) grows like N^2, contradicting an N-independent comparison. A microscopic statement must include scaled distances Nd, or the corresponding prefactor N^(n+beta*n*(n-1)/2), and specify its domain and the remaining marginal bounds. The source's later attempts at revised exponent counting do not fix the false starting definition merely by calling its normalization local. No general-beta density theorem is supplied by this audit.

The source's partition function formula is also wrong in its stated Lebesgue-angle convention, although it is marked unused. At N=2,beta=2 direct integration of 2-2cos(theta_1-theta_2) gives 2(2pi)^2. The displayed product formula gives 4(2pi)^2. This is an elementary normalization check, independent of a general Selberg integral.

## 3. Uniform one-point intensity does not control a selected close pair

The C-beta-E report attempts to obtain the one-sided density event needed for the selected pair from rho_1=N/(2pi). That implication is invalid. Take a deterministic cluster of N distinct angles in an arbitrarily short arc, with a unique smallest pair gap, and rotate the entire cluster by a uniform angle. The one-point intensity is exactly N/(2pi), because each labelled point is marginally uniform. Every realization still contains the same tight cluster. The selected pair's nearby counting function, and its sum of inverse-square distances to other points, can be arbitrarily large.

This example is not C-beta-E. It shows precisely that the claimed one-point input is insufficient. A proof for C-beta-E must use its additional correlation structure, Palm estimates, or an independently proved uniform density event. Static rotational invariance supplies none of these by itself. Claims A3(b)/(c) cannot be accepted from the stated one-point argument.

The assertion that DBM is the only known route to the required density theorem is a methodological opinion. It is not a mathematical proposition with status proved, and this audit makes no exhaustive claim about the literature.

## 4. Static stiffness does not automatically persist to collision

The CUE depth Theorem 2 explicitly assumes B*-0. The Theorem B repair requires stability on a time window and its kappa_0 condition. Tightness of S*(0)/N^2 is useful but is not the same assertion as a bound along the selected pair's evolution. The arc-sum lower bound in Lemma W may support a proof; its sufficient event H_C still has to be established for the selected pair before importing the depth conclusion.

The current intake therefore preserves both the conditional theorem and its missing event. It does not relabel the CUE or general-beta depth law as unconditional merely because a static background estimate was proposed.

## 5. A periodized window has an artificial gap

In `r1_levelB_barrier.md` the periodized version claims that a small normalized depth implies an actual zeta gap below 1/2 without additional hypotheses. Periodizing a finite real window of length H_T introduces the wrap gap H_T-(last-first). The smallest circle gap can be this artificial gap, with no small consecutive gap among the original zeros. A circle depth theorem alone identifies a circle gap, not necessarily a genuine zeta gap.

For example, points 0,1,...,n-1 in a window of length n-1+epsilon have all internal gaps one and circular wrap gap epsilon. This does not make a statement about actual zeta windows; it disproves the unqualified finite-window inference. A non-wrap witness or a valid boundary construction is needed for transfer. The actual-flow non-return/truncation assumptions must also remain explicit.

## Accepted use

The reports contain useful candidate lemmas and clearly exposed conditional inputs. The objections above identify specific places needing repair, not a refutation of every heat-flow idea. Until repaired and independently reviewed, these source status labels must not be used to claim a C-beta-E universality theorem, a true-zeta depth bound, or AH failure. The present main line remains the independently reviewed actual-prime estimates in Rounds 10 and 11.
