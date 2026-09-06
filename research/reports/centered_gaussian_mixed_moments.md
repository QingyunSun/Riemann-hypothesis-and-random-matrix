# Centered Gaussian packets: an exact mixed identity and an unavoidable pole debt

Research round 2, 2026-09-05. This note settles the proposed shortcut of replacing Inoue's shifted Gaussian packet by a Gaussian centered at zero and then using Fourier positivity to retain long mixed products for free. The Fourier kernel is positive, but the exact critical-line identity contains a pole-cut correction with the opposite phase on the relevant long-support region. That correction can exceed the purported normalization by an unbounded factor for coefficients bounded by one.

**Main conclusion.** A centered packet may be used only if its pole term, its true nondiagonal Gram form, and its low-height zero-count terms are retained. Dropping those terms is false. This is a precise obstruction to the proposed free support enlargement, not an impossibility theorem for every centered-packet method.

## 1. Conventions and source input

Let

$$
\Phi_W(t)=e^{-t^2/(2W^2)},\qquad
\widehat V(\xi)=\int_{\mathbb R}V(t)e^{-2\pi i t\xi}\,dt,
\qquad W>0.
$$

Thus $\widehat\Phi_W(\xi)=\sqrt{2\pi}W e^{-2\pi^2W^2\xi^2}>0$. The height parameter $T$ and packet width $W$ are distinct. Below $h=\pi/\log T$, while $W$ can be $T$ or $T/\log T$. A weight written as $e^{-t^2/T^2}$ corresponds to $W=T/\sqrt2$.

Use the horizontal branch

$$
\log\zeta(\sigma+it)=\int_\infty^\sigma\frac{\zeta'}{\zeta}(\alpha+it)\,d\alpha
$$

away from zero ordinates and $t=0$, with the mean of the two boundary values at exceptional ordinates. Put

$$
\Delta_h(t)=\log\zeta\left(\tfrac12+i(t+h/2)\right)
-\log\zeta\left(\tfrac12+i(t-h/2)\right),
$$

$$
g_h(k)=\frac{\Lambda(k)}{\log k}
\left(k^{-ih/2}-k^{ih/2}\right).
$$

For $k=p^e$, $g_h(k)=-2i\sin((h/2)\log k)/e$; otherwise it vanishes.

The analytic input is [Inoue, Lemma 5.5 and equations (5.42)–(5.43)](https://arxiv.org/html/2604.05733v1). For an analytic test function on the strip $-3/2\le\operatorname{Im}z\le0$ with the stated horizontal decay, its critical-line logarithm integral equals the Dirichlet contribution, zero-cut integrals, and a **negative pole-cut integral**. Under RH the zero-cut integrals to the right of the critical line disappear. We retain the pole term exactly, rather than invoking the small-error estimate used for the shifted packet.

The tests $V(z)=x^{-iz}\Phi_W(z)$ satisfy the strip and decay assumptions for every fixed $x>0$, $W>0$. Arbitrarily long but finite Dirichlet polynomials may consequently be expanded against this identity. No absolutely convergent Dirichlet series for $\log\zeta$ on the critical line is assumed.

## 2. Exact kernel identity

**Theorem 1.** Assume RH. For every $x>0$, $h>0$, and $W>0$,

$$
\begin{aligned}
K_{h,W}(x)
&:=\int_{\mathbb R}\Delta_h(t)x^{-it}\Phi_W(t)\,dt\\
&=\sqrt{2\pi}W\sum_{k\ge2}\frac{g_h(k)}{\sqrt k}
\exp\left[-\frac{W^2}{2}\log^2(kx)\right]
+\mathcal P_{h,W}(x),
\end{aligned}
\tag{1}
$$

where

$$
\begin{aligned}
\mathcal P_{h,W}(x)
&=-2\pi\int_0^{1/2}
\left[V(-h/2-i\sigma)-V(h/2-i\sigma)\right]d\sigma\\
&=\boxed{-4\pi i\,e^{-h^2/(8W^2)}
\int_0^{1/2}x^{-\sigma}e^{\sigma^2/(2W^2)}
\sin\left[\frac h2\left(\log x-\frac{\sigma}{W^2}\right)\right]d\sigma.}
\end{aligned}
\tag{2}
$$

The series in (1) is absolutely convergent: the Gaussian decay in $\log k$ dominates the $k^{-1/2}$ factor and the number of integers at each logarithmic scale.

**Proof.** Apply the cited contour identity at shifts $v=h/2$ and $v=-h/2$ and subtract. RH removes zero cuts with real part greater than $1/2$. The pole at $s=1$ leaves the first line of (2). The Fourier transform of $x^{-it}\Phi_W(t)$ at $\log k/(2\pi)$ is precisely the Gaussian in (1). Finally,

$$
V(-h/2-i\sigma)
=x^{-\sigma}e^{\sigma^2/(2W^2)-h^2/(8W^2)}
 e^{i(h/2)(\log x-\sigma/W^2)},
$$

and $V(h/2-i\sigma)$ has the conjugate phase. Their difference proves (2). This derivation uses an identity obtained by shifting to an absolutely convergent half-plane; it does not formally expand the critical-line logarithm.

### 2.1 The sign on the genuine long-support region

If

$$
0<x\le1,\qquad
0<h\left(\log(1/x)+\frac1{2W^2}\right)<2\pi,
\tag{3}
$$

then $\mathcal P_{h,W}(x)$ is purely imaginary with **strictly positive imaginary part**. At $x=1$ the integral is still positive because the phase is strictly negative for $\sigma>0$.

In contrast, $g_h(k)$ is negative imaginary whenever $0<h\log k<2\pi$. Hence at the matching frequency $x=1/k$, the pole correction has the opposite phase to the positive-kernel Dirichlet contribution.

The sign statement is deliberately restricted to (3). It is false for all positive $x$: for example $x=2,h=0.2,W=3$ gives a negative imaginary correction. This is not a defect of the theorem; it is why support information matters.

## 3. Exact mixed and Gram forms for arbitrary finite supports

Let

$$
R(t)=\sum_m\frac{r_m}{\sqrt m}m^{-it},\qquad
C(t)=\sum_q\frac{c_q}{\sqrt q}q^{-it}
$$

be arbitrary finite Dirichlet polynomials. Then (1) gives the exact identity

$$
\begin{aligned}
\langle C,\Delta_h R\rangle_{\Phi_W}
={}&\sqrt{2\pi}W\sum_{k,m,q}
\frac{g_h(k)r_m\overline{c_q}}{\sqrt{kmq}}
 e^{-\frac12W^2\log^2(km/q)}\\
&+\sum_{m,q}\frac{r_m\overline{c_q}}{\sqrt{mq}}
\mathcal P_{h,W}(m/q).
\end{aligned}
\tag{4}
$$

Here $\langle C,X\rangle_{\Phi_W}=\int X(t)\overline{C(t)}\Phi_W(t)dt$; the notation specifies the order to prevent an unnoticed conjugation change.

The penalty is also exactly

$$
\|C\|_{\Phi_W}^2
=\sqrt{2\pi}W\sum_{q,r}
\frac{c_q\overline{c_r}}{\sqrt{qr}}
 e^{-\frac12W^2\log^2(q/r)}.
\tag{5}
$$

For long dense support, (5) is not the diagonal coefficient norm. Its off-diagonal terms are positive when all $c_q$ share one phase. Fourier positivity therefore enlarges the penalty as well as the suggested mixed gain.

Suppose $r_m\ge0$, $c_q=-i d_q$ with $d_q\ge0$, and every retained $q$ exceeds every retained $m$. If (3) holds for all $x=m/q$, **every pole summand in the second line of (4) is negative real**. This is the natural configuration when a new residual direction lives in a genuinely longer tail than the existing resonator. The positive Fourier kernel does not remove its debt.

For $q\le T^{1+\eta}$ with fixed $0<\eta<1$ and $h=\pi/\log T$, the effective prime-power range in (4) has the common phase. Terms beyond the first sine sign change are Gaussian-small because $\log(km/q)$ is then bounded below by a positive multiple of $\log T$. They can be bounded absolutely. The pole term remains and is the substantive obstruction.

## 4. A counterexample to treating the pole term as a negligible uniform error

The following example uses coefficients bounded by one and no conjecture about primes in short intervals.

**Theorem 2.** Fix $0<\eta<1$. Let $M=T^{1+\eta}$, $h=\pi/\log T$, and let $W=T$ or $W=T/\log T$. Take

$$
R(t)=1,\qquad
C(t)=-i\sum_{M<q\le2M}\frac1{\sqrt q}q^{-it}.
$$

The pole contribution to (4) is negative and satisfies

$$
\boxed{
\mathcal E_{pole}
=-\left(4\pi\cos\frac{\pi\eta}{2}+o(1)\right)
\frac{M}{\log M}.
}
\tag{6}
$$

In particular,

$$
\frac{|\mathcal E_{pole}|}{\sqrt{2\pi}W}\longrightarrow\infty,
\tag{7}
$$

even though $\sum|r_m|^2/m=1$ and $\sum|c_q|^2/q\to\log2$.

**Proof.** Uniformly for $q\in(M,2M]$, formula (2) and $W\to\infty$ give

$$
\mathcal P_{h,W}(1/q)
=4\pi i\sin\left(\frac h2\log q\right)
\frac{\sqrt q-1}{\log q}\,(1+o(1)).
\tag{8}
$$

The sine is bounded away from zero in this range, since it tends to $\cos(\pi\eta/2)>0$. The factors $e^{\sigma^2/(2W^2)}$, $e^{-h^2/(8W^2)}$, and the additional sine argument $h\sigma/(2W^2)$ change the integral by a uniformly vanishing relative error. The remaining elementary integral is

$$
\int_0^{1/2}q^\sigma d\sigma=\frac{\sqrt q-1}{\log q}.
$$

Multiply (8) by $\overline{c_q}/\sqrt q=i/\sqrt q$ and sum. The sum of $(1-q^{-1/2})/\log q$ over all integers in $(M,2M]$ is $(1+o(1))M/\log M$. This proves (6). Finally $M/(W\log M)$ tends to infinity for both specified widths.

The theorem refutes a uniform long-support identity of the form “positive Dirichlet Gaussian sum plus an $o(W)$ error controlled by the diagonal norms.” It does not assert that the full mixed moment itself is negative. The prime contribution and pole contribution may substantially cancel, and the surviving fluctuation is exactly what needs arithmetic control.

### 4.1 Why the apparent gain resembles a prime-density term

For a single frequency $x=1/X$, the Gaussian Dirichlet sum samples prime powers near $X$ on multiplicative width $1/W$. If one replaces the prime density heuristically by $dy/\log y$, its leading imaginary contribution is

$$
-4\pi i\sin\left(\frac h2\log X\right)\frac{\sqrt X}{\log X}.
$$

This has the same magnitude and opposite sign as (8). The replacement is an interpretation, **not** a proved short-interval prime estimate in the relevant ranges. It explains the structural cancellation: centering transforms the proposed free positive contribution into a prime-density-subtracted quantity. Proving useful positivity of that remainder still requires arithmetic information.

## 5. The origin and the zero-count formula cannot be discarded

Let $N(t)$ be the signed zero-counting function and let $\theta(t)$ be the odd Riemann–Siegel theta function. With the branch above, the exact global form away from endpoints is

$$
N(t)=\frac{\theta(t)}\pi+S(t)+\operatorname{sgn}(t),
\qquad
S(t)=\frac1\pi\operatorname{Im}\log\zeta(\tfrac12+it).
$$

Consequently,

$$
N_h(t)=\frac{\theta(t+h/2)-\theta(t-h/2)}\pi
+S(t+h/2)-S(t-h/2)
+2\mathbf1_{\{|t|<h/2\}}.
\tag{9}
$$

The indicator is absent only when the interval avoids the origin. As $t\downarrow0$, this branch has $S(t)\to-1$; as $t\uparrow0$, it has $S(t)\to1$. At $t=0$ the jump in $S$ and the indicator in (9) cancel. There are no zeros in a sufficiently small neighborhood of zero because $\zeta(1/2)\ne0$.

A packet concentrated near heights comparable to $T$ may replace the theta increment by $(h/2\pi)\log T+O(h)$ and suppress the origin. A centered packet requires a weighted argument proving that low heights are negligible. Pointwise replacement by $\log T$ on the entire real line is false.

### 5.1 A direct coherence bound for a positive long resonator

Let

$$
R_M(t)=\sum_{M<n\le2M}n^{-1/2-it}.
$$

Factor out $M^{-it}$. For $|t|\le1$, all remaining phases have arguments in an interval of length at most $\log2<\pi/2$. Therefore

$$
|R_M(t)|\ge\cos(\log2)\sum_{M<n\le2M}n^{-1/2}\ge c\sqrt M.
$$

For $W\ge1$,

$$
\int_{-1}^{1}|R_M(t)|^2\Phi_W(t)dt\ge c'M.
\tag{10}
$$

The diagonal coefficient norm is only $\sum_{M<n\le2M}1/n\sim\log2$, whose naive Gaussian normalization would have size $W$. If $M/W\to\infty$, the low-height coherent mass is much larger. This elementary example shows why Fourier-positive off-diagonal mass is not automatically useful high-zero information.

For a general nonnegative-coefficient resonator, even the shorter interval $|t|\le c/\log L$ gives a lower bound proportional to $|R(1/2)|^2/\log L$. Such mass must be controlled rather than discarded using an unweighted measure estimate.

### 5.2 A general positivity obstruction to cutting a hole at the origin

Suppose $\Phi$ is a real Schwartz function with $\widehat\Phi\ge0$ and is not identically zero. Fourier inversion gives

$$
\Phi(0)=\int\widehat\Phi(\xi)d\xi>0,
\qquad
|\Phi(t)|\le\Phi(0).
$$

Thus one cannot have both an everywhere nonnegative Fourier transform and a weight that vanishes at the origin, unless the weight is zero. Multiplying the Gaussian by a cutoff that removes the origin necessarily loses the claimed Fourier-positivity property. Translating a packet introduces the familiar phase $e^{-2\pi i t_0\xi}$; imposing phases on resonator coefficients likewise gives up the common coefficient phase used for the free-sign argument.

This lemma does not rule out a subtler weight whose origin contribution is paid quantitatively. It rules out the exact combination “remove the origin while preserving all Fourier signs for free.”

## 6. Verification and scope

`centered_gaussian_pole_checks.py` evaluates the finite pole integral in two independent forms at 80 decimal digits: direct complex evaluations of $V(-h/2-i\sigma)-V(h/2-i\sigma)$, and the sine integral in (2). The checks do not evaluate a critical-line Dirichlet series.

Representative output:

| $x,h,W$ | Pole correction | Mixed correction when $\overline c=i$ |
|---|---|---|
| $0.1,0.2,3$ | $+2.746104573214653\ldots i$ | $-2.746104573214653\ldots$ |
| $0.001,0.1,10$ | $+18.88430170566545\ldots i$ | $-18.88430170566545\ldots$ |
| $1,0.3,2$ | $+0.05966510707903\ldots i$ | negative |
| $2,0.2,3$ | $-0.35517163933647\ldots i$ | positive |

For $\eta=1/4$, the ratio of the exact pole integral at $x=T^{-5/4}$ to (8) is approximately $0.9999196069$, $1.0000000386$, and $1.0000000000000029$ at $T=100,10^4,10^8$. The two formulas agree to at least 70 decimal places in the tested cases. The script also checks the cancellation in (9) at the origin using the local branch and the theta function. These are high-precision diagnostics; the proof of the sign and the asymptotic counterexample is analytic and does not depend on their decimal output.

Completed claims in this note are the exact identity with its retained pole term, its sign on the specified support region, the dense-tail counterexample to a negligible-pole estimate, and the elementary coherence/Fourier-positivity obstructions. A full centered-packet formula for the squared logarithm and a successful positive residual certificate are not claimed.

The next admissible research move is to seek genuine control of the **density-subtracted long mixed moment**, or to design a packet/resonator whose pole and low-height contributions can be quantitatively paid. Replacing the shifted Gaussian by a centered one alone supplies neither.

### Completion or pole regularization does not restore the missing sign

One can instead use $\log((s-1)\zeta(s))$, which removes the pole in the half-plane to the right of the critical line under RH. This changes the observable. Its absolutely convergent-side expression contains the additional term $\log(s-1)$, whose transformed contribution compensates for the removed pole cut. Likewise the completed xi-function introduces explicit gamma and polynomial factors. These are legitimate formulations, but their arithmetic kernel is no longer the uncorrected nonnegative prime sum. A proposed completed-function approach must keep that explicit continuous/archimedean contribution in its Gram certificate; regularization is not a license to erase the density subtraction identified above.
