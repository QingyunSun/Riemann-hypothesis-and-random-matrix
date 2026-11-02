# A nonnegative packet can remove the zeta pole, at an exact signed-kernel cost

Round 15, 2026-09-05. Ordinary analytic result, with explicit scope. The construction below is a legitimate alternative to the centered Gaussian shortcut rejected in Round 2: its time weight is nonnegative and its logarithmic-derivative contour has **zero pole residue**. Its arithmetic Fourier kernel necessarily has a leading negative part. We evaluate that cost exactly, give a uniformly convergent centered-prime formula with an explicit RH bound, and retain the actual positive Hilbert-space identity.

This is a classical contour/Fourier construction verified for this programme, without a novelty claim. It is a different time weight from the fixed Round 7 statistic \(W_T\). Neither \(W_T\ge1/16\), a compact form-factor bound above \(7/10\), nor an implication transferring the new weighted norm to those targets is proved here.

## 1. A precise pole-free identity for actual zeta

Use the angular-frequency convention

\[
\mathcal Fw(\lambda)=\int_{\mathbb R}w(t)e^{-it\lambda}\,dt.
\tag{1}
\]

Let \(1/2<\sigma<1\), \(a=1-\sigma\), \(W>0\), and

\[
H_\sigma(t)=-\frac{\zeta'}{\zeta}(\sigma+it),\qquad
w_{\sigma,W}(t)=\frac{t^2+a^2}{W^2}e^{-t^2/(2W^2)}.
\tag{2}
\]

The weight is strictly positive on the real axis and entire. It satisfies

\[
w_{\sigma,W}(-ia)=w_{\sigma,W}(ia)=0.
\tag{3}
\]

For every real \(X>0\), define

\[
M_{\sigma,W}(X)=
\int_{\mathbb R}H_\sigma(t)X^{it}w_{\sigma,W}(t)\,dt.
\tag{4}
\]

**Theorem 1.** Under RH, for all the parameters just specified,

\[
\boxed{
M_{\sigma,W}(X)=
\sum_{n\ge2}\Lambda(n)n^{-\sigma}
K_{\sigma,W}(\log(n/X)),
}
\tag{5}
\]

where

\[
K_{\sigma,W}(\lambda)=
\sqrt{2\pi}\,W
\left(1+\frac{a^2}{W^2}-W^2\lambda^2\right)
e^{-W^2\lambda^2/2}.
\tag{6}
\]

The integral and the series in (4)–(5) converge absolutely. The answer is real, since \(H_\sigma(-t)=\overline{H_\sigma(t)}\) and the weight is real and even. No critical-strip Dirichlet series is used.

**Proof, including the residue sign.** First consider any entire Gaussian times polynomial weight \(w\). Choose a fixed \(\beta>1\) and integrate

\[
F(s)=
-\frac{\zeta'}{\zeta}(s)\,
X^{s-\sigma}w(-i(s-\sigma))
\tag{7}
\]

around the rectangle between \(\sigma\) and \(\beta\). Under RH, its only possible pole inside is at \(s=1\); the nontrivial zero poles lie strictly to the left. The residue of \(-\zeta'/\zeta\) at one is \(+1\), so the residue of (7) is

\[
X^a w(-ia).
\]

The usual local logarithmic-derivative estimate is polynomial in \(\log(|t|+3)\), with a constant allowed to depend on \(\sigma-1/2\). The Gaussian on the fixed horizontal strip dominates this bound. Both horizontal integrals therefore vanish as the rectangle height tends to infinity. With both vertical integrals oriented upwards, the right integral minus the left integral is \(2\pi i\) times the residue. Dividing by \(i\) gives the exact general formula

\[
\int_{\mathbb R}H_\sigma(t)X^{it}w(t)\,dt
=\sum_{n\ge2}\Lambda(n)n^{-\sigma}
\mathcal Fw(\log(n/X))
-2\pi X^a w(-ia).
\tag{8}
\]

To check the series normalization directly, put \(v=\beta-\sigma\). On the right line the Dirichlet series is absolutely convergent, and the \(n\)-th integral contains

\[
X^v n^{-\beta}\int_{\mathbb R}
w(t-iv)e^{it\log(X/n)}dt.
\]

Shifting \(z=t-iv\) back to the real line multiplies the last integral by \((n/X)^v\). The resulting coefficient is exactly \(n^{-\sigma}\), not \(n^{-\beta}\) or \(X^v n^{-\sigma}\). The Gaussian Fourier decay proves absolute convergence of the final series, including its arbitrarily large \(n\) tail.

For (2), the residue in (8) is zero. Differentiating the elementary Gaussian Fourier transform twice gives (6). This proves (5).

The proof is for the logarithmic derivative at \(\sigma>1/2\), where no logarithm branch is needed. It does not remove the entire pole cut in a critical-line \(\log\zeta\) difference. A nonzero analytic weight cannot vanish on that whole cut. This distinction is why Theorem 1 is a genuine new packet choice rather than a correction to the already accepted Round 2 logarithm identity.

## 2. The continuous density cancels exactly, not just asymptotically

Set

\[
b=a/W,\qquad r=\sqrt{1+b^2},\qquad
G_b(z)=(1+b^2-z^2)e^{-z^2/2}.
\tag{9}
\]

The kernel is positive for \(|W\lambda|<r\), zero at the two boundary points, and negative outside. Define the continuum integrand

\[
f_{\sigma,W,X}(y)=y^{-\sigma}
K_{\sigma,W}(\log(y/X)),\qquad y>0.
\tag{10}
\]

It has rapid decay at both zero and infinity in the logarithmic variable. Its exact total integral is

\[
\boxed{\int_0^\infty f_{\sigma,W,X}(y)\,dy=0.}
\tag{11}
\]

Indeed, after \(z=W\log(y/X)\),

\[
\int_0^\infty f(y)\,dy
=\sqrt{2\pi}\,X^a\int_{\mathbb R}G_b(z)e^{bz}dz,
\]

and

\[
\frac{d}{dz}\left[(z+b)e^{-z^2/2+bz}\right]
=G_b(z)e^{bz}.
\tag{12}
\]

Both endpoint values vanish. This also checks the sign and normalization in (8): for an unmodified Gaussian the continuum integral is \(2\pi X^a w(-ia)\); its subtraction is precisely the zeta pole residue.

The positive and negative continuum masses in (11) are separately nonzero and exactly equal. Their common value is

\[
\boxed{
A_{\sigma,W}(X)=
2\sqrt{2\pi}\,X^a e^{-r^2/2}
\left[r\cosh(br)+b\sinh(br)\right].
}
\tag{13}
\]

Integrate (12) over \([-r,r]\) to prove (13). The remaining integral is its negative by (11). For \(W\to\infty\), uniformly for \(a\in[1/4,1/2]\),

\[
A_{\sigma,W}(X)=
\left(2\sqrt{2\pi/e}+O(W^{-2})\right)X^a.
\tag{14}
\]

These are exact statements about the continuum density model and the Fourier kernel. They do **not** assert that the actual positive and negative prime sums individually equal their continuum values on short intervals.

### 2.1 No hidden large logarithmic saddle

Our \(W\) is a time width. The continuous exponential is

\[
\exp\left(-W^2\lambda^2/2+a\lambda\right)
=\exp\left(\frac{a^2}{2W^2}\right)
\exp\left[-\frac{W^2}{2}
\left(\lambda-\frac{a}{W^2}\right)^2\right].
\tag{15}
\]

Its saddle is \(\lambda=a/W^2\). It is not \(aW^2\), which belongs to the inverse Fourier-width convention. For \(W\asymp T\) and \(X=T^\alpha\), the continuum mass is concentrated near \(y=X\), not at an exponentially more remote scale. Nevertheless both signed tails are retained before using (11). Section 3 supplies an explicit bound for the centered tails.

### 2.2 The negative Fourier mass does not vanish with increasing time width

Without the Mellin tilt, let

\[
P_b=\int_{-r}^rG_b(z)dz,\qquad
N_b=-\int_{|z|>r}G_b(z)dz.
\]

Direct integration gives

\[
P_b=2r e^{-r^2/2}
+2b^2\int_0^r e^{-z^2/2}dz,\qquad
N_b=P_b-b^2\sqrt{2\pi}.
\tag{16}
\]

Thus \(P_b,N_b\to2e^{-1/2}\) and \(N_b/P_b\to1\) as \(b\to0\). In frequency units, the positive and negative integrals of \(K_{\sigma,W}\) tend to \(2\sqrt{2\pi/e}\), while their signed difference is only \(2\pi a^2/W^2\).

Consequently the negative part cannot be treated as a vanishing Fourier error. Because \(\Lambda(n)\ge0\), discarding the negative part of (5) gives an upper bound, not the needed lower bound. Pole annihilation is exact, but it has not restored coefficientwise positivity.

## 3. A centered-prime identity and a uniform explicit RH bound

Define \(\psi(y)=\sum_{n\le y}\Lambda(n)\) for all \(y>0\), with \(\psi(y)=0\) on \(0<y<2\), and \(E(y)=\psi(y)-y\). At each prime power the right-continuous convention includes the atom. Equations (5) and (11) give the exact Stieltjes formula

\[
\boxed{
M_{\sigma,W}(X)
=\int_0^\infty f_{\sigma,W,X}(y)\,dE(y)
=-\int_0^\infty E(y)f'_{\sigma,W,X}(y)\,dy.
}
\tag{17}
\]

All boundary terms vanish, including the lower endpoint at zero. Equivalently, using only \(y\ge1\),

\[
M_{\sigma,W}(X)=
f(1)-\int_1^\infty E(y)f'(y)dy
-\int_0^1 f(y)dy.
\tag{18}
\]

Here \(E(1)=-1\). The last two explicit lower-end terms must not both be dropped if this convention is used.

The primary RH estimate is Schoenfeld's Theorem 10, equation (6.2):
\(|\psi(y)-y|<\sqrt y\log^2y/(8\pi)\) for \(y>73.2\).
For \(1\le y\le74\), the elementary bound
\(\psi(y)\le y\log y\) suffices; for \(0<y<1\), \(E(y)=-y\).
Together these imply the convenient global bound

\[
|E(y)|\le9\sqrt y(1+|\log y|)^2\qquad(y>0)
\tag{19}
\]

under ordinary RH. No Dirichlet-\(L\)-function GRH is used.

**Theorem 2.** Under RH, uniformly for

\[
\frac12<\sigma\le\frac34,\qquad W\ge1,\qquad X\ge2,
\]

one has

\[
\boxed{
|M_{\sigma,W}(X)|
\le10800\,W X^{1/2-\sigma}(1+\log X)^2.
}
\tag{20}
\]

For \(R\ge1\), the part of the last integral in (17) with
\(|W\log(y/X)|>R\) has absolute value at most

\[
\boxed{
2430\,W X^{1/2-\sigma}(1+\log X)^2
(R^4+8R^2+32)e^{-R^2/4}.
}
\tag{21}
\]

This bounds the integrated-by-parts centered tail in (17). It is not, by itself, a bound for a sharply truncated prime series. For \(y_\pm=Xe^{\pm R/W}\) away from prime-power atoms, the outside centered Stieltjes integral also contains
\(E(y_-)f(y_-)-E(y_+)f(y_+)\). These two endpoint terms must be retained when using a finite prime window.

**Proof.** Write \(\delta=\sigma-1/2\), \(z=W\log(y/X)\) and \(L=1+\log X\).
Differentiating (10), and using (19) in (17), bounds the full integral by

\[
9\sqrt{2\pi}\,X^{-\delta}
\int_{\mathbb R}e^{-\delta z/W}
(1+|\log X+z/W|)^2
\left(\sigma|G_b(z)|+W|G'_b(z)|\right)dz.
\tag{22}
\]

In the stated range,

\[
|G_b(z)|\le(5/4+z^2)e^{-z^2/2},\qquad
|G'_b(z)|\le(|z|^3+13|z|/4)e^{-z^2/2},
\]

\[
e^{-\delta z/W}\le e^{|z|/4},\qquad
(1+|\log X+z/W|)^2\le L^2(1+|z|)^2.
\]

Put \(P(z)=15/16+13z/4+3z^2/4+z^3\) for \(z\ge0\).
The integral in (22), excluding its initial \(9X^{-\delta}WL^2\), is bounded by

\[
2\sqrt{2\pi}\,e^{1/16}
\int_0^\infty P(z)(1+z)^2 e^{-z^2/4}dz
=2\sqrt{2\pi}\,e^{1/16}
\left(\frac{805}{16}\sqrt\pi+\frac{481}{4}\right)<1200.
\tag{23}
\]

We used \(|z|/4\le z^2/4+1/16\) and elementary Gaussian moments.
For a fully rational last comparison, use
\(\sqrt\pi<16/9\), \(\sqrt{2\pi}<18/7\), and \(e^{1/16}<16/15\).
The resulting upper bound is \(120784/105<1200\). This proves (20).

For \(z\ge R\ge1\), \(P(z)(1+z)^2\le(95/4)z^5\), and

\[
\int_R^\infty z^5e^{-z^2/4}dz
=2(R^4+8R^2+32)e^{-R^2/4}.
\]

Including both tails and the factor \(\sqrt{2\pi}e^{1/16}\) costs less than \(270\), before the factor 9 in (19). This gives (21).

In particular, for fixed \(c>0\),
\(\sigma=1/2+c/\log T\le3/4\), \(W\asymp T\), and
\(X=T^\alpha\), \(6/5\le\alpha\le7/5\), (20) is uniformly
\(O_c(T\log^2T)\). Its factor \(X^{-\delta}=e^{-c\alpha}\) is retained.
Choosing \(R=4\sqrt{\log T}\) in (21) makes the centered tail negligible at any of the displayed main scales. Thus no unbounded far tail is hidden by the exact density cancellation.

This is a rigorous but weak consequence of the pointwise RH estimate. It does not establish a sign, a variance constant, or a gain in the zeta pair correlation.

## 4. The nonnegative time weight still gives a real Hilbert-space tool

For any finite Dirichlet polynomial \(C(t)=\sum_q c_q q^{-it}\),

\[
\int_{\mathbb R}H_\sigma(t)\overline{C(t)}w_{\sigma,W}(t)dt
=\sum_q\overline{c_q}\,M_{\sigma,W}(q),
\tag{24}
\]

\[
\|C\|_w^2=
\sum_{q,r}c_q\overline{c_r}
K_{\sigma,W}(\log(q/r)).
\tag{25}
\]

The full matrix in (25) is positive semidefinite, because it is an actual Gram matrix for the positive time measure. Its individual off-diagonal entries need not be positive. In particular, a diagonal coefficient norm must not replace it for long support.

The elementary projection inequality is legitimate:

\[
\int_{\mathbb R}|H_\sigma(t)|^2w_{\sigma,W}(t)dt
\ge 2\Re\sum_q\overline{c_q}M_{\sigma,W}(q)-\|C\|_w^2.
\tag{26}
\]

There is also an exact positive arithmetic energy identity. Plancherel applied to (4) gives

\[
\boxed{
\int_0^\infty |M_{\sigma,W}(X)|^2\,\frac{dX}{X}
=2\pi\int_{\mathbb R}|H_\sigma(t)|^2
w_{\sigma,W}(t)^2dt.
}
\tag{27}
\]

Equation (17) may be inserted into the left side. The actual centered prime error, not a fake zero process or an uncentered prime density, is its input. The identity has weight \(w^2\), not \(w\) and not the sharp interval indicator in \(W_T\).

These formulas permit a valid variational calculation with an explicitly paid pole. A successful calculation would still require useful control of the signed quantities (24), the full Gram matrix (25), and the negative-width term when comparing the two \(c\) values. No such numerical optimization or missing estimate is claimed here.

The contour theorem is deliberately linear in \(H_\sigma\). The simple zeros of the weight do not cancel double poles arising from a derivative or a product. In particular, shifting a contour for \(H(s)H(2\sigma-s)\) would also encounter reflected zero poles; no such contour is used to prove (27). Furthermore \(w_{\sigma_c,W}\) depends on \(c\): differentiating a weighted energy adds the integral containing \(\partial_c w_{\sigma_c,W}\). The earlier unweighted mixed-moment identities cannot be reused without that term.

## 5. An exact scale certificate for the discarded-negative-part cost

To see the size of the obstacle in the same coefficient units as a dense approximator, let \(M=T^\alpha\), \(6/5\le\alpha\le7/5\), \(W=T\), \(\sigma=1/2+c/\log T\), and formally sum the continuum positive and negative kernel pieces in (24) with \(c_q=q^{-\sigma}\) for all integers \(M<q\le2M\).

Each continuum piece has the exact magnitude

\[
\frac{A_{\sigma,W}(q)}{q^\sigma}
=A_{\sigma,W}(1)\,q^{1-2\sigma}.
\]

Both totals are therefore

\[
\left(2\sqrt{2\pi/e}+o(1)\right)e^{-2c\alpha}M.
\tag{28}
\]

Their signed sum is identically zero. In contrast, the *diagonal part* of (25) is

\[
\sqrt{2\pi}W(1+a^2/W^2)
\sum_{M<q\le2M}q^{-2\sigma}
\sim \sqrt{2\pi}W e^{-2c\alpha}\log2.
\tag{29}
\]

The ratio of (28) to (29) is asymptotic to

\[
\frac{2}{\sqrt e\,\log2}\frac MW\longrightarrow\infty.
\tag{30}
\]

This is a certificate about the exact continuum pieces and their proposed diagonal normalization. It is not a prime short-interval asymptotic, not a claim about the full Gram norm, and not a lower bound for the actual mixed moment. It proves that the removed residue reappears as cancellation of leading arithmetic kernel pieces; a small negative-kernel error cannot be inferred from this normalization.

## 6. Relation to the existing targets and countermodels

The established Round 7/8 target is

\[
W_T=\frac{2}{T\log^2T}
\left[\sinh(2)\int_0^T|H_{\sigma_1}(t)|^2dt
-\sinh(1)\int_0^T|H_{\sigma_{1/2}}(t)|^2dt\right],
\quad \sigma_c=\frac12+\frac c{\log T}.
\]

Changing the time weight changes that observable. The present proof supplies neither an exact identity recovering this sharp cutoff from positive packet averages nor the uniform two-width limit needed to transfer an AH prediction to a packet norm. Even after such a transfer, a positive lower bound for the first energy in the brackets does not control the signed difference without handling the second one. Accordingly, this report establishes **no implication from (26) or (27) to \(W_T\ge1/16\)**.

The realized half-grid/ACUE process from the earlier rounds remains a valid check against an inference using only low Fourier support and point-process positivity. The new contour identity uses the actual zeta Euler product and its actual pole; an arbitrary ACUE model need not satisfy (5). That extra arithmetic structure is real, but its right side is signed. Nothing here rules out the ACUE prediction or proves the required signed gain.

The R14 selected-CUE theorem remains a finite scalar-heat result with a verified \(N^{-2/3}\) relative error in probability. It supplies no estimate for \(E(y)\) in (17). No force-energy, general-beta or heat-flow transfer is imported into this arithmetic argument.

The bounded outcome is therefore a legal positive-time-weight construction, an exact pole-free arithmetic identity, and a quantified reason that this construction alone does not obtain the missing sign. A future extension should estimate the centered signed kernel or prove a usable weighted two-width comparison. It should not repeat the already rejected claim that Fourier positivity removes the zeta pole for free.

## 7. Primary inputs, reproducibility and provenance

- Lowell Schoenfeld, [*Sharper bounds for the Chebyshev functions theta(x) and psi(x). II*](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), Mathematics of Computation 30 (1976), 337–360, Theorem 10, equation (6.2), printed p.337: ordinary RH gives the explicit \(\psi-x\) estimate used in (19). The retained local source PDF has SHA-256 8c3cac1ee52eb05af05ec410adc587a18505a46aacdde41ae097038b0e7c3897.
- Shōta Inoue, [*Small gaps between consecutive zeros of the Riemann zeta-function*](https://arxiv.org/html/2604.05733v1), arXiv:2604.05733v1, Lemma 5.5 and equations (5.42)–(5.43), is the primary contour/branch source behind the different Round 2 logarithm identity. Theorem 1 above is proved directly for the logarithmic derivative and does not differentiate an unverified error term from that source.
- The earlier programme files are pinned in source_manifest.json: the Round 2 Gaussian audit, Round 7 actual-zeta reduction, Round 8 centered-tail identity, Round 10/11 arithmetic remainder audits, and Round 14 CUE theorem.

The adjacent check script verifies the polynomial identities, Gaussian moments, positive/negative mass formulas, explicit constant comparisons, the exact pole value and Fourier-transform convention. It uses a finite Dirichlet polynomial only for a direct weighted-inner-product check. It never evaluates a nonconvergent critical-strip prime series. Its high-precision decimal comparisons are diagnostics that supplement the ordinary proofs; they are not interval certificates or measurements of the large-\(T\) zeta target.
