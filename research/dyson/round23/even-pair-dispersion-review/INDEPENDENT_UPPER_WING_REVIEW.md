# Independent review of the R23 upper-wing shift completion

Reviewer: Plato (the residual-gram agent), 2026-09-05. Status: **accepted as an ordinary proof of the stated component estimates**. No author amendment is requested. This review is independent of Euclid's author lane. It checks the whole mathematical report and the identified primary-source hypotheses; it does not constitute a new proof of the 186 paper itself.

The reviewed author report is [UPPER_WING_SHIFT_COMPLETION.md](../even-pair-dispersion/UPPER_WING_SHIFT_COMPLETION.md), 18,339 bytes, SHA256 `2ff5ea968ea2adc76d40fc81a65c23cba5b143593e61c71bbc5c5f30ffc0a1a5`. The initially read draft and the author's subsequently frozen version are byte-identical. The author's final receipt is SHA256 `4af1a6589b091442935c42ff5c4ba9619199b983ae046d4d88013841b504b239`. Thus this acceptance is final for that version, rather than provisional on unfinished provenance. The historical “submitted for independent review” wording in the author report is unchanged.

## 1. What is accepted

Put \(\ell=\log T\), \(X=T^\alpha\), \(H=X/T\), \(Q=X^{523/1000}\), with \(11/5\leq\alpha\leq9/4\). The report retains the exact Pareto factor \((m/(m+h))^T\), the original normalized radial mass \(b_T(m)\), and fixed compact smooth cutoffs \(\chi(m/X)V(h/H)\). For its full canonical odd divisor family, the two removed terms satisfy

\[
|\mathcal B_{\mathcal D}|\ll X^{-7/440}/\log X,
\qquad
|\mathcal N_{\mathcal D}|\ll X^{-15041/45000}.
\]

The proof is unconditional. The first estimate is smooth completion of a zero-mean periodic function of the **physical shift**, followed by the elementary bound \(\sum_{n\leq3X}\Lambda(n)\ll X\). The second uses a prime-factor consequence of the actual owner constraints. Neither estimate requires a new prime-distribution exponent, an unproved phase-twisted Siegel–Walfisz property, or RH. RH enters only through the separate earlier identification with the zeta variance.

The resulting exact target is

\[
\mathcal P_{T,X}^{\chi,V}
=\mathcal A_{\mathcal D}+\mathcal C_{\mathcal D}
-\mathcal M_{\mathfrak S}+o(1).
\]

No estimate for this surviving signed expression has been established. In particular this report does not prove a strict variance inequality, a Bragg deficit, or a refutation of AH.

## 2. Full divisor family and owner constraints

I compared author Section 2 with the frozen R11 conductor report, Section 1, and with Definition 2.1, Lemma 2.2 and Proposition 2.3 on printed pp.4–5 of the primary 186 paper. The relevant source and programme files are pinned in the author's source manifest and were checked against their current bytes.

The family counts each distinct odd squarefree \(d=[D,E]\) once. The coefficient used in the divisor identity is \(\mu(d)\); it is not multiplied by the number of owner representations and is not selected according to its sign. The bounds \(D,E\leq X^{523/2000}\) give \(d\leq Q\), while the lower bound is \(d>X^{1/2}\). The balanced owner budget is \(X^{501/2000}\) on each side, whose product equals \(X^{1/2}Y\), \(Y=X^{1/1000}\). This is Proposition 2.3 with its threshold variable equal to the present \(X^{1/2}\), not the present \(X\).

For the symmetric choice \(f(p)=g(p)=p^{3/2}\), each missing opposite-root guard follows directly from the displayed owner bound: the owner tail is at least one. No coprimality of the two owners is needed. These checks establish the claimed triple dense divisibility. They do not use the invalid rule that arbitrary divisors retain the same density budget.

The stronger consequence needed for prime powers is also valid for every member of this family. If \(p>Y\) occurs in an owner, its tail is at least \(p\), so

\[
p^{5/2}\leq X^{501/2000},\qquad
p\leq X^{501/5000}.
\]

For \(p\leq Y\) the same conclusion is immediate. The report correctly does not transfer this bound to an arbitrary squarefree modulus at most \(Q\). The older explicitly counted subfamily only justifies nonemptiness; it is not being substituted for the full divisor family in the proof.

## 3. Five-term identity and all centers

I independently checked the kernel identity by its two gcd cases. If \((h,d)=1\), congruence forces \((n,d)=1\), and the primitive subtraction plus principal add back to the progression indicator. If \((h,d)>1\), the primitive kernel is zero: a unit \(n\) cannot be congruent to \(h\), and a nonunit \(n\) is removed by the outer unit mask. The nonprimitive indicator then supplies precisely the original progression. Thus author equation (15) is exact for every integer pair, with neither a statistical approximation nor an omitted exceptional set.

Inserting this identity into

\[
\Lambda(m)=\sum_{d\mid m}\mu(d)\log(m/d)
\]

gives exactly the three selected-family terms \(\mathcal B,\mathcal A,\mathcal N\), plus the complementary-divisor term \(\mathcal C\). The original subtraction \(\mathfrak S(h)(\Lambda(m)+\Lambda(m+h)-2)\) is unchanged. Consequently the five-term opening preserves both prime marginals, their singular-series weights, and the parity constant two. The complementary term retains its signed coefficient and the logarithm of the actual cofactor.

The compact supports enforce \(X<m<2X\), \(H<h<2H\), and \(X<n<2X+2H<3X\). The switch \(n=m+h\) preserves odd \(m,n\) and even positive \(h\). In these finite sums the zero extension of the cutoffs makes writing all even shifts harmless. The von Mangoldt identity includes all prime powers and has value zero at \(m=1\); no prime-only replacement has been made.

## 4. Uniform derivatives of the actual weight

Author equation (22) follows from the change of variable \(x=mu\). Extending the integral to \(u=0\) is exact, because the fixed \(\omega\) vanishes at the newly added arguments. For \(m\) in the support, differentiating in \(m\) produces only powers of \(m^{-1}\), derivatives of the fixed profile, and powers of \(\ell^{-1}\). The factor

\[
T\int_0^1u^{T-2}\,du=T/(T-1)
\]

is uniformly bounded for \(T\geq4\). This proves the all-fixed-order estimate for \(b_T^{(j)}\); differentiating the unrearranged expression and keeping spurious factors \(T^j\) would not be a correct audit.

At fixed \(n\), set \(z=h/H\), \(v=(n-h)/X\). Both remain in a fixed compact region of \((0,\infty)\), and \(dv/dz=-1/T\). The exponent

\[
-T\log(1+z/(Tv))
\]

and every fixed mixed derivative in \(z,v\) are uniformly bounded. Differentiation of the true Pareto factor therefore costs \(H^{-1}\) per physical-shift derivative, with no unbounded residual power of \(T\). The logarithmic cofactor contributes at most \(O(\log X)\); its differentiated parts are smaller. All cutoff boundary derivatives vanish. Thus the bound (24), including its uniformity in the family and closed \(\alpha\)-range, is justified.

At fixed \(h\), the variation in \(n\) is instead on scale \(X\). This is the appropriate variation norm for Section 7's per-shift source application. No differentiation in the height parameter \(T\), or across a moving discontinuous family boundary, is needed anywhere.

## 5. Physical even-shift completion and the exponent

For odd \(d\) and unit \(n\), write \(h=2r\), \(a=2^{-1}n\bmod d\). The exact periodic kernel is

\[
1_{r\equiv a\bmod d}-\frac{1_{(r,d)=1}}{\varphi(d)}.
\]

Its mean is zero. With the author's negative-sign Fourier transform, Poisson summation on the grid \(h=2a+2d\mathbb Z\) gives the positive phase \(e(ka/d)\) and prefactor \(1/(2d)\). Averaging the unit grids gives \(c_d(k)/\varphi(d)\). The zero coefficient is exactly \(1-\varphi(d)/\varphi(d)=0\), not a small error. For nonunit \(n\), the original kernel vanishes identically.

Using \(J+1\) integrations by parts gives

\[
|\widehat w(\xi)|\ll_J A_XH(1+H|\xi|)^{-J-1},
\qquad A_X=\frac{\log X}{X\ell^2}.
\]

For \(H\geq d\), the nonzero frequency sum is bounded by \(O_J(A_X(d/H)^J)\). The elementary estimate \(|c_d(k)|\leq\varphi(d)\) suffices. Summing over the actual von Mangoldt sequence contributes \(O(X)\), including prime powers. Taking absolute values over the distinct moduli only now gives

\[
|\mathcal B|\ll_J\frac{Q}{\log X}(Q/H)^J.
\]

Since \(H\geq X^{6/11}\), choosing the one fixed order \(J=24\) gives

\[
24(6/11-523/1000)-523/1000=7/440.
\]

All constants remain fixed. The report correctly excludes the endpoint regime \(H\asymp Q\) and does not optimize by allowing \(J\) to grow with \(T\). A bounded-coefficient sum of \(O(\log T)\) such packets is still negligible provided their profile seminorms entering this proof are uniformly bounded. That assertion does not construct a partition of the full target or cover a sharp cutoff at zero.

## 6. Actual nonprimitive exceptions

A nonzero nonprimitive summand has \(d\mid n-h\), \((h,d)>1\), and \(\Lambda(n)\neq0\). Therefore \(n=p^j\), with \(p\mid d\). The owner constraint above forces \(p\leq X^{501/5000}\). A genuine prime \(n>X\) cannot occur. Since \(n\) is odd, the prime is odd; at most two powers of each such prime can lie in \((X,3X)\), a deliberately safe bound.

For each fixed \(n,h\), the sum of absolute divisor coefficients is at most \(\tau(n-h)\log(2X)\). There are \(O(H)\) shifts, at most \(2X^{501/5000}\) possible \(n\), and \(|F_T|\ll1/(X\ell^2)\). The additional factor \(\Lambda(n)\leq\log(3X)\) and the cofactor logarithm are absorbed by \(\ell^2\), uniformly because \(\log X/\ell\) lies in the fixed stated interval. Thus

\[
|\mathcal N|\ll_\eta H X^{501/5000-1+\eta}.
\]

With \(\eta=1/100\) and \(H\leq X^{5/9}\), the exact saving is \(15041/45000\). This is a bound on the original prime-power term, not an assertion that replacing \(\Lambda\) by primes costs zero.

## 7. Primary-source comparison and dyadic summation

I checked the retained primary text at printed pp.4–5 (family criteria), pp.6–8 (primitive discrepancy, coherence and partial summation), and p.11 (Corollary 2.19). The source expressly supplies its result for \(\Lambda\) and uniformly on subintervals. Its residue class is chosen coherently outside the modulus sum, rather than maximized independently inside that sum.

For each fixed even \(h\), the author uses exactly the legal coherent construction: retain the prime 2, remove odd primes dividing \(h\), prescribe 1 modulo 2 and \(h\) modulo the remaining primes. For the retained moduli \(2d\), the principal denominator is \(\varphi(2d)=\varphi(d)\). The unit projector is precisely \(1_{n\text{ odd}}1_{(n,d)=1}\). This matches the original kernel after restricting to odd \(n\). Terms with \((h,d)>1\) contribute zero to the primitive kernel and are not illicitly assigned a primitive class.

The factor 2 is squarefree, coprime to odd \(d\), and eventually \(Y\)-smooth, so Lemma 2.2 permits it without changing the density budget. The exact source parameters give \(240\varpi+80\delta=358/125<3\) and cutoff exponent \(5231/10000>523/1000\). The fixed positive retreat absorbs the multiplicative factor 2. Splitting the support at \(2X\) is legal: on the second interval, the density budget \((2X)^\delta\) is larger, and the same fixed cutoff margin still applies. The relevant source residue set remains coherent for each fixed shift. Uniformity of the source allows that set to depend on the shift.

The dependence on \(d\) in the weight is not passed wholesale to a theorem for one common smooth function. Splitting the cofactor logarithm as \(\log(n-h)-\log d\) leaves two common profiles, with the scalar \(\log d\) bounded by \(\log X\). Their endpoint-plus-variation norms follow from Section 4. Ordinary partial summation with the source's uniform subinterval assertion is therefore valid. This only yields an arbitrary fixed logarithmic saving for a fixed shift; after \(O(H)\) shifts it is \(H\log^{-B}X\), which is not negligible here.

The new component estimate is instead obtained by completing the shift before taking absolute values over primes and moduli. The author does not attribute this improvement to a stronger 186 distribution exponent, a Type II theorem for unverified coefficients, or an additional source estimate. Those limitations are correct and essential.

## 8. Verification receipt and unresolved mathematics

I read the entire author checker before replaying it in a disposable directory. Only the author report, checker and source-manifest bytes were copied. The replay output was retained in this review directory; the author files were not changed. The output JSON and stdout were each byte-identical to the author's frozen files, with SHA256 `04915a9ff158211d34bacf7298da6152045e39de779014c233164343f96be2de`.

The five exact groups cover the rational exponents, 7,700 primitive/principal/nonprimitive identities, 79 even-grid periods, 146 exact cyclotomic Fourier coefficients, and 12 formal-prime-log five-term identities. The checker explicitly treats its small divisor family as an algebra test, not a finite realization of the asymptotic owner family. These checks reinforce the normalization and signs; they do not experimentally establish any of the asymptotic estimates above.

All six original source/dependency hashes and all five author-file hashes listed by the two author manifests matched. The runtime was Python 3.14.3 with SymPy 1.14.0. The independent detailed verification is [source_and_replay_checks.json](source_and_replay_checks.json); the final review receipt pins this report and the replay artifacts.

The remaining principal \(\mathcal A_{\mathcal D}\) still contains \(\mu(d)/\varphi(d)\), the exact cofactor logarithm and both primitive masks. The complementary divisor term is signed. Neither has been identified with the singular-series marginals, and neither can be discarded as a positive error. Lower-height ranges, shifts near zero and non-smooth endpoints remain outside this component argument. The accepted result is a rigorous removal of two specified terms in the stated smooth packets; the actual centered quadratic bound remains open.
