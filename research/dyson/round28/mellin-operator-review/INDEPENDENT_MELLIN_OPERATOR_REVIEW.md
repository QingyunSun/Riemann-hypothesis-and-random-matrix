# Independent review: the exact Mellin operator test and its finite Gaussian comparison

Date: 2026-09-06. Reviewer: Astra root, independent of author Euclid.

Decision: accept the frozen ordinary derivation within its stated scope. The actual discrete, prime and zero identities are unconditional. The Gaussian norm asymptotic is a separate model theorem. Neither proves a new actual-prime norm bound or a strict variance improvement.

The reviewed [author manuscript](../mellin-operator-audit/MELLIN_OPERATOR_AUDIT.md) has 14,373 bytes and SHA256 243994064c74e4fda98ae0aadf7364678e49756f5d282cc36a4a56a134373e7a. I read the full manuscript, its complete bounded checker and source receipt, the actual R27 matrix proof and its independent review. I independently checked the computations below. No author file is changed by this review.

## 1. Discrete normalization and all-frequency scope

The two Mellin vectors have unit Euclidean norm because every real \(t\) gives \(|d^{it}|=|k^{it}|=1\). The transpose identity is
\[
u_t^{\mathsf T}Cv_t
=\frac1{\sqrt{N_dN_k}}\sum_m r(m)f_T(m)m^{it}.
\]
Its bound by the complex operator norm uses the unit vector \(\overline u_t\) in the Hermitian inner product. It does not require replacing the transpose by the adjoint in the displayed pairing.

The grouping counts every ordered pair. In particular repeated products have their exact integer multiplicity \(r(m)\). Product cutoffs remain inside \(f_T\). There is no assumption that the logarithms of the sampled odd indices form an equally spaced grid.

The finite Cesaro identity follows by expanding the square. For unequal products, the average of \(\exp(it\log(m/n))\) tends to zero; for equal products its coefficient is \(r(m)^2|f_T(m)|^2\). No independence of logarithms is needed. This proves the identity for fixed \(X\), but a finite frequency grid cannot enclose the supremum over all real \(t\).

At balanced scales \(\sqrt{N_dN_k}\asymp\sqrt X\), the proposed operator bound \(\|C\|_{\rm op}\ll\sqrt X(\log X)^{1-\delta/2}\) would force author (6). The converse is not established. The sampled Mellin vectors are not a basis with a proved reconstruction norm.

## 2. Exact prime center, powers of two and quadrature

For fixed \(t\), the definition
\[
a_t(x)=\sum_{m\ {\rm odd}}r(m)m^{it}F(m,x-m)
\]
is a finite sum of compact smooth real-variable functions. At odd integers \(n=m+h\), the allowed \(h\) are precisely even. Consequently the author's finite prime pairing is exact, with coefficient \(P_X=X\ell^2/\sqrt{N_dN_k}\).

Separating the odd prime sum from the full von Mangoldt sum removes precisely \((\log2)\sum_j a_t(2^j)\). The continuous center is separated by
\[
L_t=\int a_t-2\sum_{n\ {\rm odd}}a_t(n).
\]
For \(E=\Psi-x\), compact support gives
\[
\sum_n\Lambda(n)a_t(n)-\int a_t
=-\int E(x)a_t'(x)\,dx.
\]
Combining these three exact equalities verifies all signs in author (10). There are no endpoint atoms outside the compact support and no substitution of \(\log(2^j)\) for \(\Lambda(2^j)=\log2\).

The \(x\)-derivatives do not differentiate \(m^{it}\), since \(m\) is the finite summation index. Thus the author's derivative \(L^1\) estimates are uniform in all real \(t\). The odd-lattice Poisson formula has the factor \((-1)^\nu\) and lattice frequency \(\nu/2\). Three derivatives yield \(P_XL_t=O(X^{-1/2})\).

The stated powers-of-two bound uses \(r(m)\ll_\eta X^\eta\) and only \(O(Y)\) contributing \(m\) at a fixed \(x\). There are \(O(1)\) powers of two in the fixed-ratio height window. It gives \(P_XP_{2,t}=O_\eta(X^\eta)\), uniformly. This is a valid intentionally coarse bound; it is negligible compared with the proposed norm scale for fixed \(\eta<1/2\), rather than an assertion that this correction tends to zero.

## 3. Carrier and contour identities

The change of variables \(x=e^v\) gives
\[
\int E(x)a_t'(x)\,dx
=\int e^{-v/2}E(e^v)\,e^{3v/2}a_t'(e^v)\,dv.
\]
This verifies the exponent \(3/2\) in the carrier test. The actual central support lies inside a region where the fixed \(\omega\) is bounded away from zero for large \(T\), so division by \(\sqrt\omega\) is legitimate there. For another weight without this positivity, only the undivided carrier identity would apply.

For the Mellin transform \(\widetilde a_t(s)=\int a_t(x)x^{s-1}dx\), the initial log-derivative expansion is on \(\Re s>1\). The residues of \(-\zeta'/\zeta\) are positive one at the pole \(s=1\), and negative multiplicity at every nontrivial or trivial zero. Since \(\zeta(0)\ne0\), no extra \(s=0\) residue appears.

The author uses a compact smooth test supported strictly above one. Repeated integration by parts in the logarithmic variable gives rapid vertical decay, which makes the zero sum absolutely convergent using the usual zero count. In the contour proof, first fix a left boundary away from trivial zeros and take the upper and lower limits along heights avoiding nontrivial zeros; then move the left boundary through negative odd integers. The functional equation controls the logarithmic derivative there, and the factor from the support \(x>X>1\) pays the decay as the boundary moves left. These are ordinary contour limits, not a Dirichlet-series expansion on the critical line.

The resulting smoothed explicit formula and the odd correction give
\[
\mathcal M_T(t)=P_X
\left(L_t-P_{2,t}-\sum_\rho\widetilde a_t(\rho)
-\sum_{j\ge1}\widetilde a_t(-2j)\right).
\]
The original continuous center therefore cancels the pole through the exact lattice correction. The trivial-zero estimate is \(O(YX^{-5/2})=O(X^{-2})\) after multiplication by \(P_X\), as stated.

Substitution \(x=m+Yz\) directly verifies author (20), including \(m^{s-1+it}\), the factor \(Y\), and exponent \(s-1-T\). Under RH one may then use \(s=1/2+i\gamma\). Seeing \(m^{i(t+\gamma)}\) does not justify discarding all other frequencies, replacing multiplicities with a smooth density, or claiming a band projection. Those would need new estimates for the actual discrete set.

I also reopened the primary [NIST definition and continuation statement](https://dlmf.nist.gov/25.2), [functional equation](https://dlmf.nist.gov/25.4.E2), and [integer value at zero](https://dlmf.nist.gov/25.6.E1). These support the standard analytic ingredients just used; the new arithmetic pairing and its bounds are not attributed to NIST.

Dividing the proposed operator scale by \(P_X\) gives \((\log X)^{-1-\delta/2}\). The lattice, powers-of-two and trivial-zero bounds are smaller than this scale after the same division. The necessary zero estimate (21) is therefore correctly normalized. It remains unproved. The existing weighted heat norm does not bound this whole arithmetic test family without its dual multiplier norms.

## 4. Exact finite Gaussian theorem

For odd \(N\), reflecting one column index converts the cyclic Hankel matrix to a circulant. The unitary Fourier transform of the independent real Gaussian coordinates has one real coordinate and \((N-1)/2\) independent complex coordinates, with their conjugates.

Thus the normalized squared singular norm is the maximum of one \(\chi_1^2\) variable and \((N-1)/2\) independent exponential variables of mean one. This proves the displayed CDF. The exponential maximum has mean \(H_{(N-1)/2}\), while adding the real square increases the upper bound by at most one. Both expectation inequalities are valid.

The exponential maximum divided by \(\log N\) tends to one in probability; the single real square divided by \(\log N\) tends to zero. At \(X=N^2\), \(\sigma^2=N\log X\), the normalized constant is \(1/2\). It follows that every fixed logarithmic power saving in the stated uniform model norm fails in probability.

For deterministic sample-independent unit vectors, the convolution coefficient formula gives mean square at most \(N\sigma^2\). A matching Fourier pairing attains that scale. The word “matching” matters: arbitrary distinct Fourier basis vectors can instead give zero. The final manuscript has this qualification. The fixed normalized contraction tends to zero in \(L^2\) even though the uniform norm does not.

Every statement in this paragraph concerns the defined cyclic Gaussian model. Its independence, periodic wrap and index geometry have not been proved for primes. In particular this theorem cannot refute the actual R27 operator target.

## 5. Interpreting the numerical test

Projection of one leading eigenvector onto a cosine/sine plane is different from the necessary transpose test. For instance, on an orthonormal real plane where \(C=I\), the vector \(w=(q_c+iq_s)/\sqrt2\) has \(w^{\mathsf T}Cw=0\), although the plane projection is complete. An adjoint computation would produce a different quantity.

The separate R28 numerical follow-up correctly computes the transpose at its already selected frequencies, and does not treat the grid as an all-real enclosure. This review does not verify the prime arrays or quadrature in that experiment; its independent numerical review does so separately. Neither observation is an actual asymptotic bound.

## 6. Reproduction and accepted limits

The attached source-and-replay receipt checks every declared source and author artifact against its bytes and hash. An unchanged copied checker, with the exact manuscript supplied as its hash input, reproduces both whole outputs. It verifies 56 finite identities in six groups, including exact nonzero powers-of-two corrections. These are algebraic regression checks; they do not prove contour estimates or an unproved arithmetic norm bound.

The accepted result is a precise necessary test for a uniform matrix strategy and a rigorous warning from one separate model. The fixed Möbius/log pairing remains the weaker relevant target. No strict actual variance saving, famous conjecture, novelty certification or proof-assistant completion follows from this review.
