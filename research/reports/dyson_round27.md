# Round 27: remove a central divisor band and separate calculable moments from the unresolved prime correlation

Date: 2026-09-06. Scope: ordinary mathematical arguments with internal independent reviews. The central divisor-band result assumes RH. The pure-divisor completion, exact coefficient and Gram identities, and source-valid progression statements are unconditional. No strict actual-variance improvement, AH refutation, Montgomery–Dyson/GUE theorem, RH proof, or new prime-gap bound is claimed.

The useful outcome is two precise simplifications of the arithmetic target. A whole central Möbius divisor band can be removed jointly. Separately, the pure divisor-approximant correlations have a finite arithmetic main with a globally vanishing error. Neither result supplies the missing correlation with the actual shifted prime sequence.

Read the [joint dispersion proof](../dyson/round27/joint-dispersion-test/JOINT_DISPERSION_TEST.md), its [independent review](../dyson/round27/joint-dispersion-review/INDEPENDENT_JOINT_DISPERSION_REVIEW.md), the [mixed-moment proof](../dyson/round27/mixed-moment-test/MIXED_MOMENT_DIRECTION_TEST.md), the [independent mixed-moment review](../dyson/round27/mixed-moment-review/INDEPENDENT_MIXED_MOMENT_REVIEW.md), and the [coordinator mixed-moment review](../dyson/round27/coordinator-mixed-review/COORDINATOR_MIXED_MOMENT_REVIEW.md). The [bounded Goldston–Yildirim source intake](../dyson/round27/coordinator-sieve-intake/GOLDSTON_YILDIRIM_TOOL_INTAKE.md) records which classical statements were actually used.

## 1. The current target has not changed

The complete R26 result assumes ordinary RH and states
\[
\overline V_T=\mathcal Z_T+2M+o(1).
\]
Here \(M=\int\omega\), and \(\mathcal Z_T\) is the full actual covariance with odd endpoints, even physical shifts, all prime powers, and the sharp scale-dependent divisor remainder
\[
c_Q(m)=\sum_{\substack{d\mid m\\d>Q}}\mu(d)\log(m/d).
\]
Its exact dyadic packets are
\[
Z_{ij}=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F_{ij}(m,h)c_{Q_j}(m)[\Lambda(m+h)-2],
\quad
Q_j=Y_j^{2/3},\quad Y_j=2^j\sqrt{\log T}.
\]
The full kernel \(F_{ij}\) is unchanged from R26; no prime coefficient is replaced by a generic sequence.

The inherited RH variance bound already implies
\[
-2M\le\liminf\mathcal Z_T\le\limsup\mathcal Z_T\le A-2M.
\]
Thus the global covariance is \(O(1)\). A growing bound for a single packet is a weaker local estimate, not evidence that the full covariance is unbounded.

The desired new statement remains
\[
\boxed{\liminf\mathcal Z_T<A-2M.}
\]
The benchmark \(\liminf\mathcal Z_T\le1-2M\) is stronger and sufficient, but is not the only possible success criterion. Neither inequality is proved here.

## 2. A central divisor band can be removed with its signs intact

Fix \(X=T^2\), \(Y=\sqrt X\), and one original compact central packet
\[
F(m,h)=b_T(m)\chi(m/X)V(h/Y)(m/(m+h))^T
\]
with fixed smooth compact profiles. Set
\[
Z(Q)=2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)c_Q(m)[\Lambda(m+h)-2].
\]
The new central-band lemma gives under ordinary RH
\[
\boxed{
Z(X^{1/3})-Z(X^{49/100})
=O(X^{-1/100}\log^3X).}
\]
This is a bound for a signed sum; it is not an absolute-value estimate for every divisor row.

The exact difference is
\[
2\sum_{\substack{X^{1/3}<d\le X^{49/100}\\d\ {\rm odd}}}
\mu(d)\sum_{k\ {\rm odd}}\log k
\sum_{h\ {\rm even}}F(dk,h)[\Lambda(dk+h)-2].
\]
The whole cofactor sum is retained. There is no inserted coprimality condition between \(d\) and \(k\). Completing physical shifts in the prime term and the odd cofactor lattice in the flat term makes their principal contributions cancel against one another. The remaining coefficient is
\[
a_{\rm band}(m)=
\sum_{\substack{X^{1/3}<d\le X^{49/100}\\d\ {\rm odd}}}
\frac{\mu(d)}d\log(m/d).
\]
Its two constant-two Möbius means cancel before RH is applied. The surviving main is a centered prime singleton
\[
\sum_{n\ {\rm odd}}\Lambda(n)G(n)-\int G,
\qquad
G(n)=\int F(n-h,h)a_{\rm band}(n-h)\,dh.
\]
The fixed completion order is 60. The seven error powers are
\[
-11/100,\ -1/100,\ -1/2,\ -49/100,\
-1/2,\ -13/25,\ -49/300,
\]
with the displayed logarithmic factors recorded in the full proof. The largest permissible bound is the one in the boxed statement.

The retained central rows therefore satisfy
\[
d>X^{49/100},\qquad 3\le k<2X^{51/100}.
\]
The \(k=1\) term is exactly zero. Both the balanced and unbalanced surviving regions remain. This central calculation has not been extended to remove the full global shift-dependent remainder.

## 3. The actual divisor approximant has a necessary extra term

Write
\[
A_Q(m)=\sum_{\substack{d\mid m\\d\le Q}}\mu(d)\log(m/d).
\]
Then \(c_Q=\Lambda-A_Q\). In terms of the standard logarithmic cutoff,
\[
\Lambda_Q(m)=\sum_{\substack{d\mid m\\d\le Q}}\mu(d)\log(Q/d),
\qquad B_Q(m)=\sum_{\substack{d\mid m\\d\le Q}}\mu(d),
\]
the exact relation is
\[
\boxed{A_Q(m)=\Lambda_Q(m)+\log(m/Q)B_Q(m).}
\]
The second term cannot be discarded, and a theorem for \(\Lambda_Q\) is not automatically a theorem for \(A_Q\).

The actual remainder vanishes on every prime. For a prime power with \(p>Q\),
\[
c_Q(p^a)=(1-a)\log p,
\]
while it vanishes when \(p\le Q\). It has both signs on composites. At the same real cutoff \(Q=150^{1/3}\in(5,6)\),
\[
c_Q(195)=\log13>0,\qquad c_Q(183)=-\log3<0.
\]
The generalized positive witness requires three distinct primes \(p,q\le Q<r\) and \(pq>Q\); two small factors alone do not suffice. Composite support does not license an upper-sieve substitution in a signed covariance.

## 4. The pure divisor moment is calculable with summable error

For the actual R26 packet let \(X=X_i,Y=Y_j,Q=Y^{2/3}\). Define
\[
\mathscr T_{ij}=
2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F_{ij}(m,h)A_Q(m)A_Q(m+h).
\]
Its finite arithmetic main is
\[
\begin{aligned}
\mathscr D_{ij}={}&
\sum_{h\ {\rm even}}
\sum_{\substack{d_1,d_2\le Q\ {\rm odd}\\(d_1,d_2)\mid h}}
\frac{\mu(d_1)\mu(d_2)}{[d_1,d_2]}\\
&\quad\times
\int F_{ij}(m,h)
\log(m/d_1)\log((m+h)/d_2)\,dm .
\end{aligned}
\]
The complete unconditional smooth-completion lemma gives
\[
\mathscr T_{ij}=\mathscr D_{ij}+O(Y_j^5/X_i^3),
\]
and therefore
\[
\boxed{\sum_{i,j}(\mathscr T_{ij}-\mathscr D_{ij})
=O((\log T)^5T^{-1/2}).}
\]

The reason is exact and elementary. Compatible odd divisor conditions select one progression modulo \(2[d_1,d_2]\). The logarithmic weight has amplitude \(O(X^{-1})\). Three derivatives in Poisson summation give progression error
\[
O\bigl(X^{-1}([d_1,d_2]/X)^2\bigr).
\]
Summing at most \(Q^2\) divisor pairs and \(O(Y)\) shifts gives \(YQ^6/X^3=Y^5/X^3\). The actual R26 ranges \(Y\ll(\log T)X/T\), \(X\ll T^{9/4}\) then give the claimed total by two geometric sums.

This corrects a substantive scope error in the earlier trial: the crude per-shift \(O(Q^2\log^2X)\) CRT budget grows after normalization, but that budget is not an intrinsic obstruction for these smooth packets. The improved proof eliminates that particular error. It leaves the finite divisor main explicit; it does not claim a new pointwise singular-series asymptotic.

## 5. The genuine-prime mixed moment still needs stronger accuracy

For
\[
\mathscr M_F=
2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F(m,h)A_Q(m)[\Lambda(m+h)-2],
\]
define the finite main
\[
K_Q(m,h)=
\sum_{\substack{d\le Q\\d\ {\rm odd}}}
\mu(d)\log(m/d)
\left(\frac{1_{(d,h)=1}}{\varphi(d)}-\frac1d\right).
\]
Ordinary Bombieri–Vinogradov, used below the one-half modulus boundary with endpoint suprema and common smooth weights, gives for every fixed \(B,\eta>0\)
\[
\mathscr M_F
=2\sum_{h\ {\rm even}}\int F(m,h)K_Q(m,h)\,dm
O_{B,\eta}\left(
Y(\log T)^{-B}+X^\eta Y/X+
\frac{YQ^3}{X^3\log T}\right).
\]
The nonprimitive term is handled using the actual prime-power condition \(p\mid h\), including the empty case \(p>Y\). The flat-center Poisson error uses three derivatives; claiming this particular error from only two derivatives would be incorrect.

The first displayed error is not summably small on natural polynomial-length packets for any fixed \(B\). This is a limitation of this bound, not a lower bound for the true error. Goldston–Yildirim II's own approximant and its stated errors do not remove the difficulty; its lowest allowed fixed-power cutoffs also do not cover every R26 polylogarithmic cutoff.

Even a perfect mixed-moment evaluation would retain
\[
Z_{ij}=
2\sum_{\substack{m\ {\rm odd}\\h\ {\rm even}}}
F_{ij}(m,h)\Lambda(m)[\Lambda(m+h)-2]-\mathscr M_{F_{ij}}.
\]
The unknown genuine prime-prime coefficient is still present with coefficient one.

## 6. Positive projections have the wrong direction for the desired upper bound

The exact centered prime interval function \(U_T\) in the original positive measure satisfies \(\|U_T\|^2=\overline V_T\). A legitimate fixed-cutoff interval feature \(V_R\) gives the exact identity
\[
\overline V_T
=2a\langle U_T,V_R\rangle-a^2\|V_R\|^2
+\|U_T-aV_R\|^2.
\]
Knowing the mixed and pure moments, and using positivity of the last term, supplies a lower bound for the actual variance. It does not supply the needed upper bound.

For finitely many features the corresponding statement is
\[
\overline V_T=v^*G^\dagger v+\|U_T-PU_T\|^2.
\]
The missing input would be an upper bound for the residual energy with enough accuracy to improve the actual variance. No numerical inversion of a Gram matrix replaces that input.

The actual \(Q_j\) depends on pair separation; it is not one coefficient sequence inside all intervals. Cross-scale Gram terms must be derived before a family of projections can represent it. Moreover, a nonzero off-diagonal packet with zero diagonal is not a positive semidefinite form merely because its edge weights are nonnegative.

## 7. A joint prime matrix keeps the cofactor sum, but does not yet bound it

On a balanced rectangle, define for odd \(m\)
\[
f_T(m)=X(\log T)^2
\sum_{h\ {\rm even}}F(m,h)[\Lambda(m+h)-2],
\qquad C_{d,k}=f_T(dk).
\]
Set \(f_T(m)=0\) for even \(m\). With the actual vectors \(a_d=\mu(d)\), \(b_k=\log k\),
\[
Z_{D,K}=\frac{2}{X(\log T)^2}a^{\mathsf T}Cb.
\]
The exact Gram entries retain
\[
\Lambda(dk+h)\Lambda(dk'+h')
-2\Lambda(dk+h)-2\Lambda(dk'+h')+4.
\]
They involve two affine prime forms, not just one sequence in residue classes.

A sufficient balanced-block condition is
\[
\|C\|_{\rm op}^2\ll X(\log X)^{2-\delta}
\]
for some fixed \(\delta>0\). This is stronger than necessary for the fixed vectors. The weaker vector-specific condition in the proof is also unproved.

The source-valid ordinary-RH mean square currently gives only
\[
\|C\|_{\rm op}^2\le\|C\|_{\rm F}^2
\ll_\eta X^{1+\eta}Y(\log X)^2.
\]
At \(Y=\sqrt X\), the resulting individual-block estimate still grows as a power. Calling the expression a Gram matrix does not create cancellation between its rows.

## 8. A legal use of the 186 theorem, and the exact missing transfer

For an actual balanced product, take
\[
\alpha(d)=\mu(d)1_{d\ {\rm odd}}1_{D<d\le1.1D},
\quad
\beta(k)=\log k\,1_{k\ {\rm odd}}1_{K<k\le1.1K}.
\]
The untwisted logarithmic coefficient satisfies the source's Siegel–Walfisz definition. Thus the presence of Möbius coefficients does not by itself invalidate the convolution theorem.

The exact parameter choice
\[
\omega=1/200,\quad\delta=1/1000,\quad\sigma=1/10
\]
satisfies the three inequalities in Proposition 2.18 of the 186 manuscript, with values \(48/125\), \(82/125\), and \(27/50\), respectively. With the stated fixed retreat, the actual convolution \(\alpha*\beta\) has the source's distribution estimate through \(X^{509/1000}\) on its admitted triply densely divisible moduli.

That statement does not allow multiplication by the second prime indicator \(\Lambda(m+h)-2\). The latter is neither a common smooth multiplier nor one of the permitted progression indicators. A signed upper-sieve replacement is not order preserving. Using the actual cofactor itself as modulus also leaves prime cofactors of size \(\sqrt X\) outside even single dense divisibility. Their omitted signed contribution has not been estimated.

These are precise failures of proposed transfers. They do not prove that all dispersion methods are impossible.

## 9. Validation, limitations, and next decision

The original manuscripts, scripts, complete outputs, source receipts, and independent reviews are preserved unchanged. The two mixed-moment corrections were incorporated before the author version was frozen: the third Poisson derivative and the positive witness's missing product condition. The pure-moment improvement emerged in independent review and was then proved explicitly in the final author manuscript.

Author algebra checks cover exact divisor signs, rational exponent budgets, progression densities and finite Gram identities. Independent copied runs verify complete output bytes. Formula syntax checks are separate from proof review; neither is proof-assistant verification. No new prime-height scan or PDF rebuild was performed to establish this checkpoint.

The next useful test is whether the proposed uniform operator norm is an appropriate target for this multiplicative matrix, or whether coherent Mellin modes make it unnecessarily strong compared with the fixed Möbius/log pairing. That test is separate work. The present report does not contain a bound for the residual norm, a strict inequality for \(\mathcal Z_T\), or a result about actual zeta universality.

The checkpoint intake preserves 48 original files / 1,992,602 bytes locally, with 41 files / 199,627 bytes public verbatim. Seven complete primary-source bodies or page images remain local with public hashes. All 113 dependency records verify, including nine explicitly recorded exact-byte path relocations. Both complete author/independent JSON-and-stdout pairs match. The earlier and corrected coefficient-sequence terminology versions remain separately preserved. See the [integration receipt](../logs/round27-integration/INTEGRATION_RECEIPT.json) and [source link map](../dyson/round27/SOURCE_LINK_MAP.md).
