# Independent review of the actual log-prime heat representation

Date: 2026-09-05. Reviewer: Aquinas (`yau_flow`). Verdict: **accepted as an ordinary proof under RH**, with exactly the fixed-weight and asymptotic scope stated by the author. No correction to the frozen mathematical text is requested.

Reviewed author file: `../log-prime-heat/LOCALIZED_MELLIN_HEAT_ENERGY.md`, 10,290 bytes, SHA256 `1ee3d147669929f78a31e785d974eb851bf943453715c361e32ac2355407a1a8`. This review covers the entire proof, especially Sections 2–5, not merely its scalar checker. I did not edit the author files or run a numerical parameter search.

The main accepted conclusion is
\[
\overline V_T=\frac{T}{2\pi(\log T)^2}
\int_{\mathbb R}\frac{2T-1}{T-1}
\frac{\xi^2+1/4}{(T-1/2)^2+\xi^2}
|\widehat g_T(\xi)|^2d\xi
+O_\omega\!\left(\sqrt{\frac{\log T}{T}}\right),
\]
where the fixed cutoff and the actual centered prime-power error are precisely those defined in the author report. The heat-energy reformulation is an exact Fourier resolvent identity after this quantified localization error.

## 1. Inputs, assumptions and independence

I checked the frozen R20 arithmetic statistic and the location of its independent RH bound for the complete positive length average. R20 Section 3 obtains that bound before the spectral transfer. Thus using \(B_T=O((\log T)^2/T)\) in the new localization argument is not a circular use of the new representation.

I also checked the retained Schoenfeld source, Theorem 10, equation (6.2), printed p.337. Under RH its bound for \(|\Psi(x)-x|\) holds for \(x>73.2\). Enlarging an unspecified constant on a bounded initial interval gives the all-real-coordinate bound used here. For \(v<0\), the exact value is \(F(v)=-e^{v/2}\). The source does not need to provide a small-height numerical constant for this theorem.

I authored the R20 length-average input. Its separate independent Euclid review is already frozen; this review is independent of the new root-authored R21 argument, not a second independent derivation of that R20 input. The new argument does not require the R21 Wiener theorem or a conjectural pair-correlation input.

## 2. Square-root cutoff and exact arithmetic conversion

The square-root step is valid for the actual nonnegative smooth compactly supported bump. With \(M=\|\omega''\|_\infty\), the Taylor upper estimate at \(h=-\omega'(x)/M\), combined with nonnegativity, gives
\(|\omega'(x)|^2\le2M\omega(x)\). On each positive component this bounds the derivative of \(\eta=\sqrt\omega\) by \(\sqrt{M/2}\). Continuity at component endpoints extends the same Lipschitz bound across the zero set. Compact support then gives \(\eta\in H^1\). No assertion that this square root is smooth is required.

The translation inequality
\[
\|\eta_L(\cdot-u)-\eta_L\|_2^2
\le u^2\|\eta_L'\|_2^2
=\frac{u^2}{L}\|\eta'\|_2^2
\]
holds for all real \(u\), by the fundamental theorem for the Sobolev representative and Cauchy–Schwarz. It is not a local Taylor approximation in the shift.

I independently recomputed both changes of variables. With \(x=e^v\), the exact continuous subtraction turns the arithmetic increment into
\[
E(e^{v+u})-E(e^v)
=e^{v/2}\{e^{u/2}F(v+u)-F(v)\}.
\]
Its square cancels \(dx/x^2=e^{-v}dv\). With \(u=\lambda/T\), the length measure is exactly \(T e^{-Tu}du\), leaving the outer normalization \(T/L^2\). There is no lost factor of \(T\), no substitution of \(\theta\) for \(\Psi\), and no split of the centered error into divergent series.

The original integration has \(v\ge0\); extending it to the real line in the author’s \(B_T\) is legitimate because \(\eta(v/L)\) is supported in \([aL,bL]\subset(0,\infty)\). Prime-power endpoint conventions do not alter this Lebesgue integral, and the author retains the actual staircase inside it.

## 3. All-shift localization and the error exponent

The translation form and the arithmetic form differ by exactly
\[
e^{u/2}[\eta_L(v+u)-\eta_L(v)]F(v+u).
\]
This term must be kept, including where the translated cutoff enters a region in which the unshifted cutoff vanishes.

After \(w=v+u\), nonzero cutoff difference implies
\[
w\in[aL,bL]\cup[aL+u,bL+u].
\]
Consequently \(aL\le w\le bL+u\) for every \(u\ge0\). This is the required global support statement. It remains valid when the original coordinate \(v\) is negative, and it does not silently assume \(u\ll1\).

The RH bound on \(F(w)^2\), the all-shift translation inequality and the exponential measure therefore give
\[
R_T\le\frac{C_\omega}{L}
\int_0^\infty T e^{-(T-1)u}u^2(1+bL+u)^4du.
\]
The exact moments are \(T(k+2)!/(T-1)^{k+3}\), for \(0\le k\le4\). These establish finiteness for every \(T\ge2\) and \(R_T=O_\omega(L^3/T^2)\) as \(T\to\infty\). No unquantified tail in \(u\) remains.

In the product Hilbert space, let the arithmetic vector have squared norm \(B_T\), and the difference vector squared norm \(R_T\). The elementary inequality
\[
|Q_T(g_T)-B_T|\le2\sqrt{B_TR_T}+R_T
\]
does not require a sign for their cross term. With the separately known \(B_T=O_\omega(L^2/T)\), multiplication by \(T/L^2\) gives
\[
O_\omega\!\left(\sqrt{L/T}+L/T\right)
=O_\omega(\sqrt{L/T}).
\]
This is an actual arithmetic localization estimate, not a derivative of an unknown asymptotic error. Its implied constant is not evaluated.

## 4. Fourier multiplier, heat normalization and jump regularity

For the author’s angular Fourier convention, translating \(g(v+u)\) multiplies its transform by \(e^{i\xi u}\). Thus the nonnegative scalar multiplier before integration is
\(|e^{u/2+i\xi u}-1|^2\). Direct Laplace integration gives
\[
\frac{T}{T-1}+1-
\frac{2T(T-1/2)}{(T-1/2)^2+\xi^2}
=\frac{2T-1}{T-1}
\frac{\xi^2+1/4}{(T-1/2)^2+\xi^2}.
\]
The residual \(1/4\) is correct: \((T-1/2)^2-T(T-1)=1/4\). The factor \(1/(2\pi)\) in Plancherel is also correct. Tonelli applies to the original nonnegative quadratic integrand; no cancellation of divergent terms is used to justify the interchange.

For \(H_t=\exp(t\partial_v^2/2)\), its Fourier multiplier is \(e^{-t\xi^2/2}\). Squared norms therefore contain \(e^{-t\xi^2}\), exactly as in the author’s Laplace resolvent formula. This checks the heat-time factor of two and the coefficient in the final energy identity.

For every positive heat time, the derivative of \(H_tg_T\) belongs to \(L^2\). Integrating its nonnegative Fourier energy against \(e^{-(T-1/2)^2t}\) yields the bounded ratio
\((\xi^2+1/4)/((T-1/2)^2+\xi^2)\). Hence the integrated energy exists even though the original localized arithmetic function has prime-power jumps. No finite \(L^2\) norm of its unsmoothed derivative is asserted or needed.

## 5. Consequence and limits of acceptance

The factor \((2T-1)/(T-1)=2+1/(T-1)\) can be replaced by two in a limiting criterion only after bounding the correspondingly normalized energy. The author does this using the already proved arithmetic bound and the localization error. This validates the sufficient strict criterion in equation (8).

The accepted representation does **not** establish that criterion, an improvement below \(A\), a new zeta-zero dynamics theorem, or a numerical enclosure at finite height. Its ordinary heat semigroup acts on the log-prime coordinate. It is distinct from the de Bruijn–Newman deformation and stochastic Dyson Brownian motion. The comparison with those flows is correctly limited in the author report.

The crude pointwise RH bound alone gives the stated unusable \(O(TL^3)\) normalized estimate, so it supplies no hidden strict arithmetic gain. The useful saturation constant still enters through the previously proved transfer.

## 6. Bounded replay and provenance

I read the author’s small scalar checker before executing it. The accompanying independent replay script copies the unchanged checker and the pinned report to a temporary directory, runs only its eight scalar assertions, and compares the generated JSON and stdout byte-for-byte with the frozen author outputs. It also verifies every file hash in the author receipt. No author evidence is mutated.

That replay checks the scalar algebra and provenance only. The support, Sobolev, Hilbert-space, tail and Tonelli arguments were checked as ordinary mathematical proofs above. The replay is not a formal proof assistant or an empirical zeta experiment.
