# Independent review: the complete balanced central signed Mellin block is bounded under RH

Date: 2026-09-05. Reviewer: Plato (`residual_gram`), independent of author Euclid. Status: ordinary proof accepted after the explicit support clarification below; the final author version and tiny copied replay are pinned in `REVIEW_RECEIPT.json`. No original author or primary file was edited by the reviewer.

Reviewed manuscript: `../signed-mellin-test/SIGNED_MELLIN_BLOCK_BOUND.md`. I read the complete proof, complete finite checker, primary statements and relevant proofs, and the source receipt. I independently derived the smooth extension, both Sobolev bounds, the exact odd-lattice phase normalization, and the complete frequency assembly. This review accepts the stated \(O(1)\) result, not an \(o(1)\) estimate, a sign, an explicit sharp constant, or a strict global variance deficit.

## 1. Accepted theorem and the support clarification

The author proves under ordinary RH that the actual fixed-vector block
\[
Z_{D,K}=2\sum_{\substack{D<d\le2D\\d\ \mathrm{odd}}}
\sum_{\substack{K<k\le2K\\k\ \mathrm{odd}}}
\mu(d)\log k\sum_{h\ \mathrm{even}}
F(dk,h)[\Lambda(dk+h)-2]
\]
is \(O(1)\), uniformly when \(D/T\) and \(K/T\) range in fixed compact subsets of \((0,\infty)\), with \(X=T^2\), \(Y=T\) and the stated fixed smooth profiles. The product support remains in \(F\), all odd-endpoint prime powers are retained, and no coprimality condition between \(d\) and \(k\) is imposed.

The whole low Mellin interval \(|t|\le\pi K/2\) contributes \(O(1/\log X)\). The dyadic high-frequency contributions are \(O_j((R/T)^{1-j})\) for each fixed \(j\ge2\); their sum is finite and bounded. This is a statement about the complete central balanced block rather than a selected frequency band.

The initial version, SHA256 `99e25b2e25085077d47b575366e92e9609e83bd8db3584d2d744d9a99ff4c3f1`, wrote an unqualified integral of \(|S(x)|^2\) in its Schur estimate, although \(S\) was defined without the compact factor \(A\). The required integral is only over \(x\in[X,2X]\), where \(A\) and \(A'\) can contribute. Likewise the associated support bounds on \(k\) and \(r\) are used only on this relevant interval. I requested explicit localization of that displayed estimate. This is not a change to the theorem or the working argument: all subsequent quantities \(G,R\) already include \(A\) or \(A'\), and the author uses only that localized norm. The final source receipt records the clarified version, preserving the earlier version separately.

The stronger local bound does not improve the earlier global \(O(1)\) result by itself. The number, scales and signs of the other R26 blocks are separate questions. The manuscript correctly keeps those scopes apart.

## 2. Exact extension and Mellin normalization

Let
\[
A(x)=X\ell^2b_T(x)\chi(x/X),\qquad
k(x,u)=V((u-x)/Y)(x/u)^T,
\quad\ell=\log T.
\]
The extension
\[
f(x)=A(x)\sum_{n\ \mathrm{odd}}k(x,n)[\Lambda(n)-2]
\tag{R1}
\]
is a finite sum of smooth functions on the support of \(A\). It is compactly supported in \((X,2X)\). For sufficiently large \(T\), only integers \(X<n<3X\) appear. At an odd integer \(m\), substituting \(n=m+h\) identifies exactly the even shifts, with the same coefficient \(\Lambda(m+h)-2\). Thus (R1) interpolates the original arithmetic values without defining or differentiating a fictitious function \(\Lambda(x+h)\).

The Mellin transform is Fourier transform in \(v=\log x\):
\[
\widehat f(t)=\int_0^\infty f(x)x^{-it}\frac{dx}{x},
\qquad
f(x)=\frac1{2\pi}\int_{\mathbb R}\widehat f(t)x^{it}dt.
\]
Consequently both Dirichlet polynomials carry the same positive phase:
\[
M_D(t)=\sum_{d\in\mathcal D}\mu(d)d^{it},
\qquad B_K(t)=\sum_{k\in\mathcal K}(\log k)k^{it},
\]
and the exact target is
\[
Z_{D,K}=\frac1{\pi X\ell^2}
\int_{\mathbb R}\widehat f(t)M_D(t)B_K(t)dt.
\tag{R2}
\]
The original factor two combines with \(1/(2\pi)\); neither a conjugation nor an additional \(2\pi\) is inserted. For each fixed \(T\), the transform is Schwartz, while the finite polynomials are bounded in \(t\), so inversion and the finite-sum interchange are absolutely valid. Uniform estimates for the integral are then established separately, rather than inferred from nonuniform Schwartz decay.

The sharp factor endpoints are unchanged. The smooth extension incorporates the true product cutoff; it does not replace the arithmetic sum by an unrestricted rectangular product average.

## 3. Positive-derivative estimate: exact parity and legal Selberg range

From the actual defining integral for \(b_T\), substitution \(u=xz\) gives
\[
X\ell^2b_T(x)=\frac{XT}{x}
\int_{1/x}^1\omega((\log x+\log z)/\ell)z^{T-2}dz.
\]
Boundary contributions at \(u=1\) vanish because the fixed \(\omega\) is supported at positive logarithmic heights far above zero. The integral mass is at most \(1/(T-1)\). Differentiating at fixed \(T\) therefore shows
\[
(x\partial_x)^r A(x)=O_r(1)
\]
on the relevant support for every fixed order. No hidden power of \(T\) arises from this prefactor.

With \(h=n-x\) at a fixed integer \(n\), the derivative operator is precisely
\[
x(\partial_x-\partial_h).
\]
Its iteration must include differentiation of its own coefficient \(x\), as the author does. Applying this operator to the smooth kernel produces \(P_j\) with
\[
|P_j(x,h)|\ll_jT^j,
\qquad |\partial_hP_j(x,h)|\ll_jT^j/Y,
\quad Y<h<2Y.
\tag{R3}
\]
One way to see the scales directly is to hold \(n\) fixed in \((x/n)^T\): an \(x\partial_x\) derivative contributes a factor \(T\); derivatives of the shift profile contribute \(x/Y\asymp T\). In contrast, a further \(h\) derivative of these kernels costs \(Y^{-1}\), since \(T/(x+h)\asymp Y^{-1}\). All profile derivatives are fixed-order and uniformly bounded. No prime-counting derivative is used.

For real \(x,y\), the exact prefix is
\[
\mathcal A_x(y)=\sum_{x<n\le x+y,\ n\ \mathrm{odd}}[\Lambda(n)-2].
\]
With \(E(x)=\Psi(x)-x\), it satisfies
\[
\mathcal A_x(y)=E(x+y)-E(x)
+y-2N_{\mathrm{odd}}(x,x+y)
-(\log2)\#\{r:x<2^r\le x+y\},
\tag{R4}
\]
where
\[
N_{\mathrm{odd}}(x,x+y)
=\left\lfloor\frac{x+y+1}{2}\right\rfloor
-\left\lfloor\frac{x+1}{2}\right\rfloor.
\]
This formula handles endpoints equal to odd integers without a convention change. The lattice staircase has size at most two. Since \(x\asymp X=T^2\) and \(y\asymp Y=T\), the interval has multiplicative length less than two for all sufficiently large \(T\), so at most one power of two appears. Its weight is \(\log2\), not the logarithm of that power. The total correction in (R4) is therefore \(O(1)\).

Stieltjes partial summation has zero endpoint terms because the kernel is compactly supported strictly inside the shift interval. Using (R3) and Cauchy gives
\[
|(x\partial_x)^jf(x)|^2
\ll_j\frac{T^{2j}}Y\int_Y^{2Y}|\mathcal A_x(y)|^2dy.
\tag{R5}
\]

The CCCC primary input is specifically its fixed-\(\beta=3\) result
\[
J(3,S)=\int_1^{S^3}|E(x+x/S)-E(x)|^2\frac{dx}{x^2}
\ll\frac{\log^2S}{S}.
\tag{R6}
\]
To apply it, set \(\lambda=Ty/x\) in the double integral. On the rectangle \(X\le x\le2X\), \(Y\le y\le2Y\), the enclosing \(\lambda\) range is the fixed interval \([1/2,2]\) and \(dy=(x/T)d\lambda\). For each fixed \(\lambda\), take the single fixed parameter \(S=T/\lambda\); then \([X,2X]\subset[1,S^3]\) uniformly for all sufficiently large \(T\). The change of variables and the measure \(dx/x^2\) in (R6) give
\[
\int_X^{2X}\int_Y^{2Y}|E(x+y)-E(x)|^2dy\,dx
\ll\frac{X^3}{T}\int_{1/2}^2J(3,T/\lambda)d\lambda
\ll XY^2\log^2X.
\tag{R7}
\]
The \(O(1)\) corrections in (R4) add \(O(XY)\), which is smaller. The factor \(x^3\), rather than \(x^2\), accounts for the Jacobian in addition to the source weight. No integral theorem is applied at a parameter varying pointwise with \(x,y\).

Integrating (R5) against \(dx/x\) now yields
\[
\|(x\partial_x)^jf\|_{L^2(dx/x)}^2
\ll_jT^{2j}Y\log^2X.
\]
Fourier Plancherel in \(v=\log x\) and finite binomial expansion give the author's weighted estimate
\[
\int_{\mathbb R}(1+(t/T)^2)^j|\widehat f(t)|^2dt
\ll_jY\log^2X.
\tag{R8}
\]
The available input here has two logarithms. A bound with one logarithm is not silently assumed.

## 4. Negative derivative: exact decomposition and the Cramér input

The new primary input is Brent–Platt–Trudgian, printed page 741, equation (1). It states under RH
\[
\int_Z^{2Z}(\Psi(u)-u)^2du\ll Z^2.
\]
I checked the definition of \(\Psi\) in the preceding text and visually inspected the formula and Theorem 1 on that page. It concerns the full von Mangoldt function and ordinary RH. It is not a theta-only or GRH estimate. The theorem's sharper numerical constant is unnecessary. In particular, the manuscript correctly does not derive this mean-square statement by squaring the pointwise RH bound, which would lose logarithms.

Covering the needed interval by two dyadic intervals gives
\[
\int_X^{3X}|E(u)|^2du\ll X^2.
\tag{R9}
\]

For the exact kernel and \(x\in[X,2X]\), define
\[
S(x)=\int E(u)k(x,u)du,
\qquad r(x,u)=T(1/x-1/u).
\]
On this relevant support \(u-x\asymp Y\), \(u\in[X,3X]\), and
\[
\partial_xk+\partial_uk=r(x,u)k,
\qquad |r(x,u)|\ll X^{-1}.
\tag{R10}
\]
The first derivatives of \(V((u-x)/Y)\) cancel in their sum. The remaining factor is \(T/x-T/u\), of size \(TY/X^2=X^{-1}\). Both the cancellation and the scale are necessary.

Write the exact lattice and even-prime-power corrections as
\[
\mathcal L(x)=\int k(x,u)du-2\sum_{n\ \mathrm{odd}}k(x,n),
\quad
\mathcal P_2(x)=(\log2)\sum_{r\ge1}k(x,2^r).
\]
The full prime measure is \(d\Psi=du+dE\). Integration by parts in \(u\), using the smooth zero boundary values of \(k\), gives
\[
\int k\,dE=-\int E\,\partial_uk
=S'(x)-\int E(u)r(x,u)k(x,u)du.
\]
Therefore the actual odd-centered observable is exactly
\[
f(x)=A(x)\left[S'(x)-\int Erk+\mathcal L(x)-\mathcal P_2(x)\right].
\tag{R11}
\]
Both minus signs and the continuous-center correction have been independently checked. No derivative of \(E\) is taken.

Set \(x=e^v\) and \(G(v)=A(x)S(x)/x\). Direct differentiation gives
\[
G'(v)=A'(x)S(x)+A(x)S'(x)-A(x)S(x)/x.
\]
Thus
\[
f(e^v)=G'(v)+R(v),
\]
\[
R(v)=(A/x-A')S-A\int Erk+A(\mathcal L-\mathcal P_2).
\tag{R12}
\]
The sign of \(A/x-A'\) is correct. The fields \(G,R\) are compactly supported through \(A,A'\), even though \(S\) by itself need not be; this is the localization clarified in the author revision.

For completeness, the exact localized Schur calculation is
\[
\int_X^{2X}|S(x)|^2dx
\ll Y^2\int_X^{3X}|E(u)|^2du
\ll Y^2X^2.
\tag{R13}
\]
One proof first applies Cauchy on each \(u\)-section of length \(O(Y)\), then changes order and uses the \(x\)-section length \(O(Y)\). Dividing by the relevant powers of \(x\asymp X\), and using \(A=O(1)\), \(A'=O(X^{-1})\), yields
\[
\|AS/x\|_{L^2(dx/x)}^2
+\|(A/x-A')S\|_{L^2(dx/x)}^2
\ll Y^2/X=1.
\]
Replacing \(k\) by \(rk\), whose amplitude is \(O(X^{-1})\), gives the same bound for its term in (R12).

The lattice identity, with Fourier convention \(e^{-2\pi i\xi u}\), is
\[
2\sum_{n\ \mathrm{odd}}k(x,n)
=\sum_{\nu\in\mathbb Z}(-1)^\nu\widehat{k(x,\cdot)}(\nu/2).
\]
The factor two and the half-frequency lattice are correct. Thus \(\mathcal L\) is minus the nonzero-frequency sum. Since the kernel derivatives satisfy \(\|\partial_u^q k\|_1\ll_qY^{1-q}\), two derivatives give the uniform bound \(\mathcal L=O(Y^{-1})\) after the convergent \(\nu^{-2}\) sum. This term is harmless in \(L^2(dv)\).

There are only \(O(1)\) powers of two in the full relevant interval \((X,3X)\), and each contributes for an \(x\)-interval of length \(O(Y)\). Hence
\[
\|A\mathcal P_2\|_{L^2(dx/x)}^2\ll Y/X.
\]
This is an exact exceptional support calculation, not a replacement of \(\Lambda\) by a prime-only function. It follows that \(\|G\|_2+\|R\|_2=O(1)\).

Taking Fourier transforms of (R12) now proves
\[
\int_{\mathbb R}\frac{|\widehat f(t)|^2}{1+t^2}dt\ll1.
\tag{R14}
\]
Indeed \(\widehat f=it\widehat G+\widehat R\) and \(|t|/\sqrt{1+t^2}\le1\); Plancherel applies to the compactly supported fields. This bound is independent of (R8) and is the substantive reason the entire low interval can be handled without a logarithmic accumulation.

## 5. Primary Dirichlet mean value and sharp odd logarithmic sums

I visually checked Montgomery–Vaughan's *Hilbert's Inequality*, Corollary 3, printed page 75, equation (1.11). It gives
\[
\int_0^R\left|\sum_n a_nn^{-it}\right|^2dt
=\sum_n|a_n|^2(R+O(n)),
\]
with an absolute implied constant, whenever the required weighted sum is finite; here all polynomials are finite. Restriction to odd integers is implemented by zero coefficients. Translating the interval multiplies coefficients by unit phases, and reversing signs of the Fourier parameter leaves the bound unchanged. Thus
\[
\int_a^{a+R}|M_D(t)|^2dt\ll(R+D)D
\tag{R15}
\]
for every real \(a\), \(R>0\). This uses only the bounded coefficients and their diagonal sum, not a pointwise Möbius estimate.

For the logarithmic polynomial, writing \(k=2r+1\) gives exactly
\[
\phi_t'(r)=\frac{t}{\pi(2r+1)},
\qquad
\phi_t''(r)=-\frac{2t}{\pi(2r+1)^2}.
\tag{R16}
\]
For \(1\le|t|\le\pi K/2\), the magnitude of the first derivative lies between \(|t|/(2\pi K)\) and \(|t|/(\pi K)\le1/2\). Its distance from the nearest integer is therefore at least a constant times \(|t|/K\). The source Corollary 16.6 applies to the correctly oriented phase, uniformly on every consecutive subinterval. Partial summation of \(\log k\) retains the sharp endpoints and gives
\[
|B_K(t)|\ll K\log(2K)/|t|.
\]
The trivial bound handles \(|t|\le1\), proving the combined \(K\log(2K)/(1+|t|)\) statement. Negative \(t\) is handled by conjugation. There is no invalid zero-frequency first-derivative assertion.

For all nonzero \(t\), Theorem 16.7 with derivative parameter \(|t|/K^2\) and interval length \(O(K)\) gives the unweighted prefix bound \(O(\sqrt{|t|}+K/\sqrt{|t|})\). Amplitude partial summation yields
\[
|B_K(t)|\ll\log(2K)
\left(\sqrt{|t|}+\frac K{\sqrt{|t|}}\right).
\tag{R17}
\]
The source explicitly permits the negative second derivative. Even for \(|t|>K^2\) the estimate is valid, although it may be weaker than the trivial bound. It has no nonstationary hypothesis and therefore covers all larger-frequency aliases.

The continuous stationary phase condition on the odd lattice is \(t/k=\pi j\), not \(2\pi j\). The exact adjacent increment instead gives \(t=2\pi j/\log(1+2/k)\). These are distinct notions; the manuscript correctly records both and does not equate them. Neither produces a missing uncovered interval: the safe first-derivative range ends at \(\pi K/2\), and (R17) handles everything above it.

## 6. Complete frequency assembly and the remaining logarithm

Let \(R_0=\pi K/2\asymp T\). On the whole low interval, combine the bound on \(B_K\), (R14) and (R15) by Cauchy:
\[
\left|\int_{|t|\le R_0}\widehat f M_DB_Kdt\right|
\ll K\log X
\left(\int\frac{|\widehat f|^2}{1+t^2}dt\right)^{1/2}
\left(\int_{|t|\le R_0}|M_D|^2dt\right)^{1/2}
\ll T^2\log X.
\]
The elementary comparison \(\sqrt{1+t^2}\le1+|t|\) justifies the weight placement. Dividing by the exact factor \(\pi X\ell^2\) in (R2) gives \(O(1/\log X)\). This argument covers the entire low interval at once; no unnecessary count of low dyadic bands is inserted.

On \(R<|t|\le2R\) with \(R\ge R_0\), (R8), (R15) and (R17) give
\[
\|\widehat f\|_2\ll_j T^{j+1/2}(\log X)R^{-j},
\quad\|M_D\|_2\ll\sqrt{RT},
\quad\|B_K\|_\infty\ll\sqrt R\log X.
\]
The bound for \(M_D\) is valid on each signed interval separately; combining the two changes only an absolute constant. Since \(D,K\asymp T\) with fixed compact comparison constants, \(R+D\asymp R\) uniformly on this range.

The normalized product is exactly of scale
\[
\frac{T^{j+1/2}R^{-j}\sqrt{RT}\sqrt R\,(\log X)^2}
{T^2\ell^2}
\asymp (R/T)^{1-j}.
\tag{R18}
\]
The logarithms cancel because \(\log X=2\ell\). Taking \(j=2\) and \(R=2^rR_0\) gives a convergent geometric series over every high frequency. The same calculation gives an upper tail \(O_j(A^{1-j})\) beyond \(|t|>AT\), for sufficiently large fixed \(A\), without changing the assertion that the intermediate carrier range is merely bounded.

This proves the stated full-block \(O(1)\) bound. A hypothetical improvement of the derivative variance input from \(Y\log^2X\) to \(Y\log X\) would remove a square root of a logarithm in this calculation, but that is an additional local prime estimate. A variance averaged over logarithmic heights is not automatically such an input. The author explicitly avoids this substitution.

## 7. Verification, acceptance limits and source status

The independent review checks the hypotheses and consequences of the cited primary results; it does not claim to reprove those deep source theorems from scratch. The four source pages containing the Cramér normalization, Dirichlet mean value, first-derivative bound and second-derivative bound were inspected visually, as well as read from their retained extracts. The CCCC fixed-parameter theorem was checked against the primary definition and its previously verified range.

The copied tiny checker is run only in a temporary directory containing the final author Markdown and checker. Its seven groups and 147 exact cases cover derivative identities, real odd endpoints and powers of two, phase factors, Mellin signs, scale algebra and geometric tails. Its JSON and stdout are compared byte-for-byte with the final author outputs. Such finite algebra is useful for preventing sign and normalization mistakes; it is not a numerical test of the theorem's asymptotic constants. The receipt also verifies all 16 source/dependency pins and all six author artifact pins, and records the localization-only revision.

Accepted scope: the exact fixed arithmetic pairing for a complete balanced central block is bounded under RH; the low Mellin interval tends to zero with a logarithmic saving; all higher frequencies are retained and have a summable upper bound. The conclusion neither removes the carrier contribution nor gives a sign or a useful explicit constant. It does not address an increasing global collection of blocks or the other unbalanced and small-shift regimes. No strict AH deficit or famous conjecture has been proved by this checkpoint.
