# The sharp odd cofactor in its first stationary band

Date: 2026-09-07. Independent analytic challenge by the stationary-challenge agent. Status: ordinary proof submitted for root review. No novelty claim, new prime computation, RH consequence beyond the stated local estimate, or conjecture resolution is claimed.

## 1. Outcome and exact scope

The sharp cofactor admits a uniform first-band Poisson/Fresnel representation whose error is small **after** multiplication by the actual R29 prime-error Mellin transform and Möbius polynomial. In the standard interval \((K,2K]\), both the first alias and the second alias's endpoint transition must be retained. With the exact half-endpoint correction written below,

\[
B_K(t)=E_K(t)+\frac{-I_1(t)+I_2(t)}2+O(\log K),
\qquad \pi K\le t\le2\pi K.
\tag{1}
\]

Each \(I_r\) has a uniform Fresnel formula, including a saddle on either sharp endpoint, with another \(O(\log K)\) error. The combined error in the normalized R29 pairing is \(O(T^{-1/2})\).

The resulting leading term is still a signed arithmetic correlation. The transformation identifies its rational additive phases explicitly; it does not supply cancellation in that correlation. The original \(O(1)\) carrier estimate remains \(O(1)\). No \(o(1)\), strict variance constant, or global AH contradiction follows here.

## 2. Definitions inherited without alteration

Use the corrected R29 manuscript `research-round29/signed-mellin-test/SIGNED_MELLIN_BLOCK_BOUND.md`, SHA256 `753f116b8ebc5d6cc7d7a4e148c98e9b8ef9df97d4327efe2fa094507aa13492`.

Put \(X=T^2\), \(\ell=\log T\), \(D,K\asymp T\),

\[
M_D(t)=\sum_{\substack{D<d\le2D\\d\text{ odd}}}\mu(d)d^{it},
\qquad
B_K(t)=\sum_{\substack{K<k\le2K\\k\text{ odd}}}\log k\,k^{it}.
\]

The actual smooth extension is

\[
f(x)=X\ell^2b_T(x)\chi(x/X)
\sum_{n\text{ odd}}
V((n-x)/T)(x/n)^T[\Lambda(n)-2].
\tag{2}
\]

In particular the integer prime variable \(n\) is fixed when differentiating. All odd prime powers, the odd center \(2\), and the product cutoff are retained. Let

\[
\widehat f(t)=\int_0^\infty f(x)x^{-it}\frac{dx}{x}.
\]

For any measurable \(J\subset[\pi K,2\pi K]\), define its contribution by

\[
Z_J=\frac1{\pi X\ell^2}\int_J\widehat f(t)M_D(t)B_K(t)\,dt.
\tag{3}
\]

The R29 proof supplies under ordinary RH

\[
\|\widehat f\|_{L^2(J)}\ll\sqrt T\log T,
\qquad
\|M_D\|_{L^2(J)}\ll T.
\tag{4}
\]

Only these two bounds are needed for the integrated errors below. The second is unconditional. The stronger positive and negative Sobolev statements in R29 remain available, but their already proved low-band/tail estimates must not be mistaken for an improvement on this first stationary band.

## 3. Exact sharp-endpoint Poisson identity

For real \(K\ge2\), put

\[
I_r(t)=\int_K^{2K}\log x\,e^{i(t\log x-\pi r x)}\,dx,
\qquad r\in\mathbb Z,
\tag{5}
\]

\[
E_K(t)=\frac12\left[
\mathbf1_{2K\in2\mathbb Z+1}\log(2K)(2K)^{it}
-\mathbf1_{K\in2\mathbb Z+1}\log K\,K^{it}
\right].
\tag{6}
\]

Then

\[
B_K(t)=E_K(t)+\frac12\lim_{N\to\infty}
\sum_{r=-N}^{N}(-1)^r I_r(t).
\tag{7}
\]

To prove this without suppressing endpoints, periodize the compact piecewise smooth function \(h(x)=\log x\,x^{it}\mathbf1_{[K,2K]}(x)\) with period \(2\). Its Fourier coefficient at index \(r\) is \(I_r(t)/2\). The symmetric Fourier series at the odd lattice point \(1\) converges to the average of its two one-sided limits. It therefore counts each odd endpoint with weight \(1/2\). The factor at that point is \(e^{\pi i r}=(-1)^r\). Adding (6) excludes an odd lower endpoint and includes an odd upper endpoint exactly. This proves (7), with no smoothing and no change to the half-open convention.

### 3.1 A uniform finite truncation

Fix \(0<c<C<\infty\), and assume \(cK\le t\le CK\). Choose a fixed integer \(R>2C/\pi+2\). Then

\[
B_K(t)=E_K(t)+\frac12\sum_{|r|\le R}(-1)^rI_r(t)+O_{c,C,R}(\log K),
\tag{8}
\]

uniformly in real \(K\ge2\), including endpoints arbitrarily close to the odd lattice.

Here is the tail estimate. Write \(a(x)=\log x\) and \(\Phi_r(x)=t\log x-\pi r x\). For \(|r|>R\),

\[
|\Phi_r'|\gg|r|,\quad |\Phi_r''|\ll K^{-1},\quad
|\Phi_r'''|\ll K^{-2}.
\]

One integration by parts gives the endpoint term \([a e^{i\Phi_r}/(i\Phi_r')]_K^{2K}\). The integral containing \(a\Phi_r''/(\Phi_r')^2\) is \(O(\log K/r^2)\) in absolute value. The integral containing \(a'/\Phi_r'\) is integrated once more: its endpoint and integral terms are \(O(1/(Kr^2))\). Hence

\[
I_r(t)=\left[-\frac{\log x\,x^{it}e^{-\pi i r x}}{i\pi r}\right]_{K}^{2K}
+O(\log K/r^2).
\tag{9}
\]

The replacement of \(1/\Phi_r'\) by \(-1/(\pi r)\) costs \(O(\log K/r^2)\). The absolutely summable errors in (9) contribute \(O(\log K)\). Pair the remaining \(r\) and \(-r\) endpoint terms before summing. After the parity factor, they are constant multiples of

\[
\log x\,x^{it}\sum_{r>R}\frac{\sin(\pi r(x+1))}{r}.
\]

The symmetric sine tails are uniformly bounded in their real argument and truncation endpoint. An elementary proof splits at \(r\asymp1/\operatorname{dist}(\theta,2\pi\mathbb Z)\), uses \(|\sin r\theta|\le r\operatorname{dist}(\theta,2\pi\mathbb Z)\) before the split, and geometric-sum partial summation afterwards. This proves (8). The individual \(1/r\) endpoint terms must not be summed absolutely.

### 3.2 The first full band

For \(\pi K\le t\le2\pi K\), the stationary point of \(\Phi_r\) is \(x_r=t/(\pi r)\) when \(r>0\). All \(r\le0\) and all \(r\ge3\) in the finite sum (8) have derivative bounded away from zero on \([K,2K]\). One integration by parts bounds each by \(O(\log K)\). Aliases \(r=1\) and \(r=2\) remain, proving (1).

At \(t=2\pi K\), alias \(1\) has its saddle at \(2K\) and alias \(2\) has its saddle at \(K\). Omitting the second term is therefore not uniformly legitimate. On the narrower range \(t\le(2\pi-\delta)K\), alias \(2\) is nonstationary and may be absorbed into \(O_\delta(\log K)\).

For a different sharp interval \((aT,bT]\), formula (7) uses those exact endpoints and the first alias starts at \(t=\pi aT\). If \(b<2a\), the first band's upper endpoint \(\pi bT\) lies strictly below the second alias's onset \(2\pi aT\). In particular \([1.05T,1.35T]\) has this separation. This observation does not authorize moving the endpoints of the actual block.

## 4. Uniform Fresnel transitions, with a proof of the error

For \(t>0\) and fixed \(r\ge1\), let

\[
x_r=\frac{t}{\pi r},\qquad
v(y)=\operatorname{sgn}(y-1)\sqrt{2(y-1-\log y)},\qquad v(1)=0,
\]

\[
U_K=\sqrt t\,v(K/x_r),\qquad
U_{2K}=\sqrt t\,v(2K/x_r),\qquad
\mathcal F(a,b)=\int_a^b e^{-iu^2/2}\,du.
\tag{10}
\]

The function \(v\) is smooth and strictly increasing on \((0,\infty)\), with derivative \(1\) at \(1\). Let \(q\) be its inverse. Uniformly for \(cK\le t\le CK\), with fixed \(c,C,r\),

\[
I_r(t)=\frac{\sqrt t}{\pi r}\log x_r\,
e^{i(t\log x_r-t)}\mathcal F(U_K,U_{2K})+O_{c,C,r}(\log K).
\tag{11}
\]

This formula preserves both transition endpoints even when a saddle is exactly on them. It is not an asymptotic that first discards a boundary neighborhood.

Indeed, write \(x=x_r y\) and \(u=\sqrt t\,v(y)\). Then exactly

\[
t\log x-\pi r x=t\log x_r-t-u^2/2,
\]

\[
I_r(t)=e^{i(t\log x_r-t)}\frac{x_r}{\sqrt t}
\int_{U_K}^{U_{2K}}
\log\bigl(x_rq(u/\sqrt t)\bigr)q'(u/\sqrt t)e^{-iu^2/2}\,du.
\tag{12}
\]

The amplitude at \(u=0\) is \(\log x_r\). On the fixed compact range of \(u/\sqrt t\), including \(0\), write its difference from that value as \(vH(v)\). Smoothness gives \(|H|+|H'|\ll\log K\). Thus the error in (12) is bounded using

\[
\int uH(u/\sqrt t)e^{-iu^2/2}\,du
=\left[iH(u/\sqrt t)e^{-iu^2/2}\right]
-\frac i{\sqrt t}\int H'(u/\sqrt t)e^{-iu^2/2}\,du.
\]

The integration interval has length \(O(\sqrt t)\), so the last display is \(O(\log K)\). The prefactor for the amplitude difference is \(x_r/t=1/(\pi r)\), proving (11). This argument covers \(U_K=0\), \(U_{2K}=0\), and either endpoint within a distance \(O(1)\) in Fresnel coordinates.

The Fresnel primitive is uniformly bounded on the real line. Consequently every main term in (11) is \(O(\sqrt T\log T)\). In the interior \((\pi+\delta)K\le t\le(2\pi-\delta)K\), the first alias has

\[
\mathcal F(U_K,U_{2K})=\sqrt{2\pi}e^{-i\pi/4}+O_\delta(T^{-1/2}),
\]

by integration by parts on the two Fresnel tails and the Abel-regularized Gaussian integral. Therefore the simpler interior formula is

\[
B_K(t)=-\sqrt{\frac t{2\pi}}\log(t/\pi)
\exp\!\left(i[t\log(t/\pi)-t-\pi/4]\right)
+O_\delta(\log T).
\tag{13}
\]

Formula (13) is not used at a sharp endpoint; (1), (6), and (11) provide the uniform statement there.

## 5. Both signs and integrated remainder

Since the original coefficients are real,

\[
B_K(-t)=\overline{B_K(t)},\quad
M_D(-t)=\overline{M_D(t)},\quad
\widehat f(-t)=\overline{\widehat f(t)}.
\]

Thus the negative-band representation is the complex conjugate of the positive one. In the Poisson formula its stationary aliases have negative indices; their parity factors are unchanged. The contribution from \(J\cup(-J)\) is exactly \(2\operatorname{Re} Z_J\).

If \(R_B(t)=O(\log T)\) is any of the combined uniform remainders above, then (4) proves

\[
\begin{aligned}
\left|\frac1{\pi X\ell^2}\int_J\widehat f(t)M_D(t)R_B(t)\,dt\right|
&\ll\frac{\log T}{T^2\ell^2}
\|\widehat f\|_{L^2(J)}\|M_D\|_{L^2(J)}\\
&\ll T^{-1/2}.
\end{aligned}
\tag{14}
\]

The exact endpoint term \(E_K\) is also \(O(\log T)\), so it may be removed only after recording (6) and invoking (14). All constants refer to the fixed central geometry and fixed profiles. This is an integrated estimate on the stated band, not a claim that a pointwise error can be summed over every Mellin band. R29 supplies the separate estimates for frequencies outside a fixed multiple of \(T\).

## 6. What the substitution actually asks us to estimate

Define the **exact sharp Mellin-band projection**

\[
f_J(x)=\frac1{2\pi}\int_J\widehat f(t)x^{it}\,dt.
\tag{15}
\]

It is generally complex and is not the original compactly supported function \(f\). In particular it must not be replaced by a compact local prime sum without carrying this projection.

Use (1) in (3), remove the recorded \(E_K\) by (14), and interchange the finite \(d\) sum with the two compact \(k\) integrals. Mellin inversion gives the exact leading correlation

\[
\boxed{
Z_J=\frac1{X\ell^2}
\sum_{\substack{D<d\le2D\\d\text{ odd}}}\frac{\mu(d)}d
\int_{dK}^{2dK}\log(m/d)\,f_J(m)
\left[-e^{-\pi i m/d}+e^{-2\pi i m/d}\right]dm
+O(T^{-1/2}).}
\tag{16}
\]

The signs in the bracket are the genuine odd-lattice factors \((-1)^1\) and \((-1)^2\). The \(1/d\) is the Jacobian \(dk=dm/d\). The original factor \(1/\pi\), the Poisson factor \(1/2\), and inverse Mellin factor \(2\pi\) combine to the displayed \(1/(X\ell^2)\). No conjugate is inserted in the Möbius pairing.

The rational additive phases have denominator \(2d\) and \(d\), respectively. As \(d\asymp T\), they oscillate at the same scale as the original short prime kernel. Formula (16) is a concrete proof obligation for a saving: for example, proving that its displayed signed sum/integral is \(o(X\ell^2)\) would give \(Z_J=o(1)\) on this band. A strict global AH contradiction requires substantially more: noncentral packets, the remaining bands, their signs/constants, and the actual global threshold must all be controlled.

There is no independent new cancellation in the substitution itself. Reversing (15) and Poisson returns precisely the original divisor block. Nor is (16) a standard unweighted average over primes in progressions: it contains the actual Möbius coefficient, an oscillatory phase whose denominator depends on that coefficient's index, the sharp factor interval, and the band-projected actual prime error. Dropping any of these would change the target.

## 7. Why the present classical estimates still stop at a bounded answer

In the interior, (13) has size \(\asymp\sqrt T\log T\); the Fresnel transition formula gives the same upper scale at the edges. Inserting this into the already legal Cauchy estimate yields

\[
\frac1{T^2\ell^2}
(\sqrt T\log T)(\sqrt T\log T)(T)=O(1).
\tag{17}
\]

No logarithm or power remains to save. Even a hypothetical pointwise square-root estimate \(|M_D(t)|\ll\sqrt T\) would only reproduce (17) after bounding \(\int_J|\widehat f|\) by \(|J|^{1/2}\|\widehat f\|_2\). An estimate with an additional \(T^\varepsilon\) factor would be weaker for this purpose. Thus a better pointwise Möbius bound at the square-root scale is not by itself the missing correlation estimate.

For comparison, if one starts merely with a bound \(A(u)=\sum_{d\le u,\ d\text{ odd}}\mu(d)=O_\varepsilon(u^{1/2+\varepsilon})\), partial summation only gives

\[
M_D(t)=A(2D)(2D)^{it}-A(D)D^{it}
-it\int_D^{2D}A(u)u^{it-1}\,du
=O_\varepsilon((1+|t|)D^{1/2+\varepsilon}).
\]

At \(|t|\asymp D\), this is no improvement over the trivial bound. This calculation concerns that particular use of a Mertens estimate; it is not a claim that every classical theorem about twisted Möbius sums has been excluded.

The sharp remaining requirement is cancellation involving the *actual* \(\widehat f\) and \(M_D\) jointly, or a genuinely stronger applicable prime-error energy input. The explicit oscillatory phase in (11) gives a useful representation in which to search, but estimating its absolute value loses the same information as before. No bound on that joint cancellation is proved in this note.

## 8. Verification and source scope

The Poisson identity, uniform finite-tail estimate, Fresnel change of variables, endpoint bookkeeping, and normalization in (16) are proved directly above. Their only imported analytic estimates are the two R29 bounds (4), for the exact extension (2). R29 itself cites the original Montgomery–Vaughan mean-value theorem and the fixed-parameter Selberg integral under RH, with the fixed-prime-variable derivative and lambda integration retained.

The adjacent checker contains elementary symbolic and finite lattice tests only. It checks the phase identity, integration-by-parts differentiation, normalization, endpoint convention, parity, and Fresnel integral normalization. It does not certify the asymptotic proof, test actual primes, enlarge a numerical scan, or prove an unrecorded arithmetic saving.
