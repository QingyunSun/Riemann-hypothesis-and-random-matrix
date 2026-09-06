# Residual directions outside the 77-dimensional sieve trial space

**Status:** independent algebraic and measure-theoretic audit. The operators below are the finite-dimensional-sieve variational operators from the prime-gap programme, not any earlier zeta-zero operator. No positive-semidefinite assumption is made. No new prime-gap result is established.

Primary inputs checked: [*Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), §4.4, equations (4.30)–(4.40), and §4.1–§4.2; the retained local text is ../../sources/openai-short-gaps.txt, SHA256 ded13a7c74fcfce64e85769e05b5869803dccdf53b88be2c2f3c0b344f95ee84. Current cap-engine files checked were cap_trial.py and optimize_cap.py in the published round-5 geometry-trial directory. In particular, their denominator uses the product g² measure, their erased-coordinate kernels contain one factor g, and their signed face multiplier retains the negative b_h term. They are exploratory cap-form engines, not evaluations of the fully restored arithmetic form.

## 1. The two operators that must remain distinct

Let

\[
\mathcal H=L^2(H_O,d\nu^{\otimes k}),\qquad k=39,
\]

with every function extended by zero outside H_O. The measure is the unscaled fragment measure of the primary paper, not a probability measure conditioned on H_O. Its norm is the outer-square mass.

For a retained configuration Y=X with coordinate i erased, define

\[
(E_i f)(Y)=\int 1_{H_O}(Y,X_i)f(Y,X_i)\,d\nu(X_i).
\tag{1}
\]

The face space has measure dnu^(k−1), with no division by the mass of this fibre. Consequently

\[
(E_i^*v)(X)=v(X_{\widehat i})\quad (X\in H_O).
\tag{2}
\]

The indicator of H_O belongs in (2) if the ambient space is instead written as the full product space. Fubini proves the adjoint relation immediately. Replacing (1) by a conditional expectation changes the operator and its variational value.

The **relaxed cap operator** is

\[
T_{\rm cap}=\rho_* A,
\qquad A=\sum_i E_i^*
\bigl(d_0 1_{H_{0,i}}+a_h1_{H_{1,i}}+b_h\bigr)E_i.
\tag{3}
\]

The **actual support-restored operator**, on the supported subspace or extended by zero, is

\[
T_{\rm arith}=\rho_*P_O B P_O,
\qquad B=\sum_i E_i^*
\bigl(d_0 1_{L_{0,i}}+a_h1_{L_{1,i}}+b_h\bigr)E_i.
\tag{4}
\]

Here P_O is multiplication by the actual outer support indicator, and L_0⊂L_1 are the actual inner domains. The source establishes A−B≥0 because the negative full-face term cancels in their difference. It does not identify A with B, and it does not imply an ordering of the two operators after arbitrary changes of their outer trial functions.

A direction generated for T_cap can establish an improvement of the relaxed cap variational problem. It does not by itself establish a positive restored arithmetic form. If the basis is subsequently changed from u_a to P_Ou_a, its Gram matrix and projection both change. One cannot reuse the old 77-dimensional projection after this support change.

Both operators are bounded and self-adjoint. If

\[
\sum_iE_i^*E_i\le C_{\rm op}I,
\qquad b_h<0,\quad 0<a_h+b_h<1,\quad d_0+a_h+b_h=1,
\]

then the three possible multipliers are 1, a_h+b_h and b_h. Thus

\[
-mI\le T\le MI,\qquad
m=\rho_*|b_h|C_{\rm op},\quad M=\rho_*C_{\rm op},
\tag{5}
\]

for either operator, with the operator bound proved for its actual domain. The negative term must not be dropped when taking a lower bound. In the original geometric range the paper's argument gives C_op≤S k log(k)/(k−1); using C_op=4 requires the corresponding numerical inequality. Nothing here assumes T≥0.

## 2. Mass conjugation and the radial projection

Write G(X)=product_i g(t_i), where t_i is the coordinate total or its specified step representative. If amplitudes p=f/G are used, their Hilbert mass is G² dnu^k, restricted to H_O. Conjugation gives

\[
G^{-1}T_{\rm cap}(Gp)(X)
=\rho_*\sum_i\frac{m_i(X_{\widehat i})}{g(t_i)}
\int 1_{H_O}(X_{\widehat i},Y_i)
g(t(Y_i))p(X_{\widehat i},Y_i)\,d\nu(Y_i).
\tag{6}
\]

This identity explains why denominator kernels contain g², whereas each erased-coordinate marginal contains one factor g. Putting g² in the latter integral without its compensating conjugation factors is a different operator.

Let sigma(X) be the chosen radial observable: either the true sum of totals, or explicitly the sum of coordinate-cell indices in the fixed step model. Let V be the closed subspace

\[
\mathcal V=\{G(X)\phi(\sigma(X)):\phi\in L^2(q)\},
\quad q=\sigma_*\bigl(1_{H_O}G^2\nu^{\otimes k}\bigr).
\tag{7}
\]

No assumption that V contains the 77-dimensional polynomial space U is appropriate: it generally does not. For f∈H define the pushed-forward signed measures

\[
d_f=\sigma_*(1_{H_O}Gf\nu^{\otimes k}),\qquad
b_f=\sigma_*(1_{H_O}G(Tf)\nu^{\otimes k}).
\]

They have Radon–Nikodym derivatives relative to q, and

\[
P_{\mathcal V}(Tf-\lambda f)
=G\left(\frac{db_f}{dq}-\lambda\frac{dd_f}{dq}\right).
\tag{8}
\]

When all three measures have densities, this is the proposed formula G(b_f(s)−lambda d_f(s))/q(s). For a cell-index radial observable it is a ratio of discrete masses at each index, not a continuous-density formula. Set the ratio to zero on a zero-mass radial cell.

This is a genuine orthogonal projection because its error is orthogonal to every G phi(sigma), directly from the defining pushforward identity. It remains valid with fragment-dependent cap indicators, provided those indicators are included before taking each pushforward.

The one-coordinate mass of a retained cell with maximum fragment at most c h is

\[
\nu\{t\in[jh,(j+1)h),\ \max\text{fragment}\le ch\}
=h\int_0^1\rho_D((j+u)/c)\,du.
\tag{9}
\]

The survival average alone omits h. A common overall normalization of all outer Hilbert masses is harmless, but independently normalizing face and outer masses changes the adjoint unless the ratio is carried through. In the engine's tilted convolution representation, factors h, Z and the exponential untilt must therefore be kept consistently for the new cross forms as well as the original Gram matrix.

## 3. The direct outside-space residual needs no Ritz hypothesis

Let U be a finite-dimensional subspace of H, P its **true Hilbert orthogonal projection**, and Q=I−P. Let f∈U be a unit vector and put

\[
\lambda=\langle f,Tf\rangle,
\qquad r=QTf.
\]

If a=||r||>0 and v=r/a, then f and v are orthonormal, and

\[
\langle f,Tv\rangle
=\langle Tf,v\rangle
=\frac{\langle QTf,QTf\rangle}{a}=a.
\tag{10}
\]

This identity is true for **every** f∈U, not just an exact Ritz vector. Exact Ritz status means PTf=lambda f, and is needed only to identify Tf−lambda f with QTf.

For an approximate Ritz vector define e=PTf−lambda f. Then

\[
Tf-\lambda f=e+r,\quad e\perp r,\qquad
\|r\|^2=\|Tf-\lambda f\|^2-\|e\|^2.
\tag{11}
\]

Thus the full eigen-equation residual can overstate the outside-U residual. A tiny residual in the 77-by-77 matrix only controls e for that compressed matrix; it says nothing about r until an additional operator action or outside-space form is evaluated.

With mu=〈v,Tv〉, the larger Ritz value on span{f,v} is exactly

\[
\Lambda_2=\frac{\lambda+\mu+
\sqrt{(\lambda-\mu)^2+4a^2}}2.
\tag{12}
\]

If lambda<1, the signed lower bound mu≥−m implies the sufficient crossing test

\[
a^2>(1-\lambda)(1+m)
\quad\Longrightarrow\quad \sup\sigma(T)>1.
\tag{13}
\]

If mu is itself evaluated, the sharper test for lambda<1 and mu<1 is a²>(1−lambda)(1−mu). The formula (12) also handles the other cases. The result follows from the two-dimensional Rayleigh principle and uses no positive-semidefiniteness of T.

## 4. Nonnested radial compression: the correct coupling

First suppose f is an exact Ritz vector in U, so r=Tf−lambda f. Define

\[
h=P_{\mathcal V}r,\qquad w=Qh.
\tag{14}
\]

Then

\[
\langle Tf,w\rangle
=\langle r,Qh\rangle
=\langle r,h\rangle=\|h\|^2.
\tag{15}
\]

The last equality uses orthogonality of P_V; the preceding one uses r⊥U. If h≠0, then w≠0: otherwise (15) would equate zero with ||h||². For the normalized new direction v=w/||w|| the coupling is

\[
\beta=\langle f,Tv\rangle
=\frac{\|h\|^2}{\|w\|}\ge\|w\|.
\tag{16}
\]

It is generally **not** ||w||. The exact identity ||h||²=||Ph||²+||w||² explains the difference. This is the appropriate coupling for the proposed arbitrary-radial compressed direction, and the test (13) uses beta² in place of a².

For a general approximate Ritz pair, let lambda be any specified real scalar and define

\[
e=PTf-\lambda f,\qquad h=P_{\mathcal V}(Tf-\lambda f),\qquad w=Qh.
\]

An exact calculation gives

\[
\boxed{\langle Tf,w\rangle=\|h\|^2-\langle e,Ph\rangle.}
\tag{17}
\]

Indeed, 〈Tf,Qh〉=〈Tf−lambda f,h〉−〈e,h〉, and the first term is ||h||² by radial orthogonal projection. Hence if ||e||≤eta,

\[
\left|\langle f,T(w/\|w\|)\rangle\right|
\ge\frac{(\|h\|^2-\eta\|Ph\|)_+}{\|w\|}.
\tag{18}
\]

For complex spaces take the real part in (17), or choose the phase of the new vector; all proposed sieve arrays are real. If h was computed with Tf−lambda f instead of the exact QTf, the discrepancy is P_V e and has norm at most eta. It must not be silently discarded.

When lambda in (17) is merely a numerical Ritz approximation, it is not automatically the true diagonal 〈f,Tf〉 needed in the two-by-two crossing criterion. Enclose that diagonal separately or include its error in the scalar lower bound.

## 5. Approximate action, radial compression and projection errors

### 5.1 Direct action with a rigorous error

Suppose g approximates Tf with ||g−Tf||≤epsilon. Define a=||Qg|| and v=Qg/a. Then

\[
\left|\langle f,Tv\rangle\right|\ge(a-\epsilon)_+.
\tag{19}
\]

This follows from 〈Tf,Qg〉=||Qg||²+〈Tf−g,Qg〉. It requires an error in the true Hilbert mass, not a Euclidean array error without mass weights.

### 5.2 Approximate radial projection

Let h be as in (17). Suppose a computed h_tilde belongs to V and ||h_tilde−h||≤epsilon. Set w_tilde=Qh_tilde. Because h_tilde∈V,

\[
\langle Tf,w_{\rm tilde}\rangle
=\|h_{\rm tilde}\|^2
+\langle h-h_{\rm tilde},h_{\rm tilde}\rangle
-\langle e,Ph_{\rm tilde}\rangle.
\]

Consequently,

\[
\beta_{\rm lower}=
\frac{(\|h_{\rm tilde}\|^2
-\epsilon\|h_{\rm tilde}\|
-\eta\|Ph_{\rm tilde}\|)_+}
{\|Qh_{\rm tilde}\|}
\tag{20}
\]

is a valid coupling lower bound whenever the denominator is positive. If membership in V is itself only approximate, the displayed identity needs an additional error: simply declaring a numerical vector to be a radial projection is insufficient.

For interval data write A=||h_tilde||², L=||Ph_tilde||² and W=||Qh_tilde||²=A−L. If certified bounds A≥A_−, A≤A_+, L≤L_+, W≤W_+ and W>0 are known, then the conservative computable bound is

\[
\beta\ge
\frac{(A_- -\epsilon\sqrt{A_+}-\eta\sqrt{L_+})_+}
{\sqrt{W_+}}.
\tag{21}
\]

The upper denominator is intentional. Using a lower bound for W there would reverse the desired inequality. A separate positive lower bound for W certifies that the new vector is outside U and may be normalized.

### 5.3 A genuinely compressed Galerkin space

If a larger space W contains U and its projection is P_W, then

\[
(P_W-P)Tf=P_W(QTf),
\qquad
\|QTf\|^2=\|(P_W-P)Tf\|^2+\|(I-P_W)Tf\|^2.
\tag{22}
\]

A rigorously evaluated nonzero compressed residual is a valid lower witness even without a bound on the omitted tail. A small compressed residual gives no upper bound on the full residual. The nonnested radial space V is not itself such a W; confusing (22) with (14) produces the incorrect coupling ||w||.

### 5.4 Approximate projectors

If ||P_hat−P||≤delta and ||g−Tf||≤epsilon, then

\[
\|(I-P_{\rm hat})g-QTf\|
\le\epsilon+\delta\|g\|.
\tag{23}
\]

But (I−P_hat)g may not lie in U-perp. Reorthogonalize in the true mass, or account for its leakage, before using an orthonormal two-by-two formula. There is no automatic permission to replace the true Gram projection by Euclidean coefficient subtraction.

## 6. Inverse-Gram errors and an easier final certificate

Let u_1,...,u_d be a basis of U, G_ab=〈u_a,u_b〉 its positive-definite Gram matrix, and g_a=〈u_a,h〉. Then

\[
\|Ph\|^2=g^*G^{-1}g,
\qquad \|Qh\|^2=\|h\|^2-g^*G^{-1}g.
\tag{24}
\]

An ill-conditioned Gram matrix can turn tiny entry errors into a large error in this difference. The following residual formulation is often preferable. For any proposed projection coefficient vector c_0, put b=g−Gc_0 and z_0=h−sum_a(c_0)_a u_a. Then

\[
\boxed{\|Qh\|^2=\|z_0\|^2-b^*G^{-1}b.}
\tag{25}
\]

If gamma>0 is a lower bound for the smallest Euclidean eigenvalue of the exact G,

\[
\|Qh\|^2\ge\|z_0\|^2-\|b\|_2^2/\gamma.
\tag{26}
\]

For an approximate matrix G_hat with ||G−G_hat||≤epsilon_G, a valid choice is gamma=lambda_min(G_hat)−epsilon_G if positive. If g_hat and G_hat are used to solve for c_0, bound

\[
\|b\|_2\le\|g_{\rm hat}-G_{\rm hat}c_0\|_2
+\epsilon_g+\epsilon_G\|c_0\|_2.
\tag{27}
\]

Near-null basis modes cannot be declared harmless simply because a floating-point solver truncates them. Either define U to be exactly the retained smaller span, or certify the conditioning and projection error for the full span being claimed.

For a final gain certificate, a concrete profile and its directly evaluated mixed forms can avoid the entire operator-action error problem. Let A and G be the true numerator and mass matrices on any explicitly specified finite span, possibly the old 77 vectors plus one new radial vector. Suppose entrywise interval errors around A_hat,G_hat are epsilon^A_ab,epsilon^G_ab. For a fixed real coefficient vector c, the sufficient test

\[
c^T(A_{\rm hat}-G_{\rm hat})c
>\sum_{a,b}|c_ac_b|
(\epsilon^A_{ab}+\epsilon^G_{ab})
\tag{28}
\]

proves the Rayleigh quotient of the actual represented function exceeds one, provided its mass is positive. This test permits negative b_h and does not require either a matrix inverse or T≥0. Rationalize the chosen coefficients before certification so they are fixed quantities, rather than uncertain optimization outputs.

When working with a two-dimensional orthonormal block and separate certified values lambda≥lambda_−, mu≥mu_−, |coupling|≥c_−, its largest eigenvalue is at least

\[
\frac{\lambda_-+\mu_-+
\sqrt{(\lambda_- -\mu_-)^2+4c_-^2}}2.
\tag{29}
\]

The larger eigenvalue is monotone in each diagonal and in the magnitude of the off-diagonal entry. Equation (29), or (28), should be used instead of relying on the sign of a tiny rounded numerical improvement.

## 7. Function class, fragment labels and arithmetic admissibility

The full action of T_cap can introduce dependence on retained largest-fragment labels and on which cap layers survive, even when the initial amplitude depends only on coordinate totals. This occurs because both the face multiplier and the outer fibre domain depend on retained fragments. A totals-only formula for Tf that has discarded those labels is generally not the full action.

The radial projection in (8) deliberately integrates those labels out. It is legitimate if every outer/inner layer and signed contribution is included in its pushforward mass. It can remain in the original class of cap-supported total-coordinate profiles while leaving the 77-dimensional polynomial subspace. A verified W>0 in Section 5 or Section 6 is the precise certificate of leaving that span; a visual impression that the radial function is not a polynomial is not a substitute.

Projection is well-defined in L² even when q is very small. In the present fixed compact support, g is continuous and strictly positive, so G has a positive lower bound. If f is bounded, the finite-k integral action is bounded, and the radial coefficient can be viewed as a weighted conditional average of (Tf−lambda f)/G. Thus it too is bounded; division by a small q does not create an analytic singularity in the exact projection. It can nevertheless cause serious numerical cancellation. Thresholding or regularizing small q changes the direction and must be followed by a direct norm/form evaluation.

The cleanest explicit function class is a bounded radial step function on a fixed finite mesh. Such a profile has limiting-null cell boundaries under the same continuous total-size measures used by the source. Additional finite-band approximation can then follow the source's existing method. A generic L² eigenvector need not already satisfy the source's bounded-profile and limiting-null-discontinuity hypotheses; approximate it by a fixed admissible profile while retaining any certified margin. Boundedness of T controls this step: for vectors x,y,

\[
|\langle x,Tx\rangle-\langle y,Ty\rangle|
\le\|T\|\,\|x-y\|(\|x\|+\|y\|).
\tag{30}
\]

For the actual arithmetic problem, the profile must additionally be projected to O and meet the inner-domain/source hypotheses. A cap gain, even one above one, has not paid those support losses. That obligation remains explicit rather than being included implicitly in the new residual direction.

## 8. Deliverable and stopping rule

The useful next numerical output is a concrete bounded radial profile, its outside-U mass, its signed mixed forms, and a direct reevaluation of the optimized enlarged-span vector. Label floating-point values exploratory. If a convincing cap gain survives independent contractions, fix the profile and certify the necessary entries or a single explicit quadratic combination with outward arithmetic. Only after that should support restoration be attempted for that new function.

This audit does not recommend another coefficient-only optimization of the same 77-dimensional span, a zeta operator experiment, a PSD replacement of the signed sieve form, or a conclusion based on a tiny compressed residual. The intended new mathematical information is a rigorously measured component of the actual cap-operator action outside the existing span.

## 9. Exact small-model checks

The accompanying exact_residual_checks.py uses only Python's Fraction arithmetic and writes exact_residual_checks.json. All checks passed:

- 80 rational five-dimensional examples with a nonuniform mass, a self-adjoint operator having an explicit negative Rayleigh direction, and a radial-analogue subspace not containing U.
- Direct residual, nonnested radial coupling, approximate-Ritz correction, approximate radial-action identity, and the exact inverse-Gram correction (25).
- Three adjoint checks on a 23-point product-measure support, with an explicit nonzero discrepancy when an incorrect conditional-fibre normalization is substituted.
- The conjugated single-g integral in (6), and all five discrete radial projection conditions in (8).

One exact-Ritz example has ||h||²=7544/406125, ||Qh||²=9572/676875 and 〈Tf,Qh〉=7544/406125. Thus the two competing unnormalized coupling formulas are distinguishable in exact arithmetic. The same example has a negative Rayleigh witness −1/9. These checks are structural tests of the audit formulas, not estimates of the k=39 operator or evidence of an improved cap quotient.
