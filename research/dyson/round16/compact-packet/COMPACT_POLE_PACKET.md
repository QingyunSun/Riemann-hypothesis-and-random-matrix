# A compact arithmetic packet with a nonnegative time weight

Date: 2026-09-05. Author: root Astra. Status: ordinary proof draft for independent review. This uses elementary Fourier differentiation and a contour shift for the actual zeta function. No novelty or new zeta-correlation result is claimed. Compared with the R15 Gaussian packet, its prime-side sum is exactly finite.

## 1. Objects and exact theorem

Assume RH and fix 1/2<sigma<1, a=1-sigma, W>=1 and X>exp(2). W is a time width, which may later equal the height parameter T. Define the entire function with its removable value at zero

\[
h_W(t)=\left(\frac{\sin(t/(2W))}{t/(2W)}\right)^4,\qquad
w_{a,W}(t)=\frac{t^2+a^2}{W^2}h_W(t).
\tag{1}
\]

The weight is nonnegative on the real line, integrable, and has simple zeros at t=±ia. The sinc factor does not vanish there.

Let B be the density of the sum of four independent uniforms on [-1/2,1/2]. Direct convolution gives the even cubic spline

\[
B(y)=\begin{cases}
\frac23-y^2+\frac12|y|^3,&|y|\le1,\\
\frac16(2-|y|)^3,&1\le|y|\le2,\\
0,&|y|\ge2.
\end{cases}
\tag{2}
\]

It is C² with integral one. Both B and B' vanish at the support endpoints. Put b=a/W and

\[
K_b(y)=-B''(y)+b^2B(y).
\tag{3}
\]

Under the Fourier convention integral w(t)exp(-it lambda)dt,

\[
\widehat w_{a,W}(\lambda)=2\pi W K_b(W\lambda),\qquad
\operatorname{supp}\widehat w\subset[-2/W,2/W],
\tag{4}
\]
\[
Z_{a,W}=\int w_{a,W}(t)dt
=2\pi W\left(2+\frac23b^2\right)>0.
\tag{5}
\]

Write H(s)=-zeta'(s)/zeta(s). The actual-zeta identity is

\[
\boxed{\int_{\mathbb R}H(\sigma+it)X^{it}w_{a,W}(t)dt
=2\pi W\sum_{Xe^{-2/W}<n<Xe^{2/W}}
\frac{\Lambda(n)}{n^\sigma}
K_b\!\left(W\log(n/X)\right).}
\tag{6}
\]

If an endpoint is an integer its coefficient is zero. Both endpoint conventions therefore agree. Every prime power is retained. This is not a formal critical-line Dirichlet series or a random prime model.

## 2. Fourier and contour proof

The characteristic function of a uniform on [-1/2,1/2] is sin(t/2)/(t/2). Fourfold convolution gives

\[
h_W(t)=\int_{-2}^2 B(y)e^{iyt/W}dy.
\]

The unscaled Fourier density is W B(W lambda). Multiplication by t² differentiates this density twice with a minus sign. Division by W² proves (4), including every W and 2pi factor. Equation (5) uses B(0)=2/3 and B''(0)=-2.

For (6), integrate H(s)X^(s-sigma)w(-i(s-sigma)) up Re(s)=sigma and shift to any fixed c>1. RH puts all nontrivial zeros to the left. The only possible pole in this strip is H's simple pole at s=1, with residue +1. Its residue is zero because w(-ia)=0; no continuous-density residue is dropped.

For fixed sigma, W and X, the standard RH logarithmic-derivative bound in a closed strip strictly to the right of 1/2 gives at most log² growth at large imaginary height. The weight and its bounded imaginary translates are O(W²/t²). The vertical integrals converge absolutely and the horizontal sides tend to zero. This argument proves the identity for each admitted parameter; it does not assert uniform contour constants as sigma decreases to 1/2.

On Re(s)=c expand H's absolutely convergent Dirichlet series. For d=c-sigma, a horizontal contour shift of the entire weight gives

\[
\int_{\mathbb R}w(t-id)e^{-it\lambda}dt
=e^{d\lambda}\widehat w(\lambda).
\]

Inverse-square decay controls the end segments. Multiplying by X^d n^(-c) then gives n^(-sigma) at lambda=log(n/X). The interchange is justified on the c-line before the Fourier support reduces the result to the finite sum (6).

Only one H factor is shifted. No reflected logarithmic derivative, squared H or zero-correlation asymptotic is introduced by this argument.

## 3. Exact finite centering, with endpoint terms accounted for

The corresponding continuous density is exactly zero:

\[
\int_0^\infty u^{-\sigma}\widehat w(\log(u/X))du
=2\pi X^a\int_{-2}^2e^{by}[-B''(y)+b^2B(y)]dy=0.
\tag{7}
\]

The last integrand is the derivative of e^(by)[-B'(y)+bB(y)]. Its endpoint values vanish and the internal values agree. Equation (7) is exact signed cancellation, not positivity.

Let E(u)=psi(u)-u and f(u)=u^(-sigma)hat w(log(u/X)). Then f is continuous, compactly supported on [Xe^(-2/W),Xe^(2/W)] and absolutely continuous, with piecewise continuous derivative. Jumps of its derivative at spline knots do not create atoms in df. The endpoint values of f vanish. Hence

\[
\mathcal P_{\sigma,W}(X)=\int f(u)dE(u)
=-\int_{Xe^{-2/W}}^{Xe^{2/W}}E(u)f'(u)du.
\tag{8}
\]

There is no infinite arithmetic tail or omitted endpoint. An additional truncation inside these support endpoints would require its own Ef boundary terms. All von Mangoldt prime powers remain.

## 4. Uniform pointwise RH bound

Equation (8) yields the deterministic inequality

\[
|\mathcal P_{\sigma,W}(X)|\le
2\pi X^{-\sigma}e^{2\sigma/W}
\sup_{u\in[Xe^{-2/W},Xe^{2/W}]}|E(u)|
[\sigma\|K_b\|_1+W\|K_b'\|_1].
\tag{9}
\]

Indeed f'(u)=2pi W u^(-sigma-1)[-sigma K_b(y)+W K_b'(y)], with y=W log(u/X), and du/u=dy/W. Direct piecewise integrals give

\[
\|B\|_1=1,\quad\|B'\|_1=4/3,\quad
\|B''\|_1=8/3,\quad\|B^{(3)}\|_1=8,
\]
\[
\|K_b\|_1\le8/3+b^2,\qquad
\|K_b'\|_1\le8+4b^2/3.
\tag{10}
\]

The third derivative is interpreted almost everywhere. The ordinary RH consequence E(u)=O(sqrt(u)log²(2u)) now proves

\[
\boxed{|\mathcal P_{\sigma,W}(X)|\ll
W X^{1/2-\sigma}\log^2X.}
\tag{11}
\]

This is uniform for 1/2<sigma<1, W>=1 and X>exp(2): in (9), 0<b<1/2, all exponential factors are bounded, and log(2u) is bounded by a constant times log X on the support. Enlarging the RH prime-error constant on a bounded u-range handles its lower endpoint. No explicit numerical RH constant is asserted. Uniformity comes from (9), not from uniformity of the contour proof.

The logarithmic loss is the same as the Gaussian route. Dividing by Z gives the normalized-packet form but does not create a new arithmetic saving, variance asymptotic or AH contradiction.

## 5. A nonvanishing sign cost

For 1<=|y|<=2 put z=2-|y|. Then

\[
K_b(y)=-z+\frac{b^2}{6}z^3<0\quad(0<z\le1).
\]

The two outer intervals alone have negative mass

\[
\int_{1\le|y|\le2}[-K_b(y)]dy
=1-\frac{b^2}{12}\ge\frac{47}{48}
\quad(0\le b\le1/2).
\tag{12}
\]

For the normalized real time weight w/Z, the Fourier transform in scaled frequency y is K_b(y)/(2+2b²/3). Its negative mass in dy is therefore at least 47/104 throughout this range. As b tends to zero, the full positive and negative masses of K_b both tend to 4/3, so the normalized negative mass tends to 2/3. Use -B''=2-3|y| on |y|<=1 and -B''=|y|-2 on the outer interval to check these exact values.

These are masses in y. Changing to lambda divides them by W; it must not be mistaken for a sign cost vanishing relative to the natural bandwidth. Nonnegative time weight still gives a positive semidefinite full Gram operator despite negative Fourier entries. Equation (12) does not deny that positivity.

## 6. Practical research role and unproved transfers

At W=T, X=T^alpha, the finite prime interval has width X(e^(2/T)-e^(-2/T)), asymptotic to 4X/T. A finite instance can be evaluated with an interval sieve and complete prime-power enumeration, without truncating a Gaussian arithmetic tail. This is a computation surface, not an observed benchmark or proof of a new asymptotic saving.

The original W_T target uses a different time weight and a quadratic logarithmic derivative. Equation (6) is a new linear pairing. A valid transfer requires a separately proved weighted second-moment identity and all cross terms. Simple packet zeros do not cancel double poles of H² or derivatives of H. If sigma depends on a differentiation parameter, a and the weight do too; a weighted-energy derivative then contains the derivative-of-weight term. None of those obligations is discharged here.

This compact formula offers an exactly finite signed arithmetic object for further testing. It does not prove Montgomery–Dyson/GUE, RH, AH refutation, or a new prime/zeta gap. The next question is whether the retained prime structure permits a stronger estimate than (11), or a properly derived weighted covariance bound.
