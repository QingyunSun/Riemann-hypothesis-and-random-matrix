# A weighted Selberg-variance target for the frequency-two Bragg deficit

Date: 2026-09-05. Status: bounded primary-literature audit and ordinary analytic reduction, submitted for independent review. No strict actual-zeta deficit, new prime variance upper constant, AH refutation, or Montgomery–Dyson theorem is proved.

The useful outcome is an explicit **positive short-interval prime variance**, with the exact same AH saturation value as the R16 bump. A strict lower subsequential value of this variance forces a positive upper subsequential Bragg deficit. Its prime-pair kernel is finite and nonnegative; all prime powers and both centering terms remain. This replaces an oscillatory arithmetic target by a different sufficient arithmetic target, without asserting they are equal at the same height or that an existing theorem supplies the missing inequality.

## 1. Fixed normalization and the proposed arithmetic test

Assume RH. Retain the R16 smooth autocorrelation bump ψ, its normalization ψ(0)=1, and the exact constants
\[
m_0=\int_{\mathbb R}\psi(v)dv,
\qquad m_1=\int_{\mathbb R}|v|\psi(v)dv.
\]
Thus 0<m₁<m₀<1, ψ and its Fourier transform are nonnegative, and supp ψ=[−1,1]. Fix 0<ε<1 and define
\[
\omega(\alpha)=\psi((\alpha-2)/\varepsilon),\quad
A_\varepsilon=1+\varepsilon^2m_1,
\]
\[
C_T=\int\omega(\alpha)F_T(\alpha)d\alpha,
\quad D_T=C_{\varepsilon,T}(0)-C_T\ge0.
\tag{1}
\]
Zeros and all pair statistics are counted with multiplicity. The form factor has the R16 normalization T log T/(2π). The proved R16 bound is C_T≤Aε+o(1), and AH-Pairs forces C_T→Aε. In particular
\[
C_T=A_\varepsilon-D_T+o(1).
\tag{2}
\]
No near-diagonal parameter p₀ or simplicity assumption is added.

Write Ψ(x)=Σ_{n≤x}Λ(n), to distinguish the Chebyshev function from the bump ψ. Put q_T=1+1/T and
\[
\Delta_T(x)=\Psi(q_Tx)-\Psi(x)-x/T.
\]
The new concrete statistic is
\[
\boxed{V_{\varepsilon,T}
=\frac{T}{\log^2T}\int_1^\infty
 \Delta_T(x)^2\,\omega\!\left(\frac{\log x}{\log T}\right)\frac{dx}{x^2}.}
\tag{3}
\]
It is nonnegative. It has no inverse-ε normalization. Its x support is exactly the logarithmic window T^{2−ε}≤x≤T^{2+ε}, not a constant-factor neighborhood of T². The interval length is h=x/T. For ε=1/4 its exponent relative to x ranges from 3/7 to 5/9; the central value is h=√x.

The main deduction below is
\[
\boxed{\mathrm{RH+AH\!\!\!\!-Pairs}\Longrightarrow
 V_{\varepsilon,T}\longrightarrow A_\varepsilon.}
\tag{4}
\]
Consequently, for this one fixed test,
\[
\boxed{\liminf_T V_{\varepsilon,T}<A_\varepsilon
\quad\Longrightarrow\quad \limsup_T D_T>0.}
\tag{5}
\]
This is enough to exclude full AH-Pairs. It does not promise a lower bound for D at every sufficiently large height. In particular a proof of liminf V≤1 would suffice, since Aε>1. No such estimate is established here.

## 2. Primary-source input: a weighted Plancherel formula, not a conjectural equivalence

The source is Carneiro–Chandee–Chirre–Milinovich (CCCC), *On Montgomery's pair correlation conjecture: a tale of three integrals*, printed pp.22–25, especially equations (3.8)–(3.9), Lemma 13 and Theorem 14. The PDF is retained from R16; its printed p.25 was visually checked again in this audit. Their formulas in turn cite Goldston–Gonek (1990), Eq.(8), and Goldston (1988), Eqs.(5.1)–(5.3).

First let ω=|ĝ|², where ĝ is smooth with compact support in (0,∞), and g is its inverse Fourier transform with the convention e^{−2πiαu}. Define
\[
L_T=\frac{\log T}{2\pi},\quad
f_T(t)=\left|\sum_\gamma g((t-\gamma)L_T)\right|^2
      +\left|\sum_\gamma g((\gamma-t)L_T)\right|^2,
\]
\[
K_T(Y)=\int_0^Y f_T(t)dt,
\quad \kappa_T=\tfrac12\log(1+1/T).
\]
The sums are over all nontrivial zero ordinates, including negative ordinates and multiplicity. Their rapid convergence follows from g being Schwartz and the local zero count. The source gives
\[
V_T(\omega)=\frac{2T}{\pi}\int_0^\infty
 \left(\frac{\sin(\kappa_Tt)}t\right)^2 f_T(t)dt
 +O_g(\log^{-2}T),
\tag{6}
\]
\[
K_T(Y)=2Y\int\omega(\alpha)F_Y(\alpha)d\alpha+o_g(Y),
\quad T\log^{-3}T\le Y\le T\log^3T,
\tag{7}
\]
uniformly in that range. Also f_T(t)≪_g log²(t+2). Formula (7) already accounts for replacing log Y by log T when their ratio tends to one. An arbitrary change of height by a power of T is not permitted by this uniform statement.

The numerical prefactors can be checked independently. At Y=T, integrating one squared zero sum produces L_T^{-1} times the pair sum with inverse transform of |ĝ|²; dividing the latter by T L_T gives T times the form-factor integral. The two squared sums give 2T, as in (7). In (6), the unnormalized source factor is (2/π)log²T and the normalization in (3) is T/log²T. No 2π or T factor is dropped. The Lorentzian pair weight and finite-height endpoints are already present in the source's o(Y) comparison; there is no removal of early zeros by an unproved informal limit.

For the specified R16 ω, we do **not** assume without proof that its square root is Schwartz. Approximate its continuous square root uniformly on a fixed compact subinterval of (0,∞) by smooth compactly supported functions, then square them. This produces ω_j=|ĝ_j|²→ω uniformly. Positivity, the R16 local mass bound for F_T(α)dα, and the RH Selberg bound J(β,T)=O_β(log²T/T) on every fixed positive log window imply uniformly bounded masses for both sides. Thus V_T(ω_j)−V_T(ω) and C_T(ω_j)−C_T(ω) have limsup bounded by constants times ||ω_j−ω||∞. First take the large-height limits at fixed j, then j→∞. Every deduction below therefore extends to the original exact bump. No constants in a Schwartz seminorm are required to remain uniform in j.

## 3. The sharp AH transfer and its order of limits

Let
\[
k(y)=\frac{\sin^2(y/2)}{y^2},\qquad k(0)=1/4,
\quad \int_0^\infty k(y)dy=\pi/4.
\tag{8}
\]
Suppose the full limit C_T→A exists. By (7), for every fixed y>0,
\[
K_T(Ty)/T\longrightarrow2Ay.
\]
On any compact y interval this gives convergence of the positive measures d(K_T(Ty)/T). Substitution t=Ty in (6), using κ_TT→1/2, gives on compact intervals
\[
V_T=\frac2\pi\int_0^\infty k(y)\,d\!\left(K_T(Ty)/T\right)+o(1),
\tag{9}
\]
where the assertion over the infinite interval is justified by the following tail estimates, not assumed as formal weak convergence.

For y<log⁻³T, f_T(t)≪log²(t+2) gives a contribution O_g(1/log T). On log⁻³T≤y≤log³T, (7) and the bounded compact form-factor mass give K_T(Ty)/T≪_g y. The region 0<y<η consequently contributes O_g(η)+o(1). For R<y<log³T, k(y)≤1/y² and integration by parts against K_T(Ty)/T give O_g(1/R)+o(1). Beyond log³T the pointwise logarithmic bound again gives O_g(1/log T). These estimates also justify replacing κ_TT by 1/2: first on a fixed compact y interval, then remove its ends by the same uniform bounds.

Thus, in the order T→∞, η↓0, R→∞,
\[
\lim_TV_T=\frac2\pi\int_0^\infty k(y)\,2A\,dy=A.
\tag{10}
\]
For a general weight one may first work with the smooth-square approximation in §2. Under AH, all such compact tests have their full limiting value because R16 proves the local spectral limit δ₂+|α−2|dα. Hence the approximation step yields A=Aε for the original bump and proves (4).

The stronger implication (5) does not require assuming AH or choosing compatible subsequences. If limsup D_T=0, nonnegativity gives D_T→0. Equation (2) then gives the full limit C_T→Aε; (10) forces V_T→Aε. Its contrapositive proves (5). A strict liminf of V alone is therefore sufficient; the particular heights exhibiting a deficit in V need not themselves have a comparable D deficit.

This is an Abelian implication for one fixed smoothed test, with all constants and tails specified. It does not assert an unrestricted reverse Goldston–Montgomery equivalence or identify V_T with C_T at the same T.

## 4. A quantitative deficit conversion with no joint-subsequence premise

There is a modest quantitative strengthening of (5). Define
\[
d=\limsup_TD_T\in[0,A_\varepsilon],\qquad
v_*=\liminf_TV_{\varepsilon,T}.
\]
For every fixed R≥1,
\[
\boxed{A_\varepsilon-v_*
\le \frac{4A_\varepsilon}{\pi R}
+\frac{4d}{\pi}\left(3+\frac1R+\frac12\log R\right).}
\tag{11}
\]
Here R is a cutoff in rescaled zero height y=t/T, not a growing prime cutoff.

To prove it, retain only 0≤y≤R in the positive integral (6). An integration by parts and (7), with the small-y argument from §3, give
\[
V_T\ge\frac4\pi\left[Rk(R)C_{TR}
-\int_0^R yk'(y)C_{Ty}dy\right]+o(1).
\tag{12}
\]
For a fixed compact interval away from y=0, equation (2) holds uniformly after replacing T by Ty; limsup D=d implies D_{Ty}≤d+o(1), uniformly there. The negligible small-y interval is removed last. Inserting C_{Ty}=Aε−D_{Ty}+o(1) in (12) yields
\[
A_\varepsilon-v_*
\le\frac{4A_\varepsilon}{\pi}\int_R^\infty k(y)dy
+\frac{4d}{\pi}\left[Rk(R)+\int_0^R|yk'(y)|dy\right].
\tag{13}
\]
The elementary estimates are
\[
yk'(y)=\frac{\sin y}{2y}-\frac{1-\cos y}{y^2},\quad
Rk(R)\le1/R,
\]
\[
\int_0^R|yk'(y)|dy
\le 3+\tfrac12\log R\quad(R\ge1),
\quad \int_R^\infty k(y)dy\le1/R.
\]
For y≤1 use |sin y|≤y and 1−cos y≤y²/2, giving |yk'|≤1. For y≥1 use |yk'|≤1/(2y)+2/y². These prove (11). The smooth-square approximation extends it to ω exactly as in §2.

If δ=Aε−v_*>0, take any R≥max(1,8Aε/(πδ)). Then
\[
\boxed{\limsup_TD_T\ge
\frac{\pi\delta}{8(3+R^{-1}+\tfrac12\log R)}>0.}
\tag{14}
\]
The constant is deliberately conservative. It is a proved conversion **conditional on a variance deficit**, not a proved deficit for the primes. Integrating by parts over all y and pretending that the oscillatory derivative has finite L¹ norm would be wrong: |yk'(y)| has a nonintegrable 1/y oscillatory envelope. The finite R and the positive discarded tail are essential.

## 5. The actual arithmetic kernel is finite and nonoscillatory

Let W_T(x)=ω(log x/log T). For positive integers m,n define
\[
B_T(m,n)=\frac{T}{\log^2T}
\int_{\max(m,n)/q_T}^{\min(m,n)} W_T(x)\frac{dx}{x^2},
\tag{15}
\]
with value zero if the upper endpoint does not exceed the lower one. Also put
\[
L_T(n)=\frac1{\log^2T}\int_{n/q_T}^{n}W_T(x)\frac{dx}{x},
\quad M_T=\frac1{T\log^2T}\int W_T(x)dx.
\tag{16}
\]
The notation L_T(n) in this section is an arithmetic kernel, distinct from the zero scaling log T/(2π) in §2. Expanding the square in (3) gives the exact finite identity
\[
\boxed{V_{\varepsilon,T}
=\sum_n\Lambda(n)^2B_T(n,n)
+2\sum_{m<n}\Lambda(m)\Lambda(n)B_T(m,n)
-2\sum_n\Lambda(n)L_T(n)+M_T.}
\tag{17}
\]
All sums are finite because W_T has compact support. The nonzero off-diagonal pairs satisfy n/m<1+1/T; equivalently n−m<m/T for m<n. The kernel B_T≥0. Prime powers, including squares at the h≈√x scale, have not been removed.

The interval geometry independently verifies every centering factor. An integer n is counted exactly for x∈[n/q_T,n), up to endpoints of zero Lebesgue measure. Two integers are counted on the intersection used in (15). The negative cross term in Δ_T² is −2(x/T)ΣΛ(n), which after the outside T/(x²log²T) factor gives −2Λ(n)dx/(xlog²T). The continuous square gives dx/(Tlog²T). Thus neither center may be absorbed into an unspecified remainder.

The atomic diagonal has an exact leading asymptotic:
\[
\sum_n\Lambda(n)^2B_T(n,n)\longrightarrow
\int\alpha\omega(\alpha)d\alpha=2\varepsilon m_0.
\tag{18}
\]
Indeed ∫_{n/q_T}^n dx/x²=1/(Tn), while W_T varies there by Oε(1/(Tlog T)). Partial summation of Σ_{n≤z}Λ(n)²∼zlog z then gives (18), uniformly across the fixed positive power window. Endpoint cells contribute through the same smooth formula, with no boundary atoms.

Let E_T^{SI} be the last three terms in (17). Combining (5) and (18), a sufficient arithmetic assertion is
\[
\boxed{\liminf_TE_T^{SI}
<1+\varepsilon^2m_1-2\varepsilon m_0.}
\tag{19}
\]
For ε=1/4, the right side is approximately 0.6402815099 using the already frozen R16 quadrature diagnostics. That number is not a new enclosure or observed prime statistic. The exact expression in (19) controls the proof. The sine/GUE prediction would instead give E_T^{SI}→−εm₀, which is substantially stronger cancellation than required here.

The sign of B_T alone does not bound (19). The positive pair sum, negative prime-mean sum and positive mean-square term are each much larger than their desired centered remainder. This target has removed the sinc oscillation from the arithmetic pair kernel; it has not removed the need for arithmetic cancellation around the mean.

## 6. What the strongest applicable source bounds actually say

This was a bounded primary-only audit, not a claim to have exhaustively excluded every theorem. The relevant mathematical statements and their ranges were read directly, including the newer 2025/2026 material found in the search.

| Primary result | Actual range and normalization | Consequence for the present target |
|---|---|---|
| CCCC, Theorem 7 and Theorem 9, pp.8–11 | RH; fixed finite frequency intervals; upper constants retain an atom cost tending to one as length tends to zero | Does not prove a strict deficit below Aε. The tailored R16 positive-pair comparison remains sharper for this bump. |
| CCCC, Lemma 13 and Theorem 14, pp.22–25 | Fixed logarithmic prime windows; general liminf/limsup transfer has factors L⁻≈0.9028 and L⁺≈1.0736 | Gives limsup V≤L⁺Aε, which is above Aε. The full-limit argument of §3 removes the loss only when the full spectral limit is already known, as under AH. |
| CCCC, Theorem 3/Corollary 4 | Large fixed β; upper bound J(β,T)≤(1.4283β+o(1))log²T/T | The large-β coefficient is not a β≈2 or width-2ε estimate. Subtracting two upper bounds for nested J does not bound their difference. |
| Carneiro–Milinovich–Ramos, Theorem 1/Corollary 2, 2310.01913v2, pp.2–3 | RH; sufficiently large frequency length ℓ; upper long-average constant 1.3208, uniformly in center; ℓ≥ℓ₀ is still required | Multiplying 1.3208 by 2ε for the current narrow bump is invalid. Their GRH constant 1.3155 also has the long-length condition and assumes more than RH. |
| Das–Ismoilov–Ramos, Theorem 1 and Corollary 7, 2502.05106v1 | A general framework, with upper bound only for ℓ≥ℓ₀(η) and lower bound for ℓ≥ℓ₀(b,η); applications include other sequences | This newer source does not remove the finite-window restriction for the actual zeta function. Its introductory abbreviated sentence is read with the explicit theorem quantifiers. |
| Languasco–Perelli–Zaccagnini, 1308.3934v3, p.4 | RH alone: J(X,h)≪hX log²(2X/h), 1≤h≤X. A single logarithm requires an additional pair-correlation upper-bound hypothesis | At h≈√X the available bound has an extra logarithm, with no fixed coefficient at the desired variance scale. An assumed ≪hXlog(X/h) is not an RH theorem. |
| Languasco–Perelli–Zaccagnini, 1311.0597v4, Theorem 1 and its Corollary, pp.2–3 | Actual asymptotic requires T S(X,τ)/X→∞; the stated corollary has X≤T/log T | At τ=1 and X≈T², T S/X≈Tlog X/X→0, so the theorem does not reach this region. Theorem 2 adds an extended pair-correlation conjecture. |
| Rudnick, 2605.22059v1, Theorems 1.1–1.2 | Large-genus average over hyperbolic surfaces; separately degree d>1 early-time form factor with X=T^{dα} and α<1/d | The latter range still has X<T. It supplies neither a theorem for ζ at X≈T² nor a substitute for averaging this one fixed arithmetic object. |

Here the exact sunrise constants are defined using k₀(u)=(sin u/u)²:
\[
L^- =\frac2\pi\int_0^\pi k_0(u)du,
\qquad
L^+=\frac2\pi\int_0^\infty\sup_{v\ge u}k_0(v)du.
\tag{20}
\]
The first is the integral of the greatest nonnegative nonincreasing minorant of k₀: it follows k₀ until its first zero π and is zero thereafter. The second is the integral of the least nonincreasing majorant. These extremal descriptions are exact **within that monotone-envelope class**. They are not statements that every arithmetic transfer must lose these factors, or that the source's arithmetic constants are globally optimal. In particular §3 explains exactly why the factors disappear for a known full limit.

Applying the source's upper transfer to the tailored bump gives the usable existing estimate
\[
\boxed{\limsup_TV_{\varepsilon,T}\le L^+A_\varepsilon.}
\tag{21}
\]
At ε=1/4 the source's displayed approximations make its right side about 1.085, whereas AH gives about 1.01059 and the conservative target V≤1 is below both. These are comparisons of proved formulas and conditional predictions, not numerical measurements. No unqualified claim that (21) is the best conceivable RH upper bound is made.

## 7. A theorem-shaped missing estimate at the square-root scale

The smallest new assertion needed here is (19), equivalently the variance inequality in (5), along any unbounded sequence of T. It is already weaker than a complete pair-correlation asymptotic.

A stronger but more familiar local premise would also suffice. Let ν_T be the positive variance measure
\[
d\nu_T(x)=\Delta_T(x)^2\frac{dx}{x^2}.
\]
Suppose, for some fixed B and every fixed η>0, uniformly for X in a slightly enlarged version of the required power window,
\[
\nu_T([X,e^\eta X])
\le (B\eta+o(1))\frac{\log T}{T}.
\tag{22}
\]
The o(1) must be uniform in X for each fixed η. Partition the log x window into intervals of length η. Smoothness of ω shows, by upper Riemann sums with mesh η/log T, that
\[
\limsup_T V_{\varepsilon,T}\le B\int\omega=B\varepsilon m_0.
\tag{23}
\]
The number of cells is O(log T); their uniform error, multiplied by T/log²T, is still o(1). Variation errors are O(η/log T). Therefore the sufficient fixed coefficient is
\[
\boxed{B<\frac{1+\varepsilon^2m_1}{\varepsilon m_0}.}
\tag{24}
\]
For ε=1/4 this ratio is about 5.458, using the old diagnostic constants. This is **not** a known bound: (22) asks for the single-log variance scale, uniformly on fixed multiplicative windows and with its actual mean. The RH bound with an extra logarithm does not provide any fixed B. A result stated only for additive intervals with fixed h needs its own uniform Saffari–Vaughan conversion before it can be substituted for (22).

This comparison makes the missing arithmetic requirement quantitative without demanding GUE's exact coefficient one. It also clarifies why a small relative-error prime number theorem is insufficient: an error o(h) controls a square on the much larger h² scale, while the required variance is on the h log T scale. At h≈√X those scales are separated by a positive power.

The arithmetic priority is thus a centered second-moment upper bound for the full short-interval signal on this logarithmic family of scales, retaining both means and prime powers. Neither a generic positive-semidefinite model nor an exceptional close zero pair supplies it. The R18 reflected functional identity remains an exact energy representation and does not independently estimate this finite short-interval variance.

## 8. Reproducibility, sources and limits of the audit

The adjacent checker verifies the finite interval-intersection expansion with exact symbolic integration, the kernel derivative and normalization constants, and the rational finite-window source candidate. It is not an experiment on high zeta zeros, a large prime scan, or a certification of a new asymptotic bound. The download and author receipts preserve primary source bodies and hashes, including the actual PDF versions used.

Primary links:

- CCCC, [author-hosted primary PDF](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), especially (3.8)–(3.9), Lemma 13 and Theorem 14; local copy retained from R16.
- Carneiro–Milinovich–Ramos, [2310.01913](https://arxiv.org/abs/2310.01913), downloaded PDF identifies v2, 5 October 2023.
- Das–Ismoilov–Ramos, [2502.05106v1](https://arxiv.org/html/2502.05106v1), Theorem 1 and Corollary 7. The retrieved HTML labels v1 and displays a later manuscript date; this report pins the bytes rather than inferring a version chronology from that date.
- Languasco–Perelli–Zaccagnini, [1308.3934v3](https://arxiv.org/abs/1308.3934) and [1311.0597v4](https://arxiv.org/abs/1311.0597), exact classical/conjectural range distinction.
- Rudnick, [2605.22059v1](https://arxiv.org/html/2605.22059v1), range check of its recent higher-degree/geometric comparison.

The mathematical output is the precise positive variance target, its exact finite arithmetic kernel, the sharp AH limit, and the quantitative conditional deficit conversion. The literature search supplies no strict actual-zeta upper bound below that limit. No famous-conjecture breakthrough is claimed.
