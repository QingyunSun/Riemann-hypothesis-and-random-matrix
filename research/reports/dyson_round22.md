# Round 22: remove linear and parity terms from the actual pair-correlation target

Date: 2026-09-05. This checkpoint follows the substantive Round 21 correction. The impossible all-shifts sub-square-root premise is replaced by a legitimate renormalization of the full signed arithmetic sum. Ordinary PNT suffices to make the complete singleton correction negligible. A separate unconditional proof then removes every odd shift from the renormalized pair sum. A controlled parity-baseline change finally leaves only odd endpoints and even shifts.

The resulting signed quadratic estimate is still open. The work does not refute AH-Pairs, prove the Montgomery or GUE conjectures, or improve a zeta-zero or prime-gap bound. These are ordinary proofs and applications of classical tools, with internal independent review, without a novelty or proof-assistant claim.

## 1. The same fixed actual-zeta objective

Keep the fixed bump, all prime powers and exact length average of [Round 21](dyson_round21.md). Write
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},\quad T\ge4,
\]
\[
W_T(x)=\omega(\log x/\ell),\qquad
b_T(m)=\frac{T m^{-T}}{\ell^2}\int_1^mW_T(x)x^{T-2}dx,
\qquad k_{m,T}(h)=(1+h/m)^{-T}.
\]
The weight is zero for \(m\le L\). The Pareto factor is retained exactly; neither its large-shift tail nor the continuous prime window is replaced by an approximation.

For \(a_n=\Lambda(n)-1\) and \(c_h=\mathfrak S(h)-1\), the old remainder is
\[
\mathcal E_T=2\sum_{m,h\ge1}
b_T(m)k_{m,T}(h)[a_ma_{m+h}-c_h].
\tag{1}
\]
Under RH the already proved transfer says
\[
\overline V_T=M+\mathcal E_T+o(1),\qquad
M=\int\omega,\qquad
\limsup_T\overline V_T\le A.
\tag{2}
\]
The exact fixed constants satisfy \(M\approx0.1851531433\) and \(A\approx1.0105877964>1\). As before, decimals are inherited diagnostics; the targets use the defining integrals.

Proving \(\liminf\mathcal E_T\le1-M\) would give a strict deficit below \(A\), hence a positive limsup of the frequency-two zeta-pair deficit. Either strict assertion would exclude the full AH-Pairs hypothesis under RH. No strict inequality is proved in this round.

## 2. Why the pointwise obstruction does not prevent a weighted estimate

Round 21 proves that a bound
\[
\sup_{X<z\le2X}
\left|\sum_{X<m\le z}[a_ma_{m+h}-c_h]\right|
\ll X^\beta\log^B X
\]
uniformly over all shifts and all sufficiently large heights cannot hold with \(\beta<1/2\). At \(h=1\), it would force an impossible improvement of the prime-counting error and remove a genuine zeta pole.

The actual contribution of \(h=1\) in (1) is nevertheless negligible. The new [small-shift proof](../dyson/round22/small-shift-obstruction/SMALL_SHIFT_REMOVAL.md) makes this distinction quantitative. Uniformly for integers \(1\le K\le L\),
\[
2\sum_m b_T(m)\sum_{h\le K}k_{m,T}(h)
|a_ma_{m+h}-c_h|
\ll_\omega \frac K\ell+K\ell T^{-7/8}+K2^{-T}
\tag{3}
\]
unconditionally. Thus all \(K=o(\log T)\) shifts may be removed in absolute value.

Under RH, for any subset \(\mathcal H\) of odd integers in \([1,K]\),
\[
\left|
2\sum_m b_T(m)\sum_{h\in\mathcal H}k_{m,T}(h)
[a_ma_{m+h}+1]\right|
\ll_\omega |\mathcal H|T^{-7/8}+|\mathcal H|2^{-T}.
\tag{4}
\]
This removes odd \(K=o(T^{7/8})\), with the cancellation inside each centered block retained. Equation (4) is not an absolute bound on individual coefficients.

The unconditional input in (3) is a uniform dimension-two upper sieve. For even \(h\le X\), the number of forbidden classes at a prime \(p\) is one if \(p\mid h\) and two otherwise. Its local density is uniformly below one, its dimension axiom has a constant independent of \(h\), and its squarefree modulus error is bounded by \(\tau(d)\). Applying the fundamental upper sieve with fixed parameter and level \(X^{1/2}\) gives
\[
\sum_{X<m\le2X}\Lambda(m)\Lambda(m+h)
\ll X\mathfrak S(h)+\sqrt X\log^3X.
\]
All higher prime powers are included in the error. For odd \(h\), a nonzero product has an even power of two as one endpoint, giving the stronger elementary \(O(\log X)\) bound on this block.

The required singular-series upper average is especially simple:
\[
\boxed{\sum_{1\le h\le K}\mathfrak S(h)\le K.}
\tag{5}
\]
The positive divisor expansion reduces it to
\[
C_2\prod_{p>2}\left(1+\frac1{p(p-2)}\right)=1.
\]
Combining this inequality with the sieve, elementary Chebyshev and exact weight bounds proves (3). Its [independent review](../dyson/round22/small-shift-review/INDEPENDENT_SMALL_SHIFT_REVIEW.md) checks the growing-shift uniformity explicitly. It does not infer that uniformity from a fixed-pattern prime-tuple theorem in the [Tao sieve notes](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/).

These removal ranges do not cover the entire natural shift scale \(h\asymp m/T\), which runs from \(T^{3/4}\) to \(T^{5/4}\). The next transformation addresses the full sum by a different argument.

## 3. Exact singular-series centering removes the complete linear correction

Define
\[
q_{m,h}=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-1].
\tag{6}
\]
The identity
\[
a_ma_{m+h}-c_h
=q_{m,h}+c_h(a_m+a_{m+h})
\tag{7}
\]
is exact. The change is legitimate only if the whole signed correction can be controlled:
\[
\mathcal L_T=
2\sum_{m,h\ge1}b_T(m)k_{m,T}(h)c_h(a_m+a_{m+h}).
\]
Put
\[
\eta(L)=\sup_{y\ge L}
\frac{|\Psi(y)-\lfloor y\rfloor|}{y}.
\]
The new full proof gives, unconditionally,
\[
\boxed{
\mathcal L_T=O_\omega(\ell^{-1}+\eta(L)+2^{-T})=o(1).
}
\tag{8}
\]
Ordinary PNT supplies \(\eta(L)\to0\). Under RH the more useful stated rate is
\[
\mathcal L_T
=O_\omega(\ell^{-1}+\ell T^{-7/8}+2^{-T}).
\tag{9}
\]
The transfer from the actual variance still requires RH. Only the arithmetic change of center in (8) is unconditional.

The key step handles the two marginals with their different kernels. For the forward marginal, the known uniform singular-series transform is
\[
\sum_{h\ge1}c_h(1+h/m)^{-T}
=-\tfrac12\log(m/T)+O(1).
\]
For the backward marginal set \(n=m+h\). Its exact kernel is
\[
f_n(h)=b_T(n-h)(1-h/n)^T
=\frac{T}{n^T\ell^2}I_T(n-h),
\qquad
I_T(y)=\int_1^yW_T(x)x^{T-2}dx,
\tag{10}
\]
with zero extension when \(n-h\le L\). This exact cancellation of powers prevents a derivative loss from an approximate product.

In particular, with \(m=n-h\),
\[
f_n''(h)=\frac{T}{n^T\ell^2}
[W_T'(m)m^{T-2}+(T-2)W_T(m)m^{T-3}].
\tag{11}
\]
Its derivative support is exactly \(m\in[L,U]\). It may have either sign. The proof bounds its absolute logarithmic moment using a Beta\((2,T-2)\) envelope; it never treats the signed derivative as a probability density and never divides by a small \(b_T(n)\).

Writing
\[
A_2(y)=\sum_{h\ge1}(y-h)_+c_h
=-\tfrac12y\log y+O(y),
\]
the exact hinge identity and endpoint give
\[
\sum_h c_h f_n(h)=\int_0^\infty A_2(y)f_n''(y)dy,\qquad
\int_0^\infty y f_n''(y)dy=b_T(n).
\]
Hence, uniformly on \(L<n\le2U\),
\[
\sum_hc_hf_n(h)
=-\tfrac12b_T(n)\log(n/T)
+O_\omega((n\ell^2)^{-1}).
\tag{12}
\]
The region \(n>2U\) is treated through the actual support of (11), giving an exponentially small tail; the error in (12) is not summed to infinity.

Both marginals therefore yield the same smooth linear term:
\[
\mathcal L_T=-2\sum_{L<n\le2U}
b_T(n)a_n\log(n/T)+O_\omega(\ell^{-1}+2^{-T}).
\tag{13}
\]
Chebyshev and partial summation give
\(\sum_{L<n\le2U}|a_n|/n=O(\ell)\), which makes the error \(O(1/\ell)\). A pointwise \(|a_n|\le1+\log n\) bound here would lose the needed logarithm. Finally PNT applied to the smooth weight \(b_T(x)\log(x/T)\) controls the remaining main sum by \(O_\omega(\eta(L))\).

Read the [complete author proof](../dyson/round22/singleton-renormalization/SINGLETON_RENORMALIZATION.md) and [independent full derivation](../dyson/round22/singleton-renormalization-review/INDEPENDENT_SINGLETON_DERIVATION.md). The independent derivation keeps a looser polynomial-times-exponential tail, sufficient for the same conclusion; the author sharpens that tail using the signed triangular transform. Both retain all centers, endpoints and powers. Their prime-number input is the classical [PNT formulation for \(\Psi\)](https://dlmf.nist.gov/25.16.E3).

## 4. Every odd shift disappears from the new pair sum

Let
\[
\mathcal Q_T=2\sum_{m,h\ge1}b_T(m)k_{m,T}(h)q_{m,h}.
\]
Equation (8) gives \(\mathcal E_T=\mathcal Q_T+o(1)\). On odd shifts the singular series is zero, so \(q_{m,h}=\Lambda(m)\Lambda(m+h)\). The entire odd contribution is nonnegative, and the [standalone odd-pair proof](../dyson/round22/odd-primepower-pairs/ALL_ODD_PRIMEPOWER_PAIRS.md) establishes the explicit unconditional bound
\[
\boxed{
0\le
2\sum_m b_T(m)\sum_{\substack{h\ge1\\h\ {\rm odd}}}
k_{m,T}(h)\Lambda(m)\Lambda(m+h)
\le\frac{32\|\omega\|_\infty}{T}
+\frac{64\|\omega\|_\infty\,2^{-T}}{\ell^2}.
}
\tag{14}
\]
This covers all shifts and both infinite endpoint tails, not only the small range of (4).

One endpoint of each nonzero odd pair is \(2^j\), with von Mangoldt weight \(\log2\). Split according to whether that endpoint is lower or upper. In \((L,2U]\) there are \(O(\log T)\) such powers, and elementary monotone integral comparisons bound each row. Above \(2U\), the exact integral defining \(b_T\), an explicit Chebyshev bound and a geometric sum over the powers control both tails. The constants 32 and 64 are deliberately loose analytic bounds; no new prime-data experiment determines them.

This deletes odd shifts from \(\mathcal Q_T\). It does not separately prove that the complete odd portion of the old \(\mathcal E_T\) tends to zero. The global singleton correction (8) must be applied first. Moving this order of operations would erase real linear terms.

## 5. The parity baseline must change before even endpoints can be removed

Even shifts preserve the parity of the two endpoints. One cannot simply restrict (6) to odd \(m\): at an even endpoint with \(\Lambda(m)=\Lambda(m+h)=0\), it still has the nonzero baseline \(\mathfrak S(h)\).

Define instead
\[
q^{(2)}_{m,h}=\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)
[\Lambda(m)+\Lambda(m+h)-2\,1_{\{m\ {\rm odd}\}}].
\]
The exact difference is
\[
q^{(2)}_{m,h}-q_{m,h}
=\mathfrak S(h)(2\,1_{\{m\ {\rm odd}\}}-1).
\tag{15}
\]
Partial sums of this alternating parity factor have absolute value at most one. Summation by parts with the exact \(b_Tk_{m,T}\) weight and (5) proves
\[
2\sum_{m,h\ge1}b_T(m)k_{m,T}(h)
[q^{(2)}_{m,h}-q_{m,h}]
=O_\omega((T\ell)^{-1}).
\tag{16}
\]
The full shift average in a dyadic block is controlled by
\[
\sum_h\mathfrak S(h)(1+h/(2X))^{-T}
\le 2X/(T-1).
\]
The actual \(m>2U\) tail is bounded separately, without discarding an alternating boundary term.

For even \(m\) and even \(h\), every nonzero singleton in \(q^{(2)}\) occurs at a power of two, and its baseline is now zero. Summing over the lower or upper power-of-two endpoint gives
\[
2\sum_{\substack{m\ {\rm even}\\h\ge2,\ h\ {\rm even}}}
b_T(m)k_{m,T}(h)|q^{(2)}_{m,h}|
=O_\omega((T\ell)^{-1}+2^{-T}/\ell^2).
\tag{17}
\]
The [complete parity-adjustment proof](../dyson/round22/parity-adjusted-target/PARITY_ADJUSTED_PAIR_TARGET.md) proves (16) and (17) unconditionally. Its assembly section explicitly identifies the separate singleton and odd-pair dependencies.

After those dependencies are accepted, the complete new target is
\[
\boxed{
\mathcal E_T=\mathcal P_T+o(1),
}
\]
\[
\boxed{
\mathcal P_T=
2\sum_{\substack{m\ {\rm odd}\\h\ge2,\ h\ {\rm even}}}
b_T(m)k_{m,T}(h)
\{\Lambda(m)\Lambda(m+h)
-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\}.
}
\tag{18}
\]
The singleton constant is two, reflecting the allowed parity class. This is a controlled change of normalization, related to classical removal of a local congruence factor. It does not supply a new upper estimate for the surviving quadratic expression.

## 6. The remaining precise theorem target

Under RH, combining the reviewed arithmetic transformations with the unchanged variance transfer gives
\[
\boxed{\overline V_T=M+\mathcal P_T+o(1).}
\tag{19}
\]
Therefore a sufficient next theorem would be
\[
\boxed{\liminf_{T\to\infty}\mathcal P_T\le1-M.}
\tag{20}
\]
No result here proves (20), a sign for \(\mathcal P_T\), or convergence of it to the sine-kernel prediction zero. RH alone still provides only the inherited upper information at \(A-M\); the gap \(A-1>0\) remains.

The substantive gain in formulation is that the exact residual no longer carries the particular singleton obstruction which invalidated the old proposed pointwise shortcut. All odd shifts and even prime-power endpoints are controlled after the correct global transformations. A new estimate must now act on the remaining two-prime expression with its singular-series-weighted marginals. Replacing those marginals by their means inside each short interval would reintroduce an unproved assertion.

The natural-scale even shifts remain far beyond the removable \(o(\log T)\) range of (3). A one-prime arithmetic-progression theorem from the prime-gap 186 work is still insufficient by itself. Any proposed dispersion, mean-square or heat-energy estimate must account for the surviving signed coefficients on the full \(T^{7/4}\) to \(T^{9/4}\) prime window. A claimed all-shifts sub-square-root bound for the new coefficient is not established merely because the old \(h=1\) obstruction has been removed.

## 7. Review, preservation and the next bounded work

The small-shift proof has a full independent source and analytic review, including the uniform fundamental-sieve hypotheses. The singleton correction has two complete derivations and a [separate final-source review](../dyson/round22/singleton-renormalization-review/INDEPENDENT_AUTHOR_REVIEW.md); the signed derivative and tail estimates are checked as mathematics, not inferred from the scalar tests. The explicit all-odd bound has a full root review and an independent copied replay of its seven exact scalar checks. The root-authored parity lemma has a [separate independent review](../dyson/round22/parity-adjusted-review/INDEPENDENT_PARITY_ADJUSTMENT_REVIEW.md), with complete dependency acceptance recorded in the [root assembly review](../dyson/round22/root-review/ROOT_ROUND22_REVIEW.md).

All original source versions, receipts, checker outputs and the coordinator's accepted-through-Round-21 tools memo remain preserved. The [intake manifest](../dyson/round22/INTAKE_MANIFEST.json), [source-link map](../dyson/round22/SOURCE_LINK_MAP.md) and [integration receipt](../logs/round22-integration/INTEGRATION_RECEIPT.json) identify current accepted versions and exact local/public copies. Full third-party source bodies remain local with public hashes. No prime-height scan, RMT simulation, external model session or new PDF compilation is part of this checkpoint.

The next bounded research should attempt an actual inequality for (18), or determine precisely which proposed analytic or sieve estimate fails at its required scale. Further local-congruence normalization is useful only if it exposes a provable gain for that signed quantity. A large family of equivalent expressions, by itself, does not advance the strict bound. The autonomous goal remains active, and no famous-conjecture solution is claimed.
