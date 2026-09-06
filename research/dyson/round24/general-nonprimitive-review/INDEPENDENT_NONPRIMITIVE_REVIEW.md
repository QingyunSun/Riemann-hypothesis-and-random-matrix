# Independent review of the general nonprimitive packet estimate

Reviewer: Plato / residual_gram, 2026-09-05. Status: **ordinary mathematical proof accepted; no amendment requested**. The accompanying receipt records the final author-file and dependency checks. This review is independent of Aquinas's author lane. Before seeing the draft, I separately derived the key physical-shift count and sent it to the author; the author explicitly incorporated that simplification.

Reviewed report: [GENERAL_NONPRIMITIVE_BOUND.md](../general-nonprimitive/GENERAL_NONPRIMITIVE_BOUND.md), 9,934 bytes, SHA256 `fd76f0bb6915dbad962f4e74a9fa31de5e3b9d79f26572fa8b6fea400e9d6a02`. The complete mathematical text was read. No prime-height calculation, divisor-family enumeration, or asymptotic numerical test was needed.

## 1. Accepted statement and uniformity

The report proves, for every fixed \(\eta>0\),

\[
|\mathcal N_{\mathcal D}|\ll_{\eta,\omega,\chi,V}X^\eta/T
\]

uniformly for \(T\geq4\), \(X=T^\alpha\), \(11/5\leq\alpha\leq9/4\), and any set of distinct odd positive integers \(d\leq Q=X^{523/1000}\). The coefficient is the original \(\mu(d)\), so nonsquarefree integers contribute zero. Dependence of the set on the parameters does not affect the proof: no derivative of the family or statistical model for it is used.

With the fixed choice \(\eta=1/100\), the decay exponent is \(391/900\). The estimate requires neither the earlier owner constraints nor a bound on the largest prime factor of \(d\). It uses no progression theorem, PNT, or RH. This is an unconditional bound on the actual nonprimitive term, including all higher prime powers.

The assertion for every \(\eta>0\) is an upper-bound family, not a claim that every possible large choice of \(\eta\) yields decay. The displayed fixed choice gives the stated \(o(1)\) conclusion.

## 2. Real support and the continuum window

The physical cutoffs give exactly

\[
X<m=n-h<2X,\qquad H<h<2H,\qquad
X<n<2X+2H\leq(5/2)X<3X.
\]

The weak upper bound uses \(T\geq4\); all the actual cutoff endpoints are open. The original real continuum integral defining \(b_T\) is retained. In particular the argument does not replace \(b_T(m)\) by zero for \(m>U\), which would be incorrect.

Integrating the positive constant majorant for \(\omega\) gives

\[
0\leq b_T(m)\leq
\frac{T\|\omega\|_\infty}{(T-1)m(\log T)^2}.
\]

The Pareto factor is at most one because the shift is positive. Thus \(|F_T(m,h)|\ll1/(X\ell^2)\) on the entire physical support, including rows above the continuum-window endpoint. The cutoffs need not be nonnegative for this absolute estimate; their fixed supremum norms suffice. All sums used in the packet proof are finite. There is no omitted infinite endpoint tail.

The logarithmic cofactor is evaluated only on that support. Since \(d\leq Q<X<m\), its argument is positive and greater than one. No value is needed at an excluded nonpositive lower endpoint.

## 3. The actual nonprimitive condition forces a prime-power shift

For a nonzero summand, write \(n=p^j\) using \(\Lambda(n)\neq0\). Every prime dividing \((h,d)\) divides \(n\), because \(d\mid n-h\). Since \(n\) has only one prime factor, that prime must be \(p\). Therefore \(p\mid d\) and \(p\mid h\).

The upper endpoint is odd, so \(p\) is odd. Also \(j=1\) is impossible: it would give \(p=n>X>d\), contrary to \(p\mid d\). Hence \(j\geq2\) and \(p<\sqrt{3X}\). This is a deterministic support argument; it does not discard any prime powers or appeal to their approximate density.

The crucial improvement over the earlier R23 bound is to keep \(p\mid h\) when summing the shifts. Odd \(p\) and even positive \(h\) imply \(h=2pr\) for a positive integer \(r\). From \(h<2H\) one gets \(0<r<H/p\), and therefore

\[
\#\{h\in2\mathbb Z:H<h<2H,\ p\mid h\}\leq H/p.
\]

This inequality is valid at arbitrary real endpoints. It has no rounding remainder: if \(H/p\) is an integer, the last endpoint is excluded; otherwise the number of positive integers below it is still at most \(H/p\). When \(p\geq H\), the count is zero. Discarding the lower inequality \(h>H\) only enlarges the counted set.

The displayed auxiliary margin \(H/\sqrt{3X}\geq X^{1/22}/\sqrt3\) is correct, but is not required once the exact count above is used. The author correctly presents it only as a cross-check, not as an unproved substitute for endpoint control.

## 4. Divisor aggregation and every logarithmic factor

For each fixed \(n,h\), summation over the distinct divisors can first be bounded absolutely by

\[
\sum_{\substack{d\in\mathcal D\\d\mid m}}
|\mu(d)|\,|\log(m/d)|
\leq\tau(m)\log(2X)
\ll_\eta X^\eta\log(2X).
\]

There is no additional factor \(|\mathcal D|\) or \(Q\). The nonprimitive masks may be dropped only after their implication \(p\mid h\) has been retained in the outer summation; that is the order used in the proof. A sum over multiple owner representations would require a different coefficient bound, but the theorem specifies a set of distinct integers and has no such multiplicity.

The elementary divisor estimate is justified uniformly in \(m\) with a constant depending on the fixed \(\eta\). For large primes \(p\), \(e+1\leq2^e\leq p^{\eta e}\); the finitely many smaller primes have bounded \(\sup_{e\geq0}(e+1)p^{-\eta e}\). This proves the stated estimate without a hidden additional power of \(X\).

For each odd prime \(p\), at most two powers can occur in \((X,3X)\). Three powers would have largest-to-smallest ratio at least \(p^2\geq9\), contradicting the interval. This loose upper bound is sufficient and includes every allowed exponent. Each such power has weight **\(\log p\)**. Replacing it by \(\log(p^j)\) and then inadvertently summing an extra number of exponents would lose the normalization; the author makes neither error.

The needed harmonic prime-base sum follows directly from Chebyshev and partial summation:

\[
\sum_{p\leq Y}\frac{\log p}{p}
=\frac{\vartheta(Y)}Y+
\int_1^Y\frac{\vartheta(t)}{t^2}\,dt
\ll1+\log Y.
\]

I checked the elementary Chebyshev proof as stated. Every power in \((n,2n]\) contributes to the corresponding prime valuation of the central binomial coefficient; its other valuation terms are nonnegative. The estimate for \(\Psi(2n)-\Psi(n)\), dyadic telescoping and monotonicity give the quoted real-variable majorant \(4(\log2)y\). This proves the prime-base harmonic estimate and does not invoke PNT or an interval asymptotic. The retained R22 source gives the same proof.

Combining these bounds with the original ordered-pair factor two gives

\[
|\mathcal N_{\mathcal D}|
\ll\frac{HX^\eta\log(2X)}{X\ell^2}
\sum_{p\leq\sqrt{3X}}\frac{\log p}{p}
\ll\frac{HX^\eta}{X}.
\]

Both logarithmic factors are accounted for: one is the actual cofactor logarithm, and the other comes from the weighted prime-base sum. Their ratio to \(\ell^2\) is uniformly bounded because \(\log X=\alpha\ell\), with \(\alpha\) in the fixed compact range. Since \(H/X=1/T\), this is the claimed bound. Finally \(1/\alpha\geq4/9\), so \(X^{1/100}/T\leq X^{-391/900}\).

## 5. Arbitrary-subset completion and the exact complement

I separately checked the reuse of the primitive estimate against the frozen R23 proof, which I previously reviewed in full. Its proof uses the exact primitive mask and mean \(1/\varphi(d)\), the even-grid factor \(1/(2d)\), fixed-order derivatives of the actual weight, and \(|\mathcal D|\leq Q\). It does not use dense divisibility or the owner prime-factor bound. It therefore remains valid for the arbitrary odd subset specified here.

The condition \(H\geq Q\) holds in this parameter range, and the same one fixed order \(J=24\) gives the exponent \(7/440\). This reuse does not enlarge the primitive estimate to arbitrary \(Q<X\) with \(Q>H\). The statement that only \(Q<X\) is needed belongs to the **nonprimitive** estimate; the combined corollary retains the displayed \(Q=X^{523/1000}\) and the verified completion range.

The five-term von Mangoldt opening is an algebraic identity for any divisor subset. Therefore replacing the old canonical subset by all odd \(d\leq Q\) is legitimate in the combined identity. Since \(m\) is odd, all divisors of \(m\) are odd, and the complementary divisors are exactly those with \(d>Q\). Their integer cofactors satisfy \(m/d<2X/Q\), with the correct strict inequalities.

This change does not make the remaining expression nonnegative, does not identify the primitive principal with the singular-series marginals, and does not evaluate the complementary small-cofactor sum. The report keeps all three pieces \(\mathcal A+\mathcal C-\mathcal M_{\mathfrak S}\), including their signs, logarithms, primitive masks and both marginal terms. It also expressly avoids attributing a distribution theorem to an arbitrary divisor family. No 186 equidistribution result is used for this generalization.

## 6. Review and verification scope

The accepted conclusion is the stated uniform nonprimitive bound and its legal combination with the existing smooth primitive completion. It concerns the fixed positive-shift packets and height range. No strict inequality for the full variance, no AH refutation and no prime-gap improvement follows from this result alone.

The adjacent receipt pins the author version, checker and original dependencies. I read the tiny scalar checker and replayed it in an isolated disposable copy. Its six rational assertions test exponents and normalization only. Both the output JSON and stdout were byte-identical to the frozen author outputs, SHA256 `00579811e9716e49e5ea29ed79ff185a633c5ec8e13b28e7d29a05a3cf046ac8`. All three source/dependency entries and six author-file entries matched their recorded hashes. The initial complete draft and the author's subsequently frozen mathematical report are byte-identical.

These exact scalar checks do not prove the asymptotic theorem. The ordinary proof audit above supplies the mathematical review. No author or prior-round file was changed. The detailed verification is retained in [source_and_replay_checks.json](source_and_replay_checks.json).
