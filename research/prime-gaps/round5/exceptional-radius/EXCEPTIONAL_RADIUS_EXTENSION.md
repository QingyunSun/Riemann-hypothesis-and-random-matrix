# A variable-radius version of the exceptional-square estimate

**Status:** ordinary written derivation from the primary paper, with an exact rational reproduction of its finite numerical certificate. This extends the stated parameter range of Proposition 3.11 without adding a prime-distribution hypothesis. It does not establish a new prime-gap bound or certify a new support geometry.

**Primary source:** OpenAI, *Improved short gaps between primes*, dated 30 August 2026, Propositions 2.23, 3.10 and 3.11, Lemmas 3.2, 3.3 and 3.9, equations (3.26)–(3.35). The [primary PDF](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf) has Proposition 3.11 on page 23. The locally retained text is ../../sources/openai-short-gaps.txt, lines 1522–1607. The local text is the source actually checked in this audit; its SHA256 is ded13a7c74fcfce64e85769e05b5869803dccdf53b88be2c2f3c0b344f95ee84.

**Artifacts:** certify_exceptional_radius.py is a standalone Python-standard-library certificate. certify_exceptional_radius.json contains the exact reduced rational upper bounds and all endpoint checks. No float arithmetic or numerical quadrature enters those upper bounds.

## 1. Conclusion and certified constants

Replace the fixed physical coefficient radius 11/40 in Proposition 3.11 by a fixed radius r. Keep the same prime cap, exceptional minorant, fixed-profile assumptions, 1024 bins, and strict CRT slack. The same argument works throughout

\[
\frac{4879903}{40960000}<r<\frac{59499}{200000},
\qquad 0.1191382568359375<r<0.297495.
\tag{1}
\]

This range has the convenient stronger condition 0<z_j<xi_0<xi_* for every bin. Proposition 3.10 itself only requires z_j<xi_*, giving the slightly wider lower endpoint in Section 3.

The following terminating decimals are **exact rational upper bounds**, rather than rounded numerical approximations. Every last printed digit belongs to the certificate.

| Physical coefficient radius r | Certified K_1024^+(r), exact decimal | Simpler safe upper bound |
|---|---:|---:|
| 0.272 | 0.3014041534851816226069683 | 0.301405 |
| 0.2742997 | 0.3273225381113663650584938 | 0.327323 |
| 0.275 | 0.3361336040272905676441604 | 0.336134 |
| 0.276 | 0.3495799968949037559942978 | 0.349580 |
| 0.278 | 0.3800259215656200578230129 | 0.380026 |
| 0.280 | 0.4163697504037337478611794 | 0.416370 |
| 0.282 | 0.4605417963468921175216614 | 0.460542 |

At r=11/40 the exact reduced fraction is

\[
K_{1024}^{+}(11/40)=
\frac{840334010068226419110401}
{2500000000000000000000000},
\tag{2}
\]

which reproduces equation (3.35) of the paper exactly. In particular, the scale printed as “1025” by the text extraction is **10 to the power 25**, not the integer 1025.

One may safely use any K at least K_1024^+(r) in the exceptional-square conclusion. The same finite-bin proof cannot justify retaining K=0.34 at r≥0.276: a separate exact lower bound on its bin constant already exceeds 0.34 there; see Section 5. This does not assert that every other possible method of bounding the exceptional sum must fail with 0.34. Conversely, using the actual physical radius 0.2742997 in this proposition permits the smaller exceptional constant in the table, subject to the common-support condition below.

## 2. Precise parametric proposition

Keep the setting and normalization P_x of Proposition 3.11. Fix

\[
a_* = \frac{40481}{100000},\qquad
\xi_* = \frac{9519}{50000},\qquad
\xi_0 = \frac{19037}{100000} < \xi_*.
\]

Let C_i be a finite real linear combination, with coefficients independent of x, of the same canonical (k−1)-coordinate sums and exact faces used in that proposition. Assume their profiles are fixed and bounded and have limiting-null discontinuity sets. Let H_i denote their corresponding combination of canonical profiles and marginals.

Assume every summand has physical coefficient-root radius at most r, and every outer and inner coefficient root satisfies the original global largest-prime-factor cap

\[
P^+\!\left(\prod_j d_j\right)\le x^{\xi_0}.
\tag{3}
\]

The radius assumption must hold for **all roots actually used in the linear combination**. In particular, it is insufficient to use the radius of an outer trial function if an inner correction, another summand, or a separately constructed exact-face array has larger retained-coordinate radius. A valid sufficient choice is the maximum over all outer, inner, correction and exact-face radii. An exact face obtained through Lemma 3.3 retains the same total support bound as its parent array.

For fixed r in (1), define K_1024^+(r) by equation (12) below. Then

\[
\sum_n' b(n+h_i;x)\,C_i(n)^2
\le P_x\left(K_{1024}^{+}(r)\,\|H_i\|_2^2+o(1)\right).
\tag{4}
\]

The norm remains the full fragment norm. Every profile, radius, cutoff and finite band choice is fixed before x tends to infinity; exact face arrays may depend on x as in the original proposition. No assertion uniform as r approaches the upper endpoint is made.

This is deliberately stated for the same canonical class as the source. It does not assert that an arbitrary coefficient array has a bounded inverse diagonal merely from a radius bound.

## 3. Exact parameter range and the strict counting slack

Write

\[
h=\frac{a_*-2\xi_*}{1024}=\frac{481}{20480000},
\qquad s_j=2\xi_*+jh\quad(1\le j\le1024),
\]

\[
c(r)=1-2r-\frac1{5000},\qquad
z_j(r)=\frac{c(r)-s_j}{2}
=\frac{1-2r-s_j}{2}-\frac1{10000}.
\tag{5}
\]

Since s_j increases, the minimum z occurs at j=1024 and the maximum at j=1. Direct rational arithmetic gives

\[
z_{1024}(r)=\frac{59499}{200000}-r=0.297495-r,
\]

\[
z_1(r)=0.3095082568359375-r.
\tag{6}
\]

Thus all z_j are positive exactly when r<0.297495. The stronger condition z_1<xi_0 is exactly the lower bound in (1). The necessary condition for Proposition 3.10 is only z_1<xi_*, which gives

\[
\frac{24397467}{204800000}<r<\frac{59499}{200000},
\qquad 0.1191282568359375<r<0.297495.
\tag{7}
\]

Both are strict ranges. At the upper endpoint the last auxiliary exponent is zero, and the proof's Selberg-energy asymptotic with a fixed positive exponent is unavailable.

For every bin, every valid r has exactly the original counting margin:

\[
s_j+2r+2z_j=1-\frac1{5000}=\frac{4999}{5000}<1.
\tag{8}
\]

The following endpoint values show the requested radii lie comfortably inside the valid range.

| r | Minimum z_j | Maximum z_j |
|---|---:|---:|
| 0.272 | 0.025495 | 0.0375082568359375 |
| 0.2742997 | 0.0231953 | 0.0352085568359375 |
| 0.275 | 0.022495 | 0.0345082568359375 |
| 0.276 | 0.021495 | 0.0335082568359375 |
| 0.278 | 0.019495 | 0.0315082568359375 |
| 0.280 | 0.017495 | 0.0295082568359375 |
| 0.282 | 0.015495 | 0.0275082568359375 |

The original displayed bound z_j<863/25000=0.03452 is specific to r=0.275 and need not be retained. The operative inequalities are positivity, z_j<xi_*, the global coefficient cap xi_0<xi_*, and (8).

## 4. Arithmetic proof of the extension

**Diagonal reduction.** Apply exactly the inversion and face identities from Lemmas 3.2 and 3.3, as in the first paragraph of Proposition 3.11. They express C_i as B_{y_x,i} for a uniformly bounded raw array with the same physical radius bound and hereditary prime cap. The full diagonal norm converges to the norm of H_i. Neither identity uses the numerical value 11/40.

**Marked-prime separation.** In Proposition 3.10 use the ambient retained-index cap min{zeta,xi_0/rho_*}. Its physical exponent is at most xi_0. Every marked prime p or q has exponent at least xi_*, so it exceeds both that cap and the auxiliary cutoff exponent z_j. These are exactly the separation hypotheses xi_*>max{rho_* zeta_eff,z_j} needed by Proposition 3.10.

**Nonsquarefree exceptions.** Proposition 2.23 bounds the number of nonsquarefree points in the exceptional support by O(x^(1−xi_*)). Lemma 3.2 and the divisor bound make each fixed canonical sum x^o(1) pointwise; a finite linear combination and its square have the same form of bound. Consequently their total contribution is x^(1−xi_*+o(1))=o(P_x). A fixed change of radius does not remove this fixed power saving. The same original fixed-shift endpoint treatment remains applicable.

**Positive majorant.** On the remaining squarefree support, Proposition 2.23 gives b≤(12/5)N_2, where N_2 counts unordered marked pairs p<q with p,q≥x^(xi_*) and pq<x^(a_*). On the exceptional support all prime factors are at least x^(xi_*); Lemma 3.9 therefore gives L_{x^(z_j)}=1 for every selected bin. The majorant is positive before opening any signed coefficient expansion, so the full square C_i^2 remains intact.

**Counting each bin.** For pairs in the jth logarithmic-product bin, pq≤x^(s_j). Apply Proposition 3.10 with radius r and exponent z_j. Its ordinary CRT error is x^(s_j+2r+2z_j+o(1))=x^(4999/5000+o(1))=o(P_x), by (8). No distribution theorem for primes or the minorant enters this counting step. There are only 1024 bins, fixed independently of x.

**Limiting pair measure.** The same prime harmonic measure as in the source gives

\[
d\mu_2(s)=f(s)\,ds,\qquad
f(s)=\frac1s\log\frac{s-\xi_*}{\xi_*},
\qquad 2\xi_*\le s\le a_*.
\tag{9}
\]

The strict arithmetic condition pq<x^(a_*) remains in the last bin. Its limiting measure is unchanged by inclusion of the endpoint because this measure has no atom there. Thus the exact limiting constant supplied by the bin argument is

\[
K_{\mathrm{bin}}(r)=
\frac{12}{5}\sum_{j=1}^{1024}
\frac{\mu_2((s_{j-1},s_j])}{z_j(r)}.
\tag{10}
\]

It remains to certify a number above this finite sum; Section 5 does so. This proves (4). All applications are instances of the primary ordinary-counting argument with a fixed changed radius.

## 5. Finite-sum certificate and why the continuum integral alone is insufficient

The natural continuous expression is

\[
K_{\mathrm{cont}}(r)=\frac{24}{5}
\int_{2\xi_*}^{a_*}
\frac{\log((s-\xi_*)/\xi_*)}{s(c(r)-s)}\,ds.
\tag{11}
\]

Within each bin, 1/(c(r)−s) is increasing. Therefore K_cont(r)≤K_bin(r). A good approximation or even a certified upper bound for K_cont alone does **not** automatically upper-bound the larger K_bin delivered by the actual arithmetic proof. We retain the paper's finite-bin certificate.

First, f in (9) is increasing throughout the interval. Differentiation yields

\[
f'(s)=\frac{s/(s-\xi_*)-\log((s-\xi_*)/\xi_*)}{s^2}.
\]

Set y=(s−xi_*)/xi_*. Here 1≤y<2, since a_*<3xi_*. Hence log y<1 while s/(s−xi_*)=1+1/y>1. The derivative is positive. In consequence, the measure of each bin is at most h f(s_j).

Set t_j=(s_j−2xi_*)/xi_*. These rational numbers belong to (0,1). The degree-21 alternating polynomial

\[
L_{21}(t)=\sum_{m=1}^{21}\frac{(-1)^{m+1}t^m}{m}
\]

satisfies log(1+t)≤L_21(t) by the alternating-series remainder. Each bin contribution in (10) is therefore at most

\[
u_j(r)=\frac{24hL_{21}(t_j)}{5s_j(c(r)-s_j)}.
\]

Every u_j(r) is positive and rational for rational r. Define

\[
K_{1024}^{+}(r)=\frac1{10^{25}}
\sum_{j=1}^{1024}\left\lceil10^{25}u_j(r)\right\rceil.
\tag{12}
\]

Then, in the correct direction,

\[
K_{\mathrm{cont}}(r)\le K_{\mathrm{bin}}(r)
\le\sum_j u_j(r)\le K_{1024}^{+}(r).
\tag{13}
\]

The script implements (12) with exact integers and fractions. Its ceiling operation is −floor(−numerator/denominator), with positive denominator. It never converts an input radius or an intermediate summand to binary floating point. An input decimal such as 0.2742997 is parsed as its exact rational value.

The accumulated upward-rounding excess is strictly below 1024×10^(−25)=1.024×10^(−22). The alternating-polynomial excess in the sum is at most

\[
\sum_j\frac{24h}{5s_j(c(r)-s_j)}\frac{t_j^{22}}{22}.
\]

For the requested radii this latter bound is between 1.87×10^(−22) and 3.06×10^(−22). The coarser right-endpoint discretization remains the main deliberate overestimate. Reducing it is a separate possible numerical refinement, not needed here.

For an additional check, the script also constructs a lower bound on K_bin. Since f is increasing and the even alternating polynomial L_22 lies below log(1+t), the jth bin contribution is at least

\[
\ell_j(r)=\frac{24hL_{22}(t_{j-1})}
{5s_{j-1}(c(r)-s_j)}.
\]

Rounding each nonnegative term down at scale 10^(−25) gives a rigorous rational lower bound on K_bin. At r=0.276 it equals 0.3489733171373295715615596, which already exceeds 0.34. At r=0.280 and r=0.282 these lower bounds are respectively 0.4156565419431563765185887 and 0.4597595157187387148411848. Thus the need to update the constant in this bin proof is not inferred merely from its upper bound exceeding 0.34.

All factors depending on r are increasing as r increases within the valid interval. In particular, both the continuum constant and the finite-bin bound are increasing, and the rounded bound in (12) is nondecreasing. A constant certified at an upper radius R consequently applies to all smaller radii for which the same proof conditions hold.

## 6. What must change downstream when this constant is used

This result supplies an exceptional-square input to the hybrid sieve; it does not certify new mixed-modulus factorizations or source conditions. Those conditions, support realizability, the actual retained prime cap and the root radii require their own checks.

If the original choices m_0=49999/50000, lambda=1/125 and kappa_def=1/50000 are retained, equation (4.28) becomes

\[
b_h(r)=\left(1-\frac{m_0}{\lambda}\right)
\kappa_{\mathrm{def}}K
=-\frac{49599}{20000000}K,
\qquad K\ge K_{1024}^{+}(r).
\tag{14}
\]

One must therefore recompute b_h, d_0 and every numerical functional or cover weight depending on them. The source's convenient assertion |b_h|<1/1000 is equivalent here to K<20000/49599. It fails for the constants in the table at r=0.280 and r=0.282. This failure does not invalidate the hybrid algebra: it means that a downstream proof cannot cite that old numerical shortcut unchanged.

In particular, restoration should check its actual coefficient

\[
1-\rho_*|b_h(r)|C_{\mathrm{op}}>0
\]

using the operator bound justified for the new support. Do not reuse C_op=4 beyond its proved support range simply because the exceptional counting proof remains valid there. The primary statement also requires d_0>0 and 0<a_h+b_h<1 wherever those multiplier bounds are invoked.

The exceptional proposition is dimension-independent at the level of this displayed constant for fixed k, but that observation does not transfer a k=40 numerical trial, norm certificate or prime-gap conclusion to k=39.

## 7. Reproduction and audit record

Run the standalone script with Python 3:

    python3 certify_exceptional_radius.py

It writes certify_exceptional_radius.json next to itself. Optional radii can be supplied as exact decimal or rational strings with --radii. The implemented certificate deliberately enforces the stronger range (1), even though Section 3 explains the slightly weaker necessary condition.

Checks completed in this audit:

1. Read the primary proofs of Propositions 2.23, 3.10 and 3.11 and the relevant support/face identities; identified exactly where radius enters.
2. Verified every one of the 1024 rational auxiliary exponents is positive, below xi_0, and has the identical strict CRT margin, for all seven requested radii.
3. Verified the odd/even alternating-polynomial difference is t^22/22 and positivity holds at every endpoint.
4. Reproduced the primary fraction in (3.35) exactly, not only its decimal digits.
5. Verified the rounding excess bound and monotonic order of the seven certified constants.
6. Cross-checked the first five values against the prime agent's separate implementation; they agree to all communicated digits, with differences in the final displayed digit explained by rounding versus this document's exact terminating decimals.
7. Added a separately directed L_22/left-density/downward-rounding lower bound on the actual bin constant to verify the strict obstruction to retaining 0.34 in this proof at r≥0.276.

Large integer numerator and denominator fields are serialized as decimal strings in the JSON, to prevent loss when it is read by a JavaScript consumer. Reconstruct the exact fraction from those strings rather than passing the decimal display through a binary float.

The certificate is exact arithmetic accompanying an ordinary proof. It has not been formalized in Lean, and this note makes no claim that an improved global prime-gap inequality has yet been certified.
