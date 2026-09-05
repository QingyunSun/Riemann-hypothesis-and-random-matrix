# Fable 5.1: one concrete computation for Astra

## Mission and limits

Use my **existing Fable 5.1 / Claude Code session** at its current selected mode. GPT-6 Astra leads the main research; your role is one independent computational audit.

**Question:** Does the fixed symmetric prime-factor resonator below have the claimed continuum margin, and does its finite arithmetic quadratic form expose a normalization, sign, or prime-power error?

This should tell Astra whether to keep the candidate and attack its missing arithmetic transfer, repair an error, or abandon the claimed formula. Our main target is the RH-conditional zeta-zero half-gap barrier and Montgomery–Dyson statistics. A numerical audit is an input to that proof, not a solution of the conjecture.

**One session, one work packet.** Do not create subagents, new Claude sessions, parallel model calls, paid API calls, or an automatic research loop. Do not change models or billing. No additional spending is authorized. Finish the specified audit, return the result, and stop until a new concrete assignment arrives.

Do not begin a literature survey, optimize new coefficients, add features, or rerun the million-dimensional eigenvalue search.

## 1. Inputs and workspace

Shared repository:
https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix

Historical research:
https://github.com/galpha-ai/Alpha-devbox/tree/claude/riemann-zeta-random-matrix-udxp3f

Current authoritative source directory, verified after the research workspace migration:

~~~text
/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research/research/residual-gram/
~~~

Read only the relevant small files first:

~~~text
rational_trial_certificate.py
rational-trial-certificate.json
arithmetic_operator.py
general_prime_features.py
inoue_variational.py
../reports/residual_gram_round1.md
~~~

These files are now present in the shared local repository. Pin the actual commit you read and record hashes if the inputs have uncommitted edits. The formulas below are sufficient to start if a source is missing; report that once instead of searching unrelated history. The earlier research-round1 directory is historical, not the current authoritative workspace.

Read the repository's AGENTS.md. Preserve existing work, do not modify main, and use a narrow branch for this audit. **Do not run source scripts in place if they overwrite their adjacent JSON files.** Copy required inputs into your own directory. The rational certificate script also executes on import.

## 2. Fixed candidate: do not optimize

\[
\phi=\frac12,\qquad \ell=\frac{16}{15},\qquad a=\ell^2=\frac{256}{225}.
\]

\[
f(v)=\frac{145+3v-116v^2+71v^3-6v^4}{100},
\]

\[
g(v)=\frac{-563+1682v-2479v^2+1751v^3-488v^4}{100},
\qquad H(v,S)=f(v)+g(v)S.
\]

The reference claims a continuum margin approximately

\[
J_{\rm ref}=-0.014662375473369
\]

and an exact enclosure contained in

\[
-\frac{1467}{100000}<J_{\rm ref}<-\frac{1465}{100000}.
\]

Audit these claims independently. This fixed rational candidate is **different** from the optimized multi-feature candidate reported near -0.01465473. The old degree-14 one-variable baseline was reported near -0.01535798170385 at a different optimized \(\ell\). Do not confuse the three trials or treat any as a global optimum. All three margins are negative.

## 3. Independently check the continuum form

For this calculation, the background statistic satisfies

\[
\mathbb E_v S=\frac{v^2}{a+1},\qquad
\mathbb E_v S^2=\frac{a+6}{(a+1)(a+2)(a+3)}v^4.
\]

Only these two moments are needed. Set

\[
H_0=H(v,S),\quad H_u=H(v+u,S+u^2),\quad
H_w=H(v+w,S+w^2),
\]

\[
H_{u,w}=H(v+u+w,S+u^2+w^2).
\]

\[
N_H=\int_0^1v^{a-1}\mathbb E_v[H_0^2]\,dv,
\]

\[
Q_2=\frac{2\ell^2}{\pi^2}
\int_{\substack{v,u,w\ge0\\v+u+w\le1}}
v^{a-1}\frac{\sin(\pi u/2)\sin(\pi w/2)}{uw}
\mathbb E_v[H_0H_{u,w}+H_uH_w]\,dv\,du\,dw,
\]

\[
Q_3=\frac{2}{\pi^2}
\int_{\substack{v,u\ge0\\v+u\le1}}
v^{a-1}\frac{\sin^2(\pi u/2)}u\mathbb E_v[H_0^2]\,dv\,du,
\qquad
J_{\rm cont}=\frac{Q_2+Q_3}{N_H}-\frac14.
\]

Use continuous limits at removable singularities. These are the proposed continuum formulas; their applicability to arithmetic is not an established input.

Required checks:

1. Expand the expectations symbolically. Prime insertion must shift mass and \(S\) **simultaneously**, not via an accidental sequential substitution.
2. Compute the norm with exact rational arithmetic. The reference claims
   \[
   N_H=
   \frac{14048570231396640851971777495951292585559}
        {14081225337811261631891125059730620313600}.
   \]
3. Independently compute \(Q_2,Q_3,J_{\rm cont}\). Do not merely call the original integration function again. Use your own beta-integral/Taylor enclosure or an independent high-precision quadrature path.
4. Audit the original certificate's signed coefficients, \(\pi\) enclosure, remainder bounds, and division by the positive norm. Distinguish a rigorous enclosure from numerical agreement.
5. Set \(g=0\) and verify reduction to the one-variable form at the **same** \(\ell,f\). Check quotient invariance under a nonzero constant rescaling of \(H\).
6. If you find a definite certificate error, identify the earliest invalid step and give a minimal correction or counterexample. Floating-point agreement alone is not certification.

## 4. Finite arithmetic: evaluate the fixed vector

Define the multiplicative generalized divisor coefficients by

\[
d_\ell(1)=1,\qquad
d_\ell(p^e)=\frac{\ell(\ell+1)\cdots(\ell+e-1)}{e!}.
\]

For \(1\le n\le L\), use

\[
v_n=\frac{\log n}{\log L},\quad
S_{2,L}(n)=\sum_{\substack{p\mid n\\p\ {\rm prime}}}
\left(\frac{\log p}{\log L}\right)^2,
\]

\[
r_L(n)=d_\ell(n)H(v_n,S_{2,L}(n)),\qquad
x_n=\frac{r_L(n)}{\sqrt n}.
\]

The sum is over **distinct prime divisors**. Do not silently count multiplicities. Whether prime powers and repeated insertions affect the proposed limiting model is part of the transfer audit.

For \(q=p^e\), define

\[
A_{qm,m}=
\frac{2\sin\!\left(\frac{\pi\theta\log q}{2\log L}\right)}
{e\sqrt q},\qquad qm\le L,
\]

and zero otherwise. Let

\[
K=A^\top A+\frac{A^2+(A^\top)^2}{2},\qquad
J_{L,\theta}=\frac{x^\top Kx}{2\pi^2x^\top x}-\frac14.
\]

Do not form dense \(K\). For real \(x\),

\[
x^\top Kx=\|Ax\|^2+x^\top A^2x.
\]

Required runs:

1. At \(L=97\), build the prime-power convolution independently with direct loops. Compare it against the sparse implementation for this candidate and a deterministic control vector. Explicitly check \(1/e\), \(1/\sqrt q\), indexing, normalization and the sign of the \(A^2\) term.
2. Evaluate the candidate at \(L=10^3,10^4,10^5\), with \(\theta=1\). **No eigensolver, no coefficient search.**
3. At each cutoff evaluate the control \(r_L^{(0)}(n)=d_\ell(n)f(v_n)\) at the same \(\ell\), isolating the effect of \(g(v)S_2\).
4. Record \(x^\top x\), \(\|Ax\|^2\), \(x^\top A^2x\), the margin, and candidate-minus-control difference. Keep separate terms so cancellation cannot conceal an error.
5. At the largest completed cutoff, run one sensitivity check with \(\theta=0.98\). It is a different parameter, not a direct comparison with the \(\theta=1\) continuum target.

Here \(\theta=\log L/\log T\). The admissible product cutoff is of the form \(L\le T/(\log T)^2\); \(\theta=1\) is a boundary diagnostic, not a finite admissible choice \(L=T\). Three finite cutoffs cannot prove an asymptotic or disprove transfer. A positive finite margin would not prove a half-gap theorem.

## 5. Turn the computation into a useful mathematical decision

Write a short transfer-obligation table. State the exact estimate or identity needed, its status, and where it is used. At minimum cover:

- weighted prime-factor moments under \(d_\ell(n)^2/n\);
- insertion into an integer already divisible by the inserted prime;
- distinct-prime versus multiplicity conventions;
- coinciding inserted primes;
- cutoff boundaries and uniformity;
- errors beyond the diagonal arithmetic main term.

Classify each item as verified algebra, a precisely applicable sourced theorem, an unproved estimate, or an actual contradiction. Do not invent missing arithmetic mixed entries.

End with one evidence-based recommendation:

- **Keep:** the candidate survives this audit; state the next exact proof obligation.
- **Repair:** identify a concrete error to fix before continuing.
- **Reject this candidate/formula:** exhibit a genuine contradiction or counterexample.
- **Unresolved:** name the precise missing estimate or computational limitation.

“Keep” does not mean breakthrough: the claimed margin is still negative. A corrected normalization, failed transfer assumption, or reliable certificate can nevertheless save Astra substantial work on the main theorem.

## 6. Resource cap and deliverable

Use the existing Python environment. Keep the prescribed local computational batch within roughly 20 minutes; if necessary reduce the largest cutoff and record the limit. Do not expand the search. If certification is expensive, finish exact algebra and arithmetic checks and report the certification gap. If an early error invalidates later stages, stop dependent work.

Create one narrow deliverable directory, following existing repo conventions:

~~~text
research/fable-audits/prime-feature-001/
    audit.py
    results.json
    REPORT.md
~~~

The script must reproduce the independent checks. The JSON must retain source version/hashes, parameters, precision, actual cutoffs, separate quadratic terms, margins, control comparisons, runtime, and proof-status labels.

The report should lead with the recommendation, then give what was established, the transfer-obligation table, the first unresolved step, and one reproduction command. Be concise; do not regenerate the full research history.

Before edits, briefly state concept, minimal implementation, verification, and postponed work; then execute. Run relevant checks and keep the change small. Commit on your branch and open a focused PR in the shared repository if authenticated access is already available. Do not merge or overwrite Astra's work. If publishing is unavailable, preserve the files and report their locations rather than spending this session on authentication.

Return a concise result Astra can act on, with output paths and PR link if available. **Then stop this work packet in the existing session.**


## Receipt update, 2026-09-05

The existing Fable session acknowledged the earlier FABLE_001 task from commit 97df092 and published F2 computation files at Alpha-devbox commit a408e705. Those are being reviewed separately; they do not establish receipt or execution of every item in this newer packet. This update does not issue another task or authorize a new session.
