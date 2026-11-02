# Arithmetic transfer for a fixed symmetric prime-factor resonator

Date: 2026-09-05. Authoring role: Astra, primary research task.

**Status: complete written proof with independent internal review.** This note supplies the route from the weighted integer sums to the previously stipulated continuum form. The [independent review](symmetric_prime_transfer_independent_review.md) accepted the fixed-family argument. This is not Lean verification or external peer review. The three explicit estimates requested by that review are added below. The fixed rational trial still has a negative margin. No half-gap theorem is claimed.

## 1. Precise statement

Fix a real number \(\ell\geq1\), write \(a=\ell^2\), and let \(d=d_\ell\) be the multiplicative function with

\[
d(p^e)=\frac{(\ell)_e}{e!}.
\]

For \(L>1\), put

\[
v_n=\frac{\log n}{\log L},\qquad
S_L(n)=\sum_{p\mid n}\left(\frac{\log p}{\log L}\right)^2,
\quad r_L(n)=d(n)H(v_n,S_L(n)),\quad x_n=\frac{r_L(n)}{\sqrt n},
\]

where \(H(v,S)=f(v)+g(v)S\), and \(f,g\) are fixed real polynomials. Prime divisors in \(S_L\) are distinct. The proof extends to continuous \(f,g\), but the polynomial case suffices here. Define the nonnegative matrix

\[
(A_L)_{p^e m,m}=\frac{2\sin(\pi e\log p/(2\log L))}{e\sqrt{p^e}}
\quad (p^e m\leq L).
\]

Let \(\mathbb E_v\) mean the linear moment functional

\[
\mathbb E_v1=1,\quad \mathbb E_vS=\frac{v^2}{a+1},\quad
\mathbb E_vS^2=\frac{(a+6)v^4}{(a+1)(a+2)(a+3)}.
\]

No probability model is assumed. The functional is derived below from integers. Write

\[
H_0=H(v,S),\ H_u=H(v+u,S+u^2),\ H_w=H(v+w,S+w^2),
\ H_{uw}=H(v+u+w,S+u^2+w^2).
\]

The arithmetic limit is

\[
\frac{\|A_Lx\|^2+x^\top A_L^2x}{2\pi^2\|x\|^2}-\frac14
\longrightarrow \frac{M_2+M_3}{I}-\frac14,
\]

provided \(I>0\), where

\[
I=\int_0^1v^{a-1}\mathbb E_vH_0^2\,dv,
\]

\[
M_2=\frac{2\ell^2}{\pi^2}
\int_{v+u+w\leq1}v^{a-1}\frac{\sin(\pi u/2)}u\frac{\sin(\pi w/2)}w
\mathbb E_v(H_0H_{uw}+H_uH_w)\,dv\,du\,dw,
\]

\[
M_3=\frac2{\pi^2}\int_{v+u\leq1}v^{a-1}\frac{\sin^2(\pi u/2)}u
\mathbb E_vH_0^2\,dv\,du.
\]

All variables of simplex integrals are nonnegative. The scalar normalization constant below cancels from this quotient.

## 2. The unmarked integer measure

Define

\[
C_\ell=\prod_p(1-p^{-1})^a\sum_{e\geq0}\frac{d(p^e)^2}{p^e}>0.
\]

Each factor is \(1+O_\ell(p^{-2})\), so this product converges absolutely to a positive number. For real \(s>1\),

\[
D(s)=\sum_n\frac{d(n)^2}{n^s}=\zeta(s)^a F(s),\qquad F(s)\longrightarrow C_\ell\quad(s\downarrow1).
\]

Consequently the locally finite positive measures

\[
\nu_L=\frac1{(\log L)^a}\sum_{n\geq1}\frac{d(n)^2}{n}\delta_{\log n/\log L}
\]

converge on bounded intervals to

\[
\nu(dv)=\frac{C_\ell}{\Gamma(a)}v^{a-1}\,dv.
\]

One can use the Laplace continuity theorem for positive measures here, rather than needing a uniform pointwise Selberg–Delange error: for every \(t>0\),

\[
\int e^{-tv}\,d\nu_L(v)=\frac{D(1+t/\log L)}{(\log L)^a}
\longrightarrow C_\ell t^{-a}.
\]

For completeness, tilt by \(e^{-v}\). The tilted measures have convergent total masses and Laplace transforms; their tails obey
\(\int_R^\infty e^{-v}d\nu_L\leq e^{-R/2}\int e^{-v/2}d\nu_L\).
This gives tightness. Subsequential weak limits are uniquely identified by their Laplace transforms, and untilting on a compact interval gives the displayed local convergence. The limiting measure has no atom at zero or at any cutoff. This also gives

\[
\sum_{n\leq L}\frac{d(n)^2}{n}=O_\ell((\log L)^a).
\]

These arguments only need the classical simple pole of \(\zeta(s)\) at 1 and nonnegativity of the coefficients. They do not assume RH.

## 3. Marked primes and the two moments

First restrict marked primes to \(p\geq L^\varepsilon\), for a fixed \(\varepsilon>0\). For \(j>0\), the prime number theorem and partial summation give

\[
\sum_p\frac{(\log p/\log L)^j}{p}\delta_{\log p/\log L}
\ Longrightarrow\ u^{j-1}\,du
\]

on compact subintervals of \((0,\infty)\). Uniformity at zero will instead come from truncation.

If distinct marked primes are coprime to the background integer \(m\), each prime inserted into \(d(n)^2\) contributes \(d(p)^2=a\). Thus the limiting first-mark measure is the convolution

\[
\frac{C_\ell}{\Gamma(a)}a\int_0^v u(v-u)^{a-1}\,du
=\frac{C_\ell}{\Gamma(a)}v^{a-1}\frac{v^2}{a+1}.
\]

Expanding \(S^2\) produces the same-prime fourth-power term and the ordered distinct-prime term. Their respective densities are

\[
\frac{C_\ell}{\Gamma(a)}a\int_0^v u^3(v-u)^{a-1}\,du
=\frac{C_\ell}{\Gamma(a)}v^{a-1}\frac{6v^4}{(a+1)(a+2)(a+3)},
\]

\[
\frac{C_\ell}{\Gamma(a)}a^2
\int_{u+w\leq v}uw(v-u-w)^{a-1}\,du\,dw
=\frac{C_\ell}{\Gamma(a)}v^{a-1}\frac{av^4}{(a+1)(a+2)(a+3)}.
\]

These beta integrals give the claimed moment functional. Multiplying by a bounded continuous function of the total mass is permitted by weak convergence.

Here are the two discarded cases, with the order of limits specified.

* **Repeated or background primes:** for \(\ell\geq1\), \(d(p^{b+c})\leq d(p^b)d(p^c)\), since the successive ratios \((\ell+e)/(e+1)\) decrease with \(e\). Hence requiring a background integer to contain a marked prime costs an additional factor bounded by \(O_\ell(p^{-1})\) after its first reciprocal-prime weight. At \(p\geq L^\varepsilon\), the sum of the resulting \(p^{-2}\) terms is \(O(L^{-\varepsilon})\). The unmarked mass is \(O((\log L)^a)\), and the other finitely many reciprocal-prime sums cost at most powers of \(\log\log L\). Thus these contributions vanish after normalization. The same argument removes coincident distinct marks and prime exponents greater than one in this expansion.
* **Small marked primes:** deterministically, for every \(n\leq L\),
  \[
  0\leq\sum_{p\mid n,\ p<L^\varepsilon}\left(\frac{\log p}{\log L}\right)^2
  \leq\varepsilon\sum_{p\mid n}\frac{\log p}{\log L}\leq\varepsilon.
  \]
  Since \(0\leq S_L(n)\leq1\), deleting these marks changes \(H\) and its products by \(O_H(\varepsilon)\), uniformly on the cutoff.

Take \(L\to\infty\) with \(\varepsilon\) fixed, and then \(\varepsilon\downarrow0\). All product-measure cutoffs have boundary of measure zero. In particular, this approach includes the short-background range \(m\) near 1; it does not assume a uniform asymptotic for \(\sum_{m\leq L/(pq)}\) at every individual \(p,q\).

## 4. Uniform removal of small-prime and prime-power operator pieces

The preceding moment truncation alone is not enough: the creation operator also has a small-prime part. We control it with a weighted Schur estimate.

Put \(w_n=d(n)/\sqrt n>0\). The logarithmic derivative of \(\zeta(s)^\ell\), or its formal Dirichlet-series coefficient identity, gives

\[
\sum_{p^e\mid n}(\log p)d(n/p^e)=\frac{\log n}{\ell}d(n).
\]

Since \(0\leq2\sin(\pi\log q/(2\log L))\leq\pi\log q/\log L\),

\[
\frac{(A_Lw)_n}{w_n}\leq\frac{\pi\log n}{\ell\log L}\leq\frac\pi\ell.
\]

Submultiplicativity gives for any subset \(E\) of prime powers

\[
\frac{(A_E^\top w)_m}{w_m}
\leq\sum_{p^e\in E,\ p^e\leq L}
\frac{2\sin(\pi e\log p/(2\log L))}{e p^e}d(p^e).
\]

For all prime powers the right side is \(O_\ell(1)\). For the prime part \(p<L^\varepsilon\) it is at most

\[
\frac{\pi\ell}{\log L}\sum_{p<L^\varepsilon}\frac{\log p}{p}
\leq\pi\ell\varepsilon+O_\ell(1/\log L).
\]

For exponents \(e\geq2\) it is bounded by

\[
\frac\pi{\log L}\sum_p\sum_{e\geq2}\frac{d(p^e)\log p}{p^e}
=O_\ell(1/\log L).
\]

The series converges because \(d(p^e)=O_\ell((e+1)^{\ell-1})\). The weighted Schur test follows directly by Cauchy–Schwarz and summing the two displayed weighted row/column bounds. Therefore

\[
\|A_L\|=O_\ell(1),\qquad
\|A_{p<L^\varepsilon}\|=O_\ell(\sqrt\varepsilon+1/\sqrt{\log L}),\qquad
\|A_{e\geq2}\|=O_\ell(1/\sqrt{\log L}).
\]

Thus replacing \(A_L\) by its prime-only part with \(p\geq L^\varepsilon\) changes either quadratic form, divided by \(\|x\|^2\), by \(O_\ell(\sqrt\varepsilon+1/\sqrt{\log L})\). This estimate works for signed \(H\), and indeed for every vector \(x\); no coefficient positivity is needed at this step.

## 5. Evaluation of the retained integer sums

For the retained prime operator set \(\alpha_p=2\sin(\pi\log p/(2\log L))\). Exactly,

\[
\|A_Lx\|^2=\sum_{n\leq L}\frac1n\sum_{p,q\mid n}\alpha_p\alpha_q r_L(n/p)r_L(n/q),
\]

\[
x^\top A_L^2x=\sum_{mpq\leq L}\frac{\alpha_p\alpha_q}{mpq}r_L(m)r_L(mpq).
\]

In the first formula, the terms \(p=q\) are **not discarded**. With \(n=mp\), they give

\[
\sum_{mp\leq L}\frac{4\sin^2(\pi u/2)}{mp}d(m)^2H(v,S_L(m))^2.
\]

Its limit, after division by \(C_\ell(\log L)^a/\Gamma(a)\), is \(2\pi^2M_3\).

For \(p\neq q\), put \(n=mpq\). Away from the negligible coprimality defects already estimated, the coefficient is

\[
r_L(mp)r_L(mq)=\ell^2d(m)^2H_uH_w.
\]

The prime-insertion measures give the corresponding \(H_uH_w\) term of \(2\pi^2M_2\). There is no extra factor of two: \((p,q)\) is ordered both in the integer sum and in the double integral.

Similarly, in the second quadratic form the distinct-prime terms have

\[
r_L(m)r_L(mpq)=\ell^2d(m)^2H_0H_{uw}.
\]

The repeated-prime \(p=q\) terms here contain \(p^{-2}\), and vanish by the fixed-\(\varepsilon\) estimate. This is why the same-prime term survives in \(A^\top A\) but not in \(A^2\). The marked-background moments from Section 3 evaluate both expectations.

Finally,

\[
\|x\|^2\sim\frac{C_\ell}{\Gamma(a)}(\log L)^a I.
\]

Combining the three limits and the operator truncation proves the stated arithmetic limit. The independent internal audit checked these measure-convergence and discarded-term arguments.

## 6. Interface with the actual zeta theorem

The exact source is [Inoue, arXiv:2604.05733v1, Theorems 3 and 4](https://arxiv.org/html/2604.05733v1#S3). Those theorems allow arbitrary arithmetic resonator coefficients under RH and the product cutoff \(L\leq T/(\log T)^2\). Choose \(L=\lfloor T/(\log T)^2\rfloor\), \(h=\pi/\log T\), and the logarithmic increment approximator. The theorem has a coefficient-independent normalized error tending to zero; the approximator square sum is \(O(1)\).

The corresponding operator uses \(\theta=\log L/\log T\to1\). Replacing \(\theta\) by 1 changes the weighted Schur bounds, hence the operator norm, by \(O_\ell(|1-\theta|)\): apply the mean value inequality for sine and the same logarithmic derivative and prime-sum estimates. At \(\phi=1/2\), the linear coefficient cancels. The resulting lower bound for the normalized weighted zero-count expression has the proposed continuum margin, with the scope accepted in the independent review.

This would establish the arithmetic validity of the fixed symmetric-prime family. It would **not** establish a positive margin. The current certified value is approximately \(-0.014662375473369\), and a fixed negative lower bound has no half-gap consequence.

## 7. Audit requests and provenance

Independent reviewers should check: the \(\ell\geq1\) submultiplicativity restriction; the exact weighted Schur row and column orientation; local convergence of positive measures including the \(v=0\) boundary; counting of ordered distinct primes; uniform removal of background coincidences; and the error normalization when invoking Inoue Theorem 4. A successful numerical check cannot replace any of these steps.

This draft is a mathematical reconstruction intended for public verification. It records the argument and its dependencies, not a transcript of private model deliberation. No novelty claim is made for the marked-prime asymptotics or the Schur method; the purpose is to close the exact transfer obligation created by this project's fixed trial.


## 8. Explicit estimates added after independent review

The reviewed draft had SHA-256 `bf2ca70e61da1f97b4c214304180f0f45d3c26a050104bf30e6d70e46660d07f`. The review requested the following elaborations; they clarify the estimates rather than change the theorem.

First, the uniform total-mass bound follows directly from the Laplace transform:

\[
\frac1{(\log L)^a}\sum_{n\le L}\frac{d(n)^2}{n}
\le e\frac{D(1+1/\log L)}{(\log L)^a}=O_\ell(1).
\]

Second, the background coincidence bound can be written explicitly as

\[
\sum_{m\le L:\ p\mid m}\frac{d(m)^2}{m}
\le\frac{\ell^2}{p}\sum_{k\le L}\frac{d(k)^2}{k}.
\]

The additional reciprocal-prime weight outside this sum gives a summable `p^{-2}` cost. Collisions between an outer inserted prime and a prime in the expansion of the background S moment have exactly this form. There are only finitely many such marks for fixed H.

Third, if `A=A0+E`, then

\[
\|A^*A-A_0^*A_0\|\le(\|A\|+\|A_0\|)\|E\|,
\qquad
\|A^2-A_0^2\|\le(\|A\|+\|A_0\|)\|E\|.
\]

These inequalities justify removing the small-prime and prime-power operator pieces uniformly over signed vectors. If applying Inoue Theorem 4 directly, its normalized `O(h) M1` term is bounded by Theorem 3 and the same Schur estimate; the source's combined Proposition 3 packages this cancellation and error estimate explicitly. No new off-diagonal hypothesis is introduced.
