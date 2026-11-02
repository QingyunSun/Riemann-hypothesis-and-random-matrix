# The complete odd-shift prime-power pair term is negligible

Date: 2026-09-05. Status: ordinary unconditional proof, submitted for independent review. This is a companion to the small-shift estimate. It concerns the proposed renormalized pair coefficient only; no replacement of the original R21 residual is assumed or proved here.

## 1. Exact statement

Keep the unchanged fixed weight and continuum window
\[
\ell=\log T,\qquad L=T^{7/4},\qquad U=T^{9/4},\qquad
W_T(x)=\omega(\log x/\ell),\qquad T\ge4,
\]
where \(0\le\omega\le B:=\|\omega\|_\infty\) and \(\omega\) is supported on \([7/4,9/4]\). In the actual programme \(B\le1\). Use the exact weight
\[
b_T(m)=\frac{T m^{-T}}{\ell^2}\int_1^m W_T(x)x^{T-2}dx.
\tag{1}
\]
All prime powers remain in \(\Lambda\), with \(\Lambda(1)=0\).

Define the complete nonnegative odd-shift pair contribution
\[
\mathcal O_T=
2\sum_{m\ge1}b_T(m)
\sum_{\substack{h\ge1\\h\text{ odd}}}
(1+h/m)^{-T}\Lambda(m)\Lambda(m+h).
\tag{2}
\]
The sum in \(h\) is not truncated.

**Theorem.** For every real \(T\ge4\), unconditionally,
\[
\boxed{0\le\mathcal O_T\le
\frac{32B}{T}+\frac{64B}{\ell^2}2^{-T}.}
\tag{3}
\]
In particular \(\mathcal O_T=O_\omega(T^{-1})=o(1)\). The constants are deliberately loose, explicit upper constants, not computed prime statistics.

For the proposed coefficient
\[
q_{m,h}=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-1],
\tag{4}
\]
one has \(q_{m,h}=\Lambda(m)\Lambda(m+h)\) when \(h\) is odd. Thus (3) removes **all odd shifts from the sum using \(q_{m,h}\)** with a proved error. The difference between this coefficient and the original centered coefficient is recorded precisely in Section 5; that difference is not estimated in this note.

## 2. Two elementary bounds, valid at every shift size

The exact integral (1) gives
\[
b_T(m)\le\frac{TB}{(T-1)m\ell^2},\qquad
b_T(m)=0\quad(m\le L),
\tag{5}
\]
and, for \(m>U\),
\[
b_T(m)\le\frac{TB}{(T-1)\ell^2}U^{T-1}m^{-T}.
\tag{6}
\]
Both follow by integrating the positive majorant \(Bx^{T-2}\). No approximation of the Pareto weight is involved.

We use the explicit elementary Chebyshev bound
\[
\Psi(x)\le C_0x\quad(x\ge1),\qquad C_0=4\log2.
\tag{7}
\]
Indeed, every prime-power term in \(\Psi(2n)-\Psi(n)\) contributes to the corresponding prime valuation of \({2n\choose n}\). Hence this difference is at most \(\log{2n\choose n}\le2n\log2\). Telescoping on powers of two and then using monotonicity proves (7) for real \(x\). This proof retains higher prime powers and does not use PNT or RH.

For any integer \(r>L\), the function \(x\mapsto(r/x)^T\log x\) is decreasing on \([r,\infty)\), since \(T\log r>1\). Therefore
\[
\sum_{n>r}\Lambda(n)(r/n)^T
\le\sum_{n>r}\log n\,(r/n)^T
\le r\left(\frac{\log r}{T-1}+\frac1{(T-1)^2}\right).
\tag{8}
\]
Here the integral comparison starts at the integer \(r\), so there is no missing first lattice term. A different bound useful in the tail follows from Stieltjes integration and (7):
\[
\sum_{n>r}\Lambda(n)(r/n)^T
=-\Psi(r)+Tr^T\int_r^\infty\Psi(x)x^{-T-1}dx
\le\frac{C_0Tr}{T-1}.
\tag{9}
\]
The boundary term \(-\Psi(r)\) has the correct sign for the strict inequality \(n>r\), and is discarded only in this upper bound.

## 3. Split by the location of the even power of two

For odd \(h\), exactly one of \(m,n=m+h\) is even. If \(\Lambda(m)\Lambda(n)\ne0\), that even integer is a power \(r=2^j\), with \(\Lambda(r)=\log2\). Here and below the powers have integer exponent \(j\ge1\). This yields the exact nonnegative split
\[
\begin{aligned}
\mathcal O_T^-&=
2\log2\sum_{r=2^j}b_T(r)
\sum_{\substack{n>r\\n\text{ odd}}}(r/n)^T\Lambda(n),\\
\mathcal O_T^+&=
2\log2\sum_{r=2^j}r^{-T}
\sum_{\substack{m<r\\m\text{ odd}}}b_T(m)m^T\Lambda(m),\\
\mathcal O_T&=\mathcal O_T^-+\mathcal O_T^+.
\end{aligned}
\tag{10}
\]
The signs \(-,+\) label the lower and upper position of the even endpoint, not a sign of the contribution. The factor two is the original ordered-pair factor in (2). Terms with \(r\le L\) vanish in both cases.

First consider powers \(L<r\le2U\). Combining (5) and (8), and enlarging the inner sum to all integers, bounds the lower-endpoint term for each \(r\) by
\[
\frac{2(\log2)B}{\ell^2}
\left(\frac{T\log r}{(T-1)^2}
+\frac{T}{(T-1)^3}\right).
\tag{11}
\]
For the upper-endpoint term, (5), \(\Lambda(m)\le\log r\), and
\[
\sum_{1\le m<r}m^{T-1}\le\int_1^r x^{T-1}dx\le r^T/T
\]
give instead
\[
\frac{2(\log2)B\log r}{(T-1)\ell^2}.
\tag{12}
\]
These estimates do not assume prime independence or a short-interval prime asymptotic. In (11)–(12) we may include extra even inner indices because every summand being bounded is nonnegative.

Let \(N\) count powers of two in \((L,2U]\). For \(T\ge4\),
\[
N\le\frac{\log(2U/L)}{\log2}+1
=\frac{\ell}{2\log2}+2
\le\frac{3\ell}{2\log2},
\qquad \log r\le\frac{11}{4}\ell.
\]
Consequently
\(\sum_{L<r\le2U}\log r\le33\ell^2/(8\log2)\).
Summing (11)–(12) gives a bound
\[
\frac{33B}{4}\left(\frac{T}{(T-1)^2}+\frac1{T-1}\right)
+\frac{3BT}{(T-1)^3\ell}
\le\frac{247B}{9T}<\frac{32B}{T}.
\tag{13}
\]
The displayed rational estimate uses only \(T/(T-1)\le4/3\), \(T\ge4\), and \(\ell\ge\log4>1\).

## 4. All powers above the window

For a power \(r>2U\) serving as the lower endpoint, combine (6) and (9). Its contribution is at most
\[
\frac{2(\log2)C_0B}{\ell^2}
\frac{T^2}{(T-1)^2}(U/r)^{T-1}.
\tag{14}
\]

For an upper endpoint \(r>2U\), substituting the original integral (1), rather than its coarser bound (5), gives
\[
\begin{aligned}
2\log2\,r^{-T}\sum_{m<r}b_T(m)m^T\Lambda(m)
&=\frac{2T\log2}{\ell^2}r^{-T}
\int_L^U W_T(x)x^{T-2}
\sum_{x<m<r}\Lambda(m)\,dx\\
&\le\frac{2(\log2)C_0B}{\ell^2}
\frac{T}{T-1}(U/r)^{T-1}.
\end{aligned}
\tag{15}
\]
In the first line the inner sum is over all integers. It is the positive enlargement of the odd inner sum from (10). Equality is between the enlarged expressions displayed in (15), not a claim that parity disappeared from (10). Nonnegative Fubini is legal, and the strict upper endpoint is bounded by \(\Psi(r)\le C_0r\).

Let \(r_0\) be the first power of two strictly above \(2U\). The whole infinite tail is geometric:
\[
\sum_{\substack{r=2^j\\r>2U}}(U/r)^{T-1}
=\frac{(U/r_0)^{T-1}}{1-2^{1-T}}
\le\frac{16}{7}2^{-T}.
\tag{16}
\]
Using \(C_0=4\log2\), \(\log2<1\) and \(T/(T-1)\le4/3\), the sum of (14)–(15) is at most
\[
\frac{8(\log2)^2B}{\ell^2}
\left(\frac{T^2}{(T-1)^2}+\frac{T}{T-1}\right)
\frac{16}{7}2^{-T}
\le\frac{512B}{9\ell^2}2^{-T}
<\frac{64B}{\ell^2}2^{-T}.
\tag{17}
\]
Combining (13) and (17) proves (3), including absolute convergence of the full nonnegative odd-pair sum. No finite cutoff or omitted large-shift contribution remains.

## 5. Exact relation to the original centered residual

For the original R21 coefficient \(a_ma_{m+h}-c_h\), direct algebra gives
\[
a_ma_{m+h}-c_h
=q_{m,h}+c_h[\Lambda(m)+\Lambda(m+h)-2].
\tag{18}
\]
In particular on odd shifts the second term is
\(-\Lambda(m)-\Lambda(m+h)+2\). It is absent from (2), but present in the old residual. This is why (3) must not be presented as a bound for all odd shifts of that old residual.

To replace the complete old residual by the complete \(q\)-sum, one would separately need to control
\[
2\sum_m b_T(m)\sum_{h\ge1}(1+h/m)^{-T}
c_h[\Lambda(m)+\Lambda(m+h)-2].
\tag{19}
\]
No vanishing, sign or bound for (19) is assumed here. If such a replacement is established elsewhere, the present theorem then leaves only the even shifts in its \(q\)-sum, with error at most (3). The residual even-shift arithmetic still requires an independent estimate below the AH saturation value.

## Inputs and bounded checks

The exact weights and coefficient normalization are pinned to the revised R21 centered-pair report. This note's arithmetic inputs are only \(\Lambda(n)\le\log n\), the support of prime powers, and the elementary binomial proof of (7). It does not import the upper sieve or RH estimate used in the preceding small-shift report.

The adjacent checker verifies only the finite algebra, two integral primitives, geometric-series factor and rational constants. It contains no prime-data sampling, parameter search or numerical conjecture test. The ordinary proof, not those scalar checks, establishes the full infinite sum and its uniform range.
