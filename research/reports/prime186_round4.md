# A certified restoration credit and the remaining k=39 deficit

2026-09-05. This is a new research checkpoint after the 333-page handoff at commit `055a4a0`. **The prime-gap bound remains 186.** No new zeta gap, AH refutation, or Dyson–Montgomery theorem is proved.

The useful completed result is a strictly positive, outward-enclosed integral that the published sufficient criterion discards. On the same published 40-coordinate trial, it improves the certified normalized sieve margin from about **23.36045 ppm to 24.86626 ppm**, conditional on the original published cap and loss endpoints. Independently, a complete 77-coefficient cap-only optimization at dimension 39 remains about **5603.60 ppm below one**. That second result is a floating-point diagnosis, not a rigorous upper bound for the whole coefficient family.

## 1. Exact new positive credit

Proposition 4.6 of [Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf) gives

\[
\rho_*\langle P_OF,BP_OF\rangle-\|P_OF\|^2
\ge \rho_*(J_{\lambda,H}-\beta-E_O)-I_H+c_\alpha\alpha,
\]

where

\[
\alpha=\|(1-P_O)F\|^2,\qquad
c_\alpha=1-4\rho_*|b_h|
=\frac{2497786653900013}{2500000000000000}>0.
\]

The paper drops the last term in its convenient sufficient criterion. Its existing positive error covers provide upper estimates, so they cannot be reused as lower estimates for this credit.

We instead select a true sufficient-failure event. In units of the official mesh

\[
h=\frac{2742997}{258046918656},
\]

there are exactly two global fragments above \(b=18800h\), uniquely labelled by

\[
p\in[26400,29100]h,\qquad q\in[32400,36700]h.
\]

All residual coordinate totals are at most \(b\). The official radial cell index is restricted to \(95639\le r\le98263\). This event lies within the cap domain and violates an actual retained new-ladder order-three row, with a strictly positive rational failure margin. Both fragments can belong to one coordinate or to different coordinates; both cases are necessary.

Restricting the remaining fragments to total at most \(b\) makes their one-coordinate total measure exactly Lebesgue measure. Replacing \(1/p\) and \(1/q\) by their lower endpoint-independent constants yields a single coherent positive lower measure. Its cell kernels are rational box-sum volumes, computed by integer positive-part polynomials. There is no Dickman quadrature error in these new kernels.

The two-mark ring gives exactly 40 same-owner terms and \(40\cdot39\) different-owner terms, with no factor \(1/2\). The 53 signed polynomial terms all integrate the square of the same step trial against that same positive lower measure. Their signs cannot be discarded individually.

The outward calculation gives, in the official common normalization,

\[
\alpha_{\rm rect}\in
[3.5697238789\times10^{-20},\;3.5697238869\times10^{-20}],
\]

where these decimals are rounded outwards from the exact rational endpoints saved in the receipt. Safe downward-rounded consequences are

\[
\boxed{\alpha/I_H^+>1.5071462817\times10^{-6}},
\qquad
\boxed{c_\alpha\alpha/I_H^+>1.5058119471\times10^{-6}}.
\]

The original complete normalized lower margin, replayed from the published endpoints, is

\[
0.000023360452297044097\ldots.
\]

Adding only the new proved credit gives

\[
0.000024866264244232060\ldots,
\]

an increase of about 6.45 percent of that small margin. It is an improvement in the certificate for the same trial and same theorem, not a reduction of 186.

The larger two-fragment triangle gives an exploratory estimate around 9.76 ppm, while the one certified rectangle gives 1.5058 ppm. We do not promote the triangle estimate to a certified credit. The tiny exact rational anchor in the working files is only a strict-positivity/normalization regression; the meaningful quantitative result is the outward rectangle contraction.

Evidence:

* [Complete event, kernel and credit proof](../prime-gaps/round4/prime-credit/prime_alpha_credit.md).
* [Outward rectangle receipt](../prime-gaps/round4/prime-credit/alpha_rectangle_certificate.json) and [exact complete-margin replay](../prime-gaps/round4/prime-credit/alpha_credit_margin_replay.json).
* [Independent mathematical review](../prime-gaps/round4/restoration-proof/ALPHA_RECTANGLE_INDEPENDENT_REVIEW.md), including an independent integer-cell/Eulerian reconstruction of every entry in all three marked kernels.
* [Separate-process rerun](../prime-gaps/round4/independent-rectangle-recheck/alpha_rectangle_certificate.json): all 53 term intervals and the final rational endpoints agree exactly with the first run. Runtimes were about 92.6 and 90.2 seconds on this host.

## 2. The actual k=39 scale

The independent cap implementation reconstructs the published physical radii, nested fragment caps and step masks, then changes the outer/retained dimensions to 39/38. It uses the correct \(39h/Z\) face normalization. No dimension-40 integral endpoint is inherited.

On the official 98,304-cell grid:

| Trial | Cap-only quotient \(\rho_*J/I\) | Status |
|---|---:|---|
| k=40, original 77 coefficients | 1.000206086776951 | Positive control; denominator lies in the published interval |
| k=39, original coefficients | 0.994361581476018 | Fixed-vector floating evaluation |
| k=39, optimized full 77 coefficients | 0.994396399364491 | Independent direct evaluation of the numerical Ritz candidate |
| k=40, optimized full 77 coefficients | 1.000213743639754 | Optimized positive control |

The original k=39 deficit is about 5638.42 ppm. Reoptimizing the coefficients recovers about 34.82 ppm, leaving about 5603.60 ppm. This is a useful reason to change the support or trial structure instead of repeatedly evaluating the old vector.

The scaled k=39 Gram matrix has condition number about \(2.28\times10^{10}\). The optimized matrix quotient and direct scalar reevaluation differ by \(1.74\times10^{-10}\), and the numerical generalized residual is small. Those checks support the computation; they do **not** establish an interval upper bound for all possible coefficients. Likewise, the k=40 alpha lower bound cannot be inserted into a k=39 proof, nor used as an upper bound on all recoverable alpha mass.

The implementation uses exponential tilting as a numerically cancelling normalization, not as a change of trial. Two tilt values give the same fixed-grid result to about \(4.2\times10^{-15}\). NumPy's requested `longdouble` is actually binary64 on this machine; that limitation is recorded in the JSON and report.

See [full k=39 report, matrix data and returned coefficients](../prime-gaps/round4/k39-trial/REPORT.md). Neither a cap-only quotient nor a numerical family maximum pays the rootwise source-restoration costs or proves DHL[39,2].

## 3. Sharper restoration identities and a quantified failure

The exact projection identity retains both signed cross terms and removed face squares. For \(e=(1-P_O)F\), \(V_i=E_iF\) and \(W_i=E_ie\),

\[
\mathcal Q(P_OF)=\mathcal Q(F)+\alpha+
\rho_*\sum_i\int m_i\bigl(|W_i|^2-2\operatorname{Re}(\overline W_iV_i)\bigr).
\]

This identifies the actual projected-marginal matrix as the useful future optimization object. A completed-square bound instead requires an upper estimate for \(\int_{H_O\setminus O}|BF|^2\). Applying only the generic factor 40 to the old face ledger is worse than the existing Young bound. A certified effective factor below about 14.9573 would improve that particular comparison. Merely writing a sharper identity does not supply such cancellation.

There is also an exact positive inner-overlap correction, but the published ledger caps its benefit for this fixed trial at \(7.8813\times10^{-8}\) of the normalized margin. It is too small to explain the k=39 deficit. The old upper ledger gives only a loose 1.9344 percent ceiling on possible alpha credit, not any positive lower credit by itself.

The [independent restoration proof and exact ledger replay](../prime-gaps/round4/restoration-proof/RESTORATION_PROOF_AUDIT.md) state these alternatives and prevent double counting. They include 200 finite signed-product diagnostics; ordinary written arguments, not those tests, supply the identities.

## 4. Corrected runtime and verification limits

The unchanged official regression failed in the earlier packaged FLINT environment. We built a separate FLINT 3.6.0 with [the upstream signed-conversion fix](https://github.com/flintlib/flint/commit/7ad753d51c82fdec115cb179b41d0e581f1cb0ec), then built Python-FLINT against it. The native integer/polynomial and Arb suites pass, as do the original certificate checks and 467 full plus 2,188 truncated products compared with an independent Python integer implementation.

The complete Python binding suite has a separately documented assertion failure in a Jacobi test that calls the native function outside its odd-positive-denominator contract. Assertions remain enabled. The certificate does not use Jacobi, and the directly used binding APIs were tested independently. We do not claim a universally verified arithmetic library or that the whole binding suite passed.

The [runtime record and build scripts](../prime-gaps/round4/repro-flint/README.md) preserve source hashes, actual library linkage, successful checks, failed build configurations and the full-suite failure. The official PrimeGaps186 source was not modified. The new credit inherits the original published cap/loss endpoints; all 149 old physical forms were not recomputed in this round.

## 5. Reproduce and continue

Use an isolated copy when executing scripts that write adjacent JSON outputs. External primary inputs can be selected explicitly:

```sh
export PRIME186_SOURCE=/path/to/PrimeGaps186/prime_gap_186_certificate.py
export PRIME186_NUMERICS_TEXT=/path/to/short_gaps_numerics.txt
```

The latter is a `pdftotext` extraction of the pinned official numerical companion; its hash is recorded by the ledger replay. The public package does not duplicate the full third-party paper text. In the relevant copied subfolders:

```sh
python certify_alpha_rectangle.py                    # exact kernel/geometry checks
CORRECTED_PYTHON certify_alpha_rectangle.py --certify # outward integral
python replay_credit_margin.py                      # exact final inequality
python rectangle_independent_checks.py              # different integer kernel construction
python restoration_checks.py                       # source ledger + signed identities
OPENBLAS_NUM_THREADS=1 python cap_trial.py --k 39 --intervals 98304 --tilt 20
```

New code in the public copy differs from staging only where explicitly recorded in [the intake manifest](../prime-gaps/round4/INTAKE_MANIFEST.json), principally to select the external source paths. Original output receipts are retained.

The next active experiment changes the radius/plateau support geometry and recomputes any affected exceptional-square constant. It must retain actual lcm conditions, both source ladders, inner-domain intersections, the negative full-face term and inward masks. A new outward positive **complete** k=39 inequality would be needed before claiming a smaller gap. Repeated fixed-vector scans, a new full handoff rendering, and Jacobi-wrapper repair are postponed in this slice.
