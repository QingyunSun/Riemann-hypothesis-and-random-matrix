# Round 5: radius-dependent sieve bounds and a negative geometry search

The bounded search is complete. Ten radius/plateau configurations were evaluated with all 77 polynomial coefficients reoptimized at a coarse grid, and two nearby candidates were refined at the official grid. **Neither geometry change improves the original k=39 result.** The useful mathematical output is a proved variable-radius exceptional-square estimate, an exact sufficient source template, and a precise repair for a newly activated source row. None proves DHL(39,2), a prime-gap bound below 186, or a global obstruction to those goals.

This report follows [Round 4](prime186_round4.md), where a new outward lower integral increased the fixed k=40 proof margin to 24.86626 ppm by combining the new credit with inherited published endpoints. That result remains valid in its stated scope. Its approximately 1.5 ppm credit cannot be assigned to new k=39 vectors or supports without computing their own integrals.

## 1. Evidence and proof status

Three independently assigned research components are preserved with their original scripts, outputs and reports:

| Component | Result | Evidence status |
|---|---|---|
| [Exceptional-square extension](../prime-gaps/round5/exceptional-radius/EXCEPTIONAL_RADIUS_EXTENSION.md) | A radius-dependent constant follows from the existing counting argument over an explicit open interval | Ordinary written proof plus exact rational certificate; not Lean formalization |
| [Source geometry audit](../prime-gaps/round5/geometry-audit/GEOMETRY_SOURCE_AUDIT.md) | Twelve of fifteen natural cap templates pass, with a uniform one-layer mesh repair and a common inner-square source | Exact arithmetic and a sufficient-template proof; no physical sieve integrals |
| [Finite geometry search](../prime-gaps/round5/geometry-trial/REPORT.md) | Ten coarse points and two refinements give no improvement from changing radius/plateau | Floating cap-only optimization; no interval optimum or support restoration |

The primary proof is [Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), especially Propositions 3.10, 3.11, 4.2 and 4.6. The companion certificate is pinned to [PrimeGaps186 commit 61340d0](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330). Its Python source SHA256 is `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`. The preserved source is unchanged.

## 2. A parameterized exceptional-square estimate

The original proposition bounds an exceptional square with a coefficient-root radius at most 11/40. Its proof uses this radius in the ordinary CRT error, not in a new prime-distribution hypothesis. Let r bound **every** outer, inner, correction and exact-face coefficient root in the finite canonical combination. Retain the original global physical prime cap 0.19037, the fixed-profile assumptions and the original exceptional majorant.

Set

\[
\xi_*=0.19038,\quad a_*=0.40481,\quad
h_{\rm ex}=\frac{a_*-2\xi_*}{1024},\quad
s_j=2\xi_*+j h_{\rm ex},\quad
z_j=\frac{1-2r-s_j}{2}-10^{-4}.
\]

The stronger convenient range

\[
\frac{4879903}{40960000}<r<\frac{59499}{200000}
\quad (0.1191382568359375<r<0.297495)
\]

makes every auxiliary exponent positive and smaller than 0.19037. Each bin has the identical strict counting slack

\[
s_j+2r+2z_j=\frac{4999}{5000}<1.
\]

The limiting unordered-pair measure has density

\[
f(s)=\frac1s\log\frac{s-\xi_*}{\xi_*}.
\]

This density increases on the required interval. A right-endpoint bound for its 1024 bin masses, the odd degree-21 logarithm upper polynomial, and upward rounding at scale 10 to the power minus 25 give an exact rational upper constant. The resulting exceptional-square estimate has the same full fragment norm as the primary proposition. The detailed proof checks marked-prime separation, exact-face support, nonsquarefree error, and the finite canonical class; it is not a claim for arbitrary coefficient arrays.

| Physical radius r | Exact certified terminating-decimal upper constant | Convenient safe bound |
|---|---:|---:|
| 0.272 | 0.3014041534851816226069683 | 0.301405 |
| 0.2742997 | 0.3273225381113663650584938 | 0.327323 |
| 0.275 | 0.3361336040272905676441604 | 0.336134 |
| 0.276 | 0.3495799968949037559942978 | 0.349580 |
| 0.278 | 0.3800259215656200578230129 | 0.380026 |
| 0.280 | 0.4163697504037337478611794 | 0.416370 |
| 0.282 | 0.4605417963468921175216614 | 0.460542 |

At r=0.275 the script exactly reproduces the paper's fraction

\[
\frac{840334010068226419110401}{2500000000000000000000000}.
\]

Two independent implementations agree on the five radii used in the search. The parametric proof also constructs a downward lower bound on the actual bin constant. At r=0.276 it exceeds 0.3489733171, so this unchanged bin mechanism truly cannot retain 0.34 there. An upper bound exceeding 0.34 alone would not establish that conclusion. No claim is made that every different exceptional-square argument must have this loss.

The constant must be propagated into the hybrid coefficient

\[
b_h=-\frac{49599}{20000000}K,
\]

and all derived costs. The convenient old shortcut \(|b_h|<10^{-3}\) fails with the displayed constants at 0.280 and 0.282. The counting proposition remains valid there, but downstream restoration needs its actual operator bound and coefficient checks. Only radii through 0.278 were used in the present cap search.

## 3. Geometry that preserves the distribution ladders

The screen keeps \(\rho=0.262499\), \(\rho_*=0.2624989\) and imposes

\[
S=r/\rho_*,\qquad T_1=(0.5252997-r)/\rho_*,\qquad T_0=1.997-S.
\]

Thus the old and new combined root sums stay fixed. The nominal distribution ladders remain the same. Their root thresholds, actual grid endpoints, and retained rows do not all remain the same.

For \(\epsilon=10^{-7}/\rho\), put \(A=S+\epsilon/2\) and \(C_\nu=T_\nu+\epsilon/2\). The complementary allocations

\[
\phi_D(t)=\min(3t/2,L_\nu),\qquad \phi_E(t)=3t-\phi_D(t)
\]

give a sufficient natural plateau template when

\[
\frac{3A-C_\nu}{4}\le L_\nu\le\frac{3C_\nu}{5}.
\]

The audit checks the largest-fragment owner and opposite-root inequalities and the nonlargest-witness reduction. Both common-height choices

\[
L_0=L_1=(3A-C_0)/4\quad\hbox{or}\quad L_0=L_1=3C_0/5
\]

preserve both source intervals and nested inner caps. Equal heights avoid an unnecessary extra outer-cap cost caused by the larger new inner radius. This is a valid exact simplification even though the sampled numerical values did not improve.

Fifteen radius/plateau cases were audited: five radii and three choices each. Twelve pass. The unchanged published fraction \(L_\nu/C_\nu=0.575\) fails the natural cap formulas at 0.275, 0.276 and 0.278. Those failures concern this sufficient cap template; they do not invalidate all sieve supports at those radii. The original fraction was used in the numerical screen only where it passes.

At r=0.272 the old inner-square source level 0.5062 is too small. A common replacement \((\omega_s,\delta_s)=(0.0035,0.025)\) gives level 0.507 and satisfies the requisite source and row-12 containment inequalities throughout the screened interval. A rational exponential-sum inequality also rechecks \(C_{\rm op}=4\) at k=39 throughout this interval. No k=40 operator constant is silently inherited.

## 4. An actual numerical-cover obstruction and its repair

At the official 98,304 grid, the untrimmed points r=0.272, 0.275, 0.276 and 0.278 retain new-ladder row 39. Its activation width is approximately \(1.8866250\times10^{-5}\), less than two grid cells. The source theorem is still applicable, but the original low-witness numerical implementation's two-cell guard fails.

Let \(h=S/98304\), \(J_1=\lfloor T_1/h\rfloor\) and

\[
J_O=\min\{98303,\lfloor B_{n,39}/h\rfloor-J_1\}.
\]

Restrict the outer index sum to \(\sum_i j_i\le J_O-k\). This removes at most one outer layer throughout the entire interval \([0.272,0.278]\), excludes row 39, retains row 38, and leaves its activation width greater than two cells. The exact audit proves the uniform statement using endpoint inequalities; it is not an interpolation from the five sampled radii.

The repair keeps h, the normalizer, the convolution length and nominal S fixed. Every erased face must be derived again from the trimmed outer function. **The numerical trials reported here are untrimmed.** Neither their quotients nor the original 97-component numerical cover can be represented as a completed repaired certificate.

Even after trimming, the failure cover must be regenerated from the new source thresholds, caps, core boundaries and same-coordinate terms. All resulting physical integrals need fresh outward evaluation. The old 149 upper integrals and Young-cost values are not transferable solely because the analytic inequalities pass.

## 5. What the finite search found

All configurations retain the original product profile and the 77-dimensional polynomial span. Every vector is optimized afresh. The exact configuration files, full matrices, eigenvectors, conditioning, scalar reevaluations and run times are in the [search archive](../prime-gaps/round5/geometry-trial/).

| Fine-grid candidate | Direct cap quotient | Difference from the Round 4 optimized original geometry |
|---|---:|---:|
| Round 4 original r=0.2742997, original plateaus | 0.9943963993644909 | reference |
| r=0.2742997, common maximum height | 0.9943734016224463 | −22.9977 ppm |
| r=0.275, common maximum height | 0.9943501891039260 | −46.2103 ppm |

Ten coarse configurations covered r=0.272 through 0.278. The only coarse increase over the original baseline, approximately 0.6183 ppm, came from improving the exceptional constant at the unchanged original geometry; it did not come from a radius/plateau change. Only the two nearby geometry candidates above were refined. The full coarse table is preserved in the detailed report.

The scaled Gram condition number reaches approximately \(4.307\times10^{10}\). For the twelve full-77 candidates used in the comparisons above, matrix and direct candidate evaluations disagree by at most \(2.884\times10^{-10}\), and the full scaled-pencil relative residual is at most \(5.30\times10^{-16}\). Across all thirty-six saved candidates, including truncated whitening spaces, those maxima are instead \(3.0281\times10^{-10}\) and \(4.915\times10^{-9}\). This qualifies the scope of the smaller maxima in the original search report. The truncated residual is measured against the full pencil, so it need not be at roundoff scale.

These comparisons support the observed ordering at the tens-of-ppm scale. They do not provide outward error bounds, a certified finite-family maximum, or a no-go theorem for larger trial spaces. The host's NumPy long-double type has only 64 bits; no extended precision is claimed.

The approximately 5604 ppm original k=39 deficit remains far larger than the particular fixed-k=40 credit recovered in Round 4. This comparison guides effort; it does not upper-bound every possible restoration credit.

## 6. Integration verification and next decision

The primary integration replay runs in a temporary copy. It checks the seven exact exceptional constants, all fifteen source cases, twenty grid-mask nesting cases, and the saved twelve 77-by-77 matrix archives with their thirty-six candidate vectors. Source SHA verification is mandatory. Original outputs are preserved; only timing and optional source-text metadata are excluded from exact replay comparisons. See [recheck.py](../logs/round5-integration/recheck.py) and [receipt](../logs/round5-integration/recheck.json).

The 53-file [intake manifest](../prime-gaps/round5/INTAKE_MANIFEST.json) records original and published hashes. The only two code changes made for publication let an external primary-source path be supplied through `PRIME186_SOURCE`. Original per-run manifests remain intact and describe their own execution snapshots.

The next meaningful prime-gap experiment should change a component large enough to affect the k=39 deficit, such as the product profile or an analytically justified support family, or establish a certified upper bound for the currently searched finite family. Repeating these endpoint scans is postponed. Full restored certificates for the present negative candidates are also postponed. This prime-sieve work supports the wider research programme but supplies no new arithmetic transfer theorem for zeta zeros.

This is a checkpoint in an active research goal. The 333-page public handoff remains the earlier `055a4a0` snapshot; Rounds 4 and 5 are separate subsequent reports. No major-conjecture completion is claimed.
