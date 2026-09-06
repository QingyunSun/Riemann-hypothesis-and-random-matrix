# Independent root review: the finite arithmetic kernel and fixed-bump Tauberian theorem

Date: 2026-09-05. Verdict: both complete ordinary proofs accepted in their stated scopes. Root read both final reports, both entire symbolic checkers, and the exact Wiener primary statement. This review does not concern root's separately authored heat-energy proof, which has its own independent reviewer.

## 1. Actual all-length arithmetic and convergence

The complete Plato report is pinned at SHA256 bf2e13a5d62f694d638d247fe7d836d0ea57d47f15c8e9360843681ece6b58d9, 17,082 bytes.

The change from exponential length to endpoint ratio gives exactly \(Tq^{-T-1}dq\). The survival, mixed and mean-square moments are correct. For \(T>2\), \(\Psi(y)\le y\log y\) bounds all three expanded integrals absolutely, allowing their separation and the outer integration over the fixed compact prime window. The total variation argument for the signed \(dE\) kernel also converges in precisely this range.

I independently checked the outer weight moments: the first mixed term uses \(J_T(n)n^{1-T}\), and the second uses \(J_{T+1}(n)n^{-T}\). The ordering by the larger prime-power index removes the duplicated diagonal with \(-\Lambda(n)\); the remaining center combines to \(-2n/(T-1)\). The signed \(E(n)-E(x)\) term and both continuous centers remain.

## 2. Finite truncation is a coherent endpoint truncation

Cutting \(qx\) at \(N\) gives a nonnegative portion of the original centered variance. The finite pair kernel is the original survival minus \((x/N)^T\); the mixed kernel subtracts the same endpoint moment; the continuous coefficient also has three endpoint corrections. I checked all powers in the complete outer formula (17). Deleting only prime indices from the infinite formula would not give this positive truncation.

The exact tail is a positive integral of \(G_x(y)^2\). The elementary majorant \(y^2(1+\log y)^2\) gives the displayed \(P_2\) formula. At \(N_0=2U\), the three rational bounds yield \(13005/8<2048\). Ceiling the endpoint decreases the actual positive tail. Thus the unconditional error
\[
0\le\overline V_T-\overline V_{T,\lceil2T^{9/4}\rceil}
\le2048T^{9/4}2^{-T}
\]
is valid for all real \(T\ge3\). This proves equivalence of limiting criteria with a finite arithmetic functional, not a strict bound for that functional.

## 3. The centered boundary regrouping is distinct

At \(T=2\), each separated uncentered positive term diverges. The centered RH energy is finite. The finite continuous kernel has the stated logarithmic limit and vanishes at \(N=x\).

For the Stieltjes formula, right-continuous evaluation gives the jump
\(2G_x(n)\Lambda(n)-\Lambda(n)^2\). The negative endpoint
\(-(x/N)^TG_x(N)^2\) is necessary, especially if \(N\) itself is a prime power. The checker deliberately tests such an occupied cutoff and detects the failure when the endpoint is omitted.

Under RH the signed discrete and continuous terms converge absolutely for \(T>3/2\), while the boundary vanishes for \(T>1\). The report does not conflate these two ranges. At \(T=2\), the Laurent constant gives
\(\int_1^\infty E(y)y^{-2}dy=-\gamma-1\).
Subtracting the finite integral and \(E(x)/x\) gives exactly
\[
\int_x^\infty(E(y)-E(x))y^{-2}dy
=\log x-\gamma-\sum_{n\le x}\Lambda(n)/n.
\]
The resulting centered formula has the correct sign \(-2x^2\) on this expression. It retains a signed \(\Lambda E\) tail. The separate RH \(P_4\) tail formula is also correctly normalized. No numerical constant for the global RH bound is silently supplied.

The full checker confirms finite direct/event, pair/mixed/continuous, and Stieltjes expressions on both prime-power and signed rational controls. It checks the elementary tail primitives and constants. Those finite checks are separate from the ordinary convergence proof.

## 4. Exact fixed-bump Tauberian inversion

The complete Aquinas report is pinned at SHA256 3f3391cb149b69e86d6c758267eec56ae9d86f7523f2dcf078f6f351ff9ee48c, 13,500 bytes.

The theorem is one scalar fixed-bump assertion under RH:
\[
\overline V_T\to c\quad\Longleftrightarrow\quad
C_T\to c\quad\Longleftrightarrow\quad D_T\to A-c.
\]
It concerns full convergence through real heights. It asserts neither existence of a limit nor a numerical value for it.

I checked that \(f(x)=C_{e^x}\), with the declared bounded extension below \(\log2\), is measurable and bounded. R20's uniform height estimate, combined with \(C_0(T)\to A\), gives the pointwise representative's asymptotic uniform continuity. No finite zero-height jump is excluded.

For standard convolution, the kernel is the reflection \(K(u)=q(-u)\). The Mellin transform is
\[
\widehat K(\tau)
=\frac2\pi\Gamma((3+i\tau)/2)\Gamma((1-i\tau)/2)
=\frac{1+i\tau}{\cosh(\pi\tau/2)}.
\]
Both beta-integral parameters have positive real part. Gamma recurrence and reflection give the displayed sign and normalization. The real Fourier transform never vanishes.

I directly read Theorem 1 on page 2 of the retained van Neerven author-hosted preprint. It states density in \(L^1(\mathbb R)\) of the linear span of translates of an \(L^1\) function with nowhere-vanishing Fourier transform. Root used the retained primary text; the separate author source-page inspection is not attributed to root.

The application is spelled out correctly. Convergence of \(K*f\) gives convergence for every fixed finite combination of translated kernels. The \(L^1\) error is controlled by \(\|f\|_\infty+|c|\), giving convergence for every fixed \(L^1\) test. A fixed compact probability kernel is then removed using asymptotic uniform continuity. Height tends to infinity before its width tends to zero. No differentiability, \(L^1\) assumption on \(f\), or formal division of distributions is used.

The reverse direction is ordinary dominated convergence. The restriction \(0\le c\le A\) follows from the existing spectral bounds. The argument cannot invert convergence on an arbitrary subsequence because all fixed translates need convergence; the report explicitly retains this limitation.

## 5. Stability and research scope

The exponentially decaying Fourier multiplier has no bounded linear inverse on all bounded functions. Pure waves show this directly; rescaled waves preserve a fixed Lipschitz bound while keeping the same unbounded norm ratio. These are functional-analytic examples, not constructed zeta processes. They do not rule out every nonlinear conditional recovery bound.

The result is a classical Wiener application for one fixed smoothing. It is not a new proof of the Goldston–Montgomery conjectural asymptotics, does not determine the whole pair measure, and does not turn AH failure into this bump's deficit. The sine value remains a conjectural scalar target. The missing assertion in both reviewed reports remains an actual strict arithmetic estimate.

The copied checker replays, dependency hashes and final source pins are recorded separately. They validate finite algebra/provenance; ordinary source and limit arguments are checked in this review.
