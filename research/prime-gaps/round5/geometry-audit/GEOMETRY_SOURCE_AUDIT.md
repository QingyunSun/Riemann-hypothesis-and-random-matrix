# Exact source geometry for the bounded radius and plateau screen

This audit establishes a sufficient source and cap template for the round-five $k=39$ screen. It evaluates no sieve integrals and proves no smaller prime gap. The accompanying exact arithmetic checks cover physical outer radii $0.272$, $0.2742997$, $0.275$, $0.276$, and $0.278$, together with three specified plateau choices at each radius. The original source's numerical failure schedule and its 97 component bounds are **not inherited**.

The main findings are concrete. The distribution ladders themselves stay fixed, but the retained rows change after the physical grid is changed. A single inward outer index layer removes the problematic extra row. The old inner-square source fails at the smallest radius; a common replacement works throughout the screen. The exceptional-square constant and hybrid coefficients must be recomputed when the outer radius exceeds $0.275$.

## 1. Parameters and what really remains invariant

Retain the exact source constants

$$
\rho=0.262499,\qquad \rho_*=0.2624989,\qquad
 e=10^{-7}/\rho,\qquad h=S/98304,
$$

and write $r=\rho_*S$. The proposed search fixes

$$
S+T_0=\Sigma_0=1.997,
\qquad
\rho_*(S+T_1)=0.5252997.
$$

Thus $T_\nu=\Sigma_\nu-S$, where $\Sigma_1=0.5252997/\rho_*$. In particular $T_1>T_0$ throughout the screen, and their difference is constant.

The official ladder recurrence depends on $S,T_\nu$ through $E_\nu=\rho(S+T_\nu)-1/2$. Consequently **every** $\omega_{\nu,t},\delta_{\nu,t},B_{\nu,t},B^+_{\nu,t},\xi_{\nu,t}$ is unchanged. The exact script regenerates all 29 old and 43 new rows and verifies this invariance, rather than copying a rounded table.

The root-specific quantities change:

$$
a_{\nu,t}=B_{\nu,t}-T_\nu,
\qquad b_{\nu,t}=B_{\nu,t}-S.
$$

On every retained nonterminal row the recurrence gives

$$
(A,C_\nu)=
\begin{cases}
(S+e,T_\nu+e),&\text{orders 1 and 2},\\
(S+e/2,T_\nu+e/2),&\text{order 3}.
\end{cases}
$$

The exact script verifies the prime distribution inequalities of Corollary 2.19 and all minorant inequalities of Proposition 2.22. Their strict margins remain positive. Lower-order transfer requires $S-T_\nu+e\geq0$ and $\min(2S-T_\nu,2T_\nu-S)+e\geq0$, which hold here. In order three, $A+C=B+\xi$ and $\eta_D=\eta_E=\xi-e/2>0$. These are the actual combined-divisor hypotheses; a scalar modulus level alone is insufficient.

## 2. Valid plateau intervals and all largest-fragment constraints

For each ladder choose $L_\nu$ and use

$$
\phi_D(t)=\min(3t/2,L_\nu),\qquad
\phi_E(t)=3t-\phi_D(t).
$$

Both functions are nonnegative and nondecreasing, and their sum is $3t$. In the natural plateau branch used by this screen, set

$$
u_\nu=A-L_\nu,\qquad v_\nu=(C_\nu+L_\nu)/4.
$$

Here $u_\nu$ is the outer largest-fragment cap and $v_\nu$ the inner cap. The complete checks at a largest activated fragment are

$$
u+\phi_D(u)\leq A,\quad\phi_E(u)\leq C,
\qquad v+\phi_E(v)\leq C,\quad\phi_D(v)\leq A.
$$

They include both opposite-root conditions. Requiring both endpoints to lie on their plateau branches gives, in our regime $A>C>0$,

$$
\boxed{\frac{3A-C}{4}\leq L\leq\frac{3C}{5}.}
$$

The lower bound is the outer opposite-root constraint $3(A-L)-L\leq C$. The upper bound makes $v\geq2L/3$; it also implies the required outer-branch bound. The interval exists precisely when $A/C\leq17/15$ within this branch.

The balanced nonlargest-witness reduction in numerical Lemma 1.4 additionally needs

$$
\max(A,C)\leq7L/3.
$$

This was checked explicitly. It already follows from the lower endpoint here: $(3A-C)/4\geq3A/7$ since $A>C$. Below $2L/3$, both allocations equal $3t/2$; above it a nonlargest witness has inclusive tail at least $2t$, so both nonlinear obstructions and the balanced one exceed $7L/3$. This reproduces the actual reduction to nonlargest $H_{5/2}$ failures.

The intervals for $q_\nu=L_\nu/C_\nu$ are:

| Physical outer radius | Old $q_{\min}$ | New $q_{\min}$ | Upper endpoint |
|---|---:|---:|---:|
| 0.272 | 0.5588487836871093 | 0.5553700704402632 | 0.6 |
| 0.2742997 | 0.5731934484723361 | 0.5696206036612396 | 0.6 |
| 0.275 | 0.5776142414184422 | 0.5740121594208600 | 0.6 |
| 0.276 | 0.5839701980513703 | 0.5803258928258113 | 0.6 |
| 0.278 | 0.5968370022033588 | 0.5931065437793680 | 0.6 |

The exact fractions are in the JSON; decimal table entries are displays, not substitutes for endpoint tests. The original common fraction $q=23/40$ fails this natural cap template at 0.275, 0.276, and 0.278. In particular, the old opposite-root inequality still fails at the shared minimum outer cap for that unchanged choice.

The old-ladder upper radius for this branch is

$$
r\leq\frac{17\rho_*\Sigma_0+\rho_*e}{32}
=0.2784867267531238\ldots;
$$

the new-ladder bound is $0.2790654687499988\ldots$. These bound this cap parameterization, not every possible sieve support. Outside this interval one could choose smaller piecewise caps, a different allocation, or pay for additional largest-fragment failures; none is certified by the present template.

For completeness, the unrestricted largest-fragment inverse constraints can be computed piecewise. The outer owner inverse is $2A/5$ if $A\leq5L/3$, otherwise $A-L$; its opposite inverse is $2C/3$ if $C\leq L$, otherwise $(C+L)/3$. Take their minimum. The inner owner inverse is $2C/5$ if $C\leq5L/3$, otherwise $(C+L)/4$; intersect it with $t\leq2A/3$ when $L>A$. This explains precisely what ceases to hold when the simple endpoint formulas are used outside their range.

## 3. Shared supports, nested faces, and inward caps

The usable outer domain retains **both** source ladders. For a root of total $s$, each row has its original safe-core alternative $s\leq a_{\nu,t}$ and, outside it, its full owner-tail and opposite-root predicates. The inner base requires both old and new inner predicates:

$$
O=H_O\cap\bigcap O_{\nu,t},\qquad
L_1=H_1\cap L_{\rm new},\qquad
L_0=H_0\cap L_{\rm old}\cap L_{\rm new}.
$$

The exact script constructs each cap envelope as the running minimum of every applicable row cap, starting with the global cap $\zeta=0.19037/\rho$. The radius where a row becomes active is its own $a_{\nu,t}$ or $b_{\nu,t}$. It does not assume that the original three-shell comparator continues to hold after independent plateau changes.

For independent $L_0,L_1$, the final inner caps must satisfy $C_0+L_0\leq C_1+L_1$ to preserve their simple nesting. Otherwise clip the base cap to the enlarged cap on each overlapping radial interval. The implemented base envelope takes the running minimum of the old and new inner cap constraints, so $H_0\subseteq H_1$ holds cell by cell. This largest-fragment clipping does not replace the full inner tail predicates in $L_0$.

The two common-height choices used by the bounded screen,

$$
L_0=L_1=(3A-C_0)/4\quad\text{or}\quad L_0=L_1=3C_0/5,
$$

satisfy both ladders' intervals and nested caps automatically. At the common minimum, the physical caps $\rho_*u$, $\rho_*v_0$, and $\rho_*v_1$ are constant as $r$ varies under the fixed-sum constraints. The source activation radii still move. Thus this is a redistribution of radial room, not a simultaneous increase of all prime-factor allowances.

For a $d$-coordinate radial shell $(l,u]$, retain index sums

$$
\max(0,\lfloor l/h\rfloor-d+1)\leq j\leq
\min(n-1,\lfloor u/h\rfloor-d),\qquad n=98304-k,
$$

and round each fragment cap down to $h\lfloor z/h\rfloor$. Using the full upper cell endpoint is what safely handles a cell crossing an activation core. The output records all resulting cells and verifies nesting directly. The global physical cap remains $\rho_*\zeta<0.19037<\xi_*$, including inside radial cores, so the roughness restriction used in the exact-face identity is preserved.

## 4. The extra row 39 and the one-layer repair

With the untrimmed outer mask, its largest total is $98303h$; the enlarged inner largest total is $J_1h$, where $J_1=\lfloor T_1/h\rfloor$. Retain a row precisely when $B_{\nu,t}$ is strictly below the corresponding actual combined upper bound. The exact results are:

| Radius | Untrimmed new retained rows | Outer layers to trim |
|---|---|---:|
| 0.272 | 0 through 39 | 1 |
| 0.2742997 | 0 through 38 | 0 |
| 0.275 | 0 through 39 | 1 |
| 0.276 | 0 through 39 | 1 |
| 0.278 | 0 through 39 | 1 |

The old retained rows remain 0 through 27. The new extra row has

$$
\xi_{n,39}=1.886625042412619\ldots\cdot10^{-5},
$$

only 1.75–1.79 cells at these meshes. It violates the old numerical prerequisite $\xi>2h$ and the implementation's first-bin assertion. The analytic source remains valid because $\xi>0$; the breakdown concerns reuse of that numerical cover.

A rigorous inexpensive repair is

$$
J_O=\min\{98303,\lfloor B_{n,39}/h\rfloor-J_1\},
\qquad
\sum_i j_i\leq J_O-k.
$$

Then $(J_O+J_1)h\leq B_{n,39}$, so row 39 is unnecessary. At $k=39$, the trimmed outer index maximum is 98263; the untrimmed maximum is 98264. Keep $h$, $n$, the normalizer $Z$, and nominal $S$ fixed; trim the outer radial mask and derive every erased face from that changed $F$.

This repair is uniform for the whole radius interval $[0.272,0.278]$, not merely the five sampled points. Writing $\Delta=\Sigma_1-B_{n,39}$, the exact script verifies

$$
h_{\max}<\Delta<2h_{\min},\quad
B_{n,39}-B_{n,38}>h_{\max},\quad
\xi_{n,38}>2h_{\max}.
$$

Thus at most one layer is removed, row 38 remains active, and its two-cell guard holds. Separate exact inequalities keep old row 27 active and old row 28 excluded. Merely increasing grid resolution is not an automatic repair: the larger actual endpoint can activate still later rows.

## 5. Common inner-square source and the exceptional constant

The original inner-square level $0.5062$ is insufficient at $r=0.272$, where $2\rho_*T_1=0.5065994$. Use instead

$$
\omega_s=0.0035,\qquad\delta_s=0.025,
\qquad 1/2+2\omega_s=0.507.
$$

The prime order-two criterion has margin $3-280\omega_s-80\delta_s=0.02$; the fixed-$\sigma_0$ bilinear margin is $0.003996$. Every minorant inequality is also checked exactly. Put

$$
B_{\rm BV}=1/(2\rho),\quad c_s=B_{\rm BV}-T_1,\quad \xi_s=\delta_s/\rho.
$$

The retained new row 12 implies the required inner-square predicate because $c_s\geq b_{n,12}$ and $\xi_s\geq\xi_{n,12}$. The minimum core containment margin on this interval is greater than $0.02539$; the activation margin is greater than $0.04470$. The common source level exceeds every actual inner-square radius by at least $0.0004006$. The retreat $\rho_*<\rho$ retains room for the presieving modulus.

The exceptional-square proof also depends on the maximum radius of **all** coefficient roots, including exact faces. Here it is safe to use $r_c=r$. Repeating the original 1024-bin rational upper sum gives:

| $r_c$ | Safe upward six-decimal $K_{\rm ex}$ |
|---|---:|
| 0.272 | 0.301405 |
| 0.2742997 | 0.327323 |
| 0.275 | 0.336134 |
| 0.276 | 0.349580 |
| 0.278 | 0.380026 |

The script reproduces the paper's exact $r_c=0.275$ endpoint before evaluating the new radii. The separate independent proof is in `../exceptional-radius/EXCEPTIONAL_RADIUS_EXTENSION.md`. It confirms positive auxiliary cutoffs below the global cap and the unchanged counting margin $1/5000$. It also proves that this finite-bin mechanism already exceeds 0.34 at radius 0.276; that is not a universal lower bound on the best possible exceptional-square constant.

With the unchanged minorant mass and $\lambda=1/125$, recompute

$$
a_h=m^2-m\lambda,\qquad
b_h=(1-m/\lambda)(1-m)K_{\rm ex},\qquad d_0=1-a_h-b_h.
$$

Every screened radius retains $-10^{-3}<b_h<0$, $0<a_h+b_h<1$, and $d_0>0$ with the displayed safe constants. The script records these updated coefficients. Keeping the old $K=0.34$ beyond the old radius hypothesis is not justified by that proposition.

Finally, $C_{\rm op}=4$ remains valid at $k=39$: an exact finite exponential sum proves $\log39<3.664$, and

$$
\frac{39S\log39}{38}<\frac{39S\cdot3.664}{38}\leq3.982482<4.
$$

This rechecks the operator bound rather than importing the original $k=40$ estimate at changed $S$.

## 6. What remains before a sieve certificate

The exact script examined 15 radius/plateau cases in about two seconds. Twelve satisfy the natural cap template; the unchanged $q=23/40$ choices at 0.275, 0.276, and 0.278 are explicitly rejected. For the accepted cases it verifies ladder invariance, strict analytic source inequalities, natural plateau conditions, opposite-root caps, cap nesting, actual combined-modulus bands, the one-layer repair, common inner-square coverage, and the updated hybrid signs. `geometry_feasibility.json` stores exact fractions and regenerated cell masks; `geometry_feasibility.log` records the run.

No original integral bound survives merely because these hypotheses pass. The next obligation is to regenerate the nonnegative failure cover from the new thresholds, core boundaries, rounded caps, and originating rows, including low-witness clipping and same-coordinate contributions. Then evaluate the changed cap and restoration forms with outward arithmetic. The original 97-component numerical values and frozen Young parameters are not a ready-made certificate for a new point. Keeping positive old Young parameters is algebraically possible, but their new costs require fresh integrals and their previous optimality is not inherited.

No further geometry scan is part of this audit. The adjacent numerical agent's candidate screening remains a cap-only experiment until those restored forms are available. A negative candidate quotient does not prove a global sieve obstruction, and a positive cap quotient alone would not prove a smaller prime gap.

Run `python3 geometry_feasibility.py` to reproduce the certificate. The sources are the [official main proof](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), especially Propositions 3.11, 4.2, 4.6 and Lemma 4.3, and the [numerical companion](https://github.com/openai/PrimeGaps186/blob/61340d0b74163003b32756bb16e91d9209a5e330/short_gaps_numerics.pdf), §§1.1–1.5. The preserving official certificate file has SHA256 `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`. No official source was modified.
