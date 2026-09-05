# Independent review: exact Vaughan remainder and untwisted coefficient distribution

Reviewer: Aquinas (`yau_flow`), independently of author `residual_gram`. Date: 2026-09-05.

Status: **accepted within the stated scope; final frozen version checked.** The complete mathematical draft and bounded verification script have been reviewed, and the final changes and receipt verified below. No author file is edited by this review.

The accepted output is an exact classical convolution reduction for the actual smooth discrepancy, a uniform Siegel–Walfisz statement for its untwisted second coefficient, and correctly limited source-range bookkeeping. It is not a bound for the full signed bilinear remainder, a phase-twisted coefficient theorem, or a new zeta-correlation result.

## Primary source and dependencies actually checked

I read the primary *Improved short gaps between primes* text at Definitions 2.6–2.9 and Proposition 2.10, printed pages 6–7, and Proposition 2.18 and its surrounding discrepancy conventions, printed pages 10–11. The source URL is [the official PDF](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf).

Local primary PDF SHA-256: `456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930`.

Local extracted-text SHA-256: `ded13a7c74fcfce64e85769e05b5869803dccdf53b88be2c2f3c0b344f95ee84`.

The exact source definition is uniform for **all** progression moduli and auxiliary coprimality moduli. Its divisor exponent must be fixed independently of the requested logarithmic saving. A small-modulus estimate alone would not satisfy this definition.

I also reread the actual kernel, progression Poisson identity, uniform derivative bounds and short-divisor summation in the Round 14 dependency `smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md`, SHA-256 `d6143f19ddf006a1acc833ecd2e5265bffb35817930cfeaa4f4e4b973af7c849`.

## Exact identity and full discrepancy

Equations (7) and (9) have the correct signs. Splitting the Möbius factor in `mu * log`, then using `1 * Lambda = log` and `mu_{>A} * 1 = epsilon - mu_{<=A} * 1`, gives all four terms in (7), including the negative triple convolution. The identity holds for every positive integer and real cutoffs under the stated endpoint conventions; at 1 all terms vanish.

The two meanings of a Lambda cutoff are explicitly distinguished: a value cutoff in the Vaughan identity, and the divisor cutoff `mu_{>U0} * log` inherited from Round 14. Equation (9) correctly relates them, so no earlier remainder is silently replaced.

On the actual support, `n-h > X` and `h > 0`; hence `n > X > B`, and the value-cutoff term vanishes exactly. If a short factor shares a prime with a modulus, both the progression term and its primitive principal term vanish. Otherwise the inverse residue is a unit and the remaining long variable retains its coprimality mask. Expanding the convolution gives exactly (15), with both Möbius signs, the full log-cofactor/sinc weight and the primitive subtraction intact. The auxiliary restriction is not an optional simplification.

## Poisson estimate, logarithms and cutoff budget

In the triple convolution the long factor has coefficient 1. Consequently the smooth profile in (11) correctly contains **no** extra `log s`; the von Mangoldt value is an outer coefficient. The retained log-cofactor factor gives fixed derivative norms of order `log X`. The regular integral form of the sinc argument makes those bounds uniform in the admitted time range and in the held-fixed short factors.

Progression Poisson summation gives (12) with factor `L/q` and the displayed phase sign. The zero frequency cancels against the **same** primitive principal term. The ratio condition `ABQ <= X/2` ensures `L >= 2q` term by term. Summation costs

\[
H X^{1-J}(\log X)
\left(\sum_{a\le A}a^{J-1}\right)
\left(\sum_{d\le B}\Lambda(d)d^{J-1}\right)
\left(\sum_{q\le Q}q^{J-1}\right).
\]

The middle sum is bounded by a constant times `B^J log(2B)`. This proves the stated `log^2 X` error and accounts for every coefficient and multiplicity. The estimate for the first smooth term is dominated because `B >= 1`. Combining it with the separately retained `U0` term proves (5).

The cutoff condition `a+b < 477/1000` is strict. With fixed margin `eta`, the required derivative order satisfies `J eta > 2/7`; constants need not be uniform as the margin tends to zero. The displayed exponents `1711/1750` and `6991/7000` are correct.

There are only a constant number of possible sums of the two dyadic block indices for each product scale, and therefore only `O(log X)` blocks meeting `X < am < 2X`. Thus a **uniform** block bound `o(X)` is sufficient for total `o(X log X)`, exactly as stated; it is not necessary.

## Full Siegel–Walfisz quantifiers for beta_B

Proposition 2 is valid as written. Its source input is the prime-interval property with the auxiliary coprimality condition, not an assertion that an arbitrary convolution inherits it.

For a prime divisor write `m = kp`. Both terms of the discrepancy force `(k,rs)=1`, and the prime residue is `c k^{-1}` modulo `r`. The prime interval is the exact intersection of `p > B` with `kp in I`. Nonempty intervals have prime scale comparable to `M/k`, at least `B/2`; since `B >= X^{b0}`, the source's fixed-power lower-scale hypothesis applies, for example with exponent `b0/2` for sufficiently large X. An endpoint at the cutoff causes no loss of uniformity.

Partial summation for `log p` costs one logarithm; the harmonic cofactor sum costs another. The arbitrary saving in the source absorbs both, while the divisor exponent remains **one**. The upper bound `M <= X^C` keeps these logarithms uniformly comparable to `log X`.

The auxiliary prime exclusions cost at most a constant times `tau(s) M B^{-1} log X`. This is below every required logarithmic error. In particular the proof does not drop the coprimality condition and reconstruct a different principal term.

The prime-power enlargement in (19) is legitimate: discarding the lower prime-power cutoff only increases a positive upper bound. Summing the elementary bound over `k <= 2M/B` yields

\[
\sqrt M\,\log^2X\sum_{k\le 2M/B}k^{-1/2}
\ll M B^{-1/2}\log^2X.
\]

Each of the two discrepancy terms is bounded by that absolute mass; its principal multiplier is at most one. This is negligible for every fixed logarithmic saving. Finally `0 <= beta_B(m) <= log m` supplies the required coefficient bound.

As an additional check on the all-modulus quantifier, large `r` can be handled directly using `beta_B <= log(2M)` and the progression count `O(M/r+1)`, together with `r/phi(r) <= tau(r)`. Choosing the polylogarithmic dividing threshold after the desired saving preserves divisor exponent one. The isolated-point term is harmless because `M >= B/2` is a fixed power of X. This agrees with, rather than weakens, the source property used in the proof.

None of this gives Siegel–Walfisz for `beta_B(m) exp(2 pi i a m/d)` at a large conductor. The author's warning about phase absorption is essential and correct.

## Which source blocks remain uncovered

At the stated source parameters, the three Proposition 2.18 left sides are exactly `0.888`, `0.996`, and `0.990`. With `sigma = 0.101`, the SW-bearing scale must lie in `[X^0.399, X^0.5]`. The limiting edge `0.398` is excluded by the strict inequality `sigma < 0.102`.

The symmetric cutoffs leave both smaller and larger beta-scale blocks outside this direct orientation. The asymmetric cutoffs `a=0.07`, `b=0.4` remove the smaller-beta corner but leave beta scales as large as approximately `X^0.93`. Swapping factors would require an independently justified property for the Möbius interval coefficient, and would still leave the unbalanced corner. The report does not silently assume that swap.

Even a legitimate per-shift source bound retains the factor `H` when summed absolutely over shifts. The report explicitly preserves that loss and the need for a new shift-averaged argument. The exact cutoff budget and coefficient lemma therefore do not establish an improved aggregate bound by themselves.

## Signs and scope

The coefficient beta_B is nonnegative, but the bilinear coefficient and discrepancy need not be. The negative semiprime identity and positive four-prime identity in (21)–(22) follow directly by enumerating divisors. In the positive example only the large prime can contribute to beta_B; the eligible complementary divisor signs sum to `3-1=2`. The sinc/support placement does not determine the sign of the complete progression discrepancy, and the report correctly says so.

No mathematical amendment is required by this independent proof review. Acceptance is limited to the exact reduction, the untwisted coefficient property and the stated range limitations. A stronger estimate for the signed remaining form, the other covariance packets and the eventual zeta target remain unproved.

## Independent finite-check inspection and replay

I read `check_vaughan_remainder.py` before executing it. The arithmetic uses independent formal symbols for each `log p`, with integer coefficients, rather than floating-point logarithms. The grouped coefficient is compared against a separately accumulated ordered `(a,d,s)` sum. The integer and noninteger cutoffs use the same exact strict/non-strict conventions as the theorem. The finite divisor and primality routines and the rational support inequalities were inspected.

The replay tests 1 through 4096 at three cutoff triples, recording 49,152 core formal-log equalities. It also checks the short first-block property of beta_B, both signed support witnesses, the two Poisson exponents and all three source inequalities. The actual integer witnesses are `12001460033 = 100003 * 120011` and `12061713793 = 50021 * 59 * 61 * 67`. Their formal remainder values and support constraints agree with the authored report.

I invoked the unchanged author script with `--output` pointing to `signed-arithmetic-review/independent_replay.json`, leaving the authored result untouched. The replay passed and its JSON is byte-identical to the author's JSON. All six source/dependency hashes embedded in that result match the current files.

- Initially inspected and replayed script SHA-256: `0f27016bb75dbd17037cd5de1b983c1018faf415ee0a4d56226316c177336c1f`.
- Authored and independent replay JSON SHA-256: `294ee54fddb9eea2fc472dd842df6214c5be78146cd61f620ad5a919707bc156`.

These are exact finite identity and parameter checks. They do not establish Siegel–Walfisz by experiment, numerically certify an asymptotic Poisson error, or estimate the signed aggregate. Those mathematical conclusions and limitations were assessed separately in the written proof review above.

## Final frozen receipt and delta check

Accepted final author report, `VAUGHAN_SIGNED_REMAINDER.md`:

`227179985368ea9a8c961b21dee9474d1440c1c5a3b7d04958a1e28b3e11d22a`.

The final additions spell out the two integer factorizations, finite-check counts and reproduction/provenance paths. I read those additions and checked their agreement with the reviewed proof and actual certificate. They do not alter the proof's formulas or extend its accepted scope.

The final script adds an explicit assertion that the remainder vanishes at prime inputs and an optional `--research-base` argument. Both changes were inspected, and this final script was replayed independently with output again confined to this review directory. It passed and produced the same byte-identical JSON hash recorded above.

- Final script SHA-256: `39ed2285c79c6a469f2c664be7222084e500ed2bcb174b1dd6a4baa44a9ee49c`.
- Final author receipt SHA-256: `578a31eacea11138b68ea43302afff54cc0461db58f18fc87afdb62bfdf7c95f`.
- Every author file's byte count and SHA-256 in that receipt was recomputed and matched. All six dependency/source hashes were also independently verified.

The review and its independent replay are now frozen. No additional numerical scan, source edit, model call, PDF generation or repository operation was performed for this review.
