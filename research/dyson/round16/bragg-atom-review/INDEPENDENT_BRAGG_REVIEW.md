# Independent audit of the R16 forced Bragg-atom target

Date: 2026-09-05. Reviewer: Aquinas (`/root/yau_flow`). Status: **accepted as an ordinary mathematical proof, source comparison, and bounded normalization check**. This is neither a formal proof-assistant verification nor a proof of either proposed strict actual-zeta inequality.

Reviewed author file: `research-round16/bragg-atom/BRAGG_ATOM_TARGET.md`, SHA-256
`2228bfd90e7a633683936d3d611f31c1f960107fbdf111a494993f73be16e120`.
The author text and evidence were preserved unchanged. This audit covers the complete mathematical note, the relevant primary-source statements, and an independent replay of the unchanged check script. No zero-data experiment or parameter scan was performed.

## 1. Verdict and exact claim boundary

I found no mathematical gap requiring a correction in the frozen report. The conclusions accepted here are:

1. For the specified normalized autocorrelation bump, the exact actual-zero comparison is
   \[
   0\le C_{\varepsilon,T}(b)\le C_{\varepsilon,T}(0),
   \qquad C_{\varepsilon,T}(0)\longrightarrow1+\varepsilon^2m_1
   \]
   under RH, with fixed \(0<\varepsilon<1\).
2. The nonnegative deficit at frequency two is exactly
   \[
   D_{\varepsilon,T}
   =\varepsilon\int\widehat\psi(\varepsilon u)
     (1-\cos4\pi u)\,d\mu_T(u).
   \]
   Every positive spectral subsequential limit has atoms of mass at most one. This allows, rather than excludes, a unit atom.
3. RH together with the particular GLSS-II **AH-Pairs** hypothesis forces
   \(C_{\varepsilon,T}(2)\to1+\varepsilon^2m_1\) and
   \(D_{\varepsilon,T}\to0\), without requiring a limit or specified value of the near-zero parameter \(p_0\).
4. Goldston's centered explicit formula gives the stated actual arithmetic representation uniformly on the full fixed power interval \(x=T^\alpha\), \(2-\varepsilon\le\alpha\le2+\varepsilon\). The full von Mangoldt signal, continuous mean, and signed cross terms are retained.
5. Neither the current positive-pair bound nor the cited finite- or long-interval theorems give the strict deficit needed to exclude AH-Pairs. The report accurately identifies that missing arithmetic estimate.

As usual all assertions involving \(N_T=T\log T/(2\pi)\) are understood for \(T>1\), and asymptotic assertions for \(T\to\infty\). The phrase “every T” in Proposition 1 uses this natural domain. It is not a claim at the undefined normalization \(T=1\).

## 2. Positivity, normalization, and atom capacity

I checked the two distinct positivity arguments. The finite pair measure \(\mu_T\) is positive and even. That alone does not make its Fourier transform nonnegative. Nonnegativity of \(F_T\) additionally follows from the nonnegative Fourier transform of \(4/(4+t^2)\), equivalently its positive-definite quadratic-form representation. This extra fact is correctly stated in the author report.

For the fixed flat seed \(f\), its zero extension is smooth. Its normalized autocorrelation satisfies
\[
\psi(0)=1,\quad 0\le\psi\le1,\quad
\operatorname{supp}\psi=[-1,1],\quad
\widehat\psi(u)=|\widehat f(u)|^2/\|f\|_2^2\ge0.
\]
The identity \(m_0=(\int f)^2/\int f^2\), strict Cauchy–Schwarz on an interval of length one, and positivity away from its endpoints give \(0<m_1<m_0<1\).

Fourier scaling supplies exactly one factor \(\varepsilon\):
\[
\int\psi((\alpha-b)/\varepsilon)e^{2\pi i\alpha u}d\alpha
=\varepsilon e^{2\pi ibu}\widehat\psi(\varepsilon u).
\]
There is no \(\varepsilon^{-1}\) in the definition of the bump. Evenness converts the exponential to a cosine. The upper comparison follows termwise from \(\cos\le1\), and the lower bound follows from \(F_T\ge0\), not from the cosine expression. Subtracting the two finite sums proves the exact deficit identity without an interchange of infinite limits.

Montgomery's low-band limit has the distributional mass \(\delta_0+|\alpha|d\alpha\). The atom contributes the bump height one, while the density contributes \(\varepsilon^2m_1\). In particular, the approximate identity \(\log T\,T^{-2|\alpha|}\) has total mass one in the limit. This checks the constant in the RH upper bound and the distinction between a unit atom and a unit density.

The atom-capacity proof is also sound. The fixed translated-bump comparison yields uniform local mass bounds on the positive measures \(F_T(\alpha)d\alpha\), by a finite covering with regions on which a translated bump has a positive lower bound. Vague subsequences therefore exist. For any such limit \(\nu\), fixed \(b\), and fixed \(\varepsilon\),
\[
\nu(\{b\})\le\int\psi((\alpha-b)/\varepsilon)d\nu
\le1+\varepsilon^2m_1.
\]
Sending \(\varepsilon\downarrow0\) only after passing to that limit proves \(\nu(\{b\})\le1\). No assertion of atom absence follows.

## 3. AH passage: early zeros, tails, and the near-zero sector

I checked the use of GLSS-II equations (1.9) and (1.12), rather than replacing their AH-Pairs hypothesis by a stronger minimum-gap statement. The hypothesis applies to late zeros and fixed normalized compact intervals, permits multiplicity and clustering near zero, and supplies half-lattice proximity with a vanishing error. On a fixed compact interval the relevant half-lattice indices are bounded for large T, so their limiting support is indeed contained in \(\tfrac12\mathbb Z\).

The tail argument does not assume an all-radius bound absent from the source. For \(R\le T\), the cited estimate gives \(\mu_T([-R,R])\ll1+R\). For larger radii, the elementary bound
\[
\mu_T(\mathbb R)\le N(T)^2/N_T\ll T\log T
\]
is enough. A test bounded by \(C(1+u^2)^{-1}\) therefore has tails, outside a fixed large radius R, bounded by
\[
O(1/R)+O(\log T/T).
\]
The first term is the sum of dyadic shells up to scale T; the second uses the total mass beyond T. This justifies passage from compact vague convergence to tempered-distribution convergence for the Schwartz Fourier tests in use.

There are \(O(T/\log T)\) zeros below \(T/\log^2T\), and only \(O(\log T)\) potential partners per such zero in a fixed normalized interval, using the unit-interval zero bound. After division by \(N_T\), their local contribution is \(O(1/\log T)\). The same positive-measure tail domination removes their Schwartz contribution. The factor \(w(u/L)\) tends to one uniformly on fixed normalized compacts. Thus the early-zero exclusion in AH-Pairs has not been ignored.

For a limiting pair measure \(\mu\) supported on \(\tfrac12\mathbb Z\), multiplication by \(e^{4\pi iu}\) fixes \(\mu\), so its Fourier transform is 2-periodic as a tempered distribution. Montgomery's theorem fixes this transform on \((-1,1)\), and translation fixes it on \((1,3)\) as
\[
\delta_2+|\alpha-2|d\alpha.
\]
The test centered at two has compact support strictly inside this interval because \(\varepsilon<1\). Any possible boundary atoms at frequencies one and three are excluded by its support. Consequently no value or convergent choice of \(p_0\) is needed. The same test value holds for every subsequential limit; the standard subsequence argument yields the full-sequence limit claimed in the report.

I also checked the geometric interpretation. A fixed positive lower deficit can first be localized to a compact set using the tail bound. In a narrow half-lattice neighborhood, \(1-\cos4\pi u\ll\operatorname{dist}(u,\tfrac12\mathbb Z)^2\), while compact pair mass and the Fourier weight are bounded. The remaining positive deficit therefore forces a positive normalized **pair** mass outside a fixed half-lattice neighborhood. This does not prove a statement about consecutive gaps. The report correctly notes that the converse needs a positive lower bound for the Fourier weight on the chosen set; its zeros cannot be discarded.

All these passages fix \(\varepsilon\) before \(T\to\infty\). They do not license replacing it by an arbitrarily prescribed shrinking function \(\varepsilon(T)\).

## 4. Primary finite-window and long-average bounds

I read the relevant retained primary texts and visually inspected printed page 11 of the [CCCC author-hosted PDF](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf). The rendered page is saved as `cccc-primary-page11.png` beside this review.

Theorem 9 assumes RH, \(b\ge1\), and fixed \(\ell>0\). Its first upper candidate for \(0<\ell\le1\) is exactly the expression used by the author. At \(\ell=1/4\), the positive-part input \(1-\ell-\ell^2=11/16\) is positive, and direct rational substitution gives
\[
\frac43\frac54+\frac1{768}-\frac1{12}-\frac{11}{64}
=\frac{1085}{768}.
\]
Since the theorem takes a minimum of two upper candidates, using either one is a valid upper bound. No claim that this is an optimized value is necessary. Equation (2.27) and its immediately following discussion explicitly retain a limiting small-window cost of one and the possibility of delta spikes beyond support one. The report's tailored bump comparison is an application of the same positive-pair mechanism, not a new improvement of the optimized interval theorem.

The [CMR paper](https://arxiv.org/abs/2310.01913), Theorem 1 and Corollary 2, imposes a large-interval condition \(\ell\ge\ell_0\). Its constant 1.3208 cannot be multiplied by a fixed small interval length to bound the present bump. The author's separate normalization comparison is harmless because the source's \(N(T)\) and \(T\log T/(2\pi)\) have ratio tending to one. The cited GRH lower bound is in a different range and has the wrong direction for the proposed upper target. These restrictions are retained accurately.

## 5. Actual centered prime identity and all error terms

I independently checked [Goldston's primary notes](https://arxiv.org/abs/math/0412313), Proposition 1, equation (3.11), and equations (4.4)–(4.5). Proposition 1 states \(x\ge1\); there is no \(x\le T\) condition on this explicit formula. Its error has the stated form
\[
E_x(t)\ll x^{-1/2}\log(t+2)+x^{-2}/(t+2),\qquad 0\le t\le T.
\]
The sign convention \(P_x=Z_x+E_x\) is correct. Integrating the low and high parts of \(a_u(x)\) separately gives the exact continuous mean
\[
M_x(t)=x^{1-it}\left(\frac1{3/2-it}+\frac1{1/2+it}\right)
=\frac{2x^{1-it}}{(1/2+it)(3/2-it)}.
\]
The lower endpoint is zero, not one; the author does not silently discard that part of the continuous density.

For completeness, the norm comparison in the author proof has explicit bounds
\[
\|Z_x\|_2\ll \sqrt{xT}\log T,
\qquad
\|E_x\|_2\ll x^{-1/2}\sqrt T\log T+x^{-2}.
\]
The normalized main cross error is \(O(\log T/x)\). The cross term involving \(x^{-2}\) is \(O(x^{-5/2}T^{-1/2})\), dominated by the claimed error for large T and \(x\ge1\). The squared-error terms are bounded by \(O(\log T/x^2+x^{-5}/(T\log T))\), also covered. Goldston's all-zero/truncated-zero comparison contributes \(O(x\log^3T)\) before normalization, hence \(O(\log^2T/T)\) afterwards. Its x-uniformity follows from \(|x^{i\gamma}|=1\) under RH in the endpoint estimates. No omitted restriction prevents the fixed range \(\alpha\in[2-\varepsilon,2+\varepsilon]\).

Expanding the centered square yields the real symmetric kernel in equation (20). The integral of the real part of \(e^{-it\log(u/v)}\) over \([0,T]\) is exactly \(\sin(T\log(u/v))/\log(u/v)\), with diagonal value T. There is no missing factor two: the factor two appears only when the off-diagonal atomic pairs are written as \(m<n\). Weighted total variation of \(d\Psi-du\) is finite for fixed T and the compact alpha range, because the upper weight decays as \(u^{-3/2}\). This supplies the Fubini justification even before cancellation. All von Mangoldt prime powers, both mixed mean terms, and the continuous-continuous term remain present.

Partial summation of \(\sum_{n\le y}\Lambda(n)^2\sim y\log y\) gives
\[
\sum_n\Lambda(n)^2a_n(x)^2\sim x\log x.
\]
The two leading integrals contribute one half each. Uniformity over the entire power interval follows as its lower endpoint tends to infinity. The alpha diagonal is therefore \(2\varepsilon m_0\), not \(\varepsilon m_0\). Combining it with the centered cross terms gives exactly the conservative obligation
\[
\limsup E_{\varepsilon,T}<1-2\varepsilon m_0.
\]
This is an unproved upper bound on the full centered arithmetic expression, not a consequence of positivity of its uncentered terms.

The audit also confirms the stated scale obstruction. At \(\varepsilon=1/4\), the power interval is \([7/4,9/4]\), and \(h\asymp x/T\) has x-exponents \([3/7,5/9]\). The older R9 nuisance bound relative to \(x\log x\) has power \(x^{1/2-1/\alpha}\), which is zero at \(\alpha=2\) before its logarithmic loss and positive above two. This is failure of that available error estimate to prove negligibility, not a lower bound for the actual error. The report keeps this distinction and does not import the previous smaller-alpha wrappers.

## 6. Independent bounded replay and evidence

I read the complete check script before executing an unchanged copy in this review's `replay/` directory. It writes its JSON beside itself, so copying prevented any mutation of the frozen author outputs. Runtime: Python 3.14.3, NumPy 2.4.4, SymPy 1.14.0.

The replay passed and both resulting files are byte-identical to the author outputs:

- `replay/bragg_checks.json`: SHA-256 `4292d35122c0205c68031a44da8c8ad74ac271a4c8c5297a9131d443d7d45218`.
- `replay/bragg_checks.log`: SHA-256 `887adbdc289a9a8b559d9def80466a53295aac737e4ed46d81fbcfd2be1d3e63`.
- Unchanged replay script: SHA-256 `4bb27d8f3dae2eca51d9c6d9b7e17ff43f4d6101ee4fd8ae93c5afae5010bb13`.

Exact checks cover the rational CCCC candidate, shift/error exponents, a separate polynomial-seed autocorrelation identity, the diagonal leading weight, the continuous-mean denominator identity, and half-lattice cosine values. The polynomial seed is explicitly not substituted for the smooth theorem seed.

Floating checks at quadrature orders 64, 128, and 192 give \(m_0\approx0.7406125730612092\), \(m_1\approx0.16940474262803504\), and compare the two Fourier expressions on a finite synthetic configuration. Their largest final refinement change is about \(9.99\times10^{-16}\). This is a numerical diagnostic, not an interval enclosure, not actual zeta data, and not a test of the proposed strict target.

I independently verified all five entries in `AUTHOR_RECEIPT.json` and all eleven retained primary/dependency entries in `SOURCE_RECEIPT.json`, including byte counts and SHA-256 digests. The complete check is preserved in `independent_input_hash_check.json`. The audit receipt pins this review, the unchanged input report, primary source receipt, replay files, and the inspected primary-page rendering.

**Remaining mathematical work:** establish a strict actual-zeta deficit for one fixed epsilon, or the equivalent centered arithmetic bound stated above. No such estimate is obtained by this audit or by the frozen author note. General novelty, full pair correlation, a shrinking-band limit, transfer to the earlier two-scale resolvent target, and conclusions about consecutive zero gaps remain outside the accepted result.
