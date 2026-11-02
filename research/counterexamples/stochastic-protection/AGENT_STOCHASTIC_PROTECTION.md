# Exact stochastic protection, a first unprotected heat eigenfunction, and the information in a continuous trace path

Date: 2026-11-01 (America/Los_Angeles); source reading and review: 2026-11-02 UTC. Author lane: `r29_close`, renewed counterexample programme. The initial September 8 date was inherited from stale context and is corrected here; historical research notes are unchanged.

Status: self-contained finite-dimensional mathematical arguments with six exact Laurent-polynomial checks. These are statements about ACUE and genuine unitary Brownian motion. They do not identify actual zeta zeros with a matrix diffusion, refute the Alternative Hypothesis for zeta, or establish a Dyson–Montgomery conjecture. Novelty relative to the full literature has not been established.

## 1. Results and exact scope

Let \(N\ge2\), and start the **same genuine circular Dyson Brownian motion at \(\beta=2\)** from either ACUE or CUE. CUE is stationary under this stochastic process. Both unrotated ACUE and ACUE with an independent common uniform rotation are allowed.

There are three complementary conclusions.

1. **Exact multitime protection.** Every product of trace-polynomial observations at arbitrary deterministic times has the same expectation in the two processes, provided the sum of all positive Fourier weights is at most \(N\) and the sum of all negative Fourier weights is at most \(N\). Noise and repeated time evolution do not increase either weight. The budget is shared across every observation; it is not a separate allowance of \(N\) at each time.
2. **A sharp balanced witness beyond that budget.** Write \(h_r=s_{(r)}\) for the complete homogeneous symmetric polynomial and \(h_0=1\). Then
   \[
   \Phi_{N+1}=|h_{N+1}|^2-|h_N|^2
   \]
   has positive and negative weights at most \(N+1\), and, in the normalization below,
   \[
   \boxed{\mathbb E_{\mathrm A}\Phi_{N+1}(t)
   -\mathbb E_{\mathrm C}\Phi_{N+1}(t)
   =-e^{-2(N+1)t}.}
   \tag{1}
   \]
   Thus the two positive-time laws are different at every finite time, although all observations covered by the first statement match exactly. The witness is unchanged by common rotation. It proves that the universal rectangular budget cannot be enlarged from \((N,N)\) to \((N+1,N+1)\).
3. **The whole low-mode path is not protected.** Ideal continuous observation of the single complex path \(p_1(t)\) determines all the traces, using quadratic covariation recursively. It therefore determines the initial unordered spectrum. This is a precise way to escape the bounded-moment obstruction; it does not give a robust estimator from finitely many noisy samples.

The first two statements form a stochastic, multitime extension of the deterministic obstruction in [the existing generator report](../../reports/dynamic_generator.md). The third prevents an incorrect inference from moment matching to equality of low-mode path laws.

## 2. Objects, normalization, and sources

Angles are in radians. Put
\[
z_j=e^{i\theta_j},\qquad p_m=\sum_{j=1}^N z_j^m,
\quad p_0=N,\quad p_{-m}=\overline{p_m},
\]
and
\[
V_i(\theta)=\sum_{j\ne i}\cot\frac{\theta_i-\theta_j}{2}.
\]
The stochastic normalization used throughout is
\[
d\theta_i=\frac1{\sqrt N}\,dB_i+
\frac1{2N}V_i(\theta)\,dt,
\qquad
\boxed{\mathcal L=\frac1{2N}
\left(\sum_i\partial_i^2+\sum_iV_i\partial_i\right).}
\tag{2}
\]
The \(B_i\) are independent standard real Brownian motions. The eigenvalue process can be defined globally through unitary Brownian motion, so no artificial continuation through a singular coordinate chart is needed for the symmetric polynomials used here.

For a primary normalization reference, Collins–Dahlqvist–Kemp, [*Strong Convergence of Unitary Brownian Motion*, arXiv:1502.06186v2](https://arxiv.org/pdf/1502.06186), §2.1, pp. 5–6, uses the Lie-algebra inner product \(-N\operatorname{Tr}(XY)\), generator one half the resulting Laplacian, and matrix SDE
\[
dU_t=iU_t\,dX_t-\tfrac12U_t\,dt,
\]
where the Hermitian Brownian diagonal variance is \(dt/N\). Equation (2) is its radial generator. This reference is used for the standard process and its time scale; the weight argument and witness below are derived explicitly here. Trace-polynomial heat calculations are classical; see also Lévy, [*Schur–Weyl duality and the heat kernel measure on the unitary group*](https://arxiv.org/abs/math/0703690).

A direct invariant-density check fixes the factor of two:
\[
W=\log\prod_{i<j}|z_i-z_j|^2,
\qquad \partial_iW=V_i,
\]
so (2) is \((2N)^{-1}e^{-W}\sum_i\partial_i(e^W\partial_i)\). Its stationary eigenvalue law is CUE. A separate normalization check is \(\mathcal Lp_1=-p_1/2\), agreeing with the matrix SDE.

ACUE is the probability on unordered \(N\)-subsets \(S\) of the \(2N\)-th roots of unity given by
\[
\mathbb P_{\mathrm A}(S)=(2N)^{-N}
\prod_{a<b,\ a,b\in S}|\zeta^a-\zeta^b|^2,
\qquad \zeta=e^{2\pi i/(2N)}.
\tag{3}
\]
Its minimum circular angular gap at time zero is at least \(\pi/N\); CUE has positive probability of a gap below that value. The primary ACUE reference is Tao, [*The alternative hypothesis for unitary matrices*, 8 May 2019](https://terrytao.wordpress.com/2019/05/08/the-alternative-hypothesis-for-unitary-matrices/). We reproduce the exact initial identities needed below rather than assuming an unspecified low-frequency matching statement.

## 3. Initial protected algebra, including unbalanced moments

For nonnegative integers \(a,b\), let \(\mathcal F_{a,b}\) be the span of monomials
\[
\prod_{u=1}^{q}p_{m_u},\qquad m_u\in\mathbb Z\setminus\{0\},
\]
whose positive and negative weights satisfy
\[
\sum_{m_u>0}m_u\le a,
\qquad \sum_{m_u<0}|m_u|\le b.
\tag{4}
\]
The empty monomial is 1. Finite-\(N\) relations may make this spanning set redundant, but \(\mathcal F_{a,b}\) is finite dimensional and unambiguously a space of functions. Products obey
\[
\mathcal F_{a,b}\mathcal F_{c,d}\subseteq\mathcal F_{a+c,b+d}.
\tag{5}
\]

For partitions \(\alpha,\eta\) with at most \(N\) parts, the alternant formula and Cauchy–Binet applied to (3) give
\[
\mathbb E_{\mathrm A}s_\alpha\overline{s_\eta}
=\det\left[
\mathbf1_{\alpha_i+N-i\equiv\eta_j+N-j\pmod{2N}}
\right]_{i,j=1}^N.
\tag{6}
\]
Indeed the Vandermonde weight cancels the two Schur denominators, and each matrix entry after the subset sum is the average of a character over the \(2N\)-th roots. Taking both partitions empty also checks that (3) is normalized.

If \(|\alpha|,|\eta|\le N\), every exponent is between 0 and \(2N-1\). Both exponent lists are strictly decreasing. Thus the determinant in (6) is \(\delta_{\alpha\eta}\), exactly its Haar value. Expanding the positive and negative power sums separately in Schur polynomials proves
\[
\boxed{\mathbb E_{\mathrm A}f=\mathbb E_{\mathrm C}f
\quad\text{for every }f\in\mathcal F_{N,N}.}
\tag{7}
\]
This includes unbalanced monomials in the rectangular range, not just those with equal weights. A common uniform rotation of ACUE preserves (7): balanced monomials are unchanged, and unbalanced ones already have expectation zero in this range.

## 4. The stochastic cut-and-join coefficients

For \(m>0\), the deterministic identity from the existing report is
\[
V\cdot\nabla p_m
=-m\left((N-m)p_m+\sum_{a=1}^{m-1}p_ap_{m-a}\right).
\tag{8}
\]
Its conjugate gives the formula for negative indices, with \(|m|\) in place of \(m\) outside the signed trace indices. Since \(\sum_i\partial_i^2p_m=-m^2p_m\), the \(m^2\) terms cancel at \(\beta=2\), leaving
\[
\boxed{\mathcal Lp_m=-\frac{|m|}{2}p_m
-\frac{|m|}{2N}\sum_{a=1}^{|m|-1}
p_{\operatorname{sgn}(m)a}
p_{\operatorname{sgn}(m)(|m|-a)}.}
\tag{9}
\]
For two signed nonzero indices the full product correction, not half of it, is
\[
\boxed{\mathcal L(p_mp_n)-p_m\mathcal Lp_n-p_n\mathcal Lp_m
=-\frac{mn}{N}p_{m+n}.}
\tag{10}
\]
This follows directly from
\(\partial_i p_m=imz_i^m\) and the coefficient \(1/(2N)\) of the second derivatives. If carré du champ is defined as one half the product correction, its value here is \(-mn p_{m+n}/(2N)\).

For a product of any number of trace factors, apply (9) to each individual factor and add (10) for each unordered pair of distinct factors. There are no higher-order corrections. An individual trace can split into two traces with the same sign and the same total weight. A pair can merge as follows:

* When \(m,n\) have the same sign, \(p_{m+n}\) has exactly their total weight.
* When their signs differ, the positive and negative weights both decrease by \(\min(|m|,|n|)\).
* When \(m+n=0\), the resulting \(p_0=N\) is a constant, so both weights disappear.

Consequently
\[
\boxed{\mathcal L\mathcal F_{a,b}\subseteq\mathcal F_{a,b}.}
\tag{11}
\]
Unlike deterministic flow, the diffusion need not preserve each biweight exactly. The correct invariant object is the **filtered** space (4). The signed difference of the two weights, or rotation charge, is preserved term by term.

As a further check,
\[
\mathcal L|p_1|^2=-|p_1|^2+1.
\tag{12}
\]
The constant comes from \((-1/N)(1)(-1)p_0=1\). This restores stationarity of the CUE value \(\mathbb E|p_1|^2=1\); omitting this term would incorrectly reproduce the deterministic calculation.

For reference, with the more general formal circular-beta normalization
\[
d\theta_i=\sqrt{\frac2{\beta N}}\,dB_i+\frac1{2N}V_i\,dt,
\]
the two coefficients become
\[
\begin{aligned}
\mathcal L_\beta p_m
&=-\left[\frac{|m|(N-|m|)}{2N}+\frac{m^2}{\beta N}\right]p_m
-\frac{|m|}{2N}\sum_{a=1}^{|m|-1}p_{\operatorname{sgn}(m)a}p_{\operatorname{sgn}(m)(|m|-a)},\\
\mathcal L_\beta(p_mp_n)-p_m\mathcal L_\beta p_n-p_n\mathcal L_\beta p_m
&=-\frac{2mn}{\beta N}p_{m+n}.
\end{aligned}
\tag{13}
\]
Thus the same filtration argument works whenever the common circular-beta Markov process with this generator is available. No existence or collision convention for arbitrary \(\beta\) is needed for the rigorous \(\beta=2\) result above. For \(\beta\ne2\), a CUE initial law would generally not be stationary.

## 5. Semigroup and the exact multitime theorem

Let \(P_t\) denote the Markov semigroup of (2). Since trace polynomials are smooth functions on the compact group, their generators and values are bounded for each fixed \(N\). Choose any basis of \(\mathcal F_{a,b}\). Itô's formula and (11) give a closed finite linear system for the vector of conditional expectations from any initial matrix. Uniqueness of this finite ODE gives
\[
P_t\mathcal F_{a,b}\subseteq\mathcal F_{a,b}
\qquad(t\ge0).
\tag{14}
\]
This argument does not rely on formally exchanging an infinite generator series with expectation. In a chosen basis the restriction really is a finite matrix exponential.

**Theorem.** Fix deterministic times \(0\le t_1\le\cdots\le t_r<\infty\), and functions \(f_j\in\mathcal F_{a_j,b_j}\). If
\[
A=\sum_{j=1}^r a_j\le N,
\qquad B=\sum_{j=1}^r b_j\le N,
\tag{15}
\]
then
\[
\boxed{
\mathbb E_{\mathrm A}\prod_{j=1}^r f_j(\theta(t_j))
=\mathbb E_{\mathrm C}\prod_{j=1}^r f_j(\theta(t_j)).}
\tag{16}
\]

**Proof.** Starting at the last observation, define
\[
g_r=f_r,
\qquad
g_j=f_j\,P_{t_{j+1}-t_j}g_{j+1},\quad j=r-1,\ldots,1.
\tag{17}
\]
Equations (5) and (14) show by backward induction that
\[
g_j\in\mathcal F_{\sum_{k=j}^r a_k,\,\sum_{k=j}^r b_k}.
\]
The Markov property identifies the left or right expectation in (16) with the corresponding initial expectation of \(P_{t_1}g_1\). This function lies in \(\mathcal F_{A,B}\subseteq\mathcal F_{N,N}\). Apply (7). \(\square\)

There is no upper restriction on the times, and they may depend on \(N\). The number of observations may also depend on \(N\), provided (15) holds for the monomial being tested. A polynomial in observations at different times is covered term by term; the sharp convenient sufficient test is the total positive and negative budget of each monomial, rather than an unnecessarily large budget attached to an entire polynomial.

Time integration against finite deterministic measures also preserves this equality, by boundedness and Fubini. Neither an arbitrary nonlinear function of these observations nor a general adaptive stopping rule is included automatically.

For example, for \(s\le t\), both processes satisfy exactly
\[
\mathbb E[p_1(t)\overline{p_1(s)}]=e^{-(t-s)/2}.
\tag{18}
\]
Here \(P_{t-s}p_1=e^{-(t-s)/2}p_1\), and (12) together with the initial value gives \(\mathbb E|p_1(s)|^2=1\). The covariance resembles that of a stationary complex Ornstein–Uhlenbeck process. This does **not** identify the trace process with an Ornstein–Uhlenbeck process: for example its unconjugated quadratic variation depends on \(p_2\), as shown below.

## 6. An explicit witness at balanced weight \(N+1\)

For every integer \(r\ge1\), define
\[
\Phi_r=|h_r|^2-|h_{r-1}|^2.
\tag{19}
\]
We establish the exact heat eigenfunction identity
\[
\boxed{\mathcal L\Phi_r=-\frac{r(r+N-1)}N\Phi_r.}
\tag{20}
\]

### 6.1 Character identity from the one-row Pieri rule

For a dominant integral signature \(\lambda_1\ge\cdots\ge\lambda_N\), write
\[
\chi_\lambda(z)
=\frac{\det[z_j^{\lambda_i+N-i}]_{i,j=1}^N}
{\det[z_j^{N-i}]_{i,j=1}^N}.
\tag{21}
\]
Negative entries are allowed; this is a symmetric Laurent polynomial. On the unit circle,
\[
\overline{h_r}=(z_1\cdots z_N)^{-r}s_{(r^{N-1})}.
\]
The one-row Pieri expansion is particularly simple:
\[
s_{(r)}s_{(r^{N-1})}
=\sum_{k=0}^r s_{(r+k,r^{N-2},r-k)}.
\tag{22}
\]
To see the displayed list, interlacing for a horizontal \(r\)-strip forces every middle row to remain \(r\). The extra boxes divide between the first and final row, giving precisely the parameter \(k\). Each allowed strip has coefficient one. Multiplication by \((z_1\cdots z_N)^{-r}\) yields
\[
|h_r|^2=\sum_{k=0}^r\chi_{(k,0^{N-2},-k)}.
\]
Subtract the same identity at \(r-1\):
\[
\boxed{\Phi_r=\chi_{(r,0^{N-2},-r)}.}
\tag{23}
\]

### 6.2 Radial eigenvalue, with the time scale derived

Put \(\rho_i=(N+1)/2-i\). On an ordered collision-free chart, the Weyl denominator can be written, up to a nonzero constant, as
\[
\delta(\theta)=\det[e^{i\rho_i\theta_j}]_{i,j=1}^N.
\]
It satisfies
\[
\partial_j\log\delta=\tfrac12V_j,
\qquad
\Delta\delta=-\left(\sum_i\rho_i^2\right)\delta.
\]
The denominator conjugation formula is therefore
\[
2N\mathcal L f
=\delta^{-1}\left(\Delta+\sum_i\rho_i^2\right)(\delta f).
\tag{24}
\]
For \(f=\chi_\lambda\), multiplying (21) by \(\delta\) leaves the alternant with exponents \(\lambda_i+\rho_i\). Every determinant term has the same Laplacian eigenvalue. Consequently
\[
\mathcal L\chi_\lambda
=-\frac1{2N}\sum_{i=1}^N
\lambda_i(\lambda_i+N+1-2i)\,\chi_\lambda.
\tag{25}
\]
Although \(\delta\) may use half-integer exponents and a local ordering, the resulting character identity is a globally defined Laurent-polynomial identity. Thus no coordinate-chart choice persists in (25).

For the signature in (23), only its first and last entries contribute to the sum in (25). Their sum is \(2r(r+N-1)\), proving (20). As elementary checks, \(r=1\) gives eigenvalue \(-1\), as already found for \(|p_1|^2-1\), and the holomorphic signature \((1,0,\ldots,0)\) gives \(-1/2\) for \(p_1\).

### 6.3 The initial discrepancy and its exact propagation

In the ACUE alternant for \(h_{N+1}=s_{(N+1)}\), the exponent list is
\[
2N,\ N-2,\ N-3,\ldots,0.
\]
The first and final rows coincide on \(2N\)-th roots of unity. Therefore
\[
h_{N+1}=0\quad\text{at every ACUE configuration}.
\tag{26}
\]
This remains true after a common rotation, by homogeneity. Meanwhile (7) gives
\[
\mathbb E_{\mathrm A}|h_N|^2=1.
\]
For Haar measure, character orthogonality gives
\(\mathbb E_{\mathrm C}|h_r|^2=1\) for every \(r\ge0\), including \(r>N\): a one-row partition has at most \(N\) parts. Thus
\[
\mathbb E_{\mathrm A}\Phi_{N+1}=-1,
\qquad \mathbb E_{\mathrm C}\Phi_{N+1}=0.
\tag{27}
\]
The semigroup eigenvalue in (20), with \(r=N+1\), is \(-2(N+1)\). This proves (1).

For the natural choice \(t=c/N\) with fixed \(c\ge0\), this unnormalized witness has discrepancy tending to \(-e^{-2c}\). This statement is about the displayed expectation. Its sup norm grows with \(N\); it must not be promoted to an order-one total-variation lower bound or an efficient statistical test without additional estimates.

The common finite positive-time discrepancy is compatible with loss of the strict initial hard core: genuine Brownian noise does not preserve a lattice spacing constraint. The counterexample asserts equality of the specified moments alongside different laws, not persistence of the original hard core at all times.

## 7. Why complete observation of a low-mode path escapes the theorem

The stochastic martingale part of \(p_m\) in (2) is
\[
dp_m\big|_{\mathrm{mart}}=\frac{im}{\sqrt N}\sum_j z_j^m\,dB_j.
\]
For complex semimartingales, take quadratic covariation bilinearly, without conjugating its second input. It gives
\[
\boxed{d[p_m,p_n]_t=-\frac{mn}{N}p_{m+n}(t)\,dt.}
\tag{28}
\]
In particular,
\[
\frac{d}{dt}[p_1,p_1]_t=-\frac1N p_2(t),
\qquad
\frac{d}{dt}[p_1,\overline{p_1}]_t=1.
\tag{29}
\]
The first identity would vanish for a standard rotationally symmetric complex Ornstein–Uhlenbeck diffusion. It need not vanish here.

Given a continuously observed complex path \(p_1\) on a nontrivial compact time interval, its quadratic variation along a deterministic refining sequence of partitions gives \([p_1,p_1]\). The latter has a continuous density by (29), so differentiation determines the entire continuous path \(p_2\), including its value at time zero by a right derivative. Inductively,
\[
\boxed{p_{m+1}(t)=-\frac N m\frac{d}{dt}[p_1,p_m]_t.}
\tag{30}
\]
All these are legitimate path operations almost surely. For each fixed \(N,m\), the trace SDE has bounded drift and diffusion coefficients, because the traces themselves are bounded and (9) removes the apparent collision singularities. Standard Itô-isometry bounds for dyadic covariation sums give convergence along a common deterministic refining sequence; there are only finitely many reconstructions needed for a fixed \(N\). Equivalently one can fix a common almost-sure subsequence using those bounds. Since the covariance densities in (28) are continuous, their one-sided endpoint derivatives recover the initial values as well.

Knowing \(p_1(0),\ldots,p_N(0)\), Newton identities determine every coefficient of
\[
\prod_{j=1}^N(z-z_j(0)).
\]
Thus the unordered initial spectrum, and hence the initial hard-core event, is measurable from the ideal continuous \(p_1\) path. ACUE has that hard-core event with probability one; CUE does not. The continuous \(p_1\) path laws are therefore different.

There is no contradiction with (16). Repeated quadratic-covariation reconstruction and a nonlinear spectral event are not one bounded-degree polynomial observation. The theorem controls a finite total moment budget, not all moments of arbitrarily many readings of a low mode. It also supplies no stability bound for differentiation of covariation estimates, no fixed sampling rate, and no noise robustness. These distinctions matter before proposing this as an experimentally usable discriminator.

## 8. Exact symbolic verification and reproducible small check

The proof of (20) is for all \(N\ge2\) and all \(r\ge1\); the following finite check is a normalization and algebra check, not a substitute for the proof. It was executed once with Python and SymPy. In variables \(z_i\), the radial generator is
\[
\mathcal Lf=\frac1{2N}\left[
-\sum_i(z_i\partial_{z_i})^2f
-\sum_{i<j}\frac{z_i+z_j}{z_i-z_j}
(z_i\partial_{z_i}-z_j\partial_{z_j})f
\right].
\tag{31}
\]
This avoids floating-point angles and performs exact cancellation in rational Laurent expressions.

```python
import sympy as s
from itertools import product

def h(z, r):
    return s.Add(*(
        s.prod(x**k for x, k in zip(z, ks))
        for ks in product(range(r + 1), repeat=len(z))
        if sum(ks) == r
    ))

def generator(f, z):
    n = len(z)
    e = lambda f, i: z[i] * s.diff(f, z[i])
    diffusion = -sum(e(e(f, i), i) for i in range(n))
    drift = -sum(
        (z[i] + z[j]) * (e(f, i) - e(f, j)) / (z[i] - z[j])
        for i in range(n) for j in range(i + 1, n)
    )
    return s.cancel((diffusion + drift) / (2 * n))

for n, r in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 4)]:
    z = s.symbols('z:' + str(n))
    inv = tuple(1 / x for x in z)
    phi = h(z, r) * h(inv, r) - h(z, r-1) * h(inv, r-1)
    eigenvalue = s.Rational(r * (r + n - 1), n)
    residual = s.cancel(generator(phi, z) + eigenvalue * phi)
    print(f'N={n} r={r} Casimir={eigenvalue} residual={residual}')
    assert residual == 0
print('PASS: six exact Laurent-generator eigenfunction checks')
```

Complete output:

```text
N=2 r=1 Casimir=1 residual=0
N=2 r=2 Casimir=3 residual=0
N=2 r=3 Casimir=6 residual=0
N=3 r=1 Casimir=1 residual=0
N=3 r=2 Casimir=8/3 residual=0
N=3 r=4 Casimir=8 residual=0
PASS: six exact Laurent-generator eigenfunction checks
```

No stochastic simulation, parameter scan, fitted coefficient, prime calculation, PDF rebuild, external model call, or Git operation was used in this lane.

## 9. Consequences for the research decision

Adding the correct Brownian noise to deterministic Coulomb flow does not rescue a low-total-weight moment discriminator. Even arbitrary deterministic observation times and exact multitime correlations remain protected under (15). A proposed proof using only these inputs needs an explicit step leaving the protected algebra.

There are now two concrete exits to compare. The first is the balanced character \(\Phi_{N+1}\), with a fully computed heat decay and no asymptotic approximation. The second is pathwise quadratic variation, which reconstructs higher traces but requires stronger observational information. Inverse-gap observables and local singular energies also lie outside the protected trace-polynomial budget, but no new result about their evolution is proved here.

The useful next bounded work would be to quantify stable access to an unprotected observable, or to formulate an actual-zeta input that supplies more than these protected moments. A famous-conjecture claim, an identification of deterministic Newman heat flow with circular DBM, a robust finite-data path-reconstruction algorithm, and a novelty claim are all postponed.
