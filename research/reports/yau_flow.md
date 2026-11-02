# Yau flows, circular heat localization, and a candidate CUE depth theorem

Research round 1, 2026-09-05. Prepared independently from the finite-depth source files and primary literature. The results below are mathematical arguments, not a Lean-checked proof. The CUE theorem is a proposed new consequence whose novelty requires further literature review; an attempted independent Claude review was unavailable because authentication returned HTTP 401. Another agent has checked the full deterministic argument and CUE transfer without finding a fatal issue, but that review is not formal verification. It is not a theorem about the Riemann zeta function.

## 1. Main finding

The earlier programme's dynamic background condition can be replaced by a simpler **initial-data isolation condition**. For the finite circular flow used in this project, an isolated closest pair admits a Gaussian heat-kernel scaling limit. For Haar CUE, an elementary three-point overcrowding estimate supplies that isolation with high probability. Combining this with the existing CUE extreme-gap theorem gives the following candidate theorem, pending independent adversarial review:

> Let \(U_N\) be Haar distributed in \(U(N)\), let
> \(P_N(z)=\det(zI-U_N)=\sum_{j=0}^N a_jz^j\), and evolve
> \(P_{N,s}(z)=\sum_{j=0}^N a_j e^{s j(N-j)}z^j\).
> Let \(D_N\) be its first positive time with a repeated root, and let
> \(\delta_N\) be the smallest initial circular angular gap. Then
> \[
> \frac{8D_N}{\delta_N^2}\longrightarrow1
> \quad\text{in probability}.
> \]
> Consequently, for every \(t\ge0\),
> \[
> \lim_{N\to\infty}\Pr(N^{8/3}D_N>t)
> =\exp\!\left(-\frac{2\sqrt2}{9\pi}t^{3/2}\right).
> \]

This closes the finite CUE localization gap if the argument below passes further independent review. No universality assertion about arbitrary point processes or zeta zeros is included. The stochastic Yau machinery is not needed for this proof: the decisive simplification is to use the scalar heat equation directly.

## 2. Three flows that must not be conflated

Dyson Brownian motion is a stochastic eigenvalue evolution. In a conventional Hermitian normalization it has a Brownian term of order \(N^{-1/2}\), a repulsive logarithmic interaction, and an optional confining drift. Erdős–Schlein–Yau local relaxation compares probability laws with a local equilibrium law. Their reverse heat-flow argument approximately inverts smoothing on a sufficiently regular matrix-entry density; it does not run individual DBM trajectories backward. See [Erdős–Péché–Ramírez–Schlein–Yau](https://arxiv.org/abs/0905.4176) and [Erdős–Schlein–Yau–Yin](https://arxiv.org/abs/0911.3687).

The project's circular root evolution is deterministic and attractive:
\[
\dot\theta_j=-\sum_{k\ne j}\cot\frac{\theta_j-\theta_k}{2}.
\]
After multiplying the centered characteristic polynomial by a fixed phase to make it real, write
\[
Q_0(x)=\prod_{j=1}^N\sin\frac{x-\theta_j}{2}.
\]
The corresponding centered polynomial at time \(s\) is, up to its zero-irrelevant scalar factor,
\[
\widetilde Q_s(x)=e^{sN^2/4}e^{s\partial_x^2}Q_0(x).
\]
Indeed the Fourier mode \(j-N/2\) receives multiplier
\(e^{s[N^2/4-(j-N/2)^2]}=e^{sj(N-j)}\).
Thus \(Q_s=e^{s\partial_x^2}Q_0\) solves ordinary forward scalar heat flow. For odd \(N\), \(Q_0\) is antiperiodic over \(2\pi\); it is periodic over \(4\pi\), and its real-line Gaussian representation remains valid. No periodicity shortcut is needed.

The de Bruijn–Newman convention has \(\partial_tH_t=-\partial_x^2H_t\). Increasing its parameter is the repulsive direction; our collision-time parameter \(s\) is the opposite direction. A ζ window cannot simply be replaced by a polynomial: the infinite product, outer zeros, normalization, and the true \(H_t\) evolution all need control.

Rodgers and Tao already explicitly invoke the analogy with the Erdős–Schlein–Yau local relaxation method. Their theorem assumes a fixed negative global Newman parameter for contradiction, evolves over an actual interval of real-rooted \(H_t\), and drives the zeros toward local clock behavior. Their argument does not identify ζ with DBM and does not immediately turn a hard core at time zero into an interval of backward stability. See [Rodgers–Tao](https://arxiv.org/abs/1801.05914) and [Tao's explanation](https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/).

## 3. A deterministic initial-data lemma

Consider a sequence of finite configurations, with size allowed to vary. Their circular angular gaps are initially positive. Let \(\delta\) be the smallest gap, rotate its endpoints to \(-\delta/2,\delta/2\), and write the other angles as \(\theta_k\in(-\pi,\pi]\). Define
\[
H(y)=\prod_{k\notin\{-,+\}}\sin\frac{y-\theta_k}{2},\qquad
A=\sum_{k\notin\{-,+\}}\frac1{2|\sin(\theta_k/2)|}.
\]
Empty products and sums are allowed. Assume
\[
\delta\to0,\qquad \delta A\to0.
\tag{I}
\]

**Isolation lemma.** Under (I), the global first collision time satisfies
\[
D=\frac{\delta^2}{8}(1+o(1)).
\tag{L}
\]

The assumption is on the initial configuration only. It neither assumes that the closest pair remains the first colliding pair nor requires an a priori bound on the evolving background. If a different pair collides first, the upper-bound argument remains valid.

### 3.1 Global control of the background product

Since sine is \(1\)-Lipschitz,
\[
\left|\frac{\sin((y-\theta_k)/2)}{\sin(-\theta_k/2)}-1\right|
\le\frac{|y|}{2|\sin(\theta_k/2)|}.
\]
The elementary product inequality
\(|\prod(1+u_k)-1|\le\prod(1+|u_k|)-1\) implies, for every real \(y\),
\[
\left|\frac{H(y)}{H(0)}-1\right|\le e^{A|y|}-1,
\qquad
\left|\frac{H(y)}{H(0)}\right|\le e^{A|y|}.
\tag{B}
\]
These are global bounds; no cutoff in the heat convolution and no uncontrolled ratio to the global supremum of \(Q_0\) appear.

### 3.2 Heat-kernel normal form

Set \(s=\tau\delta^2\), and let \(Z\) be a standard real normal random variable. Because \(Q_0\) is a finite real trigonometric polynomial,
\[
Q_s(\delta x)=\mathbb E\,Q_0(\delta x+\sqrt{2s}Z).
\]
With \(Y=x+\sqrt{2\tau}Z\), define
\[
F_\delta(x,\tau)=\frac{4Q_{\tau\delta^2}(\delta x)}{\delta^2H(0)}
=\mathbb E\left[
\frac4{\delta^2}
\sin\frac{\delta(Y-1/2)}2
\sin\frac{\delta(Y+1/2)}2
\frac{H(\delta Y)}{H(0)}\right].
\tag{F}
\]
For fixed \(Y\), the bracket tends to \(Y^2-1/4\). Moreover,
\[
\frac4{\delta^2}
\left|\sin\frac{\delta(Y-1/2)}2\sin\frac{\delta(Y+1/2)}2\right|
\le(|Y|+1/2)^2.
\]
For \(\delta A\le1\), (B) gives a dominating factor \(e^{|Y|}\), which is integrable against a Gaussian uniformly when \(x\) and \(\tau\) range over compact sets. The same estimates with Taylor's remainder give the stronger uniform statement
\[
\sup_{|x|\le R,\,0\le\tau\le T}
\left|F_\delta(x,\tau)-(x^2-1/4+2\tau)\right|
\le C_{R,T}(\delta A+\delta^2).
\tag{U}
\]
For completeness, use 
\(|e^{a|Y|}-1|\le a|Y|e^{|Y|}\) for \(0\le a\le1\), and
\(|\sin u-u|\le|u|^3/6\). The resulting errors are bounded by a constant times
\((\delta A+\delta^2)(1+|Y|^6)e^{|Y|}\), whose expectations are uniformly bounded on the stated compact set.

### 3.3 Why the normal form forces an actual collision

Fix \(R=2\), and fix any \(\varepsilon>0\) small enough that
\(\tau_+=1/8+\varepsilon<1\). Uniform convergence (U) gives:

1. \(F_\delta(-R,\tau)>0\) and \(F_\delta(R,\tau)>0\) for every \(0\le\tau\le\tau_+\), once (I) is sufficiently small.
2. \(F_\delta(x,\tau_+)>0\) for every \(-R\le x\le R\), since the limiting polynomial is \(x^2+2\varepsilon\).
3. Initially exactly the two selected roots lie between \(-R\delta\) and \(R\delta\). To see this, any third root at circular distance at most \(R\delta\) would give \(\delta A\ge c_R>0\), contradicting (I).

Suppose, for contradiction, that no global collision occurs by \(s=\tau_+\delta^2\). The initial circle roots then remain simple and on the circle throughout: self-inversive symmetry, or equivalently the real trigonometric equation and the implicit function theorem, prevents a simple real root from leaving the real axis. The two selected roots vary continuously, and cannot cross the fixed interval's boundary because the boundary values stay nonzero throughout. They would therefore still give two real roots inside the interval at the final time, contradicting item 2.

It follows that \(D\le(1/8+\varepsilon)\delta^2\). This argument uses tracking and nonvanishing boundaries; positivity only at the final time would not suffice. No Rouché assertion is being smuggled into the proof.

### 3.4 Matching deterministic lower bound

Before the first collision, each adjacent gap \(g\) obeys
\[
g'\ge-2\cot(g/2).
\]
The scalar comparison solution initialized at the minimum gap \(\delta<\pi\) first reaches zero at
\[
D_2(\delta)=-\log\cos(\delta/2)\ge\delta^2/8.
\]
Compare every gap with this same scalar solution. The comparison function \(-2\cot(g/2)\) is increasing on \((0,2\pi)\), so this remains legitimate for an initially long gap. A collision cannot occur while the scalar solution is positive. Therefore \(D\ge D_2(\delta)\). Combining with the preceding upper bound proves (L).

One can extract an absolute-constant bound
\[
\frac{\delta^2}{8}\le D\le
\delta^2\left[\frac18+C(\delta A+\delta^2)\right]
\]
when \(\delta A+\delta^2\) is sufficiently small. No numerical value of \(C\) is claimed here.

## 4. CUE supplies the isolation condition

The Haar CUE eigenangles form the projection determinantal process with correlation kernel
\[
K_N(x,y)=\frac1{2\pi}\sum_{m=0}^{N-1}e^{im(x-y)}.
\]

### 4.1 Uniform three-point bound

For three real lifts \(x_1,x_2,x_3\), Cauchy–Binet gives
\[
\rho_3(x_1,x_2,x_3)=\frac1{(2\pi)^3}
\sum_{0\le m_1<m_2<m_3<N}
\left|\det(e^{im_a x_b})_{a,b=1}^3\right|^2.
\]
For a fixed triple of frequencies, put \(v(x)=(e^{im_1x},e^{im_2x},e^{im_3x})^T\). Divided differences give the exact identity
\[
\det(v(x_1),v(x_2),v(x_3))
=\prod_{i<j}(x_j-x_i)
\det(v[x_1],v[x_1,x_2],v[x_1,x_2,x_3]).
\]
The integral formula for divided differences and Hadamard's inequality bound the three column norms by
\(\sqrt3,\sqrt3N,\sqrt3N^2/2\), respectively. Hence each determinant has modulus at most
\((3\sqrt3/2)N^3\prod_{i<j}|x_i-x_j|\). Summing fewer than \(N^3/6\) terms proves
\[
\rho_3(x_1,x_2,x_3)\le C N^9\prod_{i<j}|x_i-x_j|^2
\tag{3P}
\]
with an absolute constant. This holds for lifts of points in a short arc, including an arc that crosses the arbitrary \(2\pi\) cut.

### 4.2 Triple-free arcs with high probability

Count ordered triples with an anchor at \(x_1\in[0,2\pi)\) and the other two points in the oriented arc \([x_1,x_1+r]\). If any arc of length \(r\) contains three points, at least one such anchored triple exists. Using (3P), integration over the two offsets gives
\[
\Pr(\exists\text{ arc of length }r\text{ containing three points})
\le C N^9r^8.
\tag{T}
\]
Choose \(r=N^{-7/6}\). The right side is \(O(N^{-1/3})\).

### 4.3 A packing bound for the reciprocal chord sum

On the event that every arc of length \(r\) contains at most two points, suppose additionally that the minimum gap obeys \(\delta<r/2\). Center that pair at zero. Any other point must have circular distance at least \(r-\delta/2\) from the pair center: otherwise it and both endpoints lie in a single arc of length \(r\).

Partition the circle in arcs of length \(r\), or order the remaining points by their circular distance \(d_k\in(0,\pi]\) from zero. The two-points-per-arc condition implies \(d_k\ge c r(k+1)\) for an absolute \(c>0\); the first few indices use the preceding isolation observation. Since \(2\sin(d/2)\ge2d/\pi\) for \(0\le d\le\pi\),
\[
A\le C r^{-1}(1+\log N).
\tag{A}
\]

### 4.4 Existing extreme-gap input and the resulting law

The CUE extreme-gap theorem gives
\[
N^{4/3}\delta_N\Rightarrow X,\qquad
\Pr(X>x)=\exp\left(-\frac{x^3}{72\pi}\right).
\tag{EG}
\]
This normalization uses angular coordinates of circumference \(2\pi\). It agrees with \(A_2=1/(24\pi)\) in Feng–Wei's gap intensity \(A_2u^2\,du\): integrating from zero to \(x\) gives \(x^3/(72\pi)\). See [Ben Arous–Bourgade](https://arxiv.org/abs/1010.1294) and [Feng–Wei, Theorem 1.1 and Corollary 1.1](https://arxiv.org/abs/1806.01555).

In particular \(N^{4/3}\delta_N\) is tight. Combining (T), (A), and \(r=N^{-7/6}\) gives
\[
\delta_N A_N
=O_{\Pr}(N^{-1/6}\log N)=o_{\Pr}(1),
\]
and also \(\delta_N/r\to0\) in probability. The isolation lemma yields \(8D_N/\delta_N^2\to1\) in probability. Slutsky's theorem then gives
\[
N^{8/3}D_N\Rightarrow X^2/8,
\qquad
\Pr(X^2/8>t)=\exp\left(-\frac{2\sqrt2}{9\pi}t^{3/2}\right).
\]

This proof needs no uniform-in-\(N\) extrapolation of the extreme-gap tail. It uses only tightness and the fixed-argument limiting law.

## 5. What is genuinely new here, and what may already be classical

The isolated-pair mechanism is closely related to the classical Lehmer-pair estimates of Csordas–Smith–Varga, which already control a Newman lower bound from an initial gap and a background sum of inverse squares. The claim “nobody knows how to control the evolving background from initial data” would therefore be misleading. See [Csordas–Smith–Varga's paper](https://www.math.kent.edu/~varga/pub/paper_206.pdf).

Andrade–Chang–Miller explicitly express the function-field background as finite csc-squared sums and use isolated small zeros to approach zero Newman parameter. Their §3.8 already connects such estimates to random matrix theory. See [Newman's conjecture in various settings](https://arxiv.org/abs/1310.3477). We must compare any eventual paper carefully with these results.

The contribution proposed in this round is the particularly short global heat-product estimate (B), its deterministic scaling lemma, and the use of elementary CUE triple-overcrowding plus the known extreme-gap theorem to get an explicit first-collision law. A search in this round did not locate that exact CUE law; this is not a guarantee of novelty. Calling it a solution of a famous ζ conjecture would be false.

## 6. Why this does not refute AH

The isolation assumption fails at lattice scale. For a clock-like configuration with gap of order \(N^{-1}\), the reciprocal chord sum is of order \(N\log N\), so \(\delta A\) is not small. ACUE's finite lattice hard core therefore does not contradict the lemma. The new theorem explains a distinction for CUE's extreme close pairs; it does not show that ζ has those pairs.

For ζ, near collisions, quantitative outer-zero control, and the true heat evolution would need to be established arithmetically. Bandwidth-one correlations alone cannot supply a theorem excluding every ACUE-type model, because such models already match that information. A proposed “energy bound” must be stated and checked on ACUE; merely naming a renormalized energy does not add arithmetic information.

Moreover, an AH that permits a zero-density exceptional set is not refuted by a first-collision statistic or infinitely many unusually small gaps. For that version, one needs positive-density violations in a fixed interval separated from the allowed half-integer spacings, or another statistic that controls the density of exceptions. The inference “AH implies every window has hard core \(1/2\)” remains invalid without strengthening AH.

## 7. Function-field transfer: a precise modest theorem and a real remaining gap

For a fixed degree, the extended-valued collision depth is expected to be continuous on the compact space of circle-rooted characteristic polynomials when \([0,\infty]\) is given its usual one-point compactification. A route to a proof is as follows:

* If \(t<D(P)\), \(Q_t\) has the full number of simple real zeros, and nearby coefficient vectors also do. This gives lower semicontinuity.
* If \(t>D(P)\), choose a nearby time with no multiple zero. Scalar heat's strict drop in zero number after a multiple zero gives fewer than the full number of real zeros at this time. This property persists under small coefficient perturbation, giving upper semicontinuity.
* At a clock polynomial \(D=\infty\), the first assertion for every finite \(t\) gives extended continuity. The same zero-number argument treats initial multiple roots if their depth is defined as zero.

This uses the classical zero-number theorem for scalar parabolic equations, rather than an unsupported assertion that the hitting time of an arbitrary discriminant is continuous. The theorem is due to Angenent; see [the original publication](https://doi.org/10.1515/crll.1988.390.79).

Once this continuity argument is fully written, fixed-rank Frobenius equidistribution immediately transports the law of any bounded continuous function of depth. One must state a specific arithmetic family and its compact symmetry group. For instance, the hyperelliptic ensemble at fixed genus and \(q\to\infty\) has \(\mathrm{USp}(2g)\) equidistribution; [Rudnick's paper](https://www.math.tau.ac.il/~rudnick/papers/acta2010.pdf) states this precisely.

This fixed-rank transfer is a useful corollary, not by itself a large universality theorem. To transport the CUE \(N^{8/3}\) law to a unitary function-field family one either takes the successive limit \(q\to\infty\) then \(N\to\infty\), or proves effective equidistribution uniform in the rank and in the increasingly singular test function. A diagonal subsequence can be chosen abstractly from successive limits, but it gives no useful growth rate \(q=q(N)\). Haar \(\mathrm{USp}\) and \(\mathrm{SO}\) have symmetry-forced spectral pairing and edges, so the CUE argument cannot simply be relabeled with another beta.

## 8. A more promising research ladder after this round

1. Independently audit the deterministic heat lemma and the CUE overcrowding proof. Write a concise standalone theorem note, then check the CSV/Stopple/Andrade literature for priority and potentially sharper initial-data criteria.
2. Generalize only under explicit assumptions: if \(a_N\delta_N\Rightarrow X\) and \(\delta_N A_N\to0\) in probability, then \(a_N^2D_N\Rightarrow X^2/8\). Bandwidth-one correlation is unnecessary for this abstract transfer theorem.
3. For circular beta ensembles, prove or cite a uniform three-point bound of the form \(\rho_3\le C_\beta N^{3+3\beta}\prod|x_i-x_j|^\beta\). It would give triple-free scale \(r=N^{-1-\eta}\) for \(\eta>1/(2+3\beta)\), compatible with the minimum-gap scale \(N^{-1-1/(\beta+1)}\). The known Feng–Wei extreme-gap theorem used in the source covers positive integer beta; do not silently assert all positive real beta.
4. For a genuinely arithmetic advance, seek a **positive-density isolated-pair theorem** with a testable arithmetic input. If normalized gaps below \(1/2\) are the target, obtaining them cannot be assumed inside the background lemma.
5. Investigate whether a natural arithmetic weighting produces an energy or multi-point statistic unavailable to the ACUE mimickers. That is where a Yau-inspired local relaxation argument might add value: formulate the actual local law, the coercive energy, and the estimate that distinguishes arithmetic zeros from a fake process.

## 9. Verification boundary

The complete reasoning of the deterministic lemma and CUE transfer is above. Independent review by another agent was requested. Numerical tests are supplementary and cannot certify the theorem. The attached script tests the scalar heat normal form, exact two-root normalization, and planted isolated-pair collision times; it does not simulate an arithmetic zeta flow or prove a famous conjecture.

The completed diagnostics are saved in `yau_flow_checks.json`. They reproduce the exact two-root time for four gaps; for planted isolated pairs at N=16,32,64,128,256 they give 8D/δ² between 1.00013025 and 1.00002066, decreasing toward 1. The tests also sample the global product bound and three-point determinant inequality. These data are not a Monte Carlo verification of the limiting distribution. The `residual_gram` agent reviewed the full deterministic and CUE arguments and reported no fatal issue; the `prime186` agent also independently checked the deterministic argument, the actual Feng–Wei source statements, the beta scope, and the tail constants without finding a fatal issue. The attempted Claude review did not run because authentication failed with HTTP 401.

## 10. Stronger supplement: the positive-integer circular-beta depth law

After the first draft, the general three-point estimate was found to follow directly from Hölder's inequality and a published coalesced-charge partition-function bound. Thus the proposed result extends to every fixed **positive integer** beta, including COE, CUE, and CSE. The restriction here comes from the published extreme-gap limit used as an input; this note does not assert that the limit is unavailable or false for other beta values.

For fixed positive integer \(\beta\), let the initial angles have density
\[
\frac1{C_{\beta,N}}\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^\beta.
\]
Use the same characteristic-polynomial coefficient flow as above; the flow itself does not depend on beta. Define
\[
A_\beta=\frac1{2\pi}\left(\frac\beta2\right)^\beta
\frac{\Gamma(1+\beta/2)^3}{\Gamma(1+3\beta/2)\Gamma(1+\beta)}.
\]

**Candidate circular-beta theorem.** For every fixed positive integer beta,
\[
\frac{8D_N}{\delta_N^2}\to1\quad\text{in probability},
\]
and
\[
\lim_{N\to\infty}\Pr\left(N^{2+2/(\beta+1)}D_N>t\right)
=\exp\left[-\frac{A_\beta}{\beta+1}(8t)^{(\beta+1)/2}\right],
\qquad t\ge0.
\tag{CB}
\]
For beta=1 the tail is \(e^{-t/6}\). For beta=2 it is the CUE law in §1. For beta=4 it is \(\exp[-(64\sqrt2/(675\pi))t^{5/2}]\). CSE here means the circular beta=4 ensemble of N distinct eigenangles, not Haar USp(2N), and no double-counting of quaternionic eigenvalues is intended.

### 10.1 The missing correlation estimate is an elementary Hölder consequence

Put \(z_a=e^{ix_a}\), \(a=1,2,3\), and \(w_j=e^{iy_j}\), \(j=1,\ldots,N-3\). The three-point correlation function is
\[
\rho_3(x_1,x_2,x_3)=\frac{(N)_3}{C_{\beta,N}}
\prod_{a<b}|z_a-z_b|^\beta\ I(z_1,z_2,z_3),
\]
where
\[
I=\int\prod_{i<j}|w_i-w_j|^\beta
\prod_{j=1}^{N-3}\prod_{a=1}^3|w_j-z_a|^\beta\,d\mathbf y.
\]
Apply Hölder with exponents (3,3,3) to the measure with density \(\prod_{i<j}|w_i-w_j|^\beta\). This gives
\[
I\le\prod_{a=1}^3\left[
\int\prod_{i<j}|w_i-w_j|^\beta
\prod_j|w_j-z_a|^{3\beta}\,d\mathbf y
\right]^{1/3}.
\]
Each bracket is independent of \(z_a\) by rotation invariance. Integrating its distinguished point over the full circle identifies it as
\(C_{\beta,N-3,(3)}/(2\pi)\), in the notation of Feng–Wei. Their Lemma 1.1 gives, for beta≥1,
\[
\frac{C_{\beta,N-3,(3)}}{C_{\beta,N}}\le(N\beta)^{3\beta}.
\]
Therefore
\[
\rho_3(x_1,x_2,x_3)
\le\frac{\beta^{3\beta}}{2\pi}
N^{3+3\beta}\prod_{a<b}|e^{ix_a}-e^{ix_b}|^\beta
\le C_\beta N^{3+3\beta}\prod_{a<b}|x_a-x_b|^\beta
\tag{B3}
\]
for real lifts of a short arc. This argument does not use a determinantal or Pfaffian representation. The only non-elementary input in (B3) is the published partition-function inequality. See [Feng–Wei, equations (1)–(4) and Lemma 1.1](https://arxiv.org/abs/1806.01555).

### 10.2 Triple exclusion and first collision

The same anchored-triple count now gives
\[
\Pr(\exists\text{ arc of length }r\text{ containing three points})
\le C_\beta N^{3+3\beta}r^{2+3\beta}.
\]
Choose any fixed
\[
\frac1{2+3\beta}<\eta<\frac1{\beta+1},\qquad r=N^{-1-\eta}.
\]
This interval is nonempty for every positive beta. The probability above tends to zero. On its complement, §4.3 gives \(A\le Cr^{-1}(1+\log N)\).

Feng–Wei's extreme-gap theorem for positive integer beta gives
\[
N^{1+1/(\beta+1)}\delta_N\Rightarrow X_\beta,
\qquad
\Pr(X_\beta>x)=\exp[-A_\beta x^{\beta+1}/(\beta+1)].
\]
It follows that
\[
\delta_N A_N
=O_{\Pr}\left(N^{\eta-1/(\beta+1)}\log N\right)=o_{\Pr}(1).
\]
The deterministic isolation lemma proves the ratio limit, and continuous mapping gives (CB). There is no beta-infinity limit in this argument. Fixed-beta asymptotics do not identify ACUE with a beta-infinity ensemble.

### 10.3 Assessment

If the isolation lemma survives the independent adversarial review, the old finite-depth programme is no longer “one dynamic background lemma away” in the COE/CUE/CSE cases: the required localization follows from a different, initial-data argument and existing partition-function estimates. This is a concrete candidate probability theorem. The arithmetic bridge to ζ and the user's requested famous conjecture remain open; the result is best treated as a proved-direction candidate and a reusable transfer mechanism, not the final research objective.


A stronger, drift-invariant version of the deterministic lemma is proved in `yau_flow_galilean_refinement.md`: the hypothesis is δ²B→0 with B=¼Σcsc²(θk/2). The exact Galilean transform removes the linear logarithmic drift, and a global quadratic exponential bound controls the heat tails. The root agent independently audited the centered-factor inequality and the moving-frame mechanism. Full formal verification and a priority review remain outstanding.

## 11. Identification of the first colliding pair

The published joint limit for the first two smallest gaps gives a useful corollary to the candidate depth theorem.

**Corollary.** For every fixed positive integer beta, with probability tending to one, the first colliding pair is the pair that had the smallest gap at time zero.

Write the first two initial gaps as \(\delta_1<\delta_2\); equality has probability zero under the continuous circular-beta density. Before the global first collision, every gap other than the minimum is bounded below by the scalar comparison solution initialized at \(\delta_2\). Therefore no such pair can collide before
\[
-\log\cos(\delta_2/2)\ge\delta_2^2/8.
\]
The selected minimum pair supplies the global upper bound
\[
D\le\delta_1^2(1/8+\varepsilon_N),\qquad\varepsilon_N\to0
\quad\text{in probability}.
\]
The joint extreme-gap limit implies that \(\delta_2/\delta_1\) converges in law to a random variable strictly greater than one almost surely. Hence
\[
\Pr(\delta_2^2/\delta_1^2>1+8\varepsilon_N)\to1.
\]
On this event, all other initial adjacent pairs remain separated until after the global first collision, proving the assertion. This is an asymptotic identification statement; it does not make the finite marked derivative exactly rank two.

## 12. The relaxation-time obstruction to the proposed AH argument

This subsection is a dimensional analysis and logical audit, not an impossibility theorem against every future heat-flow method.

At height T, the mean Riemann-zero spacing in the usual ordinate is of order \((\log T)^{-1}\). A pair-collapse equation with leading term \(g'=-4/g\) therefore has local time scale \((\log T)^{-2}\). The common convention for \(H_0\) uses twice the ordinary zeta ordinate, which changes constants but not this exponent. One must keep that coordinate factor when making a numerical claim such as π²/8.

The contradiction assumption in Rodgers–Tao is a **fixed negative global** Newman parameter, giving a time interval of length bounded away from zero on which all the relevant zeros are real. In microscopic units, the available duration at height T is consequently of order log²T, tending to infinity. This long duration in local units is what permits a relaxation-to-clock argument. Their actual proof needs renormalized energies and technical estimates; this dimensional observation is not a substitute for those estimates. See [Rodgers–Tao](https://arxiv.org/abs/1801.05914).

A hard core proportional to one mean spacing, even if it were a genuine uniform hard core rather than an almost-everywhere AH, only gives the two-body stability lower bound of order \((\log T)^{-2}\). That is **O(1)** microscopic relaxation times. It does not supply the diverging number of relaxation times available in the global negative-Λ contradiction. Rescaling the old energy argument does not remove this loss. A proposed proof must explain what new arithmetic estimate replaces that missing duration.

The finite circular normalization makes the distinction transparent. Its unnormalized deterministic clock Jacobian has eigenvalues \(k(N-k)\); the high modes have time scale \(N^{-2}\). A conventional circular DBM has repulsive drift
\[
\frac1{2N}\sum_{j\ne i}\cot\frac{\theta_i-\theta_j}{2}
\]
and diffusion coefficient \(\sqrt{2/(\beta N)}\). Thus its local relaxation scale is order \(N^{-1}\), corresponding to unnormalized deterministic time order \(N^{-2}\). At that time the Brownian displacement itself is of order one mean spacing. It cannot be discarded in a pathwise identification with the attractive deterministic flow.

At the CUE extreme-gap scale the same problem persists: deterministic first-collision time is order \(N^{-8/3}\), corresponding to DBM time order \(N^{-5/3}\); the DBM Brownian displacement over that duration is order \(N^{-4/3}\), exactly the extreme gap size. A genuine DBM comparison has to retain its noise and its repulsive sign. It cannot identify its collision behavior with the scalar heat evolution studied here.

The new isolated-pair theorem sharpens this audit. Under weak initial isolation, normalized depth is asymptotically the square of the normalized smallest gap. A ζ depth bound substantially below the half-spacing threshold would therefore require genuine microscopic arithmetic information or a mechanism outside isolated-pair behavior. Merely renaming the desired small-gap phenomenon as a first-passage event does not prove it. For an AH allowing zero-density exceptions, the needed arithmetic result must additionally control the density of violations.

## 13. Current literature on matrix heat flow

A relevant recent paper is Hall–Ho, [The heat flow conjecture for polynomials and random matrices](https://doi.org/10.1007/s11005-025-01946-9), published in 2025. It connects additive and multiplicative polynomial heat flows to deformations of random matrix models, proves second-moment and holomorphic-moment statements, and formulates macroscopic root-transport conjectures. Its multiplicative generator differs from the generator here by a scalar multiplier and a deterministic radial dilation. This is useful context for a future theorem note; its macroscopic statements do not by themselves supply the microscopic extreme first-collision law above. The exact priority of that law remains to be checked.
