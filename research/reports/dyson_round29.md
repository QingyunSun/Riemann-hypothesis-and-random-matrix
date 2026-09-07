# Round 29: the actual balanced central Möbius/log pairing is bounded under RH

Date: 2026-09-07 UTC. Status: complete ordinary proof with independent reviews. This checkpoint closes work interrupted by a usage limit. It is a local conditional theorem, not a new global variance bound, an AH contradiction, or a Montgomery–Dyson theorem. External novelty and proof-assistant verification have not been established.

The improvement is specific: R27's growing Frobenius-based estimate for an individual balanced central block is replaced by \(O(1)\), without first bounding the matrix uniformly over all input vectors. The low Mellin interval contributes \(O(1/\log X)\), and every higher frequency is accounted for by summable bounds. The range containing stationary cofactor phases is still only bounded.

## 1. Exact target and theorem

Set \(X=T^2\), \(Y=T\), \(\ell=\log T\). Retain the exact \(b_T\) kernel from [Round 26](dyson_round26.md), the fixed smooth profiles \(\chi,V\) supported in \((1,2)\), and
\[
F(x,h)=b_T(x)\chi(x/X)V(h/Y)(1+h/x)^{-T}.
\]
For sharp odd intervals \(D<d\le2D\), \(K<k\le2K\), with \(D,K\asymp T\), define
\[
Z_{D,K}=2\sum_{d,k\ {\rm odd}}\mu(d)\log k
\sum_{h\ {\rm even}}F(dk,h)[\Lambda(dk+h)-2].
\]
The summation restrictions remain part of this definition. All odd prime powers, the continuous kernel, the product cutoff, and the flat odd-endpoint center \(2\) are retained. No coprimality condition between the factors is inserted.

Under ordinary RH, for fixed profiles and fixed compact comparison ranges for \(D/T,K/T\),
\[
\boxed{Z_{D,K}=O(1).}
\]
The complete [author proof](../dyson/round29/signed-mellin-test/SIGNED_MELLIN_BLOCK_BOUND.md) and [independent full review](../dyson/round29/signed-mellin-review/INDEPENDENT_SIGNED_MELLIN_REVIEW.md) are preserved. The [coordinator review](../dyson/round29/coordinator-central-review/COORDINATOR_CENTRAL_BLOCK_REVIEW.md) refers to its own pinned earlier version; the later change makes the support in one Schur estimate explicit.

## 2. Why the fixed vector can be estimated directly

Define the smooth real extension with the prime endpoint held fixed:
\[
f(x)=X\ell^2\sum_{n\ {\rm odd}}F(x,n-x)[\Lambda(n)-2].
\]
Only finitely many \(n\) occur on the support. Differentiation acts on the smooth window at fixed integer \(n\). It does not differentiate a fictitious function \(\Lambda(x+h)\). At odd integer products \(dk\), the extension is exactly the original even-shift sum.

With
\[
\widehat f(t)=\int_0^\infty f(x)x^{-it}\frac{dx}{x},\qquad
M_D(t)=\sum_{\substack{D<d\le2D\\d\ {\rm odd}}}\mu(d)d^{it},
\]
\[
B_K(t)=\sum_{\substack{K<k\le2K\\k\ {\rm odd}}}(\log k)k^{it},
\]
Mellin inversion gives the exact formula
\[
\boxed{
Z_{D,K}=\frac1{\pi X\ell^2}
\int_{\mathbb R}\widehat f(t)M_D(t)B_K(t)\,dt.}
\]
Both polynomial phases have positive exponent; no adjoint is inserted. The factor \(1/\pi\) includes the original factor two. The integral converges absolutely for each \(T\).

The proof uses only the boundedness and mean-square diagonal of the Möbius coefficients. It has not extracted cancellation specific to their signs. That limitation matters when deciding what to attempt next.

## 3. Two different energy estimates

For each fixed nonnegative integer \(j\), the exact prime-window extension obeys under RH
\[
\int_{\mathbb R}(1+t^2/T^2)^j|\widehat f(t)|^2dt
\ll_j Y(\log X)^2.
\]
At fixed \(n=x+h\), the logarithmic derivative is \(x(\partial_x-\partial_h)\). Each application costs \(T\), and an additional shift derivative costs \(1/Y\). Partial summation expresses the derivative through the exact odd-centered prime-counting increment. The odd staircase and the removed powers of two contribute \(O(1)\) per prefix in this geometry.

The source is the fixed-\(\beta=3\) RH Selberg integral. Its use requires the change of variables \(\lambda=Th/x\), including the Jacobian \(dh=(x/T)d\lambda\), followed by integration over a fixed compact \(\lambda\) interval. This proves the estimate with two logarithms. It supplies no \(Y\log X\) one-block variance.

A separate additional bound is
\[
\int_{\mathbb R}\frac{|\widehat f(t)|^2}{1+t^2}\,dt\ll1.
\]
It uses Cramér's RH mean square
\[
\int_X^{3X}|\Psi(u)-u|^2du\ll X^2,
\]
not the square of the pointwise RH bound.

In detail, put \(A(x)=X\ell^2b_T(x)\chi(x/X)\),
\(k(x,u)=V((u-x)/Y)(x/u)^T\), and
\(S(x)=\int E(u)k(x,u)du\), \(E=\Psi-\mathrm{id}\).
The identity
\[
\partial_xk+\partial_uk=T(1/x-1/u)k
\]
leads, after exact centering, to
\[
f(e^v)=G'(v)+R(v),\qquad G(v)=A(x)S(x)/x.
\]
The fields \(G,R\) include the compact cutoff. A localized Schur estimate over \(x\in[X,2X]\), \(u\in[X,3X]\), together with Cramér's mean square, gives \(\|G\|_2+\|R\|_2=O(1)\). The exact odd-lattice correction and every power-of-two term are retained and bounded. Fourier transformation proves the negative-order estimate.

The [energy companion](../dyson/round29/mellin-energy-support/WEIGHTED_MELLIN_ENERGY.md) and [root's independent review](../dyson/round29/mellin-energy-review/INDEPENDENT_MELLIN_ENERGY_REVIEW.md) record the full derivative and source-range audit. Constants are allowed to depend on fixed \(j\); no growing-order estimate is asserted.

## 4. Every frequency is paid for

Montgomery–Vaughan mean value gives, on any translated interval of length \(R\),
\[
\int_a^{a+R}|M_D(t)|^2dt\ll(R+D)D.
\]
For the sharp odd logarithmic polynomial, first-derivative estimates give
\[
|B_K(t)|\ll \frac{K\log(2K)}{1+|t|}
\quad (|t|\le\pi K/2).
\]
Cauchy over that entire low interval, with the negative-order energy bound, gives an unnormalized contribution \(O(T^2\log X)\), hence
\[
Z_{\rm low}=O(1/\log X).
\]

Outside it, the second-derivative estimate is valid through all stationary aliases:
\[
|B_K(t)|\ll \log(2K)
\left(\sqrt{|t|}+\frac K{\sqrt{|t|}}\right).
\]
On each dyadic band \(R<|t|\le2R\), \(R\ge\pi K/2\), the three factors in the integral have norms at most
\[
T^{j+1/2}(\log X)R^{-j},\qquad
\sqrt{RT},\qquad \sqrt R\log X.
\]
After the exact normalization, their product is \(O_j((R/T)^{1-j})\). Taking \(j=2\) sums all high bands; higher fixed \(j\) gives a tail \(O_j(H^{1-j})\) beyond \(|t|>HT\), for sufficiently large fixed \(H\).

The two logarithms exactly consume the denominator. This is the remaining analytic loss. A sign, a useful strict constant, or an extra logarithmic saving has not been proved.

## 5. A single substantial matrix mode need not couple to the target

A separate [input-plane theorem and review](../dyson/round29/input-plane-review/INDEPENDENT_INPUT_PLANE_REVIEW.md) addresses the fixed R28 interval
\[
I_T=\{k\ {\rm odd}:1.05T<k\le1.35T\}.
\]
Let \(b_k=\log k\) and \(P_t\) be the exact Euclidean projection onto the real span of \(\cos(t\log k),\sin(t\log k)\). Uniformly for every \(t\in[T,2T]\),
\[
\|P_tb\|_2\ll\frac{\log T}{\sqrt T}.
\]
This is unconditional. The first harmonic sum is \(O(\log T)\); the doubled phase needs a second-derivative bound because its first derivative can cross an integer. That bound makes the exact two-by-two Gram matrix have smallest eigenvalue comparable to \(T\).

Combining this with the existing RH Frobenius estimate gives, for the actual mathematical matrix \(C\) and \(a_k=\mu(k)\),
\[
\frac2{T^2\ell^2}a^{\mathsf T}CP_tb
=O_\eta(T^{-1/2+\eta}).
\]
It controls the entire output \(CP_tb\), including its component outside the input plane. The residual \(a^{\mathsf T}C(I-P_t)b\) remains open. The result is uniform enough to permit a data-dependent choice of one \(t\) in the stated interval. It does not authorize adding individual projectors to remove a growing collection of planes.

The [Round 28](dyson_round28.md) selected transpose contractions, at 35–55% of the finite matrix norms, therefore do not contradict this lemma. They use a different input vector.

The exact odd sampling also matters. Adjacent-increment resonances satisfy
\[
t=\frac{2\pi r}{\log(1+2/k)},
\]
while continuous Poisson stationary points satisfy \(t=\pi r k\). They agree at leading scale but are not identical. The original narrow-interval numerical grid stopped near \(2.12T\), below the first continuous stationary band starting near \(3.30T\). The observed winning modes therefore did not examine the difficult stationary log-weight coupling. This observation calls for an analytic estimate, not a larger scan.

## 6. Relationship to the major target

The R26 global reduction already proves, under RH,
\[
\overline V_T=Z_T+2M+o(1),
\qquad
-2M\le\liminf Z_T\le\limsup Z_T\le A-2M.
\]
Thus global \(Z_T=O(1)\) was already inherited from the known variance bound. Round 29 proves a stronger local statement than the earlier individual-block estimate; it does not improve the displayed global bound.

The desired strict gain is still
\[
\boxed{\liminf_{T\to\infty}Z_T<A-2M.}
\]
This would contradict the programme's specified AH-pairs prediction, under the full preceding transfer hypotheses. The proof must control noncentral heights, unbalanced factor ranges, small shifts, and the signed aggregate. An unspecified constant for one central block cannot be summed into this inequality.

The next bounded analytic task is to keep the odd-lattice parity, sharp endpoint corrections and stationary transitions when expanding \(B_K\), then identify and attempt the actual signed prime-error/Möbius correlation. Merely rewriting the same integral with Poisson summation earns no cancellation and will not be described as a breakthrough.

## 7. Verification and recovery record

The final main author manuscript has 16,995 bytes, SHA256 753f116b8ebc5d6cc7d7a4e148c98e9b8ef9df97d4327efe2fa094507aa13492. The final energy companion has 13,239 bytes, SHA256 5b7378c9e4e18881c829883b199dfded12a103945d7a64b72a908343aad013a7. Historical versions and the precise corrections are retained separately.

The main checker has seven groups with 147 exact cases, replayed with complete JSON/stdout matching. The companion has 13 exact assertions, likewise matching its complete output. The independent input-plane note retains its 12 symbolic assertions. These finite checks prevent algebra, parity and normalization mistakes; they are not formal verification of the analytic theorem.

The [closure receipt](../dyson/round29/R29_REVIEW_CLOSURE_RECEIPT.json), [intake manifest](../dyson/round29/INTAKE_MANIFEST.json) and [integration receipt](../logs/round29-integration/INTEGRATION_RECEIPT.json) identify all source and review bytes. A historical energy manuscript recovered by reversing the one recorded wording change is explicitly marked as recovered, with its hash matched to the earlier recorded value; it is not presented as a contemporaneous saved copy.

No new prime-height experiment, numerical frequency scan or PDF build was performed for this checkpoint. The older large PDFs still cover through Round 14; later rounds are separate complete Markdown proofs and reports. No runtime improvement is claimed, so a performance benchmark is not applicable. The substantive risk remains a gap in an ordinary proof or an unjustified later transfer. Reverting this research checkpoint rolls back the publication without rewriting earlier source history. A conjecture announcement, global extrapolation and another large document rebuild remain postponed.
