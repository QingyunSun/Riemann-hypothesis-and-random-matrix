# Independent pair-data review: heat separation, stationary extensions, and a sine-kernel rigidity boundary

Date: 2026-11-01, America/Los_Angeles; checked on 2026-11-02 UTC. Author: stationary-challenge agent. Status: ordinary proofs and exact finite checks submitted to the root investigator. All model statements below are separate from conjectures about actual zeta zeros. No external novelty or formal-proof certification is claimed.

## 1. What was already in the archive

The earlier `historical/riemann-rmt/final_verified_paper.md`, Section 5.1, already records projection DPPs on \(\mathbb Z/12\) with frequency sets \(\{0,1,4,6\}\) and \(\{0,1,3,7\}\). They have identical full pair correlation, but the triple event \(\{0,1,2\}\) has probabilities \((8\mp\sqrt3)/432\). It also records periodic lifting. Section 5.3 separately explains why the determinantal hypothesis supplies information beyond matching correlations. These facts are prior programme results, not new discoveries in this lane.

The genuinely different check in this note concerns the root investigator's deterministic heat pair and its exact depth. A continuous, mixing stationary DPP construction is supplied as a separate explicit illustration, together with a rigidity theorem showing why that spectral construction cannot preserve the exact full sine-kernel pair law. The continuous construction and its rigidity proof were not found in the inspected archive; this is not a global novelty claim. Homometry itself is classical; see [Grimm–Baake](https://arxiv.org/abs/0808.0094).

## 2. Independent verification of the root's finite heat pair

Let

\[
S=\{0,1,3,4\},\qquad C=\{2,5,6,7\}\subset\mathbb Z/8,
\]

and place each set at angles \(2\pi j/8\). Write \(p_k(A)=\sum_{j\in A}e^{2\pi i kj/8}\).

For any half-size subset A of a finite group of size \(2N\), its complement satisfies

\[
\#(A^c\cap(A^c+h))=2N-2|A|+\#(A\cap(A+h))
=\#(A\cap(A+h)).
\tag{1}
\]

Consequently S and C have the same complete ordered pair-difference counts, including the diagonal, and \(|p_k(S)|^2=|p_k(C)|^2\) for every integer k. Their minimum circular gaps are also both \(\pi/4\). This is full pair matching between the two configurations; it does not assert that either configuration has the ACUE ensemble's expected form factor.

Directly,

\[
p_1(S)=i\sqrt2,\quad p_1(C)=-i\sqrt2,
\qquad p_2(S)=2,\quad p_2(C)=-2.
\]

Thus the rotation-invariant cubic statistic satisfies

\[
\Re(p_1^2\overline{p_2})(S)=-4,\qquad
\Re(p_1^2\overline{p_2})(C)=4.
\tag{2}
\]

### 2.1 The exact heat generator

For a trigonometric polynomial with simple real circular zeros, under
\(H_t=e^{-t\partial_x^2}H_0\), the zero velocity is

\[
\dot x_i=\frac{H_t''(x_i)}{H_t'(x_i)}
=\sum_{j\ne i}\cot\frac{x_i-x_j}{2}.
\]

Pairing the terms for i and j in the derivative of the Fourier power sum gives

\[
\dot p_2=-2(N-2)p_2-2p_1^2.
\]

At \(N=4\),

\[
\frac d{dt}|p_2|^2=-8|p_2|^2-4\Re(p_1^2\overline{p_2}).
\tag{3}
\]

Equations (2), (3) give exactly \(-16\) at S and \(-48\) at C. In particular, equal full initial pair data do not determine the initial time derivative of this pair observable under the specified deterministic heat-zero flow. No stochastic Dyson Brownian motion has been substituted for that flow.

### 2.2 Exact backward depths, with endpoint checks

After rotating both angle sets by \(-\pi/2\), their trigonometric polynomials, up to nonzero scalar multiples, are

\[
F(x)=2\cos2x-2\sqrt2\cos x+2,
\qquad
G(x)=2\sin2x+2\sqrt2\sin x.
\]

Their flows are obtained by multiplying frequency j by \(e^{j^2t}\). For F put \(c=\cos x\), \(y=e^{2t}>0\). The equation becomes

\[
4e^{4t}c^2-2\sqrt2e^t c+2-2e^{4t}=0,
\]

whose discriminant is

\[
8y(4y^3-4y+1).
\tag{4}
\]

Let \(y_*\) be the largest real root of \(4y^3-4y+1=0\). It lies in \((837/1000,838/1000)\), in particular above \(1/2\). For \(y\ge y_*\), the quadratic vertex

\[
c_0=\frac1{2\sqrt2}y^{-3/2}
\]

lies in \((0,1)\). Both endpoint values at \(c=\pm1\) are positive. To check the potentially smaller one for every t, put \(u=e^t\):

\[
u^4-\sqrt2u+1\ge1/4,
\]

since its unique positive minimum is at \(u=1/\sqrt2\). Thus whenever (4) is nonnegative and \(y\ge y_*\), both quadratic roots lie in \([-1,1]\), giving four real circular zeros with multiplicities.

For \(1/2<y<y_*\), the cubic in (4) is negative. For \(0<y\le1/2\), the vertex is at or beyond 1 and the positive value at 1 shows there is no zero in \([-1,1]\). This establishes the full threshold, not just a candidate first collision:

\[
\Lambda_F=\tfrac12\log y_*,\qquad D_F=-\Lambda_F=-\tfrac12\log y_*.
\tag{5}
\]

At the threshold there are two symmetric double zeros with interior cosine value \(c_0\).

For G the exact factorization is

\[
G_t(x)=2\sin x\left(2e^{4t}\cos x+\sqrt2e^t\right).
\]

Besides 0 and \(\pi\), the roots satisfy \(\cos x=-2^{-1/2}e^{-3t}\). Hence

\[
\Lambda_G=-\frac{\log2}{6},\qquad D_G=\frac{\log2}{6}.
\tag{6}
\]

At the threshold the cosine roots join the existing sine root at \(\pi\), producing a triple zero. The two depths differ: \(y_*>2^{-1/3}\), because the cubic at \(2^{-1/3}\) equals \(3-4\cdot2^{-1/3}<0\), and the cubic is increasing between this point and \(y_*\). Therefore \(D_F<D_G\).

### 2.3 Exact lift and stationary periodic extension

Taking preimages under \(z\mapsto z^r\) gives \(N=4r\) zeros and polynomials \(F(rx),G(rx)\). The flow identity

\[
e^{-t\partial_x^2}[F(rx)]=(e^{-r^2t\partial_x^2}F)(rx)
\]

shows the depths scale by \(r^{-2}\). The lifted power sums vanish unless \(r\mid k\); when \(k=rj\), they equal \(r p_j\). All pair data thus remain equal at every size in this sequence, while

\[
N^2D_{F,r}=16D_F\ne16D_G=N^2D_{G,r}.
\tag{7}
\]

Their minimum gaps scale equally by \(1/r\). Random rotation turns these configurations into rotation-invariant laws without changing any displayed rotation-invariant statistic.

There is also a stationary real-line extension: repeat S/2 or C/2 with period 4, then add a uniform random shift in \([0,4)\). Both processes have intensity 1, minimum gap \(1/2\), and identical full pair measures. Their cubic Fourier statistic on one period differs by (2). These are periodic processes; no mixing or sine-pair claim is made for this extension. It establishes a stationary version of the pair-data ambiguity, not a zeta-zero model.

### 2.4 Complete review of the six-particle ACUE-law perturbation

The root's completed `PAIR_MATCHED_HEAT_COUNTEREXAMPLES.md`, including its six-particle construction and probability-law perturbation, has also been independently reviewed. No substantive mathematical gap was identified in its stated finite-model conclusions. The following explicit calculations document the new portions of that review.

Let \(A_6=\{0,1,2,4,7,8\}\) and \(B_6=\{3,5,6,9,10,11\}\) in \(\mathbb Z/12\). They are complements, their dihedral orbits are disjoint and each has 24 elements, and both sorted circular gap lists are \((1,1,1,2,3,4)\). Exact twelfth-root sums give

\[
p_1(A_6)=\frac12+\frac{\sqrt3}{2}i,
\qquad p_2(A_6)=\frac12+\frac{3\sqrt3}{2}i.
\]

Consequently \(|p_2|^2=7\) and \(T(A_6)=\Re(p_1^2\overline{p_2})=2\). Both traces change sign under complementation, so \(T(B_6)=-2\). The general generator is

\[
L|p_2|^2=-4(N-2)|p_2|^2-4T,
\]

giving \(-120\) and \(-104\). Solving the triangular equations for \(p_1,p_2\) gives

\[
p_2(t)=e^{-2(N-2)t}\left[p_2(0)-p_1(0)^2(1-e^{-2t})\right].
\]

This establishes the exact forward difference

\[
|p_2(\Phi_t A_6)|^2-|p_2(\Phi_t B_6)|^2
=-8e^{-16t}(1-e^{-2t}).
\tag{7a}
\]

For the standard rank-six ACUE projection on 12 sites, the subset probability is the squared Vandermonde divided by \(12^6\). Direct radical evaluation gives the squared Vandermonde \(1728\) at either seed, hence probability \(1/1728\). Translation and reflection preserve this product, so each orbit has probability \(24/1728=1/72\).

Write \(O_A,O_B\) for these orbits and \(h=\mathbf1_{O_A}-\mathbf1_{O_B}\). For \(|\epsilon|\le1\), \(P_\epsilon=P_{\rm ACUE}(1+\epsilon h)\) is nonnegative and normalized. The joint summary \(Q\), comprising the complete ordered pair-difference measure and the sorted gap list, has one and the same value on the union of the two orbits. Reflection causes no problem: an ordered pair-difference measure always has equal counts at \(r\) and \(-r\). Therefore, for every function of this joint summary, the positive and negative changes cancel exactly. This proves equality of the **whole law** of Q, rather than just agreement of its expected coordinates.

The scalar heat and \(|p_2|^2\) are equivariant/invariant under the dihedral symmetries, so (7a) is constant as a difference across the paired orbits. The heat expectation shift is therefore

\[
\mathbb E_\epsilon|p_2(\Phi_t S)|^2
-\mathbb E_{\rm ACUE}|p_2(\Phi_t S)|^2
=-\frac{\epsilon}{9}e^{-16t}(1-e^{-2t}),
\tag{7b}
\]

with derivative \(-2\epsilon/9\) at zero. This independently confirms the root's normalization and sign, including its law-level claim. Periodic repetition with scale one half and period six gives the stated stationary line example with the same Palm nearest-gap histogram; under the Palm law the six phases are equally weighted, which is exactly the empirical gap histogram just calculated.

Two limitations in the root's note are necessary and correctly retained. First, the changed statistic \(T\) is already a protected balanced mixed moment of weight two; these laws do not match Tao's entire protected mixed-moment sector. Second, the periodic limits have lattice-supported pair measures and the explicit large-N depth constants describe chosen configurations in ACUE support, not typical ACUE samples. The review does not claim a stochastic Dyson-flow theorem, a genuine-zeta theorem, external novelty, or formal verification.

## 3. A continuous mixing stationary DPP pair with exact third-order separation

Use the integer sets

\[
A=\{0,1,4,10,12,17\},\qquad
B=\{0,1,8,11,13,17\}.
\]

Both have each positive difference in \(\{1,2,\ldots,13,16,17\}\) exactly once. They are not translates or reflected translates. Define \(\varepsilon=1/6\) and the disjoint spectral unions

\[
E_A=\bigcup_{a\in A}[a-\varepsilon/2,a+\varepsilon/2],
\qquad E_B=\bigcup_{b\in B}[b-\varepsilon/2,b+\varepsilon/2].
\]

Each has Lebesgue measure 1. The translation-invariant projection kernels are

\[
K_A(x)=\int_{E_A}e^{2\pi i\xi x}d\xi
=s(x)P_A(x),\qquad
s(x)=\frac{\sin(\pi x/6)}{\pi x},\quad
P_A(x)=\sum_{a\in A}e^{2\pi iax},
\tag{8}
\]

with the continuous value \(s(0)=1/6\), and similarly for B.

These kernels define unique simple DPPs. Indeed their operators are orthogonal projections in Fourier coordinates and are locally trace class: on a bounded spatial set, the restricted Fourier map to \(L^2(E_A)\) is Hilbert–Schmidt, and its squared operator has trace equal to that set's length. The existence and uniqueness criterion is [Soshnikov, Theorem 3, printed p.13 of arXiv v4](https://arxiv.org/pdf/math/0002099). Their translation-invariant laws are mixing, by that paper's Theorem 7, printed p.40. Only these stated DPP facts are imported.

The common ordered difference multiset gives \(|P_A(x)|^2=|P_B(x)|^2\) for every real x. Both intensities are 1, so

\[
\rho_{2,A}(0,x)=1-|K_A(x)|^2=1-|K_B(x)|^2=\rho_{2,B}(0,x)
\tag{9}
\]

at every x. This matches the complete factorial two-point density, hence all second moments of linear statistics and the associated structure factor.

For a Hermitian convolution DPP of intensity 1,

\[
\rho_3(0,u,v)=1-|K(u)|^2-|K(v-u)|^2-|K(v)|^2
+2\Re\bigl(K(u)K(v-u)K(-v)\bigr).
\]

At \(u=1/8,v=1/4\), exact eighth-root calculations give

\[
\Re(P_A(1/8)^2P_A(-1/4))=4-8\sqrt2,
\quad
\Re(P_B(1/8)^2P_B(-1/4))=4+8\sqrt2.
\]

Thus

\[
\boxed{\rho_{3,A}(0,1/8,1/4)-\rho_{3,B}(0,1/8,1/4)
=-32\sqrt2\,s(1/8)^2s(1/4)\ne0.}
\tag{10}
\]

Since these densities are continuous, the laws differ on three-point count observables supported in sufficiently small neighborhoods of those locations. A single-point density comparison is therefore not being mistaken for a positive-probability atom event.

This is a continuous mixing realization of full pair ambiguity. Its seed homometry and the DPP construction are classical in method; no new historical theorem is claimed.

## 4. Why these DPPs do not match Montgomery's sine pair, and a rigidity theorem

For the intensity-one projection DPP in (8), its structure factor is

\[
\mathcal S_A(\xi)=1-|E_A\cap(E_A+\xi)|.
\]

For \(|\xi|<1/6\), no distinct spectral intervals overlap, and therefore

\[
\mathcal S_A(\xi)=\mathcal S_B(\xi)=6|\xi|.
\tag{11}
\]

This already differs from the sine process's \(|\xi|\) ramp. Consequently the pair (8) is not even a match to the interior Montgomery form factor, and must not be presented as a counterexample to a zeta conjecture.

There is a stronger structural obstruction. Consider the explicitly defined class of Hermitian convolution-kernel DPPs on \(\mathbb R\) whose Fourier multiplier is a measurable function \(0\le w\le1\), with \(\int w=1\). If such a process satisfies

\[
\rho_2(0,x)=1-\left(\frac{\sin\pi x}{\pi x}\right)^2
\quad\text{for almost every }x,
\tag{12}
\]

then it is the sine process, up to a kernel gauge that does not alter its law.

Proof: (12) says \(|\widehat w(x)|^2=\operatorname{sinc}^2(x)\). Plancherel gives \(\int w^2=1=\int w\). Because \(0\le w\le1\), this forces \(w=\mathbf1_E\) almost everywhere for some measurable E of measure 1. Fourier inversion then gives the covariogram

\[
|E\cap(E+h)|=(1-|h|)_+\quad\text{a.e. }h.
\]

Two independent random variables uniformly distributed on E consequently differ by at most 1 almost surely. If the essential support of E had diameter greater than 1, two positive-measure subsets separated by more than 1 would contradict that assertion. Thus E is contained almost everywhere in an interval of length at most 1. Its measure is 1, so it equals an interval of length 1 up to null sets. Hence

\[
K(x)=e^{2\pi icx}\frac{\sin\pi x}{\pi x}
\]

for a real c. In every determinant, the row and column phase factors cancel. The DPP law is exactly the sine-process law.

This proof covers the stated convolution-kernel class; it does not assert that an arbitrary stationary point process, or the limiting zeta process, belongs to that class. In particular, establishing a full sine pair formula does not by itself establish the determinantal hypothesis needed here. A pair-matched countermodel for the exact sine pair must escape this class.

## 5. Precise connection to the famous conjectures

[Tao's original ACUE post](https://terrytao.wordpress.com/2019/05/08/the-alternative-hypothesis-for-unitary-matrices/) distinguishes the low-moment information reproduced by ACUE from the higher-frequency pair information that would exclude the alternative hypothesis; its Remarks 6 and 7 describe the determinantal ACUE construction and the full sine-kernel n-point prediction. Those distinctions remain essential here.

The finite heat pair refutes the inference that complete initial pair data determine deterministic heat depth, even on the same half-filled circular grid and after the natural large-size normalization. It does not refute the ACUE law, AH for actual zeros, or the Montgomery–Dyson conjectures. The stationary DPP pair refutes pair-to-law identification for general spectra but fails the known Montgomery ramp. The sine rigidity theorem explains exactly why the latter spectral approach cannot be strengthened to a full sine-pair countermodel inside its own class.

The missing arithmetic theorem for true zeros remains missing. The useful advance is an explicit diagnostic: a candidate dynamic discriminator must retain higher-order phase information even after all initial pair observables have been specified. Root's heat pair supplies this with exact depth and generator formulas.

## 6. Verification and provenance

The companion `AGENT_PAIR_CHECK.py` was executed with Python 3.14 and SymPy 1.14.0. All **49 bounded exact checks passed**; the complete result is `AGENT_PAIR_CHECK_OUTPUT.json`. Checks cover difference multisets, Fourier/bispectral values, both six-particle orbits, ACUE probabilities and tilt normalization, the exact forward response, discriminant and endpoint algebra, four finite periodic lifts, and the continuous DPP triple coefficient. An initial Python delimiter typo was corrected before the successful run; no mathematical check failed. This is deterministic exact algebra, not a large numerical scan. The checker does not certify infinite-dimensional DPP existence, mixing, rigidity, or an arithmetic conjecture; their stated justification is the ordinary proof above and the cited primary input.

The heat configurations and proposed depth formulas were supplied by the root investigator and independently derived here. The stationary spectral construction, its explicit triple witness, and the convolution-DPP sine rigidity proof were developed in this lane. Prior programme homometry and determinantal identifiability statements were checked against the earlier archive before formulating the distinctions above. No Git mutation or external model session was used.
