# Round 9: actual prime arithmetic for the Dyson–Montgomery programme

Date: 2026-09-05. This checkpoint continues the user's request to concentrate on RMT and actual zeta zeros. **No new zeta pair-correlation lower bound, AH refutation, half-gap theorem, RH proof, or prime-gap record is established.** The useful outcomes are a source-checked arithmetic transfer, a quantified removal of prime powers, a negative new resonator trial, and a precise mesoscopic lower-bound obligation.

## 1. The conjecture-level target remains unchanged

Set

\[
I_T(c)=\int_0^T\left|\frac{\zeta'}{\zeta}
\left(\frac12+\frac c{\log T}+it\right)\right|^2dt,
\qquad
W_T=\frac{2(\sinh2\,I_T(1)-\sinh1\,I_T(1/2))}{T\log^2T}.
\]

The reviewed Round 7 reduction gives, under RH and the precise AH-Pairs formulation,

\[
W_T\longrightarrow W_{\rm AH}=0.0623924179764985\ldots <\frac1{16}.
\]

The bounded but possibly nonconvergent near-diagonal mass cancels. An actual-zeta proof of liminf W_T>=1/16 would therefore contradict AH-Pairs under RH. That inequality remains unproved. Round 8 writes W_T=B+E_T+o(1), with B=0.4560939793292317..., so the missing signed residual inequality is liminf E_T>=-0.3935939793292317.... See the [Round 7 reduction](../dyson/round7/poisson-resolvent/TWO_SCALE_ZETA_TARGET.md) and [Round 8 proof](../dyson/round8/resolvent-arithmetic/SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md).

The complementary compact test has Fourier support [6/5,7/5]. Its centered prime covariance has AH value -3/5 and sine-kernel prediction -3/10. A sufficiently strong estimate here would be an actual out-of-band zeta result. The atomic diagonal, continuous mean, prime/mean cross term, and continuous mean square must all be retained.

## 2. What the 186 factorization structure really transfers

The [complete transfer proof](../dyson/round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md) applies Proposition 2.3 and Corollary 2.19 of [*Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf). It uses the ordinary analytic theorem as input, without making a claim about completion of every formalization obligation.

Choose omega=3/250, delta=1/1000 and epsilon=1/1000. Then 240 omega+80 delta=2.96<3, and the resulting full-prime distribution level is 0.523. Let Q_X be a set of distinct squarefree moduli q=[D,E] in (X^(1/2),X^(.523)] satisfying the stated complementary tail predicates. They imply triple dense divisibility at scale X^(.001), even for explicit nonsmooth examples. Repeated representations of one q are counted once; shared prime factors of D,E are allowed.

Insert the exact identity

\[
\Lambda(n)=\sum_{q\mid n}\mu(q)\log(n/q)
=B_{\mathcal Q}(n)+B_{\rm rest}(n).
\]

For a shift h and a smooth macroscopic weight w_h, define

\[
\mathcal C_{\mathcal Q,h}=\sum_n\Lambda(n+h)B_{\mathcal Q}(n)w_h(n),
\quad
\mathcal M_{\mathcal Q,h}=
\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}
\frac{\mu(q)}{\varphi(q)}\int w_h(u)\log(u/q)du.
\]

The source gives, for every fixed A>0,

\[
\mathcal C_{\mathcal Q,h}-\mathcal M_{\mathcal Q,h}
=O_A(X\log^{-A}X).
\tag{1}
\]

This estimate is uniform for 1<=h<=CH, where X=T^alpha, 6/5<=alpha<=7/5 and H=X/T. It applies to a localized version of the actual covariance's sinc weight. The proof checks the common primitive residue h across the modulus family, two common endpoint weights in partial summation, the sum of 1/phi(q), and both kinds of nonprimitive prime-power terms. Neither B_Q nor its remainder is a prime minorant.

This is an identifiable arithmetic component beyond the square-root divisor level. It is not an evaluation of the whole covariance. Summing (1) over every h gives O_A(HX log^(-A)X), whereas the needed fluctuation scale is X log X. Since H is between X^(1/6) and X^(2/7), no fixed logarithmic saving absorbs that loss. Logarithmically bounded shift packets are controlled at the required scale, but that does not evaluate the entire natural packet.

The report isolates the signed progression discrepancy sum D_Q explicitly. Under RH it proves

\[
\sum_{h\le CH}(\mathcal C_{\mathcal Q,h}-\mathcal M_{\mathcal Q,h})
=\mathfrak D_{\mathcal Q}(X,T)+O(H\sqrt X\log^4X).
\tag{2}
\]

The last error is o(X log X), uniformly over the alpha interval. The new estimate still needed for this selected component is D_Q=o(X log X). The remaining shifted bilinear form B_rest, the two support sums in M_Q, other spatial/shift ranges, and the continuous centering remain separate obligations. In particular, the source's multiplicative-convolution bilinear theorem cannot simply be applied to Lambda(qm+h), which depends jointly on all three variables.

The [independent source and proof review](../dyson/round9/factorization-covariance/INDEPENDENT_BRIDGE_REVIEW.md) accepts (1) and (2) with these scopes. The exact script checks 300 formal Mobius–log identities and five progression/discrepancy decompositions. These finite examples test algebra, not the source's asymptotic distribution estimate.

## 3. A new two-prime interaction was tried and failed

Archive inspection showed that the proposed resummed multiplicative prime profile had already been tried. Its old best continuation did not beat the existing larger polynomial trial. Repeating that scan was stopped before computation.

The replacement uses a genuinely different fixed arithmetic mark. For n<=L, let C count distinct prime divisors p with p³>L, and D=C(C-1)/2. Then C is in {0,1,2}, while D is in {0,1}. The new family is

\[
r_L(n)=d_\ell(n)[F(v_n,S(n))+D_L(n)J(v_n,S(n))],
\qquad \ell=27/25.
\]

When D=1 there is a unique unordered pair p<q of large prime divisors and n=pqm with m<L^(1/3)<min(p,q). This supplies an exact coprime starting decomposition. A singly marked prime at the same threshold does require a repeated-prime error; that error is explicitly O((log L)^a L^(-1/3)), with a=ell². The full three-state insertion calculus keeps the mixed event involving one background and one inserted large prime.

The [arithmetic derivation](../dyson/round9/multiplicative-profile/DERIVATION.md), accepted in a [separate root review](../dyson/round9/multiplicative-profile/INDEPENDENT_REVIEW.md), extends the previously reviewed fixed-moment and signed operator-truncation argument. It does not assume a general Fock limit, growing degree, or uniformity over infinitely many marks.

One fixed 30-dimensional span was tested: 20 unmarked features and ten D-marked features. Every coefficient was optimized in that span at quadrature orders 20 and 32; ell and the threshold were fixed.

| Trial | Order 32 half-gap margin |
|---|---:|
| Matched 20-feature baseline | -0.0146549380840028 |
| New 30-feature double-prime interaction | -0.0146549114371551 |
| Earlier best 48-feature trial, approximate | -0.0146547256 |

The new floating gain over its matched baseline is about 2.66e-8, with a scaled Gram condition near 5.36e7. It is not interval-certified. The new span does not contain the historical 48-feature span and performs worse than that historical value. The deficit to the required zero margin is still about 0.01465.

All coefficients and full M/G matrices are retained. The frozen rational vector is provably nonzero and has positive limiting mass independently of the numerical Gram matrix. A single actual-integer operator evaluation at L=100000, retaining every prime-power entry, has margin -0.0374094621535042. Exact finite checks include 12 unordered decompositions, 132 coprime insertion triples and 108 count-state identities. These are checks of this fixed trial, not a global obstruction to resonance and not actual zeta-zero observations.

## 4. Prime powers can be removed at both relevant scales

The [prime-power estimate](../dyson/round9/prime-power-removal/PRIME_POWER_TAIL_ESTIMATE.md) is an elementary infinite-tail argument, accepted in an [independent proof review](../dyson/round9/prime-power-removal/INDEPENDENT_REVIEW.md). It is a nuisance-term bound, without a novelty claim.

Let delta=c/log T, sigma=1/2+delta, N=floor(T/log^6 T), R_c=-zeta'/zeta(s)-sum_(n<=N) Lambda(n)n^(-s), and

\[
U_{c,N}(t)=\sum_{\substack{p\ \mathrm{prime},\ k\ge2\\p^k>N}}
(\log p)p^{-k\sigma-ikt\log p}.
\]

Uniformly for 0<delta<=1/4 and N>=4, without RH,

\[
\|U_{c,N}\|_2^2\ll TN^{-1/3}\log^4(2N)+\delta^{-4}.
\tag{3}
\]

Squares are treated by a convergent diagonal/off-diagonal mean-square expansion; the near-pair harmonic sum gives delta^(-4). Higher powers admit a sufficient absolute tail bound using their sparse counting function. No infinite polynomial theorem with a divergent remainder is invoked.

Under RH, replacing R_c by R_c-U_(c,N) changes its normalized energy by O(a_T), where

\[
a_T=N^{-1/6}\log^2(2N)+T^{-1/2}\log^2T=o(1).
\]

The bound is uniform for 1<=c<=log T/4, and holds with a c-dependent constant for each fixed c>0. The remaining continuation uses exactly the genuine-prime error theta(x)-x, including its endpoint and pole term. This removes prime powers from the open arithmetic comparison; it does not improve its limiting constant.

## 5. The mesoscopic target is a first correction, not merely a leading law

Set b=2c and r_T(b)=||R_(b/2)||²/(T log²T). A sufficient two-width asymptotic is

\[
r_T(b)=\frac{e^{-b}}b+o\left(\frac{e^{-b}}{b^2}\right)
\tag{4}
\]

uniformly on a suitable slowly growing range, including the second width. Relative o(1) is insufficient: the distinguishing signal requires relative o(1/b).

The [source and rate audit](../dyson/round9/mesoscopic-edge/EDGE_RATE_AUDIT.md) checks Theorem 5, Lemma 16 and Section 4.2 of [Carneiro–Chandee–Chirre–Milinovich, *On Montgomery's pair correlation conjecture: a tale of three integrals*](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf). Its proof-level finite-T errors can fit below the signal on a sufficiently slow diagonal. Thus a blanket claim that those errors always swamp the signal would be wrong.

The real obstruction is the limiting lower bound: its deficit from sine is of order e^(-b)/b, while sine minus ACUE is of order e^(-b)/b². The known lower bound therefore misses the required correction by a factor of order b, even when its height error is negligible. The upper deficit is larger by order b².

To remove the general AH near-diagonal nuisance, define

\[
\mathcal C_T(b)=b^2\left[
2\sinh b\,r_T(b)-2\sinh(2b)\,r_T(2b)-\frac1{2b}\right].
\]

The sine prediction tends to zero; the AH prediction tends to -3/4. The nuisance cancels exactly. The reviewed sufficient arithmetic target is: find increasing G(T) tending to infinity with G(T)=o(log log T) such that

\[
\lim_{B\to\infty}\liminf_{T\to\infty}
\inf_{B\le b\le G(T)}\mathcal C_T(b)>-\frac34.
\tag{5}
\]

Fixed-width AH convergence permits an existential stepwise slow diagonal inside this envelope, giving a contradiction if (5) were proved. It does not justify choosing a prescribed rate such as sqrt(log log T). The [independent review](../dyson/round9/mesoscopic-edge/INDEPENDENT_EDGE_REVIEW.md) states these quantifiers explicitly.

The prime-power replacement from (3) remains negligible even after the amplification: its effect on C_T is O(b² e^(2b) a_T)=o(1), uniformly for 2<=b<=G(T)=o(log log T). Thus (5) can be pursued using genuine primes. No estimate (4) or (5) is established here.

## 6. Reproducibility, record ownership and next decision

All 28 source files, totaling 1,174,410 bytes, are retained verbatim in the adjacent local `Astra-Local-Archive/round9-originals/`. The public folder retains 26 files; the two omitted third-party PDF/text bodies remain local with URL and SHA256 receipts. The existing 186 primary PDF/text are separately retained under `round9-external-sources/`. No author files were edited for publication. Historical “review pending” labels are superseded by the separately hashed later reviews and the current claim ledger.

The [intake manifest](../dyson/round9/INTAKE_MANIFEST.json) records every original. The [bounded integration replay](../logs/round9-integration/recheck.py) parses the four scripts, runs one fresh order-32 calculation and the three check scripts in a temporary copy, compares five JSON outputs, and compares the full recomputed M/G arrays. Timing and temporary source-file paths are the only excluded metadata; the order-20 matrices are checked as saved evidence, not advertised as newly recomputed.

Run from the repository root with Python, NumPy and SciPy:

```text
python3 research/logs/round9-integration/recheck.py --prime-gap-source-dir /path/to/retained/round9-external-sources
python3 tools/verify_manifest.py
```

The replayer sets the portable Round 7 dependency path explicitly, verifies its pinned hash, and stages the primary references at the unmodified author's expected relative location. The primary references are inputs to provenance checking; finite arithmetic identities do not constitute a proof of their analytic theorem. Original evidence is unchanged by replay.

The next bounded task is to estimate the actual sum across shifts, testing smooth completion before paying the full H loss. A second lane checks whether known prime short-interval mean squares control the required signed residual correction at sufficient precision. Independent agents challenge the arithmetic hypotheses and normalization. These tasks remain in progress and are not part of this checkpoint's accepted claims.

Postponed: further scans of the failed feature, generic positivity countermodels already covered by Round 8, prime-gap coefficient sweeps, new Fable sessions, and another large PDF rebuild for a negative diagnostic. The 333-page public handoff, 381-page local handoff and 59-page supplement keep their explicit earlier checkpoints. Reverting this research commit removes the new slice without rewriting prior results. The open arithmetic inequalities, rather than the volume of documentation, determine whether the programme advances toward a famous conjecture.
