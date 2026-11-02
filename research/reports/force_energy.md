# Circular force-square observable: exact identities and expectation audit

2026-09-05. All angles in this report are measured in radians on a circle of circumference 2π. Here **D means force-square energy**, not the first-collision time denoted D in earlier reports. The calculations concern the deterministic repulsive flow θ̇i=Vi.

## 1. Findings

For distinct angles, define

$$V_i=\sum_{j\ne i}\cot\frac{\theta_i-\theta_j}{2},\qquad
D=\sum_iV_i^2,\qquad
Q=\sum_{i\ne j}\csc^2\frac{\theta_i-\theta_j}{2},\qquad
C_N=\frac{N(N^2-1)}3.$$

Then the following are exact mathematical identities:

$$D=Q-C_N,$$

$$\mathbb E_{\mathrm{CUE}}D=C_N,\qquad
\mathbb E_{\mathrm{ACUE}}D=\frac{C_N}{2},$$

where ACUE is the N-particle projection process on the 2N-th roots of unity with the consecutive N Fourier modes. For the deterministic generator

$$\mathcal L=\sum_iV_i\partial_{\theta_i},$$

one has

$$\mathcal L D=-\sum_{i<j}\csc^2\frac{\theta_i-\theta_j}{2}(V_i-V_j)^2\le0.$$

For every N≥2,

$$\mathbb E_{\mathrm{CUE}}\mathcal LD=-\infty,$$

whereas the ACUE expectation is finite and in fact

$$\mathbb E_{\mathrm{ACUE}}\mathcal LD=-\frac{2N(N^4-1)}{15}.$$

The last formula was first suggested by floating-point enumeration and then derived algebraically below. It is not being promoted from a numerical fit to a theorem without a proof.

The score normalization in the user's proposed argument needs correction: for the CUE density in radian coordinates, **the score is V, not 2V**. Also, the apparent higher-order observable D collapses pointwise to a singular two-point energy. Its different expectations do not automatically provide an arithmetically accessible statistic of ζ zeros.

## 2. Score and deterministic-flow normalization

The circular-beta density is

$$p_\beta(\boldsymbol\theta)=Z_{N,\beta}^{-1}
\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^\beta.$$

Differentiating log|eiθi−eiθj| gives one half of the cotangent. Thus

$$\partial_{\theta_i}\log p_\beta=\frac\beta2V_i.$$

For CUE, β=2, so the score is exactly V. This density convention agrees with [Feng–Wei's definition of CβE](https://arxiv.org/abs/1806.01555). The discrete ACUE measure does not have a Lebesgue density on the full angular configuration space, so V should not be called its ordinary continuous Fisher score.

The generator here is for θ̇=V. If the deterministic drift is instead V/(2N), all generator expectations below are divided by 2N; the observable D itself is unchanged. If the attractive flow θ̇=−V is used, the generator signs reverse. These deterministic flows are not stochastic DBM; Haar CUE invariance under a stochastic process does not imply invariance under the deterministic drift alone.

For the centered real characteristic polynomial

$$Q_0(x)=\prod_j\sin\frac{x-\theta_j}{2},$$

the force has the exact intrinsic expression

$$V_i=\frac{Q_0''(\theta_i)}{Q_0'(\theta_i)}.$$

This does identify a natural derivative-ratio candidate when one studies another real entire function. It does not evaluate its average over that function's zeros.

## 3. Pointwise collapse of the force square

Put cij=cot((θi−θj)/2), so cji=−cij. Expanding the square,

$$D=\sum_{i\ne j}c_{ij}^2
 +2\sum_{\{i,j,k\}}
(c_{ij}c_{ik}+c_{ji}c_{jk}+c_{ki}c_{kj}).$$

For each unordered triple, the expression in parentheses is −1. This follows from cot(a+b)=(cot a cot b−1)/(cot a+cot b), or from clearing denominators in that identity. Since cot²=csc²−1,

$$D=Q-N(N-1)-2\binom N3
=Q-\frac{N(N^2-1)}3.$$

No averaging, randomness, or spacing approximation has been used. In particular, an expectation of D contains only two-point information once the singular test kernel is specified.

## 4. CUE expectation by a legitimate integration by parts

The divergence of V is

$$\sum_i\partial_{\theta_i}V_i=-\frac12Q.$$

For β=2, integration by parts against p2 therefore yields

$$\mathbb E_{\mathrm{CUE}}D=\frac12\mathbb E_{\mathrm{CUE}}Q.$$

This particular integration by parts is legitimate. Near an isolated collision with gap g, the density vanishes quadratically, while V has at most a first-order pole. The boundary flux p2Vi consequently vanishes. Alternatively, multiplying out the Vandermonde factors removes the apparent pole in p2Vi, and its derivative is integrable on the compact torus. The products p2Vi² and p2Q are integrable as well, including at intersections of collision hyperplanes.

Combining this identity with D=Q−CN gives EQ=2CN and ED=CN. The same calculation for β>1 gives ED=CN/(β−1), but no extension of the present task to other model families is needed.

Crucially, this integrability check does **not** justify applying the same argument to LD, which has a fourth-order gap singularity.

## 5. ACUE expectation from its exact discrete kernel

Let M=2N and label the grid by x in Z/MZ, with θx=2πx/M. The rank-N projection kernel is

$$K(x,y)=\frac1{2N}\sum_{a=0}^{N-1}e^{2\pi ia(x-y)/(2N)}.$$

It has K(x,x)=1/2. For d≠0 mod 2N, define

$$w_d=\csc^2\frac{\pi d}{2N}.$$

Then K(x,x+d)=0 for nonzero even d, while for odd d,

$$|K(x,x+d)|^2=\frac{w_d}{4N^2}.$$

Hence the two-site inclusion probability is

$$\rho_2(0,d)=\frac14-\frac{\mathbf1_{d\text{ odd}}}{4N^2}w_d.$$

It follows that

$$\mathbb E_{\mathrm{ACUE}}Q
=\frac N2\sum_{d=1}^{2N-1}w_d
-\frac1{2N}\sum_{\substack{1\le d<2N\\d\text{ odd}}}w_d^2.$$

The needed trigonometric sums are

$$\sum_{d=1}^{M-1}\csc^2\frac{\pi d}{M}=\frac{M^2-1}{3},$$

$$\sum_{d=1}^{M-1}\csc^4\frac{\pi d}{M}=\frac{M^4+10M^2-11}{45},$$

and subtraction of the even sites gives

$$\sum_{d\text{ odd}}w_d^2=\frac{N^2(N^2+2)}3.$$

Consequently

$$\mathbb E_{\mathrm{ACUE}}Q=\frac{N(N^2-1)}2=\frac32C_N,$$

which proves ED=CN/2. The model convention is the ACUE described in [Tao's original post](https://terrytao.wordpress.com/2019/05/08/the-alternative-hypothesis-for-unitary-matrices/).

The cosecant identities can be derived from

$$\sum_{d=0}^{M-1}\cot(x+\pi d/M)=M\cot(Mx)$$

by differentiation and comparison of Laurent coefficients at zero. This gives exact algebraic identities, rather than an approximation of a continuum integral by a lattice sum.

## 6. The dissipative generator identity

Let wij=csc²((θi−θj)/2). The Jacobian JV of V is symmetric, with diagonal entries −(1/2)Σj≠i wij and off-diagonal entries wij/2. Therefore

$$\mathcal LD=2V^T J_VV
=-\sum_{i<j}w_{ij}(V_i-V_j)^2.$$

This proves pointwise nonpositivity. The repulsive flow exists globally for each initially distinct configuration: the logarithmic Vandermonde potential

$$W=\sum_{i<j}\log|e^{i\theta_i}-e^{i\theta_j}|$$

satisfies dW/dt=D/2≥0. Every summand is bounded above by log2, so a collision would force W to negative infinity, contradicting its lower bound W(0). The vector field therefore remains away from its singular set along each fixed initial trajectory, and D decreases.

## 7. Why the CUE expected derivative is negative infinity

Restrict to configurations in which exactly one pair has gap g→0 and all other points remain uniformly separated from that pair and each other. This set has positive measure in the remaining coordinates. Then

$$V_i-V_j=\frac4g+O(g),\qquad w_{ij}=\frac4{g^2}+O(1),$$

so

$$\mathcal LD=-\frac{64}{g^4}+O(g^{-2}).$$

The CUE joint density on this region is a positive smooth factor times g². Since LD≤0 everywhere,

$$\mathbb E_{\mathrm{CUE}}[-\mathcal LD]
\ge c\int_0^\varepsilon g^{-2}\,dg=+\infty.$$

Thus E LD=−∞ in the extended sense for N≥2. There is no cancellation between positive and negative parts to rescue an ordinary finite expectation.

Moreover, it is possible to state the expectation-level consequence without illegally exchanging derivative and integral. Let Φt be this deterministic repulsive flow. Since 0≤D(Φt)≤D initially and ED is finite, Fatou's lemma applied to

$$\frac{D(\theta)-D(\Phi_t\theta)}t\ge0$$

shows

$$\lim_{t\downarrow0}\frac{\mathbb E D(\Phi_t)-\mathbb ED}{t}=-\infty.$$

This is an infinite right slope, not a finite derivative obtained by a formal interchange. The finite ACUE support allows differentiation of its finite weighted sum at t=0.

For N=2 there is a transparent check. If g is the labeled angle difference, its CUE density is sin²(g/2)/π on (0,2π). Integrating only over ε≤g≤2π−ε gives

$$\mathbb E[D;\epsilon\le g\le2\pi-\epsilon]
=2-\frac2\pi(\epsilon+\sin\epsilon)\to2,$$

$$\mathbb E[\mathcal LD;\epsilon\le g\le2\pi-\epsilon]
=8-\frac{16}{\pi}\cot(\epsilon/2)-\frac{8\epsilon}{\pi}\to-\infty.$$

## 8. Exact finite ACUE derivative

The explicit finite answer is

$$\mathbb E_{\mathrm{ACUE}}\mathcal LD=-\frac{2N(N^4-1)}{15}.$$

Here is a derivation, including the ordering factors.

### 8.1 Reducing the derivative to at most three sites

Differentiating Q−CN directly and using a three-angle cotangent identity yields

$$\mathcal LD=-4\sum_{i<j}(w_{ij}^2-w_{ij})
 +\sum_{i<j<k}(w_{ij}w_{ik}+w_{ij}w_{jk}+w_{ik}w_{jk}). \tag{8.1}$$

For verification of the triple algebra, put c=cot((θ1−θ2)/2), a=cot((θ2−θ3)/2), b=(ca−1)/(c+a). Then

$$\begin{aligned}
&(1+c^2)c(b-a)+(1+b^2)b(c+a)+(1+a^2)a(b-c)\\
&=-\frac12[(1+c^2)(1+a^2)+(1+c^2)(1+b^2)+(1+a^2)(1+b^2)].
\end{aligned}$$

The expression extends by continuity wherever the chosen cotangent-addition denominator vanishes but the original angles are distinct.

### 8.2 ACUE three-site probability

Among any three grid sites at least two have the same parity. Their off-diagonal kernel entry is zero, so the triangular product in the 3×3 determinant vanishes. Therefore

$$\rho_3(0,d,e)=\frac18-\frac1{8N^2}
[\mathbf1_{d\text{ odd}}w_d+\mathbf1_{e\text{ odd}}w_e+
\mathbf1_{d-e\text{ odd}}w_{d-e}],$$

for d,e nonzero and distinct modulo 2N.

Put S2=Σd wd, S4=Σd wd², O4=Σd odd wd², O6=Σd odd wd³. The pair part of (8.1) has expectation

$$-\frac M2(S_4-S_2)+\frac{M}{2N^2}(O_6-O_4),\qquad M=2N.$$

By symmetry the three edge products in the unordered-triple term contribute equally. Its expectation is

$$\frac M2\sum_{d,e\ne0,\ d\ne e}\rho_3(0,d,e)w_dw_e.$$

The factor is M/2: the ordered triple count gives M/6, followed by the three equal edge-product contributions.

For odd d, the useful even-site convolution is

$$\sum_{\substack{e\ne0\\e\text{ even}}}w_e w_{d-e}
=\frac{4N^2+5}{3}w_d-3w_d^2.$$

To derive it, use

$$\csc^2u\csc^2v=\csc^2(u+v)
[\csc^2u+\csc^2v+2\cot(u+v)(\cot u+\cot v)]$$

with u=πe/(2N), v=π(d−e)/(2N), and sum over nonzero even e. The shifted cotangent sum vanishes before its e=0 term is removed, because cot(πd/2)=0 for odd d. This gives the displayed convolution exactly.

It follows that the triple term has expectation

$$\frac M{16}\left[
S_2^2-S_4-\frac1{N^2}
\left(\frac83(2N^2+1)O_4-8O_6\right)\right].$$

Adding the pair term gives

$$\mathbb E\mathcal LD=\frac M{16}\left[
S_2^2-9S_4+8S_2+\frac{16}{N^2}O_6
-\frac{16(N^2+2)}{3N^2}O_4\right].$$

Finally,

$$S_2=\frac{4N^2-1}{3},\quad
S_4=\frac{16N^4+40N^2-11}{45},\quad
O_4=\frac{N^2(N^2+2)}3,$$

$$O_6=\frac{N^2(2N^4+5N^2+8)}{15}.$$

The last identity is the odd-site difference of

$$\sum_{d=1}^{M-1}\csc^6\frac{\pi d}{M}
=\frac{2M^6+21M^4+168M^2-191}{945},$$

obtained by further differentiation of the same cotangent partial-fraction identity. Substitution simplifies to −2N(N⁴−1)/15, as claimed.

## 9. What this does and does not provide for the research programme

The finite mean separation is genuine: ED/N³ tends to 1/3 in CUE and 1/6 in ACUE. But the mechanism is a singular two-point test. It is not a new independent three-point invariant disguised as a force square. Any laws that have the same full two-point marginal on the same finite grid must have the same ED. Thus this mean alone does not distinguish all the previous ACUE moment-fiber counterexamples.

The kernel csc² has a diagonal singularity and requires information beyond the usual bounded, limited-Fourier-support pair-correlation tests. A finite-grid trigonometric interpolant of that kernel is a different function away from the grid; using its CUE expectation would silently change the observable. A rigorous arithmetic use needs a specified regularization, an evaluable weighted zero sum, and uniform control of the error when the diagonal cutoff is removed.

The canonical ratio H0″/H0′ at simple zeros is a possible arithmetic formulation of the force. Its squared mean involves inverse derivatives and singular near-pair behavior; the circle identities and CUE integration by parts do not evaluate that mean for ζ. Gamma-factor contributions, the chosen H-coordinate, and the canonical-product normalization would all have to be retained in a direct real-line formulation.

The infinite CUE initial slope is another constraint on a proposed comparison. One cannot posit a finite Taylor expansion of the expected energy around zero time and then compare its first coefficients with ACUE. Regularized observables or a nonanalytic short-time analysis would be necessary. No such arithmetic comparison is proved here.

## 10. Floating-point enumeration and algebra checks

`research/force-energy/force_energy.py` visits every N-subset of the 2N grid for N=2,…,10, using the weights

$$\mu(S)=(2N)^{-N}\prod_{i<j\in S}|e^{i\theta_i}-e^{i\theta_j}|^2.$$

The traversal is exhaustive; all trigonometric values, weights, and expectations are float64. It is therefore **not exact-arithmetic enumeration**. The proof of the exact formulas is in the preceding sections.

| N | Subsets visited | E D, float64 | E LD, float64 |
|---:|---:|---:|---:|
| 2 | 6 | 1 | −4 |
| 3 | 20 | 4 | −32 |
| 4 | 70 | 10 | −136 |
| 5 | 252 | 20 | −416 |
| 6 | 924 | 35 | −1036 |
| 7 | 3432 | 56 | −2240 |
| 8 | 12870 | 84 | −4368 |
| 9 | 48620 | 120 | −7872 |
| 10 | 184756 | 165 | −13332 |

At N=10 the total probability differs from 1 by about 2.5×10⁻¹⁴, and the maximum pointwise error in D=Q−CN is below 6.9×10⁻¹³. The script also checks the generator formula against a finite directional difference at four configurations, and evaluates the exact N=2 truncated integrals to exhibit the divergent derivative expectation. Its JSON and log are saved beside this report. These computations support normalization checks; they do not replace the integrability proof.
