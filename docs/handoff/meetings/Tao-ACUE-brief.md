# Testing the half-lattice model for zeta zeros

Discussion with Terence Tao · 5 November 2026

The Alternative Hypothesis allows normalized zeta gaps to concentrate near half-integers. Tao’s 2019 alternative circular unitary ensemble (ACUE) realizes this geometry with $N$ eigenangles on $2N$ equally spaced sites. Its low trace moments agree exactly with those of a Haar unitary matrix (CUE). We seek a statistic that separates the models and can also be estimated for zeta zeros.

**One test on actual zeros.** Assume RH. Let $F_T$ be Montgomery’s form factor and let $\phi$ be a smooth probability density on $[6/5,7/5]$, symmetric about $13/10$. Under AH-Pairs, half-lattice support makes the limiting form factor 2-periodic, giving $\int\phi F_T\to 7/10$. Montgomery’s conjecture predicts $1$. The prime diagonal contributes $13/10+o(1)$. A subsequential lower bound strictly above $-3/5$ for the signed, centered remainder would therefore rule out AH-Pairs. This estimate is open. In a separate frequency-two calculation under RH, one family of balanced sums is $o(1)$ for $T^{2+\varepsilon}\le X\le T^{9/4}$. A signed Möbius–prime correlation remains at $X=T^2$.

**Three-point tests.** Take $10\mid N$ and write $p_m=\operatorname{tr}(U^m)$. At $m=3N/5$, the mean of $p_m^2\overline{p_{2m}}/N$ is $1/5$ in CUE and zero in ACUE. Removing repeated indices gives zero in both ensembles. For the ordered sum over three distinct indices at frequencies $(11,1,-12)N/10$, the normalized means are instead zero and $1/5$, respectively. Even this difference can be expressed through the known pair form factor.

**What heat flow detects.** For scalar flow of the characteristic polynomial, $a_j(s)=a_j(0)e^{sj(N-j)}$, let $D$ be the first collision time and $\delta$ the smallest angular gap. For Haar CUE, $8D/\delta^2\to1$ in probability. Nonclock ACUE configurations satisfy $N^2D\ge\pi^2/8$. Two six-point configurations on the twelfth roots have identical pair differences and gap histograms, yet differ in their heat response and in a clipped Gram trace. For one window used in zeta zero counting, the half-lattice Gram norm is below 2.217, short of its clipping threshold of 3.4. Under circular Dyson Brownian motion, ACUE and CUE still match at several times if the total positive and negative trace weights are each at most $N$ across all observations.

**Other results.** Among intensity-one processes with a Hermitian convolution determinantal kernel, the full sine pair density determines the sine process. In general, planting one close pair preserves every fixed local sine limit while forcing an arbitrarily small minimum gap. Separately, we verified an admissible 39-tuple of diameter 182. A sieve estimate forcing two primes in infinitely many translates remains open.

## Five questions for discussion

1. For the $7/10$ test, which average over prime shifts $h\asymp x/T$ offers the best chance of retaining the sign lost in a mean-square bound?
2. Which combination of three- or four-point tests would cancel the known pair contributions and leave one arithmetic term we could estimate, perhaps first over a function field?
3. Can a positive perturbation of finite ACUE preserve both its pair-data law and *all* its mixed trace moments through weight $N$ on each side, while changing a specified higher moment?
4. Which bandlimited window could make spectral clipping active on a half-lattice and still yield a usable inequality for counting zeros?
5. What estimate on the zeros surrounding a close pair would be accessible from the explicit formula and strong enough to control its first heat collision?

[Tao’s original ACUE note (2019)](https://terrytao.wordpress.com/2019/05/08/the-alternative-hypothesis-for-unitary-matrices/) · [Precise AH-Pairs formulation](https://arxiv.org/abs/2507.06823) · [Gram window](https://arxiv.org/abs/2609.33043) · [Research archive, PR 1](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/pull/1)
