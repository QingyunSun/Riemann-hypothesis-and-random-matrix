# The log-weighted prime-tail moment: a primary-source check and its arithmetic remainder

Date: 2026-09-05. This bounded attempt proves no new lower bound at the required scale. It identifies a relevant derivative theorem, checks a legitimate centered finite-prime expansion, and isolates the missing arithmetic coefficient. The positive prime diagonal is explicit; the required lower bound on the jointly centered remainder is not established.

## 1. A derivative theorem does not supply the missing mixed moment

The directly relevant primary source is Andrés Chirre, [A note on the mean values of the derivatives of ζ′/ζ, arXiv:2107.13636v2](https://arxiv.org/html/2107.13636v2), 3 January 2022. Proposition 5, equation (2.3), expresses the normalized squared norm of the kth logarithmic derivative as a known integral on \([0,1]\) plus
\[
\int_1^\infty \alpha^{2k}e^{-2a\alpha}F(\alpha,T)\,d\alpha+o(1)
\]
for fixed \(a>0\). Theorem 1 makes its sharp fixed-width asymptotic equivalent to pair correlation. Thus this theorem does not provide a sharper RH-only arithmetic value for the signed mixed moment considered here. Its fixed-width remainder cannot be differentiated or made uniform along a growing width without further proof. The source HTML and its hash are retained in `sources/receipt.json`.

This is a narrow source conclusion, not an assertion that every theorem on derivatives or short intervals has been exhausted. The stronger centered-small-arc input being investigated separately is outside this note.

## 2. A finite, centered arithmetic expansion with its cutoff error

Assume RH. Let \(L=\log T\), \(N=\lfloor T/L^6\rfloor\),
\(s=1/2+\delta+it\), and \(\delta=b/(2L)>0\). Let \(R_b\) be the genuine-prime residual already defined in Round 10, including its pole and endpoint. Define
\[
K_b=-R_b-L^{-1}\partial_sR_b,
\qquad
M_T(b)=\frac{e^b}{TL^2}\Re\int_0^T R_b\overline{K_b}\,dt.
\]
The derivative acts on the actual analytic continuation, not on a bare prime series in the critical strip.

For finite \(Y>N\), put
\[
C_Y(s)=\sum_{N<p\leq Y}(\log p)p^{-s}-\int_N^Y x^{-s}\,dx,
\quad
D_Y=-C_Y-L^{-1}\partial_s C_Y.
\tag{1}
\]
These are finite expressions. Write \(E_1(x)=\theta(x)-x\), with endpoints including primes equal to their argument, and
\(P_N(s)=N^{1-s}/(s-1)\). Stieltjes summation gives exactly
\[
C_Y=E_1(Y)Y^{-s}-E_1(N)N^{-s}
  +s\int_N^Y E_1(x)x^{-s-1}\,dx.
\]
Consequently \(C_Y\to C:=R_b-P_N\), uniformly on \(0\leq t\leq T\) for each fixed \(T,b\). For \(Y\geq4\), the RH estimate on \(E_1\) gives the explicit error
\[
|C-C_Y|\ll Y^{-\delta}\left[
\log^2Y+|s|\left(
\frac{\log^2Y}{\delta}+\frac{2\log Y}{\delta^2}
+\frac2{\delta^3}\right)\right].
\tag{2}
\]
Differentiation adds one logarithm and one possible inverse power of \(\delta\). In particular, for \(T\geq e\) and \(0<\delta\leq1/4\), a convenient coarse common bound is
\[
|C-C_Y|+|(-C-L^{-1}C_s')-D_Y|
\ll (1+T)\delta^{-4}(1+\log Y)^3Y^{-\delta}.
\tag{3}
\]
This justifies the mixed-moment limit at fixed \(T,b\); it also states its real cost. For example, on \(2\leq b\leq2G(T)\), \(G=o(\log L)\), the choice \(Y=\exp(L^3)\) makes (3) at most \(O(TL^{13}e^{-L^2})\). This is a legitimate uniform analytic cutoff, not a computationally efficient prime experiment. No finite prime computation is offered as evidence for the limiting remainder.

## 3. Pole terms are negligible at this scale, with a direct norm estimate

Here and below \(2\leq b\leq2G(T)\) with \(G=o(\log L)\). For all sufficiently large \(T\), \(\delta\in[1/L,1/4]\). The RH local-zero partial fractions yield uniformly
\[
\|R_b\|_{L^2(0,T)}+\|K_b\|_{L^2(0,T)}\ll\sqrt T L^2.
\tag{4}
\]
For the derivative in (4), the nearby-zero bound is \(O(L/\delta^2)=O(L^3)\), before division by \(L\); the remote sum is smaller. The absolutely convergent prime-power correction and its derivative are respectively \(O(\delta^{-2})\) and \(O(\delta^{-3})\). Their contributions to \(K_b\) are therefore \(O(L^2)\). The finite prime polynomial and its log-weighted companion obey the same uniform mean-value majorant used in Round 8, since \(\log p/L\leq1\) for \(p\leq N\). This establishes (4) without differentiating an unknown asymptotic error.

Since \(\sigma\leq3/4\),
\[
\|P_N\|_2\ll\sqrt N,
\qquad
-P_N-L^{-1}P_N'
=\left(\frac{\log N}{L}-1+\frac1{L(s-1)}\right)P_N.
\]
Its companion has norm \(O((\log L)/L)\sqrt N\). Expanding the two mixed products and applying Cauchy–Schwarz gives
\[
M_T(b)=\frac{e^b}{TL^2}\Re\int_0^T
C\,\overline{(-C-L^{-1}C_s')}\,dt
+O(e^bL^{-3}).
\tag{5}
\]
The error in (5) is \(o(b^{-3})\) uniformly on the stated slow range. Thus the pole is accounted for and then removed at a proved error; the endpoint \(E_1(N)N^{-s}\) remains part of \(C\).

## 4. The arithmetic diagonal and the exact missing coefficient

Let \(u(x)=\log x/L-1\) and
\[
d\mu_Y(x)=\sum_{N<p\leq Y}(\log p)\delta_p(dx)-\mathbf1_{(N,Y]}(x)\,dx.
\]
Set
\[
G_{T,b}(x,y)=(xy)^{-1/2-b/(2L)}
\frac{u(x)+u(y)}2\,
\operatorname{sinc}_0\!\left(T\log(x/y)\right).
\]
Finite expansion of (1), with the real part symmetrized in \(x,y\), gives
\[
\frac{e^b}{TL^2}\Re\int_0^T C_Y\overline{D_Y}\,dt
=\frac{e^b}{L^2}\iint G_{T,b}(x,y)\,d\mu_Y(x)d\mu_Y(y).
\tag{6}
\]
The prime-prime diagonal of (6) is
\[
\mathcal D_T(b;Y)=\frac{e^b}{L^2}
\sum_{N<p\leq Y}(\log p)^2p^{-1-b/L}
\left(\frac{\log p}{L}-1\right).
\]
Its limit \(\mathcal D_T(b)\) converges absolutely. Applying the RH estimate for \(\theta(x)-x\) by partial summation gives, uniformly in the slow range,
\[
\mathcal D_T(b)=e^b\int_{\log N/L}^{\infty}
v(v-1)e^{-bv}\,dv
+O(e^bN^{-1/2}L).
\tag{7}
\]
The elementary tail integral from \(v=1\) is
\[
e^b\int_1^\infty v(v-1)e^{-bv}\,dv
=\frac1{b^2}+\frac2{b^3}.
\]
The interval \(\log N/L<v<1\) contributes a nonpositive term of size
\(O((\log L/L)^2)\), since \(1-\log N/L=6\log L/L+o(1/L)\). Both errors in (7), multiplied by \(b^3\), tend to zero uniformly. Therefore
\[
\boxed{\mathcal D_T(b)=\frac1{b^2}+\frac2{b^3}+o(b^{-3}).}
\tag{8}
\]

Define \(\mathcal B_T(b;Y)\) by subtracting this finite prime-prime diagonal from the double integral in (6), and put
\(\mathcal B_T(b)=\lim_{Y\to\infty}\mathcal B_T(b;Y)\).
The limit exists by (2)–(3) and absolute convergence of the diagonal. It contains together the off-diagonal prime-prime sum, both prime-continuum terms, and the continuum-continuum term. Those components must not be assigned independent infinite limits: only their centered combination has been justified.

Equations (5)–(8) prove the arithmetic decomposition
\[
\boxed{M_T(b)=\frac1{b^2}+\frac2{b^3}
+\mathcal B_T(b)+o(b^{-3})}
\tag{9}
\]
uniformly on the slow range. Thus, for example, the additional lower bound
\[
\mathcal B_T(s)\geq-\frac{4-\varepsilon}{s^3}
-\frac{\eta_T}{s^3},\qquad \eta_T\to0,
\tag{10}
\]
uniformly up to \(2G(T)\), would give the Round 10 criterion
\(M_T(s)\geq s^{-2}-(2-\varepsilon)s^{-3}-o(s^{-3})\).
An averaged sufficient version is
\[
\int_b^{2b}\mathcal B_T(s)\,ds
\geq-\frac{3}{2b^2}+\frac{\varepsilon}{b^2}+o(b^{-2}).
\tag{11}
\]
Indeed the integrated diagonal equals \(1/(2b)+3/(4b^2)+o(b^{-2})\), so (11) yields the required value strictly above \(-3/4\) after the coupled normalization. Equations (10) and (11) are unproved arithmetic inputs, not consequences of positivity of the prime coefficients.

## 5. What the accessible short-prime projection actually sees

A projection confined to prime lengths below \(T\) sees only \(u(p)\leq0\). In the residual's available slice \(N<p\leq T\), its diagonal log-weighted contribution is \(O((\log L/L)^2)\) and nonpositive. It cannot supply the positive leading term \(1/b^2\) in (8).

That term comes from logarithmic excess of size \(1/b\), hence prime lengths \(X=T^{1+O(1/b)}\). The elementary contour/mixed-polynomial estimate used for the short projection has error \(O(X\log^3T)\) at such a cutoff, before normalization; even disregarding any further logarithmic costs, its normalized error is \(O(e^b(X/T)L)\). On a fixed edge shell \(X=T^{1+s/b}\), \(1\leq s\leq2\), this majorant contains \(\exp(sL/b)\), far larger than \(b^{-3}\). This states the failure of that particular bound, not the magnitude of the actual error or an impossibility theorem.

The inspected higher-derivative theorem leaves an unknown pair-correlation integral, and the elementary short-prime projection misses the required positive-excess sector at the necessary precision. The explicit remaining obligation is the centered arithmetic remainder (10) or its averaged version (11). No generic point-process counterexample, parameter scan, or numerical approximation to a divergent prime series was used.
