# Short-residue averaging: the exact norm budget and missing dispersion estimate

Round 19, 2026-09-05. Author: Euclid. Status: ordinary lemmas and a bounded primary-source application audit, submitted for independent review. No improvement of the full zeta covariance is claimed.

On actual squarefree moduli admitted by the 186 construction, the primitive-centered packet of \(H\) shifts has squared residue norm asymptotic to \(H\int|V|^2\), not \(H^2/q\). Complete-residue variance therefore supplies no free \(H/q\) saving. A specific additional localized variance estimate would close the separated component for \(X^{1/6}\le H\le X^{477/2000-\eta}\). That estimate is not proved here or supplied by the audited theorems.

The current programme bound remains \(O(X^{1.023}\log^5X)\) **under RH**. The finite norm/algebra lemmas below are unconditional.

## 1. Actual coefficients and exact primitive centering

Set
\[
\rho=\frac{523}{1000},\quad Q=X^\rho,\qquad X^{1/6}\le H\le X^{2/7}.
\]
Use the canonical family \(\mathcal Q_X\) from R11/R18, counting each distinct squarefree \(q=[D,E]\) once:
\[
D,E\le X^{523/2000},\quad q>X^{1/2},\quad
p^{3/2}D_{\ge p},\ p^{3/2}E_{\ge p}\le X^{501/2000}
\]
on the respective prime factors \(p>X^{1/1000}\). Source Proposition 2.3 proves the required triple dense divisibility. First consider the terminal portion
\(\mathcal T_X=\mathcal Q_X\cap(Q/2,Q]\).

Fix \(f,V\in C_c^\infty((1,2))\), with \(V\not\equiv0\). They may be complex unless otherwise stated. Define
\[
A_f=\sum_p(\log p)f(p/X),\qquad
\Delta_q(a)=\sum_{p\equiv a\ (q)}(\log p)f(p/X)-\frac{A_f}{\varphi(q)}
\quad ((a,q)=1).
\tag{1}
\]
Every supported prime exceeds \(Q\), so
\[
\sum_{a\bmod q}^{*}\Delta_q(a)=0
\tag{2}
\]
exactly. For \(j=0,1\), the terminal component is
\[
\mathcal D_j=\sum_{q\in\mathcal T_X}\mu(q)(\log q)^j
\sum_{(h,q)=1}V(h/H)\Delta_q(h).
\tag{3}
\]
There is **no \(1/q\) modulus coefficient** in (3): the exact R18 Ramanujan inversion restores \(\mu(q)(\log q)^j\). Its principal term is never discarded.

The full sinc/log-cofactor packet consists of separated components and nonterminal moduli, as established in R10. A sufficient estimate for the whole discrepancy must be uniform in the needed smooth seminorms, include the nonterminal portion, and retain the previously bounded prime-power remainders. Controlling (3) alone does not prove the full zeta inequality.

## 2. Exact short-residue norm, including the removed constant mode

For \(q>2H\), let \(v_q(a)=V(h/H)\) if the primitive residue \(a\) has a representative \(H<h<2H\), and zero otherwise. There is at most one such representative. Put
\[
\bar v_q=\frac1{\varphi(q)}\sum_a^*v_q(a),\qquad v_q^\circ=v_q-\bar v_q.
\]
Equation (2) allows replacement by \(v_q^\circ\) in (3).

**Lemma 1.** The exact norm is
\[
\|v_q^\circ\|_2^2=
\sum_{(h,q)=1}|V(h/H)|^2-
\frac{|\sum_{(h,q)=1}V(h/H)|^2}{\varphi(q)}.
\tag{4}
\]
On arrays \(E_q(a)\) with \(\sum_a^*E_q(a)=0\), the norm of the functional
\[
E\longmapsto\sum_q\mu(q)(\log q)^j\sum_a^*v_q(a)E_q(a)
\]
is exactly
\[
\mathcal N_j^{1/2},\qquad
\mathcal N_j=\sum_{q\in\mathcal T_X}(\log q)^{2j}\|v_q^\circ\|_2^2.
\tag{5}
\]

**Proof.** Expand \(\|v_q-\bar v_q\|^2\). Orthogonal projection and Cauchy–Schwarz give (5); equality holds for a common scalar multiple of
\(\overline{\mu(q)(\log q)^jv_q^\circ(a)}\).
These extremal arrays are not asserted to be prime discrepancies. ∎

The inherited real-prime subfamily \(\mathcal F_X\subset\mathcal T_X\) consists of two primes in \((\lambda X^{9/100},X^{9/100}]\) and 346 primes in \((\lambda X^\kappa,X^\kappa]\), all distinct, with
\[
\kappa=\frac{343}{346000},\qquad\lambda=2^{-1/348}.
\]
Its proved R11 properties, for all sufficiently large real \(X\), are
\[
|\mathcal F_X|\sim c_0 Q/(\log X)^{348},\quad
\mu(q)=1,\quad P^-(q)>\lambda X^\kappa,\quad\omega(q)=348,
\tag{6}
\]
where \(c_0>0\) is explicit there. These are actual integers satisfying the source guards.

**Lemma 2.** Uniformly for this family and our \(H\)-range,
\[
\|v_q^\circ\|_2^2=H\int|V(u)|^2\,du+o_V(H).
\tag{7}
\]
In particular, for positive constants and all sufficiently large \(X\),
\[
c_V H Q(\log X)^{2j-348}
\le\mathcal N_j\le C_V H Q(\log X)^{2j}.
\tag{8}
\]

**Proof.** Riemann summation gives the unmasked sum \(H\int|V|^2+O_V(1)\). The number of omitted nonunits is at most
\[
\sum_{p\mid q}(H/p+2)\ll H X^{-\kappa}+696=o(H).
\]
Also \(\varphi(q)/q=1+o(1)\) uniformly. The subtracted term in (4) is \(O_V(H^2/q)=o(H)\). Sum over (6), using \(\log q=\rho\log X+O(1)\). The upper bound uses at most \(Q\) moduli and \(O_V(H)\) squared norm per modulus. ∎

This rules out a coefficient-norm power improvement in this complete-residue Hilbert space from complementary support alone. It does not rule out cancellation in the joint arithmetic pairing.

## 3. The variance comparison and a genuinely useful conditional window

Write
\[
\mathcal V_{\rm all}=\sum_{q\in\mathcal T_X}\sum_a^*|\Delta_q(a)|^2,\qquad
\mathcal V_{\rm loc}=\sum_{q\in\mathcal T_X}
\sum_{\substack{H<h<2H\\(h,q)=1}}|\Delta_q(h)|^2.
\]
The two different Cauchy estimates are
\[
|\mathcal D_j|\le\sqrt{\mathcal N_j\mathcal V_{\rm all}},
\tag{9}
\]
\[
|\mathcal D_j|\ll_V(\log X)^j\sqrt{HQ\mathcal V_{\rm loc}}.
\tag{10}
\]
Positivity does not imply
\(\mathcal V_{\rm loc}\le(H/Q)\mathcal V_{\rm all}\). A zero-sum residue array can concentrate on the packet; Lemma 1 gives the sharp test with the actual modulus support and exact primitive centering.

Even **hypothetically** granting
\(\mathcal V_{\rm all}\ll XQ(\log X)^C\) here, (9) gives only
\[
|\mathcal D_j|\ll Q\sqrt{HX}(\log X)^{j+C/2}
=X^{1023/1000+\theta/2}(\log X)^{j+C/2},\quad H=X^\theta.
\tag{11}
\]
Its power exponent runs from \(3319/3000=1.10633\ldots\) to
\(8161/7000=1.16585\ldots\), worse than R11. The hypothetical premise is not attributed to ordinary RH or to unconditional BDH.

The inspected Montgomery–Vaughan author text, Theorem 20.12, equation (20.38), printed pp.214–215, proves its \(xQ\log x\) bound for
\(x/(\log x)^A\le Q\le x\), fixed \(A\). Our \(Q=X^{.523}\) is outside that range. Enlarging the modulus range gives only
\[
\mathcal V_{\rm all}\ll_{A,f}X^2/(\log X)^A
\tag{12}
\]
for every fixed \(A\), which cannot compensate for the power of \(H\).

Here is the precise transfer to (1). Primitive orthogonal projection is a contraction. Smooth partial summation uses only prefix endpoints in \([X,2X]\), where the enlarged-modulus application is uniform. Removing prime powers costs at most
\[
O_f\!\left(Q\left(\sum_{\substack{p^k\le2X\\k\ge2}}\log p\right)^2\right)
\ll_f XQ(\log X)^4,
\]
smaller than the right side of (12) for fixed \(A\). Constants may depend on smooth seminorms. No GRH refinement is used.

**Conditional usable window.** A new localized arithmetic estimate
\[
\boxed{\mathcal V_{\rm loc}\ll_f HX(\log X)^C}
\tag{13}
\]
would imply
\[
|\mathcal D_j|\ll_{f,V}
H\sqrt{XQ}(\log X)^{j+C/2}
=X^{\theta+1523/2000}(\log X)^{j+C/2}.
\tag{14}
\]
Therefore it gives \(o(X\log X)\) with a power margin when
\[
\theta\le477/2000-\eta,\qquad \eta>0.
\tag{15}
\]
For \(H=X/T,\ X=T^\alpha\), this is the nonempty old compact-kernel window
\[
6/5\le\alpha<2000/1523=1.313197\ldots
\]
with a fixed gap below the upper endpoint. To close the original full arithmetic component, (13) must hold uniformly for the full required modulus family and separated smooth profiles. It is not established here.

The R16 Bragg test near \(\alpha=2\) has a different \(H\)-scale and additional normalization issues. Neither this conditional window nor a single controlled divisor component transfers to that Bragg target.

## 4. Primary variable-residue theorems and one legal but insufficient allocation

We inspect Maynard, arXiv:2006.08250v1, without claiming an exhaustive latest-theorem survey.

* Theorem 1.1, printed p.3: two-factor maximal-residue estimate with weak error \(O(\delta\pi(x)+x(\log\log x)^2/\log^2x)\), factor bounds \(Q_1\le x^{.1-3\delta}/\log^C x\), \(Q_2\le x^{.4+4\delta}\log^C x\).
* Theorem 1.2, printed p.3: strong logarithmic error and partly compatible variable residues, but explicitly \(0<\delta<1/1000\). Our \(23/1000\) excess fails this hypothesis before factor allocation.
* Theorem 1.3, printed p.4: a prime minorant. The centered signed functional (3) is not monotone under that substitution.

The weak theorem actually permits a concrete allocation on \(\mathcal F_X\). Take \(\delta_*=3/125=.024\), put 28 small primes into \(q_1\) by deterministic ordering, and the rest into \(q_2\). Then
\[
s_1=28\kappa=.027757225\ldots<.028=.1-3\delta_*,
\]
\[
s_2=\rho-s_1=.495242774\ldots<.496=.4+4\delta_*.
\tag{16}
\]
The strict power margins absorb logarithms. Each factor is between a fixed positive multiple of its power scale and that scale, so boundedly many dyadic boxes suffice. The map \(q\mapsto(q_1,q_2)\) is injective; dropping its image restriction is legal in the source's nonnegative absolute sum.

Partial summation to \(\log p\,f(p/X)\) gives only
\(O_f(\delta_*X+X(\log\log X)^2/\log X)\) for that summed maximal-residue norm. Pairing the \(H\)-packet by this norm gives \(O_{f,V}(\delta_*HX+\cdots)\), before inserting the factor \((\log q)^j\); the full \(\mathcal D_j\) has an additional \(O((\log X)^j)\) factor. This is not the target scale. The source warns that its unspecified constant can make a particular positive \(\delta\) uninformative.

That \(H\) cost is exact at the maximal-residue norm level. For \(V\ge0\), take a zero-sum array equal to one on active primitive residues and minus the active-count divided by the inactive-count elsewhere. Its sup norm is one for large \(X\), while the packet pairing is \((1+o(1))H\int V\) on the terminal family. These remain test arrays, not prime errors.

The 186 paper's equation (2.5) and Corollary 2.19 already give a legal stronger per-shift estimate on their admitted family. Nothing here invalidates it. The missing step is a genuinely localized or signed shift estimate, not permission to use the moduli for a single coherent residue.

## 5. Physical shifts inside the Maynard factorization mechanism

Maynard II, arXiv:2006.07088v1, printed pp.4–5, factors \(r_1=s_1t_1\) before an outer Cauchy–Schwarz step: its diagonal cost grows by \(S\), while the automorphic level drops from \(R^2\) to \(T^2\), \(ST\asymp R\). Its letter \(h\) is a Fourier-dual variable. It is not our physical shift.

For a unit \(n\), write
\[
K_\ell(m;n,h)=1_{mn\equiv h\pmod\ell}
-\frac{1_{(mn,\ell)=1}1_{(h,\ell)=1}}{\varphi(\ell)}.
\]
The squared packet has independent physical shifts \(h_1,h_2\). For
\(\ell_i=qr_i\), with \((q,r_1r_2)=(r_1,r_2)=1\), and \(n_i,h_i\) primitive for \(\ell_i\), the two progression indicators have a simultaneous solution in \(m\) exactly when
\[
\boxed{h_1n_2\equiv h_2n_1\pmod q.}
\tag{17}
\]
Indeed the two residues are \(h_i\overline n_i\); their equality modulo \(q\) is precisely (17). The principal cross terms are
\[
K_1K_2=I_1I_2-I_1U_2/\varphi(\ell_2)
-U_1I_2/\varphi(\ell_1)+U_1U_2/(\varphi(\ell_1)\varphi(\ell_2)),
\tag{18}
\]
where \(U_i=1_{(mn_i,\ell_i)=1}1_{(h_i,\ell_i)=1}\).
Every term belongs in a dispersion calculation.

When \(h_1=h_2=a\), (17) reduces to \(n_1\equiv n_2\pmod q\). In the packet it usually does not. The switched variable is instead
\[
f=\frac{h_1n_2-h_2n_1}{q},\qquad |f|\ll HN/q,
\tag{19}
\]
rather than the fixed-residue length \(N/q\). Fourier completion of a length \(M\) sum modulo \(qr_1r_2\) has dual scale \(qr_1r_2/M\), which is distinct from the physical \(H\).

For an exact diagonal test, restrict \(n_i\in[N,2N]\) to primes larger than \(2H\). Then \(h_1n_2=h_2n_1\) forces both \(n_1=n_2\) and \(h_1=h_2\), by divisibility. This physical diagonal includes the factor
\(\sum_h|V(h/H)|^2\asymp_V H\). Primitive projection does not remove that order: its exact correction in (4) is \(O(H^2/q)=o(H)\). This is a coefficient-level comparison, not an assertion that all signed off-diagonal contributions are positive.

A legal *fixed-residue numerical allocation* is easy. In Maynard II Proposition 8.2, printed p.19, take
\[
N=X^{.4},\ M=X^{.6},\quad
(Q_1,Q_2,Q_3)=(X^{.38},X^{.12},X^{.025}).
\]
Its four size inequalities have strict exponent margins
\[
.4-.38=.02,\quad 1-(.8+.12+2(.025))=.03,
\]
\[
2-(.8+.38+4(.12)+3(.025))=.265,\quad
2-(.4+.38+5(.12)+2(.025))=.57.
\tag{20}
\]
They allow a fixed sufficiently small source \(\epsilon\), at total level \(X^{.525}\).

However, the proposition additionally requires product-form bounded modulus coefficients, a fixed residue (constants may depend on it), and its rough/Siegel–Walfisz short factor. R18 does not produce a controlled product decomposition of the original \(\lambda_j\) in that functional. The proposition says nothing about the extra \(h_1,h_2\) determinant (17). Neither its conclusion nor the margins (20) are a completed physical-packet diagonal/off-diagonal budget. A reproof with averaged physical shifts would need a new bound for that determinant kernel and the full centered expansion (18).

This is a precise failed direct application, not an impossibility theorem for an averaged dispersion argument exploiting smoothness before absolute values.

## 6. Scope and next arithmetic obligation

Proved: exact centered packet norm and sharp duality; its order on a genuine admitted prime-factor family; the conditional localized-variance window; and the CRT change when physical shifts remain inside Cauchy–Schwarz. Equation (16) is a concrete legally allocated use of a variable-residue theorem with insufficient output.

Unproved: (13), any improvement of the RH \(X^{1.023}\) aggregate, a controlled original-weight decomposition for a stronger joint theorem, or a strict true-zeta Bragg deficit. Full-residue positivity and a convenient modulus factorization alone prove none of them.

A useful next input is quantitatively defined: a localized primitive variance like (13), uniform in the actual smooth profiles, or a signed joint dispersion estimate treating (17)–(18) at the original coefficient norm. No phase-twisted SW hypothesis, RH-to-GRH substitution, or omitted negative prime–continuum term is used here.

## Primary sources and verification

* James Maynard, [Primes in arithmetic progressions to large moduli III: Uniform residue classes, v1](https://arxiv.org/pdf/2006.08250v1), Theorems 1.1–1.3, printed pp.3–4; variable-residue outline p.5.
* James Maynard, [Primes in arithmetic progressions to large moduli II: Well-factorable estimates, v1](https://arxiv.org/pdf/2006.07088v1), printed pp.4–6 and Proposition 8.2 p.19.
* Hugh L. Montgomery and Robert C. Vaughan, [Multiplicative Number Theory II: Primes and Sieves, author draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf), Theorem 20.12, equation (20.38), printed pp.214–215.
* [Short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), Definition 2.1, Proposition 2.3, equation (2.5), Corollary 2.19.
* Frozen R11 CONDUCTOR_MASS_LOWER_BOUND.md and R18 MODULUS_WEIGHT_LEVEL_AND_NORMALIZATION.md supply the actual-family count/guards and exact normalization. R10/R11 supply the inherited separated-prime scope and RH aggregate estimate.

The adjacent checker verifies finite primitive projection, sharp Cauchy equality, CRT compatibility, all principal cross terms, and rational exponent comparisons. It does not test the unproved variance estimate or the asymptotic PNT family count. Source receipts pin the inspected versions; source PDFs remain local.

