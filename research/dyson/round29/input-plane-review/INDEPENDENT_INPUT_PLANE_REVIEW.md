# Independent proof and review: a high-frequency Mellin input plane contributes negligibly

Date: 2026-09-05. Reviewer: Plato (`residual_gram`). Status: accepted as an ordinary deterministic projection lemma and its stated RH application. No numerical scan was performed. The coordinator's original note is preserved unchanged as `COORDINATOR_LOG_VECTOR_MELLIN_INPUT_PROJECTION.md`, SHA256 `f808242fbfddfbff337859eb375e6e22934fe2edba1bec11c7c5d822ba675739` (6,544 bytes).

I read the complete coordinator note and the actual statements and proofs around Montgomery–Vaughan Theorem 16.5, Corollary 16.6 and Theorem 16.7 in the retained author-hosted primary draft, printed pages 6–9. I independently rederived the odd-lattice phase factors, the exact Gram matrix and the normalization below. No mathematical correction is required.

The result concerns the **entire input-plane contribution** \(a^{\mathsf T}CP_tb\), not merely the compression \(P_tCP_t\). It does not prove the residual input small, give a strict global covariance bound, or sum an increasing collection of planes.

## 1. Exact statement and mathematical matrix

Let \(T\) be real and sufficiently large, and define
\[
I_T=\{k\in\mathbb Z:k\text{ odd},\ 21T/20<k\le27T/20\},
\quad N=|I_T|=3T/20+O(1).
\]
Set \(b_k=\log k\), and let \(R_t\) have columns \(\cos(t\log k)\) and \(\sin(t\log k)\), indexed by \(k\in I_T\). Let \(P_t\) be Euclidean orthogonal projection onto their real span. Uniformly for \(T\le t\le2T\),
\[
\lambda_{\min}(R_t^{\mathsf T}R_t)\gg T,
\qquad
\|P_tb\|_2\ll\frac{\log T}{\sqrt T}.
\tag{1}
\]
These assertions are unconditional, with constants independent of the choice of \(t\) in the stated interval.

For the application, \(C\) denotes the exact mathematical R28/R27 matrix with its continuum \(b_T\) integral, fixed compact profiles, actual von Mangoldt coefficients including prime powers, and flat odd-endpoint center two. It is not defined by a floating quadrature approximation. For \(X=T^2\), \(\ell=\log T\), and \(a_k=\mu(k)\), the RH consequence is
\[
\left|\frac{2}{T^2\ell^2}a^{\mathsf T}CP_tb\right|
\ll_\eta T^{-1/2+\eta}
\tag{2}
\]
for every fixed \(\eta>0\), uniformly in the same frequency range. Taking any fixed \(\eta<1/2\) makes this contribution tend to zero. The finite R28 frequencies lie in the range, but their observed numerical values are not used in the proof.

## 2. Sharp odd-lattice first-derivative estimate

Write \(k=2j+1\) and use the primary source convention \(e(x)=\exp(2\pi i x)\). The phase for \(k^{it}\) is
\[
\phi(j)=\frac{t}{2\pi}\log(2j+1),
\qquad
\phi'(j)=\frac{t}{\pi(2j+1)}.
\tag{3}
\]
The factor two from the odd lattice cancels the denominator two in the exponential convention. Uniformly on the full real interval spanning the relevant integer indices,
\[
\frac{20}{27\pi}\le\phi'(j)\le\frac{40}{21\pi}.
\tag{4}
\]
Both inequalities include the allowed extreme choices of \(t\) and of the physical endpoints; open lower endpoints only strengthen the relevant bound. The whole interval in (4) is contained in \((1/5,4/5)\). In particular \(\|\phi'(j)\|\ge1/5\), where the double bars mean distance to the nearest integer. There is no unverified alias-free assumption outside this specific range.

The derivative in (3) is decreasing, whereas the source Corollary 16.6 is stated for an increasing derivative. Apply the corollary to \(-\phi\), whose derivative is increasing and has the same distance from the integers, then conjugate the exponential sum. The stated corollary gives
\[
\left|\sum_{j_0\le j\le j_1}(2j+1)^{it}\right|
\le\frac{10}{\pi}
\tag{5}
\]
for any nonempty consecutive subinterval of the odd index set; empty intervals contribute zero. A singleton satisfies the same harmless bound directly. Sharp integer endpoints are retained. The theorem does not approximate the sum by an integral.

The source Theorem 16.5 concerns monotone successive phase increments between \(\Delta\) and \(1-\Delta\), and Corollary 16.6 obtains that condition from the derivative and mean value theorem. Its proof also permits derivatives in any interval between consecutive integers. Consequently the use of the negative derivative here meets the actual source hypotheses.

Let \(A(u)=\sum_{k\in I_T,k\le u}k^{it}\). Partial summation with the real weight \(\log u\) gives
\[
\sum_{k\in I_T}(\log k)k^{it}
=A(k_{\max})\log k_{\max}
-\int_{k_{\min}}^{k_{\max}}\frac{A(u)}u\,du.
\]
There is no lower endpoint term before the first integer. By (5), the absolute value is bounded by a constant times
\[
\log(27T/20)+\log(27/21)=O(\log T).
\]
Thus, uniformly in \(t\),
\[
S_1(t):=\sum_{k\in I_T}(\log k)k^{it}=O(\log T).
\tag{6}
\]

## 3. The doubled phase and exact Gram conditioning

The Gram matrix involves
\[
S_2(t)=\sum_{k\in I_T}k^{2it}.
\]
The doubled first derivative can cross an integer: its full possible range is twice (4), whose upper endpoint exceeds one. Therefore repeating the first-derivative argument would not be valid. The coordinator correctly uses a different estimate.

For the doubled phase,
\[
(2\phi)''(j)=-\frac{4t}{\pi(2j+1)^2}.
\tag{7}
\]
The exact uniform bounds are
\[
\frac{1600}{729\pi T}
\le |(2\phi)''(j)|
\le\frac{3200}{441\pi T}.
\tag{8}
\]
Their ratio is \(162/49\), a fixed constant. The integer interval has length \(O(T)\). Theorem 16.7 applies with \(M_2=1600/(729\pi T)\), a fixed ratio bound, and an integer length parameter of order \(T\). The source explicitly permits negative second derivative by conjugation. It gives
\[
|S_2(t)|\ll M_2^{1/2}T+M_2^{-1/2}
\ll\sqrt T,
\tag{9}
\]
uniformly. No monotonicity of a third derivative or first-derivative separation is required by this theorem.

The trigonometric identities give the exact finite matrix
\[
G_t:=R_t^{\mathsf T}R_t
=\frac12
\begin{pmatrix}
N+\Re S_2(t)&\Im S_2(t)\\
\Im S_2(t)&N-\Re S_2(t)
\end{pmatrix}.
\tag{10}
\]
Its eigenvalues are exactly \((N\pm|S_2(t)|)/2\). Since \(N=3T/20+O(1)\), (9) implies a uniform lower bound by a positive constant times \(T\) once \(T\) is sufficiently large. The proof asserts existence of that threshold, not a numerically certified threshold for the three R28 heights.

For those large \(T\), the columns have full rank and
\[
P_t=R_tG_t^{-1}R_t^{\mathsf T}.
\]
Writing \(z=R_t^{\mathsf T}b=(\Re S_1,\Im S_1)^{\mathsf T}\), the exact projection identity is
\[
\|P_tb\|_2^2=z^{\mathsf T}G_t^{-1}z
\le\lambda_{\min}(G_t)^{-1}|S_1(t)|^2
\ll\frac{(\log T)^2}{T}.
\tag{11}
\]
This proves (1). It uses the full finite Gram matrix; it does not normalize the cosine and sine columns independently or assume they are exactly orthogonal.

## 4. RH application and every normalization factor

The inherited R27 mean-square/Frobenius result, independently reviewed in R27, is
\[
\|C\|_{\mathrm F}^2
\ll_\eta X^{1+\eta}Y(\log X)^2.
\]
The unchanged fixed proportional R28 square is an allowed submatrix of that setting. Restriction cannot increase a Frobenius norm. With \(X=T^2\) and \(Y=T\),
\[
\|C\|_{\mathrm{op}}\le\|C\|_{\mathrm F}
\ll_\eta T^{3/2+\eta}\log T.
\tag{12}
\]
This is an ordinary RH input, not a fit to the finite matrices and not the unproved stronger operator conjecture. All prime powers and the flat center two are already part of the inherited estimate.

Since \(|\mu(k)|\le1\), \(\|a\|_2\le\sqrt N\ll\sqrt T\). Combining this elementary bound with (11) and (12),
\[
\begin{aligned}
\left|\frac{2}{T^2\ell^2}a^{\mathsf T}CP_tb\right|
&\le\frac{2}{T^2\ell^2}
\|a\|_2\|C\|_{\mathrm{op}}\|P_tb\|_2\\
&\ll_\eta\frac1{T^2\ell^2}
T^{1/2}T^{3/2+\eta}\ell\,T^{-1/2}\ell\\
&=O_\eta(T^{-1/2+\eta}).
\end{aligned}
\tag{13}
\]
Both logarithms cancel the original normalization \(\ell^2\). This is also \(O_\eta(X^{-1/4+\eta/2})\). No cancellation of Möbius coefficients was assumed.

The vector inequality controls \(CP_tb\) in the full output space. It neither inserts a projection on the left nor discards \((I-P_t)CP_tb\). The exact identity is
\[
\frac{2}{T^2\ell^2}a^{\mathsf T}Cb
=\frac{2}{T^2\ell^2}a^{\mathsf T}C(I-P_t)b
+\frac{2}{T^2\ell^2}a^{\mathsf T}CP_tb.
\tag{14}
\]
Thus the entire input-plane term is negligible under RH. It is not merely a statement about the real-plane compression observed in R28.

All constants used in (5), (9), (11) and (13) are uniform for \(t\in[T,2T]\). A choice \(t=t(T)\) based on the actual finite matrix therefore remains permitted. Uniformity within this fixed interval does not imply uniformity over frequencies outside it or over an increasing collection of subspaces.

## 5. Consequence and the exact remaining scope

The substantial R28 values of the operator test \(w_t^{\mathsf T}Cw_t\) are compatible with (13). That test uses an oscillatory input, while the true fixed cofactor vector \(\log k\) has the small projection (11) into the same plane. The two statements concern different vectors and are not in conflict.

This is a useful analytic consequence for the actual arithmetic matrix, not another point-process counterexample. It still leaves the residual first term of (14) unestimated. No bound for that residual, for the unbalanced cofactor ranges, for all physical scales, or for the full global covariance follows from this lemma.

The exact orthogonal projector onto a union of several Mellin planes is generally not the sum of their individual projectors. A growing family would require its joint Gram conditioning, the accumulated projection size and a controlled residual. Even a fixed collection needs the relevant joint statement if one wants to remove the full span. Individual bounds cannot be summed as if the planes were orthogonal. No such extension is claimed here.

## 6. Sources, preservation and checks

The primary source is the retained author-hosted draft of Montgomery–Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, [primary PDF](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf), printed pages 6–9. The exact inputs used are Theorem 16.5, Corollary 16.6 and Theorem 16.7, including its negative-second-derivative remark. I reread those statements and the adjacent proofs in the retained extraction. No broader source theorem or unverified aliasing principle is invoked.

The unchanged original coordinator note, primary PDF/extraction, final R27 proof and its independent review are hash-pinned in `REVIEW_RECEIPT.json`. The supplementary small symbolic checker verifies the odd-lattice derivative factors, derivative-range arithmetic, exact Gram characteristic polynomial, projection inverse identity and normalization exponents. It does not numerically sample frequencies, estimate an implicit asymptotic constant, certify a finite threshold, or replace the source theorems.

Accepted scope: the unconditional projection estimate and the RH whole-input-plane bound (13), with the exact residual identity (14). There is no new strict global bound, no asymptotic operator obstruction, and no famous-conjecture claim.
