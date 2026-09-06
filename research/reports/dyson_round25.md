# Round 25: joint cancellation at the central prime scale and the actual Fourier remainder

Date: 2026-09-06. Status: two complete ordinary proofs with independent internal reviews. The central arithmetic reduction assumes ordinary RH. The Fourier identity is unconditional; its zero-core and centered norm estimates use RH. No strict covariance bound, RH proof, Montgomery–Dyson theorem, AH refutation, new gap record or external novelty claim is made.

The new mathematical conclusion is that several separately large one-prime mains cancel jointly in the actual fixed smooth packet, including the central scale \(X=T^2\). A second proof removes the genuine zero-frequency core and distant Fourier tails of the remaining Möbius–prime covariance. Its signed contribution in the intervening frequency region remains uncontrolled at the required scale.

## 1. Exact packet and theorem

Let
\[
\ell=\log T,\quad X=T^\alpha,\quad H=X/T,\quad Q=X^\rho,
\quad\theta_0=1-1/\alpha.
\]
Keep the fixed \(\omega\) and actual kernel
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}\,dx,
\]
\[
F(m,h)=b_T(m)\chi(m/X)V(h/H)(m/(m+h))^T,
\]
where the real smooth cutoffs \(\chi,V\) have compact support in \((1,2)\). The Pareto factor, all integer endpoints and every prime power remain exact.

Define
\[
\mathcal P=
2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}F(m,h)
\{\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\},
\]
\[
c_Q(m)=\sum_{\substack{d\mid m\\d>Q}}\mu(d)\log(m/d),
\qquad
\mathcal Z_Q^{(2)}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)c_Q(m)[\Lambda(m+h)-2].
\]
The divisor cutoff is sharp, and there is no added coprimality between factors of \(m\).

The [complete author proof](../dyson/round25/joint-main-cancellation/JOINT_MAIN_CANCELLATION.md) and [Plato's independent full review](../dyson/round25/joint-main-cancellation-review/INDEPENDENT_JOINT_MAIN_REVIEW.md) prove under ordinary RH
\[
\boxed{\mathcal P=\mathcal Z_Q^{(2)}+o(1)}
\]
uniformly on any fixed closed parameter set satisfying
\[
7/4\le\alpha\le9/4,\qquad
0<\rho<\theta_0<1/2+\rho/2,
\]
with a fixed completion order \(J\) such that
\(J(\theta_0-\rho)>\rho\).

In particular one may take
\[
\boxed{Q=X^{2/5},\quad J=16,\quad
7/4\le\alpha\le9/4.}
\]
This covers \(X=T^2\). It needs no condition \(X/Q<H\), because the complementary center is completed on the pure even lattice rather than through the primitive-cofactor mask.

This is a fixed compact physical-shift theorem. It does not, by itself, sum all shift scales or prove a bound for the full variance.

## 2. Why the large mains cancel

The exact divisor opening retains five pieces:
\[
\mathcal P=\mathcal B_Q+\mathcal N_Q+\mathcal A_Q
+\mathcal C_Q-\mathcal M_{\mathfrak S}.
\]
Here the primitive small-divisor discrepancy has mean-zero physical-shift kernel. Its normalized Fourier coefficients are bounded by \(2/d\), as the independent review makes explicit. Fixed-order completion and Chebyshev give
\[
|\mathcal B_Q|\ll_J
\frac Q{\log X}(Q/H)^J.
\]
The R24 exact \(h=2pr\) count gives
\[
|\mathcal N_Q|\ll_\eta X^\eta/T.
\]
This count remains valid when \(H<p\), when there are no positive integer solutions. No \(H\gg\sqrt X\) or old owner-factor restriction is reintroduced.

Put
\[
a_Q(m)=\sum_{\substack{d\le Q\\d\ {\rm odd}}}
\frac{\mu(d)}d\log(m/d),
\qquad
J_-(m)=\int F(m,h)\,dh,\quad
J_+(n)=\int F(n-h,h)\,dh.
\]
Completing the actual principal's primitive shift mask gives
\[
\mathcal A_Q
=\sum_{n\ {\rm odd}}\Lambda(n)
\int F(n-h,h)a_Q(n-h)\,dh
+O((Q/H)\log^3X+\log X/T).
\]
The nonunit prime-power mean is paid separately through
\(\sum_{d\le Q,p\mid d}1/d\ll\log(2Q)/p\).

The complementary flat center gives
\[
\mathcal C_Q=\mathcal Z_Q^{(2)}+\mathcal L_Q^0+O(H^{-1}),
\quad
\mathcal L_Q^0=2\sum_{m\ {\rm odd}}c_Q(m)J_-(m).
\]
Opening its complementary divisor identity and completing the odd cofactor on scale \(X/d\) yields
\[
\mathcal L_Q^0=
2\sum_{m\ {\rm odd}}\Lambda(m)J_-(m)
-\int J_-(m)a_Q(m)\,dm
+O\!\left(\frac{HQ^2}{X^2\log X}\right).
\]
The factor \(d/X\) from smooth Poisson completion is essential. A plain total-variation bound would leave a growing error.

Under ordinary RH, [Soundararajan's Möbius-prefix theorem](https://arxiv.org/pdf/0705.0723v2), printed page 1, gives \(M(y)\ll_\epsilon y^{1/2+\epsilon}\). The exact odd identity
\[
M_{\rm odd}(y)=\sum_{j\ge0}M(y/2^j)
\]
and the Euler product
\[
\sum_{d\ {\rm odd}}\frac{\mu(d)}{d^s}
=\frac1{(1-2^{-s})\zeta(s)}
\]
therefore imply
\[
\sum_{d\ {\rm odd}}\frac{\mu(d)}d=0,\qquad
\sum_{d\ {\rm odd}}\frac{\mu(d)\log d}d=-2.
\]
The derivative of the Euler product at one is \(+2\). Thus
\[
a_Q(m)=2+e_Q(m),\qquad
e_Q(m)\ll Q^{-1/2+\epsilon}\log X.
\]
All derivatives here hold at fixed \(Q\), before any change of physical packet.

Combining the two main formulas makes the entire \(e_Q\) contribution a centered statistic:
\[
\mathcal R_Q=
\sum_{n\ {\rm odd}}\Lambda(n)G_Q(n)-\int G_Q(y)\,dy,
\]
\[
G_Q(n)=\int F(n-h,h)e_Q(n-h)\,dh.
\]
The ordinary-RH estimate for \(\Psi(y)-y\), with powers of two separately removed, now gives
\[
\boxed{\mathcal R_Q\ll
\frac H{\sqrt X}Q^{-1/2+\epsilon}\log X=o(1).}
\]
The proof uses the product of two errors only after exact centering. It does not bound the large absolute integral of \(e_Q\) and call it negligible.

The remaining constant-two part is
\[
2\sum_{m\ {\rm odd}}\Lambda(m)J_-(m)
+2\sum_{n\ {\rm odd}}\Lambda(n)J_+(n)
-2\int J_-(m)\,dm.
\]
Both true singular-series marginals produce precisely this expression, up to \(O(\ell^{-2})\) and an even smaller lattice error.

For this last step the unconditional triangular singular-series asymptotic from [Montgomery–Soundararajan](https://arxiv.org/pdf/math/0409258v1) gives the compact transform
\[
\sum_{h\ {\rm even}}\mathfrak S(h)f(h)
=\int f(h)\,dh+O(A_f).
\]
The function \(f\) has amplitude \(A_f\), derivative scale \(H\), and vanishes near zero. In the hinge calculation \(\int y f''(y)\,dy=0\), so the apparent \(\log H\) term cancels. Both forward and backward marginals are evaluated separately with their exact moving endpoints.

## 3. Quantitative margins and scope

For \(Q=X^{2/5}\), \(\epsilon=\eta=1/100\), the worst positive power margins are:

| Removed component | Positive margin in the power of \(X\) |
|---|---:|
| Primitive discrepancy, \(J=16\) | \(2/35\) |
| Principal-mask completion | \(1/35\) |
| Odd-cofactor grid error | \(29/45\) |
| Joint centered RH error | \(158/1125\) |
| Nonprimitive prime powers | \(391/900\) |

The remaining \(O(\ell^{-2})\) packet error is negligible for this fixed theorem. It cannot automatically be discarded in \(O(\ell^2)\) different height/shift packets. The subsequent full-window work must keep the more precise singular-series correction.

An [independent coordinator Möbius lemma](../dyson/round25/coordinator-odd-mobius/ODD_MOBIUS_CENTERED_PACKET_LEMMA.md) proves the ordinary-RH coefficient and centered-packet input separately. The [coordinator's full joint-main review](../dyson/round25/coordinator-joint-main/COORDINATOR_JOINT_MAIN_REVIEW.md) accepts the complete fixed-window proof and independently identifies the refined singular-series correction. These are separate records, not edits to the author manuscript.

## 4. The actual Fourier identity

The [Fourier author proof](../dyson/round25/mobius-fourier-audit/ACTUAL_MOBIUS_FOURIER_TEST.md) and [root's independent full review](../dyson/round25/fourier-root-review/INDEPENDENT_FOURIER_REVIEW.md) examine the remaining actual covariance in both the new range and the earlier \(Q=X^{523/1000}\) upper range.

Write \(e(u)=e^{2\pi i u}\). Expand the exact rescaled weight in its lower endpoint coordinate with period four:
\[
X\ell^2F(Xv,Hz)=\sum_{j\in\mathbb Z}a_{T,j}(z)e(jv/4).
\]
The coefficients and their fixed-order derivatives decay faster than every fixed inverse power of \(|j|\). With \(D_k=X/k\), define
\[
M_{k,j}(\vartheta)=
\sum_{\substack{d\ {\rm odd}\\d>Q\\D_k<d<2D_k}}
\mu(d)e(-kd\vartheta+jkd/(4X)),
\]
\[
P(\vartheta)=\sum_{n\ {\rm odd}}[\Lambda(n)-2]
\zeta_0(n/X)e(n\vartheta),
\quad
W_j(\vartheta)=\sum_{h\ {\rm even}}a_{T,j}(h/H)e(-h\vartheta).
\]
The smooth auxiliary cutoff \(\zeta_0\) equals one on every contributing prime endpoint; it is not the Riemann zeta function.

Fourier orthogonality gives exactly
\[
\boxed{\mathcal Z_Q^{(2)}
=\frac4{X\ell^2}\sum_{\substack{3\le k<2X/Q\\k\ {\rm odd}}}
\log k\sum_j\int_{-1/4}^{1/4}
M_{k,j}(\vartheta)P(\vartheta)W_j(\vartheta)\,d\vartheta.}
\]
The product has period one half: its two odd-endpoint factors change sign and its even-shift factor does not. The displayed factor four accounts for this exactly.

Poisson summation supplies
\[
|W_j(\vartheta)|\ll_{B,J}
(1+|j|)^{-B}H(1+H|\vartheta|)^{-J}.
\]
This is decay, not fictitious compact support.

## 5. What Fourier estimates remove, and what they fail to remove

The source-valid uniform Davenport bound, together with the ordinary-RH centered small-arc prime norm of Bhowmik–Schlage-Puchta, gives only
\[
|\mathcal Z_Q^{(2)}|\ll_A\sqrt X\,\log^{-A}X
\]
for each fixed \(A\). This is weaker than the existing
\(\sqrt H\log^{3/2}X\) estimate. Even a hypothetical factorwise square-root Möbius bound would leave a growing \(\sqrt K\) loss in that Cauchy argument. It is not a solution to keep improving the same factorwise estimate.

There is nevertheless a genuine removable piece. For a zero core \(|\vartheta|\le R/X\), actual Abel summation gives
\[
|M_{k,j}(\vartheta)|\ll_\eta
D_k^{1/2+\eta}(1+X|\vartheta|+|j|),
\]
with the essential phase length \(X|\vartheta|\), not \(D_k|\vartheta|\). The complete cofactor sum and centered prime estimate then yield
\[
|\mathcal Z_{\rm core}(R)|
\ll_\eta\frac{\sqrt K}{T}X^\eta R(1+R)^2\log X.
\]
For any fixed logarithmic \(R\), this tends to zero. The worst power of \(\sqrt K/T\) is \(-13/90\) in the new range.

The remote tail \(|\vartheta|>U_*/H\), with \(U_*=X^{1/100}\), is controlled by the fixed derivative order \(J=202\):
\[
|\mathcal Z_{\rm tail}|\ll XU_*^{1-J}=X^{-101/100}.
\]
Thus the exact remaining signed integral lies in
\[
\boxed{(\log X)^B/X<|\vartheta|\le X^{1/100}/H.}
\]
All actual cofactor weights, Fourier modes and the sharp divisor cutoff remain there. This annulus is not bounded at fluctuation scale.

In the new range \(K/H\) grows, and cofactor phases can resonate near \(\vartheta=1/k\). Ordinary RH controls a Möbius factor at its integer phase but does not supply a square-root prime progression estimate at \(1/k\). Other rational phases introduce character information not supplied by ordinary RH. This identifies a limitation of the estimate, not a lower bound proving these arcs dominate.

## 6. Validation, preservation and next obligation

The joint-main proof has eight groups comprising 3,809 exact finite checks, independently replayed with complete JSON and stdout bytes identical. Its independent proof review verifies all source hypotheses and every endpoint change. The Fourier proof has nine exact rational checks; root replayed them in a copied directory and independently opened the primary Tao, Bhowmik–Schlage-Puchta and Ng statements.

The first Fourier replay setup omitted the author manuscript required for the checker's report hash and stopped before producing results. Copying that exact manuscript repaired the setup; no checker or author source was edited. The preserved review receipt records this.

All original proofs, reviews, source receipts and outputs are retained verbatim locally. Public source omissions are limited to complete third-party reference bodies, with their URLs and hashes preserved. See the [intake manifest](../dyson/round25/INTAKE_MANIFEST.json), [source-link map](../dyson/round25/SOURCE_LINK_MAP.md) and [integration receipt](../logs/round25-integration/INTEGRATION_RECEIPT.json) for exact coverage. No large numerical scan, new model session or PDF rebuild was part of this round.

The next obligation is a legal all-scale reduction with the accumulated singular-series constant, followed by a joint signed estimate that improves the actual variance bound. A global equivalent formulation is useful only if it reveals an estimable structure; it is not itself a strict correlation theorem. Further single-factor frequency scans, searches in the excluded exact kernel family and claims of a famous-conjecture solution are postponed.
