# Independent audit of the F1 cutoff repair and F3 mass bound

Date: 2026-09-05. Independent reviewer: Astra subagent `yau_flow`. Verdict: **accepted for the stated mathematical scope**. This is a bounded ordinary-proof audit of the two authored notes, not a numerical rerun, an audit of every Fable script, or a proof of an arithmetic-to-Fock limit. The exact reviewed hashes are listed below.

## F1: the local remainder is uniform at the actual parameter

For the standard generalized-divisor Euler coefficients,
\[
d_\ell(p^j)=\frac{(\ell)_j}{j!}
=\prod_{r=1}^j\left(1+\frac{\ell-1}{r}\right),
\qquad \ell=16/15,\quad a=\ell^2=256/225.
\]
The elementary harmonic-sum bound gives
\(d_\ell(p^j)\ll_\ell(j+1)^{1/15}\). Set \(t=p^{-1-\varepsilon}\), with \(0<\varepsilon\le1\); then \(0\le t\le1/2\). Thus
\[
E(t)=\sum_{j\ge1}d_\ell(p^j)^2t^j
=at+O_\ell(t^2),\qquad E(t)=O_\ell(t),
\]
uniformly for every prime and every such \(\varepsilon\). The tail constant is bounded by the finite series
\(\sum_{j\ge2}O_\ell((j+1)^{2/15})2^{-(j-2)}\); it does not depend on the prime cutoff.

Since \(\rho=E/(1+E)\),
\[
\rho(1-\rho)=\frac E{(1+E)^2}=at+O_\ell(t^2).
\tag{A}
\]
Consequently the local error, summed against \((\log p)^4\) over any set \(p\le P\), is bounded uniformly in both \(P\) and \(\varepsilon\) by a constant times
\(\sum_p(\log p)^4p^{-2}<\infty\). Multiplication by \(\varepsilon^4\) makes this error vanish uniformly. No finite-prime experiment is needed to justify this step. In particular the coefficient is \(6a\), not \(6a^2\).

## F1: the PNT argument controls the joint cutoff limit

Put \(g_\varepsilon(x)=(\log x)^3x^{-1-\varepsilon}\). The leading prime sum in (A) is
\[
\sum_{p\le P}(\log p)^4p^{-1-\varepsilon}
=\int_{2^-}^{P}g_\varepsilon(x)\,d\theta(x).
\]
Write \(R(x)=\theta(x)-x\). Given \(\eta>0\), PNT supplies a fixed \(x_0\) such that \(|R(x)|\le\eta x\) for all \(x\ge x_0\). The contribution below \(x_0\), including endpoint conventions, is \(O_{x_0}(1)\) before scaling. For \(P\ge x_0\), integration by parts bounds the scaled upper-part error by
\[
\eta\varepsilon^4\left(P|g_\varepsilon(P)|
+x_0|g_\varepsilon(x_0)|
+\int_{x_0}^{P}x|g_\varepsilon'(x)|\,dx\right).
\tag{B}
\]
These terms are uniform in the arbitrary cutoff:
\[
\varepsilon^4P|g_\varepsilon(P)|
=\varepsilon z^3e^{-z}=O(\varepsilon),\qquad z=\varepsilon\log P,
\]
and, using
\(x|g_\varepsilon'(x)|\le x^{-1-\varepsilon}[3(\log x)^2+(1+\varepsilon)(\log x)^3]\),
\[
\varepsilon^4\int_{x_0}^{P}x|g_\varepsilon'(x)|\,dx
\le 6\varepsilon+6(1+\varepsilon)=6+12\varepsilon.
\tag{C}
\]
Here extending the positive comparison integral to \([1,\infty)\) uses the exact gamma integrals. Letting \(\varepsilon\downarrow0\), then \(\eta\downarrow0\), proves uniform convergence of this scaled PNT error over all cutoffs \(P\ge2\). This is an asymptotic uniformity argument; it supplies no explicit finite-data error constant without a quantitative PNT input.

The main integral is
\[
\frac{\varepsilon^4}{6}\int_2^P(\log x)^3x^{-1-\varepsilon}\,dx
=\frac16\int_{\varepsilon\log2}^{\varepsilon\log P}t^3e^{-t}\,dt.
\]
This proves the authored equation (1) for every joint limit with finite \(z_0\ge0\), including \(P\to\infty\) but \(z_0=0\), and for \(z_0=\infty\). It also permits \(P=\infty\) at each positive \(\varepsilon\), since the original prime sum then converges and the upper integration-by-parts boundary vanishes. If \(P\) remains fixed, the scaled finite sum tends to zero, as the note says. Thus no interchange of an uncontrolled joint limit is hidden in the proof.

The incomplete fraction at \(z_0=1\) is exactly \(1-8/(3e)\), not one. The cutoff warning and the explicit distinction from a finite-point error certificate are justified. I did not rerun the script or independently re-audit all its reported sign/output details.

## F3: discrete bound and first-bin criticism

The stated coefficients give, by exact algebra,
\[
B_M^2=\sum_{j=1}^M\frac{[2\sin(\pi j/(2M))/\sqrt j]^2}{j/M}
=\frac1M\sum_{j=1}^M f(j/M),
\qquad f(u)=\frac{4\sin^2(\pi u/2)}{u^2}.
\]
The function \(f\) extends continuously to \(f(0)=\pi^2\) and decreases on \((0,1]\). Indeed \(\sin x/x\) decreases on \((0,\pi/2]\), since the derivative numerator \(x\cos x-\sin x\) is negative there. The right-endpoint sum is therefore bounded by the integral on each bin, proving the exact inequality
\[
B_M^2\le\int_0^1 f(u)\,du=B_g^2
\]
for every positive integer \(M\), without an asymptotic quadrature claim. Integration by parts also checks the exact expression \(B_g^2=2\pi\operatorname{Si}(\pi)-4\). No certified decimal or spectral enclosure was recomputed.

The continuous sector argument uses \(\|a(g)\Psi\|^2\le B_g^2\langle\Psi,E\Psi\rangle\), not a particle-number bound. On the mass-cutoff space this gives a bounded annihilation map; its adjoint is the compressed creation extension. Different input sectors have different output sectors, so the infinite direct sum introduces no unaccounted cross terms. The resulting \(\|K\|\le2B_g^2\), and the analogous discrete bound, are consistent with the stated conventions.

Finally,
\(\int_0^{1/M}du/u=\infty\). A nonzero constant on the first bin is not an element of the one-particle Hilbert space and cannot be normalized into a piecewise-constant Galerkin basis. A profile proportional to \(g\) is square integrable there because \(g(u)=O(u)\), but that is a different construction and does not identify its compressed mass operator or creation coefficients with the literal grid model. The authored criticism is precise: it rules out the proposed normalization argument, **not** every possible convergent approximation. Uniform boundedness alone proves neither a sharp norm limit nor the desired spectral wall.

## Reviewed snapshots and limits

- `F1_REPAIR_AND_CUTOFF_REVIEW.md` — SHA256 `9f9cd67afbfd7d304f6eb42adcf34391972c54a9f49a2964be1d8fbb176da628`.
- `F3_MASS_CUTOFF_BOUND.md` — SHA256 `112eac7be3ed1294ea47c046eaa93720b170858350115960f8578e0301bb638b`.

Author files were preserved. This review accepts the local Euler remainder, incomplete-gamma limit, discrete mass bound, and first-bin objection. It does not convert the numerical Fock fits into enclosures or establish any new zeta-zero or prime-gap theorem.
