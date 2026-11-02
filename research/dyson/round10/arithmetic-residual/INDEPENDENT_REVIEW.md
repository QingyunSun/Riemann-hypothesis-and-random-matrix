# Independent review of the arithmetic range and mixed-moment audit

Date: 2026-09-05. Reviewer: root. Accepted as a bounded primary-source audit and a conditional calculus implication. No actual-prime lower bound is proved.

The final author report `ARITHMETIC_RANGE_AND_MIXED_MOMENT.md` has SHA256 `c2d2a278ffe74d8f8d8a7c00980e5e57e6c508790ff96904db4479277d1daa8c`. The root read the complete report and script, the actual Guth–Maynard v2 Corollary 1.4 and following Remark, and the saved CCCM Theorem 3/Corollary 4 and Theorem 14/Corollary 15 passages. Earlier Round 9 results are used with their independently reviewed uniformity, not strengthened by assumption.

## Source range and error

Corollary 1.4 states the prime-count asymptotic for h>=X^(2/15+epsilon), with fixed epsilon, outside an exponentially small proportion of integer starting points. In the edge shell X=T^(1+s/b), h=X/T, the exponent is exactly s/(b+s). The corollary's limiting epsilon-zero threshold is b<=13s/2; the shell 1<=s<=2 is outside it once b>13. The source's subsequent Remark permits a slight fixed-epsilon improvement with a weaker error, not an exponent tending to zero. The author now records that distinction explicitly.

The conversion of a prime count to a log-weighted count does not need a new uniform theorem for every inner endpoint. On [x,x+h], log p=log x+O(h/X). Multiplying the stated count approximation by log x introduces the displayed exponential error and an elementary O(h²/X) remainder (a sharper version is unnecessary). For h<=X^.99 that remainder is absorbed by the retained exponential error. The exceptional intervals are bounded trivially. The resulting sufficient upper bound on the squared error is far above X h log(X/h) for fixed positive h-exponent. This demonstrates a limitation of that direct consequence of the corollary, without claiming that its methods cannot yield stronger information.

The CCCM constants and quantifiers are correctly reported. Its beta is the prime-range endpoint, not the damping b. Fixed multiplicative constants 0.9028... and 1.0736... are not an error tending to zero with b. Fixed-endpoint limiting comparisons do not themselves provide the moving-endpoint uniformity required here. This is a narrow audit of these sources, not an exhaustive impossibility theorem for all known prime-variance methods.

## Conditional mixed moment

For the actual analytic residual at fixed T, differentiating the centered integral on b>0 is valid under RH: an extra log factor is integrable at every fixed positive distance from the critical line. Pole and endpoint terms must also be differentiated, as the report states. There is no differentiation of an unspecified asymptotic remainder.

With E(b)=e^b ||R_b||²/(T log²T) and K_b=-R_b-2 partial_b R_b, the real inner-product identity is M(b)=-E'(b). In the absolutely convergent region K has coefficient log(p)/log(T)-1, confirming the sign and factor two. Its use in the working strip is analytic continuation, not an unregularized prime series.

The exact two-scale identity includes -e^(-2b)E(b)+e^(-4b)E(2b). The previously reviewed RH upper estimate, after subtracting the short-prime diagonal, is O(e^(-b)) for r(b) on the slow range; its uniform height error and the prime-power replacement stay negligible after multiplication by e^b. Thus E=O(1) there, and the exponential correction vanishes uniformly as the lower cutoff B tends to infinity. A crude pointwise bound alone would not justify this step.

Finally, integrating 1/s²-(2-epsilon)/s³ from b to 2b gives 1/(2b)-3(2-epsilon)/(8b²). After multiplication by b² and subtraction of 1/(2b), the threshold is exactly -3/4+3epsilon/8. The author requires the assumed inequality through 2G(T), including a uniform o(s^-3) error; that is the needed quantifier. This implication is accepted. The mixed-moment hypothesis itself remains completely unproved in these notes, and the source audit supplies no positive epsilon.

The small exact script checks only the scalar algebra and range endpoints. Independent replay is a separate implementation check and does not certify a new analytic estimate.
