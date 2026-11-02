# One actual-zeta target beyond Fourier support one

Date: 5 September 2026. Status: primary-source audit, an exact arithmetic reduction, and a conditional AH-Pairs detector. The required new arithmetic estimate is not proved here. The reductions use existing explicit-formula and Fourier arguments; no priority or novelty claim is made. No claim to have proved Montgomery's conjecture, refuted AH for zeta, or established RH is made.

## 1. Selected research target and the result of this round

Fix once and for all a nonnegative, normalized, symmetric smooth bump $\phi$ with closed support $[6/5,7/5]\subset(1,2)$ and centered at $13/10$. For example, normalize

$$
\phi(\alpha)=C\exp\!\left(-\frac1{1-(10\alpha-13)^2}\right)
\mathbf1_{\{|10\alpha-13|<1\}}.
$$

Then $\int\phi=1$ and $\int\alpha\phi(\alpha)d\alpha=13/10$. Assuming RH, define the actual-zeta form factor, with all zeros counted with multiplicity, by

$$
F_T(\alpha)=\frac{2\pi}{T\log T}
\sum_{0<\gamma,\gamma'\le T}
T^{i\alpha(\gamma-\gamma')}
\frac4{4+(\gamma-\gamma')^2}.
\tag{1}
$$

The ambitious target is the single smoothed Montgomery prediction

$$
\mathcal C_\phi(T):=\int\phi(\alpha)F_T(\alpha)d\alpha\longrightarrow1.
\tag{2}
$$

There is a weaker, still consequential target:

$$
\liminf_{T\to\infty}\mathcal C_\phi(T)>\frac7{10}.
\tag{3}
$$

Under RH, (3) contradicts the precise AH-Pairs hypothesis defined in Goldston–Lee–Schettler–Suriajaya, not merely the particular ACUE model. This assertion is proved in §3 below. It depends on the stated AH definition; it is not a claim about every informal hypothesis sometimes called “alternative.”

The main output is the exact centered prime-covariance obligation (12)–(15). It reduces (2) to a specified signed average of shifted von Mangoldt correlations, with the pole/continuous-mean term retained. It also shows precisely why a scalar sieve distribution exponent is not the missing input. No estimate closing (3) was obtained from the currently checked tools.

## 2. Primary-source state as checked on 5 September 2026

| Result | Status and implication for this target |
|---|---|
| Montgomery's actual-zeta pair-correlation theorem | Under RH, $F_T(\alpha)=|\alpha|+T^{-2|\alpha|}\log T+o(1)$ in the known low band, interpreted distributionally at zero. This evaluates Fourier tests supported inside $(-1,1)$, not (2). See [Goldston's primary-author notes](https://arxiv.org/abs/math/0412313), Theorem 1. |
| Higher correlations | Rudnick–Sarnak obtain the GUE correlations for the usual real-zero formulation under RH and the Fourier condition $\sum_j|\xi_j|<2$. On the translation-invariant hyperplane this does not supply an independent pair frequency above one. See [their original announcement](https://www.math.tau.ac.il/~rudnick/papers/RudnickSarnakCRAS1994.pdf), Theorem 1.2 and its first remark. |
| Unconditional pair-correlation identity | [Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh](https://arxiv.org/abs/2306.04799) remove RH from a generalized identity involving the full complex zeros. Interpreting it as an ordinary positive statistic of real ordinates requires care. This is not an asymptotic plateau on an interval above one. |
| The “0.6…” AI result | The precise constant is $C_0=3/2-2^{-1/2}\cot(2^{-1/2})=0.6725007\ldots$ for zeros that are both simple and on the critical line, unconditionally. [Anthropic's paper](https://arxiv.org/abs/2608.13637) and [Lamzouri's new proof](https://arxiv.org/abs/2609.02882), Theorem 1.1, give this result and the distinct-zero proportion $(1+C_0)/2$. Lamzouri's arXiv submission is dated **2 September**, not 3 September. His Lemma 3.1 still uses support $[-1,1]$. This improves what can be inferred from available spectral information; it does not provide the covariance in §4. |
| Quantitative bounds above one | [Carneiro–Milinovich–Ramos](https://arxiv.org/abs/2310.01913), Corollary 2, bound sufficiently long interval averages between $0.9303+o(1)$ and $1.3208+o(1)$ under RH. These are bounds, not a plateau asymptotic. Their equation (1.7) records the GRH lower bound $F_T(\alpha)\ge3/2-|\alpha|-\varepsilon$ on its stated range. |
| AH and simplicity | [Goldston–Lee–Schettler–Suriajaya II](https://arxiv.org/abs/2507.06823), Theorem 4, derives asymptotic simple critical zeros from AH-Pairs **plus** their AH-Weak Density assumptions. It does not refute AH. Their companion [PCC paper](https://arxiv.org/abs/2503.15449) derives simple critical zeros conditionally on PCC without assuming RH; it does not prove PCC. |

The checked primary sources do not establish (2) or (3). Results for a family of Dirichlet $L$-functions with extra character/modulus averaging, and results for function fields, must not be imported as the corresponding theorem for this single zeta function. The CMR paper itself separates its family result with support below two from the actual-zeta problem.

This round also read the existing force-energy, dynamic-generator, attachment-bridge audit, and main handoff. Their valid conclusions remain in force: the circular force square reduces to a singular two-point observable; protected trace dynamics do not create new bandwidth; and a finite heat-depth theorem supplies no unproved local flow for actual zeta. Those old calculations were not rerun.

## 3. Why the compact test excludes the precise AH-Pairs class

Put $L=\log T/(2\pi)$ and $N_T=TL$, and consider the positive pair measure

$$
\mu_T=\frac1{N_T}\sum_{0<\gamma,\gamma'\le T}
w(\gamma-\gamma')\,\delta_{L(\gamma-\gamma')},
\qquad w(v)=\frac4{4+v^2}.
\tag{4}
$$

With Fourier convention $\widehat f(\alpha)=\int f(u)e^{-2\pi i\alpha u}du$, its Fourier transform is $F_T$; the sign is immaterial because the pair measure is even.

The primary AH-Pairs condition says that for each fixed $M$, every pair with both ordinates in $(T/\log^2T,T]$ and $|L(\gamma-\gamma')|\le M$ lies within $O((|k|+1)R(T))$ of some $k/2$, where $R(T)\to0$. The needed compactness is not assumed without evidence. Their equation (1.12), printed p.4, supplies

$$
\mu_T([-R,R])\ll1+R\qquad(0\le R\le T).
\tag{5}
$$

For $R>T$, the crude total mass bound is $O(T\log T)$; do not upgrade (5) to a global uniform linear bound. Together these two estimates control Schwartz tails uniformly. For a test decaying like $(1+u^2)^{-1}$, dyadic shells up to $T$ give $O(1/R)$ and the remaining tail gives $O(\log T/T)$. This also suffices for the Poisson pair kernels used in the parallel resolvent lane.

Pairs involving an ordinate below $T/\log^2T$ contribute $o(N_T)$ to any fixed local test: there are $O(T/\log T)$ such zeros, and the elementary unit-interval zero bound gives $O(\log T)$ possible partners in a fixed normalized window. After division by $N_T$ this is $O(1/\log T)$. The uniform tail estimate then handles Schwartz tests. On compact normalized intervals $w(u/L)\to1$, so the weighted and unweighted local limits agree.

Consequently every subsequential tempered limit $\mu$ is a measure supported on $\tfrac12\mathbb Z$. It obeys $e^{4\pi iu}\mu=\mu$, hence $\widehat\mu$ is 2-periodic as a tempered distribution. Montgomery's theorem determines its restriction to $(-1,1)$:

$$
\widehat\mu=\delta_0+|\alpha|\,d\alpha
\quad\hbox{on }(-1,1).
$$

Translation by two therefore determines it on $(1,2)$:

$$
\widehat\mu=(2-\alpha)\,d\alpha.
\tag{6}
$$

Testing (6) against the fixed $\phi$ gives $\mathcal C_\phi(T)\to7/10$. The conclusion holds for every subsequence, so no prior existence of the full limiting pair measure is needed. It proves the contradiction claimed in (3). A second agent independently checked this argument, including the restricted range in (5) and the removal of early zeros.

### The unknown near-diagonal mass is confined to odd-frequency atoms

There is a useful more explicit statement. The same paper, equations (1.14)–(1.15), printed p.4, gives, under RH and AH-Pairs,

$$
1\le p_0\le\frac32-\frac2{\pi^2}
$$

along a subsequence on which the near-zero pair mass converges. The nonzero even half-lattice masses are $p_0-1/2$; the odd ones are $3/2-p_0-2/(\pi^2k^2)$. Their difference from the $p_0=1$ measure is

$$
(p_0-1)\sum_{k\in\mathbb Z}(-1)^k\delta_{k/2}.
$$

Writing $\operatorname{tri}_2(\alpha)=\operatorname{dist}(\alpha,2\mathbb Z)$, the full pair spectral measure is therefore

$$
\widehat\mu_{p_0}
=\operatorname{tri}_2(\alpha)d\alpha
+\sum_{m\in\mathbb Z}\delta_{2m}
+2(p_0-1)\sum_{m\in\mathbb Z}\delta_{2m+1}.
\tag{7}
$$

The centered spectral measure omits the atom at zero. The fixed test in (2) avoids all integer atoms, which is why it needs no simplicity or $p_0=1$ assumption. A one-scale unbandlimited resolvent statistic generally does need to account for the last term. Two suitably chosen signed Poisson scales can cancel this parameter; that is the separate root-agent construction reviewed in the adjacent note.

## 4. Exact prime-side identity with the pole term retained

For $x>1$ and $u>0$ define

$$
a_u(x)=\min\{(u/x)^{1/2},(x/u)^{3/2}\}.
$$

The absolutely convergent arithmetic signal is

$$
P_x(t)=\sum_{n\ge2}\Lambda(n)a_n(x)n^{-it}-M_x(t),
$$
$$
M_x(t)=\int_0^\infty a_u(x)u^{-it}du
=\frac{2x^{1-it}}{(1/2+it)(3/2-it)}.
\tag{8}
$$

The equality in (8) follows by integrating separately below and above $x$. This continuous mean is precisely the pole term in Montgomery's explicit formula. It cannot be dropped. The series converges absolutely because its tail is $O_x(\Lambda(n)n^{-3/2})$; this is not a formal expansion of $\log\zeta$ or $\zeta'/\zeta$ on the critical line.

Goldston's notes, Proposition 1 and equations (4.4)–(4.5), give under RH

$$
P_x(t)=-2x^{1/2-it}\sum_{\gamma\in\mathbb R}
\frac{x^{i\gamma}}{1+(t-\gamma)^2}+E_x(t),
$$
$$
E_x(t)\ll x^{-1/2}\log(t+2)+x^{-2}/(t+2).
$$

The integrated zero kernel differs from the truncated pair sum by $O(x\log^3T)$. Its squared norm is $O(xT\log^2T+x\log^3T)$. Cauchy–Schwarz with $\int_0^T|E_x|^2\ll x^{-1}T\log^2T$ shows, uniformly for $x=T^\alpha$ with $6/5\le\alpha\le7/5$,

$$
F_T(\alpha)
=\frac1{xT\log T}\int_0^T|P_x(t)|^2dt+o(1).
\tag{9}
$$

For example, the resulting normalized error is bounded by a constant times $\log T/x+\log^2T/T$ plus smaller terms. Thus the interchange with the fixed bump has no unstated uniformity problem.

Let $d\Delta(u)=d\psi(u)-du$, where $d\psi$ has mass $\Lambda(n)$ at each integer $n$. Define the explicit real symmetric kernel

$$
\mathcal K_T(u,v)=\frac1{T\log T}
\int\phi(\alpha)T^{-\alpha}a_u(T^\alpha)a_v(T^\alpha)
\frac{\sin(T\log(u/v))}{\log(u/v)}d\alpha,
\tag{10}
$$

using the continuous value $T$ on the diagonal. Absolute convergence of the weighted total variations justifies Fubini for each fixed $T$. Expanding the finite-time square gives the exact identity

$$
C_T:=\iint\mathcal K_T(u,v)d\Delta(u)d\Delta(v)
=\frac1{T\log T}\int\phi(\alpha)T^{-\alpha}
\int_0^T|P_{T^\alpha}(t)|^2dt\,d\alpha.
\tag{11}
$$

By (9), $C_T=\mathcal C_\phi(T)+o(1)$. The kernel changes sign away from the diagonal; positivity of the whole squared norm does not make each shifted-prime summand positive.

Separate the atomic diagonal

$$
D_T=\sum_n\Lambda(n)^2\mathcal K_T(n,n).
$$

The prime number theorem with partial summation gives $\sum_n\Lambda(n)^2a_n(x)^2\sim x\log x$. Hence $D_T\to13/10$. The **centered off-diagonal remainder** is exactly

$$
\begin{aligned}
E_T={}&2\sum_{m<n}\Lambda(m)\Lambda(n)\mathcal K_T(m,n)\\
&-2\sum_n\Lambda(n)\int_0^\infty\mathcal K_T(n,v)dv
+\int_0^\infty\int_0^\infty\mathcal K_T(u,v)du\,dv.
\end{aligned}
\tag{12}
$$

Equations (9)–(12) yield the promised exact research obligations:

$$
\boxed{\text{RH implies: target (2) is equivalent to }E_T\longrightarrow-3/10.}
\tag{13}
$$
$$
\boxed{\text{RH and AH-Pairs imply }E_T\longrightarrow-3/5.}
\tag{14}
$$
$$
\boxed{\text{Under RH, proving }\liminf E_T>-3/5
\text{ suffices to refute AH-Pairs.}}
\tag{15}
$$

The second and third terms of (12) are part of the required cancellation. The arithmetic task is not to bound the first, uncentered sum by its diagonal. Individual uncentered terms can be much larger than the final normalized answer.

## 5. What known distribution tools do and do not supply

Writing $n=m+d$, the oscillatory factor in (10) changes appreciably around $d\asymp m/T$. Since the prime weight emphasizes $m$ comparable to $x=T^\alpha$, the natural short-interval length is $H=x/T=x^{1-1/\alpha}$. For this test its exponents lie between $1/6$ and $2/7$. This is a description of the principal scale, not an assertion that all larger shifts or tails may be discarded.

Goldston–Montgomery's theorem gives the established bridge to short-interval variance. Goldston's Theorem 7 states the localized multiplicative-interval version, including logarithmic padding of the ranges; his equation (9.3) gives the fixed-length version. Under RH, a sufficiently uniform asymptotic

$$
\int_1^X(\psi(y+H)-\psi(y)-H)^2dy
\sim HX\log(X/H)
\tag{16}
$$

in the corresponding padded range implies the plateau target. It is not legitimate to infer a localized equivalence from one isolated $(X,H)$ scale with no uniformity. Formula (12) is the sharper single-test obligation and avoids adding that unnecessary claim.

A standard sufficient, stronger hypothesis is the square-root-error Hardy–Littlewood prime-pair estimate

$$
\sum_{n\le X}\Lambda(n)\Lambda(n+d)
=\mathfrak S(d)X+O_\varepsilon(X^{1/2+\varepsilon})
\tag{17}
$$

uniformly in the required shifts and partial-summation ranges. The weighted singular-series sum produces the $-HX\log H$ correction to the diagonal variance. Summing errors with triangular weights costs $O(H^2X^{1/2+\varepsilon})$, which is negligible against $HX\log X$ for $H\le X^{1/2-2\varepsilon}$. The selected exponent range lies inside that regime. This is a sufficient conditional explanation, not a proof of (17); the averaged signed condition (12) is weaker than demanding (17) for every shift.

The checked existing tools leave the following precise gap:

1. The Montgomery–Vaughan mean-value error for this Dirichlet series is controlled by $\sum n\Lambda(n)^2a_n(x)^2\asymp x^2\log x$. After normalization its size is comparable to $x/T$, which grows as a power of $T$ here. It does not provide an $o(1)$ error above support one.
2. Distribution of primes in arithmetic progressions, including complementary-factorization and triply divisible-modulus inputs in the 186 proof, controls a different family of linear prime sums. No identity in that proof supplies the centered two-prime covariance (12). Replacing its supported-modulus conditions by a scalar exponent does not repair this missing estimate.
3. Almost-everywhere prime existence or a first-order short-interval prime asymptotic need not resolve the second moment at the precision $HX\log(X/H)$: the much larger scale $H^2X$ is insufficient.
4. The GRH lower bound $F_T(\alpha)\ge3/2-\alpha-\varepsilon$ yields approximately $0.2$ for this bump, below the AH value $0.7$. The long-interval CMR bounds are also compatible with AH: the long average of (7) is $p_0$, and the full allowed interval $[1,1.2973576\ldots]$ lies inside their RH bounds. These results do not close (15).

There is also a rigorous information obstruction: low-band pair data and the protected moment algebra admit the half-lattice alternative while predicting the different value $0.7$ here. Therefore an argument using only those statistical constraints cannot force the value $1$. This does not prove that all future analytic methods must fail; it specifies that a new arithmetic estimate, or genuinely additional information, is needed.

## 6. Reproducibility, independent challenge, and stopping point

`sources/download_manifest.json` records seven downloaded primary PDFs with SHA256 hashes. It also records that the Anthropic expert-note URL was readable through the web tool but its separate local download returned HTTP 403; the arXiv paper was retrieved instead.

`kernel_identity_check.py` verifies the continuous mean in (8) and the diagonal/off-diagonal/mean expansion for a deliberately truncated prime polynomial at $x=8,T=3,n\le64$, using 60-digit arithmetic. The direct and expanded integrals agree within $3.0\times10^{-59}$. Omitting the mean changes that finite answer by about $212.37$, illustrating the sign/centering issue. These are numerical normalization checks, not interval enclosures or evidence for an asymptotic prime-pair conjecture. The initial unsplit improper quadrature did not meet its tolerance; splitting the logarithmic integration range resolved that numerical issue. The bundled document Python lacked `mpmath`; the recorded run uses the existing Homebrew Python with `mpmath` 1.3.0.

The AH support/periodicity step was independently challenged by the heat-flow agent. The root agent's separate Poisson-resolvent transfer was independently reviewed in `POISSON_TRANSFER_REVIEW.md`. No old finite-model computation was rerun and no new zero-data fit is being presented as a theorem.

The outcome is an explicit, weaker-than-full-PCC arithmetic target whose success would contradict a precise famous alternative under RH. The current round closes the normalization and source-audit questions; it does not close the signed prime-correlation estimate (15). The next justified research step is to attack that estimate, or an equivalent two-scale logarithmic-derivative statistic, with additional arithmetic structure. Reoptimizing a low-band detector alone would repeat the already identified information barrier.
