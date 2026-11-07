# The exact probability cost of periodic lifting

This is a limitation on the present finite-model construction, not a no-go theorem for all possible countermodels.

Let \(P_n\) be ACUE on \(n\)-subsets \(S\) of the \(2n\)-th roots of unity. Write
\[
p_n(S)=(2n)^{-n}|\Delta(S)|^2.
\]
For \(r\ge2\), take every \(r\)-th root of every point of \(S\); denote the resulting \(nr\)-point configuration by \(L_r(S)\).

## 1. Exact atom identity

\[
p_{nr}(L_r(S))=p_n(S)^r.
\]

To prove this, set \(Q(z)=P_S(z^r)\). For every root \(z\) of \(Q\),
\[
|Q'(z)|=r|P'_S(z^r)|.
\]
Multiplying over all \(nr\) roots gives
\[
|\Delta(L_r(S))|^2
=r^{nr}|\Delta(S)|^{2r}.
\]
Divide by \((2nr)^{nr}\). The lift is injective on seed configurations. Its dihedral orbit size equals that of the seed, since rotations by \(2n\) grid sites stabilize the lift.

Consequently the ACUE probability of the entire lifted support is
\[
M_{n,r}=\sum_{|S|=n}p_n(S)^r.
\]
This sum runs over all seed subsets, not just the matched pairs used by our construction.

## 2. A closed formula from the classical Dyson constant-term identity

For \(r=2\),
\[
\boxed{M_{n,2}=\frac{(2n)!}{n!(4n)^n}.}
\]

Indeed, on the unit torus \(|\Delta|^4\) is the Dyson Laurent product with all parameters equal to 2. Its exponent in each variable lies between \(-2(n-1)\) and \(2(n-1)\), strictly inside the aliasing length \(2n\). Averaging it on the full \((2n)^n\) grid therefore extracts only its ordinary constant term. Repeated coordinates contribute zero. Dividing the ordered sum by \(n!\) gives
\[
M_{n,2}=\frac{1}{n!(2n)^n}
 \operatorname{CT}|\Delta|^4
=\frac{1}{n!(2n)^n}\frac{(2n)!}{2^n}.
\]
The constant-term theorem is classical; this application does not establish a new famous Dyson conjecture. See [Good, Short Proof of a Conjecture by Dyson, J. Math. Phys. 11 (1970), 1884](https://sites.math.rutgers.edu/~zeilberg/akherim/good1970.pdf).

At \(n=11\),
\[
M_{11,2}=\frac{1249937325}{53119845582848}
=0.00002353051503228758\ldots .
\]

Stirling's formula gives \(M_{n,2}\sim\sqrt2 e^{-n}\). This is a probability estimate, not a runtime claim.

## 3. All lift factors

The ACUE atom \(p_n(S)\) is the principal minor of the rank-\(n\) Fourier projection on \(2n\) sites. Its diagonal entries equal \(1/2\), so Hadamard's inequality gives \(p_n(S)\le2^{-n}\). The two alternating clock subsets attain equality. Hence
\[
M_{n,r}\le 2^{-n(r-2)}\frac{(2n)!}{n!(4n)^n}
\quad (r\ge2).
\]
This strengthens the simpler \(M_{n,r}\le2^{-n(r-1)}\).

## 4. The full pair data already determine membership in the lifted support

Write \(c_S(a)=|S\cap(S+a)|\) for the pair-displacement count on the \(2nr\)-site grid. Then
\[
S\in L_r\quad\Longleftrightarrow\quad c_S(2n)=nr.
\]
The right-hand condition says that translating the set by \(2n\) sites leaves every point in the set. Its translation cycles have length \(r\), so \(S\) is precisely the lift of an \(n\)-subset of the \(2n\)-site grid.

Thus the lifted support is a union of fibres of the full pair-data map. Any probability law \(Q\) with the same full pair-summary distribution as ACUE has
\[
Q(L_r)=P_{nr}(L_r)=M_{n,r}.
\]
If \(Q\) additionally agrees with \(P_{nr}\) outside that support, then, in the convention \(\operatorname{TV}(Q,P)=\sup_A|Q(A)-P(A)|\),
\[
\operatorname{TV}(Q,P_{nr})\le M_{n,r}.
\]
Every event probability, including survival under heat, differs by at most that amount. No bound on the density ratio is needed.

## Consequence for the research programme

The eleven-root theorem now gives an explicitly certified survival shift exceeding 0.0175. Its periodic copies cannot sustain a comparable macroscopic shift: at size 22, even redistributing the entire two-fold lifted support can change a probability by at most 0.0000235305151. A nonvanishing large-size separation requires perturbations affecting configurations outside this repeated-pattern support.

This result does not exclude an extensive construction, a stationary infinite-volume countermodel, or a different arithmetic route. It identifies exactly why the existing periodic-lift argument is insufficient.
