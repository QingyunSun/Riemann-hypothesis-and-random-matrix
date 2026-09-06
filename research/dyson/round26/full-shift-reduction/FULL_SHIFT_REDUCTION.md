# A global scale-dependent Möbius–prime reduction, retaining the singular-series constant

Date: 2026-09-05. Author: Euclid. Status: ordinary proof submitted for independent review. The main theorem assumes ordinary RH. The coefficient identities, smooth completions, singular-series transform and absolute truncations used in its proof are unconditional. This extends the frozen R25 compact-packet reduction without changing it. No novelty, strict variance bound or AH refutation is asserted.

## 1. The actual global target and a finite, explicitly defined covariance

Use the unchanged R21/R22 notation
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},\quad
W_T(x)=\omega(\log x/\ell),
\]
\[
b(m)=\frac{Tm^{-T}}{\ell^2}\int_1^mW_T(x)x^{T-2}dx,
\qquad k(m,h)=\left(\frac m{m+h}\right)^T.
\tag{1}
\]
The fixed \(\omega\) is nonnegative and smooth, supported in \([7/4,9/4]\). Initially put
\[
M_0=\int\omega(u)\,du,\qquad M_1=\int(u-1)\omega(u)\,du.
\tag{2}
\]
For the actual symmetric weight \(\omega(u)=\psi((u-2)/\varepsilon)\), with \(\varepsilon=1/4\) and even \(\psi\), \(M_1=M_0=:M\). We keep these constants distinct until the last step.

The full parity-adjusted remainder is
\[
\mathcal Q_{2,T}
=2\sum_{\substack{m\ {\rm odd}\\h\ge2,\ h\ {\rm even}}}
b(m)k(m,h)
\{\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\}.
\tag{3}
\]
All prime powers remain. The separately reviewed R21/R22 reductions give, under RH,
\[
\overline V_T=M_0+\mathcal Q_{2,T}+o(1).
\tag{4}
\]
Here \(\overline V_T\) is the actual exponential-length averaged variance, with its exact continuous center. This note proves a new reduction of (3), rather than assuming the sign of any of its coefficients.

Choose once and for all a smooth nonincreasing function \(r:[0,\infty)\to[0,1]\), equal to \(1\) on \([0,1]\) and \(0\) on \([2,\infty)\). Put
\[
\beta(t)=r(t)-r(2t),\qquad Y_0=\sqrt\ell,\qquad R=32\ell,
\]
\[
X_i=2^iL,\qquad Y_j=2^jY_0,\qquad Q_j=Y_j^{2/3},
\quad i,j\ge0.
\tag{5}
\]
All cutoffs are real; a divisor condition \(d>Q_j\) always means exactly that inequality for integer \(d\). Define
\[
c_{Q_j}(m)=\sum_{\substack{d\mid m\\d>Q_j}}
\mu(d)\log(m/d),\quad m\ {\rm odd},
\]
\[
c_T(m,h)=\sum_{j\ge0}\beta(h/Y_j)c_{Q_j}(m).
\tag{6}
\]
Finally define the actual scale-dependent, parity-centered covariance
\[
\boxed{
\mathcal Z_T
=2\sum_{\substack{m\ {\rm odd}\\h\ge2,\ h\ {\rm even}}}
b(m)r(m/(2U))\,r(Th/(Rm))\,k(m,h)
\,c_T(m,h)[\Lambda(m+h)-2].}
\tag{7}
\]
This is a finite arithmetic expression: \(m<4U\), \(h<2Rm/T\), and only finitely many \(j\)'s have \(\beta(h/Y_j)\ne0\). The factor \(c_T\) already contains the smooth lower shift cutoff. No coefficient of the genuine von Mangoldt function has been replaced by a generic sequence.

**Theorem 1.** Under ordinary RH, for the fixed choices (1), (5),
\[
\boxed{\mathcal Q_{2,T}=\mathcal Z_T+M_1+o(1).}
\tag{8}
\]
Consequently the actual symmetric test satisfies
\[
\boxed{\overline V_T=\mathcal Z_T+2M+o(1).}
\tag{9}
\]
The proof below provides summable bounds; in particular its errors in (8) are \(O_\omega(\ell^{-1/2})\), with constants also depending on \(r\) and fixed derivative orders. Equation (4) contributes its separately established \(o(1)\) when passing to (9).

The deterministic \(M_1\) term is essential. Discarding an \(O(\ell^{-2})\) contribution separately in each of \(O(\ell^2)\) height/shift packets would not prove (8).

## 2. An exact smooth partition and uniform derivative bounds

Define the packet
\[
F_{ij}(m,h)=b(m)\beta(m/X_i)\beta(h/Y_j)
r(m/(2U))\,r(Th/(Rm))\,k(m,h).
\tag{10}
\]
It is nonnegative. Its support has \(m\asymp X_i\), \(h\asymp Y_j\), with ratios in \((1/2,2)\). The exact telescoping identities are
\[
\sum_{i\ge0}\beta(m/X_i)=1\quad(m>L),
\]
\[
\sum_{j\ge0}\beta(h/Y_j)=1-r(2h/Y_0).
\tag{11}
\]
The first follows from \(\sum_{i=0}^N\beta(m/(2^iL))
=r(m/(2^NL))-r(2m/L)\) and \(m>L\).

Nonzero packets must satisfy
\[
X_i<8U,\qquad Y_j<8R X_i/T.
\tag{12}
\]
Indeed \(m<4U\), \(m<2X_i\), \(h>Y_j/2\), and the upper shift cutoff requires \(h<2Rm/T\). There are \(O(\ell)\) height indices and at most \(O(\ell)\) shift indices for each height. Only these finitely many indices will be summed. Bounds of the form \(X\asymp L\) at the first block and \(X\le8U\) at the last block are kept explicitly; we do not falsely require \(\log X/\ell\) to lie in the exact old closed interval at every endpoint.

Write \(X=X_i,Y=Y_j,H=X/T,A=(X\ell^2)^{-1}\). For every fixed pair of derivative orders \(a,b\),
\[
|\partial_m^a\partial_h^bF_{ij}(m,h)|
\ll_{a,b} A X^{-a}Y^{-b}.
\tag{13}
\]
The constants are uniform in \(i,j,T\). To verify this even when \(Y/H\) grows, first use the exact identity
\[
b(m)=\frac{T}{m\ell^2}
\int_0^1\omega((\log m+\log u)/\ell)u^{T-2}du
\]
to obtain \(b^{(a)}(m)\ll_a m^{-a-1}\ell^{-2}\). With \(m=Xv,h=Yz\), the Pareto factor is
\[
(1+(Y/H)z/(Tv))^{-T}.
\]
On the support, \(Y/H\le8R=O(\ell)\), whereas \(T\to\infty\). Each scaled derivative is bounded by a fixed polynomial in \(Y/H\) times \(\exp(-cY/H)\). These products are uniformly bounded for each fixed derivative order. The factor \(r(Th/(Rm))\) and its derivatives have argument \((Y/(RH))z/v\); on their support this ratio is bounded by a fixed constant. The height cutoff has derivatives on scale \(U\), and \(X/U\le8\). This proves (13), including mixed derivatives, without an unrecorded power of \(\ell\).

At fixed \(n=m+h\), derivatives in \(h\) are at scale \(Y\); derivatives in \(n\) with \(h\) fixed are at scale \(X\). Since (12) implies \(Y/X=O(\ell/T)\), \(m,n\asymp X\) uniformly. All boundary derivatives vanish. Multiplying by \(\log((n-h)/d)\), with \(d\le Q=Y^{2/3}\), adds at most \(O(\log X)\) to the amplitude. In fact \(Q<X/2\) eventually on every nonzero packet, uniformly in (12).

## 3. Absolute removal of the missing small shifts and both infinite tails

Let \(q_2(m,h)\) denote the expression in braces in (3). For \(1\le K\le L\), the same unconditional dimension-two sieve used in the reviewed R22 small-shift note gives
\[
2\sum_{\substack{m\ {\rm odd}\\2\le h\le K,\ h\ {\rm even}}}
b(m)k(m,h)|q_2(m,h)|
\ll \frac K\ell+K\ell L^{-1/2}+K2^{-T}.
\tag{14}
\]
This is a bound for \(q_2\), not an unsupported use of the old \(a_ma_{m+h}-c_h\) coefficient. To check it directly, use
\[
|q_2(m,h)|\le
\Lambda(m)\Lambda(m+h)+
\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)+2].
\]
On a block \(X<m\le2X\), the cited uniform upper sieve, including higher prime powers, gives
\[
\sum_{X<m\le2X}\Lambda(m)\Lambda(m+h)
\ll X\mathfrak S(h)+\sqrt X\log^3X
\quad(1\le h\le X).
\]
Also \(\sum_{h\le K}\mathfrak S(h)\le K\) and \(\Psi(3X)\ll X\). Summing over \(h\le K\), then using \(b\ll1/(X\ell^2)\), gives \(O(K/\ell+K\ell L^{-1/2})\) over \(O(\ell)\) height blocks. For \(m>2U\) and \(h\le K\le L\), one has \(h<m/2\), so the complete small-shift absolute sum is \(O(K\log^2(2m))\). The exact \(b\)-tail integral then gives \(O(K2^{-T})\), including its first integer term. Thus (14) applies to any subset or smooth subweight in that small range. At \(K=\lceil Y_0\rceil\), it is \(O(\ell^{-1/2})\).

Here are explicit elementary tail bounds sufficient for this proof. For \(T\) sufficiently large,
\[
2\sum_{\substack{m>2U\\h\ge1}}
b(m)k(m,h)|q_2(m,h)|\ll U2^{-T}.
\tag{15}
\]
For this estimate it is harmless to define \(q_2\) for every \(m,h\) using the bound just displayed. The exact tail is
\(b(m)\ll U^{T-1}m^{-T}/\ell^2\).
The full shift sum of the upper bound for \(|q_2|\) is
\[
\ll (m/T)\log^2(2m).
\]
Indeed \(k(m,h)\log^2(2(m+h))\) is decreasing for \(T\ge4,m\ge L\). Integral comparison handles the integer sum; partial summation with
\(\sum_{h\le y}\mathfrak S(h)\le y\) handles the singular-series sum. The continuous integrals, after \(1+h/m=t\), are bounded by \(m\log^2(2m)/T\). Integral comparison for the remaining \(m^{1-T}\log^2(2m)\) series, including its first integer term, proves (15). The condition \(2U\ge T\) controls that term uniformly.

The removed upper length tail on \(L<m\le4U\) satisfies
\[
2\sum_{\substack{L<m\le4U\\h>Rm/T}}
b(m)k(m,h)|q_2(m,h)|
\ll \frac{RU}{T}e^{-R/4}=o(1).
\tag{16}
\]
To retain the cutoff endpoint in the singular-series sum, partial summation bounds it by
\(a\,g(a)+\int_a^\infty g(y)dy\), where \(a=Rm/T\) and
\(g(y)=k(m,y)\log^2(2(m+y))\).
Together with the unweighted integer sum this is
\(O((Rm/T)\log^2(2m)e^{-R/4})\), since \(R/T\to0\). Multiplication by \(b\) and summation over \(m\le4U\) proves (16). With \(R=32\ell\), the right side is \(O(\ell T^{-27/4})\).

All summations used to justify these upper bounds are absolutely convergent. In particular, the global object (3) is well defined. By (11), (14)–(16),
\[
\mathcal Q_{2,T}=\sum_{i,j}\mathcal P_{ij}+O(\ell^{-1/2}),
\]
\[
\mathcal P_{ij}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}F_{ij}(m,h)q_2(m,h).
\tag{17}
\]
No sharp cutoff has been differentiated: the partition and the upper/height cutoffs are smooth, and their omitted parts were bounded separately.

## 4. The stronger unconditional singular-series transform

Let
\[
B_{\mathfrak S}(y)=\sum_{h\ge1}(y-h)_+\mathfrak S(h).
\]
Montgomery–Soundararajan, arXiv:math/0409258v1, printed page 16, equation (47), records the unconditional estimate, for integer \(N\),
\[
2B_{\mathfrak S}(N)
=N^2-N\log N+B N+O_\nu(N^{1/2+\nu})
\quad(\nu>0),
\tag{18}
\]
where \(B\) is a fixed constant. No conditional prime-pair hypothesis in that paper is being used.

The same formula holds for every real \(y\ge1\). The left side is exactly the linear interpolation of its integer values. The second derivative of
\(y^2-y\log y+B y\) is \(2-1/y=O(1)\) on \([1,\infty)\), so replacing its interpolation by its real value costs only \(O(1)\). The interpolated error is still \(O_\nu(y^{1/2+\nu})\). This handles real endpoints without assuming differentiability of the remainder.

For any smooth compact \(f\) on a fixed ratio interval \((Y/2,2Y)\), of amplitude \(A_f\) and derivative scale \(Y\), the exact hinge identity and two integrations by parts now give
\[
\boxed{
\sum_{h\ {\rm even}}\mathfrak S(h)f(h)
=\int f(h)dh-\frac12\int\frac{f(h)}h\,dh
+O_\nu(A_fY^{-1/2+\nu}).}
\tag{19}
\]
The sum over even \(h\) is the full sum because \(\mathfrak S(h)=0\) on odd shifts. The \(By\) term is killed by \(\int yf''=0\). The quadratic and logarithmic terms give
\(\frac12\int y^2f''=\int f\) and
\(\int y\log y\,f''=\int f/y\).
The remainder is bounded by
\(\int O(y^{1/2+\nu})|f''(y)|dy\); its derivatives are never invoked.

We use the fixed value \(\nu=1/4\). The correction in (19) is not an error to be discarded packet by packet.

## 5. A uniform variable-scale local reduction

Fix a nonzero packet and abbreviate \(F=F_{ij}\), \(X=X_i,Y=Y_j,Q=Y^{2/3}\). Put
\[
J_-(m)=\int F(m,h)dh,\qquad J_+(n)=\int F(n-h,h)dh,
\]
\[
I_-(m)=\int F(m,h)\frac{dh}{h},\qquad
I_+(n)=\int F(n-h,h)\frac{dh}{h}.
\tag{20}
\]
Their amplitudes are \(O(Y/(X\ell^2))\) and \(O(1/(X\ell^2))\), respectively, with derivative scale \(X\), uniformly in the packet.

Use the exact five-term divisor partition from R25 with this \(F,Q\):
\[
\mathcal P_{ij}=\mathcal B_Q+\mathcal N_Q+\mathcal A_Q
+\mathcal C_Q-\mathcal M_{\mathfrak S}.
\tag{21}
\]
All its actual masks \(1_{(n,d)=1}\), \(1_{(h,d)=1}\), the primitive factor \(1/\varphi(d)\), and the sharp divisor bounds are unchanged. We give the uniform error ledger explicitly to avoid extrapolating a fixed-power-\(Q\) theorem to polylogarithmic \(Q\).

Poisson summation for a smooth weight of amplitude \(A_f\) and scale \(Y\), on an even lattice \(2s\mathbb Z\), gives for every fixed integer \(j\ge1\),
\[
\sum_{h\in2s\mathbb Z}f(h)
=\frac1{2s}\int f+O_j(A_f(s/Y)^j),\quad s\le Y.
\tag{22}
\]
The mean-zero primitive discrepancy and Chebyshev therefore give, with \(J=16\),
\[
\mathcal B_Q\ll
\frac{Q}{\log X}(Q/Y)^{16}
=\frac{Y^{-14/3}}{\log X}.
\tag{23}
\]
For the actual nonprimitive term, \(n=p^a\), \(a\ge2\), and \(p\mid h\). The number of even shifts \(h\in(Y/2,2Y)\) divisible by \(p\) is \(O(Y/p)\), including the empty range \(p>Y\). The divisor coefficient is charged once by \(\tau(n-h)\log(2X)\), and \(\Lambda(n)=\log p\). Thus, for \(\eta=1/100\),
\[
\mathcal N_Q\ll_\eta X^\eta Y/X.
\tag{24}
\]
This uses no comparison between \(Y\) and \(\sqrt X\).

For \(\mathcal A_Q\), apply (22) to its primitive \(h\)-mask with fixed order \(j=36\), before summing over \(d\). The \(1/\varphi(d)\) prefactor and
\(\sum_{d\le Q}\tau(d)^2/d\ll\log^4(2Q)\) give
\[
\mathcal A_Q
=\sum_{n\ {\rm odd}}\Lambda(n)
  \int F(n-h,h)a_Q(n-h)dh
+O\!\left(Y^{-12}\log^3X+\frac{Y\log X}{X}\right),
\]
\[
a_Q(m)=\sum_{\substack{d\le Q\\d\ {\rm odd}}}
\frac{\mu(d)}d\log(m/d).
\tag{25}
\]
The second error is the removed nonunit prime-power mean: use
\(\sum_{d\le Q,p\mid d}d^{-1}\ll\log(2Q)/p\).
It must not be replaced by a new convention for the principal.

There is an exact flat-center identity
\[
\mathcal C_Q=\mathcal Z_{ij}^{(2)}
+4\sum_{m\ {\rm odd}}c_Q(m)\sum_{h\ {\rm even}}F(m,h),
\]
where \(\mathcal Z_{ij}^{(2)}=2\sum_{\rm odd,even}F c_Q(\Lambda(m+h)-2)\).
Since \(\sum_{m\asymp X}|c_Q(m)|\ll X\log^2X\), pure even-lattice completion with order \(4\) gives
\[
\mathcal C_Q=\mathcal Z_{ij}^{(2)}
+\mathcal L_Q^0+O(Y^{-4}),\qquad
\mathcal L_Q^0=2\sum_{m\ {\rm odd}}c_Q(m)J_-(m).
\tag{26}
\]
No primitive complementary-cofactor mask is introduced; no condition \(X/Q<Y\) is needed.

Completing the odd cofactor \(m=dr\) on its actual scale \(X/d\), with the \(d/X\) saving from two derivatives, gives
\[
\mathcal L_Q^0
=2\sum_{m\ {\rm odd}}\Lambda(m)J_-(m)
-\int J_-(m)a_Q(m)dm
+O\!\left(\frac{YQ^2}{X^2\log X}\right).
\tag{27}
\]
All moving support endpoints are smooth. The finite identity \(\Lambda=\mu*\log\), including \(m=1\), underlies (26)–(27); the support here has \(m>L\).

Under ordinary RH, Soundararajan's Möbius bound on printed page 1 of arXiv:0705.0723v2 gives
\[
a_Q(m)=2+e_Q(m),\quad
e_Q(m)\ll Q^{-1/2+\epsilon}\log X,\quad
e_Q'(m)\ll Q^{-1/2+\epsilon}/X
\tag{28}
\]
for any fixed \(\epsilon>0\). This remains uniform at \(Q=Y^{2/3}\ge\ell^{1/3}\). The odd Euler product is
\(1/[(1-2^{-s})\zeta(s)]=2(s-1)+O((s-1)^2)\);
odd Möbius partial sums follow from
\(M_{\rm odd}(x)=\sum_{a\ge0}M(x/2^a)\), so no GRH is used.

Combine (25) and (27) before bounding \(e_Q\). Its entire contribution is
\[
\sum_{n\ {\rm odd}}\Lambda(n)G(n)-\int G(y)dy,\qquad
G(n)=\int F(n-h,h)e_Q(n-h)dh.
\]
Its amplitude and total variation are
\(O(YQ^{-1/2+\epsilon}\log X/(X\ell^2))\).
The RH bound for \(\Psi(x)-x\), with the powers of \(2\) removed at cost \(O(\log x)\), gives the centered error
\[
O_\epsilon\!\left(\frac{Y}{\sqrt X}
Q^{-1/2+\epsilon}\log X\right).
\tag{29}
\]
The absolute size of the uncentered \(e_Q\) main is not estimated separately.

Applying (19) to both exact singular-series marginals now proves
\[
\boxed{
\mathcal P_{ij}
=\mathcal Z_{ij}^{(2)}+\mathcal D_{ij}+\mathcal R_{ij},}
\]
\[
\mathcal D_{ij}
=\sum_{m\ {\rm odd}}\Lambda(m)I_-(m)
+\sum_{n\ {\rm odd}}\Lambda(n)I_+(n)
-2\sum_{m\ {\rm odd}}I_-(m),
\tag{30}
\]
where, with \(\epsilon=1/100,\nu=1/4\),
\[
\begin{aligned}
|\mathcal R_{ij}|\ll{}&
Y^{-14/3}/\log X+X^{1/100}Y/X
+Y^{-12}\log^3X+Y\log X/X+Y^{-4}\\
&+\frac{Y^{7/3}}{X^2\log X}
+\frac{Y^{101/150}\log X}{\sqrt X}
+\ell^{-2}Y^{-1/4}
+\frac{Y}{X^2\ell^2}.
\end{aligned}
\tag{31}
\]
The last term is the odd lattice completion of \(J_-\). The singular-series remainder has become \(\ell^{-2}Y^{-1/4}\), rather than an unsummable bound of order \(\ell^{-2}\) per packet.

All constants in (31) are uniform in the finite family (12). Although orders \(36\), \(16\) and \(4\) appear in different applications of (22), each is fixed. Their seminorms are controlled by (13); none grows with \(T\).

## 6. Summing the entire error ledger

There are \(O(\ell)\) height blocks, \(\log X\asymp\ell\), and \(Y\) is dyadic between \(Y_0\) and \(8RX/T\). Negative powers of \(Y\) sum geometrically from \(Y_0\); positive powers sum geometrically from the last allowed scale. Thus the respective total bounds from (31) are
\[
\begin{array}{c|c}
\text{term}&\text{bound after summing all nonzero packets}\\ \hline
Y^{-14/3}/\log X & O(\ell^{-7/3})\\
X^{1/100}Y/X & O(R\ell\, U^{1/100}/T)\\
Y^{-12}\log^3X & O(\ell^4Y_0^{-12})=O(\ell^{-2})\\
Y\log X/X & O(R\ell^2/T)\\
Y^{-4} & O(\ell Y_0^{-4})=O(\ell^{-1})\\
Y^{7/3}/(X^2\log X)
& O(R^{7/3}T^{-19/12}/\ell)\\
Y^{101/150}\log X/\sqrt X
& O(R^{101/150}\ell T^{-17/60})\\
\ell^{-2}Y^{-1/4}
& O(\ell^{-1}Y_0^{-1/4})=O(\ell^{-9/8})\\
Y/(X^2\ell^2)&O(R/(TL\ell^2)).
\end{array}
\tag{32}
\]
Fixed factors such as \(8\) in (12) are absorbed by constants. For the sixth row, the height sum is geometric in \(X^{1/3}\):
\[
(X/T)^{7/3}/X^2=X^{1/3}/T^{7/3}
\]
and \(U^{1/3}/T^{7/3}=T^{-19/12}\). For the seventh row it is geometric in \(X^{13/75}\):
\[
U^{13/75}/T^{101/150}=T^{-17/60}.
\]
For the final row it is geometric in \(X^{-1}\). These checks prevent losing a height factor at the power endpoints. The deliberately looser second and fourth rows still tend to zero. Every term is \(o(1)\), and their sum is \(O(\ell^{-1})\).

The RH odd-prime bound and the smooth \(X\)-scale of \(I_\pm\) give independently
\[
\mathcal D_{ij}
=\iint F_{ij}(m,h)\frac{dh\,dm}{h}+O(X_i^{-1/2}).
\tag{33}
\]
Indeed each odd-prime singleton differs from its continuous integral by
\(O(\sqrt X\log^2X\cdot (X\ell^2)^{-1})\); the odd integer term has the smaller Poisson error \(O((X^2\ell^2)^{-1})\). The two continuous integrals \(\int I_-\) and \(\int I_+\) agree by Fubini. There are \(O(\ell)\) shift blocks for each height, and \(\sum_i X_i^{-1/2}\ll L^{-1/2}\), so the total error in (33) is \(O(\ell L^{-1/2})\).

By the exact height partition and the definition (6),
\(\sum_{i,j}\mathcal Z_{ij}^{(2)}=\mathcal Z_T\). The total deterministic correction is
\[
\mathcal I_T=
\iint b(m)r(m/(2U))k(m,h)
r(Th/(Rm))[1-r(2h/Y_0)]\frac{dh\,dm}{h}.
\tag{34}
\]
Equations (17), (30)–(33) prove
\[
\mathcal Q_{2,T}=\mathcal Z_T+\mathcal I_T+O(\ell^{-1/2}).
\tag{35}
\]

## 7. Evaluation of the accumulated correction

For \(L\le m\le4U\), put \(H_m=m/T\). The inner integral in (34) is exactly
\[
J_T(m)=\int_0^\infty
r(z/R)(1+z/T)^{-T}
[1-r(2H_m z/Y_0)]\,\frac{dz}{z}.
\tag{36}
\]
Uniformly in this full range,
\[
J_T(m)=\log(H_m/Y_0)+O(1).
\tag{37}
\]
To prove it, let \(\delta=Y_0/H_m\to0\) uniformly. The lower cutoff equals zero for \(z\le\delta/2\) and one for \(z\ge\delta\). Its difference from the indicator \(z\ge\delta\) contributes at most \(\log2\). On \(\delta\le z\le1\), \(0\le1-(1+z/T)^{-T}\le z\), so the difference from the logarithmic integral is bounded. The integral on \(z\ge1\) is uniformly bounded: for \(z\le T\), the kernel is at most \(e^{-z/2}\); for \(z\ge T\), substitution \(u=1+z/T\) bounds the tail by a fixed multiple of \(2^{-T}\). The upper cutoff can only decrease that uniformly bounded tail. This proves (37), retaining the true Pareto function and both smooth endpoints.

The exact integral for \(b\) and the mean value theorem give, uniformly for \(m\in[L,4U]\),
\[
b(m)=\frac{W_T(m)}{m\ell^2}
+O_\omega\!\left(\frac1{mT\ell^2}\right).
\tag{38}
\]
One can retain the slightly more precise factor \(T/(T-1)\); its difference is included in this error. Since \(J_T(m)=O(\ell)\), its integrated error in (34) is \(O(T^{-1})\). On the support of \(W_T\), \(m\le U\), and hence \(r(m/(2U))=1\). It follows that
\[
\begin{aligned}
\mathcal I_T
&=\frac1{\ell^2}\int_L^U
\frac{W_T(m)}m
[\log m-\ell-\log Y_0+O(1)]\,dm+O(T^{-1})\\
&=M_1-\frac{\log Y_0}{\ell}M_0
+O(\ell^{-1}+T^{-1})\\
&=M_1+O(\log\ell/\ell).
\end{aligned}
\tag{39}
\]
Combining (35) and (39) proves (8), with the stated \(O(\ell^{-1/2})\) error. The already reviewed exact variance reduction (4) proves (9).

The constant in (39) comes from the entire range \(Y_0\ll h\ll m/T\), not only from the natural-length packet \(h\asymp m/T\). This is why the frozen R25 theorem could have an \(o(1)\) error for each fixed compact packet while the global problem retains \(M_1\).

## 8. Precisely what this does and does not establish

Equation (9) is an actual arithmetic reduction across the whole height and length range of the fixed variance observable. The covariance in (7) is finite, has explicitly specified smooth cutoffs, retains every prime power and uses the exact divisor identity at each physical shift scale. Its scale-dependent cutoff \(Q_j=Y_j^{2/3}\) is part of the result; it is not interchangeable with an old fixed-\(Q\) family.

The strict sufficient target \(\liminf\overline V_T\le1\) is now
\[
\liminf_{T\to\infty}\mathcal Z_T\le1-2M
\tag{40}
\]
for the symmetric fixed weight. No bound of that strength is proved here. Under the previously stated AH-Pairs prediction, the new covariance would tend to \(A-2M\); under the full GUE prediction it would tend to \(-M\). Neither prediction is asserted as a theorem about the actual zeta zeros. In particular an expectation that the covariance should simply tend to zero would discard the singular-series fluctuation just computed.

Only ordinary RH is used: first in the Möbius partial sums, then in the centered prime singleton estimates and the inherited actual variance transfer. There is no phase-twisted Siegel–Walfisz assumption, GRH, or invocation of the 186 distribution theorem for a two-prime covariance. The remaining signed estimate is still a genuine arithmetic problem.

## 9. Primary sources, dependencies and validation scope

The principal source refinement is Montgomery–Soundararajan, *Primes in short intervals*, [arXiv:math/0409258v1](https://arxiv.org/pdf/math/0409258v1), printed page 16, equation (47). It is the unconditional Goldston singular-series estimate recorded there. Its real-argument extension is proved in Section 4, rather than assumed from the printed integer formula. The retained PDF/text and page image are hash-pinned.

The RH Möbius source is Soundararajan, *Partial sums of the Möbius function*, [arXiv:0705.0723v2](https://arxiv.org/pdf/0705.0723v2), printed page 1, equation (1) and Theorem 1. The RH full-prime-power bound is Schoenfeld, Theorem 10, equation (6.2), printed page 337 of [Math. Comp. 30 (1976)](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf).

The source manifest pins the frozen R25 proof and the exact R21/R22 variance/parity/small-shift dependencies. The changed polylogarithmic scale, enlarged packet count, primitive/nonprimitive masks, real cutoffs and infinite tails are checked explicitly above. No old source file is modified.

The bounded checker verifies rational exponent arithmetic and exact finite partition/hinge identities only. It does not sample large primes, certify an unproved covariance sign, or replace the ordinary proof and independent mathematical review.
