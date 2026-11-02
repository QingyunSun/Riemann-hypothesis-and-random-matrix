# An actual-zeta upper target at the forced AH atom α=2

Date: 2026-09-05. Status: ordinary proofs and a primary-source comparison, submitted for independent review. The exact translated-bump upper bound below is an application of the standard positive-pair comparison, not a new claim of priority. No strict improvement at α=2, AH refutation, RH proof, or Montgomery theorem is obtained.

The usable result is a precise saturation problem: for a specified smooth bump, RH gives an upper bound that AH-Pairs attains exactly. A strict deficit excludes AH-Pairs without any simplicity assumption. We also extend the existing centered prime identity to the full required power range and show why the old short-shift error bounds cannot simply be imported.

## 1. Objects and one fixed smooth test

Throughout assume RH, count all zeros with multiplicity, and put
\[
L=\frac{\log T}{2\pi},\qquad N_T=TL,
\quad w(t)=\frac4{4+t^2},
\]
\[
\mu_T=\frac1{N_T}\sum_{0<\gamma,\gamma'\le T}
 w(\gamma-\gamma')\delta_{L(\gamma-\gamma')},
\qquad
F_T(\alpha)=\int e^{2\pi i\alpha u}\,d\mu_T(u).
\tag{1}
\]
The pair measure is positive and even. The Lorentzian weight has a nonnegative Fourier transform, hence F_T is itself a nonnegative real continuous function. This last fact is stronger than the positivity of μ_T alone. The normalization agrees exactly with the R7 report and the 2022 Carneiro–Chandee–Chirre–Milinovich paper; the 2023 CMR paper instead divides by the zero count N(T), an asymptotically equivalent factor N(T)/N_T→1.

Choose once and for all
\[
f(x)=\exp\!\left(-\frac1{1-4x^2}\right)1_{|x|<1/2},
\quad s_2=\int f(x)^2dx,
\quad \psi(v)=\frac1{s_2}\int f(x)f(x-v)dx.
\tag{2}
\]
The zero extension of f is smooth. Consequently ψ is even, nonnegative and C∞, has closed support [−1,1], is positive on (−1,1), and satisfies
\[
\psi(0)=1,\quad 0\le\psi\le1,\qquad
\widehat\psi(u)=\frac{|\widehat f(u)|^2}{s_2}\ge0.
\tag{3}
\]
Here \(\widehat g(u)=\int g(v)e^{-2\pi iuv}dv\). Cauchy–Schwarz proves ψ≤1. Define the two fixed constants
\[
m_0=\int\psi(v)dv=\frac{(\int f)^2}{s_2},\qquad
m_1=\int |v|\psi(v)dv
 =\frac1{s_2}\iint|x-y|f(x)f(y)dxdy.
\tag{4}
\]
They obey 0<m₁<m₀<1; the last inequality is Cauchy–Schwarz on the interval of length one, with strictness because f is not constant. Numerical values, if quoted in the adjacent checks, are quadrature diagnostics; the exact definitions (2)–(4) determine the theorem.

For fixed 0<ε<1, set
\[
C_{\varepsilon,T}(b)=\int\psi((\alpha-b)/\varepsilon)F_T(\alpha)d\alpha.
\tag{5}
\]
The principal proposed target is one fixed test, for example ε=1/4:
\[
\boxed{\limsup_{T\to\infty}C_{\varepsilon,T}(2)<1.}
\tag{6}
\]
The bump is not divided by ε. Its height at the prospective atom is one. This normalization is essential: the atom contributes one while a unit spectral density contributes εm₀.

## 2. The actual RH upper bound and its exact deficit

**Proposition 1.** For every T, every real b, and the bump (2),
\[
0\le C_{\varepsilon,T}(b)\le C_{\varepsilon,T}(0).
\tag{7}
\]
Under RH and fixed 0<ε<1,
\[
C_{\varepsilon,T}(0)\longrightarrow1+\varepsilon^2m_1,
\quad
\limsup C_{\varepsilon,T}(b)\le1+\varepsilon^2m_1.
\tag{8}
\]
The exact nonnegative difference at b=2 is
\[
\boxed{D_{\varepsilon,T}:=C_{\varepsilon,T}(0)-C_{\varepsilon,T}(2)
=\varepsilon\int\widehat\psi(\varepsilon u)
  (1-\cos4\pi u)\,d\mu_T(u)\ge0.}
\tag{9}
\]

**Proof.** Fourier inversion and evenness give the finite-sum identity
\[
C_{\varepsilon,T}(b)
=\varepsilon\int\widehat\psi(\varepsilon u)\cos(2\pi bu)d\mu_T(u).
\]
All its terms are absolutely integrable; indeed μ_T is a finite measure for every fixed T. Positivity of μ_T and \(\widehat\psi\), with cos≤1, proves the upper bound. The lower bound uses F_T≥0 and ψ≥0. Montgomery's RH theorem on [−ε,ε] says distributionally
\[
F_T(\alpha)d\alpha\longrightarrow\delta_0+|\alpha|d\alpha
\quad\text{inside }(-1,1).
\]
Testing by ψ(α/ε) gives (8). Equivalently the term \(\log T\,T^{-2|\alpha|}\) is an approximate identity of total mass one, and the |α| term integrates to ε²m₁. Subtracting b=2 proves (9). ∎

This is an actual-zeta bound, not a numerical model bound. It is also the same positivity mechanism appearing explicitly in the proof of CCCC Theorem 7, equations (2.14) and the following computation. Its failure to be strict is the specific missing information.

Even a positive limsup of D would contradict the full AH-Pairs limit proved below; the liminf targets here impose a stronger, uniform asymptotic separation.

A useful consequence is an atom-capacity statement. The measures F_T(α)dα are locally bounded: translate a fixed positive bump from (2), use (7)–(8), and cover a compact interval by finitely many regions where the bump is bounded below. Thus every sequence has vaguely convergent subsequences on compact sets. For any such positive limiting measure ν and any real b,
\[
\boxed{\nu(\{b\})\le1.}
\tag{10}
\]
Indeed \(\nu(\{b\})\le\int\psi((\alpha-b)/\varepsilon)d\nu\le1+\varepsilon^2m_1\); let ε↓0 **after** passing to the subsequential limit. This permits an atom of mass exactly one. It does not prove that an atom away from zero is absent.

## 3. AH-Pairs forces saturation, with no limit assumption on p₀

Use the precise AH-Pairs formulation in Goldston–Lee–Schettler–Suriajaya II: for every fixed M, pairs of zeros in (T/log²T,T] with normalized distance at most M lie within O((|k|+1)R(T)) of k/2, where R(T)→0. This includes k=0. Multiplicity and near-coincident pairs are allowed.

The compactness/tail argument must precede the Fourier shift. Their equation (1.12) gives
\[
\mu_T([-R,R])\ll1+R\qquad(0\le R\le T).
\tag{11}
\]
It does not give a uniform linear bound for all R. Beyond T the total mass is at most O(T log T), which is enough: for a Schwartz test bounded by C(1+u²)⁻¹, tails outside a fixed R are O(1/R)+O(log T/T). The first term follows by dyadic shells up to T, and the second by the total-mass bound. There are O(T/log T) early zeros below T/log²T and O(log T) potential partners per zero in any fixed normalized interval, using the unit-interval zero bound. Their local normalized contribution is O(1/log T). The same tail estimate removes them for Schwartz tests. On a fixed normalized compact interval, w(u/L)→1 uniformly.

Every subsequential pair-measure limit is consequently a tempered positive measure supported on (1/2)Z. Multiplication by e^{4πiu} fixes that measure, so its Fourier transform is 2-periodic. Montgomery's theorem determines that transform on (−1,1) to be δ₀+|α|dα. Translation by two therefore determines it on (1,3):
\[
\delta_2+|\alpha-2|d\alpha.
\tag{12}
\]
No assumption on the existence or value of p₀ was used. In particular the optional odd-frequency atoms in R7 equation (7) lie at 1 and 3 and are outside the support of the present fixed ε<1 test. Testing (12) proves, on every subsequence and therefore on the full sequence,
\[
\boxed{\text{RH+AH-Pairs}\Longrightarrow
C_{\varepsilon,T}(2)\longrightarrow1+\varepsilon^2m_1,
\qquad D_{\varepsilon,T}\longrightarrow0.}
\tag{13}
\]
This establishes the requested forced-atom calculation. The sine/GUE pair prediction gives instead
\[
C_{\varepsilon,T}(2)\longrightarrow\varepsilon m_0,
\qquad D_{\varepsilon,T}\longrightarrow1-\varepsilon m_0+\varepsilon^2m_1.
\tag{14}
\]
These are conditional model predictions, not established actual-zeta limits.

There are two different sufficient targets:

* The sharp fixed-test saturation-breaking target is \(\liminf D_{\varepsilon,T}>0\), equivalently \(\limsup C_{\varepsilon,T}(2)<1+\varepsilon^2m_1\). It contradicts AH-Pairs under RH.
* The deliberately conservative target (6) is equivalent to \(\liminf D_{\varepsilon,T}>\varepsilon^2m_1\). It asks to go below one, not merely below the AH value.

For ε=1/4, the current upper bound lies between 1 and 17/16, while the sine prediction is smaller than 1/4. The specified seed gives the floating diagnostics m₀≈0.7406125731 and m₁≈0.1694047426: current bound/AH value ≈1.0105877964, sine value ≈0.1851531433, and the conservative deficit threshold ≈0.0105877964. These decimals are not outward enclosures and are not used to justify any strict inequality. The gap from the proved bound to the conservative threshold is exactly m₁/16; it is not the full atom mass one. Neither strict target is proved here. No monotonic relation to the earlier two-scale 1/16 resolvent target is asserted: they are different tests of the same unknown actual pair correlations.

All limits above fix ε first. Allowing ε=ε(T)→0 would require a new uniform argument; AH-Pairs only grants its proximity conclusion for each fixed normalized compact interval. A shrinking bump may probe distances tending to infinity and cannot be substituted silently.

### What a positive deficit means geometrically

Let \(k_\varepsilon(u)=\varepsilon\widehat\psi(\varepsilon u)\), a nonnegative Schwartz function. Formula (9) vanishes on all half-integers, including zero. If its liminf is a fixed positive number, Schwartz tails and (11) first localize a positive part to |u|≤M. Then \(1-\cos4\pi u\ll\operatorname{dist}(u,(1/2)\mathbb Z)^2\) and the uniform compact mass bound show that a sufficiently narrow η-neighborhood of the half-lattice cannot carry that whole positive deficit. It follows that for some fixed M,η,c>0,
\[
\liminf_T\mu_T\{u:|u|\le M,\ \operatorname{dist}(u,(1/2)\mathbb Z)\ge\eta\}\ge c.
\tag{15}
\]
Thus the target requires positive normalized **pair** density off the half-lattice; a finite or zero-density exceptional set of close pairs is insufficient. It says nothing by itself about consecutive-gap density or simplicity. A converse from arbitrary off-lattice mass requires a positive lower bound for kε on the particular set; its Fourier zeros must not be ignored.

## 4. Honest comparison with primary upper bounds

The relevant finite-window reference is Carneiro–Chandee–Chirre–Milinovich, *On Montgomery's pair correlation conjecture: a tale of three integrals*, Theorems 7 and 9, printed pp.8–11. Theorem 7 works for every fixed b and interval length ℓ>0; Theorem 9 gives explicit triangle bounds for b≥1. Crucially, their equation (2.27) says the upper constant approaches **one**, not zero, as ℓ↓0. The text immediately following it explicitly explains that delta spikes above support one cannot be excluded by those bounds.

For an exact illustrative comparison set ε=1/8, so the bump support is [15/8,17/8] and ℓ=1/4. Since ψ≤1, the interval bound applies. In Theorem 9's first upper candidate (valid at this length),
\[
\frac43(1+\ell)+\frac{\ell^3}{12}-\frac\ell3
-\frac14(1-\ell-\ell^2)_+
=\frac{1085}{768}=1.4127604166\ldots.
\tag{16}
\]
Therefore that published candidate gives \(\limsup C_{1/8,T}(2)\le1085/768\). Our direct bump comparison instead gives \(\limsup C_{1/8,T}(2)\le1+m_1/64<65/64\), but stops precisely at the AH value. This is a tailored application of the same known positivity principle, not an improvement of the published optimized interval theorem. Theorem 9 takes a minimum of two candidates; using the displayed candidate alone is sufficient for this comparison, so no numerical optimizer is assumed.

Carneiro–Milinovich–Ramos, *Fourier optimization and Montgomery's pair correlation conjecture*, Theorem 1 and Corollary 2 (2023), give the RH upper long-interval average 1.3208+o(1). Their length condition is ℓ≥ℓ₀, with ℓ₀ not a small-window assertion. Multiplying 1.3208 by 2ε for the present short interval is invalid. Even the full AH spectrum is compatible with their long-average bounds: its long average is p₀, whose allowed range [1,1.2973576…] lies below 1.3208. Their GRH lower bound near 1≤α≤3/2 is neither an upper bound nor a result near α=2.

The primary papers for extra averages over Dirichlet L-functions are not results for this one zeta function. We have not found or claimed a primary theorem that proves (6) or the weaker strict-saturation target. The published finite-window upper bounds and the exact comparison above identify a specific missing strict inequality, rather than a misleading formal inference from a long average.

## 5. Uniform extension of the actual centered prime identity

The notation “X near T²” refers to the logarithmic center. For a fixed ε the exact range is
\[
x=T^\alpha,\qquad 2-\varepsilon\le\alpha\le2+\varepsilon,
\tag{17}
\]
which is not x asymptotic to T² up to constant factors.

For u>0 retain the R7 weight and the full von Mangoldt signal:
\[
a_u(x)=\min\{(u/x)^{1/2},(x/u)^{3/2}\},
\]
\[
P_x(t)=\sum_{n\ge2}\Lambda(n)a_n(x)n^{-it}-M_x(t),
\quad
M_x(t)=\int_0^\infty a_u(x)u^{-it}du
=\frac{2x^{1-it}}{(1/2+it)(3/2-it)}.
\tag{18}
\]
The series and the continuous mean converge absolutely. The exact complex mean is kept; replacing Λ by primes alone has not been justified here.

**Proposition 2.** For any fixed 0<a≤A<∞, uniformly in x=T^α, a≤α≤A, Goldston's Proposition 1 and equations (4.4)–(4.5) imply under RH
\[
F_T(\alpha)=\frac1{xT\log T}\int_0^T|P_x(t)|^2dt
+O_{a,A}\!\left(\frac{\log T}{x}+\frac{\log^2T}{T}\right).
\tag{19}
\]
In particular this holds throughout (17), with a=2−ε>1.

**Proof with the range explicit.** Let
\[
Z_x(t)=-2x^{1/2-it}\sum_{\gamma\in\mathbb R}
 \frac{x^{i\gamma}}{1+(t-\gamma)^2}.
\]
The source explicit formula gives P_x=Z_x+E_x and
\[
E_x(t)\ll x^{-1/2}\log(t+2)+x^{-2}/(t+2).
\]
Its constants do not require x≤T or x≤T^{7/5}. The standard local zero count gives
\[
\int_0^T|Z_x|^2dt\ll xT\log^2T,
\qquad
\int_0^T|E_x|^2dt\ll x^{-1}T\log^2T+x^{-4}.
\]
The all-zero kernel/truncated-pair comparison of equations (4.4)–(4.5) has error O(x log³T), uniformly in x because |x^{iγ}|=1 under RH. Cauchy–Schwarz bounds the normalized cross error by O(log T/x), with smaller terms from x⁻²; the normalized pair-endpoint error is O(log²T/T). These estimates prove (19). All bounds are uniform for any fixed compact positive α-range, so the enlarged support introduces no hidden exchange of limits. ∎

Let dΔ(u)=dΨ(u)−du, where dΨ assigns mass Λ(n) to n. Write ψε(α)=ψ((α−2)/ε) and define
\[
\mathcal K_{\varepsilon,T}(u,v)=\frac1{T\log T}
\int\psi_\varepsilon(\alpha)T^{-\alpha}
 a_u(T^\alpha)a_v(T^\alpha)
 \frac{\sin(T\log(u/v))}{\log(u/v)}\,d\alpha,
\tag{20}
\]
with continuous diagonal value T for the sine quotient. Fubini is justified for each fixed T by the weighted total variation of dΔ and the bounded α-range. Expansion of the square, retaining all three centered pieces, gives
\[
\boxed{C_{\varepsilon,T}(2)=
\iint\mathcal K_{\varepsilon,T}(u,v)d\Delta(u)d\Delta(v)+o(1).}
\tag{21}
\]
The o(1) is uniform for the chosen fixed ε. This is the actual full arithmetic kernel, not an uncentered prime correlation and not a bandlimited random-matrix surrogate.

The atomic diagonal tends to
\[
D^{\rm prime}_{\varepsilon,T}
=\sum_n\Lambda(n)^2\mathcal K_{\varepsilon,T}(n,n)
\longrightarrow\int\alpha\psi_\varepsilon(\alpha)d\alpha
=2\varepsilon m_0.
\tag{22}
\]
For completeness, partial summation of \(\sum_{n\le y}\Lambda(n)^2\sim y\log y\) gives
\(\sum_n\Lambda(n)^2a_n(x)^2\sim x\log x\), uniformly as x ranges between the endpoints of (17). The leading two weight integrals below and above x are each x log x/2. The lower-order logarithmic contributions do not affect (22).

The exact centered off-diagonal expression is
\[
\begin{split}
E_{\varepsilon,T}={}&2\sum_{m<n}\Lambda(m)\Lambda(n)\mathcal K_{\varepsilon,T}(m,n)\\
&-2\sum_n\Lambda(n)\int_0^\infty\mathcal K_{\varepsilon,T}(n,v)dv
+\int_0^\infty\int_0^\infty\mathcal K_{\varepsilon,T}(u,v)du\,dv.
\end{split}
\tag{23}
\]
Combining (19)–(23), the conservative upper target (6) is exactly
\[
\limsup E_{\varepsilon,T}<1-2\varepsilon m_0.
\tag{24}
\]
AH-Pairs forces \(E_{\varepsilon,T}\to1+\varepsilon^2m_1-2\varepsilon m_0\), while the sine prediction is \(E_{\varepsilon,T}\to-\varepsilon m_0\). For ε=1/4 the allowance in (24) exceeds 1/2. Thus the target does not demand the precise negative GUE cancellation in this normalization. This numerical generosity alone is not a theorem: the individual uncentered terms in (23) can be far larger than their centered combination, and the continuous pole term is indispensable.

## 6. Why the previously checked arithmetic estimates do not immediately apply

The principal shift scale is h≈x/T. In terms of x, the present exponents are
\[
1-\frac1{2-\varepsilon}\le\frac{\log(x/T)}{\log x}
\le1-\frac1{2+\varepsilon}.
\tag{25}
\]
For ε=1/4 this is [3/7,5/9], straddling 1/2. The R7 compact bump used [6/5,7/5] and shift exponents [1/6,2/7]. The R9–R15 arithmetic wrappers were proved in that smaller range. Their statements cannot be imported without extending every error term.

There is a concrete failure at the central scale. The R9 selected-component bridge retained a nuisance error O(H√X log⁴X), H=X/T. Relative to the needed X log X scale, its available bound is
\[
O\!\left(X^{1/2-1/\alpha}\log^3X\right).
\tag{26}
\]
At α=2 this is O(log³X), and for α>2 it grows by a positive power. The **estimate** therefore ceases to show negligibility; this does not say that the actual error has that size. The exact kernel (20)–(23) bypasses that unproved discard by retaining every term.

Likewise the strong per-shift Hardy–Littlewood square-root error considered in R7 gives a summed variance error of scale H²X^{1/2+η}. Dividing by HX log X leaves H X^{-1/2+η}/log X. With fixed η>0 it cannot uniformly justify the part of (25) at and above H=√X. A weighted averaged covariance theorem could be better; none is supplied by that per-shift premise alone.

Finally, a Dirichlet-series mean-value theorem has error controlled by \(\sum n\Lambda(n)^2a_n(x)^2\asymp x^2\log x\); after normalization the bound is O(x/T), which is enormous here. RH's pointwise |F_T(α)|≤F_T(0)≪log T also does not give a bounded narrow-window target. The useful currently proved bound is (8), obtained after averaging in α and exploiting the positive pair measure.

These are specific failures of available estimates. They do not establish a no-go theorem for genuine primes or the full signed covariance. The next mathematical task is the strict fixed-test inequality in (9), or the explicit centered arithmetic upper bound (24), with the actual x≈T² logarithmic scales and all means/errors present.

## 7. Reproducibility and claim boundary

The adjacent bounded script records the exact rational interval-bound value (16), the exponents (25)–(26), positive Fourier/autocorrelation normalization checks on the fixed seed, and an independent polynomial-seed algebra check. Numerical seed quadrature is labelled floating and is not an enclosure or evidence of an actual-zeta inequality. There is no zero-data fit or parameter sweep.

Primary sources:

* Goldston, *Notes on Pair Correlation of Zeros and Prime Numbers*, Proposition 1, equations (3.11), (4.4)–(4.5), and §6: [arXiv](https://arxiv.org/abs/math/0412313). This supplies the actual arithmetic identity and uniform x dependence.
* Goldston–Lee–Schettler–Suriajaya II, equations (1.9), (1.12), (1.14)–(1.15): [primary text](https://arxiv.org/html/2507.06823v1). This supplies the precise AH-Pairs formulation and compactness bounds; no p₀ limit is assumed here.
* Carneiro–Chandee–Chirre–Milinovich, Theorems 7 and 9 and equation (2.27): [author-hosted PDF](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), also [arXiv](https://arxiv.org/abs/2108.09258). The downloaded PDF/text and hashes are preserved under `sources/`.
* Carneiro–Milinovich–Ramos, Theorem 1 and Corollary 2: [arXiv](https://arxiv.org/abs/2310.01913). Its 1.3208 constant is a long-average result, not a bound for the present fixed narrow interval.

The source receipt pins these primary files and the earlier R7/R9/R11 dependencies. The target is a potentially substantial AH-Pairs exclusion under RH; what is proved in this note is the exact upper bound, the saturation/deficit reduction, the atom capacity, and the uniformly valid centered arithmetic representation. The required strict actual-zeta inequality remains open.
