# Root review of the Round 20 arithmetic and height arguments

Date: 2026-09-05. Verdict: accepted in the stated scopes. This follows a complete root read of both analytic author reports, both analytic cross-reviews, the finite-prime report and all 492 lines of its two scripts. This is an ordinary proof/implementation review, not formal verification or a novelty claim.

## 1. Exact length average and its source dependence

The final length report is pinned at SHA256 cd8c2f7dc48530ed02f915dd202c8aedaaaadb1096cafc019beeb595b9beebbe.

The exact reparameterization \(S=(e^{\lambda/T}-1)^{-1}\), \(r=\log S/\log T\), and weight \(\omega(r\alpha)\) preserve the original prime window. The normalization is \((T/S)r^2\), and the mean remains \((e^{\lambda/T}-1)x\).

For \(0<\lambda\le\sqrt T\), one fixed source exponent \(B\) covers the entire prime window. CCCC (1.3) is explicitly valid for every fixed \(B>1\). It yields the integrable bounds \(\lambda(1+|\log\lambda|)^2\) and \(\lambda\). Above that length range, the centered RH Chebyshev error gives growth \(e^{\lambda/T}\), dominated by \(e^{-\lambda}\) even for finite \(T=2\). Thus existence and the far tail concern the actual centered arithmetic statistic.

On compact length intervals, the moving test is replaced by one fixed test using the positive Selberg mass bound before the fixed-test source formula is invoked. The smoothed zero measures still depend on the length. Their principal prefixes agree by the uniform equality immediately before CCCC (3.9); that equality is distinct from the later plateau inequalities numbered (3.9).

Finite integration by parts differentiates only the explicit kernel. Extreme zero-height tails vanish with all other cutoffs fixed. Intermediate tail constants, after the first height limit, depend on fixed spectral mass and allow removal of length cutoffs before zero-height cutoffs. There is no presumed uniform Schwartz bound for a moving family, derivative of an unknown error, or full limit of the spectral statistic.

The exact averaged kernel \(1/[2(1+y^2)]\) yields probability density \(p(y)=4y^2/[\pi(1+y^2)^2]\). Smooth-square approximation uses common compact support and all-length arithmetic mass bounds; height limits precede removal of the approximation. The result bounds an explicitly different length-averaged statistic. It does not imply an improvement for the old single-length variance.

I rechecked the retained CCCC primary text at (1.3), (3.8) and the equality before (3.9), and Schoenfeld Theorem 10, (6.2), including the threshold 73.2. This root check used text, not a new PDF page inspection. The separate reviewers' page inspections are attributed to them. Inaccessible older general-length formulas are unused.

## 2. Height regularity and the combined strict-deficit criterion

The height report is pinned at SHA256 6048b8792084d1523212ddd5f0c05dcc5b54fb158c3dab37762675e91a1072fe.

The denominator is \(S\log S/(2\pi)\); the physical Lorentzian remains fixed while changing logarithmic scale. The three-sinc envelope has transform \((1-|\alpha|)_+(1+\cos\pi\alpha)\), dominates \(1/[2\pi^2(1+u^2)]\), and has limiting pair mass \(7/3\). It controls the entire Schwartz dilation error from known low-band information, including remote pairs.

At frozen scale, new pair contributions obey \(0\le\Delta S_D\le2\Delta S_0\). After normalization the change is \(X-rD_T+o(1)\), with opposite signs. Keeping them gives \(2A\). Repeating the endpoint argument with the smaller height first gives the same reverse-height control. Thus
\[
|D_{Ty}-D_T|\le2A\frac{|y-1|}{\max(1,y)}+o(1)
\]
is uniform on \([1/2,2]\), with multiplicities and finite-height jumps included in the vanishing error.

For \(d=\limsup D_T>0\), choose heights approaching \(d\) and radius \(r=d/(8A)\). The deficit is eventually at least \(d/2\) throughout that fixed interval. There \(p(y)\ge16/(25\pi)\), so the separately proved length identity gives
\[
\frac{2d^2}{25\pi A}\le A-\liminf_T\overline V_T\le d.
\]
The upper bound uses the eventual upper envelope \(d\) and vanishing probability mass of bounded physical heights. The lower uses one subsequence and a fixed interval; no compatibility with another selected subsequence is assumed. At \(d=0\), positivity closes both inequalities.

The two equivalent strict objectives are a positive Bragg limsup and a strict averaged-variance liminf deficit. Either would exclude full AH-Pairs. The converse from failure of AH-Pairs to this one bump's strict deficit is not proved. Neither strict objective is established.

## 3. Finite-prime implementation and error scope

The finite report is pinned at SHA256 5fd0ecfa3f31785e84e60be55d661f35fbac456bd8038819a9ffc635599677a9; the compute/checker hashes are in the adjacent root receipt.

I read all 321 computation lines and 171 checker lines. The deterministic integer sieve generates primes and repeated powers once. Exact fourth roots set support and initial-staircase lists. Entry/exit keys \(nT,n(T+1)\) are merged in integer coordinates. Subsequent floating event coordinates, logarithms and sums are explicitly unenclosed.

The positive cell formula follows from substituting \(x=L(1+z)\). Its small-term polynomial coefficients alternate correctly, with the stated degree-13 remainder. Both expanded continuous-center terms remain separately in the data. Exact pair-kernel controls use actual prime powers and signed rational coefficients.

The seed recurrence gives conservative rational Simpson bounds protected by \(s_2>1/54\). Layer-cake interval overlaps prove even monotonicity of the autocorrelation. Positive bin masses give endpoint bounds in ideal arithmetic. Full ideal accounting also includes the separate event-series allowance; the floating table is not an interval certificate.

The 70-decimal control uses the same frozen piecewise weight at T=100, with a different antiderivative and independent high-precision prefix logs. It checks numerical stability there, not the complete smooth-weight error at all three heights. The exact identity \(n=p^k\) is checked on all stored entries; independent factorization covers only the stated small range.

Coordinator independently reaggregated all CSV rows and verified file hashes. Root integration repeats only file/row/hash validation, with no new sieve, high-precision run, height or fit. The three values belong to the R19 single-length statistic; they are not values of the new all-length statistic, actual-zero measurements or asymptotic evidence.

## 4. Preservation and conclusion

Both analytic cross-reviews and the coordinator's independently attributed source/computation audits are retained. Historical author headers remain unchanged; later acceptance is recorded separately. The two strict arithmetic/zero targets remain open, and the finite ACUE theorem supplies no missing time-zero transfer.

Before publication, a syntax check caught escaping defects in the root review's first serialization. This file repairs that serialization without changing any author proof, data or mathematical verdict. The old root-only draft is retained locally with a separate hash receipt. The complete PDFs remain at their stated through-Round-14 checkpoint.
