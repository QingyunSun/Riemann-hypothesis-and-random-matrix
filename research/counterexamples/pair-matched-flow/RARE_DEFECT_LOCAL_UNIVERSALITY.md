# A sparse modification preserves full local sine universality and destroys the CUE minimum-gap law

Date: 2026-11-01 America/Los_Angeles (2026-11-02 UTC). Status: elementary proposition with a complete proof. This is a model obstruction, not a theorem about zeta zeros and not a claimed novel method. No numerical experiment is needed.

## 1. Construction and normalization

Let T_N = R/(N Z), with Lebesgue measure of total mass N. Take the N eigenangles of a Haar unitary matrix and unfold them by x=N theta/(2 pi). Write the resulting simple point configuration as X_N, of intensity one on T_N.

Conditional on X_N, choose an ordered pair of distinct atoms (a,b) uniformly from its N(N-1) ordered pairs. For a deterministic number 0<epsilon_N<N, define

\[
Y_N=(X_N\setminus\{b\})\cup\{a+\epsilon_N\pmod N\}.
\]

Here a remains in the configuration. Collisions of the inserted point with another original atom occur with probability zero, because the CUE eigenangle law has a density. Thus Y_N has exactly N distinct points almost surely. Both X_N and Y_N are invariant under rotations of T_N and have intensity one.

The construction does not preserve a hard core of 1/2 and is not an AH counterexample. Its purpose is to separate local universality from global extreme statistics.

## 2. The local total-variation estimate

**Proposition 1.** For every deterministic Borel window W_N in T_N of Lebesgue measure L_N,

\[
d_{\rm TV}\bigl(\mathcal L(X_N|_{W_N}),\mathcal L(Y_N|_{W_N})\bigr)
\le \min\{1,2L_N/N\},
\]

where total variation is the supremum of probability differences over measurable events. The estimate is uniform over the choice and position of W_N.

**Proof.** The uniformly selected deleted atom b is uniform on T_N, because X_N is rotation invariant. The selected anchor a is also uniform; adding a deterministic displacement preserves its marginal uniform law. In the explicit coupling above, the restrictions can differ only if b or a+epsilon_N belongs to W_N. Therefore

\[
\Pr[X_N|_{W_N}\ne Y_N|_{W_N}]
\le \Pr[b\in W_N]+\Pr[a+\epsilon_N\in W_N]
=2L_N/N.
\]

The coupling inequality proves the assertion. No independence between the two altered positions is needed. QED.

In particular, for every measurable local functional F_N bounded in absolute value by M_N,

\[
|\mathbb E F_N(X_N|_{W_N})-\mathbb E F_N(Y_N|_{W_N})|
\le 4M_N L_N/N.
\]

For every deterministic sequence of windows with L_N=o(N), the two restricted laws are asymptotically indistinguishable in total variation. This is a comparison to the original CUE laws on those windows. It does not itself assert that CUE and the infinite sine process are close in total variation on arbitrary growing windows. Nor does it give simultaneous agreement over all windows, or apply to a random window chosen after locating the defect.

## 3. Full fixed-order local correlations also survive

Total variation alone need not preserve unbounded observables. Here the required moment control follows directly from the CUE determinantal kernel, so the construction preserves every fixed-order local correlation limit, not only bounded local statistics.

Relative to Lebesgue measure on T_N, the CUE correlation kernel can be written

\[
K_N(x,y)=\frac1N\sum_{r=0}^{N-1}e^{2\pi i r(x-y)/N}.
\]

Its diagonal is one. Every correlation determinant is nonnegative and at most one by the Gram/Hadamard bound. Consequently, for C_N=X_N(W) and a window W of fixed length L,

\[
\mathbb E(C_N)_q=\int_{W^q}\rho_{N,q}(\mathbf x)\,d\mathbf x\le L^q.
\]

Here (C)_q=C(C-1)...(C-q+1). Using the expansion of ordinary powers into falling factorials gives

\[
\mathbb E C_N^m\le T_m(L):=\sum_{q=0}^m {m\brace q}L^q
\]

for every fixed nonnegative integer m, uniformly in N; {m brace q} denotes a Stirling number of the second kind.

**Proposition 2.** Fix k, L, and a bounded measurable test f supported on W^k. Let F_f(Z) be the sum of f over ordered k-tuples of distinct atoms of Z in W. Then

\[
|\mathbb EF_f(Y_N)-\mathbb EF_f(X_N)|
\le \|f\|_\infty\sqrt{B_{k,L}}\sqrt{2L/N},
\]

where a finite constant independent of N is

\[
B_{k,L}=4\sum_{m=0}^{2k}\binom{2k}{m}T_m(L).
\]

**Proof.** Let E be the event that the restrictions differ. Outside E the sums agree. The modified local count is at most C_N+1, so

\[
|F_f(Y_N)-F_f(X_N)|
\le \|f\|_\infty[(C_N+1)^k+C_N^k]\mathbf1_E.
\]

Cauchy–Schwarz, Proposition 1, and the moment bound above apply; the square bracket squared is at most 4(C_N+1)^{2k}. Expanding that power yields B_{k,L}. QED.

After an irrelevant gauge factor, K_N converges on compact sets to

\[
K_{\sin}(x,y)=\frac{\sin\pi(x-y)}{\pi(x-y)}.
\]

Dominated convergence of its determinants establishes the CUE fixed-order correlation limits; Proposition 2 transfers every one of them to Y_N. The usual CUE local point-process convergence, together with Proposition 1 on each fixed compact window, also transfers the full local sine-process limit. Thus the obstruction survives all orders of fixed local correlation convergence. It does not preserve exact finite-N correlation measures.

## 4. The global minimum is nevertheless arbitrarily small

Let g_min(Z) be the shortest circular nearest-neighbor gap in a configuration on T_N.

**Proposition 3.** Almost surely,

\[
g_{\min}(Y_N)\le\epsilon_N.
\]

**Proof.** The anchor a and the inserted point a+epsilon_N both remain. The circular arc of length epsilon_N joining them is partitioned into one or more nearest-neighbor gaps. At least one of those gaps is at most epsilon_N. QED.

Set epsilon_N=N^{-A} for any fixed A>1/3. Then

\[
0\le N^{1/3}g_{\min}(Y_N)\le N^{1/3-A}\longrightarrow0.
\]

By contrast, the CUE minimum on the unfolded circle has the nondegenerate N^{-1/3} scale, equivalent to the angular N^{-4/3} scale. The limiting law and the joint smallest-gap process are proved by Ben Arous and Bourgade. [*Extreme gaps between eigenvalues of random matrices*, Theorem 1.1 and Corollary 1.2](https://math.nyu.edu/~bourgade/papers/ExtremeGaps.pdf).

For a direct finite-N separation that does not require this limiting theorem, the CUE two-point function at separation s satisfies

\[
\begin{aligned}
\rho_{N,2}(0,s)
&=1-|K_N(0,s)|^2\\
&=\frac1{N^2}\sum_{r,t=0}^{N-1}\left(1-\cos\frac{2\pi(r-t)s}{N}\right)\\
&\le\frac{\pi^2}{3}(1-N^{-2})s^2.
\end{aligned}
\]

The last line uses 1-cos u≤u²/2 and the exact sum

\[
\sum_{r,t=0}^{N-1}(r-t)^2=\frac{N^2(N^2-1)}6.
\]

Count ordered pairs whose positive circular separation lies in (0,epsilon_N]. A minimum gap at most epsilon_N entails at least one such pair. Rotation invariance and Markov's inequality therefore give

\[
\boxed{\Pr[g_{\min}(X_N)\le\epsilon_N]
\le N\int_0^{\epsilon_N}\rho_{N,2}(0,s)\,ds
\le\frac{\pi^2}{9}N\epsilon_N^3.}
\]

For A>1/3 this tends to zero, while the same event has probability one for Y_N. Consequently the full-configuration laws have total-variation distance tending to one, despite their indistinguishability on every deterministic o(N)-length window. With deterministic epsilon_N they are in fact mutually singular at each N: Y_N has a pair at exactly that prescribed separation, an event of CUE probability zero.

The singular prescribed-spacing feature is optional. Choose an independent displacement D_N with a density supported in [epsilon_N/2,epsilon_N] and insert a+D_N instead. The proofs of Propositions 1–3 and the global minimum-gap separation are unchanged. In this version the joint eigenangle law is absolutely continuous: condition on the chosen labels, retain N-1 original coordinates whose joint law has a density, and use the independent displacement density for the new coordinate. This still supplies no Wigner matrix or arithmetic structure.

## 5. Consequences for the research programme

The following implication is false for general rotation-invariant N-point model sequences:

\[
\text{full local sine limit, even all fixed-order local correlations}
\quad\Longrightarrow\quad
\text{CUE global minimum-gap law}.
\]

The extra input must rule out defects that occur only once or a bounded number of times in the full N-point configuration. Candidates include uniform shrinking-scale correlation estimates and suitable factorial-moment control for the global close-pair process. Ordinary local weak convergence does not provide them.

For zeta zeros, all-order correlation convergence can determine ordinary joint local spacing limits under appropriate moment control; this must not be confused with global extreme-gap asymptotics. [Arias de Reyna–Rodgers, *On convergence of points to limiting processes, with an application to zeta zeros*, Theorem 2](https://arxiv.org/html/2311.13441v2).

This proof does not refute any statement about actual zeta zeros, does not settle Montgomery's pair-correlation conjecture, and does not yield a Newman-depth law. Transporting a forced tiny gap to a quantitative heat collision depth would require a separate exact estimate controlling the other particles and the time normalization. That step is deliberately left open.

Verification: each probabilistic claim above follows from the explicit coupling or the displayed determinantal calculation. No simulation, external model inference, or numerical certificate was used. Independent proof review remains appropriate before publication; the sparse modification principle itself is not presented as new.
