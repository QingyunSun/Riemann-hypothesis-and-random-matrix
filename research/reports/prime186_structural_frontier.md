# The 186 structural mechanism and a finite complementary-support frontier

Date: 2026-09-05. Scope: primary-source reconstruction, an exact finite arithmetic example, a proved allocation frontier, and a concrete next obligation for $k=39$. **No smaller prime-gap bound is claimed.**

## 1. What is being transferred

The important mechanism in the 186 paper is an enlargement of the **admissible coefficient support for existing restricted-modulus distribution estimates**. It is not a replacement of the whole arithmetic input by a larger scalar exponent of distribution.

The sources used here are [*Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), especially Definition 2.1, Lemma 2.2, Proposition 2.3, §4.2, and Proposition 4.6; its [research record](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps_abridged_cot.pdf), especially pp.25–27; and the [official certificate repository](https://github.com/openai/PrimeGaps186) at the locally inspected commit `61340d0b74163003b32756bb16e91d9209a5e330`.

The user's [Weijie Su post](https://x.com/weijie444/status/2095600108956262911) could not be retrieved in this run: X returned HTTP 403. Its wording is therefore not quoted or independently authenticated here. The mathematical mechanism below is reconstructed directly from the supplied primary paper.

## 2. The actual combined divisor, including shared primes

For $Y\ge1$, order-$r$ dense divisibility asks that for every allocation $j+k=r-1$ and every target $1\le U\le Ym$, one can write

\[
 m=uv,\quad U/Y\le v\le U,\quad
 u\in\mathcal D^{(j)}(Y),\quad v\in\mathcal D^{(k)}(Y).
\]

The allocation is universal: finding one convenient factorization is not sufficient. The prime-factor criterion used by the paper is

\[
 p^r\le YQ_{<p}\quad(p\mid Q,\ p>Y)
 \quad\Longrightarrow\quad Q\in\mathcal D^{(r)}(Y),
\]

for squarefree $Q$, where $Q_{<p}$ is the product of the prime factors below $p$. This is a sufficient criterion; failure of it does not imply failure of dense divisibility.

In a mixed sieve pairing, the modulus is $WQ$, with

\[
 Q=[D,E].
\]

Proposition 2.3 takes nondecreasing $f,g\ge1$ with $f(p)g(p)=p^3$, fixed budgets $A_0C_0\le XY$, and requires

\[
\begin{array}{ll}
 f(p)D_{\ge p}\le A_0,&g(p)\le C_0\quad(p\mid D,\ p>Y),\\
 g(p)E_{\ge p}\le C_0,&f(p)\le A_0\quad(p\mid E,\ p>Y).
\end{array}
\]

When $Q>X$, these imply triple dense divisibility of $Q$. To see the crucial point, fix $p\mid D$. If $E$ has a prime $q\ge p$, take the smallest such $q$. Monotonicity yields

\[
 g(p)E_{\ge p}\le g(q)E_{\ge q}\le C_0.
\]

If $E$ has no such prime, the explicit opposite-root condition $g(p)\le C_0$ supplies the same conclusion. Therefore

\[
 p^3D_{\ge p}E_{\ge p}\le A_0C_0\le XY,
\]

and

\[
 p^3\le\frac{XY}{Q_{\ge p}}
      =\frac XQ YQ_{<p}<YQ_{<p}.
\]

The same argument handles a prime belonging only to $E$. It uses $Q_{\ge p}\mid D_{\ge p}E_{\ge p}$, not equality. Shared primes are allowed. Replacing the assumption $[D,E]>X$ by $DE>X$ would be invalid: a large gcd can make the actual modulus much smaller.

Deleting prime factors only decreases the relevant tails and maxima, so the root predicates remain valid for coefficient divisors. This is essential for the inverse Selberg transform. It is stronger bookkeeping than saying a chosen root happened to be densely divisible, because dense divisibility of a number does not automatically pass to every divisor with the same $Y$.

## 3. An exact integer example of complementary help

Take

\[
 Y=10,\quad D=330=2\cdot3\cdot5\cdot11,
 \quad E=455=5\cdot7\cdot13,
 \quad Q=[D,E]=30030.
\]

Both roots contain a prime greater than $Y$, and they share the factor 5. Let

\[
 f(p)=p,\quad g(p)=p^2,\quad A_0=121,
 \quad C_0=2197,\quad X=27000.
\]

Then $A_0C_0=265837\le270000=XY$, and $Q>X$. All four rootwise requirements hold: the only activated prime in $D$ is 11, and the only activated prime in $E$ is 13. For the merged modulus the cubic checks are

\[
 11^3=1331\le10(2\cdot3\cdot5\cdot7)=2100,
\]

\[
 13^3=2197\le10(2\cdot3\cdot5\cdot7\cdot11)=23100.
\]

The attached exact check also verifies Definition 2.1 directly by recursive divisor enumeration. It confirms $Q\in\mathcal D^{(3)}(10)$, but $E\notin\mathcal D^{(3)}(10)$. For the latter failure, take allocation $(j,k)=(2,0)$ and target $U=11$: no divisor $v\in[11/10,11]$ leaves $E/v$ doubly 10-densely divisible.

Thus complementary factors really can produce a suitable combined modulus even when one root itself lacks the required triple property. The calculation is finite and exact; it does not establish an asymptotic prime distribution estimate by itself.

## 4. Why a scalar exponent misses the new geometry

Write $R=x^{\rho_*}$, $u_p=\log_Rp$, $s_D=\log_RD$, and $Y=R^\xi$. The logarithmic form of the order-three split uses nondecreasing functions

\[
 \phi_D(u)+\phi_E(u)=3u,
\]

with owner-tail statistic

\[
 H_{\phi,\xi}(D)=
 \max_{p\mid D,\ u_p>\xi}
 \left(\sum_{q\mid D,\ q\ge p}u_q+\phi(u_p)\right).
\]

For a source band $Q>R^B$, outer and inner total radii $S,T$, and $a=B-T,b=B-S$, the predicates are

\[
 s_D\le a\quad\text{or}\quad
 [H_{\phi_D,\xi}(D)\le A,\ \phi_E(M_\xi(D))\le C],
\]

\[
 s_E\le b\quad\text{or}\quad
 [H_{\phi_E,\xi}(E)\le C,\ \phi_D(M_\xi(E))\le A],
 \qquad A+C\le B+\xi.
\]

The small-radius alternatives are genuinely safe: if $s_D\le B-T$, the size of $[D,E]$ cannot exceed the band threshold. Otherwise each activated prime and its full inclusive tail matters. Two roots with the same total logarithmic size can have different admissibility because their prime partitions differ.

Distribution estimates still restrict both the modulus level and its smoothness/dense-divisibility parameter. For example, the full-prime order-three condition in Corollary 2.19 is $240\omega+80\delta<3$, with modulus level $x^{1/2+2\omega}$ and $Y=x^\delta$. The source ladder trades these parameters across bands; increasing the level generally reduces the allowable $\delta$. It is not legitimate to retain a high level and simultaneously borrow the less restrictive support from a lower-level row.

The enlarged minorant mixed pairing has physical product bound $x^{.5252997}$, while the full-prime mixed pairing uses the slightly smaller range. The minorant's negative part, inner-square pairings, and support restoration remain separate debts. A scalar calculation resembling $M_k>2/\theta$ on an unrestricted simplex omits exactly the fragment geometry that makes this improvement work.

## 5. A proved finite frontier for every monotone allocation

Here is an inexpensive certificate useful before recomputing physical integrals.

Fix one active order-three row and owner ceilings $A,C$. Suppose an activated outer root can have largest fragment $u$, and an activated inner root can have largest fragment $v$, with $u\ge v>0$. Their remaining mass may consist of smaller fragments or the smooth seed. Because there is no larger fragment than a largest witness, the necessary owner and opposite-root constraints include

\[
 u+\phi_D(u)\le A,\qquad 3u-\phi_D(u)\le C,
\]

\[
 4v-\phi_D(v)\le C,\qquad\phi_D(v)\le A.
\]

Monotonicity gives $\phi_D(v)\le\phi_D(u)$. Two explicit nonnegative-sum identities give the frontier:

\[
\boxed{4u\le A+C,\qquad u+4v\le A+C.}
\]

Indeed,

\[
 A+C-4u=(A-u-\phi_D(u))+(C-3u+\phi_D(u)),
\]

\[
 A+C-u-4v=(A-u-\phi_D(u))+(C-4v+\phi_D(v))
             +(\phi_D(u)-\phi_D(v)).
\]

These are exact dual certificates, requiring no numerical optimizer. They apply to active predicates, not to roots in the safe small-radius alternative. If $v\ge u$, the symmetric second inequality is $4u+v\le A+C$.

The paper's capped allocation is

\[
 \phi_D(t)=\min(3t/2,L),\quad\phi_E(t)=3t-\phi_D(t).
\]

In its relevant plateau regime, the largest-fragment caps are

\[
 u=A-L,\qquad v=(C+L)/4,
\]

so **$u+4v=A+C$ exactly**. The published caps already lie on a Pareto boundary for arbitrary monotone allocations with these fixed ceilings. No cleverer piecewise allocation can simultaneously enlarge both these largest-fragment allowances. It can redistribute them, change which smaller tails are admitted, change the budgets, or leave this particular support template. Those are distinct possibilities.

This is a largest-fragment obstruction, not a universal no-go theorem for improving the whole sieve. In particular, a frontier point can remain suboptimal for the weighted integral because the outer and inner losses are very unequal.

## 6. Exact location of the current frontier and a bounded next search

For the nonterminal tight rows generated by the official ladder recurrence, put

\[
 \rho=.262499,\quad\rho_*=.2624989,\quad e=10^{-7}/\rho,
 \quad A=S+e/2,\quad C=T+e/2.
\]

The recurrence makes these ceilings independent of the individual tight row. The base and enlarged radii $T_0,T_1$ differ, so the old and new ladders have different $C$. These formulas and all values below use exact rational inputs.

For the plateau family the extreme outer endpoint is

\[
 L_{\min}=(3A-C)/4,
 \quad u_{\max}=(A+C)/4,
 \quad v=3(A+C)/16.
\]

The plateau validity range reaches $L\le3C/5$ here. The selected $L=(23/40)C=.575C$ is close to, but above, the smallest permitted value:

| Ladder | $L_{\min}/C$ | Current normalized $u$ | Current normalized $v$ | Maximum physical outer-cap gain to $L_{\min}$ | Corresponding physical inner-cap loss |
|---|---:|---:|---:|---:|---:|
| Old prime | .57319344847 | .49753017766 | .37486755082 | .00045147647 | .00011286912 |
| New minorant | .56962060366 | .49514387013 | .37650165272 | .00135022875 | .00033755719 |

Physical caps are $\rho_*$ times normalized caps. These gains are allowances in prime-factor exponents, not gains in the final sieve quotient.

At mesh $h=S/98304$, downward rounding of the two caps produces frontier slack smaller than $5h$. Consequently, the small slack in the actual integer masks is a rounding allowance, not an unexplored macroscopic joint enlargement. The JSON checks the exact rounding slack, constructs a valid allocation at four points on each frontier, and certifies infeasibility when both exact caps are increased by one cell.

A sensible bounded search is to vary the old and new plateaus **independently** inside their valid intervals while keeping every source row and opposite-root condition. A common choice below .57319344847 is invalid for the tight old rows, even though it may be allowed in the new rows. Since the global outer domain intersects both ladders and the base inner domain intersects their predicates, local improvement of one row cannot be reported as enlargement of the entire usable support.

The historical loss ledger puts about 89.5% of the published weighted restoration loss in the outer effective-order-$5/2$ class, versus about 4.66% in the corresponding enlarged-inner class. That asymmetry motivates testing this tradeoff, but does not prove the trade is beneficial: the derivatives of the physical integrals are not determined by the aggregate loss totals. The research record already reports experimenting with plateau allocations, so this proposal is a reproducible next test, not a novelty claim about discovering the plateau idea.

## 7. A more general finite-fragment allocation certificate

The frontier admits a practical extension beyond largest witnesses. Given finitely many candidate outer and inner fragment configurations, collect every activated witness size into ordered rational knots

\[
 0=u_0<u_1<\cdots<u_n,\qquad z_i=\phi_D(u_i).
\]

Monotonicity of both owners is exactly

\[
 0\le z_{i+1}-z_i\le3(u_{i+1}-u_i),\qquad z_0=0.
\]

An outer witness with inclusive tail $T_D(u_i)$ imposes

\[
 z_i\le A-T_D(u_i),
\]

and an inner witness imposes

\[
 z_i\ge3u_i+T_E(u_i)-C.
\]

Opposite-root constraints give the additional lower or upper bounds at each root's maximum. Combine them into intervals $\ell_i\le z_i\le r_i$, including $z_0=0$. These are rational difference constraints. Their feasibility can be checked explicitly:

\[
 z_i^{\min}=\max_j\{\ell_j-3\max(u_j-u_i,0)\}.
\]

There exists an admissible allocation iff $z_i^{\min}\le r_i$ for every $i$. The maximum of the displayed nondecreasing 3-Lipschitz functions has those same properties and is the least feasible lower envelope. If a constraint fails, the offending pair $(i,j)$ supplies the exact contradiction

\[
 \ell_j>r_i+3\max(u_j-u_i,0).
\]

If it succeeds, linear interpolation of the knot values, followed by a constant continuation for $\phi_D$, defines globally nondecreasing complementary functions. This proves feasibility of the finite candidate set. It does not by itself determine which candidates have enough integral weight to be worth retaining.

`prime186_frontier_checks.py` implements this exact feasibility engine using only the Python standard library. A useful next optimization can choose which high-weight fragment patterns to retain, use this engine to produce a feasible allocation or an infeasibility witness, and then evaluate the resulting full support. This separates a cheap geometric obstruction from the expensive physical integral calculation.

## 8. The concrete $k=39$ obligation

The next theorem is DHL[39,2], not merely another admissible tuple. A diameter-182 admissible 39-tuple was already checked in round 1, so that theorem would give $H_1\le182$. The unresolved obligation is to find and certify a 39-variable trial satisfying the **complete** inequality

\[
 \rho_*\left(
 J^-_{\lambda,H}-E_O^+
 -d_0\beta_{\rm old}^+
 -(1-b_h)\beta_{\rm new}^+
 \right)>I_H^+.
\]

Here $E_O$ pays for outer failures, while the two $\beta$ terms pay for the actual inner domains, including their intersection. The negative full-face term from the prime minorant remains present. The source checks for all mixed and inner-square moduli must hold with the final cell geometry. Replacing 40 by 39 changes the measure, marginal dimension, combinatorial coefficients, inward cell masks, and the integral values; none of those values can simply be inherited from the $k=40$ receipt.

A concrete next computation is:

1. Use $k=39$, initially retaining the published physical radii, source ladders, minorant, and its justified constants.
2. Keep the published 77-dimensional symmetric polynomial descriptor family as a reproducible starting space, and vary the old/new plateau or the finite-knot owner function with explicit feasibility certificates.
3. Freeze valid positive cover and Young parameters when assembling a quadratic form. Optimize the **support-restored** form against its denominator. The 77 coefficients are not a substitute for source validity.
4. For a promising vector, round its coefficients and all geometric parameters rationally, restore every source row and inward cap, and compute outward enclosures for the full displayed inequality. Only a positive final interval proves the desired sieve criterion.

A negative-definite upper certificate could prove failure of one fixed finite trial space and fixed support family. It would not rule out DHL[39,2] or other coefficient families. Conversely, a cap-only value above one remains merely a candidate until the deletion costs are paid.

There is one explicit loss-recovery option already visible in Proposition 4.6. The displayed proof actually retains

\[
 (1-\rho_*|b_h|C_{\rm op})\alpha,
 \qquad \alpha=\|(1-P_O)F\|^2,
\]

as a positive term before dropping it in the convenient sufficient criterion. A certified lower bound for $\alpha$, for example from disjoint known-failure regions, would supply a legitimate credit. Existing upper bounds for covered failure masses cannot be reused as that lower bound. The possible gain is unmeasured here and is not advertised as sufficient for $k=39$.

## 9. What was computed, and the exact remaining bottleneck

This round ran the exact integer example, the recursive definition check, eight rational frontier points, the cap-enlargement infeasibility witnesses, and the finite allocation-envelope engine. Runtime was about 0.0015 seconds. Files:

- `prime186_frontier_checks.py`
- `prime186_frontier_checks.json`
- this research note

No FLINT build, paid API call, or large numerical search was performed. The checks do not bypass the official certificate's signed-convolution startup regression: that certificate was not run in this round at all.

The bottleneck is the rigorous physical integral evaluation for the revised trial and its actual fragment support, not feasibility of the two-budget algebra. The published baseline involves 104 outer and 45 inner physical upper bounds plus cap bounds. Its official certificate specifies a corrected FLINT build. Geometry-only certificates can reject impossible support proposals and certify the allocation step, but they cannot supply those missing weighted integrals or the asymptotic distribution theorem.

The public Lean derivation remains conditional on its three documented project inputs, including the physical integral bounds. A rational support certificate verifies one component of the mathematical argument; it does not discharge those Lean inputs or create a new prime-gap theorem.

## 10. Structural lesson for the zeta programme

The transferable method is to constrain the **actual object produced by the mixed pairing**, distribute a fixed analytic budget between complementary factors, preserve the support under the algebraic transformations used in the proof, and charge the residual with a sign-correct quadratic inequality. In the prime problem the combined object is an lcm modulus and the needed property is dense divisibility. In a zeta mixed-moment problem, the corresponding object and the required distribution estimate must be identified anew.

The transfer does not authorize a larger Dirichlet support just because a similar factorization can be written down. One must prove that the actual mixed terms fall inside an available arithmetic estimate, or prove a new estimate for them. The centered-Gaussian pole correction from round 2 is an example of an additional term that survives a superficially favorable positivity argument. The useful frontier calculation above helps prevent spending research time on reallocations that cannot enlarge both sides even before those analytic issues are addressed.
