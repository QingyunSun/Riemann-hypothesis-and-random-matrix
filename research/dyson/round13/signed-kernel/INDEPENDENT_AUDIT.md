# Independent audit of the smooth signed-kernel norm

Date: 2026-09-05. Reviewer: Astra subagent `yau_flow`. Verdict: **accepted as an ordinary mathematical derivation, within its explicitly limited scope**. No correction to the author report is required by this review. In particular, the positive coherent block is not a lower bound for the complete signed remainder or the window norm.

Reviewed report: `SMOOTH_SIGNED_KERNEL_NORM.md`, SHA256 `1105564835c925b818daf7198186e77c4f0f1ad4ac1001ee1bb50c0f5c7544d9`. All author-manifest hashes and all five inherited source-receipt hashes were checked against the current files and matched. Author files and the manifest were preserved.

## Exact decomposition and centering

The unrestricted mean of \(B_q\) is \(V_0/q\), whereas its primitive subtraction is \(b_q=U_q/\varphi(q)\). Their difference is retained in \(M\); replacing one by the other would change the kernel. Fourier completion, followed by reducing each fraction, yields the stated \(C_{a/d}=S_v(a/d)\sum_{q:d\mid q}\mu(q)/q\). The Ramanujan ratio \(c_q(r)/\varphi(q)=\mu(d)/\varphi(d)\), with \(d=q/(q,r)\), verifies the separate displayed identity for \(M\).

For each pair of moduli, the CRT compatibility condition \(h_1\equiv h_2\pmod g\) and progression period \(L=q_1q_2/g\) are exact. With the specified negative-sign Fourier transform, the Poisson factor is correctly \(\widehat W(kX/L)e(kr/L)\). Expanding the primitive subtractions and then collecting zero modes gives exactly
\[
Xw_0(M^2+C_2).
\]
Finite Fourier orthogonality gives
\[
R_v(g)=g\sum_{h_1\equiv h_2\ (g)}v_{h_1}v_{h_2}-V_0^2
=\sum_{r=1}^{g-1}|S_v(r/g)|^2,
\]
and summing with the signed modulus coefficients gives \(C_2\), as stated. Real \(v\) is sufficient here; nonnegative \(v\) is only imposed later for the positive block.

The nonzero single-modulus and constant-window terms have periods at most \(Q=X^{.523}\) or 1. Their polynomially bounded total coefficients can be absorbed by arbitrarily rapid decay of the fixed smooth window, so the \(O_A(X^{-A})\) remainder in equation (10) is justified. The principal terms have not disappeared by assumption.

## The two common-divisor ranges

For \(G=X^{1/10}\), a common divisor \(g\ge G\) implies
\[
L\le X^{473/500},\qquad X/L\ge X^{27/500}.
\]
The progression's nonzero Poisson part is \(O_B((X/L)^{1-B})\). There are at most \(Q^2\) pairs and \(O_v(H^2)\) total absolute shift weight per pair. Thus any prescribed negative power follows by taking a sufficiently large fixed number of derivatives; no arithmetic cancellation is needed.

For \(g<G\), smoothness of the shift profile gives
\[
R_v(g)\ll_{v,J}H^2(g/H)^{2J}.
\]
This follows by summing the rapidly decaying shift transform at the nonzero grid points, whose distances from the nearest integer are at least \(1/g\). Since \(G/H\le X^{-1/15}\), the corresponding zero-mode covariance is also negligible after the reciprocal-modulus sum and the factor \(X\) are charged. These statements remove different pieces: the large-\(g\) Poisson remainder and the small-\(g\) full-period covariance. They do not remove the small-\(g\) Poisson remainder.

The frequency form (13) has the correct sign \(\widehat W(X(\gamma-\beta))\). Integer aliases away from the closest representative, and cross terms with \(M\), have polynomial separation on the \(X\)-scale and are negligible. The author explicitly distinguishes common divisors of reduced denominators from those of arbitrary original moduli. For the selected top conductors these objects coincide because no larger multiple fits below \(Q\).

## Coherent-block constants and what they imply

The inherited actual-support count in equation (15) was checked against the frozen Round 12 construction. Its isolation identity \(A_d=1/d\) holds in the full signed family, rather than only after deleting negative coefficients. All selected coefficient phases lie in \([-\pi/4,0]\).

Writing \(n_\Omega=|\Omega_X|\) and using at most \(J\le8X/H\) cells,
\[
\sum_jm_j(m_j-1)\ge n_\Omega^2/J-n_\Omega\ge n_\Omega^2/(2J)
\]
eventually, uniformly over the stated \(H\)-range. The lower bound for \(n_\Omega\) therefore gives the exact displayed denominator
\(128^2\cdot8\cdot2=262144\).

Within a cell, the additional window-integrand phase is at most \(3\pi/100\), since \(W\) is supported in \((1,3/2)\). Including the coefficient phase difference gives
\[
\pi/4+3\pi/100=7\pi/25<\pi/3.
\]
Nonnegativity of \(W\) therefore yields the stated half-product lower bound. The coefficient-product bound contributes the further denominator 16, giving \(4194304\) in (18). The selected ordered pairs form a conjugation-symmetric set, so their sum is real.

Every selected distinct pair satisfies
\[
\frac{\gcd(d_1,d_2)}{d_1d_2}\le|\beta-\gamma|\le\frac1{100X}.
\]
Thus its common divisor is at most \(Q^2/(100X)<G\), and its reduced CRT period is at least \(100X\). The block really lies in the long-period small-common-divisor region. No equidistribution or independence of the moduli is assumed to create it.

Equation (18) bounds this specified subsum only. Remaining pairs can have negative real part and can cancel it. Equations (20) and the final unrestricted-Cauchy–Schwarz comparison retain this distinction correctly: a smaller full norm would demand cancellation, but the report does not prove that such cancellation is impossible. It also does not identify an arbitrary coefficient-space extremizer with the actual prime vector.

## Script inspection and independent replay

I inspected `check_signed_kernel_norm.py` before execution. It uses exact `Fraction` arithmetic for one fixed squarefree family, checks 100 CRT compatibility cases, verifies the complete-period mean and variance, and expands the finite-window norm into its pair, single-centering, and constant-window remainders. It retains the Mobius signs and primitive subtractions. Its polynomial toy window has integral \(1/960\); the script explicitly does not use that window to test the rapid-decay theorem.

A temporary copy was replayed, so the author JSON was not rewritten. The regenerated JSON was byte-identical to the frozen author result. In particular:

- full-period mean: \(-43/280\);
- full-period variance: \(22843/14700\);
- finite-window norm: \(14619643/165888000\);
- cutoff exponents and both coherent-block constants: passed exactly.

Script SHA256: `d661b1ef764f5ab395a9ca2db66ae9387d6885426772a93b595a43462fdc61d0`.
Result SHA256: `9f92dc12f0ac555e42af962478288e523593cf299c177fa93727d408373fdb5a`.

These checks test finite algebra, not the asymptotic prime-family count, a numerical cancellation claim, or an improved zeta correlation estimate. The accepted result is the exact main/remainder decomposition, its stated upper bound, and the positive coherent subsum with its explicit limitation.
