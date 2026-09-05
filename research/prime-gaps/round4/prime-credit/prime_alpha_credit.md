# Retained positive deletion credit for the published prime-gap-186 trial

Status: the failure-region inclusion is proved and one meaningful rational-kernel rectangle has been contracted with outward arithmetic. It certifies $\alpha/I_H^+\geq1.5071462817258709\cdot10^{-6}$ (decimal display of an exact rational lower endpoint). The retained credit improves the source-inherited fixed-trial margin from about 23.36045 ppm to 24.86626 ppm. The larger triangle estimate remains diagnostic. This note makes no smaller prime-gap claim and does not discharge the three project inputs in the official Lean development.

## 1. The exact quantity and its scale

For the actual published $k=40$ midpoint step trial, Proposition 4.6 of the main paper gives

$$
\rho_*\langle P_OF,BP_OF\rangle-\|P_OF\|^2
\geq \rho_*(J_{\lambda,H}-\beta-E_O)-I_H+c_\alpha\alpha,
\qquad
\alpha=\|(1-P_O)F\|^2,
$$

where

$$
c_\alpha=1-4\rho_*|b_h|=0.9991146615600052\ldots>0.
$$

The published sufficient inequality drops this positive term. A lower bound on the **actual $F^2$-weighted deleted mass**, rather than the measure of a covering set, can therefore be inserted without changing the previously paid upper bounds on $\beta$ and $E_O$. This does not recover the outer cross-term for free; that cross-term remains fully charged through $E_O$.

The common normalized denominator is source-certified as

$$
23685317816\cdot10^{-24}\leq I_H\leq23685317890\cdot10^{-24}.
$$

All numerical forms in this note use the numerical companion's normalization $(hZ)^{-40}$, where $Z=\sum_{j=0}^{98263}g((j+1/2)h)^2$ and $h=2742997/258046918656$. This is essential: the main paper uses unscaled forms, whereas the companion divides every form by this same factor.

The previously replayed complete margin is about $23.3604523$ parts per million. The new, explicitly contained failure region below has a diagnostic mass of about $9.75897$ parts per million of $I_H$. Its retained credit would be about $9.75033$ parts per million if this size is certified. The diagnostic alone is not a valid replacement for an outward lower endpoint.

## 2. A disjoint lower-bound event

Let $\nu_c=e^\gamma c\,\mathcal L(\Pi_c)$, with Poisson intensity $du/u$ on $(0,c]$. Its total-size pushforward is $\rho_D(t/c)\,dt$. In particular, restricting the residual total to $0\leq t\leq c$ gives exactly Lebesgue measure, because $\rho_D(t/c)=1$ there.

Set

$$
b=18800h=0.19984095864653703\ldots,
\qquad c=46580h=0.49513786456147313\ldots.
$$

Use the actual retained new-ladder row 24, not a failure-cover threshold assembled from different rows. Its parameters are

$$
a=1.0166236774089747\ldots,
\quad A=1.0449558074337872\ldots,
\quad L=0.5498119373071242\ldots,
\quad \xi=0.028332320501728507\ldots.
$$

The exact fractions are regenerated from the preserving official source and saved in the JSON outputs. Its outer predicate is

$$
\{s\leq a\}\ \cup\
\{H_{\phi_D,\xi}\leq A,\ \phi_E(M_\xi)\leq C\},
\qquad \phi_D(u)=\min(3u/2,L).
$$

Consider configurations having precisely two global fragments above $b$, ordered as $p<q$, with

$$
b<p<q\leq c,
\qquad q+p+\min(3p/2,L)>A.
$$

Remove these two fragments. Require every residual coordinate total $x_i$ to lie in $[0,b]$, and require the restored total $s=\sum_i x_i+p+q$ to exceed $a$. Finally retain only the official radial cells $\sum_i\lfloor t_i/h\rfloor<98264$.

Every residual fragment is at most $b<p$, so the inclusive tail at the witness $p$ consists exactly of $p$ and $q$. The displayed strict inequality therefore violates this actual row. Every fragment is at most the smallest outer cap $c$, so all three outer-shell fragment caps hold. The retained radial cells put the configuration in $H_O$. Consequently this region is a subset of $H_O\setminus O$.

There is no Palm multiplicity loss here. The two large fragments are globally unique and ordered. Their coordinate owners produce disjoint cases:

- distinct owners: $40\cdot39$ ordered choices;
- one common owner: $40$ choices.

The Poisson decomposition gives the measure $\prod_i dx_i\,dp\,dq/(pq)$ on each such case. No additional $1/2$ occurs after imposing $p<q$. The same-owner case has both marked fragments in a single coordinate; it is not represented by the distinct-owner integral.

Define

$$
t^D=(x_1+p,x_2+q,x_3,\ldots,x_{40}),
\qquad
 t^S=(x_1+p+q,x_2,\ldots,x_{40}),
$$

and let $F_\square(t)$ be the **official step function**, including its exact midpoint polynomial and profile, evaluated at these totals. Let $R_D,R_S$ impose the preceding radial conditions. With

$$
\mathcal T=\{(p,q):p<q\leq c,\ q+p+\min(3p/2,L)>A\},
$$

we obtain the proved lower-bound formula

$$
\alpha\geq\frac{1}{(hZ)^{40}}\left[
1560\int_{\mathcal T}\int_{[0,b]^{40}}
1_{R_D}F_\square(t^D)^2\,dx\,\frac{dp\,dq}{pq}
+
40\int_{\mathcal T}\int_{[0,b]^{40}}
1_{R_S}F_\square(t^S)^2\,dx\,\frac{dp\,dq}{pq}
\right].
$$

Here $\mathcal T$ may equivalently start at

$$
p_{\min}=(A-c)/(5/2)=0.21992717714892562\ldots>b,
\qquad q>\max\{p,A-p-\min(3p/2,L)\}.
$$

Thus the apparently additional condition $p>b$ is automatic in the implemented triangle. These inequalities are checked with exact fractions when constructing the event.

## 3. Measured mass of this genuine subset

`alpha_credit.py` uses scrambled Sobol sampling with an explicitly evaluated importance density. Unmarked residual cells are sampled with probabilities proportional to $g_j^2e^{-\lambda jh}$; conditional positions are uniform in the selected fine cell. Marked residuals use truncated exponential densities. The code evaluates the exact published midpoint step trial, and cancels the proposal factors explicitly. The proposal tilt is 45 and the cutoff is exactly $18800h$.

Eight independent scrambles, each with $2^{20}$ points for each owner case, give:

| Disjoint event | Estimated mass divided by published $I_H^+$ | Standard error across scrambles |
|---|---:|---:|
| Distinct coordinate owners | $4.2125098941\cdot10^{-6}$ | $1.72\cdot10^{-8}$ |
| Same coordinate owner | $5.5464619292\cdot10^{-6}$ | $2.11\cdot10^{-8}$ |
| Sum | $9.7589718233\cdot10^{-6}$ | No deterministic enclosure |

The run evaluated 16,777,216 points and took about 40 seconds on this host. The same-owner contribution is about 57% of the total. The weighted fragment locations are approximately $p=0.293$–$0.294$, $q=0.362$–$0.365$, and the weighted full total is about $1.032$.

These are reproducible randomized-quadrature diagnostics. Across-scramble standard errors are not rigorous integration-error bounds; ordinary floating-point evaluation is also not an outward enclosure. The estimates do not prove $\alpha/I_H\geq9.7\cdot10^{-6}$.

## 4. Exact rational positive kernels for a certifiable rectangle

One disjoint rectangle inside the failure triangle is

$$
P=[26400h,29100h],\qquad Q=[32400h,36700h].
$$

Indeed, $P$ lies below $Q$, all marks are above $b$ and below $c$, and throughout the rectangle

$$
q+p+\phi_D(p)=q+\frac52p\geq98400h>A.
$$

The source-core condition is guaranteed on every cell with index sum

$$
95639\leq r\leq98263,
$$

since $95638h\leq a<95639h$ and the actual total is at least $rh$. This deliberately discards cells that straddle the activation boundary.

Replace the positive fragment density $1/(pq)$ by the smaller constant $1/(P_+Q_+)$. This defines a coherent positive submeasure. Its cell kernels involve **only rational box volumes**, not Dickman quadrature or a critical-line approximation.

For a vector of positive integer lengths $w=(w_1,\ldots,w_d)$ and integer offset $o$, define

$$
V_{o,w}(j)=\frac1{d!}\sum_{\epsilon\in\{0,1\}^d}(-1)^{|\epsilon|}
\left[(j+1-o-\epsilon\cdot w)_+^d-(j-o-\epsilon\cdot w)_+^d\right].
$$

It is exactly the volume of $\{0\leq y_i\leq w_i:j\leq o+\sum_i y_i<j+1\}$. In units of cell measure $h$, the four coordinate kernels are

$$
u_j=1_{0\leq j<18800},
\quad
v_j=\frac{V_{26400,(2700,18800)}(j)}{29100},
\quad
w_j=\frac{V_{32400,(4300,18800)}(j)}{36700},
$$

$$
z_j=\frac{V_{58800,(2700,4300,18800)}(j)}{29100\cdot36700}.
$$

The last channel is the same-owner measure. Multiply each by $g_j^2/Z$ and place them in the positive marking ring

$$
K_j=\frac{g_j^2}{Z}(u_j+av_j+bw_j+abz_j),\qquad a^2=b^2=0.
$$

The $ab$ coefficient of the 40-coordinate moment contraction automatically includes both $40z u^{39}$ and $40\cdot39vw u^{38}$. These multiplicities must not be added a second time.

The official finite symmetric-moment identity (numerical companion (2.10)–(2.12)) now evaluates this lower submeasure against the **same signed expansion of $F_\square^2$**. Taking signed coefficient terms separately as nonnegative would be invalid. The adapter accumulates their full outward intervals before assessing the lower endpoint.

`certify_alpha_rectangle.py` supplies the four exact integer-numerator arrays and rational denominators. Its standalone structural checks pass:

- every cell coefficient is nonnegative;
- the exact numerator mass sums are $18800$, $101520000$, $161680000$, and $1309608000000$;
- denominators are $1$, $58200$, $73400$, and $6407820000$;
- known two- and three-unit box-sum distributions agree;
- the marking-ring mass agrees exactly with the independent same/distinct owner formula;
- every rectangle point satisfies the actual source failure and cap inequalities.

A separate QMC evaluation of **this lower constant-density rectangle**, using the stricter cell mask, estimates

$$
\alpha_{\rm rect}/I_H^+\approx1.5111578472\cdot10^{-6}
$$

with distinct-owner $0.6524769$ ppm and same-owner $0.8586809$ ppm. The outward contraction subsequently completed all 53 signed square signatures in 92.582 seconds on one worker. It enclosed the normalized rectangle mass in

$$
[3.5697238789408751\cdot10^{-20},\ 3.5697238868155496\cdot10^{-20}],
$$

where the exact dyadic endpoints, not these decimal displays, are stored in `alpha_rectangle_certificate.json`. Consequently

$$
\frac{\alpha}{I_H^+}\geq
\frac{9050325235576887333393096923828125}
{6004941487970983985258771441262503395328}
=1.507146281725870950\ldots\cdot10^{-6},
$$

and the retained margin credit is at least

$$
\frac{c_\alpha\alpha^-}{I_H^+}
=1.505811947187963804\ldots\cdot10^{-6}.
$$

Replaying the printed original $I^\pm,J^-,L^+$ endpoints with this newly certified lower mass gives

$$
\mathcal M_{\rm new}\geq0.000024866264244232\ldots,
$$

a 6.44598798% increase over the previous lower-margin endpoint. This strengthens a certificate for the same trial and $k=40$; its admissible tuple and gap 186 are unchanged. `replay_credit_margin.py` records the complete exact rational addition in `alpha_credit_margin_replay.json`.

The QMC estimates at proposal tilts 45 and 35 bracket the certified value within their empirical fluctuation scale. They served as diagnostics, not as input to the proof. Tiling the larger triangle with disjoint rectangles can retain more mass; overlapping rectangle sums would not be valid lower bounds.

## 5. What is already rigorous, and the next executable obligation

`exact_cell_anchor.py` gives a completely rational positive anchor $\alpha/I_H^+\geq10^{-197}$. It uses two explicit owner types with all residual totals in one fine-cell subinterval, evaluates the constant step-trial values exactly, and proves the auxiliary bound $hZ<11/500$ by a rational monotone Riemann sum. This tiny result verifies strict positivity and normalization. It has no useful effect on the sieve margin.

The meaningful rectangle calculation uses the official `CapEngine` and `SourceJets` implementations without changing their source. `CapEngine` executes the mandatory signed-FLINT regression. The adapter does not catch, disable, replace, or bypass that check. It introduces new rational lower kernels and the proven radial mask, then asks the existing outward machinery to contract them on all 98,264 retained indices.

The completed run used `/Users/qingyunsun/.cache/astra-research/flint-3.6.0-patched/venv/bin/python`, 160-bit Arb precision, 224-bit fixed-point positive convolutions, and one worker. The original signed-FFT startup regression passed unchanged. The root agent separately reports exact signed-convolution comparisons and passing native `fmpz_poly`/`fmpz_vec` tests for this corrected build. This is not a claim that the entire Python-FLINT test suite passed: the root identified an unrelated assert-enabled Jacobi test with an even denominator. Native assertions and the certificate regression remained enabled.

The rectangle now has an actual outward lower endpoint. The remaining work is independent review/replay of this new adapter and, if the larger approximately 9.76-ppm mass is worth pursuing, a disjoint finite rectangle cover from inside followed by its outward contractions. The full triangle estimate remains uncertified.

Commands, from this directory:

```sh
python3 certify_alpha_rectangle.py
python3 exact_cell_anchor.py
python3 alpha_credit.py --power 20 --repeats 8 --output alpha_credit_p20.json
python3 alpha_credit.py --region rectangle_lower --power 19 --repeats 4 --output alpha_rectangle_p19.json
# Only a corrected runtime which passes the unmodified signed regression:
/Users/qingyunsun/.cache/astra-research/flint-3.6.0-patched/venv/bin/python certify_alpha_rectangle.py --certify --threads 1
python3 replay_credit_margin.py
```

The files `alpha_rectangle_kernel_checks.json`, `exact_cell_anchor.json`, `alpha_credit_p20.json`, and `alpha_rectangle_p19.json` record the present evidence. The completed outward run wrote `alpha_rectangle_certificate.json` and `alpha_rectangle_certificate.log`; the positive credit is taken from its exact rational lower endpoint. Independent review of the adapter and subset proof remains appropriate before publication.

## 6. Relevance to $k=39$

The adjacent independent round-four experiment reports that the published coefficient vector reused at $k=39$ gives cap-only quotient $\rho_*J/I\approx0.994361581476$, a deficit of about 5638 ppm before restoring supports. The demonstrated $k=40$ region is about 10 ppm and cannot close that particular numerical deficit. Nor can its mass be inherited by dimension 39: the trial, measure, source masks, operator constants, and their normalization must all be reevaluated.

This does not establish a global $k=39$ obstruction. It establishes a concrete scale comparison for one inherited trial and identifies a previously dropped positive term with an inexpensive rational-kernel route to certification. A better vector or changed support geometry remains a separate optimization problem.

## Sources and provenance

The mathematical sources are the [official PrimeGaps186 repository](https://github.com/openai/PrimeGaps186), its main manuscript (Proposition 4.6 and (4.40)), and [the numerical companion](https://github.com/openai/PrimeGaps186/blob/61340d0b74163003b32756bb16e91d9209a5e330/short_gaps_numerics.pdf), §§1.1–1.3 and (2.10)–(2.12). The preserving clone is at commit `61340d0b74163003b32756bb16e91d9209a5e330`; the official certificate file SHA256 is `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`.

The scripts read that source and write only in this owned staging directory. The published denominator and previous margin are inherited primary-source enclosures; they were not recomputed in this subtask. No external paid model calls, source-clone mutations, or unrelated toolchain rebuilds were used by this agent.
