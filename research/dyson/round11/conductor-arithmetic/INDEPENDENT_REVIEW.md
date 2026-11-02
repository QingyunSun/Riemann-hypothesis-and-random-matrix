# Independent review of the canonical conductor-mass construction

Date: 2026-09-05. Reviewer: root Astra, independently of the authoring lane. Accepted as an ordinary asymptotic arithmetic proof for the explicitly defined full family. This is not a lower bound for the prime pairing, and not a formal proof-assistant certificate.

Reviewed author SHA256: `46347799005bb0f53af25c2a7e8ffb2b2217d92688c7651327dde3562f114b92`.

## Membership and counting

The exact exponents are consistent: two primes of exponent 9/100 and 346 of exponent 343/346000 give total 523/1000; each root has one large prime and 173 small primes, giving 523/2000. The lower interval multiplier raised to 348 is exactly 1/2. Thus every constructed product lies strictly above Q/2 and at most Q, for every sufficiently large real X.

The small-prime exponent is strictly below 1/1000, so those factors do not trigger the complementary predicate. Each root has only one factor above that threshold; its owner tail is the factor itself. The active condition is therefore p^(5/2)<=X^(9/40), strictly inside X^(501/2000). The opposite guard is weaker. Both roots are squarefree and disjoint; their least common multiple is their product. This checks the actual Round 9 support, rather than merely assuming that dense divisibility implies membership in it.

Unique factorization and disjoint intervals give exactly binomial(L_X,2) binomial(S_X,346) different moduli. PNT in fixed-ratio intervals gives the stated constant and log exponent. Counting root partitions as different moduli would be wrong; the author does not do that. No effective or practical threshold is claimed, and the very small fixed counting constant does not affect the power comparison.

## Signed coefficients and primitive fractions

At a constructed d>Q/2 no other positive multiple d k can be at most Q. Thus the full signed regrouped coefficient is exactly mu(d)/d=1/d; negative contributions from other parent moduli cannot cancel it. Each reduced fraction is counted once. This is a conductor-isolation fact, not a claim that all moduli have positive coefficient.

For 1<=a<=d/(16H), every active h is between H and 2H, so the phase has absolute value at most pi/4. Fixed nonnegative V gives the lower real part claimed. The union bound over 348 prime divisors removes at most A*348/(lambda X^kappa) candidate numerators, while the floor costs at most one. Since A>=X^(523/1000-2/7)/32 grows uniformly, at least A/2 primitive numerators remain eventually. This proves the individual constant m_V^2 H/(256 d), then c0 m_V^2 H/(512 log^348 X). The extra log d gives at least (log X)^2/4 after squaring, yielding the second constant 1/2048.

## Scope and relation to the new RH estimate

For fixed eta>0, X^eta/log^348 X diverges. The norm lower bound therefore rules out O(H X^(-eta)) for these exact coefficients on this full family. It also refutes such an assertion made uniformly over all allowed subfamilies, since this one qualifies. It says nothing about every deliberately pruned family or altered sieve weight.

In particular it does not obstruct the separate Round 11 RH small-arc improvement, which changes the prime-frequency estimate and its localization. Nor does it give a lower bound for the signed pairing of these coefficients with actual centered prime exponential sums. A claim that the remaining X^.023 loss is unavoidable for primes would exceed the proof.

The inherited dense-divisibility parameter for a general divisor is Yq/d, not always Y. For the conductors used here d=q, so no loss of parameter occurs. The author records this distinction explicitly.

The exact-arithmetic companion verifies rational exponents and constants only. PNT, the fixed smooth Riemann sum, and the written counting argument supply the asymptotic assertions. No prime search or numerical realization was needed.
