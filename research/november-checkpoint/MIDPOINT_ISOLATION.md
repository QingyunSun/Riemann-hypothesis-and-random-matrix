# Testing the surroundings of one zeta gap at its midpoint

The input is a known pair of consecutive simple zero ordinates $a<b$, with gap $d=b-a$ and midpoint $m=(a+b)/2$. Assume first that RH holds. Sum over every other nontrivial zero ordinate $\gamma$, including negative ordinates and multiplicities, and set
\[
G=\sum_{\gamma\ne a,b}\left((\gamma-a)^{-2}+(\gamma-b)^{-2}\right).
\]
The classical Lehmer-pair condition is $d^2G<4/5$. Using ordinates in the usual $\zeta(1/2+i\gamma)$ normalization leaves this dimensionless condition invariant under the factor-of-two normalization of the Newman heat flow. The historical pair near 7005 already has a classical proof. Here it is a calibration for a single off-line evaluation. [Csordás–Smith–Varga](https://www.math.kent.edu/~varga/pub/paper_206.pdf) · [Stopple](https://arxiv.org/abs/1508.05870)

## A one-value sufficient condition

Put $s=1/2+d/2+im$, $V=d\operatorname{Re}(\xi'/\xi)(s)$ and $R=2V-4$, where $\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2$.

**Lemma.** If $R<7-3\sqrt5$, the pair satisfies the Lehmer inequality. More precisely, for $R<2$,
\[
2R\le d^2G\le\frac{2R}{(1-R/2)^2}.
\]

**Proof.** At any positive horizontal offset $h$, the real part of the completed logarithmic derivative under RH is the sum of $h/(h^2+(m-\gamma)^2)$ over all ordinates. In the genus-one product the real additive constant cancels by the symmetry of $\xi$ about $1/2$ (or by pairing zeros and evaluating at the center). The real series is absolutely convergent. At $h=d/2$, a selected endpoint contributes exactly one to $V$. After subtracting both selected zeros, $R=\sum r_\gamma$, with
\[
y_\gamma=(\gamma-m)/d,\qquad r_\gamma=(y_\gamma^2+1/4)^{-1}.
\]
Every exterior zero has $|y_\gamma|>1/2$. Its contribution to $d^2G$ is exactly
\[
(y_\gamma-1/2)^{-2}+(y_\gamma+1/2)^{-2}
=\frac{2r_\gamma}{(1-r_\gamma/2)^2}.
\]
The factor multiplying $r_\gamma$ increases on $[0,2)$. Use $r_\gamma\le R$, sum, and solve $2R/(1-R/2)^2=4/5$. Concentration in a single exterior atom attains the upper inequality for arbitrary local point data. No sharpness on zeta is asserted.

## What a verified critical-line window suffices to bound

Drop global RH. Define $G_{\rm proj}$ with **all ordinates** counted, including those of potential off-line zeros. Suppose all zeros in $|\gamma-m|<H$ are on the line, where $H>1/2$ in raw ordinate units. Pair off-line zeros at the same ordinate using the functional equation, so their real offsets from the line are $u,-u$, $|u|<1/2$. With $v=m-\gamma$ and $A=h^2+v^2$, the average contribution to the real logarithmic derivative per zero of this pair is
\[
\frac{h(A-u^2)}{(A+u^2)^2-4h^2u^2}.
\]
Relative to the contribution $h/A$ of its projected ordinate, this is at least $c=(1-\varepsilon)/(1+\varepsilon)^2$ with $\varepsilon=1/(4H^2)$, since $u^2/A\le\varepsilon$ for the far pairs. On-line zeros have ratio one. Remove the two known endpoints *before* dividing by $c$. The sum of the exterior projected $r_\gamma$ is at most $R/c$. Therefore $R/c<7-3\sqrt5$ suffices for $d^2G_{\rm proj}<4/5$. The Platt–Trudgian theorem supplies $H=3\cdot10^{12}-m$ for the finite samples below. The resulting unconditional statement concerns the static geometry of projected ordinates. Establishing an actual collision under the true $H_t$ flow requires additional hypotheses or a local evolution proof. [Verified height theorem](https://arxiv.org/abs/2004.09765)

## Independent endpoint calculation

At a simple zero $s_j=1/2+i\gamma_j$, expand $\zeta(s_j+z)=a_1z+a_2z^2+a_3z^3+\cdots$. Write $f=\xi/\zeta$ and let
\[
B_j=\operatorname{Re}\left[(\log f)''(s_j)+2a_3/a_1-(a_2/a_1)^2\right].
\]
This is the derivative of the real-part expression in the sense of taking the real part after complex differentiation of the regular part of $\xi'/\xi$. A remaining zero at offsets $u=\beta-1/2$, $v=\gamma_j-\gamma$ contributes $(v^2-u^2)/(v^2+u^2)^2$. Relative to the projected term $1/v^2$ the ratio is exactly $(1-w)/(1+w)^2$, $w=u^2/v^2$. For a pair below the verified height take $H'=3\cdot10^{12}-b>1/2$ and $c'$ as above with $H'$. The mutual endpoint contributions equal two after scaling, so
\[
D_{\rm reg}=d^2(B_a+B_b)-2
\le d^2G_{\rm proj}\le D_{\rm reg}/c'.
\]
Under RH the left-hand inequality is equality. This comparison uses derivatives at both zeros. It gives a more expensive reference decision for the cheaper midpoint test.

## Interval computation on actual zeta zeros

For each listed starting index we took **every** consecutive pair with first index in the next 128 positions. One block deliberately contains the historical Lehmer pair. These are three finite windows, chosen without a random-sampling design. The input coordinates were obtained from FLINT's certified zeta zero isolator and the local series from Arb ball arithmetic. All endpoint derivatives were checked to exclude zero. Gamma, digamma, polygamma and the rational prefactor are included. No Euler series in its divergent half-plane was used.

| First index | Pairs tested | Certified by midpoint | Below threshold by endpoint bounds |
|---:|---:|---:|---:|
| 2 | 128 | 1 | 4 |
| 6645 | 128 | 7 | 10 |
| 99937 | 128 | 7 | 10 |
| Total | 384 | 15 | 24 |

For indices 6709 and 6710, $d=0.037698497726140188\ldots$. The midpoint gives $R=0.003464431821462037\ldots$ and $d^2G_{\rm proj}<0.006953$. The endpoint check puts it within $10^{-16}$ of $0.00693322993030569$. The signed decisions at 176 and 224 bits agree for every tested index. The nine additional endpoint positives are explicit examples of the midpoint criterion's loss of information. No density conclusion follows from these counts. [FLINT zeta functions and zeros](https://flintlib.org/doc/acb_dirichlet/index.html)

## What a prime estimate would need to establish

At a pair-dependent point $s$, the rational and gamma parts of $\xi'/\xi(s)$ are explicit. The remaining input is $\operatorname{Re}(\zeta'/\zeta)(s)$. A smoothed prime-power formula with controlled tail would have to keep an error below the threshold margin **at those selected heights**. For a density theorem, one additionally needs enough qualifying pairs across all high intervals. No fixed-frequency mean bound supplied here achieves that selection. The historical Conrey–Iwaniec implication needs many sub-half gaps, separate from the isolation requirement. [Conrey–Iwaniec](https://arxiv.org/abs/math/0111012)

**Replay.** Run `python -m pip install python-flint==0.8.0`, then `python check_midpoint.py` or `python check_midpoint.py --bits 224`. The accompanying JSON records each index, outward-rounded intervals, both classification flags and the normalized gap. Arb interval lengths are computational enclosures, not sampling uncertainties. The underlying use of a logarithmic derivative to test Lehmer pairs has precedents. Independent priority review of this particular test remains open.
