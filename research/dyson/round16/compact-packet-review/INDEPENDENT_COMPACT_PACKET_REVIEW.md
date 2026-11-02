# Independent review of the compact pole-annihilating packet

Reviewer: Euclid (/root/prime186). Date: 2026-09-05.

Status: the ordinary mathematical claims in author Sections 1–6 pass this independent review. The final author version is pinned in spline_review_receipt.json; the review does not edit the author's report. This is an analytic construction under RH, not a proof of an improved zeta correlation or of a transfer to the original two-scale target.

Author report: ../compact-packet/COMPACT_POLE_PACKET.md.

Final accepted author SHA-256: 8106f3483adb71ab7ca4e5c105bfd6464dfa46954a1e1e77d2c77900392e19dc. The author confirmed this mathematical version was frozen; a separate later numerical example is outside the scope of this review.

## 1. Fourier normalization and exact support

Write \(a=1-\sigma\), \(b=a/W\), and let \(B\) be the sum-of-four-uniforms density on \([-2,2]\). Its characteristic function gives

\[
h_W(t)=\int B(y)e^{ity/W}\,dy,\qquad
\widehat h_W(\lambda)=2\pi W B(W\lambda).
\]

Here the transform uses \(e^{-it\lambda}\), with no \(2\pi\) in the exponent. Since \(t^2h_W(t)\) is integrable, Fourier differentiation can be taken in distributions and then identified with a continuous ordinary function:

\[
\widehat w(\lambda)
=\frac{-\partial_\lambda^2\widehat h_W(\lambda)+a^2\widehat h_W(\lambda)}{W^2}
=2\pi W[-B''(W\lambda)+b^2B(W\lambda)].
\]

Thus every factor of \(W\) and \(2\pi\) in author (4) is correct. No delta masses arise from differentiating \(B\) twice: \(B\) is \(C^2\) on the entire real line and is zero outside its support. In particular,

\[
\int w=2\pi W K_b(0)
=2\pi W(2+2b^2/3).
\]

The independent exact check verifies the polynomial expressions, their \(C^2\) junctions at \(\pm1,\pm2\), the even junction at zero, and \(B(0)=2/3\), \(B''(0)=-2\).

## 2. The actual one-factor contour is legal

For admitted parameters \(1/2<\sigma<1\), \(W\ge1\), \(X>e^2\), fix \(c>1\) and shift

\[
H(s)X^{s-\sigma}w(-i(s-\sigma)),\qquad H=-\zeta'/\zeta,
\]

from the line \(\sigma\) to \(c\). RH places every nontrivial zero strictly to the left of the closed strip. Trivial zeros are also outside it. The only possible pole is \(s=1\), with residue \(+1\) for \(H\). Its residue in the integrand is \(X^a w(-ia)=0\).

The entire sinc factor is nonzero at \(\pm ia\): its value there is a positive real hyperbolic-sine quotient before taking the fourth power. As \(a>0\), the polynomial has a simple zero at each point, exactly sufficient for this one simple pole.

On every fixed imaginary translate and at large real \(t\),

\[
w(t+iv)=O_{a,W,v}(t^{-2}).
\]

This follows directly from the bounded sine on a fixed horizontal strip, its fourth-power denominator, and the degree-two numerator. The usual local partial-fraction estimate for the logarithmic derivative, together with RH and the fixed distance \(\sigma-1/2>0\), bounds \(H\) by a fixed power of \(\log(|t|+3)\) in the horizontal range under consideration. Consequently the vertical integrals are absolutely convergent and the horizontal sides vanish. The proof needs no avoidance of special zero heights. Its constants may depend on the fixed contour parameters; the later uniform estimate uses a different argument.

On the right line, the von Mangoldt series is absolutely convergent and the translated weight is integrable. Fubini is therefore justified before any support restriction. Put \(d=c-\sigma\), \(\lambda=\log(n/X)\), and then \(z=t-id\):

\[
\int_{\mathbb R}w(t-id)e^{-it\lambda}\,dt
=e^{d\lambda}\widehat w(\lambda).
\]

The end segments vanish by the same inverse-square decay. The coefficient is
\(X^d n^{-c}e^{d\log(n/X)}=n^{-\sigma}\).
This proves precisely author (6), with no pole term left over and no critical-strip Dirichlet-series substitution.

Fourier support leaves only integers \(Xe^{-2/W}<n<Xe^{2/W}\). At the support endpoints \(K_b(\pm2)=0\); an integer or prime power at either endpoint contributes zero. The sum is exactly finite, rather than an approximation with an unbounded arithmetic remainder.

## 3. Centering, regularity and boundary conventions

The change \(u=Xe^{y/W}\) in the continuous-density integral contributes the Jacobian \(du=(X/W)e^{y/W}dy\). The result is exactly

\[
2\pi X^a\int_{-2}^{2}e^{by}[-B''(y)+b^2B(y)]dy.
\]

The integrand is the derivative of
\(e^{by}[-B'(y)+bB(y)]\), whose values vanish at both outer endpoints. Its internal values agree because \(B,B'\) are continuous. The continuous density is therefore exactly zero, not merely lower order.

The kernel \(K_b\) is continuous and piecewise polynomial with a bounded, piecewise continuous first derivative. It is absolutely continuous on the real line. Its first derivative can jump at the spline knots; this creates no atom in the first distributional derivative of \(K_b\). The composed function

\[
f(u)=2\pi W u^{-\sigma}K_b(W\log(u/X))
\]

has the same absolute-continuity property on its compact support and vanishes at the two outer endpoints. Stieltjes integration by parts against the right-continuous \(E=\psi-u\) thus gives exactly author (8). An interior prime-power atom remains in \(d\psi\), while \(df=f'(u)du\) has none. There is no product-jump correction because \(f\) is continuous.

This argument would not authorize dropping endpoints after an additional interior truncation. The author's explicit warning about such a truncation is correct.

## 4. Uniform RH estimate and its limits

Differentiation and \(du/u=dy/W\) give

\[
f'(u)=2\pi W u^{-\sigma-1}
[-\sigma K_b(y)+W K_b'(y)]
\]

and hence

\[
|\mathcal P_{\sigma,W}(X)|
\le 2\pi X^{-\sigma}e^{2\sigma/W}
\sup_{\mathrm{support}}|E(u)|
[\sigma\|K_b\|_1+W\|K'_b\|_1].
\]

There is no missing \(W\) in author (9).

Direct piecewise integration, reproduced with exact rational arithmetic, yields

\[
\|B\|_1=1,\quad \|B'\|_1=4/3,\quad
\|B''\|_1=8/3,\quad \|B'''\|_1=8.
\]

The last derivative is understood almost everywhere. These establish both bounds in author (10). Since \(0<b<1/2\), their bracket is at most \(45W/4\).

Ordinary RH gives \(|E(u)|\le C\sqrt u\log^2(2u)\) with one absolute \(C\), after enlarging it on a bounded range. Here \(u\ge Xe^{-2/W}>1\), \(\sqrt u\le e\sqrt X\), \(e^{2\sigma/W}\le e^2\), and
\(\log(2u)\le \log X+2+\log2\ll\log X\).
Thus the stated \(O(WX^{1/2-\sigma}\log^2X)\) bound is uniform in the complete admitted range. It uses no GRH for Dirichlet \(L\)-functions and no uniform contour estimate near the critical line.

This is a pointwise RH error bound. It establishes neither the sign of the finite prime sum nor a covariance asymptotic.

## 5. Negative mass and normalization

On either outer interval put \(z=2-|y|\in[0,1]\). Then

\[
-K_b(y)=z(1-b^2z^2/6)\ge(23/24)z.
\]

Consequently the two outer intervals have negative mass

\[
2\int_0^1(z-b^2z^3/6)dz=1-b^2/12.
\]

For \(x=b^2\in[0,1/4]\), the ratio

\[
g(x)=\frac{1-x/12}{2+2x/3}
\]

has derivative numerator \(-5/6\), so it decreases. At \(x=1/4\) it equals
\((47/48)/(13/6)=47/104\). This independently verifies the author's uniform lower bound. At \(b=0\), the inner sign change is at \(|y|=2/3\), and direct integration gives full positive and negative masses \(4/3\) each. Continuity in \(L^1\) gives normalized negative mass tending to \(2/3\).

These normalized masses are in the scaled coordinate \(y=W\lambda\). The corresponding integrals in \(\lambda\) are smaller by \(1/W\). The author explicitly preserves that convention; there is no assertion that the sign cost is negligible relative to the bandwidth. Positive semidefiniteness of the actual time-measure Gram matrix is fully compatible with negative individual Fourier entries.

## 6. Accepted scope and reproducibility

The exact finite signed arithmetic formula is accepted. At \(W=T\), \(X=T^\alpha\), its support width is \(4X/T+O(X/T^3)\). This is a legitimate finite computation surface, with complete prime powers and no Gaussian tail to approximate. No numerical runtime benchmark or arithmetic improvement is inferred.

The weight is different from the original two-scale \(W_T\), and the theorem is linear in one logarithmic derivative. Its simple zeros do not dispose of double poles or of reflected-zero residues in a two-factor contour. Parameter-dependent weights introduce derivative-of-weight terms. Those limitations are explicitly retained by the author and are essential to this acceptance.

The adjacent check_spline_review.py uses only Python's exact rational arithmetic and standard library. Its receipt pins the author and reviewer-script hashes and verifies the spline junctions, all four norms, the limiting masses, and the \(47/104\) bound. It is an independent structural check, not a zeta experiment or a substitute for the analytic arguments above. No author source, earlier round, public repository or PDF was changed.
