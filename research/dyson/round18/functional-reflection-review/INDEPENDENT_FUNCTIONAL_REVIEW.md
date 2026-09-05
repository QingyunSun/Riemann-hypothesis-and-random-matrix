# Independent audit of R18 functional reflection and the closed trace

Date: 2026-09-05. Reviewer: Aquinas (`/root/yau_flow`). Status: **accepted as an ordinary fixed-parameter RH derivation**, including the final source and boundary-wording changes. No numerical experiment, parameter scan, formal proof-assistant verification, or new strict Bragg estimate is claimed.

The complete reviewed author report is `research-round18/functional-reflection/FUNCTIONAL_REFLECTION_IDENTITY.md`, 18,635 bytes, SHA-256
`c6d8359bdecb2f0616647920ef7f7efd861ca6d1bf03995f303b4a41a77ec701`.
Its receipt has SHA-256 `b225e7c2b6a8989db842cb24eec10b617038a901aaa9821204fedb828535edad`.

I separately read and accepted the complete coordinator proof, `research-round18/root-contour-proof/ROOT_INFINITE_CONTOUR_TRACE.md`, 5,466 bytes, SHA-256
`58e103d3a5235138d1017f20577ddfae8f6f465e56298f55fd7be70c4ff79e2b`.
The independently derived pole and fixed-zero diagnostics, and my quantitative check of the far-line bound, are retained in `DIAGNOSTIC.md`. No author files were modified.

## 1. Main finding

The functional equation legally produces two absolutely convergent prime factors on a sufficiently far right line. The resulting exact identity retains a twisted finite prime-product sum, a gamma contribution, and reflected nontrivial-zero residues. At carrier one, the gamma contribution can be evaluated exactly as a negative series over the reflected trivial zeros. Both the author's digamma calculation and the coordinator's independent contour-to-infinity proof give
\[
\mathcal E_{\sigma,W}
=-2\pi\left(\mathcal R(1)+\mathcal T_{\sigma,W}\right),
\qquad W>3/\log2,
\]
with \(\mathcal T_{\sigma,W}>0\) and \(\mathcal T_{\sigma,W}\ll W^{-4}\) uniformly for \(1/2<\sigma<1\), \(W\ge6\).

This is a genuine exact evaluation and estimate for the gamma/trivial-zero part. The nontrivial reflected sum still contains the unknown quadratic zero information. In particular, the identity supplies no independent upper bound for that sum and does not by itself give the R16 Bragg deficit. The author's final explicit divergence calculation also proves that the carrier-one trivial series cannot simply be imported at \(X=T^2\).

## 2. Functional equation, real pole, and finite arithmetic terms

I source-checked the functional equation against [NIST DLMF 25.4.2](https://dlmf.nist.gov/25.4#E2) and differentiated it independently. With \(A=-\chi'/\chi\), the sign is \(H(z)=A(z)-H(1-z)\). The gamma quotient and its logarithmic derivative in the report are consistent with this convention.

The chosen line \(2\sigma<c<2\sigma+1\) makes both \(H(s)\) and \(H(s+1-2\sigma)\) absolutely convergent Dirichlet series. It crosses the reflected nontrivial line, stays below the first reflected trivial pole, and creates no new pole in the original unsplit reflected product. The coefficient of the transformed product is exactly
\[
C_\sigma(n)=\sum_{uv=n}\Lambda(u)\Lambda(v)v^{2\sigma-1}.
\]
All prime powers remain. The compact packet then gives equation (6), with the same signed Fourier kernel and factor \(2\pi W\) as in R17. No finite sum is identified with a positive energy.

The artificial real pole is accounted for correctly. Near zero, both \(A(z)\) and \(H(1-z)\) have principal term \(-1/z\), which cancels in their difference. Therefore each unsigned split product has the same residue
\[
\mathcal B(X)=H(2\sigma)X^\sigma w(-i\sigma)
\]
at \(s=2\sigma\), but the original product has none there. The multiplier is \((1-2\sigma)^2/W^4\) times the positive imaginary-sinc factor, not zero. Equation (12) has the correct plus \(2\pi\mathcal B\) when solving for the right-line gamma integral. Nontrivial residues are summed over distinct zeros with multiplicity inserted once.

The recurrence decomposition in equation (13) also checks: its remainder has no pole in the stated strip, and the separate rational term is \((s-2\sigma)^{-1}\). On the c-line its integral representation and the prime series are absolutely convergent before invoking compact support. The exact coefficient in equation (14) is \(n^{-2\sigma}\): after the Fourier shift one has \(n^{-\sigma}v^{\sigma-1}dv\), and \(u=nv\) contributes the additional \(n^{-\sigma}\). The lower limit \(\max(n,Xe^{-3/W})\) is the correct remnant of \(v\ge1\). An empty interval and a zero-valued packet endpoint create no contribution.

## 3. Digamma scale integral: convergence and normalization

The primary integral used is [NIST DLMF 5.9.16](https://dlmf.nist.gov/5.9#E16), in its domain \(\Re z>0\). On the sigma line the two digamma arguments have real parts \(1+\sigma/2\) and \(a/2\), both positive. The two time-frequency shifts consequently give exactly the increasing branch \(\mathcal L(Xe^{u/2})\) with coefficient \(e^{-(1+\sigma/2)u}\), and the decreasing branch \(\mathcal L(Xe^{-u/2})\) with coefficient \(e^{-au/2}\). The constant term is \(-\log\pi-\gamma_0\). These signs and exponents in equation (16) agree with my independent derivation.

I specifically checked the small-u interchange. The separate digamma integrals must keep their subtracting numerator terms together. Bounding them by \(u|t|\) alone would be inadequate because \(|t|w(t)\) is not absolutely integrable for this packet. The valid truncated-integral majorant is
\[
\int_0^1\frac{\min(1,(1+|t|)u)}u\,du
\ll1+\log(1+|t|).
\]
Combined with the logarithmic H bound and inverse-square packet decay, this is integrable in t. The large-u tails are exponentially bounded for fixed sigma. Dominated convergence therefore justifies the author's truncated digamma calculation. After the identity is established, local Lipschitz regularity of the finite compact packet expression also gives an \(O(u)\) numerator at zero. The proof does not obtain that regularity by illegitimately differentiating the non-absolutely-integrable time factor.

At infinity, \(|\mathcal L(Y)|\le\int|H(\sigma+it)|w(t)dt\) independently of Y, so the scale integral converges. The increasing-scale branch ranges over arbitrarily large prime indices; the author correctly refuses to call the entire gamma term a finite common prime sum.

At carrier one and \(W>3/\log2\), the rational sum, product sum, constant linear packet, and all decreasing-scale packets vanish because their upper support lies below two. The surviving increasing branch yields the jth geometric factor
\[
n^{-\sigma}n^{-2-\sigma-2j}=n^{-2\sigma-2-2j},
\]
and Laplace argument \((2+\sigma+2j)/W\). The scale change cancels the prefactor W; the resulting coefficient is **minus \(2\pi\)**. Thus the first term is at \(2\sigma+2\), not \(2\sigma\), and equation (19) has the correct sign and index.

The signed spline does not invalidate Fubini. Before evaluating its Laplace transform, an absolute majorant bounds the jth term by a constant times \(4^{-j}e^{6j/W}\), using its bounded compact support and \(\sum\Lambda(n)n^{-2\sigma-2-2j}\ll4^{-j}\). This series converges in the stated strict sufficient range. No positivity of the Fourier kernel is assumed.

## 4. Independent contour-to-infinity proof and trivial correction

I read the coordinator's final proof in full, and independently verified its new uniform line estimate. For \(c_N=2\sigma+2N+1\), the reflected argument is the negative odd line \(-2N-1-it\). Its cotangent is bounded by one in modulus, its digamma term has logarithmic growth in \(c_N+|t|\), and the first H factor is \(O(2^{-c_N})\). The elementary packet estimate can be made explicit as
\[
|w(t-id_N)|\le100W^2e^{3d_N/W}/(t^2+d_N^2),
\qquad d_N=c_N-\sigma>1.
\]
Scaling t by \(d_N\) yields the bound
\[
O\!\left(W^2 e^{-c_N(\log2-3/W)}
\frac{\log(c_N+2)}{c_N}\right)
\]
for the final vertical integral. It tends to zero in the stated sufficient range. The proof first takes horizontal-height limits at each fixed N, and only afterwards sends N to infinity. No uniform-in-N horizontal estimate is silently assumed.

The full pole inventory and clockwise contour sign agree with R17. The first N genuine reflected trivial poles have positive residues \(H(2\sigma+2k)w(-i(\sigma+2k))\), \(1\le k\le N\). Neither the artificial pole at \(2\sigma\) nor a double-counted nontrivial multiplicity is introduced. Absolute convergence then gives the exact trace.

For \(W\ge6\), I checked the uniform majorant
\[
0<H(2\sigma+2k)w(-i(\sigma+2k))
\le C W^{-4}(k+1)^4(e/4)^k.
\]
It proves both positivity and \(O(W^{-4})\), uniformly across \(1/2<\sigma<1\). The fixed-sigma \(W^4\mathcal T\) limit in equation (21) also follows by the same dominated convergence. These estimates concern only the explicit trivial correction; the constants in the nontrivial-zero bounds may blow up as sigma approaches one half.

The final texts use sufficient-condition language. Neither the author nor the coordinator now claims that the strict inequality is a necessary or optimal boundary for every displayed estimate.

## 5. Utility diagnostic and the failed carrier estimate

The fixed-zero calculation from my separate diagnostic was reproduced faithfully in the author report. For a fixed zero of multiplicity m and fixed sufficiently large W,
\[
H(2\sigma-\rho)=-m/(2\delta)+O_\rho(1),
\quad
\mathcal R_\rho(1)=-m^2w_{1/2,W}(\gamma)/(2\delta)+O_{\rho,W}(1).
\]
Its contour correction is precisely the leading local modulus-energy singularity. This identifies concrete quadratic information still carried by the nontrivial sum. It does not exchange the delta limit with the infinite sum and gives no uniform shrinking-sigma estimate.

I also checked the final additional carrier-divergence paragraph. For fixed \(\sigma,W,X\), the kth weighted trivial summand has exactly the displayed leading form
\[
\frac{(\log2)2^{-2\sigma}X^\sigma W^2e^{3\sigma/W}}
{(\sigma+2k)^2}
\left(\frac{X^2e^{6/W}}4\right)^k.
\]
It follows by combining the first-prime asymptotic for H with the imaginary-sinc asymptotic; no constant or factor of 64 survives. If \(Xe^{3/W}>2\), these positive summands fail even to tend to zero. This proves actual divergence of the proposed carrier-weighted trivial series, rather than inferring divergence from an unsuccessful upper bound. In particular the carrier-one closure is unavailable at \(X=T^2,W=T\), \(T\ge2\).

For the remaining finite-c estimate, \(C_\sigma(n)\le n^{2\sigma-1}(\log n)^2\) follows from \(\sum_{d\mid n}\Lambda(d)=\log n\). Counting the compact interval gives equation (26). Solving the exact identity gives
\[
\mathcal P-2\pi\mathcal B=\mathcal G_\sigma-\mathcal I_\sigma-2\pi\mathcal R.
\]
The packet envelope, fixed-sigma logarithmic-derivative bounds, and unit-interval zero counting imply the stated \(W(1+X^\delta)\log^4(W+2)\) bound. At \(X=W^2\), \(WX^\delta=X^\sigma\), so it gives no power improvement over the elementary finite-sum bound and has weaker displayed logarithms. The restriction to fixed sigma is explicit and essential.

These are specific valid identities, a concrete divergence test, and a quantified unsuccessful estimate. They do not prove that all functional-equation approaches are impossible. A new estimate for the retained nontrivial residue/covariance, and a justified transfer to the actual Bragg kernel, is still required.

## 6. Evidence and frozen status

This was an analytic review without numerical sweeps or zeta-data calculations. The independent initial diagnostic, explicit far-line majorant, source-inspection receipt, and this final audit are retained separately. The NIST functional-equation and digamma primary pages were read; the raw TeX download attempt returned HTTP 403, so no raw-download hash is claimed. The source receipt records that distinction.

All frozen author bytes and all four author-receipt dependency entries, including the coordinator proof, were independently checked on disk. The final delta review included both sufficient-condition wording changes, the pinned coordinator link, and the new explicit divergence asymptotic. The accompanying receipt pins every reviewed file and this review's artifacts. No author or Git files were changed.

**Accepted mathematical scope:** exact functional reflection, cancellation of the artificial pole, explicit gamma/trivial-zero evaluation, the carrier-one closed energy trace, and the stated failure of the proposed large-carrier extension. **Still unproved:** a strict actual-zeta Bragg deficit, AH exclusion, a Montgomery/Dyson conjecture, or any uniform bound that supplies the missing transfer.
