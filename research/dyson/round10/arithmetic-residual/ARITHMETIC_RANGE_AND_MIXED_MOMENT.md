# Actual-prime variance ranges and a missing logarithmic mixed moment

Date: 2026-09-05. This is a bounded arithmetic-source audit and a conditional calculus lemma. **No improved lower bound for the actual residual or the coupled zeta statistic is proved.** There is no new point-process countermodel, prime-profile search or repetition of the Stieltjes continuation proof.

The negative decision has a concrete arithmetic basis. The checked Guth–Maynard theorem has a short-interval range that misses the shrinking edge region, and even its almost-all PNT error inside that range is much larger than the needed fluctuation scale. The checked RH short-interval variance comparison retains fixed constant losses and fixed-endpoint quantifiers. A further precise mixed moment of the genuine-prime tail would suffice; its numerical threshold is derived below, but that moment is not supplied by either source.

## 1. Object and the local prime scales

Retain the already reviewed Round 9 definitions L=log T, N=floor(T/L^6), and the genuine-prime residual R_(T,b)(t). This is the analytic prime-only continuation at s=1/2+b/(2L)+it with the prime polynomial through N subtracted. It includes the endpoint and pole terms of that continuation. It is not interpreted as a convergent bare prime Dirichlet series on this line.

Write

    r_T^p(b)=integral_0^T |R_(T,b)(t)|^2 dt /(T L^2),
    E_T(b)=exp(b) r_T^p(b).

The mesoscopic statistic uses the two widths b and 2b at the same height and cutoff. The previously reviewed prime-power-removal error is o(1) after its amplified normalization uniformly on 2<=b<=G(T), for any G(T)->infinity with G(T)=o(log log T). Thus it is legitimate to study this genuine-prime residual without pretending that the removed prime powers supply a fixed positive improvement.

To inspect a fixed portion of the first edge, put

    X=T^(1+s/b),  1<=s<=2,  h=X/T.

Then the exact exponent of h relative to X is

    log h/log X = s/(b+s).

This tends to zero as b increases. The size h nevertheless exceeds every fixed power of log X on these slow diagonals. Statements about intervals of length at most a fixed power of log X, or about X<=T, therefore do not cover this edge shell. Conversely, an estimate requiring h>=X^theta for a fixed theta>0 eventually misses it. These are arithmetic scale comparisons, not a conclusion from generic spectral positivity.

## 2. Guth–Maynard: exact range gap, then a separate moment gap

The primary source inspected is Guth and Maynard, [New large value estimates for Dirichlet polynomials, arXiv:2405.20552v2](https://arxiv.org/html/2405.20552v2), dated 7 April 2026. Corollary 1.4 gives an almost-all asymptotic for the prime count when

    X^(2/15+epsilon) <= h <= X^.99,

for fixed epsilon>0. The exceptional set has size O(X exp(-(log X)^(1/4))), and on the other integers x around X the count error is O_epsilon(h exp(-(log X)^(1/4))). This is an asymptotic count statement, not a sharp variance statement. The actual improved exponent is 2/15; this audit does not repeat the obsolete 1/6 exponent as if it were current.

Even if epsilon were set to zero, the edge shell above would have to satisfy

    s/(b+s) >= 2/15,  equivalently b <= 13s/2.

Hence when b>13 the entire fixed shell 1<=s<=2 is outside the theorem. At b=14, its endpoint exponents are 1/15 and 1/8, both below 2/15. This is an exact range calculation, not a numerical parameter scan. The admissible fixed-epsilon range is smaller still. In terms of X=T^alpha, this corollary's epsilon-to-zero endpoint is alpha>=15/13, while the needed shell has alpha=1+O(1/b). This endpoint is not asserted to exhaust the authors' methods.

The final Remark after the proof of Corollary 1.4 describes a sieve treatment of the critical six-factor case that could slightly lower the fixed exponent to 2/15-epsilon, at the cost of a prime-count error roughly O(epsilon^4 h/log X). For a fixed sufficiently small epsilon this remains a positive-power lower cutoff for h, so it still misses s/(b+s)->0. Its stated count error also does not determine a fluctuation-level second moment or the shrinking variance correction needed below. Thus this remark does not remove either obstruction; no optimality of 2/15 for the underlying method is claimed.

There is a second and independent obstruction even inside the source range. Converting the count bound to the Chebyshev weight costs O(log X). Bounding the exceptional intervals trivially then gives at best a consequence of the form

    sum_(integer x in [X,2X])
       |theta(x+h)-theta(x)-h|^2
        << X h^2 (log X)^2 exp(-c (log X)^(1/4)),

with some fixed c>0; harmless endpoint and partial-summation errors are smaller here. On the good set one can square the error, but the exceptional-set contribution has only the single exponential saving. The expected fluctuation scale for this variance is X h log(X/h). For h=X^theta with any fixed theta in the source range below .99, the quotient of the displayed error bound by that scale contains

    h log X exp(-c (log X)^(1/4)),

which tends to infinity. The quoted corollary alone therefore does not control the variance to constant accuracy, let alone the relative o(1/b) edge accuracy needed here. This diagnoses the precision of this theorem's stated consequence; it does not deny stronger consequences of its underlying methods after further argument.

The large-value Theorem 1.1 in the same source does not directly resolve this issue either. The paper specifies its main improvement over earlier bounds for length N<=T^(5/6-epsilon), while a single un-factorized prime block at X=T^(1+s/b) has length greater than T. A further factorization or arithmetic estimate could exploit the method, but that would be additional work, not an application of its ready-made full-block bound. The independent shifted-modulus lane studies such a different route and is not duplicated here.

## 3. What the checked RH short-interval variance results provide

The other primary source is Carneiro–Chandee–Chirre–Milinovich, [On Montgomery's pair correlation conjecture: a tale of three integrals](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf). Its short-interval statistic is

    J(beta,T)=integral_1^(T^beta)
       [psi(x+x/T)-psi(x)-x/T]^2 dx/x^2.

The paper recalls the asymptotic J(beta,T)~beta^2 log^2(T)/(2T) for fixed 0<beta<=1. That is the side before the first edge. It does not evaluate the increment from beta=1 to beta=1+s/b>1. Theorem 3 / Corollary 4 give, for large fixed beta, constants 0.8376 and 1.4283 multiplying beta log^2(T)/T. Here beta is the exponent delimiting the prime range, not the damping parameter b. Sending the damping b to infinity does not make beta=1+s/b a large-beta instance of that theorem.

For finite endpoint intervals, Theorem 14 and Corollary 15 give a precise comparison with integrated pair correlation, with factors L_minus=0.9028... and L_plus=1.0736... . Both are separated from one by fixed amounts. As a stand-alone comparison, this retains roughly 9.7% lower-side and 7.4% upper-side slack, whereas the first-edge task requires a relative error decreasing like o(1/b). Those fixed losses cannot be read as the required coefficient of 1/b. Moreover the source's fixed-endpoint liminf/limsup statements do not license a moving endpoint beta(T)=1+s/b(T) without a uniformity or diagonal argument.

This does not claim that every RH variance theorem is exhausted or that no sharper short-interval argument exists. It records the exact scope and quantitative gap of the primary results checked here. It also avoids replacing the earlier Round 9 failure of individual logarithmic-derivative bounds by a claim that an almost-all prime-count asymptotic has already solved their coupled moment.

## 4. A concrete mixed moment of the same arithmetic tail

There is a useful way to state the missing arithmetic input more precisely. Define the logarithmically weighted companion using the derivative of the actual analytic residual:

    K_(T,b)(t) = -R_(T,b)(t) - 2 partial_b R_(T,b)(t),

    M_T(b) = exp(b)/(T L^2)
        Re integral_0^T R_(T,b)(t) conjugate(K_(T,b)(t)) dt.

At fixed T this derivative exists on b>0 in the relevant critical-strip range under RH. Differentiation of the already available centered-tail integral is justified by its additional logarithmic factor and the same RH bound for theta(x)-x. Endpoint and pole terms are differentiated as well. No derivative estimate is inferred by differentiating an uncontrolled o(1) remainder.

In the absolutely convergent right half-plane this companion weights the genuine-prime tail by log(p)/L-1; in the working strip it is the analytic continuation with its required centering. Thus M_T is a specific correlation with a logarithmic excess weight, not just the norm of either residual and not a freely chosen covariance model.

The exact derivative identity is

    M_T(b) = -d/db E_T(b).

This gives the following conditional criterion. Suppose there are fixed epsilon>0 and an increasing slow envelope G(T)=o(log log T) such that, uniformly on B0<=s<=2G(T),

    M_T(s) >= 1/s^2 - (2-epsilon)/s^3 - eta_T/s^3,
    eta_T -> 0.

Then the original AH-excluding mesoscopic target follows, with a quantitative gap:

    lim_(B->infinity) liminf_(T->infinity)
       inf_(B<=b<=G(T)) C_T(b)
          >= -3/4 + 3epsilon/8 > -3/4.

This is a sufficient additional arithmetic hypothesis, not a result established for M_T. It is stronger than merely knowing each residual's leading norm, but weaker in a different direction than demanding a full collection of prime pair correlations. It singles out exactly one signed mixed moment along a slow range.

To verify the implication, rewrite the prime-only coupled statistic exactly as

    C_T^p(b)=b^2 [E_T(b)-E_T(2b)-1/(2b)
                  -exp(-2b)E_T(b)+exp(-4b)E_T(2b)].

The already reviewed RH upper estimates of Round 9 imply E_T(s)=O(1) uniformly on the slow range: their absolute finite-height error remains negligible after multiplication by exp(s), and their limiting residual upper expression is O(exp(-s)). Prime-power removal preserves this conclusion. Therefore the two exponentially small terms contribute o(1) in the displayed double-limit regime; this uses an actual previously checked upper estimate, not an assumption of perfect residual asymptotics.

Now integrate M_T(s)=-E_T'(s) from b to 2b. The exact integrals are

    integral_b^(2b) s^(-2) ds = 1/(2b),
    integral_b^(2b) s^(-3) ds = 3/(8b^2).

The asserted lower limit follows, and the reviewed uniform genuine-prime replacement error carries it back to C_T. This reasoning needs control up to 2G(T), not only G(T), and retains the uniform range needed for compatibility with the AH slow-diagonal argument. No simplicity assumption enters.

The decisive missing quantity is therefore the coefficient below 2 in this log-weighted mixed-moment deficit. None of the inspected short-interval mean-count or variance theorems supplies that coefficient. A Cauchy–Schwarz estimate using only separate norms does not evaluate this signed mixed moment; a new arithmetic decorrelation, projection estimate, or weighted short-interval covariance result would be needed.

## 5. Evidence, reproducibility and stopping decision

[check_edge_mixed_moment.py](check_edge_mixed_moment.py) and its [JSON](check_edge_mixed_moment.json) check the exact 2/15 range threshold, the two fixed b=14 endpoint examples, the hyperbolic algebra and the coefficient 3epsilon/8. They do not evaluate actual zeta zeros, search parameters, or test the mixed-moment hypothesis.

The source receipt pins the retrieved Guth–Maynard v2 HTML and the already archived CCCM text/PDF together with the relevant Round 9 reports. Third-party source bodies are local references, not material to duplicate in a public code archive. There is no claim that this narrow audit is a complete survey of all prime-variance literature.

The bounded conclusion is negative but specific: the checked improved prime-count theorem misses the growing-damping edge and lacks fluctuation-level precision even where it applies; the checked RH variance comparisons do not supply the required shrinking first correction. The conditional logarithmic mixed-moment inequality is a reviewable next arithmetic obligation. Its proof, or a weaker averaged version sufficient on [b,2b], remains open here. Repeating finite prime-factor coefficient scans and general PSD models is postponed.
