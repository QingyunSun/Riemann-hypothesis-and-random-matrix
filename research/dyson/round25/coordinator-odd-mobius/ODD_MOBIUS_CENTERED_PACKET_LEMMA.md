# RH odd-Möbius truncation and one centered prime statistic

Date: 2026-09-05. Author: coordinator. Status: direct ordinary derivation for independent review by the Astra research task. This supplies the primary RH input, the exact odd normalization, and a quantified centered-error lemma for the owner's proposed joint-main calculation. It does not prove the complete joint-main identity, remove arithmetic masks, or bound the remaining Möbius–prime covariance.

## 1. Source and hypotheses

Fix \(0<\eta<1/2\) and put \(\sigma=1/2+\eta<1\). Under ordinary RH,
\[
M_\mu(y):=\sum_{n\le y}\mu(n)\ll_\eta y^\sigma\qquad(y\ge1).
\]
This is explicitly stated on printed p.1, equation (1), of K. Soundararajan, [Partial sums of the Möbius function, arXiv:0705.0723v2](https://arxiv.org/pdf/0705.0723v2). Theorem 1 there proves a stronger RH bound. The source's first-page statement and hypotheses were read live; the entire paper has not been independently re-proved here. Its retained PDF is 157,587 bytes, SHA256 9bacaa0c6bbaf687091d8be7b9f0df3e58727339002c9cabcb4de90e33f41fa7.

For the prime statistic in Section 4, also use the ordinary RH estimate
\[
E(y)=\Psi(y)-y\ll \sqrt y\log^2(2y).
\]
The relevant primary source is Schoenfeld, [Theorem 10, equation (6.2)](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), printed p.337. Its retained source and exact scope were previously checked in the R22 coordinator singleton review. All prime powers remain in \(\Psi\). No GRH input is used.

Let \(2\le Q<X\) be fixed while the real lower-endpoint variable m varies on [X,2X]. Define
\[
u_Q=\sum_{\substack{d\le Q\\d\ {\rm odd}}}\frac{\mu(d)}d,
\qquad
a_Q(m)=\sum_{\substack{d\le Q\\d\ {\rm odd}}}
\frac{\mu(d)}d\log(m/d).
\]
These sums include **all odd d up to Q**, with the true Möbius coefficient. There is no condition \(d\mid m\) inside \(a_Q\). This is the smooth coefficient proposed after a legitimate completion, not the original unsmoothed divisor sum. The estimates below cannot be applied to an arbitrary selected owner family, or before the divisibility mask has been handled.

## 2. Exact odd normalization and uniform truncation bounds

Set \(M_{\rm odd}(y)=\sum_{d\le y,\ d\ {\rm odd}}\mu(d)\). The exact coefficient identity gives
\[
M_{\rm odd}(y)=\sum_{j\ge0}M_\mu(y/2^j),
\]
with the sum finite. For an even integer, the last two nonzero Möbius terms cancel; for an odd integer only the j=0 term remains. Consequently
\[
M_{\rm odd}(y)\ll_\eta y^\sigma,
\]
by the geometric sum \(\sum_j2^{-j\sigma}\). Removing the prime 2 therefore requires no theorem for Möbius sums in varying progressions.

The Dirichlet series
\[
D(s)=\sum_{d\ {\rm odd}}\mu(d)d^{-s}
=\frac{1}{(1-2^{-s})\zeta(s)}
\qquad(\Re s>1)
\]
and its derivative converge locally uniformly in \(\Re s>\sigma\), by partial summation from the bound just proved. For real s decreasing to 1, integral comparison gives \((s-1)\zeta(s)\to1\). Thus \(D(1)=0\) and \(D'(1)=2\), and termwise differentiation is legitimate at 1. Equivalently,
\[
\boxed{\sum_{d\ {\rm odd}}\frac{\mu(d)}d=0,\qquad
\sum_{d\ {\rm odd}}\frac{\mu(d)\log d}{d}=-2.}
\]
These are convergent signed sums, not absolutely convergent series at s=1.

Write \(A(y)=M_{\rm odd}(y)\). Partial summation over the tail, with Q a real endpoint and \(A(Q)\) including d≤Q, gives the exact identities
\[
\boxed{u_Q=\frac{A(Q)}Q-\int_Q^\infty\frac{A(t)}{t^2}\,dt,}
\]
\[
\boxed{a_Q(m)-2=
\frac{A(Q)}Q\log(m/Q)
-\int_Q^\infty\frac{A(t)}{t^2}\{\log(m/t)+1\}\,dt.}
\]
All boundary terms at infinity vanish because \(\sigma<1\). The integrals converge even beyond t=m, where the logarithm changes sign.

Since
\[
\int_Q^\infty t^{\sigma-2}\,dt
=\frac{Q^{\sigma-1}}{1-\sigma},
\qquad
\int_Q^\infty t^{\sigma-2}\log(t/Q)\,dt
=\frac{Q^{\sigma-1}}{(1-\sigma)^2},
\]
the identities imply
\[
\boxed{|u_Q|\ll_\eta Q^{-1/2+\eta},\qquad
|a_Q(m)-2|\ll_\eta
Q^{-1/2+\eta}\{1+\log(m/Q)\}.}
\]
Uniformly for X≤m≤2X this is
\(O_\eta(Q^{-1/2+\eta}\log(2X))\).

Because Q is held fixed in the packet, the derivative is exact:
\[
\boxed{a_Q'(m)=u_Q/m.}
\]
More generally, for each integer j≥1,
\[
a_Q^{(j)}(m)=(-1)^{j-1}(j-1)!u_Qm^{-j}.
\]
A moving cutoff Q=Q(m) would introduce jumps and is not covered by this derivative assertion.

## 3. Actual packet and its derivative in the prime endpoint

Take the owner's smooth packet:
\[
X=T^\alpha,\quad H=X/T,\quad
7/4\le\alpha\le9/4,\quad T\ge4,\quad \ell=\log T,
\]
\[
F_T(m,h)=b_T(m)\chi(m/X)V(h/H)(m/(m+h))^T.
\]
Here \(\chi,V\) are fixed smooth compactly supported functions in (1,2), and \(b_T\) is the unchanged exact R21/R22 weight. The previously proved global bounds are
\[
b_T(m)\ll_\omega (m\ell^2)^{-1},
\qquad |b_T'(m)|\ll_\omega(m^2\ell^2)^{-1}.
\]

On the packet, \(m\asymp X\), \(h\asymp H\), \(n=m+h\asymp X\). Put
\(G_T(n,h)=F_T(n-h,h)\), extended smoothly by zero off the packet. Differentiation in n holds h fixed. The Pareto factor has logarithmic derivative
\[
\partial_n\log((n-h)/n)^T
=\frac{Th}{n(n-h)}=O(X^{-1}).
\]
The cutoff \(V(h/H)\) is not differentiated. The b and chi derivatives are on scale X. Consequently,
\[
\boxed{|G_T(n,h)|\ll\frac1{X\ell^2},\qquad
|\partial_nG_T(n,h)|\ll\frac1{X^2\ell^2}.}
\]
The constants depend on the fixed windows but are uniform in the specified alpha range. There is no lost factor T or H^{-1} in this endpoint derivative. Smooth compact support eliminates moving-boundary terms.

Define the small-coefficient convolution, with the integrand set to zero unless n−h lies in (X,2X) and h lies in (H,2H). No logarithm or fractional power is evaluated outside that positive support:
\[
B_Q(n)=\int_{\mathbb R}G_T(n,h)[a_Q(n-h)-2]\,dh.
\]
Its support is contained in (X,3X). Integrating over the h support of length O(H) and using Section 2 gives
\[
|B_Q(n)|\ll_\eta
\frac{H}{X\ell^2}Q^{-1/2+\eta}\log(2X),
\]
\[
\boxed{|B_Q'(n)|\ll_\eta
\frac{H}{X^2\ell^2}Q^{-1/2+\eta}\log(2X).}
\]
The term in which the derivative falls on a_Q is no larger, because its derivative lacks the extra logarithm.

## 4. Center first: the quantitative bound that actually tends to zero

Define the complete centered prime statistic
\[
\mathcal R_Q=
\sum_{n\ge1}\Lambda(n)B_Q(n)-\int_{\mathbb R}B_Q(y)\,dy.
\]
There is no omitted main term: the integral is subtracted before estimating. Exact Stieltjes integration by parts, with zero support endpoints, gives
\[
\mathcal R_Q=-\int_X^{3X}E(y)B_Q'(y)\,dy.
\]
Under RH, \(|E(y)|\ll\sqrt X\log^2(2X)\) on this support. Therefore
\[
\boxed{
|\mathcal R_Q|
\ll_{\eta,\omega,\chi,V}
\frac{H}{\sqrt X}\,
Q^{-1/2+\eta}\,
\frac{\log^3(2X)}{\ell^2}
\ll
\frac{H}{\sqrt X}Q^{-1/2+\eta}\log(2X).
}
\]
The last comparison uses the fixed compact alpha range.

If the actual completed expression sums only over odd prime endpoints, the difference is the contribution of powers of 2. There are at most two such powers in (X,3X). Their total is
\[
O_\eta\left(\frac{H}{X\ell^2}Q^{-1/2+\eta}\log(2X)\right),
\]
strictly within the displayed budget. This restriction does not change the continuous prime density to one half.

For any fixed \(Q=X^\theta\), \(0<\theta<1\), the power of X in the last bound is at most \(1/18-\theta/2+\theta\eta\). The proof does not require H greater than the square root of X, Q<H, or K<H. Those may be separate conditions for a completion preceding this lemma.

For the earlier choice \(Q=X^{523/1000}\), this exponent is
\[
\frac1{18}-\frac{523}{2000}+\frac{523\eta}{1000}
=-\frac{3707}{18000}+\frac{523\eta}{1000}.
\]
For the fixed choice \(\eta=1/100\), this equals
\[
-\frac{180643}{900000}<0.
\]
For the owner's new R25 choice \(Q=X^{2/5}\), taking the same fixed \(\eta=1/100\) gives instead
\[
\frac1{18}-\frac15+\frac1{250}
=-\frac{158}{1125}<0.
\]
Thus the centered small-coefficient error is \(o(1)\) for either choice, uniformly over the full stated range \(7/4\le\alpha\le9/4\). Any fixed outer scalar factor, such as 2 in the programme's double sum, only changes the implied constant. This does not assert a partition covering every physical shift or the complete exponential length average.

## 5. Precisely what this supplies to the joint-main calculation

The owner proposes to rewrite a combination of actual principals as a centered statistic with coefficient a_Q, then split \(a_Q=2+(a_Q-2)\). Section 4 controls the second part, **if the complete principal identity has first been derived with the actual coefficients, masks and normalizations**.

The following are not proved in this note:

- Completion of the primitive \(h\)-mask into the proposed a_Q coefficient.
- Completion of the complementary small-cofactor principal into its proposed continuous integral.
- Payment for all nonprimitive prime-power terms in those rewrites.
- Exact cancellation of the constant-2 part with both singular-series marginals and the remaining baseline.
- An upper bound for the residual Möbius–prime covariance or a strict variance deficit.

Those are distinct obligations of the full arithmetic argument. In particular, the pointwise estimate for \(a_Q-2\) cannot be multiplied by the uncentered packet mass and called small. Its useful saving here comes from the exact centered Stieltjes identity and the derivative bound.

This is a concrete RH lemma for the currently proposed joint-main route, not a new general kernel framework or a numerical fit. The source PDF is retained locally; only its bibliographic pointer and hash need be included in any public handoff. No new Fable session, model call, parameter scan or numerical certificate is involved.
