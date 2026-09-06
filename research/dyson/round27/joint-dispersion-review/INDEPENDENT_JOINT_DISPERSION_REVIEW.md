# Independent review of the R27 joint cofactor dispersion test

Date: 2026-09-05. Reviewer: Plato (`residual_gram`), independent of author Euclid. Status: ordinary mathematical and primary-source review accepted after the coefficient-sequence terminology correction described below. The exact final author hash and independent replay results are pinned in `REVIEW_RECEIPT.json`. No author file or preceding research round was edited by the reviewer.

The reviewed work is `../joint-dispersion-test/JOINT_DISPERSION_TEST.md`, final SHA256 `c7ac888dc3da29d770c7b17562a0264371ec65c62f241d3e6b5c0f1b6f107942` (17,690 bytes). Acceptance means that the displayed central-band removal, finite matrix identities, source-valid bounds and limitations follow under their stated hypotheses. It does **not** mean that the desired prime matrix bound, a strict Bragg deficit, a refutation of AH, or a Dyson–Montgomery conjecture has been proved.

## 1. Verdict and the one corrected source distinction

I read the complete author proof, the complete finite checker, its source manifest, and the relevant parts of the frozen R25/R26 dependencies. I independently rederived the normalization and seven completion errors of the central-band argument, the actual odd-endpoint mean-square conversion, the coefficient-sequence Siegel–Walfisz property, and the finite matrix inequalities. I also checked the retained primary extracts and visually inspected the supplied pages containing Montgomery–Vaughan (17.12)–(17.14), CCCC (1.3), and the 186 paper's Proposition 2.18.

The initial author version, SHA256 `c7012e375b62263ec472dcb45e362caebca6d8719fe5080c7476a1f4b0d94e5b`, called both factor sequences “divisor-bounded coefficient sequences.” This is inaccurate in the primary paper's strict terminology: Definition 2.5 permits a fixed power of the divisor function alone, whereas Definition 2.6 additionally permits a fixed power of \(\log X\). The sequence \(\beta(k)=\log k\) is not divisor-bounded in the Definition 2.5 sense, since at primes the divisor function equals two. It is a coefficient sequence in the Definition 2.6 sense. Proposition 2.18 requires the latter, so the stated application is valid after this wording correction. The final pin in the receipt records the author-authorized replacement; no mathematical formula was changed for this correction.

The accepted result with new arithmetic content is
\[
Z(X^{1/3})-Z(X^{49/100})
=O\bigl(X^{-1/100}(\log X)^3\bigr)
\]
on the actual central compact packet \(X=T^2\), \(Y=T\). It removes a signed band of genuine divisor/cofactor rows, retaining the prime and flat-center terms together. The remaining exact matrix formulation is useful for specifying the missing estimate, but is not itself a new estimate.

## 2. Scope, actual support and normalization

The author keeps
\[
F(m,h)=b_T(m)\chi(m/X)V(h/Y)
\left(\frac m{m+h}\right)^T,
\quad X=T^2,\quad Y=T,\quad \ell=\log T,
\]
with fixed real compact smooth profiles supported strictly inside \((1,2)\). Thus \(m\asymp X\), \(h\asymp Y\), and \(m+h\in(X,3X)\) for all sufficiently large \(T\). All sums in this note are finite, the physical shifts are even, and both prime endpoints are odd. There is no unannounced removal of prime powers.

The R21/R26 mass kernel obeys, for every fixed order,
\[
b_T^{(j)}(m)=O_j(m^{-j-1}\ell^{-2}).
\]
For example, write its integral using \(x=mu\); the resulting integral has mass \(1/(T-1)\), and the external factor is \(T\). Differentiation in \(m\) does not create an uncontrolled power of \(T\). In the scaled variables \(m=Xv\), \(h=Yz\), the Pareto factor is
\[
(1+z/(Tv))^{-T},
\]
whose derivatives of any fixed order are uniformly bounded on these fixed supports. Consequently \(F\) has amplitude \(O((X\ell^2)^{-1})\), derivative scales \(X\) in \(m\) and \(Y\) in \(h\). The same physical shift scale applies to \(F(n-h,h)\) at fixed \(n\).

The exact finite coefficient is
\[
c_Q(m)=\sum_{d\mid m,\ d>Q}\mu(d)\log(m/d).
\]
No smooth divisor cutoff or condition \((d,m/d)=1\) is inserted. The covariance has the actual flat parity center
\[
Z(Q)=2\sum_{m\ \mathrm{odd},\ h\ \mathrm{even}}
F(m,h)c_Q(m)[\Lambda(m+h)-2].
\]
The factor two is retained throughout. These conventions are necessary for both the completion constants and the matrix calculation.

The corresponding central R26 dyadic blocks have scale ratios in fixed compact sets. Rescaling the smooth profiles preserves the derivative bounds above. The R26 high-height and large-shift cutoffs are identically one there for sufficiently large \(T\). This observation does not justify applying the argument at the bottom polylogarithmic shift scales, and the author correctly makes no such claim.

## 3. Independent audit of the removable central band

Let \(Q_1=X^{1/3}\), \(Q_2=X^{49/100}\), and define
\[
a_{\mathrm{band}}(m)=
\sum_{Q_1<d\le Q_2,\ d\ \mathrm{odd}}
\frac{\mu(d)}d\log(m/d).
\]
The difference of the two complementary divisor sums is exactly the finite sum on this band, with a plus sign. Real cutoff endpoints cause no difficulty because the same inequalities are kept throughout.

### 3.1 The genuine prime part and primitive mean

For each odd \(d\) and unit \(n\bmod d\), the mean-zero discrepancy on the even physical lattice is
\[
1_{n\equiv h\pmod d}
-\frac{1_{(h,d)=1}}{\varphi(d)},
\qquad h\in2\mathbb Z.
\]
The unit factor \(1_{(n,d)=1}\) is retained when this expression is used. On the period in \(r=h/2\), each Fourier coefficient has absolute value at most \(2/d\): the sum of the absolute masses of the point indicator and the normalized unit indicator is at most two. Poisson summation with 61 derivatives gives the fixed-order bound needed for the author's exponent 60. This avoids an extra erroneous factor of \(d\).

With weight \(F(n-h,h)\log((n-h)/d)\), amplitude \(O((X\ell^2)^{-1}\log X)\), and Chebyshev's bound for the full von Mangoldt sum, the band discrepancy is
\[
O\left(\frac{Q_2}{\log X}(Q_2/Y)^{60}\right).
\]
No derivative is applied to a prime coefficient, and no phase-twisted Siegel–Walfisz assertion is used.

For the principal part, inclusion–exclusion on \((h,d)=1\) and even-lattice Poisson summation give the mean factor \(\varphi(d)/(2d)\). Its factor two cancels the external two in the covariance. The \(1/\varphi(d)\) in the primitive principal is preserved before cancellation, and the resulting error after the actual divisor sum is
\[
O((Q_2/Y)\log^3X).
\]
The remaining mean is
\[
\sum_{n\ \mathrm{odd}}\Lambda(n)
\int F(n-h,h)a_{\mathrm{band}}(n-h)\,dh.
\]

Removing the unit restriction on \(n\) from this mean is a distinct operation. A nonunit prime weight has \(n=p^j\), \(j\ge2\), since \(p\mid d\le Q_2<X<n\). The divisor-weight sum over \(p\mid d\) is bounded by \(O(\log(2Q_2)/p)\). The full nonunit mean is therefore \(O(Y\log X/X)\).

The original nonprimitive progression rows also force \(n=p^j\), \(p\mid h\). Writing \(h=2pr\), the actual compact support gives at most \(Y/p\) possible positive integers \(r\). This holds even if \(Y<p\), when the interval is empty; there is no hidden rounding cost. Bounding the remaining divisor coefficient by \(O_\eta(X^\eta\log X)\), and using \(\sum_{p\le z}\log p/p=O(\log(2z))\), yields \(O_\eta(X^\eta Y/X)\). The stated choice \(\eta=1/100\) is legal. These arguments keep all higher prime powers rather than treating primality and von Mangoldt support as interchangeable.

### 3.2 The flat center and the necessary cofactor saving

The negative term is exactly
\[
-4\sum_{Q_1<d\le Q_2,\ d\ \mathrm{odd}}\mu(d)
\sum_{k\ \mathrm{odd}}\log k
\sum_{h\ \mathrm{even}}F(dk,h).
\]
Even-lattice completion produces the factor \(1/2\). The sum of absolute divisor coefficients needed only for its error is \(O(X\log^2X)\), so the physical lattice error is \(O(Y^{-1})\).

Put \(J(m)=\int F(m,h)dh\). For each fixed \(d\), the smooth cofactor function \(\log k\,J(dk)\) has scale \(X/d\), not scale \(Y\). Two integrations by parts in its Fourier transform give an error
\[
O\left(\frac{Y\log X}{X\ell^2}\frac dX\right).
\]
The odd-lattice mean is \(1/(2d)\) after changing variables to \(m=dk\). It follows, with the sign retained, that the entire flat term is
\[
-\int J(m)a_{\mathrm{band}}(m)dm
+O\left(Y^{-1}+\frac{YQ_2^2}{X^2\log X}\right).
\]
This is the author's formula (9). A variation bound without the factor \(d/X\) would not establish this error; the smooth cofactor completion is substantive.

### 3.3 RH is applied after cancellation of the large constants

The primary RH Möbius input, retained from Soundararajan, is the fixed-exponent bound \(M(x)=O_\epsilon(x^{1/2+\epsilon})\). It also gives the odd Möbius partial-sum bound because
\[
M_{\mathrm{odd}}(x)=\sum_{j\ge0}M(x/2^j).
\]
The odd Dirichlet series is \(((1-2^{-s})\zeta(s))^{-1}\). Its simple zero at \(s=1\) has derivative two, so the corresponding logarithmic mean is exactly
\[
a_Q(m)=2+O_\epsilon(Q^{-1/2+\epsilon}\log X).
\]
Both occurrences of two cancel in \(a_{\mathrm{band}}=a_{Q_2}-a_{Q_1}\). The derivative bound is obtained at fixed divisor cutoffs; differentiating a moving cutoff would be a different and invalid operation here.

The combined prime and flat means are exactly
\[
\sum_{n\ \mathrm{odd}}\Lambda(n)G(n)-\int G(y)dy,
\quad
G(n)=\int F(n-h,h)a_{\mathrm{band}}(n-h)dh.
\]
The amplitude plus total variation of \(G\) is
\[
O_\epsilon\left(
\frac{YQ_1^{-1/2+\epsilon}\log X}{X\ell^2}
\right).
\]
The ordinary RH bound for \(\Psi\), subtracting the actual powers of two for the odd version, now gives
\[
O_\epsilon((Y/\sqrt X)Q_1^{-1/2+\epsilon}\log X).
\]
There is no RH estimate for an uncanceled constant-size coefficient here. This ordering is the reason the argument succeeds.

At \(\epsilon=1/100\), the powers of \(X\) in the seven errors, in order, are
\[
-11/100,\ -1/100,\ -1/2,\ -49/100,
\ -1/2,\ -13/25,\ -49/300.
\]
Their logarithmic factors are exactly those recorded by the author. The largest bound is \(O(X^{-1/100}\log^3X)\). I accept Lemma 1 with its stated central-packet scope. The surviving ranges include both balanced factors and arbitrarily small odd cofactors; the vanishing of \(k=1\) comes only from \(\log1=0\).

## 4. The exact prime matrix and the direction of its estimates

For a true rectangular factor block with product cutoff preserved, the author defines
\[
f_T(m)=X\ell^2\sum_{h\ \mathrm{even}}
F(m,h)[\Lambda(m+h)-2]
\]
on odd \(m\), and zero on even \(m\). The latter convention is essential, since two is the center on odd endpoints, not an all-integer center. With
\[
C_{d,k}=f_T(dk),\quad a_d=\mu(d),\quad b_k=\log k,
\]
the finite identity
\[
Z_{D,K}=\frac{2}{X\ell^2}a^{\mathsf T}Cb
\]
is exact. Equal products from different factor pairs remain equal entries; they are not independent samples.

For this real matrix, ordinary Cauchy gives
\[
|Z_{D,K}|^2\le
\frac{4\|a\|_2^2}{X^2\ell^4}
b^{\mathsf T}C^{\mathsf T}Cb.
\]
Bounding \(\|a\|_2^2\ll D\), \(\|b\|_2^2\ll K\log^2(2K)\), and using \(DK\asymp X\), proves formula (17). In particular the displayed bound
\[
\|C\|_{\mathrm{op}}^2\ll X(\log X)^{2-\delta}
\]
would suffice to make a balanced block tend to zero. The vector-specific condition in author (19) is weaker and also sufficient. Neither follows from the algebra.

I checked the primary Montgomery–Vaughan derivation directly: (17.12) keeps the exact Gram form; (17.13) replaces it by absolute row sums; (17.14) is the corresponding Schur bound. Thus the author's (27) is legal. The source's discussion on the following page also distinguishes the actual fixed coefficient vectors from a norm bound uniform over all vectors. There is no direction reversal or tacit probabilistic assumption in the author's use.

Expanding each Gram entry retains
\[
\Lambda(dk+h)\Lambda(dk'+h')
-2\Lambda(dk+h)-2\Lambda(dk'+h')+4.
\]
Both singleton terms and the constant are necessary. The relation
\[
k'(dk+h)-k(dk'+h')=k'h-kh'
\]
is exact. The off-diagonal problem therefore concerns actual simultaneous affine prime forms in one common divisor variable. The fact that a Gram matrix is positive semidefinite supplies no small upper bound for this expression.

## 5. Independent conversion of the RH short-interval input

CCCC printed page 1, equation (1.3), states under RH that for fixed \(1<\beta\le4\),
\[
\int_1^{S^\beta}
[\Psi((1+1/S)x)-\Psi(x)-x/S]^2\frac{dx}{x^2}
=O_\beta(\log^2S/S).
\]
The author uses only \(\beta=3\). This is inside the explicitly stated range. The following source remark about larger fixed exponents is unnecessary. The inputs here have \(S\asymp T\), \(x\asymp X=T^2<S^3\) for large \(T\), including every fixed compact dilation used below.

For odd integer \(m\), let
\[
A_m(y)=\sum_{0<h\le y,\ h\ \mathrm{even}}
[\Lambda(m+h)-2].
\]
The exact comparison to the all-integer prefix is
\[
A_m(y)=\Psi(m+y)-\Psi(m)-y
-\sum_{m<2^j\le m+y}\log2
+y-2\lfloor y/2\rfloor.
\]
The last term is bounded by two, and the powers-of-two term is uniformly \(O(\log X)\). All endpoints are real except the explicitly integral \(m\); the displayed inequalities are the actual counting convention.

The weight \(X\ell^2F(m,y)\) has bounded amplitude, derivative \(O(Y^{-1})\), and compact support in \(y\asymp Y\). Partial summation followed by Cauchy therefore bounds
\[
|f_T(m)|^2\ll
Y^{-1}\int_{cY}^{CY}|A_m(y)|^2dy
\]
for fixed positive \(c,C\). There are no boundary terms outside this compact support.

For \(x\in[m,m+1]\), replacing \(m\) by \(x\) in each uncentered prefix changes at most a fixed number of integer terms, of total weight \(O(\log X)\). Squaring and summing contributes \(O(X\log^2X)\). We may then estimate the corresponding double integral over real \(x\asymp X\), \(y\asymp Y\). Make the change
\[
\lambda=Ty/x,\qquad dy=(x/T)d\lambda.
\]
The new variable lies in a fixed compact subinterval of \((0,\infty)\). For each fixed \(\lambda\), the discrepancy has the form in the primary theorem with the single fixed parameter \(S=T/\lambda\). We first use that theorem, then integrate over \(\lambda\). Since \(x/T\asymp Y\), the outside factor \(Y^{-1}\) is absorbed. Removing the weight \(x^{-2}\) costs \(O(X^2)\). Hence
\[
\sum_{m\asymp X,\ m\ \mathrm{odd}}|f_T(m)|^2
\ll X^2\log^2T/T
\ll XY\log^2X.
\]
This independently proves author (23). Inserting \(S=m/y\) pointwise into an integral theorem would not be legal; the author correctly avoids that mistake.

The exact Frobenius identity includes product multiplicity
\[
\|C\|_{\mathrm F}^2
=\sum_m r_{D,K}(m)|f_T(m)|^2,
\qquad r_{D,K}(m)\le\tau(m).
\]
It gives \(\|C\|_{\mathrm{op}}^2\ll_\eta X^{1+\eta}Y\log^2X\), hence only \(|Z_{D,K}|\ll_\eta X^{1/4+\eta/2}\) at the central scale. This is a valid but weak local estimate. It is not a contradiction to the independently inherited global \(O(1)\) bound, and it is not a proof that the actual local block has this size. The missing operator saving is a factor of order \(X^{1/2}\) in the squared norm, apart from the stated divisor and logarithmic losses.

## 6. The exact legal 186 application, and what it does not imply

The retained source distinguishes divisor-bounded families (Definition 2.5) from coefficient sequences allowing a fixed logarithmic factor (Definition 2.6). The corrected \(\alpha,\beta\) in author (28) satisfy Definition 2.6 and the required scale conditions. Their product interval is contained in \((X,1.21X]\), so support at scale \(X\) is genuine. Sharp interval endpoints are permitted for coefficient sequences.

I independently checked Definition 2.9 for the untwisted odd logarithmic sequence. For a small modulus \(q\), a primitive residue \(a\bmod q\), and arbitrary auxiliary \(s\), expand the restriction \((k,s)=1\), retaining the odd condition. Counting the resulting compatible arithmetic progressions and using partial summation leaves endpoint error \(O(\tau(qs)^2\log X)\). The principal densities agree. If \(q\) is even, a primitive residue is already odd; if \(q\) is odd, the parity density one-half occurs in both the progression and its unit mean. Primes common to \(q\) and \(s\) are redundant on both sides. This accounts for all auxiliary moduli, not just a fixed \(s\).

For \(q>\log^{L+3}X\), direct counting bounds the discrepancy by
\[
O((K/q+1)\log X+K\log X/\varphi(q)).
\]
Using \(q/\varphi(q)\le\tau(q)\) and \(K=\sqrt X\), this is absorbed by \(O_L(\tau(qs)^2K\log^{-L}X)\). The divisor exponent two is fixed independently of the requested saving \(L\). This elementary argument proves the exact untwisted SW property without RH, GRH, or a prime-distribution theorem.

Proposition 2.18 requires coefficient sequences, \(MN\asymp X\), \(X^{1/2-\sigma}\le N\le X^{1/2}\), and this SW property. At the author's choices, its three left sides are exactly
\[
48/125,\qquad82/125,\qquad27/50,
\]
all less than one. The fixed retreat gives the level \(X^{509/1000}\). Formula (30) also retains the full source definition of \(\mathcal E_3\): squarefree moduli dividing one \(P_I\), the triply densely divisible condition, and one coherent primitive residue system fixed outside the modulus sum. It does not replace that system by independent maxima. The principal remains the exact unit-restricted sum divided by \(\varphi(q)\).

Thus (30) is a legal application of the cited primary result. This acceptance does not independently reprove that source's deep distribution theorem; it checks that the present coefficients, quantifiers and support meet its stated hypotheses.

The difference between that conclusion and the desired weighted two-prime expression is correctly stated. Multiplication by the second prime indicator \(\Lambda(m+h)\) is neither a progression restriction supplied by (30), nor a common smooth weight of Proposition 2.12. The existing theorem cannot simply be applied after inserting it. A sieve upper bound for that indicator is also not automatically an upper bound after multiplication by the signed convolution coefficient. The finite witnesses at 253 and 345 really have the displayed opposite signs in the stated factor rectangle; these certify this order obstruction only, not an asymptotic lower bound.

Finally, using an actual prime cofactor \(k=p\asymp\sqrt X\) as the source modulus does not meet even single dense divisibility at parameter \(X^{1/1000}\). In Definition 2.1, take \(U=\sqrt p\). This is inside the allowed range for both \(p\) and \(2p\). For large \(X\), the interval \([U/X^{1/1000},U]\) contains neither divisor of \(p\), and none of \(1,2,p,2p\). Therefore the claimed obstruction to directly using the full cofactor family is real. PNT gives the stated \(K\log K\) squared-log coefficient mass of these prime cofactors. It says nothing about the sign or size of their joint prime pairing, and the author does not use it to claim such a bound.

## 7. Verification receipt and accepted limits

The independent reproducibility step copies only the final author Markdown and its small checker into a temporary directory, runs the checker there, and retains its JSON and stdout in this review folder. The replay is compared byte-for-byte with the final author outputs. It does not rerun a large eigenproblem, scan high primes, or numerically test any conjectural matrix norm. The six groups cover two actual integer coefficient signs, the finite joint Gram/Cauchy algebra, nine centered-product identities, four source parameter assertions, five exact exponent margins, and four small dense-divisor illustrations: 26 scalar cases in total.

The copied replay passed all 26 scalar cases; its JSON and stdout are byte-identical to both final author outputs, SHA256 `f34d05dbdb8a5523ac973b3bdd8d08560f2e1b27a4a1e3a8f1439f623dc92709`. All 15 source/dependency files and all six files listed in the final author receipt match their recorded byte lengths and SHA256 hashes. I verified that the final author body differs from the earlier pinned body only by the one terminology replacement above. The final review receipt pins the author revision, checker, replay, source checks and review itself. The syntax check only verifies LaTeX delimiters, KaTeX parsing and absence of unexpected control bytes. These finite checks support reproducibility; the asymptotic result rests on the ordinary proof audited above.

I accept the central signed cutoff improvement and the exact matrix reduction. I accept the source-valid Frobenius estimate and the explicitly restricted 186 application. I do not infer a strict bound for the remaining balanced or unbalanced covariance, the bottom physical scales, the aggregate of all R26 packets, or the actual frequency-two Bragg atom. The precise remaining task is an estimate for the centered affine-prime Gram pairing, such as author (19), together with the other surviving ranges if one aims at the global target. No famous conjecture is settled by this checkpoint.
