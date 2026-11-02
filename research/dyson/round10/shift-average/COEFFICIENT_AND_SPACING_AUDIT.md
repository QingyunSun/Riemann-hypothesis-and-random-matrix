# Independent audit of the completed-shift coefficients and spacing bound

Date: 2026-09-05. Reviewer: `yau_flow`. This note checks the exact reduced-fraction identity, its coprime principal term, and a fully quantified bound for separable genuine-prime packets. The authoring agent and another reviewer are separately checking the actual two-variable weight and prime-power exceptions. No numerical scan or large computation is used here.

**Final verdict on the assigned analytical core:** the coefficient and spacing argument is valid. Its logarithmic losses fit the proposed fourth power. The resulting estimate improves the accumulated error for the selected divisor component but does not reach the covariance scale. The distinction between this separable lemma and a verified application to the full weight must be retained. The pinned author draft and precise review scope are recorded in Section 7.

## 1. Precisely quantified separable statement

Let \(X\geq4\), \(H\geq1\), and \(2\leq Q<X\). Let \(\mathcal Q\) be any set of distinct squarefree integers in \([1,Q]\). No dense-divisibility assumption is needed for this lemma. Let \(f\) be a bounded complex function on \([1,2]\), and let \(v\) be a complex function of bounded variation on \(\mathbb R\), supported in a fixed interval \([-C,C]\). Put
\[
M(v)=\|v\|_\infty+\operatorname{TV}(v),\qquad
B_p=(\log p)f(p/X)\mathbf1_{X<p\leq2X}.
\]
For \(j\in\{0,1\}\), define
\[
\begin{split}
D_j={}&\sum_{h\in\mathbb Z}v(h/H)
\sum_{\substack{q\in\mathcal Q\\(q,h)=1}}
\mu(q)(\log q)^j\\
&\quad\times\left\{
\sum_{\substack{X<p\leq2X\\p\equiv h\pmod q}}B_p
-\frac1{\varphi(q)}\sum_{X<p\leq2X}B_p
\right\}.
\end{split}
\tag{1}
\]
In (1), \((\log q)^0=1\), including \(q=1\). The braces for \(q=1\) vanish identically. Since every prime in the sum exceeds \(Q\), each is coprime to every modulus. This is the reason the principal sum in (1) is unrestricted; for a von Mangoldt sum this replacement would require a separate prime-power argument.

There is a constant depending only on \(C\) such that
\[
|D_j|\ll_C
\|f\|_\infty M(v)
\sqrt{HX(X+Q^2)}\,\log^{j+5/2}(2X).
\tag{2}
\]
The exponent \(j+5/2\) need not be rounded up. In particular the common \(O(\log^4(2X))\) upper bound is valid for \(j=1\), and also after multiplying \(D_0\) by a factor of size \(O(\log X)\). These are the two cases needed to separate \(\log((m-h)/q)\).

All constants in (2) are independent of the chosen family \(\mathcal Q\), its cardinality, \(X,H,Q\), and the values of \(f,v\), apart from the displayed norms. The statement is about the actual primes and progression discrepancy, not a formal spectral model.

## 2. Exact reduction, including the principal term

Use \(e(z)=e^{2\pi iz}\) and
\[
S_v(\alpha)=\sum_{h\in\mathbb Z}v(h/H)e(-\alpha h).
\]
For a prime \(p>Q\), its congruence \(p\equiv h\pmod q\) forces \((h,q)=1\). Thus the coprimality restriction can be dropped in the first term of (1), but it must be retained in the principal term. Finite Fourier inversion gives
\[
\sum_hv(h/H)\mathbf1_{p\equiv h\pmod q}
=\frac1q\sum_{r=0}^{q-1}S_v(r/q)e(rp/q),
\]
and
\[
\sum_{(h,q)=1}v(h/H)
=\frac1q\sum_{r=0}^{q-1}S_v(r/q)c_q(r),
\]
where \(c_q(r)=\sum_{a\bmod q,(a,q)=1}e(ra/q)\) is the Ramanujan sum. At a reduced fraction \(r/q=a/d\), with \((a,d)=1\),
\[
\frac{c_q(r)}{\varphi(q)}=\frac{\mu(d)}{\varphi(d)}.
\tag{3}
\]
For squarefree \(q\), (3) follows directly by multiplying the local factors: a prime dividing \(d\) contributes \(-1/(p-1)\), and a prime dividing \(q/d\) contributes one.

Define
\[
A_{d,j}=\sum_{\substack{q\in\mathcal Q\\d\mid q}}
\frac{\mu(q)(\log q)^j}{q},
\qquad
E(a/d)=\sum_{X<p\leq2X}B_p
\left(e(ap/d)-\frac{\mu(d)}{\varphi(d)}\right).
\]
Then the exact identity is
\[
D_j=\sum_{2\leq d\leq Q}\ \sum_{\substack{1\leq a<d\\(a,d)=1}}
A_{d,j}S_v(a/d)E(a/d).
\tag{4}
\]
There is one term for each reduced fraction, not one independent frequency for each original modulus. The \(d=1\) term is zero because its centered character is \(1-1\). The coefficient is a sum with denominator \(q\); replacing it by \(1/d\) before summing the multiples would lose the logarithmic norm control. No cancellation of the Möbius coefficients is used below.

## 3. Squared coefficient norm

Summing by parts in the finite shift sequence gives
\[
|S_v(\alpha)|\ll_C M(v)\min\{H,\|\alpha\|^{-1}\},
\tag{5}
\]
with the first alternative used at integral \(\alpha\). The discrete variation is at most the total variation of the zero-extended function \(v\). This proof includes indicator cutoffs with a specified endpoint convention; it does not require smoothness.

For \(d\leq H\), bound the complete nonzero residue sum by
\[
\sum_{a=1}^{d-1}|S_v(a/d)|^2
\ll_C M(v)^2d^2.
\]
For \(d>H\), split the distance of \(a\) from the nearest multiple of \(d\) at \(d/H\). Equation (5) gives
\[
\sum_{a=1}^{d-1}|S_v(a/d)|^2
\ll_C M(v)^2Hd.
\tag{6}
\]
The reduced-residue sum is smaller. Independently,
\[
|A_{d,j}|\leq
\frac{\log^j(2Q)}d\left(1+\log\frac Qd\right)
\ll\frac{\log^{j+1}(2Q)}d.
\tag{7}
\]
Hence
\[
\begin{split}
\sum_{d,a}^{*}|A_{d,j}S_v(a/d)|^2
&\ll_C M(v)^2\log^{2j+2}(2Q)
\left(\sum_{d\leq\min(H,Q)}1
+H\sum_{H<d\leq Q}\frac1d\right)\\
&\ll_C M(v)^2H\log^{2j+3}(2Q).
\end{split}
\tag{8}
\]
Thus the claimed \(H\log^3Q\) and \(H\log^5Q\) squared norms are valid for \(j=0,1\), respectively. In particular, the coefficient argument itself does not distinguish a smooth shift cutoff from a sharp finite interval. Whether the full nonseparable weight admits a controlled decomposition is a different question.

## 4. Well-spaced frequencies and centered prime sums

Distinct reduced fractions of denominator at most \(Q\) have circular separation at least \(Q^{-2}\). For any integer interval of length \(O(X)\), its exponential kernel satisfies
\[
\left|\sum_m e((\alpha-\beta)m)\right|
\ll\min\{X,\|\alpha-\beta\|^{-1}\}.
\]
For a fixed frequency, the number of others within circular distance \(r\) is \(O(1+rQ^2)\). Ordering the distances and summing the harmonic series therefore bounds every absolute Gram row sum by
\[
O\bigl(X+Q^2\log(2Q)\bigr).
\]
The elementary Schur bound and finite-dimensional duality imply
\[
\sum_{d,a}^{*}\left|\sum_m b_me(am/d)\right|^2
\ll\bigl(X+Q^2\log(2Q)\bigr)\sum_m|b_m|^2.
\tag{9}
\]
This proof retains the logarithm in the elementary spacing estimate. It does not silently invoke the sharper large-sieve constant \(X+Q^2\).

For \(b_p=B_p\) and zero coefficients on other integers, Chebyshev's elementary bound \(\sum_{p\leq2X}\log p\ll X\) gives
\[
\sum_p|B_p|^2\ll\|f\|_\infty^2X\log(2X),
\qquad
\left|\sum_pB_p\right|\ll\|f\|_\infty X.
\tag{10}
\]
Using primes in (10) saves one logarithm compared with the cruder bound obtained by assigning a \(\log X\) coefficient to every integer.

The constant terms in \(E(a/d)\) have squared norm
\[
\left|\sum_pB_p\right|^2
\sum_{d\leq Q}\frac{\mu(d)^2}{\varphi(d)}
\ll\|f\|_\infty^2X^2\log(2Q).
\tag{11}
\]
For completeness, \(\sum_{d\leq Q}1/\varphi(d)\ll\log(2Q)\) follows from
\(n/\varphi(n)=\sum_{a\mid n}\mu(a)^2/\varphi(a)\): after interchanging the two positive sums the remaining series is bounded by
\(\sum_a\mu(a)^2/(a\varphi(a))=\prod_p(1+1/(p(p-1)))<\infty\).

Combining (9)–(11), with \(|u-v|^2\leq2|u|^2+2|v|^2\), proves
\[
\sum_{d,a}^{*}|E(a/d)|^2
\ll\|f\|_\infty^2X(X+Q^2)\log^2(2X).
\tag{12}
\]
The primitive principal term is therefore affordable without assuming cancellation of the prime exponential sums. Cauchy–Schwarz in (4), using (8) and (12), proves (2).

## 5. What an application to the actual weight must verify

The separable proof applies to a sum of blocks if the full weight has an absolutely summable representation
\[
W(m/X,h/H)=\sum_\ell\gamma_\ell f_\ell(m/X)v_\ell(h/H),
\qquad
\sum_\ell|\gamma_\ell|\|f_\ell\|_\infty M(v_\ell)\leq K,
\tag{13}
\]
uniformly in \(X,H,T\). The bound is then multiplied by \(K\). If the logarithmic cofactor is present, write
\[
\log((m-h)/q)=\log X-\log q+\log(m/X-(H/X)(h/H)).
\]
The first two terms use \(j=0\) and \(j=1\); the third must be included in the smooth two-variable factor whose separation is justified. Independent choices of arbitrary \(w_h\) satisfying only a separate bounded-variation norm in \(m\) do not automatically give (13).

Likewise, replacing \(\Lambda(m)\) by genuine-prime coefficients must retain both the original nonprimitive congruence exceptions and the coprime principal-term deletions. Their errors are not part of the identity (4). The author and the other independent reviewer own these full-weight checks.

For a sharp shift interval, (5)–(8) are still available. A Fourier expansion of just the smooth kernel, leaving the interval indicator in each \(v_\ell\), is a possible rigorous use of (13): its bounded-variation cost grows polynomially with the Fourier frequency and can be absorbed by sufficiently rapid coefficient decay. This observation alone is not a completed verification of the original sharp packet's support and endpoint conventions.

## 6. Size and limitations

At \(Q=X^{523/1000}\), the proposed upper bound is
\[
O\bigl(X^{1.023}\sqrt H\log^4X\bigr).
\]
For \(X^{1/6}\leq H\leq X^{2/7}\), its ratio to \(HX\) is
\(O(X^{.023}H^{-1/2}\log^4X)\), which tends to zero by a power of \(X\). This is a real improvement over accumulating independent per-shift bounds.

However, its ratio to the required \(X\log X\) scale is
\(O(X^{.023}\sqrt H\log^3X)\), which grows throughout the stated interval. No bound in this note evaluates the selected divisor component to the required covariance precision, controls the complementary divisor remainder, or settles a zeta pair-correlation conjecture.

## 7. Final author artifact and delta-review scope

The final reviewed author artifact is **SMOOTH_SHIFT_COMPLETION_BOUND.md**, SHA-256

`7b52e4d82dc40bf90183331d548b7fffe5545d1928d7cb93223223b5b71c1d78`.

Its Sections 3–5 were read and checked against the independent derivation above. The exact Fourier signs, coprime principal term, zero-frequency cancellation, reduced-denominator grouping, smooth-shift estimate with two finite differences, the two coefficient norms, the logarithm in the Schur row bound, and the centered prime norm are all accepted. The power exponents and the comparison with the covariance scale in its introduction and Section 7 agree with exact rational arithmetic. Its final clarification that the completion bound itself is unconditional is also accepted: none of these arguments uses RH.

The actual two-variable amplitude in author Section 6 is consistent with the uniform separation criterion (13). Its complete support/separation and prime-power-exception review is assigned to the separate `residual_gram` reviewer; the present note does not replace that independent check. In particular, this audit does not enlarge the author theorem from its fixed smooth shift packet to the entire sharp packet. The bounded-variation observation in Section 5 remains a precisely stated extension criterion.

The companion author's exact-check JSON was inspected for its scope and report provenance, but its script was not independently rerun here. No assertion in this audit depends on those finite checks. The written estimates prove the assigned analytical core; they are not a machine-checked formal proof, a new distribution theorem at the required covariance scale, or a solution of AH or Montgomery's conjecture.
