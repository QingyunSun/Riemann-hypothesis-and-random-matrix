# Deterministic circular heat creates a local Bragg deficit from ACUE data

Date: 2026-09-05. Status: complete ordinary proof submitted for independent review; no claim of novelty or formal verification. This is a finite circular-model theorem with constants uniform in the number of particles. It is not a theorem about zeta zeros, a refutation of AH, or a stochastic Dyson Brownian-motion result.

The new point relative to the earlier forward-flow obstruction is a **positive lower bound at a fixed microscopic time for the same localized Bragg-deficit kernel used in Round 16**. The initial deficit is identically zero. The proof does not infer a uniform time interval from a second derivative at zero: hard-core preservation and a uniform acceleration estimate supply that interval explicitly.

## 1. The observable and the theorem

Use the fixed smooth seed and autocorrelation from the Round 16 report:
\[
f(x)=e^{-1/(1-4x^2)}1_{|x|<1/2},\quad
s_2=\int f^2,\quad \psi=f*\widetilde f/s_2,
\quad m_0=(\int f)^2/s_2>0.
\tag{1}
\]
Our Fourier convention is \(\widehat f(u)=\int f(x)e^{-2\pi iux}dx\), so
\(\widehat\psi=|\widehat f|^2/s_2\ge0\). Fix \(\varepsilon=1/4\), and put
\[
k_\varepsilon(u)=\varepsilon\widehat\psi(\varepsilon u),\qquad
k_{\varepsilon,N}(u)=\sum_{\ell\in\mathbb Z}k_\varepsilon(u+\ell N).
\tag{2}
\]
The periodization and all its derivatives converge absolutely. On a circle of circumference \(N\), for \(N\) particles \(q_1,\ldots,q_N\), define
\[
\mathfrak D_{\varepsilon,N}(q)=\frac1N\sum_{i,j=1}^N
k_{\varepsilon,N}(q_i-q_j)
\bigl(1-\cos(4\pi(q_i-q_j))\bigr)\ge0.
\tag{3}
\]
Both factors are periodic on this circle because \(N\) is an integer. Every summand is nonnegative. The diagonal contributes zero.

The initial ensemble is ACUE: choose \(N\) distinct sites from \(\mathbb Z/(2N)\) according to the rank-\(N\) projection determinantal process with kernel
\[
\mathcal K_N(r,u)=\frac1{2N}\sum_{a=0}^{N-1}
e^{2\pi ia(r-u)/(2N)},
\qquad q=r/2\pmod N.
\tag{4}
\]
Equivalently, the probability of an unordered selected set \(S\) is
\((2N)^{-N}\prod_{r<u\in S}4\sin^2(\pi(r-u)/(2N))\).
The determinant/Cauchy–Binet identity gives total mass one.

Evolve these particles by the deterministic repulsive ODE
\[
\frac{dq_i}{ds}=v_i(q)=\sum_{j\ne i}K_N(q_i-q_j),
\qquad K_N(x)=\frac{2\pi}{N}\cot\frac{\pi x}{N}.
\tag{5}
\]
Section 3 proves existence for every \(s\ge0\) for these initial data.

**Theorem.** Set
\[
\beta=\frac1{84},\quad A_*=12288,\quad
s_*:=\frac{\beta}{4A_*}=\frac1{4\,128\,768},\qquad
\kappa_\varepsilon:=\varepsilon m_0\cos^2(3\pi\varepsilon/4)>0.
\tag{6}
\]
For every integer \(N\ge8\),
\[
\mathfrak D_{\varepsilon,N}(q(0))=0
\quad\hbox{for every initial selected set},
\tag{7}
\]
whereas, for every \(0<s\le s_*\),
\[
\boxed{\mathbb E_{\rm ACUE}\mathfrak D_{\varepsilon,N}(q(s))
\ \ge\ 2\kappa_\varepsilon\beta^2s^2.}
\tag{8}
\]
The lower bound is independent of \(N\). In particular it survives taking \(N\to\infty\) along any sequence. No limiting process construction is needed for this expectation inequality.

This deliberately small time interval is sufficient for the qualitative distinction. Optimizing its constants is postponed.

## 2. Normalization: scalar heat, polynomial flow and the Bragg bump

Write \(\theta_i=2\pi q_i/N\). If
\[
P_t(z)=\sum_{k=0}^Na_ke^{-k(N-k)t}z^k,
\tag{9}
\]
then \(\partial_tP=z^2P_{zz}-(N-1)zP_z\), and its simple unit-circle roots satisfy
\[
\frac{d\theta_i}{dt}=V_i:=\sum_{j\ne i}
\cot\frac{\theta_i-\theta_j}{2}.
\tag{10}
\]
Indeed \(P_{zz}(z_i)/P_z(z_i)=2\sum_{j\ne i}(z_i-z_j)^{-1}\) and
\(z_i/(z_i-z_j)=1/2-(i/2)\cot((\theta_i-\theta_j)/2)\).
The exact microscopic change of time is
\[
s=\frac{N^2t}{4\pi^2},
\tag{11}
\]
which gives (5). If the polynomial is centered by multiplying
\(e^{-iN\theta/2}P_t(e^{i\theta})\) by the zero-irrelevant scalar
\(e^{N^2t/4}\), it satisfies \(\partial_tQ=-\partial_\theta^2Q\).
For odd \(N\), the centered function is antiperiodic; this does not affect its roots or the argument. The nonzero leading and constant coefficients remain fixed. Conversely, the global ODE solution below gives the same polynomial evolution by the root equation, with no loss through zero or infinity.

For \(p_m(q)=\sum_j e^{2\pi imq_j/N}\), define the finite-circle spectral bump
\[
C_{\varepsilon,N}(b;q)=\frac1{N^2}\sum_{m\in\mathbb Z}
\psi\!\left(\frac{m/N-b}{\varepsilon}\right)|p_m(q)|^2,
\qquad b\in\{0,2\}.
\tag{12}
\]
Poisson periodization gives Fourier coefficient
\(N^{-1}\psi(m/(N\varepsilon))\) for (2). Consequently,
\[
\mathfrak D_{\varepsilon,N}=C_{\varepsilon,N}(0)-C_{\varepsilon,N}(2).
\tag{13}
\]
The symmetric cosine produces the average of the translates at \(\pm2\); these are equal because \(|p_{-m}|^2=|p_m|^2\).
This is exactly the finite-circle version of Round 16's nonnegative pair deficit, with a periodized spatial kernel and without the finite-height zeta endpoint weight.

At half-grid data every difference belongs to \((1/2)\mathbb Z\), proving (7). Also the projection-kernel trace computation gives
\(\mathbb E|p_m|^2=|m|\) for \(0<|m|\le N\): in
\(\operatorname{Tr}\mathcal K-\operatorname{Tr}(\mathcal K U_m\mathcal K U_m^*)\), the overlap of the two frequency intervals has size \(N-|m|\). Thus initially
\[
\mathbb EC_{\varepsilon,N}(0)
=1+\frac2{N^2}\sum_{1\le m<\varepsilon N}
m\psi\!\left(\frac m{\varepsilon N}\right)
\longrightarrow1+\varepsilon^2m_1,
\quad m_1=\int |u|\psi(u)du.
\tag{14}
\]
This is the same low-band value that RH supplies in Round 16. Initial protected moments match CUE, but this statement does not say that their numerical values remain stationary under (5).

## 3. A hard core and a uniform acceleration estimate

We prove the necessary deterministic bounds, including circular wrap cases.

**Lemma 1 (hard-core preservation).** If all cyclic gaps are at least \(h>0\) initially, then they remain at least \(h\) for all positive times. The solution is global.

**Proof.** Work in the lifted chamber
\(q_1<\cdots<q_N<q_1+N\), with \(q_{N+1}=q_1+N\).
The vector field is smooth there and is translation invariant. Its off-diagonal Jacobian entries are \(-K_N'(q_i-q_j)>0\), and its row sums are zero. Both vectors
\(x_i=q_i\) and \(y_i=q_{i+1}-h\) solve the same ODE, using periodicity for the last coordinate. Initially \(y_i-x_i\ge0\). The lifted chamber is convex; integrating the Jacobian along the segment from \(x\) to \(y\) expresses their difference equation by a matrix with nonnegative off-diagonal entries. The standard first-contact comparison, or its elementary linear-system integrating-factor proof, preserves this coordinatewise inequality. It says exactly \(q_{i+1}-q_i\ge h\), including the seam gap. Hence no collision occurs. The relative configuration stays in a compact collision-free subset of the circle configuration space, and the center is conserved because the kernel is odd. The solution extends for all times. ∎

For circular distance \(d\in(0,N/2]\),
\[
|K_N(x)|\le2/d,\qquad
|K_N'(x)|\le\frac{\pi^2}{2d^2}.
\tag{15}
\]
Use \(\cot u\le1/u\) on \((0,\pi/2]\) and
\(\sin(\pi d/N)\ge2d/N\).

For an \(h\)-separated configuration, each of the two directions from a selected point contains its \(k\)-th neighbor no closer than \(kh\), up to the antipode. Therefore the number of other particles within distance \(R\) is at most \(2R/h\). This is also a valid upper bound when \(R>N/2\). In particular
\[
\sum_{d_j>R}d_j^{-2}\le\frac4{hR},\qquad
\sum_{0<d_j\le R}d_j^{-1}
\le\frac2h\bigl[1+\log(1+R/h)\bigr].
\tag{16}
\]
The first follows by Stieltjes integration of the counting function, discarding the negative lower-endpoint term; the second is the harmonic-sum bound. Empty sums cause no difficulty.

**Lemma 2 (relative velocity).** Two particles at circular distance \(d\) satisfy
\[
|v_i-v_j|\le\frac8h\bigl[1+\log(1+3d/h)\bigr]
+\frac{4\pi^2}{h}.
\tag{17}
\]

**Proof.** Split external particles into those within distance \(2d\) of \(i\) and the others. Include \(i,j\) themselves in the near set, but omit each self-term in its own force. For near points the two absolute force sums are bounded by (15)–(16), with radii \(2d\) around \(i\) and \(3d\) around \(j\). Their sum is bounded by the first term in (17), including the two mutual-interaction contributions.

For a far point at distance \(r>2d\) from \(i\), every point on a shortest arc joining \(i\) and \(j\) remains at distance at least \(r-d>r/2\) from it. No kernel pole crosses this interpolation. The mean-value theorem and (15) bound the kernel difference by \(2\pi^2d/r^2\). Applying (16) at \(R=2d\) gives the last term in (17). Distances and the interpolating arc are intrinsic to the circle, so the proof also applies across an arbitrary coordinate seam. ∎

For \(h=1/2\), write
\[
F(r)=16[1+\log(1+6r)]+8\pi^2.
\tag{18}
\]
The function \(F(r)/r^2\) decreases for \(r>0\), since
\(rF'(r)<16\) while \(2F(r)>32+16\pi^2\).
Differentiating (5), and using (15), (17) and the directional packing, gives
\[
|q_i''|\le\sum_{j\ne i}|K_N'(q_i-q_j)|\,|v_i-v_j|
\le4\pi^2\sum_{k\ge1}\frac{F(k/2)}{k^2}.
\tag{19}
\]
Now \(\log(1+3k)\le\log4+\log k<2+\sqrt k\) for \(k\ge1\), and \(\pi^2<10\). Hence
\(F(k/2)<128+16\sqrt k\). The elementary bounds
\(\sum k^{-2}<2\), \(\sum k^{-3/2}<3\) show that
\[
\boxed{|q_i''|<40(128\cdot2+16\cdot3)=12160<A_*.}
\tag{20}
\]
This holds uniformly in \(N\), in the configuration, and in time as long as the half-unit hard core holds; Lemma 1 supplies that condition for all our evolutions. Individual velocities have not been assumed bounded independently of \(N\). Also the same packing gives the uniform inverse-square background bound \(\sum_{j\ne i}d(q_i,q_j)^{-2}<16\).

## 4. A positive density of adjacent pairs that open

Let \(\eta_r\) indicate occupation of grid site \(r\). From (4),
\[
\mathbb E\eta_r=\tfrac12,\quad
\operatorname{Cov}(\eta_r,\eta_u)=-|\mathcal K_N(r,u)|^2\le0
\quad(r\ne u).
\tag{21}
\]
Adjacent occupation has probability
\[
p_N=\frac14-\frac1{4N^2\sin^2(\pi/(2N))}\ge\frac18
\qquad(N\ge2).
\tag{22}
\]
Indeed \(N\sin(\pi/(2N))\ge\sqrt2\); this follows from the decreasing function \(\sin x/x\) on \((0,\pi/4]\).

For \(N\ge8\), the 16 sites \(r,r+1,\ldots,r+15\) are distinct modulo \(2N\). Their occupation sum \(Z\) has mean 8 and variance at most 4 by (21). Chebyshev gives \(\Pr(Z=16)\le1/16\). Thus the event
\[
E_r=\{\eta_r=\eta_{r+1}=1,\ \hbox{at least one hole among }r+2,\ldots,r+15\}
\tag{23}
\]
has probability at least \(1/16\). This uses no independence assumption.

On this event the two adjacent selected sites are a consecutive particle pair. Lift the short arc and translate its initial endpoints to \(0,1/2\). The full \(2N\)-grid has zero force at each site, so the selected force is minus the sum over holes. For their gap \(g(s)\), the cotangent difference identity gives exactly
\[
g'(0)=\frac{2\pi}{N}\sin\frac{\pi}{2N}
\sum_{\substack{2\le h\le2N-1,\ h\text{ a hole}}}
\frac1{\sin(\pi h/(2N))\sin(\pi(h-1)/(2N))}.
\tag{24}
\]
Every term is positive. If a hole has \(2\le h\le15\), then
\(\sin(\pi/(2N))\ge1/N\) and \(\sin x\le x\) give
\[
g'(0)\ge\frac8{\pi h(h-1)}\ge\frac4{105\pi}>\frac1{84}=\beta.
\tag{25}
\]
The last inequality follows, for example, from \(\pi<22/7\).

By (20), \(|g''|\le2A_*\). For \(0\le s\le s_*\),
\[
g'(s)\ge\beta-2A_*s\ge\beta/2,\qquad
g(s)-1/2\ge\beta s/2.
\tag{26}
\]
Equation (17) gives \(|g'(0)|\le F(1/2)<128\). Therefore
\[
g(s)\le\tfrac12+128s+A_*s^2<\tfrac34
\qquad(0\le s\le s_*).
\tag{27}
\]
The last strict inequality is an elementary rational check at \(s_*\). The pair stays consecutive by Lemma 1, and its lifted gap remains shorter than \(N/2\). This deals with all original seam-crossing pairs without changing a factor of two.

## 5. Proof of the uniform local-deficit lower bound

For \(g\in[1/2,3/4]\), the nonnegative even seed in (1) satisfies
\[
\widehat f(\varepsilon g)
=\int f(x)\cos(2\pi\varepsilon gx)dx
\ge\cos(3\pi\varepsilon/4)\int f(x)dx>0.
\]
Consequently every periodized kernel value at a good gap is bounded below by
\[
k_{\varepsilon,N}(g)\ge k_\varepsilon(g)\ge\kappa_\varepsilon.
\tag{28}
\]
Put \(\Delta=g-1/2\in[0,1/4]\). Since \(\sin y\ge2y/\pi\) for \(0\le y\le\pi/2\),
\[
1-\cos(4\pi g)=2\sin^2(2\pi\Delta)
\ge32\Delta^2\ge8\beta^2s^2.
\tag{29}
\]
There are \(2N\) oriented positive grid bonds. Each event \(E_r\) selects one distinct unordered consecutive particle pair; different bonds cannot represent the same pair for \(N\ge8\). Its probability is at least \(1/16\), so the expected number of good unordered pairs is at least \(N/8\). The sum in (3) contains both orientations of every such pair. All other summands are nonnegative, and overlapping events cause no subtraction or independence issue. Equations (28)–(29) thus imply
\[
\mathbb E\mathfrak D_{\varepsilon,N}(q(s))
\ge\frac1N\left(\frac N4\right)
\kappa_\varepsilon\,8\beta^2s^2
=2\kappa_\varepsilon\beta^2s^2.
\]
This proves (8). ∎

## 6. What this does and does not say about true zeta heat

The deterministic flow can break exact half-lattice Bragg saturation while preserving the minimum gap of one half. These are different properties. Round 7's observation that the repulsive flow does not produce sub-half gaps from hard-core data does not prevent the positive deficit just proved.

In particular, there is no general implication
\[
\mathbb E\mathfrak D_{\varepsilon,N}(q(s))
\le C\,\mathbb E\mathfrak D_{\varepsilon,N}(q(0))+o_{N\to\infty}(1)
\tag{30}
\]
at every fixed \(s\in(0,s_*]\), if its only hypotheses are deterministic scalar-heat root evolution, a half-unit hard core, the uniform inverse-square background bound, and initial ACUE/CUE protected low-band data. This family satisfies all those hypotheses, and (7)–(8) contradict (30). The statement concerns precisely those hypotheses; ACUE is not asserted to satisfy the full arithmetic functional equation of zeta.

For the true de Bruijn–Newman family, \(\partial_tH_t=-\partial_z^2H_t\) has the same local repulsive sign: at simple real zeros, the suitably justified symmetric logarithmic derivative gives \(x_i'=2\operatorname{PV}\sum_{j\ne i}(x_i-x_j)^{-1}\). A local density \(\rho_T\) leads to microscopic time \(s=\rho_T^2t\). An attractive collision calculation reverses this time direction. A stochastic Dyson Brownian-motion generator has an additional diffusion term and is not (5).

Applying (8) to actual zeta would require separate, currently unproved inputs:

1. A comparison of true \(H_t\) local trajectories with a specified initial local point law, controlling the global principal-value background, the moving window and all endpoint/tail contributions in the Bragg kernel. AH-Pairs alone gives support near \((1/2)\mathbb Z\), not the ACUE law. It also permits near-zero clusters and multiplicities, which the simple hard-core model here does not have.
2. An arithmetic estimate transferring a positive-time deficit back to the **initial** \(H_0\) pair statistic. A generic bound of size \(O(s)\) does not overcome the lower bound of order \(s^2\). An assertion that the relevant difference is \(o(s^2)\) cannot follow from the deterministic background bounds alone, as this example shows. With fixed \(s\), one needs an actual signed estimate smaller than the specified positive constant after taking the height limit; with shrinking \(s\), all comparison errors must be quantified relative to \(s^2\).

Round 18's functional-reflection identities are exact identities for the original logarithmic derivative and include their gamma/trivial-zero terms. They do not automatically persist for \(H_t\), nor do their signed residue sums yield (30). The new finite theorem therefore isolates an initial-time/positive-time arithmetic obligation; it does not solve it. It neither refutes AH at time zero nor establishes a Montgomery or Dyson conjecture.

## 7. Verification and dependencies

The adjacent `check_local_bragg.py` performs one bounded float enumeration at \(N=8\) of all 12,870 subsets. It checks the ACUE probability normalization, adjacent/event probabilities, the selected-force/hole formula, the acceleration envelope and the independent global coherent-mode normalization. It also checks the stated rational constants exactly. Float calculations are diagnostics, not interval certificates or substitutes for the proof. No numerical ODE integration, parameter scan, zeta-zero computation or statistical inference is used.

For the last normalization check, the distinct global observable
\(B_N=N^{-2}|\sum_j e^{4\pi iq_j}|^2\) has, at half-grid initial data,
\(B_N''(0)=-128\pi^4N^{-3}\sum_jV_j^2\), so
\(\mathbb EB_N''(0)=-(64\pi^4/3)(1-N^{-2})\).
The root's separate [coherent-mode proof](../root-bragg-curvature/EXACT_COHERENT_MODE_CURVATURE.md) derives this exactly. It is not the localized statistic (3), and its fixed-\(N\) Taylor expansion is not used to prove (8).

The theorem's proof above is self-contained apart from standard finite projection-DPP identities and elementary ODE comparison/Fourier identities, all instantiated explicitly. Programme dependencies provide the choice of observable and the transfer cautions:

- [Round 16 Bragg target](../../research-round16/bragg-atom/BRAGG_ATOM_TARGET.md), SHA256 `2228bfd90e7a633683936d3d611f31c1f960107fbdf111a494993f73be16e120`: equations (2)–(9), (11)–(12), the actual-zeta near-zero/AH qualifications.
- [Round 7 forward-flow obstruction](../../research-round7/true-zeta-flow/FORWARD_FLOW_OBSTRUCTION.md): the prior distinction between deterministic flow, stochastic relaxation and an actual-zeta external-field comparison.
- [Round 3 force-energy proof](../../research-round3/force_energy.md): the independent coherent Bragg-mode check uses its ACUE force-square expectation, not as an input to (8).
- [Round 18 functional reflection](../../research-round18/functional-reflection/FUNCTIONAL_REFLECTION_IDENTITY.md), SHA256 `c6d8359bdecb2f0616647920ef7f7efd861ca6d1bf03995f303b4a41a77ec701`: the static arithmetic identities do not assert a heat-time transfer.
- [Rodgers–Tao, *The de Bruijn–Newman constant is non-negative*](https://arxiv.org/abs/1801.05914): primary context for the true entire-function heat family and zero dynamics. No additional positive-time uniform arithmetic comparison theorem is imported from that paper.

Postponed: optimizing the tiny universal constants, proving a limiting infinite ACUE flow, extending to clustered AH data, and establishing any true-zeta heat or Bragg transfer. These would be additional mathematical tasks, not consequences of the present proof.
