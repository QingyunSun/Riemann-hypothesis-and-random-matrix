# Independent review of growing-wheel centering

Date: 2026-09-05. Reviewer: Euclid. Mathematical verdict: **accepted as an ordinary proof with the stated unconditional comparison and RH transfer scopes**. No substantive amendment was required. The author incorporated the harmless clarification that the primorial telescoping product is used for \(z\ge2\); its asymptotic statement was already correct.

This is a full ordinary-proof review of GROWING_WHEEL_CENTERING.md, including its finite-height comparisons, unrestricted endpoints and length tails, sufficient growing-wheel condition, explicit primorial example, and transfer to the actual log-prime heat energy. It is not an empirical test of prime correlations. The final author is pinned at 12,163 bytes, SHA256 `d65b165547316a9b047db65295a4f1e05c3aa2a66416e287d9860688b3b3f73f`. Its receipt is SHA256 `b3cc9053a8953278f58e4dcb723c06c762a0f1928d348e66915cb5c207a8cd07`.

## 1. Exact measure, interval convention and finite-height existence

The measure is the original R20 positive product measure
\[
d\mu_T=\frac{T}{\ell^2}e^{-\lambda}
W_T(x)x^{-2}\,dx\,d\lambda,
\qquad L=T^{7/4}\le x\le U=T^{9/4}.
\]
Its mass is exactly
\[
\mathfrak m_T=\frac{T}{\ell^2}\int_L^U W_T(x)x^{-2}dx,
\]
because the exponential length law has mass one. The upper bound \(BT/(L\ell^2)\) is valid. In particular \(\sqrt{T/L}=T^{-3/8}\), which is the source of the exponent in the permitted wheel condition.

All staircases use sums through a real upper endpoint, and therefore differences count \((x,y]\) exactly. There is no approximation of \(y=e^{\lambda/T}x\) by \(x+\lambda x/T\), and no replacement of \(\Psi\) by the genuine-prime-only function \(\theta\).

The original variance is finite unconditionally for every fixed \(T\ge4\). For example \(\Psi(y)\le y\log(2y)\), with \(x\) in a finite positive window, bounds its integrand by a constant depending on that fixed \(T\) times
\(e^{2\lambda/T}(1+\lambda)^2\). Multiplication by \(e^{-\lambda}\) is integrable. This provides a direct check of the finiteness premise used in the triangle inequalities; RH is not silently required at that point.

## 2. The center error is uniform over every real endpoint

For squarefree \(\mathcal W\), inclusion-exclusion gives, for every real \(x\ge0\),
\[
N_{\mathcal W}(x)
=R\sum_{d\mid\mathcal W}\mu(d)\lfloor x/d\rfloor,\qquad
R\sum_{d\mid\mathcal W}\frac{\mu(d)}d=1.
\]
There are \(2^\kappa\) divisors. Subtracting \(x\) leaves a finite sum of fractional parts, so
\[
|N_{\mathcal W}(x)-x|\le R2^\kappa=D.
\]
Consequently the interval-center discrepancy has absolute value at most \(2D\), even at noninteger or prime-power endpoints. This pointwise estimate is global in both endpoints. In particular it remains valid for arbitrarily large \(\lambda\); there is no tail cutoff whose dependence on \(T\) or on the wheel needs to be controlled.

The difference between the wheel-centered interval and the original continuum-centered interval is the negative of this center discrepancy. Its norm is at most \(2D\sqrt{\mathfrak m_T}\). Both the reverse triangle inequality for norms and
\[
|\|u+v\|^2-\|u\|^2|
\le2\|u\|\|v\|+\|v\|^2
\]
give precisely the author's first norm and variance comparisons. No sign is assumed for their cross term.

The edge case \(\mathcal W=1\) is included: \(R=D=1\), \(N_{\mathcal W}(x)=\lfloor x\rfloor\), and the same estimate is valid.

## 3. Every removed prime power has a separately paid norm

The difference between the wheel-centered and rough-supported intervals is exactly
\[
A_{\mathcal W}(x,\lambda)
=P_{\mathcal W}(e^{\lambda/T}x)-P_{\mathcal W}(x),
\]
where \(P_{\mathcal W}\) contains every \(p^j\), including \(j=1\), for each base \(p\mid\mathcal W\).

For a fixed base,
\[
\sum_{p^j\le y}\log p
=\lfloor\log y/\log p\rfloor\log p
\le\log y.
\]
It follows without any restriction on the sizes of those primes that
\[
0\le A_{\mathcal W}(x,\lambda)
\le\kappa(b\ell+\lambda/T).
\]
If a wheel prime is above the current upper endpoint it simply contributes zero. This explains why neither \(\log\mathcal W\) nor a bound \(\mathcal W\le T^C\) is needed.

Minkowski's inequality in the normalized exponential length law uses
\[
\int_0^\infty e^{-\lambda}d\lambda=1,\qquad
\int_0^\infty \lambda^2e^{-\lambda}d\lambda=2.
\]
It gives exactly
\(\kappa(b\ell+\sqrt2/T)\sqrt{\mathfrak m_T}\).
The norm debt in the author theorem is therefore complete. Prime powers have not been discarded merely because the remaining integers are coprime to the wheel.

The original R20 bound \(\overline V_T=O_\omega(1)\) is conditional on RH and is used only to turn a small norm difference into an \(o(1)\) variance difference. Under
\[
D=o(T^{3/8}\ell),
\]
the center debt tends to zero. Since \(D\ge2^\kappa\), this same condition forces \(\kappa=O(\ell)\). The prime-power debt is then \(O_\omega(\ell T^{-3/8})=o(1)\). Thus no second hidden growth condition is needed. These estimates are uniform in the permitted varying wheel and require no differentiability or monotonicity in \(T\).

## 4. Primorial growth uses PNT, not Mertens or GRH

For \(z=c\ell\log\ell\), the ordinary PNT gives
\[
\pi(z)=\frac{z}{\log z}(1+o(1))=(c+o(1))\ell.
\]
For eventual \(z\ge2\), each factor \(n/(n-1)\) is greater than one, so enlarging the prime product to all integers yields
\[
1\le R=\prod_{p\le z}\frac p{p-1}
\le\prod_{2\le n\le\lfloor z\rfloor}\frac n{n-1}
=\lfloor z\rfloor.
\]
Therefore \(\log R=o(\ell)\) and
\(D=T^{c\log2+o(1)}\). This proves the sufficient range
\(0<c<3/(8\log2)\) exactly as stated.

The example \(c=1/2\) is rigorous: strict convexity of \(1/x\) on \([1,2]\) puts its integral strictly below the trapezoid area \(3/4\), so \((1/2)\log2<3/8\).

For \(c\) above the threshold, the stated discrepancy budget fails; the proof does not claim the actual center comparison must fail. At equality the unspecified PNT error does not decide the condition. The author explicitly avoids both stronger assertions. This audit confirms that neither Mertens' product estimate, PNT in growing progressions, RH for Dirichlet \(L\)-functions, nor any computational enumeration of the wheel is used.

I checked the retained DLMF source and opened its official page independently. Equation 27.2.3 states \(\pi(x)\sim x/\log x\), and the surrounding text identifies this as the proved prime number theorem. It is the only new external asymptotic input in the author note.

## 5. Cumulative rough residual and the exact heat multiplier

The author retains the cumulative staircase
\[
C_{\mathcal W}(x)
=\Psi(x)-P_{\mathcal W}(x)-N_{\mathcal W}(x).
\]
It includes the atom at \(n=1\) in \(N_{\mathcal W}\) and agrees exactly with the sum of \((\Lambda(n)-R)1_{(n,\mathcal W)=1}\). Its comparison with \(\Psi(x)-x\) is bounded by \(D+\kappa\log x\).

On the fixed logarithmic support, this gives
\[
\|g_{T,\mathcal W}-g_T\|_2^2
\le B\int_{a\ell}^{b\ell}e^{-v}(D+\kappa v)^2dv.
\]
Extending the positive integral to infinity, putting \(v=a\ell+s\), and applying Minkowski under the density \(e^{-s}\) yields
\[
\|g_{T,\mathcal W}-g_T\|_2
\le\sqrt{B/L}\,[D+\kappa(a\ell+\sqrt2)].
\]
The factor \(L^{-1/2}\) and the \(\sqrt2\) are both correct.

The angular Fourier convention is the one in the independently reviewed R21 input. Its exact nonnegative multiplier is
\[
M_T(\xi)=\frac{2T-1}{T-1}
\frac{\xi^2+1/4}{(T-1/2)^2+\xi^2}.
\]
For \(T\ge4\), the ratio is at most one and
\((2T-1)/(T-1)\le7/3\). Plancherel therefore gives
\[
\mathcal J_T(f)^{1/2}
\le\sqrt{\frac{7T}{3\ell^2}}\|f\|_2.
\]
Applied to the preceding difference, this is exactly the author's \(h_T\). The \(1/(2\pi)\) in \(\mathcal J_T\) has been canceled correctly by angular Plancherel; there is no additional factor of \(2\pi\).

This is a comparison of two inputs to one bounded quadratic operator. It does not assume that a new prime/zero formula holds uniformly for changing arithmetic coefficients. Only the fixed original profile \(g_T\) uses the R21 representation and its RH localization bound. The new profile transfers by the explicit norm estimate.

With RH, the original energy is bounded independently of the wheel. Hence its squared-energy difference is \(O_\omega(h_T+h_T^2)\), and adding the original \(O_\omega(\sqrt{\ell/T})\) localization error proves the author equation (21). The error constant is independent of \(\mathcal W(T)\). The separate interval comparison then gives the rough-variance version under the same hypotheses.

## 6. Infinite heat time and the limitations of the conclusion

For the semigroup \(H_t=e^{t\partial_v^2/2}\), the squared Fourier multiplier is \(e^{-t\xi^2}\). Nonnegative integration gives
\[
\int_0^\infty e^{-(T-1/2)^2t}
(\xi^2+1/4)e^{-t\xi^2}dt
=\frac{\xi^2+1/4}{(T-1/2)^2+\xi^2}.
\]
This verifies the full coefficient of the heat-energy representation. The integrated multiplier is bounded, so the heat derivative may be integrated for every \(L^2\) input, including the actual staircase profile. No square-integrable unsmoothed derivative and no truncation at small positive heat time are needed.

The note proves an equivalence of the actual arithmetic target with an explicitly supported residual, not monotonic improvement of its energy. In particular removing the wheel support also changes the surviving coefficient to \(\Lambda(n)-R\); it does not justify comparing squared energies by support inclusion. The inherited AH-Pairs saturation value remains unchanged whenever the norm debts vanish.

All claims about the unchanged zeta variance or its AH limit retain RH and the exact earlier hypotheses. The new wheel inequalities themselves are unconditional. There is no assertion about Dyson Brownian motion, de Bruijn–Newman flow, a new distribution exponent, or a strict correlation estimate.

## 7. Verification receipt

I read the complete author checker, copied it and the final manuscript to a temporary directory, and executed that unchanged copy once. Its eight exact scalar checks passed. The resulting JSON and stdout are byte-for-byte identical to both frozen author outputs, SHA256 `31e6e7f1a307adee99b382e01758f2ff94d8b29732f300a07c7e3df494c2475b`. The checker enumerates no wheels, divisors or prime heights.

All thirteen listed author, dependency and retained-source files matched their recorded byte counts and SHA256 hashes. The independent input/replay record is `input_and_replay_checks.json`, SHA256 `4248f09cecf9d7d22d4f8916ba2a0e1bb7ec91dd74d21ebb62792f715f2257fc`. It includes the retained DLMF HTML and exact formula, and both R20/R21 manuscripts with their independent reviews. I also opened the official DLMF page live and checked its formula and unconditional status.

The final author delta contains the explicit \(z\ge2\) qualification and no further requested mathematical correction. No author file was modified by this reviewer. The endpoint, support, norm, growth, and heat-transfer arguments were checked as ordinary mathematics above; the scalar replay does not replace those proofs or constitute a formal proof-assistant verification.
