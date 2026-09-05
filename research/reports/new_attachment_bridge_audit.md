# Audit of the two newly supplied heat-depth bridge manuscripts

Date: 2026-09-05. Author: internal Astra agent `prime186`. Scope: a bounded source and proof audit, with two finite-dimensional counterexamples. This is an audit of claims, not a claim to have refuted the Riemann-zeta Alternative Hypothesis.

## 1. Outcome, including a correction to our own previous audit

The finite-dimensional first-collision bridge is useful and survives with precise hypotheses. Two stronger implications in the supplied reasoning fail: the pair that first collides need not have the initially smallest gap, and inverse-Gram blowup need not produce blowup of a marked heat-depth derivative. Both failures are demonstrated below with explicit formulas; the first also has an exact rational Sturm certificate.

**Our previous source judgment also needs correction.** It is not correct to say that the Lagarias–Rodgers hard-core parameter and the number $0.606894$ have no connection in the primary literature. Their paper *Band-limited mimicry of point processes by point processes supported on a lattice*, §5, printed p.19, explicitly defines $T_1$ and its hard-core supremum (mu). It proves the lower bound through its earlier construction and proposes that a modification of the Carneiro et al. pair-correlation method should give the upper bound $0.606894$. That proposed modification is not proved there. The incoming second attachment largely preserves this distinction in its opening discussion; passages calling the bound a published, proved theorem do not. [Primary PDF](https://par.nsf.gov/servlets/purl/10187059), [arXiv record](https://arxiv.org/abs/1907.03391).

The correct source ledger is therefore:

| Object or assertion | Correct status |
|---|---|
| The class $T_1$ and hard-core supremum (mu) | Explicitly defined in the 1907.03391 paper, §5 |
| $mu\ge 1/2$ | Supported by their constructed mimicking process |
| $mu\le .606894$ | They explicitly suggest a modified existing method should establish it; no proof is supplied in that passage |
| $mu=1/2$ | A possibility they propose, not a theorem |
| $T_1$ consists by definition of stationary processes | Inaccurate: the stated class is all uniformly locally moment-bounded processes mimicking the sine process at bandwidth 1; stationarity is not an additional condition in that definition |
| The .606894 footnote in the different paper 1905.12123 | A positive-proportion small-gap result for zeta zeros, with a different quantifier |

The source error arose from inspecting the higher-correlations paper while overlooking the companion paper's §5. The authoritative handoff should correct that error explicitly, rather than retain an unjustified criticism of the incoming manuscript.

## 2. Inputs and evidence

The two audited inputs are:

1. `research/incoming/heat_depth_classification_proposal.md`: the finite heat polynomial, single-defect ACUE model, nonlinear transversality, marked Gram directions, and proposed dynamic separation programme.
2. `research/incoming/hard_gap_depth_bridge_proposal.md`: the claimed hard-core/heat-depth bridge and proposed arithmetic consequences.

Reproducible evidence in `research/bridge-audit/` (the primary PDF and text are retained in the adjacent local archive, with the hash below):

- `attachment_bridge_checks.py`: exact rational Sturm and symbolic derivative checks.
- `attachment_bridge_checks.json`: full heat polynomial, discriminant coefficients, rational intervals, root counts, symbolic formulas, and runtime.
- `lagarias-rodgers-bandlimited-1907.03391.pdf`: downloaded from the NSF primary-author manuscript URL above, 544836 bytes.
- `lagarias-rodgers-bandlimited-1907.03391.txt`: `pdftotext -layout` extraction. Lines 1058–1064 contain the decisive §5 passage; the PDF page is printed p.19 and is also the nineteenth PDF page.

PDF SHA256: `a638b6be50dd919d1866085be29836f65ed4ce50f7caac14ae372b190b82e315`.

Historical finite-enumeration evidence is in `historical/riemann-rmt/impostors_paper.md`, especially its table around lines 183–208. That historical draft itself still contains some superseded source claims elsewhere; it is evidence for the archived calculations, not an authority that overrides primary sources.

## 3. Fix the sign convention before comparing formulas

For a degree-$N$ polynomial with all roots on the circle, the supplied convention is

\[
 P_t(z)=\sum_{k=0}^N a_k e^{-t k(N-k)}z^k.
\]

Increasing $t$ is the repulsive, real-root-preserving direction after converting to circle angles. Let $D=-\Lambda\ge0$ denote the time traveled in the opposite direction from $t=0$ to the first loss of all-circle-rootedness. Thus $s=-t\ge0$ is the attractive direction. After centering the trigonometric polynomial by $e^{-iN\theta/2}$, the common scalar factor can be discarded and evolution in $s$ is ordinary scalar heat $e^{s\partial_\theta^2}$.

For a finite real polynomial the corresponding convention is

\[
 H_s(x)=e^{s\partial_x^2}P(x),\qquad
 \frac{dx_j}{ds}=-2\sum_{k\ne j}\frac1{x_j-x_k}.
\]

The real-line ODE displayed in the second attachment uses $t=-s$, so its sign is correct. The two conventions must not be combined without reversing time.

The exceptional circle clocks have $P(z)=z^N-c$, up to scale and rotation. All intermediate coefficients vanish, so this flow leaves their roots fixed. Their depth is $D=+\infty$, equivalently $\Lambda=-\infty$. They are not generic finite collision points of a discriminant hypersurface.

## 4. The exact real-line identity: valid for the colliding pair

Assume all the following on an interval $-D<t\le0$:

- The roots are real and simple and can be labeled in increasing order.
- One adjacent pair $x_j(t)<x_{j+1}(t)$ collides at $t=-D$.
- The finite sum below is defined, or in an infinite model the principal-value force and the difference of forces are justified and the displayed screening sum and integral converge.

Put

\[
 d(t)=x_{j+1}(t)-x_j(t),\qquad
 S(t)=\sum_{i\ne j,j+1}
 \frac1{(x_i-x_{j+1})(x_i-x_j)}\ge0.
\]

Positivity follows because every other root lies outside the adjacent interval. Subtracting the two repulsive root equations gives

\[
 d'=\frac4d-2dS,\qquad (d^2)'=8-4d^2S.
\]

Integration from the collision time to zero gives the exact identity

\[
 \boxed{D=\frac{d_*^2}{8}
       +\frac12\int_{-D}^0 d(t)^2S(t)\,dt},
 \qquad d_*:=d(0).
\]

If $m_0$ is the minimum of all initial gaps, the legitimate consequence is

\[
 D\ge\frac{d_*^2}{8}\ge\frac{m_0^2}{8}.
\]

One may write an exact identity with $m_0$, but then its nonnegative correction has **two** terms:

\[
 D=\frac{m_0^2}{8}
   +\underbrace{\frac{d_*^2-m_0^2}{8}}_{\text{initial pair-selection correction}}
   +\underbrace{\frac12\int_{-D}^0d(t)^2S(t)\,dt}_{\text{screening correction}}.
\]

The manuscript's replacement of $d_*$ by $m_0$ while retaining only the screening integral is false in general. It is not a harmless choice of notation.

## 5. Exact finite counterexample: the smallest gap does not collide first

Take

\[
 P(x)=x(x^2-1)\left((x-100)^2-\frac{121}{400}\right),
 \qquad H_s=e^{s\partial_x^2}P.
\]

Its roots are

\[
 -1,\quad0,\quad1,\quad100-\frac{11}{20},\quad100+\frac{11}{20}.
\]

The two minimum gaps are 1. The remote pair has the strictly larger gap (11/10).

The heat polynomial is exactly

\[
\begin{aligned}
H_s(x)={}&x^5-200x^4+
 \left(\frac{3999479}{400}+20s\right)x^3
 +(200-2400s)x^2\\
&+\left(-\frac{3999879}{400}
       +\frac{11998437}{200}s+60s^2\right)x
 +400s-2400s^2.
\end{aligned}
\]

The attached script performs exact rational Sturm calculations, not floating-point root classification:

1. The degree-10 discriminant in $s$ is squarefree.
2. It has no root in $0<s<151/1000$, and exactly one root in $151/1000<s<19/125$.
3. That root has the exact rational enclosure

\[
 \frac{12999}{85936}<D<\frac{53965}{356761},
\]

or $0.15126373114876188<D<0.15126373118137912$.

4. At $s=0$ and $s=151/1000$, there are three real roots in ([-2,2]) and two in ([98,102]).
5. At $s=19/125$, the first interval still contains three real roots, while the second contains none; there are exactly three real roots in total.
6. At each of the four interval endpoints, $H_s$ has no zero for $0\le s\le19/125$.

A real polynomial with fixed nonzero leading coefficient cannot lose a simple real root to a nonreal conjugate pair without a real multiple-root event. The discriminant counts exclude earlier events; the interval boundary checks prevent exchanging the two root groups. Therefore the unique first event is collision of the pair initially at $100\pm11/20$, not either initial minimum pair.

For this example the missing term in the incorrect identity is

\[
 \frac{(11/10)^2-1}{8}=\frac{21}{800}=0.02625.
\]

The remote pair's screening correction is small and positive: (D-121/800) is about $1.3731\times10^{-5}$. This is consistent with the exact identity, while the initially denser three-root cluster postpones its own collision.

There is a simple structural reason the example exists. As the remote center $R\to\infty$, the local heat flow of $x(x^2-1)$ reaches its triple collision at $s=1/6$, whereas the isolated gap (11/10) collapses at $s=121/800<1/6$. The rational example above certifies this effect at the finite choice $R=100$.

This is a theorem about finite scalar heat flow. It invalidates a universal minimum-first premise; it does not contradict the valid lower bound $D\ge m_0^2/8$.

## 6. The circle bound, its domain, and the ACUE consequence

For an adjacent circle gap $\Delta$, the repulsive equation is

\[
 \Delta'=2\cot(\Delta/2)-\sin(\Delta/2)B(t),\qquad B(t)\ge0.
\]

Here $B$ is the sum of reciprocal products of the two sine factors involving each other root. With the other roots outside the lifted adjacent arc, these products are positive.

For $0\le\Delta<\pi$, define

\[
 q(\Delta)=-\log\cos(\Delta/2).
\]

Then

\[
 \frac{d}{dt}q(\Delta(t))
 =1-\frac{\sin^2(\Delta/2)}{2\cos(\Delta/2)}B(t)\le1.
\]

For a tracked pair that collides in the attractive direction, its gap stays below $\pi$ throughout that part of its history. Indeed, in attractive time, the gap derivative at or above $\pi$ is nonnegative, so a gap cannot cross down through $\pi$ on its way to zero. Under the usual finite simple-root hypotheses, this gives

\[
 D\ge q(\Delta_*)\ge q(\Delta_{\min}(0)).
\]

Writing $q$ as a real function outside this domain is invalid. The antipodal $N=2$ clock is the limiting infinite-depth case, not a finite value obtained by extending the logarithm through negative cosine. All circle clocks have infinite depth, even when their minimum gap is less than $\pi$.

For $m_N=N\Delta_{\min}/(2\pi)$, the valid bound is

\[
 D\ge-\log\cos(\pi m_N/N)
 \ge\frac{\pi^2m_N^2}{2N^2}.
\]

The last inequality follows from $-\log\cos x\ge x^2/2$ on $[0,\pi/2)$. It is an exact lower bound, not just an asymptotic one. For the corresponding microscopic time $s_{\rm micro}=N^2s/(4\pi^2)$, it reads $D_{\rm micro}\ge m_N^2/8$.

A simple ACUE configuration is an $N$-element subset of the (2N)-th roots of unity, so its angular gaps are at least $\pi/N$. A nonclock configuration has at least one gap exactly $\pi/N$: otherwise all $N$ integer lattice gaps would be at least 2 and sum to (2N), forcing a clock. Thus, for nonclock configurations,

\[
 D\ge-\log\cos\frac{\pi}{2N},\qquad N^2D\ge\frac{\pi^2}{8}.
\]

Clocks satisfy the same lower bound with $D=\infty$. Consequently

\[
 N^{8/3}D_{\rm ACUE}\ge(\pi^2/8)N^{2/3}\longrightarrow\infty
\]

deterministically in the extended sense. This separation does **not** require any conjecture about an ACUE limiting median or limiting distribution. It is a particularly clean part of the finite-model programme worth retaining.

## 7. What the number 1.419640342 does and does not establish

The single-defect family

\[
 P_N(z)=\frac{(z-1)(z^N+1)}{z-e^{-i\pi/N}}
\]

is a legitimate explicit configuration. Its proposed scaled heat profile and the double-zero equations supply a useful finite-dimensional/continuum calculation. The archived candidate critical value is $s_*=1.419640342\ldots$, with location $u_*=1.812942145\ldots$.

The first attachment's inference from the $N=2,\ldots,7$ median table to a typical ACUE limit at that constant is unsupported. Later complete finite enumeration in the archived notes reports conditional medians approximately

\[
 1.41822,\quad1.41520,\quad1.41277
 \quad(N=8,9,10),
\]

after the median turns at $N=7$. This invalidates the claimed monotone convergence evidence and the identification of the finite median with the single-defect branch. **Finite data alone do not prove that the eventual limiting median cannot equal the same number.** The stronger statement in one historical note that it is definitively not the limiting median goes beyond these finite data unless supplemented by another argument.

To turn the single-defect candidate into a theorem one must establish uniform convergence of the scaled heat profile and its relevant derivatives, nondegeneracy of the limiting double root, and the absence of an earlier collision elsewhere. Solving the double-zero equations numerically establishes none of the required global first-event exclusions by itself.

A limiting law for $N^2D_{\rm ACUE}$, its tightness, and the location of its support are separate ensemble questions. In particular, a deterministic special family does not automatically put its limiting value in the support of the random ensemble's limiting law: its probability can vanish too fast. At finite $N$, the clocks have positive probability and infinite depth, so the unconditioned expectation of $D$ is infinite whenever their ensemble weights are positive.

The archived generic CUE depth argument is stronger than merely a repulsion heuristic. Its key sufficient hypothesis is an isolated-small-gap condition such as $\delta A\to0$, where $A$ controls the reciprocal chord distances of the other roots from the close pair. Under that hypothesis one obtains $D\sim\delta^2/8$. A repulsion exponent or the size of the smallest gap alone does not prove this conclusion; the three-root cluster in §5 illustrates why background control matters.

## 8. Nonlinear transversality: a correct conditional theorem

The first attachment's differential idea can be stated precisely. Work on a smooth finite-dimensional manifold of admissible polynomial coefficients, use a real phase-normalized heat polynomial (Q(s,x,a)), and assume:

1. At $a=a_0$, there is a unique first collision at finite $D_0$ and real location $x_0$.
2. $Q=Q_x=0$, while $Q_{xx}\ne0$ and $Q_s\ne0$, at this collision.
3. The other roots remain simple there; competing collision times and any degree-loss or exceptional events are excluded in a neighborhood.
4. The moment constraint map (M(a)) has constant rank locally, so its level set is a smooth manifold.

The Jacobian of $(Q,Q_x)$ with respect to ((s,x)) is then invertible. The implicit function theorem gives a smooth local collision time and

\[
 dD(v)=-\frac{Q_a(v)}{Q_s}.
\]

If there exists a tangent vector $v\in\ker dM$ with $Q_a(v)\ne0$, the collision time is nonconstant on that moment fiber. The equivalent discriminant derivative formula requires a smooth defining discriminant branch and a nonzero derivative in the heat direction. It fails at simultaneous or higher-order collisions unless separately resolved.

The key condition is existence of that transverse $v$. It cannot be inferred merely because the hitting time is nonlinear, because the coefficient heat rates are large, or because the moment fiber has positive dimension. Rotations provide a simple null direction for every rotation-invariant statistic. Any tomography claim must first quotient such symmetries and show a full-rank Jacobian on the remaining tangent space. Multiple roots, clock points, and switches between competing first collision times are natural nondifferentiable exceptions.

Likewise, if a one-parameter family opens a single isolated double root with initial gap $\delta(\varepsilon)=c\varepsilon+o(\varepsilon)$ while all other roots remain uniformly separated, the local heat normal form gives $D=c^2\varepsilon^2/8+o(\varepsilon^2)$. This is a valid local theorem under isolation. If a third root approaches on the same scale, that coefficient is not automatic.

## 9. Exact marked counterexample: inverse blowup with bounded susceptibility

For $0<\varepsilon<1/2$, take

\[
 G_\varepsilon=\operatorname{diag}(\varepsilon,1-\varepsilon),
 \qquad \widetilde G_\varepsilon
 =\operatorname{diag}(1-\varepsilon,\varepsilon),\qquad u=e_1.
\]

For each fixed $\varepsilon$, these matrices are isospectral and have identical rank, trace, and Hilbert–Schmidt norm. Their marked inverse quantities are

\[
 u^*G_\varepsilon^{-1}u=\varepsilon^{-1}\to\infty,
 \qquad
 u^*\widetilde G_\varepsilon^{-1}u=(1-\varepsilon)^{-1}\to1.
\]

The Hilbert–Schmidt norm varies along $\varepsilon$; it is identical **within each pair**, not constant along the entire path. No claim of a fixed invariant fiber across all $\varepsilon$ is being made.

Apply the Cayley map $U=(G-iI)(G+iI)^{-1}$. For ordered eigenvalues $0<a<b$, the smaller angular separation is

\[
 \Delta=2(\arctan b-\arctan a)<\pi.
\]

For $N=2$, the heat threshold is exactly

\[
 \Lambda(a,b)=\log\cos(\Delta/2)
 =\log\frac{1+ab}{\sqrt{(1+a^2)(1+b^2)}}.
\]

Under $G\mapsto G+\eta uu^*$, marking the smaller and larger eigenvalues respectively gives

\[
 \chi_a=\frac{\partial\Lambda}{\partial a}
       =\frac{b-a}{(1+ab)(1+a^2)},\qquad
 \chi_b=\frac{\partial\Lambda}{\partial b}
       =-\frac{b-a}{(1+ab)(1+b^2)}.
\]

At $a=\varepsilon,b=1-\varepsilon$,

\[
 \chi_a\longrightarrow1,\qquad\chi_b\longrightarrow-\frac12.
\]

The attached script checks these derivatives and limits symbolically. Thus marks distinguish the two isospectral orientations, but inverse blowup does not force marked-depth susceptibility blowup. If susceptibility is instead defined using $D=-\Lambda$, the two signs reverse and boundedness is unchanged.

The rank-one determinant lemma and eigenvalue perturbation formula in the first attachment remain correct. Their existence does not establish the proposed inverse-Gram-to-depth blowup implication. A more restrictive claim along a path with all additional invariants fixed would require its own hypotheses and example; it is not established or refuted by misdescribing the present path.

## 10. What is missing at the actual-zeta bridge

The arithmetic conclusion does not follow from the finite first-collision identity alone.

Under RH, the classical de Bruijn–Newman constant satisfies $\Lambda\le0$; the Rodgers–Tao theorem supplies $\Lambda\ge0$, hence $\Lambda=0$. Therefore at every negative time the genuine global $H_t$ already has some nonreal zeros. An argument on $(-D,0]$ that requires **all** zeros to remain real cannot simply be reused for a high local window of that global flow. [Rodgers–Tao primary paper](https://arxiv.org/abs/1801.05914).

The problem is concrete: contributions from nonreal background zeros are not a sum of the nonnegative real screening terms in §4. A finite polynomial formed from the zeros in a window has a well-defined finite heat flow, but it is a different analytic function, whose time evolution need not agree with the restriction of $H_t$. Uniform control of that difference, including its derivatives on the shrinking time scale, is a missing theorem.

Before using a local depth $D_T$, define the object and prove at least the following: how roots are tracked in a window; what background or renormalization is retained; how the heat evolution is inherited from the genuine $H_t$; what constitutes the first local event; and what error controls replace the all-real positivity argument. An arbitrary stationary point process does not automatically determine an admissible entire function or a unique heat deformation either.

The scale conversion in the second attachment is algebraically correct **conditional on such a bridge**. In the usual Rodgers–Tao $x=2\gamma$ convention, local density is asymptotic to $\rho_T=(\log T)/(4\pi)$. A unit-density hard core of (1/2) would give microscopic depth at least (1/32), corresponding to

\[
 -t\ge\frac{\pi^2}{2(\log T)^2}
\]

to leading order. Correct units do not supply the missing analytic comparison.

The strong AH in Lagarias–Rodgers 1905.12123, Conjecture 2.2, uses limiting consecutive-gap values in $\{1/2,1,3/2,\ldots\}$, with no zero and for all sufficiently large indices. A theorem producing $\liminf g_n<1/2$ would refute that formulation. Statements allowing a density-zero exceptional set require a positive-density or otherwise appropriately quantified contradiction; formulations allowing multiplicity need separate handling. The historical .50412 small-gap claim mentioned in the 2019 source was withdrawn and should not be revived. [AH primary paper](https://arxiv.org/abs/1905.12123), [withdrawn Goldston–Turnage-Butterbaugh record](https://arxiv.org/abs/1904.06001).

A depth theorem about a function-field family and an anti-half-lattice conclusion for that family do not refute AH for the actual Riemann zeta function. Such a theorem may be a substantial independent random-matrix/arithmetic-family result. Its quantifiers concern the chosen family, monodromy group, genus, and field-size limits. Connecting it to actual zeta ordinates is additional work.

## 11. Claim-by-claim replacement ledger

| Supplied claim | Verdict and replacement |
|---|---|
| First heat collision is a discriminant event | Valid at finite nonexceptional degree, with clock/infinite-depth and multiple-event qualifications |
| $D=m_{\min}^2/8+\frac12\int d^2S$ | False as a universal identity; use the initial gap of the pair that actually collides, or add the pair-selection correction |
| $D\ge m_{\min}^2/8$ for finite real scalar heat | Valid under the real-root flow assumptions |
| Circle $D\ge-\log\cos(\Delta_{\min}/2)$ | Valid with the real logarithm domain and extended infinite clock case handled |
| ACUE $N^2D\ge\pi^2/8$ | Valid, deterministic lower bound |
| 1.419640342 is the limiting ACUE median | Not established; early finite evidence was misleading; single-defect candidate is a separate object |
| A deterministic special family places its limit in the ensemble support | Not automatic; requires nonvanishing probability/control in neighborhoods |
| $D\sim\delta_{\min}^2/8$ from a repulsion exponent alone | Insufficient; needs extreme-gap and background-isolation estimates |
| Heat-rate amplification establishes transversality | No; an actual tangent witness and collision nondegeneracy are needed |
| Marked inverse blowup forces susceptibility blowup | False in general; exact $N=2$ counterexample above |
| Low-band agreement remains invisible for all heat observations | Only if the specified observable class is invariant under the relevant evolution; nonlinear hitting-time observations require separate analysis |
| A local true-zeta depth automatically obeys the finite screening identity | Not defined/proved; negative-time nonreal background prevents the naive import |
| A function-field depth law refutes actual-zeta AH | Invalid transfer of quantifiers |
| LR never relates hard-core $\mu$ to .606894 | Our earlier source judgment was wrong; §5 of the companion paper explicitly proposes that relation |
| LR proves the .606894 hard-core bound in that passage | Also wrong; the passage proposes a method modification |

## 12. Reproducibility and next proof obligations

Run:

```sh
python3 research/bridge-audit/attachment_bridge_checks.py
```

Environment used: Python 3, SymPy 1.14.0. The saved run completed in about 0.13 seconds. The JSON contains exact rational data, not merely decimal approximations. The proof relies on standard exact polynomial arithmetic, Sturm's theorem, real-root continuation, and the explicitly stated symbolic identities. This is an exact computer-algebra certificate; it is not a proof-assistant formalization.

The most useful retained directions are the isolated-gap heat theorem, its rigorously controlled CUE consequences, and a precisely defined arithmetic residual/flow comparison. Immediate follow-up should target a theorem that supplies new arithmetic information or the missing true-zeta local-flow control. A universal near-collision theorem based solely on low-band mimicry would run into the already constructed half-lattice process unless an additional hypothesis excludes it.

Postpone claims of actual-zeta AH refutation, support beyond the currently proved arithmetic range, marked inverse blowup, and an ACUE limiting median until their missing hypotheses and estimates are supplied. None is made by this audit.
