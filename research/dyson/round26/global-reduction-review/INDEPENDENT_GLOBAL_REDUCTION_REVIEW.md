# Independent ordinary-proof review of the full scale-dependent arithmetic reduction

Date: 2026-09-05. Reviewer: Plato, independent of author Euclid and of Aquinas's separate singular-correction derivation.

**Decision: accepted as an ordinary mathematical proof under ordinary RH, with the precise global statistic and scope stated in the manuscript.** The full mathematical audit, source checks, final provenance verification and unchanged tiny-check replay are complete. No amendment remains requested.

The object reviewed is [FULL_SHIFT_REDUCTION.md](../full-shift-reduction/FULL_SHIFT_REDUCTION.md). This review accepts only an ordinary-RH reduction of the actual full parity-adjusted statistic to the explicitly defined finite covariance plus the constant \(M_1\). It does not establish a sign for that covariance, a strict actual-zeta variance bound, or an AH refutation.

The frozen author file is 22,834 bytes, SHA256:

    c0d413f2eead98cfc97de09cd5b4f8ffaa0df7a6b81249df576ccff61a0cadd6

Its AUTHOR_RECEIPT.json is SHA256:

    ee739ec077a190962f89f0990c32b5936fc244fc632ad928aa06c6310698cd73

During review I supplied the direct \(K2^{-T}\) small-shift tail argument, distinguishing it from the looser full-shift tail. The author inserted that argument before freeze without changing a displayed formula. I reread the final insertion. No author or earlier-round file was edited by the reviewer.

## 1. What must be proved beyond R25

The frozen R25 theorem treated one fixed compact packet. Its remainder could not simply be summed over a growing number of height and length packets. In particular its coarse singular-series transform hid a term of size \(\int F/h\) which accumulates to a nonzero constant.

The new proof instead starts with the exact full expression
\[
\mathcal Q_{2,T}=2\sum_{\substack{m\ {\rm odd}\\h\ge2,\ h\ {\rm even}}}
b_T(m)\left(\frac m{m+h}\right)^T
\{\Lambda(m)\Lambda(m+h)-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\}.
\]
Every \(\Lambda(p^a)=\log p\) is retained. It separately bounds the discarded small shifts, the infinite upper shift tail, and the infinite height tail. It specifies the remaining finite partition, derives uniform derivatives for its moving cutoffs, pays every scale-dependent divisor error, and evaluates the refined singular-series correction. These are necessary new obligations, and the manuscript addresses each one.

Write
\[
M_0=\int\omega(u)\,du,\qquad M_1=\int(u-1)\omega(u)\,du.
\]
The proved conclusion is \(\mathcal Q_{2,T}=\mathcal Z_T+M_1+o(1)\). The separately established R21/R22 identity contributes the original diagonal \(M_0\). Thus the actual variance has constant \(M_0+M_1\), equal to \(2M\) for the fixed symmetric bump. The new \(M_1\) is not a second notation for a diagonal that was already included.

## 2. Exact partition, finite support and uniform derivatives

The cutoff is a fixed smooth nonincreasing \(r\), equal to one on \([0,1]\) and zero on \([2,\infty)\). Thus \(\beta(t)=r(t)-r(2t)\) is nonnegative, supported in \((1/2,2)\). With
\[
X_i=2^iL,\quad Y_j=2^jY_0,\quad
Y_0=\sqrt{\ell},\quad R=32\ell,\quad Q_j=Y_j^{2/3},
\]
the packet is exactly
\[
F_{ij}(m,h)=b_T(m)\beta(m/X_i)\beta(h/Y_j)
r(m/(2U))r(Th/(Rm))(1+h/m)^{-T}.
\]
The lower shift cutoff is contained in the sum of the \(\beta(h/Y_j)\)'s, not silently supplied by another factor in \(\mathcal Z_T\).

Telescoping at finite upper index and then taking its limit proves
\[
\sum_{i\ge0}\beta(m/X_i)=1-r(2m/L),\qquad
\sum_{j\ge0}\beta(h/Y_j)=1-r(2h/Y_0).
\]
Since \(b_T(m)=0\) for \(m\le L\), the first sum equals one everywhere needed. Nonzero packets obey
\[
X_i<8U,\qquad Y_j<8RX_i/T,\qquad
m\asymp X_i,\quad h\asymp Y_j,\quad h/m=O(\ell/T).
\]
There are \(O(\ell)\) height bins and \(O(\ell)\) length bins per height. The small endpoint inflation \(X_i\le8U\), rather than \(X_i\le U\), is retained. Constants arising from it do not change any power exponent.

Let \(X=X_i,Y=Y_j,A=(X\ell^2)^{-1}\). The exact integral
\[
b_T(m)=\frac{T}{m\ell^2}\int_0^1
\omega((\log m+\log u)/\ell)u^{T-2}\,du
\]
proves \(b_T^{(a)}(m)\ll_a m^{-1-a}\ell^{-2}\). The mass \(1/(T-1)\) prevents powers of \(T\) from appearing on differentiation.

For the Pareto factor put \(s=Th/m\). Its support has \(s\le2R=o(T)\). Each fixed derivative, multiplied by the corresponding \(X\)- and \(Y\)-scale factors, is bounded by a fixed polynomial in \(s\) times \(e^{-cs}\). This product has a uniform bound even though the largest allowed \(Y/(X/T)\) grows logarithmically. Derivatives of \(r(Th/(Rm))\) introduce only powers of its bounded transition argument. Derivatives of \(r(m/(2U))\) are also uniform because \(X/U<8\) on its support.

It follows that
\[
|\partial_m^a\partial_h^bF_{ij}|\ll_{a,b}AX^{-a}Y^{-b}
\]
for each fixed pair of orders. All cutoffs are smooth at their boundaries. The constants do not grow with \(\ell\).

At fixed \(n=m+h\), differentiation in \(h\) is \(\partial_h-\partial_m\). Since \(Y/X=o(1)\), it preserves the \(Y\)-scale bound. Differentiation in \(n\) under a continuous \(h\) integral is instead \(\partial_m\), so \(J_+\) and \(I_+\) retain derivative scale \(X\). Freezing the shifted endpoint or charging an \(Y^{-1}\) derivative in the latter step would be incorrect; neither occurs here.

Finally \(Q=Y^{2/3}<X/2\) uniformly for all nonzero packets when \(T\) is large, including the top bins. Thus every divisor logarithm is evaluated at a positive cofactor and the nonprimitive prime-power arguments apply in the enlarged support.

## 3. Direct removal of small shifts for the correct coefficient

The coefficient now used is \(q_2\), so a bound for the earlier \(a_ma_{m+h}-c_h\) cannot be cited without checking the change. The manuscript uses the valid inequality
\[
|q_2(m,h)|\le\Lambda(m)\Lambda(m+h)
+\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)+2]
\]
on the retained odd/even rows.

The reviewed R22 upper-sieve input is uniform in \(1\le h\le X\):
\[
\sum_{X<m\le2X}\Lambda(m)\Lambda(m+h)
\ll X\mathfrak S(h)+\sqrt X\log^3X.
\]
The uniformity is derived from actual residue counts, not extrapolated from a fixed-pattern theorem. For even \(h\), the local forbidden-class count is one at primes dividing \(h\) and two otherwise; the CRT remainder is \(O(\nu_h(d))\), with \(\nu_h(d)\le\tau(d)\). The dimension-two axiom has one constant for all \(h\), and the source's fundamental upper sieve with a fixed sufficiently large sifting ratio supplies the estimate. Genuine prime pairs survive; pairs containing a higher prime power are separately charged by \(O(\sqrt X\log^3X)\).

I reread the retained primary [Tao sieve notes](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/), equation (22), Lemma 17 and Corollary 19. These provide the required uniform-dimension version. The fixed-pattern threshold of Theorem 32 is not the input.

Together with \(\sum_{h\le K}\mathfrak S(h)\le K\) and Chebyshev, one block contributes
\[
O(K/\ell^2+KX^{-1/2}\ell).
\]
The first part sums over \(O(\ell)\) height bins; the second is geometric from \(L\). Hence the retained-height total is \(O(K/\ell+K\ell L^{-1/2})\).

For completeness, the sharper \(K2^{-T}\) tail in (14) follows directly rather than from the looser all-shift bound (15). If \(m>2U\), \(h\le K\le L\), then \(m+h<2m\). The positive coefficient majorant sums to \(O(K\log^2(2m))\). Insert the exact tail
\[
b_T(m)\ll U^{T-1}m^{-T}/\ell^2
\]
and compare the decreasing sum with its integral plus the first integer term. Since \(2U\ge T\), the endpoint is harmless and the result is \(O(K2^{-T})\).

The missing lower cutoff has support \(h<Y_0\). Taking \(K=\lceil Y_0\rceil\) makes its complete absolute contribution \(O(\ell^{-1/2})\). Nonnegativity of the weights allows arbitrary subsets and fractional smooth subweights in this range. No signed cancellation is assumed.

## 4. The two infinite tails and their real endpoints

For the full height tail \(m>2U\), the positive majorant for the shift sum is
\[
\sum_{h\ge1}k(m,h)|q_2(m,h)|
\ll (m/T)\log^2(2m).
\]
Here \(k(m,h)\log^2(2(m+h))\) is decreasing for large \(T\) and \(m\ge L\). Integer integral comparison handles its unweighted sum. Stieltjes partial summation with the exact inequality \(\sum_{h\le y}\mathfrak S(h)\le y\) handles its singular-series weighted sum. Direct integration after \(1+h/m=t\) gives the stated scale.

The remaining \(m\)-sum uses \(U^{T-1}m^{1-T}\log^2(2m)/(\ell^2T)\). Its integral and first possible integer term are both bounded by the deliberately loose \(O(U2^{-T})\). This proves absolute convergence and validates deletion of the height cutoff transition only where \(m>2U\).

For the upper shift tail \(h>a=Rm/T\), partial summation must preserve the finite lower endpoint. The valid positive upper bound is
\[
a\,g(a)+\int_a^\infty g(y)\,dy,
\qquad g(y)=k(m,y)\log^2(2(m+y)).
\]
The author retains this \(a g(a)\) term. Since \(R/T\to0\), the tail is
\[
O((Rm/T)\log^2(2m)e^{-R/4}).
\]
The unweighted first lattice term has the same bound because \(a\gg1\) throughout the window. After multiplication by \(b_T\) and summing \(m\le4U\), the total is
\[
O(RUe^{-R/4}/T)=O(\ell T^{-27/4}).
\]
This includes the smooth transition interval, where \(1-r(Th/(Rm))\) need not be an indicator. No sharp cutoff is differentiated. These estimates establish the finite-packet decomposition of the original absolutely convergent statistic with \(O(\ell^{-1/2})\) error.

## 5. The refined source formula and its exact real extension

The new source input is [Montgomery–Soundararajan, arXiv:math/0409258v1](https://arxiv.org/pdf/math/0409258v1), printed page 16, equation (47), where the estimate is credited to Goldston:
\[
2\sum_{h=1}^N(N-h)\mathfrak S(h)
=N^2-N\log N+B N+O_\nu(N^{1/2+\nu})
\]
for integer \(N\). This is an unconditional statement about the singular series. It imports no conditional prime-pair correlation assumption from elsewhere in the paper.

The real hinge \(B_{\mathfrak S}(y)=\sum_h(y-h)_+\mathfrak S(h)\) is exactly piecewise linear between integer arguments. Interpolating the two endpoint remainders preserves \(O_\nu(y^{1/2+\nu})\). The smooth main \(y^2-y\log y+B y\) differs from its interpolation by \(O(1)\), since its second derivative is bounded for \(y\ge1\). This is the necessary stronger real-endpoint argument; a crude \(O(y)\) extension would lose the summable remainder.

For a smooth packet in \(h\in(Y/2,2Y)\), the exact hinge identity and two integrations by parts yield
\[
\sum_{h\ {\rm even}}\mathfrak S(h)f(h)
=\int f(h)\,dh-\frac12\int\frac{f(h)}h\,dh
+O_\nu(A_fY^{-1/2+\nu}).
\]
The sum is already over all nonzero singular-series values, so no further parity factor is inserted. The quadratic main gives \(\int f\), the logarithmic main gives the negative coefficient \(-1/2\), and the linear main vanishes. The remainder is paired with \(f''\); no derivative estimate for that remainder is asserted.

All support endpoints are separated from zero for each packet, and \(Y_0\to\infty\). With \(\nu=1/4\), summation against either prime marginal or the integer baseline yields a per-packet remainder \(O(\ell^{-2}Y^{-1/4})\), which is summable.

I also read Aquinas's complete separate [REFINED_SINGULAR_CORRECTION.md](../singular-correction-review/REFINED_SINGULAR_CORRECTION.md). Its independent real interpolation, sign computation, both-marginal normalization, uniform derivative argument and exact continuum moments agree with the derivation above. That companion does not purport to prove the divisor-error portion of the global theorem.

## 6. Re-derivation of the variable-scale arithmetic errors

The finite primitive/principal/nonprimitive partition is unchanged from the fully reviewed R25 algebra, but none of its old fixed-power uniformity is presumed. Here \(Q=Y^{2/3}\) can be only \(\ell^{1/3}\) at the smallest shift scale.

For the primitive discrepancy, the normalized Fourier coefficients of one period are at most \(2/d\), by period \(\ell^1\) norm at most two. Smooth Poisson completion at order 16 therefore gives
\[
|\mathcal B_Q|\ll Q(Q/Y)^{16}/\log X
=Y^{-14/3}/\log X.
\]
For a nonprimitive row the genuine endpoint is \(n=p^a\), \(a\ge2\), with \(p\mid h\). On \((Y/2,2Y)\), writing \(h=2pr\) gives \(O(Y/p)\) possibilities, including the empty range \(p>Y\). The support ratio of the \(n\)-interval is fixed, so there are \(O(1)\) possible powers per prime. Keeping the \(\log p\) weight and summing the divisor coefficient once gives \(O_\eta(X^\eta Y/X)\). No comparison \(Y\gg\sqrt X\) or owner-family restriction is used.

The principal \(h\)-mask is expanded over \(s\mid d\). Completing at fixed order 36, multiplying by \(1/\varphi(d)\), and using \(\sum_{d\le Q}\tau(d)^2/d\ll\log^4(2Q)\) gives
\[
O((Q/Y)^{36}\log^3X)=O(Y^{-12}\log^3X).
\]
This higher order is needed at polylogarithmic \(Y\); the order-one R25 estimate could not be summed here. Its true mean is still \(\varphi(d)/(2d)\), so the original leading factor two leaves \(\mu(d)/d\). Removing the remaining nonunit \(n\)-mask is a separate higher-prime-power debt \(O(Y\log X/X)\), not a redefinition of the principal.

The exact flat center is completed only on the even lattice, at fixed order four. Since \(\sum_{m\asymp X}|c_Q(m)|\ll X\log^2X\), this costs \(O(Y^{-4})\). No primitive complementary-cofactor mask is introduced, and no \(X/Q<Y\) condition is needed.

Completing the odd cofactor \(m=dr\) at scale \(X/d\), with two derivatives and its genuine \(d/X\) saving, costs
\[
O(YQ^2/(X^2\log X))=O(Y^{7/3}/(X^2\log X)).
\]
Real sharp \(Q\) is retained in this finite identity.

Ordinary RH gives the odd Möbius tail
\[
a_Q(m)=2+e_Q(m),\quad
e_Q(m)\ll Q^{-1/2+\epsilon}\log X,\quad
e_Q'(m)\ll Q^{-1/2+\epsilon}/X.
\]
The Euler-product derivative at \(s=1\) is \(+2\); its logarithm-weighted Möbius series has sum \(-2\). Ordinary odd Möbius control follows from the exact finite identity \(M_{\rm odd}(y)=\sum_{a\ge0}M(y/2^a)\). The [Soundararajan primary](https://arxiv.org/pdf/0705.0723v2), printed page 1, equation (1), supplies this ordinary-RH bound without GRH.

The displayed upper bound for \(e_Q\) need not itself tend to zero when \(Q\) is only polylogarithmic. The proof does not require that. It combines the principal and flat-center terms first, producing the exact centered singleton
\[
\sum_{n\ {\rm odd}}\Lambda(n)G(n)-\int G,\qquad
G(n)=\int F(n-h,h)e_Q(n-h)\,dh.
\]
Schoenfeld's ordinary-RH bound for \(\Psi-x\), equation (6.2), after explicitly removing powers of two, gives
\[
O\!\left(\frac{Y}{\sqrt X}Q^{-1/2+\epsilon}\log X\right)
=O(Y^{101/150}\log X/\sqrt X)
\]
at \(\epsilon=1/100\). Its derivative norm is taken at fixed \(h\), on scale \(X\). There is no estimate of the potentially large uncentered Möbius error by itself.

Finally the refined singular transform costs \(O(\ell^{-2}Y^{-1/4})\), and completing the large continuous baseline on the odd height lattice costs \(O(Y/(X^2\ell^2))\). These are exactly the nine entries of the local error ledger; no extra source-distribution estimate is invoked.

## 7. All nine errors really sum

For each height, negative powers of \(Y\) sum geometrically from \(Y_0\); positive powers sum from the maximum \(O(RX/T)\). Summation of the local bounds gives:

| Local error | Total over the actual finite partition |
| --- | --- |
| \(Y^{-14/3}/\log X\) | \(O(\ell^{-7/3})\) |
| \(X^{1/100}Y/X\) | \(O(R\ell U^{1/100}/T)\) |
| \(Y^{-12}\log^3X\) | \(O(\ell^4Y_0^{-12})=O(\ell^{-2})\) |
| \(Y\log X/X\) | \(O(R\ell^2/T)\) |
| \(Y^{-4}\) | \(O(\ell Y_0^{-4})=O(\ell^{-1})\) |
| \(Y^{7/3}/(X^2\log X)\) | \(O(R^{7/3}T^{-19/12}/\ell)\) |
| \(Y^{101/150}\log X/\sqrt X\) | \(O(R^{101/150}\ell T^{-17/60})\) |
| \(\ell^{-2}Y^{-1/4}\) | \(O(\ell^{-9/8})\) |
| \(Y/(X^2\ell^2)\) | \(O(R/(TL\ell^2))\) |

In the sixth row the height dependence is \(X^{1/3}\), so its sum is geometric from the top, giving \(U^{1/3}/T^{7/3}=T^{-19/12}\). In the seventh it is \(X^{13/75}\), giving \(U^{13/75}/T^{101/150}=T^{-17/60}\). The final row is geometric from \(L\). The deliberately loose second and fourth rows may retain an \(O(\ell)\) height count and still decay by a fixed power of \(T\).

Thus the aggregate of these nine errors is \(O(\ell^{-1})\). The derivative orders 16, 36 and 4 remain fixed and have uniform seminorms by Section 2; no logarithmic cost was hidden in an implicit constant.

## 8. Both singular marginals leave precisely one positive continuum correction

Define \(I_-(m)=\int F(m,h)\,dh/h\) and \(I_+(n)=\int F(n-h,h)\,dh/h\). The sign from subtracting the singular-series term is
\[
D(F)=\sum_{m\ {\rm odd}}\Lambda(m)I_-(m)
+\sum_{n\ {\rm odd}}\Lambda(n)I_+(n)
-2\sum_{m\ {\rm odd}}I_-(m).
\]
It is positive in its leading continuum approximation. Each \(I_\pm\) has amplitude \(O((X\ell^2)^{-1})\), variation of that order, and derivative scale \(X\). Ordinary RH therefore replaces each prime marginal with its continuous integral at cost \(O(X^{-1/2})\). The odd integer term has density \(1/2\), so its prefactor two produces one continuous integral, which is subtracted.

The exact change \(n=m+h\) gives \(\int I_+=\int I_-\). Consequently
\[
D(F)=\iint F(m,h)\frac{dh\,dm}{h}+O(X^{-1/2}),
\]
with coefficient \(+1\), not \(+2\) or \(-1\). The total replacement error is \(O(\ell\sum_iX_i^{-1/2})=O(\ell L^{-1/2})\).

Summing the continuum terms by the exact partition gives
\[
\mathcal I_T=\iint b_T(m)r(m/(2U))k(m,h)r(Th/(Rm))
[1-r(2h/Y_0)]\,\frac{dh\,dm}{h}.
\]
Nonnegativity makes this finite partition and integral interchange direct. The original covariance sum telescopes to the author's explicit finite \(\mathcal Z_T\); the scale-dependent divisor cutoff remains inside its \(j\)-sum.

## 9. Independent calculation of the nonzero constant

Put \(H_m=m/T\), \(\delta=Y_0/H_m\), and \(z=h/H_m\). Uniformly on \(L\le m\le4U\), \(\delta\to0\). The inner integral equals
\[
\int_0^\infty r(z/R)(1+z/T)^{-T}
[1-r(2z/\delta)]\,\frac{dz}{z}
=\log(1/\delta)+O(1).
\]
The transition \([\delta/2,\delta]\) costs at most \(\log2\). On \([\delta,1]\), \(0\le1-(1+z/T)^{-T}\le z\), so comparison with \(1/z\) is uniformly integrable. Beyond one, the actual Pareto factor has a bounded integral against \(dz/z\); on the cutoff support it is at most \(e^{-z/2}\). This exponential is only a majorant, not a replacement kernel.

The author's uniform approximation
\[
b_T(m)=W_T(m)/(m\ell^2)+O(1/(mT\ell^2))
\]
follows from the exact \(u\)-integral and the mean-value theorem: \(\int_0^1|\log u|u^{T-2}du=(T-1)^{-2}\). The factor \(T/(T-1)\) contributes the remaining \(O(T^{-1})\) relative error. This remains valid just above \(U\), where \(W_T(m)=0\); the smooth weight is extended by zero. Integrated against the \(O(\ell)\) inner factor over a logarithmic height interval of length \(O(\ell)\), the error is \(O(T^{-1})\).

An independent check, also written by Aquinas, avoids this pointwise approximation. Exact Tonelli integration yields
\[
\int_1^\infty b_T(m)\,dm=\frac{T}{T-1}\frac{M_0}{\ell},
\]
\[
\int_1^\infty b_T(m)\log m\,dm
=\frac{T}{T-1}\int u\omega(u)\,du
+\frac{T}{(T-1)^2\ell}M_0.
\]
Removing the height cutoff from these moments costs only an exponentially small tail above \(2U\). Both calculations give
\[
\mathcal I_T=M_1-\frac{\log Y_0}{\ell}M_0+O(\ell^{-1}+T^{-1})
=M_1+O(\log\ell/\ell).
\]
Combining this with the absolute small-shift error and all summed arithmetic errors proves the claimed \(O(\ell^{-1/2})\) remainder in
\[
\mathcal Q_{2,T}=\mathcal Z_T+M_1+O(\ell^{-1/2}).
\]
For an even bump centered at \(u=2\), \(\int(u-2)\omega(u)\,du=0\), hence \(M_1=M_0=M\) exactly. The original variance reduction then gives \(\overline V_T=\mathcal Z_T+2M+o(1)\). No decimal evaluation is needed for this constant identity.

## 10. Scope of acceptance and remaining mathematics

The result is an actual arithmetic reduction, with a finite explicit covariance retaining the true \(\Lambda\), every prime power, the sharp per-scale Möbius cutoff, the flat parity center and all smooth transitions. It is stronger in coverage than the fixed-packet R25 reduction, because the global tails and the growing packet count have now been paid.

It gives no strict estimate for \(\mathcal Z_T\). The sufficient condition \(\liminf\overline V_T\le1\) becomes exactly \(\liminf\mathcal Z_T\le1-2M\). A convergence claim for this covariance cannot be inferred from the algebra or from generic coefficient cancellation. The stated AH and GUE values are model predictions carried through the proved identity, not estimates for the actual primes.

The only RH inputs are ordinary Möbius partial sums, the centered full-prime-power prefix estimates, and the separately proved transfer to the actual variance. The singular-series estimate and sieve bound are unconditional. No GRH, phase-twisted Siegel–Walfisz condition, growing-wheel hypothesis or 186 two-prime distribution statement enters.

## 11. Final source and reproduction receipt

I checked all 16 source/dependency entries in the author's source manifest and all six author-artifact entries in its receipt against the actual bytes. I additionally verified all six entries in the correction companion's author receipt. All 28 recorded comparisons pass. The retained primary Tao HTML/text files, whose relevant theorem ranges I reread, are additionally hash-pinned by this review.

The independently read correction companion is 14,577 bytes, SHA256:

    b6a6211db21df5e5d10031027863eb4764bdab820f60ab4befb63c8dc9caeffe

Its AUTHOR_RECEIPT.json is SHA256:

    ad06787e4fe1c8b32d2904266cd15368531aeee0cc5f5059680d3c1281908390

I read the final global checker in full, then copied only that checker and the frozen manuscript to a temporary directory and ran it with Python 3.14.3. All seven groups and 2,793 exact scalar cases pass. Both the independent JSON and captured stdout are byte-identical to the author outputs, SHA256:

    d7d96a46517180436340b9bef8e84dc55d60a675b0ee0470736d3d11ba4ccfa5

The groups contain 2,304 finite telescoping/nonnegativity checks, 256 exact lower-profile cover checks, 15 polynomial integration-by-parts checks, 200 real atomic-hinge interpolation checks, three correction-coefficient checks, five symmetry examples and ten exact summed-error exponents. The auxiliary polynomial cutoff is used only for finite telescoping tests; it is explicitly not substituted for the theorem's smooth cutoff with all derivative orders. The correction companion's checker was not rerun as part of this global review; acceptance of that companion here is by the full ordinary proof read and verified source pins.

The complete records are [source_and_replay_checks.json](source_and_replay_checks.json), [independent_exact_check_results.json](independent_exact_check_results.json) and [independent_exact_check_stdout.log](independent_exact_check_stdout.log). No prime heights, numerical asymptotic experiment or parameter scan was run. The tiny finite checks verify algebra and arithmetic of exponents; they do not replace the ordinary proof of convergence, uniformity, RH transfer or any currently unproved covariance bound.
