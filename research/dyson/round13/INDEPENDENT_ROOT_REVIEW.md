# Round 13 independent integration review

Date: 2026-09-05. Reviewer: root Astra. This review accepts bounded analytic statements, not a new theorem about zeta pair correlation.

## Phase averaging

Reviewed `phase-resonance/AVERAGED_RATIONAL_PHASE_TEST.md`, SHA-256 `7f4285cb02241e22bdb29a1ad4952f7ab8249e3ec3bef984455a57ae05e41ebb`, and its complete exact-check script. The fixed inner prime interval, the mask (m,d)=1, and the primitive Ramanujan principal term are essential and are retained.

At Q=X^.523, M=X^.6, N=X^.4, the phase grid count on a fixed C/N core is O(M/N): the possible O(1) endpoint residues are absorbed because d/N tends to infinity, and repeated residue classes cost M/d because M/d tends to infinity. RH partial summation gives an error O(sqrt(N)log²N) uniformly on that core. The actual numerator weight has total absolute mass O(1) for each d. Hence the sum of errors is O(QM/sqrt(N)log²X)=O(X^.923 log²X). The same argument allows fixed divisor-bounded outer coefficients with the stated X^eta loss. This is a valid extraction of a retained integral main term.

The positive witness uses actual terminal conductors with even prime-factor count, not invented Fourier support. Unit residues s up to d/(32N), repeated m classes, low unit numerators, and the family count give respectively the factors 1/128, 1/32, and 1/2. The centered prime sum paired with S has real part at least (integral V)HN/(16d). Their product is exactly 1/131072. This proves the stated restricted positive block only. Other phases, signs and actual outer coefficients can cancel it.

The enlarged major arcs of width 2R/(qN) correctly handle floor(N/R) in Dirichlet approximation. The complement of fixed C/N cores would not suffice. Ordinary SW yields only a fixed logarithmic error for the other small denominators; ordinary zeta RH has not been mistaken for Dirichlet-L RH. The centered unit variance is exact because each inner prime is a unit and the unit mean is mu(d)P_N(0)/phi(d). Its completion bound gives X^1.323 sqrt(log X), explicitly weaker than the existing estimate for the original prime pairing. No arithmetic improvement is attributed to that factored bound.

## Signed smooth kernel

Reviewed `signed-kernel/SMOOTH_SIGNED_KERNEL_NORM.md`, SHA-256 `1105564835c925b818daf7198186e77c4f0f1ad4ac1001ee1bb50c0f5c7544d9`. Aquinas's separate `INDEPENDENT_AUDIT.md` provides an additional analytic review and byte-identical exact replay.

The CRT main term is X(integral W)(mean²+coefficient squared mass), with the nonzero CRT modes explicitly retained. The cutoff gcd(q1,q2)>=X^.1 makes the least common multiple at most X^.946; smooth Poisson decay is therefore available. For the complementary gcd range, the zero-mode covariance is small because X^.1/H tends to zero. These observations localize the difficulty without estimating away its signed remainder.

The coherent block constant 1/4194304 includes ordered distinct pairs, cell occupancy, coefficient phases and the window phase. Its lower bound is for an explicitly selected subsum of the off-diagonal expression. The report correctly does not infer a lower bound for the full remainder or norm. Its additional observation that even an ideal generic kernel norm does not by itself match the stronger prime-specific small-arc estimate is retained.

## Primary-source audit

Reviewed `minor-arc-source/MINOR_ARC_AND_FIXED_INTERVAL_AUDIT.md`, SHA-256 `bbdb17478b9e885570b7b49c3ff9b94b0ceb98f12a41743edb1ce492cb50edc4`. It checks Montgomery--Vaughan Theorem 17.1, the interval endpoint and genuine-prime changes, the rational-arc domain and Schoenfeld's RH theta estimate. The complete author-hosted/AMS papers and page images remain in the local reference archive; public receipts retain their URLs and hashes. Root's review checks the application and does not claim a second independent reconstruction of those classical source theorems.

## Acceptance and remaining obligation

Accepted as ordinary proofs with their explicit assumptions: the q=1 extraction error, restricted positive resonance block, exact CRT decomposition, coherent subsum and stated upper estimates. Finite tests validate algebra, constants and source identity; they do not numerically prove the asymptotic inequalities.

The strongest bound for the original selected smooth prime discrepancy remains O(X^1.023 log^5 X) under RH. The strict signed covariance estimate required for the actual-zeta Dyson--Montgomery target is unproved. No AH refutation, zeta-gap improvement, GUE theorem, RH proof or prime-gap improvement follows from this round.
