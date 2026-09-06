# CUE background at the selected smallest gap: a direct finite-N bound

Date: 2026-09-05. Author: Astra subagent `yau_flow`. Status: complete ordinary-proof draft submitted for independent review. This is a CUE-only estimate using its exact finite-dimensional determinant. It does not invoke any general-beta correlation inequality, assert novelty against the entire literature, or transfer a random-matrix result to zeta zeros.

The finite CUE heat-depth ratio was already derived qualitatively in Round 1, `yau_flow.md` Sections 3–4, and its deterministic Galilean refinement was quantified in Round 2, `galilean-proof-audit.md` Sections 1–5. Those results are not being presented as new here. The additional estimate is tightness at the natural \(N^2\) scale for the background of the **selected minimum pair**, with an explicit finite-N truncated first-moment bound. It sharpens the rate obtained by applying the existing deterministic lemma.

## 1. Exact geometry and statement

Let \(U_N\) have Haar law on \(U(N)\). Its eigenangles are points of \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with ordered representatives \(\theta_1<\cdots<\theta_N\) and \(\theta_{N+1}=\theta_1+2\pi\). Write
\[
\delta_i=\theta_{i+1}-\theta_i,\quad
c_i=\theta_i+\delta_i/2\pmod{2\pi},\quad
\delta_N^{\min}=\min_i\delta_i.
\]
All roots are distinct almost surely. Any fixed deterministic tie-breaking convention may select the minimum; ties have probability zero.

For circular distance \(r(x)=\min_{k\in\mathbb Z}|x-2\pi k|\in[0,\pi]\), put
\[
q(x)=\frac1{4\sin^2(x/2)}.
\]
The midpoint background and the larger endpoint background of a consecutive gap are
\[
B_i=\sum_{k\ne i,i+1}q(\theta_k-c_i),\qquad
S_i=\sum_{k\ne i,i+1}
\bigl[q(\theta_k-\theta_i)+q(\theta_k-\theta_{i+1})\bigr].
\tag{1}
\]
The selected background is \(B_N=B_{i_*}\), where \(\delta_{i_*}=\delta_N^{\min}\).

**Finite-N proposition.** For every \(N\ge2\) and \(0<\varepsilon\le\pi\),
\[
\boxed{\quad
\mathbb E\sum_{i:\,\delta_i\le\varepsilon}B_i
\le \frac{N^6\varepsilon^3}{18}.
\quad}
\tag{2}
\]
The same bound holds with \(B_i\) replaced by \(S_i\). In fact the proof bounds the endpoint-background sum over **all ordered pairs** whose positive oriented separation is at most \(\varepsilon\), even when they are not consecutive.

Consequently, for fixed \(L>0\) and all sufficiently large \(N\),
\[
\mathbb E\sum_{i:\,\delta_i\le L N^{-4/3}}\frac{B_i}{N^2}
\le\frac{L^3}{18}.
\tag{3}
\]
No conditional density at the minimum is used.

## 2. A three-point bound that retains the endpoint zeros

With correlation densities measured against ordinary angular Lebesgue measure, use the periodic CUE kernel
\[
K_N(x,y)=\frac1{2\pi}\sum_{m=0}^{N-1}e^{im(x-y)},\qquad
\rho_k(x_1,\ldots,x_k)=\det[K_N(x_a,x_b)]_{a,b\le k}.
\]
This determinant convention counts ordered distinct tuples. It is gauge-equivalent to the sine kernel in Feng–Wei, Section 1.2, printed page 5; the integer-frequency form avoids any artificial cut or antiperiodic-kernel issue.

Let
\[
\phi(x)=\frac1{\sqrt{2\pi}}(1,e^{ix},\ldots,e^{i(N-1)x}),
\quad A=\|\phi(x)\|^2=\frac N{2\pi},
\quad D=\|\phi'(x)\|^2
=\frac{N(N-1)(2N-1)}{12\pi}\le\frac{N^3}{6\pi}.
\]
For \(0<d\le\pi\), Gram determinant factorization gives
\[
\rho_2(0,d)\le A\|\phi(d)-\phi(0)\|^2\le ADd^2.
\]
Let \(\Pi\) be orthogonal projection onto the span of \(\phi(0),\phi(d)\). Then
\[
\rho_3(0,d,z)=\rho_2(0,d)\|(I-\Pi)\phi(z)\|^2.
\]
The final squared norm is at most \(A\), and also at most
\(\|\phi(z)-\phi(0)\|^2\le D r(z)^2\), because \(\phi(0)\) belongs to that span and \(\phi\) is periodic. Therefore
\[
\rho_3(0,d,z)
\le ADd^2\min\{A,D r(z)^2\}
\le\frac{N^5d^2}{24\pi^3}
\min\{1,N^2r(z)^2\}.
\tag{4}
\]
The sharper factor \(N^2r^2/3\) in the second branch was weakened to \(N^2r^2\). Equivalently, the two elementary bounds before this weakening are \(N^5d^2/(24\pi^3)\) and \(N^7d^2r^2/(72\pi^3)\). For \(N=2\), the third density is zero, so the same conclusion holds. Coincident points are null sets and can be handled by continuity.

This is the needed finite-dimensional replacement for a general-beta background claim. It simultaneously supplies the short-pair factor \(d^2\) and the endpoint cancellation \(r(z)^2\).

## 3. Integrating the singular weight

For \(0<r\le\pi\), \(\sin(r/2)\ge r/\pi\), hence
\[
q(z)\le\frac{\pi^2}{4r(z)^2}.
\]
Splitting at \(r=1/N\) yields
\[
\begin{split}
\int_{\mathbb T}q(z)\min\{1,N^2r(z)^2\}\,dz
&\le\frac{\pi^2}{2}
\left(\int_0^{1/N}N^2\,dr+\int_{1/N}^{\pi}r^{-2}\,dr\right)\\
&=\frac{\pi^2}{2}(2N-1/\pi)\le\pi^2N.
\end{split}
\]
Equation (4) therefore gives
\[
\int_{\mathbb T}q(z)\rho_3(0,d,z)\,dz
\le\frac{N^6d^2}{24\pi}.
\tag{5}
\]
Interchanging the two pair endpoints gives the same bound with \(q(z-d)\). This can be seen either by translation/reflection invariance or by repeating the projection proof with base point \(d\).

Let \(Z_\varepsilon\) sum the endpoint background over all ordered distinct pairs \((a,b)\) whose positive oriented separation \(d=(b-a)\pmod{2\pi}\) lies in \((0,\varepsilon]\). The factorial-moment identity and rotation invariance give
\[
\begin{split}
\mathbb E Z_\varepsilon
&=2\pi\int_0^\varepsilon\int_{\mathbb T}
[q(z)+q(z-d)]\rho_3(0,d,z)\,dz\,dd\\
&\le2\pi\int_0^\varepsilon\frac{N^6d^2}{12\pi}\,dd
=\frac{N^6\varepsilon^3}{18}.
\end{split}
\tag{6}
\]
The integrands are nonnegative, so Tonelli is legitimate before the estimates prove finiteness. There is no factor \(1/2\): the correlation density counts ordered triples, and the short orientation of a consecutive gap is included once. The pair straddling the chosen \(2\pi\) cut is included by exactly the same periodic change of variables. Even at \(\varepsilon=\pi\), possible antipodal ambiguity is a null event.

To pass to midpoint backgrounds, rotate a consecutive pair of gap \(d\le\pi\) to endpoints \(\pm d/2\). Every other point has a midpoint-centered lift \(y\in[-\pi,\pi]\) with \(|y|\ge d/2\), because the open short arc contains no point. Its distance to the endpoint on the same side is \(|y|-d/2\le|y|\). Since \(q\) decreases with circular distance on \((0,\pi]\),
\[
q(y)\le q(y-\operatorname{sgn}(y)d/2)
\le q(y-d/2)+q(y+d/2).
\]
Thus \(B_i\le S_i\) for every included consecutive pair. Its endpoint-background sum is a subsum of \(Z_\varepsilon\), proving (2).

**Why this order matters.** One cannot simply drop consecutiveness from the midpoint-weighted sum: a third point can then approach the midpoint while staying away from both endpoints, where \(\rho_3\) need not vanish. The inverse-square midpoint weight would have a nonintegrable singularity. The endpoint majorant avoids this invalid enlargement.

## 4. The selected background is tight at scale \(N^2\)

The checked primary extreme-gap input is Feng–Wei, Theorem 1.1 and Corollary 1.1, printed page 4, specialized **only to CUE**. Their periodic definition includes the wrap gap, and \(A_2=1/(24\pi)\). Hence
\[
\mathbb P(N^{4/3}\delta_N^{\min}>L)
\longrightarrow\exp\left(-\frac{L^3}{72\pi}\right)
\quad(L>0).
\tag{7}
\]
See [Feng–Wei, arXiv:1806.01555v2](https://arxiv.org/abs/1806.01555v2). No finite-N uniform tail estimate is asserted.

On the event \(\delta_N^{\min}\le L N^{-4/3}\), the selected \(B_N\) is one nonnegative summand in (3). Therefore, for every fixed \(L,K>0\),
\[
\limsup_{N\to\infty}\mathbb P(B_N/N^2>K)
\le e^{-L^3/(72\pi)}+\frac{L^3}{18K}.
\tag{8}
\]
Choosing \(L\) first and then \(K\) proves
\[
\boxed{B_N/N^2=O_{\mathbb P}(1).}
\tag{9}
\]
For example, choosing the fixed value \(L^3=72\pi\log K\), for each \(K>1\), gives the asymptotic tail bound \((1+4\pi\log K)/K\) on the right side of (8). This is a limit-superior bound, not a quantitative convergence rate in \(N\), and it is not a uniform first-moment estimate for \(B_N/N^2\). The entire argument avoids conditioning on which pair is smallest.

## 5. Quantitative consequence for the already-defined finite heat flow

Let
\[
P_N(z)=\det(zI-U_N)=\sum_{j=0}^N a_jz^j,\qquad
P_{N,s}(z)=\sum_{j=0}^Na_j e^{sj(N-j)}z^j,
\]
and define the first discriminant time
\[
D_N=\inf\{s>0:\operatorname{disc}(P_{N,s})=0\}.
\]
This is the finite circular scalar-heat deformation, not stochastic Dyson Brownian motion and not a representation of the true zeta flow.

The exact deterministic statement already audited in Round 2 uses the same midpoint background \(B_N\). For
\[
\eta_N=(\delta_N^{\min})^2(B_N+1),\quad
K_0=16384,\quad\eta_0=1/524288,
\]
it proves
\[
\frac{(\delta_N^{\min})^2}{8}\le D_N
\le(\delta_N^{\min})^2\left(\frac18+K_0\eta_N\right)
\qquad\hbox{if }\eta_N\le\eta_0.
\tag{10}
\]
The source is `research-round2/galilean-proof-audit.md`, Sections 1–5, pinned in the source receipt. Its constants are independent of \(N\) and of the common background drift. Its proof controls the real Gaussian tails after an exact Galilean conjugation and keeps both moving interval boundaries nonzero throughout the comparison time. It therefore does not require a new unproved dynamic-background stability assumption. A multiple zero somewhere else earlier only helps its upper bound.

Put \(X_N=N^{4/3}\delta_N^{\min}\) and \(Y_N=B_N/N^2\). Equations (7) and (9) imply both are tight, without requiring independence. Thus
\[
N^{2/3}\eta_N=X_N^2(Y_N+N^{-2})=O_{\mathbb P}(1),
\quad\mathbb P(\eta_N\le\eta_0)\to1.
\]
Applying (10) on this event proves the strengthened estimate
\[
\boxed{\quad
\frac{8D_N}{(\delta_N^{\min})^2}-1
=O_{\mathbb P}(N^{-2/3}).
\quad}
\tag{11}
\]
The difference is nonnegative even outside the small-\(\eta_N\) event: the unconditional scalar comparison gives \(D_N\ge-\log\cos(\delta_N^{\min}/2)\ge(\delta_N^{\min})^2/8\). Here \(\delta_N^{\min}<\pi\) almost surely for \(N\ge2\), deterministically for \(N\ge3\). This is a tightness-scale rate for the approximation error, not a distributional convergence rate or a claim about its limiting correction law. Equivalently,
\(D_N-(\delta_N^{\min})^2/8=O_{\mathbb P}(N^{-10/3})\).
For completeness, \(D_N\) is finite almost surely: a generic CUE characteristic polynomial has a nonzero interior coefficient, whose prescribed exponential growth eventually exceeds the bounded coefficient size possible for a polynomial with all roots on the circle. Before a first collision, self-inversive symmetry keeps its simple roots on the circle. The exceptional exactly rotation-invariant polynomial has probability zero.

The qualitative limiting depth law already recorded in Round 1 follows again. We do not label it a new result of this round, and we do not infer an error rate for that limiting law from (11).

## 6. What this does and does not settle

The new finite-N estimate controls the initial inverse-square background attached to the actual selected minimum. Together with an existing fully quantified deterministic lemma it removes a possible missing-stability premise in this finite CUE lane and sharpens its probabilistic approximation rate.

A theorem identifying a limiting conditional background distribution, an asymptotic mean of that background, an optimal error exponent or coefficient, general-beta analogues, and any arithmetic transfer are outside the proved result. For true zeta zeros, the isolated-small-pair and positive-density arithmetic obligations documented in Round 2 remain open. CUE's three-point determinant is an actual random-matrix input, not an available identity for zeta zeros.

The companion check records exact normalization/exponent arithmetic and the \(N=3\) determinant-integral identity. It is not a grid scan, a Monte Carlo test, or a formal verification of this proof. Independent/coordinator review must be recorded separately without changing the eventual frozen author snapshot.
