# Independent review of the actual small-cofactor covariance

Date: 2026-09-05. Reviewer: Aquinas. Decision: accepted as an ordinary proof in its stated scope; no mathematical amendment requested. This is an independent analytic review, not formal verification or a numerical enclosure of a prime statistic.

The reviewed author manuscript is `SMALL_COFACTOR_CENTERED_TARGET.md`, 20,129 bytes, SHA-256 `c16cc2a52328ca673bcd97db2221235a7a61b7e40a6dff19caa85c4cb3bd4c73`. I read its complete Sections 1–8, checked the relevant retained primary statements, and separately checked the exact packet normalization. The adjacent receipt records the immutable inputs and the bounded checker replay.

## 1. Exact switch and actual bad rows

The substitution \(m=kd\) in the complement is exact. Since \(m\) is odd, both factors are odd. The strict restrictions \(d>Q\) and \(m<2X\) imply \(k<2X/Q\); the \(k=1\) term vanishes through \(\log1\). No condition \((k,d)=1\) is introduced. This matters when the original integer has repeated prime factors: \(\mu(d)\), not a restriction on \(k\), supplies the correct coefficient.

For a raw bad row, \((k,h)>1\) and \(\Lambda(kd+h)\ne0\) force \(n=p^j\) with \(p\mid k,h\). Its base is odd. Because \(k<2X/Q<X<n\) eventually, \(j=1\) is impossible. Therefore \(p<\sqrt{3X}\), and all exponents \(j\ge2\) are retained with weight \(\log p\). The support is exactly \(X<m<2X\), \(H<h<2H\), and \(X<n<3X\); compact cutoffs make every sum finite.

I independently obtain the author's bound by summing divisor coefficients for fixed \(n,h\) before summing prime bases:
\[
\sum_{kd=n-h}|\mu(d)|\log k
\le\tau(n-h)\log(2X)\ll_\eta X^\eta\log X.
\]
For odd \(p\), an allowed even shift is \(h=2pr\), so its count is at most \(H/p\) directly. Equivalently, the author's interval-length estimate with a rounding term is uniform because \(H/\sqrt X\ge X^{1/22}\). There are at most two powers of each odd base in \((X,3X)\). The exact weight bound \(|F|\ll(X\ell^2)^{-1}\), together with the elementary Chebyshev consequence
\(\sum_{p\le Y}(\log p)/p\ll\log(2Y)\), gives
\[
|\mathcal C_Q^{\rm bad}|\ll_\eta X^\eta/T.
\]
The logarithmic normalization and the uniform exponent \(391/900\) at \(\eta=1/100\) are correct. This estimates a raw prime-power term only, and does not silently delete the constant on nonprimitive residue classes.

## 2. Primitive center, parity, and its entire added-back main

For fixed \(k,h\) with \((k,h)=1\), odd \(d\)'s parameterize one primitive progression modulo \(2k\). The local density along these samples is therefore \(2k/\varphi(k)\). The author inserts this value into the covariance and adds it back with exactly the coefficient in (13). Thus (14) is an algebraic identity regardless of any prime-distribution theorem. The finite-interval primitive principal is not equated with this constant.

For fixed \(m\), Poisson summation on \(2s\mathbb Z\) has the mean factor \(1/(2s)\). Smooth compact support and the derivative bounds give the stated error \(A_X(s/H)^j\), where \(A_X=(X\ell^2)^{-1}\). Inclusion–exclusion over \(s\mid k\) therefore gives mean \(\varphi(k)/(2k)\), canceling the reciprocal factor in the added-back local main. This produces precisely \(\mathcal L_Q^0\), with its outer factor two.

The proof permits nonsquarefree \(k\). The bounds \(k/\varphi(k)\le\tau(k)\), \(\tau(k)^2\le d_4(k)\), and
\(\sum_{k\le K}\tau(k)^2/k\ll(1+\log K)^4\) have the correct directions. There are at most \(2X/k\) values of \(d\) per row. Taking the fixed derivative order \(j=1\) consequently gives the whole error
\[
O\bigl((K/H)(\log X)^3\bigr),\qquad
K/H\le2X^{-753/11000}.
\]
For the parity-only center the same computation with \(s=1\) costs \(O(H^{-1})\): the remaining sum \(\sum_{k<K}(\log k)/k\) is \(O((\log X)^2)\), exactly offset by \(\ell^2\).

Writing \(\mathcal L_Q^{\rm flat}=4\sum_{k,d}\mu(d)\log k\sum_{h\text{ even}}F(kd,h)\), the difference of the two covariance definitions is
\[
\mathcal Z_Q-\mathcal Z_Q^{(2)}
=\mathcal L_Q^{\rm flat}-\mathcal L_Q^{\rm loc}
-\mathcal C_Q^{\rm bad}.
\]
This verifies the sign and all costs in (23). It also shows why inserting a primitive mask and simply dropping the excluded baseline would be invalid. No such step occurs in this manuscript.

## 3. Primary-source check and the actual RH norm estimate

I checked the retained CCCC text, printed page 1, definitions (1.1) and bound (1.3). Under ordinary RH, it provides the author's multiplicative-interval bound with one fixed exponent \(\beta=3\). The substitution \(S=T/\lambda\), with \(\lambda\in[1/2,2]\), keeps \(S\asymp T\); the theorem has one fixed constant and does not require uniformity in a varying exponent or a varying test function. Also \(2X+1<S^3\) eventually and uniformly for the full assigned range of \(\alpha\).

I checked (31) directly with the right-continuous prime staircase. For odd integer \(m\), the odd integers in \((m,m+y]\) are precisely the even shifts. Subtracting the even prime powers removes exactly the powers of two. Since \(0\le y\le2H<m\), there is at most one such power in the interval, and the parity count differs from \(y/2\) by less than one. Thus both extra terms are \(O(1)\), uniformly at real endpoints. The remaining prime powers stay in \(E=\Psi-\mathrm{id}\).

Stieltjes integration by parts has no boundary term because the fixed shift cutoff vanishes at both ends. The weighted increment therefore satisfies (32). After \(y=\lambda m/T\), its integration interval is contained in the same fixed \([1/2,2]\), with Jacobian divided by \(H\) at most two. One can enlarge the nonnegative integral to that interval before summing \(m\), so there is no illicit use of a theorem at a sample-dependent additive length.

For each fixed \(\lambda\), compare the value at integer \(m\) with \(x\in[m,m+1]\). Each of the two staircase endpoints moves by at most two, costing \(O(\log X)\); the squared comparison error summed over \(O(X)\) integers is \(O(X\log^2X)\). The primary weighted integral multiplied by \(O(X^2)\) gives \(O(XH\ell^2)\), which absorbs the comparison errors. This proves (30) with all normalizations intact.

The coefficient bound \(\sum|c_Q(m)|^2\ll X(\log X)^5\) follows from \(|c_Q|\le\tau\log(2X)\), \(\tau^2\le d_4\), and the elementary four-divisor first moment. Cauchy–Schwarz with the outer factor \((X\ell^2)^{-1}\) then gives exactly
\[
|\mathcal Z_Q^{(2)}|\ll\sqrt H(\log X)^{3/2}.
\]
Ordinary RH suffices. This upper estimate grows and supplies neither an \(O(1)\) covariance bound nor a one-sided strict deficit.

I also checked the retained 186 source, Proposition 2.12(i) and Proposition 2.15. They have the stated common smooth-weight variation premise and ordinary-modulus prime distribution range. The small moduli here lie below the latter range, but the attached actual coefficient \(\mu((n-h)/k)\) is not a permitted common smooth weight. The manuscript's squarefree count in the class \(11\pmod{18}\) is valid: inclusion–exclusion gives a positive Euler product and \(O(\sqrt D)\) total endpoint/tail error. The adjacent odd-grid value two lower is divisible by nine, proving variation of order \(D\). This is a correctly scoped obstruction to that particular weighted source application, not to all possible arithmetic cancellation.

## 4. Main scales, sharp cofactor cutoff, and assembly status

The main-scale calculation (34) is valid for a fixed interior \(\alpha\) with \(\omega(\alpha)>0\). The exact integral gives \(b_T(Xv)\sim\omega(\alpha)/(Xv\ell^2)\) uniformly on the fixed support. The two parity grids contribute \(1/4\), and the original ordered-pair factor contributes two. Thus the displayed coefficient \(H/(2\ell^2)\) is correct. The limiting exponential is used only for this explicitly separate scale calculation.

In (37)–(38), the hypothesis on the odd Möbius prefix applies at the sharp lower endpoint \(Q\) as well as at the smooth support endpoints. Partial summation includes that boundary and costs \(\delta_\mu(Q)H/(k\ell^2)\). Summing \(\log k/k\) gives the stated \(O(\delta_\mu(Q)H)\), without deleting the main. The relative-error precision discussion is consequently accurate.

At the author's freeze, the separate enlarged-family \(\mathcal N_Q\) proof was marked pending; (24) correctly retained it exactly. That input now exists as `GENERAL_NONPRIMITIVE_BOUND.md`, SHA-256 `fd76f0bb6915dbad962f4e74a9fa31de5e3b9d79f26572fa8b6fea400e9d6a02`. This review records the later availability without altering the frozen source. The earlier primitive completion uses only odd \(d\le Q\), smooth physical shifts and Chebyshev, so it also applies to the complete odd family.

Even after inserting those two negligible errors, the retained target is the entire signed combination
\[
\mathcal A_Q+\mathcal L_Q^0+\mathcal Z_Q-\mathcal M_{\mathfrak S}.
\]
Neither primitive principal, Möbius-linear main, nor singular-series-weighted prime marginal has been evaluated at the required fluctuation precision. The note does not prove a partition of the entire variance into these packets. Its explicit statements of these remaining obligations are essential and have been retained in this acceptance.

## 5. Verification scope

I reviewed the author's eight-scalar checker before replaying an unchanged copy in a temporary directory. The receipt records the byte comparison of its output and all source/author hashes. These exact rational checks concern exponents only; the substantive identities and estimates above were independently checked as ordinary mathematics. No prime-height experiment, parameter sweep, author-file edit, or Git mutation was performed.
