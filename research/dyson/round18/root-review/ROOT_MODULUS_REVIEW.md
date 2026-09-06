# Independent root review of the modulus-level and normalization lemmas

Date: 2026-09-05. Root read the complete final author report, 16,141 bytes, SHA256 `1e06b012dc5c0964293e5cdce06b2f6b52ae6b275b5c4b50402f7f35a560e551`. The final two scope clarifications are explicit: factorization levels satisfy R>=1, and the inherited full aggregate bound assumes RH. This review accepts the stated ordinary support and algebra lemmas. It does not establish a new aggregate estimate or a priority claim.

## Primary theorem hypotheses

I read Maynard arXiv:2006.07088v1 Definition 2 and Theorem 1.1, together with the fixed-residue convention on printed page 6. The definition quantifies over every real allocation R=R1*R2*R3 with Ri>=1, with each factor sequence bounded by one. The source bound is for a fixed residue a; its constants may depend on a. I also read Definition 2.1, Proposition 2.3, equation (2.5) and Corollary 2.19 in the retained 186 paper. Its strong recursive dense-divisibility definition supplies the complementary factor orders used below. Its absolute discrepancy sum already permits bounded complex modulus coefficients for one coherent primitive class. These are distinct source inputs. No new well-factorable decomposition is required for the previously accepted per-shift 186 application.

## Necessary and sufficient support levels

For the necessary level, p=P^-(n), the real allocation R1=R2=s<p forces both corresponding divisors of n to equal one. A nonzero convolution coefficient then requires n<=R/s^2. Letting s increase to p gives R>=np^2. If R<p^2, the preliminary allocation sqrt(R),sqrt(R),1 gives immediate vanishing. The R>=1 domain avoids a vacuous allocation quantifier.

I independently checked the actual terminal family exponents: 2*(9/100)+346*(343/346000)=523/1000; one large plus 173 small primes gives 523/2000; the large-prime root guard exponent is (5/2)*(9/100)=.225<.2505. The small primes lie below Y. Products lie in (Q/2,Q], with positive Mobius sign, and the least prime is greater than lambda*X^kappa. Thus all proposed same-level summands vanish on the actual nonzero terminal coefficient, independently of their number or norm. This establishes a support obstruction, not a universal lower bound on all enlarged-level decomposition norms.

For the completed squared norm lower bound, each terminal coefficient has magnitude 1/q (or log(q)/q). The short reduced-numerator range has order q/H elements, a fixed positive lower bound for the real part of the smooth nonnegative shift sum, and primitive proportion 1-o(1). The union-bound error from the finite 348 prime divisors is negligible because q/H grows by a fixed power while the least prime grows. Summing over the actual prime family gives H/log^348(X), respectively H/log^346(X). This is a coefficient norm statement; it says nothing about the sign of the full pairing with the prime signal.

The sufficient level QY^2 follows from two legal recursive dense-divisor choices. First allocate a divisor at target R1, retaining a complement of order two; then allocate its divisor at target R2. Their two possible factors of Y leave the remaining factor bounded by R3. The cases R1>=q or R2>=the remaining complement use factors equal to one and satisfy every support bound. For squarefree q, gcd(d,qi) transfers this factor allocation to each d|q. No invalid inheritance of the same dense-divisibility parameter by arbitrary divisors is needed. The necessary exponent 45411/86500 and sufficient exponent 21/40 differ by 3/173000; both are below the named Maynard level range.

## Norm and exact inverse

The completed point-mass decomposition really does have total scalar norm at most (log Q)^j*(1+log Q)^2. Expanding the divisor function and bounding by a harmonic square proves this; a large number of conductors is not evidence against the bound. For the original coefficients, the displayed point-mass representation costs at least Q*(log X)^(j-348). That is the cost of that representation alone. The author properly leaves cheaper compressed representations open.

I derived the primitive Ramanujan identity directly at each prime: -1+p*1_(p does not divide h)/(p-1)=-c_p(h)/(p-1). Squarefreeness multiplies the local identities. Since every supported prime is larger than Q, nonprimitive progression classes contribute neither primes nor the correctly masked principal term. The completed prime kernel is consequently the sum over r|d of r*mu(d/r)*Delta_r(h), with no dropped principal contribution.

Substitution of M_d then gives r*sum_(q multiple r) mu(q)*(log q)^j/q * sum_(r|d|q)mu(d/r). The inner sum is zero unless q=r; the surviving coefficient is precisely mu(r)*(log r)^j*1_canonical(r). Thus the inverse restores the original modulus normalization exactly. The terminal absolute conversion sigma_1(d)/d=1+o(1) illustrates the same lost 1/d advantage, without asserting a lower bound on cancellation across conductors.

## Scope and bounded verification

The new support, norm and divisor identities are unconditional statements about the specified finite sequences and sufficiently large real-prime family. The inherited O(X^1.023 log^5 X) aggregate remains conditional on RH. Neither the source fixed-residue theorem nor the completed coefficient norm proves the growing h-packet estimate. The existing prime-power reduction applies on its original H-range only; no extension to the full Bragg-scale shift range is claimed.

I read the entire 5,275-byte exact checker. It uses rational arithmetic and formal log-prime vectors to test coefficient inversions, and keeps the primitive principal subtraction in both Ramanujan and complete kernel checks. These are appropriate algebra tests, not a finite realization of the asymptotic 348-prime family. The separate integration receipt records a fresh execution in a copy, compares every mathematical field, and explains the only metadata difference caused by the documentation-only RH clarification. The historical author stdout remains unchanged.

Accepted result: a nearly matching necessary/sufficient support-level comparison, a constructive polylogarithmic norm for the completed sequence, and an exact explanation of why that norm does not directly bound the original progression functional. The arithmetic cancellation needed for Dyson-Montgomery remains open.
