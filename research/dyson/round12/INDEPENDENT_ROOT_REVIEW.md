# Independent review of the three bounded Round 12 attempts

Date: 2026-09-05. Reviewer: root Astra, independently of all three authoring lanes. I read all three complete reports, checked the inherited Round 11 construction, inspected the relevant primary source statements, and checked the new elementary arguments below. Accepted scope: ordinary proofs of specific failed shortcuts and an insufficient actual-prime estimate. No stronger bound for the actual signed prime pairing is proved.

Pinned author reports:

| Report | SHA256 |
|---|---|
| sampling-geometry/ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md | cb52d72f6068c3030968209d8aa028439ea4dc309aa5584d216a1d7d30a1a59d |
| dispersion-transfer/DISPERSION_HYPOTHESIS_OBSTRUCTION.md | 26536af7b5e6ebfb8fb4f7c7be993543c57152e29c6fd2b039c5eb147ccefd95 |
| mixed-arithmetic/SELBERG_MIXED_REMAINDER_AUDIT.md | 6223e9a54c44c31d344c2f932fe81ca6ad4672e5f6ef625adfeae07b4ed5a308 |

## 1. Positive sampling on the actual modulus support

The inherited count supplies at least c0 Q/(2 log^348 X) actual terminal conductors. Each has at least d/(32H) primitive low numerators and d>Q/2, giving the stated c0 Q^2/(128 H log^348 X) distinct frequencies. The number of cells of length at most 1/(100X) in the small arc is at most 8X/H eventually. Pigeonhole therefore supplies the claimed occupation without a local distribution theorem.

For N=ceil X, M=floor(X/10), the integer frequencies N,...,N+M-1 lie in [X,1.1X]. Within the chosen cell, factoring out the carrier leaves phases at most pi/1000. The lower bound M/(2 sqrt H) and Parseval norm M/H give the sampling constant c0 Q^2/(81920 log^348 X). Squaring the actual coefficient lower bound m_v H/(2 sqrt(2)Q) gives the second constant 1/655360. The global Parseval norms also imply both local small-arc envelopes for rho>=1/H, including the derivative bound.

The constructed polynomial is artificial and phase-tuned. It is not the actual prime polynomial, nor a fixed smooth multiplier of its coefficients. The proof correctly limits its conclusion to positive sampling and the specified absolute-weight operator. It does not prove sharpness for all rearrangements of Cauchy--Schwarz or all signed weightings.

I checked the signed Gram identity directly by expanding the functional coefficient by coefficient. Completing each parent modulus and retaining its Ramanujan principal term gives exactly the residue kernel in equation (16); the zero Fourier term cancels. This equality holds for the Fourier-defined kernel at arbitrary integer n, while its identification with the original unit-restricted progression expression is made only for primes near X. The report states that distinction. Negative or complex cross terms in the signed Gram are not controlled from the positive sampling lower bound.

## 2. The proposed direct dispersion transfers violate actual source hypotheses

I checked the 186 source's Siegel--Walfisz definition, prime-interval example, product-local residue lift, and Proposition 2.18 scale/parameter conditions. At omega=.012, delta=.001, sigma=.101 the three left sides are .888, .996 and .990. N=X^.4, M=X^.6 are legal, and the allowed modulus cap is exactly X^.523. No out-of-range parameter creates the counterexample.

For each canonical d>Q/2 coprime to 3, k=(d-1)/3 or (d+1)/3 is a unit and k/d tends to 1/3. An m in [M,2M] in that residue class exists because M/d tends to infinity. For primes n in [N,2N), replacing e(mn/d) by e(n/3) costs O(N/d) per term. PNT in the two fixed reduced classes mod 3 then gives the discrepancy i sqrt(3) N/(4 log N), with uniform lower-order error O(N^2/(d log N)). Both branches have the same limiting cubic phase and leading sign. This violates the source's SW condition for L=2. The original prime coefficient has SW; the phase-twisted family does not inherit it. A bad slice is not a proof that no averaged dispersion treatment is possible.

For the CRT claim, every prime factor of the constructed conductor is at most X^.09 and at least lambda X^kappa. Counting a chosen local unit class and subtracting divisibility by each other prime leaves at least (ell H/p)(1-347/(lambda X^kappa))-348 positive candidates eventually, uniformly. Thus imposing the global gcd restriction does not reduce any local image. The smallest product hull has phi(d) classes, asymptotic to d, whereas tau(d)=2^348 stays fixed. The bounded-local-class consequence of the source lemma is unavailable. This is a failure of the product-hull reduction; the original coherent interval has many fewer global classes and could be treated differently.

Finally the source constraint forces sigma<.102, hence the short convolution factor exceeds X^.398. H<=X^(2/7) cannot be substituted for that factor at the same total scale. All three conclusions are source-application obstructions, not counterexamples to the source theorem or to the target covariance.

## 3. The direct Selberg mixed estimate is deliberately insufficient

I inspected the primary Saffari--Vaughan text and the rendered printed page 20. Equation (6.4) is indeed a uniform RH estimate for genuine theta and all 0<eta<=1. Equation (6.5) gives the stronger global weighted comparison quoted in the report; its exponent parameter must remain fixed. The report prominently states that its local calculation is weaker than previously established RH norm control and does not claim to exhaust the source's consequences.

The Mellin Gallagher inequality follows from interval convolution and Plancherel with the stated Fourier convention. Its direction and factor 2pi T^2/c0^2 are correct. Short-interval integration by parts retains the centered increment F(x(1+eta))-F(x); the derivative of the log weight is included. Applying Minkowski to the source bound gives equation (6), including the dyadic variation cost 1/log T.

The upper-cutoff crossing term tends to zero at fixed T,s as Y tends to infinity. At the strict integer lower cutoff, N exp(1/T)<N+1 ensures that the crossing interval has no retained prime atom; its continuous contribution is negligible. Dyadic subdivision partitions the integration variable rather than splitting the prime measure, so it introduces no uncounted prime endpoints. Geometric sums in 1,j,j^2 give the norms L/s and L/s^3, with s(1-log N/L)=o(1). Cauchy--Schwarz supplies only the insufficient absolute mixed bound L/s^2 and the integrated lower estimate as stated.

For the separately filtered active shell, the stronger fixed-exponent global estimate gives O(1) and O(s^-2) normalized energies. The shell lies inside its fixed range once s is sufficiently large, the Mellin damping is O(exp(-s)), and the smooth-filter derivative cost s/L is bounded. These estimates are for a component, not a decomposition asserted for the full mixed moment. They give no positive shell increment or required signed coefficient.

The integrated sinc kernel is correctly obtained from the symmetric excess factor v exp(-s v). Its negative pointwise lobe defeats a term-by-term positivity claim, but a negative kernel value is not by itself a negative quadratic-form witness. The report explicitly avoids that stronger false inference. All continuous and prime pieces remain jointly centered.

## Decision

The next substantive improvement requires actual joint arithmetic: a prime-specific concentration estimate, a signed Gram/dispersion argument retaining the coherent shift and its phase, or a one-sided centered fluctuation estimate with the necessary shrinking-shell precision. These reports justify not repeating the three failed shortcuts. They do not prove that the remaining X^.023 factor or the famous conjecture is inaccessible.
