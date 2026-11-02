# Direct Selberg control of the centered mixed remainder: the precision and sign gap

Date: 2026-09-05. This is a bounded analytical test of the actual genuine-prime remainder. It gives an explicit, insufficient one-sided bound using a primary RH short-interval theorem. It does not introduce a substitute point process, differentiate an unknown error, or separate divergent prime and continuum tails. No parameter scan was run.

**Outcome.** The direct Selberg–Gallagher route below gives
\[
|M_T(b)|\ll\frac{\log T}{b^2}.
\tag{1}
\]
Consequently its lower bound on \(\int_b^{2b}\mathcal B_T(s)\,ds\) is only of order \(-\log T/b\), whereas the target is \(-3/(2b^2)+\varepsilon/b^2\). This is a quantified failure of this particular arithmetic estimate, not an impossibility theorem and not a claim to improve the previously known individual-norm bounds.

**This is not the strongest known RH norm estimate.** Round 10 already established the stronger \(E_T(b)=O(1)\) on the slow range. The same primary page also records Selberg's stronger global weighted estimate, discussed in Section 4 below. Neither is to be replaced by the weaker local-bound calculation (1). The remaining issue is a one-sided fluctuation estimate in a shrinking logarithmic shell, with its leading coefficient and next-order precision.

## 1. Primary input is already about genuine primes

Let \(\theta(x)=\sum_{p\leq x}\log p\). Saffari and Vaughan, [On the fractional parts of x/n and related sequences II](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf), Ann. Inst. Fourier 27(2) (1977), define this prime-weighted function in (6.1). Under RH, their Lemma 5, equation (6.4), gives
\[
\int_X^{2X}|\theta(x+\eta x)-\theta(x)-\eta x|^2\,dx
\ll \eta X^2\log^2(2/\eta),
\quad X\geq4,\quad0<\eta\leq1.
\tag{2}
\]
The uniformity in \(\eta\), and the fact that the statement concerns \(\theta\), were checked in the primary text on printed pages 19–22. No GRH or pair-correlation conjecture is assumed. Formula (2) is an upper bound, with an unspecified absolute constant; it is not a variance asymptotic or a positive lower bound.

## 2. Gallagher's inequality applied to the combined centered measure

Retain \(L=\log T\), \(N=\lfloor T/L^6\rfloor\), and the Round 11 finite centered tails
\[
C_{s,Y}(t)=\int_{(N,Y]}x^{-1/2-s/(2L)-it}\,d(\theta(x)-x),
\]
\[
D_{s,Y}(t)=\int_{(N,Y]}
\left(\frac{\log x}{L}-1\right)x^{-1/2-s/(2L)-it}\,d(\theta(x)-x).
\tag{3}
\]
Both the prime and continuous terms occur inside the same finite signed measure. Let \(\tau=1/T\). For any finite measure \(\nu\) on logarithmic coordinates, Plancherel applied to its convolution with an interval of length \(\tau\) gives
\[
\int_{-T}^T|\widehat\nu(t)|^2dt
\leq\frac{2\pi T^2}{c_0^2}
\int_{\mathbb R}|\nu((v,v+\tau])|^2dv,
\quad c_0=\frac{\sin(1/2)}{1/2}.
\tag{4}
\]
Here the transform uses \(e^{-itv}\). The Fourier transform of the interval has modulus at least \(c_0/T\) for \(|t|\leq T\), which proves (4), including its direction. This remains valid for the finite prime atoms plus continuous density in (3).

For a logarithmic interval starting at \(x=e^v\), the right side contains
\(\int_x^{xe^\tau}g(u)\,d(\theta(u)-u)\). Put \(F=\theta-\mathrm{id}\). Integration by parts on this short interval expresses it as
\[
g(xe^\tau)[F(xe^\tau)-F(x)]
-\int_0^{e^\tau-1}xg'(x(1+\eta))
[F(x(1+\eta))-F(x)]\,d\eta.
\tag{5}
\]
For \(x\in[X,2X]\), apply (2) to each increment in (5), then Minkowski. The integral in \(\eta\) is bounded by a constant times the endpoint contribution since
\(\int_0^\tau\sqrt\eta\log(2/\eta)d\eta\ll\tau^{3/2}\log(2/\tau)\).
For \(\sigma=1/2+s/(2L)\in[1/2,3/4]\), this gives
\[
\int_X^{2X}\left|\int_x^{xe^\tau}g(u)\,dF(u)\right|^2\frac{dx}{x}
\ll X^{1-2\sigma}\tau L^2 w_X^2,
\tag{6}
\]
where \(w_X=1\) for \(g(u)=u^{-\sigma}\), and
\(w_X=|\log X/L-1|+O(1/L)\) for
\(g(u)=(\log u/L-1)u^{-\sigma}\). All constants are uniform in the stated range. The extra \(1/L\) controls the variation across a dyadic interval and the derivative of the logarithmic weight.

## 3. Cutoffs and dyadic summation

For the upper cutoff \(Y\), the crossing windows have total logarithmic length \(O(1/T)\). The RH pointwise bound on \(F\), together with weighted partial summation, bounds their contribution after (4) by
\[
O\left(TY^{-s/L}\log^4Y
\left(1+\left|\frac{\log Y}{L}-1\right|\right)^2\right).
\]
It tends to zero for fixed \(T,s>0\) as \(Y\to\infty\). The order of limits is explicit. The uniform analytic cutoff from Round 11 could also be used; no practical finite-prime experiment is asserted.

At the lower cutoff, \(N\) is an integer and the prime tail is strict. For large \(T\),
\(Ne^{1/T}<N+1\). Thus a crossing window from below \(N\) contains no retained prime atom and only the continuous density on its very short intersection with \((N,\infty)\). Its contribution is negligible. The endpoint term implicit in the limiting analytic continuation has not been discarded: (3) converges to precisely the centered tail defined in Round 11.

Partition the starting points \(x\geq N\) into \([2^jN,2^{j+1}N]\). This partitions the integration variable in (4), not the prime measure, so it creates no extra prime-cutoff boundary at the dyadic endpoints. Let
\(d_N=1-\log N/L=6\log L/L+o(1/L)\).
For \(2\leq s\leq2G(T)\), where \(G=o(\log L)\), geometric summation gives
\[
\sum_{j\geq0}(2^jN)^{-s/L}\ll e^{-s}\frac Ls,
\]
\[
\sum_{j\geq0}(2^jN)^{-s/L}
\left(\left|-d_N+\frac{j\log2}{L}\right|+\frac1L\right)^2
\ll e^{-s}\frac L{s^3}.
\tag{7}
\]
For the second estimate, use the exact geometric-series sums for \(1,j,j^2\), together with \(sd_N=o(1)\). Equations (4), (6), and (7) therefore prove for the limiting centered tails
\[
\frac{e^s\|C_s\|_2^2}{TL^2}\ll\frac Ls,
\qquad
\frac{e^s\|D_s\|_2^2}{TL^2}\ll\frac L{s^3}.
\tag{8}
\]
These norms are over \([0,T]\), a subinterval of that bounded by (4).

Cauchy–Schwarz in the actual mixed product now gives
\[
\left|\frac{e^s}{TL^2}\Re\langle C_s,D_s\rangle\right|
\ll\frac L{s^2}.
\]
The already quantified pole replacement is \(O(e^sL^{-3})\), uniformly negligible here; adding it proves (1) for \(M_T\) itself. No prime-power replacement is necessary because (2) was genuine-prime input from the start.

## 4. The concrete integrated lower bound is too weak

Write \(\mathcal B_T(s)\) for the single jointly centered remainder of Round 11, including all off-diagonal prime-prime, prime-continuum, and continuum-continuum terms before taking the cutoff limit. Its proved diagonal decomposition implies
\[
\int_b^{2b}\mathcal B_T(s)\,ds
\geq-C\frac Lb-\frac1{2b}-\frac3{4b^2}+o(b^{-2}).
\tag{9}
\]
This follows from the actual mixed-product bound above and the exact integrated prime diagonal. It is a valid one-sided consequence, but its negative error is larger than the required \(b^{-2}\) accuracy by a factor of order \(Lb\).

For any fixed nonnegative smooth \(\chi\) supported in \((1,2)\), the same proof gives
\[
\left|\int_b^{2b}\chi(s/b)M_T(s)\,ds\right|
\ll_\chi\frac Lb.
\]
Thus smoothing in \(b\) alone does not improve this estimate. The loss of \(L\) is visible in (2): the theorem supplies \(\log^2(2/\eta)\), while the fluctuation scale at \(\eta\asymp1/T\) has only one logarithm. Even hypothetically replacing the squared logarithm by a single logarithm in this argument would yield only \(|M_T(s)|\ll s^{-2}\), with no positive leading coefficient or the required next-order deficit below 2. This diagnoses the sign loss of the Cauchy–Schwarz step, not a logical impossibility of stronger consequences from a strengthened theorem.

There is a material stronger-input nuance. On the same primary page, equation (6.5) recalls Selberg's global estimate
\[
\int_0^{\eta^{-A}}
|\theta(x+\eta x)-\theta(x)-\eta x|^2\frac{dx}{x^2}
\ll_A\eta\log^2(2/\eta),
\tag{9a}
\]
for a fixed admissible exponent \(A>1\), corresponding to the fixed exponent parameter in the source remark. It is not legitimate to let that exponent grow with \(T\). For any such fixed \(A\), the active edge shell \(1/s\leq\log x/L-1\leq2/s\) lies within this range when \(s\) and then \(T\) are large enough. Using a fixed smooth filter of \(s(\log x/L-1)\), the argument (4)–(5) with (9a) gives normalized squared norms \(O_A(1)\) and \(O_A(s^{-2})\) for the filtered centered tail and its log-weighted companion. Indeed the Mellin damping on that shell is \(O(e^{-s})\); the excess weight is \(O(1/s)\), and its differentiation costs only \(O(1/L)\). These are bounds for a filtered component, not a new identity for the full mixed moment.

Cauchy–Schwarz then controls that component only by \(O_A(1/s)\), and does not give a positive leading \(1/s^2\). The global estimate supplies a bound on accumulated positive variance, not a quantitative lower increment on the shrinking shell and not the required signed mixed covariance. This is why merely selecting the stronger stated Selberg bound does not complete the proposed argument. The explicit lower bound (9) is retained as a fully quantified local-theorem consequence, not as a claim of optimal RH control.

## 5. Smoothing does not make the actual kernel termwise positive

At finite cutoff, Fubini in (3) shows that the sharp \(s\)-integrated mixed product has the real kernel
\[
\frac{(xy)^{-1/2}}{L^2}
\bigl(e^{-b v(x,y)}-e^{-2b v(x,y)}\bigr)
\operatorname{sinc}_0(T\log(x/y)),
\quad
v(x,y)=\frac{\log x+\log y}{2L}-1.
\tag{10}
\]
It acts on the same finite signed measure
\(d\theta-dx\) in both variables. Smooth nonnegative \(s\)-weights replace the exponential difference by the corresponding integral of \(v e^{-sv}\); they leave the sinc factor and centering intact.

For example, \(x,y>T\) and \(T\log(x/y)=3\pi/2\) give a positive exponential factor but sinc equal to \(-2/(3\pi)\). These are points in the domain of the actual continuum terms, not a fabricated point process. This rules out simply declaring every off-diagonal kernel contribution nonnegative after \(b\)-smoothing. A negative kernel value alone is not a proof that its quadratic form lacks positivity; no such general claim is made here. The relevant arithmetic lower estimate is still missing.

The bounded attempt therefore stops with the genuine-prime inequality (9) and an explicit precision/sign deficit. Repeating identities or replacing the centered covariance by separate divergent sums cannot fill that deficit. A new one-sided fluctuation estimate, or cancellation in the centered mixed pairing beyond these upper norms, is required.
