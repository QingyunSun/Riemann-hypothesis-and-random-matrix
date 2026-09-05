# A centered prime-pair target for the actual exponential-length variance

Date: 2026-09-05. Status: bounded ordinary-mathematics derivation, submitted for independent review. The transfer to the actual variance assumes RH. The singular-series calculation is unconditional. No strict variance bound, AH refutation, or new theorem on the zeta pair correlation is proved.

**Substantive correction after the first review:** the original section 5 treated the all-shifts premise (31) with \(\beta<4/9\) as merely unproved. It is impossible, already at \(h=1\), by the unconditional obstruction below. This corrects the feasibility assessment, not Proposition 1, Lemma 2, the Abel bound (29), or the actual signed target (6). The original manuscript SHA 81a676d68836bff15a50ba6190bf2c1eab7cd54f0d3ae85d604a48fc36a7e54e and its prior check/review receipts are preserved under superseded-before-h1-obstruction. The originating coordinator identified the issue in task 01a0702b-e4b0-7020-ae61-b1fe718932c1; this revised text includes the ordinary proof.

The useful output is a completely centered arithmetic target with an explicit constant, together with a quantitative audit of a tempting square-root prime-pair-error input. This is an application of classical singular-series averaging, not a novelty claim. It does not substitute a new coefficient sequence for the von Mangoldt function.

## 1. The exact missing inequality

Use the fixed Round 16 smooth autocorrelation bump, epsilon \(1/4\), and the actual Round 20 statistic
\[
W_T(x)=\omega(\log x/\log T),\qquad
\omega(\alpha)=\psi((\alpha-2)/\varepsilon),\qquad
M=\int\omega(\alpha)d\alpha=\varepsilon m_0.
\tag{1}
\]
Thus \(W_T\) is supported on \([L,U]=[T^{7/4},T^{9/4}]\). Here \(m_0=\int\psi\), and \(A=1+\varepsilon^2m_1\) is the already proved RH upper bound. Retain every prime power in \(\Lambda\), including \(\Lambda(1)=0\). Put
\[
a_n=\Lambda(n)-1,\quad n\ge1,
\qquad
b_T(m)=\frac{T m^{-T}}{\log^2T}
\int_1^m W_T(x)x^{T-2}\,dx.
\tag{2}
\]
All the \(b_T(m)\) are nonnegative; \(b_T(m)=0\) for \(m\le L\).

For an integer \(h\ge1\), write the classical prime-pair singular series as
\[
\mathfrak S(h)=
\begin{cases}
0,&h\text{ odd},\\
2C_2\displaystyle\prod_{\substack{p\mid h\\p>2}}\frac{p-1}{p-2},
&h\text{ even},
\end{cases}
\quad C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right),
\quad c_h=\mathfrak S(h)-1.
\tag{3}
\]
Define the actual signed pair error
\[
\boxed{
\mathcal E_T
=2\sum_{m\ge1}b_T(m)\sum_{h\ge1}
\left(1+\frac hm\right)^{-T}
\left[a_ma_{m+h}-c_h\right].}
\tag{4}
\]
For \(T\ge4\), these sums converge absolutely before any cancellation is used.

**Proposition 1.** Under RH,
\[
\boxed{\overline V_T=M+\mathcal E_T+o(1).}
\tag{5}
\]
Consequently the requested sufficient bound is exactly
\[
\boxed{\liminf_{T\to\infty}\mathcal E_T\le1-M.}
\tag{6}
\]
The already proved RH bound gives only
\(\limsup\mathcal E_T\le A-M\). RH plus the precise AH-Pairs hypothesis gives \(\mathcal E_T\to A-M\), so it is consistent with the available result and fails (6).

Using the previously recorded bump quadrature, only for orientation,
\[
M\approx0.1851531432653023,\quad
1-M\approx0.8148468567346977,\quad
A-M\approx0.8254346531489499.
\tag{7}
\]
The improvement needed in this normalization is \(A-1\approx0.0105877964142522\). These decimals are inherited diagnostics, not new interval certificates. The exact target is (6). In particular the target does not require proving \(\mathcal E_T\le0\), which would give the much stronger GUE-predicted constant \(M\).

## 2. Discrete centering preserves the continuous prime-mean cancellation

Let
\[
S_{\lambda,T}(x)=
\sum_{x<n\le e^{\lambda/T}x}a_n.
\tag{8}
\]
The continuous centered interval count in Round 20 equals \(S_{\lambda,T}(x)+r_{\lambda,T}(x)\), where exactly
\[
r_{\lambda,T}(x)
=\lfloor e^{\lambda/T}x\rfloor-\lfloor x\rfloor
-(e^{\lambda/T}-1)x,\qquad |r_{\lambda,T}(x)|\le1.
\tag{9}
\]
This is valid for all \(x,\lambda\), including noninteger endpoints, with the stated half-open convention.

Use the positive measure
\[
d\mu_T=\frac{T}{\log^2T}
e^{-\lambda}W_T(x)\frac{dx}{x^2}\,d\lambda.
\tag{10}
\]
The remainder has squared norm
\[
\|r\|_{\mu_T}^2
\le\frac{T\|\omega\|_\infty}{L\log^2T}
=O_\omega(T^{-3/4}/\log^2T).
\tag{11}
\]
Round 20 supplies \(\|\Delta\|_{\mu_T}^2=\overline V_T=O_\omega(1)\) under RH. The triangle inequality followed by Cauchy–Schwarz therefore gives
\[
\overline V_T-\|S\|_{\mu_T}^2
=O_\omega(T^{-3/8}/\log T)=o(1).
\tag{12}
\]
No first moment of primes on a short interval has been replaced by its expectation. Both prime-continuum terms remain present inside \(a_ma_n\); their large cancellation is preserved exactly up to (9).

For fixed \(m,n>x\),
\[
\int_0^\infty e^{-\lambda}
1_{\{m,n\le e^{\lambda/T}x\}}d\lambda
=\left(\frac{x}{\max(m,n)}\right)^T.
\tag{13}
\]
Expanding (8) and using (13) gives, exactly,
\[
\|S\|_{\mu_T}^2
=\sum_m b_T(m)a_m^2+
2\sum_m b_T(m)\sum_{h\ge1}
\left(1+\frac hm\right)^{-T}a_ma_{m+h}.
\tag{14}
\]
The factor two, the lower endpoint \(x<\min(m,n)\), and the exponent \(T\) have not been approximated. For absolute convergence of the actual part, use \(|a_n|\le1+\log n\). For the comparison part, the elementary bound \(\mathfrak S(h)\ll_\eta h^\eta\) for any fixed \(\eta>0\) suffices. One proof bounds the product in (3) by a constant times \(2^{\nu(h)}\), and uses the elementary divisor bound. Since \(x\le U\), the tails in \(m,n\) then converge for \(T\ge4\).

## 3. A uniform singular-series lemma for the exact Pareto kernel

The needed unconditional primary input is Montgomery–Soundararajan, equation (16), printed p.4:
\[
R_2(k)=2\sum_{1\le h<k}(k-h)c_h
=-k\log k+O(k).
\tag{15}
\]
The source proves a sharper remainder. The weakened form displayed here is sufficient. Extending the sum linearly between consecutive integers gives
\[
A_2(y):=\sum_{h\ge1}(y-h)_+c_h
=-\frac12y\log y+O(y)\qquad(y\ge1).
\tag{16}
\]
Indeed the left side is piecewise linear; linear interpolation of \(y\log y\) differs from it at the integers by the same \(O(y)\) bound. Set \(A_2(y)=0\) for \(0\le y\le1\).

**Lemma 2.** Uniformly for real \(T\ge4\) and \(m\ge T\),
\[
\boxed{
\sum_{h\ge1}c_h(1+h/m)^{-T}
=-\frac12\log(m/T)+O(1).}
\tag{17}
\]
The implied constant is absolute.

**Proof.** Let \(k(y)=(1+y/m)^{-T}\). Two Stieltjes integrations by parts, or integrating each hinge in (16), give
\[
\sum_hc_h k(h)=\int_0^\infty A_2(y)k''(y)dy,
\quad
k''(y)=\frac{T(T+1)}{m^2}(1+y/m)^{-T-2}.
\tag{18}
\]
Boundary terms vanish because \(A_2(y)=O(y\log(2y))\) and \(T\ge4\). In particular
\[
\int_0^\infty yk''(y)dy=1.
\tag{19}
\]
Thus the error in (16) contributes \(O(1)\). Replacing (16) also on \(0<y<1\) costs at most
\(O((T/m)^2\int_0^1y|\log y|dy)=O(1)\).

The measure \(yk''(y)dy\) is a probability measure. Under \(u=Ty/m\) its density is
\[
(1+1/T)u(1+u/T)^{-T-2}du.
\tag{20}
\]
Its mean \(u\) is \(2T/(T-1)\le8/3\). On \(0<u<1\) the density is at most \(5u/4\). Therefore its expectation of \(|\log u|\) is uniformly bounded, proving
\[
\int y\log y\,k''(y)dy=\log(m/T)+O(1).
\tag{21}
\]
For a check on constants, the exact expression is
\(\log m+\mathrm{digamma}(2)-\mathrm{digamma}(T)\); for integer \(T\) this is \(\log m+1-H_{T-1}\). The uniform proof uses only (19)–(20). Equations (18)–(21) prove (17). \(\square\)

A dangerous shortcut is avoided here. Replacing \((1+h/m)^{-T}\) by \(e^{-Th/m}\) against absolute, uncentered pair masses can cost \(m/T^2\), which grows in the part \(m\asymp T^\alpha\), \(\alpha>2\). Lemma 2 evaluates the original kernel by the proved signed singular-series average.

## 4. Diagonal and comparison terms: proof of Proposition 1

With \(W_T\) extended by zero, the substitution \(x=mu\) gives
\[
b_T(m)=\frac{T}{m\log^2T}
\int_0^1
\omega\!\left(\frac{\log m+\log u}{\log T}\right)u^{T-2}du.
\tag{22}
\]
The mean value theorem, and
\(\int_0^1|\log u|u^{T-2}du=(T-1)^{-2}\), show
\[
b_T(m)=\frac{T}{T-1}\frac{W_T(m)}{m\log^2T}
+O_\omega\!\left(\frac1{mT\log^3T}\right).
\tag{23}
\]
Use this bound on \(L<m\le2U\). For \(m>2U\), the original integral gives an exponentially small total tail: \(b_T(m)\ll_\omega U^{T-1}m^{-T}/\log^2T\). The actual and comparison sums there are at most a fixed polynomial in \(U,T\) times \(2^{-T}\). In particular
\[
\sum_m b_T(m)=O_\omega(1/\log T).
\tag{24}
\]

On RH, partial summation of \(\Psi(x)=x+O(\sqrt x\log^2(2x))\), with the prime-power correction retained, gives
\[
\sum_{n\le z}a_n^2=z\log z+O(z).
\tag{25}
\]
For example, \(\sum\Lambda(n)\log n\) follows by partial summation; its difference from \(\sum\Lambda(n)^2\) is supported on powers of exponent at least two and is \(O(\sqrt z\log^3(2z))\). Expanding \((\Lambda-1)^2\) then proves (25). Ordinary PNT estimates also suffice, but RH is already assumed here.

Equations (23)–(25) imply
\[
\sum_m b_T(m)a_m^2
=\int\alpha\omega(\alpha)d\alpha+o(1).
\tag{26}
\]
The error in (23), even bounded using \(a_m^2\ll\log^2(2m)\), sums to \(O_\omega(T^{-1})\) on \([L,2U]\). The \(O(z)\) error in (25), integrated against the smooth weight \(W_T(z)/z\), contributes \(O_\omega(1/\log T)\) after normalization.

By Lemma 2 and (24),
\[
\begin{aligned}
2\sum_m b_T(m)\sum_h c_h(1+h/m)^{-T}
&=-\sum_m b_T(m)\log(m/T)+O_\omega(1/\log T)\\
&=-\int(\alpha-1)\omega(\alpha)d\alpha+o(1).
\end{aligned}
\tag{27}
\]
The same tail and weight estimates justify the second line. Adding (26) and (27) gives \(M\); (12) and (14) prove (5). The argument never evaluates a critical-line logarithmic Dirichlet series.

## 5. Exactly how strong a prime-pair error estimate would suffice

The identity (5) is the sharp target for this particular statistic. A uniform absolute error estimate provides a formal norm benchmark, but the sub-square-root version of that benchmark is impossible for the actual centered coefficients. It must not be proposed as a feasible next arithmetic target.

For \(X\) in the present window, \(X<z\le2X\), and an integer \(h\ge1\), define
\[
E_X(z,h)=
\sum_{X<m\le z}\left[a_ma_{m+h}-c_h\right],
\qquad H=X/T.
\tag{28}
\]
These are centered prime-pair errors, including the two singleton prime errors and the integer-count endpoint. They are not discrepancies in one reduced residue class.

A direct Abel-summation estimate for one dyadic block gives
\[
\left|2\sum_{X<m\le2X}b_T(m)
\sum_{1\le h\le X}(1+h/m)^{-T}
[a_ma_{m+h}-c_h]\right|
\ll_\omega
\frac1{X\log^2T}
\sum_{1\le h\le X}(1+h/(2X))^{-T}
\sup_{X<z\le2X}|E_X(z,h)|.
\tag{29}
\]
To verify the norm, differentiate (22):
\[
|b_T(m)|\ll_\omega(m\log^2T)^{-1},
\qquad
|b_T'(m)|\ll_\omega(m^2\log^2T)^{-1}.
\tag{30}
\]
For fixed \(h\), \(m\mapsto(1+h/m)^{-T}\) is increasing. Its variation on \([X,2X]\) is at most its upper endpoint. These facts bound the endpoints and total variation of the product by the coefficient in (29). The omitted \(h>X\) tail is exponentially small since \(m\le2X\) and \(T\to\infty\); use the polynomial absolute bound on the coefficients and integrate \((1+h/(2X))^{-T}\). This is valid uniformly throughout the window.

If a bound
\[
\sup_{X<z\le2X}|E_X(z,h)|
\ll X^\beta(\log X)^B,\qquad 1\le h\le X,
\tag{31}
\]
held uniformly for all sufficiently large \(T\), all \(X\) in the stated window, and all indicated shifts, then
\[
\text{dyadic contribution}
\ll_\omega H X^{\beta-1}(\log X)^{B-2}.
\tag{32}
\]
Indeed \(\sum_{h\ge1}(1+h/(2X))^{-T}\le2X/(T-1)\). Summing \(O(\log T)\) blocks costs at most one additional logarithm. Pure exponent bookkeeping places the formal threshold at \(\beta<4/9\), but (31) is impossible for every \(\beta<1/2\). Thus this threshold describes an unavailable all-shifts premise, not a route to a strict variance bound.

### The \(h=1\) obstruction, including the singleton endpoints

Write \(E(y)=\Psi(y)-y\). For integers \(X<z\le2X\), let
\[
P_X(z)=\sum_{X<m\le z}\Lambda(m)\Lambda(m+1).
\tag{32a}
\]
In every nonzero summand the even member must be a power of \(2\). There are \(O(\log X)\) possible indices up to \(2X+1\), each product at most \((\log2)\log(2X+1)\). Therefore \(0\le P_X(z)\ll\log^2X\), uniformly. Higher prime powers are included; no assertion about Mersenne or Fermat primes is used.

Since \(c_1=-1\), the exact integer-endpoint identities are
\[
\begin{aligned}
E_X(z,1)
&=P_X(z)-[\Psi(z)-\Psi(X)]
-[\Psi(z+1)-\Psi(X+1)]+2(z-X)\\
&=P_X(z)-2[E(z)-E(X)]-\Lambda(z+1)+\Lambda(X+1)\\
&=-2[E(z)-E(X)]+O(\log^2X).
\end{aligned}
\tag{32b}
\]
In particular these singleton terms cannot be discarded from the centered pair.

Suppose (31) held with fixed \(\beta<1/2\) and fixed logarithmic loss. For every sufficiently large \(X\), choose \(T=\sqrt X\), so that \(X=T^2\) belongs to the window. Thus its all-large-\(T\) uniformity supplies the hypothesis on every large integer block. Choose
\(\max(\beta,0)<\theta<1/2\); (32b), absorbing the logarithms, gives
\[
|E(z)-E(X)|\ll X^\theta
\quad(X,z\text{ integers},\ X<z\le2X).
\tag{32c}
\]
Telescope along powers of \(2\), then use one last block to reach an arbitrary integer \(N\). The geometric series yields \(E(N)=O(N^\theta)\). For real \(y\), \(E(y)=E(\lfloor y\rfloor)-\{y\}\), so the same bound holds on the real axis.

For \(\Re s>1\), logarithmic differentiation of the absolutely convergent Euler product and partial summation give
\[
\int_1^\infty E(y)y^{-s-1}dy
=\frac{-\zeta'/\zeta(s)}s-\frac1{s-1}.
\tag{32d}
\]
The bound \(E(y)=O(y^\theta)\) makes the left side holomorphic on \(\Re s>\theta\), by locally uniform absolute convergence, also after differentiation. There is a nontrivial critical-line zero \(\rho\). If its multiplicity is \(m_\rho\ge1\), the right side has the nonzero residue
\[
-m_\rho/\rho
\tag{32e}
\]
at \(\rho\). The subtraction at \(s=1\) cannot cancel it. Uniqueness of meromorphic continuation contradicts that holomorphy. This proves the impossibility of (31) with \(\beta<1/2\).

The obstruction is unconditional: existence of a critical-line zero suffices; RH is not needed. The classical inputs were checked at [NIST DLMF 25.2.11](https://dlmf.nist.gov/25.2.E11) and [DLMF 25.10(i)](https://dlmf.nist.gov/25.10). The dyadic argument uses the original all-large-\(T\) premise; no such global conclusion has been deduced from a premise on only a sparse sequence of heights.

This is not an obstruction to the signed aggregate (6), an averaged estimate over shifts, or a theorem restricted to another specified shift range. In fact, under RH, (32b) and (29) bound the single \(h=1\) contribution on a block by \(O_\omega(X^{-1/2})\); its sum over this logarithmic window is \(o(1)\). An impossible pointwise premise is therefore compatible with a potentially useful averaged bound. Restricted or averaged hypotheses require their own complete error budgets.

### The square-root budget and the genuinely open signed average

For the often proposed square-root-size hypothesis \(\beta=1/2+\eta\), the power in (32) at \(X=T^\alpha\) is
\[
H X^{\beta-1}
=X^{1/2-1/\alpha+\eta}
=T^{\alpha/2-1+\alpha\eta}.
\tag{33}
\]
The exact range calculation is:

| \(\alpha\) | \(H=X^{1-1/\alpha}\) | power at \(\eta=0\) in \(X\) | consequence of this absolute-error method |
| --- | --- | --- | --- |
| \(7/4\) | \(X^{3/7}\) | \(-1/14\) | power decay |
| \(2\) | \(X^{1/2}\) | \(0\) | logarithms and constants decide; no automatic \(o(1)\) |
| \(9/4\) | \(X^{5/9}\) | \(1/18\) | power loss |

These are method-budget statements, not lower bounds for the actual errors. For the entire bump, a hypothetical signed-aggregation saving \(H^\rho\) beyond the square-root-per-shift/absolute-sum budget would overcome the worst power when \(\rho>1/10\), after choosing a sufficiently small fixed \(\eta>0\):
\[
\frac1{18}-\frac59\rho<0.
\tag{34}
\]
Such a signed estimate would have to hold for the actual weights in (4), or for a uniformly controlled decomposition of them. A root-mean-square estimate over shifts alone does not supply this cancellation. It cannot simply be inserted into (34).

Nor may one truncate away the upper half of \(\omega\), or replace \(\omega\) by a different low-frequency test, while claiming to have proved (6).

## 6. Primary-source audit: what is proved, what is not

### 6.1 Montgomery–Soundararajan and Chan

The unconditional input used in our proof is only Montgomery–Soundararajan's equation (16), on printed p.4. Their Theorem 3, printed p.5, instead assumes uniform prime-tuple errors \(O(N^{1/2+\eta})\). For the second moment it retains an error \(O(H^2N^{1/2+\eta})\), and is stated for \(H\le N^{1/2}\). This matches the threshold in (33); its hypothesis for prime pairs is not a consequence of RH.

Chan's version replaces that hypothesis by a conjectural mean-square condition over distinct shift tuples. His printed p.2 labels it **Conjecture 2** and derives the same conditional second-moment range and error scale. It is not an unconditional average-residue theorem. Neither paper supplies the signed saving in (34).

Sources: [Montgomery–Soundararajan, arXiv:math/0409258v1](https://arxiv.org/pdf/math/0409258v1), printed pp.4–5; [Chan, arXiv:math/0503441v2](https://arxiv.org/pdf/math/0503441v2), printed p.2. The version suffix matters: the unversioned Chan download returned v2. The retained source page images were visually checked.

### 6.2 Why the published 186 estimates do not establish (6)

The precise original source is [the published 186 manuscript](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), Definition 2.1/Lemma 2.2/Proposition 2.3, pp.3–5, and Corollary 2.19, p.11. Its complementary-divisor inequalities certify a class of triply densely divisible squarefree moduli. Corollary 2.19 bounds an absolute sum of one-prime progression discrepancies on that class by \(X(\log X)^{-B}\), uniformly in the allowed coherent residue choice and interval.

That result is already legally applicable to suitable divisor pieces at each fixed physical shift. It does not state a prime-pair asymptotic, a uniform \(E_X(z,h)\) estimate, or a bound for the signed \(h\)-aggregate in (29). Taking its absolute value separately at every shift still incurs \(H\); a logarithmic saving does not remove a power-size \(H\) in the variance normalization.

No restriction on a divisor's factorization makes a phase-twisted prime coefficient automatically Siegel–Walfisz. The independent Round 12 example rules out that claimed direct transfer. Conversely, that failure does not prohibit a different dispersion theorem retaining the phase, and it does not invalidate the actual per-shift use of Corollary 2.19.

There is also a real range change. The old compact Fourier test used \(\alpha\in[6/5,7/5]\), hence \(H\in[X^{1/6},X^{2/7}]\). Here
\[
H\in[X^{3/7},X^{5/9}].
\tag{35}
\]
The earlier RH \(X^{1.023}\log^5X\) bound was proved for a particular divisor-weighted discrepancy with its own support and tail qualifications; it is not a theorem about the complete \(a_ma_{m+h}\) in (28). Its proof is not silently imported into this new window.

For the canonical old level \(Q=X^{523/1000}\), even the ordering \(H<Q\) changes:
\[
H>Q
\quad\Longleftrightarrow\quad
\alpha>\frac{1000}{477}.
\tag{36}
\]
This suggests a possible complete-residue treatment of particular smooth divisor pieces in the upper wing, but proves no bound for (4). The positive-half-line Pareto shift weight has an endpoint at \(h=0\), and the full von Mangoldt divisor expansion has rough remaining factors. An arbitrary smooth-packet estimate cannot be declared an estimate of those remaining pieces.

The exact gap is therefore a quantitative bound on the actual centered weighted pair errors in (4), at least enough for (6). It is not merely the existence of densely divisible moduli or a larger scalar distribution exponent.

## 7. Scope, checks and next obligation

The ordinary results here are (12), the exact centered kernel (14), the uniform singular-series identity (17), the reduction (5), the Abel norm (29), and the unconditional obstruction (32a)–(32e). The numerical-looking power thresholds in (33)–(36) are exact rational calculations. The formal \(4/9\) pointwise threshold is impossible, not a feasible research obligation. Nothing proves that \(\mathcal E_T\) has the sign or upper constant in (6).

The original small checker and its output remain byte-for-byte unchanged: they verify the kernel factorization on exact rational finite signed data, the floor-centering convention, the beta moments at several integer \(T\), and the displayed exponent arithmetic, with inherited bump diagnostics for (7). Their recorded author hash refers to the preserved original manuscript, and they did not validate its mistaken feasibility assessment. A separate correction addendum checks the formal \(h=1\) expansion, exact singleton endpoint identities and Mellin residue. These bounded checks do not calculate primes at new heights or replace either ordinary proof. Source PDFs/text are retained locally with versioned URLs and hashes; only our report/checks/provenance should be published by the coordinator.

The next mathematical obligation is an upper bound for the **signed** quantity (4) along an unbounded sequence of \(T\), with threshold \(1-M\). A legal dispersion proof would have to specify its exact remaining coefficient factors, preserve the two singleton errors implicit in \(a_ma_{m+h}\), and control the physical shift packet in the new range (35). Establishing this bound would be a real strict arithmetic improvement. It remains open in this report.
