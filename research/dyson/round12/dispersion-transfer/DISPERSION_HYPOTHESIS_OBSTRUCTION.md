# Two explicit hypothesis failures in the proposed dispersion transfer

Date: 2026-09-05. Status: ordinary arithmetic proofs, with exact source-parameter checks. No improved bound for the actual prime pairing is proved here. The counterexample below concerns preservation of a coefficient hypothesis; it is not a counterexample to the source dispersion theorem.

The 186 paper's triply densely divisible dispersion theorem does not directly give the missing improvement in the completed Round 11 pairing. Two specific proposed applications fail:

1. Absorbing a completed additive phase into a Siegel–Walfisz coefficient does not preserve that property. This fails for a prime-interval coefficient at legal source scales, with a conductor in our actual canonical complementary family and the actual reduced numerator \(a=1\). The resulting discrepancy at modulus 3 is explicitly of order \(N/\log N\).
2. Lifting the growing shift interval through the source's product-of-local-residue-sets lemma requires \(\varphi(d)\) classes on an explicit subfamily. Its bounded-local-class hypothesis is therefore unavailable, even after all primitive restrictions are imposed.

These statements leave open a dispersion argument retaining the shift, the additive phase and the prime coefficient jointly. They do not prove the remaining \(X^{.023}\) loss is unavoidable for primes. The source is [OpenAI, *Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf); precise printed-page locations and file hashes are recorded below and in the companion certificate.

## 1. The exact pairing and the family being tested

Put
\[
Q=X^{523/1000},\qquad X^{1/6}\le H\le X^{2/7},
\qquad e(t)=\exp(2\pi i t).
\tag{1}
\]
Fix a nonnegative, nonzero \(V\in C_c^\infty(1,2)\). This hypothesis permits the real-prime support construction used here; no claim uniform over arbitrary signed profiles is made.

The canonical family \(\mathcal Q_X\) contains every distinct squarefree modulus \(q=[D,E]\) satisfying
\[
\begin{gathered}
D,E\le X^{523/2000},\qquad q>X^{1/2},\\
p^{3/2}D_{\ge p}\le X^{501/2000}
\quad(p\mid D,\ p>X^{1/1000}),\\
p^{3/2}E_{\ge p}\le X^{501/2000}
\quad(p\mid E,\ p>X^{1/1000}).
\end{gathered}
\tag{2}
\]
Each modulus is counted once with coefficient \(\mu(q)\). These are the balanced complementary predicates fixed in Round 9. Source Proposition 2.3, printed pp.4–5, gives
\[
\mathcal Q_X\subset
\{q\le Q:q\text{ squarefree},\ q\in\mathcal D^{(3)}(X^{1/1000})\}.
\tag{3}
\]
There is no arbitrary-subset Möbius-cancellation assertion.

For a separated fixed smooth prime weight \(f\), the exact completed expression is
\[
\mathfrak B_j(f,V)=
\sum_{\substack{2\le d\le Q\\1\le a<d,\ (a,d)=1}}
S_{V,H}(a/d)M_d^{(j)}
\left[A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)\right],
\tag{4}
\]
where
\[
\begin{split}
S_{V,H}(\beta)&=\sum_h V(h/H)e(-\beta h),\\
M_d^{(j)}&=\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}
\frac{\mu(q)(\log q)^j}{q},\qquad j=0,1,\\
A_f(\beta)&=\sum_{p\ {\rm prime}}(\log p)f(p/X)e(\beta p).
\end{split}
\tag{5}
\]
The Ramanujan principal subtraction in (4) is retained. The zero frequency cancels exactly. The actual logarithmic kernel is assembled from \(\mathfrak B_0,\mathfrak B_1\) by the already proved uniformly summable smooth separation; the term \(\log X\,\mathfrak B_0\) must also be counted. This report tests an attempted arithmetic input to (4), not a replacement positive norm.

Under RH, the frozen Round 11 bound for the complete fixed smooth discrepancy component is
\[
O_{V,\chi}\!\left(\sqrt{X(X+Q^2)}(\log X)^5\right)
=O_{V,\chi}\!\left(X^{1023/1000}(\log X)^5\right).
\tag{6}
\]
Its remaining power loss comes from \(Q/\sqrt X=X^{23/1000}\). No step below improves (6).

## 2. Actual terminal conductors and source-compatible scales

The frozen Round 11 construction uses
\[
u=\frac9{100},\quad
\kappa=\frac{343}{346000},\quad
\lambda=2^{-1/348}.
\]
Let \(\mathcal F_X\) consist of products of two distinct primes in
\((\lambda X^u,X^u]\) and 346 distinct primes in
\((\lambda X^\kappa,X^\kappa]\). For every sufficiently large real \(X\), that construction proves
\[
\mathcal F_X\subset\mathcal Q_X\cap(Q/2,Q],\qquad
|\mathcal F_X|\sim
c_0\frac{Q}{(\log X)^{348}},\quad c_0>0.
\tag{7}
\]
The exact constant is
\[
c_0=\frac{(1-\lambda)^{348}}{2!\,346!\,u^2\kappa^{346}}.
\]
Unique factorization prevents permutation overcounting. The source guards are checked by splitting one large and 173 small primes into each root:
\[
2u+346\kappa=\frac{523}{1000},\qquad
u+173\kappa=\frac{523}{2000},\qquad
\frac52u=\frac9{40}<\frac{501}{2000}.
\tag{8}
\]
Thus these are actual complementary moduli, with two factors larger than the density parameter. Their existence and count use only the prime number theorem on fixed-ratio intervals.

Every \(d\in\mathcal F_X\) has exactly 348 prime factors, all tending to infinity; in particular \(3\nmid d\) eventually. Also \(\mu(d)=1\) and
\[
M_d^{(0)}=\frac1d,\qquad M_d^{(1)}=\frac{\log d}{d},
\tag{9}
\]
because the only multiple of \(d>Q/2\) at most \(Q\) is \(d\) itself. Signed lower moduli cannot cancel these terminal coefficients.

Source Proposition 2.18, printed pp.10–11, applies to a convolution \(\alpha*\beta\) at scales \(MN\asymp X\), with
\[
X^{1/2-\sigma}\le N\le X^{1/2},
\tag{10}
\]
provided \(\beta\) has the source Siegel–Walfisz property and
\[
72\omega+24\delta<1,\quad
48\omega+16\delta+4\sigma<1,\quad
64\omega+20\delta+2\sigma<1.
\tag{11}
\]
Use the actual parameters
\[
\omega=\frac3{250},\quad
\delta=\frac1{1000},\quad
\varepsilon=\frac1{1000},\quad
\sigma=\frac{101}{1000}.
\tag{12}
\]
The modulus cutoff \(X^{1/2+2\omega-\varepsilon}\) is exactly \(Q\).
The three left sides of (11) are respectively
\[
\frac{111}{125}=.888,\qquad
\frac{249}{250}=.996,\qquad
\frac{99}{100}=.990.
\tag{13}
\]
Take
\[
N=X^{2/5},\qquad M=X^{3/5}.
\tag{14}
\]
Then \(MN=X\), and \(1/2-\sigma=.399<.4<.5\). The counterexample below therefore does not manufacture an out-of-range factor or an inadmissible modulus.

## 3. A real-prime coefficient loses Siegel–Walfisz after phase absorption

The source's Definition 2.9, printed p.6, requires one fixed \(C_{\rm SW}\) such that for every fixed \(L>0\)
\[
\left|
\sum_{\substack{n\equiv a\pmod r\\(n,s)=1}}\beta(n)
-\frac1{\varphi(r)}
\sum_{(n,rs)=1}\beta(n)
\right|
\ll_L \tau(rs)^{C_{\rm SW}}N(\log X)^{-L},
\tag{15}
\]
uniformly in \(r,s,a\) with \((a,r)=1\). Here \(r\) denotes the test modulus; it is not the conductor \(d\).

By source Proposition 2.10, printed p.7,
\[
\beta_X(n)=1_{\{n\ {\rm prime},\ N\le n<2N\}}
\tag{16}
\]
has this property, uniformly in the interval endpoints and auxiliary coprimality parameter, because \(N=X^{2/5}\). It is a coefficient sequence located at scale \(N\).

**Lemma.** For every sufficiently large real \(X\), and every
\(d\in\mathcal F_X\), there is a unit \(m\bmod d\) represented by an integer in \([M,2M]\) such that the sequence
\[
\widetilde\beta_{X,d,m}(n)=\beta_X(n)e(mn/d)
\tag{17}
\]
does not satisfy (15) as a uniform family. At \(r=3,s=1,a=1\), its discrepancy is
\[
\boxed{
\Delta(\widetilde\beta;1\bmod3)
=\left(\frac{i\sqrt3}{4}+o(1)\right)\frac{N}{\log N}.
}
\tag{18}
\]
The \(o(1)\) is uniform in the conductors \(d\) and choices of \(m\) made below. No RH assumption is used.

**Proof.** Define
\[
k=\begin{cases}
(d-1)/3,&d\equiv1\pmod3,\\
(d+1)/3,&d\equiv2\pmod3.
\end{cases}
\tag{19}
\]
Thus
\[
\frac{k}{d}=
\begin{cases}
\frac13-\frac1{3d},&d\equiv1\pmod3,\\
\frac13+\frac1{3d},&d\equiv2\pmod3,
\end{cases}
\qquad (k,d)=1.
\tag{20}
\]
The gcd assertion follows from \(3k=d\pm1\). Because
\[
\frac{M}{d}\ge X^{3/5-523/1000}=X^{77/1000}\longrightarrow\infty,
\]
the interval \([M,2M]\) contains an integer \(m\equiv k\pmod d\). Choose one. Then \(m\) is a unit modulo \(d\) and \(e(mn/d)=e(kn/d)\).

The numerator \(a=1\) used here is an actual reduced completed frequency. In fact \(d/(16H)\to\infty\) uniformly in the prescribed \(H\)-range, and the Round 11 positivity argument gives
\[
|S_{V,H}(1/d)|\ge\frac{H}{2\sqrt2}\int V>0
\]
for all sufficiently large \(X\). The phase being tested is therefore not attached to a missing or zero-weight frequency.

For \(n\in[N,2N)\), equations (20) give
\[
e(kn/d)=e(n/3)\bigl(1+O(N/d)\bigr),
\tag{21}
\]
with an absolute implied constant for either sign. The prime number theorem in the two fixed reduced classes modulo 3 gives, for \(b=1,2\),
\[
\#\{N\le p<2N:p\equiv b\pmod3\}
=\left(\frac12+o(1)\right)\frac{N}{\log N}.
\tag{22}
\]
Summing (21) over these primes shows
\[
\sum_{n\equiv b(3)}\widetilde\beta(n)
=e(b/3)\left(\frac12+o(1)\right)\frac N{\log N}
+O\!\left(\frac{N^2}{d\log N}\right).
\tag{23}
\]
The perturbation is \(o(N/\log N)\), uniformly, since
\(N/d\le2X^{-123/1000}\). All supported primes exceed 3. Hence the exact principal subtraction in (15) is one half of the sum of the two class sums. Their difference divided by two is
\[
\frac{e(1/3)-e(2/3)}4\frac N{\log N}
+o\!\left(\frac N{\log N}\right)
=\frac{i\sqrt3}{4}\frac N{\log N}
+o\!\left(\frac N{\log N}\right),
\]
which proves (18). The two signs in (20) both tend to the same cubic phase, so the leading sign in (18) does not switch with \(d\bmod3\).

Finally, for \(L=2\), the right side of (15) at \(r=3,s=1\) is
\(O(2^{C_{\rm SW}}N(\log X)^{-2})\). Since
\(\log N=(2/5)\log X\), (18) is larger by an unbounded logarithmic factor for every fixed \(C_{\rm SW}\) and implied constant. This is the claimed failure. \(\square\)

This lemma has a precise scope. A convolution expansion of an additive prime phase creates terms \(e(am n/d)\). To absorb them into the shorter factor and apply Proposition 2.18, one would have to check the Siegel–Walfisz property of \(\beta(n)e(am n/d)\), uniformly in the variables being summed. It does not follow from that property for \(\beta\), even on the actual allowed conductors, at allowed scales and with a unit \(m\). A delta sequence supported on the chosen \(m\) is itself an allowed longer coefficient, so the issue is not a failure of divisor boundedness. Moreover, the absorbed sequence varies with \(m,a,d\), whereas the source dispersion sum is stated for a fixed coefficient family before its modulus sum.

The lemma does not assert that every factor in a particular Heath–Brown expansion fails (15), or that one bad slice prevents an averaged estimate. Such an averaged estimate would be new input to the proposed transfer and would have to retain this dependence. Source Proposition 2.18 and its proof in Appendix A.4.2 remain consistent with the example: their hypothesis (15) has been violated after the proposed absorption.

## 4. The shift interval is not a bounded product of local residue sets

There is a second tempting use of the source. Equation (2.5), printed p.7, permits a set of primes and one coherent primitive residue class that depend on \(X\), uniformly, but fixes the class outside the modulus sum. For one fixed shift \(h\), this is the legal Round 9 application. Simultaneous shifts \(h\asymp H\) require more than that statement.

Source Proposition 2.14, printed pp.9–10, lifts coherent estimates to a product of local nonempty class sets \(\mathcal A_p\subseteq(\mathbb Z/p\mathbb Z)^\times\), at the explicit cost
\[
\mathfrak m(d)=\prod_{p\mid d}|\mathcal A_p|.
\tag{24}
\]
It obtains a fixed divisor-weight cost when \(|\mathcal A_p|\le K\) for a fixed \(K\). Its underlying finite inequality is valid without this restriction; the restriction is what permits the subsequent source error bound without a power cost.

Choose a closed interval \([z_0,z_1]\subset(1,2)\) of positive length \(\ell=z_1-z_0\) on which \(V\) is strictly positive. Such an interval exists. For any \(d\in\mathcal F_X\), put
\[
\mathcal H_d=\{h\in[z_0H,z_1H]\cap\mathbb Z:(h,d)=1\}.
\]
For every prime \(p\mid d\) and every unit \(a\bmod p\),
\[
\begin{split}
\#\{h\in\mathcal H_d:h\equiv a\pmod p\}
&\ge\frac{\ell H}{p}-1
-\sum_{\substack{r\mid d\\r\ {\rm prime},\,r\ne p}}
\left(\frac{\ell H}{pr}+1\right)\\
&\ge\frac{\ell H}{p}
\left(1-\frac{347}{\lambda X^\kappa}\right)-348.
\end{split}
\tag{25}
\]
The first line uses the Chinese remainder theorem for the simultaneous conditions \(h\equiv a\pmod p,\ h\equiv0\pmod r\); the primes are distinct. Every \(p\mid d\) is at most \(X^{9/100}\), so
\[
\frac Hp\ge X^{1/6-9/100}=X^{23/300}\longrightarrow\infty.
\]
Thus (25) is positive uniformly in \(p,a,d,H\), once \(X\) is sufficiently large.

Consequently, even **after the global coprimality restriction**, the image of \(\mathcal H_d\) modulo each \(p\mid d\) is the entire unit group. Its smallest product-of-local-images hull therefore has
\[
\mathcal A_p=(\mathbb Z/p\mathbb Z)^\times,\qquad
\mathfrak m(d)=\prod_{p\mid d}(p-1)=\varphi(d).
\tag{26}
\]
Since
\[
1\ge\frac{\varphi(d)}d
=\prod_{p\mid d}(1-1/p)
\ge1-\frac{348}{\lambda X^\kappa},
\]
one has \(\mathfrak m(d)\sim d\asymp Q\), uniformly on \(\mathcal F_X\). On the other hand \(\tau(d)=2^{348}\) is constant. For any fixed \(B,C\),
\[
\frac{\mathfrak m(d)}{\tau(d)^B(\log X)^C}\longrightarrow\infty.
\tag{27}
\]
Therefore the divisor-weight consequence of Proposition 2.14 is not available for this product hull. Source logarithmic savings cannot absorb this \(\asymp Q\) factor.

The actual interval supplies only \(O(H)\) coherent global classes, since \(H\ll d\). Its local images have discarded the correlation between residues at different primes. The failure in (27) is a failure of this product-hull transfer, not an impossibility theorem for a nonproduct residue set or a signed average over the interval.

## 5. A short-factor reinterpretation also misses the stated scale range

If one instead tries to treat the shift length \(H\) itself as the shorter convolution scale \(N\) at total scale \(X\), the second inequality of (11), with the actual \(\omega,\delta\), forces
\[
\sigma<
\frac{1-48\omega-16\delta}{4}
=\frac{51}{500}.
\]
It follows that
\[
N\ge X^{1/2-\sigma}>X^{199/500},
\tag{28}
\]
whereas \(H\le X^{2/7}\). The positive exponent gap is
\[
\frac{199}{500}-\frac27=\frac{393}{3500}.
\tag{29}
\]
Thus this specific reinterpretation is outside Proposition 2.18 before coefficient conditions are considered. This says nothing about a different regrouping, a different total scale with all errors tracked, or a new multivariable dispersion proof.

## 6. What is and is not established

The actual factorization information has been used, not merely a scalar distribution exponent. The conductors in the counterexample satisfy the complementary predicates and retain the full original triple dense-divisibility budget. The modulus cutoff, both convolution scales, the primitive restrictions, the sign of the cubic phase, and the source's absolute Siegel–Walfisz normalization have all been checked.

What remains absent is an estimate for the signed joint object (4), retaining its \(d\)-dependent additive phase, its conductor coefficient \(M_d^{(j)}\), and its growing coherent shift interval. A direct \(X(\log X)^C\)-scale bound for that object would already remove the remaining power loss in (6); the actual zeta covariance target requires sharper control of the logarithms and all other components as well. One sufficient component-level condition, with suitable uniformity for the smooth separated profiles, would be
\[
\log X\,|\mathfrak B_0|+|\mathfrak B_1|
=o(X\log X).
\tag{30}
\]
No assertion that (30) follows from the source theorem, or that it is false, is made.

The source's Appendix A.4.2, printed pp.35–36, fixes coefficient supports and derivative bounds before taking suprema, performs a dispersion square, chooses dense divisors with their quotient losses, and retains its original unit masks. The resulting rational completion estimate is part of that argument; it is not a theorem about arbitrary modulus-dependent twisted coefficients. Reusing it for (4) would require a new reduction with the extra variable and coefficient dependence explicitly controlled.

The bounded conclusion is therefore: phase absorption and product-local residue lifting do not justify the proposed transfer, with the exact failures proved above. A joint dispersion argument remains a meaningful open arithmetic step. The finite check accompanying this note verifies rational inequalities, the cubic-phase algebra and modular selection; it does not purport to prove a numerical prime-gap bound or realize the large asymptotic moduli on a computer.

## 7. Provenance and reproduction

Primary source: [OpenAI, *Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf).

| Source location | Use in this note |
| --- | --- |
| Definition 2.1 and Proposition 2.3, pp.4–5 | Strong recursive dense divisibility and actual complementary moduli |
| Definitions 2.6–2.9, p.6, especially equation (2.4) | Coefficient families, scale and the exact uniform SW requirement |
| Proposition 2.10 and equation (2.5), p.7 | Prime-interval SW; one coherent class fixed outside the modulus sum |
| Proposition 2.14, pp.9–10 | CRT product-set lift and its explicit \(\mathfrak m(d)\) cost |
| Proposition 2.18, pp.10–11, equation (2.14) | Bilinear dispersion hypotheses and scale inequalities |
| Appendix A.4.2, pp.35–36 | Source dependence on fixed coefficients, divisor choices and unit masks |

The local primary PDF SHA-256 is
456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930.
Its extracted text SHA-256 is
ded13a7c74fcfce64e85769e05b5869803dccdf53b88be2c2f3c0b344f95ee84.
The source-preserving official repository was pinned at commit
61340d0b74163003b32756bb16e91d9209a5e330.
No source files were modified.

The exact construction and coefficient-isolation proof used from Round 11 is
CONDUCTOR_MASS_LOWER_BOUND.md, SHA-256
46347799005bb0f53af25c2a7e8ffb2b2217d92688c7651327dde3562f114b92.
The current note only uses its explicitly stated all-large-\(X\) conclusions, not a claimed numerical realization.

Run the adjacent standard-library Python script check_dispersion_hypotheses.py. It writes dispersion_hypotheses_certificate.json, including the final report/script hashes and primary-source hashes. The fixed small integer examples in that script test only the algebra of (19)–(20); they are not substitutes for the canonical-family existence proof.
