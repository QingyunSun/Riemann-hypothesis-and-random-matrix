# Independent audit and completion of the singular-series main term

6 November 2026. This note audits the arithmetic packet and proves the remaining singular-series asymptotic using an existing uniform singular-series lemma. It does not prove the required prime-pair discrepancy estimate, and hence does not prove an RH-only zeta correlation result.

## 1. Result and dependencies

Let q, psi, Phi, L, alpha, beta and gamma=alpha+beta be as in the arithmetic packet. In particular q is real, even and smooth with compact support in (-eta,eta), psi is its inverse Fourier transform, c_psi=integral psi^3>0, and Phi is real smooth, supported in (1,2), with integral one. Assume

\[
\alpha-\eta>1,\qquad \beta>\eta,\qquad
\gamma+\eta<2,
\]

and the remaining stated packet-chamber margins. Write S_T for equation (12) of `CONDITIONAL_NEXT.md`. Then

\[
\boxed{\operatorname{Re}S_T=-\beta c_\psi+o(1).}
\]

The proof uses Fazzari-Gerspach Lemma 2.7, equation (2.29), and the prime number theorem. That lemma is a singular-series average, not their defective two-sign uniform prime-pair conjecture. Thus the main-term calculation does not inherit the endpoint defect in Conjecture 1.8.

Combined with the signed discrepancy hypothesis (11) of `CONDITIONAL_NEXT.md`, the raw prime packet has real part tending to -beta c_psi. Combined additionally with the packet's RH explicit-formula reduction, the proposed raw zero observable tends to +beta. Full local pair-AH would instead force it to zero by the count-moment argument. The unproved discrepancy hypothesis is therefore indispensable in the conditional conclusion.

The pointwise local square-root discrepancy is one sufficient input when alpha+3 beta+3 eta<2, with a strict margin. The weaker averaged signed discrepancy condition remains sufficient outside the pointwise error-transfer discussion.

## 2. Primary-source check

The local primary PDF is `/private/tmp/astra-zeta-nov06-quant/arithmetic/twisted.pdf`. I extracted its text and visually inspected printed p.17; the rendering is `fg-lemma-2-7.png` in this directory. Lemma 2.7 states, uniformly for the prime-power twist n=p^a and y in its large-y range,

\[
A_n(y):=\sum_{1\le h\le y}\mathfrak S_n(h)
=y-\frac12\min\{\log p,\log y\}
 +O((\log y)^{2/3}).
\tag{A}
\]

Replacing the error by O((1+log y)^(2/3)) handles all y>=1. Its proof refers to a prior singular-series estimate, not to the prime-pair conjecture. The section treats odd p in detail and explicitly says p=2 is obtainable with minor modification. The displayed lemma is uniform in n and y. [Versioned primary source](https://arxiv.org/abs/2412.20099v1)

No Ramanujan-series rearrangement is needed below. In particular, convergence issues in interchanging a conditionally convergent Ramanujan expansion with a shrinking-frequency kernel are avoided.

## 3. A uniform signed smoothing lemma

Let f be a fixed real even Schwartz function with integral over R equal to zero. Let H>=p>=2. Then (A) implies

\[
\boxed{
\sum_{h\ne0}\mathfrak S_{p^a}(h)f(h/H)
=-(\log p)f(0)
 +O_f\left((1+\log H)^{2/3}+(p/H)^2\right).
}
\tag{B}
\]

Here the sum excludes h=0. The singular series is even, so the left side is twice its positive-h part. Partial summation gives

\[
2\sum_{h\ge1}\mathfrak S_n(h)f(h/H)
=-2\int_0^\infty A_n(y)H^{-1}f'(y/H)\,dy.
\]

The term A_n(y)=y contributes 2H integral_0^infinity f=0. After writing y=Hu, the logarithmic term contributes

\[
\int_0^\infty
\min\{\log p,\log^+(Hu)\}\,f'(u)\,du.
\]

For u>=p/H this is the constant log p. Integrating that constant over the full half-line gives -(log p)f(0). The difference is supported on 0<=u<p/H. Since f is even, f'(0)=0 and |f'(u)|<=C_f u for u<=1. Consequently the transition contributes O_f((p/H)^2); the small interval Hu<1 is included in this bound. Finally, the error in (A) contributes at most

\[
C\int_0^\infty (1+\log(2+Hu))^{2/3}|f'(u)|\,du
\ll_f(1+\log H)^{2/3}.
\]

This proves (B), with its sign, factor of two, and exclusion of the diagonal explicit.

For our height kernel set

\[
f(u)=\operatorname{Re}\widehat\Phi(u/(2\pi)).
\]

It is even because Phi is real. Moreover f(0)=1 and integral_R f=2 pi Phi(0)=0, because Phi is supported away from zero. Thus the main term in (B) is exactly -log p, with no missing 2 pi factor.

## 4. Removing the nonlinear shift weight

The exact weight in the source packet is

\[
W_{n,h}(x)=\frac{q_\alpha(x/n)q_\gamma(x+h)}{\sqrt{x(x+h)}}
\widehat\Phi\left(\frac{T}{2\pi}\log\frac{x}{x+h}\right).
\]

Put H=x/T and define

\[
W^0_{n,h}(x)=\frac{q_\alpha(x/n)q_\gamma(x)}x
\widehat\Phi\left(-\frac{h}{2\pi H}\right).
\]

For |h|<=x/2, smoothness and Schwartz decay imply, for every fixed A,

\[
\boxed{|W_{n,h}(x)-W^0_{n,h}(x)|
\ll_A\frac{|h|}{x^2}(1+|h|/H)^{-A}.}
\tag{C}
\]

Indeed the denominator and q_gamma change by O(|h|/x) relatively at the amplitude scale 1/x. The two Fourier arguments differ by O(T(h/x)^2). Their intervening arguments remain comparable to h/H in absolute value. Multiplying the latter difference by a Schwartz derivative gives a term bounded by |h|/x^2 times (|h|/H), which is absorbed by increasing A before applying the bound.

The singular series is nonnegative. Formula (A) implies uniformly A_n(Y)<<Y for Y>=1, so partial summation gives

\[
\sum_{h\ne0}\mathfrak S_n(h)|h|(1+|h|/H)^{-A}\ll_A H^2
\]

when H>=1 and A>2. Hence the h-sum of the error in (C) is O(T^-2), uniformly in n and x.

On the comparable part of the original packet, x is at most 2 T^(gamma+eta). Also sum_n Lambda(n)|q_beta(n)|/n=O(L). After the x integral and normalization L^-3, the whole nonlinear-weight error is therefore

\[
O\left(T^{\gamma+\eta-2}/L^2\right)=o(1).
\tag{D}
\]

The region |h|>x/2, including nonpositive x+h and noncomparable positive variables, is handled before the linearization. The exact kernel there has a Fourier argument of size at least cT whenever both positive variables are comparable to their prescribed packets; outside comparable packets it is no smaller. The smooth packet supports bound all sums and integrals by fixed powers of T. Arbitrary Schwartz decay therefore makes this region negligible. The corresponding tails of the extended W^0 sum have |h|/H>T/2 and are likewise negligible. This justifies extending the linearized sum over every nonzero integer h.

## 5. Applying the signed smoothing lemma uniformly through the packet

For a prime-power n=p^a on the support, H/p is bounded below by

\[
\frac{x}{Tp}\ge\frac{x}{Tn}
\ge T^{\alpha-\eta-1}.
\]

Thus H>=p and p/H tends to zero by a fixed power, uniformly in every contributing n and x. Also log H=O(L). Applying (B) to the real part of W^0 gives

\[
\operatorname{Re}S_T
=-\frac1{L^3}\sum_n\frac{\Lambda(n)^2q_\beta(n)}n
\int_0^\infty q_\alpha(x/n)q_\gamma(x)\frac{dx}x
+o(1).
\tag{E}
\]

The smoothing error O(L^(2/3)) contributes O(L^(-1/3)) after the two logarithmic integrations. The transition error contributes O(T^(-2(alpha-eta-1))/L). These bounds, together with (D), justify the o(1) in (E).

The second Lambda factor in (E) is log p from the singular-series smoothing, equal to Lambda(n) for n=p^a. It is not log n when a>1. This distinction is necessary before discarding higher prime powers.

## 6. PNT convolution and exact coefficient

Set u=log(x/n)/L and v=log n/L. The x integral in (E) is

\[
L\int q(u-\alpha)q(u+v-\gamma)\,du.
\]

Higher powers p^a with a>=2 contribute o(1): on n>=T^(beta-eta), their sum of (log p)^2/n is power-small up to powers of L. For the prime terms, partial summation with the prime number theorem yields

\[
\operatorname{Re}S_T\longrightarrow
-\int\!\int v\,q(v-\beta)q(u-\alpha)
q(u+v-\gamma)\,du\,dv.
\]

Writing a=u-alpha and b=v-beta turns this into

\[
-\int\!\int(\beta+b)q(a)q(b)q(a+b)\,da\,db.
\]

The b term vanishes under (a,b)->(-a,-b), since q is even. Fourier inversion gives integral q(a)q(b)q(a+b)=integral psi^3=c_psi. The limit is therefore exactly -beta c_psi. In the original frequencies beta=1/5, the raw zero statistic has conditional limit +1/5.

## 7. Audit of the preceding reductions

### Raw versus distinct-index observables

The raw difference vanishes termwise on translated half-grids even with repeated labels: its complex phase ratio is exp(4 pi i(x_i-x_k)). Removing repeated-index subtraction is legitimate for this newly defined observable. It does change the sine prediction: the original distinct-index statistic and the raw statistic are not interchangeable.

Away from coordinate axes, the raw sine spectral density is

\[
1-\sum_j(1-|\xi_j|)_+
+2(1-\sum_j\xi_j^+)_+.
\]

In the high chamber it equals xi_2; in the low chamber it is zero. The even envelope cancels the first-order packet displacement, giving precisely beta c_psi. Thus the +1/5 coefficient and the prime-packet sign agree independently.

### Explicit formula and centering

With e(x)=exp(2 pi i x), each positive-frequency zero trace has prime term -L^-1 sum Lambda(n)n^-1/2 q(log n/L-alpha)n^-it. Multiplication of the three trace terms gives a minus sign. Height averaging produces Phi-hat(T log(mn/r)/(2 pi)), exactly the source convention.

The Fourier packet misses zero. All gamma-density Taylor moments consequently vanish; rapid decay handles the tail and the explicit pole evaluations. The claimed rapidly small remainders require fixed packet parameters, which are the parameters used here.

For alpha-eta>1, the unweighted long Dirichlet polynomial is rapidly small by Poisson summation: the phase has no stationary integer frequency on n>>T. Therefore replacing each long Lambda factor by Lambda-1 is valid for the complete packet. It is not a license to center the Hardy-Littlewood singular series term by term. The main-term proof above correctly starts from the uncentered pair correlation.

### Diagonal and short low packet

The h=0 prime-product diagonal forces all three von Mangoldt factors to be powers of one prime. Their positive lower packet cutoffs make its normalized contribution power-small. It is correctly excluded from the singular-series smoothing lemma.

The low packet is inside the restricted-correlation region. Its direct prime proof also works: near a product equality the target integer remains below T by a fixed power, so unequal integers are killed by the height Fourier kernel; exact equality is the negligible common-prime-power diagonal. In a general packet one should use this near-comparable argument, rather than require unnecessarily that the product of the two independent upper cutoffs be below T. The concrete eta<0.05 packet satisfies even that stronger easy condition.

### Fixed-window count moments

The positive bandlimited majorant construction in the source packet satisfies the Rudnick-Sarnak support restriction: for the \(r\)-fold convolution test, each frequency lies in \((-\delta,\delta)\) and their sum is zero, giving \(\sum_j|\xi_j|<r\delta\le k\delta<2\). It majorizes every cluster of diameter at most \(2W\). The height-localized distinct-tuple bound is \(O(T\log T)\); each tuple contributes at most \(4\pi W/\log T\) to the center integral. Repeated-index partitions then give all fixed local count moments. This uses the RH interval-cutoff extension stated after Rudnick-Sarnak Theorem 1.1. I found no missing occupancy hypothesis in this argument.

**Multiplicity convention checked explicitly.** Printed p.1028 says the ordinates are counted with multiplicities. Printed p.1029, directly after equation (1.4), specifies summation over distinct indices. Thus equal ordinate values carrying different zero indices are included in the starred correlation sum. The paper does not silently assume simplicity here. I checked the extracted source and visually inspected printed p.1029; `rs-distinct-indices.png` records the latter.

**Direct proof, also including multiplicities.** The root investigator proposed this alternative, and its coefficient and mean-square bounds were independently checked here. Fix an integer \(k\ge1\) and choose a nonnegative even Schwartz majorant \(\phi\ge1\) on \([-W,W]\), with smooth Fourier support in \((-\delta,\delta)\), where \(k\delta<1\). Such a majorant exists at arbitrarily small positive bandwidth, with constants depending on W,k. Under RH the explicit formula gives, uniformly for \(t\in[T,2T]\),

\[
0\le K_W(t)\le\sum_\gamma\phi(L(\gamma-t)/(2\pi))
\le C_{W,k}+2|D(t)|,
\]

where the zero sum includes multiplicity and

\[
D(t)=\sum_{p\le T^\delta}a_p p^{-it},\qquad
a_p=\frac{\log p}{L\sqrt p}\widehat\phi(\log p/L).
\]

The bounded gamma-density term and pole terms are absorbed into C. Prime powers \(p^a\) with \(a\ge2\) also contribute \(O(1)\) in absolute value: the squares use \(\sum_{p\le T^{\delta/2}}\log p/p\ll L\), and the contributions from \(a\ge3\) are absolutely summable before division by \(L\).

Chebyshev's prime bound and partial summation give \(\sum_p|a_p|^2=O_{W,k}(1)\). Write \(D(t)^k=\sum_{m\le N}b_m m^{-it}\), where \(N\le T^{k\delta}\). Unique prime factorization and Cauchy-Schwarz over at most k! ordered representations give

\[
\sum_m|b_m|^2\le k!\left(\sum_p|a_p|^2\right)^k.
\]

For m!=n, the elementary integral bound is

\[
\left|\int_T^{2T}(m/n)^{-it}dt\right|
\le\frac{2N}{|m-n|}.
\]

Using \(2|b_mb_n|\le|b_m|^2+|b_n|^2\) and the harmonic sum \(H_N\),

\[
\frac1T\int_T^{2T}|D(t)|^{2k}dt
\le\left(1+\frac{4NH_N}{T}\right)\sum_m|b_m|^2
=O_{W,k}(1).
\]

The strict inequality \(k\delta<1\) makes \(NH_N/T\) tend to zero. It follows that the \(2k\)-th local count moment is bounded, and therefore every fixed count moment is bounded. This direct proof requires RH for positivity of the zero majorant but no simplicity assumption and no convention about factorial correlations. It independently confirms the Rudnick-Sarnak argument.

The source's quantitative pair-AH bound is also valid: the off-half-grid pair count B_eta gives |R|<=4 pi eta K^3+2K B_eta, followed by a fourth-moment tail split. Schwartz tails are controlled by the same fixed moments and rapid envelope decay. This concerns full local off-lattice pair concentration, not protected-band pair matching.

### The localized discrepancy exponent

After x=nm the exact weight is 1/sqrt(x(x+h)); there is no additional n factor. A local discrepancy O(X^(theta+epsilon)), a weight variation O(X^-1), approximately X/T relevant shifts, and sum_{n~N} Lambda(n)=O(N) give error NX^theta/(T L^3), up to epsilon factors. Thus beta+theta(alpha+beta)<1 is correct. For theta=1/2 it is alpha+3 beta<2. Including packet widths gives the sufficient strict inequality alpha+3 beta+3 eta<2. No improvement to the source paper's different observable is claimed by this accounting.

## 8. Scope and the remaining obstacle

This completes the singular-series calculation that the earlier continuation had deliberately left open. The resulting theorem is conditional on a specified near-product prime-pair discrepancy functional; it is not an unconditional or RH-only exclusion of AH. The exact main term is consistent with the source paper's twisted-correlation mechanism and requires no claim of external novelty.

The meaningful next problem is now sharper: prove the signed discrepancy functional is o(1), or bound it away from the precise cancellation that would erase the -beta c_psi singular-series contribution. Standard first-order prime density cannot do that. The phase kernel has zero integral, so its mean-density term cancels and the secondary singular-series term survives.
