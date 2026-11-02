# Exact projection restoration, positive norm credit, and the limits of the published ledger

2026-09-05. Independent proof/audit task, confined to Proposition 4.6 of the prime-gap-186 paper and the structural frontier identified in round three. No official physical-integral computation was rerun, no Claude session was started, and no repository source was edited.

Primary source: [Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), §§4.3–4.6, especially Proposition 4.6, displayed equations (4.30)–(4.43). Numerical source: the [official certificate repository](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330), Numerical certificate for prime gaps at most 186, Proposition 1.3 and Tables 2.1–2.7. Locally read files and exact scalar replay are recorded in restoration_checks.py/json/log.

The formulas below are consequences of the source's Hilbert-space setup. They are not a claim that the needed new physical integrals have been evaluated, nor a claim of priority for elementary projection identities.

## 1. Findings

There is a completely exact restoration identity that avoids Young debts:

$$
\mathcal Q(PF)=\mathcal Q(F)+\alpha+
\rho\sum_i\int m_i\bigl(|W_i|^2-2\operatorname{Re}(\overline{W_i}V_i)\bigr),
\tag{1.1}
$$

where \(\mathcal Q(F)=\rho\langle F,BF\rangle-\|F\|^2\), \(P=1_O\), \(e=(1-P)F\), \(\alpha=\|e\|^2\), \(V_i=E_iF\), and \(W_i=E_ie\). Computing or bounding the actual removed marginals \(W_i\) is the direct route to a stronger restoration calculation.

Three useful rigorous lower bounds follow:

1. Keep the paper's Young upper bound and restore a separately certified lower bound for \(\alpha\).
2. Integrate a signed root residual on the true failure set. A pointwise completion of the square yields a new upper-cost target \(\int_{H_O\setminus O}|BF|^2\), which retains cancellation between face terms.
3. Use sharp pointwise quadratic bounds for \(W_i\), including its squared term, rather than discarding all positive face squares.

The old/new inner-domain overlap also gives an exact positive correction. The published constants cap its normalized margin benefit at \(7.8813\times10^{-8}\), so that particular overlap recovery is small for the published \(k=40\) trial.

The 52 outer root-square ledger entries imply

$$
0\le \frac{\alpha}{I_H}\le0.019361160920,
\qquad
0\le \frac{(1-4\rho|b_h|)\alpha}{I_H}\le0.019344019740.
\tag{1.2}
$$

These are upper bounds on possible credit, not positive lower bounds. The published upper ledger alone supplies no guaranteed new credit. They are also deliberately loose, and do not establish whether a \(k=39\) trial can succeed.

## 2. Setup and the exact signs

Work in the source's Hilbert space \(L^2(H_O,\nu^k)\), extending profiles by zero. Let

$$
U=H_O\setminus O,\quad P=1_O,\quad e=1_UF,\quad f=PF=F-e.
$$

Since \(P\) is an orthogonal multiplication projection,

$$
\langle f,e\rangle=0,\qquad
\|f\|^2=I_H-\alpha,\qquad
\alpha=\int_U|F|^2.
\tag{2.1}
$$

The actual face operator is

$$
B=\sum_i E_i^*m_iE_i,\qquad
m_i=d_0\,1_{L_0}+a_h\,1_{L_1}+b_h.
\tag{2.2}
$$

Put \(b=|b_h|=-b_h>0\). Its three values are

$$
m_i=
\begin{cases}
1,&Y\in L_0,\\
a_h-b,&Y\in L_1\setminus L_0,\\
-b,&Y\notin L_1.
\end{cases}
\tag{2.3}
$$

The first two are positive for the published constants. The source proves

$$
-bC_{\rm op}I\le B\le C_{\rm op}I,\qquad C_{\rm op}=4.
\tag{2.4}
$$

It also defines \(A\) using the larger cap domains, \(D=A-B\ge0\), and

$$
J_{\lambda,H}=\langle F,AF\rangle,\qquad
\beta=\langle F,DF\rangle,\qquad
\langle F,BF\rangle=J_{\lambda,H}-\beta.
\tag{2.5}
$$

Thus \(\mathcal Q(F)\) in (1.1) uses the actual \(B\) but the unprojected \(F\). It is not the cap form \(\rho J_{\lambda,H}-I_H\).

Expanding \(f=F-e\) gives, with no estimate,

$$
\mathcal Q(f)
=\rho(J_{\lambda,H}-\beta)-I_H+
\alpha-2\rho\operatorname{Re}\langle e,BF\rangle
+\rho\langle e,Be\rangle.
\tag{2.6}
$$

Applying the adjoint relation to the last two terms gives (1.1).

All face products in these equations are products of conditional integrals. In particular,

$$
|W_i(Y)|^2
=\iint e(Y\oplus_iX)\overline{e(Y\oplus_iX')}\,d\nu(X)d\nu(X').
\tag{2.7}
$$

The two integrated coordinates are independent copies conditional on the same retained configuration \(Y\). Replacing this expression with \(E_i(|e|^2)\) is incorrect.

No positivity of \(F\) is assumed. The research record explicitly notes sign changes of the optimized polynomial. In the signed hybrid form, replacing \(F\) by \(|F|\) is not automatically monotone because \(b_h<0\).

## 3. Positive-alpha credit: what is sufficient and what is not

The source's spectral lower bound gives

$$
\langle e,Be\rangle\ge-bC_{\rm op}\alpha.
$$

Define

$$
c_\alpha=1-\rho bC_{\rm op}>0.
\tag{3.1}
$$

If \(E_O\) is any valid upper bound for \(2\operatorname{Re}\langle e,BF\rangle\), then

$$
\mathcal Q(PF)\ge
\rho(J_{\lambda,H}-\beta-E_O)-I_H+c_\alpha\alpha.
\tag{3.2}
$$

Consequently, for outward bounds and a **separately proved lower bound** \(\alpha^-\le\alpha\), the strengthened sufficient criterion is

$$
\rho\bigl(J^-_{\lambda,H}-E_O^+-\beta^+\bigr)-I_H^+
+c_\alpha\alpha^->0.
\tag{3.3}
$$

The alpha term is not multiplied by another \(\rho\). It already comes from the denominator restoration \(\|PF\|^2=I_H-\alpha\), together with the small negative spectral correction.

### 3.1 Disjoint sufficient-failure regions

If \(A_1,\ldots,A_r\subset U\) are pairwise disjoint up to null sets, then

$$
\alpha\ge\sum_{\ell=1}^r\int_{A_\ell}|F|^2.
\tag{3.4}
$$

Certified lower integral enclosures on these sets can be added. The inclusion \(A_\ell\subset U\) must use the **actual complete outer-domain predicate**, including activations, row membership, radial cells, and fragment caps.

A practical construction is an inward fragment region on which one actual outer support inequality fails by a strict rational margin. Order the witness coordinates or assign the first failing row and the largest relevant fragment to half-open intervals, so the selected regions are disjoint. A lower integral requires a lower probability or a two-sided enclosure of that region. A Chernoff upper bound is not a lower probability.

More generally, nonnegative weights \(w_\ell(X)\) may be used if

$$
\sum_\ell w_\ell(X)\le1_U(X)\quad\text{a.e.}
$$

Then \(\alpha\ge\sum_\ell\int w_\ell|F|^2\). This is the appropriate partition-of-unity direction for credit.

### 3.2 Existing overlapping positive covers

The paper uses nonnegative majorants \(M_j\) with

$$
1_U\le\sum_jM_j.
\tag{3.5}
$$

The inequality is in the opposite direction. It produces upper bounds on nonnegative integrals over \(U\); it does not prove any of the \(M_j\) is supported in \(U\), or any positive lower bound on \(\alpha\).

Even if every cover set happened to lie in \(U\), adding their masses would overcount intersections. Two identical sets of mass one give a sum two and a union mass one. Remedies are disjointification, a proved multiplicity bound, Bonferroni lower bounds with correctly directed intersection enclosures, or nonnegative credit weights summing at most one.

The current Palm–Chernoff and factorial majorants can be positive outside the failure event and can exceed one. They therefore cannot simply be normalized or relabeled as disjoint lower-mass contributions.

For signed residual integrands, the restriction is stronger: multiplying by an upper event cover preserves inequalities only for a nonnegative integrand. Its positive and negative parts must be treated separately.

## 4. Signed root restoration and an optimized quadratic bound

Let

$$
G(X)=(BF)(X)=\sum_i m_i(\widehat X_i)V_i(\widehat X_i).
\tag{4.1}
$$

The adjoint formula is understood on \(H_O\), with zero extension. From (2.6) and (2.4),

$$
\mathcal Q(PF)\ge\mathcal Q(F)+
\int_U r(X)\,d\nu^k(X),
\qquad
r=c_\alpha|F|^2-2\rho\operatorname{Re}(\overline F G).
\tag{4.2}
$$

This is sharper in its treatment of the mixed term than replacing every \(m_iF V_i\) by \(h_i|F V_i|\) and applying Young separately. It retains cancellation across faces and the sign of the summed mixed term.

Completing the square pointwise gives

$$
r=c_\alpha\left|F-\frac{\rho}{c_\alpha}G\right|^2
-\frac{\rho^2}{c_\alpha}|G|^2,
$$

and hence

$$
\boxed{\quad
\mathcal Q(PF)\ge
\rho(J_{\lambda,H}-\beta)-I_H
-\frac{\rho^2}{c_\alpha}\int_U|BF|^2.
\quad}
\tag{4.3}
$$

This is an optimized quadratic bound in which the favorable denominator loss pays for part of the mixed term. It is optimal pointwise if only \(G\) is retained and \(F\) is otherwise unrestricted. It is not claimed to dominate the paper's optimized componentwise Young estimate for every trial.

### 4.1 Partial exact integration

If \(A\subset U\) is a known-failure region and \(1_{U\setminus A}\le\sum_jM_j\), then

$$
\int_Ur\ge\int_Ar-\sum_j\int M_jr_-,
\qquad r_-=\max(-r,0).
\tag{4.4}
$$

Thus one can retain signed residual on a certified region and upper-bound only the harmful residual on the remainder. The old positive-cover machinery can act on \(r_-\), provided its new weighted physical integrals are actually enclosed.

One must not add the right sides of different lower bounds such as (3.2) and (4.3). They are alternative estimates of the same correction; taking their maximum is valid, adding their claimed gains is generally double counting.

### 4.2 If only an alpha interval and a residual Gram upper bound are known

Suppose \(\alpha\in[a_-,a_+]\) and

$$
\int_U|G|^2\le K.
$$

Cauchy–Schwarz gives a rigorous correction

$$
\mathcal Q(PF)-\mathcal Q(F)
\ge\min_{a\in[a_-,a_+]}\bigl(c_\alpha a-2\rho\sqrt{aK}\bigr).
\tag{4.5}
$$

The minimizing \(\sqrt a\) is the projection of \(\rho\sqrt K/c_\alpha\) onto \([\sqrt{a_-},\sqrt{a_+}]\). Substituting a lower bound for \(\alpha\) directly into the negative square-root term is not valid: the correction need not be increasing in \(\alpha\) on the whole interval.

## 5. Retain the removed face squares

For each face let

$$
a_i(Y)=\int1_U(Y\oplus_iX)\,d\nu(X),\quad
z_i(Y)=\int1_U(Y\oplus_iX)|F(Y\oplus_iX)|^2\,d\nu(X).
$$

Then \(|W_i|^2\le a_i z_i\). Put \(R_i=\sqrt{a_i z_i}\) and \(m_i^\pm=\max(\pm m_i,0)\). Minimizing the exact quadratic term over the disk \(|W_i|\le R_i\) yields

$$
m_i\bigl(|W_i|^2-2\operatorname{Re}(\overline W_iV_i)\bigr)
\ge
-m_i^+\left[|V_i|^2-(|V_i|-R_i)_+^2\right]
-m_i^-\left[R_i^2+2R_i|V_i|\right].
\tag{5.1}
$$

For \(m_i\ge0\), write the quadratic as
\(m_i(|W_i-V_i|^2-|V_i|^2)\) and take the closest point in the disk to \(V_i\). For \(m_i<0\), take the farthest point; its distance is \(|V_i|+R_i\). This proves both signs and shows the bound is optimal under that single disk constraint.

Integrating (5.1) and adding \(\alpha\) in (1.1) gives a valid lower restoration bound. In contrast to Proposition 4.6's final estimate, it retains favorable curvature of the positive-face square. But it requires certified functions \(a_i,z_i,V_i\), not just global masses.

For real \(F\), an interval enclosure \(W_i\in[\ell_i,u_i]\) can be better. On a positive face, minimize at the point of \([\ell_i,u_i]\) closest to \(V_i\); on a negative face, minimize at an endpoint farthest from \(V_i\). If the actual \(W_i\) is computed, (1.1) is exact and no auxiliary Young parameter is needed.

For a fixed finite trial basis \(\phi_a\) and fixed support, the most direct optimization object is the exact compressed matrix

$$
M_{ab}
=\rho\sum_i\int m_i E_i(P\phi_a)\overline{E_i(P\phi_b)}
-\int P\phi_a\overline{\phi_b}.
\tag{5.2}
$$

A rational vector \(v\) with \(v^*Mv>0\), certified using outward enclosures and the source hypotheses, would establish the sieve criterion for that trial. The computational obstacle is the physical projection integral; writing the matrix does not evaluate it.

The source projection does not commute with \(E_i\). Replacing \(E_i(PF)\) by a face indicator times \(E_iF\) would discard exactly the difficult dependence on the erased coordinate.

## 6. Exact old/new inner-overlap credit

Retain the paper's order of operations: inner deletion is evaluated at the unprojected \(F\), then the outer projection is restored. On a face write

$$
A_i=H_0\setminus L_{\rm old},\qquad
C_i=H_1\setminus L_1.
$$

Because \(L_0=L_{\rm old}\cap L_1\) on the base domain and \(H_0\subset H_1\),

$$
H_0\setminus L_0=A_i\cup(C_i\cap H_0).
$$

The exact inner loss is therefore

$$
\beta=d_0\beta_{\rm old}+(1-b_h)\beta_{\rm new}
-d_0\Gamma_{\rm in},
\tag{6.1}
$$

where

$$
\Gamma_{\rm in}
=\sum_i\int_{(C_i\setminus H_0)\,\sqcup\,(A_i\cap C_i)}
|V_i|^2.
\tag{6.2}
$$

The displayed union is disjoint and lies inside \(C_i\), so

$$
0\le\Gamma_{\rm in}\le\beta_{\rm new}.
\tag{6.3}
$$

This simultaneously accounts for the unnecessary \(d_0\) charge on new failures outside the base and the duplicated \(d_0\) charge where old and new failures overlap inside the base.

To use it as a positive credit, one needs a lower bound for the true integral in (6.2). Intersections of the existing upper majorants are not lower bounds for intersections of the true failure events.

If the exact projected matrix (5.2) is used instead, this inner correction is already built in. It must not be added again.

## 7. Exact replay of what the published numerical upper ledger can say

The script reads the 52 outer rows of numerical Tables 2.1 and 2.2, checks every rational Young rounding inequality, and sums the printed integers using exact fractions. It does not import the official numerical certificate. Its conclusions remain conditional on the correctness of the published physical upper bounds.

For the common normalization used in the numerical paper, set

$$
\rho=\frac{2624989}{10^7},\quad
b=\frac{843183}{10^9},\quad
d_0=\frac{44415113}{5\cdot10^9},\quad
c_\alpha=\frac{2497786653900013}{2500000000000000}.
$$

Thus \(c_\alpha=0.9991146615600052\).

### 7.1 Upper cap on possible alpha credit

Writing \(R_j,V_j\) for the published outer root-square and outer face-square upper forms, the table sums give

$$
\frac{\sum_jR_j}{I_H^-}\le0.000653000069917512,
$$

$$
\frac{\sum_jV_j}{I_H^-}\le0.000168396875617848,
$$

$$
\frac{E_O}{I_H^-}\le0.000661756763.
\tag{7.1}
$$

The first form majorizes \(\sum_i\int_Uh_i(\widehat X_i)|F(X)|^2\,d\nu^k\). Every \(h_i\ge b\), so

$$
kb\,\alpha\le\sum_jR_j.
$$

Since \(I_H^-\le I_H\), at \(k=40\),

$$
\frac{\alpha}{I_H}
\le\frac{0.000653000069917512}{40b}
=\frac{9069445415521}{468435000000000}
=0.0193611609199163\ldots.
\tag{7.2}
$$

Multiplying by \(c_\alpha\) gives the credit cap in (1.2). The guaranteed lower bound remains zero. In particular, it is invalid to insert \(0.01936\) as the recovered mass: it is an upper ceiling obtained from overlapping majorants and a very small universal weight \(40b\).

This does not prove the actual credit is close to that ceiling, nor that a redesigned \(k=39\) profile has the same ceiling.

### 7.2 The exact inner-overlap improvement is tightly bounded

The published two new-inner weighted groups sum to

$$
\frac{(1+b)\beta_{\rm new}}{I_H}
\le\frac{1405159+32422390}{10^{12}}
=0.000033827549.
$$

Using (6.3), the normalized sieve-margin benefit from correcting only the duplicated \(d_0\) charge is at most

$$
\frac{\rho d_0\Gamma_{\rm in}}{I_H}
\le
\frac{\rho d_0}{1+b}\,0.000033827549
=7.88120730556\ldots\times10^{-8}.
\tag{7.3}
$$

This is an absolute cap for that specific correction and the published \(k=40\) profile. It does not cap all possible changes to the inner support or trial.

### 7.3 Completion of the square needs real cancellation to beat the old debt

Let \(H(X)=\sum_i h_i(\widehat X_i)\le k\). Weighted Cauchy–Schwarz gives

$$
|BF(X)|^2
\le H(X)\sum_i h_i(\widehat X_i)|V_i(\widehat X_i)|^2.
$$

The positive cover then yields the crude bound

$$
\int_U|BF|^2\le k\sum_jV_j.
\tag{7.4}
$$

For the published ledger, plugging this into (4.3) produces a normalized outer debt no larger than

$$
\frac{\rho^2k}{c_\alpha}\,0.000168396875617848
=0.000464551283571\ldots.
$$

That certified upper debt is **worse** than the published Young debt

$$
\rho\,0.000661756763
=0.000173710422355\ldots.
$$

Thus the generic completed-square inequality is not by itself an improvement. It requires a stronger bound on the actual signed sum \(BF\), or smaller effective \(H\) on failures.

Measured against the same published face ledger, a sufficient comparison target is

$$
\frac{\int_U|BF|^2/I_H^-}
{0.000168396875617848}
<14.957265516079\ldots,
\tag{7.5}
$$

instead of the crude factor \(k=40\). This is a concrete target for a new physical integral, not evidence that it holds. The quotient merely compares two certified upper-bound schemes; a larger ratio would not establish that the actual restoration fails.

## 8. Verification and unresolved proof obligation

The accompanying script performs exact fraction arithmetic on all 52 published outer table rows and their rounded Young costs. It also tests the exact projection identity, exact inner-overlap identity, signed root bound, completed-square bound, and optimal disk bound on 200 independent signed examples on a \(3\times3\times3\) product space with nested cap and actual face domains. The largest floating identity discrepancy was below \(4.5\times10^{-16}\). These finite tests are diagnostics; the arguments in §§2–6 supply the proofs.

Files:

- RESTORATION_PROOF_AUDIT.md — this derivation and audit;
- restoration_checks.py — exact ledger replay and finite-product diagnostics;
- restoration_checks.json — extracted 52 rows, exact fractions, numerical summaries;
- restoration_checks.log — complete run output.

The shortest substantive next obligation is now explicit: evaluate a certified lower mass on **true sufficient-failure regions**, or a certified signed residual/removed-marginal form for the actual source projection. Existing upper error ledgers cannot supply that lower mass. A successful new calculation must preserve independent erased-coordinate copies, retain the negative full-face term, and use one consistent restoration identity without adding the same credit twice.

No new \(k=39\) physical integral, restored positive margin, or prime-gap theorem is established by this audit.
