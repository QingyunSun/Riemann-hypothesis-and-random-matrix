# Round 20: an actual prime-variance average and an equivalent zeta-deficit target

Date: 2026-09-05. Two complete ordinary proofs under RH connect one actual positive prime statistic to the frequency-two zero-pair deficit. Exponential averaging removes the former envelope loss, and height regularity makes the two strict-deficit objectives equivalent. Both proofs have independent cross-reviews and coordinator/root reviews. **Neither strict deficit has been proved.** The separate three-height prime computation evaluates the Round 19 single-length statistic and remains a finite floating diagnostic.

## 1. The exact actual-arithmetic statistic

Use the fixed autocorrelation bump from Round 16,
\[
f(x)=e^{-1/(1-4x^2)}1_{|x|<1/2},\qquad
\psi(v)=\frac{\int f(x)f(x-v)dx}{\int f(x)^2dx}.
\]
Fix \(\varepsilon=1/4\), put
\[
\omega(\alpha)=\psi((\alpha-2)/\varepsilon),\qquad
A=1+\varepsilon^2\int |v|\psi(v)dv,
\]
and retain \(\Psi(x)=\sum_{n\le x}\Lambda(n)\), including every prime power. Define for \(T\ge2\), \(\lambda>0\),
\[
\Delta_{\lambda,T}(x)
=\Psi(e^{\lambda/T}x)-\Psi(x)-(e^{\lambda/T}-1)x,
\]
\[
V_{\lambda,T}=\frac{T}{\log^2T}\int_1^\infty
\Delta_{\lambda,T}(x)^2
\omega\!\left(\frac{\log x}{\log T}\right)\frac{dx}{x^2},
\qquad
\boxed{\overline V_T=\int_0^\infty e^{-\lambda}V_{\lambda,T}\,d\lambda.}
\]
This is one actual, nonnegative, finite statistic at each stated height. Its logarithmic prime window is exactly \([T^{7/4},T^{9/4}]\), independent of \(\lambda\). The mean is exact. Replacing it by \(\lambda x/T\) or omitting continuous centers would change the proof and the object.

Write \(C_U=C_{\varepsilon,U}(2)\) for the Round 16 translated spectral bump, and \(D_U=C_{\varepsilon,U}(0)-C_U\ge0\) for its actual-zeta deficit. Under RH,
\[
\boxed{\overline V_T=\int_0^\infty p(y)C_{Ty}\,dy+o(1),
\qquad p(y)=\frac{4y^2}{\pi(1+y^2)^2},\qquad \int_0^\infty p(y)dy=1.}
\tag{1}
\]
Consequently,
\[
0\le\limsup_T\overline V_T\le A,
\qquad
\boxed{A-\overline V_T=\int_0^\infty p(y)D_{Ty}\,dy+o(1).}
\tag{2}
\]
A bounded extension of the spectral quantities below height two is harmless. RH plus the precise AH-Pairs hypothesis forces \(\overline V_T\to A\). The bound reaches that value without the previous \(L^+\approx1.0736\) factor.

This is a useful choice of smoothing of a classical formula, with no global novelty claim. It is a bound for an explicitly different statistic; it does not improve the unsmoothed single-length variance by implication.

Read the [complete length-average proof](../dyson/round20/length-averaged-variance/EXPONENTIAL_LENGTH_AVERAGE.md), [independent Euclid review](../dyson/round20/length-average-review/INDEPENDENT_EXPONENTIAL_LENGTH_REVIEW.md), and [root review](../dyson/round20/root-review/ROOT_ROUND20_REVIEW.md).

## 2. Why all lengths and all zero heights are covered

The source is the fixed-test weighted prime/zero Plancherel formula in Carneiro–Chandee–Chirre–Milinovich, together with its RH Selberg bound. The proof uses the exact reparameterization
\[
S=(e^{\lambda/T}-1)^{-1},\qquad r=\frac{\log S}{\log T},
\qquad
V_{\lambda,T}(\omega)=\frac TSr^2
V^{\mathrm{lin}}_{1,S}(\omega(r\,\cdot)).
\tag{3}
\]
The prime window and its center agree exactly. On a fixed compact length range, the moving test is replaced by one fixed test using the positive Selberg mass bound before invoking the source. No uniform source theorem for a varying family of Schwartz functions is assumed.

The actual arithmetic length tails satisfy
\[
\limsup_T\int_L^\infty e^{-\lambda}V_{\lambda,T}d\lambda
\ll (L+1)e^{-L},
\]
\[
\limsup_T\int_0^a e^{-\lambda}V_{\lambda,T}d\lambda
\ll a^2(1+|\log a|)^2.
\tag{4}
\]
For \(\lambda\le\sqrt T\), the entire prime window fits into the source's fixed \(S^B\) window. Above \(\sqrt T\), the RH bound for \(E(x)=\Psi(x)-x\) gives a term growing as \(e^{\lambda/T}\), controlled by the outside \(e^{-\lambda}\). This proves finite-height existence and the tail, retaining the actual arithmetic square.

The source prefix relation is the equality immediately before its equation (3.9). The smoothed zero measures depend on \(\lambda\), but their principal prefixes are uniformly \(2yC_{Ty}\) on fixed compact height-ratio intervals. Finite-interval integration by parts differentiates only the elementary kernel. The elementary length integral is
\[
\int_0^\infty e^{-\lambda}\frac{\sin^2(\lambda y/2)}{y^2}d\lambda
=\frac1{2(1+y^2)}.
\tag{5}
\]
This kernel decreases, so its derivative produces the nonnegative probability weight in (1).

The proof first takes the height limit in difference estimates with all cutoffs fixed, then removes the length cutoffs, then the zero-height cutoffs. Intermediate tail constants remain uniform after the first limit; the extreme tails already vanish there. Finally the exact bump is recovered from smooth-square approximants on common compact support. These details prevent an unjustified exchange of limits or an assumed full limit of \(C_T\).

The previously inaccessible general-length Goldston/Gonek pages are documented as unused. The required inputs are in the checked CCCC primary paper and Schoenfeld's RH Chebyshev estimate. The retained review records distinguish source-text checking from actual page-image inspection.

## 3. A positive deficit persists across nearby actual heights

For the same fixed bump, a second ordinary RH proof gives
\[
\boxed{|D_{Ty}-D_T|\le
2A\frac{|y-1|}{\max(1,y)}+o(1),
\qquad \tfrac12\le y\le2,}
\tag{6}
\]
with error uniform in \(y\). It applies to the actual finite zero-pair sums, with multiplicity, the denominator \(T\log T/(2\pi)\), and the fixed physical Lorentzian weight.

A positive support-one envelope makes the dilation estimate possible. With \(s(u)=\sin(\pi u)/(\pi u)\), define
\[
q(u)=s(u)^2+\frac{s(u-1/2)^2+s(u+1/2)^2}{2}.
\]
Its Fourier transform is \((1-|\alpha|)_+(1+\cos\pi\alpha)\), it dominates \(1/[2\pi^2(1+u^2)]\), and its pair mass tends to exactly \(7/3\). It therefore controls the full Schwartz dilation error, including distant pairs, using only known low-band information.

Freeze the logarithmic scale while enlarging the height cutoff. New pairs contribute nonnegatively, and the deficit kernel is at most twice the central kernel. The normalized change has the form \(X-rD_T+o(1)\), whose terms have opposite signs. Keeping those signs gives the stated \(2A\), including the reverse-height direction. Finite sums can jump when a zero enters the window; the uniform vanishing error covers these jumps. Literal finite-height continuity is not claimed.

The [full height proof](../dyson/round20/height-regularity/MULTIPLICATIVE_HEIGHT_EQUICONTINUITY.md) and [independent Aquinas review](../dyson/round20/height-regularity-review/INDEPENDENT_HEIGHT_REVIEW.md) retain every normalization and endpoint. That reviewer authored the separate length identity; the independent review of the latter is Euclid's, and no self-review is represented as independent.

## 4. The two strict research objectives are now equivalent

Let
\[
d=\limsup_TD_T\in[0,A],\qquad
\overline\delta=A-\liminf_T\overline V_T.
\]
Combining the independently reviewed components yields
\[
\boxed{\frac{2d^2}{25\pi A}\le\overline\delta\le d.}
\tag{7}
\]
For the lower bound, choose heights approaching \(d>0\). Equation (6) makes the deficit at least \(d/2\) throughout the fixed interval \([1-d/(8A),1+d/(8A)]\). The density in (1) is at least \(16/(25\pi)\) there. The upper bound uses the eventual upper envelope \(d\), with bounded physical heights carrying vanishing probability mass. Both bounds hold at \(d=0\).

Thus, under RH,
\[
\boxed{\limsup_TD_T>0
\quad\Longleftrightarrow\quad
\liminf_T\overline V_T<A.}
\tag{8}
\]
This provides two rigorously interchangeable targets. Either strict assertion would exclude the full AH-Pairs hypothesis. Neither strict assertion is established. Failure of full AH-Pairs is not proved to imply a deficit for this one bump. In particular, the ordinary proof of (8) is not itself an AH refutation, a new out-of-band value for pair correlation, or a Dyson–Montgomery theorem.

A sufficient arithmetic goal is now especially concrete: prove \(\liminf\overline V_T\le1\), since the fixed bump has \(A\approx1.01059>1\). The difference is modest as a numerical constant but contains the unresolved arithmetic information. No argument in this checkpoint supplies that inequality.

## 5. Three finite computations of the earlier single-length variance

The computation uses the Round 19 interval \((x,(1+1/T)x]\), mean \(x/T\), and the same bump. It evaluates **the single-length variance**, not \(\overline V_T\).

| T | Single-length positive variance | Integration cells | Higher prime powers in support |
|---:|---:|---:|---:|
| 100 | 0.120406036892308 | 22,390 | 38 |
| 300 | 0.136105800521502 | 75,568 | 103 |
| 1000 | 0.154279418168189 | 762,447 | 316 |

The sine limiting benchmark is approximately \(0.1851531433\); the AH limiting value is approximately \(1.0105877964\). Those are comparisons of finite values with asymptotic predictions, with no inferred convergence rate or limiting inequality.

Every prime power and both continuous center terms are retained. The common integer sieve stores 389,500 prime-power entries, including 448 higher powers. Each requested height uses its own exact fourth-root support cutoff; the maximum relevant integer is 5,629,036, with a harmless shared storage ceiling one larger.

Entry and exit events are sorted in the integer coordinate \((T+1)x\). On a cell with constant prime-power sum \(B\),
\[
\int_L^R\frac{(B-x/T)^2}{x^2}dx
=B^2(1/L-1/R)-\frac{2B}{T}\log(R/L)+\frac{R-L}{T^2}.
\]
The implementation uses a stable positive reformulation rather than subtracting three final large totals. All three components remain in each output bin. This matters: at \(T=1000\), the weighted components are approximately \(30.2813,-60.2541,30.1270\).

The seed autocorrelation is computed at fixed Simpson resolutions. Exact derivative bounds and even monotonicity give conservative ideal quadrature and endpoint-bin bounds. The complete ideal error accounting also includes the small event-series remainder. Machine rounding in logs, exponentials, event positions and sums is not enclosed. Therefore the author table's “analytic-only” columns are not certified numerical intervals.

An independent 70-decimal calculation of all \(T=100\) cells, with a different antiderivative and prefix-log calculation but the same frozen piecewise weight, differs from the float result by approximately \(2.1\times10^{-16}\). Exact signed/prime-power pair-kernel controls and all stored integer identities pass. These validate the bounded computation at their stated scopes; they do not establish an asymptotic estimate or an effective prime-to-zero transfer.

Read the [complete diagnostic and error budget](../dyson/round20/actual-prime-variance/ACTUAL_PRIME_VARIANCE_DIAGNOSTIC.md) and [portable reproduction instructions](../dyson/round20/actual-prime-variance/REPRODUCTION.md). All 16,384 bins per height, every seed endpoint, the integer arrays, both scripts, output JSON and original logs are preserved. No height beyond 100, 300 and 1000 was scanned.

## 6. Validation and the next mathematical bottleneck

The length-average checker passes thirteen exact transform/reparameterization checks and replays byte for byte in an independent copy. The height checker passes the exact envelope/normalization identities and 3,159 rational prefix-algebra cases, also with complete byte-identical replay. The ordinary full proofs separately justify the analytic limits; the symbolic scripts do not certify them.

The root and coordinator read all three author reports. Both analytic reports have independently authored cross-reviews. The computation has an independent formula/precision checker, full script reviews, and separate file/row/hash checks; the main sieve and 70-decimal calculation were not rerun for publication. Author-source headers and all historical coordinator snapshots remain unchanged, with later acceptance recorded separately. The [intake manifest](../dyson/round20/INTAKE_MANIFEST.json), [source-link map](../dyson/round20/SOURCE_LINK_MAP.md) and [integration receipt](../logs/round20-integration/INTEGRATION_RECEIPT.json) distinguish these scopes.

The key unresolved task is a strict upper estimate for the **actual centered arithmetic** average, beyond the non-strict bound inherited from low-band pair information. The new identity supplies a precise target and removes a transfer loss; it does not create that missing cancellation. Possible next bounded work should preserve the exact centers while expanding the all-length arithmetic kernel, or test whether an applicable prime-distribution theorem yields a strict gain for that kernel. Any such source transfer needs a fresh range and error audit.

The finite ACUE dynamic theorem remains useful as a test of proposed flow arguments. It does not transfer positive-time production to the initial zeta statistic. No RH, full GUE, AH-refutation, new zeta-gap or sub-186 prime-gap theorem is claimed. Broad new scans, another large PDF rebuild, numerical extrapolation and optimization of the tiny finite-flow constants are postponed. The existing 705-page public and 753-page local compilations retain their explicit through-Round-14 checkpoint; these complete later reports update the research separately.
