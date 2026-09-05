# The h = 1 obstruction to a uniform sub-square-root pair-error premise

Date: 2026-09-05. Author: originating coordinator, task 01a0702b-e4b0-7020-ae61-b1fe718932c1. Complete ordinary argument submitted to the main research task for independent checking. No novelty or strict variance improvement is claimed.

This concerns equation (31) and the beta < 4/9 discussion in the frozen R21 manuscript CENTERED_PAIR_ERROR_TARGET.md, SHA-256 81a676d68836bff15a50ba6190bf2c1eab7cd54f0d3ae85d604a48fc36a7e54e. Its actual signed aggregate target and its main reduction remain valid.

## 1. The premise to be excluded

Let \(a_n=\Lambda(n)-1\), \(E(x)=\Psi(x)-x\), and
\[
E_X(z,h)=\sum_{X<m\le z}
\bigl[a_ma_{m+h}-(\mathfrak S(h)-1)\bigr].
\]
Suppose fixed real numbers \(\beta<1/2\), \(B\), and a fixed constant gave
\[
\sup_{X<z\le2X}|E_X(z,h)|
\ll X^\beta(\log X)^B
\tag{1}
\]
for every sufficiently large \(X\) and every integer \(1\le h\le X\).
The uniform-in-\(T\) formulation over the R21 window already implies this: for any large \(X\), choose \(T=\sqrt X\), so that \(X=T^2\) lies inside \([T^{7/4},T^{9/4}]\).

We show that (1) is impossible. It therefore cannot be treated as an available future target when \(\beta<4/9\).

## 2. Keep all prime powers and singleton terms

For integer \(X<z\le2X\), put
\[
P_X(z)=\sum_{X<m\le z}\Lambda(m)\Lambda(m+1).
\]
If a summand is nonzero, the even member of the consecutive pair must be a power of 2. There are \(O(\log X)\) such candidate indices up to \(2X+1\), and each product is at most
\((\log2)\log(2X+1)\). Hence, uniformly on the block,
\[
0\le P_X(z)\ll(\log X)^2.
\tag{2}
\]
This argument includes all higher prime powers; it makes no claim about the distribution of Mersenne or Fermat primes.

Since \(\mathfrak S(1)=0\), direct expansion gives the exact identity
\[
\begin{aligned}
E_X(z,1)
&=P_X(z)-[\Psi(z)-\Psi(X)]
 -[\Psi(z+1)-\Psi(X+1)]+2(z-X)\\
&=P_X(z)-2[E(z)-E(X)]
 -\Lambda(z+1)+\Lambda(X+1).
\end{aligned}
\tag{3}
\]
The last step uses \(E(n+1)-E(n)=\Lambda(n+1)-1\).
Consequently,
\[
E_X(z,1)=-2[E(z)-E(X)]+O((\log X)^2).
\tag{4}
\]
This is why the singleton prime errors inside the centered pair cannot be discarded.

## 3. A dyadic increment bound would remove a genuine zeta pole

Choose
\[
\max(\beta,0)<\theta<1/2.
\]
Equations (1) and (4), with logarithms absorbed into the strictly larger exponent, imply
\[
|E(z)-E(X)|\ll X^\theta
\tag{5}
\]
for all large integer \(X<z\le2X\).
First telescope (5) along powers of 2, then use one final block to reach an arbitrary integer \(N\). The resulting geometric series gives
\[
E(N)=O(N^\theta).
\tag{6}
\]
For real \(x\), \(E(x)=E(\lfloor x\rfloor)-\{x\}\), so the same bound holds.

For \(\Re s>1\), the absolutely convergent Euler product and partial summation give
\[
\int_1^\infty E(y)y^{-s-1}\,dy
=\frac{-\zeta'/\zeta(s)}s-\frac1{s-1}.
\tag{7}
\]
Bound (6) makes the left side holomorphic throughout \(\Re s>\theta\), by locally uniform absolute convergence, including after differentiation in \(s\).

There is a nontrivial zero \(\rho\) on \(\Re\rho=1/2\). If its multiplicity is \(m_\rho\ge1\), then the right side of (7) has residue
\[
-\frac{m_\rho}{\rho}\ne0
\tag{8}
\]
at \(\rho\). The subtraction at \(s=1\) cannot cancel that pole. Uniqueness of meromorphic continuation now contradicts holomorphy on \(\Re s>\theta\). This disproves (1).

Only the classical existence of a critical-line zero is used; RH is not needed for this obstruction. It applies, in particular, under the programme's standing RH hypothesis.

## 4. Scope of the correction

The exponent bookkeeping in the manuscript remains useful: a formal uniform exponent below \(4/9\) would eliminate the displayed absolute-summation error budget. The present argument shows that this particular all-shifts premise is unavailable for actual \(\Lambda-1\), even before investigating difficult even shifts.

It does not disprove the exact Pareto reduction, the singular-series average, or the signed aggregate target \(\liminf\mathcal E_T\le1-M\). It also does not exclude estimates averaged over shifts, signed cancellation between shifts, separately treating small or odd shifts, or estimates on a specified restricted shift range. Those are different hypotheses and need their own complete error budgets.

The manuscript should identify the all-shifts \(\beta<4/9\) premise as impossible, rather than merely unproved, and keep the feasible research obligation on the actual signed weighted functional.

## Classical inputs

- [NIST DLMF 25.2.11](https://dlmf.nist.gov/25.2.E11): Euler product in \(\Re s>1\), from which (7) follows by logarithmic differentiation and partial summation.
- [NIST DLMF 25.10(i)](https://dlmf.nist.gov/25.10): existence of infinitely many critical-line zeros. A single one suffices here.

Both source statements were checked live. This is an analytic obstruction, not a numerical experiment or a proof of the desired strict arithmetic bound.
