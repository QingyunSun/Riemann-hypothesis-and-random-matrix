# Independent audit of the actual-zeta short-polynomial identity

Date: 2026-09-05. Reviewer: `yau_flow`, independently of the authoring agent.

**Verdict:** the complete draft `SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md` has been read and its analytic identities independently checked below. The estimates, endpoint conventions, and signs pass. Two optional simplifications were returned to the author; neither repairs a failure of the main claim. This is ordinary internal proof review, not formal verification or external peer review. No numerical integration, parameter scan, or modification of author evidence was performed.

## 1. Statement and exact range

Assume RH. Fix \(c>0\), and for every sufficiently large real \(T\), set
\[
N=\left\lfloor\frac{T}{\log^6T}\right\rfloor,
\quad \sigma=\frac12+\frac{c}{\log T},
\quad H(t)=-\frac{\zeta'}{\zeta}(\sigma+it),
\quad P(t)=\sum_{n\leq N}\frac{\Lambda(n)}{n^{\sigma+it}}.
\]
Put \(D_N=\sum_{n\leq N}\Lambda(n)^2n^{-2\sigma}\). The checked identity is
\[
\boxed{\int_0^T|H(t)|^2dt
=T D_N+\int_0^T|H(t)-P(t)|^2dt
 +O_c(N\log^4T).}
\tag{1}
\]
The implicit constant may depend on the fixed \(c\). Uniformity as \(c\downarrow0\), or for \(c\) varying arbitrarily with \(T\), has not been established. The identity holds for all sufficiently large \(T\); no selection of top-edge heights avoiding zero ordinates is needed.

## 2. Mixed inner product: contour, orientation, and pole

Let \(q(s)=-\zeta'/\zeta(s)\), \(\beta=1+1/\log N\), and
\[
G(s)=\sum_{n\leq N}\Lambda(n)n^{s-2\sigma}.
\]
On the left edge \(s=\sigma+it\), one has exactly
\(G(s)=\overline{P(t)}\). Thus \(q(s)G(s)\), rather than a differently conjugated Dirichlet polynomial, is the required analytic integrand.

Use the rectangle with real parts \(\sigma,\beta\) and imaginary parts \(1,T\). Under RH no nontrivial zero lies in this rectangle. The pole of \(q\) at \(s=1\) lies at height zero, **below** it. Trivial zeros are also outside. Consequently the contour shift contributes horizontal integrals and no residue. The factor \(ds=i\,dt\) on either upward vertical edge preserves the normalization of the diagonal term.

The right-edge Dirichlet series is absolutely convergent. Its diagonal contribution is \((T-1)D_N\). The off-diagonal error is bounded by a constant times
\[
\sum_{n\leq N}\Lambda(n)n^{\beta-2\sigma}
 \sum_{m\ne n}\frac{\Lambda(m)m^{-\beta}}{|\log(m/n)|}.
\tag{2}
\]
The infinite \(m\)-sum is not truncated silently.

## 3. Near-diagonal and far-pair estimates

For \(n/2\leq m\leq2n\), \(m\ne n\),
\[
|\log(m/n)|\geq\frac{|m-n|}{2n},\qquad
n^{\beta-2\sigma}m^{-\beta}\ll n^{-2\sigma}.
\]
Since \(n^{1-2\sigma}=n^{-2c/\log T}\leq1\), the corresponding summand is
\[
\ll\frac{\log^2(2N)}{|m-n|}.
\]
The harmonic sum over \(m\) costs \(O(\log N)\); summing over \(n\leq N\) gives \(O(N\log^3N)\). This directly controls the potentially dangerous neighboring integers without a cancellation assumption.

For the remaining pairs, \(|\log(m/n)|\geq\log2\). Also
\[
n^{\beta-2\sigma}\leq n^{1/\log N}\leq e,
\qquad
\sum_{m\geq2}\frac{\log m}{m^{1+1/\log N}}
\ll\log^2N.
\]
Using only \(\Lambda(m)\leq\log m\) and
\(\sum_{n\leq N}\Lambda(n)\leq N\log N\), the far-pair portion of (2) is likewise \(O(N\log^3N)\). The claimed right-line error therefore holds without prime-pair estimates or cancellation.

## 4. Horizontal sides and the shrinking distance to the zeros

The standard local partial-fraction formula and the local zero-count bound imply, under RH,
\[
q(u+iT)=O_c(\log^2T),\qquad \sigma\leq u\leq\beta.
\tag{3}
\]
Indeed, there are \(O(\log T)\) zeros with \(|\gamma-T|\leq1\), and their distances to this segment are at least \(\sigma-1/2=c/\log T\); the remaining terms contribute \(O(\log T)\). This explains the dependence on \(c\) and remains valid when \(T\) itself equals a zero ordinate.

Uniformly on either horizontal side,
\[
|G(u+it)|\leq\sum_{n\leq N}\Lambda(n)n^{\beta-2\sigma}
\ll N\log N.
\]
The top side has bounded length, so it contributes \(O_c(N\log^3T)\). On the bottom side at height one, a compact meromorphic bound gives \(q(u+i)=O_c(\log T)\), even without using an explicit numerical zero-free height. Hence its contribution is smaller. The pole at height zero does not enter either estimate.

For the omitted interval \([0,1]\), one may use the crude bounds
\[
|H(t)|\ll_c\log T,
\qquad |P(t)|\ll\sqrt N\log N.
\]
They give a mixed contribution \(O_c(\sqrt N\log N\log T)\), which is absorbed by the displayed error. The replacement of \((T-1)D_N\) by \(TD_N\) is also harmless. Thus
\[
\int_0^TH(t)\overline{P(t)}\,dt
=T D_N+O_c(N\log^3T).
\tag{4}
\]

## 5. Polynomial norm and completion of the square

Directly expanding \(\int_0^T|P|^2\) gives \(TD_N\) plus off-diagonal terms. The same near-diagonal estimate just used gives \(O(N\log^3N)\). Away from comparable integers, the absolute bound
\(\sum_{n\leq N}\Lambda(n)n^{-\sigma}\ll\sqrt N\log N\)
suffices. In particular, the author's weaker bound
\[
\int_0^T|P(t)|^2dt=T D_N+O(N\log^4T)
\tag{5}
\]
is valid.

The exact Hilbert-space identity
\[
\|H-P\|_2^2=\|H\|_2^2+\|P\|_2^2
-2\Re\langle H,P\rangle
\]
combined with (4) and (5) proves (1). The main diagonal has coefficient **one**. There is no missing factor of two and no negative sign on the residual norm. With this choice of \(N\), the normalized error in (1) is \(O_c(\log^{-4}T)\) after division by \(T\log^2T\).

## 6. Exact continuation in terms of the prime-counting error

Use the endpoint convention
\[
\psi(N)=\sum_{n\leq N}\Lambda(n),\qquad E(x)=\psi(x)-x.
\]
Partial summation for \(\Re s>1\) gives
\[
\boxed{q(s)-\sum_{n\leq N}\Lambda(n)n^{-s}
=\frac{N^{1-s}}{s-1}-E(N)N^{-s}
 +s\int_N^\infty E(x)x^{-s-1}\,dx.}
\tag{6}
\]
Both the sign of the pole term and the minus sign on the endpoint error are correct. At an integer cutoff, replacing \(\psi(N)\) by its left limit would require adding the missing endpoint prime-power term; the convention above avoids that error.

RH gives \(E(x)=O(\sqrt x\log^2x)\). Therefore the integral converges absolutely and locally uniformly for \(\Re s>1/2\), and the identity extends meromorphically to that half-plane. The only pole at \(s=1\) is explicitly present on the right. Formula (6) is thus a true arithmetic continuation identity at the chosen \(s\), not a formal Dirichlet series outside its convergence half-plane.

Absolute convergence is **not** the desired fine bound on the residual. Writing \(\delta=\sigma-1/2=c/\log T\), its crude absolute majorant contains
\[
|s|N^{-\delta}
\left(\frac{\log^2N}{\delta}
 +\frac{2\log N}{\delta^2}+\frac2{\delta^3}\right).
\]
This can be far too large on \([0,T]\). Cancellation or a genuinely stronger mean-square estimate is still needed for the signed two-scale target.

## 7. Diagonal constant and the unresolved signed residual

PNT and partial summation give, for each fixed \(c>0\),
\[
\frac{D_N}{\log^2T}\longrightarrow
d(c):=\int_0^1u e^{-2cu}\,du
=\frac{1-(1+2c)e^{-2c}}{4c^2},
\]
because \(\log N/\log T\to1\). The two-scale diagonal contribution is exactly
\[
B_{\rm low}=2\{\sinh2\,d(1)-\sinh1\,d(1/2)\}
=0.4560939793292318\ldots.
\]
Writing \(R_c=H_c-P_c\), the remaining requirement for the sufficient threshold \(1/16\) is
\[
\liminf_{T\to\infty}
\frac{2}{T\log^2T}
\left(\sinh2\,\|R_1\|_2^2-\sinh1\,\|R_{1/2}\|_2^2\right)
\geq\frac1{16}-B_{\rm low}.
\]
The right side is \(-0.3935939793292318\ldots\). These decimals are ordinary evaluations of the explicit constants, not numerical zeta data or an outward enclosure. Positivity of each individual squared norm does not establish a lower bound for this signed combination. Identity (1) and continuation (6) make that remaining arithmetic obligation precise; they do not solve it.

## 8. Centered-tail refinement and additional checks of the full draft

The author's global continuation formula
\[
q(s)=\frac{s}{s-1}+s\int_1^\infty E(x)x^{-s-1}dx
\]
also has the correct constant. It specializes to (6) at \(N=1\), since \(\psi(1)=0\) and \(E(1)=-1\). For each fixed \(s\) in the claimed half-plane, the endpoint error and centered tail vanish as the cutoff tends to infinity. Hence the regularized limiting sum in the author's equation (10) is valid. Its convergence is uniform on each fixed compact vertical segment, but a subsequent \(T\)-limit requires preserving that order or proving uniform estimates.

The norm of the explicit pole term at the chosen cutoff satisfies
\[
\left\|\frac{N^{1-s_c(t)}}{s_c(t)-1}\right\|_2^2
\ll_c N.
\]
The author's use of the already reviewed stronger bound \(I_T(c)=O_c(T\log^2T)\) justifies dropping this term from the **normalized residual energy**, including its cross term. There is also a self-contained weaker route: the pointwise RH estimate already used in this proof gives \(I_T(c)=O_c(T\log^4T)\). Together with the elementary polynomial norm bound, this gives \(\|R_c\|_2^2=O_c(T\log^4T)\). Cauchy–Schwarz then bounds the change in normalized residual energy by
\[
O_c\!\left(\sqrt{N/T}+\frac{N}{T\log^2T}\right)
=O_c(\log^{-3}T)=o(1).
\]
Thus this particular removal need not depend on the Round 7 pair/resolvent transfer. This optional simplification was communicated to the author.

The change of variables \(x=Ne^v\), with
\(e_N(v)=E(Ne^v)/(Ne^v)^{1/2}\), gives exactly
\[
\widetilde R_c(t)=N^{-\delta_c-it}
\left[-e_N(0)+s_c(t)\int_0^\infty
e_N(v)e^{-\delta_cv-itv}dv\right].
\]
There is no missing power of \(N\), Jacobian, or endpoint term. Both scales use the same function \(e_N\). This shared arithmetic input must be preserved in any future estimate; treating the two residuals as arbitrarily independent objects would lose information.

The reported GUE orientation formula is consistent with the existing normalization: subtracting
\(d(c)\) from \(V_{\rm sine}(2c)/2=(1-e^{-2c})/(4c^2)\)
gives \(e^{-2c}/(2c)\). This is a conditional model prediction, as the draft states, and was not used to prove the arithmetic identity.

For the bottom contour and initial time interval, the draft's stronger bounds invoke the familiar zero-free low-height compact region. The weaker bounds in §4 of this audit avoid that extra fact altogether, using only RH and finite zero counts on compact sets. They are already sufficient for the claimed error. This was the second optional simplification sent to the author.

## 9. Provenance and scope

The fully inspected author draft has SHA-256
`8840bdfcdfa07baf369deaed39151292ee28ff386f946336f21368d867277305`.
Any later editorial version should retain this review's explicit scope or be checked as a separate delta. The mathematical constants in §7 were independently evaluated from their displayed elementary formulas. The planned numerical check script had not yet been saved when this proof review was completed and is **not** claimed to have been independently reviewed or rerun.

The primary background references used by the author are [Goldston's notes on pair correlation and prime numbers](https://arxiv.org/abs/math/0412313) and [Goldston–Lee–Schettler–Suriajaya's AH paper](https://arxiv.org/abs/2507.06823). The mixed-integral estimate itself was checked directly above rather than attributed to an unstated stronger source theorem. No claim of novelty for the contour method or continuation identities is made.

## 10. Final-version delta acceptance

The frozen final author draft was subsequently inspected and its SHA-256 independently recomputed as
`0067a1b0c7bd4f0b80ef89d6ac85eca1ae99e652375c08c41706ec1f1ddbe40e`.
**This final version is accepted.** The earlier hash in §9 records the initially reviewed draft rather than the final checkpoint.

The bounded delta review checked these changes directly:

- Section 4 now uses the compact RH logarithmic-derivative bound \(O_c(\log T)\) for the bottom side and initial interval, with errors \(O_c(N\log N\log T)\) and \(O_c(\sqrt N\log N\log T)\). Both are absorbed by \(O_c(N\log^3T)\). No low-zero table or exceptional choice of \(T\) is required.
- Section 6 now removes the pole from the normalized residual energy using only \(\|R_c\|_2^2=O_c(T\log^4T)\) and pole norm squared \(O_c(N)\). Its stated error \(O_c(\sqrt{N/T}+N/(T\log^2T))=O_c(\log^{-3}T)\) is correct.
- The source paragraph now correctly separates the RH/PNT inputs for the decomposition from the external significance of the \(1/16\) target. The decomposition and pole removal no longer depend on the stronger Round 7 pair/resolvent estimate.

These changes implement the two simplifications in §8 without changing the diagonal constant, the exact centered-tail identity, or the unproved signed-residual obligation. The author's completed numerical script and result files were not rerun in this delta review; their replay belongs to the coordinator's separate verification. This independent review file is now final.
