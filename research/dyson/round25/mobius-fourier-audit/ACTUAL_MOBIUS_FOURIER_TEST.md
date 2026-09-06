# An actual Möbius–prime Fourier test: a removable zero core and an unresolved annulus

Date: 2026-09-05. Author: Aquinas. Status: ordinary analytic feasibility proof submitted for independent review. The finite Fourier identity is unconditional. Bounds explicitly marked RH use ordinary RH for the Riemann zeta function. No GRH, phase-twisted Siegel–Walfisz assertion, strict variance bound, or new Montgomery theorem is assumed or proved.

## 1. The exact coefficient and the two parameter regimes

Keep the unchanged continuum weight and physical packet
\[
\ell=\log T,\quad X=T^\alpha,\quad H=X/T,\quad
Q=X^\rho,\quad K=2X/Q,
\]
\[
b_T(m)=\frac{Tm^{-T}}{\ell^2}
\int_1^m\omega(\log x/\ell)x^{T-2}\,dx,
\quad
F(m,h)=b_T(m)\chi(m/X)V(h/H)(1+h/m)^{-T}.
\tag{1}
\]
Here \(\omega\ge0\) is fixed, smooth and supported on \([7/4,9/4]\); the fixed real cutoffs \(\chi,V\) belong to \(C_c^\infty((1,2))\). We treat either
\[
\text{old range: }\rho=523/1000,\quad11/5\le\alpha\le9/4,
\]
or
\[
\text{new range: }\rho=2/5,\quad7/4\le\alpha\le9/4.
\tag{2}
\]
All statements are uniform on these closed ranges as real \(T\to\infty\).

For odd \(m\), use the actual complementary coefficient
\[
c_Q(m)=\sum_{\substack{d\mid m\\d>Q}}\mu(d)\log(m/d),
\]
and its parity-centered covariance
\[
Z_Q^{(2)}=2\sum_{\substack{m\text{ odd}\\h\text{ even}}}
F(m,h)c_Q(m)[\Lambda(m+h)-2].
\tag{3}
\]
All sums are finite, all prime powers remain in \(\Lambda\), and both cutoffs are fixed. The sharp condition \(d>Q\) is never smoothed away.

In the old range, the frozen R24 proof (23) identifies its primitive covariance \(Z_Q\) with (3), after paying its raw nonprimitive term and the full primitive-center comparison. That comparison uses \(K/H\to0\). **We do not apply it in the new range**, where \(K/H\to\infty\). The object (3) is nevertheless exact in both ranges; it is the appropriate coefficient for testing the new proposed joint-main reduction independently of whether that reduction has been proved.

This note does not delete the earlier primitive principal, the Möbius-linear main or either singular-series prime marginal. The unresolved arithmetic combination must still be assembled with those terms, unless a separate proof evaluates their sum to the required additive accuracy.

## 2. Exact finite Fourier identity for the actual smooth weight

Write \(e(u)=e^{2\pi i u}\), \(v=m/X\), \(z=h/H\), and set
\[
a_T(v,z)=X\ell^2 b_T(Xv)\chi(v)V(z)
\left(1+\frac{z}{Tv}\right)^{-T}.
\tag{4}
\]
The function is extended by zero outside \((1,2)^2\). Every fixed mixed derivative is uniformly bounded. This follows from the exact integral for \(b_T\) in R23 (22), whose derivative bounds do not lose powers of \(T\), and from differentiating \(-T\log(1+z/(Tv))\) on the fixed compact support. The assertion remains uniform for the enlarged range of \(\alpha\) in (2).

Expand only the \(v\) variable with period four:
\[
a_T(v,z)=\sum_{j\in\mathbb Z}a_{T,j}(z)e(jv/4),\qquad
a_{T,j}(z)=\frac14\int_0^4 a_T(v,z)e(-jv/4)\,dv.
\tag{5}
\]
For every fixed pair of integers \(B,r\ge0\),
\[
\|\partial_z^r a_{T,j}\|_\infty
\ll_{B,r}(1+|j|)^{-B}.
\tag{6}
\]
Every coefficient has support in the same fixed compact subset of \((1,2)\). Thus all series below converge absolutely, and polynomial costs in \(j\) are summable. Equation (5) represents the actual weight, not a substitute product packet.

Choose one fixed smooth \(\zeta_0\in C_c^\infty((1/2,4))\), equal to one on \([1,3]\). This notation is a cutoff, not the Riemann zeta function. For \(3\le k<K\), \(k\) odd, put \(D_k=X/k\) and
\[
\begin{aligned}
M_{k,j}(\theta)&=
\sum_{\substack{d\text{ odd}\\d>Q\\D_k<d<2D_k}}
\mu(d)e\left(-kd\theta+\frac{jkd}{4X}\right),\\
P(\theta)&=\sum_{n\text{ odd}}[\Lambda(n)-2]
\zeta_0(n/X)e(n\theta),\\
W_j(\theta)&=\sum_{h\text{ even}}a_{T,j}(h/H)e(-h\theta).
\end{aligned}
\tag{7}
\]
The artificial open bounds on \(d\) merely enforce \(X<kd<2X\); the full Fourier series vanishes at the original compact-support endpoints. The auxiliary cutoff \(\zeta_0\) equals one whenever \(n=kd+h\) can contribute, because then \(X<n<3X\).

Orthogonality of integer Fourier modes gives the exact identity
\[
\boxed{
Z_Q^{(2)}=\frac2{X\ell^2}
\sum_{\substack{3\le k<K\\k\text{ odd}}}\log k
\sum_{j\in\mathbb Z}\int_{-1/2}^{1/2}
M_{k,j}(\theta)P(\theta)W_j(\theta)\,d\theta.
}
\tag{8}
\]
Indeed the Fourier integral imposes exactly \(n=kd+h\), and (5) reconstructs \(F\). There is no coprimality condition between \(k\) and \(d\). The original coefficient \(\mu(d)\log k\) is unchanged.

Both \(M\) and \(P\) change sign under \(\theta\mapsto\theta+1/2\), whereas \(W\) is unchanged. Their product therefore has period \(1/2\). Equivalently, (8) has prefactor \(4/(X\ell^2)\) if the integration interval is the cell \(\mathcal I=[-1/4,1/4]\). This accounts for the half-integer aliases without treating them as independent new major arcs.

Poisson summation on the even shifts, followed by a fixed number of integrations by parts, yields on this cell, for every fixed \(B,J\),
\[
|W_j(\theta)|\ll_{B,J}
(1+|j|)^{-B}H(1+H|\theta|)^{-J}.
\tag{9}
\]
The transform has rapidly decaying tails; it is not compactly supported at \(|\theta|=1/H\).

## 3. A primary uniform Möbius estimate and what it actually gives

Tao's author-written Notes 8, Theorem 8, states Davenport's estimate
\[
\sup_{\beta\in\mathbb R}
\left|\sum_{n\le Y}\mu(n)e(n\beta)\right|
\ll_A Y(\log Y)^{-A}
\quad(A>0\text{ fixed}),
\tag{10}
\]
with ineffective constants. The same source proves it through its major/minor-arc decomposition. This is an estimate of the true Möbius sequence. Its uniformity in \(\beta\) is a theorem, rather than a presumed twisted Siegel–Walfisz property.

The odd restriction is legal: \(1_{n\text{ odd}}=(1-e(n/2))/2\). Subtracting two ordinary prefixes treats any real interval contained in \([D_k,2D_k]\), including the sharp lower cutoff \(Q\). Because \(D_k\ge Q/2\) on nonempty rows, \(\log D_k\asymp\log X\), uniformly in both ranges. Hence
\[
\sup_\theta |M_{k,j}(\theta)|
\ll_A D_k(\log X)^{-A},
\tag{11}
\]
uniformly also in \(j\); the shifted phase in (7) causes no variation loss in this estimate.

For the centered prime transform we use the actual RH small-arc estimate of Bhowmik–Schlage-Puchta, Lemma 3, printed page 3:
\[
\int_{-1/y}^{1/y}
\left|\sum_{n\le x}(\Lambda(n)-1)e(n\theta)\right|^2d\theta
\ll(x/y)(\log x)^4,\qquad1\le y\le x.
\tag{12}
\]
Weighted partial summation on the fixed support of \(\zeta_0\) implies
\[
\int_{-r}^{r}|P(\theta)|^2d\theta
\ll Xr(\log X)^4,\qquad X^{-1}\le r\le1/4.
\tag{13}
\]
Here is the parity and prime-power check. The exact coefficient difference between \(1_{n\text{ odd}}(\Lambda(n)-2)\) and \(\Lambda(n)-1\) is
\[
(-1)^n-1_{n\text{ even}}\Lambda(n).
\]
After multiplication by \(\zeta_0(n/X)\), its Fourier transform on \(|\theta|\le1/4\) is \(O(\log X)\): the alternating smooth integer sum has rapid decay there, while the even prime powers are powers of two and there are only a bounded number in \([X/2,4X]\). All other prime powers remain in (12). For the smallest radii, use (12) at the enclosing radius \(2/X\); all partial-summation prefix lengths are then at least \(X/2\). This gives (13) without invoking a theorem outside its \(y\)-range.

Dyadic integration of (13) against (9), together with the RH pointwise prefix bound for the tiny interval \(|\theta|<X^{-1}\), gives
\[
\int_{\mathcal I}|W_j(\theta)||P(\theta)|^2d\theta
\ll_B(1+|j|)^{-B}X(\log X)^4,
\quad
\int_{\mathcal I}|W_j(\theta)|d\theta
\ll_B(1+|j|)^{-B}.
\tag{14}
\]
For the tiny interval one can instead use (13) at radius \(1/X\); its contribution is \(O(H(\log X)^4)\), at most the displayed bound. Thus no pointwise prime estimate is needed for (14). Cauchy–Schwarz gives the weighted prime \(L^1\) bound \(O_B((1+|j|)^{-B}\sqrt X(\log X)^2)\), after relabeling \(B\).

Since \(\sum_{k<K}(\log k)D_k\ll X(\log X)^2\), equations (8), (11), and (14) prove, under RH,
\[
\boxed{|Z_Q^{(2)}|\ll_A\sqrt X(\log X)^{-A}
\qquad(A>0\text{ fixed}).}
\tag{15}
\]
The arbitrarily large fixed logarithmic saving cannot remove this positive power. In fact (15) is weaker asymptotically than the already audited Selberg/Cauchy bound
\[
|Z_Q^{(2)}|\ll\sqrt H(\log X)^{3/2}.
\tag{16}
\]
The R24 proof of (16) uses \(\sum|c_Q|^2\ll X\log^5X\), a fixed \(\beta=3\) RH Selberg theorem, \(H=X/T\), and \(X\le T^{9/4}\). It does not use \(K<H\) or the value \(\rho=523/1000\), so the same proof applies in the new range. There the power in (16) ranges from \(3/14\) to \(5/18\). Neither bound controls the covariance at \(O(1)\).

Even a hypothetical uniform square-root estimate \(|M_{k,j}|\ll_\eta D_k^{1/2}X^\eta\), used in this factorwise argument, would give only \(O_\eta(\sqrt K X^\eta\log X)\). This is an explanation of the loss in this particular inequality, not a claimed Möbius theorem or a lower bound for the true covariance. Cancellation between the factors and between cofactor rows has not been used.

## 4. Ordinary RH does remove the genuine zero-frequency core

Let \(1\le R\le X/8\), and define \(Z_{\rm core}(R)\) by the exact cell version of (8), restricted to \(|\theta|\le R/X\). Ordinary RH implies, for every fixed \(\eta>0\),
\[
M(Y):=\sum_{n\le Y}\mu(n)\ll_\eta Y^{1/2+\eta},
\qquad \Psi(Y)-Y\ll\sqrt Y(\log Y)^2.
\tag{17}
\]
For source precision, only the standard RH bounds recorded in Ng's introduction, printed pages 5–6, are used here. We do **not** invoke his Theorem 1 or its additional negative-moment hypothesis.

The odd Möbius prefix has the same bound: if \(M_o(Y)=\sum_{n\le Y,\,n\text{ odd}}\mu(n)\), the exact relation
\(M(Y)=M_o(Y)-M_o(Y/2)\) gives
\(M_o(Y)=\sum_{a\ge0}M(Y/2^a)\), a geometrically bounded sum. Partial summation with the actual linear phase, retaining both sharp interval endpoints, yields
\[
|M_{k,j}(\theta)|\ll_\eta
D_k^{1/2+\eta}(1+X|\theta|+|j|).
\tag{18}
\]
The phase length is \(D_k k|\theta|=X|\theta|\), not \(D_k|\theta|\). Similarly, the odd centered prime prefix equals \(\Psi(Y)-Y\) minus the powers-of-two prefix plus a bounded parity discrepancy. Smooth partial summation therefore gives
\[
|P(\theta)|\ll\sqrt X(\log X)^2(1+X|\theta|).
\tag{19}
\]
No nonprincipal Dirichlet character occurs in (18)–(19).

Using (9), the core length \(2R/X\), and
\(\sum_{k<K}(\log k)D_k^{1/2+\eta}\ll_\eta X^{1/2+\eta}\sqrt K\log X\), we obtain
\[
\boxed{|Z_{\rm core}(R)|
\ll_\eta\frac{\sqrt K}{T}X^\eta
R(1+R)^2\log X.}
\tag{20}
\]
The polynomial \(|j|\) cost is absorbed by the rapid decay in (6); no Fourier-series truncation is necessary. This also treats the equivalent half-integer core in the original full circle.

For any fixed \(B>0\), take \(R=(\log X)^B\). The worst powers of \(\sqrt K/T\), uniformly in (2), are
\[
\begin{array}{c|c}
\rho=523/1000& X^{-3707/18000}\text{ up to the constant }\sqrt2\\
\rho=2/5& X^{-13/90}\text{ up to the constant }\sqrt2.
\end{array}
\tag{21}
\]
Choosing any fixed \(\eta\) smaller than the relevant positive exponent proves \(Z_{\rm core}((\log X)^B)=o(1)\). This is a genuine estimate for a piece of the actual finite Fourier identity. It neither supplies a prime-density main at other rational points nor establishes a sign for the remainder.

## 5. A legal tail cutoff and the remaining frequency region

Let \(U=X^{1/100}\). Both ranges have \(U/H\to0\). Define \(Z_{\rm tail}(U)\) from (8) on the cell \(|\theta|>U/H\). Chebyshev gives \(|P(\theta)|\ll X\) globally, and the trivial bound is \(|M_{k,j}|\le2D_k\). Equation (9) with the single fixed choice \(J=202\) implies
\[
\boxed{|Z_{\rm tail}(U)|\ll XU^{1-J}
=X^{-101/100}=o(1).}
\tag{22}
\]
This pays the entire transform tail without pretending the physical cutoff has compact Fourier support, without choosing a derivative order that grows with \(T\), and without relying on logarithmic decay to beat a positive power.

For fixed \(B\), equations (20)–(22) isolate the exact remaining integral:
\[
\boxed{
Z_Q^{(2)}=
\frac4{X\ell^2}\sum_{\substack{3\le k<K\\k\text{ odd}}}\log k
\sum_j\int_{\substack{\theta\in\mathcal I\\
(\log X)^B/X<|\theta|\le X^{1/100}/H}}
M_{k,j}(\theta)P(\theta)W_j(\theta)\,d\theta+o(1).
}
\tag{23}
\]
All coefficients, the parity center and the sharp \(d>Q\) boundary remain actual. The essential frequencies \(|\theta|\asymp1/H\) lie in this annulus. A sufficient condition for this packet covariance to be \(o(1)\) is that its unnormalized signed integral and cofactor sum be \(o(X\ell^2)\). Such a condition is not supplied by (10), (12), or their factorwise combination. A strict bound for the complete arithmetic target may require less than \(Z_Q^{(2)}=o(1)\), but it must still account for the other main terms and a proved packet partition.

There is an important distinction between the two ranges. For the central Fourier mode \(j=0\), the old range has \(K/H\ll X^{-753/11000}\); its basic mean-scale Möbius phases \(k\theta\) are small. The new range has
\[
K/H=2T/Q=2X^{1/\alpha-2/5},\qquad
1/\alpha-2/5\in[2/45,6/35].
\tag{24}
\]
Thus actual cofactor resonances \(\theta=1/k\) for \(k\asymp K\) lie inside the mean-scale Fourier band. More generally \(k\theta=a/q\) can have a small nonzero rational denominator even while \(|\theta|\lesssim1/H\). The rapid mode shifts in (7) must also be retained in an exact arc decomposition; they do not invalidate the uniform estimates above.

At \(k\theta\in\mathbb Z\), the Möbius factor alone is controlled by its ordinary RH prefix. The accompanying prime transform is at \(\theta=1/k\), rather than zero. At other rational Möbius phases, nonprincipal character sums also appear. Ordinary RH for \(\zeta\) does not supply the square-root bounds for those Dirichlet-character objects, and the constant two in (3) is not an evaluated rational-arc prime main. Davenport's theorem remains valid there but saves only arbitrary fixed logarithms. This identifies a concrete legal range in which a naive zero-core RH calculation cannot be extended; it is not an assertion that a nonzero rational arc has a proved positive lower contribution.

The result of this feasibility test is therefore limited but precise: the genuine zero core and sufficiently remote Fourier tails can be removed, while the actual cofactor-weighted Möbius–prime integral on (23) remains uncontrolled at the fluctuation scale. A joint arithmetic estimate is still required; this note provides neither a generic-model obstruction nor another unproved heat-flow transfer.

## 6. Sources and verification scope

- Terence Tao, [Notes 8: the Hardy–Littlewood circle method and Vinogradov's theorem](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/), Theorem 8 and its proof: uniform Davenport bound for the actual Möbius sum. Constants are ineffective.
- Bhowmik–Schlage-Puchta, [Mean representation number of integers as the sum of primes](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/Goldbach4.2.10.pdf), Lemma 3, printed page 3: the centered RH small-arc bound. The retained original source is used, not a substitute uncentered prime estimate.
- Nathan Ng, [The distribution of the summatory function of the Möbius function](https://www.cs.uleth.ca/~nathanng/RESEARCH/mobius2b.pdf), introduction, printed pages 5–6: standard ordinary-RH bounds for \(M\) and \(\Psi-\mathrm{id}\), separately from the paper's stronger conditional theorems.
- Frozen programme dependencies: R23 exact packet/derivative proof and R24 small-cofactor Sections 3 and 6. The adjacent receipt pins the precise files.

The small checker only verifies rational scale exponents. No prime heights, divisor families or frequency grids are sampled. All finite identities, mode convergence, endpoint handling and asymptotic inequalities are ordinary proofs requiring independent review. Original source and previous-round bytes remain unchanged.
