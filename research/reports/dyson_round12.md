# Round 12: three exact tests of the remaining arithmetic gap

Date: 2026-09-05. **No stronger actual-prime estimate was obtained in this round.** The current bound remains the RH component estimate X^1.023 log^5 X from Round 11. Three bounded attempts now explain precisely why improving positive sampling, importing the 186 dispersion theorem by phase absorption, or applying known prime-interval upper norms does not yet close its gap. Each conclusion is narrower than an impossibility theorem for the actual signed prime pairing.

## Positive sampling really is crowded on the permitted support

The [sampling proof](../dyson/round12/sampling-geometry/ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md) uses the actual canonical complementary-modulus family, not the full Farey set as a substitute. Round 11 constructed at least c Q/log^348 X terminal conductors in (Q/2,Q], each with merged coefficient 1/d. They supply at least c Q^2/(H log^348 X) distinct reduced frequencies in [0,1/(16H)], with coefficient magnitude at least c_V H/Q.

Partition this arc into O(X/H) cells of length 1/(100X). One cell must contain at least c Q^2/(X log^348 X) actual frequencies. A phase-tuned Dirichlet packet with integer frequencies in [X,1.1X] concentrates there. Parseval and its value on that cell prove that the positive local sampling constant is at least

\[
c\,Q^2/(\log X)^{348}.
\]

The packet also satisfies the same known small-arc energy and derivative envelopes, even without their logarithmic factors. Including the actual squared coefficient weights gives the corresponding lower bound c_V H^2/log^348 X. Thus these hypotheses cannot justify a fixed-power improvement of that positive sampling step.

The packet is an artificial integer polynomial, not the centered genuine-prime polynomial for fixed smooth f. It is not asserted to align with the full complex coefficient vector. The actual signed functional has the exact dual kernel

\[
K(n)=\sum_{q\in\mathcal Q}\mu(q)
\left[\sum_{h\equiv n\ (q)}v(h/H)
-\frac1{\varphi(q)}\sum_{(h,q)=1}v(h/H)\right].
\]

Its Gram matrix contains signed off-diagonal contributions. A smaller norm for that functional, or cancellation with actual prime coefficients, is not ruled out by the positive sampling result. The proof specifically does not claim that X^.023 is unavoidable for primes. The inherited counting and packet constants have a [separate narrow review](../dyson/round12/sampling-geometry/COUNTING_REVIEW.md); root checked the complete argument and exact signed identity.

## Direct phase absorption violates the dispersion coefficient hypothesis

The [dispersion audit](../dyson/round12/dispersion-transfer/DISPERSION_HYPOTHESIS_OBSTRUCTION.md) checks the 186 paper's actual hypotheses at legal parameters. With omega=.012, delta=.001 and sigma=.101, the three bilinear inequalities have left sides .888, .996 and .990. The scales N=X^.4 and M=X^.6 are permitted, as are the canonical terminal conductors d near Q=X^.523.

The prime-interval sequence beta(n)=1_(n prime, N<=n<2N) has the source's Siegel--Walfisz property. But its additive twist need not. For d coprime to 3, take k=(d-1)/3 or (d+1)/3 according to d mod 3, and choose a unit m in [M,2M] with m=k mod d. This is possible since M/d tends to infinity. The actual completed numerator a=1 has nonzero shift weight. On the prime interval,

\[
e(mn/d)=e(n/3)(1+O(N/d)).
\]

PNT in the two fixed reduced classes modulo 3 therefore gives

\[
\Delta(\beta(n)e(mn/d);1\bmod3)
=\left(\frac{i\sqrt3}{4}+o(1)\right)\frac N{\log N}.
\]

The source SW requirement with logarithmic exponent two cannot accommodate this discrepancy. Both branches for k give the same leading sign. The error O(N^2/(d log N)) is uniformly lower order. Hence one cannot absorb the completed phase into the short coefficient and inherit its original SW property, even with a permitted conductor, scale and primitive numerator. The source theorem remains valid; the proposed transformed coefficient fails its premise.

This does not say that every slice or every factor in a prime identity fails, or that bad slices cannot be handled after averaging. An averaged argument keeping m, a, d and h may still succeed. The modulus-dependent coefficient also cannot be silently substituted for a fixed family before the source's modulus sum.

Two further checks close related direct substitutions. First, even after gcd(h,d)=1 is imposed, a positive subinterval of the shifts maps onto every unit class modulo every prime factor of the constructed d. Its product of local images has phi(d) classes, asymptotic to d, while tau(d)=2^348 is fixed. The source's bounded-local-class lift cannot absorb that cost. The original coherent interval has only O(H) global classes; a method preserving this cross-prime correlation is not excluded. Second, using H itself as the short convolution length fails the source range: that factor must exceed X^.398, whereas H<=X^(2/7).

## Centered prime-interval upper bounds miss the sign and precision

The [Selberg audit](../dyson/round12/mixed-arithmetic/SELBERG_MIXED_REMAINDER_AUDIT.md) reads [Saffari--Vaughan, Lemma 5](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf), including printed page 20. Under RH its local estimate concerns genuine theta and is uniform for 0<eta<=1:

\[
\int_X^{2X}|\theta(x+\eta x)-\theta(x)-\eta x|^2dx
\ll \eta X^2\log^2(2/\eta).
\]

Applying Mellin Gallagher to the finite centered prime measure, retaining both cutoff crossings and the logarithmic weight, gives the valid but insufficient bound |M_T(b)|<=C log(T)/b^2. The associated integrated lower bound on the combined remainder is only of order -log(T)/b. It is much too weak for the required b^-2 correction. The prime and continuum pieces are never separated into unjustified infinite sums.

This is deliberately not claimed as the strongest RH consequence. Round 10 already had stronger individual norm control, and the same source page records Selberg's stronger global weighted estimate with a fixed exponent range. For a smooth filter on the active excess shell, the latter gives normalized squared norms O(1) and O(b^-2), hence only O(b^-1) control of the mixed product by Cauchy--Schwarz. It gives neither a positive increment in the shrinking shell nor the necessary signed next-order coefficient. A stronger use of the theorem is not ruled out.

Smoothing b leaves the actual sinc factor and joint centering in the kernel. A negative sinc lobe prevents a term-by-term nonnegativity argument. A negative kernel value alone would not disprove positive semidefiniteness, and the report explicitly avoids that inference. No generic point-process countermodel replaces actual prime arithmetic in this calculation.

## Review, replay and the next useful attempt

The [complete independent root review](../dyson/round12/INDEPENDENT_ROOT_REVIEW.md) pins all three author hashes, checks the primary source statements, and records the exact accepted scope. All 18 originals (1,904,996 bytes) are preserved locally under `Astra-Local-Archive/round12-originals/`; 15 research files are public verbatim. The third-party PDF, extracted text and rendered page stay local with receipts.

The [intake manifest](../dyson/round12/INTAKE_MANIFEST.json) and [bounded replay](../logs/round12-integration/recheck.json) verify the source bytes and two exact scripts. The sampling output matches in full. The dispersion certificate matches after removing only four temporary provenance paths; all reference hashes remain checked. The scripts verify rational constants, 60 cyclotomic signed-kernel identities and six fixed modular-selection examples. They do not numerically test PNT, the huge conductor construction, or a conjecture.

```text
python3 research/logs/round12-integration/recheck.py --prime-gap-source-dir /path/to/pinned/186/source-directory
python3 tools/verify_manifest.py
```

The next work retains the structures that these failed transfers discarded: the signed residue kernel, the coherent shift interval, and the additive phase through the m average. In particular the modulus-3 example suggests isolating rationally resonant m values before estimating the remaining phases, rather than assuming a uniform property that is false. A separate attempt is to estimate the exact signed dual norm through common-divisor compatibility and its genuine CRT boundary error. These are ongoing investigations, not new claims in this checkpoint.

The long PDFs retain their earlier checkpoints. The manual single-session Fable packet receives only the coordinator's superseding source-status prefix; it does not dispatch a new session or ask for covered computations again. No large scan, new model service, infrastructure layer or conjecture solution was introduced. Reverting this slice removes the new records without altering earlier proofs. Formalization and the required actual-zeta lower bound remain outstanding.
