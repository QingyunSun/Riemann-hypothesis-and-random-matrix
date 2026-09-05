# F1 repair: corrected coefficient, surviving sign issue, and cutoff scaling

Date: 2026-09-05. Review of Fable PR11 commit `20730285c8f9a81539e0662c6e015023c2ed107a`. This review supersedes the corresponding old-version objections only where an actual repair is present. It does not reopen the independently proved Astra fixed-family arithmetic transfer.

## Repairs that are present

The revised F1 text changes Pi_4's leading coefficient from 6a² to 6a and correctly combines it with Pi_2² to obtain a²+6a. The displayed local inclusion probability has leading a p^(-s), while its quadratic correction is summable with log^4 p near s=1. Together with the pole of zeta'/zeta, this is an adequate analytic derivation of the leading coefficient. A numerical experiment is not logically required to close that algebraic point.

The fixed-v normalization sequence is also corrected to the actual v=1 rows. Those two earlier text objections are therefore repaired in this snapshot. Fitting the revised finite values to a log-power rate remains numerical evidence, not a proved uniform error bound.

The new direct prime-sum script is honestly described in the revised report as inconclusive. Its code computes the local tail E=sum_(e>=1)d_ell(p^e)^2 p^(-es) and rho=E/(1+E), which is the correct inclusion probability. The script's opening docstring instead writes rho=1-1/E while defining E without its constant term; that docstring is inconsistent with the code. With E including the constant one, the latter formula would be correct.

## The refuter's probe sign remains wrong

The revised prose still cites the unchanged `refute_F1_rigour.py` probe as an independent confirmation of positive six. It is not: zz3 is the third derivative of zeta'/zeta, so eps^4 zz3 tends to +6 and the script's negative probe tends to -6. Its saved data are indeed -6. The earlier separate Astra correction remains applicable. This does not invalidate the revised analytic coefficient calculation.

## The finite cutoff has a predictable incomplete-gamma limit

The claim that primes merely up to exp(1/eps) resolve the leading fourth-order pole is misleading. Write P for the prime cutoff and z=eps log P. PNT and the local expansion rho_p(1+eps)(1-rho_p(1+eps))=a p^(-1-eps)+O_a(p^(-2-2eps)) give, as eps tends to zero and P tends to infinity with z tending to z_0 in [0,infinity],

\[
\frac{\varepsilon^4}{6a}
\sum_{p\le P}(\log p)^4\rho_p(1+\varepsilon)(1-\rho_p(1+\varepsilon))
\longrightarrow
1-e^{-z_0}\left(1+z_0+\frac{z_0^2}{2}+\frac{z_0^3}{6}\right),
\tag{1}
\]

with the right side interpreted as one at z_0=infinity. In particular exp(1/eps) corresponds to the fixed incomplete fraction at z_0=1, not the whole pole. Resolving most of the leading mass requires eps log P large, not merely P exceeding exp(1/eps).

For completeness, the proof is elementary. The local quadratic error has an absolutely convergent log^4-weighted prime sum for eps near zero, hence vanishes after multiplying by eps^4. For the leading term use Stieltjes summation with theta(x)~x and weight (log x)^3 x^(-1-eps). Splitting at a fixed large x_0 makes the PNT relative error uniformly small above x_0; the lower segment contributes o(1) after scaling. Weighted integration by parts controls that error by a fixed multiple of the full positive gamma integral. Substituting t=eps log x in the main integral gives integral_0^z t^3 e^(-t)dt. Sending the PNT error to zero proves (1), including a bounded or divergent z. If P stays fixed while eps tends to zero, the finite sum is bounded and its scaled value simply tends to zero.

For the actual fixed P=2*10^6, eps=.125 has z about 1.8136, and eps=.0625 has z about .9068. The leading-mass fractions are correspondingly small. The report's assertion that the first cutoff already exceeds P at eps=.125 also contradicts its own parenthetical exp(8)<P. More relevant than that typo is the fourth-order weighting: the transformed density is t^3 exp(-t), whose bulk lies beyond t=1.

Equation (1) is an asymptotic cutoff diagnosis, not a numerical error certificate for the five stored finite points. It explains why that particular experiment is unsuitable as a full-pole confirmation. The existing analytic proof already establishes 6a; larger prime scans are unnecessary for that purpose.

## Scope retained

The latest text still describes its broader M2/coincidence transfer as incomplete. That is its own derivation status. Astra's later independently reviewed fixed-family o(1) transfer remains a separate proved result and does not require the explicit rate missing from F1. Neither a repaired intermediate coefficient nor a finite drift fit gives a positive half-gap margin, a uniform full-operator limit, or a theorem about zeta pair correlation.
