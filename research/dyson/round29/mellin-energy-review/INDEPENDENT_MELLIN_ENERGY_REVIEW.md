# Independent review: weighted Mellin energy and the sharp odd-log cofactor bound

Reviewer: Astra root. Date: 2026-09-06 UTC.

Decision: accepted as an ordinary analytic proof, subject to the final author byte pin in the adjacent receipt. The reviewed application assumes RH for the prime-window energy estimate; its cofactor exponential-sum lemma is unconditional. Neither conclusion contains a strict variance deficit or an estimate special to the Möbius signs. This review reads the entire manuscript and its complete symbolic checker. The checker verifies elementary identities; the estimates below require ordinary proof review.

## 1. Exact object and derivative convention

The manuscript retains \(X=T^2\), \(Y=T\), \(\ell=\log T\), fixed real compact smooth profiles, the exact inherited kernel \(b_T\), odd prime endpoints, and the flat center \(2\). Its real-variable extension is
\[
f(x)=X\ell^2\sum_{n\ {\rm odd}}F(x,n-x)(\Lambda(n)-2).
\]
For all \(x\) in the compact support, the allowed integers \(n\) belong to one finite interval. Thus differentiation can be done term by term at fixed \(n\), and every derivative of the compact profiles vanishes at their boundaries. This supplies a genuine smooth compact function, rather than a derivative of a discontinuous prime-counting function.

At odd integers \(m\), \(n-m\) is even and the function equals the exact discrete R27 prime window. Its even-integer values need not equal the separately defined discrete parity convention. The manuscript states this distinction, so there is no illegal extension of that identification.

The transformed amplitude satisfies the exact identity
\[
X\ell^2b_T(x)=\frac{TX}{x}
\int_0^1\omega((\log x+\log v)/\ell)v^{T-2}\,dv.
\]
The added portion below \(1/x\) is zero because \(\omega\) is supported at positive logarithmic heights. Since \(T/(T-1)\) is bounded, each fixed logarithmic derivative of \(X\ell^2b_T(x)\chi(x/X)\) is bounded. Constants may depend on derivative order; no growing-order conclusion follows.

For \(y=n-x\), the relevant differential operator is
\[
\mathcal A=x(\partial_x-\partial_y).
\]
Writing \(P=(x/(x+y))^T\), direct differentiation gives
\[
\mathcal A P=TP,\qquad
\mathcal A V(y/Y)=-(x/Y)V'(y/Y).
\]
These identities explain why a derivative costs \(T\), even though the product cutoff varies on scale \(X\). Repeated Leibniz expansion preserves compact support and gives, for each fixed \(j\),
\[
|K_j|\ll_jT^j,\qquad |\partial_yK_j|\ll_jT^j/Y.
\]
A further \(y\) derivative of \(P\) contributes \(T/(x+y)=O(1/Y)\); derivatives of the fixed profile have the same scale. The recurrence therefore covers all fixed orders, not just the two checked Pareto examples.

## 2. Centering and the decisive measure change

For real endpoints define
\[
B_x(y)=\sum_{\substack{x<n\le x+y\\n\ {\rm odd}}}(\Lambda(n)-2).
\]
Its exact decomposition is
\[
B_x(y)=\Psi(x+y)-\Psi(x)-y
-(\log2)\#\{r:x<2^r\le x+y\}
+y-2N_{\rm odd}(x,x+y).
\]
The odd staircase is uniformly bounded. On the support, \(y<x\) for large \(T\), so at most one power of \(2\) occurs. Hence the correction is \(O(1)\). Odd prime powers are part of the original sum and have not been removed.

With compact kernel endpoints, Stieltjes partial summation gives
\[
\mathcal D^jf(x)=-\int B_x(y)\partial_yK_j(x,y)\,dy,
\qquad
|\mathcal D^jf(x)|^2\ll_j\frac{T^{2j}}Y\int|B_x(y)|^2\,dy.
\]
Both the integration interval and the kernel support have length \(O(Y)\). The \(1/Y\) factor is the result of Cauchy and the squared derivative size, not an assumption about a short-interval variance.

The primary input is the fixed-\(\beta=3\) RH estimate
\[
J(3,S)=\int_1^{S^3}|E(x+x/S)-E(x)|^2\frac{dx}{x^2}
\ll \frac{\log^2S}{S}.
\]
The CCCC primary text states its bound with constant depending on fixed \(\beta\), in the stated range containing \(3\). It is not a theorem for one arbitrarily moving profile.

The substitution \(\lambda=Ty/x\) is essential. On the fixed support rectangle,
\[
\frac{dx}{x}\,dy=\frac{dx}{T}\,d\lambda,
\]
and \(\lambda\) remains in a fixed positive compact interval. For each such \(\lambda\), set \(S=T/\lambda\); then \(bX<S^3\) uniformly for large \(T\). Removing \(x^{-2}\) from the source integral costs at most \((bX)^2\). It follows that
\[
\int_{aX}^{bX}\frac{dx}{x}\int_{cY}^{dY}|B_x(y)|^2dy
\ll \frac{X^2}{T^2}\log^2T+Y
\ll Y^2\log^2X.
\]
The \(O(1)\) centering correction contributes only \(O(Y)\). Combining with the preceding partial-summation bound proves
\[
\int|\mathcal D^jf|^2\frac{dx}{x}\ll_jT^{2j}Y\log^2X.
\]
The power and logarithm bookkeeping are consistent. In particular, no \(Y\log X\) local estimate has been smuggled into the calculation.

## 3. Weighted Mellin energy

In \(v=\log x\), the Mellin transform is the Fourier transform of \(g(v)=f(e^v)\), with phase \(e^{-itv}\). Compact support and smoothness justify Plancherel for every fixed derivative:
\[
\int t^{2r}|\widehat f(t)|^2dt
=2\pi\int|\mathcal D^rf(x)|^2\frac{dx}{x}.
\]
Expanding the finite binomial and applying the derivative bounds yields
\[
\int(1+t^2/T^2)^j|\widehat f(t)|^2dt
\ll_jY\log^2X.
\]
For every fixed \(j\), this implies the stated uniform integrated tail bound with factor \((1+B^2)^{-j}\). It does not imply a pointwise bound at a selected Mellin frequency, a sharper logarithm, or constants uniform in growing \(j\).

This positive-order estimate alone does not prove the separate negative-order estimate used by Euclid. The latter uses Cramér's additional RH prime-error mean square and is reviewed separately with the complete central-block proof.

## 4. Sharp odd-log sums: source applicability and aliases

The unconditional cofactor lemma keeps the original sharp interval \(a_0T<k\le b_0T\), \(k\) odd, and the exact coefficient \(\log k\). For positive \(t\), the adjacent increments in cycles are
\[
\delta_k=\frac{t}{2\pi}\log(1+2/k).
\]
They decrease monotonically, and the elementary logarithm inequalities give
\[
\frac{t}{\pi(b_0T+2)}
\le\delta_k\le\frac{t}{\pi a_0T}
\le1-\varepsilon/\pi
\]
when \(t\le(\pi-\varepsilon)a_0T\). Thus every partial interval has increments separated from all integers by at least a fixed constant times \(\min(1,t/T)\).

Montgomery–Vaughan's Theorem 16.5, printed page 6, assumes increasing increments in \([\Delta,1-\Delta]\). Reversing and conjugating the sum transforms these positive decreasing increments into increasing positive increments without changing its modulus. Its bound therefore applies to every sharp partial interval here. Negative \(t\) follows by conjugation; intervals of at most one term satisfy the required trivial bound.

Abel summation retains the actual endpoint term, of size at most \(O(\log T)\) times the prefix bound. The total variation of \(\log k\) on the fixed-ratio interval is \(O(1)\). This proves
\[
\left|\sum_{\substack{a_0T<k\le b_0T\\k\ {\rm odd}}}
(\log k)k^{it}\right|
\ll \log(2T)\min\left(T,1+\frac{T}{|t|}\right).
\]
At zero, elementary odd-lattice summation supplies half the integral of \(\log u\), with endpoint error \(O(\log T)\). There is no claimed extension of the nonstationary estimate through a resonance band.

One precision correction was requested during review: replace “Equivalently” before the continuous Poisson stationary condition by “In the continuous Poisson representation”. Indeed, the exact adjacent-increment resonances are
\[
t=\frac{2\pi q}{\log(1+2/k)}
=\pi q(k+1+O(1/k)),
\]
whereas continuous stationary points satisfy \(t/k=\pi q\). These formulas have the same leading scale but are not identical. The corrected author version is pinned in the review receipt. This wording correction changes no bound or symbolic check.

The original selected R28 frequencies lie in a fixed compact subset below the first cofactor stationary band. This explains why a substantial transpose pairing against two modulated vectors is compatible with a small direct coupling of the unmodulated logarithmic vector to a single such input plane. It is neither an estimate for the Möbius factor nor a numerical extrapolation.

## 5. Independent check record and limits

The complete checker was read before copying it into this review directory. Its unchanged copied execution reproduces the entire JSON and stdout, including all 13 named symbolic assertions. The adjacent receipt records author/source hashes, the copied script, both complete outputs, and math-syntax results. No fields were omitted from the output comparison.

The checks cover the fixed-endpoint Pareto derivatives, profile derivative, kernel commutator, Jacobian, seven finite binomial identities, and odd-phase normalization. They do not verify the source asymptotics, constants, domination arguments, or an infinite theorem through sampling. Those conclusions rest on the ordinary derivation audited above.

Source applicability was checked against the retained primary text:

- [Carneiro–Chandee–Chirre–Milinovich, *A tale of three integrals*](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), printed page 1, equations (1.1) and (1.3): the exact \(dx/x^2\) measure, centered full prime-counting increment, fixed parameter, and RH hypothesis.
- [Montgomery–Vaughan, *Multiplicative Number Theory II*, author draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf), printed page 6, Theorem 16.5: monotone increment hypotheses and separation from integers.

The result is an accepted application of these classical estimates in the programme's exact central geometry. External novelty and Lean formalization have not been established. No prime calculation, matrix reconstruction, frequency scan, or additional model session is part of this review. The strict signed carrier estimate, the full unbalanced and height/shift partition, and the famous-conjecture conclusions remain open.

