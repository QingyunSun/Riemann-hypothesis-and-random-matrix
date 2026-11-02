# Independent review of the actual-zeta Poisson transfer

5 September 2026. This reviews the root agent's proposed transfer, not a proof of the desired arithmetic mean-square asymptotic. All statements below assume RH and a fixed $b>0$.

Put $L=\log T/(2\pi)$ and

$$
K_b(u)=\frac{2b}{b^2+4\pi^2u^2},\qquad
Q_T(b)=\frac1{TL}\sum_{0<\gamma,\gamma'\le T}K_b(L(\gamma-\gamma'))-1.
$$

The proposed identity has the correct factor:

$$
Q_T(b)=\frac2{T\log^2T}\int_0^T
\left|\frac{\zeta'}\zeta\left(\frac12+\frac{b}{2\log T}+it\right)\right|^2dt+o(1).
$$

The following checks support it.

1. If $P_a(u)=a/[\pi(a^2+u^2)]$, then $K_b=P_{2a}$ with $a=b/(4\pi)$. The physical displacement is $\delta=a/L=b/(2\log T)$. For $Y(t)=\sum_{0<\gamma\le T}P_a(L(t-\gamma))$, convolution gives the exact identity $T^{-1}\int_{\mathbb R}Y^2=Q_T(b)+1$. No circular periodization is involved.
2. The full positive zero density is $Z(t)=(\pi L)^{-1}\operatorname{Re}(\xi'/\xi)(1/2+\delta+it)$, by the symmetrically paired Hadamard product. On the interval interior, the omitted zeros below zero or above $T$ contribute $O_b(\log T/(L^2w))$ if the distance to the endpoints is at least $w=T/\log^4T$.
3. The unit-interval zero bound implies $Y,Z=O_b(\log T)$ near the endpoints. Their squared contribution divided by $T$ is $O_b(w\log^2T/T)=O_b(\log^{-2}T)$. Outside the interval and at distance $d\ge w$, one can use $Y\ll_b\log T/(L^2d)$ until $d$ reaches $T$, then $Y\ll_b N(T)/(L^2d^2)$. These bounds make the exterior squared integral $o(T)$. They avoid the incorrect use of a constant bound on an infinite exterior interval.
4. The mean $T^{-1}\int_0^TY\to1$ follows from the zero-count asymptotic and the Poisson tail estimate. The same holds for $Z$. The gamma and elementary factors give

$$
Z(t)-1=\frac2{\log T}\operatorname{Re}\frac{\zeta'}\zeta(1/2+\delta+it)
+\frac{\log(t/(2\pi))-\log T}{\log T}
+\text{a negligible compact-height correction}.
$$

The displayed drift has mean square $O(\log^{-2}T)$ after averaging over $[1,T]$. Uniform boundedness of the pair-kernel quadratic form controls its cross term by Cauchy–Schwarz.
5. For $q(s)=\zeta'/\zeta(s)$, a rectangle with vertical sides $\sigma=1/2+\delta$ and $\sigma=2$ and lower height $1$ avoids the pole at $s=1$. Under RH, $|q(\sigma+iT)|\ll_b\log^2T$ uniformly along its top, even when $T$ is a zero ordinate. Thus the top integral of $q^2$ is $O_b(\log^4T)$. At $\sigma=2$, the squared absolutely convergent Dirichlet series has no constant term and has a bounded time primitive. The lower side is harmless; alternatively choose any fixed lower height away from zero ordinates and treat the omitted compact interval separately. Consequently $\int_0^Tq(1/2+\delta+it)^2dt=o(T\log^2T)$. Using $(\operatorname{Re}q)^2=(|q|^2+\operatorname{Re}q^2)/2$ produces the claimed factor $2$.

For passage from AH-Pairs to Poisson tests, the cumulative local-pair bound in GLSS (1.12), printed p.4, suffices. It is only stated up to normalized radius $T$. Dyadic summation gives $O(1/R)$ tails for the Poisson pair kernel inside that range, and the total-mass bound gives $O(\log T/T)$ outside it. A global uniform translation bound is not required.

The nuisance term in the centered spectral measure is $2(p_0-1)\sum_m\delta_{2m+1}$. Against $e^{-b|\alpha|}$ it contributes $2(p_0-1)/\sinh b$. Hence a signed combination $\sinh(b_1)Q_T(b_1)-\sinh(b_2)Q_T(b_2)$ can eliminate this parameter without a limit assumption on $P_0(T)$: first truncate at radii $M=j+1/4$ to avoid half-lattice boundary atoms, apply the uniform finite-$T$ density formulas, and then use the tail estimates.

Verdict: the normalization, endpoint strategy, complex-square cancellation, and nuisance-parameter elimination are consistent. The remaining mathematical input is an actual estimate of the resulting signed logarithmic-derivative mean squares. The transfer identity itself does not provide that estimate or refute AH.
