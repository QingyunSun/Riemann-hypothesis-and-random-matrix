# Multiplicative-height equicontinuity of the actual zeta Bragg deficit

Round 20, 2026-09-05. Author: Euclid. Status: ordinary proof under RH, submitted for independent review. This is a regularity consequence of the classical support-one Montgomery formula, newly verified for this programme's statistic. It does not prove a positive deficit or refute AH.

**Result.** For the fixed R16 bump, let \(A=1+\varepsilon^2m_1\). Under RH,
\[
\boxed{
|D_{Ty}-D_T|
\le 2A\,\frac{|y-1|}{\max(1,y)}+o(1),
\qquad \tfrac12\le y\le2,
}
\tag{1}
\]
where the error tends to zero uniformly in \(y\). In particular the proposed bound with \(2A|y-1|\) is valid. A positive upper subsequential deficit persists on a multiplicative-height interval of fixed positive width.

The final section states the consequence for the separately investigated exponential length-average identity. That identity is a distinct dependency: it is not proved by height regularity.

## 1. Exact pair measure and the retained Lorentzian weight

Assume RH. All zero ordinates below are real, and every zero is counted with its multiplicity. For \(S\ge2\), write
\[
L_S=\frac{\log S}{2\pi},\qquad N_S=S L_S,\qquad
w(v)=\frac4{4+v^2}.
\]
For a bounded test \(\phi\), define the finite positive pair functional
\[
\mathcal M_S(\phi)=\frac1{N_S}
\sum_{0<\gamma,\gamma'\le S}
\phi\bigl(L_S(\gamma-\gamma')\bigr)w(\gamma-\gamma').
\tag{2}
\]
The denominator is \(S\log S/(2\pi)\), not the exact zero count. The factor \(w\) is unchanged as the height varies.

Let \(\psi\) be the fixed even smooth autocorrelation bump in R16, supported on \([-1,1]\), with \(\psi(0)=1\), \(\psi\ge0\) and \(\widehat\psi\ge0\). Fix \(0<\varepsilon<1\), and use
\[
\phi_0(u)=\varepsilon\widehat\psi(\varepsilon u),\qquad
\phi_D(u)=\phi_0(u)(1-\cos(4\pi u)).
\tag{3}
\]
Both are Schwartz functions. Set
\[
C_0(S)=\mathcal M_S(\phi_0),\qquad D_S=\mathcal M_S(\phi_D).
\]
Thus these are the actual R16 statistics. The exact pair kernels satisfy
\[
0\le\phi_D\le2\phi_0.
\tag{4}
\]
The Fourier representation also gives
\[
D_S=C_0(S)-\int\psi((\alpha-2)/\varepsilon)F_S(\alpha)\,d\alpha.
\]
Since \(F_S\ge0\) and \(\psi\ge0\),
\[
0\le D_S\le C_0(S).
\tag{5}
\]

The established support-one Montgomery formula implies
\[
C_0(S)\longrightarrow A:=1+\varepsilon^2m_1,\qquad
m_1=\int |v|\psi(v)\,dv.
\tag{6}
\]
This is a full limit over real heights, including zero ordinates as endpoints. No simplicity, gap restriction, or AH assumption is used.

## 2. A bandlimited envelope controls all Schwartz pair tails

Define \(s(u)=\sin(\pi u)/(\pi u)\), continuously at zero, and
\[
q(u)=s(u)^2+\frac{s(u-\tfrac12)^2+s(u+\tfrac12)^2}{2}.
\tag{7}
\]
Its Fourier transform, with the \(e^{-2\pi i\alpha u}\) convention, is
\[
\widehat q(\alpha)=(1-|\alpha|)_+\bigl(1+\cos(\pi\alpha)\bigr).
\tag{8}
\]
It is nonnegative and supported on \([-1,1]\). For all real \(u\),
\[
\boxed{q(u)\ge\frac1{2\pi^2(1+u^2)}.}
\tag{9}
\]

**Proof of the lower bound.** Each of \(u^2,(u-\tfrac12)^2,(u+\tfrac12)^2\) is at most \(2(1+u^2)\). The numerators of the shifted squared sinc terms are \(\cos^2(\pi u)\). After applying this common denominator bound, their half-weighted sum plus the unshifted term has numerator
\(\sin^2(\pi u)+\cos^2(\pi u)=1\). Removable singularities follow by continuity. ∎

Fourier inversion in the finite pair sum and the known low-band formula give
\[
\mathcal M_S(q)
=\int_{-1}^1\widehat q(\alpha)F_S(\alpha)\,d\alpha
\longrightarrow
\widehat q(0)+\int_{-1}^1|\alpha|\widehat q(\alpha)\,d\alpha
=\frac73.
\tag{10}
\]
Indeed \(\widehat q(0)=2\); the nonoscillatory integral is \(1/3\), while
\(\int_0^1\alpha(1-\alpha)\cos(\pi\alpha)\,d\alpha=0\) by reflection about \(1/2\).

In particular \(\mathcal M_S(q)\le3\) for all sufficiently large real \(S\). Hence, for any nonnegative \(R\) satisfying \(R(u)\le B/(1+u^2)\),
\[
\boxed{\mathcal M_S(R)\le6\pi^2B}
\tag{11}
\]
for such \(S\). This controls the entire pair sum, including arbitrarily large normalized differences. There is no unsupported global linear pair-count estimate and no discarded distant-zero tail.

## 3. Uniform change of logarithmic scale

For a fixed Schwartz function \(\phi\), define the finite seminorm
\[
B_\phi=
\sup_{\substack{u\in\mathbb R\\1/2\le a\le2}}
(1+u^2)|u\phi'(au)|.
\]
The mean-value theorem gives, for \(a\in[1/2,2]\),
\[
|\phi(au)-\phi(u)|
\le |a-1|\frac{B_\phi}{1+u^2}.
\]
Using (11),
\[
\boxed{
|\mathcal M_S(\phi(a\,\cdot))-\mathcal M_S(\phi)|
\le6\pi^2B_\phi|a-1|.
}
\tag{12}
\]
The bound applies to \(\phi_0\) and \(\phi_D\); the cosine derivative in \(\phi_D\) is already included in its Schwartz seminorm.

Introduce the frozen-scale unnormalized sum
\[
\mathcal S_\phi(U;\ell)=
\sum_{0<\gamma,\gamma'\le U}
\phi\bigl(\ell(\gamma-\gamma')\bigr)w(\gamma-\gamma').
\]
For \(U/T\in[1/2,2]\), take \(a=L_T/L_U\). Then
\[
\frac{\mathcal S_\phi(U;L_T)}{N_U}
=\mathcal M_U(\phi)+O_\phi(1/\log T),
\tag{13}
\]
uniformly in \(U\). This holds at zero heights as well. Crucially, the physical Lorentzian weight in (2) does not change when the logarithmic scale is frozen.

## 4. Positive prefix increments prove equicontinuity

First let \(T\le U\le2T\), and put
\[
r=1-\frac{N_T}{N_U}\in[0,1).
\]
At the common scale \(L_T\), all newly included ordered pairs have nonnegative kernels, and (4) gives the exact inequality
\[
0\le
\mathcal S_{\phi_D}(U;L_T)-\mathcal S_{\phi_D}(T;L_T)
\le
2\bigl(\mathcal S_{\phi_0}(U;L_T)-\mathcal S_{\phi_0}(T;L_T)\bigr).
\tag{14}
\]
Let
\[
E(T)=\sup_{T/2\le S\le2T}|C_0(S)-A|\longrightarrow0.
\]
By (6) and (13), after dividing (14) by \(N_U\),
\[
0\le X_{T,U}
\le2Ar+4E(T)+O_\varepsilon(1/\log T),
\tag{15}
\]
where \(X_{T,U}\) denotes its middle increment divided by \(N_U\).

Normalization and (13) now give
\[
D_U-D_T=X_{T,U}-rD_T+O_\varepsilon(1/\log T).
\tag{16}
\]
Since \(0\le D_T\le C_0(T)\le A+E(T)\), equations (15)–(16) imply
\[
|D_U-D_T|
\le2Ar+4E(T)+O_\varepsilon(1/\log T).
\tag{17}
\]
The factor is \(2A\), rather than the sum of two unrelated absolute bounds: the increment and normalization terms in (16) have opposite signs.

For \(T/2\le U\le T\), interchange the smaller and larger height in the same proof and freeze the smaller logarithmic scale. All natural-scale estimates still lie in \([T/2,2T]\). Thus, uniformly on that full range,
\[
|D_U-D_T|
\le2A\left(1-\frac{\min(N_T,N_U)}{\max(N_T,N_U)}\right)
+4E(T)+O_\varepsilon(1/\log T).
\tag{18}
\]
Writing \(U=Ty\), the normalization ratio differs by \(O(1/\log T)\), uniformly, from \(\min(1,y)/\max(1,y)\). This proves (1).

This is asymptotic equicontinuity, not literal continuity of the finite-height statistic: finite sums jump at zero ordinates. The uniform vanishing error absorbs such jumps. Positivity of the actual sums, the full limit (6), and the envelope bound already account for multiplicities and all endpoint conventions.

## 5. Persistence of a positive subsequential deficit

Let
\[
d=\limsup_{T\to\infty}D_T,\qquad 0\le d\le A.
\]
If \(d>0\), choose \(T_k\to\infty\) with \(D_{T_k}\to d\), and put
\[
r_d=\frac d{8A}\le\frac18.
\]
Equation (1) gives uniformly for \(1-r_d\le y\le1+r_d\),
\[
D_{T_ky}\ge d-2Ar_d-o(1)=\frac{3d}{4}-o(1).
\]
In particular, for all sufficiently large \(k\),
\[
\boxed{
D_{T_ky}\ge d/2
\quad\text{throughout }[1-r_d,1+r_d].
}
\tag{19}
\]
This is a fixed positive-width interval on the logarithmic height axis. For example, \(|\log y|\le d/(16A)\) implies \(|y-1|\le r_d\), since this logarithmic radius is at most \(1/16\) and \(|e^u-1|\le2|u|\) there.

No positive value of \(d\) is proved. The conclusion concerns the regularity of any positive upper subsequential value, if one exists.

## 6. Conditional consequence for the separate length-average identity

Aquinas is separately studying the positive exponential length-average statistic \(\overline V_T\). Suppose its claimed actual-zeta identity has been established:
\[
A-\overline V_T
=\int_0^\infty p(y)D_{Ty}\,dy+o(1),\qquad
p(y)=\frac4\pi\frac{y^2}{(1+y^2)^2},
\quad \int_0^\infty p(y)\,dy=1.
\tag{20}
\]
A bounded extension of \(D_S\) below \(S=2\) is harmless. The density is positive on every compact subinterval of \((0,\infty)\).

Combining (19), positivity, and (20) yields
\[
\boxed{
A-\liminf_T\overline V_T
\ge\frac d2\,P(r_d)>0,\qquad
P(r)=\int_{1-r}^{1+r}p(y)\,dy,
}
\tag{21}
\]
whenever \(d>0\). The exact positive mass is
\[
P(r)=\frac2\pi
\left[\arctan y-\frac{y}{1+y^2}\right]_{1-r}^{1+r}.
\tag{22}
\]
More generally the limsup of the right side of (20) is at most \(d\): outside \(Ty\) in a fixed bounded interval, \(D_{Ty}\le d+o(1)\), while the \(p\)-mass of that bounded-height part tends to zero. The bounded extension and (5)–(6) justify this argument. Since \(p(y)\ge16/(25\pi)\) on \([1/2,2]\), the useful explicit comparison is
\[
\boxed{
\frac{2d^2}{25\pi A}
\le A-\liminf_T\overline V_T\le d.
}
\tag{23}
\]
For \(d=0\), the lower bound follows from positivity and the upper bound is zero. Equivalently \(D_S\to0\), and dominated convergence against \(p\) gives the same conclusion.

Therefore, **conditional on the separate identity (20)**,
\[
\boxed{
\limsup_T D_T>0
\quad\Longleftrightarrow\quad
\liminf_T\overline V_T<A.
}
\tag{24}
\]
This upgrades the direction furnished merely by positivity. It still proves neither side is true for the actual zeta function, and is not an AH refutation. Acceptance of (23)–(24) must remain pinned to an independent proof of (20).

## Sources and checks

* R16 BRAGG_ATOM_TARGET.md supplies the exact fixed bump and deficit definition. Its statements (5)–(6) also follow directly from the pair/Fourier calculation above.
* Carneiro–Chandee–Chirre–Milinovich, [On Montgomery's pair correlation conjecture: a tale of three integrals](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), equations (1.5)–(1.6), printed pp.1–2: Fourier pair identity and the support-one Montgomery formula. The retained source PDF and text are pinned in the adjacent manifest.
* The length-average identity (20) is an explicitly separate R20 dependency, not assumed as a previously verified theorem in proving (1).

The adjacent exact checker verifies the Fourier-envelope normalization, denominator inequalities, normalization-ratio algebra, and the positive probability-kernel primitive. It is not a simulation of zeros or a numerical proof of a positive deficit. The ordinary arguments above establish the asymptotic and uniformity statements.
