# Growing-wheel centering of the actual prime variance and heat energy

Date: 2026-09-05. Status: bounded ordinary proof, submitted for independent review. The elementary finite-height comparison inequalities are unconditional. Their vanishing-error consequences use the established RH bound for the original R20 variance. No strict arithmetic gain, AH refutation, or novelty is claimed.

The wheel modulus below is denoted by \(\mathcal W\), distinct from the fixed logarithmic window weight \(W_T(x)\). It may depend arbitrarily on \(T\); no differentiability, monotonicity or bound \(\mathcal W\le T^C\) is assumed.

## 1. Objects and explicit error scales

Retain the actual R20 statistic, with
\[
\ell=\log T,\quad a=7/4,\quad b=9/4,\quad
L=T^a,\quad U=T^b,\quad T\ge4,
\qquad W_T(x)=\omega(\log x/\ell),
\]
where \(\omega\) is the unchanged nonnegative smooth bump supported on \([a,b]\). Write \(B=\|\omega\|_\infty\). On the positive product measure
\[
d\mu_T(x,\lambda)=\frac{T}{\ell^2}
e^{-\lambda}W_T(x)\frac{dx}{x^2}\,d\lambda,
\quad x\ge1,\ \lambda\ge0,
\]
the exactly centered prime interval count is
\[
\Delta_T(x,\lambda)=
\Psi(e^{\lambda/T}x)-\Psi(x)-(e^{\lambda/T}-1)x,
\quad \overline V_T=\|\Delta_T\|_{\mu_T}^2.
\tag{1}
\]
All prime powers are retained in \(\Psi\). Put
\[
\mathfrak m_T=\mu_T(\mathbb R^2)
=\frac{T}{\ell^2}\int_L^U W_T(x)x^{-2}dx
\le\frac{BT}{L\ell^2}.
\tag{2}
\]

Let \(\mathcal W\ge1\) be squarefree, and define
\[
\kappa=\#\{p:p\mid\mathcal W\},\quad
R=\frac{\mathcal W}{\varphi(\mathcal W)},\quad
D=R2^\kappa,\qquad
\rho_{\mathcal W}(n)=R\,1_{(n,\mathcal W)=1}.
\tag{3}
\]
For \(\mathcal W=1\), use \(R=D=1\) and \(\kappa=0\).

There are two different modified interval counts:
\[
\Delta_T^{\rm wheel}=
\sum_{x<n\le e^{\lambda/T}x}
[\Lambda(n)-\rho_{\mathcal W}(n)],
\tag{4}
\]
and the residual supported on integers coprime to the wheel,
\[
r_{\mathcal W}(n)=
\Lambda(n)1_{(n,\mathcal W)=1}-\rho_{\mathcal W}(n)
=[\Lambda(n)-R]1_{(n,\mathcal W)=1},
\qquad
\Delta_T^{\rm rough}=\sum_{x<n\le e^{\lambda/T}x}r_{\mathcal W}(n).
\tag{5}
\]
Here “rough” means coprime to this wheel; when \(\mathcal W\) is a primorial it is the usual absence of prime factors up to its cutoff. Prime powers with bases not dividing \(\mathcal W\) remain in (5).

Define \(\overline V_T^{\rm wheel}=\|\Delta_T^{\rm wheel}\|_{\mu_T}^2\) and similarly \(\overline V_T^{\rm rough}\). The explicit norm errors are
\[
e_T^{\rm wheel}=2D\sqrt{\mathfrak m_T},\qquad
e_T^{\rm rough}=
\left[2D+\kappa\left(b\ell+\frac{\sqrt2}{T}\right)\right]
\sqrt{\mathfrak m_T}.
\tag{6}
\]

**Theorem 1.** For every real \(T\ge4\) and every finite squarefree \(\mathcal W\),
\[
|\sqrt{\overline V_T^{\rm wheel}}-\sqrt{\overline V_T}|
\le e_T^{\rm wheel},\qquad
|\sqrt{\overline V_T^{\rm rough}}-\sqrt{\overline V_T}|
\le e_T^{\rm rough}.
\tag{7}
\]
For either choice, with its corresponding \(e_T\),
\[
|\overline V_T^{\rm modified}-\overline V_T|
\le 2\sqrt{\overline V_T}\,e_T+e_T^2.
\tag{8}
\]
Consequently, under RH and the sole growth condition
\[
\boxed{D_{\mathcal W(T)}=o(T^{3/8}\log T),}
\tag{9}
\]
both modified variances equal \(\overline V_T+o(1)\). This statement includes a quantified removal of every prime power whose base divides the wheel, rather than assuming such terms vanish.

## 2. Inclusion-exclusion controls the center globally

Let \(N_{\mathcal W}(x)=\sum_{1\le n\le x}\rho_{\mathcal W}(n)\), for real \(x\ge0\). Inclusion-exclusion and the exact totient identity give
\[
N_{\mathcal W}(x)=R\sum_{d\mid\mathcal W}\mu(d)\lfloor x/d\rfloor,
\qquad R\sum_{d\mid\mathcal W}\frac{\mu(d)}d=1.
\]
Hence
\[
N_{\mathcal W}(x)-x
=-R\sum_{d\mid\mathcal W}\mu(d)\{x/d\},
\qquad |N_{\mathcal W}(x)-x|\le R2^\kappa=D.
\tag{10}
\]
For arbitrary real endpoints \(0\le x\le y\), this implies
\[
|N_{\mathcal W}(y)-N_{\mathcal W}(x)-(y-x)|\le2D.
\tag{11}
\]
This is uniform over every \(\lambda\ge0\) when \(y=e^{\lambda/T}x\); no growing-length cutoff is needed. It respects the half-open interval \((x,y]\), including noninteger endpoints.

The difference of (4) and (1) is the negative of the center error (11). Its product-space norm is therefore at most \(2D\sqrt{\mathfrak m_T}\). The Hilbert-space triangle inequality proves the first half of (7), and expansion of the squared norm gives (8). The original variance is finite for \(T\ge4\), even before assuming RH, by the elementary convergent kernel bounds in R21.

## 3. Prime powers dividing the wheel are charged explicitly

Define the nonnegative removed staircase
\[
P_{\mathcal W}(x)=
\sum_{p\mid\mathcal W}\sum_{\substack{j\ge1\\p^j\le x}}\log p,
\qquad x\ge1.
\]
For each base \(p\), its contribution is at most \(\log x\); thus
\[
0\le P_{\mathcal W}(x)\le\kappa\log x.
\tag{12}
\]
In particular, the interval contribution
\(A_{\mathcal W}(x,\lambda)=P_{\mathcal W}(e^{\lambda/T}x)-P_{\mathcal W}(x)\)
satisfies, on the entire support of \(W_T\),
\[
0\le A_{\mathcal W}(x,\lambda)
\le\kappa(b\ell+\lambda/T).
\tag{13}
\]
This bound works even if some prime factors of \(\mathcal W\) lie above the physical window; it requires no estimate in terms of \(\log\mathcal W\).

Since the normalized exponential length law has \(\|1\|_2=1\) and \(\|\lambda\|_2=\sqrt2\), (13) gives
\[
\|A_{\mathcal W}\|_{\mu_T}
\le\kappa\left(b\ell+\frac{\sqrt2}{T}\right)\sqrt{\mathfrak m_T}.
\tag{14}
\]
Exactly \(\Delta_T^{\rm rough}=\Delta_T^{\rm wheel}-A_{\mathcal W}\). Combining this identity with (11) proves the second half of (7). It proves finiteness of the modified variances as well.

Under RH, the already reviewed R20 theorem gives \(\overline V_T=O_\omega(1)\). Condition (9) makes \(D\sqrt{\mathfrak m_T}=o(1)\), because \(\sqrt{T/L}=T^{-3/8}\). Also \(D\ge2^\kappa\), so (9) forces \(\kappa=O(\log T)\). The extra debt in (14) is therefore
\[
O_\omega(T^{-3/8}\log T)=o(1).
\]
Thus (9) alone is sufficient for both modifications. It is not necessary to impose a separate size bound on the wheel's prime divisors or to assert that their prime powers are absent.

## 4. A genuinely growing primorial family

Take
\[
\mathcal W(T)=\prod_{p\le z(T)}p,
\qquad z(T)=c\log T\log\log T,
\quad 0<c<\frac{3}{8\log2}.
\tag{15}
\]
Only the classical PNT is needed to check (9):
\(\pi(z)\sim z/\log z\), so \(\kappa=\pi(z)=(c+o(1))\ell\).
The elementary telescoping majorant, valid for \(z\ge2\),
\[
1\le R=\prod_{p\le z}\frac p{p-1}
\le\prod_{2\le n\le\lfloor z\rfloor}\frac n{n-1}
=\lfloor z\rfloor
\]
shows \(\log R=O(\log z)=o(\ell)\). Hence
\[
D=T^{c\log2+o(1)},
\qquad
\frac{D}{T^{3/8}\ell}
=T^{-3/8+c\log2+o(1)}/\ell\longrightarrow0.
\tag{16}
\]
Mertens' sharper product asymptotic is not needed. The constant \(c=1/2\), for example, lies strictly in the allowed range: \(\log2<3/4\), as follows from the trapezoidal upper bound for \(\int_1^2dx/x\).

The displayed range is a sufficient range from this particular discrepancy budget. For \(c>3/(8\log2)\), that budget fails, which does not prove the center replacement itself fails. No boundary assertion at equality is deduced from the first-order PNT calculation. No finite-height cutoff, wheel enumeration, or computational complexity estimate is claimed.

The PNT statement and its unconditional status were checked directly in NIST DLMF equation 27.2.3. The exact source page and formula are retained and pinned. This is the only new external asymptotic used in this note.

## 5. Transfer to an actual rough-residual log-prime heat energy

This section applies the independently reviewed R21 heat representation; it introduces no stochastic matrix model or zero-motion equation. Define the cumulative rough residual and its localized logarithmic profile by
\[
C_{\mathcal W}(x)=\sum_{1\le n\le x}r_{\mathcal W}(n)
=\Psi(x)-P_{\mathcal W}(x)-N_{\mathcal W}(x),
\qquad
g_{T,\mathcal W}(v)=\sqrt{\omega(v/\ell)}\,e^{-v/2}C_{\mathcal W}(e^v).
\tag{17}
\]
Compare with the original R21 profile
\(g_T(v)=\sqrt{\omega(v/\ell)}e^{-v/2}[\Psi(e^v)-e^v]\).
On its support \(a\ell\le v\le b\ell\), equations (10) and (12) imply
\[
|g_{T,\mathcal W}(v)-g_T(v)|
\le\sqrt B\,e^{-v/2}(D+\kappa v).
\]
Extending the positive integral past \(b\ell\), and using the \(L^2\) norm of a mean-one exponential variable, gives
\[
\boxed{
\|g_{T,\mathcal W}-g_T\|_2
\le\sqrt{B/L}\,[D+\kappa(a\ell+\sqrt2)].}
\tag{18}
\]
This controls the actual cumulative staircase, not an uncentered or divergent prime series.

Use the unchanged angular Fourier convention and R21 multiplier
\[
M_T(\xi)=\frac{2T-1}{T-1}
\frac{\xi^2+1/4}{(T-1/2)^2+\xi^2},\qquad
\mathcal J_T(g)=\frac{T}{2\pi\ell^2}\int_{\mathbb R}
M_T(\xi)|\widehat g(\xi)|^2d\xi.
\tag{19}
\]
For \(T\ge4\), \(0\le M_T\le7/3\). The quadratic-form triangle inequality and (18) imply
\[
|\sqrt{\mathcal J_T(g_{T,\mathcal W})}-\sqrt{\mathcal J_T(g_T)}|
\le h_T,
\quad
h_T=\sqrt{7B/3}\,\frac{T^{-3/8}}\ell
[D+\kappa(a\ell+\sqrt2)].
\tag{20}
\]
Under (9), \(h_T\to0\). The R21 theorem states
\(\mathcal J_T(g_T)=\overline V_T+O_\omega(\sqrt{\ell/T})\), and bounds \(\mathcal J_T(g_T)\) under RH. Thus
\[
\boxed{
\overline V_T=\mathcal J_T(g_{T,\mathcal W})
+O_\omega(\sqrt{\ell/T}+h_T+h_T^2).}
\tag{21}
\]
The implied constant is independent of the varying wheel. Equations (7)–(9) also give \(\overline V_T^{\rm rough}=\mathcal J_T(g_{T,\mathcal W})+o(1)\) under the same hypotheses.

For completeness the exact heat expression for (19), valid for any \(g\in L^2\), is
\[
\mathcal J_T(g)=\frac{T(2T-1)}{(T-1)\ell^2}
\int_0^\infty e^{-(T-1/2)^2t}
\left[\|\partial_v e^{t\partial_v^2/2}g\|_2^2
+\frac14\|e^{t\partial_v^2/2}g\|_2^2\right]dt.
\tag{22}
\]
The bounded multiplier justifies the integrated derivative even for a staircase with jumps. Its heat acts in the logarithmic integer coordinate; it is not the de Bruijn–Newman deformation or Dyson Brownian motion.

## 6. What the structure buys, and what is still missing

There is a real arithmetic reorganization: a growing set of local prime factors can be removed, leaving a fully specified residual supported on \((n,\mathcal W)=1\), with explicit variance and heat-energy errors. Neither excluded prime powers nor endpoint discrepancies are swept away. The statement is uniform in the allowed growing wheel and retains the original continuum window and complete positive length law.

This is nevertheless an equivalence of the existing target, not an improvement of its value. The coefficient on the remaining coprime integers changes to \(\Lambda(n)-R\); removing support does not make the squared residual or its heat energy smaller by monotonicity. The original bound \(A\) transfers unchanged. Under RH plus the precise AH-Pairs hypothesis, the modified variances and normalized energy still tend to \(A\).

A useful next theorem would therefore have to prove a strict upper estimate for this particular rough residual's weighted quadratic energy, using arithmetic cancellation that is not supplied by inclusion-exclusion, its mean density, or positivity of the heat operator. For instance, proving \(\liminf_T\mathcal J_T(g_{T,\mathcal W})<A\) for an admissible wheel would give a strict original variance deficit through (21). No such inequality is proved here.

## Sources and bounded verification

- [NIST DLMF 27.2.3, prime number theorem](https://dlmf.nist.gov/27.2.E3), with its source discussion in [27.2(i)](https://dlmf.nist.gov/27.2): used only for the explicit primorial family. No Mertens estimate or unproved distribution theorem is imported.
- Frozen R20 `EXPONENTIAL_LENGTH_AVERAGE.md`, SHA256 `cd8c2f7dc48530ed02f915dd202c8aedaaaadb1096cafc019beeb595b9beebbe`: actual statistic, existence, RH boundedness and AH saturation.
- Frozen R21 `LOCALIZED_MELLIN_HEAT_ENERGY.md`, SHA256 `1ee3d147669929f78a31e785d974eb851bf943453715c361e32ac2355407a1a8`: original heat representation and its localization error. Its independent review is pinned separately.

The adjacent checks, if replayed, concern exact scalar norm/moment identities and constants only. They do not enumerate wheel divisors, factor integers, sample prime heights, or test a conjecture numerically. The displayed ordinary proof establishes the all-endpoint and all-length bounds.
