# Bounded local probes: a rigorous transfer lemma and the arithmetic price

6 November 2026. Internal research note; not a zeta theorem or an external-priority claim.

## 1. Question and outcome

The PR5 audit identifies an actual logical requirement: the unnormalized signed triple statistic grows like the cube of window occupancy. An asymptotic half-grid approximation requires uniform integrability to transfer to its mean. For arbitrary point processes that is additional information. **For actual zeta zeros under RH, at fixed window width, it is available:** the companion arithmetic audit derives every fixed count moment from restricted Rudnick-Sarnak correlations and a positive bandlimited majorant. Thus fixed-window uniform integrability is not a remaining arithmetic unknown in that conditional setting.

There is a clean remedy at the level of probability: normalize by the number of ordered distinct triples. This gives a bounded local statistic, with explicit stability under approximate lattice locations, sparse bad points, and exceptional windows. It has a rigorously nonzero sine-process expectation on sufficiently short windows. For general windows, a hard occupancy cutoff preserves any proved nonzero unnormalized expectation once a determinantal tail bound is small enough.

There is an equally precise limitation. No nonconstant finite-degree correlation polynomial with continuous kernels can be uniformly bounded over arbitrary finite simple configurations in a compact window. Normalization or clipping necessarily leaves the finite three-trace algebra, unless one restricts the configuration class. Pointwise boundedness is stronger than the moment bounds available for a specified process. Consequently the theorem does not obstruct the under-RH zeta uniform-integrability argument, and the original signed three-trace statistic remains the simpler arithmetic target.

## 2. The original phase difference and a bounded normalization

Put

\[
a=(6/5,1/5,-7/5),\qquad b=(-4/5,1/5,3/5),
\]

and

\[
h(x_1,x_2,x_3)=\cos(2\pi a\cdot x)-\cos(2\pi b\cdot x).
\]

These are exactly PR5's two frequency triples. For a finite simple configuration X in a window I, let K=|X| and

\[
V(X)=\sum_{i,j,k\ \mathrm{distinct}}h(x_i,x_j,x_k),\qquad
U(X)=\begin{cases}V(X)/(K)_3,&K\ge3,\\0,&K<3.\end{cases}
\]

Here (K)_r=K(K-1)...(K-r+1). Then |U|<=2 uniformly in K. The same conclusions below hold with any attached triple weights in [0,1], including Hann product weights, while retaining the denominator (K)_3. Claims about strict sign in section 5 use unweighted triples, or positive symmetric weights.

The two complex phases have ratio exp(4 pi i(x_i-x_k)). Consequently h=0 termwise on every translated half-grid, regardless of thinning and weights.

## 3. Quantitative approximate-AH transfer, without occupancy tails

Suppose at least (1-epsilon)K points in a window are within eta of one common translate of (1/2)Z. For every entirely good triple,

\[
|h|\le |e^{4\pi i(x_i-x_k)}-1|\le8\pi\eta.
\]

At most 3 epsilon of uniformly sampled ordered distinct triples contain a bad point, by the union bound on their three uniform marginals. As |h|<=2,

\[
\boxed{|U(X)|\le8\pi\eta+6\epsilon.}
\]

No factor involving K remains. If a fraction q of windows is entirely exceptional, the absolute mean is at most

\[
\boxed{8\pi\eta+6\epsilon+2q.}
\]

These bounds may be replaced by their minimum with 2. They concern a local common lattice translate; an unrelated nearest-half-integer phase for each point would not suffice.

### Sparse deletion measured globally

There is also a useful spatial-average form, avoiding local bad-point fractions. Let B be a stationary set of bad points of intensity rho_B, and use sliding windows of fixed length L. Suppose every window with no B point is eta-close to a translated half-grid. Campbell's formula and Markov's inequality give

\[
\Pr\{B\cap I\ne\varnothing\}\le L\rho_B,
\qquad
\boxed{|\mathbb E U|\le8\pi\eta+2L\rho_B.}
\]

An additional exceptional-window fraction q costs 2q. The same statement holds deterministically for long spatial averages, up to the endpoint contribution, by integrating the number of deleted points in a sliding interval. For a unit-intensity process, deletion of a point-intensity fraction epsilon means rho_B=epsilon. This is stronger than assuming a small fraction of bad points separately in every window.

For comparison of the statistic before and after deleting b points of a particular configuration,

\[
|U(X)-U(X\setminus B)|\le\min(4,12b/K)
\]

when K>0; the conventions for occupancies below 3 make the bound valid there too. In particular this difference is at most 4b, giving a spatial-average change at most 4L rho_B without any lattice hypothesis.

## 4. Normalization does not automatically preserve the signed mean

A negative E V does not imply a negative E[V/(K)_3]: the denominator is correlated with the signed numerator. The PR5 finite-window means therefore cannot simply be relabelled as means of U. They must be recomputed or proved separately.

This is not a technicality. A two-outcome random variable can have a large negative V on high-occupancy outcomes and a small positive V on low-occupancy outcomes; dividing by a cubic occupancy can reverse its mean.

## 5. A rigorous nonzero sine-process expectation for the same normalized triple kernel

Let all three coordinates lie in an interval of length L<=1/4. Define the symmetrized kernel

\[
\bar h(x)=\frac16\sum_{\sigma\in S_3}h(x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)}),
\qquad v=\sum_{j=1}^3(x_j-\bar x)^2.
\]

Since both frequency vectors sum to zero, centering x does not change the phases. Permutation averaging gives

\[
\frac16\sum_\sigma(a\cdot x_\sigma)^2=\frac{43}{25}v,
\qquad
\frac16\sum_\sigma(b\cdot x_\sigma)^2=\frac{13}{25}v.
\]

Also |a dot x|<=7L/5 and |b dot x|<=4L/5. The elementary Taylor bound

\[
|\cos z-1+z^2/2|\le |z|^4/24
\]

therefore gives

\[
\bar h(x)\le-
\left(\frac{12\pi^2}{5}-\frac{926\pi^4}{375}L^2\right)v.
\]

For L<=1/4 the bracket is greater than pi^2/2 (use pi^2<10). Thus

\[
\boxed{\bar h(x)\le-\frac{\pi^2}{2}v<0}
\]

for every nonconstant triple. Consequently U(X)<0 whenever K>=3, and U(X)=0 otherwise, for a simple configuration in such a window.

For the unit-intensity sine process, rho_3(x)=det[sinc(pi(x_i-x_j))] is strictly positive at every distinct triple: it is the Gram determinant of three linearly independent exponentials in L^2[-1/2,1/2]. Its integral on I^3 is positive, so P(K>=3)>0. Hence

\[
\boxed{\mathbb E_{\rm sine} U<0\quad(0<L\le1/4).}
\]

This is a proof, not a Monte Carlo sign inference. It combines with section 3 to give an explicit logical separator between a sine process and an approximate half-grid process with vanishing contamination.

The same strict-sign conclusion holds for unfolded Haar CUE of every rank N>=3: the three-point density is the Gram determinant of three distinct Fourier evaluation vectors, hence is strictly positive on distinct triples in this short interval. This is a fixed-window finite-CUE statement, not a claimed zeta transfer.

### An explicit positive integral lower bound

Write c=pi^2/2 and

\[
J_L=\int_{I^3}\!\left[\sum_j(x_j-\bar x)^2\right]\rho_3(x)\,dx>0.
\]

The triple variance is at most 2L^2/3. Hadamard's inequality gives rho_r<=1 for this unit-intensity determinantal process. By Cauchy-Schwarz and

\[
(K)_3^2=(K)_6+9(K)_5+18(K)_4+6(K)_3,
\]

one obtains the completely explicit, albeit small, lower bound

\[
-\mathbb E U\ge
\frac{3c J_L^2}{2L^2(L^6+9L^5+18L^4+6L^3)}>0.
\]

The remaining integral is over a compact cube with a specified elementary nonnegative integrand; positivity does not depend on a numerical quadrature.

### Why this is not an arithmetic breakthrough

On such a short interval the probe is effectively detecting the presence of three close points. A translated half-grid has at most one point in an interval of length 1/4. Proving positive limiting frequency of three actual zeta zeros in such windows is itself a strong, currently unproved input in this programme. Boundedness removes an approximation-transfer obstacle, not the arithmetic difficulty. This local theorem should not be described as a new zeta distribution result.

## 6. A large-window cutoff preserving any proved nonzero mean

Let V have triple weights bounded by 1 and suppose a sine or unfolded CUE calculation rigorously gives E V=-m<0 in an interval of length L. Define

\[
H_M(X)=\frac{V(X)\,1_{K\le M}}{2(M)_3},\qquad M\ge3.
\]

Then |H_M|<=1, and H_M vanishes on half-grids. If K>M and 1<=r<=M-2,

\[
(K)_3\le\frac{(K)_{3+r}}{(M-2)_r}.
\]

For a unit-intensity determinantal process, E(K)_j<=L^j, so

\[
|\mathbb E[V1_{K>M}]|\le
\boxed{\frac{2L^{3+r}}{(M-2)_r}}=:R_{L,M,r}.
\]

Therefore if R<m,

\[
\mathbb E H_M\le-\frac{m-R}{2(M)_3}<0.
\]

For illustration only, L=40, M=100, r=40 gives an extremely small explicit tail bound, computable using integer powers and products. Applying this to PR5 requires a rigorous lower bound m for that precise finite-window mean; the checked-in floating expectation is not by itself an interval certificate. No such certificate is claimed here.

On a regular window H_M obeys |H_M|<=4 pi eta+3 epsilon, and exceptional windows cost at most q. The hard cutoff can be discontinuous under deletion across K=M; the pointwise lattice-transfer bound remains valid because it never compares two different occupancies.

### A smooth alternative

For R>0, let H_R=V/[2(K+R)^3]. Then |H_R|<=1 and

\[
|\mathbb E V-2R^3\mathbb E H_R|
\le\frac6R(L^4+3L^3).
\]

Indeed 1-(1+u)^(-3)<=3u and K(K)_3=(K)_4+3(K)_3. Thus sufficiently large R preserves every nonzero E V, with an explicit condition. Its generic bound is usually much weaker than the hard-cutoff tail bound. It also requires higher information in its arithmetic expectation.

## 7. The exact arithmetic price: a finite-order boundedness theorem

**Theorem.** Let I be a compact interval with nonempty interior. Suppose

\[
F(X)=c+\sum_{r=1}^d\sum_{i_1,\ldots,i_r\ \mathrm{distinct}}
f_r(x_{i_1},\ldots,x_{i_r}),
\]

where every f_r is continuous and symmetric on I^r. If |F(X)| is bounded by one constant for every finite simple configuration X in I, then all f_r vanish and F is constant.

**Proof.** Sample n iid points from an arbitrary nonatomic probability measure mu on I. They are distinct almost surely. The expectation is

\[
c+\sum_{r=1}^d(n)_r\int f_r\,d\mu^r.
\]

It is a polynomial in n bounded for all positive integers n. Each coefficient in the falling-factorial basis is zero, so the integral of each f_r against mu^r is zero. Approximate arbitrary probability measures by nonatomic ones; continuity preserves this identity. Polarize the resulting homogeneous polynomial in finite mixtures of Dirac measures to conclude f_r=0 at every tuple. QED.

The theorem covers fixed finite sums of ordinary weighted trace products after repeated-index terms are expanded. It does not cover ratios, adaptive sampling, clipping, discontinuous order statistics, or a class of processes with a deterministic occupancy bound.

Thus an arbitrary-occupancy bounded nontrivial local probe cannot remain a fixed finite-order correlation polynomial. This is why simply asking for both boundedness and the old three-trace explicit-formula calculation is incompatible on that class.

## 8. Exact representations exist, but they require more information

For K>=3,

\[
\frac1{(K)_3}=\frac12\int_0^1 t^{K-3}(1-t)^2\,dt.
\]

Hence U has an exact generating-functional representation. For a determinantal process with reduced Palm kernel K^x_I,

\[
\mathbb E U=\frac12\int_0^1(1-t)^2
\int_{I^3}h(x)\rho_3(x)
\det(1-(1-t)K^x_I)\,dx\,dt.
\]

The reduced Palm Fredholm determinant records all further points in the window. Similarly, 1/(K+R)^3=(1/2) integral_0^infinity u^2 exp[-u(K+R)] du yields a Laplace-functional representation for the soft normalization.

For actual zeta zeros, inserting an explicit formula into each linear trace does not remove these random denominators or occupancy indicators. Estimating the normalized expectation directly would require joint count/phase information. At fixed window width under RH, however, one can keep the unnormalized finite-order statistic: the required occupancy moment bound is already obtainable, so the unresolved input is the signed mean beyond the protected correlation range.

Here is the count-control mechanism. Choose a nonnegative Schwartz majorant of the fixed interval with sufficiently small compact Fourier support. For each fixed k, choose that support so that the k-fold product and every repeated-index partition remain in the restricted k-level correlation region. Applying the correlation theorem yields a bounded kth moment of the local zero count. In particular a fixed moment above degree three gives uniform integrability of a cubic statistic by Holder's inequality. The permitted cutoff in the macroscopic height average is supported by the interval-cutoff extension on p.1030 of [Rudnick-Sarnak, *The n-level correlations of zeros of the zeta function* (1994)](https://www.math.tau.ac.il/~rudnick/papers/RudnickSarnakCRAS1994.pdf). This is a consequence of existing restricted correlations, not a new unprotected correlation theorem.

## 9. A simpler bounded positive alternative

For K>=1 put

\[
Q(X)=1-\left|K^{-1}\sum_{x\in X}e^{4\pi i x}\right|^2,
\]

and Q(empty)=0. Then 0<=Q<=1. It vanishes exactly when all point phases e^(4 pi i x) agree, equivalently when the configuration lies in a translated half-grid. With eta-close good points and bad fraction epsilon,

\[
Q\le32\pi^2\eta^2+4\epsilon.
\]

For any interval of positive length, the sine-process expectation is strictly positive: its second correlation density is positive off the diagonal, and almost surely distinct points do not differ by a half-integer. This illustrates that finding a bounded statistical separator is easy; proving its positive limiting zeta expectation remains the substantive issue. Its denominator again leaves the finite pair-trace algebra.

## 10. Recommended next step

1. Keep the original unnormalized PR5 statistic for a direct three-trace arithmetic target.
2. Add U as an empirical robustness diagnostic, reporting its own means rather than reusing the original means.
3. If one wants a rigorous finite-model sign at widths 10,20,40, interval-certify E V, choose an explicit occupancy cutoff M using section 6, and then compute the bounded diagnostic.
4. State the missing zeta input exactly: **under RH and at fixed window width, it is the signed three-trace mean beyond the protected range.** Count moments provide the necessary uniform integrability. A nonzero bounded-probe mean is an alternative target, but its normalization adds joint-law complexity and is unnecessary solely to obtain uniform integrability in this setting.

## Sources and verification scope

- Local source: `../../november-checkpoint/CONCURRENT_PR5.md`, audited against PR5 commit `3b7687eb4a6be68c9093d997c473ebcf1331947e`.
- Local original statistic and finite CUE controls: `PR #5 statistic.py at the pinned commit` and `controls.py`.
- The elementary inequalities and identities above are proved in this note. The accompanying deterministic check script tests the phase cancellation, stability constants, symmetrized-kernel inequality, deletion bound, and factorial identities. Numerical testing is supplementary to the stated proofs.
- No zeta data were reprocessed, no arithmetic asymptotic established, and no external novelty or formal verification claim made.
