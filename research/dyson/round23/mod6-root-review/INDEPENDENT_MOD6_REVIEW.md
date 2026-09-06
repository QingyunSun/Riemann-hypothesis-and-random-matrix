# Independent root review of the fixed-modulus-six target

Date: 2026-09-05. Reviewer: root / Astra, distinct from author residual_gram.

## Verdict and exact object

I accept the ordinary proof of the two displayed estimates (6) and (7), and their use in the actual signed target (32) with the previously reviewed R22 inputs. I read the complete frozen 17,011-byte source, SHA256 ec3c4a258cf1ef2614e0255ee44c7c3a7e04268fe1655f082815f8012133285e, including both infinite tails and the source restriction. This is an internal mathematical review; it is not a proof-assistant certificate, external peer review or a global novelty finding.

The result changes the local centering, and then removes the now legitimate forbidden product rows. It does not lower the actual variance bound. Fixed-modulus PNT in arithmetic progressions is an unconditional input; RH is used only by the earlier transfer from the signed prime expression to the actual zeta statistic. In particular, this review does not replace that PNT with a GRH assertion.

The full target correction is
\[
2\sum_{m,h\ge1}b(m)(1+h/m)^{-T}(q_6-q_2)
=O_\omega\left(\eta_6(T^{7/4})+\frac1{T\log T}+2^{-T}\right).
\]
The complete forbidden product sum is nonnegative and
\[
2\sum_{A_6(m,h)=0}b(m)(1+h/m)^{-T}|q_6(m,h)|
=O_\omega\left(T^{-1}+\frac{2^{-T}}{(\log T)^2}\right).
\]
All statements refer to fixed modulus six and real \(T\ge4\), with asymptotic constants depending only on the fixed window.

## 1. Residue algebra and the forbidden single-prime rows

Write \(n=m+h\). For even shifts the admissible density normalizer is 3 when \(h\equiv0\pmod6\), and 6 when \(h\equiv2,4\pmod6\); it is zero on inadmissible rows. The local identity is
\[
q_6-q_2=S(h)\{(1-r_6/3)(\Lambda(m)+\Lambda(n))
+r_6-2\,1_{m\ {\rm odd}}\}.
\]
For \(d_h=S(h)(1_{h\equiv2}-1_{h\equiv4})\), the two coefficients separately satisfy
\[
S(h)(1-r_6/3)=\chi_6(m)d_h+S(h)1_{(m,6)>1}
=-\chi_6(n)d_h+S(h)1_{(n,6)>1}.
\]
I checked the signs also on inadmissible odd classes, where the prime endpoint survives. For example, \(m\equiv1,h\equiv2\pmod6\) gives a coefficient \(+S(h)\) on \(\Lambda(m)\), represented by \(+\chi_6(m)d_h\), even though the other endpoint is divisible by 3. This term cannot be removed as an exceptional prime power. The author's formula retains it. The actual exceptional staircase consists precisely of powers of 2 or 3.

Odd shifts cause no division by zero: \(S(h)=0\) and the specified convention \(r_6=0\) leaves \(q_6=q_2=\Lambda(m)\Lambda(n)\). The baseline \(r_6-2\,1_{m\ {\rm odd}}\) has zero period sum on each relevant even shift. The separate admissible formulas in (31), with singleton multiplier \(S(h)\) or \(2S(h)\), follow; changing only the constant to three would be wrong.

## 2. Signed singular-series prefix

The divisor expansion gives \(d_{2k}=S(2k)\chi_3(k)\). Complete multiplicativity of this fixed character gives the exact finite identity
\[
D(Y)=2C_2\sum_{\substack{d\le Y/2\\(d,6)=1}}
\frac{\mu^2(d)\chi_3(d)}{\prod_{p\mid d}(p-2)}
\sum_{j\le Y/(2d)}\chi_3(j).
\]
The inner prefix is bounded by one for every real endpoint. This is where the progression difference is taken before absolute values. Expanding
\[
\frac{\mu^2(d)}{\prod_{p\mid d}(p-2)}
=\frac1d\prod_{p\mid d}\left(1+\frac2{p-2}\right)
\]
on squarefree \(d\) coprime to six, then enlarging the remaining positive harmonic sum, bounds the total by
\[
(1+\log Z)\prod_{p>3}\left(1+\frac2{p(p-2)}\right).
\]
This convergent product proves \(D(Y)=O(\log(2+Y))\). No cancellation in the outer divisor variable is assumed. The separate nonnegative prefix bound \(\sum_{h\le Y}S(h)\le Y\) is the accepted R22 elementary divisor consequence and has a different role.

## 3. Forward transform and its true derivative scale

Stieltjes summation produces
\[
K_T(x)=\int_0^\infty D(h)\frac T x(1+h/x)^{-T-1}\,dh.
\]
Its differentiated kernel is
\[
\frac T{x^2}(1+h/x)^{-T-2}(Th/x-1).
\]
The logarithmic bound on \(D\) and the exact beta-integral masses in the author text give
\[
K_T(x)=O(\log(2x)),\qquad K_T'(x)=O(\log(2x)/x)
\]
uniformly for \(T\ge4\). The integral with the factor \(Tv+1\) has mass \(2T/(T+1)\), so no loss of a factor \(T\) is hidden. The logarithmic extra factor is controlled by \(v\), whose stated integral is uniformly bounded. These dominating integrals also justify differentiation.

Using both established bounds on \(b,b'\), on \([L,2U]\) the forward coefficient and derivative have bounds \(O(1/(x\ell))\) and \(O(1/(x^2\ell))\), respectively. Applying PNT in AP to this smoothed coefficient, instead of separately to every shift, is valid.

## 4. Backward transform, moving support and cancellation

The exact primitive removes the factor \((n-h)^{-T}\) before differentiating. Consequently
\[
C_T(n)=\frac{T}{n^T\ell^2}\int D(h)W_T(n-h)(n-h)^{T-2}\,dh.
\]
The integral is evaluated only where \(n-h\in[L,U]\). Its differentiated integrand includes the combined factor
\[
W_T'(s)s^{T-2}+W_T(s)s^{T-3}(Th/n-2),\qquad s=n-h.
\]
This follows by combining the derivative of \(n^{-T}\) with that of \(s^{T-2}\) before taking absolute values. Splitting these first would give an unjustified large bound. The smooth zero extension of \(W_T\) removes moving-support boundary terms, including at noninteger \(T\).

After extending the positive majorant to \(0<h<n\), the normalized variable \(h/n\) is beta \((1,T-2)\); its mean after multiplication by \(T\) is \(T/(T-1)\). This proves both bounds in (26), including the derivative \(O(\log(2n)/(n^2\ell^2))\), uniformly next to all window edges. No division by a vanishing bump occurs.

## 5. Exact PNT hypothesis, endpoints and infinite genuine-prime tails

For the fixed character modulo six, the final paragraph of [DLMF 27.11](https://dlmf.nist.gov/27.11) states PNT in fixed coprime progressions. I opened that primary page during this review and checked the stated scope. Subtracting the two classes after ordinary partial summation, and charging all higher powers by \(O(\sqrt{x}\log^2(2x))\), gives \(B_6(x)=o(x)\). Hence the tail supremum \(\eta_6(L)\) tends to zero; no effective rate or growing-modulus uniformity is asserted.

On \([L,2U]\), partial summation costs
\[
O\left(\eta_6(L)\left[\ell^{-1}
+\ell^{-1}\log(2U/L)\right]\right)=O(\eta_6(L))
\]
for each of the two smooth coefficients. The Stieltjes endpoint convention is correct for real \(L,U\); the lower coefficients vanish at the lower support edge.

For the forward tail use \(b(m)\ll U^{T-1}m^{-T}/\ell^2\), \(K_T(m)\ll\log(2m)\), and \(\Lambda(m)\le\log(2m)\). The summed tail has the scale
\[
\frac{U^{T-1}}{\ell^2}
(2U)^{1-T}\frac{\log^2(2U)}{T-1}=O(2^{-T}).
\]
The first integer term is absorbed because \(2U\ge T\). For the backward tail the actual support gives
\[
|C_T(n)|\ll U^{T-1}n^{-T}\log(2n)/\ell^2,\quad n>2U.
\]
The same sum applies. This tail proof keeps the primitive support and does not extend the coarse compact-window derivative bound into an infinite harmonic sum.

## 6. Periodic baseline and sparse exceptions

The period-six zero-mean baseline has uniformly bounded interval prefixes. For each fixed shift, integration by parts against \(b(m)k(m,h)\) on a dyadic \(m\)-block is valid. Its endpoint-plus-variation bound is \(O((X\ell^2)^{-1}(1+h/(2X))^{-T})\): the increasing variation of \(k\) can be integrated as a variation, rather than pointwise bounded by an extra \(T\). Summing against the nonnegative singular series costs \(O(X/T)\). Thus each block costs \(O(1/(T\ell^2))\), and the \(O(\ell)\) blocks cost \(O(1/(T\ell))\).

The far baseline bound retains the factor \(U\):
\[
O\left(\frac{U2^{-T}}{T^2\ell^2}\right).
\]
Absorbing it in \(O(1/(T\ell))\) is legitimate for \(U=T^{9/4}\) and all \(T\ge4\); deleting this factor before the absorption would be incorrect.

For exceptional powers of each fixed base 2 or 3, each near-window singleton row is \(O(1/(T\ell^2))\), by the same singular-series prefix and the correct forward or compact backward Pareto integral. There are \(O(\ell)\) powers. Far rows have size \(U^{T-1}r^{1-T}/(T\ell^2)\) or \(U^{T-1}r^{1-T}/\ell^2\), and sum geometrically with ratio at most \(2^{1-T}\). These give the claimed debt in (6).

On forbidden product rows, both singleton and baseline coefficients are exactly zero. A nonzero product then has a 2- or 3-power endpoint. The extra logarithm for the other endpoint raises the near-window total to \(O(1/T)\), as stated rather than incorrectly retaining \(O(1/(T\ell))\). For the far upper endpoint the primitive cancels the \(m\)-power and Chebyshev's bound controls the full other endpoint. For the far lower endpoint, the logarithmic factor is summable over powers; the first such power is between \(2U\) and \(6U\), and \(\log U/T=O(1)\). This verifies the entire \(O(2^{-T}/\ell^2)\) tail in (7).

## 7. Assembly and reproducibility

Both estimates are unconditional. Combining them with the full R22 singleton/parity reductions yields (32); combining with the inherited variance identity requires RH. The remaining signed expression has the same sufficient strict target \(1-M\) and is not bounded by this argument. The fixed congruence normalization neither implies a growing-wheel pair formula nor a uniform sub-square-root error for each shift.

I read the finite checker, copied only the frozen source and checker into an independent replay directory, and ran it there. The entire JSON and stdout each match the author output byte for byte, including source/checker pins and all fields. It checks 36 residue cases, 8 bounded divisor-prefix cases and 3 exact derivative/moment cases. These finite checks support algebra only; the all-parameter estimates were reviewed above as ordinary proofs. The source receipt's dependency hashes were checked without changing author files. No prime-height scan, new wheel enumeration or conjecture-fitting computation was run.
