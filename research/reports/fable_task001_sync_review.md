# Fable task 001: pinned-source synchronization and numerical review

Date: 2026-09-05.

**Reviewed source commit:** **a408e7050fffc74459b3c83fafa5ac03c8b7dea6**, in the old Alpha-devbox PR #11 repository. All statements about files being present or absent refer to this exact commit, not to later working state or an unseen running session.

Source directory: [Fable task001 at the reviewed commit](https://github.com/galpha-ai/Alpha-devbox/tree/a408e7050fffc74459b3c83fafa5ac03c8b7dea6/research/riemann-rmt/overnight/fable/astra_tasks/task001).

**Conclusion:** Fable has demonstrably picked up the task and returned an independent F2 numerical check. Its committed continuum and finite-sum results agree with Astra's fixed-family certificate and finite operator conventions. No mathematical counterexample, missing leading term, positive half-gap margin, or completed Fable arithmetic-transfer proof is present in the reviewed snapshot. The final task001 report is still absent.

## 1. Receipt, provenance and missing deliverables

The reviewed **FABLE_COORDINATION.md** explicitly records pickup at 06:30 UTC from new-repository commit 97df092. The immutable input mirror's **SOURCE_COMMIT.txt** gives the full hash

    97df092427a1035cf1c66dc712148ccccac09ac2

and says the copy was taken at 2026-09-05T06:26:51Z from the new repository's codex/astra-research branch.

The copied task text still says “published, awaiting explicit pickup.” That is a stale status in a historical input snapshot, not evidence that Fable never received the task. The coordination entry plus independent scripts, logs and numerical outputs demonstrate actual execution.

Present under **astra_tasks/task001/**:

- f2_continuum.py
- f2_continuum_results.json
- f2_continuum_run.log
- f2_finite_sum.py
- f2_finite_sum_results.json
- f2_finite_sum_run.log
- f2_finite_sum_run_1e7.log
- f2_drift_fit.py

Explicitly checked absent at the pinned commit:

- **astra_tasks/task001_report.md**, the promised final report;
- **astra_tasks/task001/f2_finite_sum_results_1e7.json**;
- **astra_tasks/task001/f2_drift_fit_results.json**.

The 1e7 log contains only the initial float-sieve validation line. It is not evidence that an \(L=10^7\) finite-sum computation completed. The drift-fit script is present, but no committed output establishes that it completed. Neither unfinished item should be promoted into the returned-results table.

The committed **CLAIMS.md** has prime-gap certificate entries D1.2, D1.3, D1.4, D1.6, D1.7, D1.8, and no task001/F2 claim. In particular, it does not record a completed arithmetic transfer or an independent refuter verdict for this task.

The coordination file describes Fable's adversarial workflow and intended proposer/refuter organization. That description is not a substitute for the absent task-specific final mathematical report.

Recommended current receipt state:

> **Picked up; F2 numerical artifacts returned and reviewed; final Fable arithmetic-transfer report not yet present at a408e705.**

Preserve the original input snapshot unchanged. Put the corrected live receipt state in the current task ledger or synchronization note.

## 2. Continuum computation versus the exact certificate

Fable independently implements Gauss–Jacobi/Legendre quadrature using a different simplex parametrization:
\[
u=\sigma\tau,\qquad w=\sigma(1-\tau),\qquad
\sigma=(1-v)s,\qquad du\,dw=(1-v)^2s\,ds\,d\tau.
\]
The Jacobian, weight \(v^{a-1}\), continuous sine-kernel limits, prime-insertion shifts and coefficients agree with the fixed schema. Its expectation-product expansion correctly uses both first and second background \(S_2\) moments, including the \(u^2w^2\) insertion cross term.

For \(\ell=16/15\) and the specified rational \(H=f(v)+g(v)S_2\), the order-64 result is
\[
J_{\rm Fable}=-0.014662375473370598.
\]
The order-40/order-64 spread is \(2.38698\times10^{-15}\). The difference from Astra's stored target \(-0.014662375473368985\) is
\[
-1.61329\times10^{-15}.
\]

Astra's exact rational continuum certificate encloses the value within approximately
\[
[-0.014662375473368995,\,-0.014662375473368974].
\]
Fable's ordinary floating result is **not literally inside that much narrower interval**. Agreement is to roughly fourteen decimal places, as expected for this quadrature and floating summation. This is consistent independent numerical evidence, not a new interval certificate and not a contradiction of the existing certificate.

The separated order-64 quantities are

| Quantity | Fable floating value |
|---|---:|
| \(I\) | 0.9976809471028788 |
| \(M_{2a}\) | 0.07475319679662187 |
| \(M_{2b}\) | 0.07563555032577103 |
| \(M_3\) | 0.0844031170042764 |
| \((M_2+M_3)/I\) | 0.2353376245266294 |
| equivalent raw Rayleigh value | 4.6453785095398725 |

The half-gap threshold for that raw Rayleigh value is \(\pi^2/2\), so the margin remains negative.

The mass-only version of the same rational \(f\) gives
\[
J_{\rm massonly}=-0.021565258857184827,
\]
and the fixed \(S_2\) extension improves that particular continuum value by approximately \(0.00690288338381423\). This comparison should not be confused with the much smaller improvement over the independently optimized mass-only degree-14 baseline:
\[
J_{\rm degree14}=-0.015357981703850332
\]
in Fable's calculation. Its difference from Astra's degree-14 numerical result is \(2.22\times10^{-16}\).

Fable correctly labels its continuum JSON as a stipulated-form quadrature, not a certificate and not an arithmetic theorem.

## 3. Finite arithmetic operator implementation

The finite script uses
\[
x_n=d_\ell(n)H(\log n/\log L,S_2(n))/\sqrt n,\qquad
A_{qm,m}=\frac{2\sin((\pi/2)\log q/\log L)}{e\sqrt q},
\quad q=p^e.
\]
The index ranges, prime-power exponents, \(1/\sqrt q\) factor and distinct-prime definition of \(S_2\) match the stated trial. The divisor sieve multiplies by \((\ell+e-1)/e\) at each prime-power level, giving the correct cumulative \(d_\ell(p^e)\).

The full Rayleigh expression is
\[
J_L=\frac{\|Ax\|^2+\langle x,A^2x\rangle}
{2\pi^2\|x\|^2}-\frac14.
\]
The stored scalar numerator pieces and normalized contributions reconstruct every reported trial/mode margin to within \(2.78\times10^{-17}\). The diagonal quantity is the equal-insertion part of \(\|Ax\|^2\), so its correspondence with \(M_3\) is the correct one.

Fable reports validation of the floating \(d_{16/15}\) sieve against exact rational values for all \(n\le10^4\), with maximum relative error \(1.52234\times10^{-15}\). This checks the sieve; it does not make the logarithms, trigonometric values, finite sums or eigenvalues exact.

The committed completed lengths are \(10^3,10^4,10^5,10^6\):

| \(L\) | fixed \(J_L\), full operator | same \(f\), mass only | fixed minus mass only |
|---:|---:|---:|---:|
| 1,000 | −0.0519926036839853 | −0.0624270849868530 | 0.0104344813028678 |
| 10,000 | −0.0431174919059547 | −0.0529803909830878 | 0.00986289907713303 |
| 100,000 | −0.0376302025223919 | −0.0470594610068825 | 0.00942925848449061 |
| 1,000,000 | −0.0339175762941035 | −0.0430127050936602 | 0.00909512879955668 |

The finite values approach the proposed continuum value over these lengths, but four slowly varying points cannot prove a limit. All recorded fixed-family margins are negative.

Fable also computes full-operator top eigenvalues for \(L=10^3,10^4,10^5\). Comparing the stored values with Astra's previously committed **arithmetic-results.json**, without rerunning an eigensolver:

| \(L\) | Fable top eigenvalue | Difference from Astra |
|---:|---:|---:|
| 1,000 | 3.949287136694299 | 0 |
| 10,000 | 4.105867045445441 | \(-1.78\times10^{-15}\) |
| 100,000 | 4.205255380109547 | 0 |

This is useful independent evidence that the two finite-operator implementations have the same normalization. It does not imply a uniform upper bound for all lengths.

## 4. Prime powers, background coincidences and finite drift

The script includes two diagnostic alterations:

- **nopp:** keep only prime insertions, discarding higher prime powers;
- **clean:** additionally remove insertions \(p\) into backgrounds already divisible by \(p\).

The code implements these restrictions consistently in \(A\), its transpose and the diagonal contribution. They are altered finite operators, not the exact full theorem operator.

For the fixed trial, the recorded values are:

| \(L\) | full | nopp | clean |
|---:|---:|---:|---:|
| 1,000 | −0.0519926037 | −0.1022308502 | −0.1269460914 |
| 10,000 | −0.0431174919 | −0.0892650368 | −0.1129780712 |
| 100,000 | −0.0376302025 | −0.0793053529 | −0.1015970942 |
| 1,000,000 | −0.0339175763 | −0.0715145441 | −0.0922927227 |

These differences are large at attainable lengths. They show why simply deleting exceptional terms numerically and declaring them negligible is unsafe. They do **not** refute an asymptotic theorem proving that their normalized contribution tends to zero. Astra's separately written fixed-family transfer proof uses explicit weighted Schur bounds and an ordered cutoff limit for precisely this issue.

The finite \(S_2\)-moment ratios are likewise not uniformly close to one: the first-moment ratio changes from 1.0142 to 1.0302, while the second-moment ratio changes from 1.2034 to 1.1346. Nonmonotonic finite drift of an individual ratio does not contradict convergence. These values also cannot prove the asserted Poisson–Dirichlet moment law by themselves.

The background Euler-product constant is explicitly marked recalled, truncated at primes \(\le10^7\), and not independently source-verified in Fable's script. It is a normalization diagnostic rather than a certified leading-constant enclosure.

The drift-fit script warns correctly that its fitted limits are diagnostic only. Since no committed fit output is present at the reviewed SHA, this review assigns no numerical conclusion to that script.

## 5. What this changes in the fixed-family proof status

Astra's round-two **symmetric_prime_arithmetic_transfer.md** and the independent review already give an ordinary written proof for fixed \(\ell\ge1\) and fixed \(H=f(v)+g(v)S_2\), including this rational trial. The earlier round-one certificate's “arithmetic transfer not certified” label is historical and should be accompanied by a link to that later proof, not silently rewritten.

Fable task001 contributes a genuinely separate numerical implementation supporting:

1. the stipulated continuum-integral value;
2. the exact finite operator's normalization;
3. the importance of finite prime-power and coincidence corrections;
4. the continued negative sign of the tested margin.

It does **not**, in this snapshot, contribute the requested derivation of the marked Euler product, the short-background limit, or the complete insertion/coincidence asymptotic. Its code explicitly says that the original Inoue paper was not read for this diagnostic. That is an honest scope label, but it leaves the single main mathematical obligation unfulfilled in the returned Fable artifacts.

There is no contrary theorem claim to reconcile. Keep the following three statuses distinct:

- **Exact continuum inequality:** Astra certificate; negative margin.
- **Fixed-family arithmetic transfer:** Astra written proof plus separate mathematical review.
- **Fable task001:** numerical F2 independently returned; final arithmetic report absent at the pinned source.

No new zero-gap record, global variational no-go, AH contradiction or proof of RH follows from this synchronization.

## 6. Review method and reproducibility

This review read the pinned files with git show from:

    /Users/qingyunsun/Library/CloudStorage/Dropbox/Research/ACUE-Astra-Handoff-2026-09-04/github-worktree

Example:

    git show a408e7050fffc74459b3c83fafa5ac03c8b7dea6:research/riemann-rmt/overnight/fable/astra_tasks/task001/f2_finite_sum.py

Presence and absence were checked with git ls-tree and git cat-file at the same SHA. Stored JSON values were parsed to recompute scalar normalization identities and compared with the existing Astra result files. No new large eigenproblem, finite-vector sweep, Claude message, Claude task or session was launched. All review output is in staging.

## 7. Coverage of the current single-session computation packet

This table maps the requirements in the current local packet

    /Users/qingyunsun/Documents/Codex/2026-09-04/realtime-voice-chat/outputs/FABLE_SINGLE_SESSION_COMPUTE_TASK.md

to actual artifacts already present at **a408e7050fffc74459b3c83fafa5ac03c8b7dea6**. **Receipt of that new packet is unconfirmed.** The confirmed pickup in §1 concerns the older task001 packet. Matching old outputs may satisfy individual new requirements without showing receipt or execution of the new packet.

Reviewed packet SHA256: **745c6411355b163f429cbeaa96b7c1b681f8b36e6ec92152f74cba30739743f5**.

All paths below are relative to the pinned **research/riemann-rmt/overnight/fable/astra_tasks/task001/** directory.

| Current acceptance requirement | Coverage | Existing evidence and precise limit |
|---|---|---|
| Fixed rational continuum form, simultaneous insertion shifts, and exact rational norm | **Partly** | **f2_continuum.py**, **f2_continuum_results.json** independently implement the expectation expansion and simultaneous shifts; \(J=-0.014662375473370598\) agrees numerically. Norm is float64 quadrature only. No independent exact rational norm calculation or audit of the original signed Taylor/\(\pi\)/remainder certificate is returned. |
| \(g=0\) control at the same \(\ell=16/15\) and same \(f\) | **Covered** | The **massonly** trial exists in both continuum and finite-sum scripts/JSON. It gives continuum \(J=-0.021565258857184827\) and matching finite controls. The separately requested nonzero-rescaling invariance test is **not covered** by an explicit returned test. |
| \(L=97\) direct-loop versus sparse convolution, using candidate and deterministic control | **Not covered** | No \(L=97\) run or direct/sparse two-vector comparison is present. Existing sieve validation and \(L\ge1000\) eigenvalue agreement do not substitute for this requirement. |
| Fixed-vector \(L=10^3,10^4,10^5\), \(\theta=1\), with separate quadratic terms and candidate-minus-control comparison | **Covered** | **f2_finite_sum_results.json** records \(\|x\|^2,\|Ax\|^2,x^\top A^2x,J_L\) for candidate and **massonly** control at all three cutoffs. Their differences are reconstructed in §3 from those stored values; no rerun was needed. The old run also contains additional eigenvalue calculations, which are not part of the new packet's requested batch. |
| One \(\theta=0.98\) sensitivity check at the largest completed cutoff | **Not covered** | The pinned operator hard-codes \(\theta=1\); no \(\theta=0.98\) result is present. Neither the continuum control nor a prime-insertion restriction is this sensitivity test. |
| Arithmetic-obligations table covering weighted moments, existing prime divisibility, multiplicity, coincident insertions, cutoffs/uniformity and beyond-diagonal errors | **Not covered** | F2 contains helpful finite coincidence/moment diagnostics, but no six-item estimate/status/use table or final **task001_report.md**. Astra's separate transfer proof is existing Astra evidence, not fulfillment of a Fable deliverable. |

**Acceptance state:** reuse the covered numerical outputs; retain partial or absent requirements explicitly. The old task was picked up and F2 outputs were returned. The new packet's receipt and complete acceptance are not established by this snapshot. No new calculation or Claude task was launched to fill these gaps during this review.
