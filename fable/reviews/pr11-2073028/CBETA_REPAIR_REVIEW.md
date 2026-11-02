# Independent follow-up: CβE background repair at 2073028

**Verdict: partial repair, not an accepted proof as written.** The missing microscopic powers of N have been identified correctly, and the proposed triple-count exponents can be recovered under an explicit local three-point upper bound. However, the repaired text still contains a false finite-N identity, a false arbitrary-compact comparison, and a false uniform relative-error step. These defects prevent accepting the present BB-LD and Proposition 3.1 proof with their displayed status tags. The conditional replacement below is an ordinary mathematical derivation, not a proof of general-β BB-LD or a new CβE depth theorem.

Reviewed source: the preserved `PR11_2073028-source/r1_cbe_background.md`, with cross-checks against its companion `r1_cue_background.md`. Source SHA-256 values, exact line ranges, and the final review hash are in `CBETA_REPAIR_RECEIPT.json`. No source was edited, no Fable session was invoked, and no Monte Carlo run or large computation was repeated.

## 1. Coverage and change from the previous intake

The earlier independent `research-round3/fable_heat_sync_review.md` audited public SHA `a408e7050fffc74459b3c83fafa5ac03c8b7dea6`, where these written heat reports were absent. Its conclusions about that snapshot's evidence availability remain historically accurate. The present snapshot supplies the reports, including an explicit account of Fable's internal refutations. This follow-up independently checks the repaired mathematics; it does not infer validity from an internal refuter's completion status.

| Issue | Current source lines | Independent conclusion |
|---|---:|---|
| Missing N-rescaling in the old local density comparison | CβE 3–14, 95–109 | The diagnosis is correct. The replacement needs a power-distance comparator or an explicitly restricted sine cutoff. |
| Exact finite-N CUE two-point function | CβE 99–101, 117–123 | Incorrect as written: the sine-kernel limit was substituted for the finite-N kernel. |
| Claimed comparison on any compact rescaled interval | CβE 111–123 | False if the interval reaches 2π. The upper comparison fails at an exact zero of the proposed comparator. |
| Uniform relative replacement of the third distance | CβE 202–218 | False near an endpoint; the quoted N error exponent is also wrong. |
| Triple expectation exponents | CβE 194–253 | Recoverable conditionally by the direct integral in §3 below. Retain the finite-N correction and the order of limits. |
| BB-LD proved for β=1,2,4; general-β universality implication | CβE 137–168 | The claimed proofs are not supplied. Neither the repaired two-point check nor an unquantified universality citation establishes the needed three-point bound. |

## 2. Exact finite-N correction and explicit counterexamples

The companion CUE report, lines 52–55 and 145–146, correctly gives the ordered factorial correlation kernel. With q=Nd and N≥2,

\[
\rho_2(0,d)=\left(\frac N{2\pi}\right)^2
\left[1-\left(\frac{\sin(q/2)}{N\sin(q/(2N))}\right)^2\right].
\]

For fixed q, its normalized limit as N→∞ is \(1-\operatorname{sinc}(q/2)^2\). At fixed finite N, the Taylor coefficient at q=0 is instead

\[
1-\left(\frac{\sin(q/2)}{N\sin(q/(2N))}\right)^2
=\frac{1-N^{-2}}{12}q^2+O_N(q^4).
\]

Consequently the ratio to \((2\sin(q/2))^2\) tends to \((1-N^{-2})/12\), not 1/12. This does not destroy the intended small-q scaling, but it invalidates the claimed exact finite-N verification.

At q=2π, taking d=2π/N, the exact normalized density equals 1, whereas \((2\sin(q/2))^2=0\). This is an admissible circular separation for every N≥2. Thus no finite K gives the claimed **upper** bound there. The lower inequality alone becomes the harmless inequality 0≤ρ₂; it is the two-sided comparison and its bounded-ratio assertion that fail. For q beyond 2π the unsquared sine can also be negative, making its arbitrary-real-β power unsuitable without absolute values.

A minimal definition repair is to use \(\prod(Nd_{ij})^\beta\), with a fixed bounded microscopic cutoff, or to restrict the sine formulation to \(s_0<2\pi\). The application below only needs an upper bound for n=3. For the two-point CUE case on any fixed \(0\le q\le s_0<2\pi\), the corrected finite-N ratio does have uniform positive finite bounds for N≥2: away from q=0 it follows from the strict triangle inequality for the geometric sum, compactness, and convergence to the sine limit; at q=0 the displayed Taylor coefficient is uniformly positive. This observation does not establish the n=3 general-β claim. A two-sided n-point assertion also requires N₀≥n.

For the second error, take an endpoint pair x=0, y=u with u=ε/2, and put the third point at z=−v with v=ε²/w. When ε/w→0, z is closest to x, and

\[
v'=u+v,\qquad \frac{v'}v=1+\frac{w}{2\varepsilon}\longrightarrow\infty.
\]

Hence \(v'=v(1+O(\varepsilon/w))\) cannot hold uniformly on the integration region. Lipschitz continuity of sine controls an absolute error; it cannot supply a relative error at a vanishing sine. Independently, \(\varepsilon/w=(L/c)N^{-1/(\beta+1)}\) is not O(N⁻¹) for any fixed β>0. Finally, the largest distance is bounded by w+ε, not by max(w,ε): the cutoff check must require c+Nε≤s₀. Taking fixed c<s₀ and then sufficiently large N resolves that condition.

## 3. A correct conditional triple estimate

Assume, for every triple with all \(Nd_{ij}\le s_0\), the following **upper** bound:

\[
\rho_3(x,y,z)\le \frac{K}{(2\pi)^3}
N^{3+3\beta}d(x,y)^\beta d(x,z)^\beta d(y,z)^\beta. \tag{U3}
\]

This is the exact input needed here. It follows from a valid restricted sine upper bound using \(2\sin(t/2)\le t\), but is not proved here for general β.

Let T count ordered distinct triples with d(x,y)≤ε and dist(z,{x,y})≤w. Require ε+w<π and N(ε+w)≤s₀. Apply the union bound for the two endpoint neighborhoods, anchor x on the circle, and use signed coordinates u=y−x and v=z−x. Then

\[
\begin{aligned}
\mathbb ET
&\le 2(2\pi)\frac{K N^{3+3\beta}}{(2\pi)^3}
\int_{-\varepsilon}^{\varepsilon}\int_{-w}^{w}
|u|^\beta|v|^\beta(|u|+|v|)^\beta\,dv\,du\\
&=\frac{2K}{\pi^2}N^{3+3\beta}
\int_0^\varepsilon\int_0^w u^\beta v^\beta(u+v)^\beta\,dv\,du. \tag{1}
\end{aligned}
\]

All three factors remain present. The endpoint union bound deliberately overcounts overlapping neighborhoods and is therefore safe.

For a simple bound valid without ε/w tending to zero, replace (u+v)^β by (ε+w)^β in (1). With ε=LN^{−1−1/(β+1)} and w=c/N this gives

\[
\boxed{\mathbb ET\le
\frac{2K}{\pi^2(\beta+1)^2}
L^{\beta+1}c^{\beta+1}
\bigl(c+LN^{-1/(\beta+1)}\bigr)^\beta.} \tag{2}
\]

Thus the intended exponents survive, under (U3), after taking N→∞ at fixed L,c and then c↓0.

For the sharper leading constant put δ=ε/w. Scaling both integration variables in (1) gives

\[
\mathbb ET\le\frac{2K}{\pi^2}L^{\beta+1}c^{2\beta+1}J_\beta(\delta),\qquad
J_\beta(\delta)=\int_0^1\int_0^1s^\beta t^\beta(t+\delta s)^\beta\,dt\,ds.
\]

For 0≤δ≤1,

\[
J_\beta(\delta)\le\frac1{(\beta+1)(2\beta+1)}
\begin{cases}
1+\delta^\beta,&0<\beta\le1,\\
1+\dfrac{\beta2^{\beta-1}(2\beta+1)}{\beta+2}\delta,&\beta\ge1.
\end{cases} \tag{3}
\]

The first case uses subadditivity of t↦t^β. The second uses the mean-value estimate \((t+\delta s)^\beta-t^\beta\le\beta2^{\beta-1}\delta s\) on the unit square. This proves the leading asymptotic bound by integration, without the false pointwise comparison. It also makes its lack of uniformity in c↓0 before N→∞ explicit.

For β=2 the integral in (1) is exactly

\[
\frac{\varepsilon^3w^5}{15}
+\frac{\varepsilon^4w^4}{8}
+\frac{\varepsilon^5w^3}{15}.
\]

Using the stronger CUE coefficient \(\rho_3\le C_3(N)\prod d_{ij}^2\) yields \(16\pi C_3(N)\) times this polynomial, precisely the bound stated in the companion CUE report, lines 226–240. The small symbolic check verifies this integral, the finite-N Taylor coefficients, and the q=2π counterexample; it does not certify general-β density estimates.

If E₁ refers specifically to the closest pair, only \(E_1\subseteq\{T\ge1\}\) is required. The equality asserted at CβE line 246 is generally false, because a different short pair may have a nearby third point. The correct inclusion still gives the intended Markov upper bound.

## 4. Status and remaining scope

Accept the normalization diagnosis and the conditional consequence (1)–(3). Do not accept the current proof of Proposition 3.1 or the “[P] for β∈{1,2,4}” BB-LD row as written. An explicit source or proof for the actual n=3 uniform upper bound remains necessary; β=1,4 are only recalled in the source, and ordinary weak local-process convergence by itself does not justify density control on the shrinking rescaled gap \(N\varepsilon\to0\). The claimed “exactly” equivalent universality formulation at lines 144–148 and its qualitative consequence at lines 164–167 have not been established by this report. This is a missing implication, not a claim that the required bounds are absent from all literature.

This bounded review does not audit Fable's full stiffness/heat-flow argument, the recalled Feng–Wei theorem range, the seed-sweep data, or the methodological claim that DBM is the only route. Those items receive no status upgrade here.

One additional elementary normalization error was noticed but is not used above: at β=2,N=2 the partition function written at lines 58–60 equals \(4(2\pi)^2\), whereas direct integration of \(2-2\cos(\theta_1-\theta_2)\) gives \(2(2\pi)^2\). The source explicitly says that formula is unused; it should not be copied into a handoff as verified.

The finite checks are reproducible with `python3 check_cbeta_repair.py` from this intake directory and require SymPy. No numerical research claim, ζ statement, or new famous-conjecture result follows from this review.
