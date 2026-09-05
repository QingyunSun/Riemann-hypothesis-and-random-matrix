# Two Poisson scales remove the AH near-diagonal parameter

Date: 2026-09-05. Status: written reduction and exact constant certificates; [independent ordinary-proof review completed](INDEPENDENT_REVIEW.md). The actual arithmetic inequality stated below is **not proved**. No novelty claim is made for the standard pair-correlation/logarithmic-derivative correspondence.

The useful target is now one explicit inequality for actual zeta mean squares. Put

\[
I_T(c)=\int_0^T\left|\frac{\zeta'}{\zeta}
 \left(\frac12+\frac{c}{\log T}+it\right)\right|^2dt,
\qquad
W_T=\frac{2}{T\log^2T}\left(\sinh(2)I_T(1)-\sinh(1)I_T(1/2)\right).
\tag{1}
\]

Under RH plus the precise AH-Pairs formulation discussed below, the reduction gives

\[
W_T\longrightarrow W_{\rm AH},\qquad
0.06239<W_{\rm AH}<0.06240.
\tag{2}
\]

The sine-kernel prediction is instead

\[
W_{\rm GUE}=0.0822714431214773\ldots.
\tag{3}
\]

Consequently, an actual proof under RH of

\[
\boxed{\liminf_{T\to\infty}W_T\ge\frac7{100}}
\tag{4}
\]

would refute AH-Pairs under RH. This asks for a one-sided inequality for one signed combination, not the full pair-correlation conjecture. It remains a substantial open arithmetic task. The reduction does not make (4) follow from RH or the known Fourier band.

The number 0.07 is a convenient stronger target, not a required threshold. The same exact enclosure already shows \(W_{\rm AH}<0.06240<1/16\). Thus the weaker bound \(\liminf W_T\ge1/16\) also suffices, with a separation exceeding 0.00010. Any proved lower limit strictly exceeding W_AH is acceptable; neither rational lower bound has been established here.

## 1. Definitions and the existing source input

Use Fourier transform \(\widehat f(\alpha)=\int f(x)e^{-2\pi i\alpha x}dx\), and put \(L=\log T/(2\pi)\). Multiplicities are counted throughout. Let

\[
\mu_T=\frac1{TL}\sum_{0<\gamma,\gamma'\le T}
\delta_{L(\gamma-\gamma')}.
\]

The precise AH-Pairs assumption is (AH0) in [Goldston–Lee–Schettler–Suriajaya, *Pair Correlation Conjecture II: The Alternative Hypothesis*, 2507.06823](https://arxiv.org/html/2507.06823v1): all bounded normalized pair differences in the stated high interval approach half integers with the specified decreasing error. We use its RH-dependent equations (1.14)–(1.15), and the cumulative pair bound (1.12). These are distinct from that paper's unconditional results with additional AH-Weak Density assumptions.

For each fixed half integer, the pair masses have the form, up to o(1),

\[
p_{k/2}(T)=
\begin{cases}
p_0(T),&k=0,\\
p_0(T)-1/2,&k\ne0\text{ even},\\
3/2-p_0(T)-2/(\pi^2k^2),&k\text{ odd},
\end{cases}
\tag{5}
\]

with bounded \(1+o(1)\le p_0(T)\le3/2-2/\pi^2+o(1)\). We do not assume p_0(T) converges. The symbol here abbreviates the source's finite-T P_0(T), not an already existing limit.

The base p_0=1 measure is the pair measure of the randomly translated half-lattice sine process. Relative to it, (5) adds

\[
(p_0(T)-1)\sum_{k\in\mathbb Z}(-1)^k\delta_{k/2}.
\tag{6}
\]

Formula (6) includes the diagonal. Dropping it would give the wrong nuisance term.

## 2. Bounded smoothing and exact model formulas

For a>0 define \(P_a(x)=a/[\pi(a^2+x^2)]\). Its Fourier transform is \(e^{-2\pi a|\alpha|}\). If a stationary unit-intensity process has centered structure-factor measure S, its smoothed-density variance is

\[
V(a)=\int e^{-4\pi a|\alpha|}\,dS(\alpha).
\tag{7}
\]

Write b=4πa and abbreviate this variance by V(b). For the sine process, \(dS=\min(|\alpha|,1)d\alpha\), giving

\[
V_{\rm sine}(b)=\frac{2(1-e^{-b})}{b^2}.
\tag{8}
\]

The centered spectral measure for the half-lattice model is

\[
dS_{\rm A}(\alpha)=\operatorname{dist}(\alpha,2\mathbb Z)\,d\alpha
 +\sum_{m\in\mathbb Z\setminus\{0\}}\delta_{2m}.
\tag{9}
\]

Here the distance ranges from zero to one. To derive (9), its pair measure is
\(\delta_0+\frac12\sum_{k\ne0}(1-\operatorname{sinc}^2(k/2))\delta_{k/2}\), where sinc(x)=sin(πx)/(πx). Poisson summation transforms the comb into atoms at even integers, and the sampled sinc-square into the sum of triangular functions centered at even integers. Subtracting the mean-density contribution removes only the atom at frequency zero. Thus

\[
V_{\rm A}(b)=\frac{2\tanh(b/2)}{b^2}+\frac2{e^{2b}-1}.
\tag{10}
\]

The even-frequency atoms in (9) are essential; the triangular density alone gives a wrong answer. Direct integration of one triangular period and a geometric series proves (10).

For every b>0,

\[
\Delta(b):=V_{\rm sine}(b)-V_{\rm A}(b)
=\frac{2e^{-2b}\big(4\sinh^2(b/2)-b^2\big)}{b^2(1-e^{-2b})}>0,
\tag{11}
\]

because 2sinh(b/2)>b. The signal is \(b/12+O(b^2)\) as b decreases to zero, and \(2e^{-b}/b^2(1+o(1))\) as b increases to infinity. Very large smoothing therefore requires exponential accuracy relative to its algebraic main term. The leading variance alone cannot separate the models.

## 3. Eliminate the near-diagonal freedom rather than assume simplicity

The Fourier transform of the alternating comb in (6) is \(2\sum_m\delta_{2m+1}\). Its contribution to (7) is

\[
\frac{2(p_0(T)-1)}{\sinh b}.
\tag{12}
\]

Thus a single variance does not uniformly distinguish the full AH-Pairs class. The correct combination is

\[
W=\sinh(2)V(2)-\sinh(1)V(1).
\tag{13}
\]

The two nuisance terms cancel. Moreover,

\[
\sinh(b)\Delta(b)=H(b):=\frac{(1-e^{-b})^2}{b^2}-e^{-b},
\]

so the two predictions differ by

\[
H(2)-H(1)=0.01987902514497878\ldots>0.
\tag{14}
\]

In closed form, with e the ordinary exponential constant,

\[
W_{\rm AH}=\frac{e^2}{4}+\frac5{4e^2}-e-\frac2e+\frac32,
\]
\[
W_{\rm GUE}=\frac{e^2}{4}-e+\frac34+\frac1e-\frac5{4e^2}+\frac1{4e^4}.
\tag{15}
\]

The companion rational script bounds e by its degree-40 Taylor sum and a geometric upper bound for the tail. Ordinary interval arithmetic gives
\(W_{\rm AH}\in(0.06239,0.06240)\),
\(W_{\rm GUE}\in(0.08227,0.08228)\), and their difference in (0.019879,0.019880). These are exact constant enclosures. They contain no computed ζ mean square.

## 4. Passing from AH-Pairs to these noncompact pair tests

The convolution kernel in physical space is

\[
K_b(x)=P_{2a}(x)=\frac{2b}{b^2+4\pi^2x^2},
\qquad
Q_T(b)=\int K_b\,d\mu_T-1.
\tag{16}
\]

For fixed b this kernel and the two-scale linear combination decay as O_b((1+x²)^−1). The cited pair bound gives
\(\mu_T([-h,h])\ll1+h\) for 0≤h≤T. Dyadic shells therefore bound the tail between M and T by O_b(1/M). Beyond T, total pair mass is O(T log T) and the kernel is O_b(T^−2), giving O_b(log T/T).

Fix M first along values M=j+1/4, so the hard truncation endpoints lie away from all limiting half-lattice atoms. The finite set of half-lattice mass formulas (5), plus concentration of each bin at k/2, then evaluates the compact part without an unresolved boundary atom. The early-zero range excluded in AH0 changes the compact pair sum by o(1), as in the source's Section 2. The two tails are uniform in T. The model mass tails are also O_b(1/M), uniformly for bounded p_0(T). Hence

\[
Q_T(b)=V_{\rm A}(b)+\frac{2(p_0(T)-1)}{\sinh b}+o(1)
\tag{17}
\]

under RH and AH-Pairs. Formally: the limsup error is O_b(1/M) after T tends to infinity, then M tends to infinity. One cannot cancel a finite truncated alternating sum as though it were already the entire comb. This two-limit argument justifies the cancellation in (13) without requiring existence of lim p_0(T).

## 5. Actual completed-zeta resolvent: endpoints and centering

Here is the conversion from the pair statistic to the real part of an actual meromorphic function. All following b values are fixed and positive. Set a=b/(4π), η=a/L, and

\[
Y_T(t)=\sum_{0<\gamma\le T}P_a(L(t-\gamma)),\qquad
Z_T(t)=\sum_{\gamma\in\mathbb R}P_a(L(t-\gamma)).
\]

The second sum is over all nontrivial zero ordinates, including negative ordinates. Under RH the paired canonical product of ξ gives exactly

\[
Z_T(t)=\frac1{\pi L}\Re\frac{\xi'}{\xi}(1/2+\eta+it).
\tag{18}
\]

Pairing positive and negative zeros fixes the constant: ξ is even about 1/2, and the paired product has factors \(1+(s-1/2)^2/\gamma^2\). The real part of its logarithmic derivative is the absolutely convergent sum of η/[η²+(t−γ)²]. Formula (18) does not require simple zeros.

The finite convolution identity is exact:

\[
\frac1T\int_{\mathbb R}Y_T(t)^2dt=\int K_b\,d\mu_T=Q_T(b)+1.
\tag{19}
\]

We give the endpoint estimates because they must not be hidden in a stationarity assumption. Standard unit-interval zero counting gives O(log(|u|+2)) zeros in an interval of length one. Consequently, for fixed a, both Y_T and Z_T are O_a(log T) on [0,T]. Let w=T/log⁴T. The two endpoint strips of width w contribute at most O_a(log^−2T) to a normalized square integral.

On [w,T−w], the omitted positive zeros above T and the negative zeros contribute

\[
|Z_T(t)-Y_T(t)|\ll_a\frac{\log T}{L^2w}=o(1)
\]

uniformly, by summing the inverse-square kernel with the unit-interval bound. The pair bound used in Section 4 implies \(T^{-1}\int_{\mathbb R}Y_T^2=O_a(1)\), so the square-integral difference on the interior is o(1) by Cauchy–Schwarz.

For t outside [0,T] by a distance d≥w, the same unit-interval count yields \(Y_T(t)\ll_a\log T/(L^2d)\). Its exterior squared integral divided by T is o(1); the exterior strips of width w have the same O(log^−2T) bound. Finally, \(T^{-1}\int_0^TY_T(t)dt\to1\): the full integral is N(T)/L, boundary zeros number O(w log T), and for each interior zero the missing Poisson mass is at most O_a(L^−2(γ^−1+(T−γ)^−1)). Summing this last expression gives O_a(log²T/L²)=O_a(1). Division by T removes it.

It follows from (18)–(19) that

\[
Q_T(b)=\frac1T\int_0^T\left(\frac1{\pi L}\Re\frac{\xi'}{\xi}(1/2+\eta+it)-1\right)^2dt+o(1).
\tag{20}
\]

No assertion that the finite zeros are exactly stationary was used.

## 6. Gamma factor and the real-square versus modulus distinction

By definition,

\[
\frac{\xi'}{\xi}(s)=\frac{\zeta'}{\zeta}(s)+\frac1s+\frac1{s-1}
-\frac12\log\pi+\frac12\frac{\Gamma'}{\Gamma}(s/2).
\tag{21}
\]

For t≥1 and the specified σ near 1/2, the real part of the extra terms is \(\frac12\log(t/(2\pi))+O(1/t)\). After dividing by πL and subtracting one, its discrepancy from zero has normalized L² norm O(1/log T). This follows by integrating \(|\log(t/T)-\log(2\pi)|^2\), and treating 0≤t≤1 separately using the absence of low ordinates and (21). The pair bound gives a bounded normalized L² norm for (20); hence Cauchy–Schwarz justifies removing this discrepancy. We obtain

\[
Q_T(b)=\frac4{T\log^2T}\int_0^T
 \left(\Re\frac{\zeta'}{\zeta}(1/2+\eta+it)\right)^2dt+o(1).
\tag{22}
\]

It is not an algebraic identity that the real-square integral equals half the modulus-square integral. To justify that step here, let \(F=\zeta'/\zeta\). Under RH, F² is analytic in the rectangle with horizontal sides at heights 1 and T, and vertical sides at σ=1/2+η and 2. The pole at s=1 lies below this rectangle. On the right side F² has an absolutely convergent Dirichlet series without a constant term; its vertical integral is O(1). On the top side the RH partial-fraction estimate gives \(F=O_b(\log^2T)\), uniformly across the rectangle, so that horizontal integral is O_b(log⁴T). The bottom integral is bounded. Thus

\[
\int_0^TF(1/2+\eta+it)^2dt=O_b(\log^4T)=o(T\log^2T).
\]

The bounded initial segment adds no relevant term. Since \(2(\Re F)^2=|F|^2+\Re F^2\), (22) becomes

\[
\boxed{Q_T(b)=\frac2{T\log^2T}I_T(b/2)+o(1).}
\tag{23}
\]

This is consistent with the classical correspondence of Goldston–Gonek–Montgomery; [Fazzari, 2310.15918, Introduction and Lemma 3](https://arxiv.org/html/2310.15918v2) also records its normalization and explicitly separates the real-square and holomorphic-square terms. A weighted version would need its own contour argument; the unweighted vanishing above must not be silently reused with an arbitrary arithmetic weight.

Equations (17), (13) and (23) prove the claimed reduction (2), subject to the stated primary RH+AH-Pairs density input. The threshold (4) is still missing.

## 7. Finite ensemble calibration and what cannot prove (4)

On a circle of length N, periodize P_a. For nonzero integer m the CUE trace second moment is min(|m|,N). For the randomly rotated ACUE model it is min(r,2N−r) when r=m mod 2N is nonzero, and N² when r=0. The latter large peaks become the even-frequency atoms in (9).

With q=e^(−b/N), the exact finite CUE variance is

\[
V_N^{\rm CUE}(b)=\frac{2q(1-q^N)}{N^2(1-q)^2},\qquad
\frac{V_N^{\rm CUE}(b)}{V_{\rm sine}(b)}
=\left(\frac{b/(2N)}{\sinh(b/(2N))}\right)^2.
\tag{24}
\]

The finite ACUE formula is

\[
V_N^{\rm ACUE}(b)=\frac2{N^2}
\frac{\sum_{m=1}^{2N-1}\min(m,2N-m)q^m+N^2q^{2N}}{1-q^{2N}}.
\tag{25}
\]

The script checks eight widths, four finite sizes, direct triangular-period integrals, and exhaustive float64 subset sums for N=2,…,6. Symbolic checks verify (11), both limiting signal sizes, and the paired canonical-product normalization on an exact rational finite example. These are normalization tests and finite-model evidence, not ζ data or an asymptotic numerical proof.

The base half-lattice process itself obeys the known low-frequency pair data while giving W_AH. Therefore no deduction using only those data and positivity can establish (4). Its signed Fourier kernel is \(\sinh(2)e^{-2|\alpha|}-\sinh(1)e^{-|\alpha|}\), which changes sign at \(\log(2\cosh1)>1\). The remaining arithmetic work controls information beyond the known band, including the negative tail. A fresh prime-correlation estimate, or a new effective arithmetic weighting/comparison, is necessary. Enlarging the finite matrix model or improving numerical precision does not supply it.

The retained deliverable is a precise one-sided ζ target with certified separation and no assumed near-diagonal limit. Further work should attack its actual signed mean square or the companion compact Fourier test. External novelty review and proof-assistant formalization are postponed until the ordinary proof audit and the arithmetic direction justify them.
