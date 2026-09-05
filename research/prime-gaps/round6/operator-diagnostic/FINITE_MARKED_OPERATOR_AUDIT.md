# Independent finite marked-space regression for the signed sieve operator

This is a structural test of the operator and projection formulas used in Round 6. It is not a calculation of the k=39 prime-sieve quotient, and none of its numerical values is transferable to that quotient. All identities below are checked with exact rational arithmetic in `finite_marked_operator_check.py`; floating eigenvalue displays are explicitly separated in its JSON.

## 1. Why this model is useful

The actual source Hilbert space is a product of finite fragment measures restricted to a cap domain. Erasing one coordinate integrates against that measure. Its adjoint is a lift, not a normalized conditional expectation. The hybrid face multiplier takes negative as well as positive values. A proposed new radial subspace is not nested with the original polynomial span. A regression that assumes uniform mass, rectangular support, positive operators or nested subspaces would miss the errors relevant here.

The toy coordinate has five atoms `(total, fragment-cap label)`:

| Atom | Mass |
|---|---:|
| (0,0) | 1/2 |
| (1,0) | 2/9 |
| (1,1) | 1/9 |
| (2,0) | 1/18 |
| (2,1) | 1/9 |

For three coordinates, retain total at most four and require all fragment labels to be zero when total is at least three. There are 38 ordered retained states. The exact mass matrix W is diagonal with the product masses. The face multiplier is 1 on the specified smaller background region, 3/4 on the larger region, and −1/4 on the remaining backgrounds; rho is 2/5. Thus the toy operator has the same mathematical construction as a signed sum of marginal squares, on a nonrectangular marked domain.

For a retained state x, define

\[
(Tf)(x)=\rho\sum_{i=1}^3 m(x_{\hat i})
\sum_{u:\,x\oplus_i u\in H}\mu(u)f(x\oplus_i u).
\]

The script verifies \(WT=T^{\mathsf T}W\) exactly. It also produces an explicit coordinate-vector witness with

\[
\langle v,Tv\rangle=-\frac1{38880}<0.
\]

Consequently a positive-semidefinite assumption is false even in this small model.

## 2. Nonnested compression and the correct order

Set \(G(x)=\prod_i(1+t_i)^{-1}\), \(s=\sum_i t_i\), and let

\[
U=G\operatorname{span}\{1,s,s^2,\sum_i t_i^2\},\qquad
V=\{G h(s):h\text{ arbitrary on }\{0,1,2,3,4\}\}.
\]

Both projections use the exact W inner product. In particular,

\[
P_U=U(U^{\mathsf T}WU)^{-1}U^{\mathsf T}W.
\]

The trial is a specified rational vector in U, with no requirement that it be an exact Ritz vector. Let

\[
r=(I-P_U)Tf,\quad h=P_Vr,\quad w=(I-P_U)h.
\]

The exact checks establish

\[
\langle f,Tr\rangle=\|r\|^2,\qquad
\langle f,Tw\rangle=\|h\|^2,\qquad
\|w\|^2=\|h\|^2-\|P_Uh\|^2>0.
\]

They also establish \(\|w\|^2\le\|h\|^2\le\|r\|^2\). These statements do not assume that U and V are nested. Their projections do not commute in this example. Replacing h by \(P_VTf\) and retaining the same claimed coupling identity gives a nonzero exact error, saved in the JSON. This is a concrete regression for the order of projections, not just a norm tolerance test.

For non-unit f, the normalized two-dimensional block has

\[
a=\frac{\langle f,Tf\rangle}{\|f\|^2},\quad
b=\frac{\langle w,Tw\rangle}{\|w\|^2},\quad
c^2=\frac{\langle f,Tw\rangle^2}{\|f\|^2\|w\|^2}.
\]

Its observed values are approximately a=0.9862966311, b=0.1124698915 and c=0.01468793075. The larger block eigenvalue is approximately 0.9865434471, exceeding a by 0.000246816. These are toy-model displays, not prime-gap evidence. Their purpose is to confirm that the outside-space direction, its normalization and the block formula are all consistent.

## 3. Product conjugation

For amplitudes \(f=Gp\), let D be multiplication by G. The conjugated operator is \(D^{-1}TD\), and its mass matrix is \(DWD\). The script verifies its self-adjointness under that mass and its equivalence to the original action.

The outer coordinate contributes a reciprocal factor \(1/g(t_i)\), while the erased integral contains one factor g(u). Replacing this with an average under normalized \(g(u)^2\mu(u)\) would define a different operator. The actual numerical implementation must carry the analogous cell factors and normalizers separately.

## 4. Reproduction and scope

Run `OPENBLAS_NUM_THREADS=1 python3 finite_marked_operator_check.py`. Dependencies are NumPy and SymPy. It writes a JSON receipt and prints the exact rational values. There is no random seed because the model and trial are deterministic. No source file or earlier certificate is changed.

This independent finite check validates algebraic invariants and rejects tempting incorrect formulas. The actual k=39 function-space derivation, fragment-cell integration and numerical conditioning require their own proofs and tests. In particular, passing this toy model is not an outward error enclosure for any sieve integral.
