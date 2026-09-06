# A concrete 186-to-covariance transfer beyond the square-root divisor level

Date: 2026-09-05. Status: a proved application of a published distribution estimate, an exact divisor decomposition, and an explicit missing shifted estimate. This does **not** improve a zeta pair-correlation bound or prove the Round 8 target.

The 186 input controls an identifiable part of the additive covariance: the correlation of a prime with a selected Möbius–log divisor sum on complementary, triply densely divisible moduli up to \(X^{0.523}\). The error is \(O_A(X\log^{-A}X)\) per shift, uniformly in the relevant range. This saves enough for shift packets of logarithmically bounded total weight, but the proved bound does not save enough after all \(H=X/T\) shifts are accumulated at the fluctuation scale \(X\log X\).

The application uses the ordinary mathematical theorem in the primary paper. It makes no assertion that every assumption in its Lean formalization has been formally discharged.

## 1. Exact primary input

The primary source is [OpenAI, *Improved short gaps between primes*, 30 August 2026](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf). Printed-page locations are:

- Definition 2.1, p.4: the recursive all-allocation class \(\mathcal D^{(r)}(Y)\).
- Lemma 2.2 and Proposition 2.3, pp.4–5: the cubic prime-factor test and complementary conditions for the actual least common multiple \([D,E]\), including shared primes.
- Equation (2.3), p.6: progression discrepancy with its coprime principal term.
- Equation (2.5), p.7: a coherent primitive class outside the modulus sum, uniform also in the prime set and that class.
- Corollary 2.19, p.11, equations (2.15)–(2.16): full-prime/\(\Lambda\) distribution for order three when \(240\omega+80\delta<3\), uniformly on subintervals.
- Proposition 2.18, pp.10–11, equation (2.14): the underlying multiplicative-convolution bilinear estimate, distinguished from the shifted form in Section 7.

The official repository was previously pinned at commit **61340d0b74163003b32756bb16e91d9209a5e330**. The accompanying JSON hashes the local primary PDF and text; neither is changed here.

Choose

\[
\omega=\frac3{250},\qquad \delta=\frac1{1000},\qquad
\varepsilon=\frac1{1000}.
\tag{1}
\]

Then \(240\omega+80\delta=74/25=2.96<3\), and
\(1/2+2\omega-\varepsilon=523/1000\). Thus, for any finite prime set I and one coherent primitive class \(a\bmod P_I\), the source gives

\[
\sum_{\substack{q\le X^{523/1000}\\q\mid P_I\\
q\in\mathcal D^{(3)}(X^{1/1000})}}
|\Delta(\Lambda\mathbf1_J;a\bmod q)|
\ll_A X(\log X)^{-A}
\tag{2}
\]

uniformly for common subintervals \(J\subset[X,2X)\), where

\[
\Delta(f;a\bmod q)=\sum_{m\equiv a\;(\bmod q)}f(m)
-\frac1{\varphi(q)}\sum_{(m,q)=1}f(m).
\tag{3}
\]

This is not a maximum over unrelated classes inside the modulus sum.

## 2. A complementary modulus family above the square-root range

Use Z for the threshold called X in Proposition 2.3. Set

\[
Y=X^{1/1000},\quad Z=X^{1/2},\quad
A_0=B_0=X^{501/2000},\quad f(p)=g(p)=p^{3/2}.
\tag{4}
\]

Let \(\mathcal Q_X\) be any set of distinct \(q=[D,E]\), with D,E positive and squarefree, satisfying

\[
\begin{gathered}
D,E\le X^{523/2000},\qquad [D,E]>X^{1/2},\\
p^{3/2}D_{\ge p}\le X^{501/2000}\quad(p\mid D,\ p>Y),\\
p^{3/2}E_{\ge p}\le X^{501/2000}\quad(p\mid E,\ p>Y).
\end{gathered}
\tag{5}
\]

The opposite-root guards are automatic because the functions and budgets agree and each owner tail is at least one. Moreover \(A_0B_0=ZY\), \(fg=p^3\), and both functions are nondecreasing. Proposition 2.3 yields

\[
X^{1/2}<q\le DE\le X^{523/1000},\qquad
q\in\mathcal D^{(3)}(X^{1/1000}).
\tag{6}
\]

The condition is \([D,E]>Z\), not \(DE>Z\). Repeated representations of q are counted only once.

This family contains nonsmooth examples for all sufficiently large X. Take distinct primes \(p,r\in[X^{.089},X^{.09}]\) and disjoint squarefree Y-smooth products \(d_0,e_0\in[X^{.170},X^{.171}]\); put \(D=pd_0,E=re_0\). The prime number theorem supplies p,r. To obtain the smooth products, successively multiply unused primes below Y until reaching \(X^{.170}\); each overshoot is at most Y, and the product of the available primes is much larger than \(X^{.342}\). Then

\[
X^{.259}\le D,E\le X^{.261},\quad
X^{.518}\le q=DE\le X^{.522},\quad
p^{3/2}D_{\ge p}=p^{5/2}\le X^{.225}<X^{.2505},
\tag{7}
\]

with the same inequality for r. Only the two large primes activate the predicates. The exact check verifies these exponent margins, not the density of the resulting family.

## 3. The exact divisor piece and a transfer lemma

The elementary convolution identity gives

\[
\Lambda(n)=\sum_{q\mid n}\mu(q)\log(n/q)
=B_{\mathcal Q}(n)+B_{\rm rest}(n),
\quad
B_{\mathcal Q}(n)=
\sum_{\substack{q\mid n\\q\in\mathcal Q_X}}\mu(q)\log(n/q).
\tag{8}
\]

This is a definite Type I divisor piece with a smooth cofactor coefficient \(\log(n/q)\). Both pieces are signed; neither is asserted to be a prime minorant.

Fix C>0 and

\[
X=T^\alpha,\quad \frac65\le\alpha\le\frac75,\quad
H=X/T=X^{1-1/\alpha}\in[X^{1/6},X^{2/7}].
\tag{9}
\]

For \(1\le h\le CH\), let \(w_h\) be real or complex, \(C^1\), and supported in a fixed compact subinterval of \((X,3X/2)\), with

\[
\|w_h\|_\infty+\int|w_h'(u)|du\le C_w
\tag{10}
\]

uniformly in X,T,h. For large X, \(m=n+h\) stays in [X,2X). Define

\[
\mathcal C_{\mathcal Q,h}
=\sum_n\Lambda(n+h)B_{\mathcal Q}(n)w_h(n),
\tag{11}
\]

\[
\mathcal M_{\mathcal Q,h}
=\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}
\frac{\mu(q)}{\varphi(q)}
\int w_h(u)\log(u/q)\,du.
\tag{12}
\]

**Transfer lemma.** Under the published estimate (2), for every fixed A>0,

\[
\boxed{\mathcal C_{\mathcal Q,h}=\mathcal M_{\mathcal Q,h}
+O_A(X\log^{-A}X)}
\tag{13}
\]

uniformly for the stated shifts and weights. This is unconditional when the ordinary distribution theorem is taken as input. RH is needed for the separate zeta correspondence, not this lemma.

The principal term involves only two explicit support sums,
\(\sum_{q\in\mathcal Q_X,(q,h)=1}\mu(q)/\varphi(q)\) and
\(\sum_{q\in\mathcal Q_X,(q,h)=1}\mu(q)\log q/\varphi(q)\).
No limiting evaluation of these sums is claimed. Replacing them with a universal singular-series constant would require another proof.

## 4. Proof, including coherence and prime-power exceptions

For \((q,h)=1\), substitute \(m=n+h\):

\[
\sum_{q\mid n}\Lambda(n+h)w_h(n)\log(n/q)
=\sum_{m\equiv h\;(\bmod q)}
\Lambda(m)w_h(m-h)\log((m-h)/q).
\tag{14}
\]

Let I be the union of primes occurring in the selected moduli, with primes dividing h removed. Then h is one primitive class modulo \(P_I\), restricting coherently to every remaining q. Uniformity in I and h follows from the source's definition (2.5), so (2) applies to this subset.

For weighted partial summation use

\[
w_h(u)\log(u/q)=w_h(u)\log u-(\log q)w_h(u).
\tag{15}
\]

There are just two common endpoint weight functions, with coefficients bounded by \(\log X\). Their sup norms and total variations are \(O(\log X)\). Integrating the source's modulus sum at a **common endpoint** is legal. No sum of separate endpoint suprema is substituted for it. The extra logarithm is absorbed by the arbitrary fixed saving in (2). Thus the coprime part of (11) equals

\[
\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}
\frac{\mu(q)}{\varphi(q)}
\sum_{(m,q)=1}\Lambda(m)w_h(m-h)\log((m-h)/q)
+O_A(X\log^{-A}X).
\tag{16}
\]

The prime number theorem with its classical error smaller than every fixed negative power of log X, followed by partial summation, replaces the unrestricted m-sum by the integral in (12). Summing the errors over q is harmless because
\(\sum_{q\le X^{.523}}1/\varphi(q)\ll\log X\), and the weights cost only fixed logarithmic powers.

Removing \((m,q)=1\) from that principal sum adds prime powers \(m=p^j\asymp X\) with p dividing q. Since \(p\le q<X^{.523}<X\), necessarily \(j\ge2\). Their total von Mangoldt mass is uniformly \(O(\sqrt X\log^2X)\). The logarithmic weight and the sum of \(1/\varphi(q)\) leave an error \(O(\sqrt X\log^{O(1)}X)\), absorbed by the stated error. These are all primes dividing q, not just those dividing h.

The original terms with \((q,h)>1\) are separate. If p divides q,h and q divides n, then \(\Lambda(n+h)\ne0\) forces \(n+h=p^j\), where p divides h. Uniformly for \(h\le CH\), there are \(O(\log^2X)\) such possibilities. For each n, the number of candidate divisors q is at most \(\tau(n)\ll_\eta X^\eta\), for any fixed \(\eta>0\). Their total contribution is \(O_\eta(X^\eta\log^{O(1)}X)\), also absorbed. Thus the nonprimitive terms are estimated, not silently deleted. This proves (13).

## 5. The actual localized Round 7 kernel

For fixed \(\chi\in C_c^\infty(1,3/2)\), put

\[
a_u(X)=\min\{(u/X)^{1/2},(X/u)^{3/2}\},\qquad
\operatorname{sinc}_0(v)=\sin(v)/v,\quad \operatorname{sinc}_0(0)=1,
\]

\[
w_h(u)=\chi(u/X)a_u(X)a_{u+h}(X)
\operatorname{sinc}_0\!\left(T\log(1+h/u)\right).
\tag{17}
\]

For \(h\le CH\), the argument is bounded and its u-derivative is \(O_C(1/X)\). Thus (10) holds uniformly throughout the alpha interval. This signed weight is allowed by the lemma.

The localized off-diagonal prime-prime term in the covariance is exactly

\[
\frac2{X\log T}\sum_{1\le h\le CH}
\sum_n\Lambda(n+h)\Lambda(n)w_h(n).
\tag{18}
\]

Substitution of (8) supplies the selected component (11) and an exact remainder. The factor two accounts for the two orders of each off-diagonal pair. All bounds are uniform for integration against the fixed Round 7 bump in alpha.

This is a stated component of the prime-prime term. Other n-ranges, shifts beyond CH, and the continuous-mean terms of the **centered** covariance have not been discarded.

## 6. A proved summed inequality, and the missing power

For arbitrary complex \(b_h\) supported on \(1\le h\le CH\), (13) gives

\[
\boxed{
\left|\sum_h b_h(\mathcal C_{\mathcal Q,h}-\mathcal M_{\mathcal Q,h})\right|
\ll_A X(\log X)^{-A}\sum_h|b_h|.
}
\tag{19}
\]

In particular, any shift packet with \(\sum_h|b_h|\le(\log X)^B\), B fixed, has error \(o(X\log X)\). This includes logarithmically many sampled shifts anywhere up to CH. It is a valid component-level arithmetic input.

For the whole natural packet \(b_h=1\), this only gives

\[
O_A(HX\log^{-A}X).
\tag{20}
\]

After normalization in (18) it becomes \(O_A(H\log^{-A-1}X)\), which does not tend to zero for any fixed A since \(H\ge X^{1/6}\). Arbitrary fixed logarithmic savings cannot be interpreted as an X-dependent power saving. This diagnoses the limitation of the estimate, not the size of the actual error.

## 7. The first unproved shifted forms

Define the weighted progression discrepancy

\[
\mathfrak D_{\mathcal Q}(X,T)=
\sum_{1\le h\le CH}
\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}
\mu(q)\,
\Delta\!\left(
\Lambda(m)w_h(m-h)\log((m-h)/q);
h\bmod q\right).
\tag{21}
\]

The sequence inside \(\Delta\) is a function of m with finite support. There is an aggregate identity with an error below the covariance scale. Under RH, which is already assumed for the Round 7 zeta correspondence,

\[
\boxed{
\sum_{1\le h\le CH}
(\mathcal C_{\mathcal Q,h}-\mathcal M_{\mathcal Q,h})
=\mathfrak D_{\mathcal Q}(X,T)
+O(H\sqrt X\log^4X).
}
\tag{22}
\]

Indeed the RH estimate \(\psi(y)-y=O(\sqrt y\log^2y)\), with weighted partial summation, gives a principal-term error \(O(\sqrt X\log^3X)\) per q before the factor \(1/\varphi(q)\). Summing that factor costs one more logarithm. The principal-term prime-power deletion has the same upper bound. The original nonprimitive error is \(O_\eta(X^\eta\log^{O(1)}X)\) per h and can be absorbed into this bound by fixing, for example, \(\eta=1/4\). Summation over h proves (22). Since \(H\le X^{2/7}\), its error is \(O(X^{11/14}\log^4X)=o(X\log X)\).

This use of RH is explicit: multiplying only the unconditional per-shift PNT error, however strong in logarithms, by H would not justify the same conclusion.

Consequently an additional estimate

\[
\mathfrak D_{\mathcal Q}(X,T)=o(X\log X),
\quad X=T^\alpha,\quad 6/5\le\alpha\le7/5,
\tag{23}
\]

uniform in alpha, would, under RH, evaluate the whole selected divisor piece at the desired precision. The source supplies only (20). Equation (23) requires cancellation across varying additive residues h, with the specified weight, or another argument of comparable strength.

The untouched divisor remainder is also explicit:

\[
\mathfrak B_{\rm rest}(X,T)=
\sum_{1\le h\le CH}
\sum_{\substack{q,m\ge1\\q\notin\mathcal Q_X}}
\mu(q)(\log m)\Lambda(qm+h)w_h(qm).
\tag{24}
\]

The support makes it finite. This shifted bilinear form is not covered directly by Proposition 2.18: \(\Lambda(qm+h)\) depends jointly on q,m,h and is not an independent coefficient sequence in the multiplicative convolution \(\alpha*\beta\). A Vaughan or Heath–Brown subdivision could reorganize (23), but a bound for the resulting shifted forms would still need proof.

Even (23) would not alone settle Round 7. The remainder (24), the support sums in (12), the omitted ranges, and the continuous centering remain. The actual successful transfer here is (13), (19), and the aggregate identity (22), with every source hypothesis checked; (21), (23), and (24) locate the unproved arithmetic task.

## 8. Verification and stopping point

The companion **check_divisor_bridge.py** uses only the Python standard library. It checks the parameter inequalities and the nonsmooth-family exponent margins with exact fractions. It represents \(\log n\) as a formal prime-log vector, and products as degree-two formal polynomials, to verify the convolution identity, progression reindexing, and the separation into discrepancy, coprime principal term, and nonprimitive contributions on finite examples. There is no floating-point tolerance.

The small examples test algebra and conventions. They do not satisfy the large-X source thresholds and provide no numerical evidence for the distribution theorem or for zeta pair correlations.

No prior round was modified; no prime-gap sweep or new zeta-data fit was performed.
