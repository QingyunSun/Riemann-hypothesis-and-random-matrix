# Removing the full linear singleton correction from the exact Pareto remainder

Date: 2026-09-05. Status: bounded ordinary proof submitted for independent review. The renormalization proved here is unconditional, using the prime number theorem. RH gives the stated quantitative rate and is still required for the inherited transfer from the actual prime variance. This is an application of classical singular-series averaging and partial summation; no novelty, strict variance improvement or AH refutation is claimed.

## 1. Exact statement

Keep the unchanged R21 definitions
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},\quad
W_T(x)=\omega(\log x/\ell),\quad T\ge4,
\]
where the fixed nonnegative smooth function \(\omega\) is supported on \([7/4,9/4]\). Put
\[
a_n=\Lambda(n)-1,\quad c_h=\mathfrak S(h)-1,\quad
b_T(m)=\frac{T m^{-T}}{\ell^2}\int_1^m W_T(x)x^{T-2}dx,
\quad k_{m,T}(h)=(1+h/m)^{-T}.
\tag{1}
\]
All prime powers and all positive integer shifts are retained. Define a new centered pair coefficient, with its exact singular-series factors,
\[
q_{m,h}=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)\bigl(\Lambda(m)+\Lambda(m+h)-1\bigr).
\tag{2}
\]
Direct algebra gives
\[
a_ma_{m+h}-c_h=q_{m,h}+c_h(a_m+a_{m+h}).
\tag{3}
\]
Let
\[
\mathcal L_T
=2\sum_m b_T(m)\sum_{h\ge1}k_{m,T}(h)c_h(a_m+a_{m+h}),
\tag{4}
\]
\[
\mathcal Q_T=2\sum_m b_T(m)\sum_{h\ge1}k_{m,T}(h)q_{m,h}.
\tag{5}
\]
Both sums, and all rearrangements below at fixed \(T\ge4\), converge absolutely. In particular the R21 remainder satisfies the exact identity
\(\mathcal E_T=\mathcal Q_T+\mathcal L_T\).

**Theorem.** Write
\[
\eta(L)=\sup_{y\ge L}\frac{|\Psi(y)-\lfloor y\rfloor|}{y}.
\]
Then
\[
\boxed{\mathcal L_T
=O_\omega\bigl(\ell^{-1}+\eta(L)+2^{-T}\bigr)=o(1)}
\tag{6}
\]
unconditionally. Under RH, the more useful quantitative estimate is
\[
\boxed{\mathcal L_T
=O_\omega\bigl(\ell^{-1}+\ell T^{-7/8}+2^{-T}\bigr).}
\tag{7}
\]
Consequently, under RH, the actual Round 20 variance obeys
\[
\overline V_T=\varepsilon m_0+\mathcal Q_T+o(1).
\tag{8}
\]
Thus the strict sufficient target is equivalently
\[
\liminf_T\mathcal Q_T\le1-\varepsilon m_0.
\tag{9}
\]
No bound of the form (9) is proved.

The change is specific to the full signed, weighted aggregate. Equation (2) does not define a pointwise approximation to \(\Lambda(m)\Lambda(m+h)\), and no uniform small-prefix-error assertion follows.

## 2. Classical inputs and absolute convergence

We use the unconditional triangular singular-series estimate
\[
A_2(y):=\sum_{h\ge1}(y-h)_+c_h
=-\frac12y\log y+O(y),\qquad y\ge1,
\tag{10}
\]
with \(A_2(y)=0\) for \(0\le y\le1\). At integer arguments this is half of Montgomery–Soundararajan's equation (16), printed p.4; linear interpolation proves the real-variable version. It also gives \(A_2(y)=O(y\log(2y))\) globally.

The corresponding exact forward Pareto transform was proved in R21, Lemma 2:
\[
\sum_{h\ge1}c_h(1+h/m)^{-T}
=-\frac12\log(m/T)+O(1),
\quad T\ge4,\ m\ge T,
\tag{11}
\]
with an absolute uniform constant. Its proof integrates (10) twice and controls the logarithmic moment of a beta-prime probability density. It does not replace the Pareto kernel by an exponential.

We also use the elementary bounds \(\Psi(y)\ll y\), \(|a_n|\le1+\log n\) and \(\mathfrak S(h)\ll_\delta h^\delta\) for any fixed \(\delta>0\). The last follows from the positive finite Euler product and the divisor bound. Choose \(\delta=1/2\). For \(m>2U\),
\[
b_T(m)\ll_\omega \ell^{-2}U^{T-1}m^{-T}.
\tag{12}
\]
Summing over \(h\) first with the absolute coefficient bound gives at most a constant depending on fixed \(T\) times \(m^{3/2}\log^2(2m)\). The remaining \(m\)-sum converges for \(T\ge4\). The finitely many smaller \(m\)'s cause no issue. This justifies (3)–(5), interchange of the two discrete indices, and the initial separation into marginals. Uniform bounds in \(T\) are supplied below, not inferred from this fixed-\(T\) argument.

The prime number theorem, \(\Psi(y)=y+o(y)\), implies \(\eta(L)\to0\). For the RH rate we use \(|\Psi(y)-y|\ll\sqrt y\log^2(2y)\), with the prime powers included.

## 3. The weight and the smooth signed main term

With \(\omega\) extended by zero,
\[
b_T(m)=\frac{T}{m\ell^2}
\int_0^1\omega((\log m+\log u)/\ell)u^{T-2}du.
\tag{13}
\]
It follows by differentiation under this convergent integral that
\[
|b_T(m)|\ll_\omega\frac1{m\ell^2},\qquad
|b_T'(m)|\ll_\omega\frac1{m^2\ell^2},\qquad
b_T(m)=0\quad(m\le L).
\tag{14}
\]
There is no derivative factor \(T\): the integral mass is \(1/(T-1)\).

On \(L\le y\le2U\), set
\[
g_T(y)=b_T(y)\log(y/T),\qquad
M_T=\sum_{L<n\le2U}a_ng_T(n).
\tag{15}
\]
Throughout this range,
\[
|g_T(y)|\ll_\omega\frac1{y\ell},\qquad
|g_T'(y)|\ll_\omega\frac1{y^2\ell}.
\tag{16}
\]
Let \(A(y)=\sum_{n\le y}a_n=\Psi(y)-\lfloor y\rfloor\). Abel summation on the exact real endpoints \(L,2U\) gives the main term bounds
\[
M_T=O_\omega(\eta(L))
\quad\text{unconditionally},
\tag{17}
\]
\[
M_T=O_\omega(\ell/\sqrt L)
\quad\text{under RH}.
\tag{18}
\]
For (17), the two endpoints are \(O(\eta(L)/\ell)\), and the integral is bounded by
\[
\frac{C_\omega\eta(L)}{\ell}\int_L^{2U}\frac{dy}{y}
=O_\omega(\eta(L)).
\]
For (18), use \(|A(y)|\ll\sqrt y\log^2(2y)\), where \(\log y\asymp\ell\), and integrate \(y^{-3/2}\). The integral and endpoints are \(O_\omega(\ell/\sqrt L)\). These arguments work with noninteger \(L,2U\); \(A\) is the right-continuous step function with atoms \(a_n\).

Finally Chebyshev's bound and partial summation give
\[
\sum_{L<n\le2U}\frac{|a_n|}{n}
\le\sum_{L<n\le2U}\frac{\Lambda(n)+1}{n}
=O(\ell).
\tag{19}
\]
The prime sum here must not be bounded by the pointwise \(\log n\), which would lose a logarithm.

## 4. The first marginal

Write
\[
\mathcal L_T^{(1)}
=2\sum_m b_T(m)a_m\sum_{h\ge1}c_h k_{m,T}(h).
\tag{20}
\]
For \(L<m\le2U\), substitute the uniform transform (11). Equations (14) and (19) show
\[
\mathcal L_T^{(1)}\big|_{m\le2U}
=-M_T+O_\omega(\ell^{-1}).
\tag{21}
\]
The \(O(1)\) remainder in (11) is multiplied by \(\sum b_T(m)|a_m|\), which is \(O_\omega(1/\ell)\), not by an unweighted prime count.

For \(m>2U\), (11) bounds the whole signed inner row by \(O(\log(2m))\). Combining this with (12) and \(|a_m|\ll\log(2m)\) gives
\[
\mathcal L_T^{(1)}\big|_{m>2U}
=O_\omega(2^{-T}).
\tag{22}
\]
Indeed the integral of \(m^{-T}\log^2(2m)\) from \(2U\) has size
\(O((2U)^{1-T}\ell^2/(T-1))\). The first integer term is controlled at the same scale since \(2U\ge T\). The powers of \(U\) in (12) cancel. No tail of a positive divergent series has been discarded.

## 5. A uniform backward transform

After setting \(n=m+h\), the second marginal is
\[
\mathcal L_T^{(2)}
=2\sum_{n>L}a_n C_T(n),\qquad
C_T(n)=\sum_{h\ge1}c_h f_n(h),
\tag{23}
\]
where \(f_n(h)=0\) for \(n-h\le L\), and otherwise
\[
f_n(h)=b_T(n-h)(1-h/n)^T.
\]
The cancellation of powers is exact:
\[
\boxed{
f_n(h)=\frac{T}{n^T\ell^2}I_T(n-h),\qquad
I_T(y)=\int_1^y W_T(x)x^{T-2}dx.}
\tag{24}
\]
For \(h\ge0\), use this expression until \(h=n-L\), and extend it by zero beyond. Because \(\omega\) is smooth and vanishes to all orders at its support boundaries, this is a smooth compactly supported function on the half-line. It satisfies \(f_n(0)=b_T(n)\). No value of \(\log(n-h)\) outside the positive support is used.

For \(m=n-h\) in the support,
\[
f_n'(h)=-\frac{T}{n^T\ell^2}W_T(m)m^{T-2},
\]
\[
\boxed{
f_n''(h)=\frac{T}{n^T\ell^2}
\left[W_T'(m)m^{T-2}+(T-2)W_T(m)m^{T-3}\right].}
\tag{25}
\]
The second derivative can have either sign, because \(W_T'\) does. The proof never treats it as a positive density.

**Lemma.** Uniformly for \(T\ge4\) and \(L<n\le2U\),
\[
\boxed{
C_T(n)=-\frac12 b_T(n)\log(n/T)
+O_\omega\!\left(\frac1{n\ell^2}\right).}
\tag{26}
\]

**Proof.** The exact hinge identity and compact support give
\[
C_T(n)=\int_0^\infty A_2(h)f_n''(h)dh,
\qquad
\int_0^\infty h f_n''(h)dh=f_n(0)=b_T(n).
\tag{27}
\]
There is no boundary atom: \(A_2\) is continuous and piecewise linear, with distributional second derivative \(\sum c_h\delta_h\). The second equality also follows by ordinary integration by parts; \(hf_n'(h)\) vanishes at both ends.

Use \(|W_T'(m)|\le\|\omega'\|_\infty/(m\ell)\). For \(0<h<n\), extending the bound by zero when the actual derivative vanishes, (25) implies
\[
|f_n''(h)|
\le\frac{C_\omega T(T-1)}{n^3\ell^2}
(1-h/n)^{T-3}.
\tag{28}
\]
Thus
\[
\int_0^\infty h|f_n''(h)|dh\ll_\omega\frac1{n\ell^2}.
\tag{29}
\]
For the logarithmic moment, the probability density
\[
(T-2)(T-1)t(1-t)^{T-3}dt,\qquad 0<t<1,
\tag{30}
\]
has total mass one. Under \(u=Tt\), its mean \(u\) is exactly \(2\), and its density for \(0<u<1\) is at most \(u\). Hence
\[
\mathbb E|\log u|
\le\int_0^1u|\log u|du+\mathbb E u\le9/4.
\tag{31}
\]
Multiplying by the normalization factor in (28), which differs from the probability normalization by a uniformly bounded factor \(T/(T-2)\), yields
\[
\int h|\log(Th/n)|\,|f_n''(h)|dh
\ll_\omega\frac1{n\ell^2}.
\tag{32}
\]
Therefore
\[
\int h\log h\,f_n''(h)dh
=b_T(n)\log(n/T)+O_\omega(1/(n\ell^2)).
\tag{33}
\]

Insert (10) into (27). On \(h\ge1\), its error is bounded by (29). On \(0<h<1\), replacing the zero function \(A_2\) by \(-h\log h/2\) costs at most
\[
\frac{C_\omega T^2}{n^3\ell^2}
\int_0^1h|\log h|dh
\ll_\omega\frac1{n\ell^2},
\]
since \(n\ge L\ge T\). Equations (27) and (33) prove (26). \(\square\)

The bound in the lemma is adequate on the finite main range. Summing its \(O(1/n)\) error to infinity would be invalid; the actual tail is treated next.

## 6. The second marginal's infinite endpoint

For \(n>2U\), the support of \(f_n''\) lies in
\([n-U,n-L]\subset[n/2,n]\). Thus
\[
|A_2(h)|\ll n\log(2n)
\]
on this support. Integrate the absolute value in (25), using the actual support in \(m\):
\[
\int|f_n''(h)|dh
\ll_\omega
\frac{T U^{T-2}}{\ell^2 n^T}.
\tag{34}
\]
It follows from the first identity in (27) that
\[
|C_T(n)|
\ll_\omega
\frac{T U^{T-2}n^{1-T}\log(2n)}{\ell^2}.
\tag{35}
\]
Consequently
\[
\sum_{n>2U}|a_n C_T(n)|\ll_\omega2^{-T}.
\tag{36}
\]
For a direct check, if \(Y=2U\),
\[
\int_Y^\infty y^{1-T}\log^2(2y)dy
=Y^{2-T}
\left[\frac{\log^2(2Y)}{T-2}
+\frac{2\log(2Y)}{(T-2)^2}
+\frac2{(T-2)^3}\right].
\tag{37}
\]
In (35) the \(U^{T-2}\) cancels this power of \(Y\), and \(\log Y\asymp\ell\). The first possible integer term is at most a fixed multiple of the integral because \(Y\ge T\). This is a uniform bound for the original signed row with the outer absolute value; no assertion of a sign for \(f_n''\) is required.

On \(L<n\le2U\), (26) and (19) give
\[
\mathcal L_T^{(2)}=-M_T+O_\omega(\ell^{-1}+2^{-T}).
\tag{38}
\]
Combining (21), (22) and (38),
\[
\boxed{\mathcal L_T=-2M_T+O_\omega(\ell^{-1}+2^{-T}).}
\tag{39}
\]
Equations (17)–(18) prove (6)–(7).

## 7. What the renormalization does and does not remove

The exact new coefficient is
\[
q_{m,h}
=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)\Lambda(m)
-\mathfrak S(h)\Lambda(m+h)+\mathfrak S(h).
\]
Its linear terms are still present, with their singular-series factors. Formula (6) proves the legitimacy of this replacement in the full signed weighted aggregate; it does not permit dropping these new linear terms individually.

For an odd \(h\), \(\mathfrak S(h)=0\), so \(q_{m,h}=\Lambda(m)\Lambda(m+h)\). The artificial large singleton fluctuation responsible for the R21 \(h=1\) obstruction is absent from this coefficient. This observation alone supplies no bound on the entire new remainder, in particular its even shifts. No all-shifts sub-square-root prefix bound is asserted for \(q\).

Under RH the exact target (9) is equivalent to the old signed target, because their difference is \(o(1)\). RH plus AH still predicts the same saturation constant. The unconditional renormalization does not imply an unconditional prime/zero transfer.

## 8. Sources and verification

- [Montgomery–Soundararajan, Primes in short intervals, arXiv:math/0409258v1](https://arxiv.org/pdf/math/0409258v1), printed p.4, equation (16): the unconditional triangular singular-series estimate. Its retained PDF/text and the R21 proof of the forward transform are pinned in the receipt.
- [NIST DLMF 25.16.3](https://dlmf.nist.gov/25.16.E3): the PNT formulation \(\Psi(x)=x+o(x)\), used only for (17) and unconditional \(o(1)\).
- [Schoenfeld, Theorem 10, equation (6.2)](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), printed p.337: the ordinary RH bound for \(\Psi-x\), including all prime powers, used for (18).
- R21's corrected centered-pair report and R20's variance theorem are inherited programme dependencies; their assumptions remain as stated.

The finite exact checker verifies the polynomial residual identity, backward power cancellation and derivatives, hinge and beta moments, and the tail antiderivatives. These are bounded algebra checks, not a numerical test of the strict inequality. All ordinary estimates, limits and convergence qualifications are given above. No new prime-height data or parameter scan is used.

