# Completing a genuine one-prime component in the upper-wing even-pair packet

Date: 2026-09-05. Author: Euclid. Status: ordinary proof submitted for independent review. All estimates proved in this note are unconditional. RH is needed only for the inherited identification of the full parity-adjusted target with the actual zeta/prime variance. This is a classical smooth-period completion applied to a newly checked component of this programme; no novelty, strict variance bound, or AH refutation is claimed.

## 1. Result and exact scope

Keep the final singleton-renormalization definitions
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},\quad
W_T(x)=\omega(\log x/\ell),
\]
\[
b_T(m)=\frac{T m^{-T}}{\ell^2}\int_1^m W_T(x)x^{T-2}dx,\qquad
k_T(m,h)=\left(\frac m{m+h}\right)^T.
\tag{1}
\]
The fixed function \(\omega\) is smooth, nonnegative, and supported in \([7/4,9/4]\). Extend it by zero. Choose fixed real \(\chi,V\in C_c^\infty((1,2))\). They can be nonnegative, but the estimates do not require that. Set
\[
X=T^\alpha,\quad H=X/T,\quad Q=X^\rho,\quad
\rho=\frac{523}{1000},\qquad
\frac{11}{5}\le\alpha\le\frac94.
\tag{2}
\]
Thus
\[
\frac HQ\ge X^{247/11000}.
\tag{3}
\]
Use the exact weight
\[
F_T(m,h)=b_T(m)\chi(m/X)V(h/H)k_T(m,h).
\tag{4}
\]
The corresponding piece of the actual parity-adjusted quadratic target is
\[
\mathcal P_{T,X}^{\chi,V}
=2\sum_{\substack{m\ {\rm odd}\\ h\ge2,\ h\ {\rm even}}}
F_T(m,h)\{\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\}.
\tag{5}
\]
No singleton or continuous-center term has been removed from (5).

Let \(\mathcal D_X\) be the **entire odd part** of the fixed canonical complementary-modulus family in Section 2. Its divisor coefficient below is exactly \(\mu(d)\), not \(1/d\), \(1/\varphi(d)\), a sieve majorant, or a freely chosen replacement.

The exact decomposition in Section 3 is
\[
\boxed{\mathcal P_{T,X}^{\chi,V}
=\mathcal B_{\mathcal D}+\mathcal A_{\mathcal D}
+\mathcal N_{\mathcal D}+\mathcal C_{\mathcal D}
-\mathcal M_{\mathfrak S}.}
\tag{6}
\]
Here \(\mathcal B_{\mathcal D}\) is a primitive centered one-prime progression term, \(\mathcal A_{\mathcal D}\) is its full primitive principal term, \(\mathcal N_{\mathcal D}\) is the nonprimitive part, \(\mathcal C_{\mathcal D}\) contains the complementary divisors in the exact von Mangoldt identity, and \(\mathcal M_{\mathfrak S}\) contains both singular-series-weighted prime marginals and their constant two.

**Theorem.** Uniformly in the closed range (2), as real \(T\to\infty\),
\[
\boxed{|\mathcal B_{\mathcal D}|
\ll_{\omega,\chi,V}\frac{X^{-7/440}}{\log X},\qquad
|\mathcal N_{\mathcal D}|
\ll_{\omega,\chi,V}X^{-15041/45000}.}
\tag{7}
\]
Consequently
\[
\mathcal P_{T,X}^{\chi,V}
=\mathcal A_{\mathcal D}+\mathcal C_{\mathcal D}
-\mathcal M_{\mathfrak S}+o(1).
\tag{8}
\]
This removes two explicitly identified components at the normalized fluctuation scale, including the actual prime powers in the nonprimitive term. It does **not** estimate the signed expression on the right of (8).

The saving comes from \(H>Q\) and a smooth physical shift packet, not from a new prime distribution exponent or from the parity renormalization itself. It does not apply to the earlier range \(X^{1/6}\le H\le X^{2/7}\), where \(H<Q\). The packet has fixed support away from \(h=0\); an extension to every shift of the full target is not asserted.

## 2. The actual complementary family and a useful prime-factor consequence

Put
\[
r=\frac{523}{2000},\quad \beta=\frac{501}{2000},\quad
Y=X^{1/1000}.
\]
The canonical family consists of each distinct squarefree integer \(d=[D,E]\), counted once, for which positive squarefree \(D,E\) satisfy
\[
D,E\le X^r,\quad [D,E]>X^{1/2},
\]
\[
p^{3/2}D_{\ge p}\le X^\beta
\quad(p\mid D,\ p>Y),\qquad
p^{3/2}E_{\ge p}\le X^\beta
\quad(p\mid E,\ p>Y).
\tag{9}
\]
Take \(\mathcal D_X\) to be its odd members. Here \(D_{\ge p}\) denotes the product of prime factors of \(D\) at least \(p\). This is exactly the full family fixed in the R11 conductor report; no selection by the sign of \(\mu(d)\) is made.

One has
\[
X^{1/2}<d\le Q,\qquad d\in\mathcal D^{(3)}(Y).
\tag{10}
\]
Indeed the opposite-root guards follow from (9), and the balanced budgets satisfy \(X^{2\beta}=X^{1/2}Y\). Proposition 2.3 of the 186 source applies with \(f(p)=g(p)=p^{3/2}\). The R11 report also proves this family contains an explicitly counted subfamily with 348 prime factors; nonemptiness is not being inferred from a numerical realization.

A consequence needed here is
\[
\boxed{P^+(d)\le X^\nu,\qquad \nu=\frac{501}{5000}.}
\tag{11}
\]
For \(p>Y\) in either owner, its owner tail is at least \(p\), so \(p^{5/2}\le X^\beta\). Primes at most \(Y\) also satisfy (11). This statement holds for **every** member of the full family, not merely its special 348-prime subfamily.

## 3. Exact switched progression decomposition

For all positive integers \(m\),
\[
\Lambda(m)=\sum_{d\mid m}\mu(d)\log(m/d).
\tag{12}
\]
At \(m=1\), both sides are zero. The formula follows from
\(\log=\mathbf1*\Lambda\) by Möbius inversion and includes all prime powers.

Write \(n=m+h\), and, wherever the compact cutoffs are nonzero, define
\[
w_{n,d}(h)=F_T(n-h,h)\log((n-h)/d).
\tag{13}
\]
It is extended by zero outside that support. In all expressions involving \(d\in\mathcal D_X\), its logarithm has a positive argument greater than one for sufficiently large \(X\), because \(n-h\in(X,2X)\) and \(d\le Q<X\). For complementary divisors, (13) is used only when \(d\mid n-h\).

For an odd integer \(d\), set
\[
K_{d,h}(n)
=1_{(n,d)=1}
\left(1_{n\equiv h\pmod d}-\frac{1_{(h,d)=1}}{\varphi(d)}\right).
\tag{14}
\]
There is an exact identity
\[
1_{n\equiv h\pmod d}
=K_{d,h}(n)
+\frac{1_{(n,d)=1}1_{(h,d)=1}}{\varphi(d)}
+1_{(h,d)>1}1_{n\equiv h\pmod d}.
\tag{15}
\]
It follows by separating the cases \((h,d)=1\) and \((h,d)>1\); congruent integers have the same gcd with \(d\).

The terms in (6) are exactly
\[
\mathcal B_{\mathcal D}
=2\sum_{d\in\mathcal D_X}\mu(d)
\sum_{\substack{n\ {\rm odd}\\h\ {\rm even}}}
\Lambda(n)w_{n,d}(h)K_{d,h}(n),
\tag{16}
\]
\[
\mathcal A_{\mathcal D}
=2\sum_{d\in\mathcal D_X}\frac{\mu(d)}{\varphi(d)}
\sum_{\substack{n\ {\rm odd}\\h\ {\rm even}}}
\Lambda(n)w_{n,d}(h)1_{(n,d)=1}1_{(h,d)=1},
\tag{17}
\]
\[
\mathcal N_{\mathcal D}
=2\sum_{d\in\mathcal D_X}\mu(d)
\sum_{\substack{n\ {\rm odd}\\h\ {\rm even}}}
\Lambda(n)w_{n,d}(h)
1_{(h,d)>1}1_{n\equiv h\pmod d},
\tag{18}
\]
\[
\mathcal C_{\mathcal D}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F_T(m,h)\Lambda(m+h)
\sum_{\substack{d\mid m\\d\notin\mathcal D_X}}
\mu(d)\log(m/d),
\tag{19}
\]
\[
\mathcal M_{\mathfrak S}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F_T(m,h)\mathfrak S(h)
[\Lambda(m)+\Lambda(m+h)-2].
\tag{20}
\]
All these are finite sums because of \(\chi,V\). The shift support is positive; writing all even integers in (16)–(20) is harmless. Equations (12) and (15) prove (6) with no endpoint errors. In particular the \(\mathfrak S(h)\) factors in (20) are not replaced by their average.

## 4. Derivative control for the true weight

For every fixed nonnegative integer \(j\),
\[
|b_T^{(j)}(m)|\ll_{\omega,j}m^{-j-1}\ell^{-2},
\qquad T\ge4.
\tag{21}
\]
To see the uniformity in \(T\), use the exact integral
\[
b_T(m)=\frac{T}{m\ell^2}
\int_0^1
\omega((\log m+\log u)/\ell)\,u^{T-2}du.
\tag{22}
\]
Differentiating \(j\) times produces only derivatives of the fixed \(\omega\), powers of \(m^{-1}\), and nonpositive powers of \(\ell\). The integral mass is \(1/(T-1)\); it does not produce a factor \(T^j\).

At fixed \(n\), use \(z=h/H\), \(v=(n-h)/X\). On the support, \(1<z,v<2\), and the exact Pareto factor is
\[
k_T(n-h,h)=\left(1+\frac{z}{Tv}\right)^{-T}.
\tag{23}
\]
Every fixed-order derivative in \(z,v\) is uniformly bounded for \(T\ge4\). For example \(-T\log(1+z/(Tv))\) and each of its fixed derivatives are uniformly bounded there. At fixed \(n\), \(dv/dz=-1/T\). Combining this with (21), the compact cutoffs, and
\(\log((n-h)/d)=\log X-\log d+\log v\), gives
\[
\boxed{
\sup_h|\partial_h^j w_{n,d}(h)|
\ll_{\omega,\chi,V,j}
\frac{\log X}{X\ell^2}H^{-j}.
}
\tag{24}
\]
Its support has length at most \(H\), and all boundary derivatives vanish. The constants are uniform in \(n,d,\alpha,T\) in the stated ranges.

The variation in \(n\), with \(h\) fixed, is likewise at scale \(X\), not \(H\). This matters in the source comparison in Section 7. Neither (23) nor (24) replaces the Pareto kernel by an exponential.

## 5. Smooth completion on the physical even shifts

Here is the elementary completion statement with its parity factor explicit. Let \(d\) be odd, let \(n\) be a unit modulo \(d\), and let
\(a\equiv 2^{-1}n\pmod d\). If \(h=2r\), then
\[
K_{d,2r}(n)=1_{r\equiv a\pmod d}
-\frac{1_{(r,d)=1}}{\varphi(d)}.
\tag{25}
\]
Its sum over any full period in \(r\) is exactly zero.

Use \(\widehat w(\xi)=\int_{\mathbb R}w(h)e(-\xi h)\,dh\),
\(e(t)=e^{2\pi i t}\). Poisson summation on the grids
\(h=2a+2d\mathbb Z\) and \(h=2r+2d\mathbb Z\), \((r,d)=1\), gives
\[
\boxed{
\sum_{h\ {\rm even}}w(h)K_{d,h}(n)
=\frac1{2d}\sum_{k\ne0}
\widehat w\left(\frac{k}{2d}\right)
\left(e(ka/d)-\frac{c_d(k)}{\varphi(d)}\right),
}
\tag{26}
\]
where \(c_d(k)=\sum_{(r,d)=1}e(kr/d)\). The \(k=0\) coefficient vanishes exactly. The factor is \(1/(2d)\), not \(1/d\); the primitive principal remains \(1/\varphi(d)\), not \(1/d\). If \((n,d)>1\), both sides of the desired bound vanish because of (14).

Put \(A_X=\log X/(X\ell^2)\). Repeated integration by parts in the compact support, using (24), yields, for every fixed \(J\ge1\),
\[
|\widehat w(\xi)|
\ll_J A_X H(1+H|\xi|)^{-J-1}.
\]
Also \(|c_d(k)|\le\varphi(d)\). When \(H\ge d\), (26) therefore gives
\[
\left|\sum_{h\ {\rm even}}w_{n,d}(h)K_{d,h}(n)\right|
\ll_J A_X(d/H)^J.
\tag{27}
\]
Indeed \(H d^{-1}\sum_{k\ge1}(1+Hk/(2d))^{-J-1}
\ll_J(d/H)^J\); the constants depend on the fixed order, not on \(d,H\).

The support forces \(X<n<2X+2H<3X\). Chebyshev's bound
\(\sum_{n\le3X}\Lambda(n)\ll X\) includes every prime power. Since
\(|\mu(d)|\le1\) and \(|\mathcal D_X|\le Q\), (16) and (27) imply
\[
\boxed{
|\mathcal B_{\mathcal D}|
\ll_J \frac{\log X}{\ell^2}\sum_{d\in\mathcal D_X}(d/H)^J
\ll_J \frac{Q}{\log X}(Q/H)^J.
}
\tag{28}
\]
There is no hypothesis on the phase of a prime sequence and no use of a phase-twisted Siegel–Walﬁsz assertion.

For the closed range (2), choose the fixed integer \(J=24\). Then
\[
24\left(\frac6{11}-\frac{523}{1000}\right)
-\frac{523}{1000}=\frac7{440}>0.
\tag{29}
\]
This proves the first estimate in (7).

More generally, fix
\[
\alpha_0>\frac{1000}{477},\qquad
\alpha_0\le\alpha\le\frac94.
\]
Choose any fixed \(J\) with
\[
J(1-1/\alpha_0-\rho)>\rho.
\tag{30}
\]
Equation (28) is then \(o(1)\), with a power saving. At the boundary \(H\asymp Q\), this argument does not produce that conclusion. It also does not permit \(J\) to grow with \(T\) while retaining the stated constants.

## 6. The actual nonprimitive prime-power component is also negligible

If a summand of (18) is nonzero, then \(d\mid n-h\),
\((h,d)>1\), and \(\Lambda(n)\ne0\). Hence \(n=p^j\) for a prime \(p\mid d\), and (11) implies \(p\le X^\nu\). In particular \(n\) cannot be a genuine prime in \((X,3X)\).

For each odd prime \(p\), the interval \((X,3X)\) contains at most two powers of \(p\). Thus the number of possible \(n\)'s is at most \(2X^\nu\). For fixed \(n,h\), the absolute sum over participating \(d\)'s is bounded by
\[
\sum_{d\mid n-h}|\mu(d)|\,|\log((n-h)/d)|
\le\tau(n-h)\log(2X).
\tag{31}
\]
For every fixed \(\eta>0\), \(\tau(m)\ll_\eta m^\eta\). One elementary proof bounds \(e+1\le p^{\eta e}\) for all sufficiently large primes \(p\), while the finitely many smaller primes each contribute a bounded factor
\(\sup_{e\ge0}(e+1)p^{-\eta e}\).

There are \(O(H)\) allowed \(h\)'s for each \(n\), \(\Lambda(n)\le\log(3X)\), and \(|F_T(m,h)|\ll (X\ell^2)^{-1}\). Therefore
\[
\boxed{
|\mathcal N_{\mathcal D}|
\ll_{\eta,\omega,\chi,V}
H X^{\nu-1+\eta}.
}
\tag{32}
\]
The two logarithms from \(\Lambda(n)\) and (31) are absorbed by
\(\ell^2\), since \(\log X=\alpha\ell\) with \(\alpha\) in a fixed compact interval. This is an absolute bound on the actual term, not a substitution of primes for \(\Lambda\).

Take \(\eta=1/100\). Since \(H\le X^{5/9}\),
\[
1-\frac59-\frac{501}{5000}-\frac1{100}
=\frac{15041}{45000}>0.
\tag{33}
\]
This proves the second estimate in (7). The prime-factor guard (11) is essential to this particular estimate; it must not be inherited by an arbitrary squarefree family with \(d\le Q\).

## 7. What the 186 distribution theorem does and does not add here

The source's progression discrepancy is equation (2.3), with the primitive subtraction retained. Its equation (2.5) sums absolute discrepancies over a coherent residue class. Proposition 2.10 supplies untwisted prime-interval Siegel–Walﬁsz; Corollary 2.19 treats \(\Lambda\) itself. The source does not supply a phase-twisted prime coefficient in this argument.

For fixed even \(h\), restrict to \(d\in\mathcal D_X\) coprime to \(h\). On odd \(n\), (14) is exactly the discrepancy for the primitive residue modulo \(2d\) determined by
\[
n\equiv h\pmod d,\qquad n\equiv1\pmod2.
\tag{34}
\]
The residues are coherent: remove the odd primes dividing \(h\) from the common prime set, use \(h\) modulo every remaining odd prime, and use \(1\) modulo \(2\). Lemma 2.2 permits the small coprime factor \(2\), so \(2d\) is triply \(Y\)-densely divisible.

There is a legal fixed retreat for the source theorem. For example take
\[
\varpi=\frac{29}{2500},\quad \delta=\frac1{1000},
\quad \epsilon_{\rm src}=\frac1{10000}.
\]
Then
\[
240\varpi+80\delta=\frac{358}{125}<3,\qquad
\frac12+2\varpi-\epsilon_{\rm src}=\frac{5231}{10000}>\rho.
\tag{35}
\]
Thus \(2Q\) lies below the source cutoff for all sufficiently large \(X\). Split the \(n\)-support at \(2X\); the hypotheses persist on the second dyadic interval. This is a genuine legal per-shift source application in the present new height range.

For its smooth weight, split
\(\log((n-h)/d)=\log(n-h)-\log d\).
The two common \(n\)-profiles have endpoint-plus-variation norm
\(O(\log X/(X\ell^2))\), uniformly for \(H<h<2H\). The factor
\(\log d\) is bounded by \(\log X\) and can be absorbed by choosing a stronger fixed logarithmic saving. This is ordinary weighted partial summation of the source's uniform subinterval estimate.

However, summing that absolute per-shift estimate over the \(O(H)\) shifts gives only
\[
|\mathcal B_{\mathcal D}|
\ll_B H(\log X)^{-B}
\quad\text{for every fixed }B,
\tag{36}
\]
which does not establish \(o(1)\) in (2). Equation (28) improves this particular component by **first completing the physical shift**, using its zero mean, before taking absolute values over primes or moduli. It does not improve the source theorem itself. No Type II hypothesis has been used: (12) is an exact divisor identity, and the switched inner progression involves the original one-prime sequence \(\Lambda(n)\).

## 8. The unresolved expression and the packet boundary

The surviving quantity is exactly
\[
\mathcal R_{\mathcal D}
:=\mathcal A_{\mathcal D}+\mathcal C_{\mathcal D}
-\mathcal M_{\mathfrak S}.
\tag{37}
\]
The principal in (17) contains \(\mu(d)/\varphi(d)\), the true log-cofactor and both primitive masks. The complementary sum (19) is still signed. Neither is a positive remainder, so truncating it does not create a legal inequality.

In particular the new centering at the allowed parity class does not make
\(\mathcal A_{\mathcal D}\) equal to \(\mathcal M_{\mathfrak S}\). Such an identification would require a further arithmetic argument, and the exact coefficients in (17), (19) and (20) have been retained precisely to expose that obligation. The known one-prime theorem does not bound this remaining centered quadratic combination at the fluctuation scale.

This result applies to a genuine smooth piece of the fixed \(b_T k_T\) target, rather than to a different test variance. Uniformly bounded linear combinations of \(O(\log T)\) such packets still have an \(o(1)\) total removed error by (7). This statement alone does not construct a partition of the full target: packets reaching \(h=0\), scales with \(H\le Q\), and complementary height ranges remain outside the proof. A raw half-line cutoff has endpoint terms in Poisson summation and cannot be treated as a compact smooth packet vanishing to all orders at zero.

There is therefore a concrete advance in the bookkeeping of the actual arithmetic target—a source-admitted primitive one-prime part and its actual nonprimitive exception are negligible in the stated upper-wing packets—but no strict inequality for the zeta statistic has been obtained.

## 9. Provenance and reproducibility

Primary source: OpenAI, *Improved short gaps between primes*, 30 August 2026, [official PDF](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf). Relevant locations: printed pp.4–5, Definition 2.1/Lemma 2.2/Proposition 2.3; printed pp.6–8, (2.3)–(2.5), Definition 2.9/Propositions 2.10 and 2.12; printed p.11, Corollary 2.19. The retained PDF/text and programme dependencies are pinned in the adjacent source manifest; third-party papers are not copied into this folder.

Programme dependencies:
- R11, *A real-prime subfamily prevents a coefficient-only power saving*, Section 1, fixes the exact full canonical family, and Sections 2–3 verify and count a genuine subfamily.
- R22, *Removing the full linear singleton correction from the exact Pareto remainder*, defines the unchanged kernel and proves the full signed linear correction is \(o(1)\).
- R22, *A parity-adjusted form of the renormalized pair target*, supplies the exact constant two and the allowed parity classes. This note uses its expression as a definition; its full-variance transfer has the separate dependencies and RH scope described there.

The adjacent small exact checker verifies the rational exponent margins, finite primitive-kernel decomposition, even-grid zero mean, Fourier/Ramanujan coefficients, and the exact divisor decomposition with formal prime logarithms. These are algebra and normalization checks, not experiments with large prime heights, estimates of asymptotic constants, or substitutes for the ordinary proof above.

