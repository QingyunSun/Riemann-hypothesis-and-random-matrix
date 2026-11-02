# The mass cutoff gives a finite Fock operator bound

Date: 2026-09-05. Author: root Astra. This is a self-contained bound for the idealized Fock operator defined in Fable PR11 commit `20730285c8f9a81539e0662c6e015023c2ed107a`. It corrects that report's assertions that the field norm is infinite or that multi-mode boundedness is still open. It does not prove a sharp spectral threshold, convergence of the displayed numerical discretization, or an arithmetic-to-Fock operator limit.

## Statement and exact conventions

Let h=L²((0,1),dmu), dmu(u)=du/u, and let Gamma(h) be the usual bosonic Fock space with orthonormal sector convention. The energy/mass operator E=dGamma(u) multiplies an n-particle wavefunction by u_1+...+u_n. Let P=1_(E<=1), and work on the closed subspace H_1=P Gamma(h).

For g in h suppose additionally

\[
B_g^2=\int_0^1\frac{|g(u)|^2}{u}\,d\mu(u)
=\int_0^1\frac{|g(u)|^2}{u^2}\,du<\infty.
\]

Let a(g) denote annihilation on the finite-particle core. Its restriction to H_1 extends to a bounded operator T of norm at most B_g. Its adjoint A=T* is the compressed creation operator P a*(g) P on its natural core. In the Fable convention A creates and A* annihilates. Then

\[
\|A\|=\|T\|\le B_g,\qquad
\|\Phi\|=\|A+A^*\|\le2B_g,
\qquad
\left\|K=A^*A+\tfrac12(A^2+(A^*)^2)\right\|\le2B_g^2.
\tag{1}
\]

The number operator is unbounded on H_1, but that fact does not contradict (1).

## Sector proof, including the infinite direct sum

For a symmetric n-particle wavefunction psi_n, the annihilation formula is

\[
(a(g)\psi_n)(u_2,\ldots,u_n)
=\sqrt n\int_0^1\overline{g(u_1)}\psi_n(u_1,\ldots,u_n)\,d\mu(u_1).
\]

Weighted Cauchy--Schwarz, with weights u_1 and its reciprocal, gives

\[
\|a(g)\psi_n\|^2
\le nB_g^2\int u_1|\psi_n(u_1,\ldots,u_n)|^2\,d\mu^{\otimes n}
=B_g^2\langle\psi_n,E\psi_n\rangle.
\tag{2}
\]

The equality uses symmetry, not a bound on n. Different input sectors map into different output sectors, so summing (2) yields

\[
\|a(g)\Psi\|^2\le B_g^2\langle\Psi,E\Psi\rangle
\le B_g^2\|\Psi\|^2
\]

on the dense finite-sector core inside H_1. Therefore a(g) extends continuously there to T. Annihilation only decreases total mass, hence T maps H_1 into itself. Its bounded adjoint is the closure of compressed creation. This justifies the domains in (1) without assuming an untruncated creation operator is bounded. The two final bounds follow from the triangle inequality and submultiplicativity. The algebraic identity K=Phi²/2-[A,A*]/2 is valid, but is not needed to prove boundedness.

For this proof, normalizable high-particle-number states can be made by placing each coordinate in a small positive interval inside (1/(3n),1/(2n)). Their total mass is at most 1/2 and their sector norm is finite. A state with all coordinates exactly equal to 1/(2n), as used in the Fable prose, is a delta configuration and is not an L² wavefunction. Replacing it by these packets proves only that particle number is unbounded. It does not give a lower bound on the field norm.

## The actual sine kernel and every reported grid

For the stipulated g(u)=2sin(pi u/2), integration by parts gives exactly

\[
B_g^2=4\int_0^1\frac{\sin^2(\pi u/2)}{u^2}\,du
=2\pi\operatorname{Si}(\pi)-4
\approx7.636063674837709.
\]

Thus the bound for K is approximately 15.27212734967542. This is much larger than pi²/2, so it cannot establish the desired spectral wall. Its role is to settle finite boundedness rigorously. Numerical values here describe the exact integral; no interval-certified spectral conclusion is inferred from them.

There is also a uniform bound for Fable's literal discrete model. Its modes have u_j=j/M and creation coefficients c_j=2sin(pi j/(2M))/sqrt(j). The same sector proof, with a finite sum in place of the integral, gives

\[
\|K_M\|\le2B_M^2,\qquad
B_M^2=\sum_{j=1}^M\frac{c_j^2}{u_j}
=\frac1M\sum_{j=1}^M
\frac{4\sin^2(\pi u_j/2)}{u_j^2}\le B_g^2.
\tag{3}
\]

The last inequality is exact: the integrand is decreasing on (0,1], since sin(x)/x is decreasing for 0<x<=pi/2, and (3) is its right Riemann sum. Hence the norms of all these finite matrices are uniformly bounded, not just the computed examples. This does not assert that the sequence is monotone or that its norm converges to the continuous norm.

## Remaining modelling and numerical limits

The literal c_j coefficients are a quadrature rule, not an exact piecewise-constant Galerkin projection for the measure du/u. In particular the first interval (0,1/M] has infinite du/u mass, so a nonzero constant on that interval cannot be normalized in h. One can instead choose a normalized profile proportional to g on that bin, or an infrared cutoff, but those constructions and their mass-cutoff error require an actual comparison proof. The report's first-bin normalization heuristic does not supply one.

The matrix formula is unambiguous and can be tested as a finite model. Lanczos computations are floating eigensolver results, not exact diagonalization or rigorous enclosures. Stable fits near 4.6456 are numerical evidence only, and agreement with a different trial family does not prove either operator equality or a sharp norm limit. The main arithmetic research remains independent of those unproved transfers.

The earlier Astra Schur majorant search already gives finite but nonsharp upper candidates in a different formulation. No repeat optimization is proposed here. The new contribution of this note is the complete mass-weighted sector argument and its application to the erroneous infinity claim, with the continuous and literal discrete models distinguished.
