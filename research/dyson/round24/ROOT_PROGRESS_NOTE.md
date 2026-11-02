# Round 24 working note: actual arithmetic and a closed kernel search

This is a work-in-progress record after the published Round 23 checkpoint 8015c4b4d009628cd355b64f53372f4db6f63a50. It preserves mathematical questions, explicit deductions and review status, not a claim of a strict zeta estimate.

## The additional divisibility constraint

In the R23 nonprimitive term, root identified a restriction not used by the earlier coarse estimate: a nonzero prime-power endpoint \(n=p^j\) forces \(p\mid h\), as well as divisibility of the chosen modulus. With \(d\le Q<X<n<3X\), one has \(j\ge2\) and \(p\le\sqrt{3X}\). In the upper window \(H=X/T\), \(11/5\le\alpha\le9/4\), the ratio \(H/\sqrt X\) tends to infinity.

Therefore only \(O(H/p)\) physical even shifts occur for each base, instead of \(O(H)\). There are at most two powers of any odd base in the fixed-ratio interval. After collecting actual divisors of \(m=n-h\), their absolute logarithmic coefficient is at most \(\tau(m)\log(2X)\). Chebyshev partial summation supplies
\[
\sum_{p\le Y}\frac{\log p}{p}\ll\log(2Y).
\]
Together with the unchanged weight \(O(1/(X\log^2T))\), this suggests and gives the direct bound
\[
|\mathcal N_{\mathcal D}|\ll_\eta X^\eta/T
\]
for any odd divisor subset below \(Q<X\), without the R23 owner-largest-prime guard. Root, Aquinas and Plato have independently checked this deduction in ordinary algebra; Aquinas's standalone manuscript and Plato's pinned review are being finalized. At \(\eta=1/100\) the uniform exponent is \(-391/900\). No prime-height scan is needed.

The same restriction improves the raw nonprimitive part after switching the complementary divisor to a small cofactor \(k\). The initially obtained \(X^{-91/900}\) coarse bound remains a valid fallback; \(p\mid h\) supplies the stronger \(X^\eta/T\) estimate.

## The exact remaining arithmetic, and a failed source application

Euclid's written small-cofactor draft, SHA256 c16cc2a52328ca673bcd97db2221235a7a61b7e40a6dff19caa85c4cb3bd4c73, has been read in full by root and is assigned an independent full review. It keeps the exact complement
\[
2\sum_{3\le k<2X/Q,\ k\ {\rm odd}}\log k
\sum_{d>Q,\ d\ {\rm odd}}\mu(d)
\sum_{h\ {\rm even}}F(kd,h)\Lambda(kd+h).
\]
There is no added coprimality between \(k\) and \(d\). The actual primitive density center is \(2k/\varphi(k)\). Its complete added-back main is retained, and physical-shift completion replaces that main by its continuous-shift integral with error \(O((K/H)\log^3X)\).

The remaining signed expression is the old primitive principal plus a Möbius-linear main plus the centered Möbius–prime covariance minus both singular-series marginals. It is not estimated at the \(O(1)\) fluctuation scale.

Root read the entire draft's ordinary estimates. In addition, root independently opened the author-hosted [Carneiro–Chandee–Chirre–Milinovich paper](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf) and checked printed page 1 equations (1.1) and (1.3). The fixed exponent three is inside the stated RH Selberg range. The draft's real-to-integer endpoint comparison and coefficient second moment lead to \(O(\sqrt H\log^{3/2}X)\), which is a valid candidate bound but still grows. Final independent source/derivation acceptance remains the reviewer's responsibility.

The one-prime distribution theorem cannot simply accept \(\mu((n-h)/k)\) as a smooth weight. On the odd grid, squarefree \(d\equiv11\pmod{18}\) have \(|\mu(d)|=1\) and \(\mu(d-2)=0\), giving variation of order the interval length. This rejects that literal weighted-partial-summation application, not every conceivable equivalent coefficient representation or a joint dispersion theorem.

The packet's leading mass is of order \(H/\log^2X\), so a relative \(o(1)\) approximation is not a fluctuation-scale estimate. Even the illustrative relative size \(X^{-1/2}\log^2X\) gives an absolute budget \(H/\sqrt X\), with exponent between \(1/22\) and \(1/18\). The draft correctly keeps those large main terms until their joint cancellation can be proved.

## Exact zero margins: a useful negative conclusion

Root's one/two-profile theorem, SHA256 818f0ac7b2952fd05fde28762079aeb94d23c72fbe8171e3298cedeb935bb60c, has full Plato and coordinator reviews. Plato's finite compact-window extension, SHA256 c857d22a766099049bcdc95cdb12bf876d87deb6d83f9e9654c154d4dc2a6a7d, has been read fully by root and independently accepted by the coordinator.

At one exponent the exact kernel is \(c(m)n^{-t}\), and its positive singular-series row mass makes a zero row impossible unless \(c(m)=0\). For two arbitrary row-dependent profiles, a strictly monotone ratio of row masses and induction through the first available column force the same conclusion.

For finitely many compact-window profiles, each row coefficient is eventually constant. The exact row asymptotic first forces these constants to vanish. The remaining finite translate combinations of the actual singular series have rational-frequency mean
\[
\frac{2}{(q-1)^2}e(-al/q)
\]
for odd prime \(q\) and all \(a=1,\ldots,q-1\). An absolutely controlled divisor tail justifies this limit. Vanishing at all these roots forces the coefficient polynomial to be zero, including arbitrary complex coefficients. A subpower bound for the singular series separates every distinct exponent, however close.

This closes the exact-zero-margin search over finite compact lower-window combinations with untruncated Pareto tails. It does not rule out a separate upper-endpoint cutoff, approximate margins, arbitrary growing coefficients with three profiles, or a general arithmetic method. No larger search in the excluded family will be launched. The original finite checkerboard identity remains correct; its comparison to the actual positive deficit remains missing.

## Next obligation

Complete the pinned reviews of the actual nonprimitive and small-cofactor estimates, then seek an estimate of the joint signed arithmetic expression. Do not re-open the closed exact-profile search, discard principal terms using only a relative asymptotic, or claim that a covariance lower bound proves the required upper bound. The strict target is still \(\liminf Q_{2,T}<A-M\); \(\le1-M\) is only a stronger sufficient benchmark.
