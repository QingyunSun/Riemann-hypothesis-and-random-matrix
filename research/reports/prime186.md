# Prime-gap 186 audit, a certified minorant refinement, and the next arithmetic target

Research round 1, 2026-09-05. This document records results actually obtained in this run. No bound below 186 is proved. The useful completed work is an exact rational enclosure for the fixed minorant's deficit, an honest propagation of its limited value through the full support-restored criterion, an exactly checked 39-tuple giving a concrete next target 182, and a sharp obstruction to improving one of the elementary debt constants by counting alone.

## 1. The current baseline and what was replayed

The official [PrimeGaps186 repository](https://github.com/openai/PrimeGaps186) was cloned at commit `61340d0b74163003b32756bb16e91d9209a5e330`. Its accompanying paper proves a sufficient sieve criterion for DHL[40,2], then applies a 40-point admissible tuple of diameter 186. The public Lean development is explicitly conditional on three project inputs: two cited Deligne-type estimates and the physical integral bounds. Standard logical axioms are separate. A numerical receipt does not itself discharge those Lean inputs.

The local audit inspected the main paper, the numerical companion, and the exact-input Python certificate. It replayed scalar rational arithmetic from printed endpoints; it did **not** recompute the 149 physical source integrals. This distinction applies to every margin below.

The source-preserving clone is in `prime186-work/PrimeGaps186`. All new experiments are outside that clone.

The central normalized inequality is

$$
\mathcal M(F)=\rho_*\frac{J_{\lambda,H}(F)-L(F)}{I_H(F)}-1>0.
$$

Here the admissible trial is an outer coefficient profile with its actual rootwise support conditions, and $L$ pays for every deleted part. A large cap-only Rayleigh quotient is insufficient. On the published fixed trial, exact scalar replay gives

$$
\rho_*J^-/I^+=1.0002060794024186\ldots,
$$

$$
L^+/I^-=0.000696075110,
\qquad
\rho_*(J^--L^+)/I^+-1
=0.000023360452297044097\ldots.
$$

The scale $\rho_*=2624989/10^7$ means that most of the cap surplus is consumed by support restoration. The remaining margin is about 23 parts per million.

The loss ledger matters more than the count of coefficient parameters:

| Failure class | Published weighted loss, in units $10^{-12}I^-$ | Fraction of total |
|---|---:|---:|
| Outer, effective order 2 | 38,927,522 | 5.5924% |
| Outer, effective order 5/2 | 622,829,241 | 89.4773% |
| Base inner, order 2 | 55,254 | 0.00794% |
| Base inner, order 5/2 | 435,544 | 0.06257% |
| Enlarged inner, order 2 | 1,405,159 | 0.20187% |
| Enlarged inner, order 5/2 | 32,422,390 | 4.65789% |

Thus a substantial improvement should target the outer order-5/2 support geometry and the full constrained operator. It should not spend most of its budget shaving the already tiny base-inner loss.

## 2. Completed exact refinement of the fixed minorant deficit

Write the prime minorant as $\varrho=P-b$, where $b\ge0$ is the explicitly defined five-prime exceptional contribution. Let $\kappa$ be the limiting mean of $b$ in units $x/\log x$. The implemented trial used $\kappa\le2\cdot10^{-5}$. The companion already supplied a smaller coarse rational bound. This round computes a sharper enclosure of the *same* fixed integral; it does not alter the arithmetic minorant or its distribution range.

The independently reproduced enclosure is

$$
\boxed{
\frac{9333886966775225399315932}{10^{30}}
\le\kappa\le
\frac{9334314528491567966021794}{10^{30}}
}
$$

or

$$
9.333886966775226\cdot10^{-6}
\le\kappa\le
9.334314528491569\cdot10^{-6}.
$$

The absolute enclosure width is $4.2756171634\cdot10^{-10}$. The calculation used 16,384 four-dimensional simplices and took approximately 3.88 seconds on this host. Every inequality in the enclosure uses Python integer and rational arithmetic. Floating-point values select the next cell to split, which affects efficiency only.

### 2.1 Why this is a rigorous enclosure

Use $t=481/100000$, eliminate the fifth coordinate by $\sum z_i=0$, and put

$$
\alpha_i=\frac15+t z_i,
\qquad
f(z)=\prod_{i=1}^5\alpha_i^{-1}.
$$

The minorant's two four-dimensional polytopes have the six rational simplex cells recorded in the numerical companion. On their positive domain,

$$
\log f=-\sum_{i=1}^5\log\alpha_i
$$

is convex. Therefore $f$ is convex. For a four-simplex $\Delta$ with vertices $v_0,\ldots,v_4$ and centroid $\bar v$,

$$
|\Delta|f(\bar v)
\le\int_\Delta f(z)\,dz
\le\frac{|\Delta|}{5}\sum_{j=0}^4f(v_j).
$$

The lower inequality is Jensen's inequality. For the upper inequality, convexity bounds the value at a point by its barycentric affine interpolant, whose average is the average of the five vertex values. Multiply by $t^4$, sum over cells, and round each cell contribution outwards to an integer multiple of $10^{-30}$. Longest-edge bisection preserves exact rational vertices and halves the exact volume. This yields reproducible lower and upper bounds without transcendental quadrature or FLINT.

### 2.2 Independent geometry verification

`minorant_geometry.py` verifies the underlying rational geometry, rather than merely assuming that a printed triangulation has no holes:

1. Enumerate all vertices by solving every four-active-halfspace system over the rationals, and reject candidates violating another halfspace. The first polytope has 11 defining halfspaces, the second 10. Both have exactly the seven printed vertices.
2. Check all six four-simplex determinants and volumes exactly.
3. Orient every simplex positively. Every internal tetrahedral face appears twice with opposite orientations; every remaining face lies on a supporting hyperplane of the polytope.
4. Check an explicit strict interior rational point at which the oriented covering multiplicity is exactly one.

The corresponding elementary chain-degree argument proves coverage almost everywhere: an oriented simplex chain whose boundary lies only on the boundary of a convex polytope has constant degree throughout its interior. Here that degree is one. Thus there is neither positive-volume overlap nor a missing positive-volume region. Both geometry audits pass.

The arithmetic identification of the exceptional-prime mean with these polytopes remains the mathematical input from the minorant construction, rather than a new claim proved by the Python code.

### 2.3 Carrying the refinement through the complete margin

A deficit improvement must be propagated through all coefficients, including the error weights. For fixed $\lambda=1/125$ and $K=17/50$, write

$$
m=1-\kappa,quad
 a=m^2-m\lambda,quad
 b=(1-m/\lambda)\kappa K,
\quad c=a+b,\quad d_0=1-c.
$$

The cap form is $J_0+cJ_++bJ_t$. With the refined upper bound for $\kappa$, the coefficients change as follows:

| Quantity | Published allowance | Refined allowance |
|---|---:|---:|
| $a$ | 0.9919601604 | 0.9919814061325887 |
| $b$ | -0.000843183 | -0.0003935309975205265 |
| $c=a+b$ | 0.9911169774 | 0.9915878751350682 |
| $d_0$ | 0.0088830226 | 0.0084121248649319 |

Both cap coefficients improve, because $J_+,J_t\ge0$. The base-inner weight $d_0$ and enlarged-inner weight $1-b$ decrease. However, the positive outer-restoration multiplier on the enlarged shell increases from $c_{old}$ to $c_{new}$. Ignoring that change would be an invalid free gain.

The new outer multiplier is at most $r=c_{new}/c_{old}$ times the old one everywhere. Thus a conservative complete loss bound follows from the old certified component bounds by multiplying the outer loss by $r$, the old-inner loss by $d_{0,new}/d_{0,old}$, and the new-inner loss by $(1-b_{new})/(1-b_{old})$. Even retaining only the old combined cap lower endpoint, the resulting complete margin is at least

$$
0.00002328873833218647\ldots>0.
$$

This does **not** mean the refined trial is worse. It means that the old *combined* numerator endpoint does not reveal how much of the cap form lies in $J_+$ and $J_t$. Without these separate enclosures, an actual improvement cannot be quantified sharply. Keeping the old coefficients remains valid and retains the original $0.00002336045\ldots$ margin.

There is also a rigorous ceiling on the leverage of this one adjustment. On the same fixed trial and same $\lambda$, the published operator bound gives

$$
J_++J_t\le J_{full}\le4I.
$$

Consequently, the cap-quotient gain is bounded above by

$$
4\rho_*\max\{c_{new}-c_{old},b_{new}-b_{old}\}
=0.0004944405498715189\ldots.
$$

Even if every old restoration loss disappeared, the total improvement from this fixed-trial, fixed-$\lambda$ adjustment would be below $0.0006771595$. These bounds describe its scale; they do not prove that a $k=39$ trial lies beyond or within reach. A direct $k=39$ full-form calculation is still required.

The refinement changes no source exponent, no divisor-closed support theorem, and no tuple size. It is a useful exact certificate and a starting input for reoptimization, not a smaller prime-gap theorem.

## 3. A proved obstruction: the coefficient 12/5 is sharp

The elementary majorant $b\le(12/5)N_2$ cannot be improved merely by sharpening its combinatorial case count. Here $N_2$ counts prime pairs whose product is below the specified threshold.

Take five distinct normalized prime exponents

$$
(0.198,0.199,0.200,0.201,0.202).
$$

They sum to one; every pair sum is below $0.40481$, every triple sum is above $0.59519$, and every exponent lies strictly inside the allowed roughness and upper bounds. Exhausting all 120 assignments to the labelled factors gives

$$
b_1=4,\qquad b_2=20,\qquad N_2=10,
\qquad\frac{b_1+b_2}{N_2}=\frac{12}{5}.
$$

All inequalities are strict, so this is an open exponent chamber, not a boundary coincidence. The finite assignment count is independently verified using rational arithmetic in `margin_ledger.py`.

This only closes the route of lowering the *pointwise constant* without changing the majorant. One can still seek a better majorant, retain more of the exact exceptional geometry, or prove a stronger weighted estimate for the balanced five-prime convolution. In particular, the unweighted mean $\kappa\approx9.334\cdot10^{-6}$ cannot automatically replace the weighted exceptional-energy constant $K=0.34$: those are different mathematical quantities.

## 4. A concrete next prime-gap target: DHL[39,2] implies 182

A mixed-integer search produced the following 39-point admissible tuple, and a separate integer residue check validated it:

```
0, 2, 6, 8, 12, 20, 26, 30, 36, 38, 42, 48, 50,
56, 62, 66, 68, 72, 78, 80, 90, 92, 108, 110, 126,
128, 132, 138, 140, 146, 150, 152, 156, 162, 168,
170, 176, 180, 182
```

For each prime $p\le39$, at least one residue class is omitted; for $p>39$ this is automatic from the cardinality. Its diameter is exactly 182. Thus **DHL[39,2] would imply $H_1\le182$**, giving a precise target for the analytic computation.

This tuple is not claimed to be new or optimal. The search also returned a 38-point witness of diameter 176. HiGHS reported infeasibility for 40 points within diameter 184 and for 39 points within diameter 180. Those are numerical solver outcomes, not independently checked infeasibility certificates. An attempted proof-producing Z3 replay consumed approximately 6.7 GB without delivering an inspectable certificate and was terminated; no exact minimal-diameter theorem is claimed from it.

The feasible witnesses are independently checkable and are sufficient for research planning. The old $k=49$ door to 240 is superseded as a main target by the existing 186 result.

## 5. A transferable support principle and a multi-minorant identity

The most valuable structural lesson is to preserve the exact arithmetic support and the pointwise nonnegative detector simultaneously. Rootwise conditions must imply the needed property of the actual least common multiple, including shared prime factors, exhausted roots, and inward cell restrictions. A condition on a generic product of independent roots is not a substitute.

The complementary allocation principle is a useful design language: split a required prime-power charge into nondecreasing contributions assigned to the two roots, with a fixed combined budget. Optimize the allocation as a function of prime size, then charge the actual excluded fragment configurations to the operator. This is stronger than blindly imposing one smoothness cutoff, but it does not abolish the parity or distribution barriers.

There is a clean extension of the residual-square bookkeeping to several minorants, which may be useful when support radius and minorant quality vary. This is an algebraic lemma, not a claim that suitable new arithmetic minorants have already been constructed.

Let $P\ge0$, $b_j\ge0$, $\rho_j=P-b_j$, $A=B_0+D$, and $C=\sum_j C_j$. For arbitrary $\eta_j>0$,

$$
\begin{aligned}
PA^2-&\left[P(2AB_0-B_0^2)+2\sum_j\rho_jDC_j-PC^2
-\sum_j\eta_jb_jD^2-\sum_j\eta_j^{-1}b_jC_j^2\right]\\
&=P(D-C)^2+\sum_jb_j(\sqrt{\eta_j}D+C_j/\sqrt{\eta_j})^2\ge0.
\end{aligned}
$$

Thus the residual loss is explicit and remains nonnegative. If the relevant arithmetic averages are established, the corresponding normalized variational gain is

$$
2\sum_jm_j\langle V-H_0,H_j\rangle
-\left\|\sum_jH_j\right\|^2
-\sum_j\frac{\kappa_j}{\eta_j}\|H_j\|^2
-\sum_j\eta_jK_jE_0.
$$

For mutually disjoint correction shells this separates into scalar optimizations. With different minorant qualities and distribution supports it suggests a richer admissible operator. With identical minorants and identical supports, splitting one correction into several labels provides no automatic benefit: the covariance and residual charges must still be paid. Any proposed gain must prove the needed mixed and self-square distribution estimates on all actual moduli.

This identity is more transferable to the zeta programme than another decimal improvement of $\kappa$: it makes the missing arithmetic information and its squared error cost explicit.

## 6. Reproducibility and the FLINT obstacle

The fresh official certificate was **not** run past startup. Its mandatory signed-convolution test fails in both local wheel environments tried:

- Python-FLINT 0.9.0, FLINT 3.6.0, NumPy 2.5.2;
- Python-FLINT 0.8.0, FLINT 3.3.1, NumPy 2.2.6.

The check was not disabled or replaced. The official upstream correction is identifiable: [FLINT pull request 2790](https://github.com/flintlib/flint/pull/2790), specifically commit `7ad753d51c82fdec115cb179b41d0e581f1cb0ec`. A source checkout of v3.6.0 at `8d5454b96761fafe4d5a9da76a369a602f500f49` was prepared. A patched build was not completed before the research priority was redirected to the zeta arithmetic barrier. Neither wheel failure is evidence against the mathematical theorem; it is a reproducibility requirement explicitly anticipated by its authors.

The new rational computations need none of these libraries. Run, from `prime186-work`:

```bash
python3 minorant_geometry.py
python3 minorant_mass.py
python3 margin_ledger.py
```

`tuple_search.py` additionally requires SciPy; only the search uses floating-point optimization, and every accepted tuple is checked with integer arithmetic.

Files suitable for a small research commit are:

- `prime186.md`: this report;
- `minorant_mass.py` and `.json`: exact convexity enclosure;
- `minorant_geometry.py` and `.json`: exact polytope/triangulation verification;
- `margin_ledger.py` and `.json`: full scalar margin, coefficient leverage bound, and sharp $12/5$ count;
- `tuple_search.py`, `tuple_search.json`, and `tuple_search_more.json`: feasible witnesses and explicitly limited solver results.

Do not commit cloned upstream sources, virtual environments, or the unfinished proof-producing SMT run as if they were new mathematical results.

## 7. Next action and stopping discipline

The next substantial prime-lane computation would be a correctly linked full baseline, separate enclosures for $J_0,J_+,J_t$, and a direct $k=39$ variational search that includes the dominant outer support failure. A cap-only success must not be reported as a prime-gap improvement.

Following the user's strengthened priority on a major zeta/random-matrix theorem, this round stops refining the auxiliary minorant integral. Its exact certificate is saved and can be reused. The transferable lessons are the support-preserving allocation structure, the positive residual identity, and the insistence on a complete cost ledger. These are useful when testing whether a new arithmetic zero statistic actually escapes the known ACUE mimickers.
