## Independent endpoint check on the first Lehmer pair

At the simple root $s_j=1/2+i\gamma_j$, let $a_k=\zeta^{(k)}(s_j)/k!$ and let $f(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/2$. Differentiating the regular part of $\log\xi$ twice gives
$$
b_j=\Re\!\left[-s_j^{-2}-(s_j-1)^{-2}+\tfrac14\psi_1(s_j/2)+2a_3/a_1-(a_2/a_1)^2\right].
$$
The differentiated Hadamard series is absolutely convergent. Every other zero with real displacement $u=\beta-1/2$ and ordinate displacement $v=\gamma-\gamma_j$ contributes $(v^2-u^2)/(v^2+u^2)^2$. Writing $d=b-a$ for the gap, $D_{\rm reg}=d^2(b_1+b_2)-2$ removes the two ordered evaluations on the partner root. Below the verified critical-line height $3\cdot10^{12}$ the remaining terms are the projected inverse-square terms. Beyond that height their ratio to the corresponding projected term is $(1-x)/(1+x)^2$, $0\le x=u^2/v^2\le\epsilon=1/[4(3\cdot10^{12}-b)^2]$. Thus $D_{\rm reg}\le d^2 G_{\rm proj}\le D_{\rm reg}(1+\epsilon)^2/(1-\epsilon)$. [Platt–Trudgian](https://arxiv.org/abs/2004.09765).

Independent evaluation used real Hardy $Z(t)$, for which $\xi(1/2+it)=A(t)Z(t)$ and $|A(t)|=(1/4+t^2)\pi^{-1/4}|\Gamma(1/4+it/2)|/2$. Consequently
$$b_j=(Z''/(2Z'))^2-Z'''/(3Z')-(\log|A|)'',\qquad
(\log|A|)''=2(1/4-t^2)/(1/4+t^2)^2-\tfrac14\Re\psi_1(1/4+it/2).$$

Independent 48-decimal mpmath evaluation with differentiation of real Hardy $Z$ and separate complex zeta jets agreed to $4.0\cdot10^{-44}$ at the two endpoints. A second implementation used python-flint 0.8.0, 215 bits, certified zero balls from `acb.zeta_zero` and order-four `arb_series.riemann_siegel_z`. At consecutive indices 6709 and 6710, heights $7005.06286617492058138\ldots$ and $7005.10056467264672157\ldots$, it enclosed
$$
D_{\rm reg}=0.0069332299303056902699095463211255669219767421253932058\;\pm5.0\cdot10^{-56},
$$
with projected upper endpoint $0.00693322993030569026990954689889473047900499072349173772\;\pm8.1\cdot10^{-57}$. The width due to possible remote off-line zeros is $5.77769163557\cdot10^{-28}$. As a separate rough check, summing only positive zero indices 6700–6719 outside the pair gives $0.00622423424470\ldots$.

This is an unconditional verification of a projected-ordinate inequality at a classical pair. The usual inference to the Lehmer-pair heat statement assumes RH. No lower bound on the frequency of such pairs follows from a successful sample check.
