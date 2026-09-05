# The full signed cap operator and a mass-orthogonal direction beyond 77 dimensions

Status: ordinary-mathematics derivation and independent implementation review, 5 September 2026. The results below concern a fixed cap geometry and its true fragment measure. They do not certify a new prime gap, replace arithmetic support restoration, or assert positivity of the hybrid operator.

## 1. Sources and the precise question

The pinned official source is [OpenAI, PrimeGaps186, commit 61340d0b74163003b32756bb16e91d9209a5e330](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330). The mathematical inputs used here are the main paper, equations (3.15)–(3.24), Lemma 3.8, and equations (4.28)–(4.40), and the numerical companion, §1.1 and equations (2.12)–(2.15). The local source copies and hashes are recorded in the adjacent provenance JSON. The published 77 coefficients define a trial space; they do not define the full variational operator.

For the fixed original geometry, use the exact inward cap cells of the companion, recomputed with outer dimension $k=39$ and face dimension $k-1=38$. This is the geometry evaluated by `round5/geometry-trial/cap_trial.py` with its default configuration. The ordinary Hilbert-space arguments apply to every fixed $k>1$ and every such nested family. They do not inherit the original $k=40$ numerical support-error certificate for $k=39$.

The task is to identify the full operator $T$, its actual mass inner product, and a rigorously meaningful direction outside the 77-dimensional space. A further practical goal is to evaluate one such direction without forming the enormous full matrix or calculating the entire norm of $Tf$.

## 2. Measure, erasure, and adjoint

Let $\Omega_\zeta$ be the space of fragment multisets in $(0,\zeta]$, equipped with

$$
\nu=\nu_\zeta=e^\gamma\zeta\,\mathcal L(\Pi_\zeta),
\qquad d\Pi_\zeta\text{ has intensity }du/u.
$$

The prefactor is the product $e^\gamma\zeta$, not $e^{\gamma\zeta}$. This is a finite measure, not a probability measure. If $t=|X|$ is the sum of the fragments, then its pushforward is $\rho_D(t/\zeta)\,dt$. For $0<c\le\zeta$,

$$
\nu\big|_{\{\max X\le c\}}=\nu_c,
\qquad (|X|)_*\nu_c=\rho_D(t/c)\,dt.
\tag{1}
$$

Thus a prime cap changes the actual restricted measure. It does not condition a probability distribution, and totals larger than the cap remain possible. The factor $c/\zeta$ from the Poisson void probability has already canceled the change of prefactor in (1).

Let $H_O\subset\Omega_\zeta^k$ be the outer cap domain and set

$$
\mathcal H=L^2(H_O,\nu^k),\qquad
\langle f,g\rangle=\int_{H_O}\overline f g\,d\nu^k.
$$

Every function is extended by zero outside $H_O$. Write $Y=X_{\widehat i}$ for the retained tuple and $Y\oplus_i Z$ for insertion in coordinate $i$. Define

$$
(E_i f)(Y)=\int f(Y\oplus_i Z)\,d\nu(Z).
\tag{2}
$$

The face space uses $L^2(\Omega_\zeta^{k-1},\nu^{k-1})$. Direct Fubini gives

$$
(E_i^*v)(X)=\mathbf1_{H_O}(X)v(X_{\widehat i}).
\tag{3}
$$

In particular, erasure is an integral, not a conditional mean. There is no factor $k$, $h$, or $Z$ in (2) or (3). The companion divides every quadratic form, including face pairings, by the same constant $(hZ)^k$. Multiplying both Hilbert inner products by this same constant leaves (3) unchanged. Independently normalizing the $k$- and $(k-1)$-coordinate spaces would change the adjoint and would not reproduce the source conventions.

## 3. Three different operators must remain distinct

Let $H_0\subset H_1$ be the cap-only face domains. Let $L_0\subset L_1$ be the actual face domains, with $L_a\subset H_a$. In the source,

$$
L_1=H_1\cap L_{\rm new},\qquad
L_0=H_0\cap L_{\rm old}\cap L_{\rm new}.
$$

Let $O\subset H_O$ impose the actual outer source predicates, and write $P_O=\mathbf1_O$. With the source's fixed hybrid parameters,

$$
m=0.99998,\quad \lambda_h=0.008,\quad K_{\rm ex}=0.34,
$$
$$
a_h=m^2-m\lambda_h=0.9919601604,
\quad b_h=(1-m/\lambda_h)(1-m)K_{\rm ex}=-0.000843183,
$$
$$
d_0=1-a_h-b_h=0.0088830226.
$$

These constants belong to the fixed original physical outer radius. Changed geometry requires its own exceptional constant, as audited in Round 5.

Define the face multipliers

$$
m_H=d_0\mathbf1_{H_0}+a_h\mathbf1_{H_1}+b_h,
\qquad
m_L=d_0\mathbf1_{L_0}+a_h\mathbf1_{L_1}+b_h.
\tag{4}
$$

Their respective values on the three nested regions are $1$, $a_h+b_h$, and $b_h$. The last value is negative. The implemented full-face mask $H_f$ contains the support of every erased marginal of an outer-supported profile, so writing the last term as $b_h\mathbf1_{H_f}$ in the finite engine gives the same quadratic forms as the unrestricted $b_h$ in (4). The source operators and the threshold-normalized operators are

$$
A=\sum_{i=1}^kE_i^*m_HE_i,\quad
B=\sum_{i=1}^kE_i^*m_LE_i,
$$
$$
T_{\rm cap}=\rho_*A,\qquad
T_{\rm inner}=\rho_*B,\qquad
T_{\rm arith}=\rho_*P_OBP_O.
\tag{5}
$$

Here $\rho_*=2624989/10^7$. Explicitly, the full cap action is

$$
(T_{\rm cap}f)(X)=\rho_*\mathbf1_{H_O}(X)
\sum_i m_H(X_{\widehat i})
\int f(X_{\widehat i}\oplus_i Z)\,d\nu(Z).
\tag{6}
$$

Replace $m_H$ by $m_L$ for $T_{\rm inner}$. For $T_{\rm arith}$, insert $\mathbf1_O$ both outside and inside the integral. Formula (6) defines the operator on the full Hilbert space, not only on polynomial profiles.

The cap quotient is $\langle f,T_{\rm cap}f\rangle/\|f\|^2$. The actual sieve quotient for $P_Of\ne0$ is

$$
\frac{\rho_*\langle P_Of,BP_Of\rangle}{\|P_Of\|^2}.
\tag{7}
$$

The denominator in (7) is essential. On all of $\mathcal H$, the denominator of the Rayleigh quotient of $T_{\rm arith}$ is $\|f\|^2$, which agrees with (7) only when $f=P_Of$. For the actual sieve problem one works on $L^2(O,\nu^k)$ or keeps this distinction explicit.

The arithmetic theorem requires more than a cap quotient exceeding one: the actual supported profile and source/realization hypotheses must hold. The restoration estimate is a lower bound on its quadratic form, not another fixed linear operator formed by subtracting independent error bars.

## 4. Boundedness and self-adjointness without positivity

All multipliers in (4) are real and bounded. Fubini and (3) imply self-adjointness of each term $E_i^*mE_i$. To give a bound independent of the much larger unrestricted mass, suppose $H_O$ has total support at most $S$. Put $t_j=|X_j|$, $\widehat s_i=\sum_{j\ne i}t_j$, and

$$
w_i=S-\widehat s_i+(k-1)t_i.
$$

Because the total density is at most one,

$$
\int_{H_O(Y)}\frac{d\nu(X_i)}{w_i}
\le\int_0^{S-\widehat s_i}
\frac{dt}{S-\widehat s_i+(k-1)t}
=\frac{\log k}{k-1}.
$$

The boundary $\widehat s_i=S$ has zero fiber measure. Weighted Cauchy–Schwarz followed by $\sum_iw_i=kS$ gives

$$
\sum_i\|E_if\|^2\le C_{\rm op}\|f\|^2,
\qquad C_{\rm op}=\frac{Sk\log k}{k-1}.
\tag{8}
$$

For the fixed $k=39$ geometry, the safe bound $C_{\rm op}\le4$ has an exact rational verification in the Round 5 source-geometry audit. Since $b_h\le m_H,m_L\le1$,

$$
-\rho_*|b_h|C_{\rm op}I
\le T_{\rm cap},T_{\rm inner},T_{\rm arith}
\le\rho_*C_{\rm op}I.
\tag{9}
$$

For the compressed operator $T_{\rm arith}$ these inequalities use that $P_O$ is an orthogonal projection. Also

$$
A-B=\sum_iE_i^*\{d_0(\mathbf1_{H_0}-\mathbf1_{L_0})
+a_h(\mathbf1_{H_1}-\mathbf1_{L_1})\}E_i\ge0.
$$

The negative full-face term cancels in this difference. None of these statements makes $A$ or $B$ positive semidefinite. In particular, a Perron–Frobenius argument, a positive-kernel power method, or a replacement of $b_h$ by $|b_h|$ would require a different justification and would change the problem.

If the trial and the domains are permutation invariant, these operators commute with coordinate permutations. Thus the symmetric subspace is invariant. The factor $k$ in the symmetric face formulas below comes from this symmetry, not from the erasure adjoint.

## 5. Exact mixed integrals and the information retained by fragments

For arbitrary profiles $f,g$, the true mixed form is

$$
\langle g,T_{\rm cap}f\rangle
=\rho_*\sum_i\int m_H(Y)\overline{E_ig(Y)}E_if(Y)\,d\nu^{k-1}(Y).
\tag{10}
$$

Expanding the two marginals introduces two independent erased coordinates conditional on the same retained configuration $Y$. It does not introduce two independent retained configurations. This is exactly the shared-root convention in the primary proof.

For symmetric $f$, direct calculation of $\|T_{\rm cap}f\|^2$ can reduce the double coordinate sum to $i=j$ and $i\ne j$. The first contribution has one shared retained tuple and two erased copies, together with the outer-fiber mass. The second has $k-2$ shared coordinates and four distinguished coordinate copies. They are different overlap integrals. A third operator moment has the finitely many equality patterns of three erasure indices, including the different placements of two equal indices. This is a useful organizational reduction, but no independence assumption between their shared cap states is valid.

The cap-only masks use each total cell and the largest fragment. Let all distinct positive caps be

$$
0<c_1<\cdots<c_L=\zeta,
$$

where a larger unused ambient cap can also be included. Partition a coordinate by its total cell $C_j=[jh,(j+1)h)$ and its fragment layer $c_{\ell-1}<\max X\le c_\ell$, with the layer-zero cumulative measure defined to be zero. The exact mass of this atom is

$$
\mu_{j\ell}=\int_{C_j}
\{\rho_D(t/c_\ell)-\rho_D(t/c_{\ell-1})\}\,dt.
\tag{11}
$$

For $\ell=1$ omit the second term. Empty or zero-mass atoms may be removed. Formula (11) is an exact pushforward of the fragment measure. It is not an approximation that concentrates continuous totals or fragments at a point.

For the companion's inward cell domains, outer membership is a function of the index sum $r=\sum j_i$ and the largest layer. Face membership is a function of $\widehat r_i$ and the largest retained layer. Therefore the finite subspace of functions constant on products of these atoms is invariant under $T_{\rm cap}$: integrating coordinate $i$ sums its atom values against $\mu_{j\ell}$, and all remaining arguments in (6) depend only on retained atom labels. The adjoint then produces an atom-constant output. Since $T_{\rm cap}$ is self-adjoint, this finite subspace is also reducing.

The official step trial lies in this subspace. Consequently its full $T_{\rm cap}f$ and its residual outside the 77-dimensional span lie there too. There is no uncomputed within-cell component of $T_{\rm cap}f$ for that trial and those fixed cell domains. The full Hilbert space still contains other, within-atom functions; no claim about its entire spectrum follows from this invariance alone.

The coordinate layers cannot in general be discarded. Knowing all total cells does not determine which outer-shell marginals survive after erasure. The action on coordinate $i$ depends on the largest retained fragment layer, and different erasures can leave different largest layers. Replacing this information by one global probability before taking products changes (10).

The actual predicates in $O,L_0,L_1$ involve activated fragments and inclusive prefix sums, such as $\max_{p>\xi}\{\sum_{q\ge p}q+\varphi(p)\}$. Equal total and equal largest fragment do not determine these values. Thus the preceding atom subspace generally is not invariant under $T_{\rm arith}$. More fragment information, exact conditional predicate averages, or a valid support-error argument is required there.

For clarity, product conjugation does not remove this issue. Write $G(X)=\prod_i g(t_i)>0$ and transfer $f=Gu$ to the mass $G^2d\nu^k$. The conjugated action is

$$
G^{-1}T_{\rm cap}G\,u(X)
=\rho_*\sum_i\frac{m_H(X_{\widehat i})}{g(t_i)}
\int\mathbf1_{H_O}(X_{\widehat i}\oplus_i Z)
g(|Z|)u(X_{\widehat i}\oplus_i Z)\,d\nu(Z).
\tag{12}
$$

There is one erased factor $g$, and a factor $1/g(t_i)$ outside. It is not a normalized average against $g^2d\nu$.

## 6. Full residual, nonnested radial compression, and the signed two-dimensional test

Let $U\subset\mathcal H$ be the span of the 77 step profiles and let $P_U$ be orthogonal projection in the true mass inner product. If $\phi_1,\ldots,\phi_{77}$ are an independent basis, put

$$
M_{ab}=\langle\phi_a,\phi_b\rangle,
\quad b_a=\langle\phi_a,Tf\rangle,
\quad P_UTf=\sum_a\phi_a(M^{-1}b)_a.
\tag{13}
$$

An exact nonsingular Gram matrix is needed; dependent basis vectors can instead be removed. Euclidean coefficient projection is not (13).

For any $f\in U$, define $r=(I-P_U)Tf$. Self-adjointness and orthogonality give

$$
\langle f,Tr\rangle=\langle Tf,r\rangle=\|r\|^2.
\tag{14}
$$

This does not require $f$ to be an exact Ritz eigenvector. An exact Ritz equation is required only to replace $P_UTf$ by a scalar multiple of $f$.

To avoid computing all of $r$, choose a closed subspace $V$ whose projection can be evaluated, and put

$$
v=P_Vr,\qquad w=(I-P_U)v.
\tag{15}
$$

Here $v$ is called `h` in the numerical implementation; the letter $h$ elsewhere in this note denotes the grid spacing. The spaces $U,V$ need not be nested. The projection order in (15) is essential. Since $r\perp U$,

$$
\langle f,Tw\rangle=\langle r,w\rangle
=\langle r,v\rangle=\|v\|^2,
\qquad
\|w\|^2=\|v\|^2-\|P_Uv\|^2.
\tag{16}
$$

In particular $\|w\|\le\|v\|\le\|r\|$, and $v\ne0$ forces $w\ne0$. The coupling is $\|v\|^2$, not generally $\|w\|^2$. The superficially similar direction $(I-P_U)P_VTf$ does not generally satisfy (16).

Set $F_2=\|f\|^2$, $q=\|v\|^2$, $z=\|w\|^2>0$,

$$
\lambda=\frac{\langle f,Tf\rangle}{F_2},\quad
\tau=\frac{\langle w,Tw\rangle}{z},\quad
\eta=\frac{q}{\sqrt{F_2z}}.
$$

The orthonormal basis $f/\sqrt{F_2},w/\sqrt z$ has the matrix

$$
\begin{pmatrix}\lambda&\eta\\\eta&\tau\end{pmatrix}.
$$

Its larger eigenvalue is

$$
\lambda_+=\frac{\lambda+\tau+
\sqrt{(\lambda-\tau)^2+4\eta^2}}2>\lambda.
\tag{17}
$$

No positivity of $T$ is used. For $\lambda<1$ and $\tau<1$, crossing one is equivalent to $\eta^2>(1-\lambda)(1-\tau)$. A certified lower bound $\tau\ge\tau_L$ gives a sufficient condition by substituting $\tau_L$. In the cap problem, (9) supplies the inexpensive choice $\tau_L=-\rho_*|b_h|C_{\rm op}$. Since $z\le q$, the still more conservative sufficient condition

$$
\frac{q}{F_2}>(1-\lambda)(1+\rho_*|b_h|C_{\rm op})
\tag{18}
$$

avoids calculating $\langle w,Tw\rangle$. It may be too weak numerically, but it is a valid signed-operator certificate. A strict positive improvement in (17) alone is not the threshold condition (18) or an arithmetic theorem.

## 7. An exact radial projection computed by one-dimensional convolutions

In this section $G$, every $P_\eta$, and every $g_j$ use the rational midpoint evaluations of the step trial; they are constant on their total cells. Take $V$ to consist of $\mathbf1_{H_O}G(X)a(r)$ with arbitrary values $a(r)$ on the retained radial cells. A fixed subset of radial cells may be used. Since the grid is finite, this is a closed subspace. It does not contain all 77 power-sum profiles.

Use the companion's un-tilted notation

$$
d_c(j)=h^{-1}\int_{C_j}\rho_D(t/c)dt,\quad
Z=\sum_{j<n}g_j^2,\quad
K_c(j)=g_j^2d_c(j)/Z.
$$

Let $M_{d,\sigma}^c(s)$ be the coefficient sequence obtained by integrating $G^2P_\sigma$ over $d$ coordinates with index sum $s$, common cap $c$, and normalization $(hZ)^{-d}$. This is exactly the positive-partition convolution moment of the numerical companion. Define

$$
\Delta M_{d,\sigma}^{\ell}(s)
=M_{d,\sigma}^{c_\ell}(s)-M_{d,\sigma}^{c_{\ell-1}}(s).
$$

For the lowest layer the second sequence is zero. Let $c_O(r)$ be the inward outer cap on radial cell $r$, with all formulas zero outside the outer radial masks. The mass density of the radial subspace, in the common normalization $(hZ)^{-k}$, is

$$
D(r)=M_{k,\varnothing}^{c_O(r)}(r),
\qquad \|Ga\|^2=\sum_rD(r)|a(r)|^2.
\tag{19}
$$

For the input polynomial profile $f$, let $a_{\ell,\eta}(s)$ denote the signed prefix sum of the allowed outer-shell affine rows of the companion. Thus on a background of index sum $s$ whose largest fragment lies in layer $\ell$,

$$
E_if(Y)=hG(Y)\sum_\eta a_{\ell,\eta}(s)P_\eta(Y).
\tag{20}
$$

One must sum the permitted shell rows with their signs before forming any products. Put

$$
B_\ell(s)=\sum_\eta a_{\ell,\eta}(s)
\Delta M_{k-1,\eta}^{\ell}(s),
$$

and let $m_\ell(s)$ be the signed face multiplier (4) on this layer. Direct substitution of (20) into the mixed integral (10) gives the normalized radial adjoint density

$$
N_T(r)=\frac{\rho_*kh}{Z}
\sum_{\ell:c_\ell\le c_O(r)}
\sum_{j+s=r}
g_jd_{c_O(r)}(j)\,m_\ell(s)B_\ell(s).
\tag{21}
$$

More explicitly, $\langle Ga,Tf\rangle=\sum_r\overline{a(r)}N_T(r)$. To verify the factor, each erased marginal contributes $h$, the retained $k-1$ coordinates contribute $(hZ)^{k-1}$, all forms are divided by $(hZ)^k$, and symmetry supplies $k$. Their product is $kh/Z$. The test function's erased coordinate contributes exactly one factor $g_jd_c(j)$.

It follows that

$$
P_VTf=G\,\frac{N_T(r)}{D(r)}
\tag{22}
$$

where $D(r)>0$; on zero-mass cells the value is immaterial. No distribution of fragments has been replaced by a conditional mean before the product. The layer sums in (21) perform the required conditional integration explicitly.

If $N_U(r)$ is the radial mixed density of the profile $P_UTf$, then

$$
v=P_V(I-P_U)Tf
=G\,\frac{N_T(r)-N_U(r)}{D(r)},
$$
$$
q=\|v\|^2=\sum_r\frac{|N_T(r)-N_U(r)|^2}{D(r)}.
\tag{23}
$$

The sequence $N_U$ is obtained from the ordinary $k$-coordinate moments for the coefficients in (13). Both the projection and (23) therefore use the full mass measure. Restricting to any predetermined set of positive-mass radial cells preserves all the identities in (15)–(16); it only chooses a smaller $V$.

The independent mixed forms $\langle\phi_a,Tv\rangle$ and $\langle v,Tv\rangle$ follow from the same signed face formula by replacing the radial polynomial of one or both inputs by the arbitrary sequence in (23). This gives a direct two-dimensional or 78-dimensional Rayleigh calculation without evaluating $\|Tf\|^2$ and without assuming that the radial projection captures the entire residual.

### Numerical exponential tilt is only a normalization device

The exploratory engine uses $Z_\theta=\sum_jg_j^2e^{-\theta t_j^\circ}$ and moments built from $g_j^2e^{-\theta t_j^\circ}d_c(j)/Z_\theta$. In (19) multiply the resulting moment by $e^{\theta(r+k/2)h}$. In (21), use $Z_\theta$ and multiply $B_\ell(s)$ by $e^{\theta(s+(k-1)/2)h}$. The affine rows in (20) continue to use the un-tilted erased factor $g_jd_c(j)$. These substitutions exactly undo the tilt in the actual product measure.

When combining forms evaluated at two tilts, first convert every norm and pairing to the same common normalization. Converting from the current $Z_\theta$ normalization to a reference $Z_{\theta_0}$ multiplies all forms by $(Z_\theta/Z_{\theta_0})^k$. The true operator, projections, and Rayleigh quotient do not depend on the numerical tilt.

## 8. Independent review, current limits, and the next proof obligation

The Round 6 script `residual-trial/radial_residual.py` was reviewed against (19)–(23). Its `radial_adjoint` has the correct face dimension $k-1$, the factor $\rho_*kh/Z$, one erased $g$, the signed sum of permitted outer-shell affine rows, cap-layer differences, and the background exponential correction. Its computation of $P_UTf$ uses the mass Gram solve, rather than assuming an exactly solved Ritz equation. Its active radial-cell cutoff is a legitimate choice of a smaller $V$ in ordinary mathematics. Floating-point negative mass or Gram uncertainty is not thereby certified away.

The separate exact rational regression `operator-diagnostic/finite_marked_operator_check.py` was also inspected. It uses nonuniform masses, a nonrectangular cap domain, and nonnested trial/radial spaces. The source verifies mass self-adjointness, (14), (16), product conjugation, a projection-order counterexample, and a negative quadratic witness equal to $-1/38880$. This is a structural test of the identities; its five-atom measure is not the Dickman measure and gives no $k=39$ numerical bound.

The earliest computational issue for a rigorous cap improvement is now precise: enclose the Dickman cell masses, Gram projection, radial adjoint density, and signed mixed forms coherently, or rationalize a chosen new radial profile and outwardly certify its ordinary mass and cap forms. A floating-point projected residual may be a useful way to select a profile, but its exact orthogonality is not needed after a concrete rational profile is fixed and its two-dimensional Gram and numerator forms are certified directly. This avoids pretending that numerically computed projections are exact.

The next arithmetic issue is separate and harder. A new radial profile changes the weights of the retained and deleted fragment configurations. The old outer failure covers, old inner loss numbers, and the Round 4 positive alpha credit cannot simply be reused with their old numerical values. One must evaluate their valid formulas for the new profile, or evaluate the actual predicates directly with sufficient retained fragment state. The cap operator is an exact relaxed operator at the fixed grid; it is not the actual supported sieve operator.

This closes the ordinary operator derivation. It justifies a concrete out-of-77-space search direction and a signed two-dimensional test. It does not establish a threshold crossing, a complete support-restored $k=39$ trial, or a prime gap below 186.
