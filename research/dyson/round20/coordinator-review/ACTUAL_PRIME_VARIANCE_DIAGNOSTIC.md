# Three finite actual-prime values of the positive Bragg-linked variance

Date: 2026-09-05. Status: bounded reproducible finite computation with exact algebraic controls and separate analytic discretization bounds. **This is not an asymptotic theorem, an AH refutation, a numerical enclosure including rounding, or a computation of a zeta-zero statistic.** The three requested values are T=100, 300, 1000; no other height was scanned.

The positive variance is approximately 0.120406, 0.136106 and 0.154279 at these heights. These values can be compared descriptively with the sine-process limiting benchmark 0.185153 and the AH limiting value 1.010588. A finite-height discrepancy from an asymptotic prediction cannot refute that prediction. No effective uniform error in the zeta/variance limiting transfer is established here.

## 1. Exact object, seed, support and result

Use the same fixed seed as R16–R19:
\[
f(x)=e^{-1/(1-4x^2)}1_{|x|<1/2},\quad
s_2=\int_{\mathbb R}f^2,\quad
\psi(v)=\frac1{s_2}\int_{\mathbb R}f(x)f(x-v)dx.
\tag{1}
\]
Let ε=1/4, ω(α)=ψ((α−2)/ε), q_T=1+1/T, and
\[
\Delta_T(x)=\Psi(q_Tx)-\Psi(x)-\frac{x}{T},\qquad
\Psi(y)=\sum_{n\le y}\Lambda(n).
\]
The quantity evaluated is exactly the R19 positive integral
\[
\boxed{V_{\varepsilon,T}=\frac{T}{\log^2T}
\int_0^\infty\Delta_T(x)^2
\omega\!\left(\frac{\log x}{\log T}\right)\frac{dx}{x^2}.}
\tag{2}
\]
Every prime power contributes Λ(p^k)=log p, including k≥2. The arithmetic interval is (x,q_Tx], and the full center x/T is retained before taking the square. No replacement by primes alone, Ψ(q_Tx) alone, or an uncentered pair count is made.

The support is the full logarithmic window
\[
T^{7/4}\le x\le T^{9/4}.
\tag{3}
\]
It is not a constant-factor window around T². The largest integer potentially contributing is
\(\lfloor (T+1)T^{5/4}\rfloor\).

| T | Positive variance diagnostic | Analytic-only lower | Analytic-only upper | Relevant integer cutoff | Higher prime powers in the support |
|---:|---:|---:|---:|---:|---:|
| 100 | 0.120406036892308 | 0.120384464897993 | 0.120427613263263 | 31,939 | 38 |
| 300 | 0.136105800521502 | 0.136083176293479 | 0.136128430331948 | 375,809 | 103 |
| 1000 | 0.154279418168189 | 0.154253795774156 | 0.154305045523650 | 5,629,036 | 316 |

The lower/upper columns cover the proved seed-quadrature and α-bin approximation errors in ideal exact arithmetic. They **do not include machine rounding** in exponentials, logarithms, interval locations, arithmetic coefficients or accumulation. They are therefore not certified numerical intervals for (2). A rigorous interval certificate would require an additional directed-rounding computation or a proved complete floating-error budget.

The largest actually included prime powers are respectively 31,907, 375,799 and 5,629,009. A shared sieve runs to the harmless upper storage cutoff 5,629,037 and retains 389,500 prime-power entries, of which 448 have exponent at least two. Each calculation then applies its own exact support cutoff.

For comparison only, the same seed gives
\[
m_0=\int\psi\simeq0.7406125730612161,\quad
m_1=\int |v|\psi(v)dv\simeq0.1694047426280367,
\]
\[
\varepsilon m_0\simeq0.1851531432653040,
\qquad A=1+\varepsilon^2m_1\simeq1.0105877964142522.
\tag{4}
\]
The three differences V−A are approximately −0.890182, −0.874482 and −0.856308. Their signs are facts about this finite diagnostic, not estimates for a limiting liminf or limsup. No fit or extrapolation is performed.

## 2. Integer event geometry and both centering terms

The staircase
\[
A_T(x)=\Psi(q_Tx)-\Psi(x)
\]
is constant between an entry event x=n/q_T and an exit event x=n. In the scaled coordinate y=(T+1)x these are the exact integers nT and n(T+1). The implementation sorts and merges these integer event locations, then inserts 16,384 equally spaced α-bin boundaries on [7/4,9/4]. Exact integer fourth roots determine all outer support and initial-staircase integer cutoffs; no floating comparison is used to decide which prime powers enter those support lists.

For example,
\[
\lfloor q_TT^{9/4}\rfloor
=\left\lfloor\bigl(T^5(T+1)^4\bigr)^{1/4}\right\rfloor,
\quad
\lfloor q_TT^{7/4}\rfloor
=\left\lfloor\bigl(T^3(T+1)^4\bigr)^{1/4}\right\rfloor.
\]
The event integers are subsequently divided by T+1 in floating arithmetic for the numerical integral. That last conversion is among the un-enclosed rounding operations stated above.

On a cell [L,R] with constant A=A_T(x), the elementary unweighted integral is
\[
\int_L^R\frac{(A-x/T)^2}{x^2}dx
=A^2(1/L-1/R)-\frac{2A}{T}\log(R/L)+\frac{R-L}{T^2}.
\tag{5}
\]
This identity shows both the linear mixed center and the continuous square center. The CSV output preserves all three terms separately, as well as a numerically stable evaluation of their positive combination.

| T | Weighted prime-square term | Weighted mixed center | Weighted continuous square center |
|---:|---:|---:|---:|
| 100 | 4.356210483739454 | −8.471775502931878 | 4.235971056084734 |
| 300 | 10.684758567197242 | −21.097182711094960 | 10.548529944419219 |
| 1000 | 30.281321518057090 | −60.254075471544350 | 30.127033371655443 |

Each row uses the same frozen piecewise-constant midpoint weight as the diagnostic. The variance is computed in a stable positive cell formula, rather than by subtracting these three large final totals. The unweighted component-recombination discrepancies are about 2.1×10⁻¹⁵, 5.4×10⁻¹⁵ and 4.0×10⁻¹⁴, respectively. Those are numerical consistency checks, not error certificates.

There are 22,390, 75,568 and 762,447 event-plus-bin integration cells. The code also independently recomputes the active prime-power sum by direct summation at 33 fixed cell midpoints for each T. The largest disagreements are below 2.3×10⁻¹³.

## 3. Stable positive cell formula and analytic series error

Put u=(R−L)/L and B=A−L/T. Then (5) becomes
\[
\frac{B^2}{L}I_0(u)-\frac{2B}{T}I_1(u)+\frac{L}{T^2}I_2(u),
\tag{6}
\]
where
\[
I_0=\frac{u}{1+u},\quad
I_1=\log(1+u)-\frac{u}{1+u},\quad
I_2=u-2\log(1+u)+\frac{u}{1+u}.
\]
Indeed these are respectively the integrals of 1, z and z² against dz/(1+z)² over [0,u]. Formula (6) integrates (B−Lz/T)²/[L(1+z)²] and is nonnegative. The independent exact checker differentiates it to recover that integrand.

Directly forming I₁ and I₂ at very small u would lose digits. The code instead evaluates
\[
I_1(u)=\sum_{k=2}^{12}(-1)^k\frac{k-1}{k}u^k+R_1(u),
\quad
I_2(u)=\sum_{k=3}^{12}(-1)^{k+1}\frac{k-2}{k}u^k+R_2(u).
\tag{7}
\]
For 0≤u<0.01 the alternating terms decrease, so both remainders have absolute value at most u¹³. The fixed α grid guarantees an entirely rational common bound:
\[
u\le e^{\log(T)/32768}-1
<\frac7{32761}<\frac1{4096},
\]
since T≤1000 gives log T<7. Also log n<16 for every stored integer. Both logarithm inequalities are verified exactly using e>27/10, which already follows from a finite partial sum of the exponential series.

With H=⌈T^{9/4}⌉, the active sum satisfies
\[
|B|\le B_*:=16(H/T+1)+H/T.
\]
If n_* is the relevant integer cutoff and l_*=⌊T^{7/4}⌋, the number of cells is at most 2(n_*−l_*)+16,384. Since T/log²T<T and 0≤ω≤1, an exact rational upper bound for the total ideal series truncation error is
\[
[2(n_*-l_*)+16384]T
\left(\frac{2B_*}{T}+\frac{H}{T^2}\right)
\left(\frac7{32761}\right)^{13}.
\tag{8}
\]
The three bounds are below 1.6×10⁻³⁹, 6.2×10⁻³⁸ and 4.2×10⁻³⁶. Their exact fractions are retained in JSON. This tiny analytic truncation error is unrelated to the much larger, un-enclosed machine rounding error.

## 4. Seed quadrature with an explicit analytic bound

The seed and autocorrelation are never replaced by a polynomial or a random-model surrogate. The overlap integral for v≥0 is over [v−1/2,1/2], of length 1−v. A composite Simpson rule with 4096 equal subintervals evaluates this integral at 8193 nonnegative values v=j/8192. Reflection supplies every α-grid endpoint. A 2048-subinterval calculation is retained as a separate convergence diagnostic; the maximum discrepancy is 5.6×10⁻¹⁶.

For an analytic bound, let y=1−z². Exact differentiation gives
\[
f^{(j)}(x)=2^j e^{-1/y}\frac{P_j(z)}{y^{2j}},\qquad z=2x,
\]
\[
P_{j+1}(z)=y^2P_j'(z)+(4jzy-2z)P_j(z),\quad P_0=1.
\tag{9}
\]
The coefficient ℓ¹ norms for j=0,…,4 are exactly 1,2,8,88,1096. These polynomials and norms are independently regenerated by SymPy. Because e>8/3 and the maximum of e^{-1/y}y^{-2j} occurs at y=1/(2j), valid rational derivative bounds are
\[
C_0=3/8,\quad
C_j=2^j\|P_j\|_1(3j/4)^{2j}\quad(1\le j\le4).
\]
The global extension by zero is smooth, so these bounds include the endpoints. The fourth derivative of f(x)f(x−v) is bounded uniformly in v by
\[
C_{\rm prod}=\sum_{j=0}^4\binom4jC_jC_{4-j}
=\frac{2818940211}{32}.
\tag{10}
\]
Composite Simpson error on an interval of length at most one is at most
\(E=C_{\rm prod}/(180\cdot4096^4)\).
Furthermore, on [−1/4,1/4] one has f²≥e^{-8/3}, hence s₂>1/54. Cauchy–Schwarz gives 0≤ψ(v)≤1. If a_M(v) and b_M denote the ideal exact-arithmetic Simpson numerator and denominator, then
\[
\left|\frac{a_M(v)}{b_M}-\psi(v)\right|
\le\frac{2E}{1/54-E}
=\frac{16913641266}{90071984090589287}
<1.878\times10^{-7}.
\tag{11}
\]
This inequality is about exact evaluations of the finite quadrature formula. It does not by itself bound floating evaluation of that formula.

The same derivative estimates give ideal quadrature error bounds below 1.859×10⁻⁷ for m₀ and 1.936×10⁻⁷ for m₁, with exact rational expressions retained. For m₁, the fourth derivative of vψ(v) is bounded by (81/4)(C₄+4C₃), and the ψ evaluation error contributes at most the bound in (11) after the outer Simpson sum. These deliberately conservative bounds suffice to distinguish the benchmark constants at the displayed coarse precision.

## 5. Positive α-bin bounds

An even nonnegative function decreasing on [0,∞) is a positive mixture of centered interval indicators. The convolution of two such interval indicators is even and decreasing on [0,∞), because their overlap length decreases with the separation. Applying layer-cake decomposition proves that ψ is even and decreasing on [0,1].

Each α bin lies on one side of the center α=2, or has that center as an endpoint. The minimum and maximum of its exact weight ω therefore occur at its two endpoints. Let J_j≥0 denote the exact positive unweighted mass of (2) in that bin, and let δ be the rational bound (11). Then
\[
\sum_j J_j\max\{0,\min(a_j,a_{j+1})-\delta\}
\le V_{\varepsilon,T}
\le\sum_j J_j\min\{1,\max(a_j,a_{j+1})+\delta\},
\tag{12}
\]
where a_j are the ideal exact Simpson ratios at the endpoints. The negligible event-series error (8) can be added separately if J_j is replaced by its ideal polynomial evaluation. The numerical columns in Section 1 evaluate these analytic expressions in ordinary floating arithmetic, and therefore retain the explicit qualification about rounding.

The central diagnostic uses (a_j+a_{j+1})/2 as a constant weight on each bin. Every CSV includes the endpoint weights, the analytic-only lower/upper weights, the positive J_j approximation, the three expanded center components, the cell count, and all weighted contributions. No adaptive or undocumented bin choice is made.

## 6. Independent checks and reproducibility

`check_prime_variance.py` performs the following bounded checks:

1. Exact formal-logarithm equality between direct event integration and the full ordered-pair intersection kernel plus both center terms, for T=5 on [10,45]. Coefficients are Λ(p^k)=log p through 54; in particular 16,25,27,32,49 are retained. A separate signed rational-coefficient example at T=4 on [11/2,23] prevents positivity from hiding an algebraic sign error.
2. Exact symbolic derivation of (9), the derivative coefficient norms, the three elementary integrals and the series coefficients through degree 12; exact rational cutoff and logarithm inequalities.
3. Integer checks n=p^k on every stored prime-power entry, with an independent factorization test on every integer 2≤n≤1000, including exclusion of integers with two distinct prime factors. The main sieve's prime detection and repeated-power generation are deterministic integer algorithms.
4. A 70-decimal calculation of all 22,390 cells at T=100 using the direct antiderivative (5), exact rational event positions, high-precision α endpoints, and independently computed prefix differences of prime-power logarithms. It uses the same frozen piecewise-constant weight. Its result is
\[
0.12040603689230832934313566686423073856\ldots,
\]
which differs from the primary float diagnostic by about 2.1×10⁻¹⁶. The largest individual unweighted-bin difference is about 2.1×10⁻¹⁵.
5. Independent 70-decimal adaptive integration of the actual autocorrelation at v=0,1/8,1/2,3/4,7/8,1. The discrepancies from the primary Simpson values are below 3.6×10⁻¹⁷.

The high-precision comparisons are diagnostics, not directed-rounding certificates. They do not promote the complete T=300 or 1000 calculations to proven intervals. The one repeated T=100 calculation is a precision check of an already requested value, not an added height scan.

Run from this directory:

```sh
python3 compute_prime_variance.py
python3 check_prime_variance.py
```

Both scripts also accept `--output-dir`; the checker accepts `--data-dir` to point to a frozen data package. Dependencies are NumPy, mpmath and SymPy. The actual run used Python 3.14, NumPy 2.4.4, mpmath 1.3.0 and SymPy 1.14.0. Neither a zeta-zero library nor external mathematical-model service is used. Timing fields are observations of this run, not a performance claim or a cross-machine benchmark.

The initial implementation used floating support comparisons. Before freezing, these were replaced by the exact integer fourth-root comparisons above, and a misleading generic cutoff field was split into the integer cutoff and the largest actual included prime power. This correction did not change any variance, CSV value or seed value. The final source and outputs are pinned in the receipt.

## 7. What the diagnostic establishes and what remains missing

The computation confirms that the R19 positive variance is practical to evaluate with the exact arithmetic interval, full prime powers, the fixed smooth seed and both mean terms. The explicit expanded components show why dropping a center would change the quantity substantially. The three finite values lie below the sine limiting benchmark and are far below the AH limiting value; no monotonicity, convergence rate or limit is inferred from three points.

R19 proves under RH that the full AH prediction would force V_{ε,T}→A, and that a strictly smaller limiting liminf of this actual variance would imply a positive limsup of the actual Bragg deficit. The missing input is still an **asymptotic arithmetic estimate at arbitrarily large T**, with all smoothing and center terms retained. Finite calculations do not supply that quantifier. No conversion of these three values into a finite-height zero-pair deficit is attempted.

Postponed: increasing T, fitting finite-size corrections, a directed-rounding enclosure, changing ε or the seed, evaluating actual zeta zeros, and obtaining the uniform short-interval covariance estimate needed for an AH or Dyson–Montgomery theorem. None is needed to reproduce the present bounded diagnostic.

## 8. Source and output index

Mathematical inputs, unchanged:

- [R19 positive variance proof](../../research-round19/bragg-variance-literature/BRAGG_WEIGHTED_SELBERG_VARIANCE.md), SHA256 `0c5323ac5a983148a9ec433ea1196fb0fd538f00872ac73e9de3ae105c7a2502`.
- [R16 Bragg target](../../research-round16/bragg-atom/BRAGG_ATOM_TARGET.md), SHA256 `2228bfd90e7a633683936d3d611f31c1f960107fbdf111a494993f73be16e120`.

Owned outputs:

- `compute_prime_variance.py`: deterministic three-height computation and analytic constants.
- `check_prime_variance.py`: independent exact and high-precision controls.
- `actual_prime_variance.json` and `.log`: all numerical summaries, cutoff counts, per-bin hashes, diagnostics and runtime metadata.
- `variance_T100_bins.csv`, `variance_T300_bins.csv`, `variance_T1000_bins.csv`: all 16,384 bins per height, without row omission.
- `prime_powers.npz`: exact integer n, prime base and exponent arrays; Λ is determined by log of the base.
- `seed_autocorrelation.csv` and `seed_quadrature.json`: every nonnegative endpoint weight, both Simpson resolutions, moments and exact rational analytic bounds.
- `prime_variance_checks.json` and `.log`: complete independent control results.
- `AUTHOR_RECEIPT.json`: hashes and scope of the frozen report, code, data and mathematical inputs.
