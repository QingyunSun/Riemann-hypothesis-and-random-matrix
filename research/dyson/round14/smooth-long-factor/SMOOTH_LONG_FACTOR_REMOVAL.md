# A smooth long factor removes an actual Type I component

Date: 2026-09-05. Status: unconditional ordinary proof; a classical Poisson application, newly verified for this programme's exact kernel. No novelty claim is made for the method. No estimate for the remaining component or the whole zeta covariance is proved.

Define the exact truncated divisor convolution
\[
\Lambda_{\le U}(n)=\sum_{\substack{r\mid n\\r\le U}}\mu(r)\log(n/r).
\tag{1}
\]
For the actual smooth discrepancy of Rounds 9–13, with \(Q=X^{523/1000}\), \(H=X/T\), and \(X^{1/6}\le H\le X^{2/7}\), this note proves
\[
\boxed{
|\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le U}]|
\ll_{J,V,\chi}HX\left(\frac{UQ}{X}\right)^J(\log X)^2
\quad(J\ge2,\ UQ\le X/2).
}
\tag{2}
\]
Both primitive restrictions, the modulus coefficients and the entire original covariance kernel are retained. Neither RH nor dense divisibility is needed for this component.

In particular \(U=X^{2/5}\), \(J=4\) give
\[
|\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le X^{2/5}}]|
\ll X^{1711/1750}(\log X)^2=o(X\log X).
\tag{3}
\]
The exponent margin below \(X\) is \(39/1750\). The remaining divisor portion has signs; the truncation is an exact decomposition, not an inequality for the full discrepancy.

## 1. The exact arithmetic object

Use the frozen weights
\[
a_y(X)=\min\{(y/X)^{1/2},(X/y)^{3/2}\},
\]
\[
w_h(u)=\chi(u/X)a_u(X)a_{u+h}(X)
\operatorname{sinc}_0\!\left(T\log(1+h/u)\right),
\tag{4}
\]
where \(\operatorname{sinc}_0(t)=\sin(t)/t\), with its removable value at zero,
\(V\in C_c^\infty(1,2)\), \(\chi\in C_c^\infty(1,3/2)\),
\(X=T^\alpha\), \(6/5\le\alpha\le7/5\), and \(H=X/T\).
For any coefficient sequence \(b\), define
\[
\begin{split}
\mathcal D_{\mathcal Q}^{V}[b]
=\sum_h V(h/H)
\sum_{\substack{q\in\mathcal Q_X\\(h,q)=1}}\mu(q)
\bigg[
&\sum_{n\equiv h\ (q)}
b(n)w_h(n-h)\log((n-h)/q)\\
&-\frac1{\varphi(q)}
\sum_{(n,q)=1}b(n)w_h(n-h)\log((n-h)/q)
\bigg].
\end{split}
\tag{5}
\]
Weights vanish outside their indicated support. Thus \(n\asymp X\) and \(n-h>X\), so all logarithms have positive arguments. This is the actual R9/R11 component, including its log-cofactor weight.

The family \(\mathcal Q_X\) may be the full canonical complementary family or any selected moduli \(q\le Q\). We use only the cutoff and \(|\mu(q)|\le1\). An added \((\log q)^j\) weight, for a fixed nonnegative integer \(j\), changes \((\log X)^2\) in (2) to \((\log X)^{2+j}\); it does not affect the power margin.

For all positive integers, including \(n=1\), the identity
\(\Lambda=\mu*\log\) is exact. At 1 both sides are zero. For a real \(U\ge1\), \(r\le U\) means the usual integer cutoff, with its endpoint included. Consequently
\[
\mathcal D_{\mathcal Q}^{V}[\Lambda]
=\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le U}]
+\mathcal D_{\mathcal Q}^{V}[\Lambda_{>U}],
\quad
\Lambda_{>U}(n)=
\sum_{\substack{r\mid n\\r>U}}\mu(r)\log(n/r).
\tag{6}
\]
No prime-power removal or asymptotic main-term substitution occurs here. Neither summand need be nonnegative.

## 2. Why a smooth longer coefficient cancels the complete phase mean

Let \(q\ge2\), let \(a\bmod q\) be arbitrary, and fix inner coefficients \(\beta_n\) independently of \(m\). Define the periodic function
\[
R_{q,a}(m)=1_{(m,q)=1}
\sum_{\substack{n\\(n,q)=1}}\beta_n
\left[e(amn/q)-\frac{c_q(a)}{\varphi(q)}\right],
\tag{7}
\]
where \(e(t)=e^{2\pi it}\) and \(c_q\) denotes the Ramanujan sum.
Multiplication by a unit \(n\) permutes the unit residues, so \(c_q(an)=c_q(a)\). It follows exactly that
\[
\sum_{m\bmod q}R_{q,a}(m)=0.
\tag{8}
\]
This includes nonprimitive \(a\), and does not require squarefree \(q\). For \(a=0\), the function itself vanishes.

Suppose \(A_X\) is smooth on a fixed positive compact support, and every fixed derivative has a uniform fixed-power logarithmic bound.
Use the Fourier conventions
\[
\widehat R(\ell)=q^{-1}\sum_{m\bmod q}R(m)e(-\ell m/q),
\qquad
\widehat A(t)=\int_{\mathbb R}A(u)e(-tu)\,du.
\]
Fourier expansion and Poisson summation give
\[
\sum_m A_X(m/M)R_{q,a}(m)
=M\sum_{\nu\ne0}
\widehat R(-\nu\bmod q)\widehat A_X(M\nu/q).
\tag{9}
\]
The omitted \(\nu=0\), and all nonzero multiples of \(q\), have coefficient zero by (8).
Writing \(B=\sum_n|\beta_n|\), we have \(|\widehat R(\ell)|\le2B\).
For \(M\ge q\), integration by parts \(J\ge2\) times therefore gives
\[
\left|\sum_m A_X(m/M)R_{q,a}(m)\right|
\ll_J MB(\log X)^{C_J}(q/M)^J.
\tag{10}
\]
This does not assign a Siegel–Walfisz property to the twisted sequence.

The actual shift Fourier weights satisfy, by finite summation by parts,
\[
|S_{V,H}(\beta)|\ll_{V,K}H(1+H\|\beta\|)^{-K},
\qquad
\sum_{a=1}^{q-1}|S_{V,H}(a/q)|\ll_V q.
\tag{11}
\]
Hence the full numerator sum with its \(1/q\) coefficient costs \(O_V(1)\) per modulus. Its zero numerator vanishes by (8); there is no hidden \(S_{V,H}(0)\asymp H\) term.
At \(M=X^{.6}\), \(q\le Q=X^{.523}\), the ratio \(q/M\le X^{-.077}\) permits any fixed power saving by choosing \(J\).

For a nonnegative smooth longer profile that is positive on an interval, the restricted positive rational core from R13 still has a large contribution by the same residue count on that interval. Equations (8)–(10) give a constructive reason why other phases cancel it in the full sum. They make no such claim for a nonsmooth or arithmetically oscillating longer coefficient.

## 3. A progression identity retaining the whole actual kernel

Expand (1) inside (5), writing \(n=rs\). If \((r,q)>1\), the progression \(rs\equiv h\pmod q\) is empty because \((h,q)=1\); its primitive principal sum is empty as well. Such terms vanish exactly.

For \((r,q)=1\), put \(b\equiv h\overline r\pmod q\), a unit residue.
The longer variable \(s\) has scale \(L_r=X/r\) and weight
\[
F_{r,h,q}(s)=(\log s)\,w_h(rs-h)\log((rs-h)/q).
\tag{12}
\]
Its coefficient outside is \(\mu(r)\). Write
\(F_{r,h,q}(s)=\Phi_{r,h,q}(s/L_r)\).
With \(\delta=H/X=1/T\), \(z=h/H\), and \(u=s/L_r\), the profile is exactly
\[
\begin{split}
\Phi_{r,h,q}(u)=&
\chi(u-\delta z)(u-\delta z)^{-3/2}u^{-3/2}
\operatorname{sinc}_0\!\left(\delta^{-1}\log\frac{u}{u-\delta z}\right)\\
&\times[\log(X/r)+\log u]\,
[\log(X/q)+\log(u-\delta z)].
\end{split}
\tag{13}
\]
On this support \(u-\delta z>1\) and \(u>1\), so the chosen branches of both \(a\)-factors are correct.
The apparently singular phase has the regular form
\[
\delta^{-1}\log\frac{u}{u-\delta z}
=\int_0^z\frac{dt}{u-\delta t}.
\tag{14}
\]
The fixed compact support of \(\chi\), and \(z\) in the fixed support of \(V\), imply that these profiles lie in a fixed positive compact interval and satisfy
\[
\sup_{r\le U,q\le Q,h}
\sum_{j=0}^J\|\Phi_{r,h,q}^{(j)}\|_\infty
\ll_{J,\chi}(\log X)^2
\tag{15}
\]
for every fixed \(J\). Zero extension outside the support is smooth because \(\chi\) is compactly supported in the open interval. All bounds are uniform in the displayed parameters, including \(T\). No separated substitute for the actual kernel was used.

For any such profile, \(L>0\), and a unit \(b\bmod q\), Poisson summation gives
\[
\begin{split}
&\sum_{s\equiv b\ (q)}\Phi(s/L)
-\frac1{\varphi(q)}\sum_{(s,q)=1}\Phi(s/L)\\
&\qquad=\frac Lq\sum_{k\ne0}\widehat\Phi(kL/q)
\left[e(kb/q)-\frac{c_q(k)}{\varphi(q)}\right].
\end{split}
\tag{16}
\]
The Fourier convention is that in (9). Its \(k=0\) term cancels since
\(c_q(0)=\varphi(q)\). This is finite progression summation of a smooth function; there are no contour or pole terms.
Using \(|c_q(k)|\le\varphi(q)\), followed by \(J\) integrations by parts, proves
\[
\left|\text{left side of (16)}\right|
\ll_{J,\chi}\frac Lq(q/L)^J(\log X)^2,
\quad L\ge2q,\ J\ge2.
\tag{17}
\]
The assumption \(UQ\le X/2\) ensures \(L_r=X/r\ge2q\) for every term.

## 4. Summing every short divisor, actual shift and permitted modulus

Apply (17) to (12) and use only \(|\mu(r)\mu(q)|\le1\) and
\(\sum_h|V(h/H)|\ll_VH\). Since
\(\sum_{r\le U}r^{J-1}\ll_JU^J\) and
\(\sum_{q\le Q}q^{J-1}\ll_JQ^J\), the result is
\[
\begin{split}
C_JH(\log X)^2
\sum_{r\le U}\sum_{q\le Q}q^{J-1}(X/r)^{1-J}
&\ll_J HX^{1-J}U^JQ^J(\log X)^2\\
&=HX(UQ/X)^J O_J((\log X)^2).
\end{split}
\tag{18}
\]
This proves (2). An arbitrary selected family is bounded by this full cutoff sum. All coprimality restrictions were retained until taking the upper bound.

For \(U=X^{2/5}\), \(UQ/X=X^{-77/1000}\). At the largest shift length and \(J=4\), the exponent is
\[
1+\frac27-4\frac{77}{1000}=\frac{1711}{1750}<1.
\tag{19}
\]
This needs just four fixed derivatives of the profile, explicitly covered by (15).
For example, \(J=17\) gives exponent \(-163/7000\); no high-order numerical calculation is needed.
More generally, fix \(0<\eta<477/1000\) and let
\[
U\le X^{477/1000-\eta},
\tag{20}
\]
Then \(L_r=X/r\ge X^{523/1000+\eta}\) for every retained divisor, while the profile seminorms in (15) remain \(O_J(\log^2X)\) uniformly.
For any fixed integer \(J\ge2\) with \(J\eta>2/7\), equation (18) gives
\[
|\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le U}]|
\ll X^{1+2/7-J\eta}(\log X)^2=o(X\log X).
\tag{20a}
\]
Choosing a larger fixed \(J\) gives any desired smaller absolute power.
Constants may depend on \(\eta,J,V,\chi\); no uniform claim as \(\eta\to0\) is made.

## 5. Precisely which divisor and Heath–Brown components are covered

Equation (6) is an exact arithmetic application: the \(\mu*\log\) portion with short Möbius divisor \(r\le U\) has negligible discrepancy. The Möbius factor is not assumed smooth. It is attached to the shorter fixed variable, while the logarithmic cofactor has a sufficiently long smooth summation range.

The same criterion can be stated for a Heath–Brown decomposition. Here is the needed identity with its range proved. Let \(\mathbf1(n)=1\), let \(\epsilon\) be the identity for Dirichlet convolution, and let \(\mu_{\le Y}=\mu1_{[1,Y]}\).
Then
\[
E=\epsilon-\mu_{\le Y}*\mathbf1
=\mu_{>Y}*\mathbf1
\]
is supported on integers greater than \(Y\). Thus \(E^{*k}*\Lambda\) vanishes on \(n\le Y^k\). Expanding \(\epsilon-E^{*k}\) and using
\(\mathbf1*\Lambda=\log\) proves, on that range,
\[
\Lambda=
\sum_{j=1}^k(-1)^{j-1}\binom kj
(\mu_{\le Y})^{*j}*\mathbf1^{*(j-1)}*\log.
\tag{21}
\]
The equality at 1 is again zero on both sides. Choose \(Y^k\) above the fixed upper end of the actual \(n\asymp X\) support to cover all terms.

After a smooth multiplicative partition, every component of (21) with an individual unrestricted \(\mathbf1\) or \(\log\) variable at scale
\[
L\ge QX^\eta
\tag{22}
\]
is handled by the same progression proof. Combine all other variables into a short coefficient \(c(r)\), with \(r\ll X/L\). It may contain truncated Möbius variables and divisor multiplicities. A fixed divisor bound on \(c(r)\) costs at most \(X^\varepsilon\) for any fixed \(\varepsilon>0\); increasing \(J\) absorbs this cost. Smooth partition factors and fixed powers of logarithms preserve (15), with their fixed logarithmic losses recorded.

The condition is on an individual smooth variable, not the total size of a product. If a nominal longer coefficient is itself a convolution, opening it helps only on subranges where an actual remaining smooth variable still satisfies (22). For example, a product \(ab\asymp X^{.6}\) does not establish that the \(b\)-range in
\(\alpha_m=\sum_{ab=m}c(a)A(b/L)\) exceeds \(Q\).

The exact remainder \(\Lambda_{>U}\) in (6) stays untreated. It need not be balanced: its logarithmic cofactor can be small. So do Type II and higher-factor components for which every individual smooth variable is at most \(QX^{o(1)}\). A longer Möbius or unsmoothed divisor sequence does not satisfy (15) merely because its support is long. No estimate for these remaining pieces is asserted.

## 6. Research consequence and verification scope

R13's sparse rational cores can have large positive restricted main terms. Here an adequately long smooth variable makes their complete centered sum cancel, with the original primitive mean and all frequencies retained. The direct progression proof also carries the actual joint \(s,r,h\) kernel, avoiding any unproved weight separation.

For the actual zeta-facing discrepancy, (2)–(6) remove a definite short-divisor portion unconditionally. The residual problem can therefore be studied with that portion subtracted exactly and a proved small error. This does not bound the remaining signed piece, prove a covariance asymptotic, refute AH, or establish Montgomery's conjecture.

The source paper [OpenAI, Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), Definitions 2.6–2.9 and Proposition 2.18, supplies the coefficient terminology used for comparison. Its proof of Corollary 2.19 invokes a Heath–Brown reduction; the identity used here is proved directly in (21). The actual kernel and normalization are displayed in full in (4)–(5), following the frozen R9–R11 definitions.

The adjacent check verifies complete-period centering, the Poisson sign on an independently summed Gaussian progression, exact exponent arithmetic, and a finite symbolic-coefficient version of (21). The Gaussian computation is a diagnostic; (16) is the ordinary analytic proof. No large-prime realization, parameter search, external model, or prior-file modification is used.
