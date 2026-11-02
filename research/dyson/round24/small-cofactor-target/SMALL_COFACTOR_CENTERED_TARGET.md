# The exact small-cofactor complement and its primitive Möbius–prime covariance

Date: 2026-09-05. Author: Euclid. Status: bounded ordinary proof submitted for independent review. The algebra, nonprimitive removal and smooth-center comparison are unconditional. The explicit covariance bound in Section 6 uses RH. No strict variance bound, AH refutation, new prime-gap claim or novelty is asserted.

## 1. Unchanged packet and the exact complement

Use the fixed actual R23 packet
\[
\ell=\log T,\quad X=T^\alpha,\quad H=X/T,\quad
\frac{11}{5}\le\alpha\le\frac94,\quad
Q=X^{523/1000},\quad K=2X/Q,
\tag{1}
\]
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}dx,
\]
\[
F(m,h)=b_T(m)\chi(m/X)V(h/H)
\left(\frac m{m+h}\right)^T.
\tag{2}
\]
Here the fixed \(\omega\) is the unchanged nonnegative smooth weight supported in \([7/4,9/4]\), and \(\chi,V\in C_c^\infty((1,2))\) are fixed real functions. All implicit constants may depend on these three fixed functions. The sums below are finite: \(X<m<2X\), \(H<h<2H\), and \(X<m+h<3X\) for sufficiently large \(T\). No exponential replacement of the Pareto factor is made.

Choose the complete divisor family
\(\mathcal D_Q=\{d\in\mathbb N:d\le Q,\ d\ {\rm odd}\}\).
Möbius coefficients themselves remove nonsquarefree divisors. The exact identity
\[
\Lambda(m)=\sum_{d\mid m}\mu(d)\log(m/d)
\tag{3}
\]
leaves the complementary coefficient
\[
c_Q(m)=\sum_{\substack{d\mid m\\d>Q}}\mu(d)\log(m/d)
\quad(m\ {\rm odd}).
\tag{4}
\]
The raw complement in the prime-pair product is
\[
\mathcal C_Q
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)c_Q(m)\Lambda(m+h).
\tag{5}
\]

Put \(m=kd\). This gives the exact switched formula
\[
\boxed{
\mathcal C_Q
=2\sum_{\substack{3\le k<K\\k\ {\rm odd}}}\log k
\sum_{\substack{d>Q\\d\ {\rm odd}}}\mu(d)
\sum_{h\ {\rm even}}F(kd,h)\Lambda(kd+h).
}
\tag{6}
\]
The \(k=1\) term vanishes because \(\log1=0\). The inequality \(k<K\) is strict, since \(kd<2X\) and \(d>Q\). All remaining interval constraints are enforced by the exact weight \(F\). There is no coprimality condition between \(k\) and \(d\): imposing one would change (6). In particular \(k\) need not be squarefree.

For clarity, the full packet still retains the R23 primitive principal
\[
\mathcal A_Q=
2\sum_{\substack{d\le Q\\d\ {\rm odd}}}\frac{\mu(d)}{\varphi(d)}
\sum_{\substack{n\ {\rm odd}\\h\ {\rm even}}}
\Lambda(n)F(n-h,h)\log((n-h)/d)
1_{(n,d)=1}1_{(h,d)=1},
\tag{7}
\]
and both singular-series-weighted marginals
\[
\mathcal M_{\mathfrak S}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2].
\tag{8}
\]
The exact R23 decomposition is
\[
\mathcal P_{T,X}^{\chi,V}
=\mathcal B_Q+\mathcal N_Q+\mathcal A_Q
+\mathcal C_Q-\mathcal M_{\mathfrak S}.
\tag{9}
\]
The \(d=1\) primitive discrepancy is identically zero; its principal is retained in (7). The previous smooth-shift proof applies to \(\mathcal B_Q\) without complementary owner guards. The separate R24 nonprimitive proof supplies the enlarged-family estimate for \(\mathcal N_Q\). This note independently treats the complement (6), rather than assuming it is negligible.

## 2. A further actual nonprimitive component is removable

Split (6) according to \((k,h)=1\) or \((k,h)>1\), and denote the latter raw-prime term by \(\mathcal C_Q^{\rm bad}\).

**Lemma 1.** For every fixed \(\eta>0\),
\[
\boxed{|\mathcal C_Q^{\rm bad}|
\ll_\eta X^\eta/T.}
\tag{10}
\]
In particular \(\eta=1/100\) gives the uniform bound
\(O(X^{-391/900})\) in (1).

**Proof.** If its prime factor is nonzero, then \(n=kd+h=p^j\) for an odd prime \(p\mid(k,h)\). Since \(k<K<X\), this cannot be a genuine prime \(n\in(X,3X)\); hence \(j\ge2\) and \(p\le\sqrt{3X}\). For each odd base there are at most two powers in \((X,3X)\).

The divisibility \(p\mid h\) must be used before taking absolute values over all shifts. Because \(H\gg X^{6/11}\gg\sqrt X\), the number of allowed even shifts divisible by \(p\) is \(O(H/p)\), uniformly for these primes. For fixed \(n,h\), all participating pairs \((k,d)\) factor \(m=n-h\), so
\[
\sum_{\substack{kd=m\\k<K,\ d>Q}}
|\mu(d)|\log k
\le\tau(m)\log(2X)\ll_\eta X^\eta\log X.
\tag{11}
\]
Use \(|F|\ll1/(X\ell^2)\), and charge the actual prime-power weight as \(\Lambda(n)=\log p\), not \(\log X\) before summing the bases. Chebyshev and partial summation give
\[
\sum_{p\le Y}\frac{\log p}{p}\ll\log(2Y).
\]
Thus
\[
|\mathcal C_Q^{\rm bad}|
\ll_\eta\frac{X^\eta\log X}{X\ell^2}
H\sum_{p\le\sqrt{3X}}\frac{\log p}{p}
\ll_\eta X^\eta/T.
\]
This is an absolute estimate of the actual raw-prime term. It does not discard a baseline on forbidden residue classes. The two logarithms are absorbed by \(\ell^2\), since \(\log X=\alpha\ell\).

The original coarser cube-count argument was also valid: \(K<\sqrt X\) eventually forces \(j\ge3\), and charging every shift gave \(O(X^{-91/900})\) at \(\eta=1/100\). Equation (10) improves that bound by retaining \(p\mid h\). It is the same elementary counting mechanism as the separate R24 enlarged-family nonprimitive lemma. \(\square\)

## 3. An exact primitive local center, including its full main term

On the surviving rows, \(n=kd+h\) lies in one primitive residue class modulo \(2k\): \(n\equiv h\pmod k\) and \(n\) is odd. The density constant along odd \(d\)'s is \(2k/\varphi(k)\), not \(2\).

Define the actual primitive Möbius–prime covariance
\[
\boxed{
\mathcal Z_Q
=2\sum_{\substack{3\le k<K\\k\ {\rm odd}}}\log k
\sum_{\substack{d>Q\\d\ {\rm odd}}}\mu(d)
\sum_{\substack{h\ {\rm even}\\(h,k)=1}}
F(kd,h)\left[\Lambda(kd+h)-\frac{2k}{\varphi(k)}\right].
}
\tag{12}
\]
The corresponding exact local-density main is
\[
\mathcal L_Q^{\rm loc}
=4\sum_{\substack{3\le k<K\\k\ {\rm odd}}}
\frac{k\log k}{\varphi(k)}
\sum_{\substack{d>Q\\d\ {\rm odd}}}\mu(d)
\sum_{\substack{h\ {\rm even}\\(h,k)=1}}F(kd,h).
\tag{13}
\]
There is an exact equality, not a prime-density approximation,
\[
\boxed{\mathcal C_Q
=\mathcal Z_Q+\mathcal L_Q^{\rm loc}
+\mathcal C_Q^{\rm bad}.}
\tag{14}
\]
The center in (12) is defined and added back in (13). It has not been identified with the source's finite-interval principal \(\varphi(2k)^{-1}\sum_{(n,2k)=1}\Lambda(n)\), whose error would need separate control.

Put
\[
J_T(m)=\int_{\mathbb R}F(m,h)\,dh,\qquad
\mathcal L_Q^0
=2\sum_{\substack{3\le k<K\\k\ {\rm odd}}}\log k
\sum_{\substack{d>Q\\d\ {\rm odd}}}\mu(d)J_T(kd).
\tag{15}
\]
Both are completely explicit. In particular \(J_T(m)\) has support in \(X<m<2X\).

**Lemma 2.**
\[
\boxed{
\mathcal L_Q^{\rm loc}
=\mathcal L_Q^0
+O\!\left(\frac KH(\log X)^3\right).
}
\tag{16}
\]
The error is \(o(1)\), since \(K/H\le2X^{-753/11000}\).

**Proof.** For fixed \(m\) on its support, every fixed derivative of
\(f(h)=F(m,h)\) satisfies
\[
|\partial_h^j f(h)|\ll_j A_XH^{-j},
\qquad A_X=(X\ell^2)^{-1}.
\tag{17}
\]
This uses the exact Pareto derivative and the fixed compact \(V\). All boundary derivatives vanish.

For odd \(s\le K<H\), Poisson summation on the grid \(2s\mathbb Z\), with repeated integration by parts, gives for every fixed integer \(j\ge1\)
\[
\sum_{h\in2s\mathbb Z}f(h)
=\frac1{2s}\int f(h)\,dh+O_j(A_X(s/H)^j).
\tag{18}
\]
The prefactor \(1/(2s)\) retains the parity of the physical shifts. No arithmetic coefficients have been differentiated.

Use the exact divisor identity \(1_{(h,k)=1}=\sum_{s\mid k,\ s\mid h}\mu(s)\), valid also for nonsquarefree \(k\). It follows that
\[
\sum_{\substack{h\ {\rm even}\\(h,k)=1}}f(h)
=\frac{\varphi(k)}{2k}J_T(m)
+O_j(A_X\tau(k)(k/H)^j).
\tag{19}
\]
Also \(k/\varphi(k)\le\tau(k)\). There are at most \(2X/k\) possible \(d\)'s for each \(k\), and
\[
\sum_{k\le K}\frac{\tau(k)^2}{k}\ll(1+\log K)^4.
\tag{20}
\]
For example \(\tau(n)^2\le d_4(n)\), and the four-fold harmonic convolution proves (20) directly.

Substitution in (13), taking \(j=1\), bounds the entire error by
\[
\frac{C\log X}{\ell^2}\frac KH
\sum_{k\le K}\frac{\tau(k)^2}{k}
\ll\frac KH(\log X)^3.
\]
The mean terms give (15) exactly. This proves (16). \(\square\)

The same proof with \(s=1\) gives
\[
4\sum_{k,d}\mu(d)\log k
\sum_{h\ {\rm even}}F(kd,h)
=\mathcal L_Q^0+O(H^{-1}),
\tag{21}
\]
with the same \(k,d\) ranges. Consequently, if
\[
\mathcal Z_Q^{(2)}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)c_Q(m)[\Lambda(m+h)-2],
\tag{22}
\]
then
\[
\boxed{\mathcal Z_Q
=\mathcal Z_Q^{(2)}
+O_\eta\!\left(X^\eta/T+(K/H)(\log X)^3\right).}
\tag{23}
\]
This last comparison is legitimate only after paying for the raw nonprimitive term and the exact difference of the two centers. Simply inserting a primitive mask into (22) and deleting its excluded constant would be wrong.

## 4. The remaining signed expression is fully specified

Combining the exact decomposition (9) with (10), (14) and (16) gives
\[
\boxed{
\mathcal P_{T,X}^{\chi,V}
=\mathcal B_Q+\mathcal N_Q
+\mathcal A_Q+\mathcal L_Q^0+\mathcal Z_Q
-\mathcal M_{\mathfrak S}
+O_\eta\!\left(X^\eta/T+(K/H)(\log X)^3\right).
}
\tag{24}
\]
After the separately established \(\mathcal B_Q,\mathcal N_Q=o(1)\) are inserted, the actual remaining target for this packet is
\[
\boxed{\mathcal A_Q+\mathcal L_Q^0+\mathcal Z_Q-\mathcal M_{\mathfrak S}.}
\tag{25}
\]
The principal (7), the Möbius-linear main (15), and both marginals (8) remain in this expression. None is discarded on positivity or a relative asymptotic. No sign is claimed for any of their differences.

This is a concrete cofactor covariance with \(k<2X^{477/1000}\), \(d>Q\), \(X<kd<2X\), and \(H<h<2H\), with the original Möbius coefficients, every primitive restriction and exact derivative weights. A bound for a generic substitute coefficient or for its uncentered positive version would not settle (25).

As in R23, this is a smooth piece of the actual target. A single-packet reduction does not partition the entire arithmetic window or allocate the full variance threshold to this packet. No inequality for the complete zeta statistic follows from (24) alone.

## 5. Why the one-prime source does not currently estimate this covariance

There is no modulus-size difficulty for the small cofactor itself:
\(2k\ll X^{477/1000}<X^{1/2-\epsilon}\) for a fixed \(\epsilon>0\).
The 186 source's Proposition 2.15 is therefore a legal ordinary-modulus prime distribution input at those levels, with its primitive finite principal. Its Corollary 2.19 gives more special moduli but does not change the following coefficient issue.

For fixed \(k,h\), rewriting the prime in the variable \(n=kd+h\) attaches
\[
\mu((n-h)/k)\,1_{\{(n-h)/k>Q,\ (n-h)/k\ {\rm odd}\}}
\tag{26}
\]
to \(\Lambda(n)\) on the single progression. This is not a common smooth endpoint weight on the prime sequence. The source's weighted partial summation, Proposition 2.12, requires a polylogarithmic endpoint-plus-variation norm after normalization.

The failure of that smoothness premise can be checked for the actual coefficient. On an odd \(d\)-interval of fixed proportional length at scale \(D\), there are \(\gg D\) squarefree integers \(d\equiv11\pmod{18}\). For each, \(|\mu(d)|=1\), whereas \(\mu(d-2)=0\) since \(9\mid d-2\). Hence the total variation of \(\mu(d)\) along the odd grid is \(\gg D\).

Here is an elementary quantitative count behind that assertion. Expanding the squarefree indicator and counting a primitive residue class modulo \(18s^2\) gives
\[
\#\{D<d\le2D:d\equiv11\pmod{18},\ d\ {\rm squarefree}\}
=\frac D{18}\prod_{p\nmid18}(1-p^{-2})+O(\sqrt D).
\tag{27}
\]
Only \(s\) coprime to \(18\) occur, and the \(O(\sqrt D)\) comes from summing endpoint errors and the convergent main-term tail. The product is positive. Shortening to a fixed proportional subinterval has the same proof.

In the present complement \(D\gg Q=X^{523/1000}\). Thus a continuous interpolation of the actual Möbius samples cannot have the required polylogarithmic total variation. A fixed nonvanishing smooth profile does not remove these zero-to-unit jumps on an interior interval. This is a precise obstruction to that **weighted one-prime application**, not a no-go theorem for joint dispersion.

The bilinear source theorems instead estimate distribution of a Dirichlet convolution \(\alpha*\beta\), with their specified scale and untwisted Siegel–Walﬁsz hypotheses on \(\beta\). Formula (12) contains the additive relation \(n=kd+h\) and the external prime mark \(\Lambda(n)\); it is not that distribution statistic. Even granting a suitable untwisted property for a Möbius sequence would not establish the shifted prime-weighted covariance (12). No phase-twisted SW property, interchange of physical and dual shifts, or assertion about arbitrary residue maxima is made here.

A new dispersion estimate could still handle the signed \(k,d,h\) sum. The existing source statements, applied as stated, do not supply that estimate.

## 6. A source-valid RH bound for the actual centered covariance

The preceding failure is not a reason to leave the covariance wholly unestimated. The classical RH Selberg bound gives the following explicit, but insufficient, control.

**Lemma 3.** Under RH,
\[
\boxed{|\mathcal Z_Q^{(2)}|
\ll \sqrt H\,(\log X)^{3/2}.}
\tag{28}
\]
Equation (23) gives the same bound for \(\mathcal Z_Q\), plus its already negligible errors.

**Proof.** Put, for odd integers \(m\in(X,2X)\),
\[
S_T(m)=\sum_{h\ {\rm even}}
V(h/H)k_T(m,h)[\Lambda(m+h)-2].
\]
The complementary coefficient satisfies
\[
|c_Q(m)|\le\tau(m)\log(2X),\qquad
\sum_{X<m<2X}|c_Q(m)|^2\ll X(\log X)^5.
\tag{29}
\]
The latter follows from \(\tau^2\le d_4\) and
\(\sum_{n\le2X}d_4(n)\ll X(1+\log X)^3\).

We claim the actual weighted prime increments satisfy
\[
\sum_{\substack{X<m<2X\\m\ {\rm odd}}}|S_T(m)|^2
\ll XH\ell^2.
\tag{30}
\]
For real \(0\le y\le2H<m\), define
\[
A_m(y)=\sum_{\substack{0<h\le y\\h\ {\rm even}}}
[\Lambda(m+h)-2].
\]
The exact endpoint identity is
\[
A_m(y)=E(m+y)-E(m)
-[P_2(m+y)-P_2(m)]
+y-2\#\{m<n\le m+y:n\ {\rm odd}\},
\tag{31}
\]
where \(E(x)=\Psi(x)-x\) and \(P_2\) contains every power of two with weight \(\log2\). The last two terms are uniformly \(O(1)\): the interval ratio is below two, and the parity counting discrepancy is bounded. Thus no higher prime power has been silently omitted.

The smooth \(h\)-weight has derivative \(O(1/H)\), is supported in \((H,2H)\), and vanishes at both ends. Stieltjes partial summation and Cauchy–Schwarz give
\[
|S_T(m)|^2\ll
\frac1H\int_H^{2H}|E(m+y)-E(m)|^2dy+1.
\tag{32}
\]
Set \(y=\lambda m/T\). Since \(X<m<2X\), its \(\lambda\)-range is contained in \([1/2,2]\), and \((m/T)/H=m/X\le2\).

The primary RH input is CCCC equation (1.3), with the fixed exponent \(3\):
\[
\int_1^{S^3}
|E((1+1/S)x)-E(x)|^2\frac{dx}{x^2}
\ll\frac{\log^2S}{S}.
\tag{33}
\]
Take \(S=T/\lambda\). Uniformly for \(1/2\le\lambda\le2\), one has \(S\asymp T\), and \(2X+1<S^3\) for sufficiently large \(T\). After multiplying by \(O(X^2)\), (33) bounds the corresponding unweighted \(x\)-integral on \([X,2X+1]\) by \(O(XH\ell^2)\).

To pass from real \(x\) to integer \(m\), compare \(x\in[m,m+1]\) at the same fixed \(\lambda\). Each endpoint moves by at most two, so the two prime staircases differ by \(O(\log X)\), while the continuous centers move by \(O(1)\). The sum of the resulting squared comparison errors is \(O(X\log^2X)\), which is absorbed because \(H\to\infty\). This proves (30) after integrating over the compact \(\lambda\)-range. No uniform theorem for a varying additive interval endpoint was assumed.

Finally \(|b_T(m)\chi(m/X)|\ll1/(X\ell^2)\). Cauchy–Schwarz, (29) and (30) give
\[
|\mathcal Z_Q^{(2)}|
\ll\frac1{X\ell^2}
\sqrt{X(\log X)^5}\sqrt{XH\ell^2}
\ll\sqrt H(\log X)^{3/2}.
\]
This proves (28). It uses ordinary RH for \(\zeta\), not GRH. \(\square\)

The bound still grows like a positive power of \(X\), between \(X^{3/11}\) and \(X^{5/18}\), before logarithms. It does not control (25) at \(O(1)\), and it supplies no sign for the covariance or for the cross terms with \(\mathcal A_Q+\mathcal L_Q^0-\mathcal M_{\mathfrak S}\). It is a quantified failure of this particular norm estimate to close the target, not evidence that the actual covariance is that large.

## 7. A relative main-term estimate is not a fluctuation estimate

The natural packet mass is already divergent. For fixed \(\alpha\) in the open range with \(\omega(\alpha)>0\), and fixed nonnegative nonzero \(\chi,V\), define
\[
\mathfrak B_{T,X}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}F(m,h).
\]
Riemann summation on the two parity grids, together with the exact integral for \(b_T\), gives
\[
\boxed{
\mathfrak B_{T,X}
\sim\frac{H}{2\ell^2}\omega(\alpha)
\int_1^2\int_1^2
\frac{\chi(v)}v V(z)e^{-z/v}\,dz\,dv.
}
\tag{34}
\]
The double integral is positive. The factor \(1/2\) combines the outer factor two with the two parity densities \(1/2\). In obtaining this scale calculation only, \(m=Xv\), \(h=Hz\) give \(k_T\to e^{-z/v}\), uniformly on the fixed compact support. Equation (34) is not used to replace the kernel in (6)–(33).

Since \(H\) is a positive power of \(X\), a relative \(o(1)\) error against this main scale gives only \(o(H/\ell^2)\), which need not tend to zero. To deduce an \(o(1)\) additive error from a relative bound \(\delta_X\) by this route, one needs
\[
\delta_X=o(\ell^2/H).
\tag{35}
\]
For comparison, even a relative error of the RH-like size
\(X^{-1/2}(\log X)^2\) produces a bound of order
\[
H/\sqrt X
=X^{\,1/2-1/\alpha},
\tag{36}
\]
whose exponent lies in \([1/22,1/18]\) here. Arbitrarily strong fixed logarithmic relative savings also fail to give (35). This is why the primitive main (7), the center (15), and the two marginals (8) cannot be dropped on a naive PNT-relative approximation.

There is a parallel exact bookkeeping bound for the Möbius-linear main. Suppose only that, for all \(y\ge Q\),
\[
\left|\sum_{\substack{d\le y\\d\ {\rm odd}}}\mu(d)\right|
\le\delta_\mu(Q)y.
\tag{37}
\]
This is a stated input for the following calculation, not a new Möbius theorem. The smooth weight \(J_T(m)\) has size \(O(H/(X\ell^2))\) and first derivative \(O(H/(X^2\ell^2))\). Partial summation on the actual range
\(d>Q,\ X<kd<2X\), with its sharp lower endpoint retained, gives
\[
\left|\sum_{\substack{d>Q\\d\ {\rm odd}}}\mu(d)J_T(kd)\right|
\ll\frac{\delta_\mu(Q)H}{k\ell^2}.
\]
Summing \(\log k/k\) gives only
\[
|\mathcal L_Q^0|\ll\delta_\mu(Q)H.
\tag{38}
\]
Thus a qualitative or logarithmic relative cancellation input for this linear main is not an \(o(1)\) estimate either. No use of (38) to delete \(\mathcal L_Q^0\) is made.

## 8. Accepted scope and next actual estimate

This bounded step supplies:
- the exact complement with small odd cofactors, including shared factors between \(k,d\);
- absolute removal of its genuine nonprimitive prime-power term at \(O_\eta(X^\eta/T)\);
- the precise primitive local center and a smooth-period comparison with its explicit Möbius-linear main, at \(o(1)\);
- a legal RH norm estimate for the resulting actual covariance, with its inadequate power scale quantified.

The remaining estimate must control the **signed combination** (25), or its exact recombination across a proved packet partition. It cannot be replaced by an unweighted prime-density asymptotic, a source theorem for a different Dirichlet convolution, a claim that the Möbius sequence is smooth, or a bound that omits the local-center term. A new aggregate dispersion estimate may still supply the needed cancellation; this note has not proved it.

Primary sources checked: OpenAI, *Improved short gaps between primes*, printed pp.6–11, Definitions 2.6–2.9 and Propositions 2.12/2.15/2.18/Corollary 2.19, [official PDF](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf); Carneiro–Chandee–Chirre–Milinovich, *On Montgomery's pair correlation conjecture: a tale of three integrals*, printed p.1, equations (1.1)/(1.3), [author-hosted PDF](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf). Retained source files and the exact R23/R24 dependencies are pinned adjacent to this report. The new algebra and endpoint bounds are proved above; no numerical prime-height experiment is used.

