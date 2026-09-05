# Independent review of the centered mixed-moment remainder

Date: 2026-09-05. Reviewer: root Astra, independently of the authoring lane. The centered arithmetic identity and its error bounds are accepted under RH. Neither sufficient lower bound for the remainder is proved.

Reviewed author SHA256: `85c9435bbd656bcf37f21f55fe2d54cb40638c7a56908abe57e54f551a627daa`.

## Source and continuation

I checked Proposition 5, equation (2.3), in the retained primary HTML of Chirre, arXiv:2107.13636v2. The statement is for fixed integer k>=1 and fixed positive a in the displayed asymptotic. It includes the unknown integral of alpha^(2k) exp(-2a alpha) F(alpha,T) beyond alpha=1. The note correctly declines to differentiate its unspecified remainder or use it as a uniform growing-width estimate. Theorem 1's equivalence with pair correlation does not furnish the required one-sided estimate under RH alone.

Stieltjes summation with theta(x)-x and primes N<p<=Y gives both endpoint terms with the written signs. Its tail equals minus E_1(Y)Y^(-s) plus s times the remaining integral. RH bounds it by Y^(-delta) times the displayed polynomial in log Y and inverse delta. Differentiation in s adds one logarithm, with the next inverse-delta power. This is a legitimate fixed-T limit, unlike termwise use of an uncentered prime series in the critical strip.

For b>=2, delta>=1/log T. With Y=exp((log T)^3), the coarse uniform error is bounded by T(log T)^13 exp(-(log T)^2), up to a fixed constant. This validates a mathematical cutoff but supplies no feasible brute-force experiment.

## Norms and the pole

The local-zero derivative has majorant O(log T/delta^2) before division by log T. The prime-power correction and its derivative have the stated inverse-delta bounds; the finite polynomial uses weights bounded by the original ones. These give the sufficient coarse L2 bound sqrt(T)(log T)^2 for both factors, uniformly on the slow range.

The pole is N^(1-s)/(s-1). Since sigma<=3/4 its L2 norm is O(sqrt N), including the low-height part. Direct differentiation gives the coefficient log N/log T-1+1/((log T)(s-1)), so its companion is O((log log T)/(log T))sqrt N. Cauchy--Schwarz after normalization gives O(exp(b)(log T)^(-3)). It is o(b^(-3)) when b<=2G(T), G=o(log log T). The endpoint involving E_1(N) is retained throughout.

## Diagonal and the combined remainder

Expanding the two finite centered measures, integrating time, taking real parts, and exchanging x,y gives the symmetric factor (u(x)+u(y))/2 times sinc_0(T log(x/y)). On the prime diagonal this reduces to u(p), with exactly two factors log p. The continuous measure has no atomic diagonal mass.

For partial summation write f(x)=(log x)(log x/log T-1)x^(-1-b/log T). The RH error theta(x)-x is O(sqrt(x)log^2 x). Its endpoint plus the integral against f' is O(N^(-1/2)(log T)^3), uniformly for the stated b; multiplying by exp(b)/(log T)^2 gives the author's conservative O(exp(b)N^(-1/2)log T). No unproved short-interval estimate is used here.

The main integral from v=1 is exactly b^(-2)+2b^(-3). The omitted strip log N/log T<v<1 has width O(log log T/log T), negative integrand of size proportional to that width, and hence a squared-width error. Multiplication by b^3 makes both errors vanish uniformly. Thus the positive diagonal is correct, and the short-prime slice below T cannot provide its leading term.

The limit of the full centered expression exists; its diagonal converges absolutely. Subtracting the latter defines the combined remainder. No separate limits of the prime-continuum pieces are asserted. This distinction is essential and is preserved in the report.

Integrating the diagonal over [b,2b] gives 1/(2b)+3/(4b^2). The proposed integrated remainder threshold then leaves a coefficient strictly above -3/4 after normalization. This checks the constants, but supplies no proof of that threshold. The reported long-polynomial error is a failed upper majorant, not a lower bound on the actual error.

The result identifies a specific arithmetic obligation and rules out an unjustified use of a fixed-width derivative theorem. It does not establish a new zeta pair-correlation bound.
