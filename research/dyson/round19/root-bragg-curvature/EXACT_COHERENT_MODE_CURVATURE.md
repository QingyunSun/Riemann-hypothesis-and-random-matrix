# Exact initial curvature of the coherent ACUE Bragg mode

Date: 2026-09-05. Author: Astra root. Status: finite-N ordinary identity, submitted to the independent flow reviewer. This note supplies a normalization check and an exactly evaluated dynamic statistic. It is not a uniform positive-time theorem, a localized R16 deficit identity, or a statement about true zeta zeros. No global novelty claim is made.

## 1. Observable and time convention

Let N>=2, let theta_i be radians, and evolve the collision-free circular configuration by

\[
\frac{d\theta_i}{dt}=V_i(\theta)
=\sum_{j\ne i}\cot\frac{\theta_i-\theta_j}{2}.
\]

This is the repulsive deterministic scalar polynomial heat flow, not stochastic Dyson Brownian motion. Use the same microscopic time as the earlier audited reports,

\[
s=\frac{N^2t}{4\pi^2},\qquad q_i=\frac{N\theta_i}{2\pi},\qquad
\frac{dq_i}{ds}=\frac{2\pi}{N}V_i.
\]

For any N-point subset of a rotated 2N grid, the phases exp(2Ni theta_i) initially all agree. Define the global coherent mode

\[
B_N(s)=\frac1{N^2}\left|\sum_i e^{2Ni\theta_i(s)}\right|^2
=\frac1{N^2}\left|\sum_i e^{4\pi i q_i(s)}\right|^2.
\]

Initially B_N(0)=1. This observable weights all pairs equally. The localized R16 statistic instead includes a specific decaying pair kernel, so the two must not be identified.

## 2. Deterministic curvature identity

Put u_i=4pi*q_i and Z=N^(-1)sum_i exp(i*u_i), so B_N=|Z|^2. Pairwise antisymmetry gives sum_i V_i=0 at every collision-free configuration, hence sum_i u_i'=0 and sum_i u_i''=0. At the common initial phase z_0,

\[
Z(0)=z_0,\quad Z'(0)=0,\quad
Z''(0)=-\frac{z_0}{N}\sum_i(u_i'(0))^2.
\]

Using u_i'=(8pi^2/N)V_i proves the exact formula

\[
\boxed{B_N''(0)=-\frac{128\pi^4}{N^3}\sum_iV_i(0)^2.}
\]

The derivative is nonpositive for every grid subset, and zero precisely when the initial velocity vector vanishes. A common rotation does not affect the result.

## 3. Exact expectation under the ACUE law

The unrotated ACUE law on unordered N-subsets of the 2N grid is

\[
\Pr(S)=(2N)^{-N}\prod_{a<b\in S}
|e^{\pi ia/N}-e^{\pi ib/N}|^2.
\]

Its projection determinantal kernel is

\[
K_N(a,b)=\frac1{2N}\sum_{r=0}^{N-1}e^{\pi ir(a-b)/N}.
\]

Thus for distinct grid sites at displacement d, the two-point occupation probability is

\[
p_d=\frac14-
\frac{\sin^2(\pi d/2)}{4N^2\sin^2(\pi d/(2N))}.
\]

For every collision-free circular configuration, the elementary three-point cotangent identity gives

\[
\sum_iV_i^2
=2\sum_{i<j}\csc^2\frac{\theta_i-\theta_j}{2}
-\frac{N(N^2-1)}3.
\]

To see the constant, expansion of the squares gives twice the sum of pairwise cotangent squares and, for each unordered triple, twice the quantity
cot_ij*cot_ik+cot_ji*cot_jk+cot_ki*cot_kj=-1. Replacing cot^2 by csc^2-1 gives the displayed identity.

The complete-grid trigonometric sums are

\[
\sum_{d=1}^{m-1}\csc^2(\pi d/m)=\frac{m^2-1}3,
\qquad
\sum_{d=1}^{m-1}\csc^4(\pi d/m)=
\frac{(m^2-1)(m^2+11)}{45}.
\]

They follow by differentiating the logarithm of the sine product, or by expanding
sum_(d=0)^(m-1)csc^2(x+pi*d/m)=m^2*csc^2(mx) near x=0. Subtracting the even sites gives

\[
\sum_{\substack{1\le d<2N\\d\text{ odd}}}
\csc^4(\pi d/(2N))=\frac{N^2(N^2+2)}3.
\]

Translation symmetry, followed by the two-point probability, yields

\[
\begin{aligned}
\mathbb E\left[2\sum_{i<j}\csc^2\frac{\theta_i-\theta_j}{2}\right]
&=2N\sum_{d=1}^{2N-1}p_d\csc^2(\pi d/(2N))\\
&=\frac N2\frac{4N^2-1}3
-\frac1{2N}\frac{N^2(N^2+2)}3\\
&=\frac{N(N^2-1)}2.
\end{aligned}
\]

Consequently the previously audited force-energy expectation is recovered directly:

\[
\mathbb E_{\rm ACUE}\sum_iV_i^2=\frac{N(N^2-1)}6.
\]

For each fixed N the ensemble is finite. Differentiation through its expectation at zero is therefore legitimate, and

\[
\boxed{\mathbb E B_N''(0)
=-\frac{64\pi^4}{3}(1-N^{-2}).}
\]

Equivalently, as s tends to zero at fixed N,

\[
\mathbb E B_N(s)=1-
\frac{32\pi^4}{3}(1-N^{-2})s^2+o_N(s^2).
\]

At N=2, an adjacent occupied pair has total probability 1/2 and squared force sum 2, while an opposite pair has total probability 1/2 and zero force. The expected curvature is therefore -16pi^4, agreeing with the formula. This finite exact example checks the time conversion independently.

## 4. What the identity does and does not add

The mean initial coherent-mode curvature has a nonzero N-infinity limit. This is an explicit relation between out-of-band Bragg coherence and the rational force-energy observable that already separates ACUE and CUE. It is outside the protected low-trace algebra. It shows that calling this deterministic flow stationary at ACUE would be incorrect.

The displayed fixed-N Taylor expansion has no uniform remainder in N. It cannot alone produce a fixed microscopic-time limit, a strictly smaller limiting spectral atom, or the localized R16 deficit. Such a conclusion requires a separately proved uniform estimate. The flow agent's distinct local-pair opening argument is intended to address a finite-time localized statement and must be reviewed on its own terms.

No step imports stochastic DBM universality, transports a positive-time result back to initial zeta zeros, or proves that the global H_t has this circular finite-system law. The actual initial-zeta strict deficit remains open.

## 5. Internal dependencies

The derivation is self-contained apart from the specified ACUE projection law, rederived in the earlier source audit. The normalization and force identities are independently consistent with:

- `research/reports/dynamic_generator.md`: circular root ODE, microscopic convention, protected polynomial moments and ACUE normalization.
- `research/reports/force_energy.md`: exact ensemble force expectations and cotangent identities.
- `research/dyson/round7/true-zeta-flow/FORWARD_FLOW_OBSTRUCTION.md`: deterministic/stochastic distinction and the missing actual-zeta transfer.

This is a proof calculation, not a numerical experiment; no floating simulation or performance benchmark is needed for the stated identity.
