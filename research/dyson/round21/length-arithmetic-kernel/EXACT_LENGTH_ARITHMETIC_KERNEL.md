# Exact arithmetic kernels and a finite truncation for the all-length variance

Date: 2026-09-05. Status: ordinary proof submitted for independent review. The main identities and finite truncation below are unconditional for T>2. RH is used only in the explicitly separated centered regrouping and boundary discussion. No numerical height is evaluated, and no strict Bragg bound, AH refutation or Montgomery–Dyson theorem is claimed.

The concrete reduction is that, for T≥3, the actual all-length variance can be replaced by an explicit finite, fully centered prime-power functional using only integers up to ⌈2T^{9/4}⌉, with a nonnegative error at most 2048T^{9/4}2^{-T}. This is a finite arithmetic reformulation with a proved error. It does not estimate the signed prime correlation inside that finite functional.

## 1. Definitions and the all-length law

Retain R20's exact nonnegative weight
\[
W_T(x)=\omega(\log x/\log T),\quad
\omega(\alpha)=\psi(4(\alpha-2)),\quad
0\le W_T\le1,
\]
supported on [L,U]=[T^{7/4},T^{9/4}]. Here ψ is the fixed autocorrelation from R16, not a new test function. Put E(y)=Ψ(y)−y, with Ψ right-continuous and Λ(p^k)=log p for every prime power. Define
\[
\begin{aligned}
\overline V_T
&=\frac{T}{\log^2T}\int_L^U\frac{W_T(x)}{x^2}F_T(x)dx,\\
F_T(x)
&=\int_0^\infty e^{-\lambda}
\left[\Psi(e^{\lambda/T}x)-\Psi(x)-(e^{\lambda/T}-1)x\right]^2d\lambda.
\end{aligned}
\tag{1}
\]
The interval is (x,e^{λ/T}x], and the center is its exact length. Neither the lower endpoint Ψ(x) nor either term of the continuous square expansion is discarded.

For fixed x≥1, the substitution q=e^{λ/T} gives the probability measure
\[
e^{-\lambda}d\lambda=Tq^{-T-1}dq,\qquad q\ge1.
\tag{2}
\]
With G_x(y)=E(y)−E(x), a second substitution y=qx yields the positive identity
\[
F_T(x)=T x^T\int_x^\infty G_x(y)^2y^{-T-1}dy.
\tag{3}
\]
The R20 statistic is exactly (1); the weight W_T does not change with λ.

## 2. Absolutely convergent expanded kernels for T>2

**Theorem 1.** For every real T>2 and x≥1, each term of the following expansion is absolutely convergent:
\[
\begin{aligned}
F_T(x)
={}&\sum_{m,n>x}\Lambda(m)\Lambda(n)
\left(\frac{x}{\max(m,n)}\right)^T\\
&-2x\sum_{n>x}\Lambda(n)
\left[\frac{T}{T-1}\left(\frac{x}{n}\right)^{T-1}
-\left(\frac{x}{n}\right)^T\right]
+\frac{2x^2}{(T-1)(T-2)}.
\end{aligned}
\tag{4}
\]
The sums run over all integers with the von Mangoldt weight, including all higher prime powers.

For m,n>x, the pair survival probability under (2) is
\[
\Pr(qx\ge\max(m,n))=(x/\max(m,n))^T.
\]
The mixed moment is, for n>x,
\[
\mathbb E[(q-1)1_{qx\ge n}]
=\frac{T}{T-1}(x/n)^{T-1}-(x/n)^T.
\tag{5}
\]
Finally,
\[
\mathbb E(q-1)^2
=\frac{T}{T-2}-\frac{2T}{T-1}+1
=\frac{2}{(T-1)(T-2)}.
\tag{6}
\]
These elementary integrals prove the constants, once convergence is justified.

Here is a full convergence argument. The elementary bound
\(0\le\Psi(y)\le y\log y\) holds for y≥1 because Λ(n)≤log n. For y≥x≥1, both A=Ψ(y)−Ψ(x) and B=y−x are nonnegative. Therefore
\[
|G_x(y)|=|A-B|\le\max(A,B)\le y(1+\log y).
\tag{7}
\]
The positive square in (3) is integrable for T>2. The two uncentered factors A and B are separately bounded by y(1+log y), so the three expanded integrals are also integrable. Tonelli applies to the nonnegative pair and mixed terms, and their finite sums of absolute values permit ordinary Fubini for the signed expansion. This bound is uniform when x ranges in any fixed compact interval [L,U], and consequently justifies the additional x integration in (1).

Equivalently, let dE(u)=Σ_nΛ(n)δ_n(du)−du, restricted to (x,∞). Then
\[
F_T(x)=\iint_{u,v>x}
\left(\frac{x}{\max(u,v)}\right)^T dE(u)dE(v).
\tag{8}
\]
This is an absolutely convergent signed-measure integral for T>2: the cumulative total variation is at most Ψ(y)−Ψ(x)+y−x≤y(1+log y). Applying the positive survival representation of the kernel to its total variation product gives a finite majorant of the same form as (3). Equation (8) is therefore not a formal difference of divergent integrals in this range.

## 3. The complete outer arithmetic kernel and prime-gap form

For real s define a finite weight moment
\[
J_s(b)=\int_L^{\min(U,b)}W_T(x)x^{s-2}dx,
\tag{9}
\]
with J_s(b)=0 for b≤L and J_s(∞)=J_s(U). These are ordinary finite integrals of the fixed logarithmic weight. In this section T is fixed, and no uniform-in-s approximation is assumed.

Substitution of (4) into (1), with the absolute convergence just proved, gives
\[
\begin{aligned}
\overline V_T=\frac{T}{\log^2T}\Bigg\{&
\sum_{m,n\ge2}\frac{\Lambda(m)\Lambda(n)}{\max(m,n)^T}
J_T(\min(m,n))\\
&-2\sum_{n\ge2}\Lambda(n)
\left[\frac{T}{T-1}\frac{J_T(n)}{n^{T-1}}
-\frac{J_{T+1}(n)}{n^T}\right]
+\frac{2J_2(\infty)}{(T-1)(T-2)}\Bigg\}.
\end{aligned}
\tag{10}
\]
The uncentered pair term in braces is precisely
\[
\sum_{n\ge2}\frac{\Lambda(n)^2J_T(n)}{n^T}
+2\sum_{h\ge1}\sum_{m\ge2}
\frac{\Lambda(m)\Lambda(m+h)J_T(m)}{(m+h)^T}.
\tag{11}
\]
This is an actual prime-power gap sum with its full asymmetric weight. It is not an independence approximation or an unweighted Hardy–Littlewood conjecture. The two large centering terms in (10) remain essential; positivity of the uncentered terms alone supplies no strict upper bound for their centered combination.

There is also a useful pointwise single-sum form. Ordering the pair term in (4) by its larger index gives
\[
\sum_{m,n>x}\Lambda(m)\Lambda(n)(x/\max(m,n))^T
=x^T\sum_{n>x}\frac{\Lambda(n)}{n^T}
\left[2(\Psi(n)-\Psi(x))-\Lambda(n)\right].
\]
Thus, without changing convergence range,
\[
\boxed{F_T(x)=x^T\sum_{n>x}\frac{\Lambda(n)}{n^T}
\left[2(E(n)-E(x))-\Lambda(n)-\frac{2n}{T-1}\right]
+\frac{2x^2}{(T-1)(T-2)}.}
\tag{12}
\]
The term −Λ(n) removes the duplicated diagonal. If one wants a fully integrated version, define
\(J^E_T(b)=\int_L^{\min(U,b)}W_T(x)x^{T-2}E(x)dx\).
Then the braces in (10) equal
\[
\sum_{n\ge2}\frac{\Lambda(n)}{n^T}
\left[\left(2E(n)-\Lambda(n)-\frac{2n}{T-1}\right)J_T(n)
-2J^E_T(n)\right]
+\frac{2J_2(\infty)}{(T-1)(T-2)}.
\tag{13}
\]
Equations (11) and (13) identify two exact arithmetic formulations of the same remaining signed problem. Neither controls its sign more strongly than (1).

## 4. A finite endpoint truncation with exact kernels

Choose a real endpoint N≥U, and truncate the upper interval endpoint y=qx, rather than deleting selected prime terms from an infinite expanded expression:
\[
F_{T,N}(x)=T x^T\int_x^N G_x(y)^2y^{-T-1}dy,
\qquad
\overline V_{T,N}=\frac{T}{\log^2T}\int_L^U
\frac{W_T(x)}{x^2}F_{T,N}(x)dx.
\tag{14}
\]
This is a genuine nonnegative portion of the original variance. In particular
\[
0\le\overline V_{T,N}\le\overline V_T,
\quad
\overline V_T-\overline V_{T,N}
=\frac{T^2}{\log^2T}\int_L^U W_T(x)x^{T-2}
\int_N^\infty G_x(y)^2y^{-T-1}dy\,dx.
\tag{15}
\]

Put z=x/N and B_T(r)=T r^{T-1}/(T−1)−r^T. For T>2 the exact finite formula is
\[
\begin{aligned}
F_{T,N}(x)={}&
\sum_{x<m,n\le N}\Lambda(m)\Lambda(n)
\left[(x/\max(m,n))^T-z^T\right]\\
&-2x\sum_{x<n\le N}\Lambda(n)
\left[B_T(x/n)-B_T(z)\right]+x^2 C_{T,N}(x),\\
C_{T,N}(x)={}&\frac2{(T-1)(T-2)}
-\frac{T}{T-2}z^{T-2}
+\frac{2T}{T-1}z^{T-1}-z^T.
\end{aligned}
\tag{16}
\]
These kernels integrate q only from 1 to N/x. If n=N, its survival difference vanishes as it should: the endpoint jump has zero measure in the q integral. All pair, mixed and continuous contributions are retained. For the outer statistic the exact finite version of (10) is
\[
\begin{aligned}
\overline V_{T,N}=\frac{T}{\log^2T}\Bigg\{&
\sum_{2\le m,n\le N}\Lambda(m)\Lambda(n)
\left[\max(m,n)^{-T}-N^{-T}\right]J_T(\min(m,n))\\
&-2\sum_{2\le n\le N}\Lambda(n)
\left[\frac{T}{T-1}(n^{1-T}-N^{1-T})J_T(n)
-(n^{-T}-N^{-T})J_{T+1}(n)\right]\\
&+\frac{2J_2(\infty)}{(T-1)(T-2)}
-\frac{T}{T-2}N^{2-T}J_T(\infty)\\
&+\frac{2T}{T-1}N^{1-T}J_{T+1}(\infty)
-N^{-T}J_{T+2}(\infty)\Bigg\}.
\end{aligned}
\tag{17}
\]
Thus only actual prime powers up to N and finite integrals of the fixed weight occur. The cutoff changes all three terms coherently. Merely removing n>N from (10) while keeping its original infinite continuous center is a different statistic and need not give the positive truncation (14).

## 5. Explicit unconditional remainder and a finite arithmetic target

For a>0 and b≥0 write
\[
P_2(a,b)=\frac{b^2}{a}+\frac{2b}{a^2}+\frac2{a^3}.
\]
Using (7), elementary integration gives, for T>2 and N≥x,
\[
\begin{aligned}
0\le F_T(x)-F_{T,N}(x)
&\le T x^T\int_N^\infty y^{1-T}(1+\log y)^2dy\\
&=T x^T N^{2-T}P_2(T-2,1+\log N).
\end{aligned}
\tag{18}
\]
Consequently the complete explicit bound is
\[
\boxed{0\le\overline V_T-\overline V_{T,N}
\le\frac{T^2}{\log^2T}N^{2-T}
P_2(T-2,1+\log N)J_T(\infty).}
\tag{19}
\]
No unproved prime estimate or RH is used. If desired, J_T(∞) may be replaced by
\((U^{T-1}-L^{T-1})/(T-1)\), since 0≤W_T≤1.

**Corollary.** For all real T≥3, with N=⌈2T^{9/4}⌉,
\[
\boxed{0\le\overline V_T-\overline V_{T,N}
\le2048\,T^{9/4}2^{-T}.}
\tag{20}
\]
To verify the constant, first set N₀=2U. The actual positive remainder decreases with N, so it suffices to bound at N₀. Put a=T−2 and b=1+log(2U). For T≥3, a≥1, b≥1,
\[
P_2(a,b)\le5b^2/a,\quad
b/\log T<17/4,\quad
\frac{T^2}{(T-1)(T-2)}\le9/2.
\]
The second inequality follows from log T>1 and log 2<log T. Substituting these bounds and J_T(∞)≤U^{T-1}/(T−1) into (19) gives at most
\[
\frac{13005}{8}\,U2^{-T}<2048\,U2^{-T}.
\]
Ceiling the endpoint only decreases the remainder. This proves (20).

In particular the two sequences in (20) differ by o(1), without RH. Under the separate R20 RH transfer, any strict limiting arithmetic criterion for the all-length variance can therefore be posed equivalently for the **finite expression (17)** with this explicit endpoint. For example,
\[
\liminf_{T\to\infty}\overline V_{T,\lceil2T^{9/4}\rceil}\le1
\]
would imply the same inequality for the full all-length variance, which is strictly below A_ε=1+ε²m₁. This displayed condition is a target, not a result of the present proof. The approximation error in (20) gives no upper bound on the finite expression itself.

## 6. The T=2 boundary: centered convergence is not separate-term convergence

Under RH, use the standard global consequence
\[
|E(y)|\le C\sqrt y\log^2(2y)\qquad(y\ge1)
\tag{21}
\]
for some fixed C. R20 pins the primary source and explains the harmless bounded initial range. For any T>1 this implies convergence of the centered energy (3). In particular the R20 all-length variance exists at T=2.

At T=2, however, the continuous term E(q−1)² diverges logarithmically. Even under RH the uncentered arithmetic count is Ψ(qx)−Ψ(x)=qx+o(q) for fixed x, so its square and its positive mixed moment also have logarithmically divergent integrals against 2q^{-3}dq. Thus (4) cannot be continued by interchanging and subtracting those infinite positive terms. The centered integral exists because cancellation occurs before the square is averaged.

Finite endpoint truncation is still legal at T=2. The pair difference and B_T in (16) have ordinary limits, and the continuous coefficient becomes
\[
C_{2,N}(x)=2\log(N/x)+4x/N-(x/N)^2-3.
\tag{22}
\]
This is the exact integral of 2(q−1)²q^{-3} over 1≤q≤N/x. It is zero at N=x. There is no infinite continuous constant at this boundary.

There is a separate useful **centered Stieltjes regrouping**. For a finite N≥x, the jump of G_x at an integer n>x is Λ(n). With the right-continuous convention,
\[
d(G_x^2)=2G_x\,dE-\sum_{n>x}\Lambda(n)^2\delta_n.
\]
Ordinary Stieltjes integration by parts therefore gives the exact finite identity
\[
\begin{aligned}
F_{T,N}(x)={}&
\sum_{x<n\le N}\Lambda(n)(x/n)^T
[2G_x(n)-\Lambda(n)]\\
&-2\int_x^N(x/y)^T G_x(y)dy
-(x/N)^TG_x(N)^2.
\end{aligned}
\tag{23}
\]
The final boundary term is required, including when N itself is a prime power. It cancels the spurious endpoint jump that would otherwise be counted despite its zero measure in (14).

Under (21), the two terms in (23) converge absolutely as N→∞ for T>3/2. For example the discrete term is dominated by constant multiples of Σ n^{1/2−T}log³(2n), Σn^{-T}log²n and Σn^{-T}log n. The boundary term tends to zero for T>1. Hence for T>3/2 one obtains the legal centered formula
\[
F_T(x)=\sum_{n>x}\Lambda(n)(x/n)^T
[2(E(n)-E(x))-\Lambda(n)]
-2\int_x^\infty(x/y)^T(E(y)-E(x))dy.
\tag{24}
\]
This is a new grouping, not an interpretation of the separately divergent terms of (4). No claim of absolute convergence of this grouping for 1<T≤3/2 is made.

At T=2 the remaining continuous integral can be evaluated exactly in terms of a finite prime-power prefix. For real σ>1, partial summation and the absolutely convergent Euler product give
\[
\int_1^\infty E(y)y^{-\sigma-1}dy
=\frac{-\zeta'/\zeta(\sigma)}{\sigma}-\frac1{\sigma-1}.
\]
The Laurent expansion −ζ′/ζ(σ)=1/(σ−1)−γ+O(σ−1), together with dominated convergence from (21), yields
\(\int_1^\infty E(y)y^{-2}dy=-\gamma-1\).
Subtracting the finite integral over [1,x] and then E(x)/x gives
\[
\int_x^\infty\frac{E(y)-E(x)}{y^2}dy
=\log x-\gamma-\sum_{n\le x}\frac{\Lambda(n)}n.
\tag{25}
\]
Thus the boundary statistic has the absolutely convergent RH representation
\[
\boxed{F_2(x)=x^2\sum_{n>x}\frac{\Lambda(n)}{n^2}
[2(E(n)-E(x))-\Lambda(n)]
-2x^2\left(\log x-\gamma-\sum_{n\le x}\frac{\Lambda(n)}n\right).}
\tag{26}
\]
The constant γ is Euler's constant. The right-continuous convention, including a prime power at x, is consistent on both sides. Equation (26) retains a signed ΛE tail; it gives no new positivity or strict upper estimate for that tail.

## 7. RH remainder for the centered truncation, including T=2

For a>0 define
\[
P_4(a,b)=\frac{b^4}{a}+\frac{4b^3}{a^2}
+\frac{12b^2}{a^3}+\frac{24b}{a^4}+\frac{24}{a^5}.
\]
From (21),
\[
G_x(y)^2\le2C^2\left[y\log^4(2y)+x\log^4(2x)\right].
\]
Therefore for T>1 and N≥x,
\[
\begin{aligned}
0\le F_T(x)-F_{T,N}(x)
\le2C^2\Big[&T x^T N^{1-T}P_4(T-1,\log(2N))\\
&+x(x/N)^T\log^4(2x)\Big].
\end{aligned}
\tag{27}
\]
For the full logarithmic window this implies
\[
\begin{aligned}
0\le\overline V_T-\overline V_{T,N}
\le\frac{2C^2T}{\log^2T}\Big[&T N^{1-T}P_4(T-1,\log(2N))J_T(\infty)\\
&+N^{-T}\int_L^U W_T(x)x^{T-1}\log^4(2x)dx\Big].
\end{aligned}
\tag{28}
\]
This is explicit once a global constant C in (21) is specified. It is a genuine finite centered tail estimate at T=2, where the uncentered expansion is unavailable. For large T≥3 the simpler unconditional bound (20) already suffices for finite reduction. No numerical choice of C or numerical boundary-height calculation is made here.

## 8. Verification, provenance and the remaining arithmetic obligation

The adjacent `check_length_arithmetic.py` performs only bounded symbolic checks. It verifies the survival and mixed moments, the finite continuous kernel and its T=2 limit, the elementary tail antiderivatives, the rational constant in (20), and finite equality of direct centered integration, the pair/mixed/continuous expansion and the Stieltjes formula including its boundary term. Controls include actual prime-power logarithms on a small finite interval and independent signed rational coefficients. These are algebraic controls, not numerical evaluations of any requested height and not a verification of RH or the asymptotic arithmetic estimate.

The only existing mathematical inputs used beyond elementary calculus, counting and Stieltjes integration are:

- [R20 all-length variance proof](../../research-round20/length-averaged-variance/EXPONENTIAL_LENGTH_AVERAGE.md), SHA256 `cd8c2f7dc48530ed02f915dd202c8aedaaaadb1096cafc019beeb595b9beebbe`: definition of the statistic, its RH transfer and the pinned classical RH bound (21). The present absolute kernel expansion and unconditional finite truncation are derived here.
- [R19 positive variance proof](../../research-round19/bragg-variance-literature/BRAGG_WEIGHTED_SELBERG_VARIANCE.md), SHA256 `0c5323ac5a983148a9ec433ea1196fb0fd538f00872ac73e9de3ae105c7a2502`: the fixed logarithmic weight and prior finite-length arithmetic normalization.
- The elementary Euler-product identity for −ζ′/ζ in Re σ>1 and its standard Laurent constant at 1, used only in the separately RH-centered boundary formula (26). No functional equation, zero-density estimate or new source-range assumption is imported.

The finite expression (17), the prime-gap version (11), and the signed weighted-Ψ version (13) are exact formulations. The finite cutoff error is controlled independently of any conjecture. What is still missing is a strictly improved asymptotic estimate for the centered arithmetic combination. All positive kernels and exact integrations above remain compatible with the AH saturation value. No strict bound is inferred from this calculation.

Postponed: any numerical height, any new parameter or seed choice, an unbounded prime-gap computation, optimization of the harmless constant 2048, and a proof of the remaining signed prime correlation estimate. No prior-round file or Git state is changed.
