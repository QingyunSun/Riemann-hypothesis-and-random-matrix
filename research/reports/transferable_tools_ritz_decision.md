# Transferable tools: one Ritz diagnostic and the actual support obligation

2026-09-05. This note responds to the proposal to reuse structural tools from the 186 prime-gap proof and FLT formalization. It records one completed low-cost experiment and the next exact arithmetic requirement. It does not claim a new gap bound.

## Completed diagnostic

For the fixed rational trial at `L=100000`, with `ell=16/15`, write the normalized coefficient vector as u and the actual full arithmetic operator as K. Put

\[
\lambda=\langle u,Ku\rangle,\qquad r=Ku-\lambda u,\qquad
s=\|r\|,\qquad v=r/s,\qquad b=\langle v,Kv\rangle.
\]

The exact two-dimensional compression identity is

\[
K|_{\operatorname{span}(u,v)}\ \longleftrightarrow\
\begin{pmatrix}\lambda&s\\s&b\end{pmatrix}.
\]

The computed entries are

\[
\begin{pmatrix}
4.192011775686907&0.177521239887580\\
0.177521239887580&0.933549641583058
\end{pmatrix}.
\]

Its larger eigenvalue is `4.201654608743949`, and evaluating the resulting vector directly in the full operator gives `4.2016546087439535`. The orthogonality error is `1.39e-16`. The normalized margin improves from `-0.03763020252239` to `-0.03714169089289`, a gain of `0.00048851162950`. Both remain negative. Runtime of this recorded calculation was approximately 0.08 seconds; this is not a general speed claim.

This test uses self-adjointness only. K need not be positive semidefinite. The formula was also checked on an indefinite two-by-two control matrix. It does not replace the true function inner product with a coefficient norm in a nonorthogonal basis: here the integer coefficients already use the specified orthonormal coordinate normalization.

The newly generated vector contains prime-removal and cutoff-dependent sums through `A* A u`. It is not automatically a fixed polynomial `d_ell(n)(f(v)+g(v)S2)`. The completed fixed-family transfer theorem therefore does not automatically apply to this vector as L grows. A finite gain alone is not a new asymptotic certificate.

**Decision:** the experiment does not justify a large new sweep or more digits for the old negative trial. Preserve this residual direction as a diagnostic and focus the next main step on a new arithmetic input or a rigorous transfer for a direction with substantially larger demonstrated gain.

Evidence: `research/operator-bounds/ritz_residual_diagnostic.py`, its JSON output, and its run log. No eigensolver search in dimension L was performed by this test.

## What complementary factorization contributes in the 186 proof

The relevant primary source is [the short-gap paper, Proposition 2.3](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf). Its construction works with the actual modulus `Q=lcm(D,E)`. Nondecreasing complementary functions whose product is the cube of the prime scale divide the constraints between D and E. The proof accounts for the possibility that one side has no remaining prime at that scale, then verifies the primewise condition needed for triple dense divisibility. That property permits a larger sieve support within the applicable distribution estimates.

The transferable lesson is to enlarge the **legally evaluable combined object** before optimizing weights. It is not a permission to import an arithmetic-progression modulus exponent into a zeta Dirichlet-polynomial mean value.

The user's Weijie Su post was also supplied as context. Direct retrieval of that X page returned HTTP 403 in this run; this note uses the mathematical paper for the technical statement.

## The corresponding zeta obligation

For the shifted packet with center `t0=3T/2` and width `W=T/log T`, the exact Gram kernel of two integer-frequency polynomials has off-diagonal part

\[
\mathcal E_T(U,V)=
\sum_{a\ne b}\frac{U(a)\overline{V(b)}}{\sqrt{ab}}
e^{-it_0\log(a/b)}e^{-\frac12W^2\log^2(a/b)}.
\]

The common Gaussian mass is factored out here. In the present product-cutoff method, the combined coefficients arise at indices such as `a=km` and `b=ln`. The accessible cutoff makes unequal integer products sufficiently separated for the source mean-value estimate.

A proposed complementary support must specify U and V from the same integer construction, allow genuinely new products, and prove a bound for this actual kernel on that class. For example, a usable new lemma would bound

\[
|\mathcal E_T(U,V)|\leq\epsilon_T
\left(\sum_a|U(a)|^2/a\right)^{1/2}
\left(\sum_b|V(b)|^2/b\right)^{1/2},\qquad\epsilon_T\to0,
\]

or give a sharper explicit signed contribution with an error small enough for the final residual certificate. The displayed bound is an **unproved target for a specified new coefficient class**, not a theorem for arbitrary long polynomials. Dense nearby frequencies can violate such a uniform assertion for arbitrary coefficients.

Merely imposing complementary restrictions inside the existing unrestricted product cutoff changes the trial subspace of the same K; it does not add a previously unavailable Gram entry. Moving to a larger cutoff creates a real new mean-value obligation. Centering the packet to recover Fourier positivity creates the explicit pole and low-height costs proved in the companion report. Neither issue is removed by changing terminology from smoothness to dense divisibility.

## Signed residual recovery: useful, but with all terms specified

If positive measures mu and nu and a signed difference sigma=mu-nu arise from an actual construction, one may use the independently valid inequality

\[
\|R\|_\mu^2\geq
\frac{\left(|\widehat m|-\epsilon-\sqrt{E G_\nu}\right)_+^2}{G_\mu},
\]

provided the mixed sigma correlation is within epsilon of the stated estimate, `||R||_nu^2<=E`, `||C||_nu^2<=G_nu`, and `||C||_mu^2<=G_mu`, with `G_mu>0`. This is triangle inequality followed by Cauchy–Schwarz separately in the two positive measures. A signed measure is never treated as positive.

No new zeta-specific choice of these measures with a positive net gain has yet been established. In particular, the centered-packet pole counterexample remains in force. The next research contribution must identify and estimate these objects, not repeat the abstract inequality.

## Formalization priority

The present exact identities and fixed-family transfer have sufficiently specific statements for future formalization. The useful FLT discipline is to check the actual definition and dependency closure of a result before spending time on its proof. An assumed long-support mixed-moment estimate would still be an assumption even if all subsequent linear algebra were checked by Lean.
