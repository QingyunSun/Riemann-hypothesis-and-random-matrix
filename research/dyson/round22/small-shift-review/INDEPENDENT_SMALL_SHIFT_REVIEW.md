# Independent review of the R22 small-shift removal theorem

Date: 2026-09-05. Reviewer: Euclid, the internal arithmetic agent. Decision: **accepted without amendment**, within the stated unconditional/RH scopes. This is an ordinary mathematical review plus a bounded exact-check replay, not formal verification or a proof of a strict zeta variance bound.

Reviewed author file: ../small-shift-obstruction/SMALL_SHIFT_REMOVAL.md, 12,215 bytes, SHA-256 290c1ba8e80ab64074cfe0c4ad9d2609d4930b4bf52d789ffa156f9090731a9b. The author's exact definitions agree with revised R21 SHA d7e73b8379e1adadd1fba79e3dc6141252c796502ba793030a500a8c5a6fc15e. No author/source file was edited.

## 1. What is accepted

For \(L=T^{7/4}\), \(\ell=\log T\), the proof establishes uniformly for \(1\le K\le L\)
\[
2\sum_m b_T(m)\sum_{h\le K}(1+h/m)^{-T}
|(\Lambda(m)-1)(\Lambda(m+h)-1)-(\mathfrak S(h)-1)|
\ll_\omega K/\ell+K\ell T^{-7/8}+K2^{-T}.
\]
It therefore permits unconditional absolute removal of all \(h\le K=o(\log T)\) from the signed R21 remainder.

Under RH, the signed odd-shift subaggregate, with every singleton term retained, is
\[
O_\omega(KT^{-7/8}+K2^{-T}).
\]
The same estimate has the subset cardinality in place of \(K\). It permits removal of odd shifts up to \(K=o(T^{7/8})\), eventually inside the stated \(K\le L\) domain.

The odd-shift conclusion is not an absolute coefficient bound. Neither conclusion estimates the entire typical shift range or proves a strict deficit from the AH constant.

## 2. Exact measure, Pareto kernel and endpoints

The author's
\[
b_T(m)=\frac{T m^{-T}}{\ell^2}\int_1^m
\omega(\log x/\ell)x^{T-2}dx
\]
is exactly R21's coefficient. Its product with \((1+h/m)^{-T}\) equals the original two-index survival integral after taking \(n=m+h\). I checked that there is no replacement by an exponential in \(h/m\), and no shift of the support window.

Writing \(x=mu\) makes the derivative transparent:
\[
b_T'(m)=-\frac{b_T(m)}m+
\frac{T}{m^2\ell^3}\int_0^1
\omega'((\log m+\log u)/\ell)u^{T-2}du.
\]
The factor \(T\) is canceled by the integral mass \(1/(T-1)\). Thus both bounds in author (6) are uniform; there is no hidden derivative loss of size \(T\).

For fixed positive \(h\), the Pareto factor increases with \(m\). The variation of \(b_Tk_h\) on a block is bounded using \(\int|b_T'|k_h+\sup|b_T|\int k_h'\), and the two endpoint values have the same scale. This yields author (7), including the right endpoint factor, also on a truncated last block. The argument applies to signed prefix sums only through this explicit variation norm.

In author (15), \(h\) is an integer while \(X,z\) may be real. Consequently
\(\sum_{X<m\le z}\Lambda(m+h)=\Psi(z+h)-\Psi(X+h)\) exactly. The endpoint correction is twice the difference between the number of integers in the block and its real length. Each singleton therefore has its proper endpoint. The displayed factor of two in that correction and the outer factor of two in the signed aggregate are both consistent.

## 3. Uniformity of the sieve with a growing even shift

I read the retained primary text and checked the live [Tao sieve notes](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/), equation (22), Lemma 17 and Corollary 19. The relevant source provides combinatorial sieve coefficients supported on \(d\le D\), with absolute value at most one; the application therefore has remainder at most \(\sum_{d\le D}|r_d|\). Its fixed dimension axiom is the only local-density condition needed here. The author does not invoke a fixed-pattern prime-tuple asymptotic for varying \(h\).

Independently checking the hypotheses gives the following uniform bounds. For even \(h\), the forbidden classes are \(0\) and \(-h\), with one class when \(p\mid h\). Thus \(g_h(2)=1/2\), while for every odd prime \(g_h(p)\le2/p\le2/3\). In particular \(g_h(p)\) stays uniformly below one. For \(2\le w\le z\),
\[
\frac{V_h(w)}{V_h(z)}
=\prod_{w\le p<z}(1-g_h(p))^{-1}
\le C(\log z/\log w)^2
\]
by comparison with the two-class product and the Mertens product bounds. The constant is independent of every factor of \(h\). Deleting forbidden classes only decreases the ratio.

The residue count modulo squarefree \(d\) is multiplicative by CRT. Counting its classes on a real interval of length \(X\) costs \(O(\nu_h(d))\), uniformly in the class positions. Since \(\nu_h(d)\le2^{\nu(d)}\le\tau(d)\),
\[
\sum_{d\le X^{1/2}}|r_d|\ll X^{1/2}\log X.
\]
This is an elementary integer count, not a hypothesis about prime progression errors.

Fixing a sufficiently large sieve parameter \(s\) once and taking \(D=X^{1/2}\), \(z=D^{1/s}\), is legal for every growing \(h\le X\). The resulting constant may depend on this fixed \(s\), but not on \(h,X,T,K\). Genuine primes \(m,m+h>X>z\) survive the sieve.

Finally the product comparison in author (11) has the correct direction. Factors \((p-1)/(p-2)\) for \(p\mid h\), \(p>z\), are greater than one; adjoining them only enlarges the upper bound. The baseline factorization
\[
1-2/p=(1-1/p)^2(1-1/(p-1)^2)
\]
then gives \(V_h(z)\ll\mathfrak S(h)/\log^2X\), uniformly. There is no requirement that all prime divisors of \(h\) lie below the sieve level.

## 4. Prime powers, singular-series averaging and the unconditional bound

The passage from genuine primes to \(\Lambda\) retains all higher powers. There are \(O(\sqrt X\log X)\) powers of exponent at least two up to \(3X\), a deliberately loose bound obtained by summing the possible exponents. Each such value fixes at most two candidate indices in a shifted pair. With logarithmic weight at most \(\log^2(3X)\), their total is \(O(\sqrt X\log^3X)\). The sieve remainder acquires the same power of the logarithm when prime weights are restored. This verifies author (12) without a hidden prime-power deletion.

For an odd \(h\le X\), the even member must be \(2^j\). Both members lie in \((X,3X]\), an interval of fixed multiplicative ratio. Only \(O(1)\) such powers occur there, uniformly in \(h\). Their total weighted product is \(O(\log X)\). This sharper bound also applies to every prefix of the block.

The finite singular-series sum is independently exact in its stated inequality:
\[
\sum_{h\le K}\mathfrak S(h)
\le KC_2\prod_{p>2}\left(1+\frac1{p(p-2)}\right)=K.
\]
The first inequality uses \(\lfloor K/(2d)\rfloor\le K/(2d)\), with nonnegative divisor terms. The Euler product converges absolutely and every local factor cancels the corresponding factor of \(C_2\). It follows that \(\sum_{h\le K}|c_h|\le2K\). No average prime-pair conjecture enters this step.

The elementary estimate \(\Psi(y)\ll y\) used on the two singletons is sufficient. The given binomial proof is valid: for each prime power in \((n,2n]\), its individual floor difference in the valuation of \({2n\choose n}\) is one, and all other floor differences are nonnegative. Telescoping powers of two and monotonicity provide the real-variable bound.

The absolute expansion in author (13) is an upper bound for the actual centered coefficient. Summing the sieve bound, singleton estimates and singular-series inequality yields the block mass \(O(XK+K\sqrt X\log^3X)\). Multiplication by \(1/(X\ell^2)\) and summation over \(O(\ell)\) blocks gives \(K/\ell\) for the leading term. The error uses the geometric sum of \(X^{-1/2}\), giving \(K\ell L^{-1/2}\), exactly as claimed.

## 5. The RH signed odd-shift estimate and all tails

I rechecked the retained [Schoenfeld primary source](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), Theorem 10, printed p.337, equation (6.2), including its rendered page. It supplies the bound for \(\Psi(x)-x\), not only for \(\theta(x)-x\), under ordinary RH. Its threshold is \(x>73.2\); enlarging an unspecified constant handles the bounded initial interval.

In the real-endpoint identity (15), all four arguments of \(E=\Psi-\mathrm{id}\) lie in \([X,3X]\). The RH bound and the uniform odd-pair estimate therefore give \(\sup|R_X|\ll\sqrt X\log^2X\) uniformly in every odd \(h\le X\). There is no sub-square-root assertion.

Combining this prefix bound with the exact variation norm gives \(O_\omega(X^{-1/2})\) per odd shift and per block. Because
\[
\sum_{j\ge0}(L2^j)^{-1/2}
=\frac{L^{-1/2}}{1-2^{-1/2}},
\]
the final result is \(O_\omega(KT^{-7/8})\), without an extra \(\log T\). Taking an arbitrary subset simply changes the count of shifts. The weaker ordinary-PNT comparison also checks: its maximum relative error contributes \(o(K/\ell)\), and the odd-pair/endpoint terms contribute \(O(K/(L\ell))\).

For \(m>2U\), the exact coefficient satisfies author (8). Since \(K\le L<U\), one has \(m+h\le2m\). The total absolute shifted coefficient mass is \(O(K\log^2(2m))\), using the finite singular-series upper bound. The explicit integral of \(m^{-T}\log^2(2m)\) in the manuscript is correct. After multiplying by \(U^{T-1}/\ell^2\), it is \(O(K2^{-T})\). The first integer term is bounded at the same scale because \(2U\ge T\). This controls the genuine infinite endpoint; it is not a formal tail subtraction. For an odd subset its cardinality replaces \(K\) here as well.

The estimates are uniform for \(K\le L\); the claimed small-o ranges eventually satisfy that domain. No assertion of positivity is made for an odd signed subaggregate.

## 6. Verification receipt and limits of acceptance

The copied exact checker was run in a temporary directory containing only the pinned manuscript and checker. All seven checks passed; generated JSON and stdout were byte-identical to the author results, each with SHA-256 7cbf272e314a80cedcd03b3dc0600c895c460c9dd2f647cecc4d2e44bee22c40. The full fields are retained in replay_and_source_checks.json. These checks cover Euler-factor algebra, a finite divisor expansion, exact formal-coefficient endpoints, the tail antiderivative and the rational exponent.

Fourteen author/source/dependency file size and SHA pairs were verified. The syntax-checker and its reported results were hash-checked, not rerun. The mathematical acceptance comes from the ordinary estimates above, not the seven symbolic checks.

The R21 correction remains in force: an all-large-height, all-shifts prefix bound below the square-root scale is impossible. R22 does not restore that premise. It shows why the actual small weighted portion can nevertheless be negligible. What remains is the signed aggregate over the explicitly unremoved shifts; the theorem gives no strict bound for it and does not refute AH.

