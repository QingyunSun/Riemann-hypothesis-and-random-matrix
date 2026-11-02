# A real-prime subfamily prevents a coefficient-only power saving

Date: 2026-09-05. Status: an ordinary arithmetic construction and quantitative counting proof. No numerical prime realization is required or used. The conclusion concerns a completed coefficient norm; it does not obstruct cancellation in the joint pairing with prime exponential sums.

Fix the full canonical complementary modulus family defined below. For any fixed nonnegative \(V\in C_c^\infty(1,2)\) that is not identically zero, the Round 10 completed coefficients satisfy, uniformly for \(X^{1/6}\le H\le X^{2/7}\),

\[
\boxed{\sum_{\substack{2\le d\le X^{.523}\\
1\le a<d,\ (a,d)=1}}|C_X(a/d)|^2
\gg_V \frac{H}{(\log X)^{348}}.}
\tag{1}
\]

For the coefficients with an additional \(\log q\), the lower bound is
\( \gg_V H/(\log X)^{346}\).

Consequently, neither coefficient norm admits an upper bound \(O(HX^{-\eta})\), for any fixed \(\eta>0\), on this full family. The result uses actual squarefree integers made from primes in explicit intervals, with all complementary predicates verified and their number estimated by the prime number theorem.

This is narrower than a no-go theorem for the research programme. A specially pruned family may remove these moduli. The actual prime exponential sums may also cancel against coefficients whose squared mass is large.

## 1. Fixing the family and the inherited divisor budget

Set

\[
\rho=\frac{523}{1000},\quad
r=\frac{523}{2000},\quad
b=\frac{501}{2000},\quad
\delta=\frac1{1000},\quad
Q=X^\rho,\quad Y=X^\delta.
\tag{2}
\]

Define \(\mathcal Q_X^{\mathrm{full}}\) to contain **every distinct squarefree modulus** \(q=[D,E]\) for which positive squarefree D,E obey

\[
\begin{gathered}
D,E\le X^r,\qquad [D,E]>X^{1/2},\\
p^{3/2}D_{\ge p}\le X^b\quad(p\mid D,\ p>Y),\\
p^{3/2}E_{\ge p}\le X^b\quad(p\mid E,\ p>Y).
\end{gathered}
\tag{3}
\]

Each q is counted once, irrespective of the number of representations. The coefficient on q is exactly \(\mu(q)\); no extra Selberg or cutoff coefficient is inserted.

These are the actual balanced complementary predicates fixed in Round 9, not every possible support geometry in the 186 paper. They use \(f(p)=g(p)=p^{3/2}\), equal budgets \(A_0=B_0=X^b\), and threshold \(Z=X^{1/2}\). The opposite-root guards follow from the owner bounds, and \(A_0B_0=ZY\). Hence Proposition 2.3 of [OpenAI, *Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), printed pp.4–5, proves

\[
\mathcal Q_X^{\mathrm{full}}
\subset\{X^{1/2}<q\le Q:
q\in\mathcal D^{(3)}(Y),\ q\text{ squarefree}\}.
\tag{4}
\]

The elementary divisor property stated on printed p.4 gives, for \(d\mid q\),

\[
d\in\mathcal D^{(3)}(Yq/d)
\subseteq\mathcal D^{(3)}(YQ/d).
\tag{5}
\]

Thus a conductor of size \(d=X^\beta\) retains the quantified parameter \(X^{\delta+\rho-\beta}\) in this sufficient class. This is not inheritance with unchanged Y for an arbitrary divisor. At the conductors constructed below, d=q itself, so the full original budget Y is retained with no loss.

Define the actual regrouped coefficients

\[
A_X(d)=\sum_{\substack{q\in\mathcal Q_X^{\mathrm{full}}\\d\mid q}}
\frac{\mu(q)}q,\qquad
C_X(a/d)=S_{V,H}(a/d)A_X(d),
\]

\[
S_{V,H}(\beta)=\sum_{h\in\mathbb Z}V(h/H)e(-\beta h),
\qquad e(t)=e^{2\pi it}.
\tag{6}
\]

The frequencies a/d in (1) are reduced. These are the coefficients in the exact conductor regrouping of Round 10, equation (11).

## 2. A subfamily made from 348 distinct prime factors

Put

\[
u=\frac9{100},\qquad
\kappa=\frac{343}{346000},\qquad
\lambda=2^{-1/348}.
\tag{7}
\]

Let \(\mathcal P_L(X)\) and \(\mathcal P_S(X)\) be the primes in

\[
(\lambda X^u,X^u],\qquad
(\lambda X^\kappa,X^\kappa],
\tag{8}
\]

respectively. For all sufficiently large real X, these two intervals are disjoint, the large primes exceed Y, and the small primes are below Y. Indeed
\(\kappa<\delta<u\), all strictly.

Let \(\mathcal F_X\) be the set of products of two distinct primes from \(\mathcal P_L(X)\) and 346 distinct primes from \(\mathcal P_S(X)\). The use of sets, rather than ordered prime tuples, prevents permutation overcounting.

Every q in this family is squarefree and has

\[
\mu(q)=(-1)^{348}=1.
\tag{9}
\]

The exact exponent identities are

\[
2u+346\kappa=\rho,\qquad
u+173\kappa=r,\qquad
\lambda^{348}=\frac12.
\tag{10}
\]

It follows that

\[
\frac Q2<q\le Q.
\tag{11}
\]

For large X, \(Q/2>X^{1/2}\). Partition the 346 small primes into two groups of 173 and place one large prime in each group. Their products D,E are disjoint and squarefree, \(q=DE=[D,E]\), and

\[
D,E\le X^{u+173\kappa}=X^r.
\]

Only the single large prime p in each root activates its predicate. Its owner tail is exactly p, so

\[
p^{3/2}D_{\ge p}=p^{5/2}
\le X^{(5/2)u}=X^{9/40}<X^{501/2000}.
\tag{12}
\]

The strict exponent margin is \(51/2000\). The same reasoning applies to E. The opposite-root condition \(p^{3/2}\le X^b\) holds as well. Thus

\[
\boxed{\mathcal F_X\subset\mathcal Q_X^{\mathrm{full}}\cap(Q/2,Q].}
\tag{13}
\]

The construction is not vacuous Y-smooth support: every modulus has two prime factors larger than Y, and both owner predicates are checked at those factors.

## 3. Rigorous counting, including the permutation constants

Write

\[
L_X=\pi(X^u)-\pi(\lambda X^u),\qquad
S_X=\pi(X^\kappa)-\pi(\lambda X^\kappa).
\]

Unique factorization, together with the disjoint prime intervals, gives the exact count

\[
|\mathcal F_X|=\binom{L_X}{2}\binom{S_X}{346}.
\tag{14}
\]

The prime number theorem on each fixed-ratio interval gives, as real X tends to infinity,

\[
L_X\sim\frac{1-\lambda}{u}\frac{X^u}{\log X},
\qquad
S_X\sim\frac{1-\lambda}{\kappa}\frac{X^\kappa}{\log X}.
\]

Since both counts tend to infinity, (14) yields

\[
|\mathcal F_X|
\sim c_0\frac{Q}{(\log X)^{348}},
\quad
c_0=\frac{(1-\lambda)^{348}}
{2!\,346!\,u^2\kappa^{346}}>0.
\tag{15}
\]

This assertion holds for every sufficiently large X, not merely a specially chosen subsequence. The constant is small, but fixed and positive; no estimate of its numerical size is needed for a power-saving obstruction. The factorization into D,E was used only to prove membership. Its many possible partitions are not counted again in (14).

## 4. No other signed modulus can cancel these conductor coefficients

Take \(d\in\mathcal F_X\). Since \(d>Q/2\), the only positive multiple of d at most Q is d itself. Therefore, in the **full signed family**, not just the positive subfamily,

\[
\boxed{A_X(d)=\frac{\mu(d)}d=\frac1d.}
\tag{16}
\]

This conclusion is unaffected by any other admissible moduli, including those with negative Möbius coefficient. It is an isolation statement at the reduced denominator d; no unmerged duplicate rational frequencies are being counted.

It also shows why the inherited dense-divisibility parameter in (5) cannot simply remove large conductors. Here d=q is near the largest allowed modulus and still belongs to the strongest original class \(\mathcal D^{(3)}(Y)\).

## 5. Enough primitive low numerators, and the norm lower bound

Let \(m_V=\int V(t)\,dt>0\). The Riemann-sum estimate, uniformly as H tends to infinity, gives

\[
\sum_hV(h/H)\ge\frac{m_V}2H
\tag{17}
\]

for sufficiently large H. This is uniform over the present range \(H\ge X^{1/6}\).

If \(1\le a\le d/(16H)\), every h in the support of V(h/H) satisfies
\(0\le2\pi ah/d\le\pi/4\). Positivity of V therefore gives

\[
|S_{V,H}(a/d)|
\ge\Re S_{V,H}(a/d)
\ge\frac{m_V}{2\sqrt2}H.
\tag{18}
\]

We must still count only primitive fractions. Put \(A=d/(16H)\). Each prime factor of d exceeds \(\lambda X^\kappa\), and d has exactly 348 such factors. Consequently

\[
\#\{1\le a\le A:(a,d)>1\}
\le\sum_{p\mid d}\left\lfloor\frac Ap\right\rfloor
\le A\frac{348}{\lambda X^\kappa}.
\tag{19}
\]

Uniformly for \(d\in\mathcal F_X\) and \(H\le X^{2/7}\), one has
\(A\ge X^{\rho-2/7}/32\to\infty\). For all sufficiently large X, take \(A\ge4\) and \(348/(\lambda X^\kappa)\le1/4\). Equations (19) and \(\lfloor A\rfloor\ge A-1\) then give at least \(A/2=d/(32H)\) coprime choices of a.

For each such d, (16) and (18) imply

\[
\sum_{\substack{1\le a<d\\(a,d)=1}}|C_X(a/d)|^2
\ge\frac{m_V^2}{256}\frac Hd.
\tag{20}
\]

Summing over \(\mathcal F_X\), using d≤Q and (15), proves the explicit eventual bound

\[
\boxed{
\sum_{d,a}|C_X(a/d)|^2
\ge\frac{c_0m_V^2}{512}
\frac{H}{(\log X)^{348}}.
}
\tag{21}
\]

All sufficiently-large-X conditions above can be imposed simultaneously, independently of H in its stated range.

For
\(A_X^{(1)}(d)=\sum_{q\in\mathcal Q_X^{\mathrm{full}},d\mid q}\mu(q)\log q/q\),
the same conductors have \(A_X^{(1)}(d)=\log d/d\).
Because \(d>X^{1/2}\), their squared contribution is at least
\((\log X)^2/4\) times the restricted contribution in (21). Hence

\[
\sum_{d,a}|S_{V,H}(a/d)A_X^{(1)}(d)|^2
\ge\frac{c_0m_V^2}{2048}
\frac{H}{(\log X)^{346}}
\tag{22}
\]

eventually.

## 6. Exactly what is ruled out

For every fixed \(\eta>0\), \(X^\eta/(\log X)^{348}\to\infty\). Thus (21) contradicts any proposed bound \(O(HX^{-\eta})\) for this coefficient norm on the full canonical family. More generally it rules out an upper bound of that strength asserted uniformly over **all** allowed subfamilies, since \(\mathcal F_X\) itself is an allowed family and has the same isolated conductor coefficients.

The quantifiers matter:

- A different deliberately pruned family can exclude \(\mathcal F_X\); no lower bound is asserted for every selected subset.
- A different coefficient system can suppress these moduli; the proof concerns the specified Möbius coefficients, not arbitrary sieve weights.
- The lower bound holds for fixed nonnegative nonzero V as stated. It is not asserted for every signed shift profile or every Fourier component of the full two-variable kernel.
- It supplies no lower bound for the signed joint pairing with
  \(A_f(a/d)-\mu(d)A_f(0)/\varphi(d)\), and no lower bound for the actual zeta covariance.

The conclusion is therefore specific: retaining a smaller divisor-density budget cannot by itself furnish a power saving in the completed coefficient norm for this canonical source-supported family. To improve the Round 10 bound by a power, this family requires additional cancellation in the joint prime pairing, a different use of the frequencies, or a justified change of the chosen modulus weights/support.

## 7. Provenance and exact arithmetic

The only counting input is the classical prime number theorem, applied to the two fixed-ratio prime intervals in (8). The support input is Proposition 2.3 and the divisor property on p.4 of the pinned 186 paper. The source PDF SHA256 is **456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930**.

The companion exact-arithmetic certificate records the rational exponent identities and positive margins in (7), (10), and (12), plus the uniform lower-numerator exponent. It does not claim an effective numerical threshold at which the prime-counting asymptotic has stabilized. No scan, numerical realization, or rerun of an old asymptotic bound was performed.
