# Modulus-weight factorization: a level obstruction, a legal enlargement, and the exact normalization

Round 18, 2026-09-05. Author: Euclid. Status: ordinary lemmas and an exact arithmetic normalization audit, submitted for independent review. No improvement of the smooth shift aggregate or of a zeta target is claimed.

There are three distinct conclusions:

1. The actual terminal coefficients cannot be represented by triply well-factorable weights at levels at most \(Q(\log X)^B\), for any fixed \(B\). The obstruction uses real prime factors and holds regardless of the number or size of the summands.
2. At the enlarged level \(QY^2=X^{.525}\), the completed conductor sequence **does** have a representation with total scalar coefficient norm \(O(\log^{j+2}X)\). This is constructive; it is not a claim that no useful representation exists.
3. The completed sequence is not the modulus weight in the source's prime-progression functional. Exact inversion multiplies by a divisor \(r\) and recovers \(\mu(r)(\log r)^j\). The apparent \(1/q\) norm advantage cannot be transferred to that different functional for free.

The 186 theorem is a densely-divisible **modulus** theorem with an absolute discrepancy sum. It already applies per shift to the admitted moduli and requires no well-factorable weight decomposition. The separate weighted theorem tested here is Maynard's Theorem 1.1, whose residue is fixed and whose constants may depend on it. Neither theorem, as stated, supplies the needed cancellation over the growing smooth shift packet.

## 1. Fixed canonical coefficients and the actual aggregate

Let
\[
\rho=\frac{523}{1000},\quad \delta=\frac1{1000},\quad
Q=X^\rho,\quad Y=X^\delta,\quad
X^{1/6}\le H\le X^{2/7}.
\]
Use the full canonical family \(\mathcal Q_X\) from the frozen R11/R12 reports: each distinct squarefree \(q=[D,E]\) is counted once, with
\[
D,E\le X^{523/2000},\quad q>X^{1/2},
\]
\[
p^{3/2}D_{\ge p},\ p^{3/2}E_{\ge p}\le X^{501/2000}
\]
on their respective prime factors above \(Y\). Source Proposition 2.3 proves \(q\le Q\) and \(q\in\mathcal D^{(3)}(Y)\). No arbitrary-subset Möbius cancellation is assumed.

For \(j=0,1\), the exact original and completed coefficients are
\[
\lambda_j(q)=\mu(q)(\log q)^j1_{\mathcal Q_X}(q),\qquad
M_d^{(j)}=\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}
\frac{\mu(q)(\log q)^j}{q}.
\tag{1}
\]
At \(j=0\), the logarithmic factor means one. A separated genuine-prime component of the completed smooth discrepancy is
\[
\mathfrak B_j=
\sum_{d\le Q}M_d^{(j)}
\sum_{\substack{a\bmod d\\(a,d)=1}}
S_{V,H}(a/d)
\left[A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)\right],
\tag{2}
\]
\[
S_{V,H}(\beta)=\sum_hV(h/H)e(-\beta h),\qquad
A_f(\beta)=\sum_{p\ {\rm prime}}(\log p)f(p/X)e(\beta p).
\]
Here \(f\) is a fixed smooth supported profile at scale \(X\), with supported primes larger than \(Q\). The \(d=1\) bracket is zero. The actual sinc and log-cofactor weights are assembled by the frozen smooth-separation result, including both \(\log X\,\mathfrak B_0\) and \(\mathfrak B_1\). There is no change of mark in this note.

The prime-only formulation is the previously proved R10/R11 component. It is not a new assertion that the R15 full von Mangoldt or bilinear remainder has a modulus-independent primitive mask. The existing prime-power error in that reduction remains a separate, already bounded term on this original \(H\)-range.

## 2. Precisely which weight definition is being tested

We consider only levels \(R\ge1\). Maynard, arXiv:2006.07088v1, Definition 2, printed p.2, calls a sequence triply well-factorable of level \(R\) when, for every factorization
\[
R=R_1R_2R_3,\qquad R_i\ge1,
\]
it is a convolution of three sequences bounded by one, supported respectively in \([1,R_i]\). The real factor levels, and the quantifier over every allocation, matter.

In the same source Theorem 1.1 controls
\[
\sum_{(q,a)=1}\lambda(q)
\left[\pi(x;q,a)-\frac{\pi(x)}{\varphi(q)}\right]
\ll_{a,A,\eta}x(\log x)^{-A}
\tag{3}
\]
at levels \(R\le x^{3/5-\eta}\). The fixed-residue convention is explicit again on printed p.6. We use this as a precisely identified weighted theorem, not as a claim about the best currently available distribution exponent.

By contrast, the 186 paper's equation (2.5) and Corollary 2.19 bound an absolute sum over the admitted dense moduli for one coherent primitive class. Bounded complex modulus multipliers, including \(\mu(q)\), are already harmless in that absolute sum. Our level obstruction below does not invalidate that original per-shift application.

## 3. A necessary level from the least prime factor

**Lemma 1.** If \(n>1\), \(p=P^-(n)\), \(R\ge1\), and a triply well-factorable sequence \(\gamma\) of level \(R\) has \(\gamma(n)\ne0\), then
\[
\boxed{R\ge n p^2.}
\tag{4}
\]

**Proof.** If \(R<p^2\), choose \(R_1=R_2=\sqrt R\), \(R_3=1\). No nontrivial divisor of \(n\) can occur in any factor, so the coefficient is zero. Thus assume \(R\ge p^2\). For any real \(1\le s<p\), choose
\(R_1=R_2=s\), \(R_3=R/s^2\). In any nonzero convolution term with product \(n\), the first two factors must be one. The third is \(n\), requiring \(n\le R/s^2\). Let \(s\uparrow p\). This gives (4). The argument uses only support, not the size of the factor coefficients. ∎

The frozen R11 real-prime family \(\mathcal F_X\subset\mathcal Q_X\) consists of two distinct primes in
\((\lambda X^{9/100},X^{9/100}]\) and 346 distinct primes in
\((\lambda X^\kappa,X^\kappa]\), where
\[
\kappa=\frac{343}{346000},\qquad\lambda=2^{-1/348}.
\]
For all sufficiently large real \(X\), its proved properties are
\[
Q/2<q\le Q,\quad \mu(q)=1,\quad
P^-(q)>\lambda X^\kappa,\quad
|\mathcal F_X|\sim c_0Q/(\log X)^{348},
\tag{5}
\]
with an explicit \(c_0>0\). These are actual squarefree integers, not a generic spectral example. The complementary root guards and permutation counts were verified in R11; their exact exponent identities are retained in the adjacent checker.

Every triply well-factorable weight at any level below
\[
\frac{\lambda^2}{2}QX^{2\kappa}
\tag{6}
\]
vanishes on the entire family \(\mathcal F_X\). Since \(q>Q/2\) is terminal in the original modulus support,
\[
\lambda_0(q)=1,\qquad M_q^{(0)}=1/q,\qquad
M_q^{(1)}=(\log q)/q.
\tag{7}
\]
Consequently no sum of triply well-factorable sequences whose levels are all at most \(Q(\log X)^B\) can equal either actual sequence, for any fixed \(B\), once \(X\) is sufficiently large. The number of summands and their scalar coefficient norm do not matter: every summand is zero at each witness.

Primitive shift masks do not make this support example disappear. Choose a fixed interval inside the nonzero support of \(V\). For large \(X\), it contains a prime \(h\asymp H\), by the prime number theorem. Such an \(h\) exceeds every prime factor of \(q\in\mathcal F_X\), since \(H\ge X^{1/6}\) and these factors are at most \(X^{.09}\). Thus \((h,q)=1\) for all witnesses, at a genuine active shift.

For the nonnegative, nonzero \(V\) used in the R11 coefficient-norm argument, the obstruction also survives approximation in that completed norm. Any proposed \(M_d^{(j)}\) approximation by such same-level weights has error satisfying
\[
\sum_{\substack{d\le Q\\(a,d)=1}}
|S_{V,H}(a/d)(M_d^{(0)}-\widetilde M_d^{(0)})|^2
\gg_V H/(\log X)^{348},
\tag{8}
\]
and the logarithmic version has lower bound \(H/(\log X)^{346}\). Here \(a\) ranges over the reduced residue system. Indeed \(\widetilde M_q=0\) on \(\mathcal F_X\); for \(1\le a\le q/(16H)\), the phases have real part bounded below, so \(|S_{V,H}(a/q)|\gg_VH\). A proportion \(1-o(1)\) of these numerators are primitive because \(\sum_{p\mid q}1/p=o(1)\). Summing their squared coefficients and (5) gives (8).

This is the particular completed coefficient-norm obstruction. It does not prevent cancellation in the joint pairing with \(A_f\).

## 4. A constructive enlarged level, including all conductors

**Lemma 2.** If \(q\le Q\) is triply \(Y\)-densely divisible, then its point mass \(\delta_q\) is triply well-factorable at level
\[
\boxed{R=QY^2.}
\tag{9}
\]
For squarefree \(q\), the same is true for \(\delta_d\) for every \(d\mid q\).

**Proof.** Fix an arbitrary \(R_1R_2R_3=QY^2\), with all levels at least one. If \(R_1\ge q\), use \(q_1=q,q_2=q_3=1\). Otherwise apply the strong dense-divisibility definition at target \(R_1\), allocating order two to the complementary factor and order zero to the chosen divisor. It produces
\[
q=q_1u,\quad R_1/Y\le q_1\le R_1,\quad
u\in\mathcal D^{(2)}(Y).
\]
The target is allowed since \(R_1<q\le Yq\).
If \(R_2\ge u\), take \(q_2=u,q_3=1\). Otherwise apply the definition to \(u\) at target \(R_2\), choosing
\[
u=q_2q_3,\qquad R_2/Y\le q_2\le R_2.
\]
Then
\[
q_3\le\frac{qY^2}{R_1R_2}\le R_3.
\]
In every case \(q_i\le R_i\), and the three unit point masses at \(q_i\) convolve to \(\delta_q\). For \(d\mid q\), set \(d_i=(d,q_i)\). Squarefreeness gives \(\prod d_i=d\), and \(d_i\le R_i\), so the same allocation proves the claim for \(\delta_d\). ∎

This does not assert that arbitrary divisors retain the same dense-divisibility parameter \(Y\). It transfers an already constructed factor allocation, avoiding that invalid inference.

Our sufficient level is \(X^{21/40}=X^{.525}\). The terminal-family necessary exponent is
\[
\rho+2\kappa=\frac{45411}{86500}=.5249826589\ldots,
\]
so these two support thresholds differ by only
\[
2(\delta-\kappa)=\frac3{173000}.
\tag{10}
\]
The comparison concerns this family and support question; it is not a theorem that these are optimal levels for every original coefficient sequence. Both exponents are below the level allowed by the named fixed-residue weighted theorem, so the same-level obstruction is not a blanket inapplicability result at enlarged levels.

## 5. A genuinely controlled decomposition of the completed sequence

Lemma 2 provides the exact finite representation
\[
M^{(j)}=\sum_{d\le Q} M_d^{(j)}\delta_d
\tag{11}
\]
in triply well-factorable weights of common level \(QY^2\). Its total scalar coefficient norm is bounded by
\[
\boxed{
\sum_d|M_d^{(j)}|
\le(\log Q)^j\sum_{q\in\mathcal Q_X}\frac{\tau(q)}q
\le(\log Q)^j(1+\log Q)^2.
}
\tag{12}
\]
The last step follows by writing \(\tau(q)=\sum_{ab=q}1\) and bounding the resulting sum by the square of the harmonic sum.

Thus merely counting nonzero conductors would give the wrong answer about the norm of (11). The completed \(1/q\) coefficient has a polylogarithmic decomposition norm. The positive result (12) is part of the conclusion, not an unresolved possibility.

In contrast, the displayed point-mass representation of the **original** sequence
\(\lambda_j=\sum_q\lambda_j(q)\delta_q\) costs
\[
\sum_q|\lambda_j(q)|\ge
\sum_{q\in\mathcal F_X}(\log q)^j
\gg Q(\log X)^{j-348}.
\tag{13}
\]
This is the cost of this specific representation in the linear-combination norm used to apply (3). It is not a lower bound for every possible compressed representation at level \(QY^2\). Existence of a cheaper such representation for the original signed family is left open.

## 6. Exact inversion restores the original AP normalization

For a genuine-prime profile define
\[
\Delta_r(h)=
\sum_{p\equiv h\ (r)}(\log p)f(p/X)
-\frac{1_{(h,r)=1}}{\varphi(r)}A_f(0).
\tag{14}
\]
All supported primes exceed \(Q\), so are units modulo every \(r\le Q\). For nonprimitive \(h\), both terms are zero. The indicator in the principal term is essential.

Let \(c_d(k)\) be the Ramanujan sum. For every squarefree \(d\),
\[
\begin{split}
&\sum_{\substack{a\bmod d\\(a,d)=1}}
S_{V,H}(a/d)
\left[A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)\right]\\
&\qquad=\sum_hV(h/H)\sum_{r\mid d}r\mu(d/r)\Delta_r(h).
\end{split}
\tag{15}
\]

To verify all signs and primitive terms, sum the exponentials first:
the prime term is \(c_d(p-h)\), and the principal term is
\(\mu(d)c_d(h)A_f(0)/\varphi(d)\).
Use
\[
c_d(k)=\sum_{\substack{r\mid d\\r\mid k}}r\mu(d/r)
\]
and the multiplicative identity
\[
\sum_{r\mid d}\frac{r\mu(d/r)}{\varphi(r)}1_{(h,r)=1}
=\frac{\mu(d)c_d(h)}{\varphi(d)}.
\tag{16}
\]
At a prime divisor \(p\), the latter identity is
\(-1+p1_{p\nmid h}/(p-1)=-(c_p(h))/(p-1)\); its two cases verify it exactly.

Now insert the completed coefficients. The divisor coefficient in front of \(\Delta_r(h)\) is exactly
\[
\begin{split}
\sum_{\substack{d\le Q\\r\mid d}}r\mu(d/r)M_d^{(j)}
&=\sum_{\substack{q\in\mathcal Q_X\\r\mid q}}
\frac{\mu(q)(\log q)^j}{q}\,
r\sum_{\substack{d:r\mid d\mid q}}\mu(d/r)\\
&=\boxed{\mu(r)(\log r)^j1_{\mathcal Q_X}(r).}
\end{split}
\tag{17}
\]
The inner Möbius sum is zero unless \(q=r\). Therefore the actual functional is
\[
\boxed{\mathfrak B_j=\sum_hV(h/H)\sum_r\lambda_j(r)\Delta_r(h).}
\tag{18}
\]

This is an exact equality, with no estimates or dropped means. Applying (3) to (11) as if \(\mathfrak B_j\) were simply \(\sum_d M_d^{(j)}\Delta_d(h)\) would omit the divisor multiplier \(r\), the divisor expansion, and the reduced-numerator sum. Equation (17) identifies the error precisely.

On a terminal \(d\in\mathcal F_X\), even the absolute conversion of its single \(1/d\) coefficient costs
\[
\frac1d\sum_{r\mid d}r=\frac{\sigma_1(d)}d=1+o(1),
\]
rather than \(1/d\). This is an illustrative exact normalization fact, not a lower bound for cancellation among all conductors. The full inversion (17), rather than a triangle estimate, is what restores the signed original coefficient.

## 7. The smooth shift aggregate remains the actual missing estimate

At the source parameters, the 186 absolute dense-modulus estimate already handles each fixed coherent primitive shift with uniform constants. That use survives every lemma above. Summing those guaranteed bounds against a packet of length \(H\) still carries its previously identified \(H\) loss.

The separate Maynard theorem (3) has a fixed residue and constants allowed to depend on that residue. It cannot be substituted uniformly for the growing \(h\asymp H\) without a further theorem. Even if a uniform version with the same per-shift logarithmic saving were granted, a triangle sum in \(h\) would still not produce the required aggregate cancellation. A small scalar decomposition norm for a different functional does not address this.

Under RH, the current proved aggregate remains \(O(X^{1023/1000}\log^5X)\). No theorem used here bounds its joint smooth shift sum at \(o(X\log X)\) or removes the \(X^{23/1000}\) power loss. No phase-twisted Siegel–Walfisz property is assumed.

The bounded advance is an exact answer to two representation questions, and a proof of where their operator normalizations differ. A compressed enlarged-level representation of the original \(\lambda_j\), together with a theorem controlling its actual shift-averaged functional, remains a possible route. Neither is supplied by the source statements audited here. Pruning the terminal family or changing the arithmetic mark would require a new exact zeta/covariance transfer and cannot be justified by the coefficient facts alone.

## 8. Primary sources and reproducibility

- [OpenAI, Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf): Definition 2.1 and Proposition 2.3, printed pp.4–5; equation (2.5), p.7; Corollary 2.19, p.11. This is a dense-modulus absolute-sum input, not the distinct weight theorem.
- [James Maynard, Primes in arithmetic progressions to large moduli II: Well-factorable estimates](https://arxiv.org/pdf/2006.07088v1): Definition 2 and Theorem 1.1, printed p.2; fixed-residue convention, p.6. The specific version is pinned; no claim of a newest exponent is made.
- Frozen R11 conductor construction and R12/R15 exact objects are pinned in source_manifest.json.

The adjacent exact checker verifies exponent gaps, the support obstruction on actual small integers, the coefficient inversion, and the primitive Ramanujan identities over multiple squarefree families. Its finite examples test the universal algebra, not a finite realization of the asymptotic 348-prime construction. Primary PDFs remain local. No earlier report, canonical repository, or external session was changed.
