# Independent review of the fixed symmetric-prime arithmetic transfer

Review date: 5 September 2026. Reviewer: independently assigned residual-Gram research agent.

Reviewed source, without editing it:

`/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research/research/reports/symmetric_prime_arithmetic_transfer.md`

Reviewed source SHA-256: `bf2ca70e61da1f97b4c214304180f0f45d3c26a050104bf30e6d70e46660d07f`.

## Decision

**Accept the fixed-family arithmetic-transfer argument as mathematically complete at the level of an ordinary written proof.** I found no fatal gap after checking the positive-measure limit, marked-prime coincidences, arbitrary-vector Schur estimates, same-prime terms, and the normalization of the interface with Inoue's theorem.

This decision has a precise scope. It covers fixed `ell>=1` and fixed

\[
H(v,S)=f(v)+g(v)S,
\qquad S=\sum_{p\mid n}(\log p/\log L)^2,
\]

with the polynomials stated in the draft and positive limiting norm `I`. It therefore covers the particular rational trial `ell=16/15` certified in round one. Its operator asymptotic is unconditional; RH enters only when the result is inserted into the cited zeta theorem.

It does not certify the full arithmetic-operator/Fock limit, an arbitrary infinite feature family, uniformity when the polynomial degree or coefficients grow with L, or a positive half-gap margin. The fixed certified margin remains approximately `-0.014662375473369`, and thus gives no new small-gap theorem. This is an independent mathematical review, not Lean verification or external peer review.

## 1. Positive-measure limit: valid, including the short background range

The Euler factors satisfy

\[
(1-p^{-s})^a\sum_{e\ge0}d_\ell(p^e)^2p^{-es}
=1+O_\ell(p^{-2s})
\]

uniformly as real `s` decreases to 1. Thus the real Euler product tends to the claimed positive constant. A complex analytic branch of `zeta(s)^a` is not needed for the Laplace argument.

The scaled Laplace transform tends to `C_ell t^{-a}` for every positive t. Tilting by `e^{-v}` gives finite measures with convergent total masses. The stated exponential tail inequality is enough for tightness, because the Laplace transform at `t=1/2` is uniformly bounded for sufficiently large L. Uniqueness of Laplace transforms identifies every subsequential limit. Undoing the tilt on compact intervals gives local weak convergence.

The limiting density `C_ell v^{a-1}/Gamma(a)` has no atom at zero or at the cutoff. Therefore restriction to `[0,1]` and to the simplex cutoffs is legitimate. This avoids the commonly invalid step of requiring a pointwise Selberg–Delange estimate uniformly for every short background length `L/(pq)`.

One explicit mass bound, useful to make the proof fully transparent, is

\[
\frac1{(\log L)^a}\sum_{n\le L}\frac{d_\ell(n)^2}{n}
\le e\frac{D(1+1/\log L)}{(\log L)^a}=O_\ell(1).
\]

It holds because `e^{-log n/log L}>=e^{-1}` on the cutoff. This supplies every crude background-mass estimate needed later.

## 2. Marked-prime moments: constants and coincidence removal are correct

For fixed epsilon, the marked primes lie in a compact logarithmic range bounded away from zero. The prime-number theorem gives weak convergence of the reciprocal-prime measures there. Products with the unmarked positive measure converge on compact sets. The boundary hyperplanes of the product cutoffs have zero limiting measure.

The arithmetic identity behind the first mark is exact away from the excluded coincidences: inserting a new prime into `d_ell(n)^2` multiplies the background coefficient by `ell^2=a`.

I independently recomputed the three beta integrals. Dividing the marked density by the unmarked density gives

\[
\mathbb E_v S=\frac{v^2}{a+1},
\]

\[
\mathbb E_v S^2
=\frac{6v^4}{(a+1)(a+2)(a+3)}
+\frac{av^4}{(a+1)(a+2)(a+3)}.
\]

The first summand is the same-prime fourth-power contribution. The second comes from **ordered distinct primes**. Their sum is the `(a+6)` expression in the draft. There is no missing factor of two.

The submultiplicativity condition is also correct. For `ell>=1`,

\[
\frac{d_\ell(p^{e+1})}{d_\ell(p^e)}=\frac{\ell+e}{e+1}
\]

is nonincreasing in e, hence `d_ell(p^{b+c})<=d_ell(p^b)d_ell(p^c)`. The restriction on ell is genuinely used here.

For example, the background coincidence can be bounded explicitly by

\[
\sum_{m\le L:\,p\mid m}\frac{d_\ell(m)^2}{m}
\le\frac{\ell^2}{p}\sum_{k\le L}\frac{d_\ell(k)^2}{k}.
\]

After the outside mark's reciprocal-prime factor, this is a `p^{-2}` contribution. For `p>=L^epsilon`, summing it gives at most a constant times `L^{-epsilon}` times the total background mass. Higher exponents are handled by factoring off `p^2` and using the same submultiplicativity bound. Finitely many other marked primes contribute bounded factors for fixed epsilon, or at worst harmless powers of `log log L` under the draft's coarser estimate.

The deterministic small-mark bound is particularly effective:

\[
\sum_{p\mid n,\ p<L^\epsilon}(\log p/\log L)^2\le\epsilon.
\]

Because H is fixed and linear in S, its products change uniformly by `O_H(epsilon)` on the cutoff. One therefore takes `L→infinity` first and `epsilon→0` afterward. No exchange of limits or assumption of uniformity in shrinking epsilon is needed.

The same reasoning applies when the background moments are evaluated inside the two outer prime insertions. Expanding `H_0H_{uw}` or `H_uH_w` adds only finitely many marks. Collisions between an outer inserted prime and a background mark have the same additional reciprocal-prime cost. This is worth stating explicitly in the final prose, but it does not require a new estimate.

## 3. The weighted Schur estimate is correctly oriented and works for signed vectors

Take `w_n=d_ell(n)/sqrt(n)`. The draft's weighted row bound uses

\[
\sum_{p^e\mid n}(\log p)d_\ell(n/p^e)
=\frac{\log n}{\ell}d_\ell(n).
\]

This is the coefficient identity obtained by differentiating the Dirichlet series for `zeta(s)^ell`. The sine bound cancels the exponent e exactly, leaving the displayed logarithmic derivative. Hence the weighted row sum is at most `pi/ell`.

The column calculation contains a second factor `1/sqrt(p^e)` from the weight ratio, so its denominator is `e p^e`, not `e sqrt(p^e)`. The draft uses the correct denominator. Submultiplicativity gives the stated upper bound in terms of `d_ell(p^e)`.

For the prime-only small part, the column bound is `O_ell(epsilon+1/log L)`. For all higher prime powers it is `O_ell(1/log L)`, because

\[
\sum_p\sum_{e\ge2}\frac{d_\ell(p^e)\log p}{p^e}<\infty.
\]

The fixed-ell polynomial growth in e is enough for this convergence. Combining these column bounds with the full row bound by the weighted Schur test yields exactly the square-root orders in the draft.

These are operator-norm bounds. No positivity of `x_n`, `H`, or the polynomial coefficients is needed. To make the quadratic-form passage explicit, if `A=A_0+E`, then

\[
\|A^*A-A_0^*A_0\|
\le(\|A\|+\|A_0\|)\|E\|,
\]

and

\[
\|A^2-A_0^2\|
\le(\|A\|+\|A_0\|)\|E\|.
\]

After division by `||x||^2`, the error is independent of the direction of x. This closes the small-prime and prime-power issue for the signed rational trial.

## 4. Same-prime terms and normalization of the limiting quadratic forms

The two quadratic forms treat repeated primes differently, and the draft handles the distinction correctly.

For `A^*A`, the same-prime term has `n=mp` and weight

\[
\frac{4\sin^2(\pi u/2)}{mp}d_\ell(m)^2H(v,S_L(m))^2.
\]

It is of main-term size and produces the entire M3 contribution. It must not be removed as a coincidence error. The draft retains it.

For `A^2`, applying the same prime twice instead has the reciprocal weight `p^{-2}`. At fixed epsilon it is negligible by the coincidence estimate. Distinct primes multiply the background coefficient by `ell^2`, producing `H_0H_{uw}`. The off-diagonal part of `A^*A` likewise produces `ell^2 H_uH_w`.

Both integer sums order the pair of inserted primes. The continuum double integrals use the same ordering. Multiplication by `alpha_p alpha_q` gives the coefficient `4 ell^2`, which equals the coefficient of `2 pi^2 M2`. The same-prime coefficient `4` equals that of `2 pi^2 M3`.

The norm satisfies

\[
\|x\|^2\sim\frac{C_\ell}{\Gamma(a)}(\log L)^a I.
\]

The common scalar cancels. Since I is assumed positive, division by the norm is legitimate. This reproduces the precise normalization of the rational continuum certificate.

## 5. Interface with Inoue: RH and the cutoff error are accounted for

The cited [Inoue paper](https://arxiv.org/html/2604.05733v1) supplies the zeta inequality under RH for arbitrary arithmetic resonator coefficients. This review treats that externally stated theorem as an input; it is not an independent reproof of the entire paper.

Set `L=floor(T/(log T)^2)` and `h=pi/log T`. The approximator coefficients have bounded weighted square sum. One direct check is to use the small-argument sine bound on primes and partial summation; prime powers contribute a convergent sum. Consequently the displayed normalized error tends to zero. If using Theorem 4 directly, its `O(h) M1` term is harmless because the preceding Schur bounds and Theorem 3 bound the normalized first moment. Alternatively the source's combined Proposition 3 already packages the needed coefficient-independent normalized error.

The operator in the zeta expression has `theta=log L/log T`, not exactly 1. Applying the mean-value inequality to sine gives an entrywise majorant proportional to

\[
|1-\theta|\frac{\log p}{\sqrt{p^e}\log L}.
\]

Its weighted row and column bounds are each `O_ell(|1-theta|)`, so the Schur norm is `O_ell(|1-theta|)`, as stated. The cutoff discrepancy therefore vanishes. At the half-gap boundary the leading linear coefficient cancels, leaving the two quadratic forms already analyzed.

## 6. Suggested presentation changes, none of which is a fatal repair

For publication or formalization, I recommend adding the explicit background-mass inequality in §1 of this review, the displayed bound for a background divisible by a marked prime in §2, and the quadratic-form perturbation inequalities in §3. These turn the most compressed prose estimates into short checkable lemmas.

I also recommend stating the scope in the theorem title: **fixed H linear in S2**. The higher-degree symmetric-feature experiments in the earlier numerical reports are not automatically covered merely because their formulas are similar. The same strategy likely extends to them, but that extension should receive its own finite-mark statement and proof.

The review upgrades the earlier “pending arithmetic transfer” label only for the fixed family actually proved here, including the rational ten-coefficient trial. Historical reports should retain their original status and link to this review as the later resolution. No numerical global optimum, no general operator no-go, and no new zero-gap record is established by this upgrade.
