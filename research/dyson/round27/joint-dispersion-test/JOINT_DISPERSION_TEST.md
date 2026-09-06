# Joint cofactor cancellation: a removable divisor band and the remaining prime matrix estimate

Date: 2026-09-05. Author: Euclid. Status: ordinary proof submitted for independent review. The medium-band removal uses ordinary RH. The exact bilinear and Gram identities and the explicitly identified application of the 186 convolution-distribution theorem are unconditional. The matrix estimate required for a further gain is **not proved**.

## 1. Scope: a central component of the actual global covariance

The frozen R26 theorem gives under RH
\[
\overline V_T=\mathcal Z_T+2M+o(1).
\tag{1}
\]
Together with the inherited nonnegativity and RH upper bound for the actual variance, this already implies
\[
-2M\le\liminf\mathcal Z_T\le\limsup\mathcal Z_T\le A-2M.
\tag{2}
\]
Thus the global signed aggregate is \(O(1)\). That bound is inherited; it is not a new gain from this note. The strict target remains, for example,
\(\liminf\mathcal Z_T\le1-2M<A-2M\).

Here we study an actual central compact block, keeping its original prime coefficients. Set
\[
X=T^2,\quad Y=X^{1/2}=T,\quad \ell=\log T,
\]
\[
F(m,h)=b_T(m)\chi(m/X)V(h/Y)
\left(\frac m{m+h}\right)^T,
\tag{3}
\]
where \(\chi,V\in C_c^\infty((1,2))\) are fixed real functions and \(b_T\) is the unchanged R21/R26 kernel. This also applies uniformly to the corresponding central R26 blocks with \(X_i\asymp T^2,Y_j\asymp T\), after fixed-ratio rescaling of their smooth profiles. The high and height cutoffs there are identically one on such a block for sufficiently large \(T\).

Write
\[
c_Q(m)=\sum_{\substack{d\mid m\\d>Q}}\mu(d)\log(m/d),
\quad
Z(Q)=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)c_Q(m)[\Lambda(m+h)-2].
\tag{4}
\]
All sums are finite. We do not extrapolate this central-block analysis to the lowest R26 scale \(Y=\sqrt\ell,Q=\ell^{1/3}\). In particular \(\log D\asymp\log X\), or a narrow physical Fourier arc after cofactor rescaling, is not assumed uniformly over the whole global expression.

## 2. A genuine removable component: move the central divisor cutoff towards \(Y\)

Take
\[
Q_1=X^{1/3},\qquad Q_2=X^{49/100}.
\tag{5}
\]
The entire medium-divisor band is exactly
\[
\begin{aligned}
\mathcal W
&:=Z(Q_1)-Z(Q_2)\\
&=2\sum_{\substack{Q_1<d\le Q_2\\d\ {\rm odd}}}\mu(d)
\sum_{k\ {\rm odd}}\log k
\sum_{h\ {\rm even}}F(dk,h)[\Lambda(dk+h)-2].
\end{aligned}
\tag{6}
\]
The \(k\)-sum is preserved before any prime estimate is made. There is no artificial condition \((d,k)=1\); its product support and every divisor endpoint remain exact.

**Lemma 1.** Under RH,
\[
\boxed{Z(Q_1)-Z(Q_2)\ll X^{-1/100}(\log X)^3=o(1).}
\tag{7}
\]
This is a bound for the actual signed medium-band contribution, not for its absolute summands.

**Proof.** Apply the R25 primitive/nonprimitive split only to \(Q_1<d\le Q_2\). Let
\[
a_{\rm band}(m)=
\sum_{\substack{Q_1<d\le Q_2\\d\ {\rm odd}}}
\frac{\mu(d)}d\log(m/d),\qquad
J(m)=\int F(m,h)dh.
\]
Completing the physical even shifts in the prime part gives
\[
\sum_{n\ {\rm odd}}\Lambda(n)
\int F(n-h,h)a_{\rm band}(n-h)dh
\]
with errors bounded by
\[
\frac{Q_2}{\log X}(Q_2/Y)^{60}
+(Q_2/Y)\log^3X+\frac{Y\log X}{X}
+X^{1/100}Y/X.
\tag{8}
\]
The first error is the mean-zero primitive discrepancy. The \(1/\varphi(d)\) factor is retained in the second, principal-mask error. Nonunit rows are actual prime powers with \(p\mid h\); counting \(h=2pr\) gives the final nonprimitive error. These are the same exact completions as R25, restricted to a band, with fixed derivative order \(60\).

The negative flat center in (6) is
\[
-4\sum_{d,k}\mu(d)\log k\sum_{h\ {\rm even}}F(dk,h).
\]
Pure even-lattice completion in \(h\), followed by smooth odd-cofactor completion in \(k\) on scale \(X/d\), turns it into
\[
-\int J(m)a_{\rm band}(m)dm
+O\!\left(Y^{-1}+\frac{YQ_2^2}{X^2\log X}\right).
\tag{9}
\]
The factor \(d/X\) from the latter Poisson calculation is essential. No individual \(k\)-row prime estimate has been used.

Under ordinary RH, the odd Möbius Euler product and partial-sum bound give
\[
a_Q(m)=2+O_\epsilon(Q^{-1/2+\epsilon}\log X).
\]
The two constants \(2\) cancel in
\(a_{\rm band}=a_{Q_2}-a_{Q_1}\). Therefore the main left by (8)–(9) is precisely
\[
\sum_{n\ {\rm odd}}\Lambda(n)G(n)-\int G(y)dy,
\quad
G(n)=\int F(n-h,h)a_{\rm band}(n-h)dh.
\tag{10}
\]
Its amplitude and variation are
\(O(YQ_1^{-1/2+\epsilon}\log X/(X\ell^2))\).
The RH bound for the odd-prime counting function, including all prime powers except the explicitly subtracted powers of \(2\), bounds (10) by
\[
O_\epsilon((Y/\sqrt X)Q_1^{-1/2+\epsilon}\log X).
\tag{11}
\]
At \(\epsilon=1/100\), the errors in (8)–(11) are respectively
\[
X^{-11/100}/\log X,\quad
X^{-1/100}\log^3X,\quad X^{-1/2}\log X,\quad
X^{-49/100},\quad X^{-1/2},\quad
X^{-13/25}/\log X,\quad X^{-49/300}\log X.
\]
Their sum proves (7). All profiles are fixed smooth functions and all derivative orders are fixed. \(\square\)

Consequently the central covariance can be restricted, with a proved \(o(1)\) error, to
\[
d>X^{49/100},\qquad 3\le k<2X^{51/100}.
\tag{12}
\]
The \(k=1\) term vanishes exactly. The balanced \(d,k\asymp\sqrt X\) region and the unbalanced \(d\gg\sqrt X,\ k\ll\sqrt X\) region both remain. Lemma 1 does not estimate either region. It is a cutoff improvement, not a proof of a strict global bound.

## 3. The exact joint matrix, without taking absolute values in \(k\)

Fix a rectangular block
\[
D<d\le2D,\quad K<k\le2K,\quad d,k\ {\rm odd},\quad DK\asymp X.
\]
The true product cutoff in \(F(dk,h)\) is retained by setting the expression to zero outside its support. Define the actual centered prime-window function
\[
f_T(m)=X\ell^2\sum_{h\ {\rm even}}
F(m,h)[\Lambda(m+h)-2],
\tag{13}
\]
for odd \(m\), and set \(f_T(m)=0\) for even \(m\). This parity restriction is essential: the flat center \(2\) is a center on odd endpoints. Define the finite real matrix and coefficient vectors
\[
C_{d,k}=f_T(dk),\qquad a_d=\mu(d),\qquad b_k=\log k.
\tag{14}
\]
The block of the actual covariance is exactly
\[
\boxed{Z_{D,K}=\frac{2}{X\ell^2}\,a^{\mathsf T}Cb.}
\tag{15}
\]
Thus all cofactor rows have been retained jointly, including their phases and the sign of the Möbius coefficient.

The elementary bilinear/operator step in Montgomery–Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, author-hosted draft, printed pages 58–60, equations (17.12)–(17.14), applies legally to this matrix. Its exact first step is
\[
|Z_{D,K}|^2\le
\frac{4\|a\|_2^2}{X^2\ell^4}\,
b^{\mathsf T}(C^{\mathsf T}C)b.
\tag{16}
\]
This has not replaced the \(k\)-sum by a sum of rowwise absolute values. Since
\(\|a\|_2^2\ll D\) and \(\|b\|_2^2\ll K(\log(2K))^2\), it implies the sufficient operator bound
\[
|Z_{D,K}|\ll
\frac{\log(2K)}{\sqrt X\,\ell^2}\|C\|_{\rm op}.
\tag{17}
\]
At \(D,K\asymp\sqrt X\), any fixed \(\delta>0\) in
\[
\boxed{\|C\|_{\rm op}^2\ll X(\log X)^{2-\delta}}
\tag{18}
\]
would imply \(Z_{D,K}=O((\log X)^{-\delta/2})\). Equation (18) is a **missing sufficient estimate**, not a proved theorem or an asserted random-matrix approximation. A weaker, vector-specific input sufficient for (16) is
\[
b^{\mathsf T}C^{\mathsf T}Cb
=o(X^2\ell^4/D).
\tag{19}
\]
Uniform operator control is stronger than necessary for the original fixed Möbius/log pairing.

The actual Gram entries are
\[
\begin{aligned}
(C^{\mathsf T}C)_{k,k'}
=\sum_d\sum_{\substack{h,h'\ {\rm even}}}
&W_{d,k}(h)W_{d,k'}(h')\\
{}\times\{&
\Lambda(dk+h)\Lambda(dk'+h')
-2\Lambda(dk+h)-2\Lambda(dk'+h')+4\},
\end{aligned}
\tag{20}
\]
where \(W_{d,k}(h)=X\ell^2F(dk,h)\). All ranges, masks and smooth weights remain the original ones. The minus signs and both singleton terms in (20) are indispensable.

The two prime arguments in (20) satisfy
\[
k'(dk+h)-k(dk'+h')=k'h-kh'.
\tag{21}
\]
Thus off-diagonal entries are correlations of two actual affine prime forms in the same variable \(d\), with their centers retained. They are not supplied by a theorem about one prime sequence in residue classes. On the diagonal \(k=k'\), (20) contains the genuine short-interval prime-pair variance. Merely renaming (20) a Gram matrix does not estimate it.

## 4. What a source-valid RH mean square actually proves

The available primary input is Carneiro–Chandee–Chirre–Milinovich, *A tale of three integrals*, printed page 1, equation (1.3). Under RH, at fixed exponent \(3\),
\[
\int_1^{S^3}
[\Psi((1+1/S)x)-\Psi(x)-x/S]^2\frac{dx}{x^2}
\ll\frac{\log^2S}{S}.
\tag{22}
\]
Its interval and scale are valid here: \(S\asymp\sqrt X\), so \(m\asymp X\) lies below \(S^3\) for sufficiently large \(X\).

Applied to the actual smooth physical-shift weight, it gives
\[
\sum_{\substack{m\asymp X\\m\ {\rm odd}}}|f_T(m)|^2\ll XY(\log X)^2.
\tag{23}
\]
For completeness, the centered odd prefix is
\[
A_m(y)=\sum_{\substack{1\le h\le y\\h\ {\rm even}}}
[\Lambda(m+h)-2],\quad m\ {\rm odd}.
\]
It equals \(\Psi(m+y)-\Psi(m)-y\), minus the intervening powers of \(2\), plus the bounded exact parity staircase. The powers of \(2\) contribute \(O(\log X)\), uniformly. Partial summation in \(h\) and the \(Y^{-1}\) derivative scale bound \(|f_T(m)|^2\) by
\(O(Y^{-1}\int_{cY}^{CY}|A_m(y)|^2dy)\), with fixed constants after harmless enlargement of the compact support.

One must not insert a variable \(S=m/y\) directly into (22). Instead set \(\lambda=Ty/m\) in the double integral; \(\lambda\) ranges in one fixed compact interval. For each fixed \(\lambda\), use \(S=T/\lambda\) in (22), and then integrate over \(\lambda\). Multiplication by \(m^2\asymp X^2\) yields \(O(XY\log^2X)\). Passing between integer \(m\) and real \(m\) changes the two endpoints by \(O(1)\), contributing \(O(X\log^2X)\), which is smaller. This is the source-valid argument already pinned in R24, not an assertion of GRH or a prime pair asymptotic.

The Frobenius norm of the actual matrix has the exact multiplicity expression
\[
\|C\|_{\rm F}^2
=\sum_m r_{D,K}(m)|f_T(m)|^2,\quad
r_{D,K}(m)=\#\{(d,k):dk=m,\ d\in(D,2D],k\in(K,2K],d,k\ {\rm odd}\}.
\tag{24}
\]
Since \(r_{D,K}(m)\le\tau(m)\ll_\eta X^\eta\), (23) proves
\[
\boxed{\|C\|_{\rm op}^2\le\|C\|_{\rm F}^2
\ll_\eta X^{1+\eta}Y(\log X)^2.}
\tag{25}
\]
At \(Y=\sqrt X,D,K\asymp\sqrt X\), this gives only
\[
|Z_{D,K}|\ll_\eta X^{1/4+\eta/2}.
\tag{26}
\]
This is a bound for an individual matrix block, not for the full global \(\mathcal Z_T\), whose inherited \(O(1)\) bound was stated in (2).

Equation (25) is larger than the desired squared operator scale (18) by a power \(X^{1/2+\eta}\), apart from logarithms. The missing step is genuine cancellation between cofactor rows in the prime Gram form (20); the known one-dimensional mean square controls its total mass only. Montgomery–Vaughan's further Schur estimate gives
\[
\|C\|_{\rm op}^2\le
\max_k\sum_{k'}\left|\sum_d f_T(dk)f_T(dk')\right|.
\tag{27}
\]
This is an exact legal inequality. Its right side is another unestimated actual prime-pair expression. It cannot be treated as a new arithmetic bound just because the bilinear inequality is classical.

## 5. A precise test of the 186 convolution theorem

It would be wrong to claim that the occurrence of Möbius coefficients alone violates the primary convolution theorem. A narrow application is legal.

Take \(D=K=\sqrt X\), and restrict both factors, if necessary, to \((D,11D/10]\) and \((K,11K/10]\), so their product is supported inside \([X,2X]\). Let
\[
\alpha(d)=\mu(d)1_{d\ {\rm odd}}1_{D<d\le11D/10},
\quad
\beta(k)=\log k\,1_{k\ {\rm odd}}1_{K<k\le11K/10},
\quad a_D=\alpha*\beta.
\tag{28}
\]
Then \(\alpha,\beta\) are coefficient sequences with fixed divisor and logarithmic bounds at scales \(D,K\). The **untwisted** \(\beta\) has the Siegel–Walfisz property required by Definition 2.9 of the 186 paper. For small \(q\), inclusion–exclusion for the auxiliary coprimality condition and the fixed odd restriction, followed by partial summation, leaves an endpoint error
\(O(\tau(qs)^2\log X)\). Its main densities agree in each primitive class. For \(q>(\log X)^{L+3}\), the direct interval bound
\[
O((K/q+1)\log X+K\log X/\varphi(q))
\]
is absorbed by \(\tau(qs)^2K(\log X)^{-L}\), because \(K=\sqrt X\) and \(q/\varphi(q)\le\tau(q)\). Thus the source normalization is checked with a fixed divisor exponent, independent of \(L\). No phase is inserted in \(\beta\).

For example, choose the source parameters
\[
\omega=1/200,\quad \delta=1/1000,\quad \sigma=1/10.
\]
The three inequalities in its Proposition 2.18 are
\[
72\omega+24\delta=48/125<1,\quad
48\omega+16\delta+4\sigma=82/125<1,\quad
64\omega+20\delta+2\sigma=27/50<1.
\tag{29}
\]
The scale condition \(X^{1/2-\sigma}\le K\le X^{1/2}\) holds exactly. With a fixed retreat, for example \(1/1000\), Proposition 2.18 therefore gives the legitimate conclusion
\[
\sum_{\substack{q\le X^{509/1000}\\q\mid P_I,\ q\in\mathcal D^{(3)}(X^{1/1000})}}
|\Delta(a_D;a\bmod q)|
\ll_L X(\log X)^{-L},
\tag{30}
\]
for the source's coherent primitive residue system and every fixed \(L>0\). Here its exact discrepancy is
\[
\Delta(f;a\bmod q)=\sum_{n\equiv a\pmod q}f(n)
-\frac1{\varphi(q)}\sum_{(n,q)=1}f(n).
\]
The coprime principal is not replaced by an unrestricted mean.

Equation (30) distributes the **single convolution sequence** \(a_D(m)\) on the source's admitted residue classes. The target, however, is
\[
\sum_{m,h}F(m,h)a_D(m)[\Lambda(m+h)-2].
\tag{31}
\]
The second prime indicator in (31) is not a progression indicator from (30), nor a common smooth multiplier permitted by Proposition 2.12. Inserting it would require a new weighted theorem. Likewise (20) involves two affine prime factors, rather than the Dirichlet convolution tested by (30).

An upper-sieve substitution for \(\Lambda(m+h)\) is not automatically order-preserving: \(a_D\) is genuinely signed. As an exact small coefficient illustration, for \(10<d\le20,\ 20<k\le40\), the values at \(m=253=11\cdot23\) and \(m=345=15\cdot23\) are respectively \(-\log23\) and \(+\log23\). This only verifies the sign obstruction to that substitution; it is not a numerical estimate of the large-\(X\) target.

A different attempted use of \(q=k\) as the source modulus also has an explicit support problem. Actual odd prime cofactors \(k=p\asymp\sqrt X\) are present. Such a prime is not even singly \(X^{1/1000}\)-densely divisible: in Definition 2.1 choose \(U=\sqrt p\); the interval
\([\sqrt p/X^{1/1000},\sqrt p]\) contains neither divisor \(1\) nor \(p\), for sufficiently large \(X\). The modulus \(2p\) fails for the same reason, since the lower endpoint eventually exceeds \(2\). Triple dense divisibility implies single dense divisibility.

These are actual integer cofactors, not a fictitious spectrum. PNT gives
\[
\sum_{K<p\le11K/10}(\log p)^2\asymp K\log K.
\tag{32}
\]
Their coefficient mass is only logarithmically smaller than that of all \(k\) in the interval. This does **not** give a lower bound for their signed contribution to (31), but it prevents declaring that omitted family power-negligible from its coefficient count alone. Restricting to source-admitted moduli remains legal; estimating the excluded rows is a separate obligation.

## 6. Outcome and exact unresolved task

The proved arithmetic improvement is (7): a whole central band of real Möbius/cofactor rows can be removed jointly, moving the divisor cutoff from \(X^{1/3}\) to \(X^{49/100}\) with a power-decaying error. It keeps the prime and flat-center terms together and does not use a factorwise square-root guess.

For the remaining balanced region, (15), (20) provide an exact joint matrix formulation. The primary bilinear inequality applies, but the only directly source-supported mean-square input gives (25)–(26), not the required gain. A sufficient new estimate is the vector-specific prime Gram bound (19), or the stronger operator bound (18). Both concern actual centered affine-prime correlations and retain their full singleton subtraction.

The verified 186 result (30) is useful single-sequence distribution information; this note identifies exactly where applying it to (31) would require an additional theorem. It does not prove that all dispersion approaches are impossible.

Finally, the lowest physical scales, the unbalanced surviving cofactor rows, the summation over all R26 packets and the strict improvement over \(A-2M\) remain unresolved by this central-block test. The global inherited \(O(1)\) estimate has not been strengthened here.

## 7. Sources and reproducibility

- Montgomery–Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, [author-hosted draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf), printed pages 58–60, especially page 59 equations (17.12)–(17.14), PDF page 71: exact bilinear/Gram/Schur mechanism.
- Carneiro–Chandee–Chirre–Milinovich, *A tale of three integrals*, [author-hosted primary PDF](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), printed page 1 equation (1.3): the RH centered prime short-interval mean square, at the legal fixed exponent \(3\).
- [The 186 prime-gap manuscript](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), Definition 2.1 printed page 4; Definition 2.9 and equation (2.4), page 6; the common smooth multiplier Proposition 2.12, page 8; Proposition 2.18, pages 10–11. Its admitted moduli and exact SW normalization are retained in (30).
- The frozen R25/R26 proofs, their primary RH sources and their independent reviews are pinned as dependencies. No prior file is changed.

The bounded checker tests exact coefficient signs, joint Gram algebra and rational parameter margins. It does not enumerate new high primes or test an unproved matrix norm numerically.
