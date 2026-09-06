# A mixed-moment test for the actual scale-dependent divisor remainder

Date: 2026-09-05. Author: Aquinas. Status: ordinary derivation submitted for independent review. This is a bounded source and inequality-direction audit, not a new prime-pair estimate. The inherited variance reduction assumes RH; the mixed progression estimate below is unconditional. No novelty or strict Dyson/AH conclusion is asserted.

The concrete conclusions are that the *pure* actual divisor-approximant correlations admit a summable error \(O(\ell^5T^{-1/2})\) by smooth completion, while the usual genuine-prime mixed-moment error is insufficient after our normalization. Even an exact evaluation of both moments would provide a lower bound through a positive residual norm. It does not upper-bound the remaining prime-prime second moment. The global separation-dependent cutoff also prevents an automatic identification with one orthogonal projection.

## 1. The frozen object, with no change of cutoff or center

The input is Euclid's `research-round26/full-shift-reduction/FULL_SHIFT_REDUCTION.md`, SHA256 `c0d413f2eead98cfc97de09cd5b4f8ffaa0df7a6b81249df576ccff61a0cadd6`, read in full. Write
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},\quad
X_i=2^iL,\quad Y_j=2^j\sqrt\ell,\quad Q_j=Y_j^{2/3}.
\tag{1}
\]
The nonnegative smooth packets are exactly
\[
F_{ij}(m,h)=b_T(m)\beta(m/X_i)\beta(h/Y_j)
r(m/(2U))r(Th/(32\ell m))(1+h/m)^{-T},
\]
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}\,dx.
\tag{2}
\]
Here \(r,\beta=r-r(2\cdot)\) are the fixed R26 functions. All prime powers are retained. For a nonzero packet, put \(X=X_i,Y=Y_j,Q=Q_j\); its support and seminorms satisfy
\[
m\asymp X,\quad h\asymp Y,\quad
Y\le 8(32\ell)X/T,\quad X<8U,
\]
\[
|\partial_m^a\partial_h^bF_{ij}(m,h)|
\ll_{a,b}(X\ell^2)^{-1}X^{-a}Y^{-b}.
\tag{3}
\]
In particular \(Q\ge\ell^{1/3}\) and, uniformly over all packets,
\(2Q\le X^{1/2-1/10}\) eventually. The latter follows from
\(Q\ll \ell^{2/3}X^{10/27+o(1)}\), with a fixed positive margin below \(X^{2/5}\).

Define two distinct small-divisor objects:
\[
A_Q(m)=\sum_{\substack{d\mid m\\d\le Q}}\mu(d)\log(m/d),
\qquad
a_Q^{\rm av}(m)=\sum_{\substack{d\le Q\\d\ {\rm odd}}}
\frac{\mu(d)}d\log(m/d).
\tag{4}
\]
Only the first is a pointwise divisor approximant. For odd \(m>1\),
\[
c_Q(m)=\Lambda(m)-A_Q(m)
=\sum_{\substack{d\mid m\\d>Q}}\mu(d)\log(m/d).
\tag{5}
\]
The exact global R26 expression is
\[
\mathcal Z_T=\sum_{i,j} Z_{ij},\qquad
Z_{ij}=2\sum_{\substack{m\ {\rm odd}\\h\ge2\ {\rm even}}}
F_{ij}(m,h)c_{Q_j}(m)[\Lambda(m+h)-2].
\tag{6}
\]
The frozen theorem gives under RH, for the symmetric fixed bump,
\[
\overline V_T=2M+\mathcal Z_T+o(1),\qquad M=\int\omega.
\tag{7}
\]
Thus the sufficient strict target remains
\(\liminf\mathcal Z_T\le1-2M\). We do not replace it by a claim that \(\mathcal Z_T\) tends to zero. In fact the inherited RH bounds already give
\[
-2M\le\liminf\mathcal Z_T\le\limsup\mathcal Z_T\le A-2M,
\quad A=1+\varepsilon^2m_1,
\tag{7a}
\]
and hence a global \(O(1)\) bound. The missing improvement is a strict saving below \(A-2M\); the growing packet error budgets below do not contradict this already known global bound.

## 2. The approximant is not the usual Goldston–Yildirim cutoff

For the standard logarithmic divisor sum
\[
\Lambda_Q(m)=\sum_{\substack{d\mid m\\d\le Q}}
\mu(d)\log(Q/d),\qquad
B_Q(m)=\sum_{\substack{d\mid m\\d\le Q}}\mu(d),
\]
the exact identity is
\[
\boxed{A_Q(m)=\Lambda_Q(m)+\log(m/Q)B_Q(m).}
\tag{8}
\]
The second term has no small coefficient in our range. No theorem for \(\Lambda_Q\) may simply be relabelled a theorem for \(A_Q\), nor may one differentiate an unspecified asymptotic error to evaluate \(B_Q\).

There is a useful structural distinction. If \(p>Q\) is prime, then
\[
A_Q(p)=\log p=\Lambda(p),\qquad c_Q(p)=0,
\]
whereas \(\Lambda(p)-\Lambda_Q(p)=\log(p/Q)\). Indeed \(c_Q\) vanishes on every prime, whether below or above the cutoff. For a power \(p^a\), it vanishes when \(p\le Q\); when \(p>Q\),
\[
c_Q(p^a)=(1-a)\log p.
\tag{9}
\]
These identities do not authorize discarding higher powers in (6).

Composite support does not supply a sign. For the single real cutoff \(Q=150^{1/3}\in(5,6)\),
\[
c_Q(195)=c_Q(3\cdot5\cdot13)=\log13>0,
\qquad c_Q(183)=c_Q(3\cdot61)=-\log3<0.
\tag{10}
\]
Both integers lie in \((150,300)\). These are exact finite divisor identities, not numerical logarithm tests or a claim about a particular global packet. More generally, for three distinct primes \(p,q\le Q<r\) with \(pq>Q\), the integer \(m=pqr\) gives \(c_Q(m)=\log r\); a semiprime with exactly one factor below \(Q\) gives the second sign. Two small factors alone would not imply that positive sign. Almost-prime support alone therefore does not turn the covariance into a positive sieve sum.

## 3. An actual mixed estimate, legal uniformly over the global packets

Define the exact mixed small-divisor contribution
\[
\mathscr M_F=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)A_Q(m)[\Lambda(m+h)-2]
\]
and the exact finite main coefficient
\[
K_Q(m,h)=\sum_{\substack{d\le Q\\d\ {\rm odd}}}
\mu(d)\log(m/d)
\left(\frac{1_{(d,h)=1}}{\varphi(d)}-\frac1d\right).
\tag{11}
\]
**Lemma 1.** For every fixed \(A>0,\eta>0\), uniformly for (3),
\[
\boxed{
\mathscr M_F
=2\sum_{h\ {\rm even}}\int F(m,h)K_Q(m,h)\,dm
+O_{A,\eta}\!\left(
Y\ell^{-A}+X^\eta Y/X+\frac{YQ^3}{X^3\ell}
\right).}
\tag{12}
\]
This uses ordinary Bombieri–Vinogradov, not RH or GRH. The main term is kept as the displayed finite divisor sum.

**Proof.** Set \(n=m+h\). For an odd divisor \(d\) and even \(h\), the conditions \(d\mid m\), \(m\) odd select one residue class of \(n\) modulo \(2d\). It is primitive precisely when \((d,h)=1\); its principal density for \(\Lambda\) is then \(1/\varphi(2d)=1/\varphi(d)\).

Separate the weight into the two common functions
\(F(n-h,h)\log(n-h)\) and \(F(n-h,h)\), multiplying the second by \(-\log d\). Their amplitude plus total variation on a fixed \(X\)-scale interval is
\(O((X\ell^2)^{-1}\log X)\). The endpoint-uniform Bombieri–Vinogradov theorem, with \(2Q\le X^{1/2-1/10}\), bounds the sum of primitive progression discrepancies by \(X\log^{-B}X\) for every fixed \(B\). Partial summation therefore costs \(O_A(\ell^{-A})\) per shift, after increasing \(B\) by a fixed amount. There are \(O(Y)\) shifts. This is the first error in (12). No moving prime coefficient has been treated as a smooth weight.

In a nonprimitive class an actual nonzero \(\Lambda(n)\) forces \(n=p^a\), \(p\mid d,h\), and \(a\ge2\), since \(d\le Q<X/2<n\). Here \(p\) is odd and \(h=2pr\), so there are \(O(Y/p)\) allowed shifts, including the empty case \(p>Y\). For each prime, there are \(O(1)\) powers in the fixed-ratio interval \(n\asymp X\). Sum the divisor coefficient once, before summing prime bases:
\[
\sum_{\substack{d\mid n-h\\d\le Q}}
|\mu(d)\log((n-h)/d)|
\le\tau(n-h)\log(2X)\ll_\eta X^\eta\log X.
\]
The factor \(\Lambda(p^a)\) is \(\log p\), not \(a\log p\). The elementary Chebyshev consequence
\(\sum_{p\le\sqrt{3X}}(\log p)/p\ll\log X\)
now gives \(O_\eta(X^\eta Y/X)\), using \(\log X\asymp\ell\). This is precisely the mechanism separately proved in R24, valid even when \(Y<\sqrt X\).

For the exact flat center, fix \(d,h\) and complete the odd cofactor lattice \(m=d(2r+1)\). The smooth weight \(F(m,h)\log(m/d)\) has scale \(X\), so Poisson summation with three derivatives gives
\[
\sum_{m\equiv d\ (2d)}F(m,h)\log(m/d)
=\frac1{2d}\int F(m,h)\log(m/d)\,dm
+O\!\left(\frac{\log X}{X\ell^2}(d/X)^2\right).
\]
Multiplying by the original center factor \(-4\), and summing over \(d\le Q\) and \(O(Y)\) shifts, gives the last error in (12). The factor \(1/(2d)\), together with \(-4\), is exactly the \(-2/d\) part of the displayed main. This proves (12), retaining real endpoints and all prime powers. \(\square\)

The primary progression input is the usual Bombieri–Vinogradov mechanism used in Goldston–Yildirim's mixed-correlation proofs; for the endpoint-uniform version used here, the retained short-gaps source, Proposition 2.15, explicitly includes interval suprema. Proposition 2.12 explains the common smooth-weight transfer. Only its ordinary below-one-half prime case is used, not the new 186 distribution range.

For the actual remainder, the finite algebra is simply
\[
\boxed{Z_{ij}=
2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F_{ij}(m,h)\Lambda(m)[\Lambda(m+h)-2]
-\mathscr M_{F_{ij}}.}
\tag{13}
\]
Thus even a perfect estimate for the mixed term leaves the coefficient of the true shifted prime-prime product equal to one. The fixed center \(2\), the finite \(K_Q\) main and the singular-series correction in (7) must all be retained when comparing this with the final variance.

## 4. What the specific classical mixed-moment source actually supplies

Goldston–Yildirim II uses a different approximant,
\[
\lambda_R(n)=\sum_{r\le R}\frac{\mu^2(r)}{\varphi(r)}
\sum_{d\mid(r,n)}d\mu(d).
\tag{14}
\]
Its Theorem 2, printed page 8, and the proof on pages 20–21, equation (5.6), give the two-factor mixed correlation with one genuine \(\Lambda\). In the fixed-power range
\(X^\delta\le R\le X^{1/2-\delta}\), its explicit error includes
\[
O\!\left(\frac X R\frac{h^*\tau(h^*)}{\varphi(h^*)}
+\frac X{\log^A X}\right),
\qquad h^*=\prod_{p\mid h}p.
\tag{15}
\]
The pure two-factor correlation has the additional \(O(R^2)\) remainder, equation (4.9), printed page 19. The source's higher mixed theorem has the stricter divisor range \(R\le X^{1/4-\delta}\) for two approximant factors and one genuine prime factor. Its later GRH application is not invoked here.

These statements improve the shift scope of the earlier GY I theorem. They still do not give a theorem for (4). On the natural power-sized packets, \(R=Q=Y^{2/3}\) lies within the two-factor modulus range; the source can legally be used there for its own \(\lambda_Q\). Smooth \(X\)-weights are obtained by partial summation. Reversing the sign of the shift and subtracting two prefixes gives the desired orientation on \(m\asymp X\); the source's explicit endpoint terms are absorbed in the displayed errors in this range. For even \(h\), restricting this mixed formula to odd \(m\) removes only the terms \(m+h=2^a\). Since \(\lambda_Q(m)\ll\tau(m)\log(2Q)\), their total after all shifts and packet normalization is \(O_\eta(X^\eta Y/X)\); they are an explicit error, not silently omitted prime powers. The source assumption \(R\ge X^\delta\) does **not** cover the lowest actual packets \(Q=\ell^{1/3}\). Lemma 1 avoids that assumption by keeping the exact finite main.

Here are the quantitative costs, not lower bounds for the actual errors:

* A per-shift error \(X\log^{-A}X\), with our amplitude \((X\ell^2)^{-1}\) and \(O(Y)\) shifts, allows only \(O_A(Y\ell^{-A-2})\). No fixed logarithmic saving makes that \(o(1)\) for the natural polynomial-sized \(Y\). Nor can one make \(A\) depend on \(T\) in an asymptotic theorem whose constants depend on \(A\).
* The \(X/R\) part of (15) gives a majorant of the form
  \[
  \frac1{Q\ell^2}\sum_{h\asymp Y}
  \frac{h^*\tau(h^*)}{\varphi(h^*)}.
  \tag{16}
  \]
  Even ignoring the extra arithmetic factors in that available majorant, its scale is \(Y^{1/3}/\ell^2\). This does not mean the actual error is that large; it means the displayed bound supplies no vanishing error. For \(X=T^\alpha,Y=X/T\), the positive power ranges from \(T^{1/4}\) to \(T^{5/12}\), before logarithms, as \(\alpha\) ranges over \([7/4,9/4]\).
* The pure correlation remainder \(O(Q^2)\) permits only \(O(YQ^2/(X\ell^2))\) after summing shifts. For the actual logarithmic coefficient (4), direct divisor expansion gives the safe remainder \(O(Q^2\log^2X)\) per shift, hence
  \[
  O(YQ^2/X)=O(Y^{7/3}/X).
  \tag{17}
  \]
  At \(Y=X/T\) its power is \(T^{4\alpha/3-7/3}\): zero at \(\alpha=7/4\), and \(+2/3\) at \(\alpha=9/4\). This is only a failure of that crude error ledger. It is **not** an obstruction to the attainable pure moments: the stronger smooth completion proved immediately below makes their actual global error vanish.

For (17), expansion over two divisors and an amplitude-plus-variation progression bound suffice. But here every least common multiple is much smaller than \(X\), and the fixed smoothness in (3) can be used again. The following stronger bound is a direct ordinary proof, independently derived also by Plato during review; it is not attributed to a stronger version of the cited GY theorem.

**Lemma 2 (a summably evaluated pure approximant correlation).** Put
\[
\mathscr T_{ij}=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F_{ij}(m,h)A_Q(m)A_Q(m+h),\qquad Q=Y_j^{2/3},
\]
\[
\mathscr D_{ij}=
\sum_{h\ {\rm even}}
\sum_{\substack{d_1,d_2\le Q\ {\rm odd}\\(d_1,d_2)\mid h}}
\frac{\mu(d_1)\mu(d_2)}{[d_1,d_2]}
\int F_{ij}(m,h)
\log(m/d_1)\log((m+h)/d_2)\,dm.
\tag{17a}
\]
These are finite exact expressions, with a genuine divisor sum in the second and no unknown prime coefficients. Uniformly over the actual packets,
\[
\mathscr T_{ij}=\mathscr D_{ij}+O(Y_j^5/X_i^3),
\qquad
\boxed{\sum_{i,j}(\mathscr T_{ij}-\mathscr D_{ij})
=O(\ell^5T^{-1/2}).}
\tag{17b}
\]
**Proof.** Fix \(h,d_1,d_2\). The conditions \(d_1\mid m\), \(d_2\mid m+h\), and \(m\) odd are compatible precisely when \((d_1,d_2)\mid h\). Then they select one class modulo \(2[d_1,d_2]\), since both divisors are odd and \(h\) is even. Set \(D=[d_1,d_2]\le Q^2\). The weight
\(f(m)=F_{ij}(m,h)\log(m/d_1)\log((m+h)/d_2)\)
has amplitude \(O(1/X)\) and its first three derivatives are bounded by that amplitude times the respective powers of \(X^{-1}\), using \(\log X\asymp\ell\). Poisson summation, with three integrations by parts at nonzero frequencies, gives
\[
\sum_{m\equiv a\ (2D)}f(m)=\frac1{2D}\int f(m)dm
+O\!\left(X^{-1}(D/X)^2\right).
\tag{17c}
\]
The original factor two cancels the two in the principal denominator. There are at most \(Q^2\) divisor pairs and \(O(Y)\) shifts, so the absolute error is
\(O(YQ^6/X^3)=O(Y^5/X^3)\). This used no Möbius cancellation. Summing \(Y^5\) geometrically up to \(Y\ll(32\ell)X/T\), and then \(X^2\) geometrically up to \(8U\), gives
\(O(\ell^5U^2/T^5)=O(\ell^5T^{-1/2})\).
All derivatives are fixed-order, and all boundaries are the original smooth boundaries. \(\square\)

The finite main \(\mathscr D_{ij}\) has not been replaced by a pointwise singular-series asymptotic. Lemma 2 proves a precise arithmetic evaluation with summable error, not positivity of the off-diagonal packet form. It cannot be applied to a true prime coefficient by differentiating that coefficient as if it were smooth.

The three-factor mixed range is also insufficient for the full natural packets: \(Q=Y^{2/3}\le X^{1/4-\delta}\) would require \(Y\le X^{3/8-3\delta/2}\), while \(Y=X^{1-1/\alpha}\) has exponent at least \(3/7>3/8\). These are specific source-range and error-budget limitations, not claims that every possible divisor method fails.

R26 already dealt with its estimable mixed and singleton terms by completing the smooth shift variable *before* applying centered prime estimates. Replacing that sharper calculation by (12), or by (15), weakens the error ledger and does not estimate the covariance left in (6).

## 5. The exact positive Hilbert identity, and its direction

The original positive arithmetic measure is
\[
d\mu_T(\lambda,x)=\frac T{\ell^2}e^{-\lambda}
\omega(\log x/\ell)\frac{dx}{x^2}\,d\lambda,
\quad x\ge1,\quad\lambda\ge0.
\tag{18}
\]
Let
\[
U_T(\lambda,x)=\Psi(e^{\lambda/T}x)-\Psi(x)
-(e^{\lambda/T}-1)x.
\]
Then \(\|U_T\|_{L^2(\mu_T)}^2=\overline V_T\) **exactly**, with real endpoints and the continuum center intact.

For any one fixed finite cutoff \(R=R(T)\), define the legitimate interval feature
\[
V_R(\lambda,x)=
\sum_{x<n\le e^{\lambda/T}x} A_R(n)
-(e^{\lambda/T}-1)x.
\tag{19}
\]
For each fixed \(T>2\), these functions are square-integrable: the finite divisor coefficients give at most a constant depending on \(R,T\) times \(xe^{\lambda/T}(1+\lambda)\), and the \(x\)-window is compact. No infinite prime Dirichlet series is being used. For every real coefficient \(a\),
\[
\boxed{\overline V_T
=2a\langle U_T,V_R\rangle-a^2\|V_R\|^2
+\|U_T-aV_R\|^2.}
\tag{20}
\]
Consequently, if \(V_R\ne0\), even *exactly known* mixed and pure moments imply only
\[
\overline V_T\ge
\frac{|\langle U_T,V_R\rangle|^2}{\|V_R\|^2}.
\tag{21}
\]
The same statement holds for finitely many legitimate interval features: with Gram matrix \(G\) and mixed vector \(v\),
\[
\overline V_T=v^*G^\dagger v+\|U_T-PU_T\|^2.
\tag{22}
\]
Here \(P\) is the orthogonal projection onto their span. The Moore–Penrose inverse is well defined, and \(v\) lies in the range of \(G\), because every null Gram combination is the zero feature. This is an ordinary finite-dimensional Hilbert identity, not an asserted conditioning bound for a numerical inversion.

There is also an exact Gram kernel for the interval indicators. For positive integers \(m,n\), Tonelli gives
\[
\begin{aligned}
K_T(m,n)
&=\int 1_{x<m,n\le e^{\lambda/T}x}\,d\mu_T\\
&=\frac T{\ell^2}\max(m,n)^{-T}
\int_1^{\min(m,n)}\omega(\log x/\ell)x^{T-2}dx\\
&=b_T(\min(m,n))
\left(\frac{\min(m,n)}{\max(m,n)}\right)^T.
\end{aligned}
\tag{23}
\]
This explains the normalization and the factor two for the ordered off-diagonal sum. It does not remove the continuum-centered terms in (20).

The actual global coefficient is different: it assigns \(Q_j\) according to the pair separation through \(\beta(h/Y_j)\). It is not one sequence \(\Lambda-A_R\) inside all intervals in (19). Nor is a single off-diagonal packet a positive Gram form: any symmetric matrix with zero diagonal and one positive off-diagonal entry has the corresponding principal minor
\[
\begin{pmatrix}0&f\\f&0\end{pmatrix},\qquad f>0,
\tag{24}
\]
whose eigenvalues are \(f,-f\). The R26 shift packets exclude the diagonal. Thus their nonnegative edge weights do not establish positive semidefiniteness of the quadratic form. This is a finite linear-algebra obstruction, not a fake point-process model.

A scale-indexed family of interval features can be studied, but its cross-scale Gram terms must then be proved and retained. No claim that their projection equals (6) follows from the scalar partition of the shift variable.

## 6. The remaining new input, stated with its sign

For a genuine fixed-cutoff comparison (20), suppose one has an estimate of
\(B_T=2a\langle U_T,V_R\rangle-a^2\|V_R\|^2\)
within error \(\epsilon_T\). An upper bound requires an **upper** estimate for
\(\|U_T-aV_R\|^2\), with sufficient absolute accuracy to make
\[
\liminf_T\{B_T+\|U_T-aV_R\|^2\}\le1.
\tag{25}
\]
For example, along a common subsequence an upper bound \(L_T\) for that residual and an upper approximation \(\widetilde B_T+\epsilon_T\) would give
\(\overline V_T\le\widetilde B_T+\epsilon_T+L_T\).
Positivity supplies the opposite direction and cannot replace \(L_T\). Existing RH boundedness of the true variance is not a strict improvement by itself.

For the *actual* cutoff family, the most direct missing estimate remains a signed bound for the finite covariance (6), namely
\[
\liminf_T 2\sum_{i,j}\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F_{ij}(m,h)c_{Q_j}(m)[\Lambda(m+h)-2]
\le1-2M.
\tag{26}
\]
The concrete results of this audit are Lemma 1 and the summable pure-divisor evaluation in Lemma 2, together with the exact distinction (8), mixed sign witness (10), and the upper-versus-lower separation (20)–(26). None estimates (26). A new useful mixed-moment theorem must either give a summably precise upper bound for a legitimate residual energy, or prove signed cancellation in (26); merely evaluating the classical one-prime mixed main does not do so.

## 7. Sources and validation scope

Primary sources checked:

1. Goldston–Yildirim, *Higher correlations of divisor sums related to primes I: triple correlations*, [arXiv:math/0111212v1](https://arxiv.org/pdf/math/0111212v1): definition (1.1), Theorem 1.3/1.4, and the progression mechanism in Section 4. Its direct small-shift formulation is not extrapolated to the global cutoffs.
2. Goldston–Yildirim, *Higher correlations of divisor sums related to primes II: variations of the error term in the prime number theorem*, [arXiv:math/0412366v1](https://arxiv.org/pdf/math/0412366v1): definition of \(\lambda_R\), Theorem 2 on printed page 8, and equations (4.9), (5.6) on printed pages 19–21. Only the unconditional mixed-correlation input and its stated errors are used, not the later GRH fluctuation theorem.
3. The retained [short-gaps primary paper](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), Propositions 2.12 and 2.15: below-one-half progression bounds with common smooth weights and endpoint suprema.

The source receipt pins the PDFs/text and the read R26/R24 dependencies. The tiny checker verifies exact cutoff algebra, signs, rational exponents and the finite polarization identity. It is not a prime scan, an asymptotic experiment, a proof of a new correlation estimate, or a numerical upper enclosure for (26).
