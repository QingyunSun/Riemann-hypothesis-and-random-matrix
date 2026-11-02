# What the positive length average retains: a fixed-bump Tauberian equivalence

Date: 2026-09-05. Status: ordinary proof under RH, submitted for independent review. This is an application of Wiener's classical translation-density theorem to the two independently reviewed Round 20 identities. It is not a new Montgomery theorem, a proof of a positive Bragg deficit, or a quantitatively stable inversion procedure. No novelty claim is made.

## 1. One fixed observable, with all quantifiers retained

Fix exactly the Round 16 bump, with \(\varepsilon=1/4\),
\[
\omega(\alpha)=\psi((\alpha-2)/\varepsilon),\quad
C_T=\int\omega(\alpha)F_T(\alpha)d\alpha,\quad
A=1+\varepsilon^2m_1.
\tag{1}
\]
The form factor, the exact normalization \(T\log T/(2\pi)\), the Lorentzian pair weight and multiplicities are those in the frozen R16/R20 reports. Define
\[
D_T=C_{\varepsilon,T}(0)-C_T\ge0,
\qquad C_{\varepsilon,T}(0)\longrightarrow A.
\tag{2}
\]
Use the actual, exactly centered, all-length prime variance from Round 20:
\[
\overline V_T=\frac{T}{\log^2T}\int_0^\infty e^{-\lambda}
\int_1^\infty
\left[\Psi(e^{\lambda/T}x)-\Psi(x)-(e^{\lambda/T}-1)x\right]^2
\omega\!\left(\frac{\log x}{\log T}\right)\frac{dx}{x^2}\,d\lambda.
\tag{3}
\]
Here \(\Psi=\sum_{n\le x}\Lambda(n)\) includes every prime power. All endpoint conventions, length tails and weight localizations are supplied by the pinned Round 20 proof; none are changed in this note.

**Theorem.** Assume RH. For every real constant \(c\),
\[
\boxed{\overline V_T\longrightarrow c
\quad\Longleftrightarrow\quad C_T\longrightarrow c
\quad\Longleftrightarrow\quad D_T\longrightarrow A-c,
\qquad T\to\infty.}
\tag{4}
\]
If these limits exist, \(0\le c\le A\). The assertion concerns full convergence through real heights, not convergence along one chosen subsequence. It asserts equivalence for this one fixed test and does not assert that any of these limits exists.

## 2. Precisely which Round 20 inputs enter

The all-length prime/zero comparison proved in Round 20 is
\[
\overline V_T=\int_0^\infty p(y)C_{Ty}dy+o(1),
\qquad p(y)=\frac4\pi\frac{y^2}{(1+y^2)^2},\quad \int_0^\infty p=1.
\tag{5}
\]
Values of \(C_U\) below \(U=2\) can be assigned any bounded extension. Such choices contribute \(o(1)\). This is a comparison for one actual finite-\(T\) statistic; it is not a formal interchange of unproved prime sums.

The independently proved multiplicative-height estimate is
\[
|D_{Ty}-D_T|\le2A\frac{|y-1|}{\max(1,y)}+o(1),
\qquad 1/2\le y\le2,
\tag{6}
\]
with an error uniform in \(y\). Its proof uses only RH low-band data, positivity and a global Schwartz pair envelope. It does not assume AH, simplicity or conjectural high-frequency correlation.

Set \(f(x)=C_{e^x}\) for \(x\ge\log2\), and set \(f(x)=0\) below that point. The actual finite sums are measurable, bounded on compact height intervals, and ultimately bounded by \(A+o(1)\). Thus \(f\in L^\infty(\mathbb R)\), with a specified pointwise representative.

Using (2) and (6), for every fixed \(0<\delta\le\log2\),
\[
\limsup_{x\to\infty}\sup_{|h|\le\delta}
|f(x+h)-f(x)|
\le2A(1-e^{-\delta}).
\tag{7}
\]
Indeed \(y=e^h\) gives \(|y-1|/\max(1,y)=1-e^{-|h|}\), while the difference of the two \(C_0\) terms tends to zero uniformly on this compact height-ratio range. In particular
\[
\lim_{\delta\downarrow0}\limsup_{x\to\infty}
\sup_{|h|\le\delta}|f(x+h)-f(x)|=0.
\tag{8}
\]
This is asymptotic uniform continuity. Literal continuity across every finite zero-height jump is neither asserted nor needed.

Changing variables \(y=e^u\) in (5) gives
\[
q(u)=p(e^u)e^u=\frac4\pi\frac{e^{3u}}{(1+e^{2u})^2},
\qquad
\overline V_{e^x}=\int_{\mathbb R}q(u)f(x+u)du+o(1).
\tag{9}
\]
For standard convolution \((K*f)(x)=\int K(u)f(x-u)du\), take
\(K(u)=q(-u)\). Both \(q\) and \(K\) are positive integrable functions of total mass one.

## 3. Exact transform, including the reflection convention

For this section use the angular Fourier convention
\(\widehat K(\tau)=\int K(u)e^{-i\tau u}du\). This differs from the \(2\pi\) convention used to define the spectral bump, and the change is intentional.

For every real \(\tau\),
\[
\begin{aligned}
\widehat K(\tau)
&=\int_{\mathbb R}q(u)e^{i\tau u}du
=\int_0^\infty p(y)y^{i\tau}dy\\
&=\frac2\pi\int_0^\infty
\frac{t^{(1+i\tau)/2}}{(1+t)^2}dt\\
&=\frac2\pi\Gamma\!\left(\frac{3+i\tau}{2}\right)
\Gamma\!\left(\frac{1-i\tau}{2}\right)
=\boxed{\frac{1+i\tau}{\cosh(\pi\tau/2)}}.
\end{aligned}
\tag{10}
\]
The substitution in the second line is \(t=y^2\). The beta integral is absolutely convergent: its two parameters have real parts \(3/2\) and \(1/2\). Gamma recurrence followed by reflection at \(z=(1+i\tau)/2\) proves the last step. Those two standard formulas are NIST DLMF equations 5.5.1 and 5.5.3.

The transform of \(q\) with the negative-sign convention would instead be
\((1-i\tau)/\cosh(\pi\tau/2)\). The plus sign in (10) is correct for the reflected kernel \(K\) required by (9).

In particular,
\[
\widehat K(0)=1,\qquad
|\widehat K(\tau)|^2=\frac{1+\tau^2}{\cosh^2(\pi\tau/2)}>0
\quad(\tau\in\mathbb R).
\tag{11}
\]
There is no real Fourier zero.

## 4. The exact classical theorem and the needed corollary

The external theorem used is **Theorem 1, p.2 of the author-hosted preprint** J.M.A.M. van Neerven, *Elementary operator-theoretic proof of Wiener's Tauberian theorem*, corresponding to the paper published in *Rendic. Istit. Matem. Univ. Trieste*, Suppl. XXVIII (1997), 281–286. The author's publication page identifies downloadable files as preprints. The four-page preprint, its extracted text and a rendered image of its Theorem 1 are retained and hash-pinned in the source receipt; the theorem was visually checked.

The precise translation-density statement we use is: if \(K\in L^1(\mathbb R)\) and \(\widehat K(\tau)\ne0\) for every real \(\tau\), then, for every \(g\in L^1(\mathbb R)\) and every \(\eta>0\), there are finitely many coefficients \(a_j\in\mathbb C\) and shifts \(t_j\in\mathbb R\) such that
\[
\left\|g-\sum_{j=1}^m a_jK(\,\cdot-t_j)\right\|_1<\eta.
\tag{12}
\]
The theorem concerns \(L^1\)-norm density. It gives no uniform bound here on \(m\), the shifts or the sum of coefficient magnitudes as \(\eta\) varies.

We spell out its application to bounded functions rather than importing an unspecified version of a Tauberian theorem.

**Lemma.** Suppose \(K\in L^1(\mathbb R)\), \(\int K=1\), its Fourier transform has no real zero, and \(f\) is a bounded measurable function satisfying (8). Then, for any \(c\in\mathbb C\),
\[
(K*f)(x)\to c\quad(x\to\infty)
\quad\Longleftrightarrow\quad f(x)\to c.
\tag{13}
\]
The condition (8) concerns the specified pointwise representative of \(f\).

**Proof of the Tauberian direction.** Suppose \(K*f\to c\). For every fixed shift \(t_j\),
\[
\bigl(K(\,\cdot-t_j)*f\bigr)(x)=(K*f)(x-t_j)\to c.
\]
Thus a finite combination \(h=\sum_j a_jK(\,\cdot-t_j)\) satisfies
\((h*f)(x)\to c\sum_j a_j=c\int h\).
For an arbitrary fixed \(g\in L^1\), choose \(h\) using (12). If \(M=\|f\|_\infty\), then
\[
\limsup_{x\to\infty}|(g*f)(x)-c\int g|
\le(M+|c|)\|g-h\|_1<(M+|c|)\eta.
\tag{14}
\]
Send \(\eta\downarrow0\). We have proved
\((g*f)(x)\to c\int g\) for every fixed \(g\in L^1\).

Now take the fixed probability kernel
\(g_\delta(u)=(2\delta)^{-1}1_{[-\delta,\delta]}(u)\). Its convolution tends to \(c\), while
\[
|(g_\delta*f)(x)-f(x)|
\le\sup_{|h|\le\delta}|f(x+h)-f(x)|.
\tag{15}
\]
First send \(x\to\infty\) at fixed \(\delta\), then send \(\delta\downarrow0\) using (8). This proves \(f(x)\to c\), including the actual pointwise values at zero-height jumps.

**Proof of the Abelian direction.** If \(f(x)\to c\) and \(f\) is bounded, dominated convergence in the fixed \(L^1\) kernel gives \(K*f\to c\int K=c\). ∎

No differentiability, integrability of \(f\), pointwise Fourier transform of \(f\), or formal division of a distribution by an exponentially growing function occurs in this proof.

## 5. Application and the limits it does not supply

For the actual zeta function under RH, Sections 2–3 verify every hypothesis of the lemma. The frozen Round 20 error in (9) tends to zero; therefore \(\overline V_{e^x}\to c\) is equivalent to \(K*f\to c\), hence to \(f\to c\). This gives the first equivalence in (4). Equation (2) gives the second. The bounds \(0\le C_T\le A+o(1)\) imply \(0\le c\le A\).

All limits used in this deduction are full limits. Convergence of \(\overline V_T\) on an arbitrary subsequence does not give convergence of \(C_T\) on that subsequence: the Wiener step needs convergence of every fixed translate \((K*f)(x-t_j)\). Round 20's separate quantitative strict-subsequence comparison remains useful for that different question.

The result says that the selected smoothing does not hide failure of **full scalar convergence**, once the proved RH height regularity is used. It does not produce that convergence. In particular:

- AH-Pairs implies \(C_T\to A\), hence \(\overline V_T\to A\), as already known from Round 20. The converse implication to AH-Pairs is not claimed; convergence to one scalar value does not determine the whole pair measure.
- If a new arithmetic argument proves \(\overline V_T\to c<A\), the theorem yields \(C_T\to c\) and a positive limiting Bragg deficit, excluding AH-Pairs. No such arithmetic argument is supplied here.
- The conjectural unit spectral density near frequency two would give \(c=\int\omega=\varepsilon m_0\). Proving that value for this one bump would establish one smoothed pair-correlation statement, not the complete Montgomery conjecture for all tests.

The main missing result remains an actual arithmetic estimate establishing a strict deficit or an appropriate limit for (3). Positivity, boundedness and the nonvanishing multiplier do not establish either one.

## 6. Why this is qualitative, not a stable deconvolution

The multiplier has magnitude
\[
|\widehat K(\tau)|=\frac{\sqrt{1+\tau^2}}{\cosh(\pi\tau/2)}
\sim2|\tau|e^{-\pi|\tau|/2}\quad(|\tau|\to\infty).
\tag{16}
\]
Formal inverse multiplication therefore grows exponentially. There is no bound
\(\|f\|_\infty\le B\|K*f\|_\infty\) with one fixed \(B\) for all bounded continuous functions: testing the exact wave \(f(x)=e^{i\tau x}\) gives the ratio \(1/|\widehat K(\tau)|\to\infty\). Even restricting to a fixed Lipschitz bound does not produce such a linear norm inequality, since the rescaled waves \(\tau^{-1}e^{i\tau x}\), \(\tau\ge1\), have Lipschitz constant one and the same ratio.

This is an operator diagnostic, not a constructed zeta point process. It rules out the stated uniform linear stability inequality; it does not rule out every possible nonlinear conditional modulus under additional restrictions. Neither the density theorem (12) nor the unspecified arithmetic \(o(1)\) in Round 20 supplies a convergence rate here. The proof keeps the order: fixed approximation kernel and approximation accuracy, then height to infinity, then accuracy/width to zero.

## 7. Relation to classical Goldston–Montgomery equivalences

CCCC's introduction, equations (I)–(IV), recalls the classical RH equivalences between the full pair-correlation conjecture, asymptotics over every fixed spectral interval beyond one, the family of Selberg variances, and the family of logarithmic-derivative moments. The present calculation uses the same classical Tauberian principle on a particular positive smoothing.

Our conclusion has narrower quantifiers: one fixed R16 bump and one corresponding length-averaged variance, with an arbitrary potential scalar limit \(c\). It does not strengthen those classical conjecture equivalences into a proof of their asymptotics. No extension to all fixed real compact frequency tests is asserted in this note; such an extension would require checking the appropriate regularity and signed-weight transfer hypotheses separately.

The practical value is to identify what an arithmetic proof for this positive smoothed statistic would recover without another conjectural regularity input. It does not remove the need for that arithmetic proof, and it does not justify numerically undoing the smoothing.

## Sources and bounded verification

- [Van Neerven, author-hosted preprint, Theorem 1 p.2](https://fa.ewi.tudelft.nl/~neerven/publications/papers/RIMUT_97.pdf). The [author's publication list](https://fa.ewi.tudelft.nl/~neerven/publications.htm) identifies the corresponding 1997 publication and the preprint status of downloads. The exact source version, text and theorem-page image are pinned locally.
- [NIST DLMF gamma recurrence](https://dlmf.nist.gov/5.5.E1) and [reflection](https://dlmf.nist.gov/5.5.E3), used only in the explicit Mellin-transform calculation.
- [CCCC primary paper](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), introduction (I)–(IV), for the scope of the classical equivalences; the retained primary source is pinned.
- [Round 20 all-length identity](../../research-round20/length-averaged-variance/EXPONENTIAL_LENGTH_AVERAGE.md), SHA256 `cd8c2f7dc48530ed02f915dd202c8aedaaaadb1096cafc019beeb595b9beebbe`.
- [Round 20 height regularity](../../research-round20/height-regularity/MULTIPLICATIVE_HEIGHT_EQUICONTINUITY.md), SHA256 `6048b8792084d1523212ddd5f0c05dcc5b54fb158c3dab37762675e91a1072fe`.

The adjacent checker performs only exact transform-algebra and normalization checks. It does not verify Wiener's theorem, the analytic limit passage, a numerical inverse, or any positive zeta deficit. No parameter scan is used.
