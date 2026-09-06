# Joint cancellation of the one-prime mains in an actual centered quadratic packet

Date: 2026-09-05. Author: Euclid. Status: ordinary proof submitted for independent review. The central cancellation and the resulting reduction assume the ordinary Riemann hypothesis (RH). All algebra, lattice completion, nonprimitive removal and singular-series averaging below are unconditional. This is a newly verified component of this programme using classical inputs; no novelty, strict variance bound, AH refutation or new prime-gap theorem is claimed.

## 1. Statement and the precise surviving arithmetic object

Set
\[
\ell=\log T,\quad X=T^\alpha,\quad H=X/T,\quad Q=X^\rho,
\qquad \theta=1-1/\alpha.
\tag{1}
\]
The parameters range in any fixed closed subset of
\[
\frac74\le\alpha\le\frac94,\qquad
0<\rho<\theta,\qquad
\theta<\frac12+\frac\rho2.
\tag{2}
\]
Choose a fixed integer \(J\ge1\) such that
\(J(\theta-\rho)>\rho\) uniformly on that subset. All conclusions are as \(T\to\infty\) through real values. Strict inequalities have fixed positive margins; no parameter or derivative order grows with \(T\).

Keep the actual packet
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}dx,
\]
\[
F(m,h)=b_T(m)\chi(m/X)V(h/H)
\left(\frac m{m+h}\right)^T.
\tag{3}
\]
Here \(\omega\) is the fixed nonnegative smooth weight supported in \([7/4,9/4]\), and \(\chi,V\in C_c^\infty((1,2))\) are fixed real functions. Constants may depend on these functions and fixed parameter margins. We never replace the Pareto factor by an exponential. Extend \(F\) by zero outside its positive support. Every sum in this note is finite: \(X<m<2X\), \(H<h<2H\), and \(X<m+h<3X\) eventually.

Let \(\mathfrak S(h)\) be the usual two-prime singular series; it is zero for odd \(h\). Define
\[
\mathcal P
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)\{\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\}.
\tag{4}
\]
The exact complementary coefficient and its parity-centered covariance are
\[
c_Q(m)=\sum_{\substack{d\mid m\\d>Q}}\mu(d)\log(m/d),
\quad m\ {\rm odd},
\]
\[
\boxed{\mathcal Z_Q^{(2)}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)c_Q(m)[\Lambda(m+h)-2].}
\tag{5}
\]
The cutoff is exactly \(d>Q\); it is not smoothed and no coprimality between the two factors of \(m\) is imposed.

**Theorem 1.** Under RH and (2),
\[
\boxed{\mathcal P=\mathcal Z_Q^{(2)}+o(1).}
\tag{6}
\]
In particular (6) holds uniformly for the full compact window
\[
\boxed{\frac74\le\alpha\le\frac94,\qquad
\rho=\frac25,\qquad J=16.}
\tag{7}
\]
Thus this reduction covers the central scale \(X=T^2\). It is not limited to the previous \(X\ge T^{11/5}\) window. It uses the exact flat parity center \(2\), rather than completing the additional primitive mask of the complementary cofactor \(k=m/d\). No condition \(X/Q<H\) is needed.

The theorem evaluates the jointly centered one-prime main terms. It does **not** estimate (5), which remains a genuinely signed Möbius–prime quadratic covariance at fluctuation scale. Nor does this fixed compact \(h/H\)-packet theorem itself sum the near-zero, large-length or all-height tails of the full variance target.

## 2. An exact five-term decomposition, with its two removable debts

Write
\[
w_{n,d}(h)=F(n-h,h)\log((n-h)/d),
\]
\[
K_{d,h}(n)=1_{(n,d)=1}
\left(1_{n\equiv h\pmod d}
-\frac{1_{(h,d)=1}}{\varphi(d)}\right),
\tag{8}
\]
and sum all \(d\le Q\) that are odd. Define
\[
\mathcal B_Q=2\sum_d\mu(d)
 \sum_{\substack{n\ {\rm odd}\\h\ {\rm even}}}
 \Lambda(n)w_{n,d}(h)K_{d,h}(n),
\]
\[
\mathcal N_Q=2\sum_d\mu(d)
 \sum_{\substack{n\ {\rm odd}\\h\ {\rm even}}}
 \Lambda(n)w_{n,d}(h)
 1_{(h,d)>1}1_{n\equiv h\pmod d},
\]
\[
\mathcal A_Q=2\sum_d\frac{\mu(d)}{\varphi(d)}
 \sum_{\substack{n\ {\rm odd}\\h\ {\rm even}}}
 \Lambda(n)w_{n,d}(h)1_{(n,d)=1}1_{(h,d)=1},
\]
\[
\mathcal M_{\mathfrak S}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2],
\]
\[
\mathcal C_Q
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)c_Q(m)\Lambda(m+h).
\tag{9}
\]
The identity \(\Lambda(m)=\sum_{d\mid m}\mu(d)\log(m/d)\), valid also at \(m=1\), and the partition into primitive and nonprimitive rows give exactly
\[
\mathcal P=\mathcal B_Q+\mathcal N_Q+\mathcal A_Q
+\mathcal C_Q-\mathcal M_{\mathfrak S}.
\tag{10}
\]
The \(d=1\) discrepancy is zero; its principal remains in \(\mathcal A_Q\).

We record the short proofs that the older completion arguments retain their hypotheses in the enlarged window (2). For any fixed derivative order,
\[
b_T^{(j)}(m)\ll_j m^{-j-1}\ell^{-2}.
\tag{11}
\]
Indeed
\[
b_T(m)=\frac{T}{m\ell^2}
\int_0^1\omega((\log m+\log u)/\ell)u^{T-2}du.
\]
Its integral mass is \(1/(T-1)\), so differentiation introduces no power of \(T\). On the support, put \(v=m/X,z=h/H\); the Pareto factor is \((1+z/(Tv))^{-T}\), whose fixed-order derivatives in \(v,z\) are uniformly bounded. Consequently \(F\) has amplitude
\(A=(X\ell^2)^{-1}\), \(m\)-derivative scale \(X\), and \(h\)-derivative scale \(H\). At fixed \(n\), \(F(n-h,h)\) has the same \(h\)-derivative scale \(H\), since \(dm/dh=-1\) and \(H<X\). The weight \(w_{n,d}\) has amplitude \(O(A\log X)\), with the same scales, uniformly for \(d\le Q\).

For a compact smooth weight \(f\) of amplitude \(A_f\) and derivative scale \(H\), Poisson summation gives, for odd \(s\le H\) and fixed \(j\ge1\),
\[
\sum_{h\in2s\mathbb Z}f(h)
=\frac1{2s}\int f(h)\,dh
+O_j(A_f(s/H)^j).
\tag{12}
\]
This follows by \(j+1\) integrations by parts in its Fourier transform. For a unit \(n\bmod d\), the periodic sequence \(K_{d,2r}(n)\) has mean zero. Its Fourier coefficients are bounded by \(2\); applying the same calculation on period \(2d\) gives
\[
\left|\sum_{h\ {\rm even}}w_{n,d}(h)K_{d,h}(n)\right|
\ll_J A\log X\,(d/H)^J.
\]
For nonunit \(n\) the summand vanishes. Chebyshev's bound for the full von Mangoldt sum therefore yields
\[
\boxed{\mathcal B_Q\ll_J
\frac{Q}{\log X}(Q/H)^J=o(1).}
\tag{13}
\]
No prime coefficient is differentiated or asserted to satisfy a phase-twisted Siegel–Walfisz condition.

For \(\mathcal N_Q\), any nonzero prime weight is \(n=p^j\), with an odd prime \(p\mid h\), \(j\ge2\), because \(p\mid d\le Q<X<n\). Also \(p\le\sqrt{3X}\). Write \(h=2pr\): the exact interval \(H<h<2H\) implies
\[
\#\{r:H/(2p)<r<H/p\}\le H/p.
\tag{14}
\]
This remains true when \(H<p\), when the set is empty; no assumption \(H\gg p\) is required. For each fixed \(n,h\), the total divisor coefficient is at most
\(\tau(n-h)\log(2X)\ll_\eta X^\eta\log X\).
There are at most two powers of each odd prime in \((X,3X)\), and
\(\sum_{p\le Y}\log p/p\ll\log(2Y)\). Thus for every fixed \(\eta>0\),
\[
\boxed{\mathcal N_Q\ll_\eta X^\eta/T=o(1)}
\tag{15}
\]
if, for example, \(\eta=1/100\). This is uniform throughout (2) and uses no RH or prime distribution in progressions.

## 3. Complete the actual principal \(\mathcal A_Q\)

Define
\[
a_Q(m)=\sum_{\substack{d\le Q\\d\ {\rm odd}}}
\frac{\mu(d)}d\log(m/d),
\]
\[
J_-(m)=\int F(m,h)\,dh,\qquad
J_+(n)=\int F(n-h,h)\,dh.
\tag{16}
\]
Both \(J_\pm\) are smooth with amplitude \(O(H/(X\ell^2))\) and derivative scale \(X\). Their supports are contained in \((X,3X)\), including the exact shifted endpoints for \(J_+\).

By \(1_{(h,d)=1}=\sum_{s\mid d,\ s\mid h}\mu(s)\) and (12) with \(j=1\),
\[
\sum_{\substack{h\ {\rm even}\\(h,d)=1}}w_{n,d}(h)
=\frac{\varphi(d)}{2d}\int w_{n,d}(h)\,dh
+O(A\log X\,\tau(d)d/H).
\]
Since \(1/\varphi(d)\le\tau(d)/d\) and
\(\sum_{d\le Q}\tau(d)^2/d\ll\log^4(2Q)\), the full error after summing \(n,d\) is
\[
O((Q/H)(\log X)^3).
\tag{17}
\]
The mean retains \(1_{(n,d)=1}\). Its removal is a separate prime-power debt, not a redefinition of the primitive principal. If \(\Lambda(n)\ne0\) and \((n,d)>1\), then \(n=p^j\), \(j\ge2\), and
\[
\sum_{\substack{d\le Q\\p\mid d}}\frac1d
\ll\frac{\log(2Q)}p.
\]
Using \(\int|w_{n,d}|\ll AH\log X\) and the same sum \(\sum\log p/p\), the entire removed mean is
\[
O\!\left(\frac{H}{X\ell^2}
\log X\,\log(2Q)\log X\right)
=O(\log X/T).
\tag{18}
\]
We have proved unconditionally
\[
\boxed{
\mathcal A_Q
=\sum_{n\ {\rm odd}}\Lambda(n)
 \int F(n-h,h)a_Q(n-h)\,dh
+O((Q/H)\log^3X+\log X/T).}
\tag{19}
\]
Every prime power in this estimate has been charged explicitly.

## 4. Complete the complementary flat center on its correct scale

From (5) and (9), there is an exact equality
\[
\mathcal C_Q=\mathcal Z_Q^{(2)}
+4\sum_{m\ {\rm odd}}c_Q(m)
 \sum_{h\ {\rm even}}F(m,h).
\]
Only the even lattice \(2\mathbb Z\) is involved. Equation (12) and
\[
\sum_{X<m<2X}|c_Q(m)|
\le\log(2X)\sum_{m<2X}\tau(m)
\ll X\log^2X
\]
give
\[
\mathcal C_Q=\mathcal Z_Q^{(2)}+\mathcal L_Q^0+O(H^{-1}),
\quad
\mathcal L_Q^0=2\sum_{m\ {\rm odd}}c_Q(m)J_-(m).
\tag{20}
\]
There is no requirement on \(K/H\), where \(K=2X/Q\).

The exact divisor identity now yields
\[
\mathcal L_Q^0
=2\sum_{m\ {\rm odd}}\Lambda(m)J_-(m)
-2\sum_{\substack{d\le Q\\d\ {\rm odd}}}\mu(d)
  \sum_{r\ {\rm odd}}\log r\,J_-(dr).
\tag{21}
\]
For fixed \(d\), the smooth function \(\log r\,J_-(dr)\) has support \(r\asymp X/d\), amplitude \(O(H\log X/(X\ell^2))\), and derivative scale \(X/d\). Poisson summation on the odd lattice, with two derivatives, gives
\[
2\sum_{r\ {\rm odd}}\log r\,J_-(dr)
=\frac1d\int J_-(m)\log(m/d)\,dm
+O\!\left(\frac{H\log X}{X\ell^2}\frac dX\right).
\tag{22}
\]
In particular, merely bounding total variation without this \(d/X\) saving would be insufficient. Summing the actual \(\mu(d)\) coefficients in absolute value only for this error gives
\[
\boxed{
\mathcal L_Q^0
=2\sum_{m\ {\rm odd}}\Lambda(m)J_-(m)
-\int J_-(m)a_Q(m)\,dm
+O\!\left(\frac{HQ^2\log X}{X^2\ell^2}\right).}
\tag{23}
\]
This error is \(o(1)\) in (2): \(\theta+2\rho-2<3\theta-2\le-1/3\). Real \(Q\) is harmless; all finite sums retain the original \(d\le Q\) convention.

## 5. RH evaluates the centered Möbius error, not its large absolute main

The primary Möbius input is Soundararajan, *Partial sums of the Möbius function*, arXiv:0705.0723v2, printed page 1, equation (1), and the stronger Theorem 1 on the same page. Under ordinary RH, for every fixed \(\varepsilon>0\),
\[
M(y)=\sum_{n\le y}\mu(n)\ll_\varepsilon y^{1/2+\varepsilon}.
\tag{24}
\]
No GRH or uniform arithmetic progression version is used.

The exact coefficient identity
\[
M_{\rm odd}(y)=\sum_{j\ge0}M(y/2^j)
\]
has only finitely many nonzero terms and gives the same bound for \(M_{\rm odd}\). In the half-plane of absolute convergence,
\[
\sum_{d\ {\rm odd}}\frac{\mu(d)}{d^s}
=\frac1{(1-2^{-s})\zeta(s)}.
\tag{25}
\]
Partial summation of (24) supplies locally uniform convergence, including differentiated series, in \(\Re s>1/2+\varepsilon\). The simple pole of \(\zeta\) at \(1\) therefore gives
\[
\sum_{d\ {\rm odd}}\frac{\mu(d)}d=0,\qquad
\sum_{d\ {\rm odd}}\frac{\mu(d)\log d}d=-2.
\tag{26}
\]
The derivative of the right side of (25) at \(1\) is \(+2\). In particular the parity normalization is \(a_Q\to2\), not \(1\) or \(-2\).

Tail partial summation gives, uniformly for \(m\in[X,3X]\),
\[
e_Q(m):=a_Q(m)-2
\ll_\varepsilon Q^{-1/2+\varepsilon}\log X,
\]
\[
e_Q^{(j)}(m)\ll_{\varepsilon,j}
Q^{-1/2+\varepsilon}X^{-j}\quad(j\ge1).
\tag{27}
\]
Fix \(0<\varepsilon<1/2\) sufficiently small that
\(\theta-1/2-\rho/2+\rho\varepsilon<0\) uniformly in (2).

Combine the two formulas (19) and (23) **before** estimating (27). Their \(e_Q\) component is exactly
\[
\mathcal R_Q
=\sum_{n\ {\rm odd}}\Lambda(n)G_Q(n)-\int G_Q(y)\,dy,
\quad
G_Q(n)=\int F(n-h,h)e_Q(n-h)\,dh.
\tag{28}
\]
The integral identity follows by the exact change \(m=n-h\). The function \(G_Q\) is compactly supported in \((X,3X)\), with
\[
|G_Q^{(j)}(n)|\ll_{\varepsilon,j}
\frac{H}{X^{j+1}\ell^2}
Q^{-1/2+\varepsilon}\log X\quad(j=0,1).
\tag{29}
\]
Under RH, Schoenfeld's Theorem 10, equation (6.2), or its ordinary asymptotic consequence, gives
\[
\sum_{\substack{n\le y\\n\ {\rm odd}}}\Lambda(n)-y
=O(\sqrt y\log^2(2y)).
\tag{30}
\]
Removing the powers of \(2\) from \(\Psi(y)\) costs only \(O(\log y)\). This uses the \(\Psi\) bound, including prime powers, and not a silent substitution of the \(\vartheta\) bound in equation (6.3).

Abel summation with the compactly supported \(G_Q\), using (29), proves
\[
\boxed{
\mathcal R_Q\ll_\varepsilon
\frac{H}{\sqrt X}Q^{-1/2+\varepsilon}\log X=o(1).}
\tag{31}
\]
The decisive product is the Möbius truncation error times the **centered** one-prime error. The absolute integral of \(e_Q\) would instead cost \(H Q^{-1/2+\varepsilon}/\log X\), which need not tend to zero.

Combining the \(2\)-part and (28) gives
\[
\mathcal A_Q+\mathcal L_Q^0
=2\sum_{m\ {\rm odd}}\Lambda(m)J_-(m)
+2\sum_{n\ {\rm odd}}\Lambda(n)J_+(n)
-2\int J_-(m)\,dm+\mathcal R_Q
\]
\[
\hspace{15mm}
+O\!\left((Q/H)\log^3X+\frac{\log X}{T}
+\frac{HQ^2\log X}{X^2\ell^2}\right).
\tag{32}
\]
The large terms in (32) remain until both exact singular-series marginals have been evaluated.

## 6. Both singular-series marginals, with no lost logarithmic term

The primary unconditional singular-series input is Montgomery–Soundararajan, *Primes in short intervals*, arXiv:math/0409258v1, printed page 4, equation (16). Its consequence used in the reviewed R22 proof is
\[
A_2(y):=\sum_{h\ge1}(y-h)_+[\mathfrak S(h)-1]
=-\frac12y\log y+O(y)\quad(y\ge1).
\tag{33}
\]
This concerns the singular series itself, not a conjectural prime-pair asymptotic.

Set
\[
B_2(y)=\sum_{\substack{h\ge1\\h\ {\rm even}}}
(y-h)_+[\mathfrak S(h)-2].
\]
The difference \(B_2-A_2\) is the alternating hinge sum
\(\sum_{h\ge1}(-1)^{h+1}(y-h)_+\), which is \(O(y)\), uniformly for real \(y\). Therefore
\[
B_2(y)=-\frac12 y\log y+O(y).
\tag{34}
\]
If \(f\) is supported in \((H,2H)\), with amplitude \(A_f\) and derivative scale \(H\), the exact hinge identity gives
\[
\sum_{h\ {\rm even}}[\mathfrak S(h)-2]f(h)
=\int_0^\infty B_2(y)f''(y)\,dy.
\]
Because \(f(0)=0\),
\[
\int_0^\infty yf''(y)\,dy=f(0)=0.
\]
Consequently the apparently large \(\log H\) part cancels:
\[
\left|\sum_{h\ {\rm even}}[\mathfrak S(h)-2]f(h)\right|
\ll\int_H^{2H}
y(1+|\log(y/H)|)|f''(y)|\,dy
\ll A_f.
\tag{35}
\]
Together with even-lattice completion this proves the uniform compact-packet transform
\[
\boxed{\sum_{h\ {\rm even}}\mathfrak S(h)f(h)
=\int f(h)\,dh+O(A_f).}
\tag{36}
\]
Its hypotheses require that the packet vanish near \(h=0\). For a packet with \(f(0)\ne0\), a \(-\tfrac12 f(0)\log H\) term would remain; it must not be erased when extending this note to other length weights.

Apply (36) first with \(f(h)=F(m,h)\), then independently with \(f(h)=F(n-h,h)\). The latter has the same amplitude and \(H\)-scale derivative bounds, including all moving cutoff endpoints. Summing errors using Chebyshev and the integer count \(O(X)\) gives
\[
\mathcal M_{\mathfrak S}
=2\sum_{m\ {\rm odd}}\Lambda(m)J_-(m)
+2\sum_{n\ {\rm odd}}\Lambda(n)J_+(n)
-4\sum_{m\ {\rm odd}}J_-(m)+O(\ell^{-2}).
\tag{37}
\]
The final odd-lattice completion, now at scale \(X\), is
\[
2\sum_{m\ {\rm odd}}J_-(m)
=\int J_-(m)\,dm
+O(H/(X^2\ell^2)).
\tag{38}
\]
Thus the first three terms of (32) are precisely (37), up to the stated small errors. In particular neither singular-series-weighted singleton has been omitted or replaced by a standalone relative PNT assertion.

## 7. Error ledger, the central-scale corollary, and the remaining sign problem

Equations (31)–(38) prove
\[
\boxed{
\mathcal A_Q+\mathcal L_Q^0-\mathcal M_{\mathfrak S}
\ll_\varepsilon
\ell^{-2}+(Q/H)\log^3X+\frac{\log X}{T}
+\frac{HQ^2\log X}{X^2\ell^2}
+\frac{H}{\sqrt X}Q^{-1/2+\varepsilon}\log X
+\frac{H}{X^2\ell^2}.}
\tag{39}
\]
The left side is understood in absolute value. Every term tends to zero in (2), with \(\varepsilon\) chosen as in Section 5. Adding (13), (15) and (20) proves Theorem 1.

For the explicit full-window choice (7), one can use \(\varepsilon=\eta=1/100\). The exact worst-case power margins are
\[
16\left(\frac37-\frac25\right)-\frac25=\frac2{35},
\quad
\frac37-\frac25=\frac1{35},
\]
\[
2-\frac59-\frac45=\frac{29}{45},
\quad
\frac12+\frac15-\frac1{250}-\frac59
=\frac{158}{1125},
\quad
\frac49-\frac1{100}=\frac{391}{900}.
\tag{40}
\]
These respectively control the primitive discrepancy, principal mask completion, odd-cofactor grid error, joint centered RH error and nonprimitive prime powers. All logarithmic factors are fixed powers and do not affect these strict margins. For example the overall error is \(O(\ell^{-2})\) plus explicitly power-decaying terms, with constants depending on the fixed cutoffs.

This improvement is in the **reduction**, not in a strict bound for the quadratic target. It eliminates the separately large and previously unevaluated combination \(\mathcal A_Q+\mathcal L_Q^0-\mathcal M_{\mathfrak S}\) for each fixed compact packet, including \(\alpha=2\). The exact remaining target is (5), with its real Möbius coefficients, sharp \(d>Q\) cutoff, full von Mangoldt weights and parity center. No bound here proves its needed sign, and the 186 one-prime distribution theorem is not invoked as if it estimated this covariance.

For the older upper-wing choice \(\rho=523/1000\), \(\alpha\in[11/5,9/4]\), (39) also applies, with a suitably small fixed \(\varepsilon\). One may combine it with the already reviewed R24 primitive-\(k\) center comparison there, where \(K/H\to0\). That is a separate legal specialization; it is unnecessary for the central-scale corollary.

## 8. Sources, verification and endpoint scope

Primary mathematical inputs:
- K. Soundararajan, *Partial sums of the Möbius function*, [arXiv:0705.0723v2](https://arxiv.org/pdf/0705.0723v2), printed page 1, equation (1) and Theorem 1: ordinary RH implies the Möbius bound (24). The PDF/text and first-page image are retained locally and hash-pinned.
- L. Schoenfeld, *Sharper bounds for the Chebyshev functions \(\theta(x)\) and \(\psi(x)\). II*, [Math. Comp. 30 (1976)](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), printed page 337, Theorem 10, equation (6.2): the RH bound for \(\Psi(x)\).
- H. L. Montgomery and K. Soundararajan, *Primes in short intervals*, [arXiv:math/0409258v1](https://arxiv.org/pdf/math/0409258v1), printed page 4, equation (16): the unconditional singular-series hinge asymptotic. Its conditional prime-correlation hypotheses elsewhere in the paper are not invoked.

The manifest also pins the frozen R22 singleton proof, R23 actual packet/decomposition, R24 exact complement and the enlarged-family nonprimitive lemma. The present note rederives the completion steps whose parameter range has changed rather than inheriting their older numeric window.

The finite divisor identity includes \(m=1\), where both sides vanish. Here support in \(m>X\) avoids that endpoint. All cutoffs in \(m,h\) are smooth and compact and all boundary derivatives vanish. The shift \(n=m+h\) is retained exactly in \(J_+\), the primitive principal and the RH centered statistic. There are no infinite arithmetic or length tails in this packet theorem. Real \(T,X,Q\), integer endpoints and the powers of \(2\) in the odd-prime counting function have all been kept.

The tiny checker only verifies exact finite coefficient identities, parity/centering algebra and rational exponent margins. It is not a numerical test of an asymptotic prime distribution theorem. The ordinary proof and independent review are the mathematical validation.
