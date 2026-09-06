# A legal fixed-modulus-6 centering of the actual prime-pair remainder

Date: 2026-09-05. Author: residual_gram / Astra. Status: bounded ordinary proof submitted for independent review. The modulus is fixed at 6 throughout. The centering change is unconditional, using the prime number theorem in the two reduced classes modulo 6. RH remains required for the inherited actual-variance transfer. No GRH, growing-modulus assertion, strict variance gain, or AH refutation is claimed.

The main new technical point in this note is the signed singular-series progression difference in (8), whose prefix is only logarithmic. This permits a fixed-character prime number theorem after exact kernel smoothing. In particular, forbidden classes with one genuinely prime endpoint are retained in that character calculation; they are not incorrectly declared prime-power exceptions.

## 1. Exact definitions and theorem

Retain the fixed R21/R22 weight and notation
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},\quad
W_T(x)=\omega(\log x/\ell),\quad T\ge4,
\]
\[
b(x)=\frac{T x^{-T}}{\ell^2}\int_1^xW_T(y)y^{T-2}dy,
\qquad k(m,h)=\left(\frac m{m+h}\right)^T.
\tag{1}
\]
Here omega is the same fixed nonnegative smooth function, supported in [7/4,9/4]. Extend b by zero below L. Its bounds and exact primitive representation are those already proved in R22:
\[
b(x)\ll_\omega(x\ell^2)^{-1},\quad
|b'(x)|\ll_\omega(x^2\ell^2)^{-1},\quad
b(x)\ll_\omega U^{T-1}x^{-T}/\ell^2.
\tag{2}
\]
The last bound is used on x>U. Keep all prime powers in Lambda.

Let S(h) be the usual prime-pair singular series, zero for odd h. Define
\[
A_6(m,h)=1_{\gcd(m(m+h),6)=1},\qquad
\nu_6(h)=\#\{a\bmod6:\gcd(a(a+h),6)=1\}.
\]
For even h,
\[
\nu_6(h)=\begin{cases}2,&h\equiv0\pmod6,\\1,&h\equiv2,4\pmod6,\end{cases}
\qquad r_6(m,h)=\frac{6A_6(m,h)}{\nu_6(h)},\quad c_6=3.
\tag{3}
\]
For odd h, nu_6(h)=0; set r_6(m,h)=0. This convention never divides by zero, and S(h)=0 on precisely those exceptional shifts.

The full parity-adjusted coefficient from R22 is
\[
q_2(m,h)=\Lambda(m)\Lambda(m+h)
-S(h)[\Lambda(m)+\Lambda(m+h)-2\,1_{m\ {\rm odd}}].
\]
Define the fixed-modulus-6 coefficient by the proposed local normalization,
\[
\boxed{q_6(m,h)=\Lambda(m)\Lambda(m+h)
-S(h)r_6(m,h)\left[\frac{\Lambda(m)+\Lambda(m+h)}3-1\right].}
\tag{4}
\]
All displayed double sums below converge absolutely for fixed T≥4, by the same elementary majorants as R22: r_6 is bounded by 6, S(h)≪h^{1/2}, and Lambda is bounded by a logarithm.

Let chi_6 be the nonprincipal character modulo 6: it equals 1 on 1 mod6, −1 on 5 mod6, and 0 on the other four classes. Put
\[
B_6(x)=\sum_{n\le x}\Lambda(n)\chi_6(n),\qquad
\eta_6(L)=\sup_{x\ge L}|B_6(x)|/x.
\tag{5}
\]
For this one fixed modulus, PNT in arithmetic progressions implies eta_6(L)→0 unconditionally.

**Theorem.** Uniformly as real T tends to infinity,
\[
\boxed{2\sum_{m,h\ge1}b(m)k(m,h)[q_6(m,h)-q_2(m,h)]
=O_\omega\left(\eta_6(L)+\frac1{T\ell}+2^{-T}\right)=o(1).}
\tag{6}
\]
Also,
\[
\boxed{2\sum_{\substack{m,h\ge1\\A_6(m,h)=0}}
b(m)k(m,h)|q_6(m,h)|
=O_\omega(T^{-1}+2^{-T}/\ell^2)=o(1).}
\tag{7}
\]
No effective rate for eta_6 is needed or claimed. In particular, ordinary RH for zeta is not misused as a GRH estimate for this nonprincipal character.

## 2. The exact local difference keeps the one-prime forbidden rows

Define the signed shift sequence
\[
d_h=S(h)\bigl(1_{h\equiv2\pmod6}-1_{h\equiv4\pmod6}\bigr),
\qquad D(Y)=\sum_{1\le h\le Y}d_h.
\tag{8}
\]
The algebraic difference of (4) and q_2 is
\[
q_6-q_2=S(h)\left[(1-r_6/3)(\Lambda(m)+\Lambda(m+h))
+r_6-2\,1_{m\ {\rm odd}}\right].
\tag{9}
\]
Checking the six residue classes, for every even h one has separately
\[
\begin{aligned}
S(h)(1-r_6/3)
&=\chi_6(m)d_h+S(h)1_{\gcd(m,6)>1},\\
S(h)(1-r_6/3)
&=-\chi_6(m+h)d_h+S(h)1_{\gcd(m+h,6)>1}.
\end{aligned}
\tag{10}
\]
For odd h all terms involving S or d vanish. Thus the linear part of (9) is exactly
\[
d_h\,[\Lambda(m)\chi_6(m)-\Lambda(m+h)\chi_6(m+h)]
+S(h)\,[e(m)+e(m+h)],
\tag{11}
\]
where
\[
e(n)=\Lambda(n)1_{\gcd(n,6)>1}
=(\log2)1_{n=2^j,\ j\ge1}+(\log3)1_{n=3^j,\ j\ge1}.
\tag{12}
\]
Only the e terms are prime-power exceptions. The d_h terms include all endpoints coprime to 6, whether or not the opposite endpoint is divisible by 3.

For example, if h≡2 mod6 and m≡1 mod6, the opposite endpoint is divisible by 3, r_6=0, and the coefficient of Lambda(m) in (9) is +S(h). That genuinely prime endpoint survives as chi_6(m)d_h=+S(h) in (11). On the admissible class m≡5 mod6 the sign is instead negative. Ignoring the former row would destroy this cancellation.

## 3. A logarithmic prefix bound for the signed singular-series progression difference

For k≥1 the exact positive divisor expansion is
\[
S(2k)=2C_2\sum_{d\mid k}\frac{\mu^2(d)1_{d\ {\rm odd}}}{\prod_{p\mid d}(p-2)},
\qquad C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right).
\tag{13}
\]
Let chi_3 be the nonprincipal character modulo 3, so d_{2k}=S(2k)chi_3(k). Terms with 3 dividing k vanish. Expanding (13) yields the exact identity
\[
D(Y)=2C_2\sum_{\substack{d\le Y/2\\(d,6)=1}}
g(d)\chi_3(d)\sum_{j\le Y/(2d)}\chi_3(j),
\qquad
 g(d)=\frac{\mu^2(d)}{\prod_{p\mid d}(p-2)}.
\tag{14}
\]
The partial sums of chi_3 have absolute value at most one, including arbitrary real upper endpoints. Therefore
\[
|D(Y)|\le2C_2\sum_{\substack{d\le Y/2\\(d,6)=1}}g(d).
\]
For completeness this last sum is O(log(2+Y)) by an absolutely convergent positive Euler product, not by an unproved cancellation over d. For squarefree d coprime to 6,
\[
g(d)=\frac1d\prod_{p\mid d}\left(1+\frac2{p-2}\right)
=\frac1d\sum_{e\mid d}\frac{2^{\nu(e)}}{\prod_{p\mid e}(p-2)}.
\]
Dropping squarefree and coprimality restrictions on the remaining multiple of e gives
\[
\sum_{\substack{d\le Z\\(d,6)=1}}g(d)
\le(1+\log Z)\prod_{p>3}\left(1+\frac2{p(p-2)}\right)
\quad(Z\ge1).
\tag{15}
\]
The product converges because its local increments are O(p^{-2}). Consequently
\[
\boxed{|D(Y)|\ll\log(2+Y).}
\tag{16}
\]
This is a proved fixed-modulus progression difference, not an estimate for individual prime pairs. Absolute summation of S(h) before taking this progression difference would lose it.

We also use the R22 elementary inequality
\[
\sum_{h\le Y}S(h)\le Y.
\tag{17}
\]
It follows from the same positive divisor expansion. It is useful for the periodic baseline and exceptional powers, while (16) is the essential input for the genuine-prime linear rows.

## 4. Forward smoothing: a uniform derivative bound before pairing with primes

Define the real-variable transform
\[
K_T(x)=\sum_{h\ge1}d_h(1+h/x)^{-T},\qquad x\ge L.
\]
Stieltjes integration by parts, retaining the full infinite shift range, gives
\[
K_T(x)=\int_0^\infty D(h)\frac{T}{x}(1+h/x)^{-T-1}dh.
\tag{18}
\]
The boundary terms vanish by (16). Differentiation at fixed h gives the exact kernel derivative
\[
\frac{\partial}{\partial x}\left[\frac T x(1+h/x)^{-T-1}\right]
=\frac T{x^2}(1+h/x)^{-T-2}(Th/x-1).
\tag{19}
\]
For x≥1, log(2+h)≤log(2x)+log(1+h/x). Substitution v=h/x in (18) and (19) yields uniformly for T≥4
\[
|K_T(x)|\ll\log(2x),\qquad
|K_T'(x)|\ll\log(2x)/x.
\tag{20}
\]
Here the potentially large T is controlled by explicit integrals. For example,
\[
T\int_0^\infty(1+v)^{-T-2}(Tv+1)dv=\frac{2T}{T+1}\le2.
\]
The additional log(1+v) factor is bounded by v; its integral is
\[
T\int_0^\infty v(1+v)^{-T-2}(Tv+1)dv
=\frac{2T}{(T-1)(T+1)}+\frac1{T+1},
\]
which is bounded. The non-differentiated kernel has mass one and logarithmic moment 1/T. These bounds also justify differentiating under the integral locally uniformly in x.

On [L,2U], the forward coefficient G_T(x)=b(x)K_T(x) therefore satisfies
\[
|G_T(x)|\ll_\omega\frac1{x\ell},\qquad
|G_T'(x)|\ll_\omega\frac1{x^2\ell}.
\tag{21}
\]
The forward genuine-prime contribution in (11) is sum Lambda(m)chi_6(m)G_T(m), so the fixed-character PNT applies to a genuinely smooth coefficient. We have not applied it separately to each of order x/T shifts.

## 5. Backward smoothing and the cancellation in its derivative

Put n=m+h. The backward row coefficient is
\[
C_T(n)=\sum_{h\ge1}d_h b(n-h)\left(\frac{n-h}{n}\right)^T,
\tag{22}
\]
with the summand zero for n−h≤L. Let
\[
f_n(h)=\frac{T}{n^T\ell^2}\int_1^{n-h}W_T(s)s^{T-2}ds
\]
with the same zero extension as R22. Integrating against the prefix D gives
\[
\boxed{C_T(n)=\frac{T}{n^T\ell^2}
\int_0^\infty D(h)W_T(n-h)(n-h)^{T-2}dh.}
\tag{23}
\]
The actual integrand is supported where s=n−h belongs to [L,U]. No logarithm or noninteger power of a nonpositive number is evaluated outside that support.

Using |D(h)|≪log(2n) for 0≤h<n immediately gives
\[
|C_T(n)|\ll_\omega\frac{\log(2n)}{n\ell^2}.
\]
The derivative requires keeping two terms together. Differentiating (23) at fixed h gives
\[
\begin{aligned}
C_T'(n)=\frac{T}{n^T\ell^2}\int_0^\infty D(h)
\bigg[W_T'(s)s^{T-2}
+W_T(s)s^{T-3}\left(\frac{Th}{n}-2\right)\bigg]dh.
\end{aligned}
\tag{24}
\]
The factor is Th/n−2, not an independently bounded term of size T. The moving support contributes no boundary term because W_T is smoothly zero at its support boundaries.

The bound |W_T'(s)|≪1/(s ell) and enlargement to 0<h<n reduce the derivative integral to
\[
\int_0^n(n-h)^{T-3}\left(1+\left|\frac{Th}{n}-2\right|\right)dh
\ll\frac{n^{T-2}}{T-2}.
\tag{25}
\]
Indeed the corresponding normalized variable h/n has beta distribution with parameters 1,T−2; the mean of Th/n is T/(T−1)≤4/3. Bounding the absolute difference by Th/n+2 gives a uniform constant. Thus, for every n>L,
\[
\boxed{|C_T(n)|\ll_\omega\frac{\log(2n)}{n\ell^2},\qquad
|C_T'(n)|\ll_\omega\frac{\log(2n)}{n^2\ell^2}.}
\tag{26}
\]
Both statements remain valid next to L, U and 2U. No division by b(n), relative-error statement or positivity of D is needed.

## 6. Fixed-character PNT controls the complete genuine-prime linear difference

For any continuously differentiable coefficient F with the bounds in (21), partial summation with the exact prefix B_6 gives
\[
\sum_{L<n\le2U}\Lambda(n)\chi_6(n)F(n)
=F(2U)B_6(2U)-F(L)B_6(L)-\int_L^{2U}B_6(x)F'(x)dx.
\]
With (5), the right side is
\[
O_\omega\left(\eta_6(L)\left[\ell^{-1}+\ell^{-1}\log(2U/L)\right]\right)
=O_\omega(\eta_6(L)).
\tag{27}
\]
The endpoints need not be integers. Equations (21) and (26) apply this to both the forward and backward sums in (11), with their opposite signs retained.

The tails past 2U are exponentially small. For the forward row, combine (20) with the exact b-tail and |Lambda|≤log(2x). This gives
\[
\sum_{m>2U}b(m)|\Lambda(m)\chi_6(m)K_T(m)|
\ll_\omega\frac{U^{T-1}}{\ell^2}
\sum_{m>2U}m^{-T}\log^2(2m)
\ll_\omega2^{-T}.
\tag{28}
\]
For n>2U, the actual support in (23) gives
\[
|C_T(n)|\ll_\omega U^{T-1}n^{-T}\log(2n)/\ell^2.
\]
The same elementary tail sum proves an O(2^{-T}) bound after multiplication by |Lambda(n)chi_6(n)|. Uniformity follows from the tail integral denominator T−1 and the first-term comparison 2U≥T. Thus the entire genuine-prime part of (11) is O(eta_6(L)+2^{-T}), without a factor x/T lost by summing separate prime-progression errors.

For the primary input, fixed-modulus PNT in AP states pi(x;6,a)∼x/(2log x) for a=1,5. Ordinary partial summation gives the log-weighted prime sum x/2+o(x) in each class. The total higher-prime-power correction is O(√x log²(2x)) and is negligible; therefore B_6(x)=o(x). The source is [DLMF 27.11, final paragraph](https://dlmf.nist.gov/27.11), which explicitly states the PNT in arithmetic progressions for fixed coprime residue/modulus. No uniformity in a growing modulus or GRH is imported.

## 7. The periodic baseline and genuine exceptional powers

For each even h, the sequence
\[
t_h(m)=r_6(m,h)-2\,1_{m\ {\rm odd}}
\]
is periodic modulo 6 and has mean zero: sum_mmod6 r_6=6 and sum_mmod6 2Iodd=6. Its values and interval partial sums are bounded by an absolute constant, uniformly over all h. On odd h its coefficient S(h) is zero.

On a block X<m≤2X, the endpoint plus total variation norm of b(m)k(m,h) is at most
\[
\frac{C_\omega}{X\ell^2}(1+h/(2X))^{-T}.
\]
Partial summation in m and (17), followed by decreasing-weight summation in h, gives O(1/(T ell²)) per block. Summing O(ell) blocks through 2U gives O(1/(T ell)). For the m>2U tail, absolute summation gives
\[
\ll_\omega\frac{U^{T-1}}{T\ell^2}\sum_{m>2U}m^{1-T}
\ll_\omega\frac{U2^{-T}}{T^2\ell^2}
=O_\omega(1/(T\ell)).
\tag{29}
\]
The first integer term is absorbed since 2U≥T. This is the fixed-period analogue of the R22 parity alternation and retains exactly the r_6 normalization.

The e terms in (11) are supported only on powers of 2 or 3. For either fixed p in {2,3}, a lower endpoint r=p^j in [L,2U] contributes at most
\[
b(r)\log p\sum_hS(h)k(r,h)
\le b(r)\log p\,\frac r{T-1}
\ll_\omega\frac1{T\ell^2}.
\]
For an upper endpoint r=p^j in that range, the bound
\[
b(m)(m/r)^T\le\frac{C_\omega}{r\ell^2}(1-(r-m)/r)^{T-1}
\]
and (17) give the same O(1/(T ell²)) row bound. There are O(ell) powers of either fixed prime in the window.

For r>2U, the lower-endpoint exact tail is bounded by C U^{T−1}r^{1−T}/(T ell²); the upper-endpoint row is bounded by C U^{T−1}r^{1−T}/ell². Sum over r=p^j geometrically. The first power exceeds 2U and the ratio is p^{1−T}≤1/8, so these tails are O(2^{-T}/ell²). Hence the whole e contribution is O(1/(T ell)+2^{-T}/ell²).

Together with (27)–(29), the exact decomposition (9)–(11) proves (6).

## 8. Discarding only the now legitimate forbidden product rows

When A_6(m,h)=0, r_6=0 and q_6(m,h)=Lambda(m)Lambda(m+h). If this product is nonzero, at least one endpoint is a power of 2 or 3. The contribution is nonnegative, and it suffices to sum over the two possibilities, allowing double counting.

For a lower exceptional endpoint r=p^j in [L,2U], the elementary logarithmic majorant gives
\[
\sum_{h\ge1}\Lambda(r+h)(1+h/r)^{-T}
\ll r\log(2r)/T.
\tag{30}
\]
To see the uniform constant, majorize Lambda by log(2(r+h)), integrate the decreasing function against h, and use the exact integrals r/(T−1) and r/(T−1)^2 for the constant and log(1+h/r) terms. The first term is absorbed since r≥L>T. Multiplication by b(r)log p gives O(1/(T ell)) per power, hence O(1/T) after summing O(ell) powers.

For an upper exceptional endpoint r in the same window, use Lambda(m)≤log(2r) and
\[
\sum_{m<r}b(m)(m/r)^T\ll_\omega\frac1{T\ell^2},
\]
which follows by summing (1−h/r)^{T−1} and integrating it over h. This gives the same total O(1/T). Endpoints r≤L contribute zero.

For r>2U, the lower-endpoint bound (30) together with the exact b-tail gives a geometrically summable row C U^{T−1}r^{1−T}log(2r)/(T ell²). For the upper endpoint, the exact primitive cancellation bounds each coefficient by C U^{T−1}r^{-T}/ell²; Chebyshev's inequality sum_{m<r}Lambda(m)≪r then gives a row C U^{T−1}r^{1−T}/ell². Summing powers of the two fixed primes yields O(2^{-T}/ell²), with the lower row even smaller. This proves (7), including the complete infinite endpoint and every higher prime power.

## 9. The resulting target, and the remaining limitation

On admissible pairs the coefficient (4) is explicitly
\[
q_6(m,h)=\begin{cases}
\Lambda(m)\Lambda(m+h)-S(h)[\Lambda(m)+\Lambda(m+h)-3],&h\equiv0\pmod6,\\
\Lambda(m)\Lambda(m+h)-2S(h)[\Lambda(m)+\Lambda(m+h)-3],&h\equiv2,4\pmod6.
\end{cases}
\tag{31}
\]
In both cases m and m+h are coprime to 6. The factor two in the second line is essential. Merely changing the old constant 2 to 3 while retaining the same singleton coefficient on every admissible shift is not this exact local normalization.

The accepted R22 renormalization and parity results, followed by (6)–(7), give
\[
\mathcal E_T=
2\sum_{\substack{m,h\ge1\\\gcd(m(m+h),6)=1}}
b(m)k(m,h)q_6(m,h)+o(1).
\tag{32}
\]
Under the inherited RH variance transfer, the same expression added to M=epsilon m_0 equals the actual length-averaged variance up to o(1). Thus the original strict target remains an upper bound of 1−M for the liminf of this entire signed sum.

This is a proved fixed-congruence normalization, not a strict arithmetic estimate. It handles the linear rows that made the naive p=3 exclusion illegal, but it does not bound the remaining genuine prime-pair correlation. Nothing here licenses a growing wheel, a uniform sub-square-root prefix hypothesis, or discarding further signed terms. The famous zeta-correlation target remains open.

## 10. Checks and provenance

The bounded checker records every residue case modulo 6, the two exact local marginal identities, the period-six baseline, the divisor-character prefix formula with an unevaluated common C_2 factor, and the differentiated forward/backward kernels. These are finite exact checks rather than prime-height computations or evidence for a strict asymptotic gain. Ordinary proofs above supply the uniform estimates. Source receipts pin the retained R22 inputs, the primary fixed-AP theorem page and all local artifacts. No earlier-round source, Git state or author file was edited.
