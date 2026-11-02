# Galilean localization: second-pass proof audit and the exact ζ obligation

2026-09-05. The same heat-flow research agent performed this second-pass audit; the separate prime-lane agent supplied the earlier independent review. This audit rereads the round-1 Galilean argument from its definitions. It does not extend the random-matrix model family or claim a new ζ theorem. No repository files were changed. The argument remains an ordinary mathematical proof, not a Lean or interval-arithmetic certificate.

**Audit conclusion.** The deterministic asymptotic conclusion survives. The stronger quantitative bound can also be retained: the previously unspecified constants can be chosen uniformly in N. A deliberately coarse explicit choice is

$$K=16384,\qquad \eta_0=\frac1{524288},$$

for which the proof below gives

$$\frac{\delta^2}{8}\le D\le\delta^2\left(\frac18+K\delta^2(B+1)\right)
\quad\text{if }\delta^2(B+1)\le\eta_0.$$

The constants are not optimized and are not useful numerical record constants. Their purpose is to certify that no dependence on N or on the background drift has been hidden in the big-O statement. The proof needs no complex Gaussian contour shift, Rouché theorem, or unproved continuity of a general hitting-time functional.

## 1. Exact assumptions and definitions

Let N≥2 and let P be a degree-N polynomial with N distinct roots on the unit circle. Its leading and constant coefficients are nonzero. Define

$$P_s(z)=\sum_{j=0}^N a_j e^{s j(N-j)}z^j,\qquad
D=\inf\{s>0:\operatorname{disc}(P_s)=0\},$$

with infimum of the empty set equal to infinity. Both endpoint coefficients remain fixed and nonzero for every real s.

Let δ be the smallest circular angular gap. Rotate its endpoints to −δ/2 and δ/2. Choose all other angles θk in (−π,π], and set

$$Q_0(x)=p_\delta(x)H(x),\quad
p_\delta(x)=\sin\frac{x-\delta/2}{2}\sin\frac{x+\delta/2}{2},\quad
H(x)=\prod_{k\ne\pm}\sin\frac{x-\theta_k}{2}.$$

Multiplying by a fixed nonzero scalar relates this real trigonometric polynomial to the centered characteristic polynomial. Define

$$L=\frac{H'(0)}{H(0)}=-\frac12\sum_{k\ne\pm}\cot\frac{\theta_k}{2},\qquad
B=\frac14\sum_{k\ne\pm}\csc^2\frac{\theta_k}{2},\qquad
\eta=\delta^2(B+1).$$

H(0) is nonzero. Empty background products and sums are permitted. The coefficient flow has the same zeros as

$$Q_s=e^{s\partial_x^2}Q_0,$$

because the missing scalar factor is exp(sN²/4). For odd N the centered trigonometric polynomial is antiperiodic over 2π; the real-line Gaussian formula is nevertheless exact term by term on its finitely many Fourier modes.

## 2. Global centered-factor estimate: checked

For real c,v, let w=|v|√(1+c²). We verify

$$|\cos v-c\sin v|e^{cv}\le e^{4(1+c^2)v^2}. \tag{2.1}$$

If w≥1/2, use |cos v−c sin v|≤1+|c||v|. Taking logarithms, when the factor is nonzero,

$$\log|\cos v-c\sin v|+cv
\le\log(1+|c||v|)+|c||v|
\le2w\le4w^2.$$

If w≤1/2, r(u)=cos u−c sin u is positive along the segment between 0 and v, because

$$r(u)\ge1-u^2/2-|c||u|\ge1-1/8-1/2>0.$$

The function f(u)=log r(u)+cu has f(0)=f′(0)=0 and

$$f''(u)=-\frac{1+c^2}{r(u)^2}<0.$$

Therefore f(v)≤0. The zero-factor case is immediate. This proves (2.1) on the full real line, including beyond the first background root.

Define R(y)=exp(−Ly)H(y)/H(0). Each factor is cos(y/2)−cot(θk/2)sin(y/2), with exactly the matching exponential exp(y cot(θk/2)/2). Hence

$$|R(y)|\le e^{4By^2},\qquad y\in\mathbb R. \tag{2.2}$$

There is no estimate involving |L| in (2.2).

## 3. The global error |R−1|: checked with its constants

Put ak=1/(2|sin(θk/2)|), so B=Σak². The sine Lipschitz inequality gives, for every real u,

$$\left|\frac{\sin((u-\theta_k)/2)}{\sin(-\theta_k/2)}-1\right|
\le a_k|u|.$$

If By²≤1/16, then for every u between 0 and y every ratio on the left is at least 3/4. H has constant sign there, and

$$-\frac{16}{9}B\le (\log|H|)''(u)
=-\frac14\sum_{k\ne\pm}\csc^2\frac{u-\theta_k}{2}\le0.$$

Subtract Ly and integrate twice from zero. This is valid for positive or negative y: the integral remainder has nonnegative weights in either direction. It gives

$$-\frac89By^2\le\log R(y)\le0,$$

and in particular |R(y)−1|≤By². If By²>1/16, (2.2) gives

$$|R(y)-1|\le e^{4By^2}+1\le32By^2e^{4By^2}.$$

Thus the proposed global bound is correct:

$$|R(y)-1|\le32By^2e^{4By^2}\quad(y\in\mathbb R). \tag{3.1}$$

When B=0, H is constant and the conclusion is exact. The argument does not infer global control by extending a local logarithm through its zeros.

## 4. Heat conjugation and Gaussian tails: exact and uniform

For s>0, completing the square in the real Gaussian integral gives

$$e^{s\partial_x^2}(e^{Lx}f(x))
=e^{Lx+L^2s}(e^{s\partial_x^2}f)(x+2Ls). \tag{4.1}$$

No complex contour shift occurs. In the present finite problem all integrals converge: the original Q0 is bounded on the real line, and exp(−Lx)Q0(x) has at most exponential real growth. The estimates below additionally provide uniform domination as N varies.

Put s=τδ², x=δξ−2Ls, Y=ξ+√(2τ)Z, with Z standard real normal. Then

$$F_\delta(\xi,\tau):=
\frac{4e^{-L\delta\xi+L^2s}}{\delta^2H(0)}Q_s(\delta\xi-2Ls)
=\mathbb E[A_\delta(Y)R(\delta Y)],$$

where

$$A_\delta(Y)=\frac4{\delta^2}
\sin\frac{\delta(Y-1/2)}2\sin\frac{\delta(Y+1/2)}2.$$

Let P(Y)=Y²−1/4 and q=δ²B. Two elementary global estimates are

$$|A_\delta(Y)|\le Y^2+1/4,$$

$$|A_\delta(Y)-P(Y)|
\le\frac{\delta^2}{12}|Y^2-1/4|(Y^2+1/4)
\le\frac{\delta^2}{6}(1+Y^4).$$

For the second estimate use |sin u−u|≤|u|³/6 and |sin u|≤|u|; neither estimate needs u small. Since

$$Y^4+Y^2/4\le\frac98(1+Y^4),$$

equation (3.1) implies

$$|A_\delta(Y)R(\delta Y)-P(Y)|
\le37\eta(1+Y^4)e^{4qY^2}. \tag{4.2}$$

We now fix the only compact set needed in the collision proof:

$$|\xi|\le2,\qquad0\le\tau\le\frac14.$$

On this set Y²≤8+Z². If q≤1/64, then

$$e^{4qY^2}\le e^{1/2}e^{Z^2/16},\qquad
1+Y^4\le65+16Z^2+Z^4.$$

For a=8/7, the Gaussian moment identities give

$$\mathbb E[(65+16Z^2+Z^4)e^{Z^2/16}]
=65a^{1/2}+16a^{3/2}+3a^{5/2}.$$

Each power displayed is less than 2, and exp(1/2)<2. Therefore

$$\sup\mathbb E[(1+Y^4)e^{4qY^2}]<336.$$

Combining this with (4.2) proves the explicit N-uniform estimate

$$\sup_{|\xi|\le2,\ 0\le\tau\le1/4}
|F_\delta(\xi,\tau)-(\xi^2-1/4+2\tau)|
\le K\eta,\qquad K=16384, \tag{4.3}$$

because 37·336=12432<16384. No bound on Lδ is imposed. The coefficient-normalizing exponential can be large, but it is exact, real, and nonzero.

## 5. Quantitative positivity and root tracking: checked

Assume η≤η0=1/(32K)=1/524288. This implies q≤1/64 and δ<1. Put

$$\tau_* =\frac18+K\eta\le\frac5{32}<\frac14,\qquad s_* =\delta^2\tau_*.$$

At τ=τ*, equation (4.3) gives, for every |ξ|≤2,

$$F_\delta(\xi,\tau_*)\ge\xi^2+2K\eta-K\eta
\ge K\eta>0. \tag{5.1}$$

At either boundary ξ=±2, for every 0≤τ≤τ*, it gives

$$F_\delta(\pm2,\tau)\ge\frac{15}{4}-K\eta>0. \tag{5.2}$$

Initially the moving interval I_s=[−2δ−2Ls,2δ−2Ls] contains exactly the selected two roots. Indeed any additional root with circular lift |θk|≤2δ would contribute

$$\delta^2B\ge\frac{\delta^2}{4\sin^2(\theta_k/2)}
\ge\frac{\delta^2}{\theta_k^2}\ge\frac14,$$

contrary to the assumed smallness. Also 4δ<2π, so the initial interval does not contain a duplicated lift of the same root.

Suppose D>s*. The family Ps has simple roots throughout the closed interval [0,s*]. Since the multiplier j(N−j) is symmetric under j↔N−j, the initial self-inversive relation is preserved. A root and its reciprocal-conjugate root agree initially. Local uniqueness of a simple root branch makes them agree throughout the interval. Hence every root remains on the unit circle before D. Fixed nonzero endpoint coefficients exclude escape via zero or infinity.

Continuous angle lifts of the two selected roots exist on [0,s*]. They cannot cross either moving boundary, by (5.2). They cannot disappear or merge, by D>s*. They must therefore still be real zeros inside I_s* at the final time, contradicting (5.1).

It follows that

$$D\le s_* =\delta^2(1/8+K\eta).$$

This argument remains valid if the interval translates across many initial gaps or around the circle: it is formulated on the real cover, with continuously moving nonvanishing boundaries. It also remains valid if some other pair would have collided first; that already contradicts D>s* and establishes the same upper bound. A local zero count at the final time alone would have been insufficient, but the all-time boundary estimate supplies the missing step.

For completeness, the deterministic lower bound can be checked directly. Lift one adjacent pair to a<b=a+g, and every other point to c in (b,a+2π). Its contribution to the gap derivative is

$$\cot\frac{c-b}{2}-\cot\frac{c-a}{2}>0,$$

because cot is decreasing on (0,π). The pair's own contribution is −2cot(g/2), so g′≥−2cot(g/2). Compare every gap with the same scalar solution initialized at δ. That scalar solution satisfies cos(h(s)/2)=exp(s)cos(δ/2), and reaches zero at −log cos(δ/2). No gap can collide while this comparison solution is positive. Finally −log cos(δ/2)≥δ²/8 by integrating tan u≥u on [0,δ/2]. Under η≤η0 one has δ<π, so the real logarithm is well-defined. Thus the quantitative theorem is retained. There is no need to downgrade it to o(1).

## 6. What must change when the object is the true H_t

The finite theorem does not define a global ζ depth by looking at a truncated list of zeros. In particular, a global first collision among infinitely many zeros and a local collision near a selected height are different quantities. After RH and the known nonnegativity of the Newman constant, global backward instability is not a new conclusion.

Work in the real coordinate of H_t itself; do not mix it with the usual ζ ordinate without the factor-of-two conversion. Suppose two consecutive simple real zeros of H0 are c−δ/2 and c+δ/2. Factor

$$H_0(c+y)=(y^2-\delta^2/4)h_c(y),\qquad
L_c=h_c'(0)/h_c(0),\qquad
R_c(y)=e^{-L_cy}h_c(y)/h_c(0).$$

The exact heat identity is H_{−s}=exp(s∂²)H0. It follows directly from the defining Fourier integral by real Gaussian convolution. Rodgers–Tao's equations (1) and (4) use H0(z)=ξ(1/2+iz/2)/8 and the multiplier exp(tu²), respectively; these equations were checked in the downloaded primary paper. In the moving frame y=δξ−2Lcs, the identity gives

$$\frac{e^{-L_c\delta\xi+L_c^2s}}{\delta^2h_c(0)}
H_{-s}(c+\delta\xi-2L_cs)
=\mathbb E[(Y^2-1/4)R_c(\delta Y)],
\quad s=\tau\delta^2. \tag{6.1}$$

Thus a precise sufficient analytic obligation for local collision localization is

$$\sup_{|\xi|\le2,\ 0\le\tau\le1/4}
\mathbb E[(1+Y^2)|R_c(\delta Y)-1|]\longrightarrow0. \tag{Z-tail}$$

This condition states both local flatness and Gaussian-tail uniform integrability. A Taylor approximation on a shrinking real interval, without the tail condition, would not justify (6.1).

The root-tracking conclusion in this infinite setting must be stated locally: a multiple real zero occurs in the moving tube before the specified time, or a tracked real branch already met another branch there. It is not a lower bound for a positive global first-collision time of H_t. The finite proof's assumption that all roots remain real globally before the first collision should not be imported unchanged into this setting.

## 7. Under RH, the canonical product supplies the far-tail structure

There is a useful simplification: under RH, the true H0 is a real entire function of order one with real zeros. After removing the pair and its linear logarithmic term, its genus-one canonical product gives

$$R_c(y)=\prod_{k\ne\pm}\left(1-\frac{y}{d_k}\right)e^{y/d_k},
\qquad d_k=x_k-c,\qquad B_c=\sum_{k\ne\pm}d_k^{-2}<\infty.$$ 

Multiplicity is counted in this product. The selected two zeros must be simple; other multiplicities merely increase Bc. These are classical Hadamard-product facts used in the Lehmer-pair literature, not a new random-matrix representation. See [Csordas–Smith–Varga](https://www.math.kent.edu/~varga/pub/paper_206.pdf) and [Rodgers–Tao](https://arxiv.org/abs/1801.05914).

For every real u,

$$|1-u|e^u\le e^{u^2/2}. \tag{7.1}$$

One direct proof studies f(u)=u²/2−u−log|1−u|: its derivative is u(2−u)/(1−u) on u<1 and u(u−2)/(u−1) on u>1. The minima are f(0)=f(2)=0. At u=1 the inequality is immediate.

Apply (7.1) to finite partial products and pass to the canonical-product limit. This gives the global bound

$$|R_c(y)|\le e^{B_cy^2/2}.$$

The same local logarithmic-curvature argument as in §3 yields

$$|R_c(y)-1|\le32B_cy^2e^{B_cy^2/2}.$$

Consequently, the condition δ²Bc→0 implies (Z-tail), including its Gaussian tails. This is a conditional analytic reduction in the spirit of classical Lehmer-pair estimates. It does not establish that the required isolated pairs exist, or occur with any particular frequency, among ζ zeros. No new unconditional or RH-conditional spacing result has been obtained here.

## 8. If a finite window is used, the exact omitted term

If the canonical product is split into nearby zeros and distant zeros, write R=Rnear Rfar and Bc=Bnear+Bfar. Its missing outer contribution obeys

$$|R(y)-R_{\mathrm{near}}(y)|
\le32B_{\mathrm{far}}y^2e^{B_cy^2/2}.$$

Thus, in the regime δ²Bc bounded by a sufficiently small constant, the normalized Gaussian heat error from the omitted factor is O(δ²Bfar). A sufficient truncation obligation is

$$\delta^2\sum_{|x_k-c|>W}|x_k-c|^{-2}\to0.$$

The omitted **linear drift** must also be retained or removed using the true Lc. It need not be small merely because its curvature is small. More explicitly, the correct finite approximation before heat evolution is

$$h_c(0)(y^2-\delta^2/4)
\exp\left[\left(L_c+\sum_{\mathrm{near}}d_k^{-1}\right)y\right]
\prod_{\mathrm{near}}(1-y/d_k).$$

It is a polynomial times a specified exponential; the exponential can be handled by the exact heat-conjugation identity. Replacing this by its polynomial factor alone silently changes the initial logarithmic derivative, and can shift the entire local configuration by more than one gap.

A strong uniform hard-core hypothesis can bound inverse-square tails by packing, but it generally makes δ²Bc only O(1), not o(1), at the minimum allowed spacing. A density version of AH allows exceptional clusters and therefore supplies no uniform bound on Bc for every selected window. Neither version alone yields (Z-tail) with vanishing error at the half-spacing threshold. Using the full true canonical product avoids a matrix-model or arbitrary polynomial-cutoff assumption, but it does not provide the missing arithmetic spacing information.

## 9. The shortest genuinely missing arithmetic lemma

For the proposed Level-B target of depth o(mean-spacing²) along a sequence, the clean missing input is an **isolated small-pair lemma**: there should exist consecutive simple zeros near heights c→∞ with

$$\frac{\delta_c}{h_c}\to0,\qquad
\delta_c^2\sum_{k\ne\pm}(x_k-c)^{-2}\to0,$$

where hc is the mean spacing in the H-coordinate. The preceding analytic argument explains how such input would produce a local collision statement. It does not prove this arithmetic lemma. Bandwidth-one information alone does not establish it, and merely assuming it inside a “near-collision step” would assume the main unresolved microscopic input.

For an AH that permits a zero-density exceptional set, even this subsequential lemma is insufficient to refute AH. The task then needs a positive-density arithmetic statement in a fixed forbidden normalized-gap interval, or an equivalently strong statistic controlling the density of exceptions. A toy quantifier check is a block of N gaps consisting of εN, 2−εN, and N−2 gaps equal to 1. Their sum is N; all but 2/N of the gaps are integer, hence half-integer, while the minimum εN tends to zero. Having a tiny minimum in every large block does not by itself contradict a density AH. This toy example is only a quantifier counterexample, not a claim to match all ζ correlation constraints.

The recommended next arithmetic task is therefore to specify and prove the weighted pair-count or energy estimate that creates a positive proportion of forbidden spacings, with its exact support and averaging range. The finite heat theorem cannot replace that input. The current audit supplies a clean analytic interface and identifies which tail estimates become automatic under RH; it supplies no new ζ spacing theorem.

## 10. Reproducibility and review status

The companion `galilean_audit_constants.py` checks the exact rational inequalities used to choose K and η0, and verifies symbolic derivatives in the centered sine factor and canonical-product factor. Its output is saved beside it. These checks verify the displayed algebra and numerical constants; they do not verify the topology or the analytic argument in Lean.

No Claude tool was started. No repository source was edited. All assertions above are confined to the stated deterministic theorem and explicit conditional analytic obligations.
