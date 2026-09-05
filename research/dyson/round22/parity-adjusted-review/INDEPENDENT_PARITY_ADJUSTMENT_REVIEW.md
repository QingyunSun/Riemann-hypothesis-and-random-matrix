# Independent audit of the parity-adjusted target

Date: 2026-09-05. Reviewer: Aquinas (`yau_flow`). Verdict: **the two unconditional correction estimates are accepted as ordinary proofs**. The final identification with the original R21 residual is accepted only as a conditional assembly of the explicitly named companion lemmas. No strict correlation estimate follows.

Reviewed author file: `../parity-adjusted-target/PARITY_ADJUSTED_PAIR_TARGET.md`, 7,693 bytes, SHA256 `36a995c9852e95d6c29e44f2c5dd5815d27318fbabe0a94770e9f21a59c3bb6b`. I read its full mathematical text, not only a summary. No amendment to the reviewed argument is requested. I did not edit the author manuscript, run a data scan, or rederive the separate singleton-renormalization theorem in this review.

## 1. Difference of the two coefficients

Direct expansion gives
\[
q_2(m,h)-q(m,h)
=\mathfrak S(h)(2\,1_{\{m\text{ odd}\}}-1)
=-\mathfrak S(h)(-1)^m.
\]
The sign is positive on odd \(m\), negative on even \(m\). This correction vanishes for odd \(h\), since then \(\mathfrak S(h)=0\). The original factor two outside the ordered-pair sum is retained throughout.

It would be incorrect to remove even endpoints from \(q\) before this change: when both even endpoints have zero von Mangoldt value, \(q\) equals \(\mathfrak S(h)\), whereas \(q_2\) equals zero. The author explicitly makes the adjustment first.

## 2. Uniform alternating sum and complete shift average

I checked the exact weight bounds against the integral defining \(b\). The derivative bound costs no factor of \(T\): after scaling the integral to \((0,1)\), only \(\omega\) and \(\omega'\) are differentiated, and \(T/(T-1)\) is bounded.

For fixed \(h\), the Pareto kernel increases in \(m\). Thus on \([X,2X]\), or a truncated last block,
\[
\|b(\cdot)k(\cdot,h)\|_{\text{endpoints and variation}}
\ll_\omega \frac1{X\ell^2}(1+h/(2X))^{-T}.
\]
The alternating sequence has prefix sums bounded by one for any real block endpoints. Summation by parts therefore gives the claimed bound for each fixed shift without estimating a prime discrepancy.

The finite singular-series inequality \(A(y)=\sum_{h\le y}\mathfrak S(h)\le y\) is valid for real \(y\), by applying the established integer bound at \(\lfloor y\rfloor\). For the two kernels used in the author proof, nonnegative integration gives
\[
\sum_h\mathfrak S(h)g(h)
=\int_0^\infty A(y)(-g'(y))dy
\le\int_0^\infty g(y)dy.
\]
The boundary terms vanish for both the Pareto kernel and the compact power kernel. Equivalently, their integral representation followed by Tonelli proves this identity without any ambiguous boundary limit.

In particular the complete shift sum of \((1+h/(2X))^{-T}\) with singular-series weights is at most \(2X/(T-1)\). Hence one alternating block costs \(O_\omega(1/(T\ell^2))\), and the \(O(\ell)\) blocks covering \((L,2U]\) cost \(O_\omega(1/(T\ell))\). All positive shifts have been summed; no compact shift packet is substituted.

## 3. The baseline tail above the physical window

For \(m>2U\), the exact original weight bound is essential. Combining it with the row bound
\(\sum_h\mathfrak S(h)k(m,h)\le m/(T-1)\) gives total absolute mass at most
\[
\frac{C_\omega U^{T-1}}{T\ell^2}
\sum_{m>2U}m^{1-T}
\ll_\omega\frac{U\,2^{-T}}{T^2\ell^2}.
\]
I checked the remaining factor of \(U\): it is present here, since this is a sum over all integer lower endpoints, not a sum only over powers of two. The first integer term in integral comparison is absorbed because \(2U\ge T\). Since \(U=T^{9/4}\), the exponential expression is indeed \(O_\omega(1/(T\ell))\).

This also verifies absolute convergence needed to rearrange the baseline correction: the finite middle range has finite complete shift mass, and the displayed tail is summable. The author correctly uses alternating cancellation only on the middle blocks and absolute bounds in the far tail.

## 4. Even endpoints after the adjustment

If \(m,h\) are even, both endpoints are even. Every nonzero von Mangoldt value is therefore \(\log2\) at a power \(2^j\), \(j\ge1\). The adjusted baseline is zero. The product term is controlled by the singleton sum because
\[
\Lambda(m)\Lambda(m+h)
\le \frac{\log2}{4C_2}\,
\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)]
\]
when both values are nonzero; otherwise its left side is zero. The fixed positive lower bound \(\mathfrak S(h)\ge2C_2\) for even shifts is sufficient. Its precise numerical value is not needed.

For a lower endpoint \(r=2^j\) in \((L,2U]\), the row sum is at most \(r/(T-1)\). Multiplying by \(b(r)\ll1/(r\ell^2)\) gives \(O_\omega(1/(T\ell^2))\) per power. There are \(O(\ell)\) powers.

For an upper endpoint \(r=2^j\) in the same range, the exact exponent is
\[
b(m)(m/r)^T\ll_\omega
\frac1{r\ell^2}(m/r)^{T-1}.
\]
Writing \(h=r-m\), the compact kernel is \(g(h)=(1-h/r)_+^{T-1}\). Its integral is \(r/T\), not \(r/(T-1)\). This gives the same bound per power. Enlarging the indicated sums to all integer endpoints is legitimate because their summands are nonnegative; the singular series itself forces the relevant parity when needed.

For \(r>2U\), the lower-endpoint row is
\(O_\omega(U^{T-1}r^{1-T}/(T\ell^2))\).
The upper-endpoint row is
\(O_\omega(U^{T-1}r^{1-T}/\ell^2)\), using cancellation of \(m^T\) in the original weight integral and \(\sum_{m<r}\mathfrak S(r-m)\le r\).

Both are summed over powers of two. If \(r_0>2U\) is the first such power, their common dimensionless factor sums exactly as
\[
\sum_{j\ge0}(U/(2^jr_0))^{T-1}
=\frac{(U/r_0)^{T-1}}{1-2^{1-T}}\ll2^{-T}.
\]
There is no extra factor \(U\) in these sparse tails. This distinguishes them from Section 3 and verifies the author’s stated
\(O_\omega(1/(T\ell)+2^{-T}/\ell^2)\) absolute even-endpoint bound.

## 5. Scope of the assembly

The preceding sections independently establish author equations (2) and (3) without RH, PNT, a prime-pair conjecture, or the singleton-renormalization theorem.

For the final equation (8), the logical steps are exactly:

1. Replace the original centered residual by the complete \(q\)-sum using the separate singleton-renormalization lemma.
2. Replace \(q\) by \(q_2\) using the alternating correction just proved.
3. Remove odd shifts using the separate all-odd prime-power-pair bound, since both \(q\) and \(q_2\) then equal \(\Lambda(m)\Lambda(m+h)\).
4. Remove even \(m\), even \(h\) using the absolute even-endpoint bound just proved.

The remainder has odd \(m\), even \(h\ge2\), and singleton baseline two. It has the original ordered-pair normalization. These implications are sound conditional on the two companion inputs. This review does not declare the pending global singleton-renormalization proof independently checked merely because it is cited.

I authored the all-odd companion and the preceding small-shift note. The parent separately checked the all-odd proof, and Euclid separately accepted the small-shift proof. Thus this document is an independent audit of the new root-authored parity argument, not a newly independent audit of my own companion results.

No bound below the AH saturation value is obtained. The old residual's entire odd-shift part is not deleted on its own: singleton terms are redistributed by the global renormalization first. No invalid uniform sub-square-root prefix premise is recovered.

## Verification record

This is an ordinary analytic review. All signs, kernel exponents, parity cases, factors of two, dyadic counts and both distinct tail mechanisms were checked directly. No numerical scan or new prime-data calculation was performed. The adjacent receipt pins the reviewed root manuscript and the exact companion versions used for definitions and conditional scope.
