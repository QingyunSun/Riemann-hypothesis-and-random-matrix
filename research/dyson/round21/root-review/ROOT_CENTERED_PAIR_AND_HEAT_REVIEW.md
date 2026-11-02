# Root review of the centered pair target, its correction, and the heat representation

Date: 2026-09-05. Status: ordinary mathematical review completed. This note records the main review and the substantive qualification caught by the originating coordinator. No strict actual-zeta bound is accepted or claimed.

## 1. Precisely which author versions were read

The root read the entire first centered pair manuscript, SHA256 81a676d68836bff15a50ba6190bf2c1eab7cd54f0d3ae85d604a48fc36a7e54e, and its entire original small checker. The main reduction, absolute convergence, singular-series estimate, partial summation and source-range audit checked out. The initial root assessment missed the impossibility of the all-shifts sub-square-root benchmark. The coordinator identified that qualification before publication.

The root subsequently read the complete original-to-revised diff, the complete correction checker, and the coordinator's full 4,963-byte obstruction note, SHA256 5270e51de9df32aecee7fd63e569c5f3cdcd743107fc1c7f7be69cf6df587d34. The revised author manuscript is 21,504 bytes, SHA256 d7e73b8379e1adadd1fba79e3dc6141252c796502ba793030a500a8c5a6fc15e. Its main sections 1–4, exact Abel block and original source audit are unchanged. The correction is accepted; the old feasibility assessment is superseded, not silently retained as a valid research option.

## 2. Exact centering and absolute convergence

For \(a_n=\Lambda(n)-1\), the floor identity is exact:
\[
E(qx)-E(x)=\sum_{x<n\le qx}a_n+\{x\}-\{qx\}.
\]
In the normalized positive length/prime measure, the floor error has squared mass at most \(T^{-3/4}/\log^2T\). The separately available RH variance bound and Cauchy–Schwarz give the stated \(O(T^{-3/8}/\log T)\) change of energy. This argument does not approximate the prime first moment or delete the singleton pieces in a centered product.

The survival integral of an event at integer \(n>x\) is exactly \((x/n)^T\). Consequently diagonal plus twice the positive-shift sum gives the finite signed-data kernel before its absolutely convergent infinite limit. The weight
\[
b_T(m)=\frac{T m^{-T}}{\log^2T}\int_1^mW_T(x)x^{T-2}dx
\]
vanishes below \(T^{7/4}\). Absolute convergence for \(T\ge4\) follows from the elementary logarithmic growth of von Mangoldt coefficients, a polynomial bound on the singular series, and the Pareto tail. Both singleton errors remain in the target.

## 3. Uniform singular-series kernel and diagonal cancellation

I checked the use of the unconditional triangular singular-series asymptotic in Montgomery–Soundararajan equation (16), including its factor two and negative sign. Linear interpolation extends the triangular sum from integer to real endpoints with error \(O(y)\). Twice integrating against
\[
k(y)=(1+y/m)^{-T},\qquad
k''(y)=T(T+1)m^{-2}(1+y/m)^{-T-2}
\]
is legitimate; the lower endpoint is zero and the upper boundary terms vanish.

The identity \(\int_0^\infty yk''(y)dy=1\) fixes the main logarithmic coefficient. After \(u=Ty/m\), the associated probability density is
\[
(1+1/T)u(1+u/T)^{-T-2}.
\]
Its first moment is \(2T/(T-1)\), and its density near zero is at most \(5u/4\) for \(T\ge4\). These two facts give a uniform bound for the absolute logarithmic moment. Replacing the main triangular asymptotic below \(y=1\) costs only \(O((T/m)^2)\), uniformly bounded in the required range. This proves the uniform \(-\tfrac12\log(m/T)+O(1)\) comparison.

The weight estimate has error \(O(1/(mT\log^3T))\) on the whole main range up to \(2T^{9/4}\). Smooth zero extension of the bump covers support endpoints. Its total error against the diagonal is negligible. Partial summation of the prime-power-inclusive diagonal asymptotic produces \(\int\alpha\omega\); the comparison produces \(-\int(\alpha-1)\omega\). Their sum is \(M=\int\omega\), as claimed.

For \(m>2T^{9/4}\), the original integral defining \(b_T\), rather than a support-truncated approximation, gives an exponentially small tail after multiplication by the polynomial coefficient bounds. This covers the actual product and the singular-series comparison separately. The complete identity \(\overline V_T=M+\mathcal E_T+o(1)\) is accepted under RH.

## 4. Abel summation and what the cited source theorems actually provide

The derivative formula for the outer weight gives \(|b_T'|\ll1/(m^2\log^2T)\). The Pareto factor is increasing in \(m\); its total variation is bounded by its endpoint value. Their product gives the displayed centered prefix norm with factor \(1/(X\log^2T)\). The \(h>X\) tail has uniform exponential decay and all dyadic blocks are accounted for. The formal budget \(H X^{\beta-1}\log^{B-2}X\), with \(H=X/T\), is correct.

The root read the retained primary text of Montgomery–Soundararajan through equation (16) and Theorem 3, and Chan's page containing Conjecture 2 and its conditional theorem. The root did not independently render those pages in this pass; the separate agent and coordinator receipts record their actual page-image inspections. Equation (16) is unconditional. The stronger moment assertions require conjectural prime-tuple input, and the second-moment range does not extend freely through the entire new prime window. A one-prime progression estimate from the 186 source cannot be substituted for the centered pair or signed shift aggregate.

## 5. Independent acceptance of the coordinator's obstruction

The exact integer identity is
\[
E_X(z,1)=P_X(z)-2[E(z)-E(X)]
-\Lambda(z+1)+\Lambda(X+1).
\]
I checked both endpoint signs by expanding the two singleton sums. A nonzero consecutive prime-power product has an even power of two, which proves the stated \(P_X(z)=O(\log^2X)\) without any special-prime conjecture.

The original all-large-\(T\) uniform premise covers all large blocks using \(T=\sqrt X\). After absorbing logarithms into an exponent \(\theta<1/2\), dyadic telescoping gives \(E(N)=O(N^\theta)\) for every integer, not merely powers of two. The floor identity extends it to real arguments. Absolute locally uniform convergence then makes its Mellin integral holomorphic on \(\Re s>\theta\). The meromorphic logarithmic derivative has residue \(-m_\rho/\rho\ne0\) at a critical-line zero, so the pole cannot be canceled by the subtraction at \(s=1\).

I checked the classical Euler-product and critical-line-zero statements live at NIST DLMF 25.2.11 and 25.10. Existence of one such zero suffices, so this obstruction is unconditional. The corrected manuscript properly restricts the conclusion: it rules out the uniform all-shifts \(\beta<1/2\) premise, including \(\beta<4/9\), not every dispersion or averaged approach.

The added observation that the actual weighted \(h=1\) contribution is \(o(1)\) under RH is also valid. Its centered prefix is \(O(\sqrt X\log^2X)\), and the exact Abel factor makes a single block \(O(X^{-1/2})\). Summing the geometric dyadic range starting at \(T^{7/4}\) tends to zero. This explains why the obstruction does not itself refute the signed target.

The correction checker verifies 22 formal singleton endpoint cases, six finite geometric identities, the Mellin principal-part residue, original-file preservation and the unchanged mathematical blocks. Its role is exact algebra and provenance, not analytic verification of holomorphy or zero existence. The original checker/output bytes still pin the superseded first manuscript; no fresh replay is claimed to have certified that manuscript's mistaken feasibility statement.

## 6. Heat representation: review of the independent review

The root authored LOCALIZED_MELLIN_HEAT_ENERGY.md and does not label its own derivation an independent review. The root has now read the complete independent Aquinas review, SHA256 48651b0dee077bf4ac8a576736ef5eabcc21bbeb2eb8c0f644d793c92e4f7093, including its source and independence qualification.

That review covers the square-root cutoff's Sobolev regularity; exact changes of variables; the translated support including negative original coordinates; the all-shift commutator integral; the use of the separately proved R20 arithmetic bound; Plancherel factors; heat-time factor two; Tonelli with arithmetic jumps; and the bounded prefactor replacement in the limiting criterion. Its bounded scalar checker replay is recorded separately and is byte-identical.

The accepted heat acts on the actual log-prime error, not on zeta-zero locations. The norm inequality needed for a strict deficit is still open. Neither the ordinary heat identity nor the Tauberian equivalence imports a stochastic Dyson Brownian motion theorem.

## 7. Publication scope

The corrected pair reduction, unconditional obstruction and root-authored heat formula are accepted at their precise ordinary-proof scope, with the independent reviews and coordinator feedback preserved separately. No strict estimate on \(\mathcal E_T\) or the heat energy is proved. All old author/reviewer outputs survive with their original hashes. The substantive correction belongs in the report, claim ledger and research log, not only in a hidden execution note.

The original finite checks and the independent correction replay require their pinned source context. Full third-party source bodies remain in the local archive, indexed publicly by hash. No new prime height, numerical scan, PDF rebuild or external model call was used for this review.
