# Independent review of the compact quadratic zeta packet

Date: 2026-09-05. Reviewer: Aquinas (`/root/yau_flow`). Status: **accepted as an ordinary analytic derivation**, after checking the final multiplicity clarification. No formal proof-assistant verification, numerical zeta estimate, or strict Bragg bound is claimed.

Final author file: `research-round17/quadratic-packet/QUADRATIC_COMPACT_PACKET.md`, 16,688 bytes, SHA-256
`a7b5290a3d96d2590da42f3fe13a53c1e02499b53d066366824b9f15883a7da3`.
Author receipt SHA-256:
`3739426094b514defccb42ef2ceb50cf7ce71c4aa91cbc731d325331904c36ff`.
No author files were modified during this review.

## 1. Accepted result and its limitation

I independently checked the complete report, including the Fourier normalization, both contour shifts, all pole and endpoint terms, paired-xi centering, and the parameter derivative identities. The following distinctions are essential to the acceptance:

- The compact **holomorphic-square** formula is a finite sum with coefficient \(C_2=\Lambda*\Lambda\); it is not a formula for the modulus-square energy.
- At carrier \(X=1\), \(W\ge3\), this finite sum is zero, whereas the modulus energy is strictly positive. Nevertheless the zero holomorphic integral proves the exact equality of the modulus energy with twice the real-part square.
- The real-part square has an exact centered zero-pair expression, with all ordinates, the gamma center, and the particular time weight retained. Its value is not evaluated by the empty arithmetic sum.
- A reflected-factor contour crosses the nontrivial-zero line for the stated choice of final contour. Its residues must be retained, with multiplicity counted exactly once.
- The two pieces obtained by differentiating the holomorphic identity in sigma have equal and opposite **nonzero** integrals. Fixed-W differentiation of the positive energy also requires its weight-derivative term.

Thus the note supplies valid actual-zeta identities and rules out particular incorrect substitutions. It does not establish the strict actual-zeta inequality in R16, and it does not convert a finite multiplicative prime-product calculation into an evaluation of additive prime covariance.

## 2. Compact Fourier kernel and its constants

Write \(a=1-\sigma\), \(b=a/W\), and \(\operatorname{sinc}z=\sin z/z\). The six-fold convolution of the unit-density interval \([-1/2,1/2]\) has characteristic function \(\operatorname{sinc}(t/2)^6\). Scaling and the transform convention \(\widehat w(\lambda)=\int w(t)e^{-it\lambda}dt\) give
\[
\widehat{\operatorname{sinc}(t/(2W))^6}(\lambda)=2\pi W B_6(W\lambda).
\]
Each multiplication by \(t^2\) becomes minus a second derivative in lambda. Accounting for the factor \(W^{-4}\) in the packet therefore yields exactly
\[
\widehat w_{2,a,W}(\lambda)
=2\pi W\left[B_6^{(4)}-2b^2B_6''+b^4B_6\right](W\lambda).
\]
There is no missing power of W or factor of \(2\pi\). The support is \([-3/W,3/W]\). Since \(B_6\) is \(C^4\) and its derivatives through order four vanish at the external endpoints, the kernel itself is continuous and zero there. An integer at either endpoint of the finite arithmetic window contributes zero.

Independent exact differentiation of the truncated-power expression gives
\[
B_6(0)=11/20,\quad B_6''(0)=-1,\quad B_6^{(4)}(0)=6,
\]
and hence \(\int w=2\pi W(6+2b^2+11b^4/20)\). The values at one in the report similarly give
\(K_{2,b}(1)=-4-2b^2/3+13b^4/60<0\) in the relevant range. Positivity of the real time weight is consequently compatible with a signed Fourier kernel. The report does not discard its negative entries.

The stated decay is sufficient for the contour arguments: on a fixed horizontal translate the degree-four polynomial times sinc to the sixth power is \(O(|t|^{-2})\). Six is the smallest even power with this integrable polynomial decay for the specified multiplier; no broader optimality claim is made or accepted.

## 3. The holomorphic-square contour and complete pole density

For \(H=-\zeta'/\zeta\), the expansion at one is
\[
H(s)^2=(s-1)^{-2}-2\gamma_0(s-1)^{-1}+O(1).
\]
The weight composed with \(t=-i(s-\sigma)\) has a double zero at \(s=1\). It cancels both principal terms. Under RH there are no other poles between the initial line \(\Re s=\sigma>1/2\) and a fixed line \(\Re s=c>1\). The fixed-strip logarithmic-derivative bound, together with the packet decay, supplies absolute convergence and vanishing horizontal integrals. Constants are allowed to depend on the fixed distance \(\sigma-1/2\).

The arithmetic expansion is performed only on the absolutely convergent c-line. With \(d=c-\sigma\), \(\lambda=\log(n/X)\), the entire-weight shift gives
\[
\int w(t-id)e^{-it\lambda}dt=e^{d\lambda}\widehat w(\lambda),
\qquad X^dn^{-c}e^{d\lambda}=n^{-\sigma}.
\]
This verifies equation (8), including its finite support and normalization. The convolution coefficients start at \(n=4\); the prime-power and two-distinct-prime formulas in equation (10) count the ordered factorizations correctly. They are not \(\Lambda(n)^2\).

For the centered version, integrating the compact spline by parts gives
\[
\int e^{zy}K_{2,b}(y)dy
=(z^2-b^2)^2\left(\frac{\sinh(z/2)}{z/2}\right)^6.
\]
Both its value and its first z-derivative vanish at \(z=b\). These two equalities annihilate the complete density \(\log u-2\gamma_0\), after \(u=Xe^{y/W}\). Keeping only the first equality would not suffice for the double pole. The report retains both.

The primitive used for Stieltjes centering has the correct sign:
\[
E_2(u)=A_2(u)-u\log u+(1+2\gamma_0)u.
\]
The compact test F is continuous, absolutely continuous, and zero at both support endpoints, so \(\int F\,dE_2=-\int E_2F'\) has no surviving external boundary term, even if an endpoint is an integer. The piecewise-polynomial derivative of the Fourier kernel has jumps, but F itself is continuous; a first integration by parts therefore creates no extra point masses. An interior truncation would have its own boundary terms, as the author explicitly notes. No estimate for \(E_2\) is inferred.

## 4. Empty sum, positive energy, and paired-xi centering

At \(X=1\), \(W\ge3\), the upper arithmetic endpoint obeys \(e^{3/W}\le e<4\). Since \(C_2(n)=0\) below four, the finite sum is empty. Thus \(\int H^2w=0\) exactly. The modulus energy is finite and strictly positive: w is positive outside a discrete real set, and an analytic H cannot vanish on the whole vertical line without vanishing identically, which contradicts its pole at one.

The elementary identity
\[
2(\Re H)^2=|H|^2+\Re(H^2)
\]
then proves the factor two in equation (17). The imaginary-part square has the same integral, and the real-imaginary cross integral vanishes. This is a packet-specific exact identity; it is not obtained by replacing a complex square by a modulus square inside the arithmetic formula.

I also checked the canonical-product and gamma normalization against the retained R7 source sections 5–6, and independently through the paired product. Under RH, the evenness of \(\xi\) about \(1/2\) fixes the constant in the product paired over positive and negative ordinates. Its real logarithmic derivative is
\[
\Re\frac{\xi'}{\xi}(\sigma+it)
=\sum_\gamma\frac{\delta}{\delta^2+(t-\gamma)^2},
\qquad\delta=\sigma-1/2.
\]
Here the ordinate sum counts multiplicity. Its real terms are absolutely summable. Differentiating the defining gamma factors of xi gives precisely the center \(G_\sigma\) in equation (18), so \(\Re H=G_\sigma-R_\delta\), with no asymptotic replacement of the center.

For fixed \(\delta>0\), unit-interval zero counting bounds \(R_\delta(t)\) by a constant depending on delta times \(\log(|t|+2)\); \(G_\sigma\) has the same allowed growth. The \(t^{-2}\) packet decay then makes all displayed centered square terms integrable. The positive double zero sum is justified by Tonelli, and the mean-cross terms by absolute convergence. Negative ordinates and all tails remain in the identity. This checks equation (21) without imposing stationarity or a finite-zero approximation.

## 5. Reflected contour: endpoint range, signs, and multiplicity

The identity \(\overline{H(s)}=H(2\sigma-s)\) holds on the initial line. The choice
\[
\max(1,2\sigma-1/2)<c<2\sigma
\]
is important. It crosses the full reflected nontrivial-zero line for every \(1/2<\sigma<1\), and places the reflected argument on a final real part strictly between zero and one half. Merely asking for \(c>1\) would not ensure this crossing when \(\sigma>3/4\). The final report uses the stronger, correct condition.

The pole inventory is complete. The unreflected pole at one is canceled; the reflected real pole is left of the starting contour; unreflected zero poles are left under RH; reflected trivial zeros are right of c. At \(s_\rho=2\sigma-\rho\), a zero of multiplicity \(m_\rho\) gives residue \(+m_\rho\) for the reflected H factor. Thus the full residue is
\[
\mathcal R_\rho=m_\rho H(2\sigma-\rho)X^{\sigma-\rho}
w_{2,a,W}(-i(\sigma-\rho)).
\]
The weight does not vanish there: its argument is \(-\gamma-i\delta\), off both its real sinc zeros and its two polynomial zeros. The other H factor could vanish accidentally, which can remove an individual product residue; the report correctly permits this possibility rather than asserting every residue is nonzero.

With upward vertical contours, the contour formed by the left side upward and the right side downward is clockwise. Hence the difference of the s-integrals is \(-2\pi i\) times the residue sum; conversion from ds to \(i\,dt\) gives the **minus \(2\pi\)** in equation (24). The carrier and shifted-weight factors on the final line are correct.

The final report now explicitly sums equation (24) over **distinct nontrivial zeros**, since equation (23) already includes \(m_\rho\). This is different from the multiplicity-counted ordinate series in the positive kernel of section 4. I checked the final clarification in both places, so no second multiplicity factor is introduced.

The convergence argument is sound for fixed parameters. Unit-interval zero counting permits horizontal heights at distance at least a constant divided by log height from the zero ordinates. The logarithmic derivatives on those segments have logarithmic-power bounds, and the packet contributes \(t^{-2}\). The final vertical line stays a fixed distance from the RH zero line. Residue magnitudes are dominated by \(\gamma^{-2}\) times a fixed logarithmic power, summable with the standard zero count. No uniformity as delta tends to zero has been proved here.

For \(X\ne1\), the carrier makes this modulus-square integral a signed cosine integral. Only \(X=1\) gives the positive energy. Also, no contour places both H factors in their absolutely convergent Dirichlet half-planes when \(\sigma<1\). In the separate region where two expansions are legal, the product with a conjugate imposes a ratio restriction on infinitely many pairs, not the finite product restriction in \(C_2\). The report keeps this arithmetic distinction.

## 6. Sigma derivatives and the separate W issue

I independently derived the residues in the local t coordinate \(u=t+ia\), allowing generic regular Laurent coefficients of H and a generic first derivative of the sinc factor. With \(S=h_{6,W}(-ia)\),
\[
\operatorname{Res}_{t=-ia}(H^2w_2)=0,
\]
\[
\operatorname{Res}_{t=-ia}(2HH'w_2)=8ia^2S/W^4,
\quad
\operatorname{Res}_{t=-ia}(H^2\partial_\sigma w_2)=-8ia^2S/W^4.
\]
The real-t contour moved downward contributes \(-2\pi i\) times these residues. At \(X=1\), \(W\ge3\), both right-line arithmetic sums are empty because the differentiated coefficients still begin at four and the Fourier support is unchanged. This proves the nonzero integrals \(+16\pi a^2S/W^4\) and \(-16\pi a^2S/W^4\) in equations (27)–(28), with their displayed signs. These calculations do not depend on the regular Laurent coefficient \(-\gamma_0\).

For sigma in a fixed compact subinterval of \((1/2,1)\), the original H and its derivative have logarithmic-power bounds on the line, while the weight and its sigma derivative have integrable polynomial decay. Differentiation of the positive energy at fixed W is therefore justified and necessarily includes the \(\partial_\sigma w_2\) term in equation (26).

The report correctly treats W differently. Differentiating the sinc phase costs one power of t, leaving only \(O(1/|t|)\) decay in the new term for the sixth-power packet. The previous absolute-domination argument therefore does not apply. No differentiated W-energy formula is accepted on that basis alone. The stated eighth-power alternative would supply the stronger decay, but no further result is asserted from it.

## 7. Utility, verification, and frozen evidence

The finite holomorphic formula is a legitimate narrow multiplicative prime-product identity. The positive zero-energy relation is also legitimate. Their combination does not evaluate the positive energy: in the illustrative empty-sum case the holomorphic value is zero while the positive value remains an unknown, nonzero centered square.

The positive pair kernel depends on both ordinates through the time weight. It does not automatically become R16's difference-only Lorentzian pair statistic with a fixed bump near frequency two. A transfer would still need quantified scaling in delta and W, the gamma center, control of negative/high ordinates and time-window changes, and frequency localization with signs preserved. The fixed-parameter identities supply none of the missing uniform estimates by themselves. This is the precise utility boundary accepted here.

The independent bounded script `check_local_residues.py` was saved and executed in this review directory. It verifies exact Laurent residues with generic regular coefficients and the exact central B6 derivatives. Its JSON and log are also retained. This is symbolic normalization evidence, not a proof of RH, a numerical zeta integral, a parameter sweep, or a proof of the contour estimates. The analytic justification is the review above. The author intentionally supplied no numerical checker for this slice.

The accompanying receipt independently pins the final author report and receipt, all three retained dependencies, this review, and the symbolic script/output. All reported input hashes and byte counts were checked from disk. The only final author delta after the full initial read was reviewed explicitly, including the distinct-zero convention and the harmless observation that the reflected real pole also lies at the packet's other double zero.

**Outstanding:** a strict actual-zeta Bragg deficit, or another genuinely new arithmetic estimate connecting these exact packets to the desired pair statistic. It remains unproved.
