# A power improvement for a smooth packet of the actual shifted discrepancy

Date: 2026-09-05. Status: an elementary completion bound for an identified component of the Round 9 discrepancy. It improves the triangle-inequality bound by a power of X, but remains too large to imply a zeta covariance theorem.

Let \(X=T^\alpha\), \(6/5\le\alpha\le7/5\), \(H=X/T\), and \(Q=X^{523/1000}\). For the actual complementary squarefree modulus family \(\mathcal Q_X\subset(X^{1/2},Q]\) from Round 9, the smooth packet defined below satisfies

\[
\boxed{|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{HX(X+Q^2)}\,(\log X)^4.}
\tag{1}
\]

Estimate (1) itself does not use RH. RH enters only when this discrepancy estimate is combined with the Round 9 aggregate covariance identity.

Thus, writing \(H=X^\theta\),

\[
|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll X^{1023/1000+\theta/2}(\log X)^4,
\qquad \frac16\le\theta\le\frac27.
\tag{2}
\]

Compared with the previously available \(HX\log^{-A}X\), the exponent improves by \(\theta/2-23/1000\), at least \(181/3000=0.060333\ldots\), before logarithmic factors. This is a nontrivial bound for the **actual discrepancy**, not an estimate for a substituted positive model.

However, (2) divided by \(X\log X\) still grows as a power. No bound of the required size \(o(X\log X)\) follows. The gain uses squarefreeness and the modulus cap; it does not yet exploit triple dense divisibility beyond establishing that the prescribed family is admissible. No novelty claim is made for the completion or finite-spacing argument.

## 1. The exact packet and source relationship

Keep the Round 9 discrepancy convention

\[
\Delta(f;a\bmod q)=\sum_{m\equiv a\;(\bmod q)}f(m)
-\frac1{\varphi(q)}\sum_{(m,q)=1}f(m).
\]

Fix \(V\in C_c^\infty(1,2)\) and \(\chi\in C_c^\infty(1,3/2)\), and put

\[
w_h(u)=\chi(u/X)a_u(X)a_{u+h}(X)
\operatorname{sinc}_0\!\left(T\log(1+h/u)\right),
\]
\[
a_u(X)=\min\{(u/X)^{1/2},(X/u)^{3/2}\},\qquad
\operatorname{sinc}_0(v)=\sin(v)/v,\quad \operatorname{sinc}_0(0)=1.
\]

The object in (1) is

\[
\mathfrak D_{\mathcal Q}^{V}(X,T)
=\sum_{h\in\mathbb Z}V(h/H)
\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}\mu(q)
\Delta\!\left(
\Lambda(m)w_h(m-h)\log((m-h)/q);
h\bmod q\right).
\tag{3}
\]

Each sequence inside \(\Delta\) is defined to be zero off its indicated support; there is no logarithm of a nonpositive argument. This is the actual Round 9 weighted discrepancy, with one additional smooth shift cutoff \(H<h<2H\). We assume the fixed hard-cutoff constant in that round is at least two. No claim about the entire unsmoothed shift range is hidden in this localization.

The modulus family and its validity are inherited from [OpenAI, *Improved short gaps between primes*, 30 August 2026](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf): Proposition 2.3, pp.4–5; equation (2.5), p.7; and Corollary 2.19, p.11. Round 9 checks \(\omega=3/250,\delta=\varepsilon=1/1000\), giving \(240\omega+80\delta=2.96<3\) and the cap \(X^{.523}\). That source's modulus sum gives only the \(HX\log^{-A}X\) bound after a shift triangle inequality. All additional analytic estimates needed for (1) are proved below.

In fact the completion argument applies to any squarefree subset of \((X^{1/2},Q]\). It does not assert a new distribution estimate for triply densely divisible moduli.

## 2. Replace von Mangoldt by genuine primes inside this discrepancy

Let \(\vartheta_*(m)=\log m\) when m is prime, and zero otherwise. Replacing \(\Lambda\) by \(\vartheta_*\) in (3) changes it by

\[
O_\eta\!\left(HX^{1/2+\eta}\log^3X+H\sqrt X\log^4X\right)
\tag{4}
\]

for every fixed \(\eta>0\).

For the progression term, a prime power \(m=p^j\asymp X\), \(j\ge2\), contributes only when \(q\mid m-h\). For each h there are at most \(\tau(m-h)\ll_\eta X^\eta\) possible q. The weights cost \(O(\log X)\), and
\(\sum_{p^j\asymp X,j\ge2}\log p\ll\sqrt X\log^2X\).
Summing over h proves the first bound in (4).

For the principal term, bound the h-sum by O(H), retain the coprimality restrictions or enlarge by absolute values, and use \(\sum_{q\le Q}1/\varphi(q)\ll\log X\). This gives the second bound. Thus both portions of the discrepancy are controlled; one cannot replace \(\Lambda\) in only its progression sum.

Taking, for example, \(\eta=1/100\), (4) is \(o(X\log X)\) throughout \(H\le X^{2/7}\), and is smaller than the right side of (1). This is nuisance removal, not the source of the power improvement.

Every remaining prime m satisfies \(m\asymp X>Q\). It is therefore a unit modulo every q under consideration, which makes the following completion exact.

## 3. Exact completion for a separated weight

First replace the smooth two-variable amplitude by \(f(m/X)v(h/H)\), where f,v are smooth with fixed compact supports and m is restricted to primes near X. The logarithmic factor depending on q is handled in Section 6.

Write \(e(z)=e^{2\pi iz}\) and

\[
S_v(\beta)=\sum_{h\in\mathbb Z}v(h/H)e(-\beta h),
\quad
A_f(\beta)=\sum_{p}\log p\,f(p/X)e(\beta p).
\tag{5}
\]

For any integer m,

\[
\sum_{h\equiv m\;(\bmod q)}v(h/H)
=\frac1q\sum_{r=0}^{q-1}S_v(r/q)e(rm/q).
\tag{6}
\]

Also, with the Ramanujan sum \(c_q(r)=\sum_{b\bmod q,(b,q)=1}e(rb/q)\),

\[
\sum_{(h,q)=1}v(h/H)
=\frac1q\sum_{r=0}^{q-1}S_v(r/q)c_q(r).
\tag{7}
\]

In the progression term, \((h,q)=1\) is automatic because m is a prime exceeding q. In the principal term it remains exactly the unit sum in (7). Consequently the completed separated discrepancy is

\[
\sum_{q\in\mathcal Q_X}\frac{\mu(q)}q
\sum_{r=0}^{q-1}S_v(r/q)
\left(A_f(r/q)-\frac{c_q(r)}{\varphi(q)}A_f(0)\right).
\tag{8}
\]

Reduce \(r/q=a/d\). Since q is squarefree and \(d=q/(q,r)\),

\[
\frac{c_q(r)}{\varphi(q)}=\frac{\mu(d)}{\varphi(d)}.
\tag{9}
\]

This ratio is independent of the larger modulus q. The d=1 term vanishes identically. Regrouping (8) by distinct reduced fractions gives

\[
\sum_{\substack{2\le d\le Q\\1\le a<d,\ (a,d)=1}}
C_{a/d}\,Z_f(a/d),
\tag{10}
\]

\[
C_{a/d}=S_v(a/d)\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q,
\quad
Z_f(a/d)=A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0).
\tag{11}
\]

Distinct representations of the same rational frequency must be merged before applying a finite-spacing estimate. Treating all r/q as distinct would be incorrect.

## 4. A quantitative norm for the completed coefficients

The elementary bound

\[
\left|\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q\right|
\le\frac{1+\log(Q/d)}d
\tag{12}
\]

does not assume cancellation of the Möbius coefficients.

Finite summation by parts, applied J times to the compactly supported sequence \(v(h/H)\), gives

\[
|S_v(\beta)|\ll_{v,J}
H(1+H\|\beta\|)^{-J}.
\tag{13}
\]

One can prove (13) directly: the J-th finite difference has total absolute mass \(O_{v,J}(H^{1-J})\), and its Fourier transform is multiplied by \((e(\beta)-1)^J\). Combine that estimate with the trivial O(H) bound. No convergence of a critical-strip Dirichlet series is involved.

For J=2,

\[
\sum_{a=1}^{d-1}|S_v(a/d)|^2
\ll_v
\begin{cases}
d^4/H^2,&d\le H,\\
Hd,&d\ge H.
\end{cases}
\tag{14}
\]

This follows by measuring distance to the endpoints a=0,d; the relevant convergent series is \(\sum_{a\ge1}a^{-4}\). Dropping the coprimality restriction only enlarges this upper bound. Equations (12)–(14) prove

\[
\sum_{d,a}|C_{a/d}|^2\ll_v H(\log(2Q))^3.
\tag{15}
\]

For the coefficient with \(\mu(q)\log q/q\) in place of \(\mu(q)/q\), the same proof gives \(O_v(H\log^5(2Q))\). These explicit norms replace the H-fold triangle inequality.

## 5. The required finite-spacing estimate, proved directly

The reduced fractions \(a/d\), \(d\le Q\), are distinct and separated on the unit circle by at least \(Q^{-2}\). For a consecutive integer interval of length \(N\ll X\), the Gram matrix of their exponential vectors has diagonal N and off-diagonal absolute values at most

\[
\min\!\left(N,\frac1{2\|\beta-\beta'\|}\right).
\]

Order the distances in either direction around the circle. Separation bounds the absolute row sum by

\[
N+O(Q^2\log(2Q)).
\]

The Schur bound and matrix duality therefore give the finite inequality

\[
\sum_{\beta}\left|\sum_n b_n e(\beta n)\right|^2
\ll(X+Q^2\log(2Q))\sum_n|b_n|^2.
\tag{16}
\]

For \(b_p=(\log p)f(p/X)\) at primes and zero otherwise, Chebyshev's bound gives
\(\sum|b_n|^2\ll_f X\log X\) and \(A_f(0)\ll_f X\).
The constant-centering portion of (11) has total squared mass at most

\[
|A_f(0)|^2\sum_{d\le Q}\frac{\mu(d)^2}{\varphi(d)}
\ll_f X^2\log(2Q).
\]

Combining this with (16),

\[
\sum_{d,a}|Z_f(a/d)|^2
\ll_f X(X+Q^2)(\log X)^2.
\tag{17}
\]

The logarithm in the spacing row sum has been retained. Using the prime-supported coefficient norm, rather than the cruder norm of all integers weighted by log, is also needed for the displayed logarithmic bookkeeping.

Cauchy–Schwarz in (10), with (15) and (17), now bounds the separated discrepancy by

\[
\ll_{f,v}\sqrt{HX(X+Q^2)}(\log X)^{5/2}.
\tag{18}
\]

The version with \(\log q\) costs one more logarithm.

## 6. The actual m/h kernel, including the logarithm

Put \(\epsilon=H/X=1/T\), \(y=m/X\), and \(z=h/H\). The amplitude of (3), apart from the logarithm and the prime weight, is

\[
F_\epsilon(y,z)=
V(z)\chi(y-\epsilon z)\,
y^{-3/2}(y-\epsilon z)^{-3/2}
\operatorname{sinc}_0\!\left(
\frac1\epsilon\log\frac{y}{y-\epsilon z}\right).
\tag{19}
\]

The cutoff ensures that both a-factors are on their \(u>X\) branch. The apparently singular phase is actually

\[
\frac1\epsilon\log\frac y{y-\epsilon z}
=\int_0^z\frac{du}{y-\epsilon u}.
\tag{20}
\]

It extends smoothly to z/y at \(\epsilon=0\). Every fixed mixed derivative of (19) is uniformly bounded on a fixed compact rectangle for sufficiently small epsilon. The same holds after multiplying by \(\log(y-\epsilon z)\).

Choose fixed smooth cutoffs slightly larger than that rectangle and expand the resulting functions in a two-variable Fourier series. Repeated integration by parts gives coefficients \(b_{k,\ell}\) satisfying, uniformly in epsilon,

\[
\sum_{k,\ell}|b_{k,\ell}|(1+|\ell|)^J<\infty
\]

with a common bound for any fixed J. Each term separates into a function of m/X and a function of h/H. The m-factor has uniformly bounded sup norm; the derivatives of the h-factor grow at most polynomially in \(\ell\), absorbed by the displayed coefficient sum. Thus (18) is summable over this expansion. This is a proved separation of the actual amplitude, not its replacement by a product approximation with an unspecified error.

Finally,

\[
\log((m-h)/q)=\log X-\log q+\log(y-\epsilon z).
\tag{21}
\]

The first term costs \(\log X\), the second uses the \(\log q\) coefficient norm after (15), and the third is another uniformly smooth amplitude. Their common upper bound is

\[
O_{V,\chi}\!\left(\sqrt{HX(X+Q^2)}(\log X)^4\right).
\]

Together with the smaller prime-power error (4), this proves (1).

## 7. Nontriviality, limitations, and the next mathematical obstruction

At \(\theta=1/6\), the exponent in (2) is \(3319/3000=1.106333\ldots\), compared with the triangle exponent \(7/6\). At \(\theta=2/7\), it is \(8161/7000=1.165857\ldots\), compared with \(9/7\). These are power improvements, not merely changes to logarithmic factors.

They still exceed one. Under RH, inserting (1) into the Round 9 aggregate identity leaves an error larger than \(X\log X\); the negligible \(H\sqrt X\log^4X\) nuisance there does not change that conclusion.

The now-specific place needing further arithmetic input is the pairing

\[
\sum_{d,a}
S_v(a/d)
\left(\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q\right)
\left(A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)\right),
\tag{22}
\]

and its \(\log q\) and smooth-amplitude variants. A proof reaching the covariance scale must improve this actual pairing beyond the elementary coefficient-norm and spacing bounds, for example by exploiting the complementary modulus restrictions inside the coefficient sum together with the prime exponential sums. The 186 coherent-class estimate by itself supplies no such cross-frequency cancellation.

This is a location of missing arithmetic information, not a proof that no sharper completion argument can work. No further reparameterization or generic positivity test was performed.

## 8. Exact checks and provenance

The companion **check_shift_completion.py** verifies with exact rational/integer arithmetic the Ramanujan ratio (9), regrouping by reduced denominators, the cancellation of the zero frequency, and all stated power exponents. Its finite toy modulus families test algebra, not prime-distribution asymptotics. The script records the hashes of this report and the frozen Round 9 report/source files.

The estimates (12)–(18) and the actual-kernel passage are ordinary written proofs. No floating-point experiment is being used to assert a power saving. The report does not claim to settle the unsmoothed full discrepancy, the complementary divisor remainder, AH, or Montgomery's conjecture.
