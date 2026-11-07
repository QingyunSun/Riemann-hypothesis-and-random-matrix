# A concrete obstruction to inferring original zeta statistics from DBM regularization

6 November 2026. This is a direct application of an existing universality theorem, with an explicit clock example. It is a methodological obstruction, not a new universality theorem or an actual-zeta result.

## Source theorem and scale conventions

Landon–Sosoe–Yau, [arXiv:1609.09011v4](https://arxiv.org/abs/1609.09011v4), Definition 2.1 and Theorem 2.2, consider the real-line Gaussian-divisible ensemble \(H_t=V+\sqrt{t}W\). The Hermitian/GUE version is stated in the remark following the theorem. The initial diagonal V must have polynomially bounded norm and
\[
c\le \operatorname{Im}m_V(E+i\eta)\le C
\quad (|E|\le G,\ g\le\eta\le10).
\]
The time range is \(gN^\sigma\le t\le N^{-\sigma}G^2\). The local scaling uses the free-convolution density \(\rho_{\mathrm{fc},t}(E)\). It is not the same process as circular DBM or deterministic scalar heat.

The v4 PDF was compared directly with v3: the displayed v4 correlation statement has density prefactors, and its following remark explicitly addresses the Hermitian case. Definition 2.1 and the main time constraints agree in the compared passages. Appendix F already exists in v3. The weakened-regularity universality theorem F.1 requires \(s=N^{\omega-1}\) with \(\omega>2/3\); the local-law theorem F.2 does not require this stronger time restriction. This is not an assertion that every line of the revisions was compared.

## Proposition: even a perfectly rigid clock defeats generic backward inference

Let
\[
v_j=\frac{j-(N+1)/2}{N},\quad 1\le j\le N.
\]
Choose
\[
g=N^{-9/10},\quad G=N^{-1/10},\quad
t=N^{-4/5},\quad \sigma=1/20.
\]
These parameters satisfy the source's scale requirements for large N: one may take δ=1/20 in its auxiliary assumptions \(N^{\delta-1}\le g\le N^{-\delta},\ G\le N^{-\delta}\). In particular,
\[
gN^\sigma=N^{-17/20}\le t,\qquad
t\le N^{-\sigma}G^2=N^{-1/4}.
\]
The points are the exact midpoint quantiles for the uniform density on [-1/2,1/2]: their error from those quantiles is zero (and from the alternative j/N quantile convention it is exactly 1/(2N)). Thus they satisfy optimal microscopic rigidity.

Fix nonnegative smooth bumps h,φ of integral one, with h compactly supported and supp φ contained in (1/4,1/3). Set
\[
O(a,b)=h((a+b)/2)\phi(a-b).
\]
Let ρ_N=ρ_fc,t(0), and define the ordered, distinct two-point statistic
\[
F_{N,t}(\lambda)=\sum_{i\ne j}O(N\rho_N\lambda_i,N\rho_N\lambda_j).
\]
The subscript t in F fixes the final density scaling; this same function is used at both initial and final times. Then
\[
F_{N,t}(v)=0
\]
for all sufficiently large N, but for Hermitian DBM
\[
\lim_{N\to\infty}\mathbb E F_{N,t}(\lambda(t))
=\iint O(a,b)\left[1-\left(\frac{\sin\pi(a-b)}{\pi(a-b)}\right)^2\right]\,da\,db
\ge 1-\frac8{\pi^2}>0.
\]

### Verification of the regularity premise

The v_j are midpoints of N equal intervals. For f(v)=η/((v−E)²+η²), its total variation on the real line is 2/η. Thus
\[
\left|\frac1N\sum_j f(v_j)-\int_{-1/2}^{1/2}f(v)\,dv\right|
\le\frac{2}{N\eta}.
\]
For |E|≤G≤1/4 the integral is
\[
\arctan((1/2-E)/\eta)+\arctan((1/2+E)/\eta),
\]
between 2 arctan(1/40) and π for g≤η≤10. The error is at most 2N^(-1/10)=o(1). The required positive lower and finite upper bounds follow uniformly. Also \(\|V\|\le1/2\).

### The t-dependent density causes no loophole

By symmetry the boundary Stieltjes transform of the free convolution at zero is i b_N, with b_N bounded above and below by the source's regularity conclusions. Its fixed-point equation gives
\[
b_N=\frac1N\sum_j\frac{t b_N}{v_j^2+(t b_N)^2}
=2\arctan\frac{1}{2t b_N}+O((Nt)^{-1}).
\]
Since t→0 and Nt→∞, b_N→π, hence ρ_N=b_N/π→1. Every nonzero initial unfolded separation is therefore ρ_N times a positive integer in absolute value. It cannot enter (1/4,1/3) for large N.

### Observable normalization and positive limiting difference

If \(p_t^{(2)}\) denotes the symmetrized two-coordinate marginal density used in the paper, then
\[
\mathbb E F_{N,t}
=\frac{N-1}{N}\frac1{\rho_N^2}
\iint O(a,b)\,
p_t^{(2)}\left(\frac a{N\rho_N},\frac b{N\rho_N}\right)\,da\,db.
\]
Thus the normalization is precisely the one to which the corrected density-prefactor version of Theorem 2.2 applies. The GUE limit is the unit-intensity sine two-point function.

With u=(a+b)/2 and v=a−b the Jacobian has absolute value one. On (1/4,1/3), sin(πv)/(πv) is positive and decreasing, so its square is at most 8/π². Since both bumps integrate to one, the lower bound follows.

This proves that mesoscopic resolvent regularity, even supplemented by perfect initial rigidity, cannot imply
\[
\mathbb E F_{N,t}(\lambda(t))-F_{N,t}(v)=o(1).
\]
The theorem itself supplies the counterexample to such a proposed backward inference.

## The missing estimate in Duhamel form

For real-line Hermitian DBM, in the normalization \(d\lambda_i=N^{-1/2}dB_i+N^{-1}\sum_{j\ne i}(\lambda_i-\lambda_j)^{-1}ds\), the generator is
\[
\mathcal L_N
=\frac1{2N}\sum_i\partial_i^2+
 \frac1N\sum_{i\ne j}\frac{1}{\lambda_i-\lambda_j}\partial_i.
\]
For the smooth symmetric \(F_{N,t}\), localization of Itô's formula gives
\[
\mathbb E F_{N,t}(\lambda(t))-F_{N,t}(\lambda(0))
=\int_0^t\mathbb E[(\mathcal L_NF_{N,t})(\lambda(s))]\,ds.
\]
The pair singularities cancel on smooth symmetric functions, or one can first stop away from collisions and then pass to the limit. In the clock example this integral has a positive order-one limit.

Consequently, adding DBM to a finite window of zeta zeros could prove universality for the *regularized* window once its hypotheses are checked. Returning to the original zeros requires a separate, observable-specific smallness estimate for this integral, or a comparison principle of equivalent strength. No such estimate is established here from RH, a zero-count moment bound or a local density law. The clock rules out deducing it from generic regularity and rigidity alone. This identifies where an actual-zeta comparison would need additional, plausibly arithmetic information.

The programme's [circular DBM protected-multitime theorem](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/codex/astra-research/research/counterexamples/stochastic-protection/AGENT_STOCHASTIC_PROTECTION.md) is a separate result: it preserves agreement of low-weight expectations between two initial laws. It does not establish this backward comparison for unprotected microscopic observables. The finite scalar-heat collision results use a third flow with attractive deterministic root dynamics.
