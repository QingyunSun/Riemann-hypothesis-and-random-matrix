# Small physical shifts in the actual signed Pareto aggregate

Date: 2026-09-05. Status: bounded ordinary proof, submitted for independent review. The all-shifts estimate below is unconditional; the stronger odd-shift estimate assumes RH. There is no strict variance bound or AH refutation here. No novelty claim is made.

The coordinator's \(h=1\) obstruction concerns an impossible uniform **unweighted** prefix bound below the square-root scale. That obstruction does not prevent the actual weighted contribution of \(h=1\), or a specified small-shift range, from tending to zero. This note proves that distinction with the exact R21 weights.

## 1. Statement with the exact normalization

Set
\[
\ell=\log T,\quad L=T^{7/4},\quad U=T^{9/4},\quad T\ge4,
\qquad W_T(x)=\omega(\log x/\ell),
\]
where \(\omega\) is the unchanged R16/R20 nonnegative smooth bump, supported on \([7/4,9/4]\). Retain
\[
a_n=\Lambda(n)-1,\qquad c_h=\mathfrak S(h)-1,
\qquad
b_T(m)=\frac{T m^{-T}}{\ell^2}\int_1^m W_T(x)x^{T-2}dx.
\tag{1}
\]
All prime powers remain in \(\Lambda\). For any set \(\mathcal H\) of positive integer shifts, write
\[
\mathcal E_T(\mathcal H)=2\sum_{m\ge1}b_T(m)
\sum_{h\in\mathcal H}(1+h/m)^{-T}[a_ma_{m+h}-c_h].
\tag{2}
\]
This is a subaggregate of the exact R21 signed remainder. It is not the original variance itself and need not be positive.

**Theorem.** Uniformly for integers \(1\le K\le L\), as \(T\to\infty\),
\[
\boxed{
2\sum_{m\ge1}b_T(m)\sum_{1\le h\le K}
(1+h/m)^{-T}|a_ma_{m+h}-c_h|
\ll_\omega \frac K\ell+K\ell T^{-7/8}+K2^{-T}.}
\tag{3}
\]
This estimate is unconditional and uses a classical dimension-two upper sieve. In particular every \(K(T)=o(\log T)\) can be removed from the signed aggregate with an \(o(1)\) error, including every fixed finite collection of shifts.

Under RH there is a separate, stronger signed estimate:
\[
\boxed{
|\mathcal E_T(\{1\le h\le K:h\text{ odd}\})|
\ll_\omega K T^{-7/8}+K2^{-T}.}
\tag{4}
\]
Indeed the same bound applies to any subset of these odd shifts, with its cardinality replacing \(K\). Thus any odd-shift range \(K=o(T^{7/8})\) is removable. In particular the full \(h=1\) contribution is \(O_\omega(T^{-7/8})\).

The bounds are not asserted optimal. Their implicit constants are independent of \(K,T\); no explicit numerical value is claimed. Equation (4) concerns cancellation inside each centered odd-shift sum, not the sum of absolute values of its individual coefficients.

## 2. Exact weight bounds, including the far endpoint

The substitution \(x=mu\), extending \(\omega\) by zero, gives
\[
b_T(m)=\frac{T}{m\ell^2}\int_0^1
\omega((\log m+\log u)/\ell)u^{T-2}du.
\tag{5}
\]
Consequently, uniformly for \(m>0\),
\[
|b_T(m)|\le\frac{C_\omega}{m\ell^2},\qquad
|b_T'(m)|\le\frac{C_\omega}{m^2\ell^2},\qquad
b_T(m)=0\ (m\le L).
\tag{6}
\]
Differentiating (5) costs only the fixed norms of \(\omega\) and \(\omega'\), since \(T/(T-1)\le4/3\) and \(\ell\ge\log4\). For fixed \(h\), the exact Pareto factor \(k_h(m)=(1+h/m)^{-T}\) is increasing in \(m\). Thus the endpoints and total variation of \(b_T k_h\) on \([X,2X]\), or a truncated final block, are at most
\[
\frac{C_\omega}{X\ell^2}(1+h/(2X))^{-T}.
\tag{7}
\]
This is the Abel norm from R21, derived without replacing its kernel by an exponential.

For \(m>2U\), use the original integral instead:
\[
b_T(m)\le\frac{T}{T-1}\frac{\|\omega\|_\infty}{\ell^2}
U^{T-1}m^{-T}.
\tag{8}
\]
For \(K\le L\) and these \(m\), one has \(m+h\le2m\). The singular-series bound proved in the next section and \(|a_n|\le1+\log n\) imply
\[
\sum_{h\le K}|a_ma_{m+h}-c_h|\ll K\log^2(2m).
\]
Dropping \(k_h\le1\), integral comparison of \(m^{-T}\log^2(2m)\) gives a tail \(O_\omega(K2^{-T})\). For clarity, its integral from \(Y=2U\) equals
\[
Y^{1-T}\left\{
\frac{\log^2(2Y)}{T-1}+
\frac{2\log(2Y)}{(T-1)^2}+
\frac{2}{(T-1)^3}\right\}.
\]
The first possible integer term obeys the same resulting upper bound up to an absolute constant because \(Y\ge T\). Hence the infinite endpoint in (2) has not been silently truncated.

## 3. Two elementary averaged bounds

Write
\[
C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right),
\quad
\mathfrak S(2n)=2C_2\prod_{\substack{p\mid n\\p>2}}
\left(1+\frac1{p-2}\right),\quad \mathfrak S(2n-1)=0.
\]
Expand the finite divisor product and then use nonnegative summation. The absolutely convergent Euler product gives
\[
\begin{aligned}
\sum_{h\le K}\mathfrak S(h)
&\le 2C_2\frac K2
\sum_{\substack{d\ge1\text{ odd}\\d\text{ squarefree}}}
\frac1d\prod_{p\mid d}\frac1{p-2}\\
&=KC_2\prod_{p>2}\left(1+\frac1{p(p-2)}\right)=K.
\end{aligned}
\tag{9}
\]
The last product is exactly \(C_2^{-1}\). Therefore
\(\sum_{h\le K}|c_h|\le2K\). This finite upper bound, not a conjectural singular-series asymptotic, is all that (3) needs.

We also use the unconditional elementary estimate \(\Psi(x)\ll x\). One direct proof notes that every prime-power term in \(\Psi(2n)-\Psi(n)\) occurs in the valuation of \({2n\choose n}\), so
\(\Psi(2n)-\Psi(n)\le\log {2n\choose n}\le2n\log2\).
Telescoping at powers of two and using monotonicity gives the asserted bound for real \(x\). No PNT error term is needed for (3).

## 4. A uniform upper-sieve input for growing shifts

The precise source is Tao, *254A, Notes 4: Some sieve theory* (2015), equation (22), Lemma 17 and Corollary 19. We use its upper-bound consequence with a **uniform** dimension-two axiom. We do not extrapolate the fixed-pattern threshold in that source's Theorem 32 to a growing \(h\).

For even \(1\le h\le X\), sieve \(X<m\le2X\) by the residue classes satisfying \(m(m+h)=0\pmod p\). Their number is
\(\nu_h(p)=1\) when \(p\mid h\) and \(2\) otherwise. For squarefree \(d\), the Chinese remainder theorem gives
\[
\#\{X<m\le2X:d\mid m(m+h)\}
=X\frac{\nu_h(d)}d+O(\nu_h(d)),\qquad
\nu_h(d)\le2^{\nu(d)}\le\tau(d).
\tag{10}
\]
This error is uniform in \(h\). Put \(g_h(p)=\nu_h(p)/p\). Since \(h\) is even, \(g_h(2)=1/2\), and for odd \(p\), \(g_h(p)\le2/p\le2/3\). Mertens' product bound therefore supplies the source's axiom
\[
V_h(w)/V_h(z)\le C(\log z/\log w)^2,
\qquad 2\le w\le z,
\]
with one constant for every such \(h\).

Choose \(D=X^{1/2}\) and \(z=D^{1/s}\), where \(s\) is one sufficiently large fixed constant. The cited fundamental lemma and
\(\sum_{d\le D}\tau(d)\ll D\log(2D)\) bound the sifted count by
\[
C X V_h(z)+O(\sqrt X\log X).
\]
Uniformly in \(h\), factor the local product as
\[
V_h(z)=\frac12\prod_{2<p\le z}(1-2/p)
\prod_{\substack{2<p\le z\\p\mid h}}\frac{p-1}{p-2}
\ll\frac{\mathfrak S(h)}{\log^2X}.
\tag{11}
\]
Here the baseline product is bounded by \(C/\log^2z\) using
\(1-2/p=(1-1/p)^2(1-1/(p-1)^2)\); the finite correction is at most the complete positive correction defining \(\mathfrak S(h)\). No constant depends on the size or factorization of \(h\).

If both \(m,m+h\) are genuine primes, they exceed \(X>z\) and survive this sieve. Their logarithmic weights are at most \(\log^2(3X)\). Pairs involving a higher prime power contribute at most \(O(\sqrt X\log^3X)\): there are \(O(\sqrt X\log X)\) such powers up to \(3X\), and each fixes at most two possible indices \(m\). It follows that
\[
\sum_{X<m\le2X}\Lambda(m)\Lambda(m+h)
\ll X\mathfrak S(h)+\sqrt X\log^3X,
\quad h\text{ even},\ 1\le h\le X.
\tag{12}
\]
For odd \(h\), the even member of a nonzero pair must be a power of two. There are only \(O(1)\) such powers in \([X,3X]\), and each product is at most \((\log2)\log(3X)\). Thus that pair sum is \(O(\log X)\), so the weaker displayed upper bound (12) also holds for odd \(h\), since \(\mathfrak S(h)=0\).

## 5. Proof of the all-shifts absolute estimate

The centered coefficient satisfies
\[
|a_ma_{m+h}-c_h|
\le\Lambda(m)\Lambda(m+h)+\Lambda(m)+\Lambda(m+h)+2+\mathfrak S(h).
\tag{13}
\]
For \(K\le L\le X\), sum (13) on one block \(X<m\le2X\) and over \(h\le K\). Equations (9), (12) and \(\Psi(3X)\ll X\) give
\[
\sum_{X<m\le2X}\sum_{h\le K}|a_ma_{m+h}-c_h|
\ll XK+K\sqrt X\log^3X.
\tag{14}
\]
On this block use \(k_h\le1\) and \(b_T\ll_\omega1/(X\ell^2)\). Cover \((L,2U]\) by dyadic blocks starting at \(L\), truncating the final one. There are \(O(\ell)\) blocks, \(\log X\asymp\ell\) throughout, and
\(\sum X^{-1/2}\ll L^{-1/2}\). Their total is therefore
\[
O_\omega(K/\ell+K\ell L^{-1/2}).
\]
Add the already bounded infinite tail to obtain (3). In particular an arbitrary subset of \([1,K]\) obeys the same absolute upper bound.

## 6. RH gives a larger removable odd-shift range

Fix odd \(h\le X\). For real \(X<z\le2X\), define the exact prefix
\[
R_X(z,h)=\sum_{X<m\le z}[a_ma_{m+h}+1],
\quad P_X(z,h)=\sum_{X<m\le z}\Lambda(m)\Lambda(m+h).
\]
Since \(c_h=-1\), direct expansion, with all singleton terms retained, gives
\[
R_X(z,h)=P_X(z,h)
-[E(z)-E(X)]-[E(z+h)-E(X+h)]
+2[\lfloor z\rfloor-\lfloor X\rfloor-(z-X)].
\tag{15}
\]
The endpoint bracket has absolute value at most one. The same power-of-two argument gives \(P_X(z,h)=O(\log X)\) uniformly in this prefix and in all odd \(h\le X\).

Under RH, the classical bound \(|E(x)|\ll\sqrt x\log^2(2x)\) therefore gives
\[
\sup_{X<z\le2X}|R_X(z,h)|\ll\sqrt X\log^2X,
\quad h\text{ odd},\ h\le X,
\tag{16}
\]
with one constant. This is the legal square-root-scale bound. It is not the impossible sub-square-root premise in the coordinator's obstruction.

Apply summation by parts with (7), separately for each odd \(h\le K\). A block contributes at most
\[
\frac{C_\omega}{X\ell^2}
\sum_{\substack{h\le K\\h\text{ odd}}}
(1+h/(2X))^{-T}\sqrt X\log^2X
\ll_\omega K X^{-1/2}.
\tag{17}
\]
The dyadic sum is geometric, not \(O(\ell)\) times its worst term:
\(\sum_{X=L2^j}X^{-1/2}\le L^{-1/2}/(1-2^{-1/2})\).
This proves (4), with the infinite tail handled as before. It also proves the cardinality version for any subset of the odd shifts in \([1,K]\).

For comparison, ordinary PNT alone makes the maximum of \(|E(x)|/x\) on \([L,\infty)\) tend to zero. The identical argument then gives \(o_\omega(K/\ell)+O_\omega(K/(L\ell))+O_\omega(K2^{-T})\) uniformly for odd \(K\le L\). This weaker conclusion already removes odd \(K=O(\log T)\). The stated power range uses RH, not PNT alone.

## 7. What remains after removing these shifts

Choose any \(K_0=o(\log T)\) and \(K_1=o(T^{7/8})\), with \(K_1\ge K_0\). Under RH, removing all \(h\le K_0\) and all odd \(h\le K_1\) changes the exact \(\mathcal E_T\) by \(o(1)\). Thus the R21 sufficient signed target has the same limiting status after this explicit removal.

Nothing here estimates the remaining even shifts beyond \(K_0\), or the remaining odd shifts beyond \(K_1\). The typical Pareto scale is \(h\asymp m/T\), which ranges from \(T^{3/4}\) to \(T^{5/4}\) across the unchanged window. The odd-shift bound does not delete the whole scale in the upper wing, and the all-shifts bound does not approach it.

The coordinator's obstruction and this lemma are compatible: the former disproves a uniform prefix estimate that would suppress real singleton zeta fluctuations; the latter uses those fluctuations with their actual small weight. There is no implied uniform sub-square-root pair bound and no strict reduction of the AH saturation constant.

## Sources and verification scope

- The revised R21 centered-pair report supplies only the exact definitions, the signed target and its already proved transfer. Its version and the coordinator's original obstruction are pinned in the adjacent receipt. The proof above rederives the needed Abel norm.
- [Tao, 254A Notes 4, equation (22), Lemma 17 and Corollary 19](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/): classical fundamental upper sieve. The uniformity in our varying shift follows from (10)–(11), rather than the source's fixed-pattern Theorem 32.
- [Schoenfeld, Theorem 10, equation (6.2)](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf): the retained primary RH error bound, extended over a bounded initial interval by increasing an unspecified constant.

Any adjacent exact checker addresses finite algebra, endpoint identities and rational exponents only. It cannot prove the sieve theorem or replace the displayed ordinary uniform estimates. No primes at new heights or parameter scans are used.
