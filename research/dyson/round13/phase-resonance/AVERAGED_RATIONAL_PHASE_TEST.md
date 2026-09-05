# Averaging the rational resonances: one power-saving extraction, and its retained main term

Date: 2026-09-05. Status: ordinary analytic bounds for an explicitly defined terminal Type II component. The extraction in Section 3 assumes RH for the Riemann zeta function. The counting, lower bound and minor-arc comparison do not. No improved bound for the complete actual-zeta covariance is proved.

The bad phases from Round 12 occupy a small fraction of the longer coefficient interval. That observation alone does not make them negligible. This note proves three quantitative statements at the actual scales:

- The rational core around zero can be replaced by an explicit integral with total error \(O(X^{.923}\log^2X)\), after the actual top-conductor and low-numerator weights are summed, assuming RH.
- Its retained main term cannot uniformly be discarded by absolute estimates. An admissible prime-interval convolution with the actual complementary moduli has a positive restricted core of size at least a constant times \(X^{1.123}/\log^{348}X\).
- The primary-source Vaughan bound, applied legally on enlarged minor arcs, gives only logarithmic cancellation at the chosen polylogarithmic cutoff. An elementary mean square in the longer variable is stronger here, but still gives \(O(X^{1.323}\sqrt{\log X})\), which is weaker than the existing Round 11 bound for the original prime pairing.

Thus averaging repairs the pointwise perspective but does not yet remove the need for cancellation in the retained signed main terms.

## 1. Exact component, coefficients and natural unit restrictions

Write
\[
Q=X^{523/1000},\qquad M=X^{3/5},\qquad N=X^{2/5},
\qquad X^{1/6}\le H\le X^{2/7}.
\tag{1}
\]
Let \(\mathcal Q_X\) be the full canonical balanced complementary family fixed in Rounds 9–12, and let
\[
\mathcal D_X=\mathcal Q_X\cap(Q/2,Q].
\]
For completeness, the canonical family consists of distinct squarefree \(d=[D,E]>X^{1/2}\), with
\[
D,E\le X^{523/2000},
\quad p^{3/2}D_{\ge p}\le X^{501/2000},
\quad p^{3/2}E_{\ge p}\le X^{501/2000},
\tag{2}
\]
where each respective owner condition is imposed at \(p>X^{1/1000}\).
Its source complementary theorem proves triple dense divisibility. Every prime factor of \(d\) is at most \(X^{523/2000}<N\), because it divides one of the two roots.

Fix \(V\in C_c^\infty(1,2)\), and initially assume \(|\alpha_m|\le1\), supported on \(M\le m<2M\). Define
\[
P_N(\vartheta)=\sum_{\substack{N\le p<2N\\p\ {\rm prime}}}
(\log p)e(\vartheta p),\qquad
S_{V,H}(\beta)=\sum_hV(h/H)e(-\beta h),
\quad e(t)=e^{2\pi it}.
\tag{3}
\]
The inner prime support is fixed independently of \(m\). For a set \(\mathcal A\) of phases on the circle, put
\[
\begin{split}
\mathcal T(\mathcal A)=
\sum_{d\in\mathcal D_X}\frac{\mu(d)}d
\sum_{\substack{1\le a\le d/(16H)\\(a,d)=1}}
S_{V,H}(a/d)
\sum_{\substack{M\le m<2M\\(m,d)=1\\am/d\bmod1\in\mathcal A}}
\alpha_m
\left[P_N(am/d)-\frac{\mu(d)}{\varphi(d)}P_N(0)\right].
\end{split}
\tag{4}
\]
The main variable \(m\) is the longer convolution factor; it is not a prime variable by default.

Formula (4) is a genuine terminal-conductor slice of the completed shifted progression discrepancy for the source-allowed convolution
\[
F=\alpha*\beta,\qquad
\beta(n)=(\log n)1_{\{n\ {\rm prime},\,N\le n<2N\}}.
\]
The source prime-interval Siegel–Walfisz statement, followed by partial summation, gives its required shorter-coefficient property. The scales and source parameters were checked in Round 12. This does not assert that an arbitrarily chosen \(\alpha\) is one specific factor in the actual zeta decomposition.

The mask \((m,d)=1\) in (4) is essential. All supported \(n\)-primes are units modulo \(d\), by (2). In the original progression and principal sums, primitive shifts therefore restrict the product to \((m,d)=1\). After this restriction, Fourier completion gives
\[
\frac1d\sum_{a\bmod d}S_{V,H}(a/d)
\left[
\sum_{\substack{m,n\\(mn,d)=1}}\alpha_m\beta_n e(amn/d)
-\frac{c_d(a)}{\varphi(d)}
\sum_{\substack{m,n\\(mn,d)=1}}\alpha_m\beta_n
\right],
\tag{5}
\]
where \(c_d\) is the Ramanujan sum. For \((a,d)=1\) and squarefree \(d\), \(c_d(a)=\mu(d)\), exactly as used in (4).
The full-signed-family conductor coefficient is \(\mu(d)/d\) here: no other multiple of \(d>Q/2\) fits below \(Q\). Nonprimitive Fourier numerators and all other conductors remain outside this slice.

The estimates below use the actual \(S_{V,H}\), without replacing it by a fictitious positive weight. For upper bounds, the elementary facts
\[
|S_{V,H}(\beta)|\ll_V H,\qquad
\sum_{\substack{1\le a\le d/(16H)\\(a,d)=1}}
\frac{|S_{V,H}(a/d)|}{d}\ll_V1
\tag{6}
\]
are sufficient. Summing (6) over \(\mathcal D_X\) costs at most \(O_V(Q)\).

For a fixed divisor-bounded outer family, one may multiply all the following upper bounds by \(O_\eta(X^\eta)\) for any fixed \(\eta>0\), including its prescribed logarithmic factors in a slightly larger \(\eta\). This follows from the pointwise divisor bound and is deliberately conservative. In particular, the extraction in Section 3 still has a power saving whenever \(\eta<77/1000\). The lower-bound witness uses \(\alpha_m=1\).

## 2. Exact residue counts for sparse resonances

Let \(\mathcal A\) be a disjoint union of \(J\) circular intervals with total length \(|\mathcal A|\). For a unit \(a\bmod d\), multiplication by \(a\) permutes the residue classes. Each class occurs in \([M,2M)\) at most \(M/d+1\) times. Counting grid points of spacing \(1/d\) in each interval gives
\[
\#\{M\le m<2M:am/d\bmod1\in\mathcal A\}
\le (M/d+1)\bigl(d|\mathcal A|+2J\bigr).
\tag{7}
\]
The estimate remains an upper bound after imposing \((m,d)=1\). No distribution theorem about the inverses of residues is needed.

Set \(R=(\log X)^B\), for fixed \(B>0\). The fixed-width cores around all reduced rationals of denominator \(q\le R\),
\[
\left\{\vartheta:\|\vartheta-b/q\|\le C/N\right\},
\qquad (b,q)=1,
\tag{8}
\]
are disjoint for sufficiently large \(X\), with the usual single rational \(0/1\). They have \(J\ll R^2\), total length \(O_C(R^2/N)\). Consequently their bad-\(m\) count, for each \(d,a\), is
\[
\ll_C (M+d)\left(\frac{R^2}{N}+\frac{R^2}{d}\right)
\ll_C \frac{MR^2}{N}.
\tag{9}
\]
Here \(M/d\gg X^{.077}\) and \(d/N\gg X^{.123}\), so the last simplification is uniform. The exceptional proportion is \(O(R^2/N)\), genuinely small.

For legal use of Dirichlet approximation on the complement, use the enlarged arcs
\[
\mathfrak M(R)=
\bigcup_{\substack{q\le R\\(b,q)=1}}
\left\{\vartheta:\|\vartheta-b/q\|
\le\frac{2R}{qN}\right\}.
\tag{10}
\]
They too are disjoint eventually. Their total length is
\[
\ll\frac RN\sum_{q\le R}\frac{\varphi(q)}q
\ll \frac{R^2}{N},
\]
and their number is \(O(R^2)\). Thus the same coarse count (9) holds. The enlargement does not worsen its logarithmic scale, but is needed for the minor-arc denominator conclusion in Section 6.

## 3. RH extraction of the zero-rational core with a power-saving total error

Fix \(C>0\), and let
\[
\mathcal A_0(C)=\{\vartheta:\|\vartheta\|\le C/N\}.
\]
Use the unique representative \(\vartheta\in[-C/N,C/N]\), and define the explicit continuous main term
\[
J_N(\vartheta)=\int_N^{2N}e(\vartheta u)\,du,
\qquad J_N(0)=N.
\tag{11}
\]
When \(\vartheta\ne0\), this is
\((e(2N\vartheta)-e(N\vartheta))/(2\pi i\vartheta)\).

Assume RH for \(\zeta\). The RH prime-number estimate
\(\theta(x)=x+O(\sqrt x\log^2x)\), with \(\theta(x)=\sum_{p\le x}\log p\),
follows, for example, from Schoenfeld's explicit Theorem 10, equation (6.3),
printed p.337 of [Sharper bounds for the Chebyshev functions theta(x) and psi(x), II](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf).
One partial summation gives, uniformly on this core,
\[
P_N(\vartheta)=J_N(\vartheta)+O_C(\sqrt N\log^2N).
\tag{12}
\]
Indeed the endpoint errors are \(O(\sqrt N\log^2N)\), while the differentiated exponential has total variation \(O(|\vartheta|N)=O_C(1)\). Endpoint choices \(<\) versus \(\le\) contribute at most \(O(\log N)\), already covered. Only the ordinary zeta RH is used for (12).

Let \(\mathcal J_0(C)\) be exactly (4) on this core, with its square bracket replaced by
\[
J_N(\vartheta)-\frac{\mu(d)}{\varphi(d)}N.
\tag{13}
\]
Then
\[
\boxed{
\mathcal T(\mathcal A_0(C))-\mathcal J_0(C)
\ll_{C,V}\frac{QM}{\sqrt N}\log^2X
=X^{923/1000}O_{C,V}(\log^2X).
}
\tag{14}
\]
To prove this, (7) bounds the number of core \(m\)'s by \(O_C(M/N)\) for each \(d,a\). The error in the centered bracket is at most
\((1+1/\varphi(d))O_C(\sqrt N\log^2N)\). Apply (6), and sum over at most \(Q\) conductors. This proves (14) without assuming cancellation of \(\alpha\), \(\mu(d)\) or \(S_{V,H}\).

An additional \(\log d\) conductor weight costs one logarithm, so the error is still \(o(X\log X)\). Any extra fixed logarithmic coefficient loss is likewise harmless for this positive exponent margin.

This is a proved, source-compatible arithmetic extraction for an identifiable phase component. It does not state that its main term \(\mathcal J_0\) is small. In particular, zero here describes the rational approximation to \(am/d\), not the deleted zero frequency of the original completion: \(a/d\ne0\) throughout (4).

## 4. The retained rational main is not uniformly negligible

Assume in this section that \(V\ge0\), \(m_V=\int V>0\), and choose the admissible outer sequence \(\alpha_m=1\) on \([M,2M)\).
Use the actual Round 11 subfamily \(\mathcal F_X\subset\mathcal D_X\) of products of two large and 346 small primes. It has
\[
|\mathcal F_X|\ge\frac{c_0Q}{2(\log X)^{348}},\quad
\mu(d)=1,\quad
\sum_{p\mid d}\frac1p
\le\frac{348}{\lambda X^\kappa}=o(1),
\tag{15}
\]
where
\[
\kappa=\frac{343}{346000},\quad
\lambda=2^{-1/348},\quad
c_0=\frac{(1-\lambda)^{348}}
{2!\,346!\,(9/100)^2\kappa^{346}}.
\]
All assertions hold for every sufficiently large real \(X\), uniformly in the specified \(H\)-range.

For each unit \(a\bmod d\), consider just the positive core
\[
1\le s\le\frac{d}{32N},\qquad
s\equiv am\pmod d,\qquad(s,d)=1.
\tag{16}
\]
The same elementary excluded-prime count used in Round 11 shows that (16) has at least \(d/(64N)\) possible residues \(s\), once \(X\) is large. The interval length \(d/(32N)\) tends to infinity, and its nonunits number at most that length times \(\sum_{p\mid d}1/p\), apart from the harmless endpoint unit count.
Every such residue gives at least \(M/(2d)\) representatives \(m\in[M,2M)\), because \(M/d\to\infty\). Thus there are at least
\[
\frac{M}{128N}
\tag{17}
\]
unit \(m\)'s in this positive core, for every allowed \(d,a\).

Now keep only actual low unit numerators \(1\le a\le d/(16H)\).
For \(h\) in the support of \(V(h/H)\), a prime \(p\in[N,2N)\), and \(m\) from (16),
\[
0<sp/d\le1/16,\qquad 0<ah/d<1/8.
\]
The phase of each product term \(e(sp/d-ah/d)\) is therefore between
\(-\pi/4\) and \(\pi/8\). Its real part is at least \(1/2\). Writing
\(S_0=\sum_hV(h/H)\), this gives
\[
\Re\!\left[
S_{V,H}(a/d)
\left(P_N(am/d)-\frac{P_N(0)}{\varphi(d)}\right)
\right]
\ge\left(\frac12-\frac1{\varphi(d)}\right)S_0P_N(0).
\tag{18}
\]
Eventually \(\varphi(d)\ge4\), \(S_0\ge m_VH/2\), and
\(P_N(0)\ge N/2\), the last inequality using the ordinary prime number theorem. Thus each centered term, after the coefficient \(1/d\), has real part at least
\[
\frac{m_VHN}{16d}.
\tag{19}
\]
This explicitly retains the primitive Ramanujan principal term; it has not been omitted to force positivity.

Round 11 supplies at least \(d/(32H)\) such primitive \(a\)'s for each \(d\in\mathcal F_X\). Combining (15), (17) and (19), the restricted positive-core contribution satisfies
\[
\boxed{
\Re\,\mathcal T_{\mathcal F_X}(\mathcal A_0^+)
\ge
\frac{c_0m_V}{131072}
\frac{QM}{(\log X)^{348}},
\qquad
\mathcal A_0^+=(0,1/(32N)].
}
\tag{20}
\]
Its power is \(QM=X^{1123/1000}\). Consequently it exceeds \(X\log X\) by an unbounded factor eventually, even with the displayed fixed logarithmic denominator. Equation (14), applied to this restricted positive core by the same proof, shows that the corresponding explicit integral main term has the same lower bound with a smaller fixed constant under RH.

This is an obstruction to treating all resonant slices as negligible by an absolute estimate uniformly over source-allowed coefficients. It is **not** a lower bound for the full signed family, for all rational cores combined, or for the coefficient sequence arising in one particular zeta or Heath–Brown decomposition. Cancellation against other conductors, other phases, or actual outer coefficients is still possible. The lower bound uses real primes and the actual arithmetic support, not a free choice of artificial Fourier locations.

## 5. Other small rational denominators: explicit main terms, but only logarithmic extraction from SW

For \(q\le R\), \((b,q)=1\), and
\(\vartheta=b/q+\xi\) in the enlarged arc (10), the ordinary Siegel–Walfisz theorem and partial summation give, for every fixed \(A>0\),
\[
P_N(b/q+\xi)
=\frac{\mu(q)}{\varphi(q)}J_N(\xi)
+O_{A,B}(N(\log X)^{-A}).
\tag{21}
\]
This includes the genuine-prime weights and both interval endpoints. To see the coefficient, sum the progression main terms against \(e(bc/q)\) over unit classes \(c\bmod q\); their sum is \(c_q(b)=\mu(q)\). All supported primes exceed \(q\). The costs of at most \(q\) classes and variation \(O(1+|\xi|N)\le O(1+2R)\) are fixed logarithmic powers, absorbed by choosing the source SW order larger. The finite source parameter \(B\) stays fixed.

Replacing the inner bracket in (4) accordingly, including replacement of \(P_N(0)\), defines an explicit finite rational-main expression on \(\mathfrak M(R)\). Its total extraction error is bounded by
\[
O_{A,B,V}\!\left(QM(\log X)^{-A}\right),
\tag{22}
\]
because (9) and (6) sum the inner \(N\log^{-A-2B}X\) error.
This bound by itself is insufficient for \(o(X\log X)\): \(QM=X^{1.123}\), and a fixed arbitrary logarithmic saving does not defeat its extra power.

An absolute bound for the retained oscillatory rational main is
\[
O_{B,V}(QMR).
\tag{23}
\]
For the fixed-width cores (8), count \(O(M/N)\) \(m\)'s per rational, use \(|J_N|\le N\), and sum the \(1/\varphi(q)\) main coefficient over the \(\varphi(q)\) reduced numerators. This costs \(O(M)\) per denominator.
For the enlarged arcs, the same order follows from
\[
|J_N(\xi)|\ll\min(N,|\xi|^{-1}).
\]
On the \(1/d\) phase grid, summing this bound within distance \(2R/(qN)\) of a fixed rational costs
\[
O\!\left(N+d\log(4R/q)\right).
\]
Each residue is repeated at most \(M/d+1\ll M/d\) times. After the \(1/\varphi(q)\) coefficient and its \(\varphi(q)\) numerators are summed, the total is
\[
O\!\left(M\sum_{q\le R}
\left[\log(4R/q)+N/d\right]\right)=O(MR),
\]
uniformly for \(d\asymp Q\). Then (6) gives (23).
The separate primitive principal term is retained; its absolute value on all \(m\), and hence on these arcs, is at most \(O_V(X\log X)\), as in Section 6.

Ordinary zeta RH does not imply the analogous square-root progression error for all \(q>1\). Assuming RH for the corresponding Dirichlet \(L\)-functions would change (22), but that is an additional assumption and is not used here. No failure of the desired actual average is inferred merely from the insufficiency of (22).

## 6. A legal minor-arc bound, and the stronger elementary average in \(m\)

The primary source for the pointwise estimate is Montgomery–Vaughan,
[*Multiplicative Number Theory II: Primes and Sieves*](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf),
author-hosted draft, Theorem 17.1, equation (17.29),
printed p.65 (PDF page 77). It states that, when \((b,q)=1\) and
\(|\vartheta-b/q|\le q^{-2}\),
\[
\left|\sum_{n\le Y}\Lambda(n)e(\vartheta n)\right|
\ll\left(\frac{Y}{\sqrt q}+Y^{4/5}+\sqrt{Yq}\right)
(\log Y)^{5/2}.
\tag{24}
\]
Taking the difference of prefixes at \(N,2N\), and subtracting the prime-power terms of size \(O(\sqrt N\log^2N)\), proves the same bound for \(P_N\), with \(Y\) replaced by \(N\) up to absolute constants.

For \(\vartheta\notin\mathfrak M(R)\), set \(D_0=\lfloor N/R\rfloor\).
For sufficiently large \(X\), \(D_0\ge N/(2R)\). Dirichlet approximation
with this integer cutoff supplies
\[
R<q\le D_0\le N/R,\qquad
|\vartheta-b/q|\le (qD_0)^{-1}\le q^{-2}.
\]
Indeed \(q\le R\) would place the phase inside (10), since
\((qD_0)^{-1}\le2R/(qN)\).
Therefore (24) applies legally and gives
\[
|P_N(\vartheta)|
\ll\left(NR^{-1/2}+N^{4/5}\right)(\log N)^{5/2}.
\tag{25}
\]
The complement of the fixed-width cores (8) alone does not imply \(q>R\); small denominators may still have approximation error between \(C/N\) and \(2R/(qN)\). That is why (10) was introduced.

Using (6), summing the longer variable absolutely, and keeping the primitive
principal term separately, yields the following bound. The latter term costs
at most \(O_V(MN\sum_{d\le Q}1/\varphi(d))=O_V(X\log X)\), by the
elementary reciprocal-totient estimate.
\[
|\mathcal T(\mathfrak M(R)^c)|
\ll_V
QM\left(NR^{-1/2}+N^{4/5}\right)(\log N)^{5/2}
+X\log X.
\tag{26}
\]
At polylogarithmic \(R\), its leading power is \(QMN=X^{1.523}\); only logarithms are saved. This is not a useful improvement over Round 11.

There is a stronger unconditional averaged estimate that uses the fixed inner coefficients. Since \(2N<d\) eventually, no two supported primes are congruent modulo \(d\). For any unit \(a\bmod d\), complete-period orthogonality gives
\[
\begin{split}
\sum_{M\le m<2M}|P_N(am/d)|^2
&\le(M/d+1)\sum_{r\bmod d}|P_N(r/d)|^2\\
&=(M+d)\sum_{N\le p<2N}(\log p)^2\\
&\ll (M+d)N\log N.
\end{split}
\tag{27}
\]
One can retain the centering exactly, rather than paying for it separately.
Every supported prime is a unit modulo \(d\), so the Ramanujan identity gives
\[
\frac1{\varphi(d)}\sum_{r\bmod d}^{*}P_N(r/d)
=\frac{\mu(d)}{\varphi(d)}P_N(0)=:c_d.
\]
Consequently the exact centered unit variance is
\[
\sum_{r\bmod d}^{*}|P_N(r/d)-c_d|^2
=\sum_{r\bmod d}^{*}|P_N(r/d)|^2
-\frac{|P_N(0)|^2}{\varphi(d)}
\le d\sum_{N\le p<2N}(\log p)^2.
\tag{28}
\]
Multiplication by a unit \(a\) permutes these unit residues. Splitting the
longer interval into residue periods, restricting its nonnegative squared
sum to the minor arcs, and applying Cauchy–Schwarz therefore proves
\[
\sum_{\substack{M\le m<2M\\(m,d)=1\\am/d\notin\mathfrak M(R)}}
|\alpha_m(P_N(am/d)-c_d)|
\ll M\sqrt{N\log N}.
\tag{29}
\]
This exact variance calculation was independently pointed out in the
minor-arc source audit. It requires the fixed inner support and coefficients;
it is not a formal consequence for arbitrary \(m\)-dependent inner sums.
Thus (6) and (29) give
\[
\boxed{
|\mathcal T(\mathfrak M(R)^c)|
\ll_V QM\sqrt{N\log N}
=O_V\!\left(X^{1323/1000}\sqrt{\log X}\right).
}
\tag{30}
\]
This saves a power \(X^{.2}\) relative to the absolute \(QMN\) bound, but it is still insufficient at scale \(X\log X\), and still worse than the existing \(X^{1.023}\log^5X\) estimate for the original completed prime polynomial. A bound for this factored test must not be presented as an improvement to that existing estimate.

## 7. Bounded conclusion and source record

The useful positive statement from this test is (14): ordinary RH extracts the zero-rational core with an error already below the required arithmetic scale, even after the actual weights are summed. Its explicit main term remains part of the problem.

The precise limitation is (20), together with (22) and (30): sparse resonances can retain a power-large main contribution on an admissible arithmetic block; the remaining available minor-arc estimates do not bound the whole factored pairing at the required scale. Any next advance through this route must exploit the actual outer coefficients and signs when handling those retained main terms or use a stronger joint estimate. No generic claim that such cancellation is impossible is justified by this note.

The source paper is [OpenAI, *Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf): Proposition 2.3 pp.4–5 supplies the complementary moduli; Proposition 2.10 p.7 supplies prime-interval SW; Definition 2.9 p.6 specifies its normalization; Proposition 2.18 pp.10–11 supplies the legal Type II scales. The R12 report pins and checks these exact hypotheses. The primary Montgomery–Vaughan PDF SHA-256 is
72448ec23158a3aeee534c9cde633d5402f916d0367b4f320212cd7ad179d340.
The companion source audit records the downloaded copy and printed-page check.

The adjacent exact script checks the rational exponents, finite Fourier completion with the natural unit mask, residue-count bounds, and all lower-bound constants. It does not numerically search for large primes, approximate the asymptotic threshold, or substitute a finite toy modulus for the canonical-family proof. This note and all checks are new R13 files; prior rounds remain frozen.
