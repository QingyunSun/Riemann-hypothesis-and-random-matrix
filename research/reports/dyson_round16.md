# Round 16: a sharp AH saturation target and an exactly finite prime packet

Date: 2026-09-05. This round prioritizes actual zeta zeros and the Dyson–Montgomery programme. It establishes a precise frequency-two saturation test under RH and a finite signed prime representation for a different, nonnegative time packet. The complete proofs, independent reviews, exact checks and root integration reviews are preserved. The strict actual-zeta inequality remains open.

## 1. Frequency two is a concrete AH target

Use the actual normalized, Lorentzian-weighted pair measure mu_T and Montgomery form factor F_T, with zeros counted with multiplicity. Choose a fixed nonnegative smooth autocorrelation bump psi supported on [-1,1], normalized by psi(0)=1 and with nonnegative Fourier transform. Let m0=integral psi and m1=integral |v|psi(v); these exact constants satisfy 0<m1<m0<1. For fixed 0<epsilon<1 define

\[
C_{\varepsilon,T}(b)=\int\psi((\alpha-b)/\varepsilon)F_T(\alpha)\,d\alpha.
\]

There is no inverse-epsilon normalization. Fourier inversion and positivity give the exact finite-T comparison

\[
0\le C_{\varepsilon,T}(b)\le C_{\varepsilon,T}(0),
\]
\[
D_{\varepsilon,T}=C_{\varepsilon,T}(0)-C_{\varepsilon,T}(2)
=\varepsilon\int\widehat\psi(\varepsilon u)(1-\cos(4\pi u))\,d\mu_T(u)\ge0.
\]

Under RH, the known interior Fourier band gives C_epsilon,T(0)->1+epsilon²*m1. The precise AH-Pairs hypothesis forces every subsequential pair limit onto the half-lattice. Its Fourier transform then has period two, so it has an atom of mass one at frequency two with neighboring density |alpha-2|. Therefore

\[
\mathrm{RH+AH\text{-}Pairs}
\quad\Longrightarrow\quad
C_{\varepsilon,T}(2)\to1+\varepsilon^2m_1,
\qquad D_{\varepsilon,T}\to0.
\]

No assumption on simplicity or the limit of the near-diagonal parameter p0 is needed. Early zeros, noncompact Fourier tails and odd-frequency boundary atoms are handled explicitly. Epsilon is fixed before the large-height limit.

A proof of liminf D_epsilon,T>0 for one fixed test would refute AH-Pairs under RH. Even positive limsup would contradict its full limiting prediction. The conservative target limsup C_epsilon,T(2)<1 asks for the stronger margin liminf D>epsilon²*m1. Neither strict inequality is proved.

For the fixed seed at epsilon=1/4, diagnostic quadrature gives the AH value/current upper bound 1.0105877964, while the sine/GUE prediction is 0.1851531433. The conservative deficit threshold is only m1/16, approximately 0.0105877964. These decimals are not certified enclosures and do not establish the desired gap. A positive deficit would require positive normalized pair mass off the half-lattice; a few exceptional pairs do not suffice.

The same comparison proves that every subsequential spectral measure has atoms of mass at most one, at every frequency. Here epsilon decreases only after taking the subsequential limit. This capacity permits AH's maximal atom; it does not exclude it.

Full proof and reviews: [author](../dyson/round16/bragg-atom/BRAGG_ATOM_TARGET.md), [independent review](../dyson/round16/bragg-atom-review/INDEPENDENT_BRAGG_REVIEW.md), [root review](../dyson/round16/root-review/ROOT_BRAGG_REVIEW.md).

## 2. The actual centered arithmetic target survives near T squared

The source-checked prime representation extends uniformly to any fixed positive compact alpha range. For x=T^alpha, retain all prime powers and the full continuous mean in

\[
P_x(t)=\sum_n\Lambda(n)a_n(x)n^{-it}-M_x(t),
\quad a_u(x)=\min\{(u/x)^{1/2},(x/u)^{3/2}\},
\]
\[
M_x(t)=\frac{2x^{1-it}}{(1/2+it)(3/2-it)}.
\]

Under RH,

\[
F_T(\alpha)=\frac{1}{xT\log T}\int_0^T|P_x(t)|^2dt
+O\left(\frac{\log T}{x}+\frac{\log^2T}{T}\right).
\]

The report integrates this into an exact centered quadratic prime kernel plus o(1). Its atomic diagonal tends to 2*epsilon*m0. The remaining E_epsilon,T contains prime-prime, both negative prime-continuum cross terms and the continuous-continuous term. The conservative target is precisely

\[
\limsup E_{\varepsilon,T}<1-2\varepsilon m_0.
\]

AH predicts 1+epsilon²*m1-2*epsilon*m0; sine predicts -epsilon*m0. At epsilon=1/4 the allowable upper bound exceeds one half, but the individual uncentered terms may be much larger. Retaining their cancellations is necessary.

This route uses x from T^(2-epsilon) to T^(2+epsilon), not a constant-factor neighborhood of T². Its natural shift exponents are [3/7,5/9] at epsilon=1/4. The earlier R9–R15 arithmetic estimates apply to smaller shift ranges. In particular the earlier nuisance bound H*sqrt(X)*log^4 X, divided by XlogX, is no longer negligible at alpha=2 and above. This exposes a failed transfer of an estimate, not a lower bound on the true error.

The direct positive-pair upper bound is a standard mechanism also used by Carneiro–Chandee–Chirre–Milinovich. Their finite-window upper constants retain an atom cost one as the interval shrinks. The separately published 1.3208 long-average bound has a long-interval hypothesis and cannot be substituted for this narrow bump. The author gives exact source locations and a rational finite-window comparison; no optimization record is claimed.

## 3. A nonnegative time weight gives an exactly finite signed prime sum

Independently, under RH let 1/2<sigma<1, a=1-sigma, W>=1 and X>exp(2). Define

\[
w(t)=\frac{t^2+a^2}{W^2}
\left(\frac{\sin(t/(2W))}{t/(2W)}\right)^4.
\]

This entire, nonnegative, integrable weight has simple zeros at t=±ia. If B is the cubic spline density of the sum of four uniforms on [-1/2,1/2], b=a/W and K_b=-B''+b²B, then under the angular Fourier convention

\[
\widehat w(\lambda)=2\pi W K_b(W\lambda),
\qquad\operatorname{supp}\widehat w\subset[-2/W,2/W].
\]

For actual H=-zeta'/zeta, the one-factor contour gives

\[
\int H(\sigma+it)X^{it}w(t)dt
=2\pi W\sum_{Xe^{-2/W}<n<Xe^{2/W}}
\Lambda(n)n^{-\sigma}K_b(W\log(n/X)).
\]

The simple pole at one is canceled exactly. The arithmetic sum is finite by Fourier support; no Gaussian tail was truncated. All prime powers are included, and integer endpoint contributions vanish. The continuous density integrates exactly to zero. With E=psi-u, integration by parts gives -integral E*f' with zero support-boundary terms, hence the uniform RH bound O(W*X^(1/2-sigma)*log²X).

The time normalization is Z=2pi W(2+2b²/3). The Fourier kernel remains substantially signed: its normalized negative mass in scaled frequency is at least 47/104 and tends to 2/3 as b->0. It cannot be discarded in an arithmetic bound. Nonnegative time weight nevertheless supplies a positive full Gram matrix.

This is a linear identity with a different weight. It does not automatically transfer to the original quadratic target. Simple zeros do not cancel double poles, reflected logarithmic derivatives bring additional poles, Plancherel uses the squared weight, and differentiating a parameter-dependent weight retains its derivative term.

Full proof and reviews: [author](../dyson/round16/compact-packet/COMPACT_POLE_PACKET.md), [independent ordinary review](../dyson/round16/compact-packet-review/INDEPENDENT_COMPACT_PACKET_REVIEW.md), [root integration receipt](../dyson/round16/root-review/ROOT_COMPACT_RECEIPT.md). The separately implemented exact checker and complete finite prime-power example sit beside the author file.

## 4. Verification and remaining work

Three bounded outputs reproduce byte for byte, with no excluded fields. They cover the Bragg normalization and exact rational source constants; cubic-spline C² matching, derivative norms, signed masses, an exact inverse-Fourier identity; and two independent enumerations of a finite 45-prime-power packet. The packet example includes 101². Its computed arithmetic sum is not a numerical zeta integral. Floating quadratures are explicitly diagnostic and not outward-certified asymptotic evidence.

The [intake manifest](../dyson/round16/INTAKE_MANIFEST.json) records every original, the local reference bodies and any exact duplicate replay inputs omitted publicly. Original mathematical reports are unchanged; later reviews control their acceptance status. The [replay receipt](../logs/round16-integration/REPLAY_RECEIPT.json) identifies all three outputs. The complete 705/753-page handoff remains pinned through Round 14, with this report and Round 15 forming subsequent updates.

The next useful tests are a strict upper estimate for the full centered frequency-two kernel, and a correctly derived quadratic packet identity that retains all reflected-zero residues. They are analytic tasks, not a search for a numerical appearance of GUE. No new RH, Montgomery–Dyson/GUE, AH-refutation, zeta-gap or sub-186 prime-gap theorem is claimed.

Postponed: another large PDF rebuild, broad parameter sweeps, any sharp-window transfer without its full error, and formalization of identities before the outstanding arithmetic inequality is understood. Main risk: losing a centering term, pole, Fourier normalization or order of limits during later use. Reverting this checkpoint removes the new reports and checks without altering earlier source archives.

The originating coordinator also independently read both complete frozen proofs and the primary source ranges. Its unchanged [review receipt](../dyson/round16/root-review/COORDINATOR_R16_REVIEW.json) accepts exactly these bounded conclusions and emphasizes that positive limsup of the deficit already suffices to exclude full AH-Pairs; the stronger liminf and below-one targets are optional strengthenings.
