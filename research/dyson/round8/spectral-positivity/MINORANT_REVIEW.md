# Independent review of the fixed positivity minorant

Date: 2026-09-05. Reviewer: the independent residual/arithmetic agent. Scope: the displayed minorant in [POSITIVITY_OBLIGATION_NOTE.md](POSITIVITY_OBLIGATION_NOTE.md), its closed constant, and the half-grid determinantal pair normalization. No parameter optimization, new literature survey, or actual-zeta computation was performed. The author note was not edited.

**Verdict: accepted as an ordinary mathematical proof under the stated pair-measure and interior-band assumptions, including the linear cumulative pair bound used for the tests.** I found no coefficient, sign, support, endpoint, or Palm-normalization defect. The regularization details below make explicit a step compressed into the note's decay statement. This is internal proof review, not formal verification or external peer review.

The bound is exactly the displayed expression, approximately **−0.2086745129639258**. It improves the immediate −sinh(1) consequence of pair positivity, but it is not progress to the required positive threshold 1/16, is not a new bound on actual zeta proved here, and is not optimal over general minorants. The optimum statement applies only to the specified one-parameter correction family and its displayed inference.

## 1. Nonnegativity of the remainder

Use the note's A, B, a, b, kappa and y=pi^2 x^2. To verify all parameter inequalities without decimals, put t=tanh(1/2), so 0<t<1 and

    a = 4t/(1+t^2),  b = 2t,
    kappa = 4t^3/(1+t^2),
    kappa/(4a-2b) = t^2/(3-t^2) < 1/2 < 1.

Thus 0<b<a<2b, both coefficients in the note's numerator for R+kappa are positive, and R>=-kappa. The numerator of R is -kappa+(4a-2b)y. Wherever R<0, |pi x|<1<pi/2. For 0<=z<pi/2, tan(z)>=z, because (tan(z)-z)'=tan^2(z)>=0. Hence (sin(z)/z)^2>=cos^2(z), also at z=0 by continuity. It follows on that negative region that

    cos^2(pi x) R(x) + kappa sinc^2(x)
      >= cos^2(pi x) [R(x)+kappa] >= 0.

On the remaining region both summands are nonnegative. This proves f>=0 everywhere, including zero; indeed f(0)=0. All rational identities used above pass the accompanying exact symbolic checks.

For f_c=cos^2(pi x)R+c sinc^2(x), evaluation at zero gives f_c(0)=c-kappa, so positivity requires c>=kappa. This condition is sufficient, since f_c=f_kappa+(c-kappa)sinc^2. The displayed lower-bound functional decreases by 4c/3 and is therefore maximized at c=kappa in this family. Even if one separately credits the known diagonal contribution f_c(0), the resulting functional decreases by c/3, so the same endpoint is still optimal. This observation does not establish an optimum among other band-limited minorants or other pair constraints.

## 2. Fourier support, endpoints, and legitimate pair testing

The convention is Fourier transform hhat(alpha)=integral h(x) exp(-2pi i alpha x) dx. Under this convention,

    [1/(1+pi^2 x^2)]hat = exp(-2|alpha|),
    [2/(1+4pi^2 x^2)]hat = exp(-|alpha|),
    [sinc^2(x)]hat = (1-|alpha|)_+.

The coefficients 1/2, 1/4, 1/4 in the modulation by cos^2(pi x) are therefore correct. For alpha>=1, the coefficient of a exp(-2alpha) becomes cosh^2(1), and that of b exp(-alpha) becomes cosh^2(1/2). The exact identities a cosh^2(1)=A and b cosh^2(1/2)=B cancel the whole Fourier tail. Evenness handles alpha<=-1. The triangular correction vanishes at both endpoints, and the modulation identities continue to hold there, so ghat(1)=ghat(-1)=0 exactly. There are no overlooked endpoint delta terms: J, f and g are integrable functions, and their Fourier transforms are continuous functions.

An unknown atom of the pair spectrum at either endpoint therefore contributes zero. The known band can be used without silently assuming endpoint atom-freeness. Here is also an ordinary justification for passing from Schwartz test identities to this particular g. Its compactly supported transform is continuous, piecewise smooth, vanishes linearly at the endpoints, and has first derivative of bounded variation. Smooth it and cut it off just inside (-1,1). These approximants can be chosen with uniformly bounded L1 norms and uniformly bounded total variation of their first derivatives: in an endpoint strip of width epsilon, the function is O(epsilon), so the second-derivative cutoff terms have bounded L1 norm. Their inverse transforms g_epsilon consequently obey

    |g_epsilon(x)| <= C/(1+x^2)

uniformly, and converge pointwise to g. The assumed linear cumulative pair bound gives integrability of this dominator. Dominated convergence on the pair side and the known interior spectral identity on the other side then yield

    integral g dmu = ghat(0) + integral_{-1}^{1} |alpha| ghat(alpha) dalpha.

This argument requires no guess about endpoint atoms or the unknown outer spectrum. Since f=J-g>=0 and mu is a positive measure, the note's inequality (P) follows. The subtraction A-B is correct: it is K(0), the Fourier atom of the unit mean-density contribution. Independently, J(0)=A-2B and mu>=delta_0 give W>=-B, as claimed.

## 3. Closed expression and fixed symbolic verification

For alpha in [0,1], each triple (r,c,d) contributes

    u exp(-r alpha) + v exp(r alpha),
    u = c-d(1/2+exp(-r)/4),  v = -d exp(-r)/4,

to ghat before the correction -kappa(1-alpha). Direct integration of alpha exp(+-r alpha) gives precisely I_minus and I_plus in the note. The value at zero contributes -kappa and the weighted integral contributes -kappa/3, explaining the total -4kappa/3 without any diagonal or two-sided factor ambiguity.

As an independent exact algebra check, set X=exp(1). The complete closed lower bound simplifies to

    (X-1)(3X^6-6X^5-17X^4+28X^3-35X^2-6X-15)
    / [12 X^2 (X+1)(X^2+1)].

This is an exact expression, not a fitted approximation. Substitution X=e gives -0.2086745129639258383515265856... . The script's decimal evaluation is explicitly floating, not an outward enclosure; the ordinary proof uses the exact formula and does not require a decimal certificate.

The companion [minorant_symbolic_check.py](minorant_symbolic_check.py) verifies the rational identities, the two elementary integrals, the endpoint, the correction coefficient, the Palm occupation division, the triangle-period integral and the DPP two-scale formula. [minorant_symbolic_check.json](minorant_symbolic_check.json) records PASS, versions and source hashes. Reproduction from this directory is `python3 minorant_symbolic_check.py`; it writes only its adjacent JSON. This is a small fixed identity check, not an optimization or sampled nonnegativity test.

## 4. Half-grid DPP normalization and realized obstruction

The stated Q is the Fourier projection of l2(Z) onto the interval [-1/4,1/4]. In particular it is a positive contraction with diagonal 1/2, and the standard discrete determinantal construction supplies a probability measure with finite occupation probabilities det(Q|F). The note's [Lyons reference](https://www.numdam.org/articles/10.1007/s10240-003-0016-0/) is the appropriate primary reference for the projection/positive-contraction framework. No independence of the occupation indicators is being assumed.

After scaling lattice spacing to 1/2, the occupancy probability 1/2 gives intensity 2*(1/2)=1. The independent uniform shift covers one full lattice cell; combined with integer-shift invariance of the discrete DPP this gives stationarity under every real translation. The lattice process is simple and has minimum positive spacing 1/2.

For k!=0, the conditional probability of a point at displacement k/2 from a Palm point is

    [1/4-|Q(0,k)|^2]/(1/2)
       = (1/2)[1-sinc^2(k/2)].

The Palm base point contributes exactly delta_0. Thus the displayed mu_A has the correct factor 1/2, and its nonzero weights lie between zero and 1/2. Counting the at most 2 floor(2R) nonzero lattice sites proves mu_A([-R,R])<=1+2R.

The full Fourier calculation can be written without omitting the zero sample:

    mu_A = delta_0 + (1/2) sum_k delta_(k/2)
                      - (1/2) sum_k sinc^2(k/2) delta_(k/2).

Poisson summation transforms these three terms into the constant density 1, the comb sum_m delta_(2m), and the periodized triangle sum_m (1-|alpha-2m|)_+, respectively. Hence the remaining continuous density is dist(alpha,2Z). Centering removes only the comb atom at zero. All nonzero even-frequency atoms survive, exactly as in the note.

Finally, the Laplace integral of the triangular density over one positive period is (1-exp(-r))^2/r^2. Summing its geometric repetitions on both sides gives 2 tanh(r/2)/r^2; the nonzero even comb gives 2/(exp(2r)-1). Therefore both V_A(r) and W_A=A V_A(2)-B V_A(1) are correctly normalized. The accompanying exact symbolic check reproduces the closed W_A expression, whose strict comparison with 1/16 was already enclosed in Round 7.

This actual process meets the stated low-band and positivity assumptions while remaining below 1/16. It is consequently a valid obstruction to deductions using only those assumptions. It is neither an actual-zeta construction nor a model asserted to satisfy the missing arithmetic identities. No stronger impossibility or universality conclusion is endorsed.
