# Independent review of the actual mixed-moment direction test

Date: 2026-09-05. Reviewer: Plato, independent of author Aquinas.

**Decision: accepted after the stated corrections, as an ordinary mathematical proof and source/direction audit.** Final author provenance and the unchanged tiny-check replay have been verified. The mixed lemma, the new smooth pure-moment lemma and the inequality-direction conclusions are accepted in their stated scope. No amendment remains requested.

The report reviewed is [MIXED_MOMENT_DIRECTION_TEST.md](../mixed-moment-test/MIXED_MOMENT_DIRECTION_TEST.md). The purpose is to distinguish estimable one-prime mixed terms and pure divisor terms from the still unbounded genuine-prime quadratic remainder. No strict actual variance bound or AH refutation is established.

The frozen author file is 21,089 bytes, SHA256:

    b338a3210061055f6ad5899fd168175ba2c85d6225f80f71e6cd48098923cdc5

Its AUTHOR_RECEIPT.json is SHA256:

    050a9b3beafaecbc4cc474ab7024522329ba540333500781d63fe9c8976be757

The author corrected the derivative order, qualified the positive composite witness, and incorporated the independently matching smooth pure-moment calculation as Lemma 2 before this freeze. I read those final deltas. Five latent control-byte instances in the author's LaTeX were also repaired before freeze; the final file is free of unexpected control bytes. No author file was edited by this reviewer.

## 1. Exact coefficient mapping and support

Three different objects must not share one name. On odd \(m\), the actual small-divisor coefficient is
\[
A_Q(m)=\sum_{\substack{d\mid m\\d\le Q}}\mu(d)\log(m/d).
\]
The standard Goldston–Yildirim logarithmic approximant and the sharp Möbius divisor sum are
\[
\Lambda_Q(m)=\sum_{\substack{d\mid m\\d\le Q}}\mu(d)\log(Q/d),
\qquad D_Q(m)=\sum_{\substack{d\mid m\\d\le Q}}\mu(d).
\]
The author denotes the latter \(B_Q\), which is harmless once explicitly defined. The finite identity is
\[
A_Q(m)=\Lambda_Q(m)+\log(m/Q)D_Q(m),\qquad
c_Q(m)=\Lambda(m)-A_Q(m).
\]
It follows just by splitting each logarithm, for every real \(Q\ge1\), with no limiting theorem. In particular the coefficient of \(D_Q\) is not small in the actual range. A correlation theorem for \(\Lambda_Q\) cannot be relabelled one for \(A_Q\), nor can its error be differentiated without a separate uniform derivative theorem.

For a prime \(p>Q\), only \(d=1\) occurs in \(A_Q\), so \(A_Q(p)=\log p\) and \(c_Q(p)=0\). For \(p\le Q\) the same conclusion follows from the full two-divisor identity. For a power \(p^a\), the result is zero when \(p\le Q\); when \(p>Q\), it is \((1-a)\log p\). These are exact statements, including \(a=1\). They do not remove higher powers from the actual covariance.

The two mixed-sign witnesses share the real cutoff \(Q=150^{1/3}\), and \(5<Q<6\) is certified by integer cubes. At \(m=195=3\cdot5\cdot13\), the small divisors are \(1,3,5\), giving \(A_Q=-\log13\) and \(c_Q=\log13\). At \(m=183=3\cdot61\), they are \(1,3\), giving \(A_Q=\log3\) and \(c_Q=-\log3\).

I requested that the generalization of the positive witness be qualified. It holds for \(m=pqr\) with distinct primes \(p,q\le Q<r\) and \(pq>Q\). Two small factors whose product exceeds \(Q\), without the large third factor, do not suffice: \(m=pq\) gives \(c_Q=0\). The author has inserted the needed conditions. These witnesses concern the coefficient, not the sign of a full global packet.

## 2. The actual mixed lemma and the corrected Poisson order

Fix one genuine R26 packet with height scale \(X\), shift scale \(Y\), \(Q=Y^{2/3}\), and amplitude \(A=(X\ell^2)^{-1}\). Its full smoothness is already proved in R26. Its support has \(m,n=m+h\asymp X\), \(Y/X=O(\ell/T)\), and \(Q<X/2\). Uniformly over the finite family,
\[
2Q\le X^{2/5}
\]
eventually; the exponent \(10/27<2/5\) at the upper natural scale has a fixed margin which absorbs the logarithmic endpoint inflation.

Expanding \(A_Q(m)\) is finite. Odd \(m\) divisible by odd \(d\) means \(m\equiv d\pmod{2d}\). Thus for even \(h\), the genuine prime endpoint lies in the unique class
\[
n\equiv h+d\pmod{2d}.
\]
This is primitive precisely when \((d,h)=1\), and its prime density is \(1/\varphi(2d)=1/\varphi(d)\). The continuous odd-cofactor density, in contrast, is \(1/(2d)\).

The two smooth functions \(F(n-h,h)\log(n-h)\) and \(F(n-h,h)\), with the second multiplied by \(-\log d\), give a common-weight partial-summation norm \(O(\log X/(X\ell^2))\). Ordinary Bombieri–Vinogradov below the square-root threshold supplies a logarithmically arbitrary error after summing primitive moduli. For each fixed \(h\) this is \(O_A(\ell^{-A})\), after choosing its fixed source logarithmic saving sufficiently large. Summing the \(O(Y)\) shifts costs \(O_A(Y\ell^{-A})\).

This application requires no phase-twisted prime coefficient. The progression class may depend on \(h,d\), since the source takes maxima over primitive classes. The physical \(m\)-interval can be covered by a fixed number of dyadic intervals; the common smooth weight and exact shifted endpoint are retained on each.

For nonprimitive classes, \(n=p^a\) with odd \(p\mid h,d\), \(a\ge2\). The fact \(Q<X/2<n\) rules out a genuine prime endpoint. The exact even-shift count is \(O(Y/p)\), including empty ranges, and there are \(O(1)\) relevant powers per base in a fixed-ratio height interval. Summing the absolute divisor coefficient once gives \(\ll_\eta X^\eta\log X\), while the endpoint weight is \(\log p\). Thus the entire debt is \(O_\eta(X^\eta Y/X)\). Neither \(Y>\sqrt X\) nor coprimality of two factors is assumed.

The flat center is completed on \(m\equiv d\pmod{2d}\). Here I found and requested a derivative-order correction: **three derivatives**, not two, give
\[
\sum_{m\equiv d\ (2d)}f(m)
=\frac1{2d}\int f(m)\,dm
+O\!\left(A_f(d/X)^2\right)
\]
for a smooth \(X\)-scale weight of amplitude \(A_f\). Indeed the nonzero Fourier frequencies contribute
\[
\frac{A_fX}{d}\sum_{k\ne0}\left(\frac d{X|k|}\right)^3
\ll A_f(d/X)^2.
\]
Two derivatives would yield only \(O(A_fd/X)\). The actual packet has every fixed derivative, so the corrected order is legal and changes no displayed bound in the lemma. The author has made the correction.

Multiplying its density \(1/(2d)\) by the center factor \(-4\) gives \(-2/d\). Together with the original prime factor two, this verifies the exact main
\[
2\sum_{h\ {\rm even}}\int F(m,h)
\sum_{\substack{d\le Q\\d\ {\rm odd}}}
\mu(d)\log(m/d)
\left\{\frac{1_{(d,h)=1}}{\varphi(d)}-\frac1d\right\}\,dm.
\]
The corrected flat-grid error after all \(d,h\) is \(O(YQ^3/(X^3\ell))\). Therefore the author's Lemma 1, with its stated \(Y\ell^{-A}\), \(X^\eta Y/X\) and flat-grid errors, is an unconditional valid estimate.

## 3. Primary source scopes and mean normalization

I checked the relevant primary text, not just the coordinator's summary:

* GY I, arXiv:math/0111212v1, defines the logarithmic \(\Lambda_R\). Its printed page 7, Theorem 1.3, has shift bound \(\max|j_i|\ll R^{1/k}\) and cutoff upper bound \(N^{\min(\vartheta/(k-1),1/k)-\epsilon}\). Theorem 1.4 has \(\max|j_i|\ll R^\epsilon\) and \(N^\epsilon\ll R\ll N^{\vartheta/(k-1)-\epsilon}\). Neither is directly a theorem for \(h\asymp Q^{3/2}\) in the actual family.
* GY II, arXiv:math/0412366v1, defines the different coefficient
  \[
  \lambda_R(n)=\sum_{r\le R}\frac{\mu^2(r)}{\varphi(r)}
  \sum_{d\mid(r,n)}d\mu(d).
  \]
  Theorem 2 on printed page 8 requires both \(N^\epsilon\ll R\ll N^{\vartheta/(k-1)-\epsilon}\) and \(\max|j_i|\ll N^{1/(k-1)-\epsilon}\). Ordinary Bombieri–Vinogradov supplies \(\vartheta=1/2\). Its \(k=2\) case covers the natural power-sized \(R=Q\) range for its own coefficient; it does not cover the smallest polylogarithmic cutoffs.
* GY II equations (4.9) and (5.6), on printed pages 19 and 20, contain the explicit \(Nh^*\tau(h^*)/(R\varphi(h^*))\) error; the pure correlation also has \(O(R^2)\). The negative-shift orientation in (5.3)–(5.4) has an endpoint debt bounded by \(O((R+|h|\log^2R)\log|h|)\). On the actual natural ranges, \(h\ll X^{5/9+o(1)}\) and \(R\ll X^{2/5}\), this is absorbed by \(X\log^{-A}X\) for every fixed \(A\). This absorption is range-dependent, not automatic at arbitrary shifts.
* For \(k=3\), the unconditional cutoff must be below \(X^{1/4-\epsilon}\), whereas the natural \(Q\)-exponent is at least \(2/7\). The theorem's shift bound is also below \(X^{1/2-\epsilon}\), failing at and above the central natural scale. A smaller auxiliary cutoff would require a new comparison estimate.
* The later GY II Theorem 3, printed page 9, assumes GRH and treats \(h\ll N^{1/7-\epsilon}\). It does not supply a substitute ordinary-RH bound for the present interval lengths.

The primary [GY I](https://arxiv.org/pdf/math/0111212v1) and [GY II](https://arxiv.org/pdf/math/0412366v1) versions above are the locally retained versions. The coordinator separately read the published version of Paper I; this review does not assume identical numbering or silently identify those versions.

I also checked the retained short-gaps paper's Propositions 2.12 and 2.15. Only its ordinary below-one-half prime case is used. Its discrepancy convention may center on the prime weight in unit classes, whereas the mixed lemma uses the continuous mean. This conversion is harmless but worth making explicit: ordinary PNT with arbitrary fixed logarithmic saving controls the difference between the full prime-power prefix and its continuous mean; summing \(1/\varphi(q)\) loses only logarithms. Excluding nonunit powers from that principal costs at most a fixed power of logarithms after summing \(\tau(q)/\varphi(q)\). With the common smooth-weight norm, both debts are absorbed by the lemma's freely chosen fixed logarithmic saving. Equivalently GY II (1.41)–(1.42) already states the primitive progression error relative to \(x/\varphi(q)\).

No stronger 186 distribution range, two-genuine-prime theorem, GRH assumption or differentiability of an unspecified asymptotic error is being imported.

The final author also explicitly charges restriction of the GY II mixed formula to odd \(m\): for even \(h\), deleted genuine-\(\Lambda\) endpoints are powers of two. I checked GY II (1.30), which proves \(\lambda_R(n)\ll\tau(n')\log(2R)\), with \(n'\) the product of relevant distinct prime factors and \(\tau(n')\le\tau(n)\). There are \(O(1)\) powers of two in each fixed-ratio endpoint block. Their total over shifts and the actual normalized packet is \(O_\eta(X^\eta Y/X)\), as claimed. Higher odd prime powers are not deleted by this parity restriction.

## 4. Which displayed classical errors actually fail

At the natural length \(Y=X/T\), a per-shift \(X\log^{-A}X\) error becomes \(O(Y\ell^{-A-2})\) after the actual amplitude and shift count. No fixed \(A\) makes this vanish for polynomial \(Y\). Increasing \(A\) with \(T\) is not permitted by a theorem whose implicit constants depend on \(A\).

The explicit \(X/R\) source error gives
\[
\frac1{Q\ell^2}\sum_{h\asymp Y}
\frac{h^*\tau(h^*)}{\varphi(h^*)}.
\]
The scale of this available positive majorant is at least \(Y^{1/3}/\ell^2\) when the extra factors are merely replaced by one. This is not a lower bound on the actual error. It says that this particular stated source estimate is insufficient after the required summation.

The crude \(O(Q^2)\) pure-correlation estimate, and its elementary logarithmic analogue, also give nonvanishing upper error budgets in some height ranges. However, this latter problem can be repaired by exploiting the actual smooth weight. It must not be recorded as a structural obstruction to evaluating pure divisor moments. The next section gives the repair explicitly.

The global \(\mathcal Z_T=O(1)\) is already inherited under RH from R26 and the R20 positive variance bound. I checked R20 equations (5)–(7): \(0\le\liminf\overline V_T\le\limsup\overline V_T\le A\), with the same fixed bump. Thus \(-2M\le\liminf\mathcal Z_T\le\limsup\mathcal Z_T\le A-2M\) is valid. Growing local error bounds neither contradict this fact nor provide a new lower bound on its true size.

## 5. Independent refinement: the actual pure finite-divisor moment has a summable smooth error

This section is a separate elementary calculation by the reviewer, not a claim taken from Goldston–Yildirim. It shows why the crude CRT debt should not be treated as the main barrier.

For one actual packet define
\[
\mathscr P_F=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)A_Q(m)A_Q(m+h).
\]
Expand both finite divisor sums. For odd \(d_1,d_2\le Q\), the congruences \(d_1\mid m\), \(d_2\mid m+h\) are compatible exactly when \(g=(d_1,d_2)\mid h\). In that case they select one residue modulo \(l=[d_1,d_2]\). Since \(l\) is odd, its odd representatives form one class modulo \(2l\).

For each fixed \(h\), the smooth weight
\[
f_{d_1,d_2,h}(m)
=F(m,h)\log(m/d_1)\log((m+h)/d_2)
\]
has amplitude \(O(X^{-1})\) and each fixed derivative has the corresponding \(X\)-scale bound. The two logarithms cancel the \(\ell^{-2}\) normalization at this coarse upper-bound level. Since \(l\le Q^2\ll X\), Poisson summation with three derivatives gives
\[
\sum_{m\equiv a\ (2l)}f(m)
=\frac1{2l}\int f(m)\,dm+O(l^2/X^3).
\]
The estimate is uniform in all compatible classes and actual packet indices. No relative primality of \(d_1,d_2\) or cancellation of their Möbius signs is assumed.

Multiplication by the ordered-pair factor two leaves the exact finite main
\[
\boxed{
\sum_{h\ {\rm even}}\int F(m,h)
\sum_{\substack{d_1,d_2\le Q\\d_1,d_2\ {\rm odd}\\(d_1,d_2)\mid h}}
\frac{\mu(d_1)\mu(d_2)}{[d_1,d_2]}
\log(m/d_1)\log((m+h)/d_2)\,dm.}
\]
There are at most \(Q^2\) divisor pairs and \(O(Y)\) shifts. Bounding \(l^2\le Q^4\) gives the unconditional remainder
\[
\boxed{O(YQ^6/X^3)=O(Y^5/X^3)}
\]
for \(Q=Y^{2/3}\).

Now use the actual R26 scales, without extending them. The \(Y\)-sum is geometric up to \(O(RX/T)\), and the \(X\)-sum is geometric up to \(8U\):
\[
\sum_{i,j}\frac{Y_j^5}{X_i^3}
\ll \frac{R^5}{T^5}\sum_i X_i^2
\ll \frac{R^5U^2}{T^5}
=O(\ell^5T^{-1/2}).
\]
All derivative orders are fixed, and R26's uniform smoothness already controls the moving cutoff derivatives. This is a fully proved summable-error evaluation of the finite pure main, not an asymptotic simplification of that main to a singular series.

It does not evaluate the genuine-prime mixed error, make an off-diagonal kernel positive, or upper-bound a residual norm. The author was informed of this distinction and incorporated the same calculation as final Lemma 2. I independently checked its compatibility condition, density, three-derivative bound and global exponent. A remaining obstacle should be stated in terms of those actual missing arithmetic or inequality inputs, not the avoidable crude pure-moment completion error.

## 6. Positive interval features, their Gram kernel, and the direction of projection

The actual positive Hilbert measure is
\[
d\mu_T(\lambda,x)=\frac{T}{\ell^2}e^{-\lambda}
\omega(\log x/\ell)\frac{dx}{x^2}\,d\lambda.
\]
With the exact interval \((x,e^{\lambda/T}x]\) and exact continuous center, the variance vector \(U_T\) satisfies \(\|U_T\|^2=\overline V_T\). For a fixed finite \(R=R(T)\), the feature defined using \(A_R\) and that same interval and center is legitimate.

For each fixed \(T>2\), the \(x\)-support is compact and a finite-divisor interval sum grows at most like \(C_{R,T}xe^{\lambda/T}(1+\lambda)\). Squaring and multiplying by \(e^{-\lambda}\) is integrable because \(1-2/T>0\). Thus the stated Hilbert identities have their required finite norms. There is no claim here of an absolute series interchange at \(T=2\).

For real \(a\),
\[
\|U_T\|^2=2a\langle U_T,V_R\rangle-a^2\|V_R\|^2
+\|U_T-aV_R\|^2.
\]
Optimizing the known part gives a lower bound. For several features, the exact Gram nullspace is orthogonal to the mixed vector, so the pseudoinverse formula is valid even without invertibility:
\[
\|U_T\|^2=v^*G^\dagger v+\|U_T-PU_T\|^2.
\]
No upper bound on the last term follows from positivity. This agrees with GY I's own printed page 8 calculation following (1.33), which uses the nonnegative difference square to lower-bound the prime second moment.

The author's indicator Gram kernel is also correct. For two indices, the allowed interval center has \(x<\min(m,n)\), and the \(\lambda\)-tail starts at \(T\log(\max(m,n)/x)\). Integration of \(e^{-\lambda}\) therefore gives
\[
K_T(m,n)=\frac{T}{\ell^2}\max(m,n)^{-T}
\int_1^{\min(m,n)}\omega(\log x/\ell)x^{T-2}\,dx.
\]
This is \(b_T(\min(m,n))(\min/\max)^T\), including the diagonal and the correct ordered off-diagonal factor two. Endpoints of the \(x\)-integral have zero Lebesgue mass.

The actual global \(Q_j\), however, depends on pair separation. It cannot be inserted as a single fixed sequence inside every interval feature. A scale-indexed Hilbert construction would require all cross-scale entries and an exact reconstruction argument. The scalar partition of an off-diagonal shift sum is not such a reconstruction.

Likewise, a nonzero symmetric off-diagonal packet with zero diagonal is not automatically positive semidefinite: the two-by-two principal minor associated with one positive edge has determinant \(-f^2<0\). This finite matrix observation identifies a failure of that proposed Gram interpretation. It is not a point-process countermodel or an impossibility theorem for other methods.

## 7. Accepted outcome and exact remaining requirement

After the derivative-order and factor-condition corrections, the author's unconditional mixed estimate is valid. The actual coefficient mapping, prime vanishing, both finite sign witnesses, source ranges, exact positive Hilbert identity and projection direction are also correct. The independent pure-moment refinement above removes one unnecessarily weak numerical error budget.

Even perfectly known mixed and pure moments leave the coefficient of the genuine shifted product \(\Lambda(m)\Lambda(m+h)\) equal to one in the actual remainder. In the positive interval formulation, an upper variance bound additionally needs an upper bound on the orthogonal residual energy with sufficient absolute accuracy, on a common subsequence. In the actual scale-dependent formulation, the unresolved sufficient condition remains
\[
\liminf_{T\to\infty}\mathcal Z_T\le1-2M.
\]
The results reviewed here establish neither condition. A strict bound could still come from a new arithmetic residual estimate or a different proved identity; the present projection calculation alone gives the opposite inequality direction.

## 8. Final bounded reproduction and source record

All nine source/dependency entries and seven author-artifact entries were checked against actual bytes and SHA256 hashes; all 16 comparisons pass. The coordinator's bounded intake is retained as a byte-identical context copy in the review's sources folder. Its selected-source scope is preserved; this review does not claim to have audited either GY paper in full.

I read the final checker before running an unchanged copy in a temporary directory, using Python 3.14.3 and SymPy 1.14.0. Its 15 exact scalar/formal-log assertions pass. The independent JSON and captured stdout are both byte-identical to the author output, SHA256:

    eb7a4b73d8e4bf867e299c7517d1fc7242c4c0720dda195557a3f0d6a0920584

These checks cover the polarization algebra, finite sign formulas, cutoff inequalities and rational exponents, including the new pure-moment exponent \(-1/2\). They are small regression checks, not computational proofs of Bombieri–Vinogradov, smooth Poisson estimates or any unknown correlation bound.

The full records are [source_and_replay_checks.json](source_and_replay_checks.json), [independent_mixed_moment_checks.json](independent_mixed_moment_checks.json) and [independent_mixed_moment_checks.log](independent_mixed_moment_checks.log). No prime-height scan, large numerical experiment or new asymptotic assumption is part of this review.
