# Prime powers are negligible in the remaining residual energy

Date: 2026-09-05. Status: ordinary proof draft for independent review. This is a quantified nuisance-term estimate, not a new lower bound for the signed residual and not a conjecture solution. Its purpose is to let the remaining covariance calculation use genuine primes.

## 1. Statement

Fix c>0, let T tend to infinity, and set

    delta=c/log T, sigma=1/2+delta, s=sigma+it,
    N=floor(T/log^6 T).

Let H=-zeta'/zeta(s), P_N=sum_(n<=N) Lambda(n)n^(-s), and R=H-P_N as in Round 8. Define the absolutely convergent prime-power tail

\[
U_{c,N}(t)=\sum_{\substack{p\ \mathrm{prime},\ k\ge2\\p^k>N}}
       (\log p)p^{-k\sigma-ikt\log p}.
\]

Uniformly for 0<delta<=1/4 and N>=4,

\[
\boxed{\|U_{c,N}\|_{L^2(0,T)}^2
\ll T N^{-1/3}\log^4(2N)+\delta^{-4}.}
\tag{1}
\]

The implied constant in (1) is absolute. The estimate itself does not assume RH. Under RH, the normalized residual energy changes by

\[
\boxed{\frac{\big|\|R-U_{c,N}\|_2^2-\|R\|_2^2\big|}
 {T\log^2T}
\ll_c N^{-1/6}\log^2(2N)+\frac{\log^2T}{\sqrt T}=o(1).}
\tag{2}
\]

Consequently the fixed two-scale residual in Round 8 can be replaced by its genuine-prime counterpart. Equation (2) is a bound on the replacement error; it gives no positive constant improvement in the desired signed comparison.

## 2. Squares: an elementary mean-value bound with an infinite tail

Write U_2(t)=sum_(p>sqrt N) (log p)p^(-1-2delta-2it). For the sequence

    a_n = (log n)n^(-1-2delta) if n is a prime greater than sqrt N,
          0 otherwise,

the series is absolutely convergent. Expanding the time integral, the diagonal is T sum |a_n|^2. The integrated off-diagonal kernel has absolute value at most 1/|log(m/n)| because the time frequency is 2log(m/n).

For n/2<=m<=2n, m!=n, uniformly in 0<delta<=1/4,

\[
\frac{|a_ma_n|}{|\log(m/n)|}
\ll \frac{\log^2(2n)}{n^{1+4\delta}|m-n|}.
\]

Summing the harmonic denominator over m and then over n gives

\[
\ll\sum_{n\ge2}\frac{\log^3(2n)}{n^{1+4\delta}}
\ll \delta^{-4}.
\]

For noncomparable m,n, the log denominator is at least log 2, so the contribution is at most a constant times

\[
\left(\sum_{n\ge2}\frac{\log n}{n^{1+2\delta}}\right)^2
\ll\delta^{-4}.
\]

These are convergent majorants for each delta>0. One may therefore first use finite sums and pass to the infinite sum by dominated convergence. No infinite polynomial mean-value theorem with a divergent error is invoked.

The diagonal tail satisfies

\[
\sum_{p>\sqrt N}\frac{(\log p)^2}{p^{2+4\delta}}
\le\sum_{n>\sqrt N}\frac{(\log n)^2}{n^2}
\ll N^{-1/2}\log^2(2N).
\]

Thus

\[
\|U_2\|_2^2\ll T N^{-1/2}\log^2(2N)+\delta^{-4}.
\tag{3}
\]

In particular, the exponent four in the error is intentional. A sharper Hilbert-inequality estimate is unnecessary for this use. The argument above is self-contained and only uses the actual support of prime squares and elementary upper bounds for their weights.

## 3. Higher powers: absolute convergence is now strong enough

Let

\[
A_3(x)=\sum_{\substack{p^k\le x\\k\ge3}}\log p.
\]

There are at most log(x)/log(2) relevant exponents, and for each k>=3 the number of possible bases is at most x^(1/3), with log p<=log x. Hence, for x>=2,

\[
A_3(x)\ll x^{1/3}\log^2(2x).
\]

Partial summation and sigma>=1/2 yield

\[
\sum_{\substack{p^k>N\\k\ge3}}(\log p)p^{-k\sigma}
\le \sigma\int_N^\infty A_3(x)x^{-\sigma-1}dx
\ll N^{-1/6}\log^2(2N).
\tag{4}
\]

For the last bound sigma is in [1/2,3/4], so sigma-1/3 is bounded below by 1/6 and all integration constants are uniform. The negative endpoint term from partial summation was discarded in the favorable direction. Equation (4) gives

\[
\|U_{\ge3}\|_2^2\ll T N^{-1/3}\log^4(2N).
\]

Combining this with (3), using |u+v|^2<=2|u|^2+2|v|^2, proves (1). Squares require a mean-square argument; applying the same absolute-value argument to squares would lose the useful decay.

## 4. Replacement in the actual RH residual

The pointwise RH partial-fraction bound already proved in Round 8 gives H(t)=O_c(log^2 T) throughout [0,T]. The elementary finite-polynomial mean-value bound there gives ||P_N||_2^2=O_c(T log^4 T). Consequently

    ||R||_2 <= C_c sqrt(T) log^2 T.

Set a_T=N^(-1/6)log^2(2N)+log^2(T)/sqrt(T). Equation (1), with delta=c/log T, gives ||U||_2/sqrt(T) <<_c a_T. By Cauchy-Schwarz,

\[
\frac{\big|\|R-U\|_2^2-\|R\|_2^2\big|}{T\log^2T}
\le\frac{2\|R\|_2\|U\|_2+\|U\|_2^2}{T\log^2T}
\ll_c a_T+\frac{a_T^2}{\log^2T}.
\]

Since a_T tends to zero at the stated cutoff, this proves (2) for sufficiently large T. The stronger RH pair-correlation bound on ||H|| is not needed. The same argument applies separately to c=1 and c=1/2, whose fixed hyperbolic coefficients preserve the o(1) replacement error.

## 5. The remaining error really is the prime-counting error

Define theta(x)=sum_(p<=x) log p and E_1(x)=theta(x)-x. Subtracting the absolutely convergent prime-power series from the usual Stieltjes continuation gives

\[
R-U_{c,N}
=\frac{N^{1-s}}{s-1}-E_1(N)N^{-s}
 +s\int_N^\infty E_1(x)x^{-s-1}dx.
\tag{5}
\]

The finite polynomial on the left now removes only the primes up to N from the prime-only analytic continuation: explicitly it is

    H(s) - sum_(p,k>=2) (log p)p^(-ks) - sum_(p<=N) (log p)p^(-s).

This equals R-U by cancellation of the prime powers up to N. At integer N the theta endpoint includes a prime at N. RH and the elementary prime-power counting bound imply E_1(x)=O(sqrt(x)log^2(2x)), so the integral in (5) is absolutely convergent when Re(s)>1/2. The pole can be removed from the normalized energy as in Round 8.

Thus the non-negligible unknown comparison involves the same genuine-prime error theta(x)-x at the two damping widths. Neither prime powers nor a convention at a prime-power cutoff can supply the missing fixed positive gap above the AH value. A new additive-prime covariance estimate is still required.

## 6. Scope and provenance

The RH inputs are the logarithmic-derivative and prime-counting-error bounds already used and reviewed in Round 8. The prime-power estimates use arithmetic sparsity and elementary series estimates, not a generic point-process positivity assumption. No experimental optimization or new scalar-constant certificate was run for this lemma. An independent ordinary-proof review is required before its status is upgraded.

The resulting error tends to zero and hence leaves the numerical target unchanged. This is a cleanup estimate for the hard arithmetic problem, not progress toward 1/16 by itself and not an assertion of novelty for prime-power removal.


## 7. Uniform corollary for the mesoscopic two-width statistic

Put L=log T. The bound in (2) has an absolute implied constant throughout

\[
1\le c\le L/4.
\]

Indeed delta>=1/L makes delta^(-4)<=L^4 in (1). The RH partial-fraction bound for the logarithmic derivative is O(L²) uniformly at distance at least 1/L to the right of the critical line, throughout 0<=t<=T and 1/2+1/L<=sigma<=3/4. The same elementary bound for the finite polynomial is uniform because its coefficients only decrease as sigma increases. The argument in Section 4 therefore gives a uniform O(a_T) replacement error, where

\[
a_T=N^{-1/6}\log^2(2N)+L^2T^{-1/2}
\ll T^{-1/6}L^3+T^{-1/2}L^2.
\]

Write r_T(b)=||R_(b/2)||²/(TL²), and let r_T^prime(b) be the same normalized energy with U_(b/2,N) subtracted. Define

\[
\mathcal C_T(b)=b^2\left[2\sinh(b)r_T(b)
-2\sinh(2b)r_T(2b)-\frac1{2b}\right],
\]

and define its prime-only version by substituting r_T^prime. For b>=2 and b=o(log L), both c=b/2 and c=b are in the uniform range, and

\[
\boxed{|\mathcal C_T^{\rm prime}(b)-\mathcal C_T(b)|
\ll b^2e^{2b}a_T=o(1).}
\tag{6}
\]

The conclusion is uniform on any range 2<=b<=G(T) with G(T)=o(log L): the exponential factor is only L^(o(1)), whereas a_T has a negative power of T. Thus the mesoscopic arithmetic target can also be stated using the genuine-prime continuation. This corollary removes a nuisance term at the amplified scale; it supplies no lower bound on either statistic.
