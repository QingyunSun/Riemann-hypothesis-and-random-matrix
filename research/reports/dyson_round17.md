# Round 17: test the sieve fluctuation scale and derive the correct quadratic packet

Date: 2026-09-05. Two targeted analytic attempts continue the actual-zeta Dyson–Montgomery programme. The first gives a precise failure of a scalar short-interval sieve cap, with all centering terms retained. The second proves an exact positive energy relation for a compact quadratic packet, while retaining the reflected-zero residues that prevent an incorrect finite-prime-energy formula. Neither proves a strict AH deficit.

## 1. The checked sieve cap loses the fluctuation scale

Keep the same centered prime signal P_x as in the R16 frequency-two target. In logarithmic position v, let A_x(v) be its von Mangoldt sum over (e^v,e^(v+1/T)], let m_x(v) be the exact continuous mean, and set J_x=integral|A_x-m_x|². A positive Fejer time majorant gives the exact Plancherel relation

\[
\int_{\mathbb R}|P_x(t)|^2\operatorname{sinc}^2(t/(2T))dt
=2\pi T^2J_x.
\]

The comparison to [0,T] is a valid inequality for the complete centered signal. It does not compare signed kernel entries separately.

The primary short-interval Brun–Titchmarsh bound gives a local von Mangoldt cap with constant c(alpha)=2alpha/(alpha-1). At alpha=2 the constant is four, because the prime weight contributes log x while the denominator is log(x/T). All higher prime powers are controlled, and separate small-u and remote-tail bounds make the application uniform for alpha in [7/4,9/4].

The exact continuous and mixed moments both have leading value (4/3)x²/T². Keeping the full negative mixed term therefore gives

\[
J_x\le\left[\frac43\frac{\alpha+1}{\alpha-1}+o(1)\right]\frac{x^2}{T^2}.
\]

This is a proved but inadequate upper estimate. At alpha=2 its resulting form-factor bound is (4pi/c*+o(1))T/log T, with c*=sinc²(1/2). It is much weaker than the already proved constant bound for the Bragg bump. The divergent quantity is the right side of this estimate, not the actual statistic.

The cap-times-first-moment inequality controls fluctuations at the scale of the squared mean, whereas the target needs the much smaller mean-times-logarithm scale. Improving the fixed cap to another constant above one leaves the same power loss. The diagnosis is specific to this bounding step; it does not rule out an averaged covariance sieve argument. The full proof, primary-source restriction, exact constants and independent root review are retained in [the sieve report](../dyson/round17/bragg-sieve/BRAGG_SHORT_INTERVAL_CAP_TEST.md) and [review](../dyson/round17/bragg-sieve-review/INDEPENDENT_CAP_REVIEW.md).

## 2. A double-zero packet handles H squared exactly

Under RH, write H=-zeta'/zeta, 1/2<sigma<1, a=1-sigma, b=a/W and

\[
w_2(t)=\frac{(t^2+a^2)^2}{W^4}\operatorname{sinc}^6(t/(2W)).
\]

It is nonnegative, entire, integrable and has double zeros at ±ia. For B6, the density of six uniforms on [-1/2,1/2], its angular Fourier transform is

\[
\widehat w_2(\lambda)=2\pi W[(D^2-b^2)^2B_6](W\lambda),
\qquad\operatorname{supp}\widehat w_2\subset[-3/W,3/W].
\]

A one-contour argument cancels both Laurent terms of H² at one and gives an exactly finite sum with coefficient Lambda*Lambda on Xe^(-3/W)<n<Xe^(3/W). The kernel is signed. Both tilted continuous moments vanish, removing the full pole density log u-2gamma0; compact support removes the endpoint terms. No estimate for the resulting centered arithmetic error is asserted.

At X=1 and W>=3 the arithmetic sum is empty, since Lambda*Lambda first contributes at n=4. Therefore

\[
\int H(\sigma+it)^2w_2(t)dt=0,
\qquad
\boxed{\int|H(\sigma+it)|^2w_2(t)dt
=2\int(\Re H(\sigma+it))^2w_2(t)dt>0.}
\]

This gives a correct exact energy relation. With delta=sigma-1/2, the real part is the difference between the full rational/gamma center and the actual all-ordinate Poisson sum. Squaring yields an exact centered positive pair-kernel representation. The kernel depends on both zero positions through w2 and is not automatically the R16 frequency-two statistic.

## 3. Reflected residues and parameter terms remain essential

For the modulus square, the reflected factor is H(2sigma-s). A right shift beyond the reflected zero line crosses poles at s=2sigma-rho. The report keeps their full residues, the minus2pi contour sign, and a sum over distinct zeros with multiplicity included once. The packet does not cancel the reflected zero family. No vertical line places both H factors in their absolutely convergent prime half-planes when sigma<1. The positive energy therefore has no finite Lambda*Lambda representation supplied by the holomorphic-square identity.

Differentiating sigma also has an exact diagnostic. At X=1,W>=3,

\[
\int2HH'w_2=\frac{16\pi a^2h_6(-ia)}{W^4},
\qquad
\int H^2\partial_\sigma w_2=-\frac{16\pi a^2h_6(-ia)}{W^4}.
\]

Both terms are nonzero and cancel. Omitting the weight derivative would produce an incorrect identity. For W differentiation, sinc^6 supplies only inverse-linear decay of the differentiated weight; the previous absolute-domination argument does not apply. A more rapidly decaying packet or a separate oscillatory argument is required.

See [the complete quadratic proof](../dyson/round17/quadratic-packet/QUADRATIC_COMPACT_PACKET.md), [independent review](../dyson/round17/quadratic-packet-review/INDEPENDENT_QUADRATIC_REVIEW.md), and [root review](../dyson/round17/root-review/ROOT_QUADRATIC_REVIEW.md).

## 4. Evidence and next obligation

The sieve proof has an independent full reading, primary-source range verification and a byte-identical bounded rational-check replay. The quadratic proof has separate root and independent ordinary reviews; any symbolic certificate verifies only the stated finite algebra. No numerical zeta experiment or broad sweep is used. All original research files remain unchanged, and full third-party reference bodies remain local with public hashes.

The R16 target remains positive limsup of one fixed phase deficit; uniform positive liminf is a stronger option. The next necessary ingredient is an actual centered covariance estimate, or a rigorously quantified transfer from the new positive packet to a sufficient correlation test. Repeated scalar prime caps, identifying H² with |H|², and dropping weight derivatives are now documented failed paths.

No new RH, AH-refutation, GUE, zeta-gap or prime-gap theorem is claimed. Postponed: another large PDF rebuild, an unsupported sharp-window replacement, broad numerical scans and global novelty claims. The main risk is applying these exact identities beyond their fixed-parameter scope. Reverting this checkpoint removes the new slice without altering earlier archives.

Archive receipt: 19 originals totaling 480,767 bytes are retained locally; 17 research files are public verbatim. See the [intake manifest](../dyson/round17/INTAKE_MANIFEST.json) and [integration receipt](../logs/round17-integration/INTEGRATION_RECEIPT.json). Both complete bounded JSON/stdout outputs reproduce unchanged, with no excluded fields.
