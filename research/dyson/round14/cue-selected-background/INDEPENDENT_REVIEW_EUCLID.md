# Independent review: selected CUE background and the finite heat rate

Date: 2026-09-05. Reviewer: Euclid, the independent conductor-arithmetic agent.

**Decision: accepted for the stated finite-CUE conclusions.** No mathematical defect was found in the selected-background bound, its exact constant, the circular geometry, or the stated probabilistic consequence of the pinned deterministic lemma. This is an ordinary mathematical review, not formal verification or a novelty assessment.

Reviewed author file:
SELECTED_CUE_BACKGROUND.md

SHA-256:
fbc67828d13534d8d0b4ac1f742a639b282dd93a3f7cb635291f8cdbb651c0a5.

The hash was independently recomputed. No author source, numerical check, receipt or previous-round file was modified or rerun.

## 1. The three-point bound and the constant \(1/18\)

The CUE kernel is normalized against ordinary angular Lebesgue measure:
\[
K_N(x,y)=\frac1{2\pi}\sum_{m=0}^{N-1}e^{im(x-y)}.
\]
The Gram-vector norms used in the proof are therefore
\[
A=\frac N{2\pi},\qquad
D=\frac1{2\pi}\sum_{m=0}^{N-1}m^2
\le\frac{N^3}{6\pi}.
\]
The two-point estimate \(ADd^2\) follows by subtracting the first vector from the second; the third-point Gram residual is bounded both by \(A\) and by \(D r(z)^2\). Thus the two coefficients before weakening are exactly
\[
\frac{N^5d^2}{24\pi^3},
\qquad
\frac{N^7d^2r(z)^2}{72\pi^3}.
\]
Replacing the second branch by the weaker coefficient \(1/24\) is legitimate. The displayed minimum bound in the author report follows. For \(N=2\), the rank-three determinant vanishes, so no exceptional formula is required.

The singular integration uses both halves of the circle:
\[
\int_{\mathbb T}q(z)\min(1,N^2r(z)^2)\,dz
\le\frac{\pi^2}{2}
\left[N+N-\frac1\pi\right]\le\pi^2N.
\]
This gives \(N^6d^2/(24\pi)\) for one endpoint. Adding the two endpoints, integrating the starting angle over length \(2\pi\), and integrating \(d^2\) over \((0,\varepsilon]\) gives
\[
\frac1{24}\times2\times2\times\frac13=\frac1{18}.
\]
All powers of \(\pi\) cancel. There is no missing \(1/2\): the determinant is the factorial density of ordered distinct triples, and the oriented short-pair enumeration is the one actually integrated.

The nonnegative integrand makes the initial application of Tonelli valid. The obtained upper bound then proves its finiteness.

## 2. Midpoints, endpoints and circular wrap

The midpoint singularity is handled in the correct order. Only a consecutive pair is replaced by its endpoint majorant; the resulting endpoint-weighted quantity can then be enlarged to all short ordered pairs. Enlarging the midpoint-weighted sum first would not be valid, and the report explicitly avoids that step.

For a consecutive gap with endpoints \(\pm d/2\), \(d\le\pi\), every other point has a midpoint-centered lift \(y\in[-\pi,\pi]\) with \(|y|\ge d/2\). Its distance to the endpoint on its own side is exactly \(|y|-d/2\), lying in \([0,\pi]\). Monotonicity of \(1/(4\sin^2(r/2))\) on that interval therefore gives the claimed midpoint majorant. Third-point coincidence with an endpoint is excluded by the simple-point configuration.

At \(y=\pi\) or \(-\pi\), either admissible lift leads to the same periodic value; choosing a side creates no discontinuity in the inequality. The short oriented pair crossing the original angle cut is included once under the periodic change of variables. Antipodal pair ambiguity has probability zero; the non-strict endpoint \(\varepsilon=\pi\) creates no expectation term.

The integer-frequency kernel is genuinely periodic. Hence an antiperiodic gauge of a sine-kernel representation cannot introduce an extra sign or omit a wrap pair in this proof.

## 3. Selection of the minimum and the extreme-gap normalization

I checked the stated primary normalization against the local text of Feng–Wei, arXiv:1806.01555v2, printed p.4. Its gap process uses the periodic convention
\(\theta_{i+N}=\theta_i+2\pi\). At \(\beta=2\), \(A_2=1/(24\pi)\), and Corollary 1.1 scales the smallest gap by
\[
N^{4/3}(A_2/3)^{1/3}.
\]
Thus the author report's tail
\[
\mathbb P(N^{4/3}\delta_N^{\min}>L)
\longrightarrow e^{-L^3/(72\pi)}
\]
has the correct angular normalization.

On the event that the selected gap is at most \(LN^{-4/3}\), its background is one nonnegative term of the truncated sum. Scaling the finite-\(N\) bound gives exactly \(L^3/18\). Markov's inequality then proves
\[
\limsup_N\mathbb P(B_N/N^2>K)
\le e^{-L^3/(72\pi)}+\frac{L^3}{18K}.
\]
Choosing \(L\) first and \(K\) second proves tightness. Equivalently, for each fixed \(K>1\), taking \(L^3=72\pi\log K\) yields the stated asymptotic upper tail \((1+4\pi\log K)/K\).

There is no conditioning on the identity of the minimum pair. The proof does not claim a finite-\(N\) convergence rate, a limiting background law, or a uniform bound for \(\mathbb E(B_N/N^2)\). These limitations are correctly stated.

## 4. Matching the pinned Galilean lemma

I read Sections 1–5 of the pinned deterministic dependency:

research-round2/galilean-proof-audit.md

SHA-256:
c85684fe873c19c193a81d3d16cde2507f10cf6753324ce31eda99b14672a2da.

The hypotheses match the CUE application exactly:

- A degree-\(N\) polynomial has \(N\) distinct roots on the unit circle, with fixed nonzero leading and constant coefficients.
- The coefficient deformation is \(a_j\mapsto a_j e^{s j(N-j)}\), with the same time parameter \(s\).
- The chosen pair realizes the smallest circular angular gap \(\delta\).
- Its initial background is exactly
  \(B=\frac14\sum_{\text{outside pair}}\csc^2(\theta_k/2)\), measured from the midpoint after rotation. This equals the author's \(B_N\), with no additional endpoint or scaling factor.
- The smallness condition is \(\eta=\delta^2(B+1)\le1/524288\).

The dependency proves the bound with \(K_0=16384\) independent of \(N\) and of the common logarithmic drift. Its real-line Gaussian estimate and moving-boundary argument are already uniform in the drift. The new CUE application therefore does not require a further dynamic-background-stability hypothesis.

The scalar lower comparison is valid whenever the smallest initial gap is \(<\pi\). It gives
\[
D_N\ge-\log\cos(\delta/2)\ge\delta^2/8.
\]
For \(N\ge3\), the minimum is at most \(2\pi/N<\pi\); for \(N=2\), equality \(\delta=\pi\) has probability zero. Consequently the author's nonnegativity assertion outside the good smallness event is justified as well.

The first discriminant time may be caused by another pair. That possibility only strengthens the deterministic upper bound; the application does not assume that the initially smallest pair is the first to collide.

## 5. The \(N^{-2/3}\) rate and its precise meaning

Let \(X_N=N^{4/3}\delta_N^{\min}\) and \(Y_N=B_N/N^2\). Both are tight, and
\[
N^{2/3}\eta_N=X_N^2(Y_N+N^{-2}).
\]
Products of tight random variables are tight without independence. Thus \(\eta_N=O_{\mathbb P}(N^{-2/3})\), and its fixed deterministic smallness condition holds with probability tending to one.

On this event, the pinned lemma gives
\[
0\le \frac{8D_N}{(\delta_N^{\min})^2}-1
\le 8K_0\eta_N.
\]
The exceptional event has probability tending to zero, which is sufficient for the asserted full \(O_{\mathbb P}(N^{-2/3})\) statement. No bound on the magnitude of the error on that exceptional event is needed for tightness.

The almost-sure finiteness remark is consistent: any nonzero interior coefficient eventually violates its bounded unit-circle coefficient size under the stated exponential deformation. Simple self-inversive roots cannot leave the circle before a collision. The exceptional polynomial with all interior coefficients zero has CUE probability zero.

Multiplying the relative error by the tight factor \(N^{8/3}(\delta_N^{\min})^2\) yields the absolute error
\(O_{\mathbb P}(N^{-10/3})\). This is an approximation-error rate, not a rate of convergence to the limiting depth distribution. The report keeps that distinction.

## 6. Verified provenance and remaining scope

Independently recomputed primary hashes:

- Feng–Wei PDF:
  af6c78625ceb76b422fb89ba0f5d98f18c8749ae922244fe386dbfb0133dbce7.
- Its extracted text:
  6b24cd80cede5d71415c4f1cfa527a2c0ef8fd23752549c7455a85945f777ea5.

The review read the exact finite-\(N\) proof, the relevant primary text and the deterministic dependency. It did not rerun the companion script or add a numerical scan.

Acceptance is restricted to the stated CUE proposition, tightness and finite scalar-heat approximation. No general-\(\beta\) determinant bound, true-zeta flow statement, arithmetic transfer, optimal-rate claim or historical-conjecture conclusion follows from this review.
