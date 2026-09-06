# A compact quadratic packet: holomorphic square, reflected poles, and an exact positive relation

Date: 2026-09-05. Status: ordinary analytic derivation submitted for independent review. This uses Fourier differentiation, Dirichlet convolution and contour integration; no novelty claim is made for those methods. No Bragg-atom upper bound, Montgomery theorem or AH refutation is obtained.

The result has three parts. A double-zero packet gives an exactly finite formula for H². The same formula cannot be used for |H|², whose reflected contour crosses zeta-zero poles. Nevertheless the empty finite sum at carrier X=1 yields a useful **exact** conversion from modulus energy to twice the real-part square. Centers, residues and parameter derivatives are retained.

## 1. Packet and compact Fourier transform

Assume RH. Fix 1/2<σ<1, a=1−σ, W≥1, b=a/W, and define
\[
H(s)=-\zeta'(s)/\zeta(s),\qquad
h_{6,W}(t)=\left(\frac{\sin(t/(2W))}{t/(2W)}\right)^6,
\]
\[
\boxed{w_{2,a,W}(t)=\frac{(t^2+a^2)^2}{W^4}h_{6,W}(t).}
\tag{1}
\]
Removable values are taken at zero. The weight is even, real and nonnegative on the real axis, entire, and has zeros of order two at ±ia. The sinc factor is nonzero at those points. On each fixed horizontal translate it decays as O(1/t²), with constants depending on the fixed parameters. Its exponential type is 3/W.

Six is the smallest **even** sinc power giving integrable polynomial decay after this degree-four multiplier: power 2k gives O(|t|^{4−2k}); power four does not decay and power six gives t⁻². This is only a statement about this construction and absolute contour convergence, not an optimality claim among all packets.

Let B₆ be the density of the sum of six independent uniforms on [−1/2,1/2]. Explicitly,
\[
B_6(y)=\frac1{120}\sum_{j=0}^{6}(-1)^j\binom6j(y+3-j)_+^5.
\tag{2}
\]
It is even, nonnegative, C⁴, supported on [−3,3], and its derivatives through order four vanish at the outer endpoints. The characteristic-function identity is
\[
h_{6,W}(t)=\int_{-3}^{3}B_6(y)e^{iyt/W}dy.
\]
Put
\[
K_{2,b}(y)=B_6^{(4)}(y)-2b^2B_6''(y)+b^4B_6(y).
\tag{3}
\]
Under \(\widehat w(\lambda)=\int w(t)e^{-it\lambda}dt\),
\[
\boxed{\widehat w_{2,a,W}(\lambda)=2\pi W K_{2,b}(W\lambda),
\quad\operatorname{supp}\widehat w\subset[-3/W,3/W].}
\tag{4}
\]
Multiplication by t² gives minus the second Fourier derivative; the squared factor produces \((\partial_y^2-b^2)^2B_6\), with y=Wλ. This accounts for every sign, W and 2π.

Formula (2) gives
\[
B_6(0)=11/20,\quad B_6''(0)=-1,\quad B_6^{(4)}(0)=6,
\]
\[
\boxed{Z_{2,a,W}:=\int w_{2,a,W}(t)dt
=2\pi W(6+2b^2+11b^4/20).}
\tag{5}
\]
Nonnegative time weight does not imply nonnegative Fourier entries. In fact B₆(1)=13/60, B₆''(1)=1/3, B₆⁽⁴⁾(1)=−4, hence
\[
K_{2,b}(1)=-4-2b^2/3+13b^4/60<0\quad(0\le b\le1/2).
\tag{6}
\]
This is compatible with positive semidefiniteness of the full Fourier Gram operator.

## 2. Exact one-contour identity for H²

Define
\[
C_2(n)=(\Lambda*\Lambda)(n)=\sum_{d\mid n}\Lambda(d)\Lambda(n/d).
\tag{7}
\]
For every X>0, the identity is
\[
\boxed{\int_{\mathbb R}H(\sigma+it)^2X^{it}w_{2,a,W}(t)dt
=2\pi W\sum_{Xe^{-3/W}<n<Xe^{3/W}}
 C_2(n)n^{-\sigma}K_{2,b}(W\log(n/X)).}
\tag{8}
\]
The sum is exactly finite. An integer endpoint has zero coefficient because K₂,b(±3)=0, so either endpoint convention is valid.

**Proof.** Near s=1, with γ₀ Euler's constant,
\[
H(s)=(s-1)^{-1}-\gamma_0+O(s-1),
\quad H(s)^2=(s-1)^{-2}-2\gamma_0(s-1)^{-1}+O(1).
\tag{9}
\]
The double zero of \(w_{2,a,W}(-i(s-\sigma))\) at s=1 cancels both principal terms. RH puts all nontrivial-zero poles to the left of Re(s)=σ; trivial-zero poles are also left. Shift
\(H(s)^2X^{s-\sigma}w_{2,a,W}(-i(s-\sigma))\) from the upward σ-line to a fixed c>1. The standard RH logarithmic-derivative bound in a fixed strip to the right of 1/2 is O(log²(|t|+2)); together with the translated t⁻² weight it gives absolute convergence and vanishing horizontal integrals. No uniform contour constant as σ↓1/2 is asserted.

On Re(s)=c, expand the absolutely convergent series \(H(s)^2=\sum C_2(n)n^{-s}\). Let d=c−σ and λ=log(n/X). The entire-weight contour shift gives
\[
\int w_{2,a,W}(t-id)e^{-it\lambda}dt
=e^{d\lambda}\widehat w_{2,a,W}(\lambda).
\]
The prefactor Xᵈn⁻ᶜ then becomes n^{−σ}. Formula (4) proves (8). All interchanges occur on the absolutely convergent c-line before using compact support. ∎

C₂ is not Λ(n)². It is zero if n has more than two distinct prime factors, and
\[
C_2(p^k)=(k-1)(\log p)^2\ (k\ge2),\qquad
C_2(p^iq^j)=2\log p\log q\ (p\ne q,\ i,j\ge1).
\tag{10}
\]
Its first nonzero value is C₂(4)=(log2)². In particular this is multiplicative prime-product arithmetic, not the additive near-prime covariance in the Bragg kernel. The coefficients are nonnegative, but K₂,b is signed.

## 3. Full pole density and finite centering

Endpoint integration by parts gives, for every complex z,
\[
\int e^{zy}K_{2,b}(y)dy
=(z^2-b^2)^2\left(\frac{\sinh(z/2)}{z/2}\right)^6.
\tag{11}
\]
Thus both
\[
\int e^{by}K_{2,b}(y)dy=0,\qquad
\int y e^{by}K_{2,b}(y)dy=0
\tag{12}
\]
vanish. The first equality alone would not remove a double pole. Directly, e^{by}K₂,b is the derivative of
\[
e^{by}[B_6'''-bB_6''-b^2B_6'+b^3B_6].
\]
External endpoints vanish and internal values agree; the C⁴ regularity accounts for all boundary terms. Differentiating (11) in z at b proves the second equality.

Set \(F_{\sigma,W,X}(u)=u^{-\sigma}\widehat w_{2,a,W}(\log(u/X))\). Substitution u=Xe^{y/W} proves
\[
\int_0^\infty u^{-\sigma}(\log u-2\gamma_0)
 \widehat w_{2,a,W}(\log(u/X))du
\]
\[
=2\pi X^a\left[(\log X-2\gamma_0)\int e^{by}K_{2,b}(y)dy
 +W^{-1}\int ye^{by}K_{2,b}(y)dy\right]=0.
\tag{13}
\]
The density log u−2γ₀ is the full continuous pole density from (9): its Mellin transform on [1,∞) has principal part (s−1)⁻²−2γ₀(s−1)⁻¹. Extending the same density to (0,∞) in (13) gives an exact compact integral; no asymptotic coefficient claim is required.

Let \(A_2(u)=\sum_{n\le u}C_2(n)\) and
\(E_2(u)=A_2(u)-u\log u+(1+2\gamma_0)u\). Then (8) and (13) give
\[
\int H(\sigma+it)^2X^{it}w_{2,a,W}(t)dt
=\int F_{\sigma,W,X}(u)dE_2(u)
=-\int_{Xe^{-3/W}}^{Xe^{3/W}}E_2(u)F'_{\sigma,W,X}(u)du.
\tag{14}
\]
Fσ,W,X is compactly supported, continuous, absolutely continuous, and zero at both support endpoints. K₂,b has piecewise polynomial derivative; its derivative jumps do not create atoms in this first Stieltjes integration by parts. An additional interior truncation would require its own E₂F boundary terms. No new bound on E₂ is claimed.

## 4. Exact separation from positive energy, and the useful replacement

Take X=1 and W≥3. Since e^{3/W}≤e<4 and C₂(n)=0 for n<4, the finite sum (8) is empty. Therefore
\[
\boxed{\int H(\sigma+it)^2w_{2,a,W}(t)dt=0.}
\tag{15}
\]
The weaker sufficient condition W>3/log4 also works. Meanwhile
\[
\mathcal E_{\sigma,W}:=\int|H(\sigma+it)|^2w_{2,a,W}(t)dt>0.
\tag{16}
\]
It converges for fixed parameters. The weight is positive off a discrete set, and H cannot vanish identically on the vertical line, by analytic continuation and its pole at one. This is an actual-zeta example showing why H² and |H|² cannot be interchanged in (8).

There is a correct exact positive relation. From \(2(\Re H)^2=|H|^2+\Re(H^2)\) and (15),
\[
\boxed{\mathcal E_{\sigma,W}
=2\int(\Re H(\sigma+it))^2w_{2,a,W}(t)dt
=2\int(\Im H(\sigma+it))^2w_{2,a,W}(t)dt.}
\tag{17}
\]
The mixed real-imaginary integral vanishes. This weighted conversion is justified for this packet, not for arbitrary weights.

### An exactly centered positive zero-pair identity

Put δ=σ−1/2. The paired canonical product for ξ gives, under RH and with all zero ordinates γ∈R counted with multiplicity,
\[
\Re\frac{\xi'}{\xi}(\sigma+it)
=R_\delta(t):=\sum_\gamma\frac{\delta}{\delta^2+(t-\gamma)^2}.
\]
The real series converges absolutely. Keep the exact center
\[
G_\sigma(t)=\Re\left[
\frac1{\sigma+it}+\frac1{\sigma-1+it}-\frac12\log\pi
+\frac12\frac{\Gamma'}{\Gamma}((\sigma+it)/2)\right].
\tag{18}
\]
The definition of ξ gives \(\Re H=G_\sigma-R_\delta\). Hence at X=1, W≥3,
\[
\boxed{\mathcal E_{\sigma,W}
=2\int w_{2,a,W}(t)[R_\delta(t)-G_\sigma(t)]^2dt.}
\tag{19}
\]
Writing rδ(v)=δ/(δ²+v²), define the actual pair kernel
\[
J_{\delta,W}(\gamma,\gamma')
=\int w_{2,a,W}(t)r_\delta(t-\gamma)r_\delta(t-\gamma')dt.
\tag{20}
\]
The right side of (19) is exactly
\[
2\sum_{\gamma,\gamma'}J_{\delta,W}(\gamma,\gamma')
-4\sum_\gamma\int w_{2,a,W}(t)G_\sigma(t)r_\delta(t-\gamma)dt
+2\int w_{2,a,W}(t)G_\sigma(t)^2dt.
\tag{21}
\]
For fixed δ>0, unit-interval zero counting gives \(R_\delta(t)\ll_\delta\log(|t|+2)\). Gσ also has logarithmic growth. Packet decay then justifies the positive pair sum by Tonelli and all cross terms by absolute convergence. The implicit constant may depend on δ. Negative ordinates, the gamma center and all tails are retained.

This is a positive-energy identity for actual zeta. It is not a finite Λ*Λ formula: the latter has value zero in this same instance.

## 5. The reflected contour and all its poles

On Re(s)=σ, \(\overline{H(s)}=H(2\sigma-s)\). Consider
\[
\mathcal I_\sigma(X)=\int|H(\sigma+it)|^2X^{it}w_{2,a,W}(t)dt.
\tag{22}
\]
It is real by evenness and conjugacy, but when X≠1 it is a cosine-weighted **signed** integral. Only X=1 is the positive energy (16).

Choose \(\max(1,2\sigma-1/2)<c<2\sigma\), and set d=c−σ. Such c exists for every σ>1/2. Shift
\(H(s)H(2\sigma-s)X^{s-\sigma}w_{2,a,W}(-i(s-\sigma))\).
The complete pole inventory between σ and c is:

* The pole of H(s) at one is canceled by the packet's double zero. Its nontrivial-zero and trivial-zero poles lie left of σ under RH.
* The real pole of H(2σ−s) is s=2σ−1<σ and is not crossed; the packet also has a double zero there, at t=+ia.
* Each reflected nontrivial zero contributes a possible pole at sρ=2σ−ρ, on Re(s)=2σ−1/2. If ρ has multiplicity mρ, the residue of H(2σ−s) is **+mρ** there.
* Reflected trivial-zero poles s=2σ+2k, k≥1, lie to the right of c. No others are crossed.

In this section each residue is indexed by a **distinct** nontrivial zero ρ, with its multiplicity mρ included once. This differs from the ordinate multiset convention in Rδ above. The full reflected residue is
\[
\mathcal R_\rho=m_\rho H(2\sigma-\rho)X^{\sigma-\rho}
 w_{2,a,W}(-i(\sigma-\rho)).
\tag{23}
\]
The packet factor is nonzero: at ρ=1/2+iγ its argument is −γ−iδ, with δ>0 and γ≠0, so it is neither ±ia nor a real sinc zero. An accidental zero of H(2σ−ρ) could remove an individual residue; there is no systematic packet cancellation of this family.

With upward vertical-line orientation, the exact formula is
\[
\boxed{\begin{split}
\mathcal I_\sigma(X)={}&X^d\int H(c+it)H(2\sigma-c-it)
 X^{it}w_{2,a,W}(t-id)dt\\
&-2\pi\sum_\rho\mathcal R_\rho.
\end{split}}
\tag{24}
\]
The residue sum in (24) runs over **distinct nontrivial zeros**; mρ is already present in (23), so no second multiplicity factor is inserted. The minus sign comes from Iσ=Ic−2πi times the crossed residues before replacing ds by i dt. Conjugate zero pairs make the residue sum real.

To justify the shift, choose horizontal heights tending to infinity at distance at least a fixed positive constant divided by log height from every zero ordinate; unit-interval zero counting supplies such heights. The logarithmic derivatives on those segments are O(log² height), while the shifted packet is O(t⁻²), so horizontal integrals vanish. On the final c-line, the reflected real part 2σ−c lies strictly between 0 and 1/2, separated from the RH zero line; vertical integrals converge absolutely. The residue series is absolutely convergent for fixed parameters: H(2σ−ρ) grows at most as a fixed logarithmic power, the packet contributes O_{σ,W}(γ⁻²), and zero density is only logarithmic. No uniformity as σ↓1/2 is inferred.

There is no line on which both H factors have absolutely convergent prime series: it would require Re(s)>1 and 2σ−Re(s)>1, impossible for σ<1. Expanding the first factor alone on the c-line does not delete the second or preserve a simple compact Dirichlet coefficient.

The arithmetic geometry differs even where both expansions are legal. For a comparison parameter σ*>1, |H(σ*+it)|² with carrier X^{it} gives a Fourier kernel in log(m/(Xn)), a **ratio** restriction on infinitely many pairs m,n. H² gives a **product** restriction mn≈X and thus the finite coefficient C₂. This comparison does not analytically continue a divergent double series into σ<1.

## 6. Parameter derivatives: explicit nonzero cancellation

For fixed W and a=1−σ,
\[
\partial_\sigma w_{2,a,W}(t)
=-4a(t^2+a^2)h_{6,W}(t)/W^4.
\tag{25}
\]
For σ in a fixed compact subinterval of (1/2,1), absolute domination gives
\[
\frac d{d\sigma}\mathcal E_{\sigma,W}
=2\Re\int H'(\sigma+it)\overline{H(\sigma+it)}w_{2,a,W}(t)dt
+\int|H(\sigma+it)|^2\partial_\sigma w_{2,a,W}(t)dt.
\tag{26}
\]
The weight derivative must be included.

Its nonvanishing can be checked exactly. Differentiate (15), with X=1,W≥3. The two terms are
\[
\boxed{\int2H(\sigma+it)H'(\sigma+it)w_{2,a,W}(t)dt
=16\pi a^2h_{6,W}(-ia)/W^4,}
\tag{27}
\]
\[
\boxed{\int H(\sigma+it)^2\partial_\sigma w_{2,a,W}(t)dt
=-16\pi a^2h_{6,W}(-ia)/W^4.}
\tag{28}
\]
Here \(h_{6,W}(-ia)=(\sinh(a/(2W))/(a/(2W)))^6>0\). Neither term vanishes; they cancel.

Indeed, for z=s−1 and t=−i(s−σ),
\[
t^2+a^2=-2az-z^2,\qquad
w_2(t)=4a^2z^2h_{6,W}(-ia)/W^4+O(z^3).
\]
Since \(2HH'=-2z^{-3}+O(z^{-2})\), its surviving residue is −8a²h₆,W(−ia)/W⁴. Meanwhile (25) gives \(\partial_\sigma w_2(t)=8a^2zh_{6,W}(-ia)/W^4+O(z^2)\), so H² times that weight has residue +8a²h₆,W(−ia)/W⁴. Both right-line arithmetic pairings have empty compact sums at X=1,W≥3: their coefficients still start at n=4, and multiplying by these polynomials preserves Fourier support [−3/W,3/W]. The contour sign proves (27)–(28).

If W also varies, an additional decay issue appears. Set j(z)=(sin z/z)^6. The formal derivative is
\[
\partial_Ww_2=-4w_2/W
-\frac{(t^2+a^2)^2}{W^4}\frac{t}{2W^2}j'(t/(2W)).
\tag{29}
\]
For sinc⁶ the second term is only O(1/|t|); the earlier argument therefore does not justify absolute dominated differentiation of the energy in W. Additional oscillatory analysis or a different packet is needed. For example sinc⁸ gives t⁻⁴ weight decay and t⁻³ first W-derivative decay, enough for absolute domination against logarithmic powers. No W-differentiated sinc⁶ energy identity is claimed.

## 7. Relation to the Bragg question and the remaining transfer

At W=T and X=T², (8) is a finite multiplicative prime-product sum in \((T^2e^{-3/T},T^2e^{3/T})\), of width asymptotic to 6T. Every prime power and every sign of K₂,b remains. It is a legitimate arithmetic object but measures H², not the R16 nonnegative spectral bump near α=2.

At X=1, (19)–(21) give a correct positive energy. Their kernel depends on both zero ordinates through the time weight, not only their difference. The Bragg statistic has a fixed frequency bump, truncation to 0<γ,γ'≤T and a Lorentzian pair weight. Compact support and the empty holomorphic sum do not identify these kernels.

A transfer must specify a scaling, for example δ comparable to 1/log T, keep the actual gamma center, control negative and high zero ordinates, justify time-window and pair-weight replacements, and produce the desired frequency localization with all signs and constants. Varying σ or W must retain §6. None of those asymptotic replacements follows automatically from the fixed-parameter identities.

The established statements are (8), (13)–(17), the centered positive relation (19), the reflected-residue formula (24), and the nonzero derivative cancellation (27)–(28). The excluded shortcut is replacing H² by |H|² or dropping reflected-zero residues. No estimate for the Bragg strict deficit follows yet.

## 8. Provenance and verification scope

This note uses unchanged R16 `COMPACT_POLE_PACKET.md` as the linear precedent and unchanged R7 `TWO_SCALE_ZETA_TARGET.md`, §§5–6, for the paired-ξ and gamma normalization. R7 already states that a weighted real-square/modulus conversion needs its own contour argument; (15)–(19) supply one for this particular packet. Source/report hashes are recorded in the adjacent receipt.

These are ordinary analytic derivations. No numerical zeta integral, parameter sweep, random-matrix analogy or model-to-arithmetic transfer is used as evidence. Independent mathematical review is separate.
