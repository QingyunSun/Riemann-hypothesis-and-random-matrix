# The accumulated singular-series correction and its exact constant

Date: 2026-09-05. Author/reviewer: Aquinas. Status: independent ordinary derivation of the refined singular-series transform and its summed correction. The transform and the continuum integral are unconditional; replacement of the two prime marginals uses ordinary RH. This note does not prove or assume a bound for the remaining quadratic covariance, and it does not replace the separate audit of all divisor-completion errors in a global reduction.

## 1. Source formula and extension to real endpoints

The primary input is Montgomery–Soundararajan, *Primes in short intervals*, arXiv:math/0409258v1, equation (47), printed page **16** (zero-based PDF page 15). It records Goldston's unconditional estimate, for positive integer \(N\),
\[
2\sum_{h=1}^N(N-h)\mathfrak S(h)
=N^2-N\log N+B_*N+O_\varepsilon(N^{1/2+\varepsilon}).
\tag{1}
\]
Here \(\mathfrak S(h)\) is the usual two-prime singular series, zero for odd \(h\); \(B_*\) is the fixed source constant. No conjectural prime-pair estimate elsewhere in the paper is being used. I checked (1) in the retained text and in the live primary PDF. The equation is on page 16, not page 17.

Define the genuine real hinge function
\[
G(y)=\sum_{h\ge1}(y-h)_+\mathfrak S(h),\qquad y\ge0.
\tag{2}
\]
It is exactly piecewise linear between consecutive integers: there is no prime or singular-series atom strictly between them. Let
\[
g(y)=\tfrac12y^2-\tfrac12y\log y+\tfrac12B_*y.
\]
On \([N,N+1]\), the difference between \(g\) and its linear interpolation is bounded by a constant times \(\sup|g''|\), and \(g''(y)=1-1/(2y)\) is bounded for \(y\ge1\). Interpolating (1) at the two integer endpoints therefore proves, for all real \(y\ge2\),
\[
\boxed{G(y)=g(y)+O_\varepsilon(y^{1/2+\varepsilon}).}
\tag{3}
\]
The interpolation error is only \(O(1)\), absorbed by the displayed remainder. This is an explicit real-endpoint extension; it does not presume that an integer theorem already controls a fractional hinge slope.

## 2. The refined transform and its sign

Let \(Y\ge4\), and let \(f\in C_c^2((0,\infty))\) have support in \([Y/2,2Y]\), with \(\|f''\|_\infty\le A_fY^{-2}\). Since the distributional second derivative of \(G\) is \(\sum_h\mathfrak S(h)\delta_h\), the exact hinge identity and two integrations by parts give
\[
\begin{aligned}
\sum_{h\text{ even}}\mathfrak S(h)f(h)
&=\int_0^\infty G(y)f''(y)\,dy\\
&=\int_0^\infty f(y)\,dy
-\frac12\int_0^\infty\frac{f(y)}y\,dy
+O_\varepsilon(A_fY^{-1/2+\varepsilon}).
\end{aligned}
\tag{4}
\]
All endpoint terms vanish because \(f,f'\) vanish outside a compact interval away from zero. The linear term makes no contribution: \(\int yf''(y)dy=0\). The logarithmic term has second derivative \((y\log y)''=1/y\), giving the **negative** coefficient \(-1/2\). The remainder estimate is exactly
\[
\int_{Y/2}^{2Y}y^{1/2+\varepsilon}|f''(y)|\,dy
\ll_\varepsilon A_fY^{-1/2+\varepsilon}.
\]
There is no extra factor two in (4): the source series itself vanishes at odd shifts. This formula also holds with any fixed proportional support interval in place of \([Y/2,2Y]\).

The coarser R25 transform absorbed the entire \(-\tfrac12\int f/y\) term into \(O(A_f)\). That is legitimate for a fixed compact packet. It is insufficient for deleting this term after summing a growing number of packets.

## 3. One packet: both prime marginals and the correction

Let \(F(m,h)\) be a smooth packet with \(m\asymp X\), \(h\asymp Y\), \(h=o(m)\), and fixed mixed derivative bounds of amplitude
\(A=(X\ell^2)^{-1}\) at scales \(X,Y\), where \(\ell=\log T\). Define
\[
J_-(m)=\int F(m,h)dh,\quad
J_+(n)=\int F(n-h,h)dh,
\]
\[
I_-(m)=\int\frac{F(m,h)}h\,dh,\quad
I_+(n)=\int\frac{F(n-h,h)}h\,dh.
\tag{5}
\]
The shifted endpoints in \(I_+,J_+\) are retained. Applying (4) at fixed \(m\), and independently at fixed \(n\), gives the exact sign structure
\[
\begin{aligned}
\mathcal M_{\mathfrak S}(F)
&:=2\sum_{\substack{m\text{ odd}\\h\text{ even}}}
F(m,h)\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\\
&=2\sum_{m\text{ odd}}\Lambda(m)J_-(m)
+2\sum_{n\text{ odd}}\Lambda(n)J_+(n)
-4\sum_{m\text{ odd}}J_-(m)
-D(F)+O_\varepsilon(\ell^{-2}Y^{-1/2+\varepsilon}),
\end{aligned}
\tag{6}
\]
where
\[
\boxed{D(F)=
\sum_{m\text{ odd}}\Lambda(m)I_-(m)
+\sum_{n\text{ odd}}\Lambda(n)I_+(n)
-2\sum_{m\text{ odd}}I_-(m).}
\tag{7}
\]
Chebyshev bounds the prime sums in the transform error by \(O(X)\); the integer row count is also \(O(X)\). This explains the normalization of the error in (6).

Consequently, whenever the other principal/flat-center terms have been combined as in R25, subtracting \(\mathcal M_{\mathfrak S}\) adds \(+D(F)\), not \(-D(F)\). This assertion identifies the correction only: the separate errors of that principal reduction must still be paid when the packets are summed.

Under RH, the odd prime-power prefix has the correct density one in the ambient real variable:
\[
\sum_{\substack{n\le x\\n\text{ odd}}}\Lambda(n)-x
=O(\sqrt x\log^2(2x)).
\tag{8}
\]
It follows from the RH estimate for \(\Psi(x)-x\) after removing only the powers of two, whose cumulative weight is \(O(\log x)\). Their removal here is explicit; higher powers of odd primes remain.

Both \(I_\pm\) have amplitude \(O(A)\), derivative \(O(A/X)\), and support of length \(O(X)\). Abel summation with (8) gives
\[
\sum_{m\text{ odd}}\Lambda(m)I_-(m)
=\int I_-(x)dx+O(X^{-1/2}),
\tag{9}
\]
and the same estimate for \(I_+\), uniformly while \(\log X\asymp\ell\). Odd-lattice summation gives
\(2\sum_{m\text{ odd}}I_-(m)=\int I_-(x)dx+O(A)\).
Finally \(\int I_+=\int I_-\) by the exact change of variables \(n=m+h\). Therefore
\[
\boxed{D(F)=\int_0^\infty\int_0^\infty
\frac{F(m,h)}h\,dh\,dm+O(X^{-1/2}).}
\tag{10}
\]
There is exactly one continuum integral left: the two prime means each have density one, and twice the odd integer lattice has density one. If \(F\ge0\), its leading correction is nonnegative.

## 4. The actual smooth partition and uniform derivative control

Here I use the precise partition communicated by the global-extension author. Fix a smooth nonincreasing function \(r:[0,\infty)\to[0,1]\), equal to one for \(t\le1\) and zero for \(t\ge2\). Put
\[
\beta(t)=r(t)-r(2t),\quad
L=T^{7/4},\quad U=T^{9/4},\quad
Y_0=\sqrt\ell,\quad R=32\ell,
\]
\[
X_i=2^iL,\qquad Y_j=2^jY_0\qquad(i,j\ge0),
\]
\[
\boxed{F_{ij}(m,h)=b_T(m)\beta(m/X_i)\beta(h/Y_j)
r(m/(2U))r(Th/(Rm))(1+h/m)^{-T},}
\tag{11}
\]
with the unchanged actual weight
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}dx.
\tag{12}
\]
The support of \(\omega\) is \([7/4,9/4]\), and \(b_T(m)=0\) for \(m\le L\). The cutoffs and all boundary derivatives vanish at their support boundaries.

Only finitely many packets are nonzero. Their support requires
\[
m\in[X_i/2,2X_i],\quad h\in[Y_j/2,2Y_j],\quad
X_i<8U,\quad Y_j<8R X_i/T.
\tag{13}
\]
In particular \(h/m\le2R/T=o(1)\), uniformly. There are \(O(\ell)\) allowed values of each index, and \(O(\ell)\) values of \(j\) per fixed \(i\).

All fixed mixed derivative bounds used in Section 3 hold with amplitude \(A_i=(X_i\ell^2)^{-1}\), uniformly in \(i,j,T\). Here is the point that prevents a hidden growing logarithmic constant. The exact integral for \(b_T\) gives \(b_T^{(a)}(m)\ll_a m^{-a-1}\ell^{-2}\). For the Pareto factor, put \(s=Th/m\). On the support \(s\le2R=o(T)\), and
\[
(1+h/m)^{-T}\le e^{-s/2}.
\]
After multiplying a fixed mixed derivative by the appropriate \(Y_j\)- and \(X_i\)-powers, its possible costs are bounded by a fixed polynomial in \(s\) times \(e^{-s/2}\). This is uniformly bounded for all \(s\ge0\). Derivatives of the upper length cutoff are also uniform: where its derivatives are nonzero, \(Th/(Rm)\) is in \([1,2]\). The fixed height cutoff has scale \(U\), and \(X_i/U<8\). These observations prove the claimed bounds even when \(Y_j\) is much larger or smaller than \(X_i/T\).

At fixed \(n\), differentiating \(F_{ij}(n-h,h)\) replaces \(\partial_h\) by \(\partial_h-\partial_m\). Since \(Y_j/X_i=o(1)\) on the support, this preserves the \(Y_j\)-scale bounds required in (4). Differentiating \(I_+\) in \(n\) uses \(\partial_m F\), preserving the \(X_i\)-scale bounds in (9). No moving endpoint is frozen in these arguments.

Fix \(0<\varepsilon<1/2\). The total singular-series transform error in (6) is bounded by
\[
\boxed{\sum_{i,j}O_\varepsilon(\ell^{-2}Y_j^{-1/2+\varepsilon})
=O_\varepsilon(\ell^{-1}Y_0^{-1/2+\varepsilon})=o(1).}
\tag{14}
\]
This uses a geometric sum over \(j\), then \(O(\ell)\) height bins. The total RH error in (10) is
\[
\boxed{O\left(\ell\sum_{i\ge0}X_i^{-1/2}\right)
=O(\ell L^{-1/2})=o(1).}
\tag{15}
\]
The weaker odd-lattice errors are also summable. Thus neither passage to the full finite partition relies on summing unquantified per-packet little-oh terms.

## 5. Sum the correction using the exact integral, not a prime approximation

Telescoping gives
\[
\sum_{i\ge0}\beta(m/X_i)=1-r(2m/L),\qquad
\sum_{j\ge0}\beta(h/Y_j)=1-r(2h/Y_0).
\tag{16}
\]
The first factor equals one wherever \(b_T(m)\ne0\). Therefore the sum of the continuum corrections is exactly
\[
C_T=\int_1^\infty b_T(m)r(m/(2U))
\int_0^\infty[1-r(2h/Y_0)]r(Th/(Rm))
(1+h/m)^{-T}\frac{dh}h\,dm.
\tag{17}
\]
The lower length transition is \([Y_0/2,Y_0]\), the upper one is \([Rm/T,2Rm/T]\), and the height transition is \([2U,4U]\). These are the actual conventions, not sharp approximations silently substituted for them.

For every \(m\) in the support of (17), set \(H_m=m/T\), \(a=Y_0/H_m\), and change variables \(t=h/H_m\). Uniformly there, \(a\le T Y_0/L\to0\), \(R\ge1\), and \(2R<T\) eventually. The inner integral is
\[
\int_0^\infty[1-r(2t/a)]r(t/R)(1+t/T)^{-T}\frac{dt}t
=\log(1/a)+O(1).
\tag{18}
\]
One direct proof compares with \(\int_a^1dt/t\). The lower transition costs at most \(\log2\). On \([a,1]\), the inequality \(0\le1-(1+t/T)^{-T}\le t\) costs at most one. On \([1,2R]\), the Pareto factor is at most \(e^{-t/2}\), so the remaining integral is bounded by \(\int_1^\infty e^{-t/2}dt/t\). All bounds are independent of \(m,T\); the exponential is only an upper bound, not a replacement of the kernel.

Write
\[
M_0=\int\omega(u)du,\qquad M_1=\int\omega(u)(u-1)du.
\tag{19}
\]
Tonelli and elementary integration of the exact (12) give the two useful identities
\[
\boxed{\int_1^\infty b_T(m)dm=\frac{T}{T-1}\frac{M_0}{\ell},}
\]
\[
\boxed{\int_1^\infty b_T(m)\log m\,dm
=\frac{T}{T-1}\int u\omega(u)du
+\frac{T}{(T-1)^2\ell}M_0.}
\tag{20}
\]
For example the inner integral for the second identity is
\(\int_x^\infty m^{-T}\log m\,dm
=x^{1-T}[\log x/(T-1)+(T-1)^{-2}]\).
This retains both the endpoint term and the second denominator.

The height cutoff can be removed from these logarithmic moments with an exponentially small error. For \(m>U\),
\[
b_T(m)\le\frac{T\|\omega\|_\infty}{(T-1)\ell^2}
U^{T-1}m^{-T}.
\tag{21}
\]
Integrating over \(m>2U\), including the factor
\(|\log m-\ell-\log Y_0|\), costs \(O_\omega(2^{-T}/\ell)\). In particular no prime or continuum tail beyond \(U\) was simply deleted.

Combining (18)–(21) gives
\[
C_T=\frac{T}{T-1}
\left(M_1-\frac{\log Y_0}{\ell}M_0\right)
+\frac{T M_0}{(T-1)^2\ell}+O_\omega(\ell^{-1}),
\]
and hence
\[
\boxed{C_T=M_1-\frac{\log Y_0}{\ell}M_0+O_\omega(\ell^{-1})
=M_1+O_\omega\left(\frac{\log\ell}{\ell}\right).}
\tag{22}
\]
The stated value \(Y_0=\sqrt\ell\) was used only in the final equality. No PNT or RH is needed for (17)–(22).

By (10) and (15), the actual discrete prime-marginal correction satisfies under RH
\[
\boxed{\sum_{i,j}D(F_{ij})
=M_1+O_\omega\left(\frac{\log\ell}{\ell}+\ell L^{-1/2}\right).}
\tag{23}
\]
The separately accumulated transform error is (14).

## 6. Constant, sign, and the precise remaining scope

For the programme's fixed bump \(\omega(u)=\psi((u-2)/\epsilon)\), the autocorrelation \(\psi\) is even. Thus \(\int(u-2)\omega(u)du=0\), and
\[
\boxed{M_1=M_0=\epsilon\int\psi=\epsilon m_0=M.}
\tag{24}
\]
This is the positive constant predicted for the total singular-series correction. No decimal quadrature or interval certificate is needed for the equality. The correction is additional to any previously separated diagonal constant.

For clarity about that last normalization: the frozen R21 identity is \(\overline V_T=M_0+\mathcal E_T+o(1)\). If the separately audited parity reduction is inserted, and if the global divisor-completion proof establishes
\(\mathcal E_T=\sum_{i,j}Z_{Q_j}^{(2)}(F_{ij})+\sum_{i,j}D(F_{ij})+o(1)\), then the assembled identity is
\[
\overline V_T=M_0+M_1+\sum_{i,j}Z_{Q_j}^{(2)}(F_{ij})+o(1).
\tag{25}
\]
For the symmetric bump this has constant \(2M\). This is a **conditional assembly check**, not a proof here of the global covariance reduction, and certainly not an assertion that the covariance sum tends to zero. Confusing the new truncated covariance with the original untruncated centered prime-pair error would lose one copy of \(M\).

The derivation accepts the refined transform, its sign, real endpoints, both-marginal normalization, uniform partition errors and total correction. It leaves the following separate: all \(Q_j\)-dependent primitive/complementary errors, removal of discarded arithmetic lengths and height tails from the original quadratic statistic, and any strict estimate for the remaining signed covariance. No choice of \(Q_j\) or covariance bound was needed to establish (23).

## 7. Source and reproduction record

- Montgomery–Soundararajan, [*Primes in short intervals*, arXiv:math/0409258v1](https://arxiv.org/pdf/math/0409258v1), equation (47), printed page 16: the unconditional hinge asymptotic with its \(h^{1/2+\varepsilon}\) remainder. The equation is credited there to Goldston. The source's conditional prime-correlation assumptions are not imported.
- Schoenfeld, [*Sharper bounds for the Chebyshev functions. II*](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), Theorem 10, equation (6.2), printed page 337: ordinary RH control of \(\Psi-x\), including prime powers.
- Frozen programme definitions: R21 exact \(b_T\) and diagonal constant; R25 joint-main cancellation Sections 3–6. The latter is used for identifying the sign of the correction, not as a proof that its per-packet error already sums globally.

The source/dependency receipt pins the bytes read. The small adjacent checker concerns derivative signs, exact moment algebra and rational exponents only; it contains no prime, divisor, or parameter scan. Independent ordinary proof review remains the mathematical validation.
