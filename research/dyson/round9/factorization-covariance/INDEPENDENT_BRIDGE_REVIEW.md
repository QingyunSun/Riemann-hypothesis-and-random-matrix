# Independent review of the complementary-modulus covariance component

Date: 2026-09-05. Reviewer: the independent residual/arithmetic agent. Reviewed final report: [COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md](COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md), SHA256 `982039f0e163b84c1c5b8f2b52f215eb40e7b89863085f2840c039853606f39a`.

**Verdict: accepted as an ordinary application of the stated primary distribution theorem, with the scope of equations (13), (19), and (22) exactly as written.** I found no missing modulus hypothesis, incorrect residue maximum, lost logarithmic weight, or error in the RH aggregate remainder. The comparison to the Round 7 sinc kernel has the correct normalization. This review does not prove or independently reprove the source distribution theorem, certify its formalization, evaluate the remaining shifted discrepancy, or establish a new zeta bound.

The useful output is a selected divisor component with a uniform per-shift estimate, and a separate exact aggregate reduction under RH. The full natural shift packet still requires a new bound. The report correctly keeps that obstruction visible.

## 1. Primary hypotheses and modulus family

I checked the local primary PDF/text pair against the supplied hashes and read the precise source statements: Definition 2.1 and Proposition 2.3 on printed pages 4–5; the discrepancy definition (2.3) on page 6; the coherent-class convention (2.5) on page 7; Proposition 2.18 and Corollary 2.19 on pages 10–11. The primary reference is [Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf).

The parameter choice omega=3/250, delta=1/1000 and epsilon=1/1000 gives 240omega+80delta=74/25<3 and modulus exponent 1/2+2omega-epsilon=523/1000. The source explicitly grants the r=3 estimate for Lambda and uniformly on subintervals, so neither the prime-indicator conversion nor endpoint uniformity is being invented in this application.

The complementary construction uses the actual least common multiple q=[D,E]. Its root budgets satisfy A0 B0=Z Y, and f(p)=g(p)=p^(3/2) are nondecreasing with product p^3. Since the two budgets are equal, each owner inequality also gives the opposite-root guard by dropping the tail factor, which is at least one. Squarefreeness and the strict q>Z assumption are present. Consequently the specified q belong to the source's triply densely divisible class even if D and E share primes. Using DE>Z in place of [D,E]>Z would not have sufficed, but the report does not make that substitution.

Every modulus is counted once. This is essential: no uncontrolled count of its root representations appears in the coefficient. The nonsmooth example is legitimate for sufficiently large X: the needed two large primes exist by the prime number theorem, while the product of unused primes at most X^.001 eventually exceeds any fixed power of X. Greedy disjoint smooth products have the claimed at-most-X^.001 overshoot. The listed exponent inequalities then place the example between X^.518 and X^.522 and satisfy the owner predicates. This proves existence, not density or quantitative usefulness of the selected family.

## 2. Coherent residues and q-dependent weights

Fix h and remove from the prime set every prime dividing h. Each retained q with (q,h)=1 is still a divisor of the new prime product, and h is one primitive residue class modulo that product. Its restrictions are exactly the required classes h mod q. The source's uniformity permits this prime set and coherent class to depend on X and h. The application never uses a maximum over separately chosen classes inside the modulus sum.

The progression reindexing m=n+h is exact. For the weight depending on q, use

    w_h(m-h) log((m-h)/q)
      = F_h(m) - (log q) G_h(m),
    F_h(m)=w_h(m-h)log(m-h),  G_h(m)=w_h(m-h).

These are two common functions of the endpoint, not one unrelated function per modulus. Their sup-plus-variation bounds are O(log X) and O(1), respectively, uniformly in h. The log q coefficient is bounded by .523 log X. Partial summation therefore bounds the discrepancy sum by integrals of the source's sum at a common endpoint. It does not replace a bound on sup_t sum_q |Delta_q(t)| by the stronger and unavailable sum_q sup_t |Delta_q(t)|.

All extra losses here are fixed logarithmic powers and are absorbed by choosing the arbitrary source saving sufficiently large. This proves the weighted coprime progression reduction uniformly for the stated C1 weights, including complex weights by absolute values or separate real and imaginary parts.

## 3. Principal terms and both kinds of prime-power exception

After the distribution step, the principal term carries 1/phi(q). The sum of these factors is O(log X), even for the full available modulus range. One elementary verification is

    sum_(n<=Q) 1/phi(n)
      = sum_(d<=Q) mu(d)^2/[d phi(d)] H_floor(Q/d)
      <= (1+log Q) product_p [1+1/(p(p-1))].

The product converges. Thus one does not pay the number of moduli when replacing the coprime prime sum by its integral.

The unconditional prime number theorem, with a saving stronger than every fixed negative power of log X, suffices for the per-shift result. Multiplying its uniform dyadic error by the O(log X) variation of the weight and the O(log X) inverse-totient sum still yields O_A(X log^(-A) X) after adjusting the initial exponent. This gives precisely the displayed main term, including both support sums with mu(q)/phi(q) and mu(q)log(q)/phi(q). Neither sum is evaluated as a universal singular-series constant.

There are two different exceptional sets, correctly separated in the report:

- Removing (m,q)=1 from the principal sum adds m=p^j around X with p dividing q. Since p<=q<=X^.523<X, these have j>=2. This includes all p dividing q, whether or not p divides h. Bounding by all prime powers gives von Mangoldt mass O(sqrt(X) log^2 X). The additional weight and inverse-totient sum cost at most two logarithms.
- In the original nonprimitive progression terms, a prime p dividing both q and h also divides n+h. If Lambda(n+h) is nonzero, then n+h=p^j with p dividing h. Uniformly for h<=C H there are O(log^2 X) such prime-power possibilities. For each resulting n, the number of allowed divisor moduli is at most tau(n), bounded by O_eta(X^eta). The resulting error is O_eta(X^eta log^O(1) X), for any fixed eta>0.

No nonprimitive main term was silently discarded. Both errors fit the per-shift bound, proving equation (13) given the stated source theorem.

## 4. RH aggregate identity: the square-root error is sufficient

For equation (22), the report appropriately changes its error input. Under RH, psi(y)-y=O(sqrt(y)log^2 y) uniformly on the relevant dyadic interval. Partial summation costs one logarithm and the q principal-term sum costs one more, giving

    O(sqrt(X) log^4 X)

per shift. The principal prime-power deletion obeys this same upper bound. The nonprimitive error can be absorbed by first fixing eta=1/4; any remaining fixed logarithmic power is eventually smaller than the available X^(1/4) margin.

Summing these nuisance errors over h<=C H therefore gives O(H sqrt(X)log^4 X). Since alpha lies in [6/5,7/5], H=X/T<=X^(2/7), so the total is at most O(X^(11/14)log^4 X)=o(X log X), uniformly in alpha. Constants may depend on the fixed compact weight support and C, which the report allows.

This verifies equation (22): the remaining quantity is exactly the sum of the weighted coherent progression discrepancies, not an untracked PNT error. The RH power saving is used only for this principal-term and exception replacement. It does not give a power saving for the progression-discrepancy sum itself. The report correctly warns that multiplying only an unconditional logarithmic per-shift PNT error by H would not justify the same aggregate precision.

## 5. Actual kernel and accumulation at the covariance scale

For fixed alpha and X=T^alpha, the real symmetric Round 7 kernel is

    1/(X T log T) a_u(X)a_v(X) sin(T log(u/v))/log(u/v)
      = 1/(X log T) a_u(X)a_v(X) sinc_0(T log(u/v)).

At v=u+h, sinc_0 is even, so the sign of log(u/v) does not alter the expression. Summing the two orders of an off-diagonal pair yields the stated factor 2. Multiplying by chi(u/X) selects the declared localized component, and subsequent fixed-bump integration in alpha preserves these identities. It does not remove the other components.

On the compact support inside (X,3X/2), both a_u(X) and a_(u+h)(X) lie on their smooth upper branches for large X. Their derivatives are O(1/X). For z=T log(1+h/u), h<=C X/T gives z=O_C(1) and

    z'=-T h/[u(u+h)]=O_C(1/X).

The sinc and its derivative are bounded on that fixed argument range. Hence the weight in (17) has uniformly bounded sup norm and total variation as required; the absolute-value bound does not require it to be positive.

The natural normalized covariance scale is X log T, uniformly comparable to X log X in the stated alpha interval. Equation (19) is the honest consequence of the per-shift estimate: it pays sum_h |b_h|. Logarithmically bounded packets therefore have negligible error at this scale. For the full packet b_h=1, the only available source bound is O_A(H X log^(-A) X), or O_A(H log^(-A-1) X) after covariance normalization. Since H is a fixed positive power of X, no fixed logarithmic saving makes that upper bound tend to zero. This proves insufficiency of that bound, not a lower bound on the actual error.

Thus the proposed new estimate for the aggregate shifted discrepancy, equation (23), remains unproved. Even proving it would only evaluate the selected divisor piece. The unselected divisor sum (24), its main support sums, the omitted n and h ranges, and the continuous centering of the covariance remain genuine obligations. Proposition 2.18 concerns a multiplicative convolution with independent coefficient sequences; it does not directly estimate Lambda(qm+h) as an independent sequence in one variable. The report preserves this distinction.

## 6. Reproduction and claim boundary

I reran the exact script in a temporary directory, with read-only links to the two primary files, leaving the original scripts and outputs unchanged. The 300 formal Mobius-log identities, five progression/discrepancy decompositions and parameter checks passed. At least one example has a nonzero nonprimitive prime-power contribution, so that branch is exercised. Replayed JSON matches the author's JSON exactly after removing only the temporary local source-path strings; no arithmetic field is omitted from the comparison.

The [independent receipt](independent_bridge_review_receipt.json) pins the final report, script, author JSON and source hashes. The script uses formal prime-log vectors and exact fractions, not floating agreement. These small checks validate identities and conventions; they do not prove any asymptotic distribution estimate or test the large-X support conditions numerically.

The accepted mathematical content is therefore the precise partial-component estimate (13), its weighted packet consequence (19), and the RH aggregate decomposition (22). This is a valid application of the chosen published input beyond a square-root divisor cutoff. It is not a full divisor decomposition estimate, a new Montgomery/Dyson theorem, a new prime-gap bound, or a solution of the two-scale zeta target.
