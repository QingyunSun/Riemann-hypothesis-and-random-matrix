# A size obstruction at the critical discrepancy scale

For the raw triple packet, a signed error of order one is compatible with positivity, the divisibility condition on the counting variable, the singular-series support condition on shifts, and a cumulative discrepancy of order \((T/n)T^\varepsilon\) on polynomially bounded shifts. The example below uses a separately assigned measure for each prime-power twist and shift. The prime problem imposes a further requirement on all these measures, since their weights must factor through one von Mangoldt sequence. This is a limitation on arguments that use only the listed hypotheses, not a counterexample for the actual primes.

## Statement

Set \(L=\log T\), \(\gamma=\alpha+\beta\), with fixed exponents satisfying \(\alpha-\eta>1,\ \beta>\eta>0,\ \gamma+\eta<2\). Take the real even packet \(q=\widehat\psi\in C_c^\infty(-\eta,\eta)\), \(c_\psi=\int\psi^3>0\), and write \(q_\nu(x)=q(\log x/L-\nu)\). Let \(s_{n,h}=\mathbf 1_{(n,h)=1}\mathfrak S(nh)\), the even nonnegative singular series. This construction applies to prime powers \(n=p^a\) in \(T^{\beta-\eta}<n<T^{\beta+\eta}\) and signed \(h\ne0\). Denote the overlap-length reference measure by
\[
dA^0_{n,h}(x)=\frac{s_{n,h}}n\mathbf1_{x>\max(0,-h)}dx.
\]
We take the real part of the residual formed with the complex packet weight
\[
W_{n,h}(x)=\frac{q_\alpha(x/n) q_\gamma(x+h)}{\sqrt{x(x+h)}}
\widehat\Phi\!\left(\frac{T}{2\pi}\log\frac{x}{x+h}\right).
\]
Here \(\Phi\in C_c^\infty(1,2)\) is real, with integral one. Define
\[
R_T[A]=\frac1{L^3}\sum_n\Lambda(n)q_\beta(n)\sum_{h\ne0}
\int W_{n,h}(x)\,d(A_{n,h}-A^0_{n,h})(x).
\]

For each fixed real \(c\), there are nonnegative counting measures \(A^*_{n,h}\), with integer weights supported on \(n\mathbb Z_{>0}\cap\{x+h>0\}\), such that
\[
\sup_y|A^*_{n,h}((0,y])-A^0_{n,h}((0,y])|
\ll_c 1+s_{n,h}\left(1+\frac{T\log p}{n}\right),\qquad
\operatorname{Re}R_T[A^*]\longrightarrow c\beta c_\psi .
\]
The measures work simultaneously for every fixed allowed \(q\) and \(\Phi\); error constants may depend on the fixed tests. The model assigns zero mass whenever \(s_{n,h}=0\). At \(c=1\) the residual cancels the singular-series main term of the raw packet at leading order. The actual primes would have to satisfy an additional estimate to exclude that value. After discretizing and flooring, the small bound is on the **cumulative** discrepancy; the total variation of an atomic measure minus a continuous reference need not be small.

## Construction and calculation

Choose an even real \(f\in C_c^\infty(\mathbb R)\) which equals one on \([1,2]\), vanishes near zero and has integral zero. For example start with an even plateau on \([1,2]\) supported on the union of \((1/2,5/2)\) with its reflection, then subtract two half-weighted translates to distant disjoint intervals. Write
\[
B(u)=\frac1{2\pi}\int f(t)e^{itu}dt,\qquad
K_\Phi(u)=\operatorname{Re}\widehat\Phi(u/(2\pi)).
\]
The function \(B\) is even, real, Schwartz, and \(B(0)=0\). In particular \(\int_0^\infty |B(u)|du/u<\infty\). Fourier inversion gives
\[
\int_\mathbb R B(u)K_\Phi(u)\,du=\int\Phi(t)f(t)dt=1.
\]

Choose fixed \(d>0\) with \(\gamma-\eta-d>1\), and \(0\le\chi\le1\) smooth, supported on \((\gamma-\eta-d,\gamma+\eta+d)\) and equal to one on \([\gamma-\eta,\gamma+\eta]\). Put \(H=x/T\). On positive overlap define the absolutely continuous measure
\[
dA_{n,h}(x)=dA^0_{n,h}(x)
\left[1+c\chi(\log x/L)\frac{\log p}{H}B(h/H)\right].
\]
The absolute size of the relative change on the support of \(\chi\) is \(O_c(L T^{-(\gamma-\eta-d-1)})=o(1)\), uniformly over these twists. The measure is positive on permitted rows for all sufficiently large \(T\). For every endpoint \(y\) the change in its cumulative weight is at most
\[
\frac{|c|s_{n,h}T\log p}{n}\int_{0}^\infty
\left|B(|h|T/x)\right|\frac{dx}{x}
\ll_c s_{n,h}\frac{T\log p}{n}.
\]

The estimate \(\sum_{1\le h\le y}s_{n,h}=y+O(1+\log(2+y))\) follows uniformly from Lemma 2.7 of Fazzari–Gerspach. Partial summation, with \(g=B K_\Phi\) even and Schwartz, gives
\[
\sum_{h\ne0}s_{n,h}g(h/H)
= H\int_\mathbb R g(u)du+O_g(1+\log(2+H))
=H+O_g(1+\log(2+H)).
\]
[Source for the singular-series estimate](https://arxiv.org/html/2412.20099v1#S2.L7)

In the linearized weight, the real phase is \(K_\Phi(h/H)\). On \(|h|\le x/2\) the pointwise error in replacing \(W\) by \(q_\alpha(x/n)q_\gamma(x)\widehat\Phi(-h/(2\pi H))/x\) is
\[
O_A\!\left(\frac{|h|}{x^2}(1+|h|/H)^{-A}\right).
\]
This follows by Taylor expansion of the logarithm and the smooth envelopes. Since \(\sum_{h\ne0}s_{n,h}|h|(1+|h|/H)^{-A}\ll H^2\), the shift-summed weight error is \(O(T^{-2})\). The perturbation multiplier is uniformly bounded here. In the comparable region the support of either envelope restricts \(x\ll T^{\gamma+\eta}\). After integration and twist summation the resulting error is \(O(T^{\gamma+\eta-2}L^{-2})=o(1)\). Outside this region the original Fourier kernel has argument of order at least \(T\), and the linearized kernel has arbitrary decay for \(|h|/H\gg T\). Polynomial support for the original packet, and partial summation for the linearized tail, give \(o(1)\).

On the linearized support \(H\ge T^{\gamma-\eta-1}\), and \(\chi=1\). Using the preceding shift average, the residual becomes
\[
\frac{c}{L^3}\sum_n\frac{\Lambda(n)\log p}{n}q_\beta(n)
\int q_\alpha(x/n)q_\gamma(x)\frac{dx}{x} +o(1).
\]
Indeed the relative kernel error from \(O(1+\log H)/H\) is uniformly small in absolute value, and the same expression with all envelopes replaced by their absolute values is \(O(1)\). Prime powers with exponent at least two contribute \(o(1)\) by their reciprocal tail. Partial summation of the prime number theorem in the variable \(v=\log p/L\) gives the limit
\[
c\iint(\beta+b)q(a)q(b)q(a+b)\,da\,db=c\beta c_\psi .
\]
The integral with the factor \(b\) vanishes by evenness.

For the integer version, write \(F(y)=A_{n,h}((0,y])\), and use the cumulative function \(F^*(y)=\lfloor F(n\lfloor y/n\rfloor)\rfloor\) on \(y\ge0\). It is increasing and \(0\le F(y)-F^*(y)\le 1+2s_{n,h}\) for large \(T\). Each atom has the required support. On a smooth dyadic block \(x\asymp X\), \(n\asymp N\), integrate by parts. The localized weight satisfies
\[
\|W\|_\infty+\|W'\|_1\ll_A X^{-1}(1+T|h|/X)^{-A}
\]
for \(|h|\le c_0X\) with a fixed small constant \(c_0\). The sum of \((1+s_{n,h})(1+T|h|/X)^{-A}\) is \(O(X/T)\). Thus the rounding changes the residual by \(O(N/(TL^3))\) per such block. Comparable shifts outside the small range have arbitrarily strong Fourier decay, as do all non-comparable contributing shifts. Their derivatives and the number of terms grow at most polynomially on packet supports. Summing the logarithmically many blocks gives \(o(1)\), since \(N\ll T^{\beta+\eta}\) and \(\beta+\eta<1\).

## Both linear forms can pass a growing small-prime sieve

The example can additionally require every occupied site \(x=nm\) to satisfy
\[
\gcd(m(nm+h),Q)=1,\qquad Q=\prod_{\ell\le z}\ell\le T^\kappa,
\qquad 0<\kappa<1-\beta-\eta .
\]
Here \(\ell\) ranges over primes. One may take \(z\) to be a sufficiently small positive constant times \(\log T\), by the prime number theorem. For \(s_{n,h}>0\), each prime permits at least one residue class for \(m\). At odd primes at most two classes are excluded. At two, positivity of \(s_{n,h}\) ensures that a class survives. By the Chinese remainder theorem and Mertens' product estimate the admissible fraction \(d=d_{n,h}(Q)\) of residues modulo \(Q\) satisfies \(d\gg (\log(2+z))^{-2}\).

On each allowed \(m\) with positive overlap put weight \(s_{n,h}/d\) times the multiplier in square brackets in the construction above, evaluated at \(x=nm\). Counting admissible residues up to an arbitrary endpoint gives \(d y+O(Q)\) for the integer argument \(m\le y\). The square-bracket multiplier has supremum and total variation \(O_c(1)\), uniformly in \(n,h\). Indeed its nonconstant derivative is bounded by \(C L T/x^2\) on \(x\ge T^{\gamma-\eta-d_0}\), where \(d_0\) is the fixed cutoff margin called \(d\) above. This uses boundedness of \(B\) and \(uB'(u)\). Partial summation on the positive overlap therefore shows that this sieve-supported cumulative measure differs from the continuous \(F(y)\) by \(O_c(s_{n,h}Q/d)\), uniformly in the endpoint. Flooring its cumulative function changes it by at most one and retains the sieve support.

Since \(Q/d\le T^{\kappa+o(1)}=o(T/n)\), the stated cumulative discrepancy bound still holds. The per-block rounding estimate becomes \(O(N Q (\log(2+z))^2/(T L^3))\), which tends to zero after summing blocks. The limiting residual is still \(c\beta c_\psi\). Each integer atom has weight at most \(1+2s_{n,h}/d\). On polynomially bounded \(n,h\) this is \((\log\log T)^{O(1)}\), since the elementary Euler product for \(s_{n,h}\) is \((\log\log(10+n|h|))^{O(1)}\). To see the last bound, split prime divisors at \(\log(10+n|h|)\), use Mertens' estimate below that point, and bound the number of larger prime divisors by \(\log(n|h|)/\log\log(10+n|h|)\).

**A larger sieve cutoff.** The period argument already gives a bound \(Q\), without dividing it by \(d\), for the discrepancy of the normalized residue count: every complete period has exactly \(dQ\) allowed sites, and the contribution and expected count of a remaining prefix both lie in \([0,Q]\) after normalization. A different elementary bound is useful for larger \(Q\). Let \(\nu_\ell\in\{1,2\}\) count the forbidden residue classes at \(\ell\) in an admissible row. Expand the product of the local indicators by inclusion–exclusion. By the Chinese remainder theorem each selected list of forbidden classes mod distinct primes gives one residue class modulo their product, whose count up to any real endpoint differs from its density times that endpoint by at most one. Thus the **unnormalized** count differs from its mean by at most \(\prod_{\ell\le z}(1+\nu_\ell)\le3^{\pi(z)}\). After normalization the cumulative error bound in the partial summation above may use \(\min\{Q,3^{\pi(z)}/d\}\) in place of \(Q/d\). In particular for every fixed \(K>0\) we may use \(z=K\log T\): then \(3^{\pi(z)}/d=T^{o(1)}\), regardless of the exponent of the resulting primorial. This extension still uses separately assigned rows, with no common prime weights.

## Scope of the obstruction

At the central scales \(n=T^{1/5}\) and \(X=T^{7/5}\) the critical factor is \(T/n=X^{4/7}\). Standard Euler-factor bounds give \(s_{n,h}\ll_\varepsilon (n|h|)^\varepsilon\) on nonzero shifts. Thus the cumulative error stays within \((T/n)T^\varepsilon\) throughout polynomially bounded packet ranges. On a packet of fixed positive width the precise comparator is \(T/n\) on each twist block. A uniform \(X^{4/7+o(1)}\) for every edge block would require a separate bandwidth analysis.

The displayed construction is a family indexed by \(T\). A single system of measures also realizes the limits along any prescribed sufficiently lacunary sequence of heights whose twist intervals are disjoint. Assign the construction at \(T_j\) to the twists in its interval and use the reference measure on remaining twists. Only assigned twists contribute at each \(T_j\). A global integer version can use the rounded reference measure on the remaining rows. This last statement controls the specified subsequence, not all intermediate heights for that same system.

The example isolates which information discarded by a magnitude estimate could matter. The same \(\Lambda\) values must determine the weights at every twist and shift for actual prime pairs. Our measures assign these weights row by row. They establish a limitation on deductions from the listed size and positivity constraints. The signed discrepancy of the actual primes remains open.

[Exact finite sieve checks](check_sieve_rows.py) and their [receipt](sieve_checks.json) test the residue densities, floor support and primitive bounds for both shift signs. They use a rational test multiplier, not actual primes or a numerical certification of the limiting residual.
