# Coordinator review of the complete central fixed-pairing bound

2026-09-05. Outcome: the ordinary derivation is accepted within its explicitly balanced, central, fixed-profile scope. It proves an RH O(1) bound for the whole cofactor block, a low-frequency O(1/log X) contribution, and a summable upper tail. It does not prove a strict signed bound or a global improvement.

Reviewed author file: SIGNED_MELLIN_BLOCK_BOUND.md, 16776 bytes, SHA256 99e25b2e25085077d47b575366e92e9609e83bd8db3584d2d744d9a99ff4c3f1. The complete file was read and frozen alongside this review. An earlier 16433-byte version was superseded during review; the extra paragraph distinguishing adjacent-increment resonances from continuous stationary points was included in the final read.

## What was checked

1. The smooth extension holds the prime endpoint n fixed. It equals the actual centered even-shift sum at every odd product dk; it never differentiates Lambda(x+h). The fixed product cutoff, sharp odd d/k endpoints, all prime powers, and flat center 2 survive the Mellin inversion. Its normalization is exactly 1/(pi X ell^2), with positive exponents in both Dirichlet polynomials.

2. Differentiating at fixed n produces x(partial_x-partial_h), hence a T^j scale for the j-th logarithmic derivative and T^j/Y for its h derivative. The partial-summation estimate T^(2j)/Y times the integrated centered prefix square follows with the compact endpoints zero. The explicit odd-count floor formula and subtraction of powers of 2 give O(1), rather than an unaccounted logarithmic error, in this central geometry.

3. In the Selberg mean-square application the substitution lambda=Ty/x contributes the essential Jacobian x/T. It gives the upper bound X^3/T times the integral of J(3,T/lambda) over [1/2,2], hence X Y^2 log^2 X. The exponent beta=3 stays fixed; the real x interval is below (T/lambda)^3 uniformly for large T. Multiplying by T^(2j)/(XY) gives the claimed Sobolev mass T^(2j)Y log^2 X. There is no asserted Y log X local variance.

4. The low-frequency argument uses a genuinely additional Cramer input, integral_X^(3X) |E|^2 << X^2. Direct differentiation verifies partial_x k+partial_u k=T(1/x-1/u)k, with multiplier O(1/X). Integration by parts retains the exact lattice difference and powers-of-2 term. Differentiating G(v)=A(x)S(x)/x gives the stated sign A/x-A' in R. The two kernel support lengths O(Y), Schur's bound, and dx/x give squared norms O(Y^2/X)=O(1). Thus f(e^v)=G'(v)+R(v) really proves the weighted Fourier bound with denominator 1+t^2. Pointwise RH alone was not substituted for Cramer's mean square.

5. Montgomery–Vaughan's Dirichlet mean value applies to the actual finite odd-supported polynomial with zero coefficients elsewhere and remains valid after time translation by changing coefficient phases. It gives (R+D)D without pointwise cancellation in mu. The odd variable k=2r+1 yields phase derivative t/(pi k); the stationary condition is t/k=pi j. The revised note separately records the exact adjacent increment t log(1+2/k)/(2pi). The low interval |t|<=pi K/2 is safe. Above it, the second-derivative estimate includes stationary aliases and remains a legal, if sometimes weak, bound at arbitrarily high frequency.

6. Cauchy over the entire low interval uses the negative Sobolev bound and contributes T^2 log X before normalization, hence O(1/log X). In a high dyadic band R<|t|<=2R, the three factors have scales T^(j+1/2) log X R^(-j), sqrt(RT), and sqrt R log X. After normalization their product is (R/T)^(1-j). Taking j=2 sums every high band, while fixed higher j yields the stated upper tail. Constants remain dependent on the fixed profiles and compact comparison ranges; no usable numerical threshold constant was extracted.

## Primary-source verification

- Montgomery–Vaughan, Hilbert's Inequality (1974), Corollary 3, equation (1.11), printed page 75: the primary PDF was opened and its actual page image read because the extracted formula was incomplete. The displayed mean value is sum |a_n|^2 (R+O(n)); it supplies precisely the polynomial estimate used here. https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf
- Brent–Platt–Trudgian, The mean square of the error term in the prime number theorem, printed page 741, equation (1) and Theorem 1: the primary text explicitly gives the RH O(X^2) local mean square and distinguishes it from the pointwise bound. Its numerical 0.8603 result is not imported into the packet constants. https://maths-people.anu.edu.au/~brent/pd/rpb274-final.pdf
- Carneiro–Chandee–Chirre–Milinovich, A tale of three integrals, primary printed page 1, equations (1.1) and (1.3): the J(beta,S) definition and fixed beta=3 admissibility were checked live. https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf
- Montgomery–Vaughan author draft, Corollary 16.6 and Theorem 16.7, printed pages 7–8: checked in the immediately preceding coordinator input-plane derivation, with the correct e(x)=exp(2pi i x) convention. https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf

This is a full review of the author's application and its complete frequency accounting. It is not a rereading of all proofs in the source papers, a Lean verification, execution of the author's checker, another numerical experiment, or a publication/manifest audit.

## Implication for the research target

The improvement is local and substantive: the actual balanced central fixed pairing is bounded without demanding a uniform operator saving. The proof uses no cancellation special to mu beyond its bounded coefficients and mean-square diagonal. The carrier/stationary range still has exactly enough logarithms to exhaust the normalization. The earlier global O(1) aggregate remains a separate known result; this block theorem cannot be summed over unrestricted packets to manufacture a strict global bound. A sign, an explicit threshold gain, or a correlated estimate in the actual carrier integral remains missing.
