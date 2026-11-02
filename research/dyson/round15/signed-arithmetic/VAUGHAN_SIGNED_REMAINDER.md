# A second exact reduction: the remaining discrepancy as a signed bilinear form

Date: 2026-09-05. Status: ordinary proof submitted for independent review. This is a classical Vaughan-type identity and a Poisson estimate, checked for this programme's actual kernel. No novelty claim is made for those methods. The new usable output is a fully specified bilinear remainder, a proved untwisted Siegel–Walfisz property for its second coefficient, and an exact account of the source ranges still uncovered. No bound for that full bilinear remainder or new actual-zeta lower bound is proved.

## 1. Exact object and the proposed theorem

Keep the R14 definitions, now writing the shift cutoff as V and the two arithmetic cutoffs as A,B to avoid confusion:

\[
Q=X^{523/1000},\quad X=T^\alpha,\quad 6/5\le\alpha\le7/5,
\quad H=X/T\in[X^{1/6},X^{2/7}],
\]
\[
V\in C_c^\infty(1,2),\quad \chi\in C_c^\infty(1,3/2),
\quad a_y(X)=\min\{(y/X)^{1/2},(X/y)^{3/2}\},
\]
\[
w_h(u)=\chi(u/X)a_u(X)a_{u+h}(X)
\frac{\sin(T\log(1+h/u))}{T\log(1+h/u)},
\quad W_{h,q}(n)=w_h(n-h)\log((n-h)/q).
\tag{1}
\]
Weights are zero outside this support. In every contributing term n>h and X<n−h<3X/2; in particular X<n<2X for sufficiently large X. All prime powers are retained. For any finitely supported coefficient b define

\[
\mathcal D[b]=\sum_hV(h/H)
\sum_{\substack{q\in\mathcal Q_X\\(h,q)=1}}\mu(q)
\left[\sum_{n\equiv h\ (q)}b(n)W_{h,q}(n)
-\frac1{\varphi(q)}\sum_{(n,q)=1}b(n)W_{h,q}(n)\right].
\tag{2}
\]

The family may be the canonical complementary family or any set of distinct moduli q≤Q. Its factorization predicates are not needed for the identities and Type I removals below. They are needed if one later invokes the 186 source's distribution theorem.

Put
\[
\beta_B(m)=\sum_{d\mid m,\ d>B}\Lambda(d),\qquad
R_{A,B}=\mu_{>A}*\beta_B,
\quad \mu_{>A}(a)=\mu(a)1_{a>A}.
\tag{3}
\]

**Theorem 1.** For A,B≥1, B<X, ABQ≤X/2, and any fixed integer J≥2,
\[
\boxed{\mathcal D[\Lambda]=\mathcal D[R_{A,B}]
+O_{J,V,\chi}\!\left(HX(ABQ/X)^J\log^2X\right).}
\tag{4}
\]
Moreover, for A≤U₀ and U₀Q≤X/2,
\[
\mathcal D[\Lambda_{>U_0}]=\mathcal D[R_{A,B}]
+O_{J,V,\chi}\!\left(HX\bigl[(U_0Q/X)^J+(ABQ/X)^J\bigr]\log^2X\right),
\tag{5}
\]
where \(\Lambda_{>U_0}=\mu_{>U_0}*\log\) is exactly the signed remainder of R14. Thus (5) addresses that existing remainder, rather than replacing it by a different unexplained cutoff.

For A=B=X^{1/5}, U₀=X^{2/5}, J=4, the error in both formulas is
\[
O(X^{1711/1750}\log^2X)=o(X\log X).
\tag{6}
\]
This is a reduction to a genuine arithmetic convolution, not an estimate for it. Its two coefficients and cutoff conditions are fixed explicitly; there is no arbitrary test-function replacement.

## 2. Pointwise identity, including small n and the exact signs

Let 1 be the constant arithmetic function, ε the convolution identity, and write Λ_{≤B}(n)=Λ(n)1_{n≤B}. The classical identities μ*1=ε and 1*Λ=log give, on every positive integer,
\[
\boxed{\Lambda=
\Lambda_{\le B}+\mu_{\le A}*\log
-\mu_{\le A}*\Lambda_{\le B}*1
+\mu_{>A}*\Lambda_{>B}*1.}
\tag{7}
\]
Here \(\Lambda_{>B}\) in (7) means the simple value cutoff Λ(n)1_{n>B}, in contrast with the R14 **divisor** cutoff \(\mu_{>U_0}*\log\). Equation (3) uses the former inside β_B. This distinction is essential.

To prove (7), split μ*log at A, then write
\[
\mu_{>A}*\log
=\mu_{>A}*1*\Lambda_{\le B}
+\mu_{>A}*1*\Lambda_{>B},
\]
and substitute μ_{>A}*1=ε−μ_{≤A}*1 in the first term. At n=1 all terms are zero. Real cutoffs use the ordinary integer inequalities, including equality in ≤. No limiting approximation is involved.

On the actual support of (2), n>X>B, so the term Λ_{≤B}(n) is identically zero. The other two terms with smooth final factors are
\[
T_A=\mu_{\le A}*\log,\qquad
C_{A,B}=\mu_{\le A}*\Lambda_{\le B}*1.
\tag{8}
\]
The identity for the original R14 remainder is exactly
\[
\Lambda_{>U_0}=
\Lambda_{\le B}+R_{A,B}-C_{A,B}
+(\mu_{\le A}-\mu_{\le U_0})*\log.
\tag{9}
\]
Thus the difference between the proposed bilinear coefficient and that remainder is itself a sum of explicitly controlled smooth-cofactor expressions, with their actual signs.

## 3. The second Type I estimate, without suppressing coefficient growth

The R14 estimate directly gives
\[
|\mathcal D[T_A]|\ll_J HX(AQ/X)^J\log^2X.
\tag{10}
\]
For C_{A,B}, write n=ads with a≤A and d≤B. Its outer coefficient is μ(a)Λ(d), and its longer variable s has scale L_{a,d}=X/(ad). If (ad,q)>1, both the progression and primitive sum vanish because (h,q)=1. Otherwise the progression is a unit class s≡h(ad)^{-1} mod q, and the principal mask is (s,q)=1 exactly.

Set δ=H/X, z=h/H, and u=s/L_{a,d}. The exact smooth profile for this longer variable is
\[
\Psi_{a,d,h,q}(u)=
\chi(u-\delta z)(u-\delta z)^{-3/2}u^{-3/2}
\operatorname{sinc}_0\!\left(\int_0^z\frac{dt}{u-\delta t}\right)
\bigl[\log(X/q)+\log(u-\delta z)\bigr].
\tag{11}
\]
There is **no** log s in this profile: Λ(d) is the outer coefficient. The one log-cofactor factor has been retained. Every fixed u derivative has norm O_J(log X), uniformly in a,d,h,q and the full T-range, for the same support and denominator reasons proved in R14. Zero extension is smooth. The variables a,d are held fixed during these derivatives.

Progression Poisson summation, with \(\widehat\Psi(\xi)=\int\Psi(u)e(-\xi u)du\), gives exactly
\[
\frac{L_{a,d}}q\sum_{k\ne0}
\widehat\Psi(kL_{a,d}/q)
\left[e(kh(ad)^{-1}/q)-\frac{c_q(k)}{\varphi(q)}\right].
\tag{12}
\]
The k=0 term cancels. Since L_{a,d}≥2q, the contribution before the coefficient Λ(d) is bounded by
\[
O_J\!\left(q^{J-1}(X/(ad))^{1-J}\log X\right).
\]
Now sum **all** coefficients and variables. The elementary bounds
\[
\sum_{a\le A}a^{J-1}\ll_J A^J,\qquad
\sum_{d\le B}\Lambda(d)d^{J-1}\ll_J B^J\log(2B),\qquad
\sum_{q\le Q}q^{J-1}\ll_J Q^J
\]
and \(\sum_h|V(h/H)|\ll_VH\) give
\[
|\mathcal D[C_{A,B}]|
\ll_J HX^{1-J}A^JB^JQ^J\log X\log(2B)
\ll_J HX(ABQ/X)^J\log^2X.
\tag{13}
\]
This explicitly accounts for the logarithmic coefficient and convolution sum; no unspecified ℓ¹ norm or divisor multiplicity was discarded. Equations (7), (10), and (13) prove (4). Applying R14 also to T_{U₀}, or to their signed difference, proves (5). Neither result uses RH, dense divisibility, or prime-power removal.

For A=X^a, B=X^b, fixed a,b>0 and a+b<477/1000, put η=477/1000−a−b. Any fixed J with Jη>2/7 makes (4) negligible at scale X log X. Constants may depend on the fixed exponents and J. Nothing is uniform as η tends to zero.

## 4. The remaining bilinear form and a precise threshold

The coefficient β_B has the exact elementary properties
\[
0\le\beta_B(m)\le\sum_{d\mid m}\Lambda(d)=\log m,
\quad \beta_B(m)=0\ (m\le B),
\quad \beta_B(m)=\Lambda(m)\ (B<m\le2B).
\tag{14}
\]
The last identity follows because every proper divisor is at most m/2≤B. It includes prime powers, not only primes.

After discarding only identically zero nonunit products, the actual remaining form is
\[
\begin{split}
\mathfrak B_{A,B}(X,T)=
\sum_hV(h/H)
\sum_{\substack{q\in\mathcal Q_X\\(h,q)=1}}\mu(q)
\sum_{\substack{a>A,\ m>B\\(am,q)=1}}
\mu(a)\beta_B(m)W_{h,q}(am)
\left[1_{am\equiv h\ (q)}-\frac1{\varphi(q)}\right].
\end{split}
\tag{15}
\]
It is exactly \(\mathcal D[R_{A,B}]\). The weight forces X<am<2X, so a<2X/B and m<2X/A. The unit restrictions, signed μ(a) and μ(q), log cofactor, and continuous-scale sinc factor remain visible.

Under the fixed-power cutoff condition in §3,
\[
\mathcal D[\Lambda]=o(X\log X)
\quad\Longleftrightarrow\quad
\mathfrak B_{A,B}=o(X\log X).
\tag{16}
\]
The same equivalence holds for the original R14 remainder under (5) when both error terms are o(X log X). More generally their normalized liminf/limsup values agree, including for a specified one-sided target. This equivalence concerns the **selected smooth discrepancy**; it is not an equivalence between (16) alone and Montgomery or AH refutation.

There is a useful bounded block criterion. Partition a>A into intervals (2^jA,2^{j+1}A], and m>B similarly. Only O(log X) pairs of blocks meet X<am<2X: their lower-endpoint products lie between X/4 and 2X, leaving O(1) possible sums j+k. Write \(\mathfrak B_{j,k}\) for (15) with those two exact interval indicators. A bound
\[
\max_{\text{nonempty }(j,k)}|\mathfrak B_{j,k}|=o(X)
\tag{17}
\]
uniformly in the admitted X,T range is sufficient for (16). For example, a uniform O(X/log^cX) bound for any fixed c>0, or a fixed power saving below X, suffices. Cancellation among the blocks could prove (16) even when (17) is false, so (17) is not asserted necessary.

The earlier R9 covariance bridge shows exactly where this would enter: its aggregate selected component is the primitive support main term plus \(\mathcal D[\Lambda]\), up to O(H√X log⁴X) under RH. Replacing \(\mathcal D[\Lambda]\) by (15) adds only the proved error above. Dividing by X log T is legitimate since log X=α log T with α in a fixed compact range. The complementary divisor terms, other spatial/shift packets, the support main terms, and prime-continuum centering remain separate obligations for the compact bump. Nothing here proves their sign or the sufficient lower bounds W_T≥1/16 or ∫φF_T>7/10.

## 5. A genuine arithmetic property: untwisted β_B is Siegel–Walfisz

**Proposition 2.** Fix b₀>0 and C>0. For X^{b₀}≤B≤2M, M≤X^C, and an arbitrary interval I⊆[M,2M], the family
\[
\gamma_{B,I}(m)=1_I(m)\beta_B(m)
\]
satisfies the 186 source's Definition 2.9: for every fixed L>0,
\[
\left|\sum_{\substack{m\equiv c\ (r)\\(m,s)=1}}\gamma_{B,I}(m)
-\frac1{\varphi(r)}\sum_{(m,rs)=1}\gamma_{B,I}(m)\right|
\ll_{L,b_0,C}\tau(rs)M(\log X)^{-L},
\quad(c,r)=1.
\tag{18}
\]
The fixed divisor exponent is one, independent of L. If B>2M the coefficient is zero. Constants have the usual possible ineffectivity inherited from classical Siegel–Walfisz.

**Proof.** First retain only prime d=p in the definition of β_B and write m=kp. In both terms of (18), (k,rs)=1 is required. For each such k≤2M/B, the inner primes lie in the interval
\[
p>B,\qquad kp\in I,
\]
in one primitive class p≡c k^{-1} mod r, with the auxiliary restriction (p,s)=1. The endpoints and k are fixed while applying the prime-interval estimate. Proposition 2.10 of the primary 186 paper supplies this estimate uniformly in interval endpoints, r,s and the primitive class, at all prime scales ≥X^{b₀} up to a fixed constant factor. A dyadic split beginning at B, followed by partial summation for log p, gives a bound
\[
\ll_{L'}\tau(rs)\frac{M}{k}(\log X)^{-L'}
\]
for every fixed L′. Subintervals that are empty contribute zero; no prime below the cutoff is introduced. Summing k harmonically costs O(log X), which is absorbed by choosing L′>L+1. This proves (18) for the prime part, with the same fixed τ-exponent.

For clarity, the auxiliary restriction is not being dropped: prime factors of s are excluded inside the source estimate. The elementary proof of its uniformity removes at most τ(s) primes for each k, at a possible total cost O(τ(s)M B^{-1}log X), which is below the right side for every fixed L because B is a fixed power of X.

The prime-power part is bounded absolutely in both discrepancy terms. The elementary bound
\[
\sum_{p^\nu\le Z,\ \nu\ge2}\log p\ll\sqrt Z\log^2(2Z)
\]
gives, uniformly in endpoints,
\[
\sum_{k\le2M/B}\sum_{p^\nu\le2M/k,\ \nu\ge2}\log p
\ll M B^{-1/2}\log^2X.
\tag{19}
\]
This is o(M log^{-L}X) for every fixed L. The principal multiplier is at most one, so no extra factor arises. This proves the full Λ-divisor statement. Finally |γ|≤log(2M) makes it a coefficient sequence in the source's Definition 2.6, uniformly for M≤X^C. ∎

Only a classical **untwisted** distribution property is proved. It does not assert (18) for γ(m)e(am/d) with conductor d near X^.523. On the first interval B<m≤2B, β_B=Λ exactly, so there is no new algebraic smoothing that could justify automatic inheritance of the twisted property. The R12 phase-absorption audit remains relevant. This note does not claim its selected bad outer residue necessarily has μ(a)≠0 in every long interval, or infer a lower bound for the full form from such a pointwise example.

## 6. Asymmetric cutoffs: one real advantage and the uncovered corners

At source parameters ω=.012, δ=.001, choose σ=.101. The three Proposition 2.18 inequalities have left sides .888, .996 and .990. Its SW-bearing variable must have **scale** N in [X^.399,X^.5]. The limiting lower exponent .398 is not attained by these strict source inequalities: allowing σ to approach .102 from below only permits an exponent strictly above .398.

The symmetric choice A=B=X^.2 gives a clean four-derivative error and leaves β_B at scales from approximately X^.2 to X^.8. Proposition 2.18's coefficient and length premises are established here only for the blocks where the β_B scale lies in [X^.399,X^.5]. The smaller β scales are below its range. For larger β scales, swapping the two factors would require an independent SW statement for the Möbius interval coefficient; this note does not assume or prove that extra input. Even with such a statement, blocks with one scale below X^.399 remain outside the stated source range.

An asymmetric choice gives a limited improvement in the range bookkeeping:
\[
A=X^{7/100},\quad B=X^{2/5},\quad AB=X^{47/100}.
\]
Then (4), or (5) with the earlier U₀=X^.4, has error
\[
O_J(HX\,X^{-7J/1000}\log^2X).
\]
Choosing J=41 gives exponent
\[
1+2/7-41(7/1000)=6991/7000<1.
\tag{20}
\]
All nonzero β_B scales now start at exponent .4 (up to fixed dyadic constants), which eventually exceeds the .399 lower threshold. The blocks with that scale at most X^.5 meet the tested length and untwisted SW premises. But β_B may have scale as large as X^.93. Every block above X^.5 remains unhandled by this direct orientation. A hypothetical factor swap could cover only the part where the Möbius scale is also at least X^.399, corresponding to β scales at most about X^.601; the much longer corner still fails the length condition.

Thus asymmetry removes the small-β corner from the bookkeeping, but creates a wider possible large-β corner. It is not a proof that the new choice improves the actual aggregate estimate. The cutoff condition a+b<.477 cannot force **both** variable cutoffs above .399: that would require a+b≥.798. Even at the strict limiting source edge it would require a+b>.796. This is a precise limitation of this direct cutoff/Poisson/source combination, not a no-go theorem for Vaughan identities or averaged dispersion.

Furthermore a per-shift source estimate O_L(X log^{-L}X) still sums to HX log^{-L}X. It does not reach X log X at H≥X^{1/6}. The algebra and SW result identify legitimate coefficients for a subsequent **shift-averaged** bilinear argument; they do not remove that aggregate loss or legalize an absorbed additive phase.

## 7. Exact actual-integer witnesses: the new remainder has both signs

Nonnegativity of β_B does not make R_{A,B} nonnegative. This is visible on actual integers, independently of any random model or functional-norm example.

Take X=10^{10}, A=B=100=X^{1/5}, H=100=X^{1/5}, T=10^8, and h=150. Then α=5/4 is in the admitted range. Choose χ positive near the two ratios below and V positive at 3/2. All displayed n obey X<n−h<3X/2. Their sinc arguments are between 0 and 3/2, hence positive. These facts only place the coefficient examples on legal support; they do not determine the sign of the complete progression discrepancy.

For a product n=pq of two distinct primes p,q>100,
\[
R_{100,100}(pq)=-\log p-\log q<0.
\tag{21}
\]
For n=pqrs with p>100, q,r,s≤100, and each of qr,qs,rs greater than 100, only p can contribute to β_B. Thus
\[
R_{100,100}(pqrs)
=\log p\sum_{\substack{a\mid qrs\\a>100}}\mu(a)
=(3-1)\log p=2\log p>0.
\tag{22}
\]
The explicit negative witness is 100003·120011=12001460033, giving R=−log100003−log120011. The explicit positive witness is 50021·59·61·67=12061713793, giving R=2log50021; here 59·61, 59·67 and 61·67 all exceed 100. The adjacent script checks every asserted prime by trial division, verifies these equalities as formal logarithm identities, and verifies the actual support inequalities using rational arithmetic. It never replaces a signed block by its positive portion. On prime n itself, R_{A,B}(n)=0 for A,B≥1: a prime has no factorization with both a>A and m>B. The Type I removal therefore reorganizes prime/composite cancellation rather than retaining a literal positive tail of primes.

The positive construction also has an asymptotic shape: choose the three small primes near X^.18 and the large prime near X^.46, with fixed multiplicative constants placing their product in the support. The negative semiprime shape uses two primes near X^.5. This observation is not needed for the finite certificate and is not promoted to an averaged lower bound.

## 8. Evidence, sources and next precise obligation

The finite check uses independent formal symbols for log p. For each n=1,…,4096 and cutoff triples (A,B,U₀)=(2,3,6), (5/2,9/2,45/4), (7,5,35), it verifies (7), (9), an independently enumerated ordered (a,d,s) expansion of the bilinear coefficient, and the prime-factor formula for β_B: 49,152 exact equalities. It also checks the prime-input zero identity, the first-block identity in (14), and both signed support witnesses. Exact rational arithmetic checks the cutoff margins, source inequalities and source-length gap. These checks supplement the ordinary proofs; they do not verify SW numerically, realize the enormous complementary family, or estimate actual zeta zeros.

Reproduction uses only Python’s standard library. In this directory run `python3 check_vaughan_remainder.py`; `vaughan_checks.json` records exact coefficients, rational margins and source hashes, and `vaughan_checks.log` records the successful execution. For a temporary copy, pass `--research-base` pointing to the unchanged original research base. `AUTHOR_RECEIPT.json` pins the frozen author artifacts. Independent mathematical review is kept separately in `../signed-arithmetic-review/INDEPENDENT_VAUGHAN_REVIEW.md`; its scope and hashes are not inferred from the numerical checks.

Primary source for the SW and dispersion conventions: *Improved short gaps between primes*, Definitions 2.6–2.9, Proposition 2.10 (printed pp.6–7), and Proposition 2.18 (pp.10–11), [pinned PDF](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf). The local PDF/text SHA-256 values and the frozen R9/R12/R13/R14 dependencies are in the certificate. No unproved transfer of a model spectrum is used.

The next exact mathematical problem is to estimate (15), or a stated block family from (17), with the actual μ(a), β_B(m), coherent shift interval and primitive subtraction. The R13 rational-core extraction supplies a way of isolating selected phase ranges, but its large positive subsum is not a bound for this full signed form. A useful new estimate would beat the present X^1.023 bound for the original selected smooth discrepancy, or directly provide its needed signed covariance contribution. This report proves a new explicit reduction and coefficient property, not that estimate or a famous conjecture.
