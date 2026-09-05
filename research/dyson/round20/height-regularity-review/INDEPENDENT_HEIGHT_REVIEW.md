# Independent audit of the R20 multiplicative-height lemma

Date: 2026-09-05. Reviewer: Aquinas. Verdict: **accepted as an ordinary proof under RH**, at the exact author version below. No mathematical amendment is requested.

Reviewed in full: `../height-regularity/MULTIPLICATIVE_HEIGHT_EQUICONTINUITY.md`, 10,461 bytes, SHA256
`6048b8792084d1523212ddd5f0c05dcc5b54fb158c3dab37762675e91a1072fe`.

The accepted result is
\[
|D_{Ty}-D_T|\le
2A\frac{|y-1|}{\max(1,y)}+o(1),\qquad 1/2\le y\le2,
\]
with a uniform error. It is a regularity statement for the actual zeta pair statistic. It neither asserts that its upper subsequential deficit is positive nor refutes AH.

## 1. Exact normalization, kernel inequalities and source scope

I independently checked that the denominator is exactly
\(N_S=S\log S/(2\pi)\). It is not silently replaced by the number of zeros below \(S\). The two cutoffs include all positive ordinates up to the given real height, with multiplicity. The physical Lorentzian factor \(4/(4+(\gamma-\gamma')^2)\) remains fixed when the logarithmic scale changes. That last fact is essential to the positive-prefix comparison later in the proof.

For \(\phi_0=\varepsilon\widehat\psi(\varepsilon\,\cdot)\), the spatial inequality
\(0\le\phi_D\le2\phi_0\) is immediate from the cosine factor. The sharper inequality for the whole statistic, \(0\le D_S\le C_0(S)\), additionally uses the nonnegative form factor and nonnegative frequency bump. It does not follow merely from positivity of the pair measure; the author correctly supplies the Fourier argument.

The input \(C_0(S)\to A=1+\varepsilon^2m_1\) is the established support-one Montgomery formula tested with this fixed bump. I checked its agreement with the R16 definition and the retained CCCC equations (1.5)–(1.6). The source and programme versions are hash-pinned below. This is a full large-real-height input, not an AH assumption or a conjectural correlation formula outside the known band. Endpoint heights and multiplicities have not been excluded.

## 2. The global Schwartz envelope is valid

I checked the Fourier transform of the three squared-sinc terms separately. The half-unit translations yield opposite phases whose half-weighted sum is \(\cos(\pi\alpha)\). Thus
\[
\widehat q(\alpha)=(1-|\alpha|)_+(1+\cos(\pi\alpha))
\]
is the correct nonnegative support-one transform.

For real \(u\), each squared denominator \(u^2,(u-1/2)^2,(u+1/2)^2\) is at most \(2(1+u^2)\). The two shifted numerators are \(\cos^2(\pi u)\), and their two half coefficients sum to one. Together with the unshifted \(\sin^2(\pi u)\), this proves the stated lower bound
\(q(u)\ge[2\pi^2(1+u^2)]^{-1}\). At the three removable singularities the inequalities follow by continuity; no division by zero is used.

The limiting pair mass is exactly \(7/3\): the approximate-identity contribution is \(\widehat q(0)=2\), the nonoscillatory integral is \(1/3\), and the cosine integral is zero under reflection \(\alpha\mapsto1-\alpha\). Consequently \(\mathcal M_S(q)\le3\) for every sufficiently large real \(S\), and a function bounded above by \(B/(1+u^2)\) has pair mass at most \(6\pi^2B\).

This bound controls the entire finite pair sum, including very distant normalized pairs. It does not use a global linear counting estimate beyond the range where one has been proved. I found no missing far-tail or early-zero removal in this step.

## 3. Changing scale and comparing both height directions

The seminorm
\(B_\phi=\sup_{u,\,1/2\le a\le2}(1+u^2)|u\phi'(au)|\)
is finite for a fixed Schwartz function. The mean-value theorem and the preceding positive envelope bound give the scale error with coefficient \(6\pi^2B_\phi|a-1|\). This applies also to the oscillatory deficit kernel: its derivative remains Schwartz because the cosine multiplier and its derivatives are bounded.

For \(U/T\in[1/2,2]\),
\(a=L_T/L_U\) differs from one by \(O(1/\log T)\), uniformly, and lies in the allowed scale interval for all sufficiently large \(T\). Hence the frozen-scale relation (13) has the claimed uniform error after division by \(N_U\). No pointwise bound for an individual zero cluster is required.

For \(T\le U\le2T\), I rederived the central algebra. Put
\(r=1-N_T/N_U\), and let \(X\) be the new frozen-scale deficit-pair mass divided by \(N_U\). Termwise positivity yields
\[
0\le X\le2Ar+4E(T)+O(1/\log T),
\]
while changing the denominator yields
\[
D_U-D_T=X-rD_T+O(1/\log T).
\]
The signs matter. Since \(0\le D_T\le A+E(T)\), the lower side is at worst \(-r(A+E(T))\), and the upper side is at most the displayed bound for \(X\). Taking the larger of these gives \(2Ar+4E(T)+O(1/\log T)\). Summing two unrelated absolute estimates would unnecessarily lose the factor claimed by the author; the written proof does not do that.

For \(U<T\), the valid argument is to repeat the same two-endpoint proof with the smaller cutoff first. Both endpoints remain in \([T/2,2T]\), so the same \(E(T)\) controls their errors. One should not mechanically replace the symbol \(T\) by \(U\) in the already defined supremum \(E(T)\), which would introduce an unnecessary larger interval. The author's instruction to interchange the endpoints and repeat the proof is sufficient and has the correct scope.

Finally, I checked both exact normalization ratios:
\[
1-\frac{N_T}{N_{Ty}}
=1-\frac1y+\frac{\log y}{y(\log T+\log y)}\quad(y\ge1),
\]
\[
1-\frac{N_{Ty}}{N_T}
=1-y-\frac{y\log y}{\log T}\quad(y\le1).
\]
Their errors are uniformly \(O(1/\log T)\). The denominator \(\max(1,y)\) in the theorem is therefore correct. The result is asymptotic equicontinuity, not continuity of a finite sum across its zero-height jumps.

## 4. Persistence and the combined quantitative equivalence

Let \(d=\limsup D_T\in[0,A]\). For \(d>0\), choose heights with \(D_{T_k}\to d\) and set \(r_d=d/(8A)\le1/8\). The uniform estimate gives
\(D_{T_ky}\ge3d/4-o(1)\) throughout \([1-r_d,1+r_d]\), hence the claimed eventual lower bound \(d/2\). A prescribed rate in \(T\) is not needed because \(d\), and therefore this interval, are fixed after choosing the subsequential value.

The combined consequence uses the separate frozen report
`../length-averaged-variance/EXPONENTIAL_LENGTH_AVERAGE.md`, SHA256
`cd8c2f7dc48530ed02f915dd202c8aedaaaadb1096cafc019beeb595b9beebbe`:
\[
A-\overline V_T=\int_0^\infty p(y)D_{Ty}dy+o(1),
\qquad p(y)=\frac4\pi\frac{y^2}{(1+y^2)^2}.
\]
I am the author of that separate report. This review is independent of Euclid's height proof; it is **not an independent review of my own length-average identity**. Acceptance of that dependency is recorded separately by the coordinator/root. I checked the logical and quantitative combination conditional on that pinned identity.

In particular, \(A-\liminf\overline V_T\) is the limsup of the nonnegative averaged deficit. The selected-height interval therefore gives the lower bound \((d/2)P(r_d)\). For the upper bound, at every sufficiently large physical height \(S\), \(D_S\le d+o(1)\). The exceptional bounded-height portion has \(p\)-mass tending to zero as \(T\to\infty\), since near zero \(p(y)=O(y^2)\). The statistic is bounded on every fixed finite height interval, and ultimately bounded by \(A+o(1)\). Thus the upper bound by \(d\) is justified without any selected-subsequence compatibility assumption.

I independently checked the antiderivative
\((2/\pi)(\arctan y-y/(1+y^2))\), its total mass one, and
\(p(y)\ge16/(25\pi)\) on \([1/2,2]\). Hence
\[
\frac d2P(r_d)\ge\frac d2\cdot2r_d\cdot\frac{16}{25\pi}
=\frac{2d^2}{25\pi A}.
\]
Both sides also hold at \(d=0\) by positivity and the upper bound. Therefore the combined comparison and strict-subsequence equivalence have the correct constants and directions. They assert neither side of the strict equivalence for actual zeta; no positive \(d\), AH refutation or Montgomery theorem is proved.

## 5. Reproduction, provenance and limitations

I read the complete exact checker before executing it. It contains finite symbolic identities and 3,159 rational prefix-algebra cases. I copied the unchanged script and frozen author report to a temporary directory within this review folder and ran the copy. The resulting JSON and stdout log are byte-for-byte identical to the frozen author evidence, SHA256
`5565948704e464041aa488cf37f06af4752df1d287fcc728ceeba8472d85fe2f`.

The adjacent `check_inputs_and_replay.py` and `input_and_replay_checks.json` retain that procedure. All eight entries in the author/source manifests match their declared hashes and lengths. The separate length-average report also matches the pinned hash. No author/source file was edited, no zero data were generated, and no parameter scan or Git operation was performed.

The checker verifies algebra, not the analytic uniformity statements. The ordinary proof review above checks those statements, their primary-input scope, and the combined dependence explicitly. No numerical gain enclosure or novelty claim is part of this acceptance.
