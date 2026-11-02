# QRH primary-source method and applicability audit

Review date: 2026-11-01 America/Los_Angeles / 2026-11-02 UTC. Reviewer lane: `r29_close`.

**Conclusion.** OpenAI's public manuscripts state unconditional fixed zero-free half-planes for zeta and entire character families; the repository also supplies actual Lean proof modules for the 7/8 statement. This is substantially different from a zero-density bound. It does not establish RH, a zeta pair-correlation or three-point law, or the signed arithmetic estimate missing from our programme. The most relevant reusable structures are the exact conversion of Möbius coefficients into cubic-theta coefficients, carefully retained arithmetic masks, and moment estimates that keep a common character across several factors. Their applicability has to be proved with the actual coefficients and height ranges.

This is a bounded source and applicability review, not a line-by-line certification of 248 manuscript pages or a replay of the transitive Lean proof. The source read locations, exact scope, and unperformed checks are recorded below. The official repository identifies an **unnamed internal model**; these sources alone do not identify it with “Surfic” or any particular public model.

## 1. Version and claim map

Sources were retrieved from OpenAI's repository at commit

`4eaee87548250b2682affda7d05d947c05554bae`.

| Source | Exact mathematical statement relevant here | Qualification |
|---|---|---|
| [September 30 manuscript, Theorem 1.1](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), 199 pages | No zeros in `Re(s)>7/8` for finite-order Hecke L-functions over `Q(sqrt(-3))`, hence every Dirichlet L-function and zeta | Strict half-plane; principal poles at 1 allowed |
| [October 5 alternate proof, Theorem 1.1](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf), 49 pages | The same families have no zeros in `Re(s)>11/12` | A weaker numerical boundary with a different exposition/proof route; the filename is **paper2.pdf** |
| [Formalization scope, docs/003.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/003.md) | Lists the 7/8 zeta, Dirichlet, and finite-order Hecke statements, plus a uniform real-zero gap | Later arithmetic applications are excluded from the stated formalization scope |
| [Liu, arXiv:2610.12234v2](https://arxiv.org/html/2610.12234v2) | Improves the boundary to `0.874957019420098946...` using the cubic-theta estimate system | Version 2, dated October 10, submitted October 12; not the different v1 constant |

The publication announcement is [OpenAI, October 6, 2026](https://openai.com/index/sharing-ai-progress-in-mathematics/). The [repository README](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/README.md) distinguishes verification stages and notes human editing of the 11/12 exposition. An announcement date, manuscript date, version date, and our review date must not be interchanged.

Lower is stronger for the boundary of a right zero-free half-plane:

\[
0.874957019420098946\ldots < \frac78=0.875
<\frac{11}{12}=0.916666\ldots.
\]

These numbers are horizontal real-part boundaries, not proportions of zeros proved to lie on the critical line. They are also not exponents in a statement of zero-density without further interpretation.

## 2. What “uniform” does and does not mean

The top-line exclusion includes **complex zeros at every height**, not merely real exceptional zeros. Its boundary is independent of conductor and character. All positive Dirichlet moduli and characters are included, not just primitive characters or one parity. Finite omitted Euler factors are harmless in `Re(s)>0`; this explains the extension from primitive to imprimitive presentations. The Hecke statement here concerns finite-order characters over the specified Eisenstein field, not all automorphic L-functions or all number fields.

The intermediate estimates are more qualified. In the 11/12 proof, constants depend on the fixed target character, its fixed bad-prime set, support interval, and a finite number of test-function derivatives. In the 7/8 continuation criterion, the **positive exponent margins** must be independent of the target; constants, excluded primes, and sufficiently large starting scales may depend on it. That quantifier pattern is enough to contradict the supremum of zero real parts over the whole family. It is not a blanket assertion of conductor-independent constants for every auxiliary sum.

Principal poles at 1 are not zeros and are not analytically removed by the theorem. The separate formalized Siegel statement is

\[
\exists c>0\ \forall q\ge3\ \forall\chi\text{ primitive, real, nonprincipal}:\quad
L(\beta,\chi)=0,\ 0<\beta<1
\Longrightarrow (1-\beta)\log q\ge c.
\]

It does not assert that real Dirichlet zeros anywhere in `(0,1)` are impossible. The scope note supplies no explicit numerical value of `c`.

## 3. The shorter proof: what is actually being estimated

The alternate paper's Proposition 3.1 studies ideals of `K=Q(sqrt(-3))`:

\[
A_u(D)=\sum_{(\mathfrak n,S)=1}
\mu_K(\mathfrak n)\nu(\mathfrak n)
\chi_{\mathfrak n}(u)W(N\mathfrak n/D),\qquad
\chi_{\mathfrak n}(u)=(u/n)_6.
\]

For fixed `0<vartheta<=1/10` and every positive exponent loss, it states

\[
\sum_{0<N(u)\le D^{1+\vartheta}}|A_u(D)|^2
\ll_{\nu,S,I,\vartheta,\epsilon}
\left(\max_{j\le k}\|W^{(j)}\|_\infty\right)^2
D^{2+\vartheta+\epsilon}.
\tag{A}
\]

The proof uses Poisson summation in the sextic row, a Gauss–Jacobi identity absorbing the Möbius coefficient, cube completion of cubic-theta coefficients, theta reflection into quadratic twists, and the quadratic large sieve. Cube removal is justified by inversion and a finite scale-decreasing recursion, rather than by dropping nonpositive summands. Propositions 5.1, 5.2, 5.4 and §5.6 give the recursion and its initialization. [Actual TeX proof](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex).

The following elementary extraction checks the claimed exponent. For prime generators with norm about `Y=H^(1/6)`, sixth-power rows satisfy

\[
A_{p^6}(D)=A_1(D)+O_W(D/Y),\qquad H=D^{1+\vartheta}.
\]

There are order `Y/log Y` such prime ideals. Consequently (A) gives

\[
|A_1(D)|^2\ll D^{2+\vartheta+\epsilon}/Y+D^2/Y^2
=D^{11/6+5\vartheta/6+\epsilon}
+D^{5/3-\vartheta/3}.
\]

Taking a square root, then choosing positive `vartheta` sufficiently small, gives exponent `11/12+epsilon`. The parameter cannot be set to zero inside an estimate requiring a positive descent margin; it is chosen separately for each requested loss.

To check the analytic implication, fix a purported zero `rho`, and choose `W(y)=y^(-rho)phi(y)` with nonzero nonnegative smooth `phi` supported in `(1,2)`. Its Mellin transform does not vanish at `rho`. The Mellin transform of the smoothed Möbius sum is

\[
\mathcal M_W(s)=\frac{\widehat W(s)}{L_K^S(s,\nu)}
\]

initially on `Re(s)>1`. The power bound continues the left side holomorphically across `rho`, contradicting the pole on the right. This step excludes arbitrary complex zeros. It does not locate any zero on `Re(s)=1/2` or estimate relations between two zero ordinates.

## 4. The stronger proof: shared arithmetic structure, not a zero-spacing process

The September paper's Proposition 2.1 compares a physical arithmetic sum `J_eta(Z)` to a Mellin signal containing `H_eta(s)/L_K^S(s,eta)`, with `H_eta` holomorphic and bounded away from zero. Its two estimates produce a positive common continuation margin left of the hypothetical rightmost family zero. Part I reaches 11/12; Part II uses prime compensation, unequal scales, marked inverse second moments and plain fourth moments to reach 7/8. [Proof source](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), §§2, 17–20.

Two applicability restrictions are decisive. Lemma 17.1 permits a common character in a Möbius polynomial and product-form prime factors, with strict length inequalities. Lemma 17.2 explicitly disallows an arbitrary residual coefficient. Lemma 18.1 requires the existing zero-free input `beta_* <= (1+kappa)/2` when `kappa<1`. The final contradiction sets `kappa=2 beta_*-1`; it does not silently assume RH. These are estimates for arithmetic families of character sums, not a zeta multitime stochastic process.

For later transfer work, the exact marked-second-moment restrictions are

\[
r+2z\le m-c_1,\qquad 2r+8z\le3m-c_2,
\qquad c_1,c_2>0,
\]

where `r` is the inverse-polynomial length exponent and `z` the total prime-slot length. The plain fourth-moment restriction for positive prime length is

\[
n_1+n_2+6\kappa z\le M.
\]

Keeping the same character, masks and norm power across all factors is not optional. A generic oscillatory prime-error weight does not become an admissible prime-slot product merely because it is bounded.

### Dunn–Radziwill dependence

The original [Dunn–Radziwill paper](https://arxiv.org/pdf/2109.07463), arXiv v3 of May 14, 2024, makes its prime asymptotic and dispersion conclusions conditional on GRH. Its §5 and Appendix A also supply explicit theta/Voronoi identities. I checked the separate statements of Lemma 5.4 and Proposition 5.3: the displayed transformation inputs do not carry the prime-asymptotic GRH assumption.

OpenAI explicitly invokes those unconditional transformation ingredients, and states that neither Dunn–Radziwill's GRH prime asymptotic nor OpenAI's separate cubic first-moment manuscript is an input. This bounded reading therefore identifies no imported GRH premise at that interface. It is not an independent verification of every transformed cusp coefficient in the 199-page argument.

The term **cubic** here refers to cubic residue characters, Gauss sums and metaplectic theta structure. It must not be read as a theorem about three-point correlations of zeta zeros.

## 5. Lean: actual implementations, comparator targets, and review limits

The public target files under `ComparatorChallenges` intentionally contain `sorry`. The [comparator JSON](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/QuasiRiemannHypothesis.json) instead points to `OAI.NumberTheory.DirichletL.Nonvanishing` as its solution module. This distinction resolves the apparent placeholder issue.

The actual [Nonvanishing.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean) exposes:

- `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`;
- `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re`, with arbitrary positive modulus, arbitrary complex Dirichlet character, and the explicit principal-pole exclusion.

These declarations have proof terms calling `ProbeFinalAssemblyUnconditional`, rather than placeholders. The inspected chain constructs certified moment bands by finite induction, converts them to the required source moments, and then applies the final nonvanishing argument. Internal hypotheses involving the hypothetical zero supremum occur inside that contradiction/induction; the exported declarations do not assume RH or GRH. The separate Hecke comparator points to `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing`.

The comparator configurations permit only `propext`, `Quot.sound`, and `Classical.choice`; `enable_nanoda` is false. That is a configuration statement, not a claim that I independently ran either kernel or comparator. The [published checking instruction](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/README.md) is `lake env comparator ComparatorChallenges/QuasiRiemannHypothesis.json`, after its prerequisite setup.

**Checked here:** scope documentation, target signatures, solution routing, actual top-level proof terms, `FinalAssemblyUnconditional`, `FinalAssemblyCertifiedBands`, `CertifiedExistence`, and the foundation import surface. **Not checked here:** compilation, comparator execution, complete transitive axiom extraction, every analytic definition, or all foundation lemmas. The latter library is substantial; inspecting its import list is not a proof audit of its contents. The 11/12 theorem follows numerically from a valid 7/8 theorem, but that logical implication does not formally verify the alternate 11/12 manuscript's particular argument.

## 6. Liu's improvement and its precise obstruction

[Liu v2](https://arxiv.org/html/2610.12234v2), Theorem 27.1, gives

\[
B_{\rm new}=\frac{18\xi+7}{18\xi+9},\qquad
1188\xi^3-2160\xi^2+171\xi+190=0,
\quad 0.38858<\xi<0.38859.
\]

It varies the scale and moment parameters, extends the permitted moment range, and iterates using each preceding proved bound to supply the next moment hypothesis. Only real upper bounds are passed to a limit. Section 34 proves optimality within its explicitly defined exponent/contour/moment comparison system. It is not optimality among all possible cubic-theta arguments, a lower bound for actual zero real parts, or a barrier against new joint estimates. The source reports Lean formalization; its verifier was not run here.

Recomputed values:

```text
xi        = 0.3885833542660346667974279910648928173996750659354006679
B         = 0.87495701942009894612860385056145298230715187418763
7/8 - B   = 0.000042980579901053871396149438547017692848125812367190
kappa     = 0.74991403884019789225720770112290596461430374837527
```

Theorem 34.4's limitation is mathematically useful: stronger analytic estimates or a relation between simultaneous large-value events changes the comparison system. Merely searching its same parameters cannot cross its proven scalar optimum.

For an independent exact algebra check of Proposition 34.1, set

\[
L_0=5/6+M/12-\ell/6,\quad
L_K=1/3+7M/12+\ell/3,\quad
H_\xi=1+\xi-(1+\xi)M/2+\xi\ell.
\]

The positive weights `(4+18xi,2,3)/(9+18xi)` sum to one and cancel both `M` and `ell`. Their weighted average is exactly `(18xi+7)/(18xi+9)`. Symbolic simplification returned zero for all four residuals: total weight, `M` coefficient, `ell` coefficient, and constant term. This verifies that algebraic certificate, not the analytic foundation.

## 7. Exact mismatch with our current zeta/RMT task

The current [R30 closing report](../../reports/dyson_round30_followup.md) was read directly for this comparison. Its missing estimate retains a sharp integer Möbius polynomial, a prime-error transform, the exact oscillatory projection, and the same true zeta ordinates. It is not an unspecified Möbius cancellation problem.

### 7.1 QRH cannot simply replace the RH hypothesis already used

RH puts each nontrivial zero on the critical line. A fixed bound `Re(rho)<=B` with `B>1/2` does not do that. By symmetry it confines the strip from both sides, but still leaves a positive-width strip. Neither our use of critical-line zero coordinates nor the RH estimates in the previous proof can be relabeled unconditional without redoing the arguments and accounting for off-line zeros.

If RH is retained as a working assumption for zeta, a weaker zeta zero-free boundary supplies no new zero-location information. The family-wide Dirichlet/Hecke theorem can still provide arithmetic information beyond RH for **zeta alone**, so it should not be dismissed as redundant in every part of the programme. A precise transfer lemma is the necessary next step.

### 7.2 Three obstacles to importing the smoothed Möbius bound

First, ideal Möbius coefficients over the Eisenstein field are not the integer coefficients in

\[
M_D(t)=\sum_{D<d\le2D,\ d\text{ odd}}\mu(d)d^{it},
\qquad D\asymp T.
\]

Even at the trivial Hecke character, the reciprocal Dedekind zeta function factors into the reciprocals of zeta and its quadratic twist; its Dirichlet coefficients are not just integer `mu(d)`.

Second, the fixed smooth-test bound (A) is not a uniform estimate for oscillation `t~T`. Replacing a fixed test by `W_t(y)=y^(it)W_0(y)` incurs derivative norms of size up to `(1+|t|)^k`. Since `D~T`, that can consume the stated power saving. The sharp annular endpoints introduce a further smoothing issue. Polynomial height dependence must be paid, not silently set to one.

Third, even a bound for this separate Möbius factor would not establish a saving for the **joint signed product** involving the prime error and the same zeros. The admissible marked-moment coefficient class must include the actual partner. Lemma 17.2's explicit exclusion of arbitrary residual coefficients makes this a concrete obstruction to a direct substitution.

### 7.3 Progression estimates at our moduli are not automatically sufficient

The alternate paper's Corollary 1.2 states an absolute effective uniform error `O(x^(11/12) log x)` for prime counting in reduced residue classes up to modulus `x`. At the central scale `q~sqrt(x)`, the expected main term is roughly `sqrt(x)/log x`. The displayed error is much larger. Even replacing `11/12` by a boundary near `7/8` would retain this scale mismatch.

Thus a fixed zero-free half-plane alone is not the needed relative asymptotic or a signed average over our moduli and projected weights. It also does not, by itself, give a new level of distribution beyond `1/2` or a smaller bounded prime gap. Additional averaging, factorization, or cancellation must be established for the actual sieve weights.

### 7.4 No supplied out-of-band zero-correlation theorem

None of the inspected QRH theorem statements estimates the zeta pair-correlation measure at Fourier support beyond the protected range, a three-zero correlation, a normalized minimum-gap law, or our weighted sum over true zero ordinates. Exclusion of zeros near `Re(s)=1` is a horizontal location statement. Pair and higher correlations ask how ordinates interact on their mean-spacing scale. No implication between these questions is supplied by the reviewed proofs.

This is an applicability conclusion, not a claim that these methods can never lead to such an implication. The explicit arithmetic transformations are substantial new material to test against a specifically formulated joint estimate.

## 8. Useful next slice and what to postpone

The strongest bounded follow-up is to write an exact dictionary between the desired central signed pairing and the marked-moment families of Lemmas 17.1–18.1. It must record the coefficient class, shared character, moving modulus, masks, all length inequalities, endpoint smoothing, and height seminorm loss. If any condition fails, retain the exact failed condition as the result rather than replacing the target with a more convenient norm.

A separate QRH-focused route is to alter the inputs to Liu's critical counting class through a genuinely stronger simultaneous-large-value estimate. That is a precise research target. Parameter optimization within the unchanged certified system has already reached its stated limit.

Postpone claims of RH removal in our old proofs, GUE/Montgomery–Dyson consequences, AH refutation, or prime-gap improvements until the relevant arithmetic bridge is actually proved. Also postpone model-name attribution and independent formal-verification claims that the checked sources do not support.

## 9. Audit receipt and reproducibility

Full primary source bodies remain in the adjacent **local-only** archive:

`Astra-Local-Archive/latest-literature-2026-11-01/qrh-method-audit/`

The archive has the two PDFs, two original TeX sources, extracted text, three inspected assembly modules, formalization catalogue, source receipt, and two rendered statement pages. The public note contains source links and hashes, not duplicate full third-party papers.

| Local source | Bytes | SHA-256 |
|---|---:|---|
| seven.tex | 766316 | `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3` |
| seven.pdf | 1588969 | `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7` |
| eleven.tex | 169005 | `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d` |
| eleven.pdf | 784503 | `f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18` |
| FinalAssemblyUnconditional.lean | 1607 | `0f52159a2929e7b20646f8394589d25a1a637c2f78746ad9d1447871577af615` |
| CertifiedExistence.lean | 2698 | `2d48b75fdd14ba8eabb428f79f98e0a6e532c28083075bacf16e1d57f020d7a9` |
| FinalAssemblyCertifiedBands.lean | 8626 | `d41f3d2a7fc675a1e72e02ff0be668a774120dc97ff007f04593d4a28c7e0675` |
| formalization.yaml | 81913 | `b8e7072ab9ac195a290110d78c3a3497608ce76ac5b67d307685f38408299b39` |

Detailed proof reading was concentrated on: alternate-proof §§2–3, the exact propositions and complete finite induction in §5, and its initial Gauss/theta interface; September-proof §1, the complete continuation proof in §2, the exact coefficient/hypothesis statements in §§17–19 and the final parameter ordering in §20; Liu v2's preceding-bound hypothesis, iteration, and explicit optimality system. The PDFs' statement pages were also rendered and visually checked against the TeX. This does not represent a complete reread of every auxiliary proof.

The numerical and algebraic Liu checks use SymPy `nroots` at 55 digits and exact rational simplification of the displayed weighted combination. No numerical zero search, prime scan, full Lean build, or Git operation was performed.

The newly authored stochastic-protection note's stale September date was corrected to local November 1 / UTC November 2 as requested; no historical research note was altered. Its content after that date correction has SHA-256

`90c5d88bc938f8410550d337f5689c30726efb614b29a6bf80f75c94671e14f3`.
