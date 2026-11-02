# Identical static pair data, different heat evolution

Date: 2026-11-01 (Pacific); reviewed 2026-11-02 UTC. New counterexample programme authorized after the previous programme's closeout. Author: Astra root; independent checks by the stationary-challenge agent are recorded separately. The initial draft inherited the old programme's September date; this heading is corrected to the live session date.

## What is proved, and what is not

We give exact finite counterexamples to two proposed reconstruction principles:

1. Complete static pair correlation, even together with the minimum gap, determines the first backward scalar-heat collision time.
2. Complete static pair correlation, even together with the entire nearest-neighbour gap histogram, determines the subsequent pair correlation under scalar heat.

Both principles are false on the actual support of ACUE. Moreover, an explicit positive perturbation of the **ACUE probability law itself** preserves the joint distribution of all static pair statistics and the nearest-neighbour gap histogram, while changing its subsequent heat response. The witnesses are real, reflection-invariant constructions, so their distinction is not an orientation artifact.

These are model-level statements. They do not refute Montgomery's conjecture, the GUE conjecture, RH, or AH for the actual zeros of zeta. We are not attributing either reconstruction principle to Montgomery, Dyson or Tao. Homometry and the half-filled complement identity are classical; the result assembled here concerns their exact interaction with the heat observables used in this programme. External novelty has not been established.

## 1. Conventions and the complement identity

Let K=2N and let S be an N-element subset of the cyclic group Z/K. Its complement is C. Write z=exp(2 pi i/K), and

\[
p_m(S)=\sum_{a\in S}z^{ma},\qquad
c_S(r)=\#\{(a,b)\in S^2:a-b=r\pmod K\}.
\]

Expanding (1-1_S(a))(1-1_S(a-r)) proves, for every r,

\[
c_C(r)=K-2N+c_S(r)=c_S(r).
\tag{1}
\]

Thus the full ordered pair-difference measure, including or excluding its identical diagonal, is equal. Equivalently, |p_m(S)|^2=|p_m(C)|^2 for every integer m. At frequencies not divisible by K, p_m(C)=-p_m(S); at multiples of K both equal N. This is an equality of the complete data, not just a low-frequency approximation.

The ACUE probability of an unordered subset is

\[
P_A(S)=K^{-N}\prod_{a<b\in S}|z^a-z^b|^2.
\tag{2}
\]

Since the product is a function of the pair-difference counts, P_A(S)=P_A(C)>0. Translation and reflection preserve these probabilities. Independent uniform rotation of the entire configuration makes the resulting circular ensemble rotation invariant.

For a configuration of N angles x_j, take a nonzero real multiple of

\[
H_0(x)=\prod_{j=1}^N\sin((x-x_j)/2),\qquad
H_t=e^{-t\partial_x^2}H_0.
\]

Positive t multiplies Fourier frequency k by exp(k^2 t). At a simple zero,

\[
x_j'(t)=\frac{H_t''(x_j)}{H_t'(x_j)}
=\sum_{k\ne j}\cot((x_j-x_k)/2)=:V_j.
\tag{3}
\]

This is deterministic scalar heat, with radians as the spatial coordinate; it is not Dyson Brownian motion. Define D as the first backward time magnitude at which simplicity is lost, starting from t=0 and following these real zeros. Our explicit examples also show nonreal zeros immediately beyond this first collision.

## 2. Four particles: complete pairs and minimum gap do not determine depth

Take

\[
S=\{0,1,3,4\},\qquad C=\{2,5,6,7\}\subset\mathbb Z/8.
\tag{4}
\]

Both have minimum angular gap pi/4. Their cyclic gap lists, in lattice units, have sorted versions (1,1,2,4) and (1,1,3,3). The pair measures agree by (1), despite the different gap histograms.

After rotating the angles by -pi/2, the zero sets are respectively

\[
\{-\pi/2,-\pi/4,\pi/4,\pi/2\},\qquad
\{0,\pi,3\pi/4,-3\pi/4\}.
\]

Their real trigonometric polynomials can be chosen as

\[
F_0(x)=2\cos(2x)-2\sqrt2\cos x+2,
\qquad
G_0(x)=2\sin(2x)+2\sqrt2\sin x.
\tag{5}
\]

Consequently

\[
F_t(x)=2e^{4t}\cos(2x)-2\sqrt2e^t\cos x+2,
\quad
G_t(x)=2\sin x\bigl(2e^{4t}\cos x+\sqrt2e^t\bigr).
\tag{6}
\]

For G the two moving roots have cos x=-2^{-1/2} exp(-3t). They collide at x=pi when t=-log(2)/6; together with the fixed root this is a triple zero. Before this time all four roots are distinct and real, and just after it the two moving roots are nonreal. Thus

\[
D_C=\frac{\log2}{6}=0.115524530093324218\ldots.
\tag{7}
\]

For F, put y=exp(2t), c=cos x. Its zero equation is

\[
4y^2c^2-2\sqrt{2y}\,c+2-2y^2=0.
\tag{8}
\]

The discriminant equals 8y(4y^3-4y+1). Let y_* be the largest real root of 4y^3-4y+1. It lies in (4/5,1), where this cubic is strictly increasing. For y_*<y<=1 the two roots in c are distinct and belong to [0,1). To check that they do not escape at an endpoint: their sum is positive and product nonnegative; their vertex is c_0=(2 sqrt2 y^{3/2})^{-1}<1; and both endpoint values at c=+-1 are positive. For the nontrivial endpoint c=1, putting u=sqrt y gives

\[
F_t(0)=2(u^4-\sqrt2 u+1)\ge\frac12,
\]

because the bracket has global minimum 1/4 at u=1/sqrt2. At y=y_* the interior c roots coincide, producing two simultaneous double zeros on the circle. Immediately below y_* the discriminant is negative. Therefore

\[
D_S=-\frac12\log y_*
=0.0886279433267283324\ldots.
\tag{9}
\]

The strict difference does not depend on floating arithmetic: y_*>4/5 and (4/5)^3>1/2 imply y_*>2^{-1/3}, hence D_S<D_C. The checker also isolates y_* inside a rational interval of width 10^{-11}. Decimal logarithms are explanatory evaluations, not interval certificates.

**Conclusion:** even all static pair data and the minimum gap together fail to reconstruct backward heat depth. Every statistic that is a function of that complete pair measure also agrees; this includes singular pair sums when evaluated on these simple configurations.

## 3. An exact forward-time distinction

From (3), or direct pairwise cancellation,

\[
Lp_1=-(N-1)p_1,\qquad
Lp_2=-2(N-2)p_2-2p_1^2.
\tag{10}
\]

Let \(T(S)=\operatorname{Re}(p_1(S)^2\overline{p_2(S)})\). Then

\[
L|p_2|^2=-4(N-2)|p_2|^2-4T(S).
\tag{11}
\]

For complements and N>=2, p_1 and p_2 change sign (these frequencies are not multiples of 2N), so T changes sign. Solving (10), for every forward time t>=0,

\[
p_2(\Phi_tS)=e^{-2(N-2)t}
\left[p_2(S)-p_1(S)^2(1-e^{-2t})\right].
\tag{12}
\]

Hence the exact difference is

\[
|p_2(\Phi_tS)|^2-|p_2(\Phi_tC)|^2
=-4T(S)e^{-4(N-2)t}(1-e^{-2t}).
\tag{13}
\]

For (4), using the original unrotated angles, p_1=i sqrt2, p_2=2, T=-4. The derivatives are -16 and -48. The full-time difference is 16 exp(-8t)(1-exp(-2t)), strictly positive for t>0.

The missing information is an explicit balanced third-order trace statistic, T; it is not contained in the static pair measure. This also explains the limitation of the example: the two laws do not match all the protected mixed moments in Tao's low-degree theorem. In particular T has positive and negative weight two, and already distinguishes them. They cannot serve as countermodels to a statement that assumes those additional mixed moments.

## 4. Six particles: preserve the entire nearest-gap histogram as well

Now take

\[
A=\{0,1,2,4,7,8\},\qquad
B=\{3,5,6,9,10,11\}\subset\mathbb Z/12.
\tag{14}
\]

These are complements and are not rotations or reflections of one another. Both have sorted cyclic gap list

\[
(1,1,1,2,3,4).
\tag{15}
\]

They have identical full pair measure, identical complete nearest-gap histogram, and identical minimum gap. Exact evaluation gives

\[
|p_2|^2=7,\qquad T(A)=2,\quad T(B)=-2,
\]

so (11) is -120 for A and -104 for B. For all t>=0 their form-factor difference is

\[
-8e^{-16t}(1-e^{-2t}).
\tag{16}
\]

Thus even adding the entire nearest-neighbour gap histogram to the complete pair data does not close this dynamical reconstruction problem. The order of consecutive gaps and higher correlation data are not assumed matched.

## 5. Perturb the ACUE law itself, retaining the complete static summary law

Let O_A and O_B be the dihedral orbits of (14), under the 12 translations and reflection. They are disjoint, each contains 24 subsets, and complement interchanges them. Each subset in either orbit has ACUE probability exactly 1/1728. Therefore each orbit has mass 1/72.

Set h(S)=1 on O_A, h(S)=-1 on O_B, and h(S)=0 elsewhere, and for |epsilon|<=1 define

\[
P_\epsilon(S)=P_A(S)(1+\epsilon h(S)).
\tag{17}
\]

This is a probability distribution: it is nonnegative, and the two modified orbits have equal masses. It preserves translation and reflection invariance. Add an independent uniform global rotation if continuous rotational invariance is desired.

More strongly, let Q(S) denote the **joint object** consisting of its full ordered pair-difference measure and its sorted cyclic gap list. Q is constant with the same value on O_A union O_B. Therefore for every function f of this static summary,

\[
\mathbb E_\epsilon f(Q)=\mathbb E_A f(Q).
\tag{18}
\]

This preserves the whole distribution of Q, not only its mean and not only finitely many selected pair statistics. Nevertheless, by (16),

\[
\mathbb E_\epsilon |p_2(\Phi_tS)|^2
-\mathbb E_A |p_2(\Phi_tS)|^2
=-\frac{\epsilon}{9}e^{-16t}(1-e^{-2t}).
\tag{19}
\]

In particular the derivative discrepancy at zero is -2 epsilon/9. This is a positive, explicit alternative to ACUE with exactly the same complete static summary law and a different heat response. It deliberately changes the protected mixed statistic T, so it does not contradict the older protected-moment semigroup theorem.

## 6. Arbitrarily large matrices and stationary line processes

For either N_0=4 witness, take all r preimages of every root under z->z^r. The lifted model has N=4r particles on the 8r-th roots of unity. Its centered real polynomial is F_0(rx) or G_0(rx). Scalar heat gives F_{r^2t}(rx), so

\[
D_{S,r}=D_S/r^2,\quad D_{C,r}=D_C/r^2,
\quad N^2D_{S,r}=16D_S,\quad N^2D_{C,r}=16D_C.
\tag{20}
\]

For every integer m, its trace is zero unless r divides m; if m=rj it equals r times the corresponding base trace p_j. Therefore all static pair measures still agree. The minimum gap is pi/(4r), exactly one half of the mean spacing. The distinct N^2-depth constants are approximately 1.41804709323 and 1.84839248149. These are deterministic families in ACUE support, not statements about typical ACUE depth or its limiting law.

For a line-process formulation, periodically repeat S/2 or C/2 with period 4 and then add a uniform shift in [0,4). Both processes are stationary, simple, have intensity one and minimum gap 1/2. Equality of the finite cyclic difference counts proves equality of their full stationary pair measures. The construction with A/2 and B/2, period 6, also preserves the Palm nearest-neighbour gap histogram. These processes are periodic with lattice-supported pair measures; they do not have the sine-process pair correlation.

## 7. Relation to the famous conjectures and the next test

Tao's [ACUE construction](https://terrytao.wordpress.com/2019/05/08/the-alternative-hypothesis-for-unitary-matrices/) demonstrates the insufficiency of a specified protected low-moment sector. Our older [dynamic-generator proof](../../reports/dynamic_generator.md) shows that deterministic evolution keeps that sector protected. The present examples address a different information set: **complete static pair information** can still omit the cubic information that changes the flow.

The archive already contains homometric projection DPPs on Z/12 with distinct triple probabilities; see [the historical account](../../../historical/riemann-rmt/final_verified_paper.md). We do not claim to discover general pair-versus-triple nonuniqueness. The new certificates here identify exact scalar-heat depths, arbitrarily large half-grid lifts, and an ACUE-law perturbation preserving the complete joint pair/gap-summary law.

For the actual zeta programme, the concrete follow-up is to study balanced cubic trace observables or their arithmetic logarithmic-derivative analogues **outside the protected total-weight range**, with every prime-power and centering term retained. Merely proving a generic relation between pair data and heat response cannot supply this missing information: (19) disproves such a relation on the stated class. Nothing here establishes the necessary arithmetic estimate.

The separate [stochastic-protection investigation](../stochastic-protection/AGENT_STOCHASTIC_PROTECTION.md) tests whether adding genuine DBM and multiple observation times escapes protected moments. Keep that result's hypotheses separate from the present pair-matched law.

## 8. Reproduction and limitations

Run `python3 research/counterexamples/pair-matched-flow/check_pair_matched_heat.py`. The output records exact integer pair counts, exact radical trace evaluations, orbit masses, flow identities, a rational root enclosure, complement tests over small sizes, and deliberate negative controls. All decimal heat depths are labeled diagnostic.

This is an ordinary written proof with independent internal review, not a Lean formalization. No Monte Carlo estimate or large zero/prime scan is needed. Postpone claims about genuine sine-pair rigidity outside specified model classes, nonperiodic ACUE limits, actual-zeta cubic estimates, and external novelty until those questions are separately resolved.
