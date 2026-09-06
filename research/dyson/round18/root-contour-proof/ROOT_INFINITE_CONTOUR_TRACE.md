# Independent right-line proof of the compact quadratic trace closure

Date: 2026-09-05. Author: root Astra. This is a complete ordinary proof of a fixed-parameter identity, offered for independent review beside the R18 digamma derivation. It does not supply a strict Bragg estimate or a new claim of priority.

Assume RH, 1/2<sigma<1, a=1-sigma and W>3/log 2. Let H=-zeta'/zeta and use the frozen R17 packet

\[
w_2(t)=(t^2+a^2)^2 W^{-4}\operatorname{sinc}^6(t/(2W)).
\]

Every nontrivial zero rho below is distinct, with multiplicity m_rho included explicitly. Define

\[
S_{\sigma,W}=\sum_{\rho\ \mathrm{distinct}}
 m_\rho H(2\sigma-\rho)w_2(-i(\sigma-\rho)),
\quad
Q_{\sigma,W}=\sum_{k\ge1}H(2\sigma+2k)w_2(-i(\sigma+2k)).
\]

Then both sums converge absolutely, S is real by conjugate pairing, Q is strictly positive, and

\[
\boxed{\int_{\mathbb R}|H(\sigma+it)|^2w_2(t)dt
=-2\pi(S_{\sigma,W}+Q_{\sigma,W}).}
\]

For W>=6, Q=O(W^(-4)) uniformly for 1/2<sigma<1. The nontrivial sum is not evaluated or bounded by a new arithmetic estimate.

## Proof

Start with H(s)H(2sigma-s)w_2(-i(s-sigma)) on the upward sigma line. The unreflected pole at s=1 and the reflected real pole at s=2sigma-1 are canceled by the packet zeros; the latter is also left of the initial line. Under RH all unreflected zero poles are left. Reflected nontrivial zeros occur at s=2sigma-rho, with full residue m_rho H(2sigma-rho)w_2(-i(sigma-rho)). Reflected trivial zeros at s=2sigma+2k have residue H(2sigma+2k)w_2(-i(sigma+2k)), since each trivial zero is simple. A zero of the other H factor can remove an individual nontrivial residue and is already allowed by this expression.

For an integer N>=0 choose c_N=2sigma+2N+1 and d_N=c_N-sigma. At fixed N the same horizontal-height selection as in R17 avoids nontrivial zero ordinates by a constant divided by log height. Logarithmic-power bounds for the two logarithmic derivatives and inverse-square decay of the translated packet make the horizontal integrals vanish. Thus the rightward contour formula is the integral on c_N minus 2pi times the full nontrivial residue sum and the first N trivial residues. Multiplicity is included once, not squared by the indexing convention.

The new point is that the right-line integral tends to zero as N increases. On that line the reflected argument is

\[
z=2\sigma-c_N-it=-2N-1-it.
\]

The functional equation gives

\[
H(z)=A(z)-H(1-z),
\quad A(z)=\frac{\Gamma'}{\Gamma}(1-z)-\log(2\pi)
-\frac\pi2\cot(\pi z/2).
\]

Here cot(pi*z/2) is uniformly bounded because its real argument is an odd half-period; its imaginary dependence is a hyperbolic tangent. The digamma argument 1-z has real part at least two and remains in the right half-plane, so its usual logarithmic bound is uniform. The other H factor is in the absolute Dirichlet region. Consequently

\[
|H(2\sigma-c_N-it)|\ll\log(c_N+|t|+2),
\qquad |H(c_N+it)|\ll2^{-c_N}.
\]

The second bound follows directly by factoring 2^(-c_N) from the positive absolute Dirichlet series; its remaining sum is bounded uniformly for c_N>=2. On the shifted packet line, d_N>1 and a<1/2 imply

\[
|w_2(t-id_N)|\ll
\frac{W^2e^{3d_N/W}}{t^2+d_N^2}.
\]

Indeed the polynomial numerator is bounded by a constant times (t²+d_N²)²; the sixth-power sinc denominator supplies (t²+d_N²)^3 and a factor (2W)^6, while the sine numerator is bounded by exp(3d_N/W). After the W^(-4) normalization this is exactly the displayed bound. Since d_N and c_N are uniformly comparable,

\[
\int_{\mathbb R}\frac{\log(c_N+|t|+2)}{t^2+d_N^2}dt
\ll\frac{\log(c_N+2)}{c_N}.
\]

The absolute right-line integral is therefore at most

\[
C W^2\exp[-c_N(\log2-3/W)]
\frac{\log(c_N+2)}{c_N},
\]

with the harmless exp(-3sigma/W) absorbed in C. It tends to zero in the stated sufficient range W>3/log2. This argument takes the horizontal limits at fixed N first, then increases N; it does not assume uniform horizontal estimates in N.

The nontrivial residue series is absolutely convergent for every fixed admitted sigma,W by the R17 bound: the packet is O(gamma^(-2)) on its fixed imaginary translate, and H(2sigma-rho) has a fixed logarithmic-power bound. The zero count supplies summability. For trivial residues, H(2sigma+2k) is positive and O(4^(-k)), uniformly in sigma. At y=sigma+2k,

\[
0<w_2(-iy)\le C W^{-4}(k+1)^4e^{3(\sigma+2k)/W}.
\]

Thus the trivial series converges whenever 6/W<2log2, the same range as above. Its positivity is strict because y>a and the imaginary sinc value is nonzero. Letting N increase proves the trace formula with the stated sign.

When W>=6 the bound strengthens to

\[
0<Q_{\sigma,W}\le C W^{-4}
\sum_{k\ge1}(k+1)^4(e/4)^k\ll W^{-4},
\]

uniformly for 1/2<sigma<1. This estimates only the explicit trivial-zero correction. In particular the positive energy equals -2pi*S plus O(W^(-4)), with a negative exact correction -2pi*Q. It does not make S known or small.

## Scope and independent checks still needed

The proof uses the same fixed-parameter logarithmic-derivative and horizontal-contour bounds as R17 and a uniform large-right-line estimate proved above. It applies to carrier X=1. Inserting X>1 would change the right-line exponential factor; no such extension is asserted here. The positive-energy identity continues to involve the full nontrivial zero residue sum. An independent R18 derivation via digamma/Laplace integrals can verify the sign, first trivial index and parameter range without shifting to infinity.
