# Independent review: joint cancellation in the actual compact quadratic packet

Date: 2026-09-05. Reviewer: Plato, separate from the author Euclid.

**Decision: accepted as an ordinary mathematical proof under ordinary RH, with the stated fixed compact-packet scope.** I read the complete manuscript, rederived its normalizations and all error terms, checked the three primary inputs, and replayed the tiny exact checker in a temporary copy. No mathematical amendment remains requested. This accepts the reduction \(\mathcal P=\mathcal Z_Q^{(2)}+o(1)\), including the full specified window around \(X=T^2\). It does not accept a strict bound for \(\mathcal Z_Q^{(2)}\), a sum over all length scales, an AH refutation, or a new famous theorem.

The reviewed final manuscript is [JOINT_MAIN_CANCELLATION.md](../joint-main-cancellation/JOINT_MAIN_CANCELLATION.md), 19,377 bytes, SHA256:

    6995e95c0bf3bd0ba606385f1ee50d23f23d238fccf655f96c93230a7d856d03

The author's frozen receipt is SHA256:

    2058f6d018663e6b9810c42e1a29b1d7e914eff85433236e60c69187565a9d50

The only requested change during review was the wording “Subtract the two formulas (19) and (23)” to “Combine the two formulas.” The operation is addition of \(\mathcal A_Q+\mathcal L_Q^0\), with the negative integral already present in (23). The final text contains this correction; no displayed formula changed. I have not edited an author file.

## 1. Quantifiers and the actual arithmetic object

The parameters are real \(T\to\infty\), \(X=T^\alpha\), \(H=X/T=X^\theta\), \(Q=X^\rho\), \(\theta=1-1/\alpha\). The proof requires fixed positive margins in
\[
7/4\le\alpha\le9/4,\qquad 0<\rho<\theta,\qquad
\theta<1/2+\rho/2.
\]
The derivative order \(J\) and the small Möbius and divisor exponents are fixed uniformly on the chosen parameter set. The text explicitly supplies this interpretation; it does not take a limit in which \(J\), a cutoff derivative, or a margin depends on \(T\).

The weight remains exactly
\[
F(m,h)=b_T(m)\chi(m/X)V(h/H)
\left(\frac m{m+h}\right)^T,
\quad
b_T(m)=\frac{Tm^{-T}}{\log^2T}
\int_1^m\omega(\log x/\log T)x^{T-2}\,dx.
\]
The fixed smooth functions \(\chi,V\) vanish in neighborhoods of both endpoints of \((1,2)\). Therefore the genuine arithmetic support is \(X<m<2X\), \(H<h<2H\), and \(X<n=m+h<3X\) for large \(T\). In particular \(n>h\), the cofactor logarithms have positive arguments, and all reindexed sums are finite. The tail of \(b_T\) above the support of \(\omega\) is not discarded.

The residual coefficient is the sharp, exact divisor sum
\[
c_Q(m)=\sum_{\substack{d\mid m\\d>Q}}\mu(d)\log(m/d)
\]
on odd \(m\), and the residual statistic is
\[
\mathcal Z_Q^{(2)}
=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)c_Q(m)\{\Lambda(m+h)-2\}.
\]
Real \(Q\) means exactly the indicated inequalities on integer divisors. There is no invented coprimality between divisor and cofactor, no restriction to a source-owner family, and no loss of higher prime powers.

The flat center \(2\) is appropriate to an odd-integer lattice of spacing \(2\). The odd von Mangoldt prefix, however, has continuous mean \(y\), not \(2y\). Keeping these two different normalizations is essential; the manuscript does so.

## 2. Uniform smoothness and the exact primitive partition

The identity
\[
b_T(m)=\frac{T}{m\log^2T}
\int_0^1\omega((\log m+\log u)/\log T)u^{T-2}\,du
\]
is exact after extending the fixed weight by zero. The interval corresponding to \(x<1\) contributes zero. The integral of \(u^{T-2}\) is \(1/(T-1)\), so each fixed derivative of \(b_T\) is \(O(m^{-1-j}\log^{-2}T)\). Differentiation does not incur \(T^j\).

In variables \(v=m/X,z=h/H\), the other factor is exactly \((1+z/(Tv))^{-T}\). Fixed derivatives on the compact support are bounded uniformly. Thus \(F\) has amplitude
\[
A=(X\log^2T)^{-1},
\]
\(m\)-scale \(X\), and \(h\)-scale \(H\). At fixed \(n\), derivatives of \(F(n-h,h)\) have \(H\)-scale since \(H<X\). By contrast, derivatives of \(J_+(n)=\int F(n-h,h)\,dh\) are taken at fixed \(h\); their scale is \(X\). This prevents a false \(H^{-1}\) loss in the later RH estimate. Compact cutoffs make all endpoint derivatives vanish.

For each odd \(d\), the algebra behind (10) is
\[
1_{n\equiv h\ (d)}
=1_{(n,d)=1}\left(1_{n\equiv h\ (d)}
-\frac{1_{(h,d)=1}}{\varphi(d)}\right)
+\frac{1_{(n,d)=1}1_{(h,d)=1}}{\varphi(d)}
+1_{(h,d)>1}1_{n\equiv h\ (d)}.
\]
On a congruent row, \((n,d)=(h,d)\); on a noncongruent row the two primitive means cancel. Together with the exact Möbius divisor identity this proves the five-term opening, with all signs as stated. The discrepancy for \(d=1\) is zero but its principal is retained.

I checked the Fourier normalization in the primitive completion explicitly. For a unit \(n\bmod d\), let \(k_r=K_{d,2r}(n)\) on \(r\bmod d\). Its mean is zero and its period \(\ell^1\) norm is at most \(2\). Therefore, with the normalized Fourier convention,
\[
\widehat k(j)=\frac1d\sum_{r\bmod d}k_r e(-jr/d),
\qquad |\widehat k(j)|\le2/d.
\]
Equivalently the unnormalized coefficients are at most \(2\). This makes precise the manuscript's coefficient bound. Poisson summation combines these coefficients with frequencies \(l/(2d)\), \(l\ne0\). Using \(J+1\) derivatives of the weight gives
\[
\frac{A_fH}{d}\sum_{l\ne0}
\left(\frac{d}{H|l|}\right)^{J+1}
\ll_J A_f(d/H)^J.
\]
There is no extra factor \(d\). With \(A_f=O(A\log X)\), summation over \(n\) by Chebyshev and then over \(d\le Q\) yields
\[
\mathcal B_Q\ll_J \frac{Q}{\log X}(Q/H)^J.
\]
This is a physical shift completion of the actual finite coefficient. It requires \(Q<H\) with a fixed margin; it does not assume a distribution theorem for a twisted prime sequence.

## 3. Both nonprimitive prime-power debts

In \(\mathcal N_Q\), a nonzero von Mangoldt weight forces \(n=p^j\) with an odd prime \(p\mid d,h\). Since \(d\le Q<X<n\), \(j=1\) is impossible. Hence \(j\ge2\) and \(p\le\sqrt{3X}\).

Writing \(h=2pr\) gives the exact count
\[
\#\{r\in\mathbb Z_{>0}:H/(2p)<r<H/p\}\le H/p.
\]
There is no additive rounding term to sum over primes. If \(H<p\), the range is empty. This is why the argument remains valid in the part of the new window where \(H<\sqrt X\). In a multiplicative interval \((X,3X)\), each odd prime has at most two relevant powers, an intentionally harmless upper bound.

The absolute divisor coefficient is bounded by \(\tau(n-h)\log(2X)\ll_\eta X^\eta\log X\), whereas \(\Lambda(p^j)=\log p\). Consequently
\[
|\mathcal N_Q|
\ll_\eta A X^\eta H\log X
\sum_{p\le\sqrt{3X}}\frac{\log p}{p}
\ll_\eta X^\eta/T.
\]
The Chebyshev prime sum supplies only a logarithm. No arbitrary \(\log X\) is substituted for \(\log p\) before summing \(1/p\). No source-owner bound for the largest prime factor is needed.

There is a distinct debt in completing \(\mathcal A_Q\). Its first completed mean still contains \(1_{(n,d)=1}\). Removing this mask again restricts \(n\) to \(p^j\), \(j\ge2\), and
\[
\sum_{\substack{d\le Q\\p\mid d}}\frac1d
\ll \frac{\log(2Q)}p.
\]
Combining this with \(\int|w_{n,d}|\ll AH\log X\) and the same \(\log p/p\) sum gives \(O(\log X/T)\), exactly (18). The manuscript therefore does not silently replace the original primitive principal by a full prime mean.

## 4. The principal mean and the genuinely smooth cofactor completion

For odd \(d\), expanding \(1_{(h,d)=1}\) over \(s\mid d\) and completing the even grids \(2s\mathbb Z\) gives
\[
\sum_{\substack{h\ {\rm even}\\(h,d)=1}} w(h)
=\frac{\varphi(d)}{2d}\int w
+O(A\log X\,\tau(d)d/H).
\]
Multiplication by the original \(2\mu(d)/\varphi(d)\) produces the coefficient \(\mu(d)/d\). The error is bounded by
\[
\frac{\log X}{H\log^2T}\sum_{d\le Q}\tau(d)^2
\ll (Q/H)\log^3X.
\]
For the last estimate one may use
\(\sum_{d\le Q}\tau(d)^2\le Q\sum_{d\le Q}\tau(d)^2/d\ll Q\log^4(2Q)\).
This checks both the parity factor and the absence of an unintended second factor \(Q\). With the separately paid nonunit debt, equation (19) follows.

The flat complementary center satisfies the exact identity
\[
\mathcal C_Q-\mathcal Z_Q^{(2)}
=4\sum_{m\ {\rm odd}}c_Q(m)\sum_{h\ {\rm even}}F(m,h).
\]
Completing only the grid \(2\mathbb Z\), and using
\(\sum_{m<2X}|c_Q(m)|\ll X\log^2X\), gives
\[
\mathcal C_Q-\mathcal Z_Q^{(2)}
=2\sum_{m\ {\rm odd}}c_Q(m)J_-(m)+O(H^{-1}).
\]
This step does not insert the primitive mask of the complementary cofactor. Consequently it has no \(K/H\) requirement.

After the exact divisor identity, the remaining complete divisor term has \(m=dr\), both factors odd. The function \(\log r\,J_-(dr)\) has amplitude \(O(H\log X/(X\log^2T))\) and scale \(X/d\). Two derivatives in the odd-grid Poisson formula give
\[
2\sum_{r\ {\rm odd}}\log r\,J_-(dr)
=\frac1d\int J_-(m)\log(m/d)\,dm
+O\!\left(\frac{H\log X}{X\log^2T}\frac dX\right).
\]
The \(1/d\) includes the exact change of variable; the leading \(2\) removes the odd-grid density \(1/2\). Smooth support lies away from \(r=0\), so extending the function by zero on the real line is legitimate.

The summed error is \(O(HQ^2\log X/(X^2\log^2T))\). A first-variation estimate without the \(d/X\) saving would not establish this theorem. The author's use of genuine smooth completion is therefore substantive, not interchangeable with a rough Riemann-sum estimate.

## 5. Ordinary RH gives the odd Möbius constant \(2\)

The primary [Soundararajan paper](https://arxiv.org/pdf/0705.0723v2), printed page 1, equation (1), explicitly states the consequence of ordinary RH
\[
M(y)\ll_\varepsilon y^{1/2+\varepsilon}.
\]
Its stronger theorem is not needed. I checked the retained extraction and the rendered first page. There is no GRH or arithmetic-progression Möbius hypothesis hidden in this input.

Independently, the identity
\[
M_{\rm odd}(y)=\sum_{j\ge0}M(y/2^j)
\]
holds at every real endpoint. Each integer in the double sum has its powers of \(2\) removed; the Möbius coefficients cancel for positive \(2\)-adic valuation and leave exactly the odd ones. The finite geometric sum gives the same RH estimate for \(M_{\rm odd}\).

The Dirichlet series is initially absolutely convergent on \(\Re s>1\):
\[
D_{\rm odd}(s)=\frac1{(1-2^{-s})\zeta(s)}.
\]
Partial summation and the RH prefix bound give local uniform convergence, including each fixed derivative, to the right of \(1/2+\varepsilon\). Analytic continuation and the Laurent expansion of \(\zeta\) at \(1\) then give
\[
D_{\rm odd}(1)=0,\quad D'_{\rm odd}(1)=2,
\quad
\sum_{d\ {\rm odd}}\frac{\mu(d)\log d}{d}=-2.
\]
Thus \(a_Q(m)=2+e_Q(m)\), with
\[
e_Q(m)\ll_\varepsilon Q^{-1/2+\varepsilon}\log X,
\qquad
e_Q^{(j)}(m)\ll_{\varepsilon,j}
Q^{-1/2+\varepsilon}X^{-j}\quad(j\ge1).
\]
These are conditional convergent sums and tail estimates, not assertions of absolute convergence at \(s=1\). Derivatives in \(m\) hold \(Q\) fixed; changing \(Q\) across its integer jumps is not part of the argument.

## 6. The decisive cancellation occurs before applying the prime RH bound

Combining the principal formula with the complementary-center formula leaves the small coefficient part exactly
\[
\mathcal R_Q=
\sum_{n\ {\rm odd}}\Lambda(n)G_Q(n)-\int G_Q(y)\,dy,
\quad
G_Q(n)=\int F(n-h,h)e_Q(n-h)\,dh.
\]
The two integrals agree by \(m=n-h\), with Jacobian \(1\), on the genuine compact support. The equality retains the shifted endpoint \(n\) throughout.

At fixed \(h\), each derivative in \(n\) costs \(X^{-1}\), so
\[
\|G_Q^{(j)}\|_\infty
\ll \frac{H}{X^{j+1}\log^2T}
Q^{-1/2+\varepsilon}\log X,\qquad j=0,1.
\]
The [Schoenfeld primary](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), printed page 337, Theorem 10, equation (6.2), bounds \(\Psi(y)-y\) under RH. The retained source distinguishes this from the \(\vartheta\) bound in (6.3). Removing powers of \(2\) from \(\Psi\) costs \(O(\log y)\), hence the odd prefix still has centered error \(O(\sqrt y\log^2(2y))\). Compact Abel summation now gives
\[
\mathcal R_Q\ll_\varepsilon
\frac{H}{\sqrt X}Q^{-1/2+\varepsilon}\log X.
\]
There are no boundary terms outside the compact support. This is the product of a small Möbius truncation error and a centered one-prime error. It is not a bound on a large one-prime main in isolation.

In particular, bounding the absolute \(e_Q\) integral first would cost about \(HQ^{-1/2+\varepsilon}/\log X\), which can grow. The proof never uses that invalid shortcut. It retains the two large prime mains and the continuous main until the singular-series marginals have been combined.

## 7. The singular-series transform, its endpoint condition, and both marginals

The [Montgomery–Soundararajan primary](https://arxiv.org/pdf/math/0409258v1), printed page 4, equation (16), concerns the singular series itself. With its ordered-pair convention it implies
\[
A_2(y)=\sum_{h\ge1}(y-h)_+\{\mathfrak S(h)-1\}
=-\tfrac12y\log y+O(y).
\]
The factor \(1/2\) is required. For integer \(y\), \(2A_2(y)\) is the paper's second moment. For real \(y\), the hinge is linearly interpolated between integer endpoints; \(\sum_{h\le y}\mathfrak S(h)\ll y\) bounds the interpolation change by \(O(y)\), which is sufficient here. No conditional prime-pair hypothesis elsewhere in that paper is used.

The even-shift centered hinge is
\[
B_2(y)=\sum_{\substack{h\ge1\\h\ {\rm even}}}
(y-h)_+\{\mathfrak S(h)-2\}.
\]
Its difference from \(A_2\) is exactly
\(\sum_{h\ge1}(-1)^{h+1}(y-h)_+\), which is \(O(y)\) at all real endpoints. Thus it has the same \(-y\log y/2\) term.

For a fixed smooth \(f\) supported in \((H,2H)\),
\[
\sum_{h\ {\rm even}}\{\mathfrak S(h)-2\}f(h)
=\int_0^\infty B_2(y)f''(y)\,dy.
\]
All hinge boundary terms vanish. In particular
\(\int_0^\infty yf''(y)\,dy=f(0)=0\).
Writing \(\log y=\log H+\log(y/H)\) therefore cancels the entire \(\log H\) contribution. The remaining integral is bounded by
\[
\int_H^{2H}y(1+|\log(y/H)|)|f''(y)|\,dy\ll A_f.
\]
Completing \(2\sum_{h\ {\rm even}}f(h)\) gives the continuous mean \(\int f\), so the final transform is
\[
\sum_{h\ {\rm even}}\mathfrak S(h)f(h)=\int f+O(A_f).
\]
This correct continuous coefficient is \(1\), not \(2\).

I checked its use separately for \(f(h)=F(m,h)\) and \(f(h)=F(n-h,h)\). Both satisfy the same bounds, including the moving \(m=n-h\) cutoff. Summing errors against either full von Mangoldt weights or the integer count costs \(O(XA)=O(\log^{-2}T)\). The result is exactly
\[
\mathcal M_{\mathfrak S}
=2\sum_{m\ {\rm odd}}\Lambda(m)J_-(m)
+2\sum_{n\ {\rm odd}}\Lambda(n)J_+(n)
-4\sum_{m\ {\rm odd}}J_-(m)+O(\log^{-2}T).
\]
Finally,
\[
2\sum_{m\ {\rm odd}}J_-(m)
=\int J_-(m)\,dm+O(H/(X^2\log^2T)),
\]
by two derivatives on scale \(X\). This matches all three large terms in (32), including the negative baseline sign.

The cancellation of the \(\log H\) term relies on vanishing near \(h=0\). For a different length weight with \(f(0)\ne0\), its coefficient would survive. The proof and theorem correctly withhold a conclusion about such weights or an unbounded partition over length scales.

## 8. Error ledger and the full central window

The manuscript's joint error, in absolute value, is
\[
O_\varepsilon\!\left(
\log^{-2}T+(Q/H)\log^3X+\frac{\log X}{T}
+\frac{HQ^2\log X}{X^2\log^2T}
+\frac{H}{\sqrt X}Q^{-1/2+\varepsilon}\log X
+\frac{H}{X^2\log^2T}\right).
\]
The separate primitive, nonprimitive and flat-center debts are
\[
O_J(Q(Q/H)^J/\log X),\qquad
O_\eta(X^\eta/T),\qquad O(H^{-1}).
\]
Every term has been accounted for. For the general parameter range, \(Q/H\to0\), \(J(\theta-\rho)>\rho\), and \(\theta+2\rho-2<3\theta-2\le-1/3\). A fixed sufficiently small \(\varepsilon\) makes the centered RH exponent negative.

For \(\rho=2/5\), \(\alpha\in[7/4,9/4]\), \(J=16\), \(\varepsilon=\eta=1/100\), the exact worst-case margins are:

| Error | Positive power margin |
| --- | --- |
| Primitive discrepancy | \(2/35\) |
| Principal unit-mask completion | \(1/35\) |
| Smooth odd-cofactor completion | \(29/45\) |
| Joint centered RH error | \(158/1125\) |
| Nonprimitive prime powers | \(391/900\) |

All logarithms are fixed powers, so these margins are uniform. The scale \(\alpha=2\) lies in the interior. No owner-family restriction or 186 distribution theorem has been used to claim this wider window. No primitive complementary-cofactor completion is needed, so the older \(K/H\) restriction is absent for a valid reason.

## 9. Reproduction and evidence scope

I read the entire tiny checker before executing an unchanged temporary copy with Python 3.14.3. Only the author manuscript and checker were copied; the author directory was not used as an output directory. Both retained replay files are byte-identical to the author's final JSON/stdout, SHA256:

    16bae49bb6b405a314186fdf61bd748cd1263f32ed78599e8a5e66f70acdba3e

The eight groups contain 3,809 exact scalar cases: 200 formal-log divisor identities; 399 real-endpoint odd-Möbius identities; 200 sharp-complement identities; 1,632 primitive partitions; 160 real-endpoint hinge identities; 1,200 even-shift counts including empty ranges; 12 constant-main algebra checks; and six rational power margins. The checker uses exact integers and rational numbers. Its hinge test deliberately uses an arbitrary even coefficient sequence, verifying the identity rather than pretending to test the analytic singular-series asymptotic.

The source manifest pins 12 primary/source/dependency files and the author receipt pins six author artifacts. I checked all 18 paths, byte lengths and SHA256 hashes; every comparison passed. The detailed records and interpreter version are in [source_and_replay_checks.json](source_and_replay_checks.json). The independent outputs are [independent_exact_check_results.json](independent_exact_check_results.json) and [independent_exact_check_stdout.log](independent_exact_check_stdout.log).

These finite checks are regressions for algebra and constants. Acceptance of convergence, Poisson errors, RH transfer and uniformity rests on the ordinary proof audit above, not on sampled prime heights.

The remaining mathematical task is to estimate the signed statistic \(\mathcal Z_Q^{(2)}\) with its genuine sharp Möbius coefficient and full prime weights. This report supplies no sign estimate for that statistic. Extending a fixed compact packet to the full positive variance also requires control of the near-zero and large-length tails with the appropriate surviving endpoint terms. Those limitations are explicit in the accepted author statement.
