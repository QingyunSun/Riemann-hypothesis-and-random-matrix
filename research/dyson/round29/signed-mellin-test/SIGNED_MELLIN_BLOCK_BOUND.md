# The fixed Möbius/log pairing: an RH bounded central block, with all Mellin bands retained

Date: 2026-09-05. Author: Euclid. Status: ordinary proof submitted for independent review. The theorem below assumes ordinary RH. It is a newly verified application of classical mean-value, van der Corput, Cramér and Selberg estimates within this programme; no novelty claim is made.

The result is an \(O(1)\) bound for each actual balanced central cofactor block, improving the growing bound obtained from a Frobenius norm in R27. It proves neither \(o(1)\), a numerical constant below a target, nor a strict global variance deficit. In particular, the inherited \(O(1)\) bound for the complete R26 aggregate is a separate earlier statement, not a consequence newly obtained here.

## 1. Exact arithmetic object and theorem

Put
\[
X=T^2,\qquad Y=T,\qquad \ell=\log T,
\]
and retain the fixed smooth weight \(\omega\), supported on \([7/4,9/4]\), and the exact kernel
\[
b_T(x)=\frac{T}{x^T\ell^2}\int_1^x
\omega(\log u/\ell)u^{T-2}\,du.
\]
Fix real \(\chi,V\in C_c^\infty((1,2))\), and set
\[
F(x,h)=b_T(x)\chi(x/X)V(h/Y)(1+h/x)^{-T}.
\tag{1}
\]
Let \(D,K\asymp T\), with fixed positive comparison constants, and use the sharp sets
\[
\mathcal D=\{d:D<d\le2D,\ d\ \mathrm{odd}\},\quad
\mathcal K=\{k:K<k\le2K,\ k\ \mathrm{odd}\}.
\]
The actual fixed-vector block is
\[
Z_{D,K}=2\sum_{d\in\mathcal D}\sum_{k\in\mathcal K}
\mu(d)\log k\sum_{h\ \mathrm{even}}
F(dk,h)[\Lambda(dk+h)-2].
\tag{2}
\]
All sums in (2) are finite. The product cutoff \(\chi(dk/X)\) is retained. All prime powers on odd endpoints are retained. No coprimality condition between \(d\) and \(k\) is inserted.

**Theorem.** Under RH, for all sufficiently large \(T\),
\[
\boxed{|Z_{D,K}|\ll_{\omega,\chi,V,D/T,K/T}1.}
\tag{3}
\]
The comparison constants for \(D/T,K/T\) range over any fixed compact subset of \((0,\infty)\). With the exact Mellin representation below, the frequencies \(|t|\le\pi K/2\) contribute \(O(1/\log X)\). For each fixed integer \(j\ge2\), the remaining dyadic band \(R<|t|\le2R\), \(R\ge\pi K/2\), contributes
\[
O_j((R/T)^{1-j}).
\tag{4}
\]
The sum of (4) over all such dyadic bands converges. Thus (3) concerns the complete block, not just one carrier band.

The proof actually uses only \(|\mu(d)|\le1\) and its mean-square diagonal. It keeps the genuine Möbius coefficients but establishes no additional cancellation special to \(\mu\).

## 2. A legal smooth extension and exact Mellin inversion

Write
\[
A(x)=X\ell^2 b_T(x)\chi(x/X),\quad
k(x,u)=V((u-x)/Y)(x/u)^T,
\]
and define the real-variable extension
\[
f(x)=A(x)\sum_{n\ \mathrm{odd}}k(x,n)[\Lambda(n)-2].
\tag{5}
\]
For sufficiently large \(T\), only \(X<n<3X\) can occur. Equation (5) is a finite sum of smooth functions of \(x\), supported compactly inside \((X,2X)\). At each odd integer \(m\),
\[
f(m)=X\ell^2\sum_{h\ \mathrm{even}}
F(m,h)[\Lambda(m+h)-2].
\tag{6}
\]
We never differentiate an expression \(\Lambda(x+h)\). Derivatives in (5) hold the integer \(n\) fixed and have natural scale \(Y\), not \(X\).

Use
\[
\widehat f(t)=\int_0^\infty f(x)x^{-it}\frac{dx}{x},\qquad
f(x)=\frac1{2\pi}\int_{\mathbb R}\widehat f(t)x^{it}\,dt,
\]
\[
M_D(t)=\sum_{d\in\mathcal D}\mu(d)d^{it},\qquad
B_K(t)=\sum_{k\in\mathcal K}(\log k)k^{it}.
\]
Then the exact identity is
\[
\boxed{
Z_{D,K}=\frac1{\pi X\ell^2}
\int_{\mathbb R}\widehat f(t)M_D(t)B_K(t)\,dt.}
\tag{7}
\]
The inverse-Mellin signs are both positive in \(M_D,B_K\). The factor \(1/\pi\) includes the original \(2\) in (2). The integral converges absolutely for each \(T\): \(\widehat f\) is Schwartz and the two Dirichlet polynomials are finite and bounded. Sharp \(d,k\) endpoints cause no issue in this inversion.

## 3. The two arithmetic Sobolev bounds for the true extension

We prove under RH, for each fixed nonnegative integer \(j\),
\[
\boxed{
\int_{\mathbb R}(1+(t/T)^2)^j|\widehat f(t)|^2\,dt
\ll_j Y(\log X)^2,}
\tag{8}
\]
and the additional low-frequency bound
\[
\boxed{
\int_{\mathbb R}\frac{|\widehat f(t)|^2}{1+t^2}\,dt\ll1.}
\tag{9}
\]
The second statement does not follow merely by dropping a factor from (8).

### 3.1 Positive derivatives: centered short intervals and fixed-parameter Selberg

The exact weight satisfies \((x\partial_x)^r A(x)=O_r(1)\). For instance, after substituting \(u=xz\) in its defining integral,
\[
X\ell^2 b_T(x)=\frac{XT}{x}
\int_{1/x}^{1}\omega((\log x+\log z)/\ell)z^{T-2}\,dz.
\]
Boundary terms at \(u=1\) vanish for this fixed weight. Differentiation of the smooth weight costs at most fixed powers of \(1/\ell\), and the integral has mass at most \(1/(T-1)\). Multiplying by \(\chi(x/X)\) preserves the bound.

Put \(P_0(x,h)=A(x)V(h/Y)(1+h/x)^{-T}\) and
\[
P_j(x,h)=\bigl[x(\partial_x-\partial_h)\bigr]^jP_0(x,h).
\]
Then
\[
(x\partial_x)^jf(x)=
\sum_{n\ \mathrm{odd}}P_j(x,n-x)[\Lambda(n)-2].
\]
On \(x\asymp X,\ h\asymp Y\), each fixed \(j\) obeys
\[
|P_j(x,h)|\ll_j T^j,\qquad
|\partial_hP_j(x,h)|\ll_j T^j/Y,
\tag{10}
\]
with compact support in \(Y<h<2Y\). These are derivatives of the kernel at fixed \(n\). The large factors are controlled by \(x/Y\asymp T\) and \(T\), and differentiation creates no prime-counting derivative.

For real \(x,y\), let
\[
\mathcal A_x(y)=\sum_{\substack{x<n\le x+y\\n\ {\rm odd}}}
[\Lambda(n)-2].
\]
Writing \(E(x)=\Psi(x)-x\), the exact endpoint formula is
\[
\mathcal A_x(y)=E(x+y)-E(x)
+y-2N_{\rm odd}(x,x+y)
-(\log2)\#\{r:x<2^r\le x+y\},
\tag{11}
\]
where
\[
N_{\rm odd}(x,x+y)
=\left\lfloor\frac{x+y+1}{2}\right\rfloor
-\left\lfloor\frac{x+1}{2}\right\rfloor.
\]
The staircase term in (11) has absolute value at most \(2\). If \(x\asymp X,\ y\asymp Y\), there is at most one power of \(2\) in the interval for large \(T\), so the total correction to the \(E\) increment is \(O(1)\).

Stieltjes partial summation, with the compact kernel endpoints exactly zero, gives
\[
|(x\partial_x)^jf(x)|^2
\ll_j\frac{T^{2j}}{Y}\int_Y^{2Y}|\mathcal A_x(y)|^2\,dy.
\tag{12}
\]
The primary CCCC paper defines
\[
J(3,S)=\int_1^{S^3}
\bigl[E(x+x/S)-E(x)\bigr]^2\,\frac{dx}{x^2},
\]
and its equation (1.3) gives under RH
\[
J(3,S)\ll\frac{\log^2S}{S}.
\tag{13}
\]
This is a fixed-\(\beta=3\) statement. To use it legally in the double integral in (12), set \(\lambda=Ty/x\). The enclosing interval is the fixed \([1/2,2]\), and \(dy=(x/T)d\lambda\). For each fixed \(\lambda\) put \(S=T/\lambda\). For large \(T\), \([X,2X]\subset[1,S^3]\) uniformly on that interval. Positivity, \(x^3\ll X^3\), and (13) yield
\[
\int_X^{2X}\int_Y^{2Y}|E(x+y)-E(x)|^2\,dy\,dx
\ll \frac{X^3}{T}
\int_{1/2}^{2}J(3,T/\lambda)\,d\lambda
\ll XY^2(\log X)^2.
\tag{14}
\]
The \(O(1)\) corrections in (11) add only \(O(XY)\). Integrating (12) in \(dx/x\) therefore proves
\[
\int_0^\infty|(x\partial_x)^jf(x)|^2\frac{dx}{x}
\ll_j T^{2j}Y(\log X)^2.
\]
Plancherel on \(v=\log x\), followed by the finite binomial expansion, proves (8). This does not assume a \(Y\log X\) one-block variance.

### 3.2 One negative derivative: Cramér mean square, with the center retained

The classical RH bound, explicitly stated in Brent–Platt–Trudgian, equation (1), printed page 741, is
\[
\int_Z^{2Z}|E(u)|^2\,du\ll Z^2.
\]
Covering \([X,3X]\) by \([X,2X]\) and \([2X,4X]\) gives
\[
\int_X^{3X}|E(u)|^2\,du\ll X^2.
\tag{15}
\]
The paper proves a sharper numerical constant, but no such constant is used here. Pointwise RH \(E(x)=O(\sqrt{x}\log^2x)\) alone would introduce extra logarithms and would not give (15).

In the kernel estimates in this subsection, restrict \(x\in[X,2X]\) and \(u\in[X,3X]\), as required by the factors \(A\) and \(A'\). The auxiliary function \(S\) below is not itself globally compactly supported. For the exact kernel in (5) define
\[
S(x)=\int E(u)k(x,u)\,du,\qquad
r(x,u)=T(1/x-1/u).
\]
There is the elementary derivative identity
\[
\partial_xk+\partial_uk=r(x,u)k,\qquad
|r(x,u)|\ll 1/X
\quad\hbox{on the support}.
\tag{16}
\]
Also define the exact lattice and even-prime-power corrections
\[
\mathcal L(x)=\int k(x,u)\,du
-2\sum_{n\ {\rm odd}}k(x,n),\qquad
\mathcal P_2(x)=(\log2)\sum_{r\ge1}k(x,2^r).
\]
Stieltjes integration by parts in \(u\), retaining all prime powers and the continuous center, gives
\[
f(x)=A(x)\left[
S'(x)-\int E(u)r(x,u)k(x,u)\,du
+\mathcal L(x)-\mathcal P_2(x)\right].
\tag{17}
\]
No endpoint term survives: \(k\) vanishes smoothly at both ends of its compact \(u\) support.

In logarithmic coordinates put
\[
G(v)=\frac{A(x)S(x)}{x},\quad x=e^v.
\]
Then (17) is exactly
\[
f(e^v)=G'(v)+R(v),
\tag{18}
\]
\[
R(v)=\left(\frac{A(x)}x-A'(x)\right)S(x)
-A(x)\int E(u)r(x,u)k(x,u)\,du
+A(x)[\mathcal L(x)-\mathcal P_2(x)].
\]
The sign of \(A/x-A'\) follows by differentiating \(AS/x\) in \(v\). We do not differentiate \(E\).

The kernel \(k\) has bounded amplitude, with both its \(x\) and \(u\) support sections of length \(O(Y)\). Schur's integral bound, or Cauchy followed by changing order, gives
\[
\int_X^{2X}|S(x)|^2dx\ll Y^2\int_X^{3X}|E(u)|^2du\ll Y^2X^2.
\]
Since \(A=O(1)\), \(A'=O(1/X)\), and \(dx/x\asymp dx/X\),
the first terms in \(G,R\) have squared \(L^2(dv)\) norms \(O(Y^2/X)=O(1)\). The term involving \(r k\) has the same bound by (16).

Poisson summation on the odd lattice retains its exact half-step:
\[
\mathcal L(x)=-\sum_{\nu\ne0}(-1)^\nu
\widehat{k(x,\cdot)}(\nu/2).
\]
For every fixed \(q\ge2\),
\(\|\partial_u^q k(x,\cdot)\|_1\ll_qY^{1-q}\); hence
\(|\mathcal L(x)|\ll_qY^{1-q}\). This is uniformly \(O(Y^{-1})\) when \(q=2\).
There are \(O(1)\) powers of \(2\) in \((X,3X)\). Each contributes a bounded function of \(x\) supported on an interval of length \(O(Y)\), so
\[
\|A\mathcal P_2\|_{L^2(dx/x)}^2\ll Y/X.
\]
Consequently
\[
\|G\|_2+\|R\|_2\ll1.
\tag{19}
\]
All fields in (18) are compactly supported; \(G\) is smooth since the derivatives fall on the kernel. Fourier transforming (18) gives
\(\widehat f(t)=it\,\widehat G(t)+\widehat R(t)\).
Plancherel and \(|t|/\sqrt{1+t^2}\le1\) prove (9).

## 4. Source-valid bounds for the two fixed Dirichlet polynomials

Montgomery–Vaughan's primary *Hilbert's Inequality*, Corollary 3, equation (1.11), printed page 75, gives the ordinary Dirichlet-polynomial mean-value theorem. Applying it to a finite polynomial supported on \(\mathcal D\), and absorbing a translation of the \(t\) interval into unimodular coefficients, gives
\[
\boxed{
\int_a^{a+R}|M_D(t)|^2dt
\ll (R+D)\sum_{d\in\mathcal D}|\mu(d)|^2
\ll (R+D)D.}
\tag{20}
\]
This holds for every real \(a\) and every \(R>0\), with no RH assumption. It does not assume square-root cancellation pointwise in \(M_D\).

For \(B_K\), write the odd integers as \(k=2r+1\). The phase in the \(e^{2\pi i(\cdot)}\) convention is
\[
\phi_t(r)=\frac{t}{2\pi}\log(2r+1),\quad
\phi_t'(r)=\frac{t}{\pi(2r+1)},\quad
\phi_t''(r)=-\frac{2t}{\pi(2r+1)^2}.
\tag{21}
\]
Therefore the stationary Poisson aliases satisfy \(t/k=\pi j\), \(j\in\mathbb Z\), not \(2\pi j\).
The adjacent-term phase increment is exactly
\(t\log(1+2/k)/(2\pi)\); its integer resonances occur at
\(t=2\pi j/\log(1+2/k)=\pi j(k+1+O(1/k))\).
These discrete increment centers and the continuous stationary points are not identified with each other. The safe low interval below stays away from both, and (23) handles all higher frequencies.

For \(|t|\le\pi K/2\), the derivative stays in a half-cell away from all nonzero integers. The Kusmin–Landau first-derivative estimate, followed by partial summation of \(\log k\), proves
\[
\boxed{
|B_K(t)|\ll\frac{K\log(2K)}{1+|t|},
\qquad |t|\le\pi K/2.}
\tag{22}
\]
For \(0<|t|\le1\) the trivial bound is enough. For \(1\le |t|\le\pi K/2\), the distance of the phase derivative from the nearest integer is at least a constant times \(|t|/K\). Reversing orientation or taking conjugates handles decreasing derivatives and negative \(t\). The estimate applies to every partial interval of the original sharp odd-index set, so the amplitude partial summation does not smooth or discard its endpoints.

For every \(t\ne0\), the second-derivative theorem gives
\[
|B_K(t)|\ll\log(2K)
\left(\sqrt{|t|}+\frac K{\sqrt{|t|}}\right).
\tag{23}
\]
For \(|t|\ge\pi K/2\), this is \(O(\sqrt{|t|}\log X)\). It remains a valid upper bound when \(|t|>K^2\), where it can be weaker than the trivial bound. It includes all stationary aliases and their edge cases; we have not used a nonstationary estimate past its range.

The exact primary references for (22), (23) are Montgomery–Vaughan's author-hosted *Multiplicative Number Theory II* draft, Corollary 16.6, printed page 7, and Theorem 16.7, printed page 8. In (23), the derivative parameter is \(|t|/K^2\) and the integer interval has length \(O(K)\), giving precisely the two displayed terms.

## 5. Complete frequency accounting

Let \(R_0=\pi K/2\asymp T\). From (9), (20), (22) and Cauchy–Schwarz over the entire low interval,
\[
\begin{aligned}
\left|\int_{|t|\le R_0}\widehat f(t)M_D(t)B_K(t)\,dt\right|
&\ll K\log X
\left(\int\frac{|\widehat f(t)|^2}{1+t^2}dt\right)^{1/2}
\left(\int_{|t|\le R_0}|M_D(t)|^2dt\right)^{1/2}\\
&\ll T^2\log X.
\end{aligned}
\]
After the exact normalization \(1/(\pi X\ell^2)\), this is
\[
O(1/\log X).
\tag{24}
\]
No summation over low dyadic bands, and therefore no gratuitous logarithm from such a sum, is required.

Now let \(R=2^rR_0\), \(r\ge0\), and consider either or both of the bands \(R<|t|\le2R\). Equations (8), (20), (23) give
\[
\|\widehat f\|_{L^2(R<|t|\le2R)}
\ll_j T^{j+1/2}(\log X)R^{-j},
\]
\[
\|M_D\|_{L^2(R<|t|\le2R)}\ll\sqrt{RT},\qquad
\|B_K\|_{L^\infty(R<|t|\le2R)}
\ll \sqrt R\log X.
\]
Thus the normalized integral on that band is
\[
\ll_j\frac{
T^{j+1/2}(\log X)R^{-j}\sqrt{RT}\sqrt R\log X}
{T^2\ell^2}
\ll_j (R/T)^{1-j}.
\tag{25}
\]
Choosing \(j=2\) sums a convergent geometric series and proves (3). For any fixed \(j\ge2\), the total contribution of \(|t|>AT\), with \(A\) larger than a fixed constant, is \(O_j(A^{1-j})\), uniformly for large \(T\). This latter assertion is an upper tail bound; it is not a claim that the intermediate carrier interval tends to zero.

The \(\log X\) from the actual cofactor weight and the \(\log X\) from the available short-interval \(L^2\) estimate exactly cancel the \(\ell^2\) denominator in (25). There is no remaining logarithmic saving. If, hypothetically, (8) for the relevant derivative orders improved to \(Y\log X\), the same carrier/high-band calculation would gain \((\log X)^{-1/2}\). Such a pointwise central-block improvement is **not** supplied by a log-height averaged variance bound, and is not assumed here.

## 6. What has and has not been obtained

This proof bounds the true fixed \(\mu(d)\log k\) contraction at the natural scale without first taking an operator norm over all vectors. It preserves the nonseparable arithmetic packet and covers all Mellin frequencies. The classical RH Cramér bound removes the nonstationary low interval with a logarithmic saving; the genuine stationary-alias range remains only bounded.

The result is restricted to the balanced central geometry \(D,K\asymp T\), \(X=T^2\), \(Y=T\), and fixed smooth profiles. It does not handle all unbalanced cofactor rows, the lowest \(Y=\sqrt{\log T}\) scales, or the complete height/shift partition of R26. In particular, one cannot sum an unspecified \(O(1)\) constant over the global collection of packets and infer a strict or even improved global bound.

No asserted inequality here gives \(Z_{D,K}=o(1)\), gives the needed sign, or compares an explicit constant with the AH variance threshold. The remaining task is quantitative improvement or joint cancellation in the actual signed carrier integral in (7), rather than a uniform matrix estimate. A stronger local prime-variance input or an actual correlated estimate for \(\widehat f M_D B_K\) would be needed to extract the missing logarithm by this argument.

Primary sources used:

- [Montgomery–Vaughan, *Hilbert's Inequality* (1974)](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf), Corollary 3, equation (1.11), printed page 75.
- [Montgomery–Vaughan, author-hosted *Multiplicative Number Theory II* draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf), Corollary 16.6 and Theorem 16.7, printed pages 7–8.
- [Brent–Platt–Trudgian, *The mean square of the error term in the prime number theorem*](https://maths-people.anu.edu.au/~brent/pd/rpb274-final.pdf), JNT 238 (2022), equation (1) and Theorem 1, printed page 741. Only its \(O(X^2)\) RH upper bound is used.
- [Carneiro–Chandee–Chirre–Milinovich, *A tale of three integrals*](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), equations (1.1), (1.3), printed page 1; the application keeps fixed \(\beta=3\) and integrates over a fixed \(\lambda\) interval.

Frozen R27/R28 supply the target definitions and prior scope, not a stronger arithmetic bound. The adjacent finite checker verifies algebra and normalizations only; it does not perform a prime-height scan or certify the asymptotic constants.
