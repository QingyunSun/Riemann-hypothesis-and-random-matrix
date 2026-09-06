# Riemann zeros, random matrices and actual prime arithmetic

## Rounds 6–14: complete takeover supplement / 第 6–14 轮完整接棒补编

**Source checkpoint: `2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba`, 2026-09-05.** This book follows the earlier main handoff and Rounds 4–5 supplement. It prints the complete substantial reports and independent reviews from the subsequent work, including the final R14 proofs and both later Fable intakes. It is a faithful research archive, not an announcement that a famous conjecture has been solved.

**当前结论：没有证明 RH、Montgomery/GUE 猜想、AH-Pairs 的反驳、新的 ζ 半间隙定理或小于 186 的素数间隙。** 已完成的工作包括：真实算术误差项的两次改进、一个可在所需尺度下消去的精确 Type I 分量、有限 CUE 热流的定量误差、具有精确假设的反例与障碍，以及完整保留的负向变分实验。数值增益、普通证明、独立内部审查与形式验证在本文中始终分开。

The intended next researcher is GPT-6 Astra or a human analyst taking over without access to the live conversation. Read this synthesis first, then the integrated report for the chosen lane, then its full proof and independent review. The main earlier archive remains necessary for the original ACUE constructions, fixed-family arithmetic-transfer proof, Galilean heat lemma, force-energy identities, and Rounds 1–5 prime-gap certificates. Those earlier documents are linked by pinned source paths rather than silently reproduced under a new date.

## 1. What the programme is trying to prove

The main target is a substantive theorem about **actual zeta zeros** and the Montgomery–Dyson connection. Random-matrix examples and heat flow are tools for isolating missing hypotheses, not substitutes for the arithmetic explicit formula. The most concrete accepted reductions concern the precise AH-Pairs formulation, including its possible near-diagonal mass. General AH must not be replaced by a simple hard-core process with gap at least one half. Multiplicity or near-coincident pairs can occupy the zero lattice point. An arbitrarily small gap, or a positive proportion of gaps below one half, need not by itself refute the full hypothesis unless the statistic also excludes that near-zero freedom.

There are three explicit formulations of the arithmetic target. Each is sufficient under its recorded RH and limiting hypotheses; none has been proved here.

**Notation warning / 记号须按章节理解.** N denotes the CUE matrix dimension in the heat-flow reports, the Dirichlet cutoff floor(T/log⁶T) in the resolvent reports, and a short factor of size X^.4 in the R13 Type II discussion. These are different objects. D_N is finite polynomial heat depth, while \(\mathcal D_{\mathcal Q}^V\) is an arithmetic progression discrepancy. The resonator length L, a smooth long-factor length, and the L used to truncate the minimum-gap tail also have separate local meanings. Each full report resets its definitions. Exceptional close pairs in an RMT model do not by themselves refute a density-version AH statement for zeta.

### 1.1 The fixed two-width resolvent target

For fixed c>0 define

\[
I_T(c)=\int_0^T\left|\frac{\zeta'}{\zeta}
\left(\frac12+\frac c{\log T}+it\right)\right|^2dt,
\qquad
W_T=\frac{2[\sinh(2)I_T(1)-\sinh(1)I_T(1/2)]}{T\log^2T}.
\]

Under RH and AH-Pairs, the reviewed reduction gives

\[
W_T\longrightarrow W_{\rm AH},\qquad
0.06239<W_{\rm AH}<0.06240<\frac1{16}.
\]

The sine-kernel prediction is approximately 0.0822714431214773. Therefore

\[
\boxed{\liminf_{T\to\infty}W_T\ge\frac1{16}}
\]

would refute AH-Pairs under RH. The previously discussed target 0.07 is also sufficient, but unnecessarily strong. The two widths were chosen to cancel the bounded near-diagonal parameter P₀(T) exactly; no convergence of that parameter is assumed. Tail truncation, finite-height endpoints, the Gamma factor, ξ′/ξ normalization and the holomorphic-square passage are part of the printed proof and reviews. The reduction itself is established; the displayed actual-zeta lower bound is not.

### 1.2 A compact out-of-band Fourier test

Fix the recorded nonnegative smooth bump φ, integral one, supported on [6/5,7/5] and symmetric about 13/10. For the normalized form factor F_T,

| Observable | RH + AH-Pairs prediction | Sine-kernel prediction |
|---|---:|---:|
| ∫φ(α)F_T(α)dα | 7/10 | 1 |
| Centered prime-covariance remainder | −3/5 | −3/10 |

An actual lower limit strictly above 7/10 for the first observable, or strictly above −3/5 for the corresponding centered remainder, would exclude AH-Pairs. The limit 1 would establish this one smooth Montgomery prediction. It would not automatically prove the entire pair-correlation conjecture or RH. The full prime-prime term, prime-continuum cross terms, continuous mean square and diagonal must remain present.

### 1.3 A shrinking mesoscopic correction

The residual route uses N=floor(T/log⁶T) and

\[
R_c(t)=-\frac{\zeta'}{\zeta}\left(\frac12+\frac c{\log T}+it\right)
-\sum_{n\le N}\Lambda(n)n^{-1/2-c/\log T-it}.
\]

Round 8 proves under RH that W_T=B+\(\mathcal E_T\)+o(1), where B≈0.4560939793292317 and

\[
\mathcal E_T=
\frac{2[\sinh(2)\|R_1\|_2^2-\sinh(1)\|R_{1/2}\|_2^2]}{T\log^2T}.
\]

The fixed-width sufficient target is therefore liminf \(\mathcal E_T\)≥−0.3935939793292317…. The residual combination is signed and of leading order. Positivity of its two individual energies does not prove the target.

For b=2c set r_T(b)=\(\|R_{b/2}\|_2^2/(T\log^2T)\). The coupled statistic

\[
\mathcal C_T(b)=b^2\left[
2\sinh b\,r_T(b)-2\sinh(2b)\,r_T(2b)-\frac1{2b}\right]
\]

has sine prediction 0 and AH prediction −3/4 after the same nuisance cancellation. The sufficient lower bound has uniform quantifiers on a slowly growing envelope G(T)=o(log log T), followed by B→∞:

\[
\lim_{B\to\infty}\liminf_{T\to\infty}
\inf_{B\le b\le G(T)}\mathcal C_T(b)>-\frac34.
\]

A fixed-width limit does not authorize a prescribed growing rate. The needed error is a first correction of relative order 1/b, not merely a leading relative o(1) estimate. The reports state an equivalent sufficient signed logarithmic mixed-moment bound. Its positive diagonal is explicit, but its centered off-diagonal remainder remains open.

## 2. The strongest arithmetic results at this checkpoint

Write X=T^α with 6/5≤α≤7/5, H=X/T, and Q=X^(523/1000). Thus H ranges from X^(1/6) to X^(2/7). The selected complementary squarefree modulus family is inherited from the 186 paper's verified ordinary analytic input. Repeated representations of one modulus are counted only once. These numbers belong to a particular arithmetic component; 0.523 is not a zero-distribution exponent or a new prime-gap record.

The exact smooth discrepancy retains a fixed V(h/H), the original sinc kernel, μ(q) log((m−h)/q), and the primitive principal sum. Its useful bounds progress as follows.

| Stage | Proved bound for the specified discrepancy | Assumptions and remaining limitation |
|---|---|---|
| R9 source transfer, summed absolutely over h | O_A(HX log^(−A)X) | Ordinary source theorem; fixed logarithmic saving cannot absorb polynomial H. |
| R10 shift completion | O(√(HX(X+Q²)) log⁴X) | Unconditional; original smooth joint kernel restored after separation. |
| R11 centered small arcs | O(√(X(X+Q²)) log⁵X)=O(X^1.023 log⁵X) | Under RH; removes √H, but remains above X log X. |
| R14 short Möbius divisor portion | O_J(HX(UQ/X)^J log²X) | Unconditional for UQ≤X/2 and fixed J≥2; the exact signed remainder is retained. |

Round 11 uses an actual RH centered-prime small-arc estimate, including its derivative version, before sampling at the rational frequencies. Equal fractions are merged first. Its coefficient band mass and local arc length cancel H. The integer mean and primitive Ramanujan mean are treated separately and both remain accounted for. This is a genuine improvement of a defined arithmetic error bound. It still leaves a factor X^.023, apart from logarithms, above the required covariance scale. It is not a proof that this factor is necessary for primes.

Round 14 makes a further exact reduction. Define

\[
\Lambda_{\le U}(n)=\sum_{r\mid n,\ r\le U}\mu(r)\log(n/r),
\qquad \Lambda=\Lambda_{\le U}+\Lambda_{>U}.
\]

For U=X^.4 and J=4, the bound for the first portion is O(X^(1711/1750)log²X)=o(X log X). More generally every fixed η>0 with η<.477 permits U≤X^(.477−η), choosing fixed J with Jη>2/7. This follows from exact progression Poisson summation in the genuinely smooth long cofactor. Its zero mode cancels the actual primitive principal term. The normalized joint kernel has uniform derivatives; no regularity is assigned to the short Möbius sequence. A product of several rough long factors does not satisfy this hypothesis merely because its total length exceeds Q. The remaining Λ_{>U} discrepancy is an exact signed arithmetic object and is unestimated.

The strongest full selected smooth-packet bound is consequently still the R11 RH estimate. The short-divisor removal identifies a smaller residual problem; it is not a bound for every remaining piece. The complete covariance additionally requires complementary moduli, support main terms, other ranges and continuous centering. None may be suppressed because the selected component is attractive to calculate.

## 3. The finite CUE theorem that is now on firm ground

For Haar CUE(N), let δ_min be the smallest angular gap, and B_N the inverse-square circular background at that gap's midpoint. Round 14 proves directly from the exact finite-N three-point Gram determinant that

\[
\mathbb E\sum_{i:\delta_i\le\varepsilon} B_i
\le\frac{N^6\varepsilon^3}{18},\qquad 0<\varepsilon\le\pi.
\]

The endpoint zeros in the determinant cancel the singular endpoint weight. The proof enlarges an endpoint-weighted count to all short ordered pairs only after that cancellation; enlarging a midpoint-weighted count directly would be invalid. Circular ordering includes the wrap gap. No conditional density of a selected minimum is assumed. Combining the estimate with the classical CUE minimum-gap law gives B_N/N²=O_p(1), with an explicit truncation-tail bound.

For the specified scalar-heat evolution of the characteristic polynomial, with D_N its first positive discriminant time, the existing deterministic Galilean lemma then yields

\[
\frac{8D_N}{\delta_{\min}^2}-1=O_{\mathbb P}(N^{-2/3}),
\qquad D_N-\delta_{\min}^2/8=O_{\mathbb P}(N^{-10/3}).
\]

This is a quantitative approximation in probability for finite CUE. It is not a rate for convergence of the entire depth distribution, a theorem for general β, a stochastic Dyson Brownian motion theorem, or an established property of actual zeta zeros. The earlier qualitative ratio and deterministic lemma are explicitly credited in the new proof. No global literature novelty claim is made.

The distinction matters for the original research aspiration. RMT supplies a rigorous reference law and precise mechanisms. A zeta theorem needs the arithmetic hypothesis that forces the corresponding local behavior. Reusing the RMT conclusion under a name such as “alternative COE” cannot supply that missing hypothesis.

## 4. Failed approaches that materially changed the programme

### 4.1 More fixed resonator features did not cross the half-gap threshold

The original request to enlarge S₂/S₃ polynomials was checked against the archive before computation; it duplicated an earlier sweep. The replacement in R7 was the sharp integer mark for a prime divisor above √L. The fixed family has a direct unique-large-prime decomposition and a reviewed limiting arithmetic transfer. Its 30-dimensional half-gap margin is about −0.01465492379421, improving its matched baseline by only 1.429×10⁻⁸. It remains worse than the older 48-feature value near −0.0146547256.

A later proposed multiplicative profile also duplicated an already resummed experiment. R9 instead used the nonmultiplicative event of two distinct prime divisors above L^(1/3). Its unique unordered double-prime decomposition is exactly coprime; its singly marked formula requires an explicit repeated-prime error. The new fixed 30-dimensional margin is −0.0146549114371551 versus −0.0146549380840028 for its matched baseline, a floating gain of about 2.66×10⁻⁸ at scaled Gram condition about 5.36×10⁷. Its actual finite-integer frozen-vector test at L=100000 has margin −0.0374094621535042.

These are new concrete arithmetic families and useful transfer checks. The numerical gains are not interval-certified and are far from crossing zero. Their spans do not contain the entire older 48-feature space. They prove no global no-go for resonators, and do not justify another blind coefficient sweep. All coefficients and matrices remain in the repository with hashes.

### 4.2 Generic positivity does not deliver the arithmetic gain

The explicit R8 minorant gives a valid bound around −0.208674513 for W, far below 1/16. Optimality was proved only inside that fixed one-parameter family. A realized stationary half-grid determinantal process satisfies the available low-band information and positivity yet attains W_AH<1/16. This blocks an inference from those hypotheses alone. It does not describe actual primes or rule out an arithmetic theorem.

The two residuals do arise from the same centered arithmetic function ψ(x)−x, and after the justified prime-power removal from θ(x)−x. Their common origin is useful structure. Its mere existence, or the positivity of each residual norm, does not fix the sign of their weighted difference. The pole and endpoint terms must first be bounded; an unregularized infinite prime series in the critical strip is not a legal replacement.

### 4.3 Deterministic heat and protected traces do not force GUE

The R7 flow report supplies a deterministic contraction bound under its stated external-field condition, but leaves an actual-zeta boundary-propagation estimate open. Its exact finite polynomial family begins on a half-grid up to rotation and retains all normalized gaps at least one half under forward flow, tending toward a clock. This defeats a proposed implication from those dynamical hypotheses. It is not a counterexample obeying the full zeta explicit formula.

The protected trace algebra also remains matched under the recorded full DBM comparison. At a protected frequency m=N/2 the stochastic microscopic generator contribution at CUE is π². Thus a deterministic calculation cannot simply discard stochastic smoothing because a collection of low moments agrees. The original AH definition and the distinction between actual and artificial wrap gaps remain essential.

### 4.4 Actual conductor geometry obstructs norm-only shortcuts

R11 constructs an admissible terminal complementary family using two primes of exponent .09 and 346 distinct smaller primes of exponent 343/346000. It has ≫Q/log^348X moduli near Q. At terminal d=q>Q/2, no other permitted multiple exists, so the full Möbius coefficient is exactly 1/d. The coefficient squared mass is at least a constant times H/log^348X. This rules out a fixed-power coefficient-norm improvement for that full family. It does not rule out pruning, different weights, or cancellation with genuine prime sums.

R12 uses the same actual frequencies to prove sharpness up to logarithms for a positive sampling step, including its known local energy and derivative envelopes. The saturating polynomial is artificial. This is an obstruction to that general sampling argument, not a lower bound for the actual centered-prime functional and not evidence that X^.023 is unavoidable for primes.

### 4.5 Direct import of the 186 dispersion theorem fails specific premises

An additive twist of a genuine-prime short coefficient can lose the required Siegel–Walfisz property. The explicit modulus-3 example, at legal source scales M=X^.6 and N=X^.4, gives a discrepancy of leading size N/log N. The source theorem remains true; the transformed coefficient does not satisfy its hypothesis. The coherent shift interval also cannot be replaced by the Cartesian product of all its local residue images without an enormous class cost. Taking H itself as the short convolution length falls below the checked source range.

These failures identify what an averaged replacement must preserve: the joint m,a,d,h phases and cross-prime coherence. They do not prove that every averaged use of dispersion fails.

### 4.6 Short-interval theorems miss the needed scale or correction

The checked Guth–Maynard corollary concerns h≥X^(2/15+ε), with fixed ε. The mesoscopic shell here has exponent s/(b+s)→0. Even the corollary's ε-zero endpoint misses that shell for b>13; the following remark's slight fixed improvement does not resolve a vanishing exponent. Almost-all PNT counts also do not by themselves provide a variance constant.

The checked three-integral comparisons have constant losses larger than the shrinking sine-versus-AH signal. Their finite-T errors can be made small on a sufficiently slow diagonal, so it would be wrong to blame only height errors. The limiting lower bound misses a first correction. R12's actual Selberg audit retains both cutoff crossings and the joint mean, yet does not supply the necessary sign or b⁻³ precision in the mixed moment. These are source-specific quantitative failures, not a claim that all existing analytic methods are exhausted.

### 4.7 A positive rational core does not lower-bound the signed whole

R13 extracts the zero-rational Type II core with total RH replacement error O(X^.923 log²X), retaining the explicit integral main term. An admissible restricted positive block can have size at least a constant times X^1.123/log^348X. Other phases and the actual long coefficients may cancel it. R14 gives a constructive instance of such complete cancellation when a long factor is smooth.

The exact signed-kernel norm has a CRT/Poisson main term and an explicit remainder. Large original common divisors give short enough CRT periods for smooth decay. The small-gcd long-period terms remain. A coherent positive off-diagonal subsum of size at least a constant times Q²H/log^696X is not a lower bound for the complete signed remainder. Reduced denominator gcd and original modulus gcd are different quantities. Even an ideal unrestricted integer norm of order XH would not alone give the desired prime-specific bound.

## 5. The R6 prime-gap work that had not reached the earlier PDFs

R6 constructs the full signed cap operator, rather than defining an operator only through a 77×77 matrix. Its finite fragment measure is not a probability measure conditioned on the outer domain. The erased-coordinate adjoint is an unweighted lift with outer support. On product amplitudes the single erased g factor must not become a g² conditional expectation. The face multiplier can be negative; positive-semidefinite assumptions are invalid.

For the old mass-orthogonal projection P and a radial projection P_V that need not commute with it, the useful direction is

\[
r=(I-P)Tf,\qquad h=P_Vr,\qquad w=(I-P)h,
\qquad \langle f,Tw\rangle=\|h\|^2.
\]

For unit f, its normalized mixed entry is \(\|h\|^2/\|w\|\), not simply \(\|w\|\). The actual mass projection of Tf is used, without assuming an exact Ritz vector. The active radial cells are frozen and define the chosen subspace; small excluded mass is not a bound for omitted residual energy.

The fixed k=39 direct cap quotient rises from 0.9943963993644909 to 0.9944678209006830, about 71.4215 ppm. An exact dyadic-rational/polynomial-root certificate proves the stored direction is genuinely outside the old 77-space on positive-measure cells. That exact independence certificate does not certify the numerical gain. The Gram condition is large, the quotient is still about 5532.18 ppm below one, and arithmetic support restoration remains unproved for the candidate. The actual 2×2 plane supplies only about 1.26% of its crossing requirement, without estimating the full residual.

Four public compact NPZ witnesses retain all candidate and projection arrays except the regenerable 77×N density cache. The four original full archives remain local with hashes and array-by-array compaction receipts. This is explicit storage compaction, not deletion of adverse outputs. The prime-gap bound remains 186; the prior R4 rigorous margin gain and R5 geometry constraints should be read in their separate earlier supplement. Prime-gap broad sweeps were paused when the user redirected the main lane to actual zeta and Dyson–Montgomery.

## 6. Fable corrections must travel with their source snapshots

The 89393d5 intake repaired the moment coefficient to Π₄∼6aε⁻⁴, while also finding a sign error in the refuter's own derivative probe and a table mixing different v values. A successful replay of a refuter reproduces its failures; it does not certify every assertion in it. Finite drift does not disprove an asymptotic fixed-family limit without a proved constant and threshold. The later Astra fixed-family transfer remains separate from Fable's unfinished quantitative-rate discussion.

At 2073028 the corrected F1 coefficient and fixed-v table are accepted. The finite prime-sum cutoff is explained by the reviewed incomplete-gamma limit. The F3 assertion of an infinite field norm on the mass cutoff is false. A complete weighted sector proof gives, for g(u)=2sin(πu/2),

\[
\|K\|\le2\int_0^1\frac{|g(u)|^2}{u^2}du
=4\pi\operatorname{Si}(\pi)-8\approx15.27212735.
\]

This proves finite boundedness for the stipulated idealized operator and uniformly for the literal discrete grids. It lies above π²/2, so it proves no sharp spectral wall. The first interval has infinite du/u measure, and a nonzero constant there is not a normalized Galerkin basis vector. Numerical extrapolations near 4.6456 remain numerical evidence, with no proved full arithmetic-to-Fock transfer.

The general-β background repair is still only partial. Its purported exact finite-N CUE formula is a sine limit; its comparator vanishes at q=2π while the true normalized two-point density is one. Its uniform replacement v′=v(1+O(ε/w)) fails near an endpoint. A direct conditional triple integral restores the intended L^(β+1)c^(2β+1) exponents, but does not prove general-β density control. Uniform one-point intensity alone cannot control the background of a selected smallest pair: a randomly rotated clustered configuration is a counterexample to that inference. The independent R14 finite-CUE argument uses the needed higher correlation structure and does not rely on these uncorrected general-β claims.

Both intake reviews are printed in full below. The 141-file and 160-file Fable snapshots remain separately pinned in the repository; their complete duplicated source texts are not printed again in this supplement. This separation preserves original errors and later corrections without rewriting history.

## 7. Prioritized next work, with concrete success criteria

These are research proposals, not claims that any famous conjecture is now within a guaranteed final step. Prefer one bounded calculation or lemma with a falsifiable acceptance condition before a larger search.

1. **Estimate the actual remaining arithmetic term after R14 removal.** Start with the exact Λ_{>U} discrepancy, fixed U≤X^(.477−η), and the original joint sinc/log kernel. Use a stated Heath–Brown decomposition and preserve the primitive mean. Identify one remaining factor pattern and prove an aggregate bound strictly below X log X, or exhibit the exact source hypothesis that fails. A smooth long variable is already handled; relabeling that case is not new progress.
2. **Keep signed phase information through the long-variable average.** R12 forbids a blanket SW inheritance claim for twisted coefficients. R13 isolates rational cores and their main terms. A useful next theorem must estimate their full signed combination with the actual coefficients, not only a positive subblock or a norm for arbitrary integer polynomials. Record every denominator, numerator and gcd range. Success requires a power improvement over the X^1.023 bound or a directly useful signed covariance estimate, not a logarithmic cosmetic gain.
3. **Attack the mixed genuine-prime remainder at the exact first correction.** Use the finite centered measure and logarithmic companion already proved in R11. The positive diagonal is b⁻²+2b⁻³. A strict one-sided improvement for the combined off-diagonal remainder, or its integrated version, could imply the mesoscopic AH-excluding criterion. State uniformity through twice a valid slow envelope; keep the two prime-continuum terms and continuum square together. A mere O(1) energy bound is not the requested result.
4. **Use the CUE theorem as a precise reference theorem.** Any zeta heat-flow transfer must supply an actual local arithmetic hypothesis strong enough to control selected near-pair backgrounds and true boundaries. Test it against the half-grid, rotated-cluster and artificial-wrap examples before trying to prove it. A general-β extension would require a correct finite-N n=3 bound with the stated domain; it cannot be imported from weak process convergence alone.
5. **If returning to variational search, demand a structural reason for a gain.** The simple power-sum, resummed multiplicative, single-large-prime and double-large-prime directions are already archived. Choose a genuinely different fixed integer feature or a proved extension of the available mixed arithmetic form. Give exact coefficient meaning and a controlled transfer before treating a continuum model as a zeta test. A negative finite span is not a global barrier.
6. **Formalize selected stable components after proof review.** Good bounded candidates are the primitive Poisson cancellation, the exact mass-cutoff Fock inequality, the finite-N CUE Gram/singular-weight estimate, and the finite rational outside-span witness. The FLT formalization work motivates careful decomposition and proof checking; it supplies no unproved analytic input. A proof-assistant certificate must be reported separately from Python checks and internal reviews.

暂缓：同一负向系数空间的重复扫描、把普通 PSD 或点过程正性再包装成算术输入、忽略 ζ 的 pole/mean 交叉项、以假设缺失的 periodization 推出真实小间隙、重复开启 Fable 会话，以及把数值外推或程序复算称为已证明的历史级定理。研究主线应以“缺少的真实算术估计是否推进”为进度标准，而不是文件数或模型轮数。

## 8. 中文接棒判断与阅读顺序

最值得继续的变化，不是又找到了一个更像随机矩阵的模型，而是已经把若干模糊目标改写为可核查的真实算术不等式。第 7 轮消除了 AH 中可能不收敛的近零质量；第 8–11 轮把两个 resolvent 的能量差写成同一个中心化素数误差的耦合，并保留了必要的 pole、端点和连续均值；第 10–11 轮确实改进了指定误差项；第 14 轮又把其中一个完整、带原始权重的 Type I 分量严格消掉。这些结果值得保存，但距离所需的严格符号增益仍有未完成的算术部分。

有限 CUE 方面，现在有选定最小间隙背景在自然 N² 尺度的紧性和热碰撞时间的定量误差。这是一条清楚的普通证明链。它说明在真实 RMT 中什么条件足够，同时也明确揭示了向 ζ 迁移时缺少什么。不能把 CUE 的高阶相关性偷偷当作 ζ 的已知事实，也不能把一般 AH 偷换为没有重根的硬核 ACUE。

接手时建议先读 R14 综合报告，确认最新真正完成的两项结果；再读 R7/R8 确定终极目标和归一化；随后读 R9–R13 的真实算术链及失败的迁移假设。若选择变分路线，先读 R7/R9 的完整负向试验，避免重复。若选择素数间隙路线，先读 R6 与前一本 R4–R5 补编，注意 cap-only、支撑恢复和浮点/区间证书的区别。最后对照 Fable 两次审查，避免重新引入已被否定的公式。

0.6725007… 在本项目核对的源文献中是关于临界线上简单零点的无条件比例下界；它不直接估计本文的带外相关性。186 是此前源论文的素数间隙结论，本文没有改成更小。FLT 的形式化技术是一种组织和验证证明的方式，不会把缺失的算术引理自动补齐。希望得到重大定理的目标不变，但接棒者应对所有这些类别区别保持严格。

## 9. Evidence, preservation and reproducibility contract

Each complete source report below has its original repository path, pinned Git blob identity, SHA-256 digest and byte length in the JSON index. The assembler compares working bytes to that exact Git blob before use. It does not take the current working tree's newer contents on trust. All original mathematical statements, caveats, failed attempts, commands and review-status history remain in the embedded bodies. A historical “review pending” sentence is preserved when a later separately printed review supersedes it. Historical agent instructions are source records, not new instructions for the reader to execute.

Presentation changes are limited to the established `build_handoff.cleaned` transformations, heading nesting, resolving Markdown links/images to the source checkpoint, and spelling vertical bars inside table-cell inline mathematics as equivalent LaTeX commands. Raw single bars become `\vert` and existing LaTeX double bars become `\Vert`; this prevents Markdown from treating mathematical bars as column separators. Every replacement is recorded with its source line and column, and no mathematical meaning is changed. Code fences and inline code are protected from this table repair. The JSON index records the digest of each displayed body as well as its raw source. Any later layout-only adjustment belongs in a separately recorded rendering step, not a silent source edit.

Code, JSON certificates, arrays, small plots, run logs and integration receipts are retained as repository artifacts by path and hash rather than printed as enormous tables. The index covers the selected round/review folders and their integration-log folders. Earlier proof dependencies and snapshot manifests reached by resolvable source links are indexed too. Third-party full papers and optional large original caches remain in the adjacent local archive where the source receipts say so; their absence from the public book is not concealed. The one in-report R6 figure is linked to the pinned raw image.

Rebuild this Markdown and index from the repository root with:

```text
python3 tools/build_round6_14_handoff.py
```

The per-round recheck scripts printed in the reports are the appropriate bounded acceptance surfaces. Some require pinned local primary PDFs or earlier runtime dependencies; read their supplied arguments before running. An exact finite check validates its algebraic case, not an asymptotic prime theorem. Agreement of floating matrices, a tiny eigensolver residual or a reproduced fit is not an interval enclosure. Internal independent review is not external peer review or Lean verification. This supplement itself performs assembly and provenance checks only; it does not rerun the mathematical experiments.

For the earlier context, retain the pinned main archive and R4–R5 supplement alongside this book. The present index is a precise catalogue of later-round coverage, not a claim to include private conversations or every earlier source document for a second time.

## Complete source texts / 完整原文目录

| No. | Group | Source report |
|---:|---|---|
| 01 | R6 | [Round 6: a full signed-operator direction beyond the 77-dimensional sieve trial](#report-01) |
| 02 | R6 | [The full signed cap operator and a mass-orthogonal direction beyond 77 dimensions](#report-02) |
| 03 | R6 | [Residual directions outside the 77-dimensional sieve trial space](#report-03) |
| 04 | R6 | [Independent finite marked-space regression for the signed sieve operator](#report-04) |
| 05 | R6 | [Round 6: one full cap-operator residual beyond the 77-dimensional family](#report-05) |
| 06 | R6 | [Provenance and compact witness export](#report-06) |
| 07 | R6 | [Independent review of the frozen radial profile outside the old span](#report-07) |
| 08 | R7 | [Round 7: two explicit actual-zeta targets for Dyson–Montgomery](#report-08) |
| 09 | R7 | [Two Poisson scales remove the AH near-diagonal parameter](#report-09) |
| 10 | R7 | [Independent review of the two-scale actual-zeta reduction](#report-10) |
| 11 | R7 | [Independent review of the actual-zeta Poisson transfer](#report-11) |
| 12 | R7 | [One actual-zeta target beyond Fourier support one](#report-12) |
| 13 | R7 | [Forward true-zeta localization: a contractive comparison and a sharp universality obstruction](#report-13) |
| 14 | R7 | [Arithmetic transfer for a fixed large-prime sector](#report-14) |
| 15 | R7 | [Round 7: an arithmetic large-prime sector for zeta's half-gap problem](#report-15) |
| 16 | R7 | [Independent audit of the half-threshold arithmetic transfer](#report-16) |
| 17 | R8 | [Round 8: isolate the actual arithmetic remainder](#report-17) |
| 18 | R8 | [The actual-zeta two-scale target: short-prime projection and a centered tail](#report-18) |
| 19 | R8 | [Independent audit of the actual-zeta short-polynomial identity](#report-19) |
| 20 | R8 | [A bounded positivity audit of the two-scale target](#report-20) |
| 21 | R8 | [Independent review of the fixed positivity minorant](#report-21) |
| 22 | R9 | [Round 9: actual prime arithmetic for the Dyson–Montgomery programme](#report-22) |
| 23 | R9 | [A concrete 186-to-covariance transfer beyond the square-root divisor level](#report-23) |
| 24 | R9 | [Independent review of the complementary-modulus covariance component](#report-24) |
| 25 | R9 | [A fixed interaction between two large prime divisors](#report-25) |
| 26 | R9 | [Round 9: duplicate profile avoided, two-prime interaction tested](#report-26) |
| 27 | R9 | [Independent review: the fixed two-large-prime interaction](#report-27) |
| 28 | R9 | [Prime powers are negligible in the remaining residual energy](#report-28) |
| 29 | R9 | [Independent review of the actual prime-power tail estimate](#report-29) |
| 30 | R9 | [Mesoscopic damping: the missing arithmetic edge term and its rate requirements](#report-30) |
| 31 | R9 | [Independent review of the mesoscopic edge obligation](#report-31) |
| 32 | R10 | [Round 10: a power saving for one actual shifted-prime discrepancy](#report-32) |
| 33 | R10 | [A power improvement for a smooth packet of the actual shifted discrepancy](#report-33) |
| 34 | R10 | [Independent audit of the completed-shift coefficients and spacing bound](#report-34) |
| 35 | R10 | [Independent review: actual shift kernel and genuine-prime replacement](#report-35) |
| 36 | R10 | [Actual-prime variance ranges and a missing logarithmic mixed moment](#report-36) |
| 37 | R10 | [Independent review of the arithmetic range and mixed-moment audit](#report-37) |
| 38 | R11 | [Round 11: remove the shift-length loss using actual RH prime input](#report-38) |
| 39 | R11 | [Removing the shift-length loss from the actual completed pairing, under RH](#report-39) |
| 40 | R11 | [Independent review of the RH centered-small-arc improvement](#report-40) |
| 41 | R11 | [A real-prime subfamily prevents a coefficient-only power saving](#report-41) |
| 42 | R11 | [Independent review of the canonical conductor-mass construction](#report-42) |
| 43 | R11 | [The log-weighted prime-tail moment: a primary-source check and its arithmetic remainder](#report-43) |
| 44 | R11 | [Independent review of the centered mixed-moment remainder](#report-44) |
| 45 | R12 | [Round 12: three exact tests of the remaining arithmetic gap](#report-45) |
| 46 | R12 | [The actual support saturates positive sampling at the power scale](#report-46) |
| 47 | R12 | [Independent review of the inherited count and sampling constants](#report-47) |
| 48 | R12 | [Two explicit hypothesis failures in the proposed dispersion transfer](#report-48) |
| 49 | R12 | [Direct Selberg control of the centered mixed remainder: the precision and sign gap](#report-49) |
| 50 | R12 | [Independent review of the three bounded Round 12 attempts](#report-50) |
| 51 | R13 | [Dyson--Montgomery round 13: extract a rational core and retain the signed remainder](#report-51) |
| 52 | R13 | [Averaging the rational resonances: one power-saving extraction, and its retained main term](#report-52) |
| 53 | R13 | [Round 13 — Genuine-prime minor arcs and a fixed-inner-interval averaging audit](#report-53) |
| 54 | R13 | [The signed kernel norm: exact main term and a large coherent CRT remainder](#report-54) |
| 55 | R13 | [Independent audit of the smooth signed-kernel norm](#report-55) |
| 56 | R13 | [Round 13 independent integration review](#report-56) |
| 57 | R14 | [Dyson--Montgomery round 14: an actual Type I removal and a quantitative CUE heat theorem](#report-57) |
| 58 | R14 | [A smooth long factor removes an actual Type I component](#report-58) |
| 59 | R14 | [Independent review: smooth long-factor removal](#report-59) |
| 60 | R14 | [CUE background at the selected smallest gap: a direct finite-N bound](#report-60) |
| 61 | R14 | [Independent review: selected CUE background and the finite heat rate](#report-61) |
| 62 | R14 | [Independent root review: two bounded R14 advances](#report-62) |
| 63 | Fable intake | [Fable PR11 snapshot 89393d5: separate intake and two-sided arithmetic audit](#report-63) |
| 64 | Fable intake | [Independent background and boundary objections to the same Fable snapshot](#report-64) |
| 65 | Fable intake | [Fable 2073028: repaired arithmetic, finite Fock bound and retained gaps](#report-65) |
| 66 | Fable intake | [Independent audit of the F1 cutoff repair and F3 mass bound](#report-66) |
| 67 | Fable intake | [F1 repair: corrected coefficient, surviving sign issue, and cutoff scaling](#report-67) |
| 68 | Fable intake | [The mass cutoff gives a finite Fock operator bound](#report-68) |
| 69 | Fable intake | [Independent follow-up: CβE background repair at 2073028](#report-69) |

<a id="report-01"></a>

# Current report 01: Round 6: a full signed-operator direction beyond the 77-dimensional sieve trial

**Collection:** R6 — full signed prime-sieve operator and residual direction.

**Source:** [research/reports/prime186_round6.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/prime186_round6.md).

**SHA-256:** `e1d83da09a54cf3cf9f2fd77b3ec5f246c00cd1647ba3954146152d2e417003c`. **Git blob:** `8f627cc49aa9f211a8f09e0e92330ac0a1a1b5ab`. **Original bytes:** 11486.

## Round 6: a full signed-operator direction beyond the 77-dimensional sieve trial

The new fixed-geometry k=39 cap trial has directly evaluated quotient **0.9944678209006830**, up from **0.9943963993644909** by approximately **71.4215 ppm**. This improvement comes from a direction generated by the full cap operator outside the old 77-dimensional space. A separate exact algebraic certificate proves that the frozen new direction is outside that space. The gain itself remains a floating-point result; the quotient is still approximately 5532.18 ppm below one, and the actual arithmetic support has not been restored. No smaller prime gap is proved.

This is the completed bounded diagnostic requested after [Round 5](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/prime186_round5.md). It is unrelated to the earlier finite zeta operator K_L. It neither repeats the same 77-by-77 eigenproblem nor performs another radius sweep.

### 1. Full operator, actual measure and signed weights

The source Hilbert space is \(\mathcal H=L^2(H_O,\nu^{\otimes39})\), where \(\nu\) is the finite fragment measure. It is not a probability measure conditioned on the outer domain. Profiles are extended by zero. Erasing coordinate i means

\[
(E_i f)(Y)=\int f(Y\oplus_i X)\,d\nu(X),\qquad
(E_i^*v)(X)=1_{H_O}(X)v(X_{\widehat i}).
\]

Freeze the original geometry, the exceptional constant 0.34 and all hybrid parameters. With

\[
a_h=0.9919601604,\quad b_h=-0.000843183,\quad d_0=0.0088830226,
\]

the full cap operator is

\[
T_{\rm cap}=\rho_*\sum_i E_i^*
(d_0 1_{H_{0,i}}+a_h1_{H_{1,i}}+b_h)E_i.
\]

This formula acts on arbitrary profiles in the Hilbert space; it is not a definition by a 77-dimensional matrix. The face multiplier takes values 1, \(a_h+b_h\), and the negative value \(b_h\). The operator is bounded and self-adjoint, with

\[
-\rho_*|b_h|C_{\rm op}I\le T_{\rm cap}\le\rho_*C_{\rm op}I,
\qquad C_{\rm op}\le4
\]

in the fixed support range. No positivity assumption is used.

The actual arithmetic operator additionally uses the complete inner predicates and the outer projection \(P_O\). Its supported quotient has denominator \(\|P_Of\|^2\). That denominator cannot be replaced by \(\|f\|^2\) unless f is already supported on O. A cap improvement, even one exceeding one, would still require this restoration step.

The [full derivation](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/operator-proof/FULL_SIGNED_CAP_OPERATOR.md) checks the source measure, adjoints, boundedness, overlap integrals and the exact finite cell representation. For the fixed inward cap domains, profiles constant on total-cell/fragment-layer atoms form an invariant subspace of the full cap operator. Thus the step trial has no omitted within-atom action component. It can still have a large component outside the 77 polynomials. The actual tail/prefix support predicates require more fragment information and do not inherit that atom invariance.

### 2. A radial compression that exposes a new direction

Let U be the old 77-dimensional step-polynomial space, P its true mass-orthogonal projection, Q=I−P, and f the stored optimized trial. Put \(G=\prod_i g(t_i)\). Choose the closed subspace

\[
V=\{G\phi(s):\phi\text{ is arbitrary on a fixed selected set of radial cells}\}.
\]

U and V are not nested, and their projections need not commute. The construction is

\[
r=QTf,\qquad h=P_Vr,\qquad w=Qh.
\]

It follows exactly, for every f in U, that

\[
\langle f,Tw\rangle=\|h\|^2,\qquad
\|w\|^2=\|h\|^2-\|Ph\|^2.
\]

For unit f the two-dimensional off-diagonal entry is therefore

\[
\beta=\frac{\|h\|^2}{\|w\|},
\]

not simply \(\|w\|\). No exact Ritz assumption is needed, because the implementation computes \(PTf\) from the full mass projection \(M^{-1}Bc\), rather than replacing it with \(\lambda f\).

Writing q for the radial pushforward of \(1_{H_O}G^2\nu^{\otimes39}\), D for the basis cross-mass densities, and b for the pushed-forward pairing with Tf, the radial profile is

\[
\phi(s)=1_{\rm active}(s)\frac{b(s)-D(s)^{\mathsf T}M^{-1}Bc}{q(s)}.
\]

All fragment-cap layers and their signed face contributions are integrated before this projection. One-dimensional adjoint convolutions evaluate b. The single erased factor g, the reciprocal output factor \(1/g(t_i)\), the mesh factor and the common tilt normalization are retained. A normalized conditional average under \(g^2\nu\) would give a different operator.

The active radial set is frozen from the declared numerical cutoff. It defines V; the experiment does not claim that excluded cells carry no residual energy. In particular, a small excluded q-mass does not bound omitted \(\|r\|^2\).

### 3. A separate exact certificate of leaving U

The numerical norm calculation is not the only evidence that the new direction is outside U. The stored float64 profile is a specified finite list of exact dyadic rationals. Its entries at radial indices 0 through 12 are exactly zero, while

\[
\phi(18422)=-\frac{6264072493613325}{4611686018427387904}\ne0.
\]

Fix the other 38 coordinate cells at index zero and vary the first coordinate cell index r. After dividing by the common positive product G, each original basis function is a polynomial in r of degree at most 12: at most six from its radial power and at most six from its power-sum signature. If the frozen radial function belonged to U, the resulting polynomial would vanish at 13 distinct indices and hence everywhere, contradicting the displayed nonzero entry.

The argument concerns positive-measure product cells, not isolated points. Exact rational inequalities place every selected coordinate cell below the smallest cap and the whole product cell inside the first outer shell. Its measure is the positive number \(h_{\rm mesh}^{39}\). An [independent reviewer](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/operator-diagnostic/OUTSIDE_SPAN_INDEPENDENT_REVIEW.md) decoded the binary NPZ directly and checked the nonzero rational and these support inequalities. That review verifies the polynomial-root argument; it does not independently rerun the additional modular-rank computation below.

A second finite certificate evaluates the old basis at 77 explicit positive-measure cells and obtains rank 77 modulo 1,000,000,007. The new radial column is zero at these cells and nonzero at the additional cell, proving rank 78 over the rationals. See [the certificate script](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/operator-diagnostic/certify_outside_span.py) and [exact receipt](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/operator-diagnostic/outside_span_certificate.json).

These certificates establish independence of the frozen functions. They do not bound the quantitative distance to U or certify the Rayleigh gain. Those remain separate integral questions.

### 4. What the bounded numerical experiment gives

For the official 98,304 grid, tilt 20 and density cutoff \(10^{-9}\):

| Quantity | Observed value |
|---|---:|
| Original 77-space matrix quotient a | 0.9943963991909279 |
| Radial compression norm squared | 0.00006670688589594228 |
| Outside-U norm squared | 0.00006589186717477095 |
| Fraction of radial norm squared remaining outside U | 0.9877820901062194 |
| Normalized new-direction diagonal b | 0.043583189070450945 |
| Actual normalized mixed entry beta | 0.008217784708256407 |
| Larger eigenvalue on span(f,w) | 0.9944674193880856 |
| Full 78-space matrix quotient | 0.9944678209367751 |
| Direct evaluation of the final profile | 0.9944678209006830 |

The simple two-dimensional gain is 71.0202 ppm. Reoptimizing the other coefficients adds approximately 0.40155 ppm. For the realized two-dimensional plane, crossing one would require \(\beta^2>(1-a)(1-b)\); the observed coupling squared supplies only about 1.26% of that threshold. This describes that plane, not the uncomputed full residual.

The [detailed report](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/residual-trial/REPORT.md) preserves the coarse calculation and two controls. Tilt 20 and tilt 25 matrix values agree to approximately \(2.2\times10^{-16}\); their direct values differ by approximately \(1.53\times10^{-10}\). Changing the density cutoff from \(10^{-9}\) to \(10^{-8}\) shifts the result by about 0.0177 ppm. The old scaled mass Gram condition number remains approximately \(2.28\times10^{10}\). Small residuals and agreement between contractions are not outward rounding bounds.

A separate root process replayed the fine calculation in an isolated copy. Its matrix quotient, direct quotient, compressed norm, outside norm, coupling, active cells and radial profile agree exactly with the recorded run. That reproducibility does not replace interval certification.

### 5. Where this particular radial signal appears

![Observed radial energy and product-weight mass](https://raw.githubusercontent.com/QingyunSun/Riemann-hypothesis-and-random-matrix/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/operator-diagnostic/radial_energy_profile.png)

The plot uses the saved arrays, with no new operator integration. Half the observed radial compression energy lies below normalized radius approximately 0.95403; its peak is approximately 0.95599, close to the inner cutoffs. The central half lies between approximately 0.94578 and 0.97133. This localization suggests examining the transitions of the face domains when designing a less restrictive compression, but does not establish a causal explanation. The comparison curve is the product-weight mass \(G^2\), not the optimized trial's \(f^2\) mass. This is the radial projection's energy, not the full residual's energy.

### 6. Independent checks, stored data and remaining work

The [independent residual audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/residual-audit/SIEVE_RESIDUAL_AUDIT.md) gives the correct nonnested identities, approximate-Ritz corrections, inverse-Gram error formulas and signed crossing criteria. Eighty exact rational indefinite-operator examples and finite weighted-measure tests pass. A separately written [38-state marked model](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/operator-diagnostic/FINITE_MARKED_OPERATOR_AUDIT.md) checks nonuniform product mass, nonrectangular support, noncommuting projections and an explicit negative quadratic witness. Neither toy model estimates the prime-sieve operator.

The [integration receipt](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/logs/round6-integration/recheck.json) records exact replay of both algebraic test suites and the saved-output audit, followed by one fine-grid numerical replay. All original outputs are retained. Four compact NPZ witnesses publish every candidate and projection array except the reproducible 77-by-N D cache. The 183,046,525 bytes of original full NPZ files are preserved in the local archive; their hashes and array-by-array compaction checks are public. No coefficient, active cell, scalar result or new radial profile is omitted from the compact witnesses. The separate [archive check](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/logs/round6-integration/archive_check.json) verifies all 37 verbatim intake files, all 44 retained arrays against the full originals, Python syntax, report links and an isolated replay of the exact independence certificate.

The earliest route to a rigorous variational gain would freeze rational coefficients and the radial profile, then enclose its ordinary mass and signed mixed forms directly. That would avoid depending on an exactly computed orthogonal projection. Since the current value remains below one, it would not itself yield a smaller prime gap. The next substantive decision is whether another implementable compression captures substantially more of the full cap residual, or whether a new support/product profile is needed. The full residual norm and the true support-restored form remain uncomputed. No further iteration is included in this checkpoint.


<a id="report-02"></a>

# Current report 02: The full signed cap operator and a mass-orthogonal direction beyond 77 dimensions

**Collection:** R6 — full signed prime-sieve operator and residual direction.

**Source:** [research/prime-gaps/round6/operator-proof/FULL_SIGNED_CAP_OPERATOR.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/operator-proof/FULL_SIGNED_CAP_OPERATOR.md).

**SHA-256:** `020099a5ab6927f17b82dfbb2b96aa5b2cfbc3720c41d388f9c8f39b08d0339b`. **Git blob:** `a2e19c9a336fa654171c4bf75b182f54be3f319e`. **Original bytes:** 21540.

## The full signed cap operator and a mass-orthogonal direction beyond 77 dimensions

Status: ordinary-mathematics derivation and independent implementation review, 5 September 2026. The results below concern a fixed cap geometry and its true fragment measure. They do not certify a new prime gap, replace arithmetic support restoration, or assert positivity of the hybrid operator.

### 1. Sources and the precise question

The pinned official source is [OpenAI, PrimeGaps186, commit 61340d0b74163003b32756bb16e91d9209a5e330](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330). The mathematical inputs used here are the main paper, equations (3.15)–(3.24), Lemma 3.8, and equations (4.28)–(4.40), and the numerical companion, §1.1 and equations (2.12)–(2.15). The local source copies and hashes are recorded in the adjacent provenance JSON. The published 77 coefficients define a trial space; they do not define the full variational operator.

For the fixed original geometry, use the exact inward cap cells of the companion, recomputed with outer dimension $k=39$ and face dimension $k-1=38$. This is the geometry evaluated by `round5/geometry-trial/cap_trial.py` with its default configuration. The ordinary Hilbert-space arguments apply to every fixed $k>1$ and every such nested family. They do not inherit the original $k=40$ numerical support-error certificate for $k=39$.

The task is to identify the full operator $T$, its actual mass inner product, and a rigorously meaningful direction outside the 77-dimensional space. A further practical goal is to evaluate one such direction without forming the enormous full matrix or calculating the entire norm of $Tf$.

### 2. Measure, erasure, and adjoint

Let $\Omega_\zeta$ be the space of fragment multisets in $(0,\zeta]$, equipped with

$$
\nu=\nu_\zeta=e^\gamma\zeta\,\mathcal L(\Pi_\zeta),
\qquad d\Pi_\zeta\text{ has intensity }du/u.
$$

The prefactor is the product $e^\gamma\zeta$, not $e^{\gamma\zeta}$. This is a finite measure, not a probability measure. If $t=|X|$ is the sum of the fragments, then its pushforward is $\rho_D(t/\zeta)\,dt$. For $0<c\le\zeta$,

$$
\nu\big|_{\{\max X\le c\}}=\nu_c,
\qquad (|X|)_*\nu_c=\rho_D(t/c)\,dt.
\tag{1}
$$

Thus a prime cap changes the actual restricted measure. It does not condition a probability distribution, and totals larger than the cap remain possible. The factor $c/\zeta$ from the Poisson void probability has already canceled the change of prefactor in (1).

Let $H_O\subset\Omega_\zeta^k$ be the outer cap domain and set

$$
\mathcal H=L^2(H_O,\nu^k),\qquad
\langle f,g\rangle=\int_{H_O}\overline f g\,d\nu^k.
$$

Every function is extended by zero outside $H_O$. Write $Y=X_{\widehat i}$ for the retained tuple and $Y\oplus_i Z$ for insertion in coordinate $i$. Define

$$
(E_i f)(Y)=\int f(Y\oplus_i Z)\,d\nu(Z).
\tag{2}
$$

The face space uses $L^2(\Omega_\zeta^{k-1},\nu^{k-1})$. Direct Fubini gives

$$
(E_i^*v)(X)=\mathbf1_{H_O}(X)v(X_{\widehat i}).
\tag{3}
$$

In particular, erasure is an integral, not a conditional mean. There is no factor $k$, $h$, or $Z$ in (2) or (3). The companion divides every quadratic form, including face pairings, by the same constant $(hZ)^k$. Multiplying both Hilbert inner products by this same constant leaves (3) unchanged. Independently normalizing the $k$- and $(k-1)$-coordinate spaces would change the adjoint and would not reproduce the source conventions.

### 3. Three different operators must remain distinct

Let $H_0\subset H_1$ be the cap-only face domains. Let $L_0\subset L_1$ be the actual face domains, with $L_a\subset H_a$. In the source,

$$
L_1=H_1\cap L_{\rm new},\qquad
L_0=H_0\cap L_{\rm old}\cap L_{\rm new}.
$$

Let $O\subset H_O$ impose the actual outer source predicates, and write $P_O=\mathbf1_O$. With the source's fixed hybrid parameters,

$$
m=0.99998,\quad \lambda_h=0.008,\quad K_{\rm ex}=0.34,
$$
$$
a_h=m^2-m\lambda_h=0.9919601604,
\quad b_h=(1-m/\lambda_h)(1-m)K_{\rm ex}=-0.000843183,
$$
$$
d_0=1-a_h-b_h=0.0088830226.
$$

These constants belong to the fixed original physical outer radius. Changed geometry requires its own exceptional constant, as audited in Round 5.

Define the face multipliers

$$
m_H=d_0\mathbf1_{H_0}+a_h\mathbf1_{H_1}+b_h,
\qquad
m_L=d_0\mathbf1_{L_0}+a_h\mathbf1_{L_1}+b_h.
\tag{4}
$$

Their respective values on the three nested regions are $1$, $a_h+b_h$, and $b_h$. The last value is negative. The implemented full-face mask $H_f$ contains the support of every erased marginal of an outer-supported profile, so writing the last term as $b_h\mathbf1_{H_f}$ in the finite engine gives the same quadratic forms as the unrestricted $b_h$ in (4). The source operators and the threshold-normalized operators are

$$
A=\sum_{i=1}^kE_i^*m_HE_i,\quad
B=\sum_{i=1}^kE_i^*m_LE_i,
$$
$$
T_{\rm cap}=\rho_*A,\qquad
T_{\rm inner}=\rho_*B,\qquad
T_{\rm arith}=\rho_*P_OBP_O.
\tag{5}
$$

Here $\rho_*=2624989/10^7$. Explicitly, the full cap action is

$$
(T_{\rm cap}f)(X)=\rho_*\mathbf1_{H_O}(X)
\sum_i m_H(X_{\widehat i})
\int f(X_{\widehat i}\oplus_i Z)\,d\nu(Z).
\tag{6}
$$

Replace $m_H$ by $m_L$ for $T_{\rm inner}$. For $T_{\rm arith}$, insert $\mathbf1_O$ both outside and inside the integral. Formula (6) defines the operator on the full Hilbert space, not only on polynomial profiles.

The cap quotient is $\langle f,T_{\rm cap}f\rangle/\|f\|^2$. The actual sieve quotient for $P_Of\ne0$ is

$$
\frac{\rho_*\langle P_Of,BP_Of\rangle}{\|P_Of\|^2}.
\tag{7}
$$

The denominator in (7) is essential. On all of $\mathcal H$, the denominator of the Rayleigh quotient of $T_{\rm arith}$ is $\|f\|^2$, which agrees with (7) only when $f=P_Of$. For the actual sieve problem one works on $L^2(O,\nu^k)$ or keeps this distinction explicit.

The arithmetic theorem requires more than a cap quotient exceeding one: the actual supported profile and source/realization hypotheses must hold. The restoration estimate is a lower bound on its quadratic form, not another fixed linear operator formed by subtracting independent error bars.

### 4. Boundedness and self-adjointness without positivity

All multipliers in (4) are real and bounded. Fubini and (3) imply self-adjointness of each term $E_i^*mE_i$. To give a bound independent of the much larger unrestricted mass, suppose $H_O$ has total support at most $S$. Put $t_j=|X_j|$, $\widehat s_i=\sum_{j\ne i}t_j$, and

$$
w_i=S-\widehat s_i+(k-1)t_i.
$$

Because the total density is at most one,

$$
\int_{H_O(Y)}\frac{d\nu(X_i)}{w_i}
\le\int_0^{S-\widehat s_i}
\frac{dt}{S-\widehat s_i+(k-1)t}
=\frac{\log k}{k-1}.
$$

The boundary $\widehat s_i=S$ has zero fiber measure. Weighted Cauchy–Schwarz followed by $\sum_iw_i=kS$ gives

$$
\sum_i\|E_if\|^2\le C_{\rm op}\|f\|^2,
\qquad C_{\rm op}=\frac{Sk\log k}{k-1}.
\tag{8}
$$

For the fixed $k=39$ geometry, the safe bound $C_{\rm op}\le4$ has an exact rational verification in the Round 5 source-geometry audit. Since $b_h\le m_H,m_L\le1$,

$$
-\rho_*|b_h|C_{\rm op}I
\le T_{\rm cap},T_{\rm inner},T_{\rm arith}
\le\rho_*C_{\rm op}I.
\tag{9}
$$

For the compressed operator $T_{\rm arith}$ these inequalities use that $P_O$ is an orthogonal projection. Also

$$
A-B=\sum_iE_i^*\{d_0(\mathbf1_{H_0}-\mathbf1_{L_0})
+a_h(\mathbf1_{H_1}-\mathbf1_{L_1})\}E_i\ge0.
$$

The negative full-face term cancels in this difference. None of these statements makes $A$ or $B$ positive semidefinite. In particular, a Perron–Frobenius argument, a positive-kernel power method, or a replacement of $b_h$ by $|b_h|$ would require a different justification and would change the problem.

If the trial and the domains are permutation invariant, these operators commute with coordinate permutations. Thus the symmetric subspace is invariant. The factor $k$ in the symmetric face formulas below comes from this symmetry, not from the erasure adjoint.

### 5. Exact mixed integrals and the information retained by fragments

For arbitrary profiles $f,g$, the true mixed form is

$$
\langle g,T_{\rm cap}f\rangle
=\rho_*\sum_i\int m_H(Y)\overline{E_ig(Y)}E_if(Y)\,d\nu^{k-1}(Y).
\tag{10}
$$

Expanding the two marginals introduces two independent erased coordinates conditional on the same retained configuration $Y$. It does not introduce two independent retained configurations. This is exactly the shared-root convention in the primary proof.

For symmetric $f$, direct calculation of $\|T_{\rm cap}f\|^2$ can reduce the double coordinate sum to $i=j$ and $i\ne j$. The first contribution has one shared retained tuple and two erased copies, together with the outer-fiber mass. The second has $k-2$ shared coordinates and four distinguished coordinate copies. They are different overlap integrals. A third operator moment has the finitely many equality patterns of three erasure indices, including the different placements of two equal indices. This is a useful organizational reduction, but no independence assumption between their shared cap states is valid.

The cap-only masks use each total cell and the largest fragment. Let all distinct positive caps be

$$
0<c_1<\cdots<c_L=\zeta,
$$

where a larger unused ambient cap can also be included. Partition a coordinate by its total cell $C_j=[jh,(j+1)h)$ and its fragment layer $c_{\ell-1}<\max X\le c_\ell$, with the layer-zero cumulative measure defined to be zero. The exact mass of this atom is

$$
\mu_{j\ell}=\int_{C_j}
\{\rho_D(t/c_\ell)-\rho_D(t/c_{\ell-1})\}\,dt.
\tag{11}
$$

For $\ell=1$ omit the second term. Empty or zero-mass atoms may be removed. Formula (11) is an exact pushforward of the fragment measure. It is not an approximation that concentrates continuous totals or fragments at a point.

For the companion's inward cell domains, outer membership is a function of the index sum $r=\sum j_i$ and the largest layer. Face membership is a function of $\widehat r_i$ and the largest retained layer. Therefore the finite subspace of functions constant on products of these atoms is invariant under $T_{\rm cap}$: integrating coordinate $i$ sums its atom values against $\mu_{j\ell}$, and all remaining arguments in (6) depend only on retained atom labels. The adjoint then produces an atom-constant output. Since $T_{\rm cap}$ is self-adjoint, this finite subspace is also reducing.

The official step trial lies in this subspace. Consequently its full $T_{\rm cap}f$ and its residual outside the 77-dimensional span lie there too. There is no uncomputed within-cell component of $T_{\rm cap}f$ for that trial and those fixed cell domains. The full Hilbert space still contains other, within-atom functions; no claim about its entire spectrum follows from this invariance alone.

The coordinate layers cannot in general be discarded. Knowing all total cells does not determine which outer-shell marginals survive after erasure. The action on coordinate $i$ depends on the largest retained fragment layer, and different erasures can leave different largest layers. Replacing this information by one global probability before taking products changes (10).

The actual predicates in $O,L_0,L_1$ involve activated fragments and inclusive prefix sums, such as $\max_{p>\xi}\{\sum_{q\ge p}q+\varphi(p)\}$. Equal total and equal largest fragment do not determine these values. Thus the preceding atom subspace generally is not invariant under $T_{\rm arith}$. More fragment information, exact conditional predicate averages, or a valid support-error argument is required there.

For clarity, product conjugation does not remove this issue. Write $G(X)=\prod_i g(t_i)>0$ and transfer $f=Gu$ to the mass $G^2d\nu^k$. The conjugated action is

$$
G^{-1}T_{\rm cap}G\,u(X)
=\rho_*\sum_i\frac{m_H(X_{\widehat i})}{g(t_i)}
\int\mathbf1_{H_O}(X_{\widehat i}\oplus_i Z)
g(|Z|)u(X_{\widehat i}\oplus_i Z)\,d\nu(Z).
\tag{12}
$$

There is one erased factor $g$, and a factor $1/g(t_i)$ outside. It is not a normalized average against $g^2d\nu$.

### 6. Full residual, nonnested radial compression, and the signed two-dimensional test

Let $U\subset\mathcal H$ be the span of the 77 step profiles and let $P_U$ be orthogonal projection in the true mass inner product. If $\phi_1,\ldots,\phi_{77}$ are an independent basis, put

$$
M_{ab}=\langle\phi_a,\phi_b\rangle,
\quad b_a=\langle\phi_a,Tf\rangle,
\quad P_UTf=\sum_a\phi_a(M^{-1}b)_a.
\tag{13}
$$

An exact nonsingular Gram matrix is needed; dependent basis vectors can instead be removed. Euclidean coefficient projection is not (13).

For any $f\in U$, define $r=(I-P_U)Tf$. Self-adjointness and orthogonality give

$$
\langle f,Tr\rangle=\langle Tf,r\rangle=\|r\|^2.
\tag{14}
$$

This does not require $f$ to be an exact Ritz eigenvector. An exact Ritz equation is required only to replace $P_UTf$ by a scalar multiple of $f$.

To avoid computing all of $r$, choose a closed subspace $V$ whose projection can be evaluated, and put

$$
v=P_Vr,\qquad w=(I-P_U)v.
\tag{15}
$$

Here $v$ is called `h` in the numerical implementation; the letter $h$ elsewhere in this note denotes the grid spacing. The spaces $U,V$ need not be nested. The projection order in (15) is essential. Since $r\perp U$,

$$
\langle f,Tw\rangle=\langle r,w\rangle
=\langle r,v\rangle=\|v\|^2,
\qquad
\|w\|^2=\|v\|^2-\|P_Uv\|^2.
\tag{16}
$$

In particular $\|w\|\le\|v\|\le\|r\|$, and $v\ne0$ forces $w\ne0$. The coupling is $\|v\|^2$, not generally $\|w\|^2$. The superficially similar direction $(I-P_U)P_VTf$ does not generally satisfy (16).

Set $F_2=\|f\|^2$, $q=\|v\|^2$, $z=\|w\|^2>0$,

$$
\lambda=\frac{\langle f,Tf\rangle}{F_2},\quad
\tau=\frac{\langle w,Tw\rangle}{z},\quad
\eta=\frac{q}{\sqrt{F_2z}}.
$$

The orthonormal basis $f/\sqrt{F_2},w/\sqrt z$ has the matrix

$$
\begin{pmatrix}\lambda&\eta\\\eta&\tau\end{pmatrix}.
$$

Its larger eigenvalue is

$$
\lambda_+=\frac{\lambda+\tau+
\sqrt{(\lambda-\tau)^2+4\eta^2}}2>\lambda.
\tag{17}
$$

No positivity of $T$ is used. For $\lambda<1$ and $\tau<1$, crossing one is equivalent to $\eta^2>(1-\lambda)(1-\tau)$. A certified lower bound $\tau\ge\tau_L$ gives a sufficient condition by substituting $\tau_L$. In the cap problem, (9) supplies the inexpensive choice $\tau_L=-\rho_*|b_h|C_{\rm op}$. Since $z\le q$, the still more conservative sufficient condition

$$
\frac{q}{F_2}>(1-\lambda)(1+\rho_*|b_h|C_{\rm op})
\tag{18}
$$

avoids calculating $\langle w,Tw\rangle$. It may be too weak numerically, but it is a valid signed-operator certificate. A strict positive improvement in (17) alone is not the threshold condition (18) or an arithmetic theorem.

### 7. An exact radial projection computed by one-dimensional convolutions

In this section $G$, every $P_\eta$, and every $g_j$ use the rational midpoint evaluations of the step trial; they are constant on their total cells. Take $V$ to consist of $\mathbf1_{H_O}G(X)a(r)$ with arbitrary values $a(r)$ on the retained radial cells. A fixed subset of radial cells may be used. Since the grid is finite, this is a closed subspace. It does not contain all 77 power-sum profiles.

Use the companion's un-tilted notation

$$
d_c(j)=h^{-1}\int_{C_j}\rho_D(t/c)dt,\quad
Z=\sum_{j<n}g_j^2,\quad
K_c(j)=g_j^2d_c(j)/Z.
$$

Let $M_{d,\sigma}^c(s)$ be the coefficient sequence obtained by integrating $G^2P_\sigma$ over $d$ coordinates with index sum $s$, common cap $c$, and normalization $(hZ)^{-d}$. This is exactly the positive-partition convolution moment of the numerical companion. Define

$$
\Delta M_{d,\sigma}^{\ell}(s)
=M_{d,\sigma}^{c_\ell}(s)-M_{d,\sigma}^{c_{\ell-1}}(s).
$$

For the lowest layer the second sequence is zero. Let $c_O(r)$ be the inward outer cap on radial cell $r$, with all formulas zero outside the outer radial masks. The mass density of the radial subspace, in the common normalization $(hZ)^{-k}$, is

$$
D(r)=M_{k,\varnothing}^{c_O(r)}(r),
\qquad \|Ga\|^2=\sum_rD(r)|a(r)|^2.
\tag{19}
$$

For the input polynomial profile $f$, let $a_{\ell,\eta}(s)$ denote the signed prefix sum of the allowed outer-shell affine rows of the companion. Thus on a background of index sum $s$ whose largest fragment lies in layer $\ell$,

$$
E_if(Y)=hG(Y)\sum_\eta a_{\ell,\eta}(s)P_\eta(Y).
\tag{20}
$$

One must sum the permitted shell rows with their signs before forming any products. Put

$$
B_\ell(s)=\sum_\eta a_{\ell,\eta}(s)
\Delta M_{k-1,\eta}^{\ell}(s),
$$

and let $m_\ell(s)$ be the signed face multiplier (4) on this layer. Direct substitution of (20) into the mixed integral (10) gives the normalized radial adjoint density

$$
N_T(r)=\frac{\rho_*kh}{Z}
\sum_{\ell:c_\ell\le c_O(r)}
\sum_{j+s=r}
g_jd_{c_O(r)}(j)\,m_\ell(s)B_\ell(s).
\tag{21}
$$

More explicitly, $\langle Ga,Tf\rangle=\sum_r\overline{a(r)}N_T(r)$. To verify the factor, each erased marginal contributes $h$, the retained $k-1$ coordinates contribute $(hZ)^{k-1}$, all forms are divided by $(hZ)^k$, and symmetry supplies $k$. Their product is $kh/Z$. The test function's erased coordinate contributes exactly one factor $g_jd_c(j)$.

It follows that

$$
P_VTf=G\,\frac{N_T(r)}{D(r)}
\tag{22}
$$

where $D(r)>0$; on zero-mass cells the value is immaterial. No distribution of fragments has been replaced by a conditional mean before the product. The layer sums in (21) perform the required conditional integration explicitly.

If $N_U(r)$ is the radial mixed density of the profile $P_UTf$, then

$$
v=P_V(I-P_U)Tf
=G\,\frac{N_T(r)-N_U(r)}{D(r)},
$$
$$
q=\|v\|^2=\sum_r\frac{|N_T(r)-N_U(r)|^2}{D(r)}.
\tag{23}
$$

The sequence $N_U$ is obtained from the ordinary $k$-coordinate moments for the coefficients in (13). Both the projection and (23) therefore use the full mass measure. Restricting to any predetermined set of positive-mass radial cells preserves all the identities in (15)–(16); it only chooses a smaller $V$.

The independent mixed forms $\langle\phi_a,Tv\rangle$ and $\langle v,Tv\rangle$ follow from the same signed face formula by replacing the radial polynomial of one or both inputs by the arbitrary sequence in (23). This gives a direct two-dimensional or 78-dimensional Rayleigh calculation without evaluating $\|Tf\|^2$ and without assuming that the radial projection captures the entire residual.

#### Numerical exponential tilt is only a normalization device

The exploratory engine uses $Z_\theta=\sum_jg_j^2e^{-\theta t_j^\circ}$ and moments built from $g_j^2e^{-\theta t_j^\circ}d_c(j)/Z_\theta$. In (19) multiply the resulting moment by $e^{\theta(r+k/2)h}$. In (21), use $Z_\theta$ and multiply $B_\ell(s)$ by $e^{\theta(s+(k-1)/2)h}$. The affine rows in (20) continue to use the un-tilted erased factor $g_jd_c(j)$. These substitutions exactly undo the tilt in the actual product measure.

When combining forms evaluated at two tilts, first convert every norm and pairing to the same common normalization. Converting from the current $Z_\theta$ normalization to a reference $Z_{\theta_0}$ multiplies all forms by $(Z_\theta/Z_{\theta_0})^k$. The true operator, projections, and Rayleigh quotient do not depend on the numerical tilt.

### 8. Independent review, current limits, and the next proof obligation

The Round 6 script `residual-trial/radial_residual.py` was reviewed against (19)–(23). Its `radial_adjoint` has the correct face dimension $k-1$, the factor $\rho_*kh/Z$, one erased $g$, the signed sum of permitted outer-shell affine rows, cap-layer differences, and the background exponential correction. Its computation of $P_UTf$ uses the mass Gram solve, rather than assuming an exactly solved Ritz equation. Its active radial-cell cutoff is a legitimate choice of a smaller $V$ in ordinary mathematics. Floating-point negative mass or Gram uncertainty is not thereby certified away.

The separate exact rational regression `operator-diagnostic/finite_marked_operator_check.py` was also inspected. It uses nonuniform masses, a nonrectangular cap domain, and nonnested trial/radial spaces. The source verifies mass self-adjointness, (14), (16), product conjugation, a projection-order counterexample, and a negative quadratic witness equal to $-1/38880$. This is a structural test of the identities; its five-atom measure is not the Dickman measure and gives no $k=39$ numerical bound.

The earliest computational issue for a rigorous cap improvement is now precise: enclose the Dickman cell masses, Gram projection, radial adjoint density, and signed mixed forms coherently, or rationalize a chosen new radial profile and outwardly certify its ordinary mass and cap forms. A floating-point projected residual may be a useful way to select a profile, but its exact orthogonality is not needed after a concrete rational profile is fixed and its two-dimensional Gram and numerator forms are certified directly. This avoids pretending that numerically computed projections are exact.

The next arithmetic issue is separate and harder. A new radial profile changes the weights of the retained and deleted fragment configurations. The old outer failure covers, old inner loss numbers, and the Round 4 positive alpha credit cannot simply be reused with their old numerical values. One must evaluate their valid formulas for the new profile, or evaluate the actual predicates directly with sufficient retained fragment state. The cap operator is an exact relaxed operator at the fixed grid; it is not the actual supported sieve operator.

This closes the ordinary operator derivation. It justifies a concrete out-of-77-space search direction and a signed two-dimensional test. It does not establish a threshold crossing, a complete support-restored $k=39$ trial, or a prime gap below 186.


<a id="report-03"></a>

# Current report 03: Residual directions outside the 77-dimensional sieve trial space

**Collection:** R6 — full signed prime-sieve operator and residual direction.

**Source:** [research/prime-gaps/round6/residual-audit/SIEVE_RESIDUAL_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/residual-audit/SIEVE_RESIDUAL_AUDIT.md).

**SHA-256:** `be0a8c6ea16af80f27b7c9abc77466884bfee6c02c8750a2f4d72d5381beacc7`. **Git blob:** `a6e8e8bd3ce5ab8987a86f297c7d3817e483eb85`. **Original bytes:** 19067.

## Residual directions outside the 77-dimensional sieve trial space

**Status:** independent algebraic and measure-theoretic audit. The operators below are the finite-dimensional-sieve variational operators from the prime-gap programme, not any earlier zeta-zero operator. No positive-semidefinite assumption is made. No new prime-gap result is established.

Primary inputs checked: [*Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), §4.4, equations (4.30)–(4.40), and §4.1–§4.2; the retained local text is ../../sources/openai-short-gaps.txt, SHA256 ded13a7c74fcfce64e85769e05b5869803dccdf53b88be2c2f3c0b344f95ee84. Current cap-engine files checked were cap_trial.py and optimize_cap.py in the published round-5 geometry-trial directory. In particular, their denominator uses the product g² measure, their erased-coordinate kernels contain one factor g, and their signed face multiplier retains the negative b_h term. They are exploratory cap-form engines, not evaluations of the fully restored arithmetic form.

### 1. The two operators that must remain distinct

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

### 2. Mass conjugation and the radial projection

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

### 3. The direct outside-space residual needs no Ritz hypothesis

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

### 4. Nonnested radial compression: the correct coupling

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

### 5. Approximate action, radial compression and projection errors

#### 5.1 Direct action with a rigorous error

Suppose g approximates Tf with ||g−Tf||≤epsilon. Define a=||Qg|| and v=Qg/a. Then

\[
\left|\langle f,Tv\rangle\right|\ge(a-\epsilon)_+.
\tag{19}
\]

This follows from 〈Tf,Qg〉=||Qg||²+〈Tf−g,Qg〉. It requires an error in the true Hilbert mass, not a Euclidean array error without mass weights.

#### 5.2 Approximate radial projection

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

#### 5.3 A genuinely compressed Galerkin space

If a larger space W contains U and its projection is P_W, then

\[
(P_W-P)Tf=P_W(QTf),
\qquad
\|QTf\|^2=\|(P_W-P)Tf\|^2+\|(I-P_W)Tf\|^2.
\tag{22}
\]

A rigorously evaluated nonzero compressed residual is a valid lower witness even without a bound on the omitted tail. A small compressed residual gives no upper bound on the full residual. The nonnested radial space V is not itself such a W; confusing (22) with (14) produces the incorrect coupling ||w||.

#### 5.4 Approximate projectors

If ||P_hat−P||≤delta and ||g−Tf||≤epsilon, then

\[
\|(I-P_{\rm hat})g-QTf\|
\le\epsilon+\delta\|g\|.
\tag{23}
\]

But (I−P_hat)g may not lie in U-perp. Reorthogonalize in the true mass, or account for its leakage, before using an orthonormal two-by-two formula. There is no automatic permission to replace the true Gram projection by Euclidean coefficient subtraction.

### 6. Inverse-Gram errors and an easier final certificate

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

### 7. Function class, fragment labels and arithmetic admissibility

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

### 8. Deliverable and stopping rule

The useful next numerical output is a concrete bounded radial profile, its outside-U mass, its signed mixed forms, and a direct reevaluation of the optimized enlarged-span vector. Label floating-point values exploratory. If a convincing cap gain survives independent contractions, fix the profile and certify the necessary entries or a single explicit quadratic combination with outward arithmetic. Only after that should support restoration be attempted for that new function.

This audit does not recommend another coefficient-only optimization of the same 77-dimensional span, a zeta operator experiment, a PSD replacement of the signed sieve form, or a conclusion based on a tiny compressed residual. The intended new mathematical information is a rigorously measured component of the actual cap-operator action outside the existing span.

### 9. Exact small-model checks

The accompanying exact_residual_checks.py uses only Python's Fraction arithmetic and writes exact_residual_checks.json. All checks passed:

- 80 rational five-dimensional examples with a nonuniform mass, a self-adjoint operator having an explicit negative Rayleigh direction, and a radial-analogue subspace not containing U.
- Direct residual, nonnested radial coupling, approximate-Ritz correction, approximate radial-action identity, and the exact inverse-Gram correction (25).
- Three adjoint checks on a 23-point product-measure support, with an explicit nonzero discrepancy when an incorrect conditional-fibre normalization is substituted.
- The conjugated single-g integral in (6), and all five discrete radial projection conditions in (8).

One exact-Ritz example has ||h||²=7544/406125, ||Qh||²=9572/676875 and 〈Tf,Qh〉=7544/406125. Thus the two competing unnormalized coupling formulas are distinguishable in exact arithmetic. The same example has a negative Rayleigh witness −1/9. These checks are structural tests of the audit formulas, not estimates of the k=39 operator or evidence of an improved cap quotient.


<a id="report-04"></a>

# Current report 04: Independent finite marked-space regression for the signed sieve operator

**Collection:** R6 — full signed prime-sieve operator and residual direction.

**Source:** [research/prime-gaps/round6/operator-diagnostic/FINITE_MARKED_OPERATOR_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/operator-diagnostic/FINITE_MARKED_OPERATOR_AUDIT.md).

**SHA-256:** `486d31e88130a394b42987e8af29f15c4ad902318e65343b92f2f95fce1348c2`. **Git blob:** `652292d836aa12e6ac71f3e5c5c817f56505b290`. **Original bytes:** 4828.

## Independent finite marked-space regression for the signed sieve operator

This is a structural test of the operator and projection formulas used in Round 6. It is not a calculation of the k=39 prime-sieve quotient, and none of its numerical values is transferable to that quotient. All identities below are checked with exact rational arithmetic in `finite_marked_operator_check.py`; floating eigenvalue displays are explicitly separated in its JSON.

### 1. Why this model is useful

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

### 2. Nonnested compression and the correct order

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

### 3. Product conjugation

For amplitudes \(f=Gp\), let D be multiplication by G. The conjugated operator is \(D^{-1}TD\), and its mass matrix is \(DWD\). The script verifies its self-adjointness under that mass and its equivalence to the original action.

The outer coordinate contributes a reciprocal factor \(1/g(t_i)\), while the erased integral contains one factor g(u). Replacing this with an average under normalized \(g(u)^2\mu(u)\) would define a different operator. The actual numerical implementation must carry the analogous cell factors and normalizers separately.

### 4. Reproduction and scope

Run `OPENBLAS_NUM_THREADS=1 python3 finite_marked_operator_check.py`. Dependencies are NumPy and SymPy. It writes a JSON receipt and prints the exact rational values. There is no random seed because the model and trial are deterministic. No source file or earlier certificate is changed.

This independent finite check validates algebraic invariants and rejects tempting incorrect formulas. The actual k=39 function-space derivation, fragment-cell integration and numerical conditioning require their own proofs and tests. In particular, passing this toy model is not an outward error enclosure for any sieve integral.


<a id="report-05"></a>

# Current report 05: Round 6: one full cap-operator residual beyond the 77-dimensional family

**Collection:** R6 — full signed prime-sieve operator and residual direction.

**Source:** [research/prime-gaps/round6/residual-trial/REPORT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/residual-trial/REPORT.md).

**SHA-256:** `11a346f72bc5540864367d52740a9d77b1a7866cf5074e562509b94f921d4b35`. **Git blob:** `7adf315b11ee02136a4838a68ca3a400c98dd6fc`. **Original bytes:** 15322.

## Round 6: one full cap-operator residual beyond the 77-dimensional family

**Outcome.** An explicit direction generated by the fixed-geometry k39 signed cap operator increases the fine-grid quotient from `0.99439639919` to `0.99446782094`, about **71.42 ppm**. This direction is not another polynomial degree or an eigenvector of the old 77-by-77 matrix. About 98.78% of its radial residual mass survives true mass projection away from the whole 77-dimensional space. The new value is still below one by about **5,532 ppm**. No smaller prime gap, DHL(39,2), full support-restored certificate, or global variational bound is proved.

The bounded experiment consists of one coarse construction, one fine construction, and two numerical consistency checks. There is no iterative Krylov expansion or parameter scan in this report. The independent ordinary derivation below is exact for the stated finite cap model; all reported numerical values remain floating-point diagnostics without outward error enclosures.

### 1. The operator and its measure

The geometry, k=39, product profile g, exceptional constant K=.34, hybrid parameters, and 98,304-cell fine grid are those of the original Round 4 experiment. The official source pin is `61340d0b74163003b32756bb16e91d9209a5e330`; the coefficient-source SHA256 is `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`.

Each coordinate consists of its total t and a fragment mark. For a fragment cap c, write d_c(j) for the cell-average Dickman survival probability at total cell j. An exact finite marked model assigns mass

    nu_h(j,ell) = h [d_{c_ell}(j)-d_{c_(ell-1)}(j)]

to the mark layer ell. This definition retains fragment-cap information rather than pretending that a coordinate total exceeding c is forbidden. The implemented d_c values use eight-point cell quadrature and floating Dickman evaluations; exact d_c would define the corresponding exact finite model.

Let H_O be the fixed outer cap support, E_i the erased-coordinate integral against nu_h, and

    m = 1_H0 + (a+b) 1_(H1\H0) + b 1_(Hfull\H1),
    a = .99998^2 - .99998*.008,
    b = (1-.99998/.008)*(1-.99998)*.34.

On the real Hilbert space L2(H_O,nu_h^k), the cap operator is

    T = rho_star * 1_HO * sum_i E_i^* m E_i * 1_HO.

The adjoint E_i^* is an unweighted lift followed by outer restriction. There is no conditional fibre normalization. The signed coefficient b is negative, so T must not be assumed positive semidefinite. This is the **cap operator**, not the operator with all true source predicates and support-restoration losses inserted.

Write G(t)=product_i g(t_i). Amplitudes f=G p have mass measure G^2 nu_h^k. In this representation the action contains `1/g(t_i)` outside the erased integral and a *single* g inside that integral. Replacing this with a g-squared conditional average would give the wrong adjoint and a different operator.

### 2. A compressed direction from the full operator

Let U be the original 77-dimensional amplitude space and f in U the stored optimized vector. Let P_U be the orthogonal projection for the actual mass form, not Euclidean coefficient projection. Let V consist of all amplitudes G h(s), with arbitrary radial cell profile h(s), supported on a fixed selected set of radial cells. V is substantially larger than the degree-six radial polynomial subspace.

Define

    r = (I-P_U) T f,
    h = P_V r,
    w = (I-P_U) h.

The order of these projections matters: P_V U need not be contained in U. In code `P_U Tf` is computed as `Gmat^-1 Bmat c`; it is not replaced by a scalar multiple of f. This avoids relying on exact Ritz accuracy.

Self-adjointness and orthogonality give the ordinary identity

    <f,Tw> = <Tf,w> = <r,h> = ||h||^2.

Moreover `||w||^2=||h||^2-||P_Uh||^2`. Consequently nonzero h necessarily gives a genuine outside-U direction w and positive coupling, regardless of the sign of T. For unit f and v=w/||w||, the off-diagonal entry is

    beta = ||h||^2 / ||w||,

which is generally **not** ||w||. This is a projected residual construction using a nonnested radial subspace; its identities are standard Hilbert-space facts, not a claimed new theorem about prime gaps.

The main computational point is that P_V can be obtained by one-dimensional adjoint convolutions while still integrating the full cap marks. It therefore exposes an outside-77 component without constructing a 39-dimensional tensor grid or pretending that another eigenvector of the same 77-by-77 matrix is new information.

### 3. Exact finite-array formula for the radial adjoint

The numerical tilt tau is only a change of normalization. Set

    Z_tau = sum_j g_j^2 exp(-tau*t_j),
    p_c(j) = g_j^2 exp(-tau*t_j) d_c(j) / Z_tau.

Let M^c_(d,eta)(s) denote the same polynomial background moments used by the original cap engine. The product-power identities are expanded by set partitions, and moments are computed by one-dimensional convolutions. Background cap layer ell uses the difference between moments at consecutive caps.

For the input polynomial f, the erased-coordinate amplitude on layer ell is

    E_i f(Y) = h_mesh * product_(j!=i) g(t_j)
               * sum_eta A_(ell,eta)(s) P_eta(Y).

The existing affine arrays A include all allowed outer radial shells **before** the background contraction. Define

    B_ell(s) = sum_eta A_(ell,eta)(s)
               [M^(c_ell)_(k-1,eta)(s)-M^(c_(ell-1))_(k-1,eta)(s)].

For an output total r whose outer fragment cap is c_O(r), the radial numerator density is

    b_f(r) = rho_star * k*h_mesh/Z_tau
      * sum_(ell:c_ell<=c_O(r)) sum_(j+s=r)
          g_j d_(c_O(r))(j) m_ell(s) B_ell(s)
          exp(tau*(s+(k-1)/2)*h_mesh).

The radial mass density is

    q(r) = exp(tau*(r+k/2)*h_mesh) M^(c_O(r))_(k,empty)(r).

Let D_i(r) be the corresponding mass cross-density with basis amplitude u_i, so that `<G h,u_i>=sum_r h(r)D_i(r)`. If p is the coefficient vector of P_U Tf, the desired radial residual profile is

    h(r) = [b_f(r)-sum_i p_i D_i(r)] / q(r)

on the selected radial cells, and zero elsewhere. The same notation h for a profile and G h for its amplitude is used only in these array formulas.

The implementation selects cells where `q(r)>10^-9*max(q)`. This defines V explicitly; it does not assume that the residual on excluded cells is zero. The saved active index set is frozen and defines the exact subspace V_active. Restricting V in this way preserves the projection identity in exact arithmetic and avoids division by unreliable tiny numerical masses. Small excluded q-mass is **not a bound on omitted residual energy**; no such bound is used here. The fine run excludes approximately 1.325e-10 of the positive radial mass. The negative radial mass generated by FFT rounding is only about 3.6e-25 of total positive mass and is outside the selected region. These are observed diagnostics, not certified rounding bounds.

The formula was independently checked against the source normalization by the prime186 agent: k, h_mesh/Z, the erased single-g factor, layer differences, and placement of the exponential agree. Root's independent marked-state toy and ordinary operator proof are separate artifacts; they should accompany this report when the larger package is assembled.

### 4. The mixed forms and the actual new space

The new direction is not assessed solely through an action-norm estimate. The program independently evaluates all 77 mixed mass entries `<u_i,h>`, all 77 signed numerator entries `<u_i,Th>`, and `<h,h>`, `<h,Th>`. A separate sampled-profile evaluator then directly evaluates the final polynomial-plus-radial amplitude.

Writing g_i=<u_i,h>, Gmat for the old mass Gram, and p=Gmat^-1 g, the true outside-space norm is

    gamma = <h,h> - g^T Gmat^-1 g.

The numerator entries for w=h-U p are formed by the same subtraction in the numerator form. The implementation whitens the original 77-dimensional mass Gram, appends w/sqrt(gamma), and solves the resulting 78-dimensional symmetric pencil. The raw matrices, radial profile, projection coefficients and new vector are retained, so this is a reviewable explicit finite-dimensional extension.

### 5. Main numerical evidence

At the original fine grid, with tau=20 and radial mass cutoff 10^-9:

| quantity | observed value |
|---|---:|
| original 77-space quotient | .9943963991909279 |
| compressed radial norm squared ||h||^2 | 6.670688589594228e-5 |
| outside-77 norm squared ||w||^2 | 6.589186717477095e-5 |
| surviving norm-squared fraction | .9877820901062194 |
| directly evaluated <f,Tw> | 6.670688584662753e-5 |
| relative coupling-identity error | -7.39e-10 |
| mixed-adjoint absolute discrepancy | -4.83e-14 |
| full 78-space matrix quotient | .9944678209367751 |
| final direct profile quotient | .9944678209006830 |
| matrix/direct difference | 3.61e-11 |

The original matrix quotient differs slightly from the old directly evaluated value `.9943963993644909`; that previously recorded discrepancy is numerical and is not counted as new improvement. The full 78-space improvement relative to its matrix baseline is about **71.4217 ppm**.

The actual two-dimensional span of f and normalized w has matrix

    [ .9943963991909279    .008217784708256407 ]
    [ .008217784708256407 .043583189070450945 ].

Its largest eigenvalue is `.9944674193880856`, giving **71.0202 ppm** improvement. Reoptimizing all 78 coefficients adds approximately **0.40155 ppm** beyond that simple two-direction step. Thus the observed gain genuinely comes from the new direction rather than merely from re-solving the old polynomial coefficients.

The computed mass norm of `P_U Tf-lambda f` is approximately 1.64e-10. This approximate Ritz defect is recorded for context; it is not used to justify the projection identity, because the full mass projection is used directly.

For this particular two-dimensional plane, crossing one requires

    beta^2 > (1-a)(1-b),

since both diagonal entries are below one. The observed coupling squared is only about 1.26% of that plane's crossing threshold. This explains why the positive new direction does not come close to proving the desired k39 criterion. It says nothing about the uncomputed full residual outside the chosen radial compression.

### 6. Bounded consistency checks

| grid | cutoff | tilt | full 78 matrix quotient | direct quotient |
|---:|---:|---:|---:|---:|
| 16,384 | 1e-9 | 20 | .9934506692779733 | .9934506693945010 |
| 98,304 | 1e-9 | 20 | .9944678209367751 | .9944678209006830 |
| 98,304 | 1e-9 | 25 | .9944678209367753 | .9944678210538511 |
| 98,304 | 1e-8 | 20 | .9944678032713334 | .9944678033480433 |

The tilt-20 and tilt-25 matrix results differ by 2.2e-16. Their direct evaluations differ by approximately 1.53e-10, consistent with the contraction sensitivity already present in the ill-conditioned polynomial Gram. Changing the radial cutoff by a factor of ten changes the result by only about .0177 ppm. The coarse and fine new-direction gains are respectively about 71.3164 and 71.4217 ppm.

The old fine scaled-Gram condition is about 2.28e10, so small pencil residuals alone are not rounding certificates. All operations here use actual float64 on this host. The main fine construction took about 10.6 seconds before concurrent consistency checks. No speed comparison or scaling theorem is claimed.

### 7. Reproduction and files

From this directory:

```sh
OPENBLAS_NUM_THREADS=1 python3 radial_residual.py --intervals 16384
OPENBLAS_NUM_THREADS=1 python3 radial_residual.py --intervals 98304
OPENBLAS_NUM_THREADS=1 python3 radial_residual.py --intervals 98304 --tilt 25
OPENBLAS_NUM_THREADS=1 python3 radial_residual.py --intervals 98304 --density-cutoff 1e-8
OPENBLAS_NUM_THREADS=1 python3 audit_outputs.py
OPENBLAS_NUM_THREADS=1 python3 validate_outputs.py
```

`radial_residual.py` contains the radial adjoint, full mixed-form construction, mass projection, 78-space solve and direct sampled-profile evaluation. `cap_trial.py` is the copied fixed-geometry cap engine; the upstream clone is never imported as executable code or modified. `audit_outputs.py` derives and saves the actual two-by-two matrices and Ritz-defect diagnostics from retained arrays without performing new integrations.

Inputs include the pinned literal coefficient source, and the already completed Round 4 files `ritz_k39_n16384.json/.npz` and `ritz_k39_n98304.json/.npz`. Their paths are resolved relative to the common staging BASE. The exported archive must preserve this layout or adjust the explicit paths. `PRIME186_SOURCE` can override the coefficient-source path, and `PRIME186_TRIAL_ROOT` can override the directory containing the four old trial input files. These path overrides were added after the numerical runs and do not change their recorded values.

Each run has JSON diagnostics and NPZ arrays. The NPZ retains q, all D_i, b_f, the new h, P_U Tf, mixed forms, projection coefficients, final polynomial coefficients and the 78-space matrix. JSON includes the final radial multiplier beta and direct evaluation. `projection_audit.json` contains the separate two-dimensional evidence. `validate_outputs.py` checks the mass-projection inequalities, coupling and adjoint identities, two-dimensional gain, normalized candidate mass, direct-form agreement, and tilt consistency at explicit numerical tolerances; `validation.json` records the passing regressions. These regression thresholds are not outward arithmetic enclosures. The full final amplitude is reproducible as the stored polynomial coefficient vector plus beta times the stored arbitrary radial profile, multiplied by the unchanged product g and outer support.

### 8. What remains unproved and what this establishes

The ordinary projection identities and finite-array adjoint derivation explain why this is a legitimate outside-space search. The numerical evidence supports a real positive direction in the cap model. It is not an outward certificate even for the new finite profile, and the new profile has not been supplied with the full source-dependent support repairs. No support-restored operator norm, T-squared moment, or global extremizer has been computed.

A future exact certificate could fix and rationalize the new profile and enclose only its mixed mass and numerator entries. Positivity of the resulting concrete quadratic expression would avoid relying on an unproved action-norm error estimate. Here, however, the quotient remains below one, so that certification would not yield the desired prime-gap result. The next substantive research question is whether a less restrictive compression captures a much larger fraction of the full cap residual. This report does not answer that question and does not continue the iteration automatically.

#### Compact public witness and historical program metadata

The public-sized `*_compact.npz` exports retain every candidate/projection array and omit only the regenerable 77-by-N cache D. `compaction_manifest.json` records the original full hashes, compact hashes, and exact raw-byte identity of every retained array. Full NPZs remain local. See `PROVENANCE.md` for the regeneration instructions and the precise distinction between earlier outputs without embedded program hashes and later metadata additions. No earlier run is retrospectively described as containing a hash it did not record.


<a id="report-06"></a>

# Current report 06: Provenance and compact witness export

**Collection:** R6 — full signed prime-sieve operator and residual direction.

**Source:** [research/prime-gaps/round6/residual-trial/PROVENANCE.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/residual-trial/PROVENANCE.md).

**SHA-256:** `4a3a8f57b27e88053b12030487ed84fd939c3e32541ead1ecef047949ace04ea`. **Git blob:** `4724dc6dd0afca4c68d0f8b2d9ea7d2e917bec8d`. **Original bytes:** 2842.

## Provenance and compact witness export

The four numerical integrations are the coarse run at N=16384, the primary fine run at N=98304, a fine run with density cutoff 1e-8, and a fine run with tilt 25. Each full NPZ and JSON is retained locally. No output numbers were replaced by estimates or by the later independent replay.

The first coarse integration preceded two small program revisions: explicit conversion between the stored matrix's tilt normalization and the current integration normalization, and extra hash fields in JSON. At tilt 20, the conversion is exactly one, so the first coarse calculation is the same mathematical computation. The primary fine run included the normalization conversion but preceded the extra embedded program/engine/input hash fields. The two consistency runs include those hash fields. It would be inaccurate to claim the earlier files contained an embedded program hash; instead, the archive manifest records their actual file hashes and the current program hash separately. The old upstream source SHA and old trial JSON SHA were present in every numerical output.

`audit_outputs.py` subsequently computed the actual 2-by-2 subspace matrices and projection-defect diagnostics from retained arrays without new integration. `projection_audit.json` pins each input JSON. It does not alter the original integration evidence.

For public export, `compact_witness.py` removes only the 77-by-N radial mass cross-density cache named `D` from each compressed NPZ. Every other array, including the actual h, the output polynomial coefficients, projection data, q, b_f, active mask, radial coordinates and 78-by-78 pencil, is copied without changing its dtype, shape or raw bytes. `compaction_manifest.json` records full and compact file SHA256s, sizes, the removed D cache's shape/dtype/raw-byte SHA, and each retained array's raw-byte SHA. The script checks exact byte equality after reopening each compact archive.

D is reproducible by the `radial_mass` function; the full run commands in REPORT.md regenerate the original full model data and all candidate forms. Full NPZs remain in this local staging directory. Public consumers can use the compact witness for the explicit amplitude, projection audit, and two-dimensional forms; workflows that require D must regenerate it or obtain the pinned full archive. Omission of this cache is an explicit size reduction, not loss or substitution of the candidate vector.

`PRIME186_TRIAL_ROOT` was added to the main and post-audit scripts after the numerical runs, solely to select the old-trial input directory in a public package. The post-audit also accepts the compact witness when the full archive is absent. These path/input-selection changes are pinned by the final archive manifest; they do not retroactively change the stored run's program provenance.


<a id="report-07"></a>

# Current report 07: Independent review of the frozen radial profile outside the old span

**Collection:** R6 — full signed prime-sieve operator and residual direction.

**Source:** [research/prime-gaps/round6/operator-diagnostic/OUTSIDE_SPAN_INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/prime-gaps/round6/operator-diagnostic/OUTSIDE_SPAN_INDEPENDENT_REVIEW.md).

**SHA-256:** `a1f8b3fc86c4232f6f0e6f17b930935d927671466b40274c02ace7893432ad0e`. **Git blob:** `dc3bc5fdd61798b278e99668f9d2c1631351ac28`. **Original bytes:** 4931.

## Independent review of the frozen radial profile outside the old span

**Verdict: the outside-span argument is valid.** This note records the independent review already completed by the Yau-flow audit agent. It certifies a new direction in the true cap Hilbert space, not an enclosure of a numerical Rayleigh gain.

### Evidence independently checked

The reviewed witness is ../residual-trial/radial_residual_n98304_cut1e-09_tilt20_compact.npz. Its SHA256 is b283cab182b0b32091f24ac898def31cc263fa6af1a4540b30721e8122b80c77. A read-only hash comparison confirmed that this public checkpoint is byte-identical to the staged witness used in the independent review.

The h.npy member was decoded independently with Python's standard-library ZIP, NPY-header and binary-structure handling, rather than through the certificate's NumPy loading path. The stored array is little-endian binary64. Its entries at indices 0 through 12 are exactly zero, and its first nonzero entry is at index 18422, with exact dyadic value

\[
h_{18422}=-\frac{6264072493613325}{4611686018427387904}\ne0.
\]

This interprets the frozen stored value as an exact rational definition of the new step profile. It does not assert that the floating computation producing that value exactly evaluated an operator residual.

The 11 official coefficient signatures were separately read from the preserved source using its literal syntax tree. Their maximum exponent sum is 6. The old basis combines these signatures with radial powers of degrees 0 through 6. On the product cell with indices

\[
(j_1,j_2,\ldots,j_{39})=(r,0,\ldots,0),
\]

division by the common strictly positive product factor G leaves a polynomial in r of degree at most 12. The midpoint representatives are affine in r, the radial shift is affine in r, and each power-sum signature has degree at most its exponent sum. This degree assertion is for the actual frozen midpoint-step basis.

### Whole-cell support and positive measure

The argument uses whole product cells, not isolated representative points, which would not by themselves establish an L² assertion. The mesh is

\[
\Delta=\frac{2742997}{258046918656}>0.
\]

For the largest selected index, the maximum coordinate-total endpoint and maximum whole-cell total are respectively

\[
18423\Delta=0.1958335096353804\ldots,
\qquad
(18422+39)\Delta=0.19623744348796382\ldots.
\]

These were checked with exact rational arithmetic. The whole-cell total is strictly below the first outer-shell boundary

\[
\frac{653622010000}{689056987511}
=0.9485746779246842\ldots.
\]

Every selected coordinate cell is also strictly below the retained fragment cap. The companion certificate uses the sufficient conservative cap

\[
\frac{41328816845772771}{110249118001760000},
\]

which exceeds 18423 Delta. The independently reconstructed final outer cap was larger still, approximately 0.4951438701; using the smaller common cap is therefore harmless.

All 14 selected product cells consequently lie inside the same first outer shell and satisfy its cap automatically. On these small coordinate-total intervals, the unscaled fragment measure has total-size density one. Each selected product cell has mass Delta^39, which is strictly positive. The common factor G is strictly positive on them.

### Proof of nonmembership

Suppose the frozen cap-supported radial profile G h belongs to the old span U in L². The old profiles and the new profile are constant after the prescribed midpoint evaluation on each selected product cell. Equality almost everywhere therefore forces equality of their values on each such positive-mass cell.

After dividing by G, an old-span representation would give a polynomial p(r) of degree at most 12 satisfying

\[
p(0)=p(1)=\cdots=p(12)=0,
\qquad
p(18422)=h_{18422}\ne0.
\]

Thirteen distinct roots force p to vanish identically, a contradiction. Hence G h is outside U. Equivalently, its orthogonal projection onto U-perp has strictly positive true Hilbert norm. This conclusion is independent of inverse-Gram conditioning and of the accuracy of the computed projection norm.

### Scope of this review

The implementation certify_outside_span.py and its outside_span_certificate.json receipt were read when preparing this record. They additionally contain a modular rank-77 witness for the old basis and an augmented-rank-78 conclusion. This reviewer did not independently rerun that modular rank computation. The 13-zero argument above does not need it; dimension exactly 78 additionally uses independence of the 77 old basis vectors.

No fine integral, optimization, or existing certificate was rerun or modified for this note. The result proves nonmembership for the frozen dyadic step profile. It supplies no quantitative lower bound for the outside-space norm, no outward enclosure of the new quotient or its gain, and no certification of the fully restored arithmetic support. Those remain separate obligations.


<a id="report-08"></a>

# Current report 08: Round 7: two explicit actual-zeta targets for Dyson–Montgomery

**Collection:** R7 — actual-zeta targets, arithmetic mark, and flow obstruction.

**Source:** [research/reports/dyson_round7.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/dyson_round7.md).

**SHA-256:** `30ae0f293454aabdf22dbbc9908f1551c1c5a0488d3e3b9ac0f1105459569b33`. **Git blob:** `63ad174f355fab585a63895eb4d592f5e8af10ad`. **Original bytes:** 8767.

## Round 7: two explicit actual-zeta targets for Dyson–Montgomery

The user's direction is now the main lane: actual Riemann-zeta pair correlations and the Alternative Hypothesis, with random matrices and heat flow used to find precise tests. The prime-gap parameter search is paused. This round has two rigorous reductions to explicit arithmetic inequalities, a new arithmetic resonator with a negative test result, and a forward-flow obstruction. **Neither required new zeta inequality is proved.**

### 1. The most concrete target: two logarithmic-derivative mean squares

For fixed c>0 write

\[
I_T(c)=\int_0^T\left|\frac{\zeta'}{\zeta}
\left(\frac12+\frac c{\log T}+it\right)\right|^2dt,
\quad
W_T=\frac{2[\sinh(2)I_T(1)-\sinh(1)I_T(1/2)]}{T\log^2T}.
\]

The [complete reduction](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/poisson-resolvent/TWO_SCALE_ZETA_TARGET.md) gives, under RH and the precise AH-Pairs formulation in the cited primary paper,

\[
W_T\to W_{\rm AH},\qquad
0.06239<W_{\rm AH}<0.06240.
\]

The sine-kernel prediction is 0.0822714431214773…. Therefore a proof under RH that

\[
\boxed{\liminf_{T\to\infty}W_T\ge1/16}
\]

would already refute AH-Pairs under RH. The easier-to-remember 0.07 target is sufficient but unnecessarily strong as an acceptance threshold. Every lower limit strictly exceeding W_AH would suffice.

The construction fixes a genuine issue with comparing only ACUE to CUE. General AH-Pairs leaves a bounded near-diagonal parameter P_0(T), which need not converge. For a Poisson smoothing width b/(4π), that freedom contributes exactly 2(P_0(T)−1)/sinh(b) to the limiting variance formula. The displayed two-scale combination cancels it. The argument does not assume simple zeros or replace the full AH class by one example.

The proof explicitly controls the noncompact pair-kernel tails, the removed low-zero interval, finite-height endpoints, the Gamma factor, and the holomorphic-square term required to pass from squared real part to squared modulus. The truncations avoid half-lattice boundary atoms. [One independent review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/dyson-frontier/POISSON_TRANSFER_REVIEW.md) checks these conversions; a [second review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/poisson-resolvent/INDEPENDENT_REVIEW.md) also reruns the scalar and finite-model checks. The constant enclosure is exact rational arithmetic. These facts establish the reduction, not the missing lower bound for W_T.

### 2. A compact Fourier target and its exact prime covariance

The [primary-source frontier report](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md) chooses one nonnegative smooth bump φ with integral one, supported on [6/5,7/5] and symmetric about 13/10. For Montgomery's normalized form factor F_T, the two predictions are

| Statistic | RH + AH-Pairs | Montgomery sine-kernel target |
|---|---:|---:|
| Integral φ(α) F_T(α) dα | 7/10 | 1 |
| Centered prime-covariance remainder E_T | −3/5 | −3/10 |

The AH conclusion follows from half-lattice support and the known low band: the limiting pair Fourier distribution is 2-periodic, so its density on (1,2) must be 2−α. The chosen test avoids the integer atoms and all dependence on the unknown near-diagonal mass. Uniform pair-tail bounds justify this statement without assuming a full limiting process exists.

The report then gives an exact prime kernel for E_T. It retains both von Mangoldt sums and the continuous mean from the pole. An independently checked finite expansion demonstrates why omitting that mean changes the problem. A proof that liminf E_T>−3/5 would suffice to refute AH-Pairs under RH; the stronger limit −3/10 would prove this one smoothed Montgomery prediction. Both remain open here.

These are alternative precise targets. Neither comes from reinterpreting the distribution exponent of the 186 prime-gap proof. The missing quantity is a signed two-prime covariance, at the accuracy displayed in the report.

### 3. A genuinely different arithmetic resonator was tried and did not cross

The first proposed S2/S3 polynomial extension had already been tested in the earlier archive. The agent identified that duplication and instead used the sharp arithmetic mark

\[
C_L(n)=1_{\{P^+(n)>\sqrt L\}},\qquad n\le L.
\]

There is an exact unique-large-prime decomposition n=pm with p>√L and m<p. It gives the new marked moments and insertion rules directly from integers. The [derivation](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/arithmetic-resonator/DERIVATION.md) and [independent audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/arithmetic-resonator/INDEPENDENT_REVIEW.md) explain the small-prime truncation, threshold boundary, short background and surviving same-prime term.

A complete 30-dimensional trial was optimized at one fixed ell=27/25. Its limiting half-gap margin is numerically −0.01465492379421, a gain of only about 1.429×10^−8 over its matched 20-dimensional baseline. It remains slightly worse than the older 48-feature best trial, which the report states explicitly. Three split quadrature orders agree, and a frozen rational vector has negative directly evaluated integer-operator margins through L=10^6. These are numerical checks, not interval enclosures or actual zero samples. This particular feature does not justify another coefficient sweep.

The [full report and data](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/arithmetic-resonator/REPORT.md) retain the fixed coefficients, full matrices and failed trial. The failure does not prove that every discontinuous prime-factor feature or the full resonance method is incapable of crossing the threshold.

### 4. Forward heat flow: a useful comparison, with two missing estimates

The [forward-flow report](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/true-zeta-flow/FORWARD_FLOW_OBSTRUCTION.md) proves a contraction estimate for ordered real repulsive systems with a decreasing common external field. Its constant does not deteriorate as an internal gap becomes small. However, a remote-field approximation valid at the central particles need not be valid at the retained block's boundary; a specific boundary-propagation integral remains to be controlled for actual H_t.

Even perfect deterministic localization is insufficient for GUE. The exact family

\[
P_t(z)=z^{2M}-2\cos(\pi/4)e^{-M^2t}z^M+1
\]

starts on the ACUE half-grid up to rotation, has bounded counting discrepancy, and keeps all normalized gaps at least 1/2 throughout forward flow. It approaches the unit clock. This is a counterexample to insufficient dynamical hypotheses, not a model satisfying the full arithmetic explicit formula.

The missing stochastic term is quantitatively visible: for a protected trace frequency m=N/2, its expected microscopic generator contribution at CUE is exactly π². Moreover, the entire protected trace filtration remains matched between ACUE and CUE under full DBM. Thus unchanged low moments cannot justify removing stochastic smoothing. The report states the exact Duhamel and boundary estimates a genuine zeta comparison would need.

### 5. What the recent 0.6725 result contributes

The source audit identifies 0.6725007… as an unconditional lower proportion of zeros that are both simple and on the critical line, with the separate distinct-zero consequence stated in the primary papers. It does not evaluate the out-of-band covariance used here. The checked new proof still uses its stated support-one input. The report records exact source URLs, dates and hashes; it does not infer that a percentage-of-zeros theorem supplies a Montgomery plateau.

### 6. Verification and the next decision

The focused folders preserve source provenance, ordinary proofs, independent reviews, exact scalar certificates, complete numerical witnesses and execution logs. Third-party primary PDFs stay in the local reference archive; their URLs and hashes are public. The independent integration receipt is under `research/logs/round7-integration/`.

The next mathematical step is to prove a nontrivial lower bound for the signed mean square W_T or the centered prime covariance E_T using additional arithmetic structure. The two-scale spectral weight is sinh(2)exp(-2|u|)-sinh(1)exp(-|u|); it changes sign at |u|=log(2 cosh 1). Dropping the unknown high-frequency contribution therefore gives no lower bound. More decisively, the actual stationary ACUE comparison process matches the known low band and satisfies point-process positivity while attaining W_AH<1/16. Those inputs alone cannot prove the desired inequality. A bounded continuation examines exactly where additional arithmetic information enters a centered-psi representation.

Numerical model separation and the present reductions do not estimate either required arithmetic quantity. A complete GUE theorem, a new prime-gap sweep, and proof-assistant formalization of an unclosed argument are postponed. The long research goal remains active.


<a id="report-09"></a>

# Current report 09: Two Poisson scales remove the AH near-diagonal parameter

**Collection:** R7 — actual-zeta targets, arithmetic mark, and flow obstruction.

**Source:** [research/dyson/round7/poisson-resolvent/TWO_SCALE_ZETA_TARGET.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/poisson-resolvent/TWO_SCALE_ZETA_TARGET.md).

**SHA-256:** `b275eedbba276097e3729bd0f75dff4108c11ab7c4f038093b5722e0b3fc7f51`. **Git blob:** `ecca372d887258f7073d9eefa1777b9172660ab0`. **Original bytes:** 14073.

## Two Poisson scales remove the AH near-diagonal parameter

Date: 2026-09-05. Status: written reduction and exact constant certificates; [independent ordinary-proof review completed](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/poisson-resolvent/INDEPENDENT_REVIEW.md). The actual arithmetic inequality stated below is **not proved**. No novelty claim is made for the standard pair-correlation/logarithmic-derivative correspondence.

The useful target is now one explicit inequality for actual zeta mean squares. Put

\[
I_T(c)=\int_0^T\left|\frac{\zeta'}{\zeta}
 \left(\frac12+\frac{c}{\log T}+it\right)\right|^2dt,
\qquad
W_T=\frac{2}{T\log^2T}\left(\sinh(2)I_T(1)-\sinh(1)I_T(1/2)\right).
\tag{1}
\]

Under RH plus the precise AH-Pairs formulation discussed below, the reduction gives

\[
W_T\longrightarrow W_{\rm AH},\qquad
0.06239<W_{\rm AH}<0.06240.
\tag{2}
\]

The sine-kernel prediction is instead

\[
W_{\rm GUE}=0.0822714431214773\ldots.
\tag{3}
\]

Consequently, an actual proof under RH of

\[
\boxed{\liminf_{T\to\infty}W_T\ge\frac7{100}}
\tag{4}
\]

would refute AH-Pairs under RH. This asks for a one-sided inequality for one signed combination, not the full pair-correlation conjecture. It remains a substantial open arithmetic task. The reduction does not make (4) follow from RH or the known Fourier band.

The number 0.07 is a convenient stronger target, not a required threshold. The same exact enclosure already shows \(W_{\rm AH}<0.06240<1/16\). Thus the weaker bound \(\liminf W_T\ge1/16\) also suffices, with a separation exceeding 0.00010. Any proved lower limit strictly exceeding W_AH is acceptable; neither rational lower bound has been established here.

### 1. Definitions and the existing source input

Use Fourier transform \(\widehat f(\alpha)=\int f(x)e^{-2\pi i\alpha x}dx\), and put \(L=\log T/(2\pi)\). Multiplicities are counted throughout. Let

\[
\mu_T=\frac1{TL}\sum_{0<\gamma,\gamma'\le T}
\delta_{L(\gamma-\gamma')}.
\]

The precise AH-Pairs assumption is (AH0) in [Goldston–Lee–Schettler–Suriajaya, *Pair Correlation Conjecture II: The Alternative Hypothesis*, 2507.06823](https://arxiv.org/html/2507.06823v1): all bounded normalized pair differences in the stated high interval approach half integers with the specified decreasing error. We use its RH-dependent equations (1.14)–(1.15), and the cumulative pair bound (1.12). These are distinct from that paper's unconditional results with additional AH-Weak Density assumptions.

For each fixed half integer, the pair masses have the form, up to o(1),

\[
p_{k/2}(T)=
\begin{cases}
p_0(T),&k=0,\\
p_0(T)-1/2,&k\ne0\text{ even},\\
3/2-p_0(T)-2/(\pi^2k^2),&k\text{ odd},
\end{cases}
\tag{5}
\]

with bounded \(1+o(1)\le p_0(T)\le3/2-2/\pi^2+o(1)\). We do not assume p_0(T) converges. The symbol here abbreviates the source's finite-T P_0(T), not an already existing limit.

The base p_0=1 measure is the pair measure of the randomly translated half-lattice sine process. Relative to it, (5) adds

\[
(p_0(T)-1)\sum_{k\in\mathbb Z}(-1)^k\delta_{k/2}.
\tag{6}
\]

Formula (6) includes the diagonal. Dropping it would give the wrong nuisance term.

### 2. Bounded smoothing and exact model formulas

For a>0 define \(P_a(x)=a/[\pi(a^2+x^2)]\). Its Fourier transform is \(e^{-2\pi a|\alpha|}\). If a stationary unit-intensity process has centered structure-factor measure S, its smoothed-density variance is

\[
V(a)=\int e^{-4\pi a|\alpha|}\,dS(\alpha).
\tag{7}
\]

Write b=4πa and abbreviate this variance by V(b). For the sine process, \(dS=\min(|\alpha|,1)d\alpha\), giving

\[
V_{\rm sine}(b)=\frac{2(1-e^{-b})}{b^2}.
\tag{8}
\]

The centered spectral measure for the half-lattice model is

\[
dS_{\rm A}(\alpha)=\operatorname{dist}(\alpha,2\mathbb Z)\,d\alpha
 +\sum_{m\in\mathbb Z\setminus\{0\}}\delta_{2m}.
\tag{9}
\]

Here the distance ranges from zero to one. To derive (9), its pair measure is
\(\delta_0+\frac12\sum_{k\ne0}(1-\operatorname{sinc}^2(k/2))\delta_{k/2}\), where sinc(x)=sin(πx)/(πx). Poisson summation transforms the comb into atoms at even integers, and the sampled sinc-square into the sum of triangular functions centered at even integers. Subtracting the mean-density contribution removes only the atom at frequency zero. Thus

\[
V_{\rm A}(b)=\frac{2\tanh(b/2)}{b^2}+\frac2{e^{2b}-1}.
\tag{10}
\]

The even-frequency atoms in (9) are essential; the triangular density alone gives a wrong answer. Direct integration of one triangular period and a geometric series proves (10).

For every b>0,

\[
\Delta(b):=V_{\rm sine}(b)-V_{\rm A}(b)
=\frac{2e^{-2b}\big(4\sinh^2(b/2)-b^2\big)}{b^2(1-e^{-2b})}>0,
\tag{11}
\]

because 2sinh(b/2)>b. The signal is \(b/12+O(b^2)\) as b decreases to zero, and \(2e^{-b}/b^2(1+o(1))\) as b increases to infinity. Very large smoothing therefore requires exponential accuracy relative to its algebraic main term. The leading variance alone cannot separate the models.

### 3. Eliminate the near-diagonal freedom rather than assume simplicity

The Fourier transform of the alternating comb in (6) is \(2\sum_m\delta_{2m+1}\). Its contribution to (7) is

\[
\frac{2(p_0(T)-1)}{\sinh b}.
\tag{12}
\]

Thus a single variance does not uniformly distinguish the full AH-Pairs class. The correct combination is

\[
W=\sinh(2)V(2)-\sinh(1)V(1).
\tag{13}
\]

The two nuisance terms cancel. Moreover,

\[
\sinh(b)\Delta(b)=H(b):=\frac{(1-e^{-b})^2}{b^2}-e^{-b},
\]

so the two predictions differ by

\[
H(2)-H(1)=0.01987902514497878\ldots>0.
\tag{14}
\]

In closed form, with e the ordinary exponential constant,

\[
W_{\rm AH}=\frac{e^2}{4}+\frac5{4e^2}-e-\frac2e+\frac32,
\]
\[
W_{\rm GUE}=\frac{e^2}{4}-e+\frac34+\frac1e-\frac5{4e^2}+\frac1{4e^4}.
\tag{15}
\]

The companion rational script bounds e by its degree-40 Taylor sum and a geometric upper bound for the tail. Ordinary interval arithmetic gives
\(W_{\rm AH}\in(0.06239,0.06240)\),
\(W_{\rm GUE}\in(0.08227,0.08228)\), and their difference in (0.019879,0.019880). These are exact constant enclosures. They contain no computed ζ mean square.

### 4. Passing from AH-Pairs to these noncompact pair tests

The convolution kernel in physical space is

\[
K_b(x)=P_{2a}(x)=\frac{2b}{b^2+4\pi^2x^2},
\qquad
Q_T(b)=\int K_b\,d\mu_T-1.
\tag{16}
\]

For fixed b this kernel and the two-scale linear combination decay as O_b((1+x²)^−1). The cited pair bound gives
\(\mu_T([-h,h])\ll1+h\) for 0≤h≤T. Dyadic shells therefore bound the tail between M and T by O_b(1/M). Beyond T, total pair mass is O(T log T) and the kernel is O_b(T^−2), giving O_b(log T/T).

Fix M first along values M=j+1/4, so the hard truncation endpoints lie away from all limiting half-lattice atoms. The finite set of half-lattice mass formulas (5), plus concentration of each bin at k/2, then evaluates the compact part without an unresolved boundary atom. The early-zero range excluded in AH0 changes the compact pair sum by o(1), as in the source's Section 2. The two tails are uniform in T. The model mass tails are also O_b(1/M), uniformly for bounded p_0(T). Hence

\[
Q_T(b)=V_{\rm A}(b)+\frac{2(p_0(T)-1)}{\sinh b}+o(1)
\tag{17}
\]

under RH and AH-Pairs. Formally: the limsup error is O_b(1/M) after T tends to infinity, then M tends to infinity. One cannot cancel a finite truncated alternating sum as though it were already the entire comb. This two-limit argument justifies the cancellation in (13) without requiring existence of lim p_0(T).

### 5. Actual completed-zeta resolvent: endpoints and centering

Here is the conversion from the pair statistic to the real part of an actual meromorphic function. All following b values are fixed and positive. Set a=b/(4π), η=a/L, and

\[
Y_T(t)=\sum_{0<\gamma\le T}P_a(L(t-\gamma)),\qquad
Z_T(t)=\sum_{\gamma\in\mathbb R}P_a(L(t-\gamma)).
\]

The second sum is over all nontrivial zero ordinates, including negative ordinates. Under RH the paired canonical product of ξ gives exactly

\[
Z_T(t)=\frac1{\pi L}\Re\frac{\xi'}{\xi}(1/2+\eta+it).
\tag{18}
\]

Pairing positive and negative zeros fixes the constant: ξ is even about 1/2, and the paired product has factors \(1+(s-1/2)^2/\gamma^2\). The real part of its logarithmic derivative is the absolutely convergent sum of η/[η²+(t−γ)²]. Formula (18) does not require simple zeros.

The finite convolution identity is exact:

\[
\frac1T\int_{\mathbb R}Y_T(t)^2dt=\int K_b\,d\mu_T=Q_T(b)+1.
\tag{19}
\]

We give the endpoint estimates because they must not be hidden in a stationarity assumption. Standard unit-interval zero counting gives O(log(|u|+2)) zeros in an interval of length one. Consequently, for fixed a, both Y_T and Z_T are O_a(log T) on [0,T]. Let w=T/log⁴T. The two endpoint strips of width w contribute at most O_a(log^−2T) to a normalized square integral.

On [w,T−w], the omitted positive zeros above T and the negative zeros contribute

\[
|Z_T(t)-Y_T(t)|\ll_a\frac{\log T}{L^2w}=o(1)
\]

uniformly, by summing the inverse-square kernel with the unit-interval bound. The pair bound used in Section 4 implies \(T^{-1}\int_{\mathbb R}Y_T^2=O_a(1)\), so the square-integral difference on the interior is o(1) by Cauchy–Schwarz.

For t outside [0,T] by a distance d≥w, the same unit-interval count yields \(Y_T(t)\ll_a\log T/(L^2d)\). Its exterior squared integral divided by T is o(1); the exterior strips of width w have the same O(log^−2T) bound. Finally, \(T^{-1}\int_0^TY_T(t)dt\to1\): the full integral is N(T)/L, boundary zeros number O(w log T), and for each interior zero the missing Poisson mass is at most O_a(L^−2(γ^−1+(T−γ)^−1)). Summing this last expression gives O_a(log²T/L²)=O_a(1). Division by T removes it.

It follows from (18)–(19) that

\[
Q_T(b)=\frac1T\int_0^T\left(\frac1{\pi L}\Re\frac{\xi'}{\xi}(1/2+\eta+it)-1\right)^2dt+o(1).
\tag{20}
\]

No assertion that the finite zeros are exactly stationary was used.

### 6. Gamma factor and the real-square versus modulus distinction

By definition,

\[
\frac{\xi'}{\xi}(s)=\frac{\zeta'}{\zeta}(s)+\frac1s+\frac1{s-1}
-\frac12\log\pi+\frac12\frac{\Gamma'}{\Gamma}(s/2).
\tag{21}
\]

For t≥1 and the specified σ near 1/2, the real part of the extra terms is \(\frac12\log(t/(2\pi))+O(1/t)\). After dividing by πL and subtracting one, its discrepancy from zero has normalized L² norm O(1/log T). This follows by integrating \(|\log(t/T)-\log(2\pi)|^2\), and treating 0≤t≤1 separately using the absence of low ordinates and (21). The pair bound gives a bounded normalized L² norm for (20); hence Cauchy–Schwarz justifies removing this discrepancy. We obtain

\[
Q_T(b)=\frac4{T\log^2T}\int_0^T
 \left(\Re\frac{\zeta'}{\zeta}(1/2+\eta+it)\right)^2dt+o(1).
\tag{22}
\]

It is not an algebraic identity that the real-square integral equals half the modulus-square integral. To justify that step here, let \(F=\zeta'/\zeta\). Under RH, F² is analytic in the rectangle with horizontal sides at heights 1 and T, and vertical sides at σ=1/2+η and 2. The pole at s=1 lies below this rectangle. On the right side F² has an absolutely convergent Dirichlet series without a constant term; its vertical integral is O(1). On the top side the RH partial-fraction estimate gives \(F=O_b(\log^2T)\), uniformly across the rectangle, so that horizontal integral is O_b(log⁴T). The bottom integral is bounded. Thus

\[
\int_0^TF(1/2+\eta+it)^2dt=O_b(\log^4T)=o(T\log^2T).
\]

The bounded initial segment adds no relevant term. Since \(2(\Re F)^2=|F|^2+\Re F^2\), (22) becomes

\[
\boxed{Q_T(b)=\frac2{T\log^2T}I_T(b/2)+o(1).}
\tag{23}
\]

This is consistent with the classical correspondence of Goldston–Gonek–Montgomery; [Fazzari, 2310.15918, Introduction and Lemma 3](https://arxiv.org/html/2310.15918v2) also records its normalization and explicitly separates the real-square and holomorphic-square terms. A weighted version would need its own contour argument; the unweighted vanishing above must not be silently reused with an arbitrary arithmetic weight.

Equations (17), (13) and (23) prove the claimed reduction (2), subject to the stated primary RH+AH-Pairs density input. The threshold (4) is still missing.

### 7. Finite ensemble calibration and what cannot prove (4)

On a circle of length N, periodize P_a. For nonzero integer m the CUE trace second moment is min(|m|,N). For the randomly rotated ACUE model it is min(r,2N−r) when r=m mod 2N is nonzero, and N² when r=0. The latter large peaks become the even-frequency atoms in (9).

With q=e^(−b/N), the exact finite CUE variance is

\[
V_N^{\rm CUE}(b)=\frac{2q(1-q^N)}{N^2(1-q)^2},\qquad
\frac{V_N^{\rm CUE}(b)}{V_{\rm sine}(b)}
=\left(\frac{b/(2N)}{\sinh(b/(2N))}\right)^2.
\tag{24}
\]

The finite ACUE formula is

\[
V_N^{\rm ACUE}(b)=\frac2{N^2}
\frac{\sum_{m=1}^{2N-1}\min(m,2N-m)q^m+N^2q^{2N}}{1-q^{2N}}.
\tag{25}
\]

The script checks eight widths, four finite sizes, direct triangular-period integrals, and exhaustive float64 subset sums for N=2,…,6. Symbolic checks verify (11), both limiting signal sizes, and the paired canonical-product normalization on an exact rational finite example. These are normalization tests and finite-model evidence, not ζ data or an asymptotic numerical proof.

The base half-lattice process itself obeys the known low-frequency pair data while giving W_AH. Therefore no deduction using only those data and positivity can establish (4). Its signed Fourier kernel is \(\sinh(2)e^{-2|\alpha|}-\sinh(1)e^{-|\alpha|}\), which changes sign at \(\log(2\cosh1)>1\). The remaining arithmetic work controls information beyond the known band, including the negative tail. A fresh prime-correlation estimate, or a new effective arithmetic weighting/comparison, is necessary. Enlarging the finite matrix model or improving numerical precision does not supply it.

The retained deliverable is a precise one-sided ζ target with certified separation and no assumed near-diagonal limit. Further work should attack its actual signed mean square or the companion compact Fourier test. External novelty review and proof-assistant formalization are postponed until the ordinary proof audit and the arithmetic direction justify them.


<a id="report-10"></a>

# Current report 10: Independent review of the two-scale actual-zeta reduction

**Collection:** R7 — actual-zeta targets, arithmetic mark, and flow obstruction.

**Source:** [research/dyson/round7/poisson-resolvent/INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/poisson-resolvent/INDEPENDENT_REVIEW.md).

**SHA-256:** `82db15288f7b6f902a461c296abe30eb1d21253bf14ae4949da4dc12c592a370`. **Git blob:** `15b2800098652211278edc2e0c0b62b9b277d92e`. **Original bytes:** 11724.

## Independent review of the two-scale actual-zeta reduction

Date: 2026-09-05. Reviewer: the residual/arithmetic lane, independently of the authoring lane.

**Verdict: accepted as an ordinary RH-dependent reduction, with no remaining mathematical obstruction found in the reviewed argument.** The review accepts `RH + AH-Pairs => W_T -> W_AH`, including cancellation without a limit for P_0(T), and accepts both proposed sufficient arithmetic lower bounds. It does **not** prove either lower bound for actual zeta mean squares, refute AH, establish a new zeta-spacing theorem, certify novelty, or constitute proof-assistant verification.

One minor truncation issue was identified and corrected by the author during review: the fixed physical pair cutoff must avoid limiting half-lattice atoms. The current text explicitly takes M=j+1/4. The transfer proof and model formulas were otherwise unchanged. The subsequent addition of the weaker sufficient threshold 1/16 has also been checked.

The reviewed report and script hashes, temporary-copy replay details, and final metadata-only status change are pinned in `independent_review_receipt.json`.

### 1. Acceptance coverage

| component | result | reason |
|---|---|---|
| Exact source AH formulation and RH dependence | accepted | The source's AH0, (1.12), (1.14), (1.15) supply exactly the stated pair concentration, tail bound and finite-T masses. |
| Near-diagonal nuisance cancellation | accepted | The alternating comb includes k=0 and contributes 2(P_0(T)-1)/sinh(b); the two coefficients cancel at the same T. No limit for P_0(T) is used. |
| Noncompact pair test | accepted after the endpoint clarification | Uniform O(1/M) tails allow fixed-M asymptotics first; M=j+1/4 avoids atomic truncation endpoints. |
| Completed-zeta normalization | accepted | Pairing positive and negative zeros removes the possible exponential constant; the real logarithmic derivative has the required absolutely convergent Poisson sum. |
| Finite-zero endpoints and gamma centering | accepted | Width T/log^4(T), unit-interval zero counts and the pair bound control all normalized square tails; the gamma discrepancy has normalized L2 norm O(1/log T). |
| Real square to modulus square | accepted | Under RH, the square of zeta'/zeta has no poles in the chosen rectangle; the holomorphic-square vertical integral is negligible for every large T. |
| Constants and sufficient thresholds | accepted | Exact rational enclosures separate W_AH from both 7/100 and 1/16; independent symbolic checks link the closed constants to the variance formulas. |
| Script scope | accepted | The scripts prove/check constants and finite-model identities. They do not compute an actual-zeta mean square. |

### 2. Primary source check and the role of P_0(T)

The primary paper was read directly at [Goldston–Lee–Schettler–Suriajaya, arXiv:2507.06823v1](https://arxiv.org/html/2507.06823v1). Its AH-Pairs formulation uses the high interval T/log^2(T)<gamma,gamma'<=T. The RH-dependent fixed-k formulas and bounded P_0(T) are available there; its Section 2 explains removal of the excluded early range. The reduction correctly keeps these inputs separate from the paper's additional AH-Weak Density hypotheses.

Only additive o(1) accuracy for each fixed k is required. Since only finitely many k occur before the truncation limit, those errors may be combined without imposing uniform asymptotics for k growing with T. The near-zero bin may include multiplicity and near-coincident distinct zeros. It is therefore correct to preserve P_0(T), rather than silently replacing it by one.

Relative to the p_0=1 half-lattice pair measure, the finite-T mass change is

    (P_0(T)-1) sum_k (-1)^k delta_(k/2).

Its Fourier transform has mass 2 at every odd integer. Therefore its Poisson variance contribution is

    2(P_0(T)-1) sum_(m in Z) exp(-b |2m+1|)
      = 2(P_0(T)-1)/sinh(b).

The coefficient two and the inclusion of the diagonal are both necessary. The same formula follows in physical space from the classical alternating Cauchy-kernel sum. The combination at b=2 and b=1 cancels the entire nuisance parameter at each T, after the noncompact-test approximation has been justified.

### 3. Pair tails and the corrected cutoff

The source pair bound gives normalized mass O(1+h) for differences of size at most h, for 0<=h<=T. Since K_b(x)=O_b((1+x^2)^-1), a dyadic decomposition between M and T contributes O_b(1/M). Beyond T, the total normalized pair mass is O(T log T), whereas the kernel is O_b(T^-2), giving O_b(log T/T). These estimates are uniform in T for fixed b.

For the model family, bounded P_0(T) gives uniformly bounded absolute atomic weights, hence another O_b(1/M) tail. Positivity of every finite-T approximate model weight is not needed for that latter absolute bound.

A hard cutoff at a half integer would not by itself have a determined limit: an AH cluster could approach that endpoint from either side. The author's repair M=j+1/4 eliminates this ambiguity. The early-range discrepancy is o(1) for each such fixed cutoff, and the limiting bin concentration then evaluates the finite sum. Sending T to infinity first and M to infinity second proves the stated expansion uniformly for the bounded nuisance parameter. It is legitimate that Q_T(b) need not itself converge when P_0(T) oscillates; only the two-scale combination is asserted to converge.

### 4. Completed-zeta identity and endpoints

With L=log(T)/(2pi), a=b/(4pi), and eta=a/L, a single Poisson term satisfies

    P_a(L(t-gamma))
      = 1/(pi L) * eta/[eta^2+(t-gamma)^2].

Under RH, the paired canonical product about 1/2 has factors `1+(s-1/2)^2/gamma^2`. The function is even about 1/2 and has order one; no nonconstant exponential prefactor remains after pairing. Its logarithmic derivative consequently gives exactly the sum over both positive and negative ordinates, with multiplicities. The real-part series converges absolutely. There is no missing factor of two: summing over both signs already supplies the two linear factors of each paired zero.

The finite convolution identity uses `P_a*P_a=P_(2a)` and a change of variable dt=dx/L. Its normalization is therefore exactly the report's `(TL)^-1` pair measure. The kernel evaluates to

    K_b(x)=2b/(b^2+4pi^2 x^2).

The unit-interval zero count is sufficient for the stated endpoint estimates. On the two strips of width w=T/log^4(T), both finite and completed sums are O_b(log T), so their normalized squared integrals are O_b(log^-2 T). On the interior, omitted negative and above-T zeros have total Poisson contribution O_b(log T/(L^2 w)). The pair bound provides a bounded normalized square integral for the finite sum, so Cauchy–Schwarz controls the interior replacement.

The far exterior estimate O_b(log T/(L^2 d)) has an integrable square for d>=w. The full integral of a finite Poisson sum is N(T)/L; the loss from interior zero tails is bounded by summing the displayed reciprocal distances, and the boundary zero count gives a vanishing normalized contribution. Thus the mean tends to one and the subtraction of one in the centered square is correctly normalized. No exact stationarity of finite zeta zeros is assumed.

### 5. Gamma centering and the holomorphic-square rectangle

The extra real terms in xi'/xi equal one half of log(t/(2pi)), with the stated uniform lower-order error. Since pi L=log(T)/2, dividing by pi L and subtracting one leaves

    [log(t/T)-log(2pi)]/log(T) + lower-order terms.

Its normalized L2 norm is O(1/log T): the integral of |log(t/T)|^2 divided by T stays bounded, and the fixed initial interval causes no difficulty. The bounded normalized L2 norm supplied by the pair statistic justifies removal of this centering discrepancy by Cauchy–Schwarz. This yields the factor four in front of the real-square mean.

For F=zeta'/zeta, RH places every nontrivial zero strictly to the left of the rectangle whose left side is 1/2+eta. The pole at one is below its bottom side t=1. Thus F^2 is analytic in the rectangle. On Re(s)=2, its absolutely convergent Dirichlet series has no constant coefficient, so its vertical integral is O(1). On the top side, the local zero count and distance eta from the critical line give the uniform bound F=O_b(log^2 T), hence an O_b(log^4 T) horizontal integral. This works even if T is exactly a zero ordinate: the positive real displacement eta prevents a pole. The bottom and the initial segment are harmless.

Consequently the holomorphic-square integral is o(T log^2 T). Applying

    2(Re F)^2 = |F|^2 + Re(F^2)

is now justified, rather than merely assumed. Finally eta=b/(2log T), so the modulus integral is exactly I_T(b/2), giving

    Q_T(b)=2 I_T(b/2)/(T log^2 T)+o(1).

This argument is unweighted. An arbitrary arithmetic weight would change the contour problem and cannot inherit this vanishing without a separate proof.

### 6. Model spectra and exact constants

The half-lattice pair measure has diagonal mass one and the correct nonzero half-lattice masses. Fourier transformation gives the triangular periodic density plus atoms at the nonzero even integers. Those atoms are essential. The nuisance modification instead adds atoms at odd integers. The reported spectra and their Poisson integrals are consistent with these two different combs.

The variance formulas were checked independently against the closed W expressions as exact rational-function identities in x=exp(1). This closes a small verification gap that a script evaluating only the closed constants would leave: the constants really are the stated two-variance combination, not merely two separated numbers.

The rational exponential enclosure uses the sum through degree 40 and bounds the remaining factorial series by a geometric majorant. Its interval arithmetic is valid even though it repeats the same exponential variable, because independent interval multiplication only enlarges the enclosure. The certified inequalities imply both

    W_AH < .06240 < .07,
    W_AH < .06240 < 1/16,

and `1/16-W_AH > .00010`. Therefore either RH-conditional lower bound on the corresponding liminf would contradict AH-Pairs. The number .07 is a convenient stronger target, not a logically necessary threshold. Neither arithmetic lower bound follows from the constant calculation.

### 7. Replay, scope and remaining obligation

Both check scripts were copied to a fresh temporary directory and run there. Their generated JSON matched the author's files after ignoring the elapsed-time field. The exact constant script was replayed again after addition of the 1/16 assertions. Original mathematical files were not altered by the reviewer. The only authorized final report edit is the first paragraph's review-status metadata and link to this review; the receipt verifies that distinction and pins the final files.

The finite subset enumerations are floating-point calibration, while the symbolic identities and Fraction arithmetic establish their stated algebraic and constant assertions. A rational finite canonical-product example checks a normalization; it does not by itself prove the infinite xi-product statement, which is instead justified analytically above.

The unresolved work is the actual signed mean-square inequality. The half-lattice model already matches the known interior Fourier band and satisfies spectral positivity, so those facts alone cannot force a value above W_AH. The reviewed reduction makes the missing arithmetic statement precise; it does not supply the out-of-band information or control the negative tail by a new prime-correlation estimate. Acceptance of this reduction must not be described as a proof of such an inequality or as a refutation of AH.


<a id="report-11"></a>

# Current report 11: Independent review of the actual-zeta Poisson transfer

**Collection:** R7 — actual-zeta targets, arithmetic mark, and flow obstruction.

**Source:** [research/dyson/round7/dyson-frontier/POISSON_TRANSFER_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/dyson-frontier/POISSON_TRANSFER_REVIEW.md).

**SHA-256:** `fc7959a2f6147380709467776add8e4a59aa255747e46c70cad413d808e64b36`. **Git blob:** `e6c81f58e05560d6f3b6d5fced09da33a1381244`. **Original bytes:** 3945.

## Independent review of the actual-zeta Poisson transfer

5 September 2026. This reviews the root agent's proposed transfer, not a proof of the desired arithmetic mean-square asymptotic. All statements below assume RH and a fixed $b>0$.

Put $L=\log T/(2\pi)$ and

$$
K_b(u)=\frac{2b}{b^2+4\pi^2u^2},\qquad
Q_T(b)=\frac1{TL}\sum_{0<\gamma,\gamma'\le T}K_b(L(\gamma-\gamma'))-1.
$$

The proposed identity has the correct factor:

$$
Q_T(b)=\frac2{T\log^2T}\int_0^T
\left|\frac{\zeta'}\zeta\left(\frac12+\frac{b}{2\log T}+it\right)\right|^2dt+o(1).
$$

The following checks support it.

1. If $P_a(u)=a/[\pi(a^2+u^2)]$, then $K_b=P_{2a}$ with $a=b/(4\pi)$. The physical displacement is $\delta=a/L=b/(2\log T)$. For $Y(t)=\sum_{0<\gamma\le T}P_a(L(t-\gamma))$, convolution gives the exact identity $T^{-1}\int_{\mathbb R}Y^2=Q_T(b)+1$. No circular periodization is involved.
2. The full positive zero density is $Z(t)=(\pi L)^{-1}\operatorname{Re}(\xi'/\xi)(1/2+\delta+it)$, by the symmetrically paired Hadamard product. On the interval interior, the omitted zeros below zero or above $T$ contribute $O_b(\log T/(L^2w))$ if the distance to the endpoints is at least $w=T/\log^4T$.
3. The unit-interval zero bound implies $Y,Z=O_b(\log T)$ near the endpoints. Their squared contribution divided by $T$ is $O_b(w\log^2T/T)=O_b(\log^{-2}T)$. Outside the interval and at distance $d\ge w$, one can use $Y\ll_b\log T/(L^2d)$ until $d$ reaches $T$, then $Y\ll_b N(T)/(L^2d^2)$. These bounds make the exterior squared integral $o(T)$. They avoid the incorrect use of a constant bound on an infinite exterior interval.
4. The mean $T^{-1}\int_0^TY\to1$ follows from the zero-count asymptotic and the Poisson tail estimate. The same holds for $Z$. The gamma and elementary factors give

$$
Z(t)-1=\frac2{\log T}\operatorname{Re}\frac{\zeta'}\zeta(1/2+\delta+it)
+\frac{\log(t/(2\pi))-\log T}{\log T}
+\text{a negligible compact-height correction}.
$$

The displayed drift has mean square $O(\log^{-2}T)$ after averaging over $[1,T]$. Uniform boundedness of the pair-kernel quadratic form controls its cross term by Cauchy–Schwarz.
5. For $q(s)=\zeta'/\zeta(s)$, a rectangle with vertical sides $\sigma=1/2+\delta$ and $\sigma=2$ and lower height $1$ avoids the pole at $s=1$. Under RH, $|q(\sigma+iT)|\ll_b\log^2T$ uniformly along its top, even when $T$ is a zero ordinate. Thus the top integral of $q^2$ is $O_b(\log^4T)$. At $\sigma=2$, the squared absolutely convergent Dirichlet series has no constant term and has a bounded time primitive. The lower side is harmless; alternatively choose any fixed lower height away from zero ordinates and treat the omitted compact interval separately. Consequently $\int_0^Tq(1/2+\delta+it)^2dt=o(T\log^2T)$. Using $(\operatorname{Re}q)^2=(|q|^2+\operatorname{Re}q^2)/2$ produces the claimed factor $2$.

For passage from AH-Pairs to Poisson tests, the cumulative local-pair bound in GLSS (1.12), printed p.4, suffices. It is only stated up to normalized radius $T$. Dyadic summation gives $O(1/R)$ tails for the Poisson pair kernel inside that range, and the total-mass bound gives $O(\log T/T)$ outside it. A global uniform translation bound is not required.

The nuisance term in the centered spectral measure is $2(p_0-1)\sum_m\delta_{2m+1}$. Against $e^{-b|\alpha|}$ it contributes $2(p_0-1)/\sinh b$. Hence a signed combination $\sinh(b_1)Q_T(b_1)-\sinh(b_2)Q_T(b_2)$ can eliminate this parameter without a limit assumption on $P_0(T)$: first truncate at radii $M=j+1/4$ to avoid half-lattice boundary atoms, apply the uniform finite-$T$ density formulas, and then use the tail estimates.

Verdict: the normalization, endpoint strategy, complex-square cancellation, and nuisance-parameter elimination are consistent. The remaining mathematical input is an actual estimate of the resulting signed logarithmic-derivative mean squares. The transfer identity itself does not provide that estimate or refute AH.


<a id="report-12"></a>

# Current report 12: One actual-zeta target beyond Fourier support one

**Collection:** R7 — actual-zeta targets, arithmetic mark, and flow obstruction.

**Source:** [research/dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md).

**SHA-256:** `3b8eb5fb9efc2f53af550db64c1e8eef7233f8be83564e906357b3acf00a0301`. **Git blob:** `5cb96f2a0878978a39cf4025d1f40e760d0d4e67`. **Original bytes:** 17526.

## One actual-zeta target beyond Fourier support one

Date: 5 September 2026. Status: primary-source audit, an exact arithmetic reduction, and a conditional AH-Pairs detector. The required new arithmetic estimate is not proved here. The reductions use existing explicit-formula and Fourier arguments; no priority or novelty claim is made. No claim to have proved Montgomery's conjecture, refuted AH for zeta, or established RH is made.

### 1. Selected research target and the result of this round

Fix once and for all a nonnegative, normalized, symmetric smooth bump $\phi$ with closed support $[6/5,7/5]\subset(1,2)$ and centered at $13/10$. For example, normalize

$$
\phi(\alpha)=C\exp\!\left(-\frac1{1-(10\alpha-13)^2}\right)
\mathbf1_{\{|10\alpha-13|<1\}}.
$$

Then $\int\phi=1$ and $\int\alpha\phi(\alpha)d\alpha=13/10$. Assuming RH, define the actual-zeta form factor, with all zeros counted with multiplicity, by

$$
F_T(\alpha)=\frac{2\pi}{T\log T}
\sum_{0<\gamma,\gamma'\le T}
T^{i\alpha(\gamma-\gamma')}
\frac4{4+(\gamma-\gamma')^2}.
\tag{1}
$$

The ambitious target is the single smoothed Montgomery prediction

$$
\mathcal C_\phi(T):=\int\phi(\alpha)F_T(\alpha)d\alpha\longrightarrow1.
\tag{2}
$$

There is a weaker, still consequential target:

$$
\liminf_{T\to\infty}\mathcal C_\phi(T)>\frac7{10}.
\tag{3}
$$

Under RH, (3) contradicts the precise AH-Pairs hypothesis defined in Goldston–Lee–Schettler–Suriajaya, not merely the particular ACUE model. This assertion is proved in §3 below. It depends on the stated AH definition; it is not a claim about every informal hypothesis sometimes called “alternative.”

The main output is the exact centered prime-covariance obligation (12)–(15). It reduces (2) to a specified signed average of shifted von Mangoldt correlations, with the pole/continuous-mean term retained. It also shows precisely why a scalar sieve distribution exponent is not the missing input. No estimate closing (3) was obtained from the currently checked tools.

### 2. Primary-source state as checked on 5 September 2026

| Result | Status and implication for this target |
|---|---|
| Montgomery's actual-zeta pair-correlation theorem | Under RH, $F_T(\alpha)=\vert \alpha\vert +T^{-2\vert \alpha\vert }\log T+o(1)$ in the known low band, interpreted distributionally at zero. This evaluates Fourier tests supported inside $(-1,1)$, not (2). See [Goldston's primary-author notes](https://arxiv.org/abs/math/0412313), Theorem 1. |
| Higher correlations | Rudnick–Sarnak obtain the GUE correlations for the usual real-zero formulation under RH and the Fourier condition $\sum_j\vert \xi_j\vert <2$. On the translation-invariant hyperplane this does not supply an independent pair frequency above one. See [their original announcement](https://www.math.tau.ac.il/~rudnick/papers/RudnickSarnakCRAS1994.pdf), Theorem 1.2 and its first remark. |
| Unconditional pair-correlation identity | [Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh](https://arxiv.org/abs/2306.04799) remove RH from a generalized identity involving the full complex zeros. Interpreting it as an ordinary positive statistic of real ordinates requires care. This is not an asymptotic plateau on an interval above one. |
| The “0.6…” AI result | The precise constant is $C_0=3/2-2^{-1/2}\cot(2^{-1/2})=0.6725007\ldots$ for zeros that are both simple and on the critical line, unconditionally. [Anthropic's paper](https://arxiv.org/abs/2608.13637) and [Lamzouri's new proof](https://arxiv.org/abs/2609.02882), Theorem 1.1, give this result and the distinct-zero proportion $(1+C_0)/2$. Lamzouri's arXiv submission is dated **2 September**, not 3 September. His Lemma 3.1 still uses support $[-1,1]$. This improves what can be inferred from available spectral information; it does not provide the covariance in §4. |
| Quantitative bounds above one | [Carneiro–Milinovich–Ramos](https://arxiv.org/abs/2310.01913), Corollary 2, bound sufficiently long interval averages between $0.9303+o(1)$ and $1.3208+o(1)$ under RH. These are bounds, not a plateau asymptotic. Their equation (1.7) records the GRH lower bound $F_T(\alpha)\ge3/2-\vert \alpha\vert -\varepsilon$ on its stated range. |
| AH and simplicity | [Goldston–Lee–Schettler–Suriajaya II](https://arxiv.org/abs/2507.06823), Theorem 4, derives asymptotic simple critical zeros from AH-Pairs **plus** their AH-Weak Density assumptions. It does not refute AH. Their companion [PCC paper](https://arxiv.org/abs/2503.15449) derives simple critical zeros conditionally on PCC without assuming RH; it does not prove PCC. |

The checked primary sources do not establish (2) or (3). Results for a family of Dirichlet $L$-functions with extra character/modulus averaging, and results for function fields, must not be imported as the corresponding theorem for this single zeta function. The CMR paper itself separates its family result with support below two from the actual-zeta problem.

This round also read the existing force-energy, dynamic-generator, attachment-bridge audit, and main handoff. Their valid conclusions remain in force: the circular force square reduces to a singular two-point observable; protected trace dynamics do not create new bandwidth; and a finite heat-depth theorem supplies no unproved local flow for actual zeta. Those old calculations were not rerun.

### 3. Why the compact test excludes the precise AH-Pairs class

Put $L=\log T/(2\pi)$ and $N_T=TL$, and consider the positive pair measure

$$
\mu_T=\frac1{N_T}\sum_{0<\gamma,\gamma'\le T}
w(\gamma-\gamma')\,\delta_{L(\gamma-\gamma')},
\qquad w(v)=\frac4{4+v^2}.
\tag{4}
$$

With Fourier convention $\widehat f(\alpha)=\int f(u)e^{-2\pi i\alpha u}du$, its Fourier transform is $F_T$; the sign is immaterial because the pair measure is even.

The primary AH-Pairs condition says that for each fixed $M$, every pair with both ordinates in $(T/\log^2T,T]$ and $|L(\gamma-\gamma')|\le M$ lies within $O((|k|+1)R(T))$ of some $k/2$, where $R(T)\to0$. The needed compactness is not assumed without evidence. Their equation (1.12), printed p.4, supplies

$$
\mu_T([-R,R])\ll1+R\qquad(0\le R\le T).
\tag{5}
$$

For $R>T$, the crude total mass bound is $O(T\log T)$; do not upgrade (5) to a global uniform linear bound. Together these two estimates control Schwartz tails uniformly. For a test decaying like $(1+u^2)^{-1}$, dyadic shells up to $T$ give $O(1/R)$ and the remaining tail gives $O(\log T/T)$. This also suffices for the Poisson pair kernels used in the parallel resolvent lane.

Pairs involving an ordinate below $T/\log^2T$ contribute $o(N_T)$ to any fixed local test: there are $O(T/\log T)$ such zeros, and the elementary unit-interval zero bound gives $O(\log T)$ possible partners in a fixed normalized window. After division by $N_T$ this is $O(1/\log T)$. The uniform tail estimate then handles Schwartz tests. On compact normalized intervals $w(u/L)\to1$, so the weighted and unweighted local limits agree.

Consequently every subsequential tempered limit $\mu$ is a measure supported on $\tfrac12\mathbb Z$. It obeys $e^{4\pi iu}\mu=\mu$, hence $\widehat\mu$ is 2-periodic as a tempered distribution. Montgomery's theorem determines its restriction to $(-1,1)$:

$$
\widehat\mu=\delta_0+|\alpha|\,d\alpha
\quad\hbox{on }(-1,1).
$$

Translation by two therefore determines it on $(1,2)$:

$$
\widehat\mu=(2-\alpha)\,d\alpha.
\tag{6}
$$

Testing (6) against the fixed $\phi$ gives $\mathcal C_\phi(T)\to7/10$. The conclusion holds for every subsequence, so no prior existence of the full limiting pair measure is needed. It proves the contradiction claimed in (3). A second agent independently checked this argument, including the restricted range in (5) and the removal of early zeros.

#### The unknown near-diagonal mass is confined to odd-frequency atoms

There is a useful more explicit statement. The same paper, equations (1.14)–(1.15), printed p.4, gives, under RH and AH-Pairs,

$$
1\le p_0\le\frac32-\frac2{\pi^2}
$$

along a subsequence on which the near-zero pair mass converges. The nonzero even half-lattice masses are $p_0-1/2$; the odd ones are $3/2-p_0-2/(\pi^2k^2)$. Their difference from the $p_0=1$ measure is

$$
(p_0-1)\sum_{k\in\mathbb Z}(-1)^k\delta_{k/2}.
$$

Writing $\operatorname{tri}_2(\alpha)=\operatorname{dist}(\alpha,2\mathbb Z)$, the full pair spectral measure is therefore

$$
\widehat\mu_{p_0}
=\operatorname{tri}_2(\alpha)d\alpha
+\sum_{m\in\mathbb Z}\delta_{2m}
+2(p_0-1)\sum_{m\in\mathbb Z}\delta_{2m+1}.
\tag{7}
$$

The centered spectral measure omits the atom at zero. The fixed test in (2) avoids all integer atoms, which is why it needs no simplicity or $p_0=1$ assumption. A one-scale unbandlimited resolvent statistic generally does need to account for the last term. Two suitably chosen signed Poisson scales can cancel this parameter; that is the separate root-agent construction reviewed in the adjacent note.

### 4. Exact prime-side identity with the pole term retained

For $x>1$ and $u>0$ define

$$
a_u(x)=\min\{(u/x)^{1/2},(x/u)^{3/2}\}.
$$

The absolutely convergent arithmetic signal is

$$
P_x(t)=\sum_{n\ge2}\Lambda(n)a_n(x)n^{-it}-M_x(t),
$$
$$
M_x(t)=\int_0^\infty a_u(x)u^{-it}du
=\frac{2x^{1-it}}{(1/2+it)(3/2-it)}.
\tag{8}
$$

The equality in (8) follows by integrating separately below and above $x$. This continuous mean is precisely the pole term in Montgomery's explicit formula. It cannot be dropped. The series converges absolutely because its tail is $O_x(\Lambda(n)n^{-3/2})$; this is not a formal expansion of $\log\zeta$ or $\zeta'/\zeta$ on the critical line.

Goldston's notes, Proposition 1 and equations (4.4)–(4.5), give under RH

$$
P_x(t)=-2x^{1/2-it}\sum_{\gamma\in\mathbb R}
\frac{x^{i\gamma}}{1+(t-\gamma)^2}+E_x(t),
$$
$$
E_x(t)\ll x^{-1/2}\log(t+2)+x^{-2}/(t+2).
$$

The integrated zero kernel differs from the truncated pair sum by $O(x\log^3T)$. Its squared norm is $O(xT\log^2T+x\log^3T)$. Cauchy–Schwarz with $\int_0^T|E_x|^2\ll x^{-1}T\log^2T$ shows, uniformly for $x=T^\alpha$ with $6/5\le\alpha\le7/5$,

$$
F_T(\alpha)
=\frac1{xT\log T}\int_0^T|P_x(t)|^2dt+o(1).
\tag{9}
$$

For example, the resulting normalized error is bounded by a constant times $\log T/x+\log^2T/T$ plus smaller terms. Thus the interchange with the fixed bump has no unstated uniformity problem.

Let $d\Delta(u)=d\psi(u)-du$, where $d\psi$ has mass $\Lambda(n)$ at each integer $n$. Define the explicit real symmetric kernel

$$
\mathcal K_T(u,v)=\frac1{T\log T}
\int\phi(\alpha)T^{-\alpha}a_u(T^\alpha)a_v(T^\alpha)
\frac{\sin(T\log(u/v))}{\log(u/v)}d\alpha,
\tag{10}
$$

using the continuous value $T$ on the diagonal. Absolute convergence of the weighted total variations justifies Fubini for each fixed $T$. Expanding the finite-time square gives the exact identity

$$
C_T:=\iint\mathcal K_T(u,v)d\Delta(u)d\Delta(v)
=\frac1{T\log T}\int\phi(\alpha)T^{-\alpha}
\int_0^T|P_{T^\alpha}(t)|^2dt\,d\alpha.
\tag{11}
$$

By (9), $C_T=\mathcal C_\phi(T)+o(1)$. The kernel changes sign away from the diagonal; positivity of the whole squared norm does not make each shifted-prime summand positive.

Separate the atomic diagonal

$$
D_T=\sum_n\Lambda(n)^2\mathcal K_T(n,n).
$$

The prime number theorem with partial summation gives $\sum_n\Lambda(n)^2a_n(x)^2\sim x\log x$. Hence $D_T\to13/10$. The **centered off-diagonal remainder** is exactly

$$
\begin{aligned}
E_T={}&2\sum_{m<n}\Lambda(m)\Lambda(n)\mathcal K_T(m,n)\\
&-2\sum_n\Lambda(n)\int_0^\infty\mathcal K_T(n,v)dv
+\int_0^\infty\int_0^\infty\mathcal K_T(u,v)du\,dv.
\end{aligned}
\tag{12}
$$

Equations (9)–(12) yield the promised exact research obligations:

$$
\boxed{\text{RH implies: target (2) is equivalent to }E_T\longrightarrow-3/10.}
\tag{13}
$$
$$
\boxed{\text{RH and AH-Pairs imply }E_T\longrightarrow-3/5.}
\tag{14}
$$
$$
\boxed{\text{Under RH, proving }\liminf E_T>-3/5
\text{ suffices to refute AH-Pairs.}}
\tag{15}
$$

The second and third terms of (12) are part of the required cancellation. The arithmetic task is not to bound the first, uncentered sum by its diagonal. Individual uncentered terms can be much larger than the final normalized answer.

### 5. What known distribution tools do and do not supply

Writing $n=m+d$, the oscillatory factor in (10) changes appreciably around $d\asymp m/T$. Since the prime weight emphasizes $m$ comparable to $x=T^\alpha$, the natural short-interval length is $H=x/T=x^{1-1/\alpha}$. For this test its exponents lie between $1/6$ and $2/7$. This is a description of the principal scale, not an assertion that all larger shifts or tails may be discarded.

Goldston–Montgomery's theorem gives the established bridge to short-interval variance. Goldston's Theorem 7 states the localized multiplicative-interval version, including logarithmic padding of the ranges; his equation (9.3) gives the fixed-length version. Under RH, a sufficiently uniform asymptotic

$$
\int_1^X(\psi(y+H)-\psi(y)-H)^2dy
\sim HX\log(X/H)
\tag{16}
$$

in the corresponding padded range implies the plateau target. It is not legitimate to infer a localized equivalence from one isolated $(X,H)$ scale with no uniformity. Formula (12) is the sharper single-test obligation and avoids adding that unnecessary claim.

A standard sufficient, stronger hypothesis is the square-root-error Hardy–Littlewood prime-pair estimate

$$
\sum_{n\le X}\Lambda(n)\Lambda(n+d)
=\mathfrak S(d)X+O_\varepsilon(X^{1/2+\varepsilon})
\tag{17}
$$

uniformly in the required shifts and partial-summation ranges. The weighted singular-series sum produces the $-HX\log H$ correction to the diagonal variance. Summing errors with triangular weights costs $O(H^2X^{1/2+\varepsilon})$, which is negligible against $HX\log X$ for $H\le X^{1/2-2\varepsilon}$. The selected exponent range lies inside that regime. This is a sufficient conditional explanation, not a proof of (17); the averaged signed condition (12) is weaker than demanding (17) for every shift.

The checked existing tools leave the following precise gap:

1. The Montgomery–Vaughan mean-value error for this Dirichlet series is controlled by $\sum n\Lambda(n)^2a_n(x)^2\asymp x^2\log x$. After normalization its size is comparable to $x/T$, which grows as a power of $T$ here. It does not provide an $o(1)$ error above support one.
2. Distribution of primes in arithmetic progressions, including complementary-factorization and triply divisible-modulus inputs in the 186 proof, controls a different family of linear prime sums. No identity in that proof supplies the centered two-prime covariance (12). Replacing its supported-modulus conditions by a scalar exponent does not repair this missing estimate.
3. Almost-everywhere prime existence or a first-order short-interval prime asymptotic need not resolve the second moment at the precision $HX\log(X/H)$: the much larger scale $H^2X$ is insufficient.
4. The GRH lower bound $F_T(\alpha)\ge3/2-\alpha-\varepsilon$ yields approximately $0.2$ for this bump, below the AH value $0.7$. The long-interval CMR bounds are also compatible with AH: the long average of (7) is $p_0$, and the full allowed interval $[1,1.2973576\ldots]$ lies inside their RH bounds. These results do not close (15).

There is also a rigorous information obstruction: low-band pair data and the protected moment algebra admit the half-lattice alternative while predicting the different value $0.7$ here. Therefore an argument using only those statistical constraints cannot force the value $1$. This does not prove that all future analytic methods must fail; it specifies that a new arithmetic estimate, or genuinely additional information, is needed.

### 6. Reproducibility, independent challenge, and stopping point

`sources/download_manifest.json` records seven downloaded primary PDFs with SHA256 hashes. It also records that the Anthropic expert-note URL was readable through the web tool but its separate local download returned HTTP 403; the arXiv paper was retrieved instead.

`kernel_identity_check.py` verifies the continuous mean in (8) and the diagonal/off-diagonal/mean expansion for a deliberately truncated prime polynomial at $x=8,T=3,n\le64$, using 60-digit arithmetic. The direct and expanded integrals agree within $3.0\times10^{-59}$. Omitting the mean changes that finite answer by about $212.37$, illustrating the sign/centering issue. These are numerical normalization checks, not interval enclosures or evidence for an asymptotic prime-pair conjecture. The initial unsplit improper quadrature did not meet its tolerance; splitting the logarithmic integration range resolved that numerical issue. The bundled document Python lacked `mpmath`; the recorded run uses the existing Homebrew Python with `mpmath` 1.3.0.

The AH support/periodicity step was independently challenged by the heat-flow agent. The root agent's separate Poisson-resolvent transfer was independently reviewed in `POISSON_TRANSFER_REVIEW.md`. No old finite-model computation was rerun and no new zero-data fit is being presented as a theorem.

The outcome is an explicit, weaker-than-full-PCC arithmetic target whose success would contradict a precise famous alternative under RH. The current round closes the normalization and source-audit questions; it does not close the signed prime-correlation estimate (15). The next justified research step is to attack that estimate, or an equivalent two-scale logarithmic-derivative statistic, with additional arithmetic structure. Reoptimizing a low-band detector alone would repeat the already identified information barrier.


<a id="report-13"></a>

# Current report 13: Forward true-zeta localization: a contractive comparison and a sharp universality obstruction

**Collection:** R7 — actual-zeta targets, arithmetic mark, and flow obstruction.

**Source:** [research/dyson/round7/true-zeta-flow/FORWARD_FLOW_OBSTRUCTION.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/true-zeta-flow/FORWARD_FLOW_OBSTRUCTION.md).

**SHA-256:** `33431c7878caae9fa30af2cd09b993f9040493e447311d67bb0b393b2e8ce7da`. **Git blob:** `0e1b29fd3c73f4148883a194aafd4409a070b08f`. **Original bytes:** 19946.

## Forward true-zeta localization: a contractive comparison and a sharp universality obstruction

**Status:** ordinary written proofs of the comparison and model obstruction below. They identify an explicit missing boundary estimate and an independent stochastic-comparison obligation. No new Montgomery theorem, refutation of actual-zeta AH, or RH result is claimed.

The substantive conclusion is that positive time removes the negative-time nonreal-background problem, but does not turn the deterministic zero dynamics into finite-temperature Dyson Brownian motion. Even perfect local control of the remote field is compatible with a persistent half-spacing hard core. An exact two-periodic family demonstrates this, and a protected Fourier observable shows that the omitted diffusion acts at order one on the microscopic time scale.

### 1. Sources and conventions

The primary sources checked were:

- [Rodgers–Tao, *The de Bruijn–Newman constant is non-negative*, version 5](https://arxiv.org/abs/1801.05914v5), especially the H_t convention, Theorem 11/equation (56), and the discussion of local clock equilibrium. The retained local text is research-round2/rodgers-tao-1801.05914.txt. Their displayed theorem is stated on Lambda<t≤0 under the contradiction assumption; it must not be cited as a newly established uniform positive-time zero-count theorem.
- [Erdős–Schlein–Yau–Yin, *The local relaxation flow approach to universality of the local statistics for random matrices*](https://www.numdam.org/article/AIHPB_2012__48_1_1_0.pdf), particularly the stochastic evolution and its diffusion term, equation (5.5).
- [Landon–Sosoe–Yau, *Fixed energy universality for Dyson Brownian motion*](https://arxiv.org/abs/1609.09011v3): the initial data can be deterministic, but the subsequent dynamics has Brownian noise. The density hypotheses and time scales in this theorem do not eliminate that noise.

Earlier internal reports checked were yau_flow.md, galilean-proof-audit.md, dynamic_generator.md and new_attachment_bridge_audit.md. This note retains their warning that finite-window scalar heat is not automatically the restriction of the global H_t, and adds a forward-time comparison with its precise boundary limitation.

The genuine convention is

\[
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad \partial_tH_t=-\partial_z^2H_t.
\]

Increasing t is repulsive zero motion. Under RH, all zeros are real for t≥0. Work on a compact positive-time interval where the tracked zeros are simple, or begin at t=0 with the needed simple branches. No negative-time all-real assumption is imported. The standard H-coordinate zero is twice the usual zeta ordinate.

At a simple zero x_i, implicit differentiation gives x_i'=H_t''(x_i)/H_t'(x_i). The even canonical product supplies the principal-value identity

\[
x_i'=2\operatorname{PV}\sum_{j\ne i}\frac1{x_i-x_j}.
\tag{1}
\]

The principal value is the one associated with the even global product. Splitting off finitely many terms does not permit changing its renormalization. On an interval free of external zeros the derivative of the external field is absolutely convergent and nonpositive.

### 2. Gap-independent contraction for a correctly localized system

**Proposition 1.** Let x_1<...<x_n and y_1<...<y_n be C¹ real trajectories on [0,S]. Suppose

\[
\dot x_i=2\sum_{j\ne i}\frac1{x_i-x_j}+F(s,x_i),
\qquad
\dot y_i=2\sum_{j\ne i}\frac1{y_i-y_j}+F(s,y_i)+e_i(s),
\tag{2}
\]

where F is C¹ in its spatial argument on an interval containing both configurations and F_x≤0. Then

\[
\|x(s)-y(s)\|_\infty
\le\|x(0)-y(0)\|_\infty+
\int_0^s\|e(u)\|_\infty\,du.
\tag{3}
\]

The constant is independent of the smallest internal gap. The order and absence of collisions are hypotheses on the comparison interval, not conclusions obtained by ignoring a collision.

**Proof.** Put w_i=x_i−y_i. The internal difference is exactly

\[
2\sum_{j\ne i}\left(\frac1{x_i-x_j}-\frac1{y_i-y_j}\right)
=-\sum_{j\ne i}a_{ij}(w_i-w_j),
\quad
a_{ij}=\frac2{(x_i-x_j)(y_i-y_j)}>0.
\tag{4}
\]

The external difference equals b_i w_i, with

\[
b_i=\int_0^1F_x(s,y_i+v w_i)\,dv\le0.
\]

At an index realizing a positive maximum of w, the internal and external terms are nonpositive. At a negative minimum, they are nonnegative. Upper Dini derivatives therefore give (3). This is a maximum principle for a cooperative graph Laplacian, not an estimate by the absolute value of its potentially very large derivative.

If the true external field is F_true and the surrogate uses F_approx, take e_i=F_approx(s,y_i)−F_true(s,y_i). The estimate requires its bound at **every retained particle**.

There is also an exact spatially resolved form. Let U(s,u) be the positive, substochastic propagator generated by the matrix with off-diagonals a_ij and diagonal entries −sum_j a_ij+b_i. Then

\[
|w_i(s)|\le\sum_j U_{ij}(s,0)|w_j(0)|
+\int_0^s\sum_jU_{ij}(s,u)|e_j(u)|\,du.
\tag{5}
\]

This follows from variation of constants and positivity. It records exactly how a possibly poor boundary approximation propagates into a central window.

### 3. What remote-zero counting controls, and what it does not

In microscopic coordinates, fix a center and write the remote zero offsets as d_j with |d_j|≥L. For |z|≤R≤L/2 set

\[
F_{\rm far}(z)=2\operatorname{PV}\sum_{|d_j|\ge L}\frac1{z-d_j},
\qquad B_p=\sum_{|d_j|\ge L}|d_j|^{-p}.
\]

The following estimates follow term by term; only the constant term needs principal-value interpretation:

\[
F_{\rm far}'(z)=-2\sum_{|d_j|\ge L}(z-d_j)^{-2}\le0,
\tag{6}
\]

\[
|F_{\rm far}(z)-F_{\rm far}(0)|\le4R B_2,
\tag{7}
\]

\[
|F_{\rm far}(z)-F_{\rm far}(0)+2B_2z|\le4R^2B_3.
\tag{8}
\]

For (8), expand 1/(z−d)=−1/d−z/d²−z²/[d²(d−z)]. The error is at most 2z²/|d|³ per reciprocal, and the zero ODE contributes its factor 2.

If the remote counting function obeys # {j:L≤|d_j|≤r}≤Ar+B for every r≥L, integration by parts gives

\[
B_p\le\frac{pA}{p-1}L^{1-p}+BL^{-p}\qquad(p>1).
\tag{9}
\]

At t=0 for the true H-function, normalize a large H-height X by

\[
\rho_X=\frac1{4\pi}\log\frac{X}{4\pi},\qquad
q_j=\rho_X(x_j-X),\qquad s=\rho_X^2 t.
\tag{10}
\]

The Riemann–von Mangoldt counting formula gives, for p=2,3 and 1≤L≤X rho_X/2,

\[
\sum_{|q_j|\ge L}|q_j|^{-p}
\ll L^{1-p}+\frac{\log X}{L^p}.
\tag{11}
\]

One way to check (11) is to use the local bound O(r+log X) on dyadic shells up to distance X rho_X/2. Beyond that distance, the global O(Y log Y) zero-count bound gives a convergent geometric tail of order (X rho_X)^(1−p). This is absorbed in the first displayed term. No uniform linear-count bound at all arbitrarily large normalized distances is being assumed.

Thus ordinary zero counting already makes a sufficiently remote field nearly a common translation in a fixed central window. For example L=(log X)² makes the right sides in (7)–(8) tend to zero for fixed R. The translation itself need not be small and must be retained or removed by a moving center. The curvature term is a scalar linear drift, not independent Brownian forcing of neighboring particles.

**Boundary limitation.** Suppose the retained block consists of all zeros out to distance L. Its edge particles are close to the first omitted zeros, not a distance comparable to L from them. Estimate (8) is small in the central core, but generally is not small on every retained particle. Dense zeta configurations do not supply an empty annulus that fixes this problem. It is invalid to substitute a central-core Taylor estimate into the whole-block norm in (3).

For a proposed finite-window comparison, a precise remaining estimate is

\[
\sup_{i\in I_{\rm core}}\int_0^{S_X}
\sum_{j\in I_X}U_{ij}(S_X,u)
\left|F_{\rm approx}(u,y_j)-F_{\rm true}(u,y_j)\right|\,du=o(1),
\tag{B}
\]

together with the corresponding initial-error term in (5). All terms refer to the actual chosen moving window, microscopic normalization, external principal value and coupled trajectories. This is a boundary-propagation obligation, not just a static inverse-square-tail estimate. A short-range comparison or a killed-propagator estimate could establish it, but it has not been established for the true-zeta windows in this report.

To use (11) during an interval of true H_t flow, one must also establish the relevant uniform zero-count estimate on that shrinking positive-time interval. The static formula at t=0 alone does not prove it. Neither this temporal issue nor (B) can be silently supplied by citing a DBM theorem.

### 4. An exact half-grid obstruction even with excellent external-field control

**Proposition 2.** There exist deterministic circular heat families whose normalized local counting discrepancy is uniformly at most 2, whose initial configurations belong to the ACUE half-grid support up to rotation, and whose normalized nearest-neighbor gaps are at least 1/2 for every forward microscopic time. Their local pair statistics never equal the sine-kernel pair law.

**Construction and proof.** Let N=2M and

\[
P_0(z)=z^{2M}-2c z^M+1,\qquad c=\cos(\pi/4)=1/\sqrt2.
\tag{12}
\]

For the repulsive circular coefficient flow

\[
\partial_tP=z^2P_{zz}-(N-1)zP_z,
\]

the coefficient of z^k is multiplied by exp(−k(N−k)t). Therefore

\[
P_t(z)=z^{2M}-2c e^{-M^2t}z^M+1.
\tag{13}
\]

Put a(t)=arccos(c e^(−M²t)). Its roots have arguments (2pi j±a(t))/M. At time zero, rotation by pi/(4M) places them at grid indices 4j and 4j+1 on the 4M=2N grid. They are consequently a valid ACUE-support configuration; this is not an assertion that the family is typical under ACUE's random law.

In normalized position q=N theta/(2pi), consecutive gaps alternate between

\[
g_-(s)=\frac2\pi\arccos(c e^{-\pi^2s}),\qquad
g_+(s)=2-g_-(s),
\quad s=\frac{N^2t}{4\pi^2}.
\tag{14}
\]

For all s≥0, 1/2≤g_−(s)≤1≤g_+(s)≤3/2. The limit as s tends to infinity is the unit clock. The periodically unfolded configuration is a union of two arithmetic progressions of spacing 2. Each progression's count differs from half the interval length by less than one, so the total counting discrepancy is at most 2 in every interval, uniformly in time. Its far inverse-power tails therefore satisfy (9) with absolute constants and have exactly the sort of small central external variation that motivates the localization proposal.

Nevertheless no pair has positive separation in (0,1/2), at any time. Let phi be a nonnegative smooth function of integral one supported in (1/4,1/3). The normalized pair statistic tested against phi vanishes identically for this family, while for the unit-density sine-kernel process it equals

\[
\int\phi(u)\left[1-\left(\frac{\sin\pi u}{\pi u}\right)^2\right]du
\ge1-\frac8{\pi^2}>0.
\tag{15}
\]

The inequality uses monotonic decrease of sin(x)/x on the relevant positive interval. Randomly translating the periodic family makes it stationary without changing this discrepancy. The argument does not depend on a doubtful expectation of a minimum gap or on a rare collision event.

The exact clock c=0 is an even simpler stationary obstruction. The two-periodic family is useful because it starts with the characteristic half-grid gap pair 1/2,3/2 and evolves nontrivially. It shows that a successful deterministic positive-time localization theorem, even with strong density control, cannot by itself imply finite-beta Montgomery/GUE statistics.

This family has no claim to satisfy the arithmetic explicit formula or all known zeta correlations. It refutes only an inference whose hypotheses consist of real repulsive flow plus local counting/remote-field control. Actual arithmetic input must distinguish it.

### 5. The missing diffusion is visible at the microscopic generator scale

Use radian circle coordinates and write

\[
V_i=\sum_{j\ne i}\cot\frac{\theta_i-\theta_j}{2},\qquad
L=\sum_iV_i\partial_{\theta_i}.
\]

With this drift normalization, circular beta-DBM has generator

\[
\mathcal G_\beta=L+\frac2\beta\Delta.
\tag{16}
\]

Indeed its diffusion coefficient is sqrt(4/beta), and the score of the circular beta density is (beta/2)V. For beta=2, the generator is L+Delta and CUE is stationary. A change to the common 1/N drift convention rescales both time and noise, not just the drift.

For p_m=sum_j exp(im theta_j) and F_m=|p_m|²/N,

\[
\Delta F_m=2m^2(1-F_m).
\tag{17}
\]

CUE has E F_m=m/N for 1≤m≤N. Its stationarity under L+Delta yields

\[
\mathbb E_{\rm CUE}LF_m=-2m^2(1-m/N).
\tag{18}
\]

In microscopic time s=N²t/(4pi²), the expected initial contribution of the omitted diffusion is

\[
8\pi^2(m/N)^2(1-m/N).
\tag{19}
\]

For even N and m=N/2, this is exactly pi², whereas the deterministic CUE initial derivative is −pi². These are exact finite-N generator identities. No uniform finite-time expansion is inferred solely from a derivative at zero. They already disprove an identification of the deterministic and stochastic generators or a claim that the Brownian term is a negligible microscopic perturbation.

The clock gives another check: for 1≤m<N, F_m=0 and LF_m=0 pointwise, whereas Delta F_m=2m². The deterministic clock is fixed; beta=2 DBM immediately creates fluctuations.

### 6. Protected moments remain blind even after adding DBM

Let W_N be the finite vector space spanned by symmetric trace monomials whose total positive Fourier weight and total negative Fourier weight are separately at most N. The previous dynamic-generator audit proved that L preserves each such weight block and that ACUE and CUE have the same initial expectation on W_N.

The Laplacian also preserves this filtration. For any signed integers m,n,

\[
\Delta(p_m p_n)=-(m^2+n^2)p_m p_n-2mn p_{m+n},
\qquad p_0=N.
\tag{20}
\]

For products of more traces, apply the product rule to each pair of factors. Same-sign merging preserves the positive/negative weights; opposite-sign merging reduces both by min(|m|,|n|). Thus L+Delta acts on the same finite space W_N.

The expectation vector of every finite-time beta=2 DBM evolution consequently solves a closed finite linear ODE on W_N. Since the initial ACUE and CUE vectors agree, their expectations agree there for every t≥0. CUE stationarity makes their common value the original CUE value:

\[
\mathbb E_{\rm ACUE}[F(\Theta_t)]
=\mathbb E_{\rm CUE}F\qquad(F\in W_N, t\ge0).
\tag{21}
\]

This proof uses the existing exact ACUE/CUE initial Gram identity, plus the explicitly checked generator closure. It is not a new assertion that all observables are protected. Local sub-half-gap indicators lie outside this polynomial sector. At finite N, positive-time nondegenerate DBM can reach an open collision-free set with a sub-half gap. One may choose an ordered continuous path to such a set staying a positive distance from collisions; on a tube around this path the drift is smooth and bounded and the noise is nondegenerate. The usual Brownian support argument then gives positive probability. Thus sub-half gaps can be created from ACUE-supported initial data while retaining all identities (21). This qualitative finite-N statement does not assert a uniform microscopic-time lower probability as N grows.

It follows that adding stochastic smoothing, invoking a DBM universality theorem, and then pointing to unchanged protected moments cannot justify undoing the smoothing. The omitted observables are exactly where the half-grid alternative can change.

### 7. An explicit stochastic-removal obligation, not an automatic transfer

For a finite circular model let D_t=exp(tL) and P_t=exp(t(L+Delta)). On the invariant trace-polynomial spaces, differentiation gives the exact Duhamel identity

\[
P_tF-D_tF=\int_0^t P_u\Delta D_{t-u}F\,du.
\tag{22}
\]

For more singular gap or resolvent tests, establish a regularized domain and the corresponding bounds before using the same formula. A proposed comparison of a height-averaged zeta ensemble to a noise-regularized ensemble must control the analogue of the right side for the **specific statistics outside the protected sector**. It cannot discard Delta because the external field has a small derivative or because the original data are deterministic.

The natural missing estimate is thus not another low-band moment match. It is a quantitative bound on stochastic smoothing/removal, or a direct arithmetic evaluation of a discriminating statistic such as the test in (15), with an error smaller than its explicit sine-versus-half-grid discrepancy. Proving that estimate is substantial new arithmetic work. Treating it as an assumption inside a proposed universality argument would assume the unresolved comparison rather than solve it.

For true H_t, remote-field randomness may produce a random common translation; (7) shows why its effect on a fixed core becomes almost common when the cutoff is remote. Such a translation does not provide independent relative-particle diffusion. This observation does not exclude every possible homogenization mechanism from a more elaborate arithmetic environment, but any such mechanism would need its own covariance and error theorem. The present localization argument supplies none.

### 8. Failed arguments retained for the next researcher

1. **Discarding remote zeros after a Taylor estimate at the center:** fails at the retained block's boundary; the error must be propagated as in (B).
2. **Using static Riemann–von Mangoldt bounds throughout a positive-time interval:** requires an additional uniform H_t counting estimate with its stated time range.
3. **Replacing deterministic heat by DBM once the drift is similar:** fails by the exact microscopic generator discrepancy (19).
4. **Expecting deterministic local relaxation to select sine_2:** fails for the explicit alternating-half-grid family, which relaxes to a clock and preserves a half hard core.
5. **Using protected-moment equality to undo DBM smoothing:** fails because that entire filtration stays equal throughout the smoothing, while the unprotected gap support changes.
6. **Inferring typical-ACUE or actual-zeta conclusions from the constructed family:** would confuse a pathwise counterexample to insufficient hypotheses with an ensemble or arithmetic theorem. No such conclusion is made.

The rigorous gain from this round is a correctly normalized forward comparison framework and a sharp obstruction to the proposed transfer. The arithmetic programme should now target a discriminating observable and the actual prime-side accuracy it requires, rather than seek more drift-only analogies.

### 9. Bounded checks and reproducibility

The standalone forward_flow_checks.py uses only the Python standard library and writes forward_flow_checks.json. It performs no true-zeta heat simulation. Completed checks were:

- 200 exact rational tests of the interaction difference identity and its maximum-principle sign, with nonuniform gaps and a decreasing external field.
- 81 exact rational tests of the remote-field constant and affine remainder bounds.
- Float64 evaluation of the explicit two-periodic solution at N=4,8,16,32,64 and five microscopic times, compared with the full cotangent force. The maximum relative discrepancy was below 4.30×10^(−13). This is a numerical normalization check accompanying the explicit proof, not its replacement.
- Exact rational microscopic-generator constants for m=N/2 and 576 integer checks of the signed Fourier-weight filtration.

For example the alternating small gap is 0.5 at time zero, approximately 0.557329 at microscopic time 0.01, 0.830217 at time 0.1, and 0.999977 at time 1. It approaches a clock rather than creating the small gaps required by the sine-kernel pair law. The explicit lower discrepancy in (15) is approximately 0.18943053.

Run the checks with:

    python3 forward_flow_checks.py

The script's empirical parts are labelled float64; the other checks use exact fractions or integers. No Claude call, paid model API, repository operation or PDF work was performed in this round.


<a id="report-14"></a>

# Current report 14: Arithmetic transfer for a fixed large-prime sector

**Collection:** R7 — actual-zeta targets, arithmetic mark, and flow obstruction.

**Source:** [research/dyson/round7/arithmetic-resonator/DERIVATION.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/arithmetic-resonator/DERIVATION.md).

**SHA-256:** `3ab12c7227f0c41aaf78aab733f0353c054973cfe599f7b9275e47b12e8ee1f5`. **Git blob:** `0bbf469ec5685bfb4972908b58a2238b22ef4c91`. **Original bytes:** 9456.

## Arithmetic transfer for a fixed large-prime sector

**Status:** ordinary proof extension of the fixed symmetric-prime transfer argument, plus deterministic numerical implementation. The fixed-family transfer has received a separate [independent internal review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/arithmetic-resonator/INDEPENDENT_REVIEW.md), including its truncations and insertion terms. This is not formal verification or external peer review. Its numerical experiment remains negative.

### 1. Fixed family and normalization

Fix ell>=1, a=ell^2, and the multiplicative coefficients

    d_ell(p^e)=(ell)_e/e!.

For n<=L set

    v_n=log(n)/log(L),
    S_k(n)=sum_(p|n, distinct) (log(p)/log(L))^k,  k>=2,
    C_L(n)=sum_(p|n) 1_(p>sqrt(L)).

Since n<=L, C_L(n) is exactly zero or one. A repeated prime p>sqrt(L) cannot divide n. Thus C^2=C without approximation. We allow a fixed polynomial

    H(v,S,C)=F(v,S)+C J(v,S),

where S denotes finitely many S_k. Fixed radial Legendre polynomials are included in this class. All variables satisfy 0<=v<=1, 0<=S_k<=1 and C in {0,1}, so H is uniformly bounded. Its coefficients do not vary with L.

The resonator coefficients and creation matrix are

    r_L(n)=d_ell(n) H(v_n,S(n),C_L(n)),
    x_n=r_L(n)/sqrt(n),
    (A_L)_(p^e m,m)=2 sin(pi e log(p)/(2log(L)))/(e sqrt(p^e)).

The normalized half-gap main term is

    Q_L = [||A_L x||^2 + x^T A_L^2 x]/[2 pi^2 ||x||^2] - 1/4.

The target is a *positive limiting value*, not a finite-L value or a positive coefficient in one summand.

### 2. General unmarked moments

For a list of labeled positive integers I=(k_1,...,k_j), write K=sum I. The existing marked-prime expansion gives

    E_v product_i S_(k_i) = v^K m_I(a),

where

    m_I(a) = [sum_(set partitions pi of {1,...,j})
                  a^(number of blocks) product_(B in pi) Gamma(sum_(i in B) k_i)]
             / (a)_K,
    m_empty(a)=1.

This follows directly by grouping equal marked primes in the product and integrating the distinct-prime logarithmic sizes. It is not an assumption of an asymptotic Poisson-Dirichlet model. The same formula may of course be interpreted using that probability distribution.

For completeness, the unmarked positive measure is

    (log L)^(-a) sum_(n>=1) d_ell(n)^2/n delta_(log(n)/log(L)),

on all n>=1. Its Laplace transform tends to C_ell t^(-a), giving local weak convergence to

    C_ell/Gamma(a) * v^(a-1) dv.

The full measure is first treated on compact logarithmic intervals, and then restricted to v<=1; it is not truncated at n=L before taking its Laplace transform. The independent review gives the explicit short-background limiting procedure.

To derive the displayed product moment, restrict every marked prime to p>=L^epsilon, apply the prime number theorem to the finitely many reciprocal-prime measures, and use the unmarked weak limit for the remaining factor. Background collisions and coincident distinct marks have an extra reciprocal prime and vanish. At n<=L,

    sum_(p|n,p<L^epsilon) (log(p)/log(L))^k <= epsilon^(k-1),

so deleting the small marked primes changes any fixed polynomial in the S_k by O_H(epsilon). First let L tend to infinity with epsilon fixed, then let epsilon tend to zero. The joint limiting densities assign zero mass to simplex cutoff boundaries. This is the same finite-mark argument as the previously reviewed S2 transfer, now with a finite general list of k>=2; it needs no uniform pointwise asymptotic at each individual prime tuple.

### 3. The new large-prime marked moment: an exact integer decomposition

There is an especially simple exact starting identity. If C_L(n)=1, then uniquely

    n=p m, p>sqrt(L), m<=L/p<p.

Hence p and m are coprime, p occurs exactly once, and

    d_ell(pm)^2 = a d_ell(m)^2,
    S_k(pm)=S_k(m)+u_p^k.

For every test function Phi on the displayed variables, exactly

    sum_(n<=L) d_ell(n)^2/n * C_L(n) Phi(v_n,S(n))
      = a sum_(p>sqrt(L),p<=L) 1/p
          sum_(m<=L/p) d_ell(m)^2/m
            Phi(v_m+u_p, S(m)+(u_p^k)_k).

There is no coprimality error in this decomposition: m<p makes it automatic. The prime variable stays in the compact logarithmic interval (1/2,1], so its limiting measure is dt/t by the prime number theorem. Combine this with the unmarked and finitely marked background weak limits from Section 2. The boundaries t=1/2 and t+w=1 have zero limiting measure. The potentially short background is included in that weak convergence; it is not replaced by an unjustified uniform asymptotic in m.

At fixed total v<=1, the resulting moment is zero for v<=1/2. For v>1/2 it is

    E_v[C product_(i in I) S_(k_i)]
      = a v^(1-a) sum_(A subset of the labeled index set I) m_(I\A)(a)
          integral_(1/2)^v
            t^(sum_(i in A) k_i - 1)
            (v-t)^(a-1+sum_(i notin A) k_i) dt.

Repeated entries of I are still labeled in this subset sum, so their binomial multiplicities are retained. Every product involving C^r, r>=1, uses this same moment because C^2=C. The formula therefore evaluates all norm and insertion moments of the fixed family F+CJ.

An independent internal reviewer checked this formula and uniqueness at the half threshold. The exact integer decomposition above provides its arithmetic justification independently of any probability-model interpretation.

### 4. Insertion rules and the two distinct diagonal mechanisms

Put chi(u)=1_(u>1/2). On the simplex v+u+w<=1, define

    H0  = H(v,     S,                  C),
    Hu  = H(v+u,   S+(u^k)_k,          C+chi(u)),
    Hw  = H(v+w,   S+(w^k)_k,          C+chi(w)),
    Huw = H(v+u+w, S+(u^k+w^k)_k,      C+chi(u)+chi(w)).

At most one of the background and inserted primes can exceed the half threshold. These are precisely the changes of the distinct-prime statistic away from the already negligible operator/background coincidences.

The limiting forms are

    I = integral_0^1 v^(a-1) E_v[H0^2] dv,

    M2 = (2 ell^2/pi^2) integral_(v+u+w<=1)
           v^(a-1) sin(pi u/2)/u * sin(pi w/2)/w
           E_v[H0 Huw + Hu Hw] dv du dw,

    M3 = (2/pi^2) integral_(v+u<=1)
           v^(a-1) sin^2(pi u/2)/u * E_v[H0^2] dv du.

With I>0,

    Q_L -> (M2+M3)/I - 1/4.

To check the normalization and indexing, first restrict A_L to prime multipliers p>=L^epsilon. Then

    ||A x||^2 = sum_(n<=L) 1/n sum_(p,q|n) alpha_p alpha_q
                     r_L(n/p) r_L(n/q),

    x^T A^2 x = sum_(mpq<=L) alpha_p alpha_q/(mpq)
                     r_L(m) r_L(mpq),

with alpha_p=2 sin(pi log(p)/(2log L)). The ordered distinct-prime terms give the two displayed M2 products, with no additional factor of two.

The p=q terms in A^*A have n=mp and contain r_L(m)^2. They survive and give M3 with **H0 squared**, not an inserted H_u. Conversely, p=q in A^2 costs p^(-2); its retained-prime contribution vanishes. This distinction is unchanged by adding the large-prime mark and is implemented explicitly.

The uniform operator truncation estimates from the previous transfer proof apply to every vector x:

    ||A_L||=O_ell(1),
    ||A_(p<L^epsilon)||=O_ell(sqrt(epsilon)+1/sqrt(log L)),
    ||A_(prime powers e>=2)||=O_ell(1/sqrt(log L)).

They follow by the positive Schur weight d_ell(n)/sqrt(n), the logarithmic-derivative divisor identity and submultiplicativity for ell>=1. They do not require H to be nonnegative or continuous as a function of a mark. After these truncations, coincidences are negligible by the same reciprocal-square bounds and uniform boundedness of H. Every remaining discontinuity is at a fixed prime-size threshold with zero limiting mass. This completes the extension of the fixed-family arithmetic limit.

### 5. Interface with actual zeta zeros

The source is [Inoue, arXiv:2604.05733v1, Theorems 3 and 4](https://arxiv.org/html/2604.05733v1#S3). The paper's theorem assumes RH and permits arbitrary resonator coefficients subject to its product cutoff. Use L=floor(T/(log T)^2), so theta=log L/log T tends to one; the same Schur comparison controls replacement of theta by one in the sine kernel. No finite integer table is used as a substitute for that limit.

A fixed strictly positive limiting margin at phi=1/2 would make a half-gap improvement a meaningful next consequence after handling the source's continuity and error terms. This trial's margin is negative, so there is no new zero-spacing theorem. Even a successful small-gap statement must preserve the distinction between zeros counted with multiplicity and a gap interval separated from zero; it cannot automatically refute every half-lattice formulation of the Alternative Hypothesis.

### 6. Numerical quadrature adapted to the discontinuity

The unmarked block is the ordinary smooth simplex integral. For every block with at least one C factor, the M2 integrand is supported only in three disjoint sectors:

1. v>1/2: the background can contain the unique large prime; u,w<1/2 automatically.
2. u>1/2: the inserted u-prime is large, and v,w<1/2.
3. w>1/2: the symmetric inserted-prime sector.

In the first sector the marked moment factors as `(v-1/2)^a` times a smooth function, so a Jacobi rule absorbs that factor. The other two sectors use the usual v^(a-1) Jacobi weight and smooth triangular substitutions. No quadrature cell crosses a step in chi. M3's marked block only uses the first, background sector.

This is why the order-20, order-28 and order-40 calculations are stable without a dense multidimensional mesh. Their agreement is a useful independent numerical check, not a rigorous error enclosure.


<a id="report-15"></a>

# Current report 15: Round 7: an arithmetic large-prime sector for zeta's half-gap problem

**Collection:** R7 — actual-zeta targets, arithmetic mark, and flow obstruction.

**Source:** [research/dyson/round7/arithmetic-resonator/REPORT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/arithmetic-resonator/REPORT.md).

**SHA-256:** `a1ad13dac36a646c82c857c771fa4c9c9b0e42aa5daa9d4c964361aebf7e2983`. **Git blob:** `a3454c2ecb27cfd7c84699a55e8c1f9a97320ad4`. **Original bytes:** 11454.

## Round 7: an arithmetic large-prime sector for zeta's half-gap problem

**Result:** a fixed, discontinuous arithmetic feature beyond every finite polynomial in the old power sums was added and tested. The enlarged resonator's limiting half-gap margin is numerically approximately **-0.01465492379421**. The added feature improves the matched baseline by only **1.429e-8**, so this concrete route does not cross the half-gap threshold. Three quadrature orders agree to about 1.4e-15, and direct evaluation of a frozen rational coefficient vector on actual integers is also negative.

The useful output is the explicit large-prime-sector arithmetic transfer, its mixed insertion formulas, a complete rational test vector, and a bounded negative decision. This is not a new theorem about zeta zeros or an impossibility theorem for the full resonance-correlation method.

### 1. Why this family was selected

The initial suggestion to add S3 or S2^2 was corrected after checking the existing archive. Round 1 had already tested these features, and a 48-term, twelve-group power-sum family had reached approximately -0.01465472564383. Repeating that sweep would not be a new research direction. That old number remains slightly better than the new trial below; differences in the finite spans and ell values must not be concealed.

The genuinely new mark is

    C_L(n) = 1_(there is a prime p|n with p>sqrt(L)).

For n<=L it is a binary mark. It cuts the prime-factor configurations into a large-prime sector and its complement. This sharp fixed threshold is not represented by a finite polynomial in S2,S3,..., although sufficiently large polynomial spaces could approximate it in a suitable mass norm.

The exact identity n=pm with p>sqrt(L), m<p gives a simple arithmetic proof route, rather than an unsupported identification with a limiting Fock operator. No physical prime-gap k39 matrices, heat-flow matrices, or model-only random-matrix distribution were used in this computation.

### 2. The precise 30-dimensional experiment

Fix ell=27/25 and a=729/625. Use the coefficient family

    r_L(n)=d_ell(n) H(v_n,S2(n),S3(n),C_L(n)),

with v_n=log(n)/log(L) and the same distinct-prime power sums as the previous arithmetic transfer proof.

The matched unmarked space has twenty features:

    {1,S2,S3,S2^2} times Legendre_d(2v-1), 0<=d<=4.

The enlarged space adds ten features:

    C times {1,S2} times Legendre_d(4v-3), 0<=d<=4.

The second radial basis is centered on the marked support 1/2<v<=1, avoiding needless conditioning loss from monomials on a short interval. This is only a basis choice: it does not restrict the five radial degrees available in either marked group.

All thirty coefficients are optimized together at the one fixed ell. There is no ell scan, threshold scan, degree scan, or new eigenvalue scan of the full integer operator. The basis and threshold remain fixed as L tends to infinity.

### 3. Arithmetic derivation and its review status

[DERIVATION.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/arithmetic-resonator/DERIVATION.md) gives the ordinary proof extension in full. The main new identity is

    E_v[C product S_(k_i)]
      = a v^(1-a) sum_(A subset of labeled factors) m_(I\A)(a)
          integral_(1/2)^v t^(sum_A k_i-1)
             (v-t)^(a-1+sum_(I\A) k_i) dt,

with zero value when v<=1/2. It follows from an exact unique-large-prime integer decomposition and the prime number theorem, together with the already established finite marked-prime moments. The background factor is automatically coprime to the large prime. A fixed threshold's boundary has zero limiting measure.

The insertion changes are C -> C+1_(u>1/2). The off-diagonal M2 terms use H0 Huw and Hu Hw. The same-prime A^*A term survives as M3 with H0^2; it must not be given an inserted mark. The repeated-prime A^2 term vanishes after the usual truncations. The previous weighted Schur estimates are valid for arbitrary signed coefficient vectors and remove small-prime/prime-power operator pieces without assuming a positive H.

The full fixed-family transfer now has a separate [independent internal review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/arithmetic-resonator/INDEPENDENT_REVIEW.md), including the short background, fixed-threshold boundary and signed-vector truncations. This is not formal verification or external peer review. Numerical agreement is not used as a substitute for the proof review. The source interface remains [Inoue's RH-conditional resonance-correlation theorem](https://arxiv.org/html/2604.05733v1#S3), with its stated product cutoff and error terms.

### 4. Limiting-form numerical results

The quantity displayed is

    margin = (M2+M3)/I - 1/4,

with the normalization fixed in DERIVATION.md. A positive number is required for the intended half-gap attack.

| quadrature order | 20-dimensional baseline | enlarged 30-dimensional family |
|---:|---:|---:|
| 20 | -.0146549380840022 | -.0146549237942085 |
| 28 | -.0146549380840022 | -.0146549237942086 |
| 40 | -.0146549380840038 | -.0146549237942099 |

The order-40 scaled mass-Gram condition numbers are approximately 5.17e7 for the baseline and 1.20e8 for the enlarged family. Every direction survives the stated relative eigenvalue cutoff. The enlarged pencil's residual norm is near 2e-16. These are diagnostics for floating matrices; they do not certify integration or eigenvalue errors.

The quadrature is specifically split at the mark discontinuities. Marked M2 blocks are supported only in three disjoint sectors: a background total greater than 1/2, an inserted u greater than 1/2, or an inserted w greater than 1/2. The background-sector Jacobi weight absorbs the exact (v-1/2)^a endpoint factor. Consequently no integration cell crosses an unresolved step in the mark.

The enlarged value is still about .01465 below zero, vastly larger than the tiny observed gain. It is therefore a useful negative test of this particular sector feature, not evidence of a new record. Nor does it rule out other thresholds, richer occupation functions, or an altogether different resonator.

### 5. Complete frozen rational vector

The order-40 optimizing coefficients were rounded to denominator 100,000,000 and then evaluated again as one fixed vector. In each row below the five integers multiply the radial Legendre degrees 0,1,2,3,4. The first four rows use Legendre_d(2v-1); the last two use Legendre_d(4v-3). Divide every integer by 100,000,000.

| factor | five coefficient numerators |
|---|---|
| 1 | -117846152, 38918251, 1078497, -33600, 411449 |
| S2 | 46899554, -54583075, 43523183, -40218573, 12782032 |
| S3 | 295982141, -383374116, 290083532, -105264757, 17704774 |
| S2^2 | -109987670, 186525942, -226829807, 150959435, -47011938 |
| C | 87192, -72400, 513184, -115799, -690461 |
| C S2 | -361789, 437850, -2512958, 557662, 2084511 |

Its quadrature norm is `1.0000000030188823` and margin is `-0.014654923794209879`. Rational coefficients do not make the integral evaluation an interval certificate. `fixed_rational_vector.json` stores the exact integers, basis labels and denominator so that no coefficient must be reconstructed from a screenshot or rounded prose.

### 6. Direct finite-integer check

The same frozen rational vector was evaluated on actual integers, using the full finite prime-power creation matrix

    A_(p^e m,m)=2 sin(pi log(p^e)/(2log L))/(e sqrt(p^e)).

These are direct Rayleigh evaluations, not optimized eigenvalues. The distinct-prime mark is tested by the exact integer comparison p*p>L. The divisor coefficients include all prime exponents, and the finite operator includes all prime-power multipliers.

| L | ||Ax||^2/||x||^2 | x^T A^2 x/||x||^2 | finite margin |
|---:|---:|---:|---:|
| 10,000 | 2.98343331577942 | 1.10733089333213 | -.04275946416555 |
| 100,000 | 3.02158248945693 | 1.17479313763796 | -.03740912722744 |
| 1,000,000 | 3.04668220745756 | 1.22147565861788 | -.03377259651844 |

The finite evaluations set theta=log L/log T to its limiting value one. They do not assert that a literal finite T already satisfies that equality under the source cutoff. Their slow approach toward a limiting form is not extrapolated to an asymptotic certificate. These data concern resonator coefficients and the arithmetic operator; they are not measurements of actual zeta zeros.

### 7. Independent numerical checks

`validate_sector.py` performs checks that use different formulas or representations:

- The unmarked Gram and numerator blocks are compared with the previous independent monomial implementation after an explicit Legendre-to-monomial change of basis. Maximum absolute discrepancies are about 1.92e-13 and 9.07e-13.
- At a=1, the marked moments are checked against closed formulas `E_v C=log(2v)` and `E_v(C S2)=.75(v^2-.25)-v(v-.5)+.5v^2 log(2v)`.
- For noninteger a=729/625, direct integration in the marked-prime variable t is compared with the implemented scaled Jacobi formula, including repeated labeled factors S2^2 and S2^3. Observed differences are at most about 1e-15.
- The sampled marked moments satisfy 0<=E(C product S_k)<=E(product S_k), and three quadrature orders give an enlarged-margin spread of 1.36e-15.
- The finite integer construction asserts C in {0,1} for every integer evaluated.

The numerical integration routines' reported errors and matrix residuals are not outward enclosures. The report deliberately distinguishes the ordinary arithmetic derivation, the finite matrix model, the numerical tests, and the actual zeta theorem.

### 8. Files and reproduction

All new files are confined to this directory. No Git operation, Claude call, paid API, prime-gap matrix run, or PDF build was used.

```sh
OPENBLAS_NUM_THREADS=1 python3 large_prime_sector.py --order 20
OPENBLAS_NUM_THREADS=1 python3 large_prime_sector.py --order 28
OPENBLAS_NUM_THREADS=1 python3 large_prime_sector.py --order 40
OPENBLAS_NUM_THREADS=1 python3 finite_integer_check.py
OPENBLAS_NUM_THREADS=1 python3 validate_sector.py
```

`large_prime_sector.py` is self-contained apart from NumPy/SciPy. Each quadrature order has JSON containing every coefficient, basis label, Gram spectrum and diagnostic, plus an NPZ with the full numerator and mass matrices. `finite_integer_check.py` records the frozen rational vector and the actual integer values. `validate_sector.py` uses the older `general_prime_features.py` only for its independent unmarked normalization comparison; its SHA is pinned in `validation.json`. The validation script's input location is the existing common BASE layout.

`DERIVATION.md` supplies all additional marked moments and insertion rules. `manifest.json` pins the new code/data and environment. The normal public export is small; no large eigenvector or omitted private service is required.

### 9. Decision and remaining work

This fixed half-threshold sector is now a tested arithmetic family with a concrete transfer argument. Its tiny numerical improvement does not justify further tuning of the same degree-four coefficients. A materially different occupation structure or a new estimate connecting the resonator to arithmetic correlations remains necessary for a serious chance of crossing the half-gap threshold.

No implication for Montgomery-Dyson pair correlation or a refutation of general AH follows from this negative result. Even a future positive small-gap result would need care about multiplicity and the zero atom allowed in some AH formulations. The current run ends with this specific negative decision and preserves all formulas and coefficients for independent review.


<a id="report-16"></a>

# Current report 16: Independent audit of the half-threshold arithmetic transfer

**Collection:** R7 — actual-zeta targets, arithmetic mark, and flow obstruction.

**Source:** [research/dyson/round7/arithmetic-resonator/INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/arithmetic-resonator/INDEPENDENT_REVIEW.md).

**SHA-256:** `b18387755f10dfdb1bb86e9fe755ecd778fb10b71f3b46ea7b6dec987264a3cb`. **Git blob:** `41815e70565aff8ee0f0a648bd68124ceb226f4f`. **Original bytes:** 15802.

## Independent audit of the half-threshold arithmetic transfer

Date: 2026-09-05. Reviewer: the separate `yau_flow` research agent.

**Verdict:** the fixed-family arithmetic limit in `DERIVATION.md` is accepted as an ordinary mathematical argument, with the full-measure clarification and explicit limiting procedure below. I found no missing large-prime sector, extra factor of two, erroneous same-prime insertion, or unjustified extension of the Schur estimate to signed coefficients. This is independent internal review, not formal verification or external peer review. It does not certify the floating numerical optimum or prove a zero-spacing result.

I read the complete derivation, report, `large_prime_sector.py`, `finite_integer_check.py`, and the preceding `symmetric_prime_arithmetic_transfer.md`, including its explicit collision and operator-error estimates. I also checked the primary source's Theorems 3 and 4. The filename `threshold_model.py` in the review request is stale; the implementation in this checkpoint is `large_prime_sector.py`.

### 1. Precise scope of the accepted statement

Fix \(\ell\geq1\), \(a=\ell^2\), and one real polynomial
\[
H(v,S,C)=F(v,S)+C J(v,S),
\]
where only finitely many distinct-prime power sums \(S_k\), with \(k\geq2\), occur. The polynomial, its degree, its coefficients, and the threshold \(1/2\) remain fixed as \(L\to\infty\). With \(I>0\), the proposed arithmetic quotient converges to
\[
\frac{M_2+M_3}{I}-\frac14.
\]
The statement is unconditional as an assertion about weighted integer sums and the specified finite arithmetic matrices. RH enters only in its separate application to the zeta theorem. No uniformity in a growing basis, a moving threshold, \(\ell\), or optimizing coefficients depending on \(L\) has been proved. The frozen rational coefficient vector is within the accepted fixed-family scope.

### 2. Exact large-prime decomposition and mixed moments

For \(n\leq L\), two distinct prime divisors greater than \(\sqrt L\) are impossible, as is the square of such a prime. Thus
\[
C_L(n)=\mathbf1_{P^+(n)>\sqrt L}\in\{0,1\},
\]
where \(C_L(1)=0\). If this mark is one, there is exactly one decomposition \(n=pm\) with \(p>\sqrt L\), and \(m\leq L/p<p\). Consequently the coprimality in this decomposition is exact, not asymptotic:
\[
d_\ell(pm)^2=a d_\ell(m)^2,
\qquad S_k(pm)=S_k(m)+u_p^k.
\]
The identity in DERIVATION §3 therefore holds for every test function for which its finite sums are defined. No prime-density approximation is involved at this stage.

The unmarked moment for a labeled list \(I=(k_1,\ldots,k_j)\), of total weight \(K\), is
\[
m_I(a)=\frac{1}{(a)_K}
 \sum_{\pi}a^{|\pi|}\prod_{B\in\pi}\Gamma\!\left(\sum_{i\in B}k_i\right).
\]
Each block denotes one distinct prime shared by precisely those marks. The factor \(\Gamma(\sum_B k_i)\), rather than \(\Gamma(1+\sum_B k_i)\), is correct because the prime-size measure is \(du/u\). There is no factorial for ordering blocks: each labeled set partition appears once. In particular,
\[
m_{(2)}=\frac1{a+1},\quad
m_{(3)}=\frac2{(a+1)(a+2)},\quad
m_{(2,2)}=\frac{a+6}{(a+1)(a+2)(a+3)}.
\]

Disintegrating the exact large-prime identity by total size \(v\), and dividing by the unmarked density \(v^{a-1}\), gives
\[
\mathbb E_v\!\left[C\prod_{i\in I}S_{k_i}\right]
=a v^{1-a}\sum_{A\subseteq I}m_{I\setminus A}(a)
\int_{1/2}^{v}t^{\sum_{i\in A}k_i-1}
 (v-t)^{a-1+\sum_{i\notin A}k_i}\,dt
\]
for \(v>1/2\), and zero otherwise. The subset notation is over labeled positions. For example, the \(C S_2^2\) integrand has exactly the three contributions
\[
t^3(v-t)^{a-1}
 +2m_{(2)}t(v-t)^{a+1}
 +m_{(2,2)}t^{-1}(v-t)^{a+3}.
\]
The middle factor two is necessary and is retained by the implementation's bit-subset expansion. All higher powers of \(C\) reduce to the same marked moment. These formulas check for the mixed \(S_2,S_3\) features and their products appearing in both numerator and norm.

### 3. Measure convergence, discontinuities, and short backgrounds

One wording clarification is needed in DERIVATION §2: the measure whose Laplace transform tends to \(C_\ell t^{-a}\) must be
\[
\nu_L=(\log L)^{-a}\sum_{n\geq1}\frac{d_\ell(n)^2}{n}
 \delta_{\log n/\log L},
\]
with the sum over **all** positive integers. The measure truncated to \(n\leq L\) does not have that Laplace transform. The preceding transfer proof correctly uses the full measure and then restricts to compact intervals, so this is a clarification of the new note's abbreviated notation, not a failure of its argument.

The full positive measures converge locally to
\[
\nu(dv)=\frac{C_\ell}{\Gamma(a)}v^{a-1}\,dv.
\]
The Laplace bound also gives uniformly bounded mass on \([0,1]\). This supplies all total-mass control needed here. To make the new limit argument explicit:

1. Fix \(\varepsilon>0\), and restrict the finitely many ordinary marked primes and operator primes to \(p\geq L^\varepsilon\). The threshold prime already lies in \((L^{1/2},L]\).
2. Expand a fixed polynomial into finitely many labeled-prime terms. After discarding coincidences as below, each is a product of the background measure and finitely many reciprocal-prime measures on compact logarithmic intervals bounded away from zero. PNT and partial summation identify the latter as \(du/u\).
3. Take the product-measure weak limit, restricted by the relevant simplex. Its limiting measure is absolutely continuous in the continuous prime sizes and background size. The hyperplanes \(u=1/2\), \(w=1/2\), the large-prime threshold \(t=1/2\), and each total-size cutoff have zero mass. Bounded piecewise polynomial test functions are therefore legitimate.
4. Finally let \(\varepsilon\downarrow0\). For \(k\geq2\), deleting small ordinary marks changes \(S_k\) by at most \(\varepsilon^{k-1}\), uniformly for \(n\leq L\). Fixed polynomial products change by \(O_H(\varepsilon)\). The threshold mark is never deleted in this step.

This is not an appeal to pointwise uniform Selberg–Delange estimates at each prime tuple. For an explicit short-background check, after the prime cutoffs are fixed, the part with remaining background size \(v\leq\eta\) is bounded by a fixed constant depending on \(H,\ell,\varepsilon\) times \(\nu_L([0,\eta])\). For each fixed \(\eta>0\),
\[
\nu_L([0,\eta])\longrightarrow
\frac{C_\ell}{\Gamma(a+1)}\eta^a.
\]
Taking \(L\to\infty\), then \(\eta\downarrow0\), controls this portion. The background atom \(m=1\) has normalized mass \((\log L)^{-a}\to0\). The large-prime endpoint \(p\) near \(L\) causes no new atom or missing boundary term. These observations close the short-background and discontinuity obligations for this fixed family.

### 4. Coincidences and signed coefficient bounds

For \(\ell\geq1\), the decreasing ratios \((\ell+e)/(e+1)\) give
\[
d_\ell(p^{b+c})\leq d_\ell(p^b)d_\ell(p^c).
\]
In particular,
\[
\sum_{m\leq L:p\mid m}\frac{d_\ell(m)^2}{m}
\leq\frac{\ell^2}{p}\sum_{k\leq L}\frac{d_\ell(k)^2}{k}.
\]
An external reciprocal-prime factor then makes an operator/background coincidence cost \(p^{-2}\). At \(p\geq L^\varepsilon\), the sum of these costs is \(O(L^{-\varepsilon})\). Other retained prime measures have bounded mass for fixed \(\varepsilon\); using a weaker power of \(\log\log L\) bound would also suffice. There are only finitely many coincidence patterns.

The jump of \(C\) does not invalidate this estimate. A coincidence can change an amplitude discontinuously, but both amplitudes are bounded by a constant times \(d_\ell\); the contribution of the exceptional integer set still has the same vanishing upper bound. One does not need differentiability or positivity of \(H\).

### 5. Operator normalization and the two diagonal mechanisms

For the retained prime operator, put \(\alpha_p=2\sin(\pi u_p/2)\). Direct multiplication gives
\[
(Ax)_n=\frac1{\sqrt n}\sum_{p\mid n}\alpha_p r(n/p).
\]
Squaring this expression gives the stated ordered \((p,q)\) sum for \(A^*A\). Multiplying a second time gives the stated ordered sum for \(A^2\). For distinct primes coprime to the background, the coefficient factors are
\[
r(mp)r(mq)=\ell^2d(m)^2H_uH_w,
\quad r(m)r(mpq)=\ell^2d(m)^2H_0H_{uw}.
\]
The four sine factors from \(\alpha_p\alpha_q\), divided by \(2\pi^2\), give \(2\ell^2/\pi^2\). Both discrete and continuous prime pairs are ordered, so another factor of two would be an error.

For \(A^*A\), the same-prime term is exactly
\[
\sum_{mp\leq L}\frac{\alpha_p^2}{mp}r(m)^2.
\]
Its amplitude is evaluated at \(m\). Thus \(M_3\) uses \(H_0^2\), without adding the prime's mark, its power sums, or its size to \(H\). There is no extra \(\ell^2\) here. In contrast, the same-prime term in \(A^2\) contains \(p^{-2}\) and vanishes after the fixed lower prime cutoff. I independently checked this distinction directly from matrix multiplication; it is essential and correctly implemented.

The positive Schur weight \(d_\ell(n)/\sqrt n\) from the preceding proof gives the uniform operator bounds used in the new derivation. For \(A=A_0+E\),
\[
\|A^*A-A_0^*A_0\|,\ \|A^2-A_0^2\|
\leq(\|A\|+\|A_0\|)\|E\|.
\]
Thus the errors \(O_\ell(\sqrt\varepsilon+(\log L)^{-1/2})\) hold after division by \(\|x\|^2\), for every nonzero signed vector. The denominator's asymptotic follows separately from \(I>0\). No positivity or positive-semidefinite assumption on the entire numerator is being used.

### 6. Insertion sectors and implementation audit

On \(v+u+w\leq1\), at most one of the background's large prime, the inserted \(u\)-prime, and the inserted \(w\)-prime can exceed the global half threshold. Insertion must use \(\chi(u)=\mathbf1_{u>1/2}\), not a threshold relative to the new total size. The code uses the correct global threshold.

For two feature factors with inserted indicators \(d_l,d_r\), the code's marked product is the exact identity
\[
(C+d_l)(C+d_r)=C(1+d_l+d_r)+d_l d_r.
\]
The `expand` routine retains labeled multiplicities, including repeated \(S_2\) factors. The `partitions` routine may return equal-looking blocks when numerical labels repeat; their multiplicities correctly represent different partitions of the labeled positions.

For a matrix block containing at least one marked feature, the three integration domains are disjoint, up to zero-measure boundaries:

| Domain | Source of the possible mark | Treatment in the code |
|---|---|---|
| \(v>1/2\) | Background prime | Marked background moment; both inserted primes below half |
| \(u>1/2\) | First inserted prime | Background mark zero; explicit insertion indicator |
| \(w>1/2\) | Second inserted prime | Symmetric insertion sector |

The first domain contains configurations with and without a background large prime; the marked moment, rather than the condition \(v>1/2\) alone, supplies the correct weight. The code respects this distinction. \(M_3\)'s marked blocks use only the first domain because its amplitude is uninserted.

Writing \(\delta=v-1/2\) and \(t=v-\delta z\) in a marked moment extracts \(\delta^a\). The remaining integrand is smooth up to \(\delta=0\), since \(t\geq1/2\). Its background-size factor is \(z^{a-1}\), with additional integer powers of \(z\) for unassigned marks. The scaled Jacobi implementation is correct. The outer Gram factor is \((v-1/2)^a v^{a-1}\), and the marked \(M_2\) background domain has this factor times \((1-v)^2(1-x)\). In an inserted-prime domain, the Jacobian is \((1/2-v)^2(1-x)\). These are exactly the weights used by `forms()`.

The sine-kernel replacements using NumPy's normalized `sinc` also have the correct constants. Symmetrizing the final real matrix preserves its quadratic form. The finite-integer implementation uses distinct prime factors for the marks, the full divisor coefficients for prime powers, and the exact integer condition \(p^2>L\). I found no disagreement between the formulas and the inspected implementation.

### 7. Primary-source interface and the limits of the result

[Inoue, arXiv:2604.05733v1, Theorems 3 and 4](https://arxiv.org/html/2604.05733v1#S3) allow arbitrary arithmetic resonator coefficients under RH, with \(L\leq T/(\log T)^2\). Choosing the approximator equal to the logarithmic increment coefficients yields the specified two quadratic forms; at \(\phi=1/2\) the linear term cancels. The earlier Schur argument controls the remaining normalized errors and the replacement \(\log L/\log T\to1\). The new mark does not introduce a new source restriction.

This confirms the **interface**, not a favorable sign. A strictly positive limiting margin would still have to be exhibited, and a strict improvement below half would use continuity in \(\phi\) for a fixed vector. The present negative numerical trial proves neither a new zeta theorem nor a refutation of AH. A statement about zeros counted with multiplicity cannot silently become a statement about positive pair distances bounded away from zero.

### 8. What the numerical evidence does and does not establish

The reported values at quadrature orders 20, 28, and 40 are consistent with the inspected implementation and each other. I inspected the stored validation data but did **not** rerun the integrations, finite-\(L\) million-integer evaluations, or any eigenvalue optimization. No new scan was performed.

Agreement of quadrature orders is not an outward enclosure. A small pencil residual does not bound integration error. The scaled Gram condition number near \(1.2\times10^8\) must remain visible when interpreting extremely small improvements. The rational vector is genuinely fixed, but rational coefficients do not make its transcendental limiting integrals exact. Accordingly:

- Accepted: a numerically negative test of this particular 30-dimensional family, with all inputs preserved.
- Not established: a rigorous negative upper bound over the whole 30-dimensional space.
- Not established: a certified gain of \(1.429\times10^{-8}\), despite its stable floating estimate.
- Rejected as an inference: a structural impossibility theorem for larger occupation families or the full resonance-correlation method.

These are scope boundaries, not objections to the authors' present negative decision.

### 9. Independent exact checks and pinned evidence

`independent_identity_checks.py` is a separate, standard-library-only check at the single fixed cutoff \(L=120\), with \(\ell=27/25\). It uses exact integer and `Fraction` arithmetic. Rational formal prime labels and kernels replace logarithms and sines only to check their algebraic roles; this is expressly not an asymptotic or numerical-margin test. It checked all 120 integers, the 70 unique-large-prime pairs, 132 coprime ordered distinct-prime insertion triples, both exact quadratic-form expansions, the surviving uninserted diagonal, and all eight Boolean product assignments. Every assertion passed. The results are in `independent_identity_checks.json`.

Run the bounded algebra check with:

```sh
python3 independent_identity_checks.py
```

The reviewed author-file SHA-256 values are:

| File | SHA-256 |
|---|---|
| DERIVATION.md | `62970c91f2ff757eabc5d9a364d189fb7a42494c0f188713b2974003df4833b0` |
| REPORT.md | `439e08210143acf4adfae7918f8e8ca92e5ce6d66080ce8a8858cc62bbe35d06` |
| large_prime_sector.py | `255ad9a2f29e086eca01b3823bd9ece3ecbfa47b431259a6af3fee260c9afa8d` |
| finite_integer_check.py | `2126542d6b75822fb79e0910d43e4e5639be5455e079be3095c534c60a171295` |
| validate_sector.py | `72a286b477034a3f3aae63aeaba479d5de5640a1e13fe8043f37b3f918b07d26` |
| fixed_rational_vector.json | `1858e8c2ec1effa0f51e93ff28561057d1e1c5d8c9d9c08b50d099ab71e9943f` |
| validation.json | `cf8970966bcbdb9d65cde8043461466a9633c3ad74de624d2a84b1f7c2e0bc2a` |

No author file, source repository, or existing experiment output was modified. This review and its small algebra-check files are the only new outputs.


<a id="report-17"></a>

# Current report 17: Round 8: isolate the actual arithmetic remainder

**Collection:** R8 — short-prime projection and signed residual.

**Source:** [research/reports/dyson_round8.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/dyson_round8.md).

**SHA-256:** `111901c83af7481b414b9ef08728baf0fadbabc696a8e69f533b4a55c05a2cf6`. **Git blob:** `bcf9481b26ba287e04b0770c6842052fbe8dc851`. **Original bytes:** 6061.

## Round 8: isolate the actual arithmetic remainder

The two-scale target from [Round 7](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/dyson_round7.md) can be written as a computable short-prime main term plus one signed difference of residual energies. The residuals have an exact convergent representation using the same centered prime-counting error. This round proves that decomposition under RH and identifies why two tempting lower-bound arguments fail. **It does not prove the required residual inequality or refute AH-Pairs.**

### 1. A short-prime projection identity for actual zeta

Fix c>0 and put

\[
N=\left\lfloor\frac{T}{\log^6T}\right\rfloor,
\quad s_c(t)=\frac12+\frac c{\log T}+it,
\quad H_c(t)=-\frac{\zeta'}{\zeta}(s_c(t)),
\]
\[
P_c(t)=\sum_{n\le N}\Lambda(n)n^{-s_c(t)},
\qquad R_c(t)=H_c(t)-P_c(t).
\]

The [ordinary analytic proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/resolvent-arithmetic/SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md) establishes, under RH,

\[
\int_0^T|H_c(t)|^2dt
=T\sum_{n\le N}\frac{\Lambda(n)^2}{n^{1+2c/\log T}}
+\|R_c\|_{L^2(0,T)}^2+O_c(N\log^4T).
\tag{1}
\]

The mixed product is evaluated by a contour shift to the absolutely convergent Dirichlet-series half-plane. The contour avoids the pole at one; RH controls the shrinking horizontal distance from the zeros. The infinite right-line off-diagonal sum, the top edge and the initially removed short interval all receive explicit bounds. A finite-polynomial mean-value estimate and completion of the square give (1). Exact finite-height orthogonality is not assumed.

An [independent audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/resolvent-arithmetic/INDEPENDENT_IDENTITY_AUDIT.md) checks the contour orientation, diagonal coefficient, near-diagonal summation, infinite tail, T-dependent error and continuation signs. No novelty claim or proof-assistant certification accompanies this ordinary reduction.

### 2. The precise remaining inequality

For the Round 7 statistic

\[
W_T=\frac{2}{T\log^2T}
\left[\sinh(2)\|H_1\|_2^2-\sinh(1)\|H_{1/2}\|_2^2\right],
\]

(1) and PNT imply

\[
W_T=B+\mathcal E_T+o(1),
\quad B=2\int_0^1u[\sinh(2)e^{-2u}-\sinh(1)e^{-u}]du
=0.4560939793292317\ldots,
\]
\[
\mathcal E_T=\frac{2}{T\log^2T}
\left[\sinh(2)\|R_1\|_2^2-\sinh(1)\|R_{1/2}\|_2^2\right].
\]

Thus the sufficient AH-refutation target is precisely

\[
\boxed{\liminf_{T\to\infty}\mathcal E_T\ge\frac1{16}-B
=-0.3935939793292317\ldots.}
\tag{2}
\]

The positive short-prime main term does not prove (2). The residual combination is signed and of leading order. The sine prediction would make it about -0.3738225362077544, but that value has not been obtained for actual zeta.

### 3. The two residuals come from the same arithmetic function

Set E(x)=psi(x)-x with psi(N) including the atom at N. For Re(s)>1/2, s≠1, RH gives the exact identity

\[
-\frac{\zeta'}{\zeta}(s)-\sum_{n\le N}\Lambda(n)n^{-s}
=\frac{N^{1-s}}{s-1}-E(N)N^{-s}
+s\int_N^\infty E(x)x^{-s-1}dx.
\tag{3}
\]

The integral converges absolutely under RH. The formula is obtained in the original convergence half-plane and then continued; no unregularized critical-strip prime series is used. The pole and endpoint subtraction have fixed signs.

At the chosen cutoff, the pole term can be removed from the normalized residual energy using its L2 estimate and the pointwise RH bound already proved in the same argument. The normalized cross-term error is O_c(log^-3 T); the decomposition needs no stronger pair-correlation input. Writing e_N(v)=E(Ne^v)/(Ne^v)^(1/2), the remaining residual is

\[
N^{-c/\log T-it}\left[-e_N(0)+s_c(t)
\int_0^\infty e_N(v)e^{-(c/\log T)v-itv}dv\right].
\]

The two damping widths therefore act on one actual arithmetic function. This coupling is a concrete structure for the next estimate. Replacing the two energies by independent nonnegative variables loses that structure; assuming it forces (2) without a proof would also be an error.

Using only |E(x)|≪sqrt(x) log²(x) and absolute values gives a residual bound of order T log³(T) for a power-of-T cutoff. Its squared integral is far too large. This is a documented failure of that particular estimate, not a proof that RH or all analytic approaches are insufficient.

### 4. Positivity gives a valid weak bound, but cannot reach the target

The [bounded positivity note](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/spectral-positivity/POSITIVITY_OBLIGATION_NOTE.md) gives an explicit band-limited minorant, using the known interior Montgomery band and positivity of the pair measure. Its resulting exact expression is approximately -0.208674513 for W, far below 1/16. The minorant is optimal only within the one-parameter correction family written there. Its [independent review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/spectral-positivity/MINORANT_REVIEW.md) checks the Fourier support, endpoint pairing and realizable point-process obstruction.

The decisive obstruction remains the actual stationary half-grid determinantal process. It matches the known low band, satisfies the stated point-process positivity constraints, and attains W_AH<1/16. Thus neither generic positivity nor merely changing two smoothing widths supplies the required arithmetic input. The frequency weight changes sign above log(2 cosh 1); even a one-term positive-coefficient polynomial disproves a universal positive-coefficient quadratic-form claim.

### 5. Verification and next scope

The accompanying checks verify exact scalar enclosures, a finite-step integration-by-parts identity and an absolutely convergent comparison with zeta'/zeta. Low-height regularized-prime sums are explicitly labeled diagnostics. They are not evaluations of the large-T target, and no convergence rate in the critical strip is inferred from them. Intake hashes and an isolated integration replay preserve the received evidence.

The next mathematical obligation is (2), exploiting the common centered prime error in (3), or the alternative compact prime-covariance target in Round 7. Repeating a positive-coefficient argument, dropping the pole before bounding its cross term, and scanning generic random-matrix models are postponed. The famous conjecture remains open in this programme.


<a id="report-18"></a>

# Current report 18: The actual-zeta two-scale target: short-prime projection and a centered tail

**Collection:** R8 — short-prime projection and signed residual.

**Source:** [research/dyson/round8/resolvent-arithmetic/SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/resolvent-arithmetic/SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md).

**SHA-256:** `0067a1b0c7bd4f0b80ef89d6ac85eca1ae99e652375c08c41706ec1f1ddbe40e`. **Git blob:** `03cf06eaf07980d2bb1a04a4aa3fb41540c44fd4`. **Original bytes:** 14389.

## The actual-zeta two-scale target: short-prime projection and a centered tail

Date: 2026-09-05. Status: ordinary analytic identities and an explicit remaining inequality. The requested lower bound \(1/16\) is **not proved**. This note does not claim a new theorem about zeta zeros. Round 7 is unchanged.

The useful outcome is a precise arithmetic decomposition. The part supplied by short primes is positive and completely evaluable. The remaining term is one **signed difference of actual residual energies**, with an absolutely convergent representation involving ψ(x)−x under RH. Positivity of the von Mangoldt coefficients does not control that signed difference.

### 1. Definitions and the resulting obligation

Write

\[
s_c(t)=\frac12+\frac{c}{\log T}+it,
\qquad H_c(t)=-\frac{\zeta'}{\zeta}(s_c(t)),
\qquad I_T(c)=\int_0^T|H_c(t)|^2dt,
\]

where c>0 is fixed, and

\[
W_T=\frac2{T\log^2T}
\left(\sinh(2)I_T(1)-\sinh(1)I_T(1/2)\right).
\tag{1}
\]

Set \(N=\lfloor T/\log^6T\rfloor\), for sufficiently large T, and define the genuine finite polynomials

\[
P_c(t)=\sum_{n\le N}\frac{\Lambda(n)}{n^{s_c(t)}},
\qquad R_c(t)=H_c(t)-P_c(t).
\tag{2}
\]

Under RH, the contour calculation below proves

\[
\boxed{
W_T=B+\mathcal E_T+o(1),
\quad
\mathcal E_T=\frac2{T\log^2T}
\left(\sinh(2)\|R_1\|_2^2-
\sinh(1)\|R_{1/2}\|_2^2\right),}
\tag{3}
\]

where all norms are over [0,T] and

\[
\begin{aligned}
B&=2\int_0^1u\left(\sinh(2)e^{-2u}-\sinh(1)e^{-u}\right)du\\
&=\frac{e^2}{4}-e+\frac54+\frac1e
-\frac9{4e^2}+\frac3{4e^4}\\
&=0.4560939793292317215\ldots.
\end{aligned}
\tag{4}
\]

Thus the precise remaining task is

\[
\boxed{\liminf_{T\to\infty}\mathcal E_T
\ge\frac1{16}-B
=-0.3935939793292317215\ldots.}
\tag{5}
\]

By (3), (5) is equivalent to the requested lower bound for W_T. Equation (5) is not deduced here from RH. The existing Round 7 AH calculation gives a limiting W below 1/16, so treating (5) as a consequence of formal coefficient positivity would be circular progress.

### 2. An exact continuation from centered prime counting

Put \(E(x)=\psi(x)-x\), with \(\psi(x)=\sum_{n\le x}\Lambda(n)\). At an integer cutoff, ψ includes the atom at that integer. Assuming RH, the classical bound

\[
E(x)=O\!\left(x^{1/2}\log^2(2x)\right)
\tag{6}
\]

implies that, for every s with Re(s)>1/2 and s≠1,

\[
\boxed{-\frac{\zeta'}{\zeta}(s)
=\frac{s}{s-1}
+s\int_1^\infty E(x)x^{-s-1}dx.}
\tag{7}
\]

The integral in (7) is absolutely convergent. To prove it, first take Re(s)>1, use Stieltjes integration by parts in the absolutely convergent von Mangoldt series, and subtract the integral of x. Both sides then continue meromorphically to Re(s)>1/2. RH excludes logarithmic-derivative poles from this open region except the pole at s=1. The residue of the right side at s=1 is +1, as required for −ζ′/ζ. No critical-strip Dirichlet series has been expanded.

For any real X≥1, finite summation by parts gives

\[
\boxed{
-\frac{\zeta'}{\zeta}(s)
=\sum_{n\le X}\Lambda(n)n^{-s}
+\frac{X^{1-s}}{s-1}
-E(X)X^{-s}
+s\int_X^\infty E(x)x^{-s-1}dx.}
\tag{8}
\]

Consequently the residual in (2) is **exactly**

\[
R_c(t)=\frac{N^{1-s_c(t)}}{s_c(t)-1}
-E(N)N^{-s_c(t)}
+s_c(t)\int_N^\infty E(x)x^{-s_c(t)-1}dx.
\tag{9}
\]

The positive prime coefficients have therefore been replaced in the tail by a centered, signed arithmetic error. The pole term is part of the identity; it cannot be discarded before estimating it at the chosen scale.

Equivalently, for fixed Re(s)>1/2 and s≠1,

\[
-\frac{\zeta'}{\zeta}(s)
=\lim_{M\to\infty}\left(
\sum_{n\le M}\Lambda(n)n^{-s}
+\frac{M^{1-s}}{s-1}\right).
\tag{10}
\]

For a fixed T the convergence is uniform on the two compact vertical segments used in (1). It is not an assertion that the unregularized Dirichlet series converges there. The order of limits in (10), followed by any T asymptotic, must be retained unless a uniform remainder is proved.

### 3. A quantitative bound that exposes the limitation of pointwise RH

Write δ=Re(s)−1/2>0 and ℓ=log X, with X≥2. Formula (6) implies

\[
\left|-E(X)X^{-s}+s\int_X^\infty E(x)x^{-s-1}dx\right|
\ll X^{-\delta}\left[
(\ell+1)^2+|s|\left(
\frac{(\ell+1)^2}{\delta}
+\frac{2(\ell+1)}{\delta^2}
+\frac2{\delta^3}\right)\right].
\tag{11}
\]

This follows by integrating \(x^{-1-\delta}(\log x+1)^2\) explicitly; the implied constant is the one in (6), up to an absolute factor. At δ=c/log T, X=T^θ with fixed θ>0, and t≤T, (11) supplies only

\[
O_{c,\theta}(T\log^3T),
\tag{12}
\]

which is far larger than the natural mean-square scale. Integrating the square of this estimate gives O(T³ log⁶T), whereas (1) is normalized by T log²T. This explicitly identifies a failure of the **pointwise RH estimate used in (6)**, not a proof that every possible consequence of RH is insufficient.

Trying to repair this particular absolute-value bound by making \(X^{-\delta}\) as small as a negative power of T forces log X to be of order (log T)². Such a cutoff destroys the short-polynomial mean-value regime. It is not a support extension obtained for free.

### 4. The actual mixed-integral lemma

For fixed c>0, T sufficiently large, \(3\le N\le T\), and

\[
\sigma=\frac12+\frac c{\log T},\quad
P(t)=\sum_{n\le N}\Lambda(n)n^{-\sigma-it},\quad
D=\sum_{n\le N}\Lambda(n)^2n^{-2\sigma},
\]

assume σ≤3/4 and \(\beta=1+1/\log N\le2\). Under RH,

\[
\int_0^T\left(-\frac{\zeta'}{\zeta}(\sigma+it)\right)
\overline{P(t)}dt
=TD+O_c(N\log^3T).
\tag{13}
\]

This is a complex identity with a bounded complex error. In particular its real part has the same main term.

**Contour and pole control.** Use

\[
F(s)=\left(-\frac{\zeta'}{\zeta}(s)\right)
\sum_{n\le N}\Lambda(n)n^{s-2\sigma}
\tag{14}
\]

on the rectangle from σ+i to β+iT. On the left side the finite sum is exactly \(\overline{P(t)}\). The pole at s=1 is below the rectangle, and RH places every nontrivial zero strictly to its left. The standard local partial-fraction estimate for the logarithmic derivative, together with O(log T) zeros in a unit interval, gives

\[
\frac{\zeta'}{\zeta}(u+iT)=O_c(\log^2T)
\quad(\sigma\le u\le\beta).
\]

Also

\[
\left|\sum_{n\le N}\Lambda(n)n^{u-2\sigma+iT}\right|
\le\sum_{n\le N}\log n\,n^{\beta-2\sigma}
\le eN\log N.
\]

The top integral is therefore O_c(N log³T). On the compact bottom segment, RH and finiteness of the number of nearby zeros give the sufficient bound \(O_c(\log T)\) for the logarithmic derivative: its distance to any nontrivial zero is at least c/log T, and the pole at s=1 has height zero. The bottom integral is thus \(O_c(N\log N\log T)\). The same compact RH bound on the initially omitted left interval \(0\le t\le1\), together with \(\sum_{n\le N}\Lambda(n)n^{-\sigma}\ll\sqrt N\log N\), bounds that interval by \(O_c(\sqrt N\log N\log T)\). These errors are absorbed by \(O_c(N\log^3T)\). No assumption that T avoids a zero ordinate, and no separately verified low-zero table, is needed.

**The right line is an honest absolutely convergent series.** At Re(s)=β>1,

\[
-\frac{\zeta'}{\zeta}(s)=\sum_{m\ge2}\Lambda(m)m^{-s}.
\]

The m=n terms of the vertical integral give (T−1)D. The absolute value of all other integrated terms is at most twice

\[
\sum_{n\le N}\Lambda(n)n^{\beta-2\sigma}
\sum_{\substack{m\ge2\\m\ne n}}
\frac{\Lambda(m)m^{-\beta}}{|\log(m/n)|}.
\tag{15}
\]

For n/2≤m≤2n, m≠n, the inner sum is

\[
O\!\left(n^{1-\beta}\log^2(2N)\right),
\]

by Λ(m)≤log m and the harmonic sum over |m−n|. After the outer factor is applied, summing over n costs O(N log³N), because \(n^{1-2\sigma}\le1\).

Outside that range the denominator is at least log 2, and

\[
\sum_{m\ge2}(\log m)m^{-\beta}
\ll(\beta-1)^{-2}\ll\log^2N.
\]

The remaining outer sum is O(N log N), since \(n^{\beta-2\sigma}\le N^{1/\log N}=e\). Thus the infinite right-line off-diagonal sum is O(N log³N). This completes (13). Neither an unproved long-polynomial mean value nor a critical-strip Dirichlet expansion has been used.

### 5. Orthogonal decomposition to leading order

An elementary finite-polynomial mean-value bound gives

\[
\|P\|_2^2=TD+O(N\log^4T).
\tag{16}
\]

For completeness, bound each non-diagonal integral by \(2/|\log(m/n)|\), use \(|\log(m/n)|\ge|m-n|/N\), then \(2|a_ma_n|\le|a_m|^2+|a_n|^2\), and sum the resulting harmonic series. This gives O(N log N Σ|a_n|²). Here \(\sum|a_n|^2\le\sum_{n\le N}(\log n)^2/n=O(\log^3N)\), proving the stated error. Sharper standard mean-value estimates are unnecessary.

Combining (13) and (16) gives

\[
\boxed{I_T(c)=TD+\|R_c\|_2^2+O_c(N\log^4T).}
\tag{17}
\]

This is an asymptotic projection identity for these specific coefficients, not a claim that the finite functions \(n^{-it}\) are exactly orthogonal on [0,T]. In particular, the cross term \(\langle R_c,P_c\rangle\) is O_c(N log⁴T), rather than identically zero.

With \(N=\lfloor T/\log^6T\rfloor\), the error in (17), divided by T log²T, is O_c(log⁻⁴T). The prime number theorem and partial summation give

\[
\frac D{\log^2T}\longrightarrow\int_0^1u e^{-2cu}du.
\tag{18}
\]

One may obtain (18) from Σ_{n≤x}Λ(n)²∼x log x; the contribution of prime powers of exponent at least two is negligible. Equations (17)–(18) prove (3). All leading constants and both values of c use the same cutoff N.

### 6. What the residual condition measures

The pole term in (9) is individually negligible in the normalized L² scale at this N:

\[
\int_0^T\left|\frac{N^{1-s_c(t)}}{s_c(t)-1}\right|^2dt
\ll_c N^{1-2c/\log T}\ll_c N.
\tag{19}
\]

Its denominator has real part bounded away from zero for sufficiently large T. Dropping it from **the residual energy** also requires a bound on the other factor in the cross term. The same RH partial-fraction estimate used in Section 4 gives the sufficient pointwise bound \(H_c(t)=O_c(\log^2T)\) on [0,T]. Equation (16) also gives \(\|P_c\|_2^2=O_c(T\log^4T)\). Thus \(\|R_c\|_2^2=O_c(T\log^4T)\), and Cauchy–Schwarz with (19) bounds the change of residual energy, divided by T log²T, by

\[
O_c\!\left(\sqrt{\frac NT}+\frac{N}{T\log^2T}\right)
=O_c(\log^{-3}T)=o(1).
\]

This weaker estimate is sufficient and makes the removal independent of the sharper Round 7 pair/resolvent bound.

Accordingly (5) can also be stated with

\[
\widetilde R_c(t)=-E(N)N^{-s_c(t)}
+s_c(t)\int_N^\infty E(x)x^{-s_c(t)-1}dx
\tag{20}
\]

in place of R_c. This version pinpoints the missing arithmetic information: a comparison of two Laplace-damped Fourier energies of the **same centered prime error**.

More explicitly, put \(e_N(v)=E(Ne^v)/(Ne^v)^{1/2}\), v≥0, and δ_c=c/log T. Then

\[
\widetilde R_c(t)=N^{-\delta_c-it}
\left[-e_N(0)+s_c(t)\int_0^\infty
e_N(v)e^{-\delta_cv-itv}dv\right].
\tag{21}
\]

The two copies of e_N are coupled. Replacing their energies by two unrelated nonnegative numbers loses actual analytic structure; asserting that the coupling forces (5) without proof is equally unjustified. A new usable estimate must exploit that common arithmetic function at precision sufficient for (5).

For orientation only, under the full sine/GUE prediction the normalized residual energy would be

\[
\frac{\|R_c\|_2^2}{T\log^2T}\longrightarrow\frac{e^{-2c}}{2c}.
\tag{22}
\]

Its signed contribution to (3) would be −0.3738225362077544… . Thus these residuals are leading-order objects, not errors tending to zero. Formula (22) is a model prediction, not an additional result of the contour lemma.

### 7. Why positive coefficients do not close the argument

For a finite polynomial with nonnegative coefficients, the diagonal coefficient in the two-scale difference is

\[
g(u)=\sinh(2)e^{-2u}-\sinh(1)e^{-u},
\quad u=\frac{\log n}{\log T}.
\]

It is negative for \(u>\log(2\cosh1)=1.126928011\ldots\). Even the one-term polynomial \(\Lambda(p)p^{-s}\), with \(T=p^{1/2}\) and p a sufficiently large prime, has a strictly negative two-scale squared-norm difference because g(2)<0. This is a counterexample to a **universal positive-coefficient quadratic-form assertion**, not a counterexample to the target for actual ζ.

Moreover, (10) has a mandatory continuous counterterm. At a real point s between 1/2 and 1 the finite positive prime sum grows, while (M^{1-s}/(s-1)) is negative and cancels that growth. Removing the counterterm changes the analytic function. These two obstacles survive before any sophisticated arithmetic estimate is attempted.

### 8. Verification and scope

The accompanying `check_centered_tail.py` records:

- exact rational enclosures for B and 1/16−B, obtained by enclosing e with its Taylor series and a geometric remainder;
- an independent finite-step integration-by-parts check of (8), with a finitely supported von Mangoldt measure and a completely evaluated tail, in its absolute-convergence half-plane;
- a comparison with actual ζ′/ζ at Re(s)=3, with an explicit bound on the omitted absolutely convergent von Mangoldt tail;
- small, labeled diagnostic evaluations of the **regularized** sum (10) at s=3/4, showing the size and sign of the mandatory counterterm. These finite diagnostics do not certify convergence rates in the critical strip.

The analytic proof, rather than the numerical checks, supplies continuation and the large-T statements. No numerical value of W_T has been inferred from the low-height examples.

Source inputs for the decomposition are standard RH consequences and the prime number theorem. Relevant primary background is [Goldston, *Notes on Pair Correlation of Zeros and Prime Numbers*](https://arxiv.org/abs/math/0412313), particularly the explicit-formula and mean-value discussion. The significance of the 1/16 threshold comes from the separate, independently reviewed Round 7 reduction using [Goldston–Lee–Schettler–Suriajaya, *Pair Correlation Conjecture II: The Alternative Hypothesis*](https://arxiv.org/abs/2507.06823). The full mixed-integral proof needed here is written in Section 4; neither the decomposition nor the removal of the pole term requires the stronger pair/resolvent estimate.

**Conclusion of this bounded test:** the short-prime main term can be rigorously isolated, and the actual arithmetic term that must improve is (5), equivalently (20)–(21). No lower bound beyond the existing information has been established. Further work should address this signed centered-prime energy rather than reusing coefficient positivity or omitting the pole subtraction.


<a id="report-19"></a>

# Current report 19: Independent audit of the actual-zeta short-polynomial identity

**Collection:** R8 — short-prime projection and signed residual.

**Source:** [research/dyson/round8/resolvent-arithmetic/INDEPENDENT_IDENTITY_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/resolvent-arithmetic/INDEPENDENT_IDENTITY_AUDIT.md).

**SHA-256:** `5159f2127474e57041368aa3741cefa9b7c29040b8286492bb6107eea052c8ab`. **Git blob:** `988ec3ec381faeb3d4a9b4b4f6ef830bc8be9a39`. **Original bytes:** 12823.

## Independent audit of the actual-zeta short-polynomial identity

Date: 2026-09-05. Reviewer: `yau_flow`, independently of the authoring agent.

**Verdict:** the complete draft `SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md` has been read and its analytic identities independently checked below. The estimates, endpoint conventions, and signs pass. Two optional simplifications were returned to the author; neither repairs a failure of the main claim. This is ordinary internal proof review, not formal verification or external peer review. No numerical integration, parameter scan, or modification of author evidence was performed.

### 1. Statement and exact range

Assume RH. Fix \(c>0\), and for every sufficiently large real \(T\), set
\[
N=\left\lfloor\frac{T}{\log^6T}\right\rfloor,
\quad \sigma=\frac12+\frac{c}{\log T},
\quad H(t)=-\frac{\zeta'}{\zeta}(\sigma+it),
\quad P(t)=\sum_{n\leq N}\frac{\Lambda(n)}{n^{\sigma+it}}.
\]
Put \(D_N=\sum_{n\leq N}\Lambda(n)^2n^{-2\sigma}\). The checked identity is
\[
\boxed{\int_0^T|H(t)|^2dt
=T D_N+\int_0^T|H(t)-P(t)|^2dt
 +O_c(N\log^4T).}
\tag{1}
\]
The implicit constant may depend on the fixed \(c\). Uniformity as \(c\downarrow0\), or for \(c\) varying arbitrarily with \(T\), has not been established. The identity holds for all sufficiently large \(T\); no selection of top-edge heights avoiding zero ordinates is needed.

### 2. Mixed inner product: contour, orientation, and pole

Let \(q(s)=-\zeta'/\zeta(s)\), \(\beta=1+1/\log N\), and
\[
G(s)=\sum_{n\leq N}\Lambda(n)n^{s-2\sigma}.
\]
On the left edge \(s=\sigma+it\), one has exactly
\(G(s)=\overline{P(t)}\). Thus \(q(s)G(s)\), rather than a differently conjugated Dirichlet polynomial, is the required analytic integrand.

Use the rectangle with real parts \(\sigma,\beta\) and imaginary parts \(1,T\). Under RH no nontrivial zero lies in this rectangle. The pole of \(q\) at \(s=1\) lies at height zero, **below** it. Trivial zeros are also outside. Consequently the contour shift contributes horizontal integrals and no residue. The factor \(ds=i\,dt\) on either upward vertical edge preserves the normalization of the diagonal term.

The right-edge Dirichlet series is absolutely convergent. Its diagonal contribution is \((T-1)D_N\). The off-diagonal error is bounded by a constant times
\[
\sum_{n\leq N}\Lambda(n)n^{\beta-2\sigma}
 \sum_{m\ne n}\frac{\Lambda(m)m^{-\beta}}{|\log(m/n)|}.
\tag{2}
\]
The infinite \(m\)-sum is not truncated silently.

### 3. Near-diagonal and far-pair estimates

For \(n/2\leq m\leq2n\), \(m\ne n\),
\[
|\log(m/n)|\geq\frac{|m-n|}{2n},\qquad
n^{\beta-2\sigma}m^{-\beta}\ll n^{-2\sigma}.
\]
Since \(n^{1-2\sigma}=n^{-2c/\log T}\leq1\), the corresponding summand is
\[
\ll\frac{\log^2(2N)}{|m-n|}.
\]
The harmonic sum over \(m\) costs \(O(\log N)\); summing over \(n\leq N\) gives \(O(N\log^3N)\). This directly controls the potentially dangerous neighboring integers without a cancellation assumption.

For the remaining pairs, \(|\log(m/n)|\geq\log2\). Also
\[
n^{\beta-2\sigma}\leq n^{1/\log N}\leq e,
\qquad
\sum_{m\geq2}\frac{\log m}{m^{1+1/\log N}}
\ll\log^2N.
\]
Using only \(\Lambda(m)\leq\log m\) and
\(\sum_{n\leq N}\Lambda(n)\leq N\log N\), the far-pair portion of (2) is likewise \(O(N\log^3N)\). The claimed right-line error therefore holds without prime-pair estimates or cancellation.

### 4. Horizontal sides and the shrinking distance to the zeros

The standard local partial-fraction formula and the local zero-count bound imply, under RH,
\[
q(u+iT)=O_c(\log^2T),\qquad \sigma\leq u\leq\beta.
\tag{3}
\]
Indeed, there are \(O(\log T)\) zeros with \(|\gamma-T|\leq1\), and their distances to this segment are at least \(\sigma-1/2=c/\log T\); the remaining terms contribute \(O(\log T)\). This explains the dependence on \(c\) and remains valid when \(T\) itself equals a zero ordinate.

Uniformly on either horizontal side,
\[
|G(u+it)|\leq\sum_{n\leq N}\Lambda(n)n^{\beta-2\sigma}
\ll N\log N.
\]
The top side has bounded length, so it contributes \(O_c(N\log^3T)\). On the bottom side at height one, a compact meromorphic bound gives \(q(u+i)=O_c(\log T)\), even without using an explicit numerical zero-free height. Hence its contribution is smaller. The pole at height zero does not enter either estimate.

For the omitted interval \([0,1]\), one may use the crude bounds
\[
|H(t)|\ll_c\log T,
\qquad |P(t)|\ll\sqrt N\log N.
\]
They give a mixed contribution \(O_c(\sqrt N\log N\log T)\), which is absorbed by the displayed error. The replacement of \((T-1)D_N\) by \(TD_N\) is also harmless. Thus
\[
\int_0^TH(t)\overline{P(t)}\,dt
=T D_N+O_c(N\log^3T).
\tag{4}
\]

### 5. Polynomial norm and completion of the square

Directly expanding \(\int_0^T|P|^2\) gives \(TD_N\) plus off-diagonal terms. The same near-diagonal estimate just used gives \(O(N\log^3N)\). Away from comparable integers, the absolute bound
\(\sum_{n\leq N}\Lambda(n)n^{-\sigma}\ll\sqrt N\log N\)
suffices. In particular, the author's weaker bound
\[
\int_0^T|P(t)|^2dt=T D_N+O(N\log^4T)
\tag{5}
\]
is valid.

The exact Hilbert-space identity
\[
\|H-P\|_2^2=\|H\|_2^2+\|P\|_2^2
-2\Re\langle H,P\rangle
\]
combined with (4) and (5) proves (1). The main diagonal has coefficient **one**. There is no missing factor of two and no negative sign on the residual norm. With this choice of \(N\), the normalized error in (1) is \(O_c(\log^{-4}T)\) after division by \(T\log^2T\).

### 6. Exact continuation in terms of the prime-counting error

Use the endpoint convention
\[
\psi(N)=\sum_{n\leq N}\Lambda(n),\qquad E(x)=\psi(x)-x.
\]
Partial summation for \(\Re s>1\) gives
\[
\boxed{q(s)-\sum_{n\leq N}\Lambda(n)n^{-s}
=\frac{N^{1-s}}{s-1}-E(N)N^{-s}
 +s\int_N^\infty E(x)x^{-s-1}\,dx.}
\tag{6}
\]
Both the sign of the pole term and the minus sign on the endpoint error are correct. At an integer cutoff, replacing \(\psi(N)\) by its left limit would require adding the missing endpoint prime-power term; the convention above avoids that error.

RH gives \(E(x)=O(\sqrt x\log^2x)\). Therefore the integral converges absolutely and locally uniformly for \(\Re s>1/2\), and the identity extends meromorphically to that half-plane. The only pole at \(s=1\) is explicitly present on the right. Formula (6) is thus a true arithmetic continuation identity at the chosen \(s\), not a formal Dirichlet series outside its convergence half-plane.

Absolute convergence is **not** the desired fine bound on the residual. Writing \(\delta=\sigma-1/2=c/\log T\), its crude absolute majorant contains
\[
|s|N^{-\delta}
\left(\frac{\log^2N}{\delta}
 +\frac{2\log N}{\delta^2}+\frac2{\delta^3}\right).
\]
This can be far too large on \([0,T]\). Cancellation or a genuinely stronger mean-square estimate is still needed for the signed two-scale target.

### 7. Diagonal constant and the unresolved signed residual

PNT and partial summation give, for each fixed \(c>0\),
\[
\frac{D_N}{\log^2T}\longrightarrow
d(c):=\int_0^1u e^{-2cu}\,du
=\frac{1-(1+2c)e^{-2c}}{4c^2},
\]
because \(\log N/\log T\to1\). The two-scale diagonal contribution is exactly
\[
B_{\rm low}=2\{\sinh2\,d(1)-\sinh1\,d(1/2)\}
=0.4560939793292318\ldots.
\]
Writing \(R_c=H_c-P_c\), the remaining requirement for the sufficient threshold \(1/16\) is
\[
\liminf_{T\to\infty}
\frac{2}{T\log^2T}
\left(\sinh2\,\|R_1\|_2^2-\sinh1\,\|R_{1/2}\|_2^2\right)
\geq\frac1{16}-B_{\rm low}.
\]
The right side is \(-0.3935939793292318\ldots\). These decimals are ordinary evaluations of the explicit constants, not numerical zeta data or an outward enclosure. Positivity of each individual squared norm does not establish a lower bound for this signed combination. Identity (1) and continuation (6) make that remaining arithmetic obligation precise; they do not solve it.

### 8. Centered-tail refinement and additional checks of the full draft

The author's global continuation formula
\[
q(s)=\frac{s}{s-1}+s\int_1^\infty E(x)x^{-s-1}dx
\]
also has the correct constant. It specializes to (6) at \(N=1\), since \(\psi(1)=0\) and \(E(1)=-1\). For each fixed \(s\) in the claimed half-plane, the endpoint error and centered tail vanish as the cutoff tends to infinity. Hence the regularized limiting sum in the author's equation (10) is valid. Its convergence is uniform on each fixed compact vertical segment, but a subsequent \(T\)-limit requires preserving that order or proving uniform estimates.

The norm of the explicit pole term at the chosen cutoff satisfies
\[
\left\|\frac{N^{1-s_c(t)}}{s_c(t)-1}\right\|_2^2
\ll_c N.
\]
The author's use of the already reviewed stronger bound \(I_T(c)=O_c(T\log^2T)\) justifies dropping this term from the **normalized residual energy**, including its cross term. There is also a self-contained weaker route: the pointwise RH estimate already used in this proof gives \(I_T(c)=O_c(T\log^4T)\). Together with the elementary polynomial norm bound, this gives \(\|R_c\|_2^2=O_c(T\log^4T)\). Cauchy–Schwarz then bounds the change in normalized residual energy by
\[
O_c\!\left(\sqrt{N/T}+\frac{N}{T\log^2T}\right)
=O_c(\log^{-3}T)=o(1).
\]
Thus this particular removal need not depend on the Round 7 pair/resolvent transfer. This optional simplification was communicated to the author.

The change of variables \(x=Ne^v\), with
\(e_N(v)=E(Ne^v)/(Ne^v)^{1/2}\), gives exactly
\[
\widetilde R_c(t)=N^{-\delta_c-it}
\left[-e_N(0)+s_c(t)\int_0^\infty
e_N(v)e^{-\delta_cv-itv}dv\right].
\]
There is no missing power of \(N\), Jacobian, or endpoint term. Both scales use the same function \(e_N\). This shared arithmetic input must be preserved in any future estimate; treating the two residuals as arbitrarily independent objects would lose information.

The reported GUE orientation formula is consistent with the existing normalization: subtracting
\(d(c)\) from \(V_{\rm sine}(2c)/2=(1-e^{-2c})/(4c^2)\)
gives \(e^{-2c}/(2c)\). This is a conditional model prediction, as the draft states, and was not used to prove the arithmetic identity.

For the bottom contour and initial time interval, the draft's stronger bounds invoke the familiar zero-free low-height compact region. The weaker bounds in §4 of this audit avoid that extra fact altogether, using only RH and finite zero counts on compact sets. They are already sufficient for the claimed error. This was the second optional simplification sent to the author.

### 9. Provenance and scope

The fully inspected author draft has SHA-256
`8840bdfcdfa07baf369deaed39151292ee28ff386f946336f21368d867277305`.
Any later editorial version should retain this review's explicit scope or be checked as a separate delta. The mathematical constants in §7 were independently evaluated from their displayed elementary formulas. The planned numerical check script had not yet been saved when this proof review was completed and is **not** claimed to have been independently reviewed or rerun.

The primary background references used by the author are [Goldston's notes on pair correlation and prime numbers](https://arxiv.org/abs/math/0412313) and [Goldston–Lee–Schettler–Suriajaya's AH paper](https://arxiv.org/abs/2507.06823). The mixed-integral estimate itself was checked directly above rather than attributed to an unstated stronger source theorem. No claim of novelty for the contour method or continuation identities is made.

### 10. Final-version delta acceptance

The frozen final author draft was subsequently inspected and its SHA-256 independently recomputed as
`0067a1b0c7bd4f0b80ef89d6ac85eca1ae99e652375c08c41706ec1f1ddbe40e`.
**This final version is accepted.** The earlier hash in §9 records the initially reviewed draft rather than the final checkpoint.

The bounded delta review checked these changes directly:

- Section 4 now uses the compact RH logarithmic-derivative bound \(O_c(\log T)\) for the bottom side and initial interval, with errors \(O_c(N\log N\log T)\) and \(O_c(\sqrt N\log N\log T)\). Both are absorbed by \(O_c(N\log^3T)\). No low-zero table or exceptional choice of \(T\) is required.
- Section 6 now removes the pole from the normalized residual energy using only \(\|R_c\|_2^2=O_c(T\log^4T)\) and pole norm squared \(O_c(N)\). Its stated error \(O_c(\sqrt{N/T}+N/(T\log^2T))=O_c(\log^{-3}T)\) is correct.
- The source paragraph now correctly separates the RH/PNT inputs for the decomposition from the external significance of the \(1/16\) target. The decomposition and pole removal no longer depend on the stronger Round 7 pair/resolvent estimate.

These changes implement the two simplifications in §8 without changing the diagonal constant, the exact centered-tail identity, or the unproved signed-residual obligation. The author's completed numerical script and result files were not rerun in this delta review; their replay belongs to the coordinator's separate verification. This independent review file is now final.


<a id="report-20"></a>

# Current report 20: A bounded positivity audit of the two-scale target

**Collection:** R8 — short-prime projection and signed residual.

**Source:** [research/dyson/round8/spectral-positivity/POSITIVITY_OBLIGATION_NOTE.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/spectral-positivity/POSITIVITY_OBLIGATION_NOTE.md).

**SHA-256:** `485b7778a0f7bab21492dac710b8732e5e1996734014fbba770d4b076a7b6329`. **Git blob:** `fcf57a8936ea557feb1a41b99f824d8e2cfa59f4`. **Original bytes:** 7514.

## A bounded positivity audit of the two-scale target

Date: 2026-09-05. This note closes one bounded proof audit; it contains no new parameter scan, arithmetic estimate, or zeta result. Round 7 files were not changed.

**Conclusion.** The known interior Montgomery band, spectral positivity, and realizable stationary point-process constraints do not imply the target \(W\geq1/16\). The obstruction is an actual determinantal point process, not merely a proposed nonnegative spectrum. The additional calculation below gives an explicit, substantially weaker lower bound using pair-measure positivity. It identifies a valid inference but does not close the arithmetic obligation.

### 1. Normalization and the formal-spectrum warning

Write
\[
A=\sinh2,\quad B=\sinh1,\qquad
K(\alpha)=Ae^{-2|\alpha|}-Be^{-|\alpha|}.
\]
For a unit-intensity stationary process, let \(\mu\) be its pair measure including the diagonal, and let \(S=\widehat\mu-\delta_0\) be its centered structure-factor measure. Assume the relevant Poisson integrals are finite. The two-scale statistic is
\[
W=\int K\,dS
 =\int J(x)\,d\mu(x)-(A-B),
\quad
J(x)=\frac{A}{1+\pi^2x^2}-\frac{2B}{1+4\pi^2x^2}.
\]
The known band is \(dS(\alpha)=|\alpha|\,d\alpha\) on \((-1,1)\); this specifies no atoms at the endpoints.

The sign change is exactly
\[
\alpha_0=\log(A/B)=\log(2\cosh1)>1.
\]
Adding arbitrarily large nonnegative atoms at \(\pm R\), for fixed \(R>\alpha_0\), leaves the interior band unchanged and sends \(\int K\,dS\) to minus infinity. This proves only that **formal spectral positivity alone** supplies no finite lower bound. Such modified spectra have not been shown to be realizable by point processes and are not used as the actual obstruction below.

Pair positivity is a meaningful extra constraint. For \(y=\pi^2x^2\),
\[
J(x)=\frac{(A-2B)+(4A-2B)y}{(1+y)(1+4y)}>0.
\]
Since \(\mu\geq\delta_0\), it immediately gives the valid but weak bound \(W\geq-B\). Thus the formal unbounded-below example cannot respect all these pair constraints.

### 2. An explicit band-limited minorant

The following stronger bound is already available from the same data. It is not claimed optimal over all positivity arguments.

Set
\[
a=2\tanh1,\qquad b=2\tanh(1/2),\qquad \kappa=2b-a>0,
\]
and define
\[
R(x)=\frac{a}{1+\pi^2x^2}-\frac{2b}{1+4\pi^2x^2},
\quad
f(x)=\cos^2(\pi x)R(x)+\kappa\operatorname{sinc}^2(x),
\quad g(x)=J(x)-f(x),
\]
with \(\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)\).

**Claim:** \(f\geq0\), and \(\widehat g\) is supported on \([-1,1]\), with \(\widehat g(\pm1)=0\). Consequently
\[
W\geq \widehat g(0)+2\int_0^1\alpha\widehat g(\alpha)\,d\alpha-(A-B)
=:\mathcal B.
\tag{P}
\]
The right side is an elementary expression in exponentials and hyperbolic tangents. Its floating evaluation is \(-0.208674512963925\ldots\); the exact expression, rather than these digits, is the proved bound.

To prove nonnegativity, note \(0<b<a<2b\). Direct calculation gives \(R(x)\geq-\kappa\) for all \(x\), since
\[
R(x)+\kappa
=\frac{y\{(8b-a)+(8b-4a)y\}}{(1+y)(1+4y)}\geq0.
\]
Also \(R(x)<0\) only if \(y<\kappa/(4a-2b)<1\). There \(|\pi x|<1<\pi/2\), and \(\operatorname{sinc}^2(x)\geq\cos^2(\pi x)\). Hence
\(f\geq\cos^2(\pi x)(R+\kappa)\geq0\). Where \(R\geq0\), nonnegativity is immediate.

For the Fourier support, put \(E(\alpha)=ae^{-2|\alpha|}-be^{-|\alpha|}\). Then
\[
\widehat f(\alpha)=\tfrac12E(\alpha)
 +\tfrac14E(\alpha-1)+\tfrac14E(\alpha+1)
 +\kappa(1-|\alpha|)_+.
\]
For \(|\alpha|\geq1\), the first three terms equal \(K(\alpha)\), using
\(a\cosh^2(1)=A\) and \(b\cosh^2(1/2)=B\). Thus \(\widehat g\) vanishes there, including the endpoints. Pair-measure positivity and the known band prove (P). The \(O(x^{-2})\) decay permits these tests under the linear pair-mass bound used in Round 7.

Here is a closed finite expression for reproducing \(\mathcal B\). For each triple \((r,c,d)\) in \(\{(2,A,a),(1,-B,-b)\}\), define
\[
u=c-d(1/2+e^{-r}/4),\quad v=-de^{-r}/4,
\]
\[
I_-(r)=\frac{1-(1+r)e^{-r}}{r^2},\qquad
I_+(r)=\frac{(r-1)e^r+1}{r^2}.
\]
Then
\[
\boxed{\mathcal B=
\sum_{(r,c,d)}\{u(1+2I_-(r))+v(1+2I_+(r))\}
-\frac43\kappa-(A-B).}
\]
For the one-parameter correction \(f_c=\cos^2(\pi x)R+c\operatorname{sinc}^2(x)\), positivity at zero requires \(c\geq\kappa\). Since the bound decreases by \(4c/3\), the chosen correction is optimal **within this particular one-parameter family**, not among all minorants or point processes.

### 3. The obstruction is a genuine point process

On \(\mathbb Z\), take the determinantal process with kernel
\[
Q(j,k)=\int_{-1/4}^{1/4}e^{2\pi i(j-k)t}\,dt
=\begin{cases}1/2,&j=k,\\
\sin(\pi(j-k)/2)/(\pi(j-k)),&j\ne k.
\end{cases}
\]
This is the orthogonal projection onto a frequency interval of length \(1/2\), so it defines an actual determinantal probability measure; see [Lyons, *Determinantal probability measures*](https://www.numdam.org/articles/10.1007/s10240-003-0016-0/). If \(\mathcal X\subset\mathbb Z\) is its random occupied set and \(U\) is independently uniform on \([0,1)\), then
\[
\{(j+U)/2:j\in\mathcal X\}
\]
is a stationary, simple, unit-intensity point process on the line. Stationarity follows from integer-translation invariance of the discrete process and uniform random translation within one lattice cell.

Its Palm pair measure is exactly
\[
\mu_A=\delta_0+\frac12\sum_{k\ne0}
 \left(1-\operatorname{sinc}^2(k/2)\right)\delta_{k/2}.
\]
Indeed the discrete pair occupation probability is \(1/4-|Q(0,k)|^2\), and conditioning on the occupied point divides by \(Q(0,0)=1/2\). All pair weights are nonnegative. In particular, \(\mu_A([-R,R])\leq1+2R\), giving the required linear cumulative bound. The process has a hard core of one half.

Poisson summation gives its centered spectrum
\[
dS_A(\alpha)=\operatorname{dist}(\alpha,2\mathbb Z)\,d\alpha
 +\sum_{m\ne0}\delta_{2m}.
\]
Thus it has exactly the prescribed Montgomery data on \((-1,1)\), and satisfies spectral positivity, diagonal normalization, pair-measure positivity, simplicity, and the cumulative pair bound. The nonzero even-frequency atoms must be retained.

Its Poisson variance and two-scale statistic are
\[
V_A(r)=\frac{2\tanh(r/2)}{r^2}+\frac2{e^{2r}-1},
\]
\[
W_A=\frac{e^2}{4}+\frac5{4e^2}-e-\frac2e+\frac32
\in(0.06239,0.06240)<\frac1{16}.
\]
The exact constant enclosure is already certified in the frozen Round 7 artifact. No new decimal scan is needed. This gives the realizable obstruction to the proposed inference. It is not a construction of actual zeta zeros and is not claimed to satisfy every arithmetic identity known about zeta.

### 4. The remaining arithmetic obligation

For any fixed pair of positive smoothing scales, this same process remains compatible with the stated low-band and point-process assumptions. A statistic whose proved lower bound would exclude its value therefore cannot follow from those assumptions alone. Changing the scales may improve the size or shape of the target; it does not add the missing arithmetic information.

For the present scales, the unresolved requirement is an actual-zeta estimate for the signed out-of-band contribution
\[
\int_{|\alpha|\geq1}
 \left(Ae^{-2|\alpha|}-Be^{-|\alpha|}\right)dS_\zeta(\alpha),
\]
or its finite-height counterpart with controlled errors. The negative tail beyond \(\log(2\cosh1)\) prevents simply discarding the unknown part. The concrete arithmetic identity proposed for this contribution must be audited on its own; generic positivity and another random-matrix calculation cannot replace it.


<a id="report-21"></a>

# Current report 21: Independent review of the fixed positivity minorant

**Collection:** R8 — short-prime projection and signed residual.

**Source:** [research/dyson/round8/spectral-positivity/MINORANT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/spectral-positivity/MINORANT_REVIEW.md).

**SHA-256:** `383af540ae53eba3a0fbcb471fcf79d72b821167450cc05e9a89198c7dbc843a`. **Git blob:** `caaadd49825fc344d29371a28bedd8a938180293`. **Original bytes:** 9174.

## Independent review of the fixed positivity minorant

Date: 2026-09-05. Reviewer: the independent residual/arithmetic agent. Scope: the displayed minorant in [POSITIVITY_OBLIGATION_NOTE.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/spectral-positivity/POSITIVITY_OBLIGATION_NOTE.md), its closed constant, and the half-grid determinantal pair normalization. No parameter optimization, new literature survey, or actual-zeta computation was performed. The author note was not edited.

**Verdict: accepted as an ordinary mathematical proof under the stated pair-measure and interior-band assumptions, including the linear cumulative pair bound used for the tests.** I found no coefficient, sign, support, endpoint, or Palm-normalization defect. The regularization details below make explicit a step compressed into the note's decay statement. This is internal proof review, not formal verification or external peer review.

The bound is exactly the displayed expression, approximately **−0.2086745129639258**. It improves the immediate −sinh(1) consequence of pair positivity, but it is not progress to the required positive threshold 1/16, is not a new bound on actual zeta proved here, and is not optimal over general minorants. The optimum statement applies only to the specified one-parameter correction family and its displayed inference.

### 1. Nonnegativity of the remainder

Use the note's A, B, a, b, kappa and y=pi^2 x^2. To verify all parameter inequalities without decimals, put t=tanh(1/2), so 0<t<1 and

    a = 4t/(1+t^2),  b = 2t,
    kappa = 4t^3/(1+t^2),
    kappa/(4a-2b) = t^2/(3-t^2) < 1/2 < 1.

Thus 0<b<a<2b, both coefficients in the note's numerator for R+kappa are positive, and R>=-kappa. The numerator of R is -kappa+(4a-2b)y. Wherever R<0, |pi x|<1<pi/2. For 0<=z<pi/2, tan(z)>=z, because (tan(z)-z)'=tan^2(z)>=0. Hence (sin(z)/z)^2>=cos^2(z), also at z=0 by continuity. It follows on that negative region that

    cos^2(pi x) R(x) + kappa sinc^2(x)
      >= cos^2(pi x) [R(x)+kappa] >= 0.

On the remaining region both summands are nonnegative. This proves f>=0 everywhere, including zero; indeed f(0)=0. All rational identities used above pass the accompanying exact symbolic checks.

For f_c=cos^2(pi x)R+c sinc^2(x), evaluation at zero gives f_c(0)=c-kappa, so positivity requires c>=kappa. This condition is sufficient, since f_c=f_kappa+(c-kappa)sinc^2. The displayed lower-bound functional decreases by 4c/3 and is therefore maximized at c=kappa in this family. Even if one separately credits the known diagonal contribution f_c(0), the resulting functional decreases by c/3, so the same endpoint is still optimal. This observation does not establish an optimum among other band-limited minorants or other pair constraints.

### 2. Fourier support, endpoints, and legitimate pair testing

The convention is Fourier transform hhat(alpha)=integral h(x) exp(-2pi i alpha x) dx. Under this convention,

    [1/(1+pi^2 x^2)]hat = exp(-2|alpha|),
    [2/(1+4pi^2 x^2)]hat = exp(-|alpha|),
    [sinc^2(x)]hat = (1-|alpha|)_+.

The coefficients 1/2, 1/4, 1/4 in the modulation by cos^2(pi x) are therefore correct. For alpha>=1, the coefficient of a exp(-2alpha) becomes cosh^2(1), and that of b exp(-alpha) becomes cosh^2(1/2). The exact identities a cosh^2(1)=A and b cosh^2(1/2)=B cancel the whole Fourier tail. Evenness handles alpha<=-1. The triangular correction vanishes at both endpoints, and the modulation identities continue to hold there, so ghat(1)=ghat(-1)=0 exactly. There are no overlooked endpoint delta terms: J, f and g are integrable functions, and their Fourier transforms are continuous functions.

An unknown atom of the pair spectrum at either endpoint therefore contributes zero. The known band can be used without silently assuming endpoint atom-freeness. Here is also an ordinary justification for passing from Schwartz test identities to this particular g. Its compactly supported transform is continuous, piecewise smooth, vanishes linearly at the endpoints, and has first derivative of bounded variation. Smooth it and cut it off just inside (-1,1). These approximants can be chosen with uniformly bounded L1 norms and uniformly bounded total variation of their first derivatives: in an endpoint strip of width epsilon, the function is O(epsilon), so the second-derivative cutoff terms have bounded L1 norm. Their inverse transforms g_epsilon consequently obey

    |g_epsilon(x)| <= C/(1+x^2)

uniformly, and converge pointwise to g. The assumed linear cumulative pair bound gives integrability of this dominator. Dominated convergence on the pair side and the known interior spectral identity on the other side then yield

    integral g dmu = ghat(0) + integral_{-1}^{1} |alpha| ghat(alpha) dalpha.

This argument requires no guess about endpoint atoms or the unknown outer spectrum. Since f=J-g>=0 and mu is a positive measure, the note's inequality (P) follows. The subtraction A-B is correct: it is K(0), the Fourier atom of the unit mean-density contribution. Independently, J(0)=A-2B and mu>=delta_0 give W>=-B, as claimed.

### 3. Closed expression and fixed symbolic verification

For alpha in [0,1], each triple (r,c,d) contributes

    u exp(-r alpha) + v exp(r alpha),
    u = c-d(1/2+exp(-r)/4),  v = -d exp(-r)/4,

to ghat before the correction -kappa(1-alpha). Direct integration of alpha exp(+-r alpha) gives precisely I_minus and I_plus in the note. The value at zero contributes -kappa and the weighted integral contributes -kappa/3, explaining the total -4kappa/3 without any diagonal or two-sided factor ambiguity.

As an independent exact algebra check, set X=exp(1). The complete closed lower bound simplifies to

    (X-1)(3X^6-6X^5-17X^4+28X^3-35X^2-6X-15)
    / [12 X^2 (X+1)(X^2+1)].

This is an exact expression, not a fitted approximation. Substitution X=e gives -0.2086745129639258383515265856... . The script's decimal evaluation is explicitly floating, not an outward enclosure; the ordinary proof uses the exact formula and does not require a decimal certificate.

The companion [minorant_symbolic_check.py](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/spectral-positivity/minorant_symbolic_check.py) verifies the rational identities, the two elementary integrals, the endpoint, the correction coefficient, the Palm occupation division, the triangle-period integral and the DPP two-scale formula. [minorant_symbolic_check.json](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/spectral-positivity/minorant_symbolic_check.json) records PASS, versions and source hashes. Reproduction from this directory is `python3 minorant_symbolic_check.py`; it writes only its adjacent JSON. This is a small fixed identity check, not an optimization or sampled nonnegativity test.

### 4. Half-grid DPP normalization and realized obstruction

The stated Q is the Fourier projection of l2(Z) onto the interval [-1/4,1/4]. In particular it is a positive contraction with diagonal 1/2, and the standard discrete determinantal construction supplies a probability measure with finite occupation probabilities det(Q|F). The note's [Lyons reference](https://www.numdam.org/articles/10.1007/s10240-003-0016-0/) is the appropriate primary reference for the projection/positive-contraction framework. No independence of the occupation indicators is being assumed.

After scaling lattice spacing to 1/2, the occupancy probability 1/2 gives intensity 2*(1/2)=1. The independent uniform shift covers one full lattice cell; combined with integer-shift invariance of the discrete DPP this gives stationarity under every real translation. The lattice process is simple and has minimum positive spacing 1/2.

For k!=0, the conditional probability of a point at displacement k/2 from a Palm point is

    [1/4-|Q(0,k)|^2]/(1/2)
       = (1/2)[1-sinc^2(k/2)].

The Palm base point contributes exactly delta_0. Thus the displayed mu_A has the correct factor 1/2, and its nonzero weights lie between zero and 1/2. Counting the at most 2 floor(2R) nonzero lattice sites proves mu_A([-R,R])<=1+2R.

The full Fourier calculation can be written without omitting the zero sample:

    mu_A = delta_0 + (1/2) sum_k delta_(k/2)
                      - (1/2) sum_k sinc^2(k/2) delta_(k/2).

Poisson summation transforms these three terms into the constant density 1, the comb sum_m delta_(2m), and the periodized triangle sum_m (1-|alpha-2m|)_+, respectively. Hence the remaining continuous density is dist(alpha,2Z). Centering removes only the comb atom at zero. All nonzero even-frequency atoms survive, exactly as in the note.

Finally, the Laplace integral of the triangular density over one positive period is (1-exp(-r))^2/r^2. Summing its geometric repetitions on both sides gives 2 tanh(r/2)/r^2; the nonzero even comb gives 2/(exp(2r)-1). Therefore both V_A(r) and W_A=A V_A(2)-B V_A(1) are correctly normalized. The accompanying exact symbolic check reproduces the closed W_A expression, whose strict comparison with 1/16 was already enclosed in Round 7.

This actual process meets the stated low-band and positivity assumptions while remaining below 1/16. It is consequently a valid obstruction to deductions using only those assumptions. It is neither an actual-zeta construction nor a model asserted to satisfy the missing arithmetic identities. No stronger impossibility or universality conclusion is endorsed.


<a id="report-22"></a>

# Current report 22: Round 9: actual prime arithmetic for the Dyson–Montgomery programme

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/reports/dyson_round9.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/dyson_round9.md).

**SHA-256:** `37e6f98bc96fdd9686a1e4ec158d822c087f89b35d7bf4aa9ac523c1b9a4d642`. **Git blob:** `8d10e985a2e7712b95dff4d42aef3f4c794b4b7c`. **Original bytes:** 13988.

## Round 9: actual prime arithmetic for the Dyson–Montgomery programme

Date: 2026-09-05. This checkpoint continues the user's request to concentrate on RMT and actual zeta zeros. **No new zeta pair-correlation lower bound, AH refutation, half-gap theorem, RH proof, or prime-gap record is established.** The useful outcomes are a source-checked arithmetic transfer, a quantified removal of prime powers, a negative new resonator trial, and a precise mesoscopic lower-bound obligation.

### 1. The conjecture-level target remains unchanged

Set

\[
I_T(c)=\int_0^T\left|\frac{\zeta'}{\zeta}
\left(\frac12+\frac c{\log T}+it\right)\right|^2dt,
\qquad
W_T=\frac{2(\sinh2\,I_T(1)-\sinh1\,I_T(1/2))}{T\log^2T}.
\]

The reviewed Round 7 reduction gives, under RH and the precise AH-Pairs formulation,

\[
W_T\longrightarrow W_{\rm AH}=0.0623924179764985\ldots <\frac1{16}.
\]

The bounded but possibly nonconvergent near-diagonal mass cancels. An actual-zeta proof of liminf W_T>=1/16 would therefore contradict AH-Pairs under RH. That inequality remains unproved. Round 8 writes W_T=B+E_T+o(1), with B=0.4560939793292317..., so the missing signed residual inequality is liminf E_T>=-0.3935939793292317.... See the [Round 7 reduction](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round7/poisson-resolvent/TWO_SCALE_ZETA_TARGET.md) and [Round 8 proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round8/resolvent-arithmetic/SHORT_PRIME_PROJECTION_AND_CENTERED_TAIL.md).

The complementary compact test has Fourier support [6/5,7/5]. Its centered prime covariance has AH value -3/5 and sine-kernel prediction -3/10. A sufficiently strong estimate here would be an actual out-of-band zeta result. The atomic diagonal, continuous mean, prime/mean cross term, and continuous mean square must all be retained.

### 2. What the 186 factorization structure really transfers

The [complete transfer proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md) applies Proposition 2.3 and Corollary 2.19 of [*Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf). It uses the ordinary analytic theorem as input, without making a claim about completion of every formalization obligation.

Choose omega=3/250, delta=1/1000 and epsilon=1/1000. Then 240 omega+80 delta=2.96<3, and the resulting full-prime distribution level is 0.523. Let Q_X be a set of distinct squarefree moduli q=[D,E] in (X^(1/2),X^(.523)] satisfying the stated complementary tail predicates. They imply triple dense divisibility at scale X^(.001), even for explicit nonsmooth examples. Repeated representations of one q are counted once; shared prime factors of D,E are allowed.

Insert the exact identity

\[
\Lambda(n)=\sum_{q\mid n}\mu(q)\log(n/q)
=B_{\mathcal Q}(n)+B_{\rm rest}(n).
\]

For a shift h and a smooth macroscopic weight w_h, define

\[
\mathcal C_{\mathcal Q,h}=\sum_n\Lambda(n+h)B_{\mathcal Q}(n)w_h(n),
\quad
\mathcal M_{\mathcal Q,h}=
\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}
\frac{\mu(q)}{\varphi(q)}\int w_h(u)\log(u/q)du.
\]

The source gives, for every fixed A>0,

\[
\mathcal C_{\mathcal Q,h}-\mathcal M_{\mathcal Q,h}
=O_A(X\log^{-A}X).
\tag{1}
\]

This estimate is uniform for 1<=h<=CH, where X=T^alpha, 6/5<=alpha<=7/5 and H=X/T. It applies to a localized version of the actual covariance's sinc weight. The proof checks the common primitive residue h across the modulus family, two common endpoint weights in partial summation, the sum of 1/phi(q), and both kinds of nonprimitive prime-power terms. Neither B_Q nor its remainder is a prime minorant.

This is an identifiable arithmetic component beyond the square-root divisor level. It is not an evaluation of the whole covariance. Summing (1) over every h gives O_A(HX log^(-A)X), whereas the needed fluctuation scale is X log X. Since H is between X^(1/6) and X^(2/7), no fixed logarithmic saving absorbs that loss. Logarithmically bounded shift packets are controlled at the required scale, but that does not evaluate the entire natural packet.

The report isolates the signed progression discrepancy sum D_Q explicitly. Under RH it proves

\[
\sum_{h\le CH}(\mathcal C_{\mathcal Q,h}-\mathcal M_{\mathcal Q,h})
=\mathfrak D_{\mathcal Q}(X,T)+O(H\sqrt X\log^4X).
\tag{2}
\]

The last error is o(X log X), uniformly over the alpha interval. The new estimate still needed for this selected component is D_Q=o(X log X). The remaining shifted bilinear form B_rest, the two support sums in M_Q, other spatial/shift ranges, and the continuous centering remain separate obligations. In particular, the source's multiplicative-convolution bilinear theorem cannot simply be applied to Lambda(qm+h), which depends jointly on all three variables.

The [independent source and proof review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/factorization-covariance/INDEPENDENT_BRIDGE_REVIEW.md) accepts (1) and (2) with these scopes. The exact script checks 300 formal Mobius–log identities and five progression/discrepancy decompositions. These finite examples test algebra, not the source's asymptotic distribution estimate.

### 3. A new two-prime interaction was tried and failed

Archive inspection showed that the proposed resummed multiplicative prime profile had already been tried. Its old best continuation did not beat the existing larger polynomial trial. Repeating that scan was stopped before computation.

The replacement uses a genuinely different fixed arithmetic mark. For n<=L, let C count distinct prime divisors p with p³>L, and D=C(C-1)/2. Then C is in {0,1,2}, while D is in {0,1}. The new family is

\[
r_L(n)=d_\ell(n)[F(v_n,S(n))+D_L(n)J(v_n,S(n))],
\qquad \ell=27/25.
\]

When D=1 there is a unique unordered pair p<q of large prime divisors and n=pqm with m<L^(1/3)<min(p,q). This supplies an exact coprime starting decomposition. A singly marked prime at the same threshold does require a repeated-prime error; that error is explicitly O((log L)^a L^(-1/3)), with a=ell². The full three-state insertion calculus keeps the mixed event involving one background and one inserted large prime.

The [arithmetic derivation](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/DERIVATION.md), accepted in a [separate root review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/INDEPENDENT_REVIEW.md), extends the previously reviewed fixed-moment and signed operator-truncation argument. It does not assume a general Fock limit, growing degree, or uniformity over infinitely many marks.

One fixed 30-dimensional span was tested: 20 unmarked features and ten D-marked features. Every coefficient was optimized in that span at quadrature orders 20 and 32; ell and the threshold were fixed.

| Trial | Order 32 half-gap margin |
|---|---:|
| Matched 20-feature baseline | -0.0146549380840028 |
| New 30-feature double-prime interaction | -0.0146549114371551 |
| Earlier best 48-feature trial, approximate | -0.0146547256 |

The new floating gain over its matched baseline is about 2.66e-8, with a scaled Gram condition near 5.36e7. It is not interval-certified. The new span does not contain the historical 48-feature span and performs worse than that historical value. The deficit to the required zero margin is still about 0.01465.

All coefficients and full M/G matrices are retained. The frozen rational vector is provably nonzero and has positive limiting mass independently of the numerical Gram matrix. A single actual-integer operator evaluation at L=100000, retaining every prime-power entry, has margin -0.0374094621535042. Exact finite checks include 12 unordered decompositions, 132 coprime insertion triples and 108 count-state identities. These are checks of this fixed trial, not a global obstruction to resonance and not actual zeta-zero observations.

### 4. Prime powers can be removed at both relevant scales

The [prime-power estimate](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/prime-power-removal/PRIME_POWER_TAIL_ESTIMATE.md) is an elementary infinite-tail argument, accepted in an [independent proof review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/prime-power-removal/INDEPENDENT_REVIEW.md). It is a nuisance-term bound, without a novelty claim.

Let delta=c/log T, sigma=1/2+delta, N=floor(T/log^6 T), R_c=-zeta'/zeta(s)-sum_(n<=N) Lambda(n)n^(-s), and

\[
U_{c,N}(t)=\sum_{\substack{p\ \mathrm{prime},\ k\ge2\\p^k>N}}
(\log p)p^{-k\sigma-ikt\log p}.
\]

Uniformly for 0<delta<=1/4 and N>=4, without RH,

\[
\|U_{c,N}\|_2^2\ll TN^{-1/3}\log^4(2N)+\delta^{-4}.
\tag{3}
\]

Squares are treated by a convergent diagonal/off-diagonal mean-square expansion; the near-pair harmonic sum gives delta^(-4). Higher powers admit a sufficient absolute tail bound using their sparse counting function. No infinite polynomial theorem with a divergent remainder is invoked.

Under RH, replacing R_c by R_c-U_(c,N) changes its normalized energy by O(a_T), where

\[
a_T=N^{-1/6}\log^2(2N)+T^{-1/2}\log^2T=o(1).
\]

The bound is uniform for 1<=c<=log T/4, and holds with a c-dependent constant for each fixed c>0. The remaining continuation uses exactly the genuine-prime error theta(x)-x, including its endpoint and pole term. This removes prime powers from the open arithmetic comparison; it does not improve its limiting constant.

### 5. The mesoscopic target is a first correction, not merely a leading law

Set b=2c and r_T(b)=||R_(b/2)||²/(T log²T). A sufficient two-width asymptotic is

\[
r_T(b)=\frac{e^{-b}}b+o\left(\frac{e^{-b}}{b^2}\right)
\tag{4}
\]

uniformly on a suitable slowly growing range, including the second width. Relative o(1) is insufficient: the distinguishing signal requires relative o(1/b).

The [source and rate audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/mesoscopic-edge/EDGE_RATE_AUDIT.md) checks Theorem 5, Lemma 16 and Section 4.2 of [Carneiro–Chandee–Chirre–Milinovich, *On Montgomery's pair correlation conjecture: a tale of three integrals*](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf). Its proof-level finite-T errors can fit below the signal on a sufficiently slow diagonal. Thus a blanket claim that those errors always swamp the signal would be wrong.

The real obstruction is the limiting lower bound: its deficit from sine is of order e^(-b)/b, while sine minus ACUE is of order e^(-b)/b². The known lower bound therefore misses the required correction by a factor of order b, even when its height error is negligible. The upper deficit is larger by order b².

To remove the general AH near-diagonal nuisance, define

\[
\mathcal C_T(b)=b^2\left[
2\sinh b\,r_T(b)-2\sinh(2b)\,r_T(2b)-\frac1{2b}\right].
\]

The sine prediction tends to zero; the AH prediction tends to -3/4. The nuisance cancels exactly. The reviewed sufficient arithmetic target is: find increasing G(T) tending to infinity with G(T)=o(log log T) such that

\[
\lim_{B\to\infty}\liminf_{T\to\infty}
\inf_{B\le b\le G(T)}\mathcal C_T(b)>-\frac34.
\tag{5}
\]

Fixed-width AH convergence permits an existential stepwise slow diagonal inside this envelope, giving a contradiction if (5) were proved. It does not justify choosing a prescribed rate such as sqrt(log log T). The [independent review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/mesoscopic-edge/INDEPENDENT_EDGE_REVIEW.md) states these quantifiers explicitly.

The prime-power replacement from (3) remains negligible even after the amplification: its effect on C_T is O(b² e^(2b) a_T)=o(1), uniformly for 2<=b<=G(T)=o(log log T). Thus (5) can be pursued using genuine primes. No estimate (4) or (5) is established here.

### 6. Reproducibility, record ownership and next decision

All 28 source files, totaling 1,174,410 bytes, are retained verbatim in the adjacent local `Astra-Local-Archive/round9-originals/`. The public folder retains 26 files; the two omitted third-party PDF/text bodies remain local with URL and SHA256 receipts. The existing 186 primary PDF/text are separately retained under `round9-external-sources/`. No author files were edited for publication. Historical “review pending” labels are superseded by the separately hashed later reviews and the current claim ledger.

The [intake manifest](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/INTAKE_MANIFEST.json) records every original. The [bounded integration replay](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/logs/round9-integration/recheck.py) parses the four scripts, runs one fresh order-32 calculation and the three check scripts in a temporary copy, compares five JSON outputs, and compares the full recomputed M/G arrays. Timing and temporary source-file paths are the only excluded metadata; the order-20 matrices are checked as saved evidence, not advertised as newly recomputed.

Run from the repository root with Python, NumPy and SciPy:

```text
python3 research/logs/round9-integration/recheck.py --prime-gap-source-dir /path/to/retained/round9-external-sources
python3 tools/verify_manifest.py
```

The replayer sets the portable Round 7 dependency path explicitly, verifies its pinned hash, and stages the primary references at the unmodified author's expected relative location. The primary references are inputs to provenance checking; finite arithmetic identities do not constitute a proof of their analytic theorem. Original evidence is unchanged by replay.

The next bounded task is to estimate the actual sum across shifts, testing smooth completion before paying the full H loss. A second lane checks whether known prime short-interval mean squares control the required signed residual correction at sufficient precision. Independent agents challenge the arithmetic hypotheses and normalization. These tasks remain in progress and are not part of this checkpoint's accepted claims.

Postponed: further scans of the failed feature, generic positivity countermodels already covered by Round 8, prime-gap coefficient sweeps, new Fable sessions, and another large PDF rebuild for a negative diagnostic. The 333-page public handoff, 381-page local handoff and 59-page supplement keep their explicit earlier checkpoints. Reverting this research commit removes the new slice without rewriting prior results. The open arithmetic inequalities, rather than the volume of documentation, determine whether the programme advances toward a famous conjecture.


<a id="report-23"></a>

# Current report 23: A concrete 186-to-covariance transfer beyond the square-root divisor level

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/dyson/round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md).

**SHA-256:** `982039f0e163b84c1c5b8f2b52f215eb40e7b89863085f2840c039853606f39a`. **Git blob:** `f09e89d10ab31d35f0d86782d7929a7db26e21f1`. **Original bytes:** 14048.

## A concrete 186-to-covariance transfer beyond the square-root divisor level

Date: 2026-09-05. Status: a proved application of a published distribution estimate, an exact divisor decomposition, and an explicit missing shifted estimate. This does **not** improve a zeta pair-correlation bound or prove the Round 8 target.

The 186 input controls an identifiable part of the additive covariance: the correlation of a prime with a selected Möbius–log divisor sum on complementary, triply densely divisible moduli up to \(X^{0.523}\). The error is \(O_A(X\log^{-A}X)\) per shift, uniformly in the relevant range. This saves enough for shift packets of logarithmically bounded total weight, but the proved bound does not save enough after all \(H=X/T\) shifts are accumulated at the fluctuation scale \(X\log X\).

The application uses the ordinary mathematical theorem in the primary paper. It makes no assertion that every assumption in its Lean formalization has been formally discharged.

### 1. Exact primary input

The primary source is [OpenAI, *Improved short gaps between primes*, 30 August 2026](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf). Printed-page locations are:

- Definition 2.1, p.4: the recursive all-allocation class \(\mathcal D^{(r)}(Y)\).
- Lemma 2.2 and Proposition 2.3, pp.4–5: the cubic prime-factor test and complementary conditions for the actual least common multiple \([D,E]\), including shared primes.
- Equation (2.3), p.6: progression discrepancy with its coprime principal term.
- Equation (2.5), p.7: a coherent primitive class outside the modulus sum, uniform also in the prime set and that class.
- Corollary 2.19, p.11, equations (2.15)–(2.16): full-prime/\(\Lambda\) distribution for order three when \(240\omega+80\delta<3\), uniformly on subintervals.
- Proposition 2.18, pp.10–11, equation (2.14): the underlying multiplicative-convolution bilinear estimate, distinguished from the shifted form in Section 7.

The official repository was previously pinned at commit **61340d0b74163003b32756bb16e91d9209a5e330**. The accompanying JSON hashes the local primary PDF and text; neither is changed here.

Choose

\[
\omega=\frac3{250},\qquad \delta=\frac1{1000},\qquad
\varepsilon=\frac1{1000}.
\tag{1}
\]

Then \(240\omega+80\delta=74/25=2.96<3\), and
\(1/2+2\omega-\varepsilon=523/1000\). Thus, for any finite prime set I and one coherent primitive class \(a\bmod P_I\), the source gives

\[
\sum_{\substack{q\le X^{523/1000}\\q\mid P_I\\
q\in\mathcal D^{(3)}(X^{1/1000})}}
|\Delta(\Lambda\mathbf1_J;a\bmod q)|
\ll_A X(\log X)^{-A}
\tag{2}
\]

uniformly for common subintervals \(J\subset[X,2X)\), where

\[
\Delta(f;a\bmod q)=\sum_{m\equiv a\;(\bmod q)}f(m)
-\frac1{\varphi(q)}\sum_{(m,q)=1}f(m).
\tag{3}
\]

This is not a maximum over unrelated classes inside the modulus sum.

### 2. A complementary modulus family above the square-root range

Use Z for the threshold called X in Proposition 2.3. Set

\[
Y=X^{1/1000},\quad Z=X^{1/2},\quad
A_0=B_0=X^{501/2000},\quad f(p)=g(p)=p^{3/2}.
\tag{4}
\]

Let \(\mathcal Q_X\) be any set of distinct \(q=[D,E]\), with D,E positive and squarefree, satisfying

\[
\begin{gathered}
D,E\le X^{523/2000},\qquad [D,E]>X^{1/2},\\
p^{3/2}D_{\ge p}\le X^{501/2000}\quad(p\mid D,\ p>Y),\\
p^{3/2}E_{\ge p}\le X^{501/2000}\quad(p\mid E,\ p>Y).
\end{gathered}
\tag{5}
\]

The opposite-root guards are automatic because the functions and budgets agree and each owner tail is at least one. Moreover \(A_0B_0=ZY\), \(fg=p^3\), and both functions are nondecreasing. Proposition 2.3 yields

\[
X^{1/2}<q\le DE\le X^{523/1000},\qquad
q\in\mathcal D^{(3)}(X^{1/1000}).
\tag{6}
\]

The condition is \([D,E]>Z\), not \(DE>Z\). Repeated representations of q are counted only once.

This family contains nonsmooth examples for all sufficiently large X. Take distinct primes \(p,r\in[X^{.089},X^{.09}]\) and disjoint squarefree Y-smooth products \(d_0,e_0\in[X^{.170},X^{.171}]\); put \(D=pd_0,E=re_0\). The prime number theorem supplies p,r. To obtain the smooth products, successively multiply unused primes below Y until reaching \(X^{.170}\); each overshoot is at most Y, and the product of the available primes is much larger than \(X^{.342}\). Then

\[
X^{.259}\le D,E\le X^{.261},\quad
X^{.518}\le q=DE\le X^{.522},\quad
p^{3/2}D_{\ge p}=p^{5/2}\le X^{.225}<X^{.2505},
\tag{7}
\]

with the same inequality for r. Only the two large primes activate the predicates. The exact check verifies these exponent margins, not the density of the resulting family.

### 3. The exact divisor piece and a transfer lemma

The elementary convolution identity gives

\[
\Lambda(n)=\sum_{q\mid n}\mu(q)\log(n/q)
=B_{\mathcal Q}(n)+B_{\rm rest}(n),
\quad
B_{\mathcal Q}(n)=
\sum_{\substack{q\mid n\\q\in\mathcal Q_X}}\mu(q)\log(n/q).
\tag{8}
\]

This is a definite Type I divisor piece with a smooth cofactor coefficient \(\log(n/q)\). Both pieces are signed; neither is asserted to be a prime minorant.

Fix C>0 and

\[
X=T^\alpha,\quad \frac65\le\alpha\le\frac75,\quad
H=X/T=X^{1-1/\alpha}\in[X^{1/6},X^{2/7}].
\tag{9}
\]

For \(1\le h\le CH\), let \(w_h\) be real or complex, \(C^1\), and supported in a fixed compact subinterval of \((X,3X/2)\), with

\[
\|w_h\|_\infty+\int|w_h'(u)|du\le C_w
\tag{10}
\]

uniformly in X,T,h. For large X, \(m=n+h\) stays in [X,2X). Define

\[
\mathcal C_{\mathcal Q,h}
=\sum_n\Lambda(n+h)B_{\mathcal Q}(n)w_h(n),
\tag{11}
\]

\[
\mathcal M_{\mathcal Q,h}
=\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}
\frac{\mu(q)}{\varphi(q)}
\int w_h(u)\log(u/q)\,du.
\tag{12}
\]

**Transfer lemma.** Under the published estimate (2), for every fixed A>0,

\[
\boxed{\mathcal C_{\mathcal Q,h}=\mathcal M_{\mathcal Q,h}
+O_A(X\log^{-A}X)}
\tag{13}
\]

uniformly for the stated shifts and weights. This is unconditional when the ordinary distribution theorem is taken as input. RH is needed for the separate zeta correspondence, not this lemma.

The principal term involves only two explicit support sums,
\(\sum_{q\in\mathcal Q_X,(q,h)=1}\mu(q)/\varphi(q)\) and
\(\sum_{q\in\mathcal Q_X,(q,h)=1}\mu(q)\log q/\varphi(q)\).
No limiting evaluation of these sums is claimed. Replacing them with a universal singular-series constant would require another proof.

### 4. Proof, including coherence and prime-power exceptions

For \((q,h)=1\), substitute \(m=n+h\):

\[
\sum_{q\mid n}\Lambda(n+h)w_h(n)\log(n/q)
=\sum_{m\equiv h\;(\bmod q)}
\Lambda(m)w_h(m-h)\log((m-h)/q).
\tag{14}
\]

Let I be the union of primes occurring in the selected moduli, with primes dividing h removed. Then h is one primitive class modulo \(P_I\), restricting coherently to every remaining q. Uniformity in I and h follows from the source's definition (2.5), so (2) applies to this subset.

For weighted partial summation use

\[
w_h(u)\log(u/q)=w_h(u)\log u-(\log q)w_h(u).
\tag{15}
\]

There are just two common endpoint weight functions, with coefficients bounded by \(\log X\). Their sup norms and total variations are \(O(\log X)\). Integrating the source's modulus sum at a **common endpoint** is legal. No sum of separate endpoint suprema is substituted for it. The extra logarithm is absorbed by the arbitrary fixed saving in (2). Thus the coprime part of (11) equals

\[
\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}
\frac{\mu(q)}{\varphi(q)}
\sum_{(m,q)=1}\Lambda(m)w_h(m-h)\log((m-h)/q)
+O_A(X\log^{-A}X).
\tag{16}
\]

The prime number theorem with its classical error smaller than every fixed negative power of log X, followed by partial summation, replaces the unrestricted m-sum by the integral in (12). Summing the errors over q is harmless because
\(\sum_{q\le X^{.523}}1/\varphi(q)\ll\log X\), and the weights cost only fixed logarithmic powers.

Removing \((m,q)=1\) from that principal sum adds prime powers \(m=p^j\asymp X\) with p dividing q. Since \(p\le q<X^{.523}<X\), necessarily \(j\ge2\). Their total von Mangoldt mass is uniformly \(O(\sqrt X\log^2X)\). The logarithmic weight and the sum of \(1/\varphi(q)\) leave an error \(O(\sqrt X\log^{O(1)}X)\), absorbed by the stated error. These are all primes dividing q, not just those dividing h.

The original terms with \((q,h)>1\) are separate. If p divides q,h and q divides n, then \(\Lambda(n+h)\ne0\) forces \(n+h=p^j\), where p divides h. Uniformly for \(h\le CH\), there are \(O(\log^2X)\) such possibilities. For each n, the number of candidate divisors q is at most \(\tau(n)\ll_\eta X^\eta\), for any fixed \(\eta>0\). Their total contribution is \(O_\eta(X^\eta\log^{O(1)}X)\), also absorbed. Thus the nonprimitive terms are estimated, not silently deleted. This proves (13).

### 5. The actual localized Round 7 kernel

For fixed \(\chi\in C_c^\infty(1,3/2)\), put

\[
a_u(X)=\min\{(u/X)^{1/2},(X/u)^{3/2}\},\qquad
\operatorname{sinc}_0(v)=\sin(v)/v,\quad \operatorname{sinc}_0(0)=1,
\]

\[
w_h(u)=\chi(u/X)a_u(X)a_{u+h}(X)
\operatorname{sinc}_0\!\left(T\log(1+h/u)\right).
\tag{17}
\]

For \(h\le CH\), the argument is bounded and its u-derivative is \(O_C(1/X)\). Thus (10) holds uniformly throughout the alpha interval. This signed weight is allowed by the lemma.

The localized off-diagonal prime-prime term in the covariance is exactly

\[
\frac2{X\log T}\sum_{1\le h\le CH}
\sum_n\Lambda(n+h)\Lambda(n)w_h(n).
\tag{18}
\]

Substitution of (8) supplies the selected component (11) and an exact remainder. The factor two accounts for the two orders of each off-diagonal pair. All bounds are uniform for integration against the fixed Round 7 bump in alpha.

This is a stated component of the prime-prime term. Other n-ranges, shifts beyond CH, and the continuous-mean terms of the **centered** covariance have not been discarded.

### 6. A proved summed inequality, and the missing power

For arbitrary complex \(b_h\) supported on \(1\le h\le CH\), (13) gives

\[
\boxed{
\left|\sum_h b_h(\mathcal C_{\mathcal Q,h}-\mathcal M_{\mathcal Q,h})\right|
\ll_A X(\log X)^{-A}\sum_h|b_h|.
}
\tag{19}
\]

In particular, any shift packet with \(\sum_h|b_h|\le(\log X)^B\), B fixed, has error \(o(X\log X)\). This includes logarithmically many sampled shifts anywhere up to CH. It is a valid component-level arithmetic input.

For the whole natural packet \(b_h=1\), this only gives

\[
O_A(HX\log^{-A}X).
\tag{20}
\]

After normalization in (18) it becomes \(O_A(H\log^{-A-1}X)\), which does not tend to zero for any fixed A since \(H\ge X^{1/6}\). Arbitrary fixed logarithmic savings cannot be interpreted as an X-dependent power saving. This diagnoses the limitation of the estimate, not the size of the actual error.

### 7. The first unproved shifted forms

Define the weighted progression discrepancy

\[
\mathfrak D_{\mathcal Q}(X,T)=
\sum_{1\le h\le CH}
\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}
\mu(q)\,
\Delta\!\left(
\Lambda(m)w_h(m-h)\log((m-h)/q);
h\bmod q\right).
\tag{21}
\]

The sequence inside \(\Delta\) is a function of m with finite support. There is an aggregate identity with an error below the covariance scale. Under RH, which is already assumed for the Round 7 zeta correspondence,

\[
\boxed{
\sum_{1\le h\le CH}
(\mathcal C_{\mathcal Q,h}-\mathcal M_{\mathcal Q,h})
=\mathfrak D_{\mathcal Q}(X,T)
+O(H\sqrt X\log^4X).
}
\tag{22}
\]

Indeed the RH estimate \(\psi(y)-y=O(\sqrt y\log^2y)\), with weighted partial summation, gives a principal-term error \(O(\sqrt X\log^3X)\) per q before the factor \(1/\varphi(q)\). Summing that factor costs one more logarithm. The principal-term prime-power deletion has the same upper bound. The original nonprimitive error is \(O_\eta(X^\eta\log^{O(1)}X)\) per h and can be absorbed into this bound by fixing, for example, \(\eta=1/4\). Summation over h proves (22). Since \(H\le X^{2/7}\), its error is \(O(X^{11/14}\log^4X)=o(X\log X)\).

This use of RH is explicit: multiplying only the unconditional per-shift PNT error, however strong in logarithms, by H would not justify the same conclusion.

Consequently an additional estimate

\[
\mathfrak D_{\mathcal Q}(X,T)=o(X\log X),
\quad X=T^\alpha,\quad 6/5\le\alpha\le7/5,
\tag{23}
\]

uniform in alpha, would, under RH, evaluate the whole selected divisor piece at the desired precision. The source supplies only (20). Equation (23) requires cancellation across varying additive residues h, with the specified weight, or another argument of comparable strength.

The untouched divisor remainder is also explicit:

\[
\mathfrak B_{\rm rest}(X,T)=
\sum_{1\le h\le CH}
\sum_{\substack{q,m\ge1\\q\notin\mathcal Q_X}}
\mu(q)(\log m)\Lambda(qm+h)w_h(qm).
\tag{24}
\]

The support makes it finite. This shifted bilinear form is not covered directly by Proposition 2.18: \(\Lambda(qm+h)\) depends jointly on q,m,h and is not an independent coefficient sequence in the multiplicative convolution \(\alpha*\beta\). A Vaughan or Heath–Brown subdivision could reorganize (23), but a bound for the resulting shifted forms would still need proof.

Even (23) would not alone settle Round 7. The remainder (24), the support sums in (12), the omitted ranges, and the continuous centering remain. The actual successful transfer here is (13), (19), and the aggregate identity (22), with every source hypothesis checked; (21), (23), and (24) locate the unproved arithmetic task.

### 8. Verification and stopping point

The companion **check_divisor_bridge.py** uses only the Python standard library. It checks the parameter inequalities and the nonsmooth-family exponent margins with exact fractions. It represents \(\log n\) as a formal prime-log vector, and products as degree-two formal polynomials, to verify the convolution identity, progression reindexing, and the separation into discrepancy, coprime principal term, and nonprimitive contributions on finite examples. There is no floating-point tolerance.

The small examples test algebra and conventions. They do not satisfy the large-X source thresholds and provide no numerical evidence for the distribution theorem or for zeta pair correlations.

No prior round was modified; no prime-gap sweep or new zeta-data fit was performed.


<a id="report-24"></a>

# Current report 24: Independent review of the complementary-modulus covariance component

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/dyson/round9/factorization-covariance/INDEPENDENT_BRIDGE_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/factorization-covariance/INDEPENDENT_BRIDGE_REVIEW.md).

**SHA-256:** `86844e29f08ca834ebdebf04bb7d2df79fa28f37b09bfed2fcc8c5d1534c50b6`. **Git blob:** `ad2752d801935a57097a215f03d98c03b57b70c1`. **Original bytes:** 11399.

## Independent review of the complementary-modulus covariance component

Date: 2026-09-05. Reviewer: the independent residual/arithmetic agent. Reviewed final report: [COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/factorization-covariance/COMPLEMENTARY_MODULI_TYPE_I_BRIDGE.md), SHA256 `982039f0e163b84c1c5b8f2b52f215eb40e7b89863085f2840c039853606f39a`.

**Verdict: accepted as an ordinary application of the stated primary distribution theorem, with the scope of equations (13), (19), and (22) exactly as written.** I found no missing modulus hypothesis, incorrect residue maximum, lost logarithmic weight, or error in the RH aggregate remainder. The comparison to the Round 7 sinc kernel has the correct normalization. This review does not prove or independently reprove the source distribution theorem, certify its formalization, evaluate the remaining shifted discrepancy, or establish a new zeta bound.

The useful output is a selected divisor component with a uniform per-shift estimate, and a separate exact aggregate reduction under RH. The full natural shift packet still requires a new bound. The report correctly keeps that obstruction visible.

### 1. Primary hypotheses and modulus family

I checked the local primary PDF/text pair against the supplied hashes and read the precise source statements: Definition 2.1 and Proposition 2.3 on printed pages 4–5; the discrepancy definition (2.3) on page 6; the coherent-class convention (2.5) on page 7; Proposition 2.18 and Corollary 2.19 on pages 10–11. The primary reference is [Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf).

The parameter choice omega=3/250, delta=1/1000 and epsilon=1/1000 gives 240omega+80delta=74/25<3 and modulus exponent 1/2+2omega-epsilon=523/1000. The source explicitly grants the r=3 estimate for Lambda and uniformly on subintervals, so neither the prime-indicator conversion nor endpoint uniformity is being invented in this application.

The complementary construction uses the actual least common multiple q=[D,E]. Its root budgets satisfy A0 B0=Z Y, and f(p)=g(p)=p^(3/2) are nondecreasing with product p^3. Since the two budgets are equal, each owner inequality also gives the opposite-root guard by dropping the tail factor, which is at least one. Squarefreeness and the strict q>Z assumption are present. Consequently the specified q belong to the source's triply densely divisible class even if D and E share primes. Using DE>Z in place of [D,E]>Z would not have sufficed, but the report does not make that substitution.

Every modulus is counted once. This is essential: no uncontrolled count of its root representations appears in the coefficient. The nonsmooth example is legitimate for sufficiently large X: the needed two large primes exist by the prime number theorem, while the product of unused primes at most X^.001 eventually exceeds any fixed power of X. Greedy disjoint smooth products have the claimed at-most-X^.001 overshoot. The listed exponent inequalities then place the example between X^.518 and X^.522 and satisfy the owner predicates. This proves existence, not density or quantitative usefulness of the selected family.

### 2. Coherent residues and q-dependent weights

Fix h and remove from the prime set every prime dividing h. Each retained q with (q,h)=1 is still a divisor of the new prime product, and h is one primitive residue class modulo that product. Its restrictions are exactly the required classes h mod q. The source's uniformity permits this prime set and coherent class to depend on X and h. The application never uses a maximum over separately chosen classes inside the modulus sum.

The progression reindexing m=n+h is exact. For the weight depending on q, use

    w_h(m-h) log((m-h)/q)
      = F_h(m) - (log q) G_h(m),
    F_h(m)=w_h(m-h)log(m-h),  G_h(m)=w_h(m-h).

These are two common functions of the endpoint, not one unrelated function per modulus. Their sup-plus-variation bounds are O(log X) and O(1), respectively, uniformly in h. The log q coefficient is bounded by .523 log X. Partial summation therefore bounds the discrepancy sum by integrals of the source's sum at a common endpoint. It does not replace a bound on sup_t sum_q |Delta_q(t)| by the stronger and unavailable sum_q sup_t |Delta_q(t)|.

All extra losses here are fixed logarithmic powers and are absorbed by choosing the arbitrary source saving sufficiently large. This proves the weighted coprime progression reduction uniformly for the stated C1 weights, including complex weights by absolute values or separate real and imaginary parts.

### 3. Principal terms and both kinds of prime-power exception

After the distribution step, the principal term carries 1/phi(q). The sum of these factors is O(log X), even for the full available modulus range. One elementary verification is

    sum_(n<=Q) 1/phi(n)
      = sum_(d<=Q) mu(d)^2/[d phi(d)] H_floor(Q/d)
      <= (1+log Q) product_p [1+1/(p(p-1))].

The product converges. Thus one does not pay the number of moduli when replacing the coprime prime sum by its integral.

The unconditional prime number theorem, with a saving stronger than every fixed negative power of log X, suffices for the per-shift result. Multiplying its uniform dyadic error by the O(log X) variation of the weight and the O(log X) inverse-totient sum still yields O_A(X log^(-A) X) after adjusting the initial exponent. This gives precisely the displayed main term, including both support sums with mu(q)/phi(q) and mu(q)log(q)/phi(q). Neither sum is evaluated as a universal singular-series constant.

There are two different exceptional sets, correctly separated in the report:

- Removing (m,q)=1 from the principal sum adds m=p^j around X with p dividing q. Since p<=q<=X^.523<X, these have j>=2. This includes all p dividing q, whether or not p divides h. Bounding by all prime powers gives von Mangoldt mass O(sqrt(X) log^2 X). The additional weight and inverse-totient sum cost at most two logarithms.
- In the original nonprimitive progression terms, a prime p dividing both q and h also divides n+h. If Lambda(n+h) is nonzero, then n+h=p^j with p dividing h. Uniformly for h<=C H there are O(log^2 X) such prime-power possibilities. For each resulting n, the number of allowed divisor moduli is at most tau(n), bounded by O_eta(X^eta). The resulting error is O_eta(X^eta log^O(1) X), for any fixed eta>0.

No nonprimitive main term was silently discarded. Both errors fit the per-shift bound, proving equation (13) given the stated source theorem.

### 4. RH aggregate identity: the square-root error is sufficient

For equation (22), the report appropriately changes its error input. Under RH, psi(y)-y=O(sqrt(y)log^2 y) uniformly on the relevant dyadic interval. Partial summation costs one logarithm and the q principal-term sum costs one more, giving

    O(sqrt(X) log^4 X)

per shift. The principal prime-power deletion obeys this same upper bound. The nonprimitive error can be absorbed by first fixing eta=1/4; any remaining fixed logarithmic power is eventually smaller than the available X^(1/4) margin.

Summing these nuisance errors over h<=C H therefore gives O(H sqrt(X)log^4 X). Since alpha lies in [6/5,7/5], H=X/T<=X^(2/7), so the total is at most O(X^(11/14)log^4 X)=o(X log X), uniformly in alpha. Constants may depend on the fixed compact weight support and C, which the report allows.

This verifies equation (22): the remaining quantity is exactly the sum of the weighted coherent progression discrepancies, not an untracked PNT error. The RH power saving is used only for this principal-term and exception replacement. It does not give a power saving for the progression-discrepancy sum itself. The report correctly warns that multiplying only an unconditional logarithmic per-shift PNT error by H would not justify the same aggregate precision.

### 5. Actual kernel and accumulation at the covariance scale

For fixed alpha and X=T^alpha, the real symmetric Round 7 kernel is

    1/(X T log T) a_u(X)a_v(X) sin(T log(u/v))/log(u/v)
      = 1/(X log T) a_u(X)a_v(X) sinc_0(T log(u/v)).

At v=u+h, sinc_0 is even, so the sign of log(u/v) does not alter the expression. Summing the two orders of an off-diagonal pair yields the stated factor 2. Multiplying by chi(u/X) selects the declared localized component, and subsequent fixed-bump integration in alpha preserves these identities. It does not remove the other components.

On the compact support inside (X,3X/2), both a_u(X) and a_(u+h)(X) lie on their smooth upper branches for large X. Their derivatives are O(1/X). For z=T log(1+h/u), h<=C X/T gives z=O_C(1) and

    z'=-T h/[u(u+h)]=O_C(1/X).

The sinc and its derivative are bounded on that fixed argument range. Hence the weight in (17) has uniformly bounded sup norm and total variation as required; the absolute-value bound does not require it to be positive.

The natural normalized covariance scale is X log T, uniformly comparable to X log X in the stated alpha interval. Equation (19) is the honest consequence of the per-shift estimate: it pays sum_h |b_h|. Logarithmically bounded packets therefore have negligible error at this scale. For the full packet b_h=1, the only available source bound is O_A(H X log^(-A) X), or O_A(H log^(-A-1) X) after covariance normalization. Since H is a fixed positive power of X, no fixed logarithmic saving makes that upper bound tend to zero. This proves insufficiency of that bound, not a lower bound on the actual error.

Thus the proposed new estimate for the aggregate shifted discrepancy, equation (23), remains unproved. Even proving it would only evaluate the selected divisor piece. The unselected divisor sum (24), its main support sums, the omitted n and h ranges, and the continuous centering of the covariance remain genuine obligations. Proposition 2.18 concerns a multiplicative convolution with independent coefficient sequences; it does not directly estimate Lambda(qm+h) as an independent sequence in one variable. The report preserves this distinction.

### 6. Reproduction and claim boundary

I reran the exact script in a temporary directory, with read-only links to the two primary files, leaving the original scripts and outputs unchanged. The 300 formal Mobius-log identities, five progression/discrepancy decompositions and parameter checks passed. At least one example has a nonzero nonprimitive prime-power contribution, so that branch is exercised. Replayed JSON matches the author's JSON exactly after removing only the temporary local source-path strings; no arithmetic field is omitted from the comparison.

The [independent receipt](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/factorization-covariance/independent_bridge_review_receipt.json) pins the final report, script, author JSON and source hashes. The script uses formal prime-log vectors and exact fractions, not floating agreement. These small checks validate identities and conventions; they do not prove any asymptotic distribution estimate or test the large-X support conditions numerically.

The accepted mathematical content is therefore the precise partial-component estimate (13), its weighted packet consequence (19), and the RH aggregate decomposition (22). This is a valid application of the chosen published input beyond a square-root divisor cutoff. It is not a full divisor decomposition estimate, a new Montgomery/Dyson theorem, a new prime-gap bound, or a solution of the two-scale zeta target.


<a id="report-25"></a>

# Current report 25: A fixed interaction between two large prime divisors

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/dyson/round9/multiplicative-profile/DERIVATION.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/DERIVATION.md).

**SHA-256:** `0b717ee45e31abcd399ba48d58069b47bab6b1d9ea5086afed42ca9df6438438`. **Git blob:** `8c52d8da3faab437f6e69ebfed44e804015b5221`. **Original bytes:** 10851.

## A fixed interaction between two large prime divisors

Date: 2026-09-05. Status: written ordinary arithmetic transfer extending the previously reviewed fixed-prime-moment argument. This new note awaits a separate full proof review. The diagnostic is negative and floating; no zeta-spacing theorem or numerical enclosure is claimed.

### 1. Exact arithmetic object

Fix tau=1/3, ell>=1 and a=ell^2. Write d=d_ell, with d(p^e)=(ell)_e/e!, and, for n<=L, define

    v_n=log(n)/log(L),
    S_k(n)=sum_(distinct p|n) (log(p)/log(L))^k, k>=2,
    C_L(n)=number of distinct prime divisors p|n with p^3>L,
    D_L(n)=C_L(n)(C_L(n)-1)/2.

There are at most two such distinct primes. Thus C takes values 0,1,2 and D takes values 0,1, with

    C^2=C+2D,  CD=2D,  D^2=D.

The new coefficient family is

    r_L(n)=d(n) H(v_n,S(n),D_L(n)),
    H(v,S,D)=F(v,S)+D J(v,S),

where F and J are fixed polynomials in finitely many variables. Every H in this family is uniformly bounded on n<=L. Its coefficients, threshold, number of marks and degree remain fixed as L tends to infinity. This is not a growing occupation-state limit.

The trial fixes ell=27/25. F has groups 1,S2,S3,S2^2, each multiplied by the five Legendre polynomials P_j(2v-1), 0<=j<=4. J has groups 1,S2, each multiplied by P_j(6v-5). There are 20 unmarked and 10 D-marked coefficients. The marked radial basis is scaled to [2/3,1], since D vanishes below total mass 2/3.

This D interaction is nonmultiplicative. On configurations with respectively zero, one and two large prime divisors, it takes values 0,0,1. It cannot be introduced by replacing each individual prime by one common scalar multiplier. It also jumps when the second large prime crosses the fixed threshold. No fixed finite polynomial in the continuous S_k variables realizes that jump on the relevant open prime-size configurations. The computational baseline is nevertheless only the specified 20-dimensional span: the new 30-dimensional span does not contain the old best 48-dimensional span.

### 2. Unmarked and singly marked measures

For a labeled index list I=(k_1,...,k_j), put |I|=sum k_i and

    m_I(a) = Gamma(a)/Gamma(a+|I|)
        * sum_(set partitions pi of the labeled indices)
              a^(number of blocks) product_(B in pi) Gamma(sum_(i in B) k_i),
    m_empty(a)=1.

The previously reviewed finite-mark arithmetic argument gives E_v product_i S_(k_i)=v^|I| m_I(a). Here E_v denotes the resulting conditional moment functional, not an assumed random-matrix model. The unmarked positive measures are first defined on all n>=1:

    (log L)^(-a) sum_(n>=1) d(n)^2/n delta_(log(n)/log(L)).

Their local weak limit is C_ell/Gamma(a) v^(a-1) dv. Restriction to v<=1 occurs after this limit; the full measure is not truncated before taking its Laplace transform. Small polynomial marks can be deleted uniformly because sum_(p|n,p<L^epsilon) u_p^k<=epsilon^(k-1). Fix epsilon, use the prime number theorem and the unmarked weak limit on the finite collection of marks, then send epsilon to zero.

For any polynomial P in the S_k, the C-marked limit is

    E_v[C P(S)]
      = a v^(1-a) integral_(tau)^v (v-t)^(a-1)/t
            E_(v-t)[P(S+(t^k)_k)] dt,

with value zero for v<=tau. Unlike the Round 7 threshold 1/2, this is generally an ASYMPTOTIC identity, not an exact coprime decomposition: p>L^(1/3) can divide the remaining factor m when n=pm.

Here is the required error explicitly. For ell>=1, d(pk)<=ell d(k), including when p divides k; hence

    sum_(m<=L,p|m) d(m)^2/m
        <= a/p sum_(k<=L) d(k)^2/k.

The factors H and any fixed polynomial in the marks are bounded, and C<=2 on n<=L. Replacing d(pm)^2 by a d(m)^2 and using the additive mark insertion outside the coprime set therefore costs at most a fixed constant times

    (sum_(k<=L) d(k)^2/k) * sum_(p>L^tau) p^(-2)
       = O_H,ell((log L)^a L^(-tau)).

After normalization this tends to zero. This same estimate handles a large designated prime appearing again among the polynomial background marks. Thus the formula does not import the stronger, false automatic-coprimality statement at the one-third threshold.

### 3. The genuinely new double mark has an exact decomposition

If D_L(n)=1, n has a unique unordered pair p<q of distinct divisors exceeding L^(1/3). Writing n=pqm gives

    m <= L/(pq) < L^(1/3) < min(p,q).

Consequently p and q occur exactly once and are automatically coprime to m. In particular

    d(pqm)^2=a^2 d(m)^2,
    S_k(pqm)=S_k(m)+u_p^k+u_q^k.

For every test polynomial Phi, exactly

    sum_(n<=L) d(n)^2/n D_L(n) Phi(v_n,S(n))
      = a^2 sum_(L^tau<p<q,pq<=L) 1/(pq)
          sum_(m<=L/(pq)) d(m)^2/m
            Phi(v_m+u_p+u_q,S(m)+(u_p^k+u_q^k)_k).

Applying the same finite-product measure limit yields

    E_v[D P(S)]
      = (a^2/2) v^(1-a)
          integral_(t>tau,s>tau,t+s<v)
            (v-t-s)^(a-1)/(ts)
            E_(v-t-s)[P(S+(t^k+s^k)_k)] dt ds.

It vanishes for v<=2tau. The factor 1/2 converts the unique unordered pair into an ordered integral. The removed equal-prime diagonal has an extra reciprocal-prime factor, is O((log L)^a L^(-tau)) before normalization, and also has zero limiting two-dimensional measure.

All prime thresholds stay fixed. The planes t=tau, s=tau, t+s+v=1, and the corresponding operator-insertion planes have zero limiting measure. No uniform pointwise estimate for every short background cutoff is asserted: use the joint product-measure weak limit first, restrict away from the total-mass boundary, and then remove this restriction. The residual density w^(a-1) is locally integrable for a>0; the already available uniform total-mass bound controls the discarded shrinking background strip. This includes m near one.

### 4. Insertions and the three-state interpolation

Let chi(u)=1_(u>tau). For a prime multiplier not already dividing the input integer,

    C -> C+chi(u),
    D -> D+C chi(u).

For two distinct new prime multipliers,

    C -> C+chi(u)+chi(w),
    D -> D+C(chi(u)+chi(w))+chi(u)chi(w).

The polynomial S_k inserts u^k, or u^k+w^k, as usual. Define H0, Hu, Hw and Huw by these exact rules together with their total-mass arguments v, v+u, v+w and v+u+w.

The code does not treat C as binary. For an insertion product q(C)P(S), its three possible background values determine it exactly:

    E_v[q(C)P(S)] = q(0) E_v[P]
       + (q(1)-q(0)) E_v[C P]
       + (q(2)-2q(1)+q(0)) E_v[D P].

For marked factors on the left and right, the code sets

    q(c) = choose(c+number of large left insertions,2)^(left mark)
           * choose(c+number of large right insertions,2)^(right mark).

The exponents are zero or one. The interpolation identity is only used at c=0,1,2, where it is exact even if the expression for q is a higher-degree polynomial. Impossible background/insertion configurations have zero measure by the total-mass constraint. This construction retains the mixed terms involving a single background large prime as well as the event with two large inserted primes.

### 5. The arithmetic limiting quadratic forms

For x_n=r_L(n)/sqrt(n), retain the exact arithmetic creation matrix

    (A_L)_(p^e m,m)
      = 2 sin(pi e log(p)/(2log(L)))/(e sqrt(p^e)),  p^e m<=L.

Define

    I = integral_0^1 v^(a-1) E_v[H0^2] dv,

    M2 = (2 ell^2/pi^2) integral_(v+u+w<=1)
            v^(a-1) sin(pi u/2)/u sin(pi w/2)/w
            E_v[H0 Huw+Hu Hw] dv du dw,

    M3 = (2/pi^2) integral_(v+u<=1)
            v^(a-1) sin^2(pi u/2)/u E_v[H0^2] dv du.

Then, for fixed H with I>0,

    [||A_L x||^2+x^T A_L^2 x]/[2pi^2 ||x||^2]-1/4
       -> (M2+M3)/I-1/4.

The inherited proof is applicable because the added marks are bounded and their thresholds fixed. More explicitly, remove operator primes below L^epsilon and prime powers with e>=2 using the previously proved weighted Schur bounds, valid uniformly for arbitrary signed vectors:

    ||A_L||=O_ell(1),
    ||A_(p<L^epsilon)||=O_ell(sqrt(epsilon)+(log L)^(-1/2)),
    ||A_(e>=2)||=O_ell((log L)^(-1/2)).

The standard norm inequalities for A*A and A^2 show that the normalized quadratic forms change by o(1)+O(sqrt(epsilon)). With retained primes, collisions with the background or another designated prime have the reciprocal-square error just described. The fixed polynomial marks and bounded C,D do not invalidate that estimate. The ordered distinct-prime terms then use d(mp)d(mq)=a d(m)^2 and d(m)d(mpq)=a d(m)^2 on the coprime part, yielding the two terms of M2 with the displayed coefficients.

There are two different diagonals. In A*A, p=q gives r_L(m)^2/(mp) and survives: this is M3 with uninserted H0 squared. In A^2, repeated p gives the extra p^(-2) and vanishes after the retained-prime restriction. No g(u)^2 or inserted D is attached to M3. First let L tend to infinity at fixed epsilon, then send epsilon to zero. This completes the written fixed-family extension; it has no growing-family or uniform-in-degree assertion.

The source interface remains Inoue, arXiv:2604.05733v1, Theorems 3 and 4 / combined Proposition 3 under RH, with L=floor(T/(log T)^2). The previously audited coefficient-uniform normalized error and theta=log L/log T ->1 comparison are unchanged by this bounded fixed resonator. A positive limiting margin could feed that source argument. The present negative trial supplies no such consequence. In particular it supplies neither a gap bound nor an AH refutation; multiplicities and near-zero AH pairs would still need the correct treatment after any future successful small-gap argument.

### 6. Quadrature and verification boundary

For the C moment set delta=v-tau and t=v-delta z. Its endpoint factor is delta^a; the remaining z integral has Jacobi weight z^(a-1). For the D moment put

    delta=v-2tau,
    t=tau+delta(1-z)s,
    w=tau+delta(1-z)(1-s),
    background=delta z.

The Jacobian is delta^2(1-z), so the endpoint factor is delta^(a+1), with residual weight z^(a-1)(1-z)/(tw). The coefficient remains a^2/2. These are the substitutions implemented in `marked_values`.

The v integration is divided at tau and 2tau. For each v slab, the u integration is divided at tau and 1-v-tau in their correct order, and the w integration is divided at tau where present. No positive-weight quadrature cell straddles an inserted-prime step. The v endpoint powers above are absorbed by Jacobi rules. Norm and M3 use the same three-state decomposition with no inserted large primes.

This is deterministic quadrature, not a rigorous error enclosure. A 20/32 comparison and independent raw adaptive integrals check its implementation but do not certify the small observed gain. The separate exact checks establish finite arithmetic identities only. Full coefficients, M/G arrays, a frozen rational vector and the actual-integer operator evaluation are retained; none of these numeric checks is substituted for the transfer argument.


<a id="report-26"></a>

# Current report 26: Round 9: duplicate profile avoided, two-prime interaction tested

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/dyson/round9/multiplicative-profile/REPORT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/REPORT.md).

**SHA-256:** `ecc98ab471b4e0b24516d0315a59481a3e8b76140543a52dade81f1bb917fa84`. **Git blob:** `e97c09952b23aa1a1e5efe28733c4b211eddcc71`. **Original bytes:** 9353.

## Round 9: duplicate profile avoided, two-prime interaction tested

Date: 2026-09-05. This directory keeps its initially assigned `multiplicative-profile` name so the task history and dependency paths remain traceable. The actual new experiment is a nonmultiplicative interaction between two distinct large prime divisors.

**Outcome:** the fixed 30-dimensional interaction trial has floating half-gap margin **−0.0146549114371551**. It does not cross zero and remains worse than the old 48-feature best value, approximately −0.0146547256. The written arithmetic extension is in [DERIVATION.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/DERIVATION.md); separate independent review is pending. There is no new zeta theorem, no certified optimizer, and no global obstruction theorem.

### 1. The archive check changed the task before computation

The initial suggestion was a multiplicative prime-size profile such as a product of exp(sum c_k u_p^k), summing all mark orders. The public Round 2 report `research/reports/resummed_prime_profiles.md` and scripts `research/prime-profiles/euler_profile_precise.py/.json` already implement precisely that mechanism. Their convolution-density recurrence resums all powers, rather than merely taking the old finite S2/S3 span. Recorded cases include one, two, three and five exponent coefficients, through u^6. The best validated local continuation was approximately −0.0146638632200778, with radial degree 9 and quadrature order 40; it was a continuum calculation with 110/140-term density comparison, not a completed all-orders arithmetic remainder theorem.

The literal product of (1+eta u_p^2) was not located as an executed trial. It would be inaccurate to claim that every such parameter was already tested. But its multiplicative one-prime mechanism is not new relative to the existing resummed Euler-profile approach. Under the task's stop-on-duplication instruction, no new exponential-profile or eta scan was run.

The old Fock report contains broad bin-occupation states, but explicitly keeps its general operator-transfer issue separate. That is not a prior fixed-integer test of the new D mark below. Searches of the existing research reports and Round 7 arithmetic derivation found no earlier implementation of this fixed two-large-prime interaction. This is an archive-coverage statement, not a mathematical novelty claim.

### 2. What was actually added

For n<=L set

    D_L(n)=1 if at least two DISTINCT prime divisors p of n satisfy p^3>L,
           0 otherwise.

There are at most two. When D=1, the unique unordered pair p<q gives n=pqm with m<L^(1/3)<min(p,q), so the new double-mark starting identity is exact and automatically coprime. The singly marked background count C also occurs in mixed insertions; its one-third-threshold formula needs the explicit repeated-prime error in the derivation and is not mislabeled exact.

The new span has ell=27/25, radial degree four, the same 20 unmarked features as the matched Round 7 baseline, and ten D-marked features: D times 1 or S2, with radial basis P_j(6v-5). The mark is an interaction: adding the first large prime leaves it zero, while adding a second switches it on. A three-state interpolation in the background count C supplies the mixed insertion forms. All thresholds and coefficient counts stay fixed in the arithmetic limit.

The matrices are newly integrated for this mark. Only generic labeled-partition moments, polynomial insertion expansion, Gauss-Jacobi nodes and the generalized-eigenvalue helper are imported from the pinned Round 7 script. The old marked matrices and the prime-gap 77-dimensional problem are not reused.

### 3. The bounded numerical decision

| Fixed trial | Order 20 margin | Order 32 margin |
|---|---:|---:|
| Matched 20 unmarked features | −0.0146549380840023 | −0.0146549380840028 |
| New 30-feature D interaction | −0.0146549114371546 | −0.0146549114371551 |

At order 32 the observed gain over its matched baseline is about 2.66468477e−8. The new value is still roughly 1.858e−7 below the old 48-feature best, and about 0.01465 short of the required zero margin. Those comparisons are numerical only; the larger historical span is not nested in this new 30-dimensional span.

The diagonally scaled mass Gram condition is approximately 5.35731565e7 for the enlarged span. All 30 directions survive the fixed 1e−11 relative eigenvalue cutoff. The final floating pencil residual norm is approximately 2.52e−16 and the mass norm is 1 to rounding. A tiny residual verifies a floating solve, not the correctness of its quadrature or an enclosure of the top eigenvalue. In particular the 2.66e−8 gain is not advertised as certified. The negative main deficit is much larger than that gain.

The baseline M/G blocks independently agree with the existing Round 7 order-40 unmarked blocks to maximum absolute differences 8.33e−16 and 2.22e−15. The two new quadrature orders agree in the enlarged margin to about 5.6e−16. No further degree increase, threshold change, parameter sweep or optimization of ell was performed.

### 4. Fixed vector and independent checks

[fixed_rational_vector.json](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/fixed_rational_vector.json) contains all 30 integer coefficients with denominator 100000000, the exact ell and threshold, the complete ordered feature list and radial conventions. Its continuum quadrature margin is −0.0146549114371553. Its polynomial value at v=S=D=0 is exactly 155237743/100000000, so it is nonzero; positivity of the limiting mass follows already on a sufficiently small unmarked total-mass interval. The nonzero norm is not based solely on the numerical Gram matrix.

[check_two_prime_trial.py](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/check_two_prime_trial.py) records the following in [validation.json](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/validation.json):

- At integer cutoff 120, an exact Fraction identity matches all 12 unique unordered two-large-prime decompositions and their coefficient factor a^2.
- The two insertion identities and divisor factors pass on 132 ordered coprime insertion triples.
- The Newton interpolation in {1,C,D} passes 108 exact state checks, keeping C=2 distinct from C=1.
- At a=(27/25)^2 and total mass v=.91, two independent nested adaptive integrations of the raw E[D] and E[D S2] formulas agree with the substituted Jacobi expressions within 1.11e−16 and 5.56e−17. These are floating checks of different integration formulas, not interval certificates.
- A single actual-integer calculation at L=100000 uses the frozen vector and every prime-power entry of A_L. It has 11109 integers with D=1, 343614 matrix nonzeros, norm about 20.46127, A*A/norm about 3.02145870, A^2/norm about 1.17491031 and margin **−0.0374094621535042**. It is a finite arithmetic calculation at theta=1, not a zeta-zero sample or proof of an asymptotic rate.

The exact checks deliberately use rational formal prime labels for polynomial identities. They do not claim that log(p)/log(L) is rational or replace the actual logarithms used by the final finite-integer evaluation.

### 5. Files, reproduction and limitations

The two computation files are [two_large_prime_sector.py](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/two_large_prime_sector.py) and [check_two_prime_trial.py](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/check_two_prime_trial.py). The former produces complete `two_large_prime_d4_q20.json/.npz` and `two_large_prime_d4_q32.json/.npz`; each NPZ retains the full symmetric numerator M and mass G. The latter freezes the rational vector and writes the validation record. A small [manifest.json](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/manifest.json) pins the new outputs and the relevant archived source files.

From this directory, with Python, NumPy and SciPy:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 two_large_prime_sector.py --order 20
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 two_large_prime_sector.py --order 32
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 check_two_prime_trial.py
```

The environment variable `ASTRA_LARGE_PRIME_SOURCE` can point to the pinned Round 7 `large_prime_sector.py`. Its expected SHA256 is checked before import. The current default is the local public-repository path; a publication copy may replace that default with a portable repository-relative path and must record that change explicitly. The old imported file is not edited. The only output fields expected to vary on replay are recorded run times, runtime/version metadata if added, and environment-dependent floating differences; an identical environment can demand exact arrays as a stronger diagnostic. No speed claim is made from these small local run times.

The arithmetic-transfer argument uses existing fixed-moment asymptotics and uniform operator truncations, plus the explicit new count identities. It does not assume a global Fock limit or an unsupported all-orders coefficient limit. The optimization and the finite-integer sine calculations remain ordinary floating arithmetic. Review of the new proof and code is separate from numerical agreement, and no external novelty or formal verification claim is made.

This round is closed at a useful negative decision. It rules out neither other nonmultiplicative arithmetic features nor the full resonance method. Repeating the old exponential profile, adding more digits to this small gain, or treating it as evidence toward a historic conjecture is postponed. Further work needs a quantitatively different arithmetic direction or a new estimate for the actual out-of-band covariance.


<a id="report-27"></a>

# Current report 27: Independent review: the fixed two-large-prime interaction

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/dyson/round9/multiplicative-profile/INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/multiplicative-profile/INDEPENDENT_REVIEW.md).

**SHA-256:** `b88133d0b6dbd38d3c1a4c7a8fb70599ce6ef7968297a05f21105682c7ae6997`. **Git blob:** `324021cc5d9aedd7513274395c0f10ff4ce6965a`. **Original bytes:** 4454.

## Independent review: the fixed two-large-prime interaction

Date: 2026-09-05. Reviewer: the root research lane, independently of the author. **Accepted as an ordinary fixed-family arithmetic extension and a negative floating experiment.** No interval certification, external novelty claim, or new zeta theorem is accepted or implied.

Reviewed author files:

- `DERIVATION.md`: SHA256 `0b717ee45e31abcd399ba48d58069b47bab6b1d9ea5086afed42ca9df6438438`.
- `two_large_prime_sector.py`: SHA256 `ed6fa274593a04d8a168a8597c76a994ad0595edb337995a7904a93b6a845de0`.
- `check_two_prime_trial.py`: SHA256 `61c4c5c92b5d502670fbf469fe61d422f69778369125ff569a28418aa3dab9ff`.

The root read the complete derivation, report, and two scripts. The review uses the previously independently reviewed Round 7 fixed-moment and weighted Schur estimates as inputs; it does not supply a new proof of those inherited results or a general Fock-space limit.

### Arithmetic checks independent of the optimizer

1. For two distinct prime divisors exceeding L^(1/3), their product leaves a cofactor less than either prime. The unordered double-mark decomposition, the coefficient a², and the factor 1/2 in the ordered limiting integral are correct. Three such distinct primes cannot divide n<=L.
2. A *single* designated prime at this threshold need not be coprime to the cofactor. The author handles this explicitly. For ell>=1, the ratio d_ell(p^(e+1))/d_ell(p^e)=(ell+e)/(e+1) is at most ell. Hence the background repeat estimate has an extra 1/p, and summing designated primes supplies sum p^(-2)=O(L^(-1/3)). Bounded fixed marks preserve this estimate. No automatic-coprimality claim is imported from the older threshold 1/2.
3. C is three-valued, while D is binary. The identities C²=C+2D, CD=2D, D²=D and the three-state Newton interpolation are correct. The two insertion rules include the mixed term from one old and one new large prime, as well as the event with two newly inserted large primes. Infeasible states disappear through total mass, not an artificial truncation of C.
4. The measure used before the Laplace limit is on all n>=1. Restriction to total mass at most one follows the weak limit. Fixed threshold planes have zero limiting measure, and the locally integrable residual density controls the small-cofactor strip. This avoids a false pointwise uniform asymptotic at a cofactor cutoff near one.
5. The bounded, fixed coefficient family permits the inherited signed operator truncations. The distinct-prime terms produce H0 Huw and Hu Hw. The A*A same-prime term survives with uninserted H0²; the repeated-prime term in A² has the extra reciprocal-prime factor and vanishes. The displayed M2/M3 constants agree with the actual creation matrix normalization.

### Implementation and interpretation

The two-mark substitution has Jacobian delta²(1-z), residual density (delta z)^(a-1), and denominator tw, giving exactly delta^(a+1) z^(a-1)(1-z)/(tw). The one-mark endpoint exponent is a. The code divides the total-mass and insertion domains at each fixed threshold and uses the corresponding Jacobi factors. Its coefficient interpolation keeps all three background count states.

The rational frozen vector is nonzero without appealing to a numerical Gram matrix: its unmarked value at the origin is 155237743/100000000. Continuity then gives a positive limiting norm on a sufficiently small unmarked interval.

The reported margin is approximately -0.0146549114371551. The observed 2.66e-8 improvement over the matched baseline is not certified, especially with a diagonally scaled Gram condition near 5.36e7. The full negative deficit is about 0.01465. The new span does not contain the earlier best 48-feature span, and its value is worse than that historical result. Thus this fixed trial supplies no small-gap or AH consequence. It also does not rule out a different interaction, a larger coefficient space, or the resonance method.

Finite exact checks validate the stated identities and cutoff conventions; quadrature agreement and the finite-integer experiment validate specific implementations. They do not prove the asymptotic transfer. Independent integration replay and full-array comparisons are recorded separately when this folder is published.

The author files retain their historical “review pending” wording. This separately hashed review records their later acceptance without silently rewriting the original research record.


<a id="report-28"></a>

# Current report 28: Prime powers are negligible in the remaining residual energy

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/dyson/round9/prime-power-removal/PRIME_POWER_TAIL_ESTIMATE.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/prime-power-removal/PRIME_POWER_TAIL_ESTIMATE.md).

**SHA-256:** `e7fff21fa21285a20968c218e99b17b3bc634bf28b88268c002f406a0fdd6cd0`. **Git blob:** `55d4fa8c233145abee92164b9546cd1fcd231f33`. **Original bytes:** 8037.

## Prime powers are negligible in the remaining residual energy

Date: 2026-09-05. Status: ordinary proof draft for independent review. This is a quantified nuisance-term estimate, not a new lower bound for the signed residual and not a conjecture solution. Its purpose is to let the remaining covariance calculation use genuine primes.

### 1. Statement

Fix c>0, let T tend to infinity, and set

    delta=c/log T, sigma=1/2+delta, s=sigma+it,
    N=floor(T/log^6 T).

Let H=-zeta'/zeta(s), P_N=sum_(n<=N) Lambda(n)n^(-s), and R=H-P_N as in Round 8. Define the absolutely convergent prime-power tail

\[
U_{c,N}(t)=\sum_{\substack{p\ \mathrm{prime},\ k\ge2\\p^k>N}}
       (\log p)p^{-k\sigma-ikt\log p}.
\]

Uniformly for 0<delta<=1/4 and N>=4,

\[
\boxed{\|U_{c,N}\|_{L^2(0,T)}^2
\ll T N^{-1/3}\log^4(2N)+\delta^{-4}.}
\tag{1}
\]

The implied constant in (1) is absolute. The estimate itself does not assume RH. Under RH, the normalized residual energy changes by

\[
\boxed{\frac{\big|\|R-U_{c,N}\|_2^2-\|R\|_2^2\big|}
 {T\log^2T}
\ll_c N^{-1/6}\log^2(2N)+\frac{\log^2T}{\sqrt T}=o(1).}
\tag{2}
\]

Consequently the fixed two-scale residual in Round 8 can be replaced by its genuine-prime counterpart. Equation (2) is a bound on the replacement error; it gives no positive constant improvement in the desired signed comparison.

### 2. Squares: an elementary mean-value bound with an infinite tail

Write U_2(t)=sum_(p>sqrt N) (log p)p^(-1-2delta-2it). For the sequence

    a_n = (log n)n^(-1-2delta) if n is a prime greater than sqrt N,
          0 otherwise,

the series is absolutely convergent. Expanding the time integral, the diagonal is T sum |a_n|^2. The integrated off-diagonal kernel has absolute value at most 1/|log(m/n)| because the time frequency is 2log(m/n).

For n/2<=m<=2n, m!=n, uniformly in 0<delta<=1/4,

\[
\frac{|a_ma_n|}{|\log(m/n)|}
\ll \frac{\log^2(2n)}{n^{1+4\delta}|m-n|}.
\]

Summing the harmonic denominator over m and then over n gives

\[
\ll\sum_{n\ge2}\frac{\log^3(2n)}{n^{1+4\delta}}
\ll \delta^{-4}.
\]

For noncomparable m,n, the log denominator is at least log 2, so the contribution is at most a constant times

\[
\left(\sum_{n\ge2}\frac{\log n}{n^{1+2\delta}}\right)^2
\ll\delta^{-4}.
\]

These are convergent majorants for each delta>0. One may therefore first use finite sums and pass to the infinite sum by dominated convergence. No infinite polynomial mean-value theorem with a divergent error is invoked.

The diagonal tail satisfies

\[
\sum_{p>\sqrt N}\frac{(\log p)^2}{p^{2+4\delta}}
\le\sum_{n>\sqrt N}\frac{(\log n)^2}{n^2}
\ll N^{-1/2}\log^2(2N).
\]

Thus

\[
\|U_2\|_2^2\ll T N^{-1/2}\log^2(2N)+\delta^{-4}.
\tag{3}
\]

In particular, the exponent four in the error is intentional. A sharper Hilbert-inequality estimate is unnecessary for this use. The argument above is self-contained and only uses the actual support of prime squares and elementary upper bounds for their weights.

### 3. Higher powers: absolute convergence is now strong enough

Let

\[
A_3(x)=\sum_{\substack{p^k\le x\\k\ge3}}\log p.
\]

There are at most log(x)/log(2) relevant exponents, and for each k>=3 the number of possible bases is at most x^(1/3), with log p<=log x. Hence, for x>=2,

\[
A_3(x)\ll x^{1/3}\log^2(2x).
\]

Partial summation and sigma>=1/2 yield

\[
\sum_{\substack{p^k>N\\k\ge3}}(\log p)p^{-k\sigma}
\le \sigma\int_N^\infty A_3(x)x^{-\sigma-1}dx
\ll N^{-1/6}\log^2(2N).
\tag{4}
\]

For the last bound sigma is in [1/2,3/4], so sigma-1/3 is bounded below by 1/6 and all integration constants are uniform. The negative endpoint term from partial summation was discarded in the favorable direction. Equation (4) gives

\[
\|U_{\ge3}\|_2^2\ll T N^{-1/3}\log^4(2N).
\]

Combining this with (3), using |u+v|^2<=2|u|^2+2|v|^2, proves (1). Squares require a mean-square argument; applying the same absolute-value argument to squares would lose the useful decay.

### 4. Replacement in the actual RH residual

The pointwise RH partial-fraction bound already proved in Round 8 gives H(t)=O_c(log^2 T) throughout [0,T]. The elementary finite-polynomial mean-value bound there gives ||P_N||_2^2=O_c(T log^4 T). Consequently

    ||R||_2 <= C_c sqrt(T) log^2 T.

Set a_T=N^(-1/6)log^2(2N)+log^2(T)/sqrt(T). Equation (1), with delta=c/log T, gives ||U||_2/sqrt(T) <<_c a_T. By Cauchy-Schwarz,

\[
\frac{\big|\|R-U\|_2^2-\|R\|_2^2\big|}{T\log^2T}
\le\frac{2\|R\|_2\|U\|_2+\|U\|_2^2}{T\log^2T}
\ll_c a_T+\frac{a_T^2}{\log^2T}.
\]

Since a_T tends to zero at the stated cutoff, this proves (2) for sufficiently large T. The stronger RH pair-correlation bound on ||H|| is not needed. The same argument applies separately to c=1 and c=1/2, whose fixed hyperbolic coefficients preserve the o(1) replacement error.

### 5. The remaining error really is the prime-counting error

Define theta(x)=sum_(p<=x) log p and E_1(x)=theta(x)-x. Subtracting the absolutely convergent prime-power series from the usual Stieltjes continuation gives

\[
R-U_{c,N}
=\frac{N^{1-s}}{s-1}-E_1(N)N^{-s}
 +s\int_N^\infty E_1(x)x^{-s-1}dx.
\tag{5}
\]

The finite polynomial on the left now removes only the primes up to N from the prime-only analytic continuation: explicitly it is

    H(s) - sum_(p,k>=2) (log p)p^(-ks) - sum_(p<=N) (log p)p^(-s).

This equals R-U by cancellation of the prime powers up to N. At integer N the theta endpoint includes a prime at N. RH and the elementary prime-power counting bound imply E_1(x)=O(sqrt(x)log^2(2x)), so the integral in (5) is absolutely convergent when Re(s)>1/2. The pole can be removed from the normalized energy as in Round 8.

Thus the non-negligible unknown comparison involves the same genuine-prime error theta(x)-x at the two damping widths. Neither prime powers nor a convention at a prime-power cutoff can supply the missing fixed positive gap above the AH value. A new additive-prime covariance estimate is still required.

### 6. Scope and provenance

The RH inputs are the logarithmic-derivative and prime-counting-error bounds already used and reviewed in Round 8. The prime-power estimates use arithmetic sparsity and elementary series estimates, not a generic point-process positivity assumption. No experimental optimization or new scalar-constant certificate was run for this lemma. An independent ordinary-proof review is required before its status is upgraded.

The resulting error tends to zero and hence leaves the numerical target unchanged. This is a cleanup estimate for the hard arithmetic problem, not progress toward 1/16 by itself and not an assertion of novelty for prime-power removal.


### 7. Uniform corollary for the mesoscopic two-width statistic

Put L=log T. The bound in (2) has an absolute implied constant throughout

\[
1\le c\le L/4.
\]

Indeed delta>=1/L makes delta^(-4)<=L^4 in (1). The RH partial-fraction bound for the logarithmic derivative is O(L²) uniformly at distance at least 1/L to the right of the critical line, throughout 0<=t<=T and 1/2+1/L<=sigma<=3/4. The same elementary bound for the finite polynomial is uniform because its coefficients only decrease as sigma increases. The argument in Section 4 therefore gives a uniform O(a_T) replacement error, where

\[
a_T=N^{-1/6}\log^2(2N)+L^2T^{-1/2}
\ll T^{-1/6}L^3+T^{-1/2}L^2.
\]

Write r_T(b)=||R_(b/2)||²/(TL²), and let r_T^prime(b) be the same normalized energy with U_(b/2,N) subtracted. Define

\[
\mathcal C_T(b)=b^2\left[2\sinh(b)r_T(b)
-2\sinh(2b)r_T(2b)-\frac1{2b}\right],
\]

and define its prime-only version by substituting r_T^prime. For b>=2 and b=o(log L), both c=b/2 and c=b are in the uniform range, and

\[
\boxed{|\mathcal C_T^{\rm prime}(b)-\mathcal C_T(b)|
\ll b^2e^{2b}a_T=o(1).}
\tag{6}
\]

The conclusion is uniform on any range 2<=b<=G(T) with G(T)=o(log L): the exponential factor is only L^(o(1)), whereas a_T has a negative power of T. Thus the mesoscopic arithmetic target can also be stated using the genuine-prime continuation. This corollary removes a nuisance term at the amplified scale; it supplies no lower bound on either statistic.


<a id="report-29"></a>

# Current report 29: Independent review of the actual prime-power tail estimate

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/dyson/round9/prime-power-removal/INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/prime-power-removal/INDEPENDENT_REVIEW.md).

**SHA-256:** `0650ede489f745fa0eea7d7761ccd356f86b2eca7f9e5a5858d63bab644dcbb6`. **Git blob:** `5454bb68fd06136b20d51e1f747daecbbf614b32`. **Original bytes:** 8940.

## Independent review of the actual prime-power tail estimate

Date: 2026-09-05. Reviewer: `yau_flow`, separately from the authoring coordinator.

Reviewed final author artifact: `PRIME_POWER_TAIL_ESTIMATE.md`, SHA-256 `e7fff21fa21285a20968c218e99b17b3bc634bf28b88268c002f406a0fdd6cd0`. The initial complete review covered the corrected six-section version `b28cc13877d38d7cc83956127ace275df1f87585df8f2905fc309e77ae6d2349`; the final appended uniform corollary and corrected formula markup were subsequently read and accepted. Section 7 below records the independent derivation of that corollary.

**Verdict:** the tail estimate, residual-energy replacement, and exact genuine-prime continuation are accepted as ordinary mathematical arguments. No missing endpoint, square-frequency factor, or uncontrolled infinite off-diagonal sum was found. The author has corrected the minor provenance sentence to acknowledge the RH prime-counting-error estimate as well as the logarithmic-derivative estimate. No numerical scan or new experiment was run.

### 1. Scope of the unconditional estimate

For \(0<\delta\leq1/4\), \(\sigma=1/2+\delta\), \(N\geq4\), and \(T>0\), the series
\[
U(t)=\sum_{p^k>N,\ k\geq2}(\log p)p^{-k\sigma-ikt\log p}
\]
converges absolutely and uniformly in real \(t\) for each fixed \(\delta>0\). The sum over squares is majorized by \(\sum_{n\geq2}(\log n)n^{-1-2\delta}\); the higher powers converge even at \(\delta=0\). The claimed uniform estimate
\[
\|U\|_{L^2(0,T)}^2
\ll T N^{-1/3}\log^4(2N)+\delta^{-4}
\tag{1}
\]
does not use RH. Uniformity means the implied constant is independent of \(\delta,N,T\) in the displayed range, not that the second term remains bounded as \(\delta\downarrow0\).

### 2. Squares: frequency and infinite near-diagonal terms

For prime squares, the coefficients are
\(a_p=(\log p)p^{-1-2\delta}\), and the time phase is \(e^{-2it\log p}\). Therefore
\[
\left|\int_0^T e^{2it\log(m/n)}dt\right|
\leq\frac1{|\log(m/n)|}
\]
for \(m\ne n\). The factor one, rather than two, is correct because of the square frequency.

If \(n/2\leq m\leq2n\), then
\(|\log(m/n)|\geq|m-n|/(2n)\). Uniformly in the allowed \(\delta\),
\[
\frac{|a_ma_n|}{|\log(m/n)|}
\ll\frac{\log^2(2n)}{n^{1+4\delta}|m-n|}.
\]
The remaining harmonic sum costs \(O(\log(2n))\), giving
\[
\sum_{n\geq2}\frac{\log^3(2n)}{n^{1+4\delta}}
\ll\delta^{-4}.
\]
The comparison follows directly from integrals of \((\log x)^j x^{-1-4\delta}\), \(0\leq j\leq3\). Their powers \(\delta^{-j-1}\) are all absorbed by \(\delta^{-4}\) on \(0<\delta\leq1/4\). This checks the deliberate fourth power of the error.

For noncomparable pairs the denominator is bounded below by \(\log2\). The product majorant is
\[
\left(\sum_{n\geq2}\frac{\log n}{n^{1+2\delta}}\right)^2
\ll\delta^{-4}.
\]
Both estimates legitimately enlarge prime sums to integer sums and remove the cutoff. Every resulting series converges for each positive \(\delta\). Finite partial sums can consequently be passed to the infinite series without invoking a mean-value theorem with divergent error.

The diagonal is bounded by
\[
T\sum_{p>\sqrt N}\frac{(\log p)^2}{p^{2+4\delta}}
\ll T N^{-1/2}\log^2(2N).
\]
This proves the square part of the author's estimate, including its normalization and uniformity.

### 3. Higher powers and the endpoint sign

For \(A_3(x)=\sum_{p^k\leq x,k\geq3}\log p\), the elementary bound
\(A_3(x)\ll x^{1/3}\log^2(2x)\) is valid: there are at most \(O(\log x)\) exponents, at most \(x^{1/3}\) bases for each, and each weight is \(O(\log x)\). No prime-counting asymptotic is assumed.

The exact partial-summation formula for the strict tail is
\[
\sum_{p^k>N,k\geq3}(\log p)p^{-k\sigma}
=-A_3(N)N^{-\sigma}
 +\sigma\int_N^\infty A_3(x)x^{-\sigma-1}dx.
\]
The endpoint term is nonpositive and can be discarded in this upper bound. This remains correct when \(N\) itself is a prime power, provided \(A_3(N)\) includes that atom, as the definition does.

Since \(\sigma-1/3\geq1/6\), the integral is
\(O(N^{-1/6}\log^2(2N))\) uniformly for \(\sigma\in(1/2,3/4]\). Squaring the resulting uniform-in-time bound gives
\(O(TN^{-1/3}\log^4(2N))\). Combining the square and higher-power estimates with \(|u+v|^2\leq2|u|^2+2|v|^2\) proves (1). Prime powers have a unique prime base; there is no duplicate counting between the \(k=2\) and \(k\geq3\) pieces.

### 4. Replacement in the actual residual

Now set \(\delta=c/\log T\), with fixed \(c>0\), and \(N=\lfloor T/\log^6T\rfloor\). Under RH, the already proved bound
\(\|R\|_2\ll_c\sqrt T\log^2T\) applies. Taking a square root in (1) gives
\[
\frac{\|U\|_2}{\sqrt T}
\ll_c a_T:=N^{-1/6}\log^2(2N)+\frac{\log^2T}{\sqrt T}.
\]
The exact norm expansion and Cauchy–Schwarz yield
\[
\frac{|\|R-U\|_2^2-\|R\|_2^2|}{T\log^2T}
\ll_c a_T+\frac{a_T^2}{\log^2T}.
\]
At the stated cutoff \(a_T\to0\), so its quadratic term is absorbed into \(O_c(a_T)\) for all sufficiently large \(T\). This proves the author's displayed error. The dependence on \(c\), including the factor from \(\delta^{-2}\), is correctly contained in \(\ll_c\). Applying the estimate separately at the two fixed widths preserves an \(o(1)\) replacement error; it does not improve the signed target's limiting constant.

### 5. The exact genuine-prime identity

Let \(U_{\rm all}(s)=\sum_{p,k\geq2}(\log p)p^{-ks}\), which is absolutely convergent on \(\Re s>1/2\). Decompose the finite von Mangoldt polynomial as
\[
P_N=P_N^{\rm prime}+P_N^{\rm power},\qquad
U_{\rm tail}=U_{\rm all}-P_N^{\rm power}.
\]
Then exactly
\[
R-U_{\rm tail}=H-U_{\rm all}-P_N^{\rm prime}.
\]
This checks that powers \(p^k\leq N\) cancel once, and the strict tail \(p^k>N\) removes precisely the remaining powers. In particular, there is no off-by-one correction at a prime-power cutoff.

For \(\theta(x)=\sum_{p\leq x}\log p\), the Stieltjes continuation of the prime-only function gives
\[
R-U_{\rm tail}
=\frac{N^{1-s}}{s-1}-(\theta(N)-N)N^{-s}
 +s\int_N^\infty(\theta(x)-x)x^{-s-1}dx.
\]
The endpoint includes a prime equal to \(N\). Under RH,
\(\psi(x)-x=O(\sqrt x\log^2(2x))\), and the elementary sum of powers \(k\geq2\) is \(O(\sqrt x\log^2(2x))\), so the same bound holds for \(\theta(x)-x\). The integral is absolutely convergent for \(\Re s>1/2\). These facts verify the exact continuation and its analytic domain.

The only requested editorial clarification concerned §6 of the initial author draft: its phrase “the only RH input” needed to acknowledge both the logarithmic-derivative bound used for the norm and the RH prime-counting-error bound used for this representation. The revised §6 does so. Both inputs were already present in Round 8; this correction does not change the result.

### 6. Review scope

The entire six-section author draft was inspected. The review checked the infinite sums directly and did not replace them with finite numerical evidence. No numerical check is needed to establish their convergence or endpoint signs, and none was run. The result is an arithmetic simplification of the unresolved covariance problem. It neither supplies the missing positive constant nor certifies the desired residual lower bound.

### 7. Independently checked uniform mesoscopic corollary

Write \(L=\log T\). The same proof makes the residual-energy replacement uniform for
\[
1\leq c\leq L/4.
\]
Indeed, the RH logarithmic-derivative estimate used in the edge audit is
\(O(L^2/c+L)=O(L^2)\) uniformly on this range. The finite-polynomial bound is also uniform there. Thus \(\|R\|_2\ll\sqrt T L^2\) with an absolute implied constant. Moreover, \(\delta^{-2}=(L/c)^2\leq L^2\), so the unconditional bound (1) gives the same \(a_T\), with an absolute constant. Consequently
\[
\sup_{1\leq c\leq L/4}
\frac{|\|R_c-U_{c,N}\|_2^2-\|R_c\|_2^2|}{TL^2}
\ll a_T.
\tag{2}
\]

At \(N=\lfloor T/L^6\rfloor\),
\[
a_T\ll T^{-1/6}L^3+T^{-1/2}L^2.
\]
If \(b=b(T)\to\infty\) and \(b=o(\log L)\), both widths \(c=b/2\) and \(c=b\) eventually lie in the uniform range. Applying (2) to the coupled statistic
\[
b^2\{2\sinh(b)r_T(b)-2\sinh(2b)r_T(2b)\}
\]
changes it by at most \(O(b^2e^{2b}a_T)=o(1)\). The last limit follows because \(e^{2b}=L^{o(1)}\), whereas \(a_T\) contains a negative power of \(T\). Prime-power removal therefore remains justified at this mesoscopic edge scale. It still supplies no new arithmetic covariance estimate and does not choose an AH convergence rate.

The final author §7 is accepted, including its uniformity on every range \(2\leq b\leq G(T)\) with \(G(T)=o(\log L)\). Its statement that decreasing polynomial coefficients preserve the elementary bound refers to the positive coefficient majorants in that bound; no monotonicity of the exact finite-time polynomial norm is required or claimed. The author's historical draft-status sentence is retained as provenance; the present independent review supplies the current ordinary-proof verdict. This is not a formal machine-checked proof or a numerical gain enclosure.


<a id="report-30"></a>

# Current report 30: Mesoscopic damping: the missing arithmetic edge term and its rate requirements

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/dyson/round9/mesoscopic-edge/EDGE_RATE_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/mesoscopic-edge/EDGE_RATE_AUDIT.md).

**SHA-256:** `47e69edb32f9e2a083ff8a56ed0a6c19c6b6e69477c63f727eb4713458e05934`. **Git blob:** `7c6fe349387a601f91222b676b1f5c6d727e7669`. **Original bytes:** 11044.

## Mesoscopic damping: the missing arithmetic edge term and its rate requirements

Date: 2026-09-05. Status: bounded analytic audit; no new bound for actual zeta zeros is proved. The conclusions concern the explicitly checked mean-square estimates and the Round 8 arithmetic identity, not a universal impossibility theorem.

**Outcome.** Increasing the damping does not extract the required first edge correction from the checked RH estimates. Their limiting lower bound already loses a term larger than the desired signal by an unbounded factor. However, two tempting reasons for rejecting this route are false: finite-height errors can be made smaller than the signal by increasing the damping sufficiently slowly, and unquantified AH convergence permits an existential slow diagonal. The missing ingredient is an actual arithmetic estimate of the residual energy to relative precision \(o(1/b)\), with a coupled two-scale version if one does not assume simplicity.

### 1. Exact normalization and the arithmetic estimate that would suffice

Write \(L=\log T\), \(N=\lfloor T/L^6\rfloor\), and \(b=2c\). Define actual functions
\[
H_{T,b}(t)=-\frac{\zeta'}{\zeta}\left(\frac12+\frac{b}{2L}+it\right),
\qquad P_{T,b}(t)=\sum_{n\leq N}\Lambda(n)n^{-1/2-b/(2L)-it},
\]
\[
r_T(b)=\frac{1}{TL^2}\int_0^T|H_{T,b}(t)-P_{T,b}(t)|^2dt.
\]
Under RH the exact centered-tail representation from Round 8 is
\[
H_{T,b}(t)-P_{T,b}(t)
=\frac{N^{1-s}}{s-1}-E(N)N^{-s}
 +s\int_N^\infty E(x)x^{-s-1}dx,
\quad E(x)=\psi(x)-x,
\quad s=\frac12+\frac{b}{2L}+it.
\tag{1}
\]
The integral is absolutely convergent. This supplies the actual arithmetic object; no divergent critical-strip Dirichlet series is substituted for it.

One sufficient, presently unproved, edge estimate is
\[
\boxed{r_T(b)=\frac{e^{-b}}b+o\left(\frac{e^{-b}}{b^2}\right).}
\tag{AE}
\]
For a usable AH contradiction it would suffice to establish (AE) uniformly along every sufficiently slow \(b=b(T)\to\infty\), including both \(b\) and \(2b\). A more explicit formulation is a bound
\[
\left|r_T(b)-e^{-b}/b\right|
\leq\epsilon_T(b)e^{-b}/b^2,
\]
on \(B_0\leq b\leq B(T)\), with \(B(T)\to\infty\), and with the error tending to zero on a selectable increasing range. A result at one preassigned increasing rate does not automatically provide this uniformity.

Estimate (AE) asks for relative \(o(1/b)\) accuracy in a residual of size \(e^{-b}/b\). A leading-order asymptotic with unspecified relative \(o(1)\) is insufficient. The exact one-sided coupled target in §4 is weaker than proving both individual estimates.

### 2. The short-prime truncation errors are compatible with a slow diagonal

The proof of the Round 8 identity is uniform for
\(1\leq c\leq L/4\). Its logarithmic-derivative bound is
\(O(L^2/c+L)\), the right-line off-diagonal estimates only use
\(n^{1-2\sigma}\leq1\), and the auxiliary polynomial bound remains \(eN\log N\). Thus, uniformly for \(2\leq b\leq L/2\),
\[
\frac{1}{TL^2}\int_0^T|H_{T,b}(t)|^2dt
=\frac{D_N(b)}{L^2}+r_T(b)+O(L^{-4}),
\quad D_N(b)=\sum_{n\leq N}\frac{\Lambda(n)^2}{n^{1+b/L}}.
\tag{2}
\]
The implicit constant can be absolute on this range; no hidden exponential dependence on \(b\) is generated by the contour proof.

The prime diagonal can also be estimated uniformly. Under RH,
\[
\sum_{n\leq x}\Lambda(n)^2=x\log x-x+O(\sqrt x\log^3(2x)).
\]
For example, integrate \(\log x\) against \(d\psi(x)\), then remove the excess contribution of prime powers. Partial summation then gives
\[
\sum_{n\leq x}\frac{\Lambda(n)^2}{n}=\frac12\log^2x+O(1).
\]
Applying the decreasing weight \(n^{-b/L}\) preserves the \(O(1)\) error, uniformly for \(b\geq0\). Consequently, with \(\theta=\log N/L\),
\[
\frac{D_N(b)}{L^2}=\int_0^\theta u e^{-bu}\,du+O(L^{-2}),
\]
\[
\left|\frac{D_N(b)}{L^2}-d(b)\right|
\ll L^{-2}+(1-\theta)e^{-b\theta},
\quad d(b)=\frac{1-(1+b)e^{-b}}{b^2}.
\tag{3}
\]
Here \(1-\theta=6\log L/L+o(L^{-1})\). The respective ratios of the known errors to the edge scale \(e^{-b}/b^2\) are bounded by constants times
\[
\frac{b^2e^b}{L^4},\qquad
\frac{b^2e^b}{L^2},\qquad
\frac{b^2\log L}{L}\,e^{b(1-\theta)}.
\tag{4}
\]
All tend to zero for \(b=o(\log L)=o(\log\log T)\), and the same is true with \(2b\). Thus this sufficiently slow regime resolves the known arithmetic truncation and diagonal errors. It does **not** prove (AE).

Keeping the explicit pole in (1) is harmless for the argument. If it is removed using the weaker Round 8 estimate, the normalized residual-energy error is \(O(L^{-3})\), which is also \(o(e^{-b}/b^2)\) throughout the same slow regime.

### 3. What the checked primary mean-square bounds actually deliver

The primary source is Carneiro–Chandee–Chirre–Milinovich, [*On Montgomery's pair correlation conjecture: a tale of three integrals*](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), Theorem 5 and its proof in §4.2. Its Lemma 16 explicitly states the Goldston–Gonek–Montgomery Poisson correspondence with a uniform parameter range and errors. The source PDF is saved under `sources/`, with SHA-256 in `sources/receipt.json`.

For \(q=e^{-b}\), the theorem's RH lower and upper limiting expressions, in the present normalization \(I_T(b/2)/(TL^2)\), are
\[
U_-(b)=\frac{1-(1+b)q}{b^2}
 +\left(\frac1b+\frac1{\sqrt3}\right)e^{-b(1+1/\sqrt3)},
\]
\[
U_+(b)=\frac{1+q}{(1-q)b^2}
 -\frac{2q}{b(1-q)^2}+\frac{q}{1-q}.
\tag{5}
\]
The published relative error is \(O((\log\log T)^{-1/2})\), over
\(T^{-1}L^{5/2}\leq c\leq L^{1/4}/\sqrt{\log L}\).
For slow \(c\geq1\), the proof retains the stronger absolute normalized error
\[
O\left(\sqrt{\frac{\log L}{L}}+\frac cL+\frac{L^2}{Tc^2}\right).
\tag{6}
\]
Using only the compressed relative error would unnecessarily weaken the allowed diagonal rate.

Here is the resulting independent comparison with the signal. The sine and base-ACUE predictions for the normalized actual mean square are
\[
S(b)=\frac{1-q}{b^2},\qquad
A(b)=\frac{1-q}{(1+q)b^2}+\frac{q^2}{1-q^2}.
\]
Their difference is exactly
\[
\delta(b)=S(b)-A(b)
=\frac{q(1-q)}{(1+q)b^2}-\frac{q^2}{1-q^2}
\sim\frac{q}{b^2}.
\tag{7}
\]
Even with zero finite-height error, the lower expression in (5) falls below the sine prediction by
\[
S(b)-U_-(b)
=\frac qb-\left(\frac1b+\frac1{\sqrt3}\right)e^{-b(1+1/\sqrt3)}
\sim\frac qb.
\]
Its deficit divided by the desired signal tends to \(b\). In particular, it remains below the ACUE value for sufficiently large \(b\). The upper expression exceeds the sine prediction by
\[
U_+(b)-S(b)=q\left(1-\frac2b+\frac3{b^2}\right)+O(q^2),
\]
which is larger than the signal by order \(b^2\). These are deficiencies of the inspected bounds themselves, independent of how large \(T\) is chosen.

The error in (6) is below the signal when, for example,
\(c\leq(1/4-\varepsilon)\log\log T\), with fixed \(\varepsilon>0\). For the simultaneous scales \(b\) and \(2b\), the conservative condition \(b=o(\log\log T)\) suffices. This confirms that there is no honest blanket rate obstruction for arbitrarily slow damping. The limiting lower expression, rather than its finite-height error, is the decisive failed step.

### 4. The coupled edge statistic removes the AH nuisance exactly

A single variance cannot be compared with the base \(p_0=1\) ACUE value without controlling the near-diagonal parameter. Under RH plus AH-Pairs, its extra contribution to the normalized actual mean square is
\[
\frac{p_0(T)-1}{\sinh b}.
\]
At large \(b\), this is approximately \(2(p_0(T)-1)e^{-b}\), larger than the edge signal unless \(p_0(T)-1=o(b^{-2})\). That additional assertion is not part of the AH hypothesis being used.

Instead define the actual arithmetic statistic
\[
\boxed{\mathcal C_T(b)=b^2\left[
2\sinh(b)r_T(b)-2\sinh(2b)r_T(2b)-\frac1{2b}\right].}
\tag{8}
\]
Both residuals are built from the same \(E(x)=\psi(x)-x\) and the same cutoff \(N\). The nuisance contributions in (8) are \(2(p_0(T)-1)\) and its negative, so they cancel at the same finite height without a limit for \(p_0(T)\).

The sine residual prediction is \(r_S(b)=q/b\). Its exact substitution into (8) is
\[
\mathcal C_S(b)=-b e^{-2b}+\tfrac b2 e^{-4b}\longrightarrow0.
\]
Let
\[
H(b)=\frac{(1-e^{-b})^2}{b^2}-e^{-b}.
\]
The ACUE substitution obeys exactly
\[
\mathcal C_A(b)=\mathcal C_S(b)-b^2\{H(b)-H(2b)\},
\quad b^2\{H(b)-H(2b)\}\longrightarrow\frac34.
\tag{9}
\]
Thus the coupled first-edge limits are **zero versus \(-3/4\)**. This is an algebraic sharpening of the obligation, not a proof of the zero limit for zeta.

In particular, a uniform arithmetic lower bound for (8) whose lower limit is strictly greater than \(-3/4\), valid on a selectable increasing slow range, would suffice. Establishing (AE) at both scales would give the stronger limit zero. This identifies exactly the term that actual \(\Lambda\)/\(\psi\) estimates must improve.

### 5. What unquantified AH does and does not permit

The frozen Round 7 reduction gives an error \(\eta_T(b)\to0\) for each **fixed** \(b>0\), after retaining the displayed \(p_0(T)\) term. It does not license inserting an arbitrary prescribed \(b(T)\to\infty\).

Nevertheless, the following elementary diagonal lemma applies. Given any increasing envelope \(G(T)\to\infty\), one can select increasing thresholds \(T_j\) such that for all \(T\geq T_j\),
\[
G(T)\geq j,\qquad
|\eta_T(j)|+|\eta_T(2j)|\leq e^{-2j}/j^3.
\]
Set \(b(T)=j\) for \(T_j\leq T<T_{j+1}\). Then \(b(T)\to\infty\), \(b(T)\leq G(T)\), and the AH errors after multiplying (8)'s weights and \(b(T)^2\) are \(O(1/b(T))\). Taking, for instance, an envelope \(G(T)=o(\log\log T)\) also makes all explicit errors above negligible. It follows that AH forces \(\mathcal C_T(b(T))\to-3/4\) along such an **existential** slow diagonal.

The thresholds depend on unknown convergence rates. No effective formula for them, no prescribed rate such as \(b(T)=\sqrt{\log\log T}\), and no uniform AH estimate over a growing continuum of widths has been proved. Therefore an arithmetic theorem valid only at one prescribed rate would still need a compatibility argument. A theorem uniform over a suitable increasing slow range would avoid this issue.

### 6. Bounded decision and preserved checks

This lane closes with a precise unresolved arithmetic estimate, not with a new zero-spacing theorem. The checked primary RH mean-square bounds fail by factors \(b\) and \(b^2\) at the first edge scale. The Round 8 prime truncation and the source's uniform Poisson-transfer errors are compatible with sufficiently slow damping. AH's missing rate obstructs an effective prescribed diagonal, but not an existential one. None of these facts supplies (AE) or the weaker lower bound for (8).

`edge_identity_checks.py` and its JSON preserve exact rational checks of the model subtraction and nuisance cancellation, together with two fixed floating diagnostics of the source-bound deficits. They perform no optimization, zeta experiment, or parameter scan. The primary source PDF/text and receipt are included for the stated source audit. No Round 7 or Round 8 evidence was modified.


<a id="report-31"></a>

# Current report 31: Independent review of the mesoscopic edge obligation

**Collection:** R9 — complementary moduli, genuine-prime tails, and the edge.

**Source:** [research/dyson/round9/mesoscopic-edge/INDEPENDENT_EDGE_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round9/mesoscopic-edge/INDEPENDENT_EDGE_REVIEW.md).

**SHA-256:** `715ca92465ab81f1e2b3c0c4198fa4f861cb9394168ad749ae2f602d5ff67dd6`. **Git blob:** `f5e3ac2cf75ed3c9d1e6ce088931a39eb6100cc1`. **Original bytes:** 3656.

## Independent review of the mesoscopic edge obligation

Date: 2026-09-05. Reviewer: the root research lane, independently of the source-audit author. **Accepted as a bounded analytic/source audit, without a new arithmetic edge estimate.**

I read the complete `EDGE_RATE_AUDIT.md`, its small algebra script, and the saved primary source at Theorem 5, Lemma 16 and Section 4.2. The following points were checked directly rather than inferred from the script's PASS status.

1. The source uses c where the report uses b/2. Substitution gives exactly the displayed lower and upper functions. The absolute proof error for c>=1 contains the square root of log(log T)/log T, the c/log T term, and log²(T)/(T c²). Keeping this error instead of the theorem's compressed relative error is legitimate. It can be below the exponential edge signal on a sufficiently slow diagonal.
2. The limiting lower bound's deficit is asymptotic to e^(-b)/b, while sine minus base ACUE is asymptotic to e^(-b)/b² in normalized I. The failure therefore persists even after the finite-height error is removed. The upper deficit is larger by order b². These are statements about the checked bounds, not every consequence of RH.
3. The RH estimate for sum Lambda(n)² has the stated main terms x log x-x. Partial summation cancels the log x terms and leaves (1/2)log²x+O(1) for the sum divided by n. A decreasing exponential weight has bounded total variation, so the bounded primitive error stays O(1) uniformly in b. The missing interval between log N/log T and one gives the displayed endpoint error. All normalized errors vanish relative to e^(-b)/b² for b=o(log log T), including the second scale.
4. The factors two in the residual statistic are correct. Substituting r_S(b)=e^(-b)/b gives -b e^(-2b)+(b/2)e^(-4b). The difference from ACUE is b²[H(b)-H(2b)], tending to 3/4. The additive AH parameter contributes exactly equal constants with opposite signs, so a limit for p_0(T) is unnecessary.
5. The fixed-width AH errors permit an existential stepwise increasing diagonal. Choosing their errors at widths j and 2j below e^(-2j)/j³ makes the amplified error O(1/j). This does not justify a predetermined formula for b(T).

### An explicit sufficient uniform quantifier

To avoid ambiguity in the phrase “a selectable increasing range”, the following is one precise sufficient arithmetic target. Find an increasing G(T) tending to infinity with G(T)=o(log log T), for which

\[
\lim_{B\to\infty}\liminf_{T\to\infty}
\inf_{B\le b\le G(T)}\mathcal C_T(b)>-\frac34.
\tag{R}
\]

The intervals are nonempty for every fixed B once T is sufficiently large. If (R) holds, choose the AH diagonal under the envelope G(T). Along that diagonal the statistic tends to -3/4 by the reviewed argument, contradicting (R). The outer limit in (R) exists as an extended monotone limit of the inner lower bounds. Equivalently, one may supply a strict uniform gap for all sufficiently large lower cutoffs B.

This condition does not assert an exact GUE law at each fixed b. It is stronger than a statement at a single predetermined growing b(T), because such a statement might be incompatible with the unknown AH convergence rate. It is weaker than proving both individual residual asymptotics (AE). None of these arithmetic conditions is proved in the report or this review.

The source audit and model algebra are useful because they identify the required first correction and rule out two incorrect rate objections. They supply no positive improvement in the current lower bound. No additional numerical experiment, parameter scan or formal verification was performed for this review.


<a id="report-32"></a>

# Current report 32: Round 10: a power saving for one actual shifted-prime discrepancy

**Collection:** R10 — complete the actual shift packet.

**Source:** [research/reports/dyson_round10.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/dyson_round10.md).

**SHA-256:** `c276e4c0da7d40fc275a1c8d10fd8cf94641753a7add8febc4a90f05bb712737`. **Git blob:** `455f5f62d4d54e287de47328267337f6b0351c90`. **Original bytes:** 9485.

## Round 10: a power saving for one actual shifted-prime discrepancy

Date: 2026-09-05. **This round proves an unconditional bound for a specified smooth packet of the actual arithmetic discrepancy. It does not prove a new zeta pair-correlation lower bound.** The accompanying source audit explains why two tempting short-interval inputs do not supply the missing precision.

### The bound and how far it remains from the target

Use the complementary squarefree modulus family Q_X from Round 9, with q<=Q=X^.523. Let X=T^alpha, 6/5<=alpha<=7/5, and H=X/T. The discrepancy D_Q^V uses the actual localized prime-covariance sinc kernel, its Mobius–log divisor coefficient, its coprime principal term, and a fixed smooth cutoff V(h/H), supported in 1<h/H<2.

The [complete ordinary proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/shift-average/SMOOTH_SHIFT_COMPLETION_BOUND.md) gives

\[
\boxed{|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{HX(X+Q^2)}\,(\log X)^4.}
\tag{1}
\]

The estimate itself is unconditional. RH is used only when inserting it into the earlier actual-zeta correspondence. The proof works for any squarefree modulus subset with this cap; it does not yet exploit triple dense divisibility beyond the selection of the prescribed family. No novelty claim is made for its elementary completion and spacing ingredients.

For H=X^theta, the new exponent is 1.023+theta/2. The previous per-shift estimate, summed by the triangle inequality, had exponent 1+theta with any fixed logarithmic saving.

| H exponent | Previous triangle exponent | New smooth-packet exponent | Power saved, before logarithms |
|---|---:|---:|---:|
| 1/6 | 7/6 | 3319/3000 | 181/3000 = 0.060333... |
| 2/7 | 9/7 | 8161/7000 | 839/7000 = 0.119857... |

This is a power improvement in a genuine arithmetic error bound. Nevertheless, after division by the required X log X fluctuation scale, the estimate still grows as X^.023 sqrt(H) log³X. It does not evaluate this selected component at the precision needed for the compact Fourier test. The whole unsmoothed shift range, complementary divisor remainder, support main terms and continuous centering also remain unresolved.

### Why completing the shift sum helps

First remove prime powers from both terms of the progression discrepancy. Their total contribution is O_eta(H X^(.5+eta) log³X+H sqrt(X) log⁴X), which is o(X log X) for eta=.01 and the stated H range. Every remaining prime exceeds every modulus, so it is a unit modulo each q. This permits exact finite Fourier completion while retaining the principal unit sum.

For a separated amplitude f(p/X)v(h/H), define

\[
S_v(\beta)=\sum_hv(h/H)e(-\beta h),\qquad
A_f(\beta)=\sum_p(\log p)f(p/X)e(\beta p).
\]

Combining repeated rational frequencies before estimating gives the exact pairing

\[
\sum_{d,a}^{*} S_v(a/d)
\left(\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q\right)
\left(A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)\right).
\tag{2}
\]

The star means 2<=d<=Q, 1<=a<d and (a,d)=1. The zero frequency cancels. The principal coefficient mu(d)/phi(d) follows from the exact Ramanujan ratio and is independent of the parent modulus q. Treating all original fractions r/q as distinct would invalidate the subsequent spacing estimate.

The squared norm of the first two factors in (2) is O(H log³Q), or O(H log⁵Q) when a log q coefficient is present. A direct Schur/spacing argument bounds the centered prime sums' squared norm by O(X(X+Q²) log²X). The proof retains the logarithm in the elementary spacing bound. Cauchy–Schwarz then yields (1), after including the logarithmic cofactor.

The original two-variable sinc kernel is not simply replaced by a separated model. With y=m/X, z=h/H and epsilon=H/X=1/T, its phase is

\[
\epsilon^{-1}\log\frac y{y-\epsilon z}
=\int_0^z\frac{du}{y-\epsilon u}.
\]

It and its derivatives are uniformly smooth on the fixed support. A Fourier expansion with uniformly summable derivative-weighted coefficients transfers the separated estimate to the actual kernel, including log(y-epsilon z). The fixed support also keeps both cutoff factors on their correct branch.

Separate reviews cover the [coefficients and spacing](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/shift-average/COEFFICIENT_AND_SPACING_AUDIT.md) and the [actual kernel/prime-power passage](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/shift-average/ACTUAL_KERNEL_AND_PRIME_POWER_REVIEW.md). The root additionally read the complete author argument. The accepted scope is the explicitly defined smooth packet. A possible bounded-variation extension in a review is not silently promoted to a theorem for the full sharp packet.

### What the checked prime-variance sources do not give

The [arithmetic source audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/arithmetic-residual/ARITHMETIC_RANGE_AND_MIXED_MOMENT.md), with [independent review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/arithmetic-residual/INDEPENDENT_REVIEW.md), examines the edge shell X=T^(1+s/b), 1<=s<=2, h=X/T. Its interval-length exponent is s/(b+s), tending to zero.

[Guth–Maynard, arXiv:2405.20552v2](https://arxiv.org/html/2405.20552v2), Corollary 1.4, gives almost-all prime-count asymptotics for h>=X^(2/15+epsilon), with fixed epsilon. Even the corollary's epsilon-zero endpoint misses the whole shell once b>13. The subsequent Remark discusses a slight fixed-epsilon improvement with a worse error; it still does not cover an exponent tending to zero.

Inside the stated range, a direct conversion of the count theorem and its exceptional-set bound gives an error in the squared count far above the fluctuation scale X h log(X/h). Almost-all PNT is therefore not itself a constant-precision variance theorem. The audit does not rule out stronger uses of the underlying methods.

The checked [Carneiro–Chandee–Chirre–Milinovich short-interval comparisons](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf) retain fixed factors approximately 0.9028 and 1.0736, and fixed-endpoint quantifiers. These do not supply the shrinking first correction required by the mesoscopic test. The large-beta statements in that source use beta as the endpoint of the prime range, not the damping b.

### One precise remaining arithmetic mixed moment

Let R_b be the genuine-prime residual at displacement b/(2 log T), with the same cutoff N=floor(T/log^6 T), and put

\[
E_T(b)=\frac{e^b\|R_b\|_2^2}{T\log^2T},\quad
K_b=-R_b-2\partial_bR_b,\quad
M_T(b)=\frac{e^b\operatorname{Re}\langle R_b,K_b\rangle}{T\log^2T}.
\]

Exactly M_T=-E_T'. In the absolutely convergent region, K gives the genuine-prime weight log(p)/log(T)-1; the working-strip object is its centered analytic continuation. Differentiating an unspecified asymptotic error is not part of the argument.

For some fixed epsilon>0, an actual uniform bound

\[
M_T(s)\ge s^{-2}-(2-\epsilon)s^{-3}+o(s^{-3})
\tag{3}
\]

through twice a suitable slow envelope would imply that the Round 9 coupled statistic has lower limit at least -3/4+3epsilon/8, with the required uniform quantifiers. This would contradict AH-Pairs under RH. The implication follows by integrating from b to 2b; the correction integral is exactly 3/(8b²). Reviewed RH upper estimates control the small exponential terms.

**Inequality (3) is not proved.** This formulation identifies one signed, logarithmically weighted genuine-prime correlation; it is not a substitute for estimating it. Neither source checked here supplies a positive epsilon.

### Verification and next mathematical decision

The finite script checks 9,615 exact Ramanujan-ratio cases, reduced-frequency grouping with formal log q coefficients, zero-frequency cancellation and both endpoint exponents. A second exact script checks the prime-range thresholds and mixed-moment normalization. These checks validate algebra; the power bound rests on the written analytic proof and independent reviews.

All 15 original files (1,452,061 bytes) are preserved in the adjacent local `Astra-Local-Archive/round10-originals/`; 14 research files are verbatim public. The third-party Guth–Maynard HTML body stays local, identified by URL/hash. Earlier primary references remain in their pinned local folders. The [intake manifest](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/INTAKE_MANIFEST.json) and [integration replay](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/logs/round10-integration/recheck.json) record their exact scope. Both output JSON files reproduce in a separate process. The mixed-moment JSON is identical in full; the completion output differs only in two temporary provenance paths, with source hashes still checked. No new floating optimization, prime-gap sweep, or zeta-data fit was run.

From the repository root, with Python and SymPy:

```text
python3 research/logs/round10-integration/recheck.py --prime-gap-source-dir /path/to/retained/round9-external-sources
python3 tools/verify_manifest.py
```

The next useful arithmetic work is an estimate for the pairing (2) that uses the selected Mobius coefficients together with the centered prime exponential sums, beyond separate norm bounds. A separate possibility is an averaged version of (3) with a strict quantitative gain. Repeating the same completion with different notation or improving only its logarithmic exponent would not close the existing power gap.

The large handoff PDFs retain their stated earlier checkpoints; this compact report is an additional source record. The goal remains active. Reverting this research slice removes its reports and rechecks without altering earlier proofs. New model sessions, generic positivity scans and claims of a solved famous conjecture are outside this checkpoint.


<a id="report-33"></a>

# Current report 33: A power improvement for a smooth packet of the actual shifted discrepancy

**Collection:** R10 — complete the actual shift packet.

**Source:** [research/dyson/round10/shift-average/SMOOTH_SHIFT_COMPLETION_BOUND.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/shift-average/SMOOTH_SHIFT_COMPLETION_BOUND.md).

**SHA-256:** `7b52e4d82dc40bf90183331d548b7fffe5545d1928d7cb93223223b5b71c1d78`. **Git blob:** `ec368290b4a8627d406b769b68cbc7b3ca6bfd5d`. **Original bytes:** 13008.

## A power improvement for a smooth packet of the actual shifted discrepancy

Date: 2026-09-05. Status: an elementary completion bound for an identified component of the Round 9 discrepancy. It improves the triangle-inequality bound by a power of X, but remains too large to imply a zeta covariance theorem.

Let \(X=T^\alpha\), \(6/5\le\alpha\le7/5\), \(H=X/T\), and \(Q=X^{523/1000}\). For the actual complementary squarefree modulus family \(\mathcal Q_X\subset(X^{1/2},Q]\) from Round 9, the smooth packet defined below satisfies

\[
\boxed{|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{HX(X+Q^2)}\,(\log X)^4.}
\tag{1}
\]

Estimate (1) itself does not use RH. RH enters only when this discrepancy estimate is combined with the Round 9 aggregate covariance identity.

Thus, writing \(H=X^\theta\),

\[
|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll X^{1023/1000+\theta/2}(\log X)^4,
\qquad \frac16\le\theta\le\frac27.
\tag{2}
\]

Compared with the previously available \(HX\log^{-A}X\), the exponent improves by \(\theta/2-23/1000\), at least \(181/3000=0.060333\ldots\), before logarithmic factors. This is a nontrivial bound for the **actual discrepancy**, not an estimate for a substituted positive model.

However, (2) divided by \(X\log X\) still grows as a power. No bound of the required size \(o(X\log X)\) follows. The gain uses squarefreeness and the modulus cap; it does not yet exploit triple dense divisibility beyond establishing that the prescribed family is admissible. No novelty claim is made for the completion or finite-spacing argument.

### 1. The exact packet and source relationship

Keep the Round 9 discrepancy convention

\[
\Delta(f;a\bmod q)=\sum_{m\equiv a\;(\bmod q)}f(m)
-\frac1{\varphi(q)}\sum_{(m,q)=1}f(m).
\]

Fix \(V\in C_c^\infty(1,2)\) and \(\chi\in C_c^\infty(1,3/2)\), and put

\[
w_h(u)=\chi(u/X)a_u(X)a_{u+h}(X)
\operatorname{sinc}_0\!\left(T\log(1+h/u)\right),
\]
\[
a_u(X)=\min\{(u/X)^{1/2},(X/u)^{3/2}\},\qquad
\operatorname{sinc}_0(v)=\sin(v)/v,\quad \operatorname{sinc}_0(0)=1.
\]

The object in (1) is

\[
\mathfrak D_{\mathcal Q}^{V}(X,T)
=\sum_{h\in\mathbb Z}V(h/H)
\sum_{\substack{q\in\mathcal Q_X\\(q,h)=1}}\mu(q)
\Delta\!\left(
\Lambda(m)w_h(m-h)\log((m-h)/q);
h\bmod q\right).
\tag{3}
\]

Each sequence inside \(\Delta\) is defined to be zero off its indicated support; there is no logarithm of a nonpositive argument. This is the actual Round 9 weighted discrepancy, with one additional smooth shift cutoff \(H<h<2H\). We assume the fixed hard-cutoff constant in that round is at least two. No claim about the entire unsmoothed shift range is hidden in this localization.

The modulus family and its validity are inherited from [OpenAI, *Improved short gaps between primes*, 30 August 2026](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf): Proposition 2.3, pp.4–5; equation (2.5), p.7; and Corollary 2.19, p.11. Round 9 checks \(\omega=3/250,\delta=\varepsilon=1/1000\), giving \(240\omega+80\delta=2.96<3\) and the cap \(X^{.523}\). That source's modulus sum gives only the \(HX\log^{-A}X\) bound after a shift triangle inequality. All additional analytic estimates needed for (1) are proved below.

In fact the completion argument applies to any squarefree subset of \((X^{1/2},Q]\). It does not assert a new distribution estimate for triply densely divisible moduli.

### 2. Replace von Mangoldt by genuine primes inside this discrepancy

Let \(\vartheta_*(m)=\log m\) when m is prime, and zero otherwise. Replacing \(\Lambda\) by \(\vartheta_*\) in (3) changes it by

\[
O_\eta\!\left(HX^{1/2+\eta}\log^3X+H\sqrt X\log^4X\right)
\tag{4}
\]

for every fixed \(\eta>0\).

For the progression term, a prime power \(m=p^j\asymp X\), \(j\ge2\), contributes only when \(q\mid m-h\). For each h there are at most \(\tau(m-h)\ll_\eta X^\eta\) possible q. The weights cost \(O(\log X)\), and
\(\sum_{p^j\asymp X,j\ge2}\log p\ll\sqrt X\log^2X\).
Summing over h proves the first bound in (4).

For the principal term, bound the h-sum by O(H), retain the coprimality restrictions or enlarge by absolute values, and use \(\sum_{q\le Q}1/\varphi(q)\ll\log X\). This gives the second bound. Thus both portions of the discrepancy are controlled; one cannot replace \(\Lambda\) in only its progression sum.

Taking, for example, \(\eta=1/100\), (4) is \(o(X\log X)\) throughout \(H\le X^{2/7}\), and is smaller than the right side of (1). This is nuisance removal, not the source of the power improvement.

Every remaining prime m satisfies \(m\asymp X>Q\). It is therefore a unit modulo every q under consideration, which makes the following completion exact.

### 3. Exact completion for a separated weight

First replace the smooth two-variable amplitude by \(f(m/X)v(h/H)\), where f,v are smooth with fixed compact supports and m is restricted to primes near X. The logarithmic factor depending on q is handled in Section 6.

Write \(e(z)=e^{2\pi iz}\) and

\[
S_v(\beta)=\sum_{h\in\mathbb Z}v(h/H)e(-\beta h),
\quad
A_f(\beta)=\sum_{p}\log p\,f(p/X)e(\beta p).
\tag{5}
\]

For any integer m,

\[
\sum_{h\equiv m\;(\bmod q)}v(h/H)
=\frac1q\sum_{r=0}^{q-1}S_v(r/q)e(rm/q).
\tag{6}
\]

Also, with the Ramanujan sum \(c_q(r)=\sum_{b\bmod q,(b,q)=1}e(rb/q)\),

\[
\sum_{(h,q)=1}v(h/H)
=\frac1q\sum_{r=0}^{q-1}S_v(r/q)c_q(r).
\tag{7}
\]

In the progression term, \((h,q)=1\) is automatic because m is a prime exceeding q. In the principal term it remains exactly the unit sum in (7). Consequently the completed separated discrepancy is

\[
\sum_{q\in\mathcal Q_X}\frac{\mu(q)}q
\sum_{r=0}^{q-1}S_v(r/q)
\left(A_f(r/q)-\frac{c_q(r)}{\varphi(q)}A_f(0)\right).
\tag{8}
\]

Reduce \(r/q=a/d\). Since q is squarefree and \(d=q/(q,r)\),

\[
\frac{c_q(r)}{\varphi(q)}=\frac{\mu(d)}{\varphi(d)}.
\tag{9}
\]

This ratio is independent of the larger modulus q. The d=1 term vanishes identically. Regrouping (8) by distinct reduced fractions gives

\[
\sum_{\substack{2\le d\le Q\\1\le a<d,\ (a,d)=1}}
C_{a/d}\,Z_f(a/d),
\tag{10}
\]

\[
C_{a/d}=S_v(a/d)\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q,
\quad
Z_f(a/d)=A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0).
\tag{11}
\]

Distinct representations of the same rational frequency must be merged before applying a finite-spacing estimate. Treating all r/q as distinct would be incorrect.

### 4. A quantitative norm for the completed coefficients

The elementary bound

\[
\left|\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q\right|
\le\frac{1+\log(Q/d)}d
\tag{12}
\]

does not assume cancellation of the Möbius coefficients.

Finite summation by parts, applied J times to the compactly supported sequence \(v(h/H)\), gives

\[
|S_v(\beta)|\ll_{v,J}
H(1+H\|\beta\|)^{-J}.
\tag{13}
\]

One can prove (13) directly: the J-th finite difference has total absolute mass \(O_{v,J}(H^{1-J})\), and its Fourier transform is multiplied by \((e(\beta)-1)^J\). Combine that estimate with the trivial O(H) bound. No convergence of a critical-strip Dirichlet series is involved.

For J=2,

\[
\sum_{a=1}^{d-1}|S_v(a/d)|^2
\ll_v
\begin{cases}
d^4/H^2,&d\le H,\\
Hd,&d\ge H.
\end{cases}
\tag{14}
\]

This follows by measuring distance to the endpoints a=0,d; the relevant convergent series is \(\sum_{a\ge1}a^{-4}\). Dropping the coprimality restriction only enlarges this upper bound. Equations (12)–(14) prove

\[
\sum_{d,a}|C_{a/d}|^2\ll_v H(\log(2Q))^3.
\tag{15}
\]

For the coefficient with \(\mu(q)\log q/q\) in place of \(\mu(q)/q\), the same proof gives \(O_v(H\log^5(2Q))\). These explicit norms replace the H-fold triangle inequality.

### 5. The required finite-spacing estimate, proved directly

The reduced fractions \(a/d\), \(d\le Q\), are distinct and separated on the unit circle by at least \(Q^{-2}\). For a consecutive integer interval of length \(N\ll X\), the Gram matrix of their exponential vectors has diagonal N and off-diagonal absolute values at most

\[
\min\!\left(N,\frac1{2\|\beta-\beta'\|}\right).
\]

Order the distances in either direction around the circle. Separation bounds the absolute row sum by

\[
N+O(Q^2\log(2Q)).
\]

The Schur bound and matrix duality therefore give the finite inequality

\[
\sum_{\beta}\left|\sum_n b_n e(\beta n)\right|^2
\ll(X+Q^2\log(2Q))\sum_n|b_n|^2.
\tag{16}
\]

For \(b_p=(\log p)f(p/X)\) at primes and zero otherwise, Chebyshev's bound gives
\(\sum|b_n|^2\ll_f X\log X\) and \(A_f(0)\ll_f X\).
The constant-centering portion of (11) has total squared mass at most

\[
|A_f(0)|^2\sum_{d\le Q}\frac{\mu(d)^2}{\varphi(d)}
\ll_f X^2\log(2Q).
\]

Combining this with (16),

\[
\sum_{d,a}|Z_f(a/d)|^2
\ll_f X(X+Q^2)(\log X)^2.
\tag{17}
\]

The logarithm in the spacing row sum has been retained. Using the prime-supported coefficient norm, rather than the cruder norm of all integers weighted by log, is also needed for the displayed logarithmic bookkeeping.

Cauchy–Schwarz in (10), with (15) and (17), now bounds the separated discrepancy by

\[
\ll_{f,v}\sqrt{HX(X+Q^2)}(\log X)^{5/2}.
\tag{18}
\]

The version with \(\log q\) costs one more logarithm.

### 6. The actual m/h kernel, including the logarithm

Put \(\epsilon=H/X=1/T\), \(y=m/X\), and \(z=h/H\). The amplitude of (3), apart from the logarithm and the prime weight, is

\[
F_\epsilon(y,z)=
V(z)\chi(y-\epsilon z)\,
y^{-3/2}(y-\epsilon z)^{-3/2}
\operatorname{sinc}_0\!\left(
\frac1\epsilon\log\frac{y}{y-\epsilon z}\right).
\tag{19}
\]

The cutoff ensures that both a-factors are on their \(u>X\) branch. The apparently singular phase is actually

\[
\frac1\epsilon\log\frac y{y-\epsilon z}
=\int_0^z\frac{du}{y-\epsilon u}.
\tag{20}
\]

It extends smoothly to z/y at \(\epsilon=0\). Every fixed mixed derivative of (19) is uniformly bounded on a fixed compact rectangle for sufficiently small epsilon. The same holds after multiplying by \(\log(y-\epsilon z)\).

Choose fixed smooth cutoffs slightly larger than that rectangle and expand the resulting functions in a two-variable Fourier series. Repeated integration by parts gives coefficients \(b_{k,\ell}\) satisfying, uniformly in epsilon,

\[
\sum_{k,\ell}|b_{k,\ell}|(1+|\ell|)^J<\infty
\]

with a common bound for any fixed J. Each term separates into a function of m/X and a function of h/H. The m-factor has uniformly bounded sup norm; the derivatives of the h-factor grow at most polynomially in \(\ell\), absorbed by the displayed coefficient sum. Thus (18) is summable over this expansion. This is a proved separation of the actual amplitude, not its replacement by a product approximation with an unspecified error.

Finally,

\[
\log((m-h)/q)=\log X-\log q+\log(y-\epsilon z).
\tag{21}
\]

The first term costs \(\log X\), the second uses the \(\log q\) coefficient norm after (15), and the third is another uniformly smooth amplitude. Their common upper bound is

\[
O_{V,\chi}\!\left(\sqrt{HX(X+Q^2)}(\log X)^4\right).
\]

Together with the smaller prime-power error (4), this proves (1).

### 7. Nontriviality, limitations, and the next mathematical obstruction

At \(\theta=1/6\), the exponent in (2) is \(3319/3000=1.106333\ldots\), compared with the triangle exponent \(7/6\). At \(\theta=2/7\), it is \(8161/7000=1.165857\ldots\), compared with \(9/7\). These are power improvements, not merely changes to logarithmic factors.

They still exceed one. Under RH, inserting (1) into the Round 9 aggregate identity leaves an error larger than \(X\log X\); the negligible \(H\sqrt X\log^4X\) nuisance there does not change that conclusion.

The now-specific place needing further arithmetic input is the pairing

\[
\sum_{d,a}
S_v(a/d)
\left(\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q\right)
\left(A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)\right),
\tag{22}
\]

and its \(\log q\) and smooth-amplitude variants. A proof reaching the covariance scale must improve this actual pairing beyond the elementary coefficient-norm and spacing bounds, for example by exploiting the complementary modulus restrictions inside the coefficient sum together with the prime exponential sums. The 186 coherent-class estimate by itself supplies no such cross-frequency cancellation.

This is a location of missing arithmetic information, not a proof that no sharper completion argument can work. No further reparameterization or generic positivity test was performed.

### 8. Exact checks and provenance

The companion **check_shift_completion.py** verifies with exact rational/integer arithmetic the Ramanujan ratio (9), regrouping by reduced denominators, the cancellation of the zero frequency, and all stated power exponents. Its finite toy modulus families test algebra, not prime-distribution asymptotics. The script records the hashes of this report and the frozen Round 9 report/source files.

The estimates (12)–(18) and the actual-kernel passage are ordinary written proofs. No floating-point experiment is being used to assert a power saving. The report does not claim to settle the unsmoothed full discrepancy, the complementary divisor remainder, AH, or Montgomery's conjecture.


<a id="report-34"></a>

# Current report 34: Independent audit of the completed-shift coefficients and spacing bound

**Collection:** R10 — complete the actual shift packet.

**Source:** [research/dyson/round10/shift-average/COEFFICIENT_AND_SPACING_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/shift-average/COEFFICIENT_AND_SPACING_AUDIT.md).

**SHA-256:** `eccd80ad4909639a53583376444cbc9fce9fab518b75de7f82052c31c7a27fc7`. **Git blob:** `464c498e14af12781d28377818662f6bd3a6eccd`. **Original bytes:** 11413.

## Independent audit of the completed-shift coefficients and spacing bound

Date: 2026-09-05. Reviewer: `yau_flow`. This note checks the exact reduced-fraction identity, its coprime principal term, and a fully quantified bound for separable genuine-prime packets. The authoring agent and another reviewer are separately checking the actual two-variable weight and prime-power exceptions. No numerical scan or large computation is used here.

**Final verdict on the assigned analytical core:** the coefficient and spacing argument is valid. Its logarithmic losses fit the proposed fourth power. The resulting estimate improves the accumulated error for the selected divisor component but does not reach the covariance scale. The distinction between this separable lemma and a verified application to the full weight must be retained. The pinned author draft and precise review scope are recorded in Section 7.

### 1. Precisely quantified separable statement

Let \(X\geq4\), \(H\geq1\), and \(2\leq Q<X\). Let \(\mathcal Q\) be any set of distinct squarefree integers in \([1,Q]\). No dense-divisibility assumption is needed for this lemma. Let \(f\) be a bounded complex function on \([1,2]\), and let \(v\) be a complex function of bounded variation on \(\mathbb R\), supported in a fixed interval \([-C,C]\). Put
\[
M(v)=\|v\|_\infty+\operatorname{TV}(v),\qquad
B_p=(\log p)f(p/X)\mathbf1_{X<p\leq2X}.
\]
For \(j\in\{0,1\}\), define
\[
\begin{split}
D_j={}&\sum_{h\in\mathbb Z}v(h/H)
\sum_{\substack{q\in\mathcal Q\\(q,h)=1}}
\mu(q)(\log q)^j\\
&\quad\times\left\{
\sum_{\substack{X<p\leq2X\\p\equiv h\pmod q}}B_p
-\frac1{\varphi(q)}\sum_{X<p\leq2X}B_p
\right\}.
\end{split}
\tag{1}
\]
In (1), \((\log q)^0=1\), including \(q=1\). The braces for \(q=1\) vanish identically. Since every prime in the sum exceeds \(Q\), each is coprime to every modulus. This is the reason the principal sum in (1) is unrestricted; for a von Mangoldt sum this replacement would require a separate prime-power argument.

There is a constant depending only on \(C\) such that
\[
|D_j|\ll_C
\|f\|_\infty M(v)
\sqrt{HX(X+Q^2)}\,\log^{j+5/2}(2X).
\tag{2}
\]
The exponent \(j+5/2\) need not be rounded up. In particular the common \(O(\log^4(2X))\) upper bound is valid for \(j=1\), and also after multiplying \(D_0\) by a factor of size \(O(\log X)\). These are the two cases needed to separate \(\log((m-h)/q)\).

All constants in (2) are independent of the chosen family \(\mathcal Q\), its cardinality, \(X,H,Q\), and the values of \(f,v\), apart from the displayed norms. The statement is about the actual primes and progression discrepancy, not a formal spectral model.

### 2. Exact reduction, including the principal term

Use \(e(z)=e^{2\pi iz}\) and
\[
S_v(\alpha)=\sum_{h\in\mathbb Z}v(h/H)e(-\alpha h).
\]
For a prime \(p>Q\), its congruence \(p\equiv h\pmod q\) forces \((h,q)=1\). Thus the coprimality restriction can be dropped in the first term of (1), but it must be retained in the principal term. Finite Fourier inversion gives
\[
\sum_hv(h/H)\mathbf1_{p\equiv h\pmod q}
=\frac1q\sum_{r=0}^{q-1}S_v(r/q)e(rp/q),
\]
and
\[
\sum_{(h,q)=1}v(h/H)
=\frac1q\sum_{r=0}^{q-1}S_v(r/q)c_q(r),
\]
where \(c_q(r)=\sum_{a\bmod q,(a,q)=1}e(ra/q)\) is the Ramanujan sum. At a reduced fraction \(r/q=a/d\), with \((a,d)=1\),
\[
\frac{c_q(r)}{\varphi(q)}=\frac{\mu(d)}{\varphi(d)}.
\tag{3}
\]
For squarefree \(q\), (3) follows directly by multiplying the local factors: a prime dividing \(d\) contributes \(-1/(p-1)\), and a prime dividing \(q/d\) contributes one.

Define
\[
A_{d,j}=\sum_{\substack{q\in\mathcal Q\\d\mid q}}
\frac{\mu(q)(\log q)^j}{q},
\qquad
E(a/d)=\sum_{X<p\leq2X}B_p
\left(e(ap/d)-\frac{\mu(d)}{\varphi(d)}\right).
\]
Then the exact identity is
\[
D_j=\sum_{2\leq d\leq Q}\ \sum_{\substack{1\leq a<d\\(a,d)=1}}
A_{d,j}S_v(a/d)E(a/d).
\tag{4}
\]
There is one term for each reduced fraction, not one independent frequency for each original modulus. The \(d=1\) term is zero because its centered character is \(1-1\). The coefficient is a sum with denominator \(q\); replacing it by \(1/d\) before summing the multiples would lose the logarithmic norm control. No cancellation of the Möbius coefficients is used below.

### 3. Squared coefficient norm

Summing by parts in the finite shift sequence gives
\[
|S_v(\alpha)|\ll_C M(v)\min\{H,\|\alpha\|^{-1}\},
\tag{5}
\]
with the first alternative used at integral \(\alpha\). The discrete variation is at most the total variation of the zero-extended function \(v\). This proof includes indicator cutoffs with a specified endpoint convention; it does not require smoothness.

For \(d\leq H\), bound the complete nonzero residue sum by
\[
\sum_{a=1}^{d-1}|S_v(a/d)|^2
\ll_C M(v)^2d^2.
\]
For \(d>H\), split the distance of \(a\) from the nearest multiple of \(d\) at \(d/H\). Equation (5) gives
\[
\sum_{a=1}^{d-1}|S_v(a/d)|^2
\ll_C M(v)^2Hd.
\tag{6}
\]
The reduced-residue sum is smaller. Independently,
\[
|A_{d,j}|\leq
\frac{\log^j(2Q)}d\left(1+\log\frac Qd\right)
\ll\frac{\log^{j+1}(2Q)}d.
\tag{7}
\]
Hence
\[
\begin{split}
\sum_{d,a}^{*}|A_{d,j}S_v(a/d)|^2
&\ll_C M(v)^2\log^{2j+2}(2Q)
\left(\sum_{d\leq\min(H,Q)}1
+H\sum_{H<d\leq Q}\frac1d\right)\\
&\ll_C M(v)^2H\log^{2j+3}(2Q).
\end{split}
\tag{8}
\]
Thus the claimed \(H\log^3Q\) and \(H\log^5Q\) squared norms are valid for \(j=0,1\), respectively. In particular, the coefficient argument itself does not distinguish a smooth shift cutoff from a sharp finite interval. Whether the full nonseparable weight admits a controlled decomposition is a different question.

### 4. Well-spaced frequencies and centered prime sums

Distinct reduced fractions of denominator at most \(Q\) have circular separation at least \(Q^{-2}\). For any integer interval of length \(O(X)\), its exponential kernel satisfies
\[
\left|\sum_m e((\alpha-\beta)m)\right|
\ll\min\{X,\|\alpha-\beta\|^{-1}\}.
\]
For a fixed frequency, the number of others within circular distance \(r\) is \(O(1+rQ^2)\). Ordering the distances and summing the harmonic series therefore bounds every absolute Gram row sum by
\[
O\bigl(X+Q^2\log(2Q)\bigr).
\]
The elementary Schur bound and finite-dimensional duality imply
\[
\sum_{d,a}^{*}\left|\sum_m b_me(am/d)\right|^2
\ll\bigl(X+Q^2\log(2Q)\bigr)\sum_m|b_m|^2.
\tag{9}
\]
This proof retains the logarithm in the elementary spacing estimate. It does not silently invoke the sharper large-sieve constant \(X+Q^2\).

For \(b_p=B_p\) and zero coefficients on other integers, Chebyshev's elementary bound \(\sum_{p\leq2X}\log p\ll X\) gives
\[
\sum_p|B_p|^2\ll\|f\|_\infty^2X\log(2X),
\qquad
\left|\sum_pB_p\right|\ll\|f\|_\infty X.
\tag{10}
\]
Using primes in (10) saves one logarithm compared with the cruder bound obtained by assigning a \(\log X\) coefficient to every integer.

The constant terms in \(E(a/d)\) have squared norm
\[
\left|\sum_pB_p\right|^2
\sum_{d\leq Q}\frac{\mu(d)^2}{\varphi(d)}
\ll\|f\|_\infty^2X^2\log(2Q).
\tag{11}
\]
For completeness, \(\sum_{d\leq Q}1/\varphi(d)\ll\log(2Q)\) follows from
\(n/\varphi(n)=\sum_{a\mid n}\mu(a)^2/\varphi(a)\): after interchanging the two positive sums the remaining series is bounded by
\(\sum_a\mu(a)^2/(a\varphi(a))=\prod_p(1+1/(p(p-1)))<\infty\).

Combining (9)–(11), with \(|u-v|^2\leq2|u|^2+2|v|^2\), proves
\[
\sum_{d,a}^{*}|E(a/d)|^2
\ll\|f\|_\infty^2X(X+Q^2)\log^2(2X).
\tag{12}
\]
The primitive principal term is therefore affordable without assuming cancellation of the prime exponential sums. Cauchy–Schwarz in (4), using (8) and (12), proves (2).

### 5. What an application to the actual weight must verify

The separable proof applies to a sum of blocks if the full weight has an absolutely summable representation
\[
W(m/X,h/H)=\sum_\ell\gamma_\ell f_\ell(m/X)v_\ell(h/H),
\qquad
\sum_\ell|\gamma_\ell|\|f_\ell\|_\infty M(v_\ell)\leq K,
\tag{13}
\]
uniformly in \(X,H,T\). The bound is then multiplied by \(K\). If the logarithmic cofactor is present, write
\[
\log((m-h)/q)=\log X-\log q+\log(m/X-(H/X)(h/H)).
\]
The first two terms use \(j=0\) and \(j=1\); the third must be included in the smooth two-variable factor whose separation is justified. Independent choices of arbitrary \(w_h\) satisfying only a separate bounded-variation norm in \(m\) do not automatically give (13).

Likewise, replacing \(\Lambda(m)\) by genuine-prime coefficients must retain both the original nonprimitive congruence exceptions and the coprime principal-term deletions. Their errors are not part of the identity (4). The author and the other independent reviewer own these full-weight checks.

For a sharp shift interval, (5)–(8) are still available. A Fourier expansion of just the smooth kernel, leaving the interval indicator in each \(v_\ell\), is a possible rigorous use of (13): its bounded-variation cost grows polynomially with the Fourier frequency and can be absorbed by sufficiently rapid coefficient decay. This observation alone is not a completed verification of the original sharp packet's support and endpoint conventions.

### 6. Size and limitations

At \(Q=X^{523/1000}\), the proposed upper bound is
\[
O\bigl(X^{1.023}\sqrt H\log^4X\bigr).
\]
For \(X^{1/6}\leq H\leq X^{2/7}\), its ratio to \(HX\) is
\(O(X^{.023}H^{-1/2}\log^4X)\), which tends to zero by a power of \(X\). This is a real improvement over accumulating independent per-shift bounds.

However, its ratio to the required \(X\log X\) scale is
\(O(X^{.023}\sqrt H\log^3X)\), which grows throughout the stated interval. No bound in this note evaluates the selected divisor component to the required covariance precision, controls the complementary divisor remainder, or settles a zeta pair-correlation conjecture.

### 7. Final author artifact and delta-review scope

The final reviewed author artifact is **SMOOTH_SHIFT_COMPLETION_BOUND.md**, SHA-256

`7b52e4d82dc40bf90183331d548b7fffe5545d1928d7cb93223223b5b71c1d78`.

Its Sections 3–5 were read and checked against the independent derivation above. The exact Fourier signs, coprime principal term, zero-frequency cancellation, reduced-denominator grouping, smooth-shift estimate with two finite differences, the two coefficient norms, the logarithm in the Schur row bound, and the centered prime norm are all accepted. The power exponents and the comparison with the covariance scale in its introduction and Section 7 agree with exact rational arithmetic. Its final clarification that the completion bound itself is unconditional is also accepted: none of these arguments uses RH.

The actual two-variable amplitude in author Section 6 is consistent with the uniform separation criterion (13). Its complete support/separation and prime-power-exception review is assigned to the separate `residual_gram` reviewer; the present note does not replace that independent check. In particular, this audit does not enlarge the author theorem from its fixed smooth shift packet to the entire sharp packet. The bounded-variation observation in Section 5 remains a precisely stated extension criterion.

The companion author's exact-check JSON was inspected for its scope and report provenance, but its script was not independently rerun here. No assertion in this audit depends on those finite checks. The written estimates prove the assigned analytical core; they are not a machine-checked formal proof, a new distribution theorem at the required covariance scale, or a solution of AH or Montgomery's conjecture.


<a id="report-35"></a>

# Current report 35: Independent review: actual shift kernel and genuine-prime replacement

**Collection:** R10 — complete the actual shift packet.

**Source:** [research/dyson/round10/shift-average/ACTUAL_KERNEL_AND_PRIME_POWER_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/shift-average/ACTUAL_KERNEL_AND_PRIME_POWER_REVIEW.md).

**SHA-256:** `df6d6602ce9b68ac4759a8cbb8a3caad84d82b4694105a3bb466a9a69fd22732`. **Git blob:** `efd1c98498378d8ea9cb8970eb8c1d4dc1cc6d14`. **Original bytes:** 6575.

## Independent review: actual shift kernel and genuine-prime replacement

Date: 2026-09-05. **Accepted for the stated smooth packet.** This is a narrow ordinary-proof review of Sections 1–2 and 6 of `SMOOTH_SHIFT_COMPLETION_BOUND.md`, pinned to SHA256 `7b52e4d82dc40bf90183331d548b7fffe5545d1928d7cb93223223b5b71c1d78`. The reduced-fraction coefficients and finite-spacing bounds are independently covered by `COEFFICIENT_AND_SPACING_AUDIT.md`; this review does not present that other review as its own work.

No fatal gap was found in the object identification, prime-power deletion, coprime completion prerequisites, or exact separation of the actual two-variable weight. This acceptance does not upgrade the resulting discrepancy estimate to the required zeta covariance scale.

### 1. The object really is the localized Round 9 discrepancy

Author equation (3) is precisely the Round 9 equation (21) with the additional scalar shift weight V(h/H). The convention for Delta includes both a progression sum and the coprime principal sum. The residue is h; the shifted argument is m-h; the logarithm is log((m-h)/q). These remain in their correct places. The smooth packet has H<h<2H, and therefore is contained in the earlier hard shift cutoff provided its fixed constant is at least two, as explicitly assumed.

The source modulus family is squarefree and has q<=X^.523. No new source-distribution conclusion is being imported: the subsequent completion only uses squarefreeness and this cap. The claimed power improvement concerns this one identified smooth discrepancy component. The unsmoothed full shift range, other divisor components, and continuous covariance centering are not estimated here.

### 2. Both prime-power portions have been bounded

Write theta_*(m)=log m on primes and zero otherwise. On the fixed support, m and m-h are comparable to X, the a-factors and sinc are bounded, and the extra logarithm is O(log X). For each h and each prime power m=p^j with j>=2, the progression contribution only involves q dividing m-h. Hence the number of possible q is at most tau(m-h), independently of the detailed selected family. The bound tau(n)<<_eta X^eta together with the prime-power von Mangoldt mass O(sqrt(X) log^2 X) gives the first term of the author's (4):

    O_eta(H X^(1/2+eta) log^3 X).

The principal portion is a different sum and cannot be omitted. Bound its prime-power mass absolutely, multiply by the O(log X) logarithmic weight and by sum_(q<=Q)1/phi(q)=O(log X), then sum the O(H) shifts. This gives

    O(H sqrt(X) log^4 X).

Retaining or dropping the principal coprimality restrictions by an absolute upper bound is valid. In particular this step accounts for prime powers with primes dividing q as well as those not dividing q; it does not confuse these with primes dividing h. At eta=1/100 and H<=X^(2/7), the largest displayed power is X^(557/700), which is strictly smaller than X. Both nuisance terms are therefore o(X log X), and also smaller than the claimed completion bound.

Only after this replacement is every surviving m a genuine prime exceeding Q. Then m is a unit modulo every q. In the progression sum, h congruent to m modulo q forces (h,q)=1 automatically, so the h-coprimality restriction may be removed there. It must remain in the principal term, where it becomes the exact unit-residue projector. The order of operations in the draft is correct. Performing this extension before prime-power removal would need extra terms, and the draft does not do that.

All these estimates are unconditional. RH is only needed in the previously stated conversion from this discrepancy to the relevant aggregate zeta covariance component.

### 3. Uniform smooth separation of the actual kernel

Put epsilon=H/X=1/T, y=m/X and z=h/H. On the support, y-epsilon z lies in a fixed compact subset of (1,3/2), and z lies in a fixed compact subset of (1,2). Thus both original a-factors take their inverse-three-halves branch. Their product is exactly

    y^(-3/2) (y-epsilon z)^(-3/2).

The sinc phase is exactly

    epsilon^(-1) log(y/(y-epsilon z))
       = integral_0^z du/(y-epsilon u).

This integral representation also proves the removable epsilon=0 limit z/y and gives uniform bounds for every fixed mixed y,z derivative on a slightly larger fixed rectangle, for all sufficiently small epsilon. It avoids differentiating the misleading 1/epsilon factor separately. The sinc function is smooth at zero, so there is no hidden singularity. The support stays away from y-epsilon z=0 and from the a-factor branch corner; the minimum definition of a therefore introduces no derivative defect.

The same derivative bounds hold after multiplication by log(y-epsilon z). On a larger fixed rectangle, use fixed compact cutoffs and the two-variable Fourier series of the smooth amplitude. Its coefficients decay faster than any fixed power in both frequency indices, uniformly in epsilon. Each term becomes f_k(m/X)v_l(h/H). The prime-factor estimate used later depends only on the bounded sup norm of f_k, not on its derivatives; the finite-difference estimate for v_l costs at most a fixed polynomial in l. Uniform rapid coefficient decay absorbs that polynomial, so the separated estimates sum absolutely with a uniform constant. No approximation remainder is left unestimated.

Finally the exact cofactor identity is

    log((m-h)/q)=log X-log q+log(y-epsilon z).

The constant log X factor, the log q conductor coefficient, and the additional smooth logarithmic amplitude are the three legitimate cases treated in the author proof. The resulting log^(7/2) bound from the first two cases is harmlessly relaxed to log^4. A q-dependent function has not been silently included in a common smooth amplitude.

### 4. Scope and acceptance

The actual sinc kernel is retained, including its sign. No positivity, variance asymptotic, RH, or convergent critical-strip prime series is used in this component estimate. The completed bound remains larger than X log X throughout the displayed alpha interval. The draft says so explicitly.

This review accepts the fixed smooth packet only. A bounded-variation extension of the separated coefficient estimate may be possible, but the full sharp packet is not claimed or required here. No endpoint extension, parameter search, or new numerical prime experiment was performed. The attached receipt pins the reviewed author report, Round 9 source convention, and this review; its exact fraction checks verify the nuisance exponent and the support cap inequality, not asymptotic prime distribution.


<a id="report-36"></a>

# Current report 36: Actual-prime variance ranges and a missing logarithmic mixed moment

**Collection:** R10 — complete the actual shift packet.

**Source:** [research/dyson/round10/arithmetic-residual/ARITHMETIC_RANGE_AND_MIXED_MOMENT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/arithmetic-residual/ARITHMETIC_RANGE_AND_MIXED_MOMENT.md).

**SHA-256:** `c2d2a278ffe74d8f8d8a7c00980e5e57e6c508790ff96904db4479277d1daa8c`. **Git blob:** `fcff74de2703ccf23dc5cd8708dca39e46d994de`. **Original bytes:** 12502.

## Actual-prime variance ranges and a missing logarithmic mixed moment

Date: 2026-09-05. This is a bounded arithmetic-source audit and a conditional calculus lemma. **No improved lower bound for the actual residual or the coupled zeta statistic is proved.** There is no new point-process countermodel, prime-profile search or repetition of the Stieltjes continuation proof.

The negative decision has a concrete arithmetic basis. The checked Guth–Maynard theorem has a short-interval range that misses the shrinking edge region, and even its almost-all PNT error inside that range is much larger than the needed fluctuation scale. The checked RH short-interval variance comparison retains fixed constant losses and fixed-endpoint quantifiers. A further precise mixed moment of the genuine-prime tail would suffice; its numerical threshold is derived below, but that moment is not supplied by either source.

### 1. Object and the local prime scales

Retain the already reviewed Round 9 definitions L=log T, N=floor(T/L^6), and the genuine-prime residual R_(T,b)(t). This is the analytic prime-only continuation at s=1/2+b/(2L)+it with the prime polynomial through N subtracted. It includes the endpoint and pole terms of that continuation. It is not interpreted as a convergent bare prime Dirichlet series on this line.

Write

    r_T^p(b)=integral_0^T |R_(T,b)(t)|^2 dt /(T L^2),
    E_T(b)=exp(b) r_T^p(b).

The mesoscopic statistic uses the two widths b and 2b at the same height and cutoff. The previously reviewed prime-power-removal error is o(1) after its amplified normalization uniformly on 2<=b<=G(T), for any G(T)->infinity with G(T)=o(log log T). Thus it is legitimate to study this genuine-prime residual without pretending that the removed prime powers supply a fixed positive improvement.

To inspect a fixed portion of the first edge, put

    X=T^(1+s/b),  1<=s<=2,  h=X/T.

Then the exact exponent of h relative to X is

    log h/log X = s/(b+s).

This tends to zero as b increases. The size h nevertheless exceeds every fixed power of log X on these slow diagonals. Statements about intervals of length at most a fixed power of log X, or about X<=T, therefore do not cover this edge shell. Conversely, an estimate requiring h>=X^theta for a fixed theta>0 eventually misses it. These are arithmetic scale comparisons, not a conclusion from generic spectral positivity.

### 2. Guth–Maynard: exact range gap, then a separate moment gap

The primary source inspected is Guth and Maynard, [New large value estimates for Dirichlet polynomials, arXiv:2405.20552v2](https://arxiv.org/html/2405.20552v2), dated 7 April 2026. Corollary 1.4 gives an almost-all asymptotic for the prime count when

    X^(2/15+epsilon) <= h <= X^.99,

for fixed epsilon>0. The exceptional set has size O(X exp(-(log X)^(1/4))), and on the other integers x around X the count error is O_epsilon(h exp(-(log X)^(1/4))). This is an asymptotic count statement, not a sharp variance statement. The actual improved exponent is 2/15; this audit does not repeat the obsolete 1/6 exponent as if it were current.

Even if epsilon were set to zero, the edge shell above would have to satisfy

    s/(b+s) >= 2/15,  equivalently b <= 13s/2.

Hence when b>13 the entire fixed shell 1<=s<=2 is outside the theorem. At b=14, its endpoint exponents are 1/15 and 1/8, both below 2/15. This is an exact range calculation, not a numerical parameter scan. The admissible fixed-epsilon range is smaller still. In terms of X=T^alpha, this corollary's epsilon-to-zero endpoint is alpha>=15/13, while the needed shell has alpha=1+O(1/b). This endpoint is not asserted to exhaust the authors' methods.

The final Remark after the proof of Corollary 1.4 describes a sieve treatment of the critical six-factor case that could slightly lower the fixed exponent to 2/15-epsilon, at the cost of a prime-count error roughly O(epsilon^4 h/log X). For a fixed sufficiently small epsilon this remains a positive-power lower cutoff for h, so it still misses s/(b+s)->0. Its stated count error also does not determine a fluctuation-level second moment or the shrinking variance correction needed below. Thus this remark does not remove either obstruction; no optimality of 2/15 for the underlying method is claimed.

There is a second and independent obstruction even inside the source range. Converting the count bound to the Chebyshev weight costs O(log X). Bounding the exceptional intervals trivially then gives at best a consequence of the form

    sum_(integer x in [X,2X])
       |theta(x+h)-theta(x)-h|^2
        << X h^2 (log X)^2 exp(-c (log X)^(1/4)),

with some fixed c>0; harmless endpoint and partial-summation errors are smaller here. On the good set one can square the error, but the exceptional-set contribution has only the single exponential saving. The expected fluctuation scale for this variance is X h log(X/h). For h=X^theta with any fixed theta in the source range below .99, the quotient of the displayed error bound by that scale contains

    h log X exp(-c (log X)^(1/4)),

which tends to infinity. The quoted corollary alone therefore does not control the variance to constant accuracy, let alone the relative o(1/b) edge accuracy needed here. This diagnoses the precision of this theorem's stated consequence; it does not deny stronger consequences of its underlying methods after further argument.

The large-value Theorem 1.1 in the same source does not directly resolve this issue either. The paper specifies its main improvement over earlier bounds for length N<=T^(5/6-epsilon), while a single un-factorized prime block at X=T^(1+s/b) has length greater than T. A further factorization or arithmetic estimate could exploit the method, but that would be additional work, not an application of its ready-made full-block bound. The independent shifted-modulus lane studies such a different route and is not duplicated here.

### 3. What the checked RH short-interval variance results provide

The other primary source is Carneiro–Chandee–Chirre–Milinovich, [On Montgomery's pair correlation conjecture: a tale of three integrals](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf). Its short-interval statistic is

    J(beta,T)=integral_1^(T^beta)
       [psi(x+x/T)-psi(x)-x/T]^2 dx/x^2.

The paper recalls the asymptotic J(beta,T)~beta^2 log^2(T)/(2T) for fixed 0<beta<=1. That is the side before the first edge. It does not evaluate the increment from beta=1 to beta=1+s/b>1. Theorem 3 / Corollary 4 give, for large fixed beta, constants 0.8376 and 1.4283 multiplying beta log^2(T)/T. Here beta is the exponent delimiting the prime range, not the damping parameter b. Sending the damping b to infinity does not make beta=1+s/b a large-beta instance of that theorem.

For finite endpoint intervals, Theorem 14 and Corollary 15 give a precise comparison with integrated pair correlation, with factors L_minus=0.9028... and L_plus=1.0736... . Both are separated from one by fixed amounts. As a stand-alone comparison, this retains roughly 9.7% lower-side and 7.4% upper-side slack, whereas the first-edge task requires a relative error decreasing like o(1/b). Those fixed losses cannot be read as the required coefficient of 1/b. Moreover the source's fixed-endpoint liminf/limsup statements do not license a moving endpoint beta(T)=1+s/b(T) without a uniformity or diagonal argument.

This does not claim that every RH variance theorem is exhausted or that no sharper short-interval argument exists. It records the exact scope and quantitative gap of the primary results checked here. It also avoids replacing the earlier Round 9 failure of individual logarithmic-derivative bounds by a claim that an almost-all prime-count asymptotic has already solved their coupled moment.

### 4. A concrete mixed moment of the same arithmetic tail

There is a useful way to state the missing arithmetic input more precisely. Define the logarithmically weighted companion using the derivative of the actual analytic residual:

    K_(T,b)(t) = -R_(T,b)(t) - 2 partial_b R_(T,b)(t),

    M_T(b) = exp(b)/(T L^2)
        Re integral_0^T R_(T,b)(t) conjugate(K_(T,b)(t)) dt.

At fixed T this derivative exists on b>0 in the relevant critical-strip range under RH. Differentiation of the already available centered-tail integral is justified by its additional logarithmic factor and the same RH bound for theta(x)-x. Endpoint and pole terms are differentiated as well. No derivative estimate is inferred by differentiating an uncontrolled o(1) remainder.

In the absolutely convergent right half-plane this companion weights the genuine-prime tail by log(p)/L-1; in the working strip it is the analytic continuation with its required centering. Thus M_T is a specific correlation with a logarithmic excess weight, not just the norm of either residual and not a freely chosen covariance model.

The exact derivative identity is

    M_T(b) = -d/db E_T(b).

This gives the following conditional criterion. Suppose there are fixed epsilon>0 and an increasing slow envelope G(T)=o(log log T) such that, uniformly on B0<=s<=2G(T),

    M_T(s) >= 1/s^2 - (2-epsilon)/s^3 - eta_T/s^3,
    eta_T -> 0.

Then the original AH-excluding mesoscopic target follows, with a quantitative gap:

    lim_(B->infinity) liminf_(T->infinity)
       inf_(B<=b<=G(T)) C_T(b)
          >= -3/4 + 3epsilon/8 > -3/4.

This is a sufficient additional arithmetic hypothesis, not a result established for M_T. It is stronger than merely knowing each residual's leading norm, but weaker in a different direction than demanding a full collection of prime pair correlations. It singles out exactly one signed mixed moment along a slow range.

To verify the implication, rewrite the prime-only coupled statistic exactly as

    C_T^p(b)=b^2 [E_T(b)-E_T(2b)-1/(2b)
                  -exp(-2b)E_T(b)+exp(-4b)E_T(2b)].

The already reviewed RH upper estimates of Round 9 imply E_T(s)=O(1) uniformly on the slow range: their absolute finite-height error remains negligible after multiplication by exp(s), and their limiting residual upper expression is O(exp(-s)). Prime-power removal preserves this conclusion. Therefore the two exponentially small terms contribute o(1) in the displayed double-limit regime; this uses an actual previously checked upper estimate, not an assumption of perfect residual asymptotics.

Now integrate M_T(s)=-E_T'(s) from b to 2b. The exact integrals are

    integral_b^(2b) s^(-2) ds = 1/(2b),
    integral_b^(2b) s^(-3) ds = 3/(8b^2).

The asserted lower limit follows, and the reviewed uniform genuine-prime replacement error carries it back to C_T. This reasoning needs control up to 2G(T), not only G(T), and retains the uniform range needed for compatibility with the AH slow-diagonal argument. No simplicity assumption enters.

The decisive missing quantity is therefore the coefficient below 2 in this log-weighted mixed-moment deficit. None of the inspected short-interval mean-count or variance theorems supplies that coefficient. A Cauchy–Schwarz estimate using only separate norms does not evaluate this signed mixed moment; a new arithmetic decorrelation, projection estimate, or weighted short-interval covariance result would be needed.

### 5. Evidence, reproducibility and stopping decision

[check_edge_mixed_moment.py](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/arithmetic-residual/check_edge_mixed_moment.py) and its [JSON](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/arithmetic-residual/check_edge_mixed_moment.json) check the exact 2/15 range threshold, the two fixed b=14 endpoint examples, the hyperbolic algebra and the coefficient 3epsilon/8. They do not evaluate actual zeta zeros, search parameters, or test the mixed-moment hypothesis.

The source receipt pins the retrieved Guth–Maynard v2 HTML and the already archived CCCM text/PDF together with the relevant Round 9 reports. Third-party source bodies are local references, not material to duplicate in a public code archive. There is no claim that this narrow audit is a complete survey of all prime-variance literature.

The bounded conclusion is negative but specific: the checked improved prime-count theorem misses the growing-damping edge and lacks fluctuation-level precision even where it applies; the checked RH variance comparisons do not supply the required shrinking first correction. The conditional logarithmic mixed-moment inequality is a reviewable next arithmetic obligation. Its proof, or a weaker averaged version sufficient on [b,2b], remains open here. Repeating finite prime-factor coefficient scans and general PSD models is postponed.


<a id="report-37"></a>

# Current report 37: Independent review of the arithmetic range and mixed-moment audit

**Collection:** R10 — complete the actual shift packet.

**Source:** [research/dyson/round10/arithmetic-residual/INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round10/arithmetic-residual/INDEPENDENT_REVIEW.md).

**SHA-256:** `375ab6c0ae80f43c86273a38868b045732f547ac9ce2eb3ffa363edaad2bd1a8`. **Git blob:** `7db5b9a77ecf065e4b9289df3de26c9e72332032`. **Original bytes:** 4155.

## Independent review of the arithmetic range and mixed-moment audit

Date: 2026-09-05. Reviewer: root. Accepted as a bounded primary-source audit and a conditional calculus implication. No actual-prime lower bound is proved.

The final author report `ARITHMETIC_RANGE_AND_MIXED_MOMENT.md` has SHA256 `c2d2a278ffe74d8f8d8a7c00980e5e57e6c508790ff96904db4479277d1daa8c`. The root read the complete report and script, the actual Guth–Maynard v2 Corollary 1.4 and following Remark, and the saved CCCM Theorem 3/Corollary 4 and Theorem 14/Corollary 15 passages. Earlier Round 9 results are used with their independently reviewed uniformity, not strengthened by assumption.

### Source range and error

Corollary 1.4 states the prime-count asymptotic for h>=X^(2/15+epsilon), with fixed epsilon, outside an exponentially small proportion of integer starting points. In the edge shell X=T^(1+s/b), h=X/T, the exponent is exactly s/(b+s). The corollary's limiting epsilon-zero threshold is b<=13s/2; the shell 1<=s<=2 is outside it once b>13. The source's subsequent Remark permits a slight fixed-epsilon improvement with a weaker error, not an exponent tending to zero. The author now records that distinction explicitly.

The conversion of a prime count to a log-weighted count does not need a new uniform theorem for every inner endpoint. On [x,x+h], log p=log x+O(h/X). Multiplying the stated count approximation by log x introduces the displayed exponential error and an elementary O(h²/X) remainder (a sharper version is unnecessary). For h<=X^.99 that remainder is absorbed by the retained exponential error. The exceptional intervals are bounded trivially. The resulting sufficient upper bound on the squared error is far above X h log(X/h) for fixed positive h-exponent. This demonstrates a limitation of that direct consequence of the corollary, without claiming that its methods cannot yield stronger information.

The CCCM constants and quantifiers are correctly reported. Its beta is the prime-range endpoint, not the damping b. Fixed multiplicative constants 0.9028... and 1.0736... are not an error tending to zero with b. Fixed-endpoint limiting comparisons do not themselves provide the moving-endpoint uniformity required here. This is a narrow audit of these sources, not an exhaustive impossibility theorem for all known prime-variance methods.

### Conditional mixed moment

For the actual analytic residual at fixed T, differentiating the centered integral on b>0 is valid under RH: an extra log factor is integrable at every fixed positive distance from the critical line. Pole and endpoint terms must also be differentiated, as the report states. There is no differentiation of an unspecified asymptotic remainder.

With E(b)=e^b ||R_b||²/(T log²T) and K_b=-R_b-2 partial_b R_b, the real inner-product identity is M(b)=-E'(b). In the absolutely convergent region K has coefficient log(p)/log(T)-1, confirming the sign and factor two. Its use in the working strip is analytic continuation, not an unregularized prime series.

The exact two-scale identity includes -e^(-2b)E(b)+e^(-4b)E(2b). The previously reviewed RH upper estimate, after subtracting the short-prime diagonal, is O(e^(-b)) for r(b) on the slow range; its uniform height error and the prime-power replacement stay negligible after multiplication by e^b. Thus E=O(1) there, and the exponential correction vanishes uniformly as the lower cutoff B tends to infinity. A crude pointwise bound alone would not justify this step.

Finally, integrating 1/s²-(2-epsilon)/s³ from b to 2b gives 1/(2b)-3(2-epsilon)/(8b²). After multiplication by b² and subtraction of 1/(2b), the threshold is exactly -3/4+3epsilon/8. The author requires the assumed inequality through 2G(T), including a uniform o(s^-3) error; that is the needed quantifier. This implication is accepted. The mixed-moment hypothesis itself remains completely unproved in these notes, and the source audit supplies no positive epsilon.

The small exact script checks only the scalar algebra and range endpoints. Independent replay is a separate implementation check and does not certify a new analytic estimate.


<a id="report-38"></a>

# Current report 38: Round 11: remove the shift-length loss using actual RH prime input

**Collection:** R11 — RH small arcs and actual conductor structure.

**Source:** [research/reports/dyson_round11.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/dyson_round11.md).

**SHA-256:** `293125227f1a9eef69441f1d15934ecd970466cce7bb14eb2aa1ee273886e9ad`. **Git blob:** `4ff7d5072a8c3249fb5c4bdf4d4130251d36536c`. **Original bytes:** 8602.

## Round 11: remove the shift-length loss using actual RH prime input

Date: 2026-09-05. **Under RH, this round improves the same actual smooth shifted-prime discrepancy to X^1.023 log^5 X.** It also proves a narrow arithmetic obstruction to coefficient-only power savings and makes the log-weighted residual's positive diagonal explicit. None of these results proves the required new zeta pair-correlation lower bound.

### The component improvement

Keep the Round 10 discrepancy, with Q=X^(523/1000), X=T^alpha, 6/5<=alpha<=7/5 and H=X/T. It is the actual Mobius-log weighted progression discrepancy selected by the Round 9 complementary conditions, with its original sinc kernel and fixed smooth cutoffs V in C_c^infinity(1,2) and chi in C_c^infinity(1,3/2). The [full proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/prime-frequency/CENTERED_SMALL_ARC_BOUND.md) establishes

\[
\boxed{|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{X(X+Q^2)}\,(\log X)^5
\ll X^{1.023}(\log X)^5\qquad\text{under RH}.}
\]

This removes sqrt(H) from Round 10. The additional RH assumption is material; the earlier bound was unconditional. The saving in powers of X is 1/12 at H=X^(1/6), and 1/7 at H=X^(2/7). The bound applies to any squarefree subfamily with the specified cap and therefore does not claim a new dense-divisibility theorem.

After division by the required X log X covariance scale, the estimate is still O(X^.023 log^4 X). The full sharp shift packet, complementary divisor piece, support main terms and final signed covariance remain outside this bound. In particular, the compact Fourier target greater than -3/5 and the two-scale target 1/16 remain unproved.

### Where the arithmetic gain comes from

[Bhowmik–Schlage-Puchta, Lemma 3](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/Goldbach4.2.10.pdf), printed page 3, proves under RH

\[
\int_{-1/y}^{1/y}\left|\sum_{n\le x}(\Lambda(n)-1)e(\beta n)\right|^2d\beta
\ll (x/y)\log^4 x,\qquad 1\le y\le x.
\]

Its proof includes the cutoff errors in the Selberg/Gallagher passage. Partial summation transfers it to a smooth genuine-prime polynomial minus its integer mean, E_f=A_f-B_f. Prime powers cost no more than the same bound. The frequency derivative is another such polynomial, E_f'=2pi i X E_(u f), so its norm is controlled without differentiating an asymptotic error.

The exact Round 10 pairing has coefficients C_(a/d)=S_v(a/d)M_d, with

\[
M_d=\sum_{q\in\mathcal Q,\ d\mid q}\frac{\mu(q)}q,
\qquad S_v(\beta)=\sum_h v(h/H)e(-\beta h).
\]

Equal rational frequencies are already merged. Sampling on disjoint intervals of length comparable to Q^-2 and retaining only the local arc gives a squared prime norm O(X(X+Q^2)rho log^4 X). The coefficient mass on the jth dyadic band is O(H 2^((1-2J)j) log^3 Q), while rho is at most 2^j/H. These factors cancel H before summation. J=2 suffices to sum all frequency tails.

Both remaining mean terms are retained: the smooth integer mean is handled by Poisson summation, and the primitive Ramanujan mean by a first-power shift bound and the reciprocal-totient sum. Neither introduces a new H loss. The two-variable Fourier separation includes derivative costs in both indices; its rapid decay handles the actual sinc kernel and log cofactor. The original progression prime-power error and the later centered-polynomial prime-power subtraction are distinct, and both are included.

The [independent review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/prime-frequency/SMALL_ARC_INDEPENDENT_REVIEW.md) checks the primary source, weighted prefixes, derivatives, local sampling, every tail band, both means and the full kernel. Root also read the complete argument. This is an internally reviewed ordinary proof, not formal verification or a novelty claim for the classical ingredients.

### Actual prime moduli prevent a coefficient-only shortcut

The [conductor construction](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/conductor-arithmetic/CONDUCTOR_MASS_LOWER_BOUND.md), with [independent review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/conductor-arithmetic/INDEPENDENT_REVIEW.md), fixes the full canonical family of all distinct q=[D,E] satisfying the Round 9 balanced complementary predicates and coefficient mu(q). For fixed nonnegative nonzero V it proves

\[
\sum_{d,a}^{*}|S_v(a/d)M_d|^2\gg_V H/(\log X)^{348}.
\]

The construction uses two primes in a fixed-ratio interval of exponent .09 and 346 primes in one of exponent 343/346000. All factors are distinct. Their product is in (Q/2,Q], has positive Mobius sign, and splits into two roots within the exact radius .2615. Only the large prime in each root triggers its guard, leaving a strict margin .0255. PNT and unique factorization give a positive constant times Q/log^348 X different moduli, for every sufficiently large X.

At a terminal conductor d=q>Q/2 no other multiple is at most Q, so its full signed coefficient is exactly 1/d. Enough primitive low numerators have a shift transform bounded below by a positive multiple of H. Summing their squares proves the lower bound. An additional log q improves its logarithmic power to log^-346 X.

This excludes an O(H X^(-eta)) coefficient-norm bound for any fixed eta>0 on this full family. It does not exclude a specially pruned family, different weights, frequency localization, or cancellation between the actual prime polynomial and these coefficients. It is entirely compatible with the small-arc improvement above. No numerical prime realization or claim of an effective threshold is involved.

### The exact positive diagonal leaves a signed arithmetic remainder

The [mixed-tail note](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/log-weighted-tail/ARITHMETIC_DIAGONAL_AND_SOURCE_GAP.md), with [independent review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/log-weighted-tail/INDEPENDENT_REVIEW.md), starts from the genuine-prime residual R_b at displacement b/(2 log T), with N=floor(T/log^6 T). Define K_b=-R_b-(log T)^(-1)partial_s R_b and

\[
M_T(b)=\frac{e^b}{T\log^2T}\operatorname{Re}\langle R_b,K_b\rangle.
\]

The finite centered measure uses prime atoms of mass log p minus Lebesgue measure on (N,Y]. RH gives an explicit uniform cutoff error for it and its log-weighted companion. The pole is then removed at O(e^b log^-3 T), retaining the endpoint correction. On 2<=b<=2G(T), G=o(log log T), the result is

\[
M_T(b)=\frac1{b^2}+\frac2{b^3}+\mathcal B_T(b)+o(b^{-3}).
\]

Here B_T is the combined centered off-diagonal remainder, including both prime-continuum terms and the continuum square. Only their combined limit is justified. The explicit diagonal comes from prime lengths T^(1+O(1/b)); the accessible slice below T is nonpositive and negligible.

A uniform bound B_T(s)>=-(4-epsilon)/s^3-o(s^-3), or the stated strict integrated improvement, would supply the earlier AH-excluding criterion. **Neither bound is proved.** Chirre's checked derivative identity leaves the unknown out-of-band form-factor integral; its fixed-width asymptotic does not supply this arithmetic estimate. The valid but enormous analytic cutoff is not presented as a practical computation.

### Verification, provenance and next step

All 18 original files, 536,670 bytes, are retained locally under `Astra-Local-Archive/round11-originals/`; 15 research files are public verbatim. Three third-party PDF/text/HTML bodies stay local with URL/hash receipts. The [intake manifest](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/INTAKE_MANIFEST.json) records each file. The [separate replay](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/logs/round11-integration/recheck.json) checks both bounded scripts in a copy, excluding only the temporary primary-source path from the conductor certificate. The complete small-arc JSON is identical. Exact checks cover rational exponents, counting constants, 384 finite arc counts and 2,901 unique frequency memberships; they are not tests of RH itself.

```text
python3 research/logs/round11-integration/recheck.py --prime-gap-source /path/to/openai-short-gaps.pdf
python3 tools/verify_manifest.py
```

The next useful attempt must use signed joint prime/modulus cancellation beyond positive sampling, or prove a one-sided estimate for the combined mixed remainder. The coefficient construction alone cannot rule these out. A generic positive-sampling improvement, an unqualified import of the 186 dispersion theorem, and short-interval upper bounds are being checked against their exact hypotheses before further computation.

The long PDFs retain their previously stated checkpoints; this report adds a new source record. Rollback is a revert of this slice. Formalization, a full covariance theorem, and a solved famous conjecture remain outstanding. No new external-model session, large scan, or infrastructure layer was added.


<a id="report-39"></a>

# Current report 39: Removing the shift-length loss from the actual completed pairing, under RH

**Collection:** R11 — RH small arcs and actual conductor structure.

**Source:** [research/dyson/round11/prime-frequency/CENTERED_SMALL_ARC_BOUND.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/prime-frequency/CENTERED_SMALL_ARC_BOUND.md).

**SHA-256:** `9ebf2d8daaac37702302f5a798611e6a6152e352e5b7dd680c319ba76b3f6e29`. **Git blob:** `ab5378d9ff03e967ef0c74a01947c00a7a61e835`. **Original bytes:** 13797.

## Removing the shift-length loss from the actual completed pairing, under RH

Date: 2026-09-05. Status: ordinary proof independently audited and accepted for the stated RH component bound; see [the separate review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/prime-frequency/SMALL_ARC_INDEPENDENT_REVIEW.md). This proves a bound for the same fixed smooth discrepancy component as Round 10, assuming RH. It does not prove the needed zeta covariance estimate, AH failure, Montgomery's conjecture, or a new prime-gap bound. No novelty claim is made for the classical small-arc method.

With the Round 10 notation

    X=T^alpha, 6/5<=alpha<=7/5,
    H=X/T=X^theta, 1/6<=theta<=2/7,
    Q=X^(523/1000),

the conclusion is

    |D_Q^V(X,T)| <<_(V,chi) sqrt[X(X+Q^2)] (log X)^5
                     << X^(1023/1000) (log X)^5.                 (1)

Compared with Round 10's unconditional bound X^(1023/1000) sqrt(H) log^4 X, this removes the factor sqrt(H), at the explicit additional assumption of RH. The saving in the exponent of X is theta/2, ranging from 1/12 to 1/7. It still leaves an X^(23/1000) power loss relative to X log X, before logarithms. Thus this is a useful component improvement, not the requested historical conjecture.

### 1. Exact object, ranges and the arithmetic input

Keep the actual squarefree family Q_X contained in (sqrt(X),Q], the discrepancy convention and the kernel from the frozen Round 10 report:

    Delta(F;h mod q) = sum_(m=h mod q) F(m)
                       - phi(q)^(-1) sum_((m,q)=1) F(m),

    w_h(u)=chi(u/X) a_u(X) a_(u+h)(X)
                         sinc_0(T log(1+h/u)),
    a_u(X)=min((u/X)^(1/2),(X/u)^(3/2)),

    D_Q^V = sum_h V(h/H) sum_(q in Q_X,(q,h)=1) mu(q)
                 Delta(Lambda(m) w_h(m-h) log((m-h)/q);h mod q), (2)

where V is fixed in C_c^infinity(1,2), chi is fixed in C_c^infinity(1,3/2), and sinc_0(x)=sin(x)/x with its removable value at zero. Functions inside Delta are zero outside their stated support. Formula (1) actually holds for any squarefree subfamily in this modulus interval; no new dense-divisibility property is assumed.

The primary analytic input is Bhowmik–Schlage-Puchta, [Mean representation number of integers as the sum of primes](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/Goldbach4.2.10.pdf), Lemma 3, printed page 3. For

    R_x(beta)=sum_(n<=x) (Lambda(n)-1) e(beta n),
    e(t)=exp(2 pi i t),

it proves under RH that

    integral_(-1/y)^(1/y) |R_x(beta)|^2 d beta
                    << (x/y) (log x)^4,  1<=y<=x.             (3)

The author's proof uses Selberg's short-interval mean square and Gallagher's lemma, including the cutoff endpoint contributions. We use this already proved centered small-arc bound, not an asymptotic pair-correlation conjecture. The fourth logarithmic power is retained.

We first treat a separated smooth amplitude f(m/X)v(h/H), with f,v compactly supported in fixed positive intervals. Restoring the actual kernel and logarithm is done in Section 6. All reduced frequencies have the complete range

    2<=d<=Q, 1<=a<d, gcd(a,d)=1, beta=a/d.                    (4)

There is no zero frequency: its centered completed contribution vanishes exactly. Neither a lower cutoff d>sqrt(X) nor an inherited cutoff on numerator a is asserted. The arc weights, rather than the original modulus lower bound, suppress small d.

### 2. Centered genuine primes, smooth weights and derivatives

For fixed smooth f supported in [c,C], with 0<c<C fixed, set

    A_f(beta)=sum_p (log p) f(p/X)e(beta p),
    B_f(beta)=sum_n f(n/X)e(beta n),
    E_f(beta)=A_f(beta)-B_f(beta).                            (5)

The sum defining B_f is over integers; this is not a silently substituted continuous main term. The polynomial E_f has genuine-prime coefficients minus the integer mean.

First apply partial summation to the Lambda-minus-one prefix polynomials in (3). Minkowski's integral inequality gives, for 1/X<<rho<=1/2,

    integral_(||beta||<=rho) |sum_n (Lambda(n)-1)
                                   f(n/X)e(beta n)|^2 d beta
                              <<_f X rho (log X)^4.          (6)

We only need rho>=1/H, so the length y=1/rho is at most H=o(X) and eventually less than every prefix endpoint x>=cX occurring in partial summation. For larger constant arcs one may equally use Parseval. The constants depend on the sup norm and total variation of f on a fixed interval.

Replacing Lambda by genuine primes subtracts the finite polynomial supported on p^j near X with j>=2. Its absolute value is at most

    sum_(p^j near X,j>=2) log p << sqrt(X) (log X)^2.

Its squared integral on this arc is therefore O(X rho log^4 X). Consequently (6) holds for E_f itself. There is no use of a critical-strip prime Dirichlet series here.

The derivative is exactly

    E_f'(beta)=2 pi i X E_(u f(u))(beta).

Applying the same argument with u f(u) proves

    integral_(||beta||<=rho) |E_f'(beta)|^2 d beta
                              <<_f X^3 rho (log X)^4.        (7)

This controls the frequency derivative by another source-backed centered prime polynomial. No small L2 estimate has been differentiated formally.

### 3. Sampling the small arc at distinct Farey frequencies

Distinct reduced fractions in (4) are separated on the circle by at least Q^(-2). Around each selected frequency choose a disjoint interval of length comparable to Q^(-2). For any continuously differentiable F, the fundamental theorem of calculus applied to |F|^2, followed by averaging on each such interval, gives

    sum_(beta in selected frequencies) |F(beta)|^2
      << Q^2 integral_U |F(t)|^2 dt
          + integral_U |F(t) F'(t)| dt,                      (8)

where U is their union. One direct proof is to bound |F(beta)|^2 by the interval average plus 2 integral |F F'| and then sum over the disjoint intervals. This is a local estimate; the integrals do not need to run over the whole circle.

If ||beta||<=rho, then U lies inside ||t||<=rho+O(Q^(-2)). Throughout our range rho>=1/H and Q^2>>H, this enlargement is O(rho). At arcs reaching the whole circle use Parseval for F and F'. Inserting (6)–(7) into (8), and applying Cauchy–Schwarz only to its derivative integral, gives

    sum_(d,a as in (4), ||a/d||<=rho) |E_f(a/d)|^2
                  <<_f X (Q^2+X) rho (log X)^4.              (9)

This is the arithmetic gain: centering and the RH prime mean square supply the factor rho. Merely knowing that the number of frequencies is smaller would not justify (9) with this factor. The local sampling argument does not replace the minimum spacing Q^(-2) by a larger spacing.

### 4. Dyadic frequency tails, with every coefficient retained

For the separated shift weight put

    S_v(beta)=sum_h v(h/H)e(-beta h),
    M_d=sum_(q in Q_X,d|q) mu(q)/q,
    C_(a/d)=S_v(a/d) M_d.                                   (10)

Round 10's exact completion gives the pairing

    sum_(d,a as in (4)) C_(a/d)
                 [A_f(a/d)-mu(d)A_f(0)/phi(d)].              (11)

We use only |M_d|<=(1+log(Q/d))/d. Finite summation by parts gives, for each fixed integer J>=2,

    |S_v(beta)| <<_(v,J) H(1+H||beta||)^(-J).                (12)

Partition all nonzero reduced frequencies into the central arc I_0 with ||beta||<=1/H and the annular bands

    I_j: 2^(j-1)/H < ||beta|| <= min(2^j/H,1/2), j>=1,      (13)

stopping when the circle has been covered. For each band, the numerator condition is exactly on min(a,d-a). In the central arc it is min(a,d-a)<=d/H; in I_j it lies between 2^(j-1)d/H and 2^j d/H, with the upper half-circle clipping. Nonempty arcs with upper radius rho require d>=1/rho. This treats low denominators, not just the top block.

For fixed d the number of fractions in an arc of upper radius rho<=1/2 is at most 2 rho d, even before imposing coprimality. Using (12), the divisor-coefficient bound, and summing 1/d proves

    sum_(beta in I_j) |C_beta|^2
                  <<_(v,J) H 2^((1-2J)j) (log(2Q))^3,      (14)

with j=0 interpreted as the central arc. The factors implicit in the first annulus are absolute constants. No sharp truncation of S_v has been made.

Apply (9) with rho at most 2^j/H, or with the whole-circle Parseval bound at the final band. Cauchy–Schwarz on I_j gives

    |sum_(beta in I_j) C_beta E_f(beta)|
      <<_(f,v,J) sqrt[X(Q^2+X)]
                    2^((1-J)j) (log X)^(7/2).              (15)

The series over j converges already for J=2. Therefore

    |sum_beta C_beta E_f(beta)|
                   <<_(f,v) sqrt[X(Q^2+X)] log^(7/2) X.     (16)

Unlike the unweighted Round 10 sampling, this retains the concentration in a width 1/H arc and also bounds every tail band.

### 5. Both mean terms in the completed pairing

Two terms remain after A_f is replaced by E_f. They are different and are bounded separately.

First, B_f is a smooth integer polynomial. Poisson summation gives, for each fixed A>0,

    |B_f(beta)| <<_(f,A) X(1+X||beta||)^(-A).

Every nonzero fraction in (4) has ||beta||>=1/Q, while X/Q is a positive power of X. Also (12) implies

    sum_(a=1)^(d-1) |S_v(a/d)| <<_v d                       (17)

for every d: compare with an integral when d>=H, and use the convergent a^(-J) sum when d<H. It follows that sum_beta |C_beta|<<Q log(2Q). Thus the B_f contribution is at most

    O_(f,v,A)(X Q log(2Q) (X/Q)^(-A)),                      (18)

which is negligible with a fixed sufficiently large A. This estimate uses the discrete integer mean itself, so no continuous/discrete substitution error is hidden.

Second, the exact primitive Ramanujan principal term in (11) is bounded by

    |A_f(0)| sum_(d<=Q) |M_d| |mu(d)|/phi(d)
                                   sum_(a,d)=1 |S_v(a/d)|
         <<_f,v X log(2Q) sum_(d<=Q) 1/phi(d)
         <<_f,v X (log(2Q))^2.                             (19)

Here |A_f(0)|<<_f X follows from Chebyshev, and the elementary reciprocal-totient sum is O(log Q). Using a global Cauchy–Schwarz bound for this principal term would unnecessarily reintroduce an H loss; (19) avoids it without asserting cancellation.

Together (16), (18), and (19) prove the separated pairing estimate. Frequencies d=1 remain absent because their completed centered contribution is identically zero, not because a large term was discarded by hand.

### 6. The actual logarithm, smooth kernel, and prime-power discrepancy

The log q version of M_d costs one extra logarithm. Its analogue of (14) has log^5 rather than log^3, so (16) has log^(9/2). The corresponding principal term (19) costs at most log^3. The factor log X is treated explicitly in the same way.

For the actual amplitude, use epsilon=1/T, y=m/X, z=h/H. The frozen Round 10 proof and its independent kernel audit show that it is exactly

    V(z) chi(y-epsilon z) y^(-3/2) (y-epsilon z)^(-3/2)
        sinc_0(integral_0^z du/(y-epsilon u)),                (20)

and that this function and its product with log(y-epsilon z) have uniformly bounded mixed derivatives of every fixed order on a fixed rectangle. The source identity

    log((m-h)/q)=log X-log q+log(y-epsilon z)

is retained. Expand the smooth amplitudes in a two-variable Fourier series with fixed outer cutoffs. Unlike the earlier global sampling proof, the constants here depend on the variation of the m-factor as well as the derivatives of the h-factor. Both costs grow polynomially in the two Fourier indices, and the uniform rapid decay of the coefficients absorbs both. Thus the bound sums for the actual kernel, with no approximation error or unrecorded oscillatory derivative loss. We round log^(9/2) up to log^5.

The exact completion used genuine primes to make every m near X a unit modulo q. The original discrepancy (2), however, contains Lambda. The frozen Round 10 argument bounds the change in both its progression and principal sums by

    O_eta(H X^(1/2+eta) log^3 X + H sqrt(X) log^4 X).        (21)

This is logically distinct from subtracting the finite prime-power polynomial in (6). The former makes the modulus completion exact; the latter identifies the centered prime polynomial used in the source mean-square estimate. Both are included. Fixing eta=1/100 makes (21) o(X log X) uniformly for H<=X^(2/7), so it is smaller than (1). This completes the proof.

### 7. Quantitative decision and remaining arithmetic task

The improved exponent is 1.023 throughout the entire specified theta range. At theta=1/6 the previous exponent was 3319/3000=1.106333..., and at theta=2/7 it was 8161/7000=1.165857.... The conditional power savings are respectively 1/12 and 1/7. They are comparisons between an RH consequence and the earlier unconditional component estimate; the assumption change is material.

After the actual covariance normalization 1/(X log T), a bound of this size is still O(X^.023 log^4 X), which does not tend to zero. Ordinary RH small-arc control therefore removes the shift-length loss but does not settle the selected divisor component at the required precision. Replacing (3) by a conjectural sharp variance asymptotic would not by itself remove the Q^2 sampling scale used in this proof.

The remaining task is quantitative cancellation in the actual signed pairing of the conductor coefficients M_d and the centered genuine-prime exponential sums, or another argument improving the aggregate top-conductor contribution beyond this sampling/Cauchy–Schwarz bound. No statement that such cancellation is impossible is made. The independent conductor lane checks whether the source support removes high d; this proof does not assume that it does.

The only computation here is a small exact check of exponents, finite arc counting, and the dyadic geometric factors. The proof uses no fitted constants, zeta-zero sample, coefficient search, or unbounded scan. Other divisor pieces and omitted covariance ranges remain outside its scope.


<a id="report-40"></a>

# Current report 40: Independent review of the RH centered-small-arc improvement

**Collection:** R11 — RH small arcs and actual conductor structure.

**Source:** [research/dyson/round11/prime-frequency/SMALL_ARC_INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/prime-frequency/SMALL_ARC_INDEPENDENT_REVIEW.md).

**SHA-256:** `fdeba2af8e447ed7ec382155496f22e23255267f0d4051afdc3759a1f933daab`. **Git blob:** `bc9dc853d1a9f9046caac3a8d59c91e701549bff`. **Original bytes:** 9325.

## Independent review of the RH centered-small-arc improvement

Date: 2026-09-05. Reviewer: `yau_flow`, separately from the author `residual_gram`.

**Verdict:** the written proof of
\[
|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{X(X+Q^2)}\log^5X,
\qquad Q=X^{523/1000},
\]
is accepted under RH for the fixed smooth packet and modulus family specified in the author report. The removal of the previous \(\sqrt H\) factor is supported by actual centered-prime input. No lost tail band, undeclared GRH assumption, or omitted mean term was found. The bound remains larger than the required \(X\log X\) covariance scale. This is an ordinary independent proof audit, not formal verification or a claim of novelty.

### 1. Primary source and its exact applicability

I read Lemma 3 and its proof on printed page 3 of Bhowmik–Schlage-Puchta, [Mean representation number of integers as the sum of primes](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/Goldbach4.2.10.pdf), together with the preceding definitions and Lemmas 1–2. The PDF SHA-256 is `6cf48524eb9473cca93c1ce0ea97e00fc7dab7c49a3db4e01a490cc165296607`.

The polynomial is exactly the finite prefix with coefficients \(\Lambda(n)-1\). The centered interval is \([-1/y,1/y]\), and the upper bound is \((x/y)\log^4x\) under RH. The source states \(y\leq x\); the application uses the unproblematic subrange \(1\leq y\leq x\). Its proof includes the two prefix-edge regions, so no unproved endpoint cancellation is being imported. The source's separate discussion of GRH near general rational arcs is not needed here: this proof uses its RH arc around zero, then a local sampling inequality at points within that arc.

### 2. Weighted prefixes, genuine primes, and frequency derivatives

Let \(f\) have fixed compact support in \([c,C]\subset(0,\infty)\). Stieltjes partial summation expresses the weighted \(\Lambda-1\) polynomial as an integral of prefix polynomials with endpoints \(x\in[cX,CX]\), plus any endpoint terms. Minkowski's inequality gives a factor controlled by \(\|f\|_\infty+\int|f'|\). On the needed arcs, \(\rho\geq1/H\), so \(y=1/\rho\leq H=o(X)\), eventually below every prefix endpoint. The source therefore applies uniformly, yielding
\[
\int_{\|\alpha\|\leq\rho}|E_f(\alpha)|^2\,d\alpha
\ll_f X\rho\log^4X.
\tag{1}
\]
Here \(E_f=A_f-B_f\), with \(A_f\) genuinely prime-supported and \(B_f\) the integer polynomial. Replacing the von Mangoldt coefficients by prime coefficients subtracts a finite prime-power polynomial. Its sup norm is \(O_f(\sqrt X\log^2X)\), so its squared integral is \(O_f(X\rho\log^4X)\). This proves (1) for exactly the polynomial used later.

The derivative identity
\[
E_f'(\alpha)=2\pi iX E_{u f(u)}(\alpha)
\]
is exact coefficient by coefficient. Applying (1) with the new fixed weight \(u f(u)\) gives
\[
\int_{\|\alpha\|\leq\rho}|E_f'(\alpha)|^2\,d\alpha
\ll_f X^3\rho\log^4X.
\tag{2}
\]
Thus no estimate has been formally differentiated. The needed seminorms of both \(f\) and \(u f\) are accounted for.

### 3. Local sampling retains the original Farey spacing

All distinct reduced fractions with \(2\leq d\leq Q\) have circular separation at least \(Q^{-2}\). Take disjoint intervals of length, for example, \(Q^{-2}/2\), centered at the selected fractions. For each continuously differentiable \(F\), the fundamental theorem applied to \(|F|^2\) gives at each center
\[
|F(\beta)|^2\leq |I_\beta|^{-1}\int_{I_\beta}|F|^2
+2\int_{I_\beta}|F F'|.
\]
Summing preserves disjointness. If the centers satisfy \(\|\beta\|\leq\rho\), their intervals lie in the enlarged arc of radius \(\rho+Q^{-2}/4\). Because \(\rho\geq1/H\) and \(Q^2\gg H\), this enlargement is at most a constant times \(\rho\). Combining (1)–(2) and Cauchy–Schwarz only in the derivative integral yields
\[
\sum_{\|a/d\|\leq\rho}^{*}|E_f(a/d)|^2
\ll_f X(Q^2+X)\rho\log^4X.
\tag{3}
\]
For a band reaching the whole circle, Parseval for the polynomial and its derivative gives the same bound with \(\rho\asymp1\). This handles wraparound and the final band. The argument neither improves the spacing to \(1/(HQ)\) nor assumes each small interval is a new arithmetic major arc.

### 4. Coefficient bands and their summation

The exact Round 10 completion has coefficients
\[
C_{a/d}=S_v(a/d)M_d,
\quad
M_d=\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}\frac{\mu(q)}q.
\]
The bound \(|M_d|\leq(1+\log(Q/d))/d\) and smooth finite-difference estimate
\(|S_v(\alpha)|\ll_{v,J}H(1+H\|\alpha\|)^{-J}\) do not require Möbius cancellation.

For any denominator \(d\), at most \(2\rho d\) nonzero residues satisfy \(\|a/d\|\leq\rho\); if \(\rho d<1\), there are none. Hence, for the central arc \(j=0\) and the annuli with upper radius \(2^j/H\),
\[
\sum_{\beta\in I_j}|C_\beta|^2
\ll_{v,J}H2^{(1-2J)j}\log^3(2Q).
\tag{4}
\]
This counts every reduced denominator from 2 through \(Q\), including divisors much smaller than the original moduli. There is no inherited cutoff \(d>\sqrt X\). The last clipped annulus obeys the same estimate since its upper radius is only enlarged for this upper bound.

Combining (3)–(4) on each band gives
\[
\left|\sum_{\beta\in I_j}C_\beta E_f(\beta)\right|
\ll_{f,v,J}\sqrt{X(Q^2+X)}\,
2^{(1-J)j}\log^{7/2}X.
\]
The \(H\) factors cancel. The geometric series converges for \(J=2\), independently of the number of bands. Thus no hidden \(\log H\) or discarded high-frequency tail is needed. A \(\log q\) factor in the conductor coefficient contributes one extra logarithm, giving \(\log^{9/2}X\).

### 5. The integer mean and the primitive mean are both present

The decomposition being bounded is exactly
\[
A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)
=E_f(a/d)+B_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0).
\]
The two terms after \(E_f\) must be handled separately.

For smooth compact \(f\), Poisson summation gives
\(|B_f(\alpha)|\ll_{f,A}X(1+X\|\alpha\|)^{-A}\). Since every nonzero fraction has distance at least \(1/Q\) from the integers, and
\(\sum_{a=1}^{d-1}|S_v(a/d)|\ll_v d\), one has
\(\sum_\beta|C_\beta|\ll_v Q\log(2Q)\). The resulting integer-mean error is
\(O_{f,v,A}(XQ\log(2Q)(X/Q)^{-A})\). A fixed sufficiently large \(A\) makes it negligible. The estimate is on the discrete integer mean itself.

For the primitive mean, the same first-power shift bound gives
\[
|A_f(0)|\sum_{d\leq Q}
\frac{|M_d\mu(d)|}{\varphi(d)}
\sum_{(a,d)=1}|S_v(a/d)|
\ll_{f,v}X\log^2(2Q).
\]
This uses Chebyshev and \(\sum_{d\leq Q}1/\varphi(d)\ll\log(2Q)\). It introduces no \(H\) loss and claims no unproved cancellation. The denominator-one term is identically zero in the original completion; it was not discarded during this later decomposition.

### 6. Actual kernel, the two prime-power uses, and scope

The smooth kernel is the exact Round 10 kernel in the variables \(y=m/X\), \(z=h/H\), \(\epsilon=1/T\), and its phase equals
\(\int_0^z(y-\epsilon u)^{-1}du\). The compact support stays away from the denominator singularity. All fixed mixed derivatives, including those after multiplication by \(\log(y-\epsilon z)\), remain uniformly bounded as \(\epsilon\to0\).

In the Fourier separation with fixed outer cutoffs, the constants in (1)–(3) grow polynomially with the m-frequency through the variations of \(f\) and \(u f\). The Poisson bound also costs a fixed number of m-derivatives. Smooth shift bounds cost a fixed number of h-derivatives. Uniform rapid decay of the two-variable Fourier coefficients absorbs all of these costs. The author explicitly includes both m- and h-frequency dependence. The logarithmic identity \(\log((m-h)/q)=\log X-\log q+\log(y-\epsilon z)\) is exact. Rounding the resulting \(\log^{9/2}\) to \(\log^5\) is legitimate.

There are two distinct prime-power steps. The local polynomial replacement proving (1) was checked in Section 2 above. Separately, replacing \(\Lambda\) inside the original progression discrepancy is needed to make every remaining prime a unit modulo every modulus. Its progression error is bounded by the divisor count of \(m-h\); its principal error uses the reciprocal-totient sum. Both are at most the displayed Round 10 error
\[
O_\eta(HX^{1/2+\eta}\log^3X+H\sqrt X\log^4X).
\]
For \(\eta=1/100\) and \(H\leq X^{2/7}\), this is \(o(X\log X)\) and below the new bound. It is not the same operation as the local prime-power replacement, and neither step is omitted.

The accepted statement is restricted to the fixed smooth packet \(V\in C_c^\infty(1,2)\), the actual stated kernel, and the chosen squarefree family. It is conditional on RH. At \(Q=X^{.523}\), it leaves \(X^{.023}\log^4X\) after covariance normalization. No bound for the entire sharp packet, complementary divisor piece, or desired conjecture follows from this audit.

### 7. Evidence and final version

The final author artifact is **CENTERED_SMALL_ARC_BOUND.md**, SHA-256 `9ebf2d8daaac37702302f5a798611e6a6152e352e5b7dd680c319ba76b3f6e29`. The full mathematical draft and primary source were read; the final status paragraph and its link to this review were checked after the author froze the mathematical text. No numerical experiment was necessary, and the author's finite exact-check script was not independently rerun. The acceptance concerns the ordinary analytical proof and its stated scope, not the status of any unreviewed later revision.


<a id="report-41"></a>

# Current report 41: A real-prime subfamily prevents a coefficient-only power saving

**Collection:** R11 — RH small arcs and actual conductor structure.

**Source:** [research/dyson/round11/conductor-arithmetic/CONDUCTOR_MASS_LOWER_BOUND.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/conductor-arithmetic/CONDUCTOR_MASS_LOWER_BOUND.md).

**SHA-256:** `46347799005bb0f53af25c2a7e8ffb2b2217d92688c7651327dde3562f114b92`. **Git blob:** `6b4ccb2eba477c26215aa12697d9fa620aba6c4b`. **Original bytes:** 11083.

## A real-prime subfamily prevents a coefficient-only power saving

Date: 2026-09-05. Status: an ordinary arithmetic construction and quantitative counting proof. No numerical prime realization is required or used. The conclusion concerns a completed coefficient norm; it does not obstruct cancellation in the joint pairing with prime exponential sums.

Fix the full canonical complementary modulus family defined below. For any fixed nonnegative \(V\in C_c^\infty(1,2)\) that is not identically zero, the Round 10 completed coefficients satisfy, uniformly for \(X^{1/6}\le H\le X^{2/7}\),

\[
\boxed{\sum_{\substack{2\le d\le X^{.523}\\
1\le a<d,\ (a,d)=1}}|C_X(a/d)|^2
\gg_V \frac{H}{(\log X)^{348}}.}
\tag{1}
\]

For the coefficients with an additional \(\log q\), the lower bound is
\( \gg_V H/(\log X)^{346}\).

Consequently, neither coefficient norm admits an upper bound \(O(HX^{-\eta})\), for any fixed \(\eta>0\), on this full family. The result uses actual squarefree integers made from primes in explicit intervals, with all complementary predicates verified and their number estimated by the prime number theorem.

This is narrower than a no-go theorem for the research programme. A specially pruned family may remove these moduli. The actual prime exponential sums may also cancel against coefficients whose squared mass is large.

### 1. Fixing the family and the inherited divisor budget

Set

\[
\rho=\frac{523}{1000},\quad
r=\frac{523}{2000},\quad
b=\frac{501}{2000},\quad
\delta=\frac1{1000},\quad
Q=X^\rho,\quad Y=X^\delta.
\tag{2}
\]

Define \(\mathcal Q_X^{\mathrm{full}}\) to contain **every distinct squarefree modulus** \(q=[D,E]\) for which positive squarefree D,E obey

\[
\begin{gathered}
D,E\le X^r,\qquad [D,E]>X^{1/2},\\
p^{3/2}D_{\ge p}\le X^b\quad(p\mid D,\ p>Y),\\
p^{3/2}E_{\ge p}\le X^b\quad(p\mid E,\ p>Y).
\end{gathered}
\tag{3}
\]

Each q is counted once, irrespective of the number of representations. The coefficient on q is exactly \(\mu(q)\); no extra Selberg or cutoff coefficient is inserted.

These are the actual balanced complementary predicates fixed in Round 9, not every possible support geometry in the 186 paper. They use \(f(p)=g(p)=p^{3/2}\), equal budgets \(A_0=B_0=X^b\), and threshold \(Z=X^{1/2}\). The opposite-root guards follow from the owner bounds, and \(A_0B_0=ZY\). Hence Proposition 2.3 of [OpenAI, *Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), printed pp.4–5, proves

\[
\mathcal Q_X^{\mathrm{full}}
\subset\{X^{1/2}<q\le Q:
q\in\mathcal D^{(3)}(Y),\ q\text{ squarefree}\}.
\tag{4}
\]

The elementary divisor property stated on printed p.4 gives, for \(d\mid q\),

\[
d\in\mathcal D^{(3)}(Yq/d)
\subseteq\mathcal D^{(3)}(YQ/d).
\tag{5}
\]

Thus a conductor of size \(d=X^\beta\) retains the quantified parameter \(X^{\delta+\rho-\beta}\) in this sufficient class. This is not inheritance with unchanged Y for an arbitrary divisor. At the conductors constructed below, d=q itself, so the full original budget Y is retained with no loss.

Define the actual regrouped coefficients

\[
A_X(d)=\sum_{\substack{q\in\mathcal Q_X^{\mathrm{full}}\\d\mid q}}
\frac{\mu(q)}q,\qquad
C_X(a/d)=S_{V,H}(a/d)A_X(d),
\]

\[
S_{V,H}(\beta)=\sum_{h\in\mathbb Z}V(h/H)e(-\beta h),
\qquad e(t)=e^{2\pi it}.
\tag{6}
\]

The frequencies a/d in (1) are reduced. These are the coefficients in the exact conductor regrouping of Round 10, equation (11).

### 2. A subfamily made from 348 distinct prime factors

Put

\[
u=\frac9{100},\qquad
\kappa=\frac{343}{346000},\qquad
\lambda=2^{-1/348}.
\tag{7}
\]

Let \(\mathcal P_L(X)\) and \(\mathcal P_S(X)\) be the primes in

\[
(\lambda X^u,X^u],\qquad
(\lambda X^\kappa,X^\kappa],
\tag{8}
\]

respectively. For all sufficiently large real X, these two intervals are disjoint, the large primes exceed Y, and the small primes are below Y. Indeed
\(\kappa<\delta<u\), all strictly.

Let \(\mathcal F_X\) be the set of products of two distinct primes from \(\mathcal P_L(X)\) and 346 distinct primes from \(\mathcal P_S(X)\). The use of sets, rather than ordered prime tuples, prevents permutation overcounting.

Every q in this family is squarefree and has

\[
\mu(q)=(-1)^{348}=1.
\tag{9}
\]

The exact exponent identities are

\[
2u+346\kappa=\rho,\qquad
u+173\kappa=r,\qquad
\lambda^{348}=\frac12.
\tag{10}
\]

It follows that

\[
\frac Q2<q\le Q.
\tag{11}
\]

For large X, \(Q/2>X^{1/2}\). Partition the 346 small primes into two groups of 173 and place one large prime in each group. Their products D,E are disjoint and squarefree, \(q=DE=[D,E]\), and

\[
D,E\le X^{u+173\kappa}=X^r.
\]

Only the single large prime p in each root activates its predicate. Its owner tail is exactly p, so

\[
p^{3/2}D_{\ge p}=p^{5/2}
\le X^{(5/2)u}=X^{9/40}<X^{501/2000}.
\tag{12}
\]

The strict exponent margin is \(51/2000\). The same reasoning applies to E. The opposite-root condition \(p^{3/2}\le X^b\) holds as well. Thus

\[
\boxed{\mathcal F_X\subset\mathcal Q_X^{\mathrm{full}}\cap(Q/2,Q].}
\tag{13}
\]

The construction is not vacuous Y-smooth support: every modulus has two prime factors larger than Y, and both owner predicates are checked at those factors.

### 3. Rigorous counting, including the permutation constants

Write

\[
L_X=\pi(X^u)-\pi(\lambda X^u),\qquad
S_X=\pi(X^\kappa)-\pi(\lambda X^\kappa).
\]

Unique factorization, together with the disjoint prime intervals, gives the exact count

\[
|\mathcal F_X|=\binom{L_X}{2}\binom{S_X}{346}.
\tag{14}
\]

The prime number theorem on each fixed-ratio interval gives, as real X tends to infinity,

\[
L_X\sim\frac{1-\lambda}{u}\frac{X^u}{\log X},
\qquad
S_X\sim\frac{1-\lambda}{\kappa}\frac{X^\kappa}{\log X}.
\]

Since both counts tend to infinity, (14) yields

\[
|\mathcal F_X|
\sim c_0\frac{Q}{(\log X)^{348}},
\quad
c_0=\frac{(1-\lambda)^{348}}
{2!\,346!\,u^2\kappa^{346}}>0.
\tag{15}
\]

This assertion holds for every sufficiently large X, not merely a specially chosen subsequence. The constant is small, but fixed and positive; no estimate of its numerical size is needed for a power-saving obstruction. The factorization into D,E was used only to prove membership. Its many possible partitions are not counted again in (14).

### 4. No other signed modulus can cancel these conductor coefficients

Take \(d\in\mathcal F_X\). Since \(d>Q/2\), the only positive multiple of d at most Q is d itself. Therefore, in the **full signed family**, not just the positive subfamily,

\[
\boxed{A_X(d)=\frac{\mu(d)}d=\frac1d.}
\tag{16}
\]

This conclusion is unaffected by any other admissible moduli, including those with negative Möbius coefficient. It is an isolation statement at the reduced denominator d; no unmerged duplicate rational frequencies are being counted.

It also shows why the inherited dense-divisibility parameter in (5) cannot simply remove large conductors. Here d=q is near the largest allowed modulus and still belongs to the strongest original class \(\mathcal D^{(3)}(Y)\).

### 5. Enough primitive low numerators, and the norm lower bound

Let \(m_V=\int V(t)\,dt>0\). The Riemann-sum estimate, uniformly as H tends to infinity, gives

\[
\sum_hV(h/H)\ge\frac{m_V}2H
\tag{17}
\]

for sufficiently large H. This is uniform over the present range \(H\ge X^{1/6}\).

If \(1\le a\le d/(16H)\), every h in the support of V(h/H) satisfies
\(0\le2\pi ah/d\le\pi/4\). Positivity of V therefore gives

\[
|S_{V,H}(a/d)|
\ge\Re S_{V,H}(a/d)
\ge\frac{m_V}{2\sqrt2}H.
\tag{18}
\]

We must still count only primitive fractions. Put \(A=d/(16H)\). Each prime factor of d exceeds \(\lambda X^\kappa\), and d has exactly 348 such factors. Consequently

\[
\#\{1\le a\le A:(a,d)>1\}
\le\sum_{p\mid d}\left\lfloor\frac Ap\right\rfloor
\le A\frac{348}{\lambda X^\kappa}.
\tag{19}
\]

Uniformly for \(d\in\mathcal F_X\) and \(H\le X^{2/7}\), one has
\(A\ge X^{\rho-2/7}/32\to\infty\). For all sufficiently large X, take \(A\ge4\) and \(348/(\lambda X^\kappa)\le1/4\). Equations (19) and \(\lfloor A\rfloor\ge A-1\) then give at least \(A/2=d/(32H)\) coprime choices of a.

For each such d, (16) and (18) imply

\[
\sum_{\substack{1\le a<d\\(a,d)=1}}|C_X(a/d)|^2
\ge\frac{m_V^2}{256}\frac Hd.
\tag{20}
\]

Summing over \(\mathcal F_X\), using d≤Q and (15), proves the explicit eventual bound

\[
\boxed{
\sum_{d,a}|C_X(a/d)|^2
\ge\frac{c_0m_V^2}{512}
\frac{H}{(\log X)^{348}}.
}
\tag{21}
\]

All sufficiently-large-X conditions above can be imposed simultaneously, independently of H in its stated range.

For
\(A_X^{(1)}(d)=\sum_{q\in\mathcal Q_X^{\mathrm{full}},d\mid q}\mu(q)\log q/q\),
the same conductors have \(A_X^{(1)}(d)=\log d/d\).
Because \(d>X^{1/2}\), their squared contribution is at least
\((\log X)^2/4\) times the restricted contribution in (21). Hence

\[
\sum_{d,a}|S_{V,H}(a/d)A_X^{(1)}(d)|^2
\ge\frac{c_0m_V^2}{2048}
\frac{H}{(\log X)^{346}}
\tag{22}
\]

eventually.

### 6. Exactly what is ruled out

For every fixed \(\eta>0\), \(X^\eta/(\log X)^{348}\to\infty\). Thus (21) contradicts any proposed bound \(O(HX^{-\eta})\) for this coefficient norm on the full canonical family. More generally it rules out an upper bound of that strength asserted uniformly over **all** allowed subfamilies, since \(\mathcal F_X\) itself is an allowed family and has the same isolated conductor coefficients.

The quantifiers matter:

- A different deliberately pruned family can exclude \(\mathcal F_X\); no lower bound is asserted for every selected subset.
- A different coefficient system can suppress these moduli; the proof concerns the specified Möbius coefficients, not arbitrary sieve weights.
- The lower bound holds for fixed nonnegative nonzero V as stated. It is not asserted for every signed shift profile or every Fourier component of the full two-variable kernel.
- It supplies no lower bound for the signed joint pairing with
  \(A_f(a/d)-\mu(d)A_f(0)/\varphi(d)\), and no lower bound for the actual zeta covariance.

The conclusion is therefore specific: retaining a smaller divisor-density budget cannot by itself furnish a power saving in the completed coefficient norm for this canonical source-supported family. To improve the Round 10 bound by a power, this family requires additional cancellation in the joint prime pairing, a different use of the frequencies, or a justified change of the chosen modulus weights/support.

### 7. Provenance and exact arithmetic

The only counting input is the classical prime number theorem, applied to the two fixed-ratio prime intervals in (8). The support input is Proposition 2.3 and the divisor property on p.4 of the pinned 186 paper. The source PDF SHA256 is **456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930**.

The companion exact-arithmetic certificate records the rational exponent identities and positive margins in (7), (10), and (12), plus the uniform lower-numerator exponent. It does not claim an effective numerical threshold at which the prime-counting asymptotic has stabilized. No scan, numerical realization, or rerun of an old asymptotic bound was performed.


<a id="report-42"></a>

# Current report 42: Independent review of the canonical conductor-mass construction

**Collection:** R11 — RH small arcs and actual conductor structure.

**Source:** [research/dyson/round11/conductor-arithmetic/INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/conductor-arithmetic/INDEPENDENT_REVIEW.md).

**SHA-256:** `b146b7427417bc3acca5443e167e3a07257830cfeb80e7f02523a6fd1f3e252d`. **Git blob:** `a543227dac25c0c76b8817c8f2902cc1779e3845`. **Original bytes:** 3863.

## Independent review of the canonical conductor-mass construction

Date: 2026-09-05. Reviewer: root Astra, independently of the authoring lane. Accepted as an ordinary asymptotic arithmetic proof for the explicitly defined full family. This is not a lower bound for the prime pairing, and not a formal proof-assistant certificate.

Reviewed author SHA256: `46347799005bb0f53af25c2a7e8ffb2b2217d92688c7651327dde3562f114b92`.

### Membership and counting

The exact exponents are consistent: two primes of exponent 9/100 and 346 of exponent 343/346000 give total 523/1000; each root has one large prime and 173 small primes, giving 523/2000. The lower interval multiplier raised to 348 is exactly 1/2. Thus every constructed product lies strictly above Q/2 and at most Q, for every sufficiently large real X.

The small-prime exponent is strictly below 1/1000, so those factors do not trigger the complementary predicate. Each root has only one factor above that threshold; its owner tail is the factor itself. The active condition is therefore p^(5/2)<=X^(9/40), strictly inside X^(501/2000). The opposite guard is weaker. Both roots are squarefree and disjoint; their least common multiple is their product. This checks the actual Round 9 support, rather than merely assuming that dense divisibility implies membership in it.

Unique factorization and disjoint intervals give exactly binomial(L_X,2) binomial(S_X,346) different moduli. PNT in fixed-ratio intervals gives the stated constant and log exponent. Counting root partitions as different moduli would be wrong; the author does not do that. No effective or practical threshold is claimed, and the very small fixed counting constant does not affect the power comparison.

### Signed coefficients and primitive fractions

At a constructed d>Q/2 no other positive multiple d k can be at most Q. Thus the full signed regrouped coefficient is exactly mu(d)/d=1/d; negative contributions from other parent moduli cannot cancel it. Each reduced fraction is counted once. This is a conductor-isolation fact, not a claim that all moduli have positive coefficient.

For 1<=a<=d/(16H), every active h is between H and 2H, so the phase has absolute value at most pi/4. Fixed nonnegative V gives the lower real part claimed. The union bound over 348 prime divisors removes at most A*348/(lambda X^kappa) candidate numerators, while the floor costs at most one. Since A>=X^(523/1000-2/7)/32 grows uniformly, at least A/2 primitive numerators remain eventually. This proves the individual constant m_V^2 H/(256 d), then c0 m_V^2 H/(512 log^348 X). The extra log d gives at least (log X)^2/4 after squaring, yielding the second constant 1/2048.

### Scope and relation to the new RH estimate

For fixed eta>0, X^eta/log^348 X diverges. The norm lower bound therefore rules out O(H X^(-eta)) for these exact coefficients on this full family. It also refutes such an assertion made uniformly over all allowed subfamilies, since this one qualifies. It says nothing about every deliberately pruned family or altered sieve weight.

In particular it does not obstruct the separate Round 11 RH small-arc improvement, which changes the prime-frequency estimate and its localization. Nor does it give a lower bound for the signed pairing of these coefficients with actual centered prime exponential sums. A claim that the remaining X^.023 loss is unavoidable for primes would exceed the proof.

The inherited dense-divisibility parameter for a general divisor is Yq/d, not always Y. For the conductors used here d=q, so no loss of parameter occurs. The author records this distinction explicitly.

The exact-arithmetic companion verifies rational exponents and constants only. PNT, the fixed smooth Riemann sum, and the written counting argument supply the asymptotic assertions. No prime search or numerical realization was needed.


<a id="report-43"></a>

# Current report 43: The log-weighted prime-tail moment: a primary-source check and its arithmetic remainder

**Collection:** R11 — RH small arcs and actual conductor structure.

**Source:** [research/dyson/round11/log-weighted-tail/ARITHMETIC_DIAGONAL_AND_SOURCE_GAP.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/log-weighted-tail/ARITHMETIC_DIAGONAL_AND_SOURCE_GAP.md).

**SHA-256:** `85c9435bbd656bcf37f21f55fe2d54cb40638c7a56908abe57e54f551a627daa`. **Git blob:** `60dcf395d101e223087db8ac4f355640de016fff`. **Original bytes:** 8660.

## The log-weighted prime-tail moment: a primary-source check and its arithmetic remainder

Date: 2026-09-05. This bounded attempt proves no new lower bound at the required scale. It identifies a relevant derivative theorem, checks a legitimate centered finite-prime expansion, and isolates the missing arithmetic coefficient. The positive prime diagonal is explicit; the required lower bound on the jointly centered remainder is not established.

### 1. A derivative theorem does not supply the missing mixed moment

The directly relevant primary source is Andrés Chirre, [A note on the mean values of the derivatives of ζ′/ζ, arXiv:2107.13636v2](https://arxiv.org/html/2107.13636v2), 3 January 2022. Proposition 5, equation (2.3), expresses the normalized squared norm of the kth logarithmic derivative as a known integral on \([0,1]\) plus
\[
\int_1^\infty \alpha^{2k}e^{-2a\alpha}F(\alpha,T)\,d\alpha+o(1)
\]
for fixed \(a>0\). Theorem 1 makes its sharp fixed-width asymptotic equivalent to pair correlation. Thus this theorem does not provide a sharper RH-only arithmetic value for the signed mixed moment considered here. Its fixed-width remainder cannot be differentiated or made uniform along a growing width without further proof. The source HTML and its hash are retained in `sources/receipt.json`.

This is a narrow source conclusion, not an assertion that every theorem on derivatives or short intervals has been exhausted. The stronger centered-small-arc input being investigated separately is outside this note.

### 2. A finite, centered arithmetic expansion with its cutoff error

Assume RH. Let \(L=\log T\), \(N=\lfloor T/L^6\rfloor\),
\(s=1/2+\delta+it\), and \(\delta=b/(2L)>0\). Let \(R_b\) be the genuine-prime residual already defined in Round 10, including its pole and endpoint. Define
\[
K_b=-R_b-L^{-1}\partial_sR_b,
\qquad
M_T(b)=\frac{e^b}{TL^2}\Re\int_0^T R_b\overline{K_b}\,dt.
\]
The derivative acts on the actual analytic continuation, not on a bare prime series in the critical strip.

For finite \(Y>N\), put
\[
C_Y(s)=\sum_{N<p\leq Y}(\log p)p^{-s}-\int_N^Y x^{-s}\,dx,
\quad
D_Y=-C_Y-L^{-1}\partial_s C_Y.
\tag{1}
\]
These are finite expressions. Write \(E_1(x)=\theta(x)-x\), with endpoints including primes equal to their argument, and
\(P_N(s)=N^{1-s}/(s-1)\). Stieltjes summation gives exactly
\[
C_Y=E_1(Y)Y^{-s}-E_1(N)N^{-s}
  +s\int_N^Y E_1(x)x^{-s-1}\,dx.
\]
Consequently \(C_Y\to C:=R_b-P_N\), uniformly on \(0\leq t\leq T\) for each fixed \(T,b\). For \(Y\geq4\), the RH estimate on \(E_1\) gives the explicit error
\[
|C-C_Y|\ll Y^{-\delta}\left[
\log^2Y+|s|\left(
\frac{\log^2Y}{\delta}+\frac{2\log Y}{\delta^2}
+\frac2{\delta^3}\right)\right].
\tag{2}
\]
Differentiation adds one logarithm and one possible inverse power of \(\delta\). In particular, for \(T\geq e\) and \(0<\delta\leq1/4\), a convenient coarse common bound is
\[
|C-C_Y|+|(-C-L^{-1}C_s')-D_Y|
\ll (1+T)\delta^{-4}(1+\log Y)^3Y^{-\delta}.
\tag{3}
\]
This justifies the mixed-moment limit at fixed \(T,b\); it also states its real cost. For example, on \(2\leq b\leq2G(T)\), \(G=o(\log L)\), the choice \(Y=\exp(L^3)\) makes (3) at most \(O(TL^{13}e^{-L^2})\). This is a legitimate uniform analytic cutoff, not a computationally efficient prime experiment. No finite prime computation is offered as evidence for the limiting remainder.

### 3. Pole terms are negligible at this scale, with a direct norm estimate

Here and below \(2\leq b\leq2G(T)\) with \(G=o(\log L)\). For all sufficiently large \(T\), \(\delta\in[1/L,1/4]\). The RH local-zero partial fractions yield uniformly
\[
\|R_b\|_{L^2(0,T)}+\|K_b\|_{L^2(0,T)}\ll\sqrt T L^2.
\tag{4}
\]
For the derivative in (4), the nearby-zero bound is \(O(L/\delta^2)=O(L^3)\), before division by \(L\); the remote sum is smaller. The absolutely convergent prime-power correction and its derivative are respectively \(O(\delta^{-2})\) and \(O(\delta^{-3})\). Their contributions to \(K_b\) are therefore \(O(L^2)\). The finite prime polynomial and its log-weighted companion obey the same uniform mean-value majorant used in Round 8, since \(\log p/L\leq1\) for \(p\leq N\). This establishes (4) without differentiating an unknown asymptotic error.

Since \(\sigma\leq3/4\),
\[
\|P_N\|_2\ll\sqrt N,
\qquad
-P_N-L^{-1}P_N'
=\left(\frac{\log N}{L}-1+\frac1{L(s-1)}\right)P_N.
\]
Its companion has norm \(O((\log L)/L)\sqrt N\). Expanding the two mixed products and applying Cauchy–Schwarz gives
\[
M_T(b)=\frac{e^b}{TL^2}\Re\int_0^T
C\,\overline{(-C-L^{-1}C_s')}\,dt
+O(e^bL^{-3}).
\tag{5}
\]
The error in (5) is \(o(b^{-3})\) uniformly on the stated slow range. Thus the pole is accounted for and then removed at a proved error; the endpoint \(E_1(N)N^{-s}\) remains part of \(C\).

### 4. The arithmetic diagonal and the exact missing coefficient

Let \(u(x)=\log x/L-1\) and
\[
d\mu_Y(x)=\sum_{N<p\leq Y}(\log p)\delta_p(dx)-\mathbf1_{(N,Y]}(x)\,dx.
\]
Set
\[
G_{T,b}(x,y)=(xy)^{-1/2-b/(2L)}
\frac{u(x)+u(y)}2\,
\operatorname{sinc}_0\!\left(T\log(x/y)\right).
\]
Finite expansion of (1), with the real part symmetrized in \(x,y\), gives
\[
\frac{e^b}{TL^2}\Re\int_0^T C_Y\overline{D_Y}\,dt
=\frac{e^b}{L^2}\iint G_{T,b}(x,y)\,d\mu_Y(x)d\mu_Y(y).
\tag{6}
\]
The prime-prime diagonal of (6) is
\[
\mathcal D_T(b;Y)=\frac{e^b}{L^2}
\sum_{N<p\leq Y}(\log p)^2p^{-1-b/L}
\left(\frac{\log p}{L}-1\right).
\]
Its limit \(\mathcal D_T(b)\) converges absolutely. Applying the RH estimate for \(\theta(x)-x\) by partial summation gives, uniformly in the slow range,
\[
\mathcal D_T(b)=e^b\int_{\log N/L}^{\infty}
v(v-1)e^{-bv}\,dv
+O(e^bN^{-1/2}L).
\tag{7}
\]
The elementary tail integral from \(v=1\) is
\[
e^b\int_1^\infty v(v-1)e^{-bv}\,dv
=\frac1{b^2}+\frac2{b^3}.
\]
The interval \(\log N/L<v<1\) contributes a nonpositive term of size
\(O((\log L/L)^2)\), since \(1-\log N/L=6\log L/L+o(1/L)\). Both errors in (7), multiplied by \(b^3\), tend to zero uniformly. Therefore
\[
\boxed{\mathcal D_T(b)=\frac1{b^2}+\frac2{b^3}+o(b^{-3}).}
\tag{8}
\]

Define \(\mathcal B_T(b;Y)\) by subtracting this finite prime-prime diagonal from the double integral in (6), and put
\(\mathcal B_T(b)=\lim_{Y\to\infty}\mathcal B_T(b;Y)\).
The limit exists by (2)–(3) and absolute convergence of the diagonal. It contains together the off-diagonal prime-prime sum, both prime-continuum terms, and the continuum-continuum term. Those components must not be assigned independent infinite limits: only their centered combination has been justified.

Equations (5)–(8) prove the arithmetic decomposition
\[
\boxed{M_T(b)=\frac1{b^2}+\frac2{b^3}
+\mathcal B_T(b)+o(b^{-3})}
\tag{9}
\]
uniformly on the slow range. Thus, for example, the additional lower bound
\[
\mathcal B_T(s)\geq-\frac{4-\varepsilon}{s^3}
-\frac{\eta_T}{s^3},\qquad \eta_T\to0,
\tag{10}
\]
uniformly up to \(2G(T)\), would give the Round 10 criterion
\(M_T(s)\geq s^{-2}-(2-\varepsilon)s^{-3}-o(s^{-3})\).
An averaged sufficient version is
\[
\int_b^{2b}\mathcal B_T(s)\,ds
\geq-\frac{3}{2b^2}+\frac{\varepsilon}{b^2}+o(b^{-2}).
\tag{11}
\]
Indeed the integrated diagonal equals \(1/(2b)+3/(4b^2)+o(b^{-2})\), so (11) yields the required value strictly above \(-3/4\) after the coupled normalization. Equations (10) and (11) are unproved arithmetic inputs, not consequences of positivity of the prime coefficients.

### 5. What the accessible short-prime projection actually sees

A projection confined to prime lengths below \(T\) sees only \(u(p)\leq0\). In the residual's available slice \(N<p\leq T\), its diagonal log-weighted contribution is \(O((\log L/L)^2)\) and nonpositive. It cannot supply the positive leading term \(1/b^2\) in (8).

That term comes from logarithmic excess of size \(1/b\), hence prime lengths \(X=T^{1+O(1/b)}\). The elementary contour/mixed-polynomial estimate used for the short projection has error \(O(X\log^3T)\) at such a cutoff, before normalization; even disregarding any further logarithmic costs, its normalized error is \(O(e^b(X/T)L)\). On a fixed edge shell \(X=T^{1+s/b}\), \(1\leq s\leq2\), this majorant contains \(\exp(sL/b)\), far larger than \(b^{-3}\). This states the failure of that particular bound, not the magnitude of the actual error or an impossibility theorem.

The inspected higher-derivative theorem leaves an unknown pair-correlation integral, and the elementary short-prime projection misses the required positive-excess sector at the necessary precision. The explicit remaining obligation is the centered arithmetic remainder (10) or its averaged version (11). No generic point-process counterexample, parameter scan, or numerical approximation to a divergent prime series was used.


<a id="report-44"></a>

# Current report 44: Independent review of the centered mixed-moment remainder

**Collection:** R11 — RH small arcs and actual conductor structure.

**Source:** [research/dyson/round11/log-weighted-tail/INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round11/log-weighted-tail/INDEPENDENT_REVIEW.md).

**SHA-256:** `97a8e45507e0df1cf21e6045ba6d689990401a4eff5f2ba79a00739ab69e08f6`. **Git blob:** `031535f861ac31d697fd45128e263acf313b16fd`. **Original bytes:** 4187.

## Independent review of the centered mixed-moment remainder

Date: 2026-09-05. Reviewer: root Astra, independently of the authoring lane. The centered arithmetic identity and its error bounds are accepted under RH. Neither sufficient lower bound for the remainder is proved.

Reviewed author SHA256: `85c9435bbd656bcf37f21f55fe2d54cb40638c7a56908abe57e54f551a627daa`.

### Source and continuation

I checked Proposition 5, equation (2.3), in the retained primary HTML of Chirre, arXiv:2107.13636v2. The statement is for fixed integer k>=1 and fixed positive a in the displayed asymptotic. It includes the unknown integral of alpha^(2k) exp(-2a alpha) F(alpha,T) beyond alpha=1. The note correctly declines to differentiate its unspecified remainder or use it as a uniform growing-width estimate. Theorem 1's equivalence with pair correlation does not furnish the required one-sided estimate under RH alone.

Stieltjes summation with theta(x)-x and primes N<p<=Y gives both endpoint terms with the written signs. Its tail equals minus E_1(Y)Y^(-s) plus s times the remaining integral. RH bounds it by Y^(-delta) times the displayed polynomial in log Y and inverse delta. Differentiation in s adds one logarithm, with the next inverse-delta power. This is a legitimate fixed-T limit, unlike termwise use of an uncentered prime series in the critical strip.

For b>=2, delta>=1/log T. With Y=exp((log T)^3), the coarse uniform error is bounded by T(log T)^13 exp(-(log T)^2), up to a fixed constant. This validates a mathematical cutoff but supplies no feasible brute-force experiment.

### Norms and the pole

The local-zero derivative has majorant O(log T/delta^2) before division by log T. The prime-power correction and its derivative have the stated inverse-delta bounds; the finite polynomial uses weights bounded by the original ones. These give the sufficient coarse L2 bound sqrt(T)(log T)^2 for both factors, uniformly on the slow range.

The pole is N^(1-s)/(s-1). Since sigma<=3/4 its L2 norm is O(sqrt N), including the low-height part. Direct differentiation gives the coefficient log N/log T-1+1/((log T)(s-1)), so its companion is O((log log T)/(log T))sqrt N. Cauchy--Schwarz after normalization gives O(exp(b)(log T)^(-3)). It is o(b^(-3)) when b<=2G(T), G=o(log log T). The endpoint involving E_1(N) is retained throughout.

### Diagonal and the combined remainder

Expanding the two finite centered measures, integrating time, taking real parts, and exchanging x,y gives the symmetric factor (u(x)+u(y))/2 times sinc_0(T log(x/y)). On the prime diagonal this reduces to u(p), with exactly two factors log p. The continuous measure has no atomic diagonal mass.

For partial summation write f(x)=(log x)(log x/log T-1)x^(-1-b/log T). The RH error theta(x)-x is O(sqrt(x)log^2 x). Its endpoint plus the integral against f' is O(N^(-1/2)(log T)^3), uniformly for the stated b; multiplying by exp(b)/(log T)^2 gives the author's conservative O(exp(b)N^(-1/2)log T). No unproved short-interval estimate is used here.

The main integral from v=1 is exactly b^(-2)+2b^(-3). The omitted strip log N/log T<v<1 has width O(log log T/log T), negative integrand of size proportional to that width, and hence a squared-width error. Multiplication by b^3 makes both errors vanish uniformly. Thus the positive diagonal is correct, and the short-prime slice below T cannot provide its leading term.

The limit of the full centered expression exists; its diagonal converges absolutely. Subtracting the latter defines the combined remainder. No separate limits of the prime-continuum pieces are asserted. This distinction is essential and is preserved in the report.

Integrating the diagonal over [b,2b] gives 1/(2b)+3/(4b^2). The proposed integrated remainder threshold then leaves a coefficient strictly above -3/4 after normalization. This checks the constants, but supplies no proof of that threshold. The reported long-polynomial error is a failed upper majorant, not a lower bound on the actual error.

The result identifies a specific arithmetic obligation and rules out an unjustified use of a fixed-width derivative theorem. It does not establish a new zeta pair-correlation bound.


<a id="report-45"></a>

# Current report 45: Round 12: three exact tests of the remaining arithmetic gap

**Collection:** R12 — exact limits of sampling and dispersion transfers.

**Source:** [research/reports/dyson_round12.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/dyson_round12.md).

**SHA-256:** `5e697b2ba41e12869bb471a1294d110b1dbf8d2592e9652f467c776d6272a89a`. **Git blob:** `84cf3fbc0f42b330021ccf98d8e744010272557b`. **Original bytes:** 8922.

## Round 12: three exact tests of the remaining arithmetic gap

Date: 2026-09-05. **No stronger actual-prime estimate was obtained in this round.** The current bound remains the RH component estimate X^1.023 log^5 X from Round 11. Three bounded attempts now explain precisely why improving positive sampling, importing the 186 dispersion theorem by phase absorption, or applying known prime-interval upper norms does not yet close its gap. Each conclusion is narrower than an impossibility theorem for the actual signed prime pairing.

### Positive sampling really is crowded on the permitted support

The [sampling proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/sampling-geometry/ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md) uses the actual canonical complementary-modulus family, not the full Farey set as a substitute. Round 11 constructed at least c Q/log^348 X terminal conductors in (Q/2,Q], each with merged coefficient 1/d. They supply at least c Q^2/(H log^348 X) distinct reduced frequencies in [0,1/(16H)], with coefficient magnitude at least c_V H/Q.

Partition this arc into O(X/H) cells of length 1/(100X). One cell must contain at least c Q^2/(X log^348 X) actual frequencies. A phase-tuned Dirichlet packet with integer frequencies in [X,1.1X] concentrates there. Parseval and its value on that cell prove that the positive local sampling constant is at least

\[
c\,Q^2/(\log X)^{348}.
\]

The packet also satisfies the same known small-arc energy and derivative envelopes, even without their logarithmic factors. Including the actual squared coefficient weights gives the corresponding lower bound c_V H^2/log^348 X. Thus these hypotheses cannot justify a fixed-power improvement of that positive sampling step.

The packet is an artificial integer polynomial, not the centered genuine-prime polynomial for fixed smooth f. It is not asserted to align with the full complex coefficient vector. The actual signed functional has the exact dual kernel

\[
K(n)=\sum_{q\in\mathcal Q}\mu(q)
\left[\sum_{h\equiv n\ (q)}v(h/H)
-\frac1{\varphi(q)}\sum_{(h,q)=1}v(h/H)\right].
\]

Its Gram matrix contains signed off-diagonal contributions. A smaller norm for that functional, or cancellation with actual prime coefficients, is not ruled out by the positive sampling result. The proof specifically does not claim that X^.023 is unavoidable for primes. The inherited counting and packet constants have a [separate narrow review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/sampling-geometry/COUNTING_REVIEW.md); root checked the complete argument and exact signed identity.

### Direct phase absorption violates the dispersion coefficient hypothesis

The [dispersion audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/dispersion-transfer/DISPERSION_HYPOTHESIS_OBSTRUCTION.md) checks the 186 paper's actual hypotheses at legal parameters. With omega=.012, delta=.001 and sigma=.101, the three bilinear inequalities have left sides .888, .996 and .990. The scales N=X^.4 and M=X^.6 are permitted, as are the canonical terminal conductors d near Q=X^.523.

The prime-interval sequence beta(n)=1_(n prime, N<=n<2N) has the source's Siegel--Walfisz property. But its additive twist need not. For d coprime to 3, take k=(d-1)/3 or (d+1)/3 according to d mod 3, and choose a unit m in [M,2M] with m=k mod d. This is possible since M/d tends to infinity. The actual completed numerator a=1 has nonzero shift weight. On the prime interval,

\[
e(mn/d)=e(n/3)(1+O(N/d)).
\]

PNT in the two fixed reduced classes modulo 3 therefore gives

\[
\Delta(\beta(n)e(mn/d);1\bmod3)
=\left(\frac{i\sqrt3}{4}+o(1)\right)\frac N{\log N}.
\]

The source SW requirement with logarithmic exponent two cannot accommodate this discrepancy. Both branches for k give the same leading sign. The error O(N^2/(d log N)) is uniformly lower order. Hence one cannot absorb the completed phase into the short coefficient and inherit its original SW property, even with a permitted conductor, scale and primitive numerator. The source theorem remains valid; the proposed transformed coefficient fails its premise.

This does not say that every slice or every factor in a prime identity fails, or that bad slices cannot be handled after averaging. An averaged argument keeping m, a, d and h may still succeed. The modulus-dependent coefficient also cannot be silently substituted for a fixed family before the source's modulus sum.

Two further checks close related direct substitutions. First, even after gcd(h,d)=1 is imposed, a positive subinterval of the shifts maps onto every unit class modulo every prime factor of the constructed d. Its product of local images has phi(d) classes, asymptotic to d, while tau(d)=2^348 is fixed. The source's bounded-local-class lift cannot absorb that cost. The original coherent interval has only O(H) global classes; a method preserving this cross-prime correlation is not excluded. Second, using H itself as the short convolution length fails the source range: that factor must exceed X^.398, whereas H<=X^(2/7).

### Centered prime-interval upper bounds miss the sign and precision

The [Selberg audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/mixed-arithmetic/SELBERG_MIXED_REMAINDER_AUDIT.md) reads [Saffari--Vaughan, Lemma 5](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf), including printed page 20. Under RH its local estimate concerns genuine theta and is uniform for 0<eta<=1:

\[
\int_X^{2X}|\theta(x+\eta x)-\theta(x)-\eta x|^2dx
\ll \eta X^2\log^2(2/\eta).
\]

Applying Mellin Gallagher to the finite centered prime measure, retaining both cutoff crossings and the logarithmic weight, gives the valid but insufficient bound |M_T(b)|<=C log(T)/b^2. The associated integrated lower bound on the combined remainder is only of order -log(T)/b. It is much too weak for the required b^-2 correction. The prime and continuum pieces are never separated into unjustified infinite sums.

This is deliberately not claimed as the strongest RH consequence. Round 10 already had stronger individual norm control, and the same source page records Selberg's stronger global weighted estimate with a fixed exponent range. For a smooth filter on the active excess shell, the latter gives normalized squared norms O(1) and O(b^-2), hence only O(b^-1) control of the mixed product by Cauchy--Schwarz. It gives neither a positive increment in the shrinking shell nor the necessary signed next-order coefficient. A stronger use of the theorem is not ruled out.

Smoothing b leaves the actual sinc factor and joint centering in the kernel. A negative sinc lobe prevents a term-by-term nonnegativity argument. A negative kernel value alone would not disprove positive semidefiniteness, and the report explicitly avoids that inference. No generic point-process countermodel replaces actual prime arithmetic in this calculation.

### Review, replay and the next useful attempt

The [complete independent root review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/INDEPENDENT_ROOT_REVIEW.md) pins all three author hashes, checks the primary source statements, and records the exact accepted scope. All 18 originals (1,904,996 bytes) are preserved locally under `Astra-Local-Archive/round12-originals/`; 15 research files are public verbatim. The third-party PDF, extracted text and rendered page stay local with receipts.

The [intake manifest](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/INTAKE_MANIFEST.json) and [bounded replay](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/logs/round12-integration/recheck.json) verify the source bytes and two exact scripts. The sampling output matches in full. The dispersion certificate matches after removing only four temporary provenance paths; all reference hashes remain checked. The scripts verify rational constants, 60 cyclotomic signed-kernel identities and six fixed modular-selection examples. They do not numerically test PNT, the huge conductor construction, or a conjecture.

```text
python3 research/logs/round12-integration/recheck.py --prime-gap-source-dir /path/to/pinned/186/source-directory
python3 tools/verify_manifest.py
```

The next work retains the structures that these failed transfers discarded: the signed residue kernel, the coherent shift interval, and the additive phase through the m average. In particular the modulus-3 example suggests isolating rationally resonant m values before estimating the remaining phases, rather than assuming a uniform property that is false. A separate attempt is to estimate the exact signed dual norm through common-divisor compatibility and its genuine CRT boundary error. These are ongoing investigations, not new claims in this checkpoint.

The long PDFs retain their earlier checkpoints. The manual single-session Fable packet receives only the coordinator's superseding source-status prefix; it does not dispatch a new session or ask for covered computations again. No large scan, new model service, infrastructure layer or conjecture solution was introduced. Reverting this slice removes the new records without altering earlier proofs. Formalization and the required actual-zeta lower bound remain outstanding.


<a id="report-46"></a>

# Current report 46: The actual support saturates positive sampling at the power scale

**Collection:** R12 — exact limits of sampling and dispersion transfers.

**Source:** [research/dyson/round12/sampling-geometry/ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/sampling-geometry/ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md).

**SHA-256:** `cb52d72f6068c3030968209d8aa028439ea4dc309aa5584d216a1d7d30a1a59d`. **Git blob:** `9336b996cf951f72f54edfa3e6a56fc7ffef8424`. **Original bytes:** 11979.

## The actual support saturates positive sampling at the power scale

Date: 2026-09-05. Status: ordinary geometric proof; the inherited support count and packet constants have been independently checked. The complete proof is awaiting the coordinator's final review. No improved actual-prime bound is proved in this task.

The Q^2 term in the Round 11 **positive local sampling inequality** cannot be reduced by a power of X uniformly on the full canonical complementary-modulus support. This remains true for trigonometric polynomials supported on the actual integer-frequency interval n near X, and after including the absolute squares of the actual coefficients S_v(a/d)M_d. An explicit packet obeying the same small-arc norm and derivative bounds makes this precise.

This is **not an obstruction for the genuine-prime polynomial or for the full signed pairing**. The sampling extremizer constructed here is an artificial band polynomial, not a prime sum. The exact signed Gram formula in Section 5 retains a possible route for improvement; it cannot be rejected using the positive sampling lower bound. Accordingly the result closes one proposed geometric shortcut, not every possible use of frequency geometry.

### 1. Actual arithmetic support already established in Round 11

Write

    Q=X^(523/1000), X^(1/6)<=H<=X^(2/7).

Fix the full canonical squarefree modulus family Q_X^full defined by the balanced complementary predicates of Round 9. Fix a nonnegative nonzero v in C_c^infinity(1,2), and let m_v=integral v>0. The actual completed coefficients are

    M_d=sum_(q in Q_X^full,d|q) mu(q)/q,
    C_(a/d)=S_v(a/d) M_d,
    S_v(beta)=sum_h v(h/H)e(-beta h), e(t)=exp(2 pi i t).

The frozen Round 11 conductor construction proves the following facts, including their quantifiers. There is a subfamily F_X of admissible moduli with

    F_X subset (Q/2,Q],
    |F_X| >= c0 Q/[2(log X)^348]                            (1)

for all sufficiently large real X. Here c0 is the explicit fixed positive constant in that report. Every d in F_X has 348 distinct prime factors, mu(d)=1, and

    M_d=1/d                                                    (2)

in the **full signed family**, because no larger multiple of d fits below Q. The construction checks the actual root bounds and both large-prime predicates; it is not an unconstrained Farey model.

For each such d there are at least d/(32H) integers

    1<=a<=d/(16H), gcd(a,d)=1,

and on all those actual reduced frequencies

    |S_v(a/d)| >= m_v H/(2 sqrt(2)),
    |C_(a/d)| >= m_v H/(2 sqrt(2) Q).                       (3)

These statements hold simultaneously and uniformly in the stated H range once X is sufficiently large. Their proof uses only the ordinary prime number theorem on fixed-ratio intervals and the verified complementary predicates. No estimate about short-interval primes or actual prime exponential sums is added here.

Let Omega_X be exactly the reduced fractions just described. Distinct pairs (a,d) give distinct frequencies, by coprimality. Equations (1)–(3) yield

    Omega_X subset (0,1/(16H)],
    |Omega_X| >= c0 Q^2/[128 H(log X)^348].                 (4)

Thus this very small arc contains many actual frequencies with actual coefficient size of order H/Q, up to fixed constants.

### 2. A microscopic cluster follows without a local distribution theorem

Partition [0,1/(16H)] into intervals of length at most 1/(100X), using at most

    ceil(100X/(16H)) <= 8X/H

intervals, for all sufficiently large X. By the pigeonhole principle some interval J_X contains K_X actual reduced frequencies, with

    K_X >= c0 Q^2/[1024 X(log X)^348].                      (5)

No equidistribution of the moduli or numerators inside subintervals is assumed. The one dense cell is forced by the already proved total count. Its occupation tends to infinity, since

    Q^2/X = X^(23/500)

dominates every fixed power of log X. This lower bound is uniform in H; H cancels in the average occupation.

Let beta_X be the midpoint of J_X. Every selected frequency in this cluster has distance at most 1/(200X) from beta_X. It still has a genuine reduced denominator in F_X near Q. We have not assigned new artificial locations to any frequency.

### 3. Explicit band polynomial and a lower bound for the sampling constant

Set N=ceil(X), M=floor(X/10), and define

    P_X(beta)=H^(-1/2) sum_(n=N)^(N+M-1)
                               e(n(beta-beta_X)).          (6)

For X sufficiently large, M>=X/20, and all its integer Fourier frequencies lie in [X,11X/10]. Its coefficient magnitudes are exactly H^(-1/2), in particular at most one. The carrier is in the same positive-frequency range as the prime polynomial; this is not a test function allowed an arbitrarily high bandwidth.

For beta in J_X factor out the unit-modulus carrier e(N(beta-beta_X)). Each remaining phase has magnitude at most pi/1000. Hence the real part of their sum is at least M/2, and

    |P_X(beta)| >= M/(2 sqrt(H)) >= X/(40 sqrt(H)).         (7)

Parseval gives the exact norm

    integral_0^1 |P_X(beta)|^2 d beta=M/H.                  (8)

Combining (5), (7) and (8),

    sum_(beta in Omega_X) |P_X(beta)|^2
       / integral_0^1 |P_X(beta)|^2 d beta
          >= K_X M/4
          >= c0 Q^2/[81920(log X)^348].                    (9)

Replacing the denominator integral by its restriction to ||beta||<=1/H only makes the ratio larger. The numerator could also be restricted to J_X. Therefore any positive local sampling estimate valid for every polynomial in this positive-frequency band must have sampling constant at least Q^2 times a fixed negative logarithmic power on the actual canonical support.

In particular no uniform bound of the form

    sum_(actual frequencies in the central arc) |P(beta)|^2
          <= O(Q^2 X^(-eta)) integral_(local arc) |P(beta)|^2

is possible for any fixed eta>0 in this class. Nor can the Q^2 term be replaced by X times any fixed logarithmic power: the ratio Q^2/X is the positive power X^.046. Allowing a smooth nonnegative arc cutoff which equals one on [0,1/(16H)] does not change this lower bound.

An analogous lower bound holds with the actual squared coefficient weights retained. By (3) and (9),

    sum_(all actual beta) |C_beta|^2 |P_X(beta)|^2
        / integral_0^1 |P_X(beta)|^2 d beta
          >= c0 m_v^2 H^2/[655360(log X)^348].              (10)

All omitted terms here are nonnegative. Thus cancellation between different signed moduli cannot remove this weighted quadratic lower bound: on the selected conductors their merged coefficient is exactly 1/d, and elsewhere the quadratic sum only increases. In the natural top-conductor normalization (Q/H)^2 |C_beta|^2, equation (10) again gives a sampling constant at least a fixed multiple of Q^2/(log X)^348. It concerns that positive weighted sampling operator; it does not assert that every possible reweighting or Cauchy-Schwarz arrangement is sharp, and it does not concern the signed linear pairing.

### 4. The packet even obeys the known small-arc envelopes

For every rho>=1/H, nonnegativity and (8) show

    integral_(||beta||<=rho) |P_X(beta)|^2 d beta
                    <= M/H << X rho.

Differentiating (6) coefficient by coefficient and applying Parseval gives

    integral_0^1 |P_X'(beta)|^2 d beta
        =4 pi^2 H^(-1) sum_(n=N)^(N+M-1) n^2
                    << X^3/H.

Therefore, simultaneously for every such rho,

    integral_(||beta||<=rho) |P_X'(beta)|^2 d beta
                    << X^3 rho.                            (11)

These are stronger than the log^4 versions supplied by the RH centered-prime input in Round 11. On the other hand (5) and (7) give

    sum_(beta in Omega_X) |P_X(beta)|^2
                    >> X Q^2/[H(log X)^348].               (12)

Consequently the already known norm and derivative envelopes, the positive integer-frequency band, and the actual dense-divisibility support together do not force a power improvement of the sampled energy. The location of the packet depends on the actual frequency cluster, as a worst-case operator test may.

The crucial limitation is equally explicit: P_X is **not** the centered genuine-prime polynomial E_f for a fixed smooth f. Its coefficients are phase-tuned across all integers. Equations (9)–(12) say nothing about whether E_f concentrates at this cell. A new bound excluding such concentration specifically for the prime coefficients, or a bound for the signed coefficient pairing, remains possible.

### 5. What signed weights could still accomplish

The positive sampling step bounds a sum of absolute squares. The actual completed expression is instead

    L(F)=sum_beta C_beta [F(beta)-r_beta F(0)],
    r_(a/d)=mu(d)/phi(d).                                  (13)

For F(beta)=sum_(n in I) b_n e(n beta), its exact dual coefficient sequence is

    K(n)=sum_beta C_beta [e(n beta)-r_beta],
    L(F)=sum_(n in I) b_n K(n).                             (14)

Thus the squared norm of this signed functional on the coefficient space is exactly

    sum_(n in I) |K(n)|^2
     =sum_(beta,gamma) C_beta conjugate(C_gamma)
          sum_(n in I) [e(n beta)-r_beta]
                        [e(-n gamma)-r_gamma].             (15)

The off-diagonal terms in (15) have signs and phases. Nothing in the lower bound for the diagonal positive sampling operator implies a lower bound for (15), or for its value on the actual prime coefficients. In particular, the packet in (6) is not asserted to align with the full coefficient vector C_beta.

Using the exact completion from Round 10, K has the arithmetic form

    K(n)=sum_(q in Q_X^full) mu(q)
       [sum_(h=n mod q) v(h/H)
          -phi(q)^(-1) sum_((h,q)=1) v(h/H)].               (16)

This finite identity holds coefficient by coefficient. When n is a genuine prime near X it is a unit modulo every q, so (16) is exactly the corresponding residue-discrepancy kernel. For arbitrary n, (16) is the Fourier-defined kernel in (14); it need not be identified with the original progression discrepancy with its additional nonunit restrictions.

For the actual prime pairing the coefficients are b_p=(log p)f(p/X) on primes and zero elsewhere. The primitive subtraction in (13)–(16) is retained. An improved estimate exploiting the full signed Gram (15), or cancellation between the prime coefficients and (16), could therefore improve Round 11. Such an estimate would analyze actual correlations of the permitted moduli, their varying residues and/or primes. It is not supplied by a larger minimum spacing, fewer frequencies in the central arc, or a smaller positive sampling norm.

### 6. Bounded decision and quantifier limits

No sharper upper bound for the actual prime pairing was obtained in this task. What is now ruled out is precise: a **uniform positive sampling or absolute-weight sampling improvement by a power**, based only on the Round 11 arc envelopes and canonical factorization support. The Q^2 sampling term is sharp up to logarithmic powers in that class, including on the correct integer-frequency band.

This does not rule out a deliberately pruned modulus family, a specially chosen signed shift profile, a direct signed-Gram argument, an improved prime-specific concentration theorem, or cancellation in the full genuine-prime pairing. In particular, it is not a proof that the remaining X^.023 in the actual arithmetic bound is unavoidable. Treating a worst-case artificial polynomial as the prime polynomial would be a logical error.

The small companion script checks exact exponent differences, the constants derived from the Round 11 count, and the finite completion identity on one fixed toy modulus family using formal cyclic Fourier arithmetic. That toy identity checks the placement of the primitive term, not the large-X support construction or a prime estimate. The actual support construction is an ordinary asymptotic proof already pinned in the source receipt. No parameter search or large computation was performed.


<a id="report-47"></a>

# Current report 47: Independent review of the inherited count and sampling constants

**Collection:** R12 — exact limits of sampling and dispersion transfers.

**Source:** [research/dyson/round12/sampling-geometry/COUNTING_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/sampling-geometry/COUNTING_REVIEW.md).

**SHA-256:** `820dfdc6707cdc1c29f7eef61dc884d3f6c96980ffcffab661cd790e3843bbc2`. **Git blob:** `9311aa64f31b7d0d07a87706c442941362346dc0`. **Original bytes:** 2258.

## Independent review of the inherited count and sampling constants

Date: 2026-09-05. Reviewer: the conductor-arithmetic/dispersion-transfer agent.
Scope: Sections 1–3 of ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md only.

Reviewed report SHA-256:
cb52d72f6068c3030968209d8aa028439ea4dc309aa5584d216a1d7d30a1a59d.
This hash was recomputed from the frozen file. The inherited Round 11 conductor
report was also checked at its pinned SHA-256
46347799005bb0f53af25c2a7e8ffb2b2217d92688c7651327dde3562f114b92.

**Accepted within the stated scope.** The following calculations were checked
independently against the actual arithmetic support proof.

- The count \(c_0Q/(2\log^{348}X)\), denominator bound \(d>Q/2\), and
  \(d/(32H)\) primitive numerators give at least
  \(c_0Q^2/(128H\log^{348}X)\) distinct reduced frequencies. No duplicate
  rational frequencies or permutation counts enter.
- Partition into at most \(8X/H\) intervals gives a cell containing at least
  \(c_0Q^2/(1024X\log^{348}X)\) frequencies. This only uses the proved total
  count; no distribution theorem within short intervals is assumed.
- With \(N=\lceil X\rceil\), \(M=\lfloor X/10\rfloor\), the integer support
  really is inside \([X,1.1X]\). Factoring out the carrier on a cell of width
  at most \(1/(100X)\) leaves phase spread at most \(\pi/1000\).
- The lower pointwise bound \(M/(2\sqrt H)\), Parseval norm \(M/H\), and
  \(M\ge X/20\) give the stated sampling ratio
  \(c_0Q^2/(81920\log^{348}X)\).
- The actual coefficient lower bound
  \(|C_\beta|^2\ge m_v^2H^2/(8Q^2)\) then gives precisely the weighted
  denominator 655360 in equation (10).

The constants and their directions are correct for all sufficiently large real
\(X\), uniformly in the stated \(H\)-range. The asymptotic threshold is not
claimed effective or numerically reached.

This review does not turn the artificial sampling packet into a prime
polynomial, and does not establish a lower bound for the full signed pairing.
The final wording correctly keeps the positive unweighted and fixed
absolute-coefficient sampling statements separate from other possible
reweightings or signed arguments. Sections 4–6 and the finite script are
outside this narrow review; the coordinator conducts the wider review.


<a id="report-48"></a>

# Current report 48: Two explicit hypothesis failures in the proposed dispersion transfer

**Collection:** R12 — exact limits of sampling and dispersion transfers.

**Source:** [research/dyson/round12/dispersion-transfer/DISPERSION_HYPOTHESIS_OBSTRUCTION.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/dispersion-transfer/DISPERSION_HYPOTHESIS_OBSTRUCTION.md).

**SHA-256:** `26536af7b5e6ebfb8fb4f7c7be993543c57152e29c6fd2b039c5eb147ccefd95`. **Git blob:** `f94a750227ddad82bfc5b86b3f5c7ea171330072`. **Original bytes:** 18370.

## Two explicit hypothesis failures in the proposed dispersion transfer

Date: 2026-09-05. Status: ordinary arithmetic proofs, with exact source-parameter checks. No improved bound for the actual prime pairing is proved here. The counterexample below concerns preservation of a coefficient hypothesis; it is not a counterexample to the source dispersion theorem.

The 186 paper's triply densely divisible dispersion theorem does not directly give the missing improvement in the completed Round 11 pairing. Two specific proposed applications fail:

1. Absorbing a completed additive phase into a Siegel–Walfisz coefficient does not preserve that property. This fails for a prime-interval coefficient at legal source scales, with a conductor in our actual canonical complementary family and the actual reduced numerator \(a=1\). The resulting discrepancy at modulus 3 is explicitly of order \(N/\log N\).
2. Lifting the growing shift interval through the source's product-of-local-residue-sets lemma requires \(\varphi(d)\) classes on an explicit subfamily. Its bounded-local-class hypothesis is therefore unavailable, even after all primitive restrictions are imposed.

These statements leave open a dispersion argument retaining the shift, the additive phase and the prime coefficient jointly. They do not prove the remaining \(X^{.023}\) loss is unavoidable for primes. The source is [OpenAI, *Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf); precise printed-page locations and file hashes are recorded below and in the companion certificate.

### 1. The exact pairing and the family being tested

Put
\[
Q=X^{523/1000},\qquad X^{1/6}\le H\le X^{2/7},
\qquad e(t)=\exp(2\pi i t).
\tag{1}
\]
Fix a nonnegative, nonzero \(V\in C_c^\infty(1,2)\). This hypothesis permits the real-prime support construction used here; no claim uniform over arbitrary signed profiles is made.

The canonical family \(\mathcal Q_X\) contains every distinct squarefree modulus \(q=[D,E]\) satisfying
\[
\begin{gathered}
D,E\le X^{523/2000},\qquad q>X^{1/2},\\
p^{3/2}D_{\ge p}\le X^{501/2000}
\quad(p\mid D,\ p>X^{1/1000}),\\
p^{3/2}E_{\ge p}\le X^{501/2000}
\quad(p\mid E,\ p>X^{1/1000}).
\end{gathered}
\tag{2}
\]
Each modulus is counted once with coefficient \(\mu(q)\). These are the balanced complementary predicates fixed in Round 9. Source Proposition 2.3, printed pp.4–5, gives
\[
\mathcal Q_X\subset
\{q\le Q:q\text{ squarefree},\ q\in\mathcal D^{(3)}(X^{1/1000})\}.
\tag{3}
\]
There is no arbitrary-subset Möbius-cancellation assertion.

For a separated fixed smooth prime weight \(f\), the exact completed expression is
\[
\mathfrak B_j(f,V)=
\sum_{\substack{2\le d\le Q\\1\le a<d,\ (a,d)=1}}
S_{V,H}(a/d)M_d^{(j)}
\left[A_f(a/d)-\frac{\mu(d)}{\varphi(d)}A_f(0)\right],
\tag{4}
\]
where
\[
\begin{split}
S_{V,H}(\beta)&=\sum_h V(h/H)e(-\beta h),\\
M_d^{(j)}&=\sum_{\substack{q\in\mathcal Q_X\\d\mid q}}
\frac{\mu(q)(\log q)^j}{q},\qquad j=0,1,\\
A_f(\beta)&=\sum_{p\ {\rm prime}}(\log p)f(p/X)e(\beta p).
\end{split}
\tag{5}
\]
The Ramanujan principal subtraction in (4) is retained. The zero frequency cancels exactly. The actual logarithmic kernel is assembled from \(\mathfrak B_0,\mathfrak B_1\) by the already proved uniformly summable smooth separation; the term \(\log X\,\mathfrak B_0\) must also be counted. This report tests an attempted arithmetic input to (4), not a replacement positive norm.

Under RH, the frozen Round 11 bound for the complete fixed smooth discrepancy component is
\[
O_{V,\chi}\!\left(\sqrt{X(X+Q^2)}(\log X)^5\right)
=O_{V,\chi}\!\left(X^{1023/1000}(\log X)^5\right).
\tag{6}
\]
Its remaining power loss comes from \(Q/\sqrt X=X^{23/1000}\). No step below improves (6).

### 2. Actual terminal conductors and source-compatible scales

The frozen Round 11 construction uses
\[
u=\frac9{100},\quad
\kappa=\frac{343}{346000},\quad
\lambda=2^{-1/348}.
\]
Let \(\mathcal F_X\) consist of products of two distinct primes in
\((\lambda X^u,X^u]\) and 346 distinct primes in
\((\lambda X^\kappa,X^\kappa]\). For every sufficiently large real \(X\), that construction proves
\[
\mathcal F_X\subset\mathcal Q_X\cap(Q/2,Q],\qquad
|\mathcal F_X|\sim
c_0\frac{Q}{(\log X)^{348}},\quad c_0>0.
\tag{7}
\]
The exact constant is
\[
c_0=\frac{(1-\lambda)^{348}}{2!\,346!\,u^2\kappa^{346}}.
\]
Unique factorization prevents permutation overcounting. The source guards are checked by splitting one large and 173 small primes into each root:
\[
2u+346\kappa=\frac{523}{1000},\qquad
u+173\kappa=\frac{523}{2000},\qquad
\frac52u=\frac9{40}<\frac{501}{2000}.
\tag{8}
\]
Thus these are actual complementary moduli, with two factors larger than the density parameter. Their existence and count use only the prime number theorem on fixed-ratio intervals.

Every \(d\in\mathcal F_X\) has exactly 348 prime factors, all tending to infinity; in particular \(3\nmid d\) eventually. Also \(\mu(d)=1\) and
\[
M_d^{(0)}=\frac1d,\qquad M_d^{(1)}=\frac{\log d}{d},
\tag{9}
\]
because the only multiple of \(d>Q/2\) at most \(Q\) is \(d\) itself. Signed lower moduli cannot cancel these terminal coefficients.

Source Proposition 2.18, printed pp.10–11, applies to a convolution \(\alpha*\beta\) at scales \(MN\asymp X\), with
\[
X^{1/2-\sigma}\le N\le X^{1/2},
\tag{10}
\]
provided \(\beta\) has the source Siegel–Walfisz property and
\[
72\omega+24\delta<1,\quad
48\omega+16\delta+4\sigma<1,\quad
64\omega+20\delta+2\sigma<1.
\tag{11}
\]
Use the actual parameters
\[
\omega=\frac3{250},\quad
\delta=\frac1{1000},\quad
\varepsilon=\frac1{1000},\quad
\sigma=\frac{101}{1000}.
\tag{12}
\]
The modulus cutoff \(X^{1/2+2\omega-\varepsilon}\) is exactly \(Q\).
The three left sides of (11) are respectively
\[
\frac{111}{125}=.888,\qquad
\frac{249}{250}=.996,\qquad
\frac{99}{100}=.990.
\tag{13}
\]
Take
\[
N=X^{2/5},\qquad M=X^{3/5}.
\tag{14}
\]
Then \(MN=X\), and \(1/2-\sigma=.399<.4<.5\). The counterexample below therefore does not manufacture an out-of-range factor or an inadmissible modulus.

### 3. A real-prime coefficient loses Siegel–Walfisz after phase absorption

The source's Definition 2.9, printed p.6, requires one fixed \(C_{\rm SW}\) such that for every fixed \(L>0\)
\[
\left|
\sum_{\substack{n\equiv a\pmod r\\(n,s)=1}}\beta(n)
-\frac1{\varphi(r)}
\sum_{(n,rs)=1}\beta(n)
\right|
\ll_L \tau(rs)^{C_{\rm SW}}N(\log X)^{-L},
\tag{15}
\]
uniformly in \(r,s,a\) with \((a,r)=1\). Here \(r\) denotes the test modulus; it is not the conductor \(d\).

By source Proposition 2.10, printed p.7,
\[
\beta_X(n)=1_{\{n\ {\rm prime},\ N\le n<2N\}}
\tag{16}
\]
has this property, uniformly in the interval endpoints and auxiliary coprimality parameter, because \(N=X^{2/5}\). It is a coefficient sequence located at scale \(N\).

**Lemma.** For every sufficiently large real \(X\), and every
\(d\in\mathcal F_X\), there is a unit \(m\bmod d\) represented by an integer in \([M,2M]\) such that the sequence
\[
\widetilde\beta_{X,d,m}(n)=\beta_X(n)e(mn/d)
\tag{17}
\]
does not satisfy (15) as a uniform family. At \(r=3,s=1,a=1\), its discrepancy is
\[
\boxed{
\Delta(\widetilde\beta;1\bmod3)
=\left(\frac{i\sqrt3}{4}+o(1)\right)\frac{N}{\log N}.
}
\tag{18}
\]
The \(o(1)\) is uniform in the conductors \(d\) and choices of \(m\) made below. No RH assumption is used.

**Proof.** Define
\[
k=\begin{cases}
(d-1)/3,&d\equiv1\pmod3,\\
(d+1)/3,&d\equiv2\pmod3.
\end{cases}
\tag{19}
\]
Thus
\[
\frac{k}{d}=
\begin{cases}
\frac13-\frac1{3d},&d\equiv1\pmod3,\\
\frac13+\frac1{3d},&d\equiv2\pmod3,
\end{cases}
\qquad (k,d)=1.
\tag{20}
\]
The gcd assertion follows from \(3k=d\pm1\). Because
\[
\frac{M}{d}\ge X^{3/5-523/1000}=X^{77/1000}\longrightarrow\infty,
\]
the interval \([M,2M]\) contains an integer \(m\equiv k\pmod d\). Choose one. Then \(m\) is a unit modulo \(d\) and \(e(mn/d)=e(kn/d)\).

The numerator \(a=1\) used here is an actual reduced completed frequency. In fact \(d/(16H)\to\infty\) uniformly in the prescribed \(H\)-range, and the Round 11 positivity argument gives
\[
|S_{V,H}(1/d)|\ge\frac{H}{2\sqrt2}\int V>0
\]
for all sufficiently large \(X\). The phase being tested is therefore not attached to a missing or zero-weight frequency.

For \(n\in[N,2N)\), equations (20) give
\[
e(kn/d)=e(n/3)\bigl(1+O(N/d)\bigr),
\tag{21}
\]
with an absolute implied constant for either sign. The prime number theorem in the two fixed reduced classes modulo 3 gives, for \(b=1,2\),
\[
\#\{N\le p<2N:p\equiv b\pmod3\}
=\left(\frac12+o(1)\right)\frac{N}{\log N}.
\tag{22}
\]
Summing (21) over these primes shows
\[
\sum_{n\equiv b(3)}\widetilde\beta(n)
=e(b/3)\left(\frac12+o(1)\right)\frac N{\log N}
+O\!\left(\frac{N^2}{d\log N}\right).
\tag{23}
\]
The perturbation is \(o(N/\log N)\), uniformly, since
\(N/d\le2X^{-123/1000}\). All supported primes exceed 3. Hence the exact principal subtraction in (15) is one half of the sum of the two class sums. Their difference divided by two is
\[
\frac{e(1/3)-e(2/3)}4\frac N{\log N}
+o\!\left(\frac N{\log N}\right)
=\frac{i\sqrt3}{4}\frac N{\log N}
+o\!\left(\frac N{\log N}\right),
\]
which proves (18). The two signs in (20) both tend to the same cubic phase, so the leading sign in (18) does not switch with \(d\bmod3\).

Finally, for \(L=2\), the right side of (15) at \(r=3,s=1\) is
\(O(2^{C_{\rm SW}}N(\log X)^{-2})\). Since
\(\log N=(2/5)\log X\), (18) is larger by an unbounded logarithmic factor for every fixed \(C_{\rm SW}\) and implied constant. This is the claimed failure. \(\square\)

This lemma has a precise scope. A convolution expansion of an additive prime phase creates terms \(e(am n/d)\). To absorb them into the shorter factor and apply Proposition 2.18, one would have to check the Siegel–Walfisz property of \(\beta(n)e(am n/d)\), uniformly in the variables being summed. It does not follow from that property for \(\beta\), even on the actual allowed conductors, at allowed scales and with a unit \(m\). A delta sequence supported on the chosen \(m\) is itself an allowed longer coefficient, so the issue is not a failure of divisor boundedness. Moreover, the absorbed sequence varies with \(m,a,d\), whereas the source dispersion sum is stated for a fixed coefficient family before its modulus sum.

The lemma does not assert that every factor in a particular Heath–Brown expansion fails (15), or that one bad slice prevents an averaged estimate. Such an averaged estimate would be new input to the proposed transfer and would have to retain this dependence. Source Proposition 2.18 and its proof in Appendix A.4.2 remain consistent with the example: their hypothesis (15) has been violated after the proposed absorption.

### 4. The shift interval is not a bounded product of local residue sets

There is a second tempting use of the source. Equation (2.5), printed p.7, permits a set of primes and one coherent primitive residue class that depend on \(X\), uniformly, but fixes the class outside the modulus sum. For one fixed shift \(h\), this is the legal Round 9 application. Simultaneous shifts \(h\asymp H\) require more than that statement.

Source Proposition 2.14, printed pp.9–10, lifts coherent estimates to a product of local nonempty class sets \(\mathcal A_p\subseteq(\mathbb Z/p\mathbb Z)^\times\), at the explicit cost
\[
\mathfrak m(d)=\prod_{p\mid d}|\mathcal A_p|.
\tag{24}
\]
It obtains a fixed divisor-weight cost when \(|\mathcal A_p|\le K\) for a fixed \(K\). Its underlying finite inequality is valid without this restriction; the restriction is what permits the subsequent source error bound without a power cost.

Choose a closed interval \([z_0,z_1]\subset(1,2)\) of positive length \(\ell=z_1-z_0\) on which \(V\) is strictly positive. Such an interval exists. For any \(d\in\mathcal F_X\), put
\[
\mathcal H_d=\{h\in[z_0H,z_1H]\cap\mathbb Z:(h,d)=1\}.
\]
For every prime \(p\mid d\) and every unit \(a\bmod p\),
\[
\begin{split}
\#\{h\in\mathcal H_d:h\equiv a\pmod p\}
&\ge\frac{\ell H}{p}-1
-\sum_{\substack{r\mid d\\r\ {\rm prime},\,r\ne p}}
\left(\frac{\ell H}{pr}+1\right)\\
&\ge\frac{\ell H}{p}
\left(1-\frac{347}{\lambda X^\kappa}\right)-348.
\end{split}
\tag{25}
\]
The first line uses the Chinese remainder theorem for the simultaneous conditions \(h\equiv a\pmod p,\ h\equiv0\pmod r\); the primes are distinct. Every \(p\mid d\) is at most \(X^{9/100}\), so
\[
\frac Hp\ge X^{1/6-9/100}=X^{23/300}\longrightarrow\infty.
\]
Thus (25) is positive uniformly in \(p,a,d,H\), once \(X\) is sufficiently large.

Consequently, even **after the global coprimality restriction**, the image of \(\mathcal H_d\) modulo each \(p\mid d\) is the entire unit group. Its smallest product-of-local-images hull therefore has
\[
\mathcal A_p=(\mathbb Z/p\mathbb Z)^\times,\qquad
\mathfrak m(d)=\prod_{p\mid d}(p-1)=\varphi(d).
\tag{26}
\]
Since
\[
1\ge\frac{\varphi(d)}d
=\prod_{p\mid d}(1-1/p)
\ge1-\frac{348}{\lambda X^\kappa},
\]
one has \(\mathfrak m(d)\sim d\asymp Q\), uniformly on \(\mathcal F_X\). On the other hand \(\tau(d)=2^{348}\) is constant. For any fixed \(B,C\),
\[
\frac{\mathfrak m(d)}{\tau(d)^B(\log X)^C}\longrightarrow\infty.
\tag{27}
\]
Therefore the divisor-weight consequence of Proposition 2.14 is not available for this product hull. Source logarithmic savings cannot absorb this \(\asymp Q\) factor.

The actual interval supplies only \(O(H)\) coherent global classes, since \(H\ll d\). Its local images have discarded the correlation between residues at different primes. The failure in (27) is a failure of this product-hull transfer, not an impossibility theorem for a nonproduct residue set or a signed average over the interval.

### 5. A short-factor reinterpretation also misses the stated scale range

If one instead tries to treat the shift length \(H\) itself as the shorter convolution scale \(N\) at total scale \(X\), the second inequality of (11), with the actual \(\omega,\delta\), forces
\[
\sigma<
\frac{1-48\omega-16\delta}{4}
=\frac{51}{500}.
\]
It follows that
\[
N\ge X^{1/2-\sigma}>X^{199/500},
\tag{28}
\]
whereas \(H\le X^{2/7}\). The positive exponent gap is
\[
\frac{199}{500}-\frac27=\frac{393}{3500}.
\tag{29}
\]
Thus this specific reinterpretation is outside Proposition 2.18 before coefficient conditions are considered. This says nothing about a different regrouping, a different total scale with all errors tracked, or a new multivariable dispersion proof.

### 6. What is and is not established

The actual factorization information has been used, not merely a scalar distribution exponent. The conductors in the counterexample satisfy the complementary predicates and retain the full original triple dense-divisibility budget. The modulus cutoff, both convolution scales, the primitive restrictions, the sign of the cubic phase, and the source's absolute Siegel–Walfisz normalization have all been checked.

What remains absent is an estimate for the signed joint object (4), retaining its \(d\)-dependent additive phase, its conductor coefficient \(M_d^{(j)}\), and its growing coherent shift interval. A direct \(X(\log X)^C\)-scale bound for that object would already remove the remaining power loss in (6); the actual zeta covariance target requires sharper control of the logarithms and all other components as well. One sufficient component-level condition, with suitable uniformity for the smooth separated profiles, would be
\[
\log X\,|\mathfrak B_0|+|\mathfrak B_1|
=o(X\log X).
\tag{30}
\]
No assertion that (30) follows from the source theorem, or that it is false, is made.

The source's Appendix A.4.2, printed pp.35–36, fixes coefficient supports and derivative bounds before taking suprema, performs a dispersion square, chooses dense divisors with their quotient losses, and retains its original unit masks. The resulting rational completion estimate is part of that argument; it is not a theorem about arbitrary modulus-dependent twisted coefficients. Reusing it for (4) would require a new reduction with the extra variable and coefficient dependence explicitly controlled.

The bounded conclusion is therefore: phase absorption and product-local residue lifting do not justify the proposed transfer, with the exact failures proved above. A joint dispersion argument remains a meaningful open arithmetic step. The finite check accompanying this note verifies rational inequalities, the cubic-phase algebra and modular selection; it does not purport to prove a numerical prime-gap bound or realize the large asymptotic moduli on a computer.

### 7. Provenance and reproduction

Primary source: [OpenAI, *Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf).

| Source location | Use in this note |
| --- | --- |
| Definition 2.1 and Proposition 2.3, pp.4–5 | Strong recursive dense divisibility and actual complementary moduli |
| Definitions 2.6–2.9, p.6, especially equation (2.4) | Coefficient families, scale and the exact uniform SW requirement |
| Proposition 2.10 and equation (2.5), p.7 | Prime-interval SW; one coherent class fixed outside the modulus sum |
| Proposition 2.14, pp.9–10 | CRT product-set lift and its explicit \(\mathfrak m(d)\) cost |
| Proposition 2.18, pp.10–11, equation (2.14) | Bilinear dispersion hypotheses and scale inequalities |
| Appendix A.4.2, pp.35–36 | Source dependence on fixed coefficients, divisor choices and unit masks |

The local primary PDF SHA-256 is
456f05e0a3ef589ebb0e9abcfd31f140f3c945adbf6950e00ef371a3c88b0930.
Its extracted text SHA-256 is
ded13a7c74fcfce64e85769e05b5869803dccdf53b88be2c2f3c0b344f95ee84.
The source-preserving official repository was pinned at commit
61340d0b74163003b32756bb16e91d9209a5e330.
No source files were modified.

The exact construction and coefficient-isolation proof used from Round 11 is
CONDUCTOR_MASS_LOWER_BOUND.md, SHA-256
46347799005bb0f53af25c2a7e8ffb2b2217d92688c7651327dde3562f114b92.
The current note only uses its explicitly stated all-large-\(X\) conclusions, not a claimed numerical realization.

Run the adjacent standard-library Python script check_dispersion_hypotheses.py. It writes dispersion_hypotheses_certificate.json, including the final report/script hashes and primary-source hashes. The fixed small integer examples in that script test only the algebra of (19)–(20); they are not substitutes for the canonical-family existence proof.


<a id="report-49"></a>

# Current report 49: Direct Selberg control of the centered mixed remainder: the precision and sign gap

**Collection:** R12 — exact limits of sampling and dispersion transfers.

**Source:** [research/dyson/round12/mixed-arithmetic/SELBERG_MIXED_REMAINDER_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/mixed-arithmetic/SELBERG_MIXED_REMAINDER_AUDIT.md).

**SHA-256:** `6223e9a54c44c31d344c2f932fe81ca6ad4672e5f6ef625adfeae07b4ed5a308`. **Git blob:** `83e7372b38b74227b67a9579413ae7773bb6a7a8`. **Original bytes:** 10511.

## Direct Selberg control of the centered mixed remainder: the precision and sign gap

Date: 2026-09-05. This is a bounded analytical test of the actual genuine-prime remainder. It gives an explicit, insufficient one-sided bound using a primary RH short-interval theorem. It does not introduce a substitute point process, differentiate an unknown error, or separate divergent prime and continuum tails. No parameter scan was run.

**Outcome.** The direct Selberg–Gallagher route below gives
\[
|M_T(b)|\ll\frac{\log T}{b^2}.
\tag{1}
\]
Consequently its lower bound on \(\int_b^{2b}\mathcal B_T(s)\,ds\) is only of order \(-\log T/b\), whereas the target is \(-3/(2b^2)+\varepsilon/b^2\). This is a quantified failure of this particular arithmetic estimate, not an impossibility theorem and not a claim to improve the previously known individual-norm bounds.

**This is not the strongest known RH norm estimate.** Round 10 already established the stronger \(E_T(b)=O(1)\) on the slow range. The same primary page also records Selberg's stronger global weighted estimate, discussed in Section 4 below. Neither is to be replaced by the weaker local-bound calculation (1). The remaining issue is a one-sided fluctuation estimate in a shrinking logarithmic shell, with its leading coefficient and next-order precision.

### 1. Primary input is already about genuine primes

Let \(\theta(x)=\sum_{p\leq x}\log p\). Saffari and Vaughan, [On the fractional parts of x/n and related sequences II](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf), Ann. Inst. Fourier 27(2) (1977), define this prime-weighted function in (6.1). Under RH, their Lemma 5, equation (6.4), gives
\[
\int_X^{2X}|\theta(x+\eta x)-\theta(x)-\eta x|^2\,dx
\ll \eta X^2\log^2(2/\eta),
\quad X\geq4,\quad0<\eta\leq1.
\tag{2}
\]
The uniformity in \(\eta\), and the fact that the statement concerns \(\theta\), were checked in the primary text on printed pages 19–22. No GRH or pair-correlation conjecture is assumed. Formula (2) is an upper bound, with an unspecified absolute constant; it is not a variance asymptotic or a positive lower bound.

### 2. Gallagher's inequality applied to the combined centered measure

Retain \(L=\log T\), \(N=\lfloor T/L^6\rfloor\), and the Round 11 finite centered tails
\[
C_{s,Y}(t)=\int_{(N,Y]}x^{-1/2-s/(2L)-it}\,d(\theta(x)-x),
\]
\[
D_{s,Y}(t)=\int_{(N,Y]}
\left(\frac{\log x}{L}-1\right)x^{-1/2-s/(2L)-it}\,d(\theta(x)-x).
\tag{3}
\]
Both the prime and continuous terms occur inside the same finite signed measure. Let \(\tau=1/T\). For any finite measure \(\nu\) on logarithmic coordinates, Plancherel applied to its convolution with an interval of length \(\tau\) gives
\[
\int_{-T}^T|\widehat\nu(t)|^2dt
\leq\frac{2\pi T^2}{c_0^2}
\int_{\mathbb R}|\nu((v,v+\tau])|^2dv,
\quad c_0=\frac{\sin(1/2)}{1/2}.
\tag{4}
\]
Here the transform uses \(e^{-itv}\). The Fourier transform of the interval has modulus at least \(c_0/T\) for \(|t|\leq T\), which proves (4), including its direction. This remains valid for the finite prime atoms plus continuous density in (3).

For a logarithmic interval starting at \(x=e^v\), the right side contains
\(\int_x^{xe^\tau}g(u)\,d(\theta(u)-u)\). Put \(F=\theta-\mathrm{id}\). Integration by parts on this short interval expresses it as
\[
g(xe^\tau)[F(xe^\tau)-F(x)]
-\int_0^{e^\tau-1}xg'(x(1+\eta))
[F(x(1+\eta))-F(x)]\,d\eta.
\tag{5}
\]
For \(x\in[X,2X]\), apply (2) to each increment in (5), then Minkowski. The integral in \(\eta\) is bounded by a constant times the endpoint contribution since
\(\int_0^\tau\sqrt\eta\log(2/\eta)d\eta\ll\tau^{3/2}\log(2/\tau)\).
For \(\sigma=1/2+s/(2L)\in[1/2,3/4]\), this gives
\[
\int_X^{2X}\left|\int_x^{xe^\tau}g(u)\,dF(u)\right|^2\frac{dx}{x}
\ll X^{1-2\sigma}\tau L^2 w_X^2,
\tag{6}
\]
where \(w_X=1\) for \(g(u)=u^{-\sigma}\), and
\(w_X=|\log X/L-1|+O(1/L)\) for
\(g(u)=(\log u/L-1)u^{-\sigma}\). All constants are uniform in the stated range. The extra \(1/L\) controls the variation across a dyadic interval and the derivative of the logarithmic weight.

### 3. Cutoffs and dyadic summation

For the upper cutoff \(Y\), the crossing windows have total logarithmic length \(O(1/T)\). The RH pointwise bound on \(F\), together with weighted partial summation, bounds their contribution after (4) by
\[
O\left(TY^{-s/L}\log^4Y
\left(1+\left|\frac{\log Y}{L}-1\right|\right)^2\right).
\]
It tends to zero for fixed \(T,s>0\) as \(Y\to\infty\). The order of limits is explicit. The uniform analytic cutoff from Round 11 could also be used; no practical finite-prime experiment is asserted.

At the lower cutoff, \(N\) is an integer and the prime tail is strict. For large \(T\),
\(Ne^{1/T}<N+1\). Thus a crossing window from below \(N\) contains no retained prime atom and only the continuous density on its very short intersection with \((N,\infty)\). Its contribution is negligible. The endpoint term implicit in the limiting analytic continuation has not been discarded: (3) converges to precisely the centered tail defined in Round 11.

Partition the starting points \(x\geq N\) into \([2^jN,2^{j+1}N]\). This partitions the integration variable in (4), not the prime measure, so it creates no extra prime-cutoff boundary at the dyadic endpoints. Let
\(d_N=1-\log N/L=6\log L/L+o(1/L)\).
For \(2\leq s\leq2G(T)\), where \(G=o(\log L)\), geometric summation gives
\[
\sum_{j\geq0}(2^jN)^{-s/L}\ll e^{-s}\frac Ls,
\]
\[
\sum_{j\geq0}(2^jN)^{-s/L}
\left(\left|-d_N+\frac{j\log2}{L}\right|+\frac1L\right)^2
\ll e^{-s}\frac L{s^3}.
\tag{7}
\]
For the second estimate, use the exact geometric-series sums for \(1,j,j^2\), together with \(sd_N=o(1)\). Equations (4), (6), and (7) therefore prove for the limiting centered tails
\[
\frac{e^s\|C_s\|_2^2}{TL^2}\ll\frac Ls,
\qquad
\frac{e^s\|D_s\|_2^2}{TL^2}\ll\frac L{s^3}.
\tag{8}
\]
These norms are over \([0,T]\), a subinterval of that bounded by (4).

Cauchy–Schwarz in the actual mixed product now gives
\[
\left|\frac{e^s}{TL^2}\Re\langle C_s,D_s\rangle\right|
\ll\frac L{s^2}.
\]
The already quantified pole replacement is \(O(e^sL^{-3})\), uniformly negligible here; adding it proves (1) for \(M_T\) itself. No prime-power replacement is necessary because (2) was genuine-prime input from the start.

### 4. The concrete integrated lower bound is too weak

Write \(\mathcal B_T(s)\) for the single jointly centered remainder of Round 11, including all off-diagonal prime-prime, prime-continuum, and continuum-continuum terms before taking the cutoff limit. Its proved diagonal decomposition implies
\[
\int_b^{2b}\mathcal B_T(s)\,ds
\geq-C\frac Lb-\frac1{2b}-\frac3{4b^2}+o(b^{-2}).
\tag{9}
\]
This follows from the actual mixed-product bound above and the exact integrated prime diagonal. It is a valid one-sided consequence, but its negative error is larger than the required \(b^{-2}\) accuracy by a factor of order \(Lb\).

For any fixed nonnegative smooth \(\chi\) supported in \((1,2)\), the same proof gives
\[
\left|\int_b^{2b}\chi(s/b)M_T(s)\,ds\right|
\ll_\chi\frac Lb.
\]
Thus smoothing in \(b\) alone does not improve this estimate. The loss of \(L\) is visible in (2): the theorem supplies \(\log^2(2/\eta)\), while the fluctuation scale at \(\eta\asymp1/T\) has only one logarithm. Even hypothetically replacing the squared logarithm by a single logarithm in this argument would yield only \(|M_T(s)|\ll s^{-2}\), with no positive leading coefficient or the required next-order deficit below 2. This diagnoses the sign loss of the Cauchy–Schwarz step, not a logical impossibility of stronger consequences from a strengthened theorem.

There is a material stronger-input nuance. On the same primary page, equation (6.5) recalls Selberg's global estimate
\[
\int_0^{\eta^{-A}}
|\theta(x+\eta x)-\theta(x)-\eta x|^2\frac{dx}{x^2}
\ll_A\eta\log^2(2/\eta),
\tag{9a}
\]
for a fixed admissible exponent \(A>1\), corresponding to the fixed exponent parameter in the source remark. It is not legitimate to let that exponent grow with \(T\). For any such fixed \(A\), the active edge shell \(1/s\leq\log x/L-1\leq2/s\) lies within this range when \(s\) and then \(T\) are large enough. Using a fixed smooth filter of \(s(\log x/L-1)\), the argument (4)–(5) with (9a) gives normalized squared norms \(O_A(1)\) and \(O_A(s^{-2})\) for the filtered centered tail and its log-weighted companion. Indeed the Mellin damping on that shell is \(O(e^{-s})\); the excess weight is \(O(1/s)\), and its differentiation costs only \(O(1/L)\). These are bounds for a filtered component, not a new identity for the full mixed moment.

Cauchy–Schwarz then controls that component only by \(O_A(1/s)\), and does not give a positive leading \(1/s^2\). The global estimate supplies a bound on accumulated positive variance, not a quantitative lower increment on the shrinking shell and not the required signed mixed covariance. This is why merely selecting the stronger stated Selberg bound does not complete the proposed argument. The explicit lower bound (9) is retained as a fully quantified local-theorem consequence, not as a claim of optimal RH control.

### 5. Smoothing does not make the actual kernel termwise positive

At finite cutoff, Fubini in (3) shows that the sharp \(s\)-integrated mixed product has the real kernel
\[
\frac{(xy)^{-1/2}}{L^2}
\bigl(e^{-b v(x,y)}-e^{-2b v(x,y)}\bigr)
\operatorname{sinc}_0(T\log(x/y)),
\quad
v(x,y)=\frac{\log x+\log y}{2L}-1.
\tag{10}
\]
It acts on the same finite signed measure
\(d\theta-dx\) in both variables. Smooth nonnegative \(s\)-weights replace the exponential difference by the corresponding integral of \(v e^{-sv}\); they leave the sinc factor and centering intact.

For example, \(x,y>T\) and \(T\log(x/y)=3\pi/2\) give a positive exponential factor but sinc equal to \(-2/(3\pi)\). These are points in the domain of the actual continuum terms, not a fabricated point process. This rules out simply declaring every off-diagonal kernel contribution nonnegative after \(b\)-smoothing. A negative kernel value alone is not a proof that its quadratic form lacks positivity; no such general claim is made here. The relevant arithmetic lower estimate is still missing.

The bounded attempt therefore stops with the genuine-prime inequality (9) and an explicit precision/sign deficit. Repeating identities or replacing the centered covariance by separate divergent sums cannot fill that deficit. A new one-sided fluctuation estimate, or cancellation in the centered mixed pairing beyond these upper norms, is required.


<a id="report-50"></a>

# Current report 50: Independent review of the three bounded Round 12 attempts

**Collection:** R12 — exact limits of sampling and dispersion transfers.

**Source:** [research/dyson/round12/INDEPENDENT_ROOT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round12/INDEPENDENT_ROOT_REVIEW.md).

**SHA-256:** `bff32012d2eb29877b51cd569d976016418d16abe6120a000a3c811f737a8557`. **Git blob:** `4e1e0a5cf1592d01c9bb2ab182f5e2c72eeec035`. **Original bytes:** 7673.

## Independent review of the three bounded Round 12 attempts

Date: 2026-09-05. Reviewer: root Astra, independently of all three authoring lanes. I read all three complete reports, checked the inherited Round 11 construction, inspected the relevant primary source statements, and checked the new elementary arguments below. Accepted scope: ordinary proofs of specific failed shortcuts and an insufficient actual-prime estimate. No stronger bound for the actual signed prime pairing is proved.

Pinned author reports:

| Report | SHA256 |
|---|---|
| sampling-geometry/ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md | cb52d72f6068c3030968209d8aa028439ea4dc309aa5584d216a1d7d30a1a59d |
| dispersion-transfer/DISPERSION_HYPOTHESIS_OBSTRUCTION.md | 26536af7b5e6ebfb8fb4f7c7be993543c57152e29c6fd2b039c5eb147ccefd95 |
| mixed-arithmetic/SELBERG_MIXED_REMAINDER_AUDIT.md | 6223e9a54c44c31d344c2f932fe81ca6ad4672e5f6ef625adfeae07b4ed5a308 |

### 1. Positive sampling on the actual modulus support

The inherited count supplies at least c0 Q/(2 log^348 X) actual terminal conductors. Each has at least d/(32H) primitive low numerators and d>Q/2, giving the stated c0 Q^2/(128 H log^348 X) distinct frequencies. The number of cells of length at most 1/(100X) in the small arc is at most 8X/H eventually. Pigeonhole therefore supplies the claimed occupation without a local distribution theorem.

For N=ceil X, M=floor(X/10), the integer frequencies N,...,N+M-1 lie in [X,1.1X]. Within the chosen cell, factoring out the carrier leaves phases at most pi/1000. The lower bound M/(2 sqrt H) and Parseval norm M/H give the sampling constant c0 Q^2/(81920 log^348 X). Squaring the actual coefficient lower bound m_v H/(2 sqrt(2)Q) gives the second constant 1/655360. The global Parseval norms also imply both local small-arc envelopes for rho>=1/H, including the derivative bound.

The constructed polynomial is artificial and phase-tuned. It is not the actual prime polynomial, nor a fixed smooth multiplier of its coefficients. The proof correctly limits its conclusion to positive sampling and the specified absolute-weight operator. It does not prove sharpness for all rearrangements of Cauchy--Schwarz or all signed weightings.

I checked the signed Gram identity directly by expanding the functional coefficient by coefficient. Completing each parent modulus and retaining its Ramanujan principal term gives exactly the residue kernel in equation (16); the zero Fourier term cancels. This equality holds for the Fourier-defined kernel at arbitrary integer n, while its identification with the original unit-restricted progression expression is made only for primes near X. The report states that distinction. Negative or complex cross terms in the signed Gram are not controlled from the positive sampling lower bound.

### 2. The proposed direct dispersion transfers violate actual source hypotheses

I checked the 186 source's Siegel--Walfisz definition, prime-interval example, product-local residue lift, and Proposition 2.18 scale/parameter conditions. At omega=.012, delta=.001, sigma=.101 the three left sides are .888, .996 and .990. N=X^.4, M=X^.6 are legal, and the allowed modulus cap is exactly X^.523. No out-of-range parameter creates the counterexample.

For each canonical d>Q/2 coprime to 3, k=(d-1)/3 or (d+1)/3 is a unit and k/d tends to 1/3. An m in [M,2M] in that residue class exists because M/d tends to infinity. For primes n in [N,2N), replacing e(mn/d) by e(n/3) costs O(N/d) per term. PNT in the two fixed reduced classes mod 3 then gives the discrepancy i sqrt(3) N/(4 log N), with uniform lower-order error O(N^2/(d log N)). Both branches have the same limiting cubic phase and leading sign. This violates the source's SW condition for L=2. The original prime coefficient has SW; the phase-twisted family does not inherit it. A bad slice is not a proof that no averaged dispersion treatment is possible.

For the CRT claim, every prime factor of the constructed conductor is at most X^.09 and at least lambda X^kappa. Counting a chosen local unit class and subtracting divisibility by each other prime leaves at least (ell H/p)(1-347/(lambda X^kappa))-348 positive candidates eventually, uniformly. Thus imposing the global gcd restriction does not reduce any local image. The smallest product hull has phi(d) classes, asymptotic to d, whereas tau(d)=2^348 stays fixed. The bounded-local-class consequence of the source lemma is unavailable. This is a failure of the product-hull reduction; the original coherent interval has many fewer global classes and could be treated differently.

Finally the source constraint forces sigma<.102, hence the short convolution factor exceeds X^.398. H<=X^(2/7) cannot be substituted for that factor at the same total scale. All three conclusions are source-application obstructions, not counterexamples to the source theorem or to the target covariance.

### 3. The direct Selberg mixed estimate is deliberately insufficient

I inspected the primary Saffari--Vaughan text and the rendered printed page 20. Equation (6.4) is indeed a uniform RH estimate for genuine theta and all 0<eta<=1. Equation (6.5) gives the stronger global weighted comparison quoted in the report; its exponent parameter must remain fixed. The report prominently states that its local calculation is weaker than previously established RH norm control and does not claim to exhaust the source's consequences.

The Mellin Gallagher inequality follows from interval convolution and Plancherel with the stated Fourier convention. Its direction and factor 2pi T^2/c0^2 are correct. Short-interval integration by parts retains the centered increment F(x(1+eta))-F(x); the derivative of the log weight is included. Applying Minkowski to the source bound gives equation (6), including the dyadic variation cost 1/log T.

The upper-cutoff crossing term tends to zero at fixed T,s as Y tends to infinity. At the strict integer lower cutoff, N exp(1/T)<N+1 ensures that the crossing interval has no retained prime atom; its continuous contribution is negligible. Dyadic subdivision partitions the integration variable rather than splitting the prime measure, so it introduces no uncounted prime endpoints. Geometric sums in 1,j,j^2 give the norms L/s and L/s^3, with s(1-log N/L)=o(1). Cauchy--Schwarz supplies only the insufficient absolute mixed bound L/s^2 and the integrated lower estimate as stated.

For the separately filtered active shell, the stronger fixed-exponent global estimate gives O(1) and O(s^-2) normalized energies. The shell lies inside its fixed range once s is sufficiently large, the Mellin damping is O(exp(-s)), and the smooth-filter derivative cost s/L is bounded. These estimates are for a component, not a decomposition asserted for the full mixed moment. They give no positive shell increment or required signed coefficient.

The integrated sinc kernel is correctly obtained from the symmetric excess factor v exp(-s v). Its negative pointwise lobe defeats a term-by-term positivity claim, but a negative kernel value is not by itself a negative quadratic-form witness. The report explicitly avoids that stronger false inference. All continuous and prime pieces remain jointly centered.

### Decision

The next substantive improvement requires actual joint arithmetic: a prime-specific concentration estimate, a signed Gram/dispersion argument retaining the coherent shift and its phase, or a one-sided centered fluctuation estimate with the necessary shrinking-shell precision. These reports justify not repeating the three failed shortcuts. They do not prove that the remaining X^.023 factor or the famous conjecture is inaccessible.


<a id="report-51"></a>

# Current report 51: Dyson--Montgomery round 13: extract a rational core and retain the signed remainder

**Collection:** R13 — rational-core extraction and the signed CRT remainder.

**Source:** [research/reports/dyson_round13.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/dyson_round13.md).

**SHA-256:** `b41b76a69d98b282aecc9223a90ba793182f6594f7e57a86245b404b1f779a0c`. **Git blob:** `debde73169d82f89966d80e848ff9b46ead92af7`. **Original bytes:** 5410.

## Dyson--Montgomery round 13: extract a rational core and retain the signed remainder

Date: 2026-09-05. All claims below concern explicitly specified components of the actual arithmetic programme. The strongest bound for the original selected smooth prime discrepancy remains O(X^1.023 log^5 X) under RH. No actual-zeta lower bound is proved here.

### The arithmetic outcome

The new useful extraction is on the terminal Type II slice with Q=X^.523, M=X^.6, N=X^.4 and X^(1/6)<=H<=X^(2/7). Its conductor coefficient is the actual mu(d)/d, d>Q/2; its shift Fourier sum and primitive principal subtraction are retained. The inner coefficients are log-weighted primes in a fixed interval [N,2N), with natural unit restrictions on the longer variable.

On the zero-rational phase core ||am/d||<=C/N, ordinary RH and partial summation replace that prime sum by integral_N^(2N) e(theta u)du. Exact residue counting and the actual numerator weights give total replacement error

\[
O_{C,V}(QM N^{-1/2}\log^2X)=O_{C,V}(X^{923/1000}\log^2X).
\]

This is below X log X, including fixed logarithmic losses. The integral main term is explicit and remains. The proof does not estimate it away. The zero rational in this expression is not the already deleted zero frequency of the original progression completion.

With the admissible test alpha_m=1 and an actual complementary subfamily, a restricted positive phase block has real contribution at least

\[
\frac{c_0\int V}{131072}\frac{X^{1123/1000}}{(\log X)^{348}}.
\]

The primitive principal term is included in this inequality. This is a real-prime arithmetic witness, but only for a subsum. Other phases, conductors and the actual outer coefficients can cancel it. It establishes neither a lower bound for the complete functional nor a failure of the desired zeta theorem.

For other small rational denominators, ordinary SW only gives the recorded logarithmic replacement error, insufficient after the present absolute summation. The legal minor arcs use width 2R/(qN), not fixed C/N cores. Centering over unit residues gives an exact variance improvement; the resulting factored estimate X^1.323 sqrt(log X) is still worse than Round 11's estimate for the original prime pairing. No improvement is claimed from it.

Read the [complete phase report](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/phase-resonance/AVERAGED_RATIONAL_PHASE_TEST.md), [primary-source audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/minor-arc-source/MINOR_ARC_AND_FIXED_INTERVAL_AUDIT.md) and [independent root review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/INDEPENDENT_ROOT_REVIEW.md).

### The exact signed-kernel remainder

The [complete CRT report](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/signed-kernel/SMOOTH_SIGNED_KERNEL_NORM.md) evaluates the smooth integer norm of the actual signed discrepancy kernel. Its main term is exactly X(integral W)(mean²+coefficient squared mass). Its remaining nonzero CRT modes are explicit.

Pairs of original moduli with gcd at least X^.1 have period at most X^.946, so smooth Poisson decay handles them. The complementary small-gcd range contains the unresolved long-period modes. The zero-mode covariance there is small because X^.1/H tends to zero. Reduced-denominator gcd and original-modulus gcd are carefully distinguished.

A specified coherent block in the actual frequencies contributes at least a positive constant times Q²H/log^696 X. Its phase and occupancy constants are explicit. This remains a subsum of a signed expression; the report makes no inference that it lower-bounds the complete norm or remainder. Even an ideal generic norm of order XH would not by itself supply the desired prime-specific estimate. The [separate independent audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/signed-kernel/INDEPENDENT_AUDIT.md) accepts these conclusions with their limited scope.

### Evidence and reproducibility

All 21 original research, review and reference files, totaling 6,973,902 bytes, are preserved in the local `Astra-Local-Archive/round13-originals`. Fifteen research/review/receipt files are public and verbatim. The six full third-party paper/text/page-image files remain local, identified by primary URLs and hashes in the public receipts.

The [integration replay](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/logs/round13-integration/recheck.json) runs two inspected scripts in a temporary copy. The exact CRT output is unchanged in every field. The phase output is unchanged after excluding only three temporary primary-source paths. Tests cover 100 CRT compatibility cases, the unit-masked Fourier identity, exact centered variance, residue bounds, rational exponents, constants and primary-source hashes. These are checks of the algebra and provenance, not numerical proofs of the analytic source theorems.

No new computational search, model service, infrastructure, prime realization at an enormous X or Fable session is introduced. The next arithmetic task is to control the signed retained main terms for the actual long coefficients. A separate Type I removal is being investigated and is not assumed by this report.

### Remaining research target

The complete sharp covariance, its complementary divisor pieces and the strict mixed residual lower bound remain open. In particular the sufficient W_T lower limit 1/16 and compact Fourier test above 7/10 have not been established. These documents preserve a checkable advance in one extraction and an exact description of its remaining terms, not a proof of RH, AH refutation, GUE, a zeta-gap improvement or a sub-186 prime gap.


<a id="report-52"></a>

# Current report 52: Averaging the rational resonances: one power-saving extraction, and its retained main term

**Collection:** R13 — rational-core extraction and the signed CRT remainder.

**Source:** [research/dyson/round13/phase-resonance/AVERAGED_RATIONAL_PHASE_TEST.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/phase-resonance/AVERAGED_RATIONAL_PHASE_TEST.md).

**SHA-256:** `7f4285cb02241e22bdb29a1ad4952f7ab8249e3ec3bef984455a57ae05e41ebb`. **Git blob:** `5e5d74961452f7f7bd53ec8b59ef1bb0157ba7ef`. **Original bytes:** 20890.

## Averaging the rational resonances: one power-saving extraction, and its retained main term

Date: 2026-09-05. Status: ordinary analytic bounds for an explicitly defined terminal Type II component. The extraction in Section 3 assumes RH for the Riemann zeta function. The counting, lower bound and minor-arc comparison do not. No improved bound for the complete actual-zeta covariance is proved.

The bad phases from Round 12 occupy a small fraction of the longer coefficient interval. That observation alone does not make them negligible. This note proves three quantitative statements at the actual scales:

- The rational core around zero can be replaced by an explicit integral with total error \(O(X^{.923}\log^2X)\), after the actual top-conductor and low-numerator weights are summed, assuming RH.
- Its retained main term cannot uniformly be discarded by absolute estimates. An admissible prime-interval convolution with the actual complementary moduli has a positive restricted core of size at least a constant times \(X^{1.123}/\log^{348}X\).
- The primary-source Vaughan bound, applied legally on enlarged minor arcs, gives only logarithmic cancellation at the chosen polylogarithmic cutoff. An elementary mean square in the longer variable is stronger here, but still gives \(O(X^{1.323}\sqrt{\log X})\), which is weaker than the existing Round 11 bound for the original prime pairing.

Thus averaging repairs the pointwise perspective but does not yet remove the need for cancellation in the retained signed main terms.

### 1. Exact component, coefficients and natural unit restrictions

Write
\[
Q=X^{523/1000},\qquad M=X^{3/5},\qquad N=X^{2/5},
\qquad X^{1/6}\le H\le X^{2/7}.
\tag{1}
\]
Let \(\mathcal Q_X\) be the full canonical balanced complementary family fixed in Rounds 9–12, and let
\[
\mathcal D_X=\mathcal Q_X\cap(Q/2,Q].
\]
For completeness, the canonical family consists of distinct squarefree \(d=[D,E]>X^{1/2}\), with
\[
D,E\le X^{523/2000},
\quad p^{3/2}D_{\ge p}\le X^{501/2000},
\quad p^{3/2}E_{\ge p}\le X^{501/2000},
\tag{2}
\]
where each respective owner condition is imposed at \(p>X^{1/1000}\).
Its source complementary theorem proves triple dense divisibility. Every prime factor of \(d\) is at most \(X^{523/2000}<N\), because it divides one of the two roots.

Fix \(V\in C_c^\infty(1,2)\), and initially assume \(|\alpha_m|\le1\), supported on \(M\le m<2M\). Define
\[
P_N(\vartheta)=\sum_{\substack{N\le p<2N\\p\ {\rm prime}}}
(\log p)e(\vartheta p),\qquad
S_{V,H}(\beta)=\sum_hV(h/H)e(-\beta h),
\quad e(t)=e^{2\pi it}.
\tag{3}
\]
The inner prime support is fixed independently of \(m\). For a set \(\mathcal A\) of phases on the circle, put
\[
\begin{split}
\mathcal T(\mathcal A)=
\sum_{d\in\mathcal D_X}\frac{\mu(d)}d
\sum_{\substack{1\le a\le d/(16H)\\(a,d)=1}}
S_{V,H}(a/d)
\sum_{\substack{M\le m<2M\\(m,d)=1\\am/d\bmod1\in\mathcal A}}
\alpha_m
\left[P_N(am/d)-\frac{\mu(d)}{\varphi(d)}P_N(0)\right].
\end{split}
\tag{4}
\]
The main variable \(m\) is the longer convolution factor; it is not a prime variable by default.

Formula (4) is a genuine terminal-conductor slice of the completed shifted progression discrepancy for the source-allowed convolution
\[
F=\alpha*\beta,\qquad
\beta(n)=(\log n)1_{\{n\ {\rm prime},\,N\le n<2N\}}.
\]
The source prime-interval Siegel–Walfisz statement, followed by partial summation, gives its required shorter-coefficient property. The scales and source parameters were checked in Round 12. This does not assert that an arbitrarily chosen \(\alpha\) is one specific factor in the actual zeta decomposition.

The mask \((m,d)=1\) in (4) is essential. All supported \(n\)-primes are units modulo \(d\), by (2). In the original progression and principal sums, primitive shifts therefore restrict the product to \((m,d)=1\). After this restriction, Fourier completion gives
\[
\frac1d\sum_{a\bmod d}S_{V,H}(a/d)
\left[
\sum_{\substack{m,n\\(mn,d)=1}}\alpha_m\beta_n e(amn/d)
-\frac{c_d(a)}{\varphi(d)}
\sum_{\substack{m,n\\(mn,d)=1}}\alpha_m\beta_n
\right],
\tag{5}
\]
where \(c_d\) is the Ramanujan sum. For \((a,d)=1\) and squarefree \(d\), \(c_d(a)=\mu(d)\), exactly as used in (4).
The full-signed-family conductor coefficient is \(\mu(d)/d\) here: no other multiple of \(d>Q/2\) fits below \(Q\). Nonprimitive Fourier numerators and all other conductors remain outside this slice.

The estimates below use the actual \(S_{V,H}\), without replacing it by a fictitious positive weight. For upper bounds, the elementary facts
\[
|S_{V,H}(\beta)|\ll_V H,\qquad
\sum_{\substack{1\le a\le d/(16H)\\(a,d)=1}}
\frac{|S_{V,H}(a/d)|}{d}\ll_V1
\tag{6}
\]
are sufficient. Summing (6) over \(\mathcal D_X\) costs at most \(O_V(Q)\).

For a fixed divisor-bounded outer family, one may multiply all the following upper bounds by \(O_\eta(X^\eta)\) for any fixed \(\eta>0\), including its prescribed logarithmic factors in a slightly larger \(\eta\). This follows from the pointwise divisor bound and is deliberately conservative. In particular, the extraction in Section 3 still has a power saving whenever \(\eta<77/1000\). The lower-bound witness uses \(\alpha_m=1\).

### 2. Exact residue counts for sparse resonances

Let \(\mathcal A\) be a disjoint union of \(J\) circular intervals with total length \(|\mathcal A|\). For a unit \(a\bmod d\), multiplication by \(a\) permutes the residue classes. Each class occurs in \([M,2M)\) at most \(M/d+1\) times. Counting grid points of spacing \(1/d\) in each interval gives
\[
\#\{M\le m<2M:am/d\bmod1\in\mathcal A\}
\le (M/d+1)\bigl(d|\mathcal A|+2J\bigr).
\tag{7}
\]
The estimate remains an upper bound after imposing \((m,d)=1\). No distribution theorem about the inverses of residues is needed.

Set \(R=(\log X)^B\), for fixed \(B>0\). The fixed-width cores around all reduced rationals of denominator \(q\le R\),
\[
\left\{\vartheta:\|\vartheta-b/q\|\le C/N\right\},
\qquad (b,q)=1,
\tag{8}
\]
are disjoint for sufficiently large \(X\), with the usual single rational \(0/1\). They have \(J\ll R^2\), total length \(O_C(R^2/N)\). Consequently their bad-\(m\) count, for each \(d,a\), is
\[
\ll_C (M+d)\left(\frac{R^2}{N}+\frac{R^2}{d}\right)
\ll_C \frac{MR^2}{N}.
\tag{9}
\]
Here \(M/d\gg X^{.077}\) and \(d/N\gg X^{.123}\), so the last simplification is uniform. The exceptional proportion is \(O(R^2/N)\), genuinely small.

For legal use of Dirichlet approximation on the complement, use the enlarged arcs
\[
\mathfrak M(R)=
\bigcup_{\substack{q\le R\\(b,q)=1}}
\left\{\vartheta:\|\vartheta-b/q\|
\le\frac{2R}{qN}\right\}.
\tag{10}
\]
They too are disjoint eventually. Their total length is
\[
\ll\frac RN\sum_{q\le R}\frac{\varphi(q)}q
\ll \frac{R^2}{N},
\]
and their number is \(O(R^2)\). Thus the same coarse count (9) holds. The enlargement does not worsen its logarithmic scale, but is needed for the minor-arc denominator conclusion in Section 6.

### 3. RH extraction of the zero-rational core with a power-saving total error

Fix \(C>0\), and let
\[
\mathcal A_0(C)=\{\vartheta:\|\vartheta\|\le C/N\}.
\]
Use the unique representative \(\vartheta\in[-C/N,C/N]\), and define the explicit continuous main term
\[
J_N(\vartheta)=\int_N^{2N}e(\vartheta u)\,du,
\qquad J_N(0)=N.
\tag{11}
\]
When \(\vartheta\ne0\), this is
\((e(2N\vartheta)-e(N\vartheta))/(2\pi i\vartheta)\).

Assume RH for \(\zeta\). The RH prime-number estimate
\(\theta(x)=x+O(\sqrt x\log^2x)\), with \(\theta(x)=\sum_{p\le x}\log p\),
follows, for example, from Schoenfeld's explicit Theorem 10, equation (6.3),
printed p.337 of [Sharper bounds for the Chebyshev functions theta(x) and psi(x), II](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf).
One partial summation gives, uniformly on this core,
\[
P_N(\vartheta)=J_N(\vartheta)+O_C(\sqrt N\log^2N).
\tag{12}
\]
Indeed the endpoint errors are \(O(\sqrt N\log^2N)\), while the differentiated exponential has total variation \(O(|\vartheta|N)=O_C(1)\). Endpoint choices \(<\) versus \(\le\) contribute at most \(O(\log N)\), already covered. Only the ordinary zeta RH is used for (12).

Let \(\mathcal J_0(C)\) be exactly (4) on this core, with its square bracket replaced by
\[
J_N(\vartheta)-\frac{\mu(d)}{\varphi(d)}N.
\tag{13}
\]
Then
\[
\boxed{
\mathcal T(\mathcal A_0(C))-\mathcal J_0(C)
\ll_{C,V}\frac{QM}{\sqrt N}\log^2X
=X^{923/1000}O_{C,V}(\log^2X).
}
\tag{14}
\]
To prove this, (7) bounds the number of core \(m\)'s by \(O_C(M/N)\) for each \(d,a\). The error in the centered bracket is at most
\((1+1/\varphi(d))O_C(\sqrt N\log^2N)\). Apply (6), and sum over at most \(Q\) conductors. This proves (14) without assuming cancellation of \(\alpha\), \(\mu(d)\) or \(S_{V,H}\).

An additional \(\log d\) conductor weight costs one logarithm, so the error is still \(o(X\log X)\). Any extra fixed logarithmic coefficient loss is likewise harmless for this positive exponent margin.

This is a proved, source-compatible arithmetic extraction for an identifiable phase component. It does not state that its main term \(\mathcal J_0\) is small. In particular, zero here describes the rational approximation to \(am/d\), not the deleted zero frequency of the original completion: \(a/d\ne0\) throughout (4).

### 4. The retained rational main is not uniformly negligible

Assume in this section that \(V\ge0\), \(m_V=\int V>0\), and choose the admissible outer sequence \(\alpha_m=1\) on \([M,2M)\).
Use the actual Round 11 subfamily \(\mathcal F_X\subset\mathcal D_X\) of products of two large and 346 small primes. It has
\[
|\mathcal F_X|\ge\frac{c_0Q}{2(\log X)^{348}},\quad
\mu(d)=1,\quad
\sum_{p\mid d}\frac1p
\le\frac{348}{\lambda X^\kappa}=o(1),
\tag{15}
\]
where
\[
\kappa=\frac{343}{346000},\quad
\lambda=2^{-1/348},\quad
c_0=\frac{(1-\lambda)^{348}}
{2!\,346!\,(9/100)^2\kappa^{346}}.
\]
All assertions hold for every sufficiently large real \(X\), uniformly in the specified \(H\)-range.

For each unit \(a\bmod d\), consider just the positive core
\[
1\le s\le\frac{d}{32N},\qquad
s\equiv am\pmod d,\qquad(s,d)=1.
\tag{16}
\]
The same elementary excluded-prime count used in Round 11 shows that (16) has at least \(d/(64N)\) possible residues \(s\), once \(X\) is large. The interval length \(d/(32N)\) tends to infinity, and its nonunits number at most that length times \(\sum_{p\mid d}1/p\), apart from the harmless endpoint unit count.
Every such residue gives at least \(M/(2d)\) representatives \(m\in[M,2M)\), because \(M/d\to\infty\). Thus there are at least
\[
\frac{M}{128N}
\tag{17}
\]
unit \(m\)'s in this positive core, for every allowed \(d,a\).

Now keep only actual low unit numerators \(1\le a\le d/(16H)\).
For \(h\) in the support of \(V(h/H)\), a prime \(p\in[N,2N)\), and \(m\) from (16),
\[
0<sp/d\le1/16,\qquad 0<ah/d<1/8.
\]
The phase of each product term \(e(sp/d-ah/d)\) is therefore between
\(-\pi/4\) and \(\pi/8\). Its real part is at least \(1/2\). Writing
\(S_0=\sum_hV(h/H)\), this gives
\[
\Re\!\left[
S_{V,H}(a/d)
\left(P_N(am/d)-\frac{P_N(0)}{\varphi(d)}\right)
\right]
\ge\left(\frac12-\frac1{\varphi(d)}\right)S_0P_N(0).
\tag{18}
\]
Eventually \(\varphi(d)\ge4\), \(S_0\ge m_VH/2\), and
\(P_N(0)\ge N/2\), the last inequality using the ordinary prime number theorem. Thus each centered term, after the coefficient \(1/d\), has real part at least
\[
\frac{m_VHN}{16d}.
\tag{19}
\]
This explicitly retains the primitive Ramanujan principal term; it has not been omitted to force positivity.

Round 11 supplies at least \(d/(32H)\) such primitive \(a\)'s for each \(d\in\mathcal F_X\). Combining (15), (17) and (19), the restricted positive-core contribution satisfies
\[
\boxed{
\Re\,\mathcal T_{\mathcal F_X}(\mathcal A_0^+)
\ge
\frac{c_0m_V}{131072}
\frac{QM}{(\log X)^{348}},
\qquad
\mathcal A_0^+=(0,1/(32N)].
}
\tag{20}
\]
Its power is \(QM=X^{1123/1000}\). Consequently it exceeds \(X\log X\) by an unbounded factor eventually, even with the displayed fixed logarithmic denominator. Equation (14), applied to this restricted positive core by the same proof, shows that the corresponding explicit integral main term has the same lower bound with a smaller fixed constant under RH.

This is an obstruction to treating all resonant slices as negligible by an absolute estimate uniformly over source-allowed coefficients. It is **not** a lower bound for the full signed family, for all rational cores combined, or for the coefficient sequence arising in one particular zeta or Heath–Brown decomposition. Cancellation against other conductors, other phases, or actual outer coefficients is still possible. The lower bound uses real primes and the actual arithmetic support, not a free choice of artificial Fourier locations.

### 5. Other small rational denominators: explicit main terms, but only logarithmic extraction from SW

For \(q\le R\), \((b,q)=1\), and
\(\vartheta=b/q+\xi\) in the enlarged arc (10), the ordinary Siegel–Walfisz theorem and partial summation give, for every fixed \(A>0\),
\[
P_N(b/q+\xi)
=\frac{\mu(q)}{\varphi(q)}J_N(\xi)
+O_{A,B}(N(\log X)^{-A}).
\tag{21}
\]
This includes the genuine-prime weights and both interval endpoints. To see the coefficient, sum the progression main terms against \(e(bc/q)\) over unit classes \(c\bmod q\); their sum is \(c_q(b)=\mu(q)\). All supported primes exceed \(q\). The costs of at most \(q\) classes and variation \(O(1+|\xi|N)\le O(1+2R)\) are fixed logarithmic powers, absorbed by choosing the source SW order larger. The finite source parameter \(B\) stays fixed.

Replacing the inner bracket in (4) accordingly, including replacement of \(P_N(0)\), defines an explicit finite rational-main expression on \(\mathfrak M(R)\). Its total extraction error is bounded by
\[
O_{A,B,V}\!\left(QM(\log X)^{-A}\right),
\tag{22}
\]
because (9) and (6) sum the inner \(N\log^{-A-2B}X\) error.
This bound by itself is insufficient for \(o(X\log X)\): \(QM=X^{1.123}\), and a fixed arbitrary logarithmic saving does not defeat its extra power.

An absolute bound for the retained oscillatory rational main is
\[
O_{B,V}(QMR).
\tag{23}
\]
For the fixed-width cores (8), count \(O(M/N)\) \(m\)'s per rational, use \(|J_N|\le N\), and sum the \(1/\varphi(q)\) main coefficient over the \(\varphi(q)\) reduced numerators. This costs \(O(M)\) per denominator.
For the enlarged arcs, the same order follows from
\[
|J_N(\xi)|\ll\min(N,|\xi|^{-1}).
\]
On the \(1/d\) phase grid, summing this bound within distance \(2R/(qN)\) of a fixed rational costs
\[
O\!\left(N+d\log(4R/q)\right).
\]
Each residue is repeated at most \(M/d+1\ll M/d\) times. After the \(1/\varphi(q)\) coefficient and its \(\varphi(q)\) numerators are summed, the total is
\[
O\!\left(M\sum_{q\le R}
\left[\log(4R/q)+N/d\right]\right)=O(MR),
\]
uniformly for \(d\asymp Q\). Then (6) gives (23).
The separate primitive principal term is retained; its absolute value on all \(m\), and hence on these arcs, is at most \(O_V(X\log X)\), as in Section 6.

Ordinary zeta RH does not imply the analogous square-root progression error for all \(q>1\). Assuming RH for the corresponding Dirichlet \(L\)-functions would change (22), but that is an additional assumption and is not used here. No failure of the desired actual average is inferred merely from the insufficiency of (22).

### 6. A legal minor-arc bound, and the stronger elementary average in \(m\)

The primary source for the pointwise estimate is Montgomery–Vaughan,
[*Multiplicative Number Theory II: Primes and Sieves*](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf),
author-hosted draft, Theorem 17.1, equation (17.29),
printed p.65 (PDF page 77). It states that, when \((b,q)=1\) and
\(|\vartheta-b/q|\le q^{-2}\),
\[
\left|\sum_{n\le Y}\Lambda(n)e(\vartheta n)\right|
\ll\left(\frac{Y}{\sqrt q}+Y^{4/5}+\sqrt{Yq}\right)
(\log Y)^{5/2}.
\tag{24}
\]
Taking the difference of prefixes at \(N,2N\), and subtracting the prime-power terms of size \(O(\sqrt N\log^2N)\), proves the same bound for \(P_N\), with \(Y\) replaced by \(N\) up to absolute constants.

For \(\vartheta\notin\mathfrak M(R)\), set \(D_0=\lfloor N/R\rfloor\).
For sufficiently large \(X\), \(D_0\ge N/(2R)\). Dirichlet approximation
with this integer cutoff supplies
\[
R<q\le D_0\le N/R,\qquad
|\vartheta-b/q|\le (qD_0)^{-1}\le q^{-2}.
\]
Indeed \(q\le R\) would place the phase inside (10), since
\((qD_0)^{-1}\le2R/(qN)\).
Therefore (24) applies legally and gives
\[
|P_N(\vartheta)|
\ll\left(NR^{-1/2}+N^{4/5}\right)(\log N)^{5/2}.
\tag{25}
\]
The complement of the fixed-width cores (8) alone does not imply \(q>R\); small denominators may still have approximation error between \(C/N\) and \(2R/(qN)\). That is why (10) was introduced.

Using (6), summing the longer variable absolutely, and keeping the primitive
principal term separately, yields the following bound. The latter term costs
at most \(O_V(MN\sum_{d\le Q}1/\varphi(d))=O_V(X\log X)\), by the
elementary reciprocal-totient estimate.
\[
|\mathcal T(\mathfrak M(R)^c)|
\ll_V
QM\left(NR^{-1/2}+N^{4/5}\right)(\log N)^{5/2}
+X\log X.
\tag{26}
\]
At polylogarithmic \(R\), its leading power is \(QMN=X^{1.523}\); only logarithms are saved. This is not a useful improvement over Round 11.

There is a stronger unconditional averaged estimate that uses the fixed inner coefficients. Since \(2N<d\) eventually, no two supported primes are congruent modulo \(d\). For any unit \(a\bmod d\), complete-period orthogonality gives
\[
\begin{split}
\sum_{M\le m<2M}|P_N(am/d)|^2
&\le(M/d+1)\sum_{r\bmod d}|P_N(r/d)|^2\\
&=(M+d)\sum_{N\le p<2N}(\log p)^2\\
&\ll (M+d)N\log N.
\end{split}
\tag{27}
\]
One can retain the centering exactly, rather than paying for it separately.
Every supported prime is a unit modulo \(d\), so the Ramanujan identity gives
\[
\frac1{\varphi(d)}\sum_{r\bmod d}^{*}P_N(r/d)
=\frac{\mu(d)}{\varphi(d)}P_N(0)=:c_d.
\]
Consequently the exact centered unit variance is
\[
\sum_{r\bmod d}^{*}|P_N(r/d)-c_d|^2
=\sum_{r\bmod d}^{*}|P_N(r/d)|^2
-\frac{|P_N(0)|^2}{\varphi(d)}
\le d\sum_{N\le p<2N}(\log p)^2.
\tag{28}
\]
Multiplication by a unit \(a\) permutes these unit residues. Splitting the
longer interval into residue periods, restricting its nonnegative squared
sum to the minor arcs, and applying Cauchy–Schwarz therefore proves
\[
\sum_{\substack{M\le m<2M\\(m,d)=1\\am/d\notin\mathfrak M(R)}}
|\alpha_m(P_N(am/d)-c_d)|
\ll M\sqrt{N\log N}.
\tag{29}
\]
This exact variance calculation was independently pointed out in the
minor-arc source audit. It requires the fixed inner support and coefficients;
it is not a formal consequence for arbitrary \(m\)-dependent inner sums.
Thus (6) and (29) give
\[
\boxed{
|\mathcal T(\mathfrak M(R)^c)|
\ll_V QM\sqrt{N\log N}
=O_V\!\left(X^{1323/1000}\sqrt{\log X}\right).
}
\tag{30}
\]
This saves a power \(X^{.2}\) relative to the absolute \(QMN\) bound, but it is still insufficient at scale \(X\log X\), and still worse than the existing \(X^{1.023}\log^5X\) estimate for the original completed prime polynomial. A bound for this factored test must not be presented as an improvement to that existing estimate.

### 7. Bounded conclusion and source record

The useful positive statement from this test is (14): ordinary RH extracts the zero-rational core with an error already below the required arithmetic scale, even after the actual weights are summed. Its explicit main term remains part of the problem.

The precise limitation is (20), together with (22) and (30): sparse resonances can retain a power-large main contribution on an admissible arithmetic block; the remaining available minor-arc estimates do not bound the whole factored pairing at the required scale. Any next advance through this route must exploit the actual outer coefficients and signs when handling those retained main terms or use a stronger joint estimate. No generic claim that such cancellation is impossible is justified by this note.

The source paper is [OpenAI, *Improved short gaps between primes*](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf): Proposition 2.3 pp.4–5 supplies the complementary moduli; Proposition 2.10 p.7 supplies prime-interval SW; Definition 2.9 p.6 specifies its normalization; Proposition 2.18 pp.10–11 supplies the legal Type II scales. The R12 report pins and checks these exact hypotheses. The primary Montgomery–Vaughan PDF SHA-256 is
72448ec23158a3aeee534c9cde633d5402f916d0367b4f320212cd7ad179d340.
The companion source audit records the downloaded copy and printed-page check.

The adjacent exact script checks the rational exponents, finite Fourier completion with the natural unit mask, residue-count bounds, and all lower-bound constants. It does not numerically search for large primes, approximate the asymptotic threshold, or substitute a finite toy modulus for the canonical-family proof. This note and all checks are new R13 files; prior rounds remain frozen.


<a id="report-53"></a>

# Current report 53: Round 13 — Genuine-prime minor arcs and a fixed-inner-interval averaging audit

**Collection:** R13 — rational-core extraction and the signed CRT remainder.

**Source:** [research/dyson/round13/minor-arc-source/MINOR_ARC_AND_FIXED_INTERVAL_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/minor-arc-source/MINOR_ARC_AND_FIXED_INTERVAL_AUDIT.md).

**SHA-256:** `bbdb17478b9e885570b7b49c3ff9b94b0ceb98f12a41743edb1ce492cb50edc4`. **Git blob:** `ef97aa38a8c9de57b7d032e54121e0b903118f92`. **Original bytes:** 11180.

## Round 13 — Genuine-prime minor arcs and a fixed-inner-interval averaging audit

Status: completed ordinary mathematical source/proof audit, not a numerical enclosure or a theorem about zeta pair correlation. This note records the source theorem, the necessary major-arc coverage correction, and exactly what the current arithmetic packet permits. No new parameter scan was run.

### 1. Objects and the primary minor-arc theorem

Write \(e(u)=\exp(2\pi i u)\), and let
\[
P_N(\alpha)=\sum_{N\le p<2N}(\log p)e(\alpha p),
\qquad M\asymp X^{3/5},\quad N\asymp X^{2/5},\quad Q=X^{523/1000}.
\]
The inner support is fixed independently of the integer \(m\in I_M\), where \(I_M\) is an interval containing \(M+O(1)\) consecutive integers. The current outer coefficients initially satisfy \(|\alpha_m|\le1\). Extra divisor/logarithmic weights must be charged through their actual norms.

**Source theorem.** Montgomery and Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, author-hosted manuscript, Theorem 17.1, equation (17.29), printed page 65 (PDF page 77, zero-based index 76), states that, for coprime integers \(a,q\), \(q\ge1\), and
\[
|\alpha-a/q|\le q^{-2},
\]
\[
\left|\sum_{n\le Y}\Lambda(n)e(\alpha n)\right|
\ll \left(Yq^{-1/2}+Y^{4/5}+Y^{1/2}q^{1/2}\right)(\log Y)^{5/2}.
\tag{1}
\]
Definition (17.28) is explicitly the von Mangoldt prefix, not an arbitrarily twisted coefficient sequence. The proof on printed pages 65–66 chooses the Vaughan parameters \(U=V=Y^{2/5}\). It explicitly says that \(q>Y\) gives a bound weaker than the trivial estimate. Thus no usable \(q\le Y\) restriction should be silently imported into an application whose exact denominator exceeds \(Y\).

Primary source: [author-hosted Montgomery–Vaughan manuscript](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf). The version and local SHA256 are recorded in `sources/receipt.json`; this is a manuscript source, not a claim about publication status or the strongest possible modern estimate.

Taking two prefixes, and subtracting the prime powers, gives
\[
|P_N(\alpha)|\ll B_N(q),\qquad
B_N(q)=\left(Nq^{-1/2}+N^{4/5}+\sqrt{Nq}\right)(\log(2N))^{5/2}.
\tag{2}
\]
Indeed, the discarded powers contribute at most
\(\sum_{k\ge2,p^k\le2N}\log p\ll\sqrt N\log^2(2N)\), which is absorbed by (2). No RH is used here.

If \(w\) is of bounded variation on \([N,2N]\), partial summation gives the uniform weighted version
\[
\left|\sum_{N\le p<2N}(\log p)w(p)e(\alpha p)\right|
\ll \bigl(\|w\|_\infty+\operatorname{Var}(w)\bigr)B_N(q).
\tag{3}
\]
The same rational approximation applies to every prefix with endpoint between \(N\) and \(2N\), so there is no interval-uniformity gap. Smooth scaled weights \(w(p/N)\) have a constant depending on their fixed variation norm. Unweighted prime sums follow by replacing \(w(x)\) with \(w(x)/\log x\), which costs \(O(1/\log N)\). Uniform variation suffices for this pointwise statement even if the weight depends on \(m\); it does not, by itself, establish the fixed-coefficient orthogonality argument in Section 3.

### 2. The required major arcs, and an obstruction to narrower coverage

Let \(R=(\log X)^B\), with fixed \(B>0\), and take \(X\) large enough that \(2\le R\le\sqrt N\). Put
\[
\mathfrak M_R=\bigcup_{1\le q\le R}\ \bigcup_{(a,q)=1}
\left\{\alpha\pmod1:\left\|\alpha-a/q\right\|\le\frac{2R}{qN}\right\}.
\tag{4}
\]
The harmless factor 2 accommodates floors. Dirichlet approximation with denominator cap \(K=\lfloor N/R\rfloor\) gives coprime \(a,q\), \(q\le K\), and
\[
|\alpha-a/q|\le\frac1{qK}\le\frac{2R}{qN},
\qquad |\alpha-a/q|\le q^{-2}.
\]
Consequently, outside (4), \(R<q\le N/R\). Applying (2),
\[
|P_N(\alpha)|\ll
\left(NR^{-1/2}+N^{4/5}\right)(\log(2N))^{5/2}.
\tag{5}
\]
For any fixed desired logarithmic saving, a sufficiently large fixed \(B\) supplies it in this pointwise estimate.

It is incorrect to deduce this denominator range after deleting only neighborhoods \(|\alpha-a/q|\le C/N\), with fixed \(C\), for \(q\le R\). The available Dirichlet error is \(O(R/(qN))\), which is larger for small \(q\). A concrete obstruction is \(\alpha=K_0/N\), where \(K_0>C\) is a fixed nonintegral number. For large \(N\), this is outside all those fixed-width cores: for \(q\ge2\), \(a/q\) is separated from zero by at least \(1/R\), much larger than \(1/N\). But the ordinary PNT and partial summation give
\[
P_N(K_0/N)=N\int_1^2e(K_0u)\,du+o(N),
\]
with nonzero integral. It is therefore not a minor arc with arbitrary logarithmic cancellation. Grid phases with denominator \(d\gg N\) approximate such a point within \(1/d=o(1/N)\), so the issue also occurs in the sampled setting.

The coverage repair does **not** worsen the coarse bad-point count already contemplated. The total length of (4) is
\[
\ll\frac R N\sum_{q\le R}\frac{\varphi(q)}q\ll\frac{R^2}N,
\]
and the number of constituent circular intervals is \(O(R^2)\). For any reduced \(a/d\), multiplication by \(a\) permutes the grid of \(d\) residues. Counting complete periods and enlarging the final incomplete period yields
\[
\#\{m\in I_M:am/d\in\mathfrak M_R\}
\ll(M+d)\left(\frac{R^2}N+\frac{R^2}d\right).
\tag{6}
\]
Restriction to \((m,d)=1\) only decreases this count. The interval-count term in (6) must be retained before using the actual \(d>N\) range.

### 3. A stronger exact average at \(a=1\), including the natural centering

Let \(d>N\), and let \(b_n\) be any fixed coefficients supported in an integer interval of diameter less than \(d\). Orthogonality gives the exact identity
\[
\sum_{r\bmod d}\left|\sum_n b_ne(rn/d)\right|^2=d\sum_n|b_n|^2.
\tag{7}
\]
Completing successive periods of an arbitrary interval \(I_M\), using nonnegativity for its incomplete period, gives
\[
\sum_{m\in I_M}\left|\sum_n b_ne(mn/d)\right|^2
\le (\lfloor |I_M|/d\rfloor+1)d\sum_n|b_n|^2
\ll(M+d)\sum_n|b_n|^2.
\tag{8}
\]
For log-prime coefficients, Chebyshev's estimate gives
\(\sum_{N\le p<2N}(\log p)^2\ll N\log N\). Hence
\[
\sum_{m\in I_M}|P_N(m/d)|\ll\sqrt{M(M+d)N\log N}.
\tag{9}
\]
Here \(M>d\), so this is \(\ll M\sqrt{N\log N}\), with power \(X^{4/5}\). No minor-arc theorem is needed for this average. For general outer coefficients replace (9) by
\[
\left|\sum_m\alpha_mP_N(m/d)\right|
\ll\|\alpha\|_2\sqrt{(M+d)N\log N}.
\tag{10}
\]
This remains valid for every \((a,d)=1\) in place of 1.

The actual terminal expression has a unit mask and a principal centering. Suppose \(d\) is squarefree and all supported \(n\) are coprime to \(d\). Then the Ramanujan identity gives
\[
\frac1{\varphi(d)}\sum_{r\bmod d}^{*}\sum_n b_ne(rn/d)
=\frac{\mu(d)}{\varphi(d)}\sum_n b_n.
\]
Subtracting this exact unit-average constant decreases the unit mean square:
\[
\sum_{r\bmod d}^{*}\left|\sum_n b_ne(rn/d)-
\frac{\mu(d)}{\varphi(d)}\sum_n b_n\right|^2
=\sum_{r\bmod d}^{*}\left|\sum_n b_ne(rn/d)\right|^2
-\frac{|\sum_n b_n|^2}{\varphi(d)}
\le d\sum_n|b_n|^2.
\tag{11}
\]
Thus (8)–(10) also control the centered terminal sum restricted to \((m,d)=1\), without an added centering debt. In the current canonical conductor family every prime factor of \(d\) is \(\le X^{0.2615}<N\), so the required unit condition holds for every inner prime.

This calculation is strictly about fixed inner coefficients/support. A smooth product weight may be transferred through an explicitly summable separable expansion, with the sum of its coefficient norms charged. It is not permission to absorb \(e(amn/d)\) into arbitrary coefficients and then invoke Siegel–Walfisz. Arbitrary \(m\)-dependent phase absorption invalidates that inference.

For the top-conductor packet \(Q/2<d\le Q\), its exact conductor coefficient is \(M_d=\mu(d)/d\), the low reduced numerators satisfy \(a\le d/(16H)\), and \(|S_V(a/d)|\ll_V H\). Summing (9) absolutely over these indices gives only
\[
\sum_{d\asymp Q}\frac H d\frac d H\,
O\bigl(M\sqrt{N\log N}\bigr)
\ll Q M\sqrt{N\log N}=X^{1.323}(\log X)^{1/2}.
\tag{12}
\]
The coarse enlarged-major-arc count (6), followed by the trivial prime-sum bound, instead gives \(\ll QM R^2\) on those arcs. Neither bound is \(o(X\log X)\). There is a genuine averaging improvement for each fixed conductor/frequency; it does not yet give the required full arithmetic pairing improvement.

### 4. The \(q=1\) core has an RH square-root remainder

Schoenfeld's *Sharper bounds for the Chebyshev functions \(\theta(x)\) and \(\psi(x)\). II*, Theorem 10, equation (6.3), printed page 337, proves under RH
\[
|\theta(x)-x|<\frac1{8\pi}\sqrt x\log^2x\qquad(x\ge599).
\tag{13}
\]
Primary source: [AMS original paper](https://www.ams.org/journals/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf). The publisher PDF was downloaded directly and its first page read. Endpoint changes in the chosen half-open prime interval contribute at most \(O(\log N)\), already absorbed below.

Let \(\beta\) be the representative of \(am/d\pmod1\) with \(|\beta|\le C/N\), for fixed \(C\). Partial summation of (13) gives
\[
P_N(\beta)=J_N(\beta)+O\bigl((1+N|\beta|)\sqrt N\log^2N\bigr),
\qquad J_N(\beta)=\int_N^{2N}e(\beta u)\,du.
\tag{14}
\]
The error follows from two endpoint errors and
\(2\pi|\beta|\int_N^{2N}|\theta(u)-u|\,du\); this states the precise frequency uniformity. Fixed BV weights have the analogous variation cost.

For the centered terminal sum one can keep
\[
J_N(\beta)-\frac{\mu(d)}{\varphi(d)}P_N(0)
\]
as the explicit main term, retaining the principal term exactly. Alternatively \(P_N(0)=N+O(\sqrt N\log^2N)\) by RH, with a smaller additional error after division by \(\varphi(d)\).

The number of core \(m\)'s is
\[
\ll_C(M+d)(1/N+1/d).
\]
Combining this count with the same low-numerator and conductor weights as in (12), the total absolute remainder in (14) is at most
\[
\ll_{C,V}Q(M+Q)\sqrt N(1/N+1/Q)\log^2N
\ll_{C,V}\frac{QM}{\sqrt N}\log^2X
=X^{0.923}\,O_{C,V}(\log^2X).
\tag{15}
\]
This is a valid power-saving extraction for this identifiable component, initially with \(|\alpha_m|\le1\). It does not bound the explicit major main term, does not cover the enlarged \(q=1\) core uniformly in a growing \(C\) without paying the factor in (14), and does not transfer automatically to small \(q>1\). Square-root prime-AP errors at those other rationals require corresponding Dirichlet-L information; ordinary zeta RH does not provide it.

### 5. Accepted result and remaining obligation

The exact minor-arc theorem is applicable after the enlarged rational neighborhoods (4) are used. The fixed-inner-interval average is stronger than its pointwise application here, and the true unit mask/principal centering cause no loss by (11). The \(q=1\) component admits the rigorously small remainder (15), with its main term retained.

The missing step is cancellation in the actual weighted sum over conductors, reduced numerators, and the extracted arithmetic main terms. The estimates above neither prove such cancellation nor a zeta pair-correlation improvement. No claim is made for a coefficient sequence with an absorbed oscillatory phase, for unspecified product-weight separation, for arbitrary outer divisor coefficients at unit cost, or for the whole unsmoothed arithmetic packet.


<a id="report-54"></a>

# Current report 54: The signed kernel norm: exact main term and a large coherent CRT remainder

**Collection:** R13 — rational-core extraction and the signed CRT remainder.

**Source:** [research/dyson/round13/signed-kernel/SMOOTH_SIGNED_KERNEL_NORM.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/signed-kernel/SMOOTH_SIGNED_KERNEL_NORM.md).

**SHA-256:** `1105564835c925b818daf7198186e77c4f0f1ad4ac1001ee1bb50c0f5c7544d9`. **Git blob:** `ed4749d4c65bbe050d4496963ebd61a6b1022bc3`. **Original bytes:** 13904.

## The signed kernel norm: exact main term and a large coherent CRT remainder

Date: 2026-09-05. Status: ordinary proof draft, independent review pending. No stronger actual-prime upper bound is claimed. The finite-kernel identities and estimates here require no RH assumption; the comparison with the Round 11 prime-specific bound retains that bound's RH hypothesis.

This task derives the exact smooth-window main term for the unrestricted dual norm retained in Round 12, bounds its remainder at the currently available scale, and isolates a positive part of that actual signed remainder of size

    >> Q^2 H/(log X)^696, Q=X^.523,

on the full canonical source-supported family. Other signed terms may cancel it. Thus it is not a lower bound for the complete norm or a prime obstruction. It proves that the dangerous long-period CRT interactions really occur in the permitted support and require quantitative cancellation if one wants a smaller norm bound.

The currently proved upper bound remains

    sum_n W(n/X)|K(n)|^2 <<_(v,W) (X+Q^2)H log^4 X.       (1)

This does not improve the Round 11 prime-specific small-arc estimate. Even an ideal evaluation by the full-period main term would generally be too large for unrestricted-coefficient Cauchy–Schwarz to replace that estimate.

### 1. Exact finite kernel and its mean

Fix X large, X^(1/6)<=H<=X^(2/7), Q=X^(523/1000), a squarefree family Q_X contained in (sqrt(X),Q], and a fixed real v in C_c^infinity(1,2). Write v_h=v(h/H), and define

    V0=sum_h v_h,
    U_q=sum_((h,q)=1) v_h,
    B_q(n)=sum_(h=n mod q) v_h,
    b_q=U_q/phi(q),
    K(n)=sum_(q in Q_X) mu(q)[B_q(n)-b_q].                (2)

Take a fixed nonnegative nonzero W in C_c^infinity(1,3/2), with Fourier convention

    W_hat(t)=integral W(u)e(-tu)du, w0=W_hat(0)>0.

The norm to be estimated is N_W=sum_n W(n/X)|K(n)|^2. The coefficients in K are exactly those in Round 12. For a genuine prime n near X it is the actual completed residue discrepancy. For nonunit composite n it is the unrestricted Fourier-defined dual kernel; that distinction is not suppressed.

Define the full-period mean

    M=sum_q mu(q)[V0/q-b_q].                              (3)

The reduced-frequency representation is

    K(n)=M+sum_beta C_beta e(n beta),
    C_(a/d)=S_v(a/d) A_d,
    A_d=sum_(q in Q_X,d|q) mu(q)/q,
    S_v(beta)=sum_h v_h e(-beta h),                        (4)

over all distinct reduced fractions 2<=d<=Q, 1<=a<d. In particular

    M=-sum_beta C_beta mu(d)/phi(d).

The Round 11 first-power shift estimate sum_a |S_v(a/d)|<<_v d and |A_d|<=(1+log(Q/d))/d give

    |M|<<_v log^2(2Q),
    C2:=sum_beta |C_beta|^2<<_v H log^3(2Q).               (5)

The primitive centering is therefore present. It is not assumed equal to the unrestricted mean V0/q for each modulus.

### 2. Exact CRT covariance and main term

For q1,q2 let g=gcd(q1,q2), L=lcm(q1,q2)=q1q2/g. Simultaneous congruences n=h1 mod q1 and n=h2 mod q2 are solvable precisely when h1=h2 mod g. When compatible, denote their unique residue modulo L by r(h1,h2).

The smooth count of that progression is exactly, by Poisson summation,

    sum_(n=r mod L) W(n/X)
       = X/L sum_(k in Z) W_hat(kX/L)e(kr/L).             (6)

The zero mode is Xw0/L. The covariance after subtracting the unrestricted means V0/q_i has full-period value

    Gamma(q1,q2)
       =[g sum_(h1=h2 mod g) v_h1 v_h2 - V0^2]/(q1q2).

Let

    R_v(g)=g sum_(h1=h2 mod g) v_h1 v_h2 - V0^2
           =sum_(r=1)^(g-1) |S_v(r/g)|^2 >=0.             (7)

Grouping these frequencies by their reduced denominators yields the exact identity

    sum_(q1,q2) mu(q1)mu(q2) R_v(gcd(q1,q2))/(q1q2)
          =sum_beta |C_beta|^2=C2.                        (8)

The left side retains the actual signs and common-divisor compatibility; its individual terms cannot be treated as independent congruences. The identity follows alternatively from orthogonality over a common period. It is not an asymptotic assertion about the X-window.

Consequently the exact main term for N_W is

    X w0 (M^2+C2).                                         (9)

All nonzero modes in (6), and the analogous single-modulus modes of the centering terms, constitute the remainder. The latter single-modulus modes have period at most Q=o(X), so their total is O_A(X^(-A)) for every fixed A, by smooth Poisson decay, with constants depending on finitely many derivatives of v,W. The same is true for the integer-period correction to sum_n W(n/X).

Thus

    N_W=Xw0(M^2+C2)+E_CRT+O_A(X^(-A)),                   (10)

where the explicit signed remainder is

    E_CRT=X sum_(q1,q2) mu(q1)mu(q2)/L
       sum_(k!=0) W_hat(kX/L)
       sum_(h1=h2 mod g) v_h1 v_h2 e(k r(h1,h2)/L).       (11)

This is an equality with a controlled smooth-window error; no assertion that E_CRT is negligible is made.

### 3. Only the small-common-divisor remainder survives at power scales

Choose the fixed cutoff G=X^(1/10). It lies strictly between Q^2/X=X^(23/500) and the least H=X^(1/6).

If g>=G, then

    L<=Q^2/G=X^(473/500), X/L>=X^(27/500).

The nonzero Poisson sum in (6) is therefore O_B((X/L)^(1-B)). There are at most Q^2 modulus pairs, and the absolute total h1,h2 weight is O_v(H^2). Choosing B sufficiently large for any requested A shows that the entire g>=G portion of (11) is O_A(X^(-A)). No cancellation or short-interval hypothesis is used for this removal.

The zero-mode covariance for g<G is also negligible. Since g/H<=X^(-1/15), (12)'s shift estimate from Round 11 gives, for each fixed J>=2,

    R_v(g)<<_(v,J) H^2(g/H)^(2J).

Here every nonzero r/g has distance at least 1/g from the integers, and summing r^(-2J) gives the displayed bound. Multiplying by X, using sum_(q<=Q)1/q<<log Q, and choosing J large proves that the g<G portion of the main covariance in (8) is O_A(X^(-A)). Thus the substantial full-period covariance comes from shared divisors larger than G, where the CRT averaging itself is harmless.

The problematic term is exactly

    E_small = the expression (11) restricted to gcd(q1,q2)<G,

and (10) remains true with E_small in place of E_CRT, up to O_A(X^(-A)). Small-gcd compatibility is not a reason to discard this term: it is precisely where the least common multiple can exceed X.

For comparison, the elementary finite-spacing bound on (4), applied on the support of W, proves

    N_W <<_(v,W) (X+Q^2 log(2Q))C2 + X M^2
          <<_(v,W) (X+Q^2)H log^4 X.

Combining this actual upper bound with (5), (9), and nonnegativity gives

    |E_small| <<_(v,W) (X+Q^2)H log^4 X.                  (12)

The current remainder bound exceeds the natural XH main scale by Q^2/X=X^.046, up to logarithms. The exact source root predicates have not supplied cancellation in (11).

### 4. The remainder contains actual small determinants

There is an equivalent and simpler frequency form of the remainder. By (4), smooth Poisson summation on n gives

    E_small
      = X sum_(beta!=gamma) C_beta conjugate(C_gamma)
                       W_hat(X(gamma-beta))
          + O_A(X^(-A)),                                  (13)

where all frequency differences are represented in (-1/2,1/2]; integer aliases away from this representative are negligible. Cross terms with M are negligible because every nonzero beta has distance at least 1/Q from the integers. Equal frequencies give exactly the main C2. For reduced denominators d1,d2, a common divisor at least G forces a nonzero frequency distance at least G/Q^2, so rapid Fourier decay independently makes those terms negligible. The gcd of reduced denominators is not silently identified with the gcd of arbitrary original moduli in (11). On the isolated top conductors used in Section 5, however, d_i=q_i exactly, so the identification there is legitimate.

To make the dangerous arithmetic ranges explicit, fix any small epsilon>0, for example epsilon=1/100. By rapid decay of W_hat and S_v, one may restrict (13), at a cost O_A(X^(-A)), to nonzero signed numerators r_i with

    beta=r1/d1, gamma=r2/d2,
    2<=d_i<=Q, gcd(r_i,d_i)=1,
    0<|r_i|<=X^epsilon d_i/H,
    0<|r2 d1-r1 d2|<=X^epsilon d1d2/X.                   (14)

The residues here are centered near the integers. Bounds are uniform after choosing sufficiently many fixed derivatives to absorb the polynomial number of terms. There are no terms with exactly one zero numerator in these ranges: its nonzero partner would have magnitude at least 1/Q, which exceeds X^epsilon/X. The determinant is divisible by gcd(d1,d2); its small nonzero size is the CRT resonance.

This is not a source-class distribution conclusion. The allowed-support predicates constrain prime factors of each modulus separately. They do not state cancellation in the signed determinant pairing (13)–(14). In fact the next section shows that such pairs are forced inside the full canonical support.

### 5. A positive coherent part of the actual signed Gram has the large scale

For this lower bound on a **part** of the remainder, specialize to the full canonical family and a fixed nonnegative nonzero v. Let m_v=integral v. The frozen Round 11–12 arithmetic construction supplies a set Omega_X of actual reduced frequencies such that

    Omega_X subset (0,1/(16H)],
    |Omega_X|>=c0 Q^2/[128H(log X)^348],
    d in (Q/2,Q], A_d=1/d,
    |C_beta|>=m_v H/(2sqrt(2)Q),
    arg C_beta in [-pi/4,0].                              (15)

The phase statement follows directly from v_h>=0 and H<h<2H: each term in S_v(beta) lies in that sector. The identity A_d=1/d holds in the full signed family, so it is not changed by other negative-Mobius moduli.

Partition the small arc into at most J<=8X/H cells of length at most 1/(100X), and let m_j be their actual occupations. Since |Omega_X|/J tends to infinity,

    sum_j m_j(m_j-1) >= |Omega_X|^2/J-|Omega_X|
       >= c0^2 Q^4/[262144 XH(log X)^696]                 (16)

for all sufficiently large X, uniformly in H. This counts ordered pairs of distinct actual frequencies in the same cell.

On each such pair, |X(gamma-beta)|<=1/100. In the integral for W_hat, u lies in (1,3/2), so the added phase has magnitude at most 3pi/100. Together with the coefficient phase difference at most pi/4, the total is at most 7pi/25<pi/3. Consequently

    Re[X C_beta conjugate(C_gamma)
                          W_hat(X(gamma-beta))]
         >= X w0 |C_beta C_gamma|/2
         >= X w0 m_v^2 H^2/(16Q^2).                      (17)

Let E_coherent be exactly the sub-sum of (13) over these ordered within-cell pairs, without any other terms. Equations (16)–(17) prove

    E_coherent >= c0^2 w0 m_v^2 Q^2 H
                       /[4194304(log X)^696].             (18)

This is an actual contribution with the actual merged coefficient signs; it is not obtained by replacing the full remainder by absolute values. Its definition is symmetric in beta,gamma and it is real.

Moreover, distinct fractions with denominators d1,d2 satisfy

    |beta-gamma|>=gcd(d1,d2)/(d1d2).

Every pair used in (18) therefore has

    gcd(d1,d2)<=Q^2/(100X)<G.                             (19)

Its reduced CRT period is at least 100X. Thus these are precisely nonzero long-period modes in the small-gcd region, not harmless diagonal or large-gcd contributions. The root support cannot make this region empty.

**Equation (18) is not a lower bound for E_small or N_W.** All remaining signed pairs define E_other=E_small-E_coherent and may cancel it. For example, a norm estimate N_W<<XH log^A X would force

    E_other=-E_coherent+O_(v,W,A)(XH log^max(A,4) X),       (20)

up to the negligible errors already stated. Since Q^2/X=X^.046 dominates log^(696+A) X, this would be cancellation at the scale of the coherent block. We have identified and quantified the missing cancellation, not proved that it is unavailable.

### 6. Why the unrestricted norm may be the wrong target

The full-period coefficient norm in (9) satisfies C2>>_v H/(log X)^348 on the canonical family, by Round 11, and C2<<_v H log^3 X. If one could show that the smooth-window remainder is small compared with this main term, the resulting unrestricted norm would therefore have size XH up to logarithmic powers.

Ordinary Cauchy–Schwarz against the genuine-prime coefficient vector, whose squared norm is O_f(X log X), would then only give Xsqrt(H) times logarithms. This is already worse in the present H range than the Round 11 prime-specific small-arc bound X^1.023 log^5 X. Reaching o(X log X) by unrestricted-coefficient Cauchy–Schwarz would instead require N_W=o(X log X), subject to matching a window majorizing the coefficient support. That is far below the natural full-period main scale.

This is a conditional scale comparison, not a proved lower bound for N_W: (11) may have negative signed contributions. It explains why evaluating the dual norm alone need not attack the desired prime correlation. A stronger argument may need the alignment of the actual prime vector with K, rather than its largest value on all coefficient vectors.

The bounded result is (10)–(12) together with the explicit actual coherent block (18). There is no new power-saving upper bound. The remaining obligation is a signed small-determinant/CRT correlation estimate, or a prime-specific pairing estimate that avoids the unrestricted norm. No root factorization, common-divisor independence or Mobius cancellation was assumed without proof.

### 7. Verification scope

The companion exact-arithmetic check verifies the CRT mean/covariance identities and finite-window remainder on one fixed small squarefree family, with all signs and primitive subtractions retained. It also checks the rational cutoff exponents and the coherent-block counting constants. These are algebraic checks, not a numerical realization of the asymptotic modulus family or evidence for the required cancellation. No parameter scan, numerical prime experiment, or previous-round edit was performed.


<a id="report-55"></a>

# Current report 55: Independent audit of the smooth signed-kernel norm

**Collection:** R13 — rational-core extraction and the signed CRT remainder.

**Source:** [research/dyson/round13/signed-kernel/INDEPENDENT_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/signed-kernel/INDEPENDENT_AUDIT.md).

**SHA-256:** `5ada6ceefda4f1df6435a992876ed1eee5fe567907c183fd3a6e193814c0a731`. **Git blob:** `32c316e4209a8baa431b2e52ef5246dcdc65e894`. **Original bytes:** 6833.

## Independent audit of the smooth signed-kernel norm

Date: 2026-09-05. Reviewer: Astra subagent `yau_flow`. Verdict: **accepted as an ordinary mathematical derivation, within its explicitly limited scope**. No correction to the author report is required by this review. In particular, the positive coherent block is not a lower bound for the complete signed remainder or the window norm.

Reviewed report: `SMOOTH_SIGNED_KERNEL_NORM.md`, SHA256 `1105564835c925b818daf7198186e77c4f0f1ad4ac1001ee1bb50c0f5c7544d9`. All author-manifest hashes and all five inherited source-receipt hashes were checked against the current files and matched. Author files and the manifest were preserved.

### Exact decomposition and centering

The unrestricted mean of \(B_q\) is \(V_0/q\), whereas its primitive subtraction is \(b_q=U_q/\varphi(q)\). Their difference is retained in \(M\); replacing one by the other would change the kernel. Fourier completion, followed by reducing each fraction, yields the stated \(C_{a/d}=S_v(a/d)\sum_{q:d\mid q}\mu(q)/q\). The Ramanujan ratio \(c_q(r)/\varphi(q)=\mu(d)/\varphi(d)\), with \(d=q/(q,r)\), verifies the separate displayed identity for \(M\).

For each pair of moduli, the CRT compatibility condition \(h_1\equiv h_2\pmod g\) and progression period \(L=q_1q_2/g\) are exact. With the specified negative-sign Fourier transform, the Poisson factor is correctly \(\widehat W(kX/L)e(kr/L)\). Expanding the primitive subtractions and then collecting zero modes gives exactly
\[
Xw_0(M^2+C_2).
\]
Finite Fourier orthogonality gives
\[
R_v(g)=g\sum_{h_1\equiv h_2\ (g)}v_{h_1}v_{h_2}-V_0^2
=\sum_{r=1}^{g-1}|S_v(r/g)|^2,
\]
and summing with the signed modulus coefficients gives \(C_2\), as stated. Real \(v\) is sufficient here; nonnegative \(v\) is only imposed later for the positive block.

The nonzero single-modulus and constant-window terms have periods at most \(Q=X^{.523}\) or 1. Their polynomially bounded total coefficients can be absorbed by arbitrarily rapid decay of the fixed smooth window, so the \(O_A(X^{-A})\) remainder in equation (10) is justified. The principal terms have not disappeared by assumption.

### The two common-divisor ranges

For \(G=X^{1/10}\), a common divisor \(g\ge G\) implies
\[
L\le X^{473/500},\qquad X/L\ge X^{27/500}.
\]
The progression's nonzero Poisson part is \(O_B((X/L)^{1-B})\). There are at most \(Q^2\) pairs and \(O_v(H^2)\) total absolute shift weight per pair. Thus any prescribed negative power follows by taking a sufficiently large fixed number of derivatives; no arithmetic cancellation is needed.

For \(g<G\), smoothness of the shift profile gives
\[
R_v(g)\ll_{v,J}H^2(g/H)^{2J}.
\]
This follows by summing the rapidly decaying shift transform at the nonzero grid points, whose distances from the nearest integer are at least \(1/g\). Since \(G/H\le X^{-1/15}\), the corresponding zero-mode covariance is also negligible after the reciprocal-modulus sum and the factor \(X\) are charged. These statements remove different pieces: the large-\(g\) Poisson remainder and the small-\(g\) full-period covariance. They do not remove the small-\(g\) Poisson remainder.

The frequency form (13) has the correct sign \(\widehat W(X(\gamma-\beta))\). Integer aliases away from the closest representative, and cross terms with \(M\), have polynomial separation on the \(X\)-scale and are negligible. The author explicitly distinguishes common divisors of reduced denominators from those of arbitrary original moduli. For the selected top conductors these objects coincide because no larger multiple fits below \(Q\).

### Coherent-block constants and what they imply

The inherited actual-support count in equation (15) was checked against the frozen Round 12 construction. Its isolation identity \(A_d=1/d\) holds in the full signed family, rather than only after deleting negative coefficients. All selected coefficient phases lie in \([-\pi/4,0]\).

Writing \(n_\Omega=|\Omega_X|\) and using at most \(J\le8X/H\) cells,
\[
\sum_jm_j(m_j-1)\ge n_\Omega^2/J-n_\Omega\ge n_\Omega^2/(2J)
\]
eventually, uniformly over the stated \(H\)-range. The lower bound for \(n_\Omega\) therefore gives the exact displayed denominator
\(128^2\cdot8\cdot2=262144\).

Within a cell, the additional window-integrand phase is at most \(3\pi/100\), since \(W\) is supported in \((1,3/2)\). Including the coefficient phase difference gives
\[
\pi/4+3\pi/100=7\pi/25<\pi/3.
\]
Nonnegativity of \(W\) therefore yields the stated half-product lower bound. The coefficient-product bound contributes the further denominator 16, giving \(4194304\) in (18). The selected ordered pairs form a conjugation-symmetric set, so their sum is real.

Every selected distinct pair satisfies
\[
\frac{\gcd(d_1,d_2)}{d_1d_2}\le|\beta-\gamma|\le\frac1{100X}.
\]
Thus its common divisor is at most \(Q^2/(100X)<G\), and its reduced CRT period is at least \(100X\). The block really lies in the long-period small-common-divisor region. No equidistribution or independence of the moduli is assumed to create it.

Equation (18) bounds this specified subsum only. Remaining pairs can have negative real part and can cancel it. Equations (20) and the final unrestricted-Cauchy–Schwarz comparison retain this distinction correctly: a smaller full norm would demand cancellation, but the report does not prove that such cancellation is impossible. It also does not identify an arbitrary coefficient-space extremizer with the actual prime vector.

### Script inspection and independent replay

I inspected `check_signed_kernel_norm.py` before execution. It uses exact `Fraction` arithmetic for one fixed squarefree family, checks 100 CRT compatibility cases, verifies the complete-period mean and variance, and expands the finite-window norm into its pair, single-centering, and constant-window remainders. It retains the Mobius signs and primitive subtractions. Its polynomial toy window has integral \(1/960\); the script explicitly does not use that window to test the rapid-decay theorem.

A temporary copy was replayed, so the author JSON was not rewritten. The regenerated JSON was byte-identical to the frozen author result. In particular:

- full-period mean: \(-43/280\);
- full-period variance: \(22843/14700\);
- finite-window norm: \(14619643/165888000\);
- cutoff exponents and both coherent-block constants: passed exactly.

Script SHA256: `d661b1ef764f5ab395a9ca2db66ae9387d6885426772a93b595a43462fdc61d0`.
Result SHA256: `9f92dc12f0ac555e42af962478288e523593cf299c177fa93727d408373fdb5a`.

These checks test finite algebra, not the asymptotic prime-family count, a numerical cancellation claim, or an improved zeta correlation estimate. The accepted result is the exact main/remainder decomposition, its stated upper bound, and the positive coherent subsum with its explicit limitation.


<a id="report-56"></a>

# Current report 56: Round 13 independent integration review

**Collection:** R13 — rational-core extraction and the signed CRT remainder.

**Source:** [research/dyson/round13/INDEPENDENT_ROOT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round13/INDEPENDENT_ROOT_REVIEW.md).

**SHA-256:** `d38cfc0ec3f7031276340e4984fbc330185b5c9eef34df1e0955fc9853555456`. **Git blob:** `80d1bedb45164cf0b9f944602560da77f374ffda`. **Original bytes:** 4599.

## Round 13 independent integration review

Date: 2026-09-05. Reviewer: root Astra. This review accepts bounded analytic statements, not a new theorem about zeta pair correlation.

### Phase averaging

Reviewed `phase-resonance/AVERAGED_RATIONAL_PHASE_TEST.md`, SHA-256 `7f4285cb02241e22bdb29a1ad4952f7ab8249e3ec3bef984455a57ae05e41ebb`, and its complete exact-check script. The fixed inner prime interval, the mask (m,d)=1, and the primitive Ramanujan principal term are essential and are retained.

At Q=X^.523, M=X^.6, N=X^.4, the phase grid count on a fixed C/N core is O(M/N): the possible O(1) endpoint residues are absorbed because d/N tends to infinity, and repeated residue classes cost M/d because M/d tends to infinity. RH partial summation gives an error O(sqrt(N)log²N) uniformly on that core. The actual numerator weight has total absolute mass O(1) for each d. Hence the sum of errors is O(QM/sqrt(N)log²X)=O(X^.923 log²X). The same argument allows fixed divisor-bounded outer coefficients with the stated X^eta loss. This is a valid extraction of a retained integral main term.

The positive witness uses actual terminal conductors with even prime-factor count, not invented Fourier support. Unit residues s up to d/(32N), repeated m classes, low unit numerators, and the family count give respectively the factors 1/128, 1/32, and 1/2. The centered prime sum paired with S has real part at least (integral V)HN/(16d). Their product is exactly 1/131072. This proves the stated restricted positive block only. Other phases, signs and actual outer coefficients can cancel it.

The enlarged major arcs of width 2R/(qN) correctly handle floor(N/R) in Dirichlet approximation. The complement of fixed C/N cores would not suffice. Ordinary SW yields only a fixed logarithmic error for the other small denominators; ordinary zeta RH has not been mistaken for Dirichlet-L RH. The centered unit variance is exact because each inner prime is a unit and the unit mean is mu(d)P_N(0)/phi(d). Its completion bound gives X^1.323 sqrt(log X), explicitly weaker than the existing estimate for the original prime pairing. No arithmetic improvement is attributed to that factored bound.

### Signed smooth kernel

Reviewed `signed-kernel/SMOOTH_SIGNED_KERNEL_NORM.md`, SHA-256 `1105564835c925b818daf7198186e77c4f0f1ad4ac1001ee1bb50c0f5c7544d9`. Aquinas's separate `INDEPENDENT_AUDIT.md` provides an additional analytic review and byte-identical exact replay.

The CRT main term is X(integral W)(mean²+coefficient squared mass), with the nonzero CRT modes explicitly retained. The cutoff gcd(q1,q2)>=X^.1 makes the least common multiple at most X^.946; smooth Poisson decay is therefore available. For the complementary gcd range, the zero-mode covariance is small because X^.1/H tends to zero. These observations localize the difficulty without estimating away its signed remainder.

The coherent block constant 1/4194304 includes ordered distinct pairs, cell occupancy, coefficient phases and the window phase. Its lower bound is for an explicitly selected subsum of the off-diagonal expression. The report correctly does not infer a lower bound for the full remainder or norm. Its additional observation that even an ideal generic kernel norm does not by itself match the stronger prime-specific small-arc estimate is retained.

### Primary-source audit

Reviewed `minor-arc-source/MINOR_ARC_AND_FIXED_INTERVAL_AUDIT.md`, SHA-256 `bbdb17478b9e885570b7b49c3ff9b94b0ceb98f12a41743edb1ce492cb50edc4`. It checks Montgomery--Vaughan Theorem 17.1, the interval endpoint and genuine-prime changes, the rational-arc domain and Schoenfeld's RH theta estimate. The complete author-hosted/AMS papers and page images remain in the local reference archive; public receipts retain their URLs and hashes. Root's review checks the application and does not claim a second independent reconstruction of those classical source theorems.

### Acceptance and remaining obligation

Accepted as ordinary proofs with their explicit assumptions: the q=1 extraction error, restricted positive resonance block, exact CRT decomposition, coherent subsum and stated upper estimates. Finite tests validate algebra, constants and source identity; they do not numerically prove the asymptotic inequalities.

The strongest bound for the original selected smooth prime discrepancy remains O(X^1.023 log^5 X) under RH. The strict signed covariance estimate required for the actual-zeta Dyson--Montgomery target is unproved. No AH refutation, zeta-gap improvement, GUE theorem, RH proof or prime-gap improvement follows from this round.


<a id="report-57"></a>

# Current report 57: Dyson--Montgomery round 14: an actual Type I removal and a quantitative CUE heat theorem

**Collection:** R14 — smooth Type I removal and quantitative finite CUE heat.

**Source:** [research/reports/dyson_round14.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/dyson_round14.md).

**SHA-256:** `2ec5f48334de9a85e0a481c3bc7fabc33f9398afc957a019db8f62ee2bfb9140`. **Git blob:** `794f70e45c9832711de07ad8babc3d48ad4db47c`. **Original bytes:** 6653.

## Dyson--Montgomery round 14: an actual Type I removal and a quantitative CUE heat theorem

Date: 2026-09-05. Two bounded results now have complete ordinary proofs, independent reviews and reproducible checks. One removes an exact portion of the actual arithmetic discrepancy. The other strengthens the finite CUE scalar-heat comparison. Neither proves a theorem about the full zeta pair correlation.

### 1. A specified arithmetic component is below the required scale

For the exact smooth discrepancy already defined in Rounds 9--13, retain its original sinc kernel, both logarithmic weights, all permitted moduli q<=Q=X^.523 and the primitive principal subtraction. Split the von Mangoldt coefficient by the exact identity

\[
\Lambda=\Lambda_{\le U}+\Lambda_{>U},\qquad
\Lambda_{\le U}(n)=\sum_{r\mid n,\ r\le U}\mu(r)\log(n/r).
\]

The [complete unconditional proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md) establishes

\[
|\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le U}]|
\ll_{J,V,\chi} HX(UQ/X)^J\log^2X
\quad(J\ge2,\ UQ\le X/2).
\]

For U=X^.4, J=4 and H<=X^(2/7), this is O(X^(1711/1750)log²X)=o(X log X). More generally, for every fixed 0<eta<.477, all divisors below U<=X^(.477-eta) are covered by choosing a fixed J with J eta>2/7. The constants may depend on eta and J. No uniform limit as eta tends to zero is claimed.

The reason is exact progression Poisson summation in the smooth long cofactor n/r. Its zero mode cancels the actual primitive principal mean, and its nonzero modes decay because that cofactor exceeds q by a fixed power. The original joint kernel has uniform derivatives after the displayed integral representation removes its apparent singular phase. No smoothness is assigned to the shorter Möbius coefficients, and no dense-divisibility or RH estimate is needed for this portion.

This is a classical method applied and checked for the programme's actual kernel, not a novelty claim for Poisson summation. It also explains constructively how the large positive restricted rational cores from Round 13 can cancel when the actual longer factor is smooth. The signed Lambda_{>U} discrepancy remains exactly in the formula and is unestimated. Its cofactor need not be large or balanced. The full original discrepancy still has only the previously recorded RH bound, above X log X.

The [independent Type I review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/smooth-long-factor/INDEPENDENT_REVIEW.md) checks every primitive mask, normalized derivative, frequency sign, summation factor and the precise individual-variable criterion for a Heath--Brown component.

### 2. A finite CUE heat-flow approximation has an explicit error scale

Let delta_min be the minimum circular angular gap of Haar CUE(N). At its midpoint define

\[
B_N=\sum_{k\text{ outside the pair}}
\frac1{4\sin^2((\theta_k-c)/2)}.
\]

The [complete CUE proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/cue-selected-background/SELECTED_CUE_BACKGROUND.md) establishes the finite-N estimate

\[
\mathbb E\sum_{i:\delta_i\le\varepsilon}B_i
\le N^6\varepsilon^3/18
\qquad(0<\varepsilon\le\pi).
\]

The proof uses the exact finite CUE three-point Gram determinant. Its simultaneous short-pair and endpoint vanishing factors control the singular inverse-square weights. Endpoint weights are used before enlarging to nonconsecutive pairs; directly enlarging a midpoint-weighted sum would be invalid. Circular ordering includes the wrap gap.

The classical minimum-gap law and Markov then give B_N/N²=O_p(1), without assigning a conditional density to the selected pair. For each fixed L,K>0 the proof supplies the explicit bound

\[
\limsup_N\Pr(B_N/N^2>K)
\le e^{-L^3/(72\pi)}+L^3/(18K).
\]

For the finite scalar-heat polynomial

\[
P_{N,s}(z)=\sum_{j=0}^N a_j e^{sj(N-j)}z^j,
\quad P_N(z)=\det(zI-U_N),
\]

let D_N be the first positive discriminant time. Applying the already quantified Galilean lemma with its verified uniform constants yields

\[
\frac{8D_N}{\delta_{\min}^2}-1=O_{\mathbb P}(N^{-2/3}),
\qquad
D_N-\delta_{\min}^2/8=O_{\mathbb P}(N^{-10/3}).
\]

This strengthens the programme's prior qualitative CUE comparison. It is an approximation error in probability, not a convergence rate for the limiting depth distribution. It is not a stochastic Dyson Brownian motion result or an available identity for true zeta zeros. General-beta analogues and global novelty remain outside this proof.

The [independent CUE review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/cue-selected-background/INDEPENDENT_REVIEW_EUCLID.md) and [root review of both results](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/INDEPENDENT_ROOT_REVIEW.md) accept the proofs with these restrictions.

### 3. Preserved evidence

Seventeen original files totaling 548,013 bytes are preserved in the adjacent local `Astra-Local-Archive/round14-originals`. Fifteen research, review and receipt files are public and verbatim. The full Feng--Wei PDF/text remain local with public source hashes and precise source locations.

The [separate-process replay](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/logs/round14-integration/recheck.json) passes both bounded scripts. It checks the symbolic N=3 CUE determinant and singular-weight cancellation, the constant 1/18, 63 complete-period centering cases, exact divisor/HB identities through n=125, rational exponent arithmetic and two fixed floating Gaussian Poisson diagnostics. One temporary source path is excluded from the Type I certificate comparison; the CUE JSON matches every field. These tests supplement ordinary proofs; they do not replace them or provide interval-certified stochastic estimates.

The integration receipt also records the earlier Galilean publication edit: only its title and reviewer attribution differ from the original hash cited by the CUE author. Root compared the complete mathematical bodies and found them identical. Both hashes remain visible; the original proof provenance is not silently rewritten.

### 4. What is still needed for the famous-conjecture target

The actual-zeta route still requires a signed estimate for the retained arithmetic remainder, with all covariance cross terms and principal means present. The CUE theorem supplies a rigorous RMT reference statement and exposes the missing zeta input: isolated close pairs and their background control cannot be assumed from low-band correlation data.

The sufficient two-scale W_T lower limit 1/16, compact Fourier test above 7/10, positive-density violation of AH-Pairs, sub-half normalized zeta gap and sub-186 prime gap remain unproved. No famous conjecture is reported solved. Broad numerical sweeps, another Fable session and a claim of full arithmetic-to-Fock convergence are postponed; the next arithmetic work concerns the exact remaining signed terms.


<a id="report-58"></a>

# Current report 58: A smooth long factor removes an actual Type I component

**Collection:** R14 — smooth Type I removal and quantitative finite CUE heat.

**Source:** [research/dyson/round14/smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md).

**SHA-256:** `d6143f19ddf006a1acc833ecd2e5265bffb35817930cfeaa4f4e4b973af7c849`. **Git blob:** `97e25b8fc8488e5cd5c538fceddb450d42dfd227`. **Original bytes:** 13229.

## A smooth long factor removes an actual Type I component

Date: 2026-09-05. Status: unconditional ordinary proof; a classical Poisson application, newly verified for this programme's exact kernel. No novelty claim is made for the method. No estimate for the remaining component or the whole zeta covariance is proved.

Define the exact truncated divisor convolution
\[
\Lambda_{\le U}(n)=\sum_{\substack{r\mid n\\r\le U}}\mu(r)\log(n/r).
\tag{1}
\]
For the actual smooth discrepancy of Rounds 9–13, with \(Q=X^{523/1000}\), \(H=X/T\), and \(X^{1/6}\le H\le X^{2/7}\), this note proves
\[
\boxed{
|\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le U}]|
\ll_{J,V,\chi}HX\left(\frac{UQ}{X}\right)^J(\log X)^2
\quad(J\ge2,\ UQ\le X/2).
}
\tag{2}
\]
Both primitive restrictions, the modulus coefficients and the entire original covariance kernel are retained. Neither RH nor dense divisibility is needed for this component.

In particular \(U=X^{2/5}\), \(J=4\) give
\[
|\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le X^{2/5}}]|
\ll X^{1711/1750}(\log X)^2=o(X\log X).
\tag{3}
\]
The exponent margin below \(X\) is \(39/1750\). The remaining divisor portion has signs; the truncation is an exact decomposition, not an inequality for the full discrepancy.

### 1. The exact arithmetic object

Use the frozen weights
\[
a_y(X)=\min\{(y/X)^{1/2},(X/y)^{3/2}\},
\]
\[
w_h(u)=\chi(u/X)a_u(X)a_{u+h}(X)
\operatorname{sinc}_0\!\left(T\log(1+h/u)\right),
\tag{4}
\]
where \(\operatorname{sinc}_0(t)=\sin(t)/t\), with its removable value at zero,
\(V\in C_c^\infty(1,2)\), \(\chi\in C_c^\infty(1,3/2)\),
\(X=T^\alpha\), \(6/5\le\alpha\le7/5\), and \(H=X/T\).
For any coefficient sequence \(b\), define
\[
\begin{split}
\mathcal D_{\mathcal Q}^{V}[b]
=\sum_h V(h/H)
\sum_{\substack{q\in\mathcal Q_X\\(h,q)=1}}\mu(q)
\bigg[
&\sum_{n\equiv h\ (q)}
b(n)w_h(n-h)\log((n-h)/q)\\
&-\frac1{\varphi(q)}
\sum_{(n,q)=1}b(n)w_h(n-h)\log((n-h)/q)
\bigg].
\end{split}
\tag{5}
\]
Weights vanish outside their indicated support. Thus \(n\asymp X\) and \(n-h>X\), so all logarithms have positive arguments. This is the actual R9/R11 component, including its log-cofactor weight.

The family \(\mathcal Q_X\) may be the full canonical complementary family or any selected moduli \(q\le Q\). We use only the cutoff and \(|\mu(q)|\le1\). An added \((\log q)^j\) weight, for a fixed nonnegative integer \(j\), changes \((\log X)^2\) in (2) to \((\log X)^{2+j}\); it does not affect the power margin.

For all positive integers, including \(n=1\), the identity
\(\Lambda=\mu*\log\) is exact. At 1 both sides are zero. For a real \(U\ge1\), \(r\le U\) means the usual integer cutoff, with its endpoint included. Consequently
\[
\mathcal D_{\mathcal Q}^{V}[\Lambda]
=\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le U}]
+\mathcal D_{\mathcal Q}^{V}[\Lambda_{>U}],
\quad
\Lambda_{>U}(n)=
\sum_{\substack{r\mid n\\r>U}}\mu(r)\log(n/r).
\tag{6}
\]
No prime-power removal or asymptotic main-term substitution occurs here. Neither summand need be nonnegative.

### 2. Why a smooth longer coefficient cancels the complete phase mean

Let \(q\ge2\), let \(a\bmod q\) be arbitrary, and fix inner coefficients \(\beta_n\) independently of \(m\). Define the periodic function
\[
R_{q,a}(m)=1_{(m,q)=1}
\sum_{\substack{n\\(n,q)=1}}\beta_n
\left[e(amn/q)-\frac{c_q(a)}{\varphi(q)}\right],
\tag{7}
\]
where \(e(t)=e^{2\pi it}\) and \(c_q\) denotes the Ramanujan sum.
Multiplication by a unit \(n\) permutes the unit residues, so \(c_q(an)=c_q(a)\). It follows exactly that
\[
\sum_{m\bmod q}R_{q,a}(m)=0.
\tag{8}
\]
This includes nonprimitive \(a\), and does not require squarefree \(q\). For \(a=0\), the function itself vanishes.

Suppose \(A_X\) is smooth on a fixed positive compact support, and every fixed derivative has a uniform fixed-power logarithmic bound.
Use the Fourier conventions
\[
\widehat R(\ell)=q^{-1}\sum_{m\bmod q}R(m)e(-\ell m/q),
\qquad
\widehat A(t)=\int_{\mathbb R}A(u)e(-tu)\,du.
\]
Fourier expansion and Poisson summation give
\[
\sum_m A_X(m/M)R_{q,a}(m)
=M\sum_{\nu\ne0}
\widehat R(-\nu\bmod q)\widehat A_X(M\nu/q).
\tag{9}
\]
The omitted \(\nu=0\), and all nonzero multiples of \(q\), have coefficient zero by (8).
Writing \(B=\sum_n|\beta_n|\), we have \(|\widehat R(\ell)|\le2B\).
For \(M\ge q\), integration by parts \(J\ge2\) times therefore gives
\[
\left|\sum_m A_X(m/M)R_{q,a}(m)\right|
\ll_J MB(\log X)^{C_J}(q/M)^J.
\tag{10}
\]
This does not assign a Siegel–Walfisz property to the twisted sequence.

The actual shift Fourier weights satisfy, by finite summation by parts,
\[
|S_{V,H}(\beta)|\ll_{V,K}H(1+H\|\beta\|)^{-K},
\qquad
\sum_{a=1}^{q-1}|S_{V,H}(a/q)|\ll_V q.
\tag{11}
\]
Hence the full numerator sum with its \(1/q\) coefficient costs \(O_V(1)\) per modulus. Its zero numerator vanishes by (8); there is no hidden \(S_{V,H}(0)\asymp H\) term.
At \(M=X^{.6}\), \(q\le Q=X^{.523}\), the ratio \(q/M\le X^{-.077}\) permits any fixed power saving by choosing \(J\).

For a nonnegative smooth longer profile that is positive on an interval, the restricted positive rational core from R13 still has a large contribution by the same residue count on that interval. Equations (8)–(10) give a constructive reason why other phases cancel it in the full sum. They make no such claim for a nonsmooth or arithmetically oscillating longer coefficient.

### 3. A progression identity retaining the whole actual kernel

Expand (1) inside (5), writing \(n=rs\). If \((r,q)>1\), the progression \(rs\equiv h\pmod q\) is empty because \((h,q)=1\); its primitive principal sum is empty as well. Such terms vanish exactly.

For \((r,q)=1\), put \(b\equiv h\overline r\pmod q\), a unit residue.
The longer variable \(s\) has scale \(L_r=X/r\) and weight
\[
F_{r,h,q}(s)=(\log s)\,w_h(rs-h)\log((rs-h)/q).
\tag{12}
\]
Its coefficient outside is \(\mu(r)\). Write
\(F_{r,h,q}(s)=\Phi_{r,h,q}(s/L_r)\).
With \(\delta=H/X=1/T\), \(z=h/H\), and \(u=s/L_r\), the profile is exactly
\[
\begin{split}
\Phi_{r,h,q}(u)=&
\chi(u-\delta z)(u-\delta z)^{-3/2}u^{-3/2}
\operatorname{sinc}_0\!\left(\delta^{-1}\log\frac{u}{u-\delta z}\right)\\
&\times[\log(X/r)+\log u]\,
[\log(X/q)+\log(u-\delta z)].
\end{split}
\tag{13}
\]
On this support \(u-\delta z>1\) and \(u>1\), so the chosen branches of both \(a\)-factors are correct.
The apparently singular phase has the regular form
\[
\delta^{-1}\log\frac{u}{u-\delta z}
=\int_0^z\frac{dt}{u-\delta t}.
\tag{14}
\]
The fixed compact support of \(\chi\), and \(z\) in the fixed support of \(V\), imply that these profiles lie in a fixed positive compact interval and satisfy
\[
\sup_{r\le U,q\le Q,h}
\sum_{j=0}^J\|\Phi_{r,h,q}^{(j)}\|_\infty
\ll_{J,\chi}(\log X)^2
\tag{15}
\]
for every fixed \(J\). Zero extension outside the support is smooth because \(\chi\) is compactly supported in the open interval. All bounds are uniform in the displayed parameters, including \(T\). No separated substitute for the actual kernel was used.

For any such profile, \(L>0\), and a unit \(b\bmod q\), Poisson summation gives
\[
\begin{split}
&\sum_{s\equiv b\ (q)}\Phi(s/L)
-\frac1{\varphi(q)}\sum_{(s,q)=1}\Phi(s/L)\\
&\qquad=\frac Lq\sum_{k\ne0}\widehat\Phi(kL/q)
\left[e(kb/q)-\frac{c_q(k)}{\varphi(q)}\right].
\end{split}
\tag{16}
\]
The Fourier convention is that in (9). Its \(k=0\) term cancels since
\(c_q(0)=\varphi(q)\). This is finite progression summation of a smooth function; there are no contour or pole terms.
Using \(|c_q(k)|\le\varphi(q)\), followed by \(J\) integrations by parts, proves
\[
\left|\text{left side of (16)}\right|
\ll_{J,\chi}\frac Lq(q/L)^J(\log X)^2,
\quad L\ge2q,\ J\ge2.
\tag{17}
\]
The assumption \(UQ\le X/2\) ensures \(L_r=X/r\ge2q\) for every term.

### 4. Summing every short divisor, actual shift and permitted modulus

Apply (17) to (12) and use only \(|\mu(r)\mu(q)|\le1\) and
\(\sum_h|V(h/H)|\ll_VH\). Since
\(\sum_{r\le U}r^{J-1}\ll_JU^J\) and
\(\sum_{q\le Q}q^{J-1}\ll_JQ^J\), the result is
\[
\begin{split}
C_JH(\log X)^2
\sum_{r\le U}\sum_{q\le Q}q^{J-1}(X/r)^{1-J}
&\ll_J HX^{1-J}U^JQ^J(\log X)^2\\
&=HX(UQ/X)^J O_J((\log X)^2).
\end{split}
\tag{18}
\]
This proves (2). An arbitrary selected family is bounded by this full cutoff sum. All coprimality restrictions were retained until taking the upper bound.

For \(U=X^{2/5}\), \(UQ/X=X^{-77/1000}\). At the largest shift length and \(J=4\), the exponent is
\[
1+\frac27-4\frac{77}{1000}=\frac{1711}{1750}<1.
\tag{19}
\]
This needs just four fixed derivatives of the profile, explicitly covered by (15).
For example, \(J=17\) gives exponent \(-163/7000\); no high-order numerical calculation is needed.
More generally, fix \(0<\eta<477/1000\) and let
\[
U\le X^{477/1000-\eta},
\tag{20}
\]
Then \(L_r=X/r\ge X^{523/1000+\eta}\) for every retained divisor, while the profile seminorms in (15) remain \(O_J(\log^2X)\) uniformly.
For any fixed integer \(J\ge2\) with \(J\eta>2/7\), equation (18) gives
\[
|\mathcal D_{\mathcal Q}^{V}[\Lambda_{\le U}]|
\ll X^{1+2/7-J\eta}(\log X)^2=o(X\log X).
\tag{20a}
\]
Choosing a larger fixed \(J\) gives any desired smaller absolute power.
Constants may depend on \(\eta,J,V,\chi\); no uniform claim as \(\eta\to0\) is made.

### 5. Precisely which divisor and Heath–Brown components are covered

Equation (6) is an exact arithmetic application: the \(\mu*\log\) portion with short Möbius divisor \(r\le U\) has negligible discrepancy. The Möbius factor is not assumed smooth. It is attached to the shorter fixed variable, while the logarithmic cofactor has a sufficiently long smooth summation range.

The same criterion can be stated for a Heath–Brown decomposition. Here is the needed identity with its range proved. Let \(\mathbf1(n)=1\), let \(\epsilon\) be the identity for Dirichlet convolution, and let \(\mu_{\le Y}=\mu1_{[1,Y]}\).
Then
\[
E=\epsilon-\mu_{\le Y}*\mathbf1
=\mu_{>Y}*\mathbf1
\]
is supported on integers greater than \(Y\). Thus \(E^{*k}*\Lambda\) vanishes on \(n\le Y^k\). Expanding \(\epsilon-E^{*k}\) and using
\(\mathbf1*\Lambda=\log\) proves, on that range,
\[
\Lambda=
\sum_{j=1}^k(-1)^{j-1}\binom kj
(\mu_{\le Y})^{*j}*\mathbf1^{*(j-1)}*\log.
\tag{21}
\]
The equality at 1 is again zero on both sides. Choose \(Y^k\) above the fixed upper end of the actual \(n\asymp X\) support to cover all terms.

After a smooth multiplicative partition, every component of (21) with an individual unrestricted \(\mathbf1\) or \(\log\) variable at scale
\[
L\ge QX^\eta
\tag{22}
\]
is handled by the same progression proof. Combine all other variables into a short coefficient \(c(r)\), with \(r\ll X/L\). It may contain truncated Möbius variables and divisor multiplicities. A fixed divisor bound on \(c(r)\) costs at most \(X^\varepsilon\) for any fixed \(\varepsilon>0\); increasing \(J\) absorbs this cost. Smooth partition factors and fixed powers of logarithms preserve (15), with their fixed logarithmic losses recorded.

The condition is on an individual smooth variable, not the total size of a product. If a nominal longer coefficient is itself a convolution, opening it helps only on subranges where an actual remaining smooth variable still satisfies (22). For example, a product \(ab\asymp X^{.6}\) does not establish that the \(b\)-range in
\(\alpha_m=\sum_{ab=m}c(a)A(b/L)\) exceeds \(Q\).

The exact remainder \(\Lambda_{>U}\) in (6) stays untreated. It need not be balanced: its logarithmic cofactor can be small. So do Type II and higher-factor components for which every individual smooth variable is at most \(QX^{o(1)}\). A longer Möbius or unsmoothed divisor sequence does not satisfy (15) merely because its support is long. No estimate for these remaining pieces is asserted.

### 6. Research consequence and verification scope

R13's sparse rational cores can have large positive restricted main terms. Here an adequately long smooth variable makes their complete centered sum cancel, with the original primitive mean and all frequencies retained. The direct progression proof also carries the actual joint \(s,r,h\) kernel, avoiding any unproved weight separation.

For the actual zeta-facing discrepancy, (2)–(6) remove a definite short-divisor portion unconditionally. The residual problem can therefore be studied with that portion subtracted exactly and a proved small error. This does not bound the remaining signed piece, prove a covariance asymptotic, refute AH, or establish Montgomery's conjecture.

The source paper [OpenAI, Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), Definitions 2.6–2.9 and Proposition 2.18, supplies the coefficient terminology used for comparison. Its proof of Corollary 2.19 invokes a Heath–Brown reduction; the identity used here is proved directly in (21). The actual kernel and normalization are displayed in full in (4)–(5), following the frozen R9–R11 definitions.

The adjacent check verifies complete-period centering, the Poisson sign on an independently summed Gaussian progression, exact exponent arithmetic, and a finite symbolic-coefficient version of (21). The Gaussian computation is a diagnostic; (16) is the ordinary analytic proof. No large-prime realization, parameter search, external model, or prior-file modification is used.


<a id="report-59"></a>

# Current report 59: Independent review: smooth long-factor removal

**Collection:** R14 — smooth Type I removal and quantitative finite CUE heat.

**Source:** [research/dyson/round14/smooth-long-factor/INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/smooth-long-factor/INDEPENDENT_REVIEW.md).

**SHA-256:** `3a6bef5c4cddf0973cacd69826aefa3fbea1db3659beb7f856ecaf3f6cee356b`. **Git blob:** `7ca9c893f44978336db65b43ee2cc9befb8026a8`. **Original bytes:** 8401.

## Independent review: smooth long-factor removal

Date: 2026-09-05. **Accepted as an unconditional ordinary proof of the stated component bound.** No mathematical correction is requested. This is an independent check of the complete authored note, with special attention to the exact kernel, primitive restrictions, Poisson normalization, uniform derivatives, and total error. It does not claim an estimate for the remaining signed discrepancy or the zeta covariance.

The reviewed author file is `SMOOTH_LONG_FACTOR_REMOVAL.md`, SHA-256 **d6143f19ddf006a1acc833ecd2e5265bffb35817930cfeaa4f4e4b973af7c849**. The author file and its existing outputs were left unchanged. The proof was compared with the frozen R9 discrepancy definition and R11 kernel formula. The bounded author script was inspected and replayed in a temporary copy; its certificate agrees after normalizing only the temporary source path. Replay details are in `INDEPENDENT_REPLAY.json`, and hashes of the reviewed dependencies and review artifacts are in `INDEPENDENT_REVIEW_RECEIPT.json`.

### Acceptance coverage

| Item | Author location | Finding |
|---|---|---|
| Actual discrepancy and log-cofactor weight | Equations (4)–(6) | Matches R9/R11; no weight or primitive principal term is dropped. |
| Periodic phase mean and Fourier sign | Equations (7)–(11) | Correct, including nonprimitive numerators and nonsquarefree moduli. |
| Exact profile and uniform derivatives | Equations (12)–(15) | Correct in the full stated parameter range. |
| Progression Poisson formula and zero mode | Equations (16)–(17) | Correct sign, factor L/q, and exact principal cancellation. |
| Sum over every r,h,q | Equations (18)–(20a) | Correct bound HX(UQ/X)^J log²X and exponent thresholds. |
| Exact signed remainder and HB identity | Equations (6), (21)–(22) | Correct; the criterion requires an individual smooth long variable. |
| Validation scope | Adjacent script/certificate | Small exact algebra and floating Gaussian diagnostic only; not a computational proof of the analytic estimate. |

### 1. Kernel and parameter uniformity

For n=rs, L_r=X/r, u=s/L_r, δ=H/X=1/T, and z=h/H, the exact identities are rs=Xu and rs−h=X(u−δz). Because χ is supported inside (1,3/2), both arguments of the a-factors lie above X on the nonzero support. Thus both use the power −3/2. The two logarithms become precisely

\[
\log s=\log(X/r)+\log u,\qquad
\log((rs-h)/q)=\log(X/q)+\log(u-\delta z).
\]

The sinc argument has no hidden large derivative:

\[
\delta^{-1}\log\frac{u}{u-\delta z}
=\int_0^z\frac{dt}{u-\delta t},\qquad
\partial_u^j\int_0^z\frac{dt}{u-\delta t}
=(-1)^j j!\int_0^z\frac{dt}{(u-\delta t)^{j+1}}.
\]

Here z lies in a fixed compact subset of (1,2). On the support, u−δt≥u−δz is bounded away from zero for 0≤t≤z. Also δ≤X^{-5/7} in the stated range. The profile therefore has a fixed positive compact support for all sufficiently large X, and every fixed u derivative of the nonlogarithmic factors is uniformly bounded. The only growth is from the two logarithms, each O(log X), since 1≤r≤U<X and 1≤q≤Q<X. This proves the uniform O_J(log²X) seminorm bound. Smooth zero extension is legitimate because χ is compactly supported strictly inside its open interval.

The needed derivatives are derivatives in the normalized summation variable u, **uniformly in** r,h,q,T; the proof does not require differentiating an arithmetic cutoff with respect to r or q. There is no missing r^J factor: the rescaling to L_r already accounts for it. The exact joint kernel is retained throughout.

### 2. Primitive masks and Poisson cancellation

If (r,q)>1 and (h,q)=1, rs≡h mod q has no solutions, and the primitive principal sum has no terms because (rs,q)>1. Such terms vanish in both parts, rather than contributing an exceptional error. If (r,q)=1, multiplication by r gives

\[
rs\equiv h\pmod q\iff s\equiv h\bar r\pmod q,
\qquad (rs,q)=1\iff(s,q)=1.
\]

The resulting class b=h r̄ is a unit. For the Fourier convention \(\widehat\Phi(t)=\int\Phi(u)e(-tu)du\), the progression formula is

\[
\sum_{s\equiv b\ (q)}\Phi(s/L)
=\frac Lq\sum_k\widehat\Phi(kL/q)e(kb/q).
\]

Averaging this formula over all unit b produces exactly c_q(k)/φ(q). The k=0 terms cancel since c_q(0)=φ(q). The sign in author equation (16) is consequently correct. The bounds |c_q(k)|≤φ(q) and |Φ̂(t)|≪_J log²X |t|^{-J}, together with J≥2 and L≥2q, give equation (17), including its factor L/q.

The auxiliary periodic identity in §2 is also correct: a unit inner n permutes the units, so the period mean of R is zero. With R(m)=Σ_ℓ R̂(ℓ)e(ℓm/q), Poisson yields the coefficient R̂(−ν mod q) in equation (9). Multiples of q vanish as well. The shift bound Σ_{1≤a<q}|S_{V,H}(a/q)|≪q follows by summing the stated decay, both when q≥H and when q<H. This auxiliary explanation is not substituted for the direct progression proof of the actual kernel.

### 3. Total error and numerical exponents

The bound for one retained r,h,q is

\[
\ll_J q^{J-1}(X/r)^{1-J}\log^2X.
\]

Taking absolute values of the Möbius coefficients, summing the actual shifts with Σ_h|V(h/H)|≪H, and enlarging the permitted moduli to every q≤Q gives

\[
\ll_J HX^{1-J}\log^2X
\left(\sum_{r\le U}r^{J-1}\right)
\left(\sum_{q\le Q}q^{J-1}\right)
\ll_J HX(UQ/X)^J\log^2X.
\]

No extra q, H, or divisor-count factor is omitted. The q=1 discrepancy is identically zero, so including it in this upper sum causes no issue. Real U≥1 with the stated integer cutoff also causes no endpoint term.

For U=X^{2/5}, Q=X^{523/1000}, H≤X^{2/7}, and J=4, the exponent is 1711/1750, with margin 39/1750 below 1. For U≤X^{477/1000−η}, fixed η>0 ensures UQ≤X/2 for sufficiently large X. Any fixed integer J≥2 satisfying Jη>2/7 gives o(X log X), despite the remaining logarithmic square. The dependence of constants on η and J is properly stated; no claim uniform as η↓0 is needed.

### 4. Signed remainder and Heath–Brown scope

The identities Λ=μ*log and Λ=Λ_{≤U}+Λ_{>U} hold pointwise, including n=1, and the discrepancy is linear. Therefore equation (6) is exact before estimation. Neither sign nor cancellation properties of the untreated divisor portion are inferred from the small estimate for the retained portion. Prime powers have not been removed, so there is no missing prime-power exception here.

For the displayed Heath–Brown identity, E=ε−μ_{≤Y}*1=μ_{>Y}*1 is supported on integers greater than Y. Thus E^{*k}*Λ vanishes for n≤Y^k. Expanding ε−E^{*k} and using 1*Λ=log gives equation (21) with its displayed binomial coefficients and signs. Taking Y^k beyond the support covers all terms.

After a smooth multiplicative partition, an individual unrestricted 1 or log variable of scale L≥QX^η admits exactly the same progression argument. The other variables may be grouped into a short arithmetic coefficient c(r); no smoothness is assigned to c(r). For fixed identity order, divisor multiplicities cost at most X^ε and fixed logarithmic factors, which a larger fixed J absorbs. The criterion does not apply merely because a product of several rough variables is long. This limitation, the possibility of an unbalanced Λ_{>U}, and the absence of a bound for the whole remaining discrepancy are all stated correctly in the author report.

### 5. Replay and final scope

The inspected script checks 63 exact periodic-centering cases, the formal-logarithm divisor and HB identities through n=125, the real short cutoff 9/2, and exact rational exponent arithmetic. Its two Gaussian progression comparisons have the correct Poisson sign and agree within the stated binary64 tolerance; these are diagnostics, not rigorous enclosures. The temporary replay passed every assertion and reproduced the certificate modulo its temporary source path. Original report, script, certificate, and log were not changed.

This review accepts the displayed unconditional removal of a definite short-divisor component. It does not upgrade the R13 positive restricted-core claim into a full signed lower bound, establish cancellation for an arithmetic long coefficient, estimate the remaining Λ_{>U} discrepancy, or imply AH/RH/Montgomery progress beyond the explicit component reduction. No additional scan, literature claim, or author edit is required for acceptance of the result as stated.


<a id="report-60"></a>

# Current report 60: CUE background at the selected smallest gap: a direct finite-N bound

**Collection:** R14 — smooth Type I removal and quantitative finite CUE heat.

**Source:** [research/dyson/round14/cue-selected-background/SELECTED_CUE_BACKGROUND.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/cue-selected-background/SELECTED_CUE_BACKGROUND.md).

**SHA-256:** `fbc67828d13534d8d0b4ac1f742a639b282dd93a3f7cb635291f8cdbb651c0a5`. **Git blob:** `5df1a161d2aea573ed2a24336325c5fa5ae248c5`. **Original bytes:** 11711.

## CUE background at the selected smallest gap: a direct finite-N bound

Date: 2026-09-05. Author: Astra subagent `yau_flow`. Status: complete ordinary-proof draft submitted for independent review. This is a CUE-only estimate using its exact finite-dimensional determinant. It does not invoke any general-beta correlation inequality, assert novelty against the entire literature, or transfer a random-matrix result to zeta zeros.

The finite CUE heat-depth ratio was already derived qualitatively in Round 1, `yau_flow.md` Sections 3–4, and its deterministic Galilean refinement was quantified in Round 2, `galilean-proof-audit.md` Sections 1–5. Those results are not being presented as new here. The additional estimate is tightness at the natural \(N^2\) scale for the background of the **selected minimum pair**, with an explicit finite-N truncated first-moment bound. It sharpens the rate obtained by applying the existing deterministic lemma.

### 1. Exact geometry and statement

Let \(U_N\) have Haar law on \(U(N)\). Its eigenangles are points of \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with ordered representatives \(\theta_1<\cdots<\theta_N\) and \(\theta_{N+1}=\theta_1+2\pi\). Write
\[
\delta_i=\theta_{i+1}-\theta_i,\quad
c_i=\theta_i+\delta_i/2\pmod{2\pi},\quad
\delta_N^{\min}=\min_i\delta_i.
\]
All roots are distinct almost surely. Any fixed deterministic tie-breaking convention may select the minimum; ties have probability zero.

For circular distance \(r(x)=\min_{k\in\mathbb Z}|x-2\pi k|\in[0,\pi]\), put
\[
q(x)=\frac1{4\sin^2(x/2)}.
\]
The midpoint background and the larger endpoint background of a consecutive gap are
\[
B_i=\sum_{k\ne i,i+1}q(\theta_k-c_i),\qquad
S_i=\sum_{k\ne i,i+1}
\bigl[q(\theta_k-\theta_i)+q(\theta_k-\theta_{i+1})\bigr].
\tag{1}
\]
The selected background is \(B_N=B_{i_*}\), where \(\delta_{i_*}=\delta_N^{\min}\).

**Finite-N proposition.** For every \(N\ge2\) and \(0<\varepsilon\le\pi\),
\[
\boxed{\quad
\mathbb E\sum_{i:\,\delta_i\le\varepsilon}B_i
\le \frac{N^6\varepsilon^3}{18}.
\quad}
\tag{2}
\]
The same bound holds with \(B_i\) replaced by \(S_i\). In fact the proof bounds the endpoint-background sum over **all ordered pairs** whose positive oriented separation is at most \(\varepsilon\), even when they are not consecutive.

Consequently, for fixed \(L>0\) and all sufficiently large \(N\),
\[
\mathbb E\sum_{i:\,\delta_i\le L N^{-4/3}}\frac{B_i}{N^2}
\le\frac{L^3}{18}.
\tag{3}
\]
No conditional density at the minimum is used.

### 2. A three-point bound that retains the endpoint zeros

With correlation densities measured against ordinary angular Lebesgue measure, use the periodic CUE kernel
\[
K_N(x,y)=\frac1{2\pi}\sum_{m=0}^{N-1}e^{im(x-y)},\qquad
\rho_k(x_1,\ldots,x_k)=\det[K_N(x_a,x_b)]_{a,b\le k}.
\]
This determinant convention counts ordered distinct tuples. It is gauge-equivalent to the sine kernel in Feng–Wei, Section 1.2, printed page 5; the integer-frequency form avoids any artificial cut or antiperiodic-kernel issue.

Let
\[
\phi(x)=\frac1{\sqrt{2\pi}}(1,e^{ix},\ldots,e^{i(N-1)x}),
\quad A=\|\phi(x)\|^2=\frac N{2\pi},
\quad D=\|\phi'(x)\|^2
=\frac{N(N-1)(2N-1)}{12\pi}\le\frac{N^3}{6\pi}.
\]
For \(0<d\le\pi\), Gram determinant factorization gives
\[
\rho_2(0,d)\le A\|\phi(d)-\phi(0)\|^2\le ADd^2.
\]
Let \(\Pi\) be orthogonal projection onto the span of \(\phi(0),\phi(d)\). Then
\[
\rho_3(0,d,z)=\rho_2(0,d)\|(I-\Pi)\phi(z)\|^2.
\]
The final squared norm is at most \(A\), and also at most
\(\|\phi(z)-\phi(0)\|^2\le D r(z)^2\), because \(\phi(0)\) belongs to that span and \(\phi\) is periodic. Therefore
\[
\rho_3(0,d,z)
\le ADd^2\min\{A,D r(z)^2\}
\le\frac{N^5d^2}{24\pi^3}
\min\{1,N^2r(z)^2\}.
\tag{4}
\]
The sharper factor \(N^2r^2/3\) in the second branch was weakened to \(N^2r^2\). Equivalently, the two elementary bounds before this weakening are \(N^5d^2/(24\pi^3)\) and \(N^7d^2r^2/(72\pi^3)\). For \(N=2\), the third density is zero, so the same conclusion holds. Coincident points are null sets and can be handled by continuity.

This is the needed finite-dimensional replacement for a general-beta background claim. It simultaneously supplies the short-pair factor \(d^2\) and the endpoint cancellation \(r(z)^2\).

### 3. Integrating the singular weight

For \(0<r\le\pi\), \(\sin(r/2)\ge r/\pi\), hence
\[
q(z)\le\frac{\pi^2}{4r(z)^2}.
\]
Splitting at \(r=1/N\) yields
\[
\begin{split}
\int_{\mathbb T}q(z)\min\{1,N^2r(z)^2\}\,dz
&\le\frac{\pi^2}{2}
\left(\int_0^{1/N}N^2\,dr+\int_{1/N}^{\pi}r^{-2}\,dr\right)\\
&=\frac{\pi^2}{2}(2N-1/\pi)\le\pi^2N.
\end{split}
\]
Equation (4) therefore gives
\[
\int_{\mathbb T}q(z)\rho_3(0,d,z)\,dz
\le\frac{N^6d^2}{24\pi}.
\tag{5}
\]
Interchanging the two pair endpoints gives the same bound with \(q(z-d)\). This can be seen either by translation/reflection invariance or by repeating the projection proof with base point \(d\).

Let \(Z_\varepsilon\) sum the endpoint background over all ordered distinct pairs \((a,b)\) whose positive oriented separation \(d=(b-a)\pmod{2\pi}\) lies in \((0,\varepsilon]\). The factorial-moment identity and rotation invariance give
\[
\begin{split}
\mathbb E Z_\varepsilon
&=2\pi\int_0^\varepsilon\int_{\mathbb T}
[q(z)+q(z-d)]\rho_3(0,d,z)\,dz\,dd\\
&\le2\pi\int_0^\varepsilon\frac{N^6d^2}{12\pi}\,dd
=\frac{N^6\varepsilon^3}{18}.
\end{split}
\tag{6}
\]
The integrands are nonnegative, so Tonelli is legitimate before the estimates prove finiteness. There is no factor \(1/2\): the correlation density counts ordered triples, and the short orientation of a consecutive gap is included once. The pair straddling the chosen \(2\pi\) cut is included by exactly the same periodic change of variables. Even at \(\varepsilon=\pi\), possible antipodal ambiguity is a null event.

To pass to midpoint backgrounds, rotate a consecutive pair of gap \(d\le\pi\) to endpoints \(\pm d/2\). Every other point has a midpoint-centered lift \(y\in[-\pi,\pi]\) with \(|y|\ge d/2\), because the open short arc contains no point. Its distance to the endpoint on the same side is \(|y|-d/2\le|y|\). Since \(q\) decreases with circular distance on \((0,\pi]\),
\[
q(y)\le q(y-\operatorname{sgn}(y)d/2)
\le q(y-d/2)+q(y+d/2).
\]
Thus \(B_i\le S_i\) for every included consecutive pair. Its endpoint-background sum is a subsum of \(Z_\varepsilon\), proving (2).

**Why this order matters.** One cannot simply drop consecutiveness from the midpoint-weighted sum: a third point can then approach the midpoint while staying away from both endpoints, where \(\rho_3\) need not vanish. The inverse-square midpoint weight would have a nonintegrable singularity. The endpoint majorant avoids this invalid enlargement.

### 4. The selected background is tight at scale \(N^2\)

The checked primary extreme-gap input is Feng–Wei, Theorem 1.1 and Corollary 1.1, printed page 4, specialized **only to CUE**. Their periodic definition includes the wrap gap, and \(A_2=1/(24\pi)\). Hence
\[
\mathbb P(N^{4/3}\delta_N^{\min}>L)
\longrightarrow\exp\left(-\frac{L^3}{72\pi}\right)
\quad(L>0).
\tag{7}
\]
See [Feng–Wei, arXiv:1806.01555v2](https://arxiv.org/abs/1806.01555v2). No finite-N uniform tail estimate is asserted.

On the event \(\delta_N^{\min}\le L N^{-4/3}\), the selected \(B_N\) is one nonnegative summand in (3). Therefore, for every fixed \(L,K>0\),
\[
\limsup_{N\to\infty}\mathbb P(B_N/N^2>K)
\le e^{-L^3/(72\pi)}+\frac{L^3}{18K}.
\tag{8}
\]
Choosing \(L\) first and then \(K\) proves
\[
\boxed{B_N/N^2=O_{\mathbb P}(1).}
\tag{9}
\]
For example, choosing the fixed value \(L^3=72\pi\log K\), for each \(K>1\), gives the asymptotic tail bound \((1+4\pi\log K)/K\) on the right side of (8). This is a limit-superior bound, not a quantitative convergence rate in \(N\), and it is not a uniform first-moment estimate for \(B_N/N^2\). The entire argument avoids conditioning on which pair is smallest.

### 5. Quantitative consequence for the already-defined finite heat flow

Let
\[
P_N(z)=\det(zI-U_N)=\sum_{j=0}^N a_jz^j,\qquad
P_{N,s}(z)=\sum_{j=0}^Na_j e^{sj(N-j)}z^j,
\]
and define the first discriminant time
\[
D_N=\inf\{s>0:\operatorname{disc}(P_{N,s})=0\}.
\]
This is the finite circular scalar-heat deformation, not stochastic Dyson Brownian motion and not a representation of the true zeta flow.

The exact deterministic statement already audited in Round 2 uses the same midpoint background \(B_N\). For
\[
\eta_N=(\delta_N^{\min})^2(B_N+1),\quad
K_0=16384,\quad\eta_0=1/524288,
\]
it proves
\[
\frac{(\delta_N^{\min})^2}{8}\le D_N
\le(\delta_N^{\min})^2\left(\frac18+K_0\eta_N\right)
\qquad\hbox{if }\eta_N\le\eta_0.
\tag{10}
\]
The source is `research-round2/galilean-proof-audit.md`, Sections 1–5, pinned in the source receipt. Its constants are independent of \(N\) and of the common background drift. Its proof controls the real Gaussian tails after an exact Galilean conjugation and keeps both moving interval boundaries nonzero throughout the comparison time. It therefore does not require a new unproved dynamic-background stability assumption. A multiple zero somewhere else earlier only helps its upper bound.

Put \(X_N=N^{4/3}\delta_N^{\min}\) and \(Y_N=B_N/N^2\). Equations (7) and (9) imply both are tight, without requiring independence. Thus
\[
N^{2/3}\eta_N=X_N^2(Y_N+N^{-2})=O_{\mathbb P}(1),
\quad\mathbb P(\eta_N\le\eta_0)\to1.
\]
Applying (10) on this event proves the strengthened estimate
\[
\boxed{\quad
\frac{8D_N}{(\delta_N^{\min})^2}-1
=O_{\mathbb P}(N^{-2/3}).
\quad}
\tag{11}
\]
The difference is nonnegative even outside the small-\(\eta_N\) event: the unconditional scalar comparison gives \(D_N\ge-\log\cos(\delta_N^{\min}/2)\ge(\delta_N^{\min})^2/8\). Here \(\delta_N^{\min}<\pi\) almost surely for \(N\ge2\), deterministically for \(N\ge3\). This is a tightness-scale rate for the approximation error, not a distributional convergence rate or a claim about its limiting correction law. Equivalently,
\(D_N-(\delta_N^{\min})^2/8=O_{\mathbb P}(N^{-10/3})\).
For completeness, \(D_N\) is finite almost surely: a generic CUE characteristic polynomial has a nonzero interior coefficient, whose prescribed exponential growth eventually exceeds the bounded coefficient size possible for a polynomial with all roots on the circle. Before a first collision, self-inversive symmetry keeps its simple roots on the circle. The exceptional exactly rotation-invariant polynomial has probability zero.

The qualitative limiting depth law already recorded in Round 1 follows again. We do not label it a new result of this round, and we do not infer an error rate for that limiting law from (11).

### 6. What this does and does not settle

The new finite-N estimate controls the initial inverse-square background attached to the actual selected minimum. Together with an existing fully quantified deterministic lemma it removes a possible missing-stability premise in this finite CUE lane and sharpens its probabilistic approximation rate.

A theorem identifying a limiting conditional background distribution, an asymptotic mean of that background, an optimal error exponent or coefficient, general-beta analogues, and any arithmetic transfer are outside the proved result. For true zeta zeros, the isolated-small-pair and positive-density arithmetic obligations documented in Round 2 remain open. CUE's three-point determinant is an actual random-matrix input, not an available identity for zeta zeros.

The companion check records exact normalization/exponent arithmetic and the \(N=3\) determinant-integral identity. It is not a grid scan, a Monte Carlo test, or a formal verification of this proof. Independent/coordinator review must be recorded separately without changing the eventual frozen author snapshot.


<a id="report-61"></a>

# Current report 61: Independent review: selected CUE background and the finite heat rate

**Collection:** R14 — smooth Type I removal and quantitative finite CUE heat.

**Source:** [research/dyson/round14/cue-selected-background/INDEPENDENT_REVIEW_EUCLID.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/cue-selected-background/INDEPENDENT_REVIEW_EUCLID.md).

**SHA-256:** `54f03e2f3f2636392fd630a19900dddb81d56e1fcffa7a656a7af36c4f1a6018`. **Git blob:** `57db6633b90fc1154f25a9fccb27ce070a054f53`. **Original bytes:** 8634.

## Independent review: selected CUE background and the finite heat rate

Date: 2026-09-05. Reviewer: Euclid, the independent conductor-arithmetic agent.

**Decision: accepted for the stated finite-CUE conclusions.** No mathematical defect was found in the selected-background bound, its exact constant, the circular geometry, or the stated probabilistic consequence of the pinned deterministic lemma. This is an ordinary mathematical review, not formal verification or a novelty assessment.

Reviewed author file:
SELECTED_CUE_BACKGROUND.md

SHA-256:
fbc67828d13534d8d0b4ac1f742a639b282dd93a3f7cb635291f8cdbb651c0a5.

The hash was independently recomputed. No author source, numerical check, receipt or previous-round file was modified or rerun.

### 1. The three-point bound and the constant \(1/18\)

The CUE kernel is normalized against ordinary angular Lebesgue measure:
\[
K_N(x,y)=\frac1{2\pi}\sum_{m=0}^{N-1}e^{im(x-y)}.
\]
The Gram-vector norms used in the proof are therefore
\[
A=\frac N{2\pi},\qquad
D=\frac1{2\pi}\sum_{m=0}^{N-1}m^2
\le\frac{N^3}{6\pi}.
\]
The two-point estimate \(ADd^2\) follows by subtracting the first vector from the second; the third-point Gram residual is bounded both by \(A\) and by \(D r(z)^2\). Thus the two coefficients before weakening are exactly
\[
\frac{N^5d^2}{24\pi^3},
\qquad
\frac{N^7d^2r(z)^2}{72\pi^3}.
\]
Replacing the second branch by the weaker coefficient \(1/24\) is legitimate. The displayed minimum bound in the author report follows. For \(N=2\), the rank-three determinant vanishes, so no exceptional formula is required.

The singular integration uses both halves of the circle:
\[
\int_{\mathbb T}q(z)\min(1,N^2r(z)^2)\,dz
\le\frac{\pi^2}{2}
\left[N+N-\frac1\pi\right]\le\pi^2N.
\]
This gives \(N^6d^2/(24\pi)\) for one endpoint. Adding the two endpoints, integrating the starting angle over length \(2\pi\), and integrating \(d^2\) over \((0,\varepsilon]\) gives
\[
\frac1{24}\times2\times2\times\frac13=\frac1{18}.
\]
All powers of \(\pi\) cancel. There is no missing \(1/2\): the determinant is the factorial density of ordered distinct triples, and the oriented short-pair enumeration is the one actually integrated.

The nonnegative integrand makes the initial application of Tonelli valid. The obtained upper bound then proves its finiteness.

### 2. Midpoints, endpoints and circular wrap

The midpoint singularity is handled in the correct order. Only a consecutive pair is replaced by its endpoint majorant; the resulting endpoint-weighted quantity can then be enlarged to all short ordered pairs. Enlarging the midpoint-weighted sum first would not be valid, and the report explicitly avoids that step.

For a consecutive gap with endpoints \(\pm d/2\), \(d\le\pi\), every other point has a midpoint-centered lift \(y\in[-\pi,\pi]\) with \(|y|\ge d/2\). Its distance to the endpoint on its own side is exactly \(|y|-d/2\), lying in \([0,\pi]\). Monotonicity of \(1/(4\sin^2(r/2))\) on that interval therefore gives the claimed midpoint majorant. Third-point coincidence with an endpoint is excluded by the simple-point configuration.

At \(y=\pi\) or \(-\pi\), either admissible lift leads to the same periodic value; choosing a side creates no discontinuity in the inequality. The short oriented pair crossing the original angle cut is included once under the periodic change of variables. Antipodal pair ambiguity has probability zero; the non-strict endpoint \(\varepsilon=\pi\) creates no expectation term.

The integer-frequency kernel is genuinely periodic. Hence an antiperiodic gauge of a sine-kernel representation cannot introduce an extra sign or omit a wrap pair in this proof.

### 3. Selection of the minimum and the extreme-gap normalization

I checked the stated primary normalization against the local text of Feng–Wei, arXiv:1806.01555v2, printed p.4. Its gap process uses the periodic convention
\(\theta_{i+N}=\theta_i+2\pi\). At \(\beta=2\), \(A_2=1/(24\pi)\), and Corollary 1.1 scales the smallest gap by
\[
N^{4/3}(A_2/3)^{1/3}.
\]
Thus the author report's tail
\[
\mathbb P(N^{4/3}\delta_N^{\min}>L)
\longrightarrow e^{-L^3/(72\pi)}
\]
has the correct angular normalization.

On the event that the selected gap is at most \(LN^{-4/3}\), its background is one nonnegative term of the truncated sum. Scaling the finite-\(N\) bound gives exactly \(L^3/18\). Markov's inequality then proves
\[
\limsup_N\mathbb P(B_N/N^2>K)
\le e^{-L^3/(72\pi)}+\frac{L^3}{18K}.
\]
Choosing \(L\) first and \(K\) second proves tightness. Equivalently, for each fixed \(K>1\), taking \(L^3=72\pi\log K\) yields the stated asymptotic upper tail \((1+4\pi\log K)/K\).

There is no conditioning on the identity of the minimum pair. The proof does not claim a finite-\(N\) convergence rate, a limiting background law, or a uniform bound for \(\mathbb E(B_N/N^2)\). These limitations are correctly stated.

### 4. Matching the pinned Galilean lemma

I read Sections 1–5 of the pinned deterministic dependency:

research-round2/galilean-proof-audit.md

SHA-256:
c85684fe873c19c193a81d3d16cde2507f10cf6753324ce31eda99b14672a2da.

The hypotheses match the CUE application exactly:

- A degree-\(N\) polynomial has \(N\) distinct roots on the unit circle, with fixed nonzero leading and constant coefficients.
- The coefficient deformation is \(a_j\mapsto a_j e^{s j(N-j)}\), with the same time parameter \(s\).
- The chosen pair realizes the smallest circular angular gap \(\delta\).
- Its initial background is exactly
  \(B=\frac14\sum_{\text{outside pair}}\csc^2(\theta_k/2)\), measured from the midpoint after rotation. This equals the author's \(B_N\), with no additional endpoint or scaling factor.
- The smallness condition is \(\eta=\delta^2(B+1)\le1/524288\).

The dependency proves the bound with \(K_0=16384\) independent of \(N\) and of the common logarithmic drift. Its real-line Gaussian estimate and moving-boundary argument are already uniform in the drift. The new CUE application therefore does not require a further dynamic-background-stability hypothesis.

The scalar lower comparison is valid whenever the smallest initial gap is \(<\pi\). It gives
\[
D_N\ge-\log\cos(\delta/2)\ge\delta^2/8.
\]
For \(N\ge3\), the minimum is at most \(2\pi/N<\pi\); for \(N=2\), equality \(\delta=\pi\) has probability zero. Consequently the author's nonnegativity assertion outside the good smallness event is justified as well.

The first discriminant time may be caused by another pair. That possibility only strengthens the deterministic upper bound; the application does not assume that the initially smallest pair is the first to collide.

### 5. The \(N^{-2/3}\) rate and its precise meaning

Let \(X_N=N^{4/3}\delta_N^{\min}\) and \(Y_N=B_N/N^2\). Both are tight, and
\[
N^{2/3}\eta_N=X_N^2(Y_N+N^{-2}).
\]
Products of tight random variables are tight without independence. Thus \(\eta_N=O_{\mathbb P}(N^{-2/3})\), and its fixed deterministic smallness condition holds with probability tending to one.

On this event, the pinned lemma gives
\[
0\le \frac{8D_N}{(\delta_N^{\min})^2}-1
\le 8K_0\eta_N.
\]
The exceptional event has probability tending to zero, which is sufficient for the asserted full \(O_{\mathbb P}(N^{-2/3})\) statement. No bound on the magnitude of the error on that exceptional event is needed for tightness.

The almost-sure finiteness remark is consistent: any nonzero interior coefficient eventually violates its bounded unit-circle coefficient size under the stated exponential deformation. Simple self-inversive roots cannot leave the circle before a collision. The exceptional polynomial with all interior coefficients zero has CUE probability zero.

Multiplying the relative error by the tight factor \(N^{8/3}(\delta_N^{\min})^2\) yields the absolute error
\(O_{\mathbb P}(N^{-10/3})\). This is an approximation-error rate, not a rate of convergence to the limiting depth distribution. The report keeps that distinction.

### 6. Verified provenance and remaining scope

Independently recomputed primary hashes:

- Feng–Wei PDF:
  af6c78625ceb76b422fb89ba0f5d98f18c8749ae922244fe386dbfb0133dbce7.
- Its extracted text:
  6b24cd80cede5d71415c4f1cfa527a2c0ef8fd23752549c7455a85945f777ea5.

The review read the exact finite-\(N\) proof, the relevant primary text and the deterministic dependency. It did not rerun the companion script or add a numerical scan.

Acceptance is restricted to the stated CUE proposition, tightness and finite scalar-heat approximation. No general-\(\beta\) determinant bound, true-zeta flow statement, arithmetic transfer, optimal-rate claim or historical-conjecture conclusion follows from this review.


<a id="report-62"></a>

# Current report 62: Independent root review: two bounded R14 advances

**Collection:** R14 — smooth Type I removal and quantitative finite CUE heat.

**Source:** [research/dyson/round14/INDEPENDENT_ROOT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/INDEPENDENT_ROOT_REVIEW.md).

**SHA-256:** `8350088f7454529e209379e8f4692a78be6cc49fe1c67257a053a5065112bf3e`. **Git blob:** `6379a8ce78ba33a80ae923da44076ac4d3dbb198`. **Original bytes:** 5564.

## Independent root review: two bounded R14 advances

Date: 2026-09-05. Reviewer: root Astra. Both complete author reports were read and their proofs checked independently. This review is not formal verification, a global novelty assessment or a claim about the full zeta covariance.

### Actual Type I component

Reviewed `smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md`, SHA-256 `d6143f19ddf006a1acc833ecd2e5265bffb35817930cfeaa4f4e4b973af7c849`.

The identity Lambda=mu*log, including n=1, makes the split at a real cutoff U exact. After n=rs, a nonunit r contributes to neither a primitive residue progression nor its principal sum. For a unit r the required residue is h times its inverse. No discarded nonunit main term remains.

The profile displayed in equation (13) uses the actual n-h kernel. Both a-factors have the negative-three-halves branch because the compact chi support forces n-h>X and n>X. The integral representation in (14) removes the apparent small-denominator phase singularity. Its derivatives, the compact support and the two logarithms give the claimed uniform O_J(log²X) seminorms for all retained r,h,q. Constants can depend on fixed derivative order and cutoff separation; they do not silently depend on T.

Poisson summation has the positive progression phase e(kb/q) for the stipulated negative-sign Fourier transform. Its zero frequency cancels exactly against the primitive mean, including c_q(0)=phi(q). The nonzero modes are bounded by (L/q)(q/L)^J log²X. Summing q^(J-1) and r^(J-1), and the actual h weights, gives HX(UQ/X)^J log²X without any omitted factor of q or H.

The explicit choice U=X^.4,J=4 has exponent 1711/1750 and margin 39/1750 below one. More generally the uniform proof applies to every fixed positive separation U<=X^(.477-eta), with fixed J eta>2/7. There is no uniform assertion as eta tends to zero. The proof of the recalled Heath--Brown identity is algebraically valid, and the criterion concerns an individual smooth unrestricted variable; a long product does not automatically satisfy it.

Accepted as an unconditional classical Poisson application to this programme's exact discrepancy. The signed Lambda_{>U} term remains exact and unestimated. Its cofactor can be small. Removing this component supplies neither an inequality for the full Lambda sum nor a solution of Montgomery's conjecture.

### Selected CUE background and finite heat-depth error

Reviewed `cue-selected-background/SELECTED_CUE_BACKGROUND.md`, SHA-256 `fbc67828d13534d8d0b4ac1f742a639b282dd93a3f7cb635291f8cdbb651c0a5`, and reread Sections 1--5 of the existing quantified Galilean audit.

For the exact finite CUE Gram representation, ||phi||²=N/(2pi) and ||phi'||²<=N³/(6pi). The two-point determinant is bounded by AD d². Projecting the third vector off the first two gives both A and D r(z)² bounds. Their minimum yields precisely the stated rho3 upper bound N^5 d²/(24pi³) min(1,N²r(z)²).

The singular endpoint integral is finite because the retained r(z)² factor cancels it. The elementary bound q(z)<=pi²/(4r(z)²) and the split r=1/N give an integral at most pi²N. Two endpoints, the 2pi anchor integral and integration of d² from zero to epsilon give N^6 epsilon³/18. These are ordered factorial correlations, so there is no extra half factor. The periodic orientation includes the wrap gap.

The midpoint comparison is made only for consecutive pairs: every third point is outside the open short arc and is at least as close to one endpoint as to the midpoint. Dropping consecutiveness only after replacing by endpoint weights avoids a divergent midpoint integral. The selected minimum requires no conditional density: on delta_min<=L N^(-4/3), its nonnegative background is one of the counted summands. Markov followed by the fixed-L minimum-gap tail gives B_min/N² tightness. The order of limits is valid and does not assume a uniform finite-N tail estimate.

The pinned deterministic lemma uses exactly this midpoint B and controls the heat product after its Galilean conjugation, with constants independent of N and drift. Since delta_min=N^(-4/3) times a tight variable, eta=delta_min²(B+1)=O_p(N^(-2/3)). The lemma's small-eta event has probability tending to one. This proves 8D/delta_min²-1=O_p(N^(-2/3)), and multiplication by the tight squared gap gives absolute difference O_p(N^(-10/3)). No independence between the gap and background is required.

The scalar minimum-gap lower comparison is available without the small-eta condition when delta_min<pi, which holds almost surely for CUE N>=2. Thus the stated nonnegativity is consistent. Finiteness of D for almost every CUE polynomial follows from growth of an interior coefficient and self-inversive root tracking before a collision, as stated in the report.

Accepted as an ordinary finite-CUE result based on the checked classical extreme-gap input and the existing audited deterministic lemma. This is an approximation error in probability, not a rate of convergence to the limiting depth distribution. It is not a stochastic DBM theorem, a general-beta result or an identity available for zeta zeros.

### Remaining work

Both results are appropriate to preserve as concrete progress: one removes an exact actual arithmetic component, and the other strengthens a finite random-matrix heat-flow comparison. The full signed arithmetic remainder, the desired out-of-band zeta correlation inequality and all famous-conjecture targets remain open. Separate agent reviews and bounded algebra replays are retained alongside this review.


<a id="report-63"></a>

# Current report 63: Fable PR11 snapshot 89393d5: separate intake and two-sided arithmetic audit

**Collection:** Fable intake — 89393d5 and 2073028, separate reviewed corrections.

**Source:** [fable/reviews/pr11-89393d5/INTAKE_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-89393d5/INTAKE_REVIEW.md).

**SHA-256:** `6e5a08438cdf6abc3dbffdab699374f72738d894a472d47c6d78fa4db91276eb`. **Git blob:** `bc6a8343f54e80e77875a02237c7f41705256e3b`. **Original bytes:** 6968.

## Fable PR11 snapshot 89393d5: separate intake and two-sided arithmetic audit

Date: 2026-09-05. Source: [Alpha-devbox commit 89393d5da61a45561ed199330c5b836f47fcd629](https://github.com/galpha-ai/Alpha-devbox/commit/89393d5da61a45561ed199330c5b836f47fcd629). This review accepts a source snapshot and reports specific checks. It does not approve every mathematical claim in that snapshot or establish a new zeta-gap result.

### What arrived

The [new snapshot](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/tree/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/snapshots/89393d5/files) contains 141 files, 1,062,904 bytes, preserved verbatim. Its [manifest](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/snapshots/89393d5/SOURCE_MANIFEST.json) pins every file. The earlier 81-file a408e705 mirror remains unchanged. The retained local source tarball has 3,104,082 bytes and SHA256 `9ca9fd9c7b907512db107a59e8f2d8caf5489887a532a55b4d6503bea42f1976`.

Three source commits recovered six proposer reports, added the C-beta-E background and F1 arithmetic-transfer drafts, then added two F1 refuters. The recovered claims include Theorem B repair, CUE background, Level B, structure, H2 and finite-sum diagnostics. These reports are now present; the earlier snapshot's absent-file assessment must not be applied to them. Presence is not proof acceptance. The source's own claim ledger describes several as awaiting refutation, and its last commit message says an F1 repair is in progress. That message is not a completed repair receipt.

This bounded intake examines F1/F2 arithmetic and reproduces the two F1 refuters. The [separate background and boundary audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-89393d5/BACKGROUND_AND_BOUNDARY_REVIEW.md) records additional specific objections; neither review is a full acceptance audit of the heat-flow drafts. No new Claude session, model request, automated next task, or large prime computation was launched.

### The valid F1 objection, and the refuter's own sign error

The proposer text gives the leading coefficient of Pi_4 as 6a^2, then concludes m4=a^2+6a after adding Pi_2^2. The two expressions are inconsistent. The correct leading terms are

\[
\Pi_2^2\sim a^2\varepsilon^{-4},\qquad
\Pi_4\sim 6a\varepsilon^{-4},\qquad
m_4=a^2+6a.
\]

To see the second coefficient, the local inclusion probability has rho_p=a p^(-s)+O(p^(-2s)). Thus rho_p(1-rho_p) has the same leading a p^(-s). The sum of (log p)^4 p^(-s) has leading 6/(s-1)^4; prime powers and local quadratic errors are analytic near s=1. This supplies a single factor a. The proposer's script assigns the correct final m4 as a literal; that assignment does not verify its incorrect written intermediate coefficient. The resulting conditional moment expression (a+6)v^4/((a+1)(a+2)(a+3)) is consistent with the corrected coefficient.

However, the refuter's numerical probe also has an error. Its function zz3 is the third derivative of zeta'/zeta. Since zeta'/zeta(1+eps)=-1/eps+analytic, zz3 has leading **+6/eps^4**. The script evaluates **-zz3*eps^4** and labels it as tending to +6. All three saved values are actually -6. The subsequent coefficient is separately assigned as 6a and does not depend on this bad probe.

The [independent correction](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-89393d5/check_pole_coefficient.py) differentiates the pole using exact rational algebra and separately runs the correctly signed high-precision diagnostic. The exact pole algebra supplies the coefficient; the numerical probe is a secondary sign check. This correction preserves the refuter's valid objection to the proposer while rejecting its faulty numerical verification. The original scripts and outputs are untouched.

### The quoted normalization table mixes different v values

For fixed v=1, the stored two-term normalization ratios are:

| L | Actual v=1 ratio |
|---:|---:|
| 10^4 | 1.0001888352957300 |
| 10^5 | 1.0001190371666680 |
| 10^6 | 1.0000833930992132 |
| 10^7 | 1.0000616581233717 |

The proposer's first two quoted values, 1.002005 and 1.000396, come from other v rows at L=10^4, not this fixed-v sequence. The last two entries were correctly transcribed. The refuter detects this mismatch and the bounded replay confirms it.

The [replay receipt](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-89393d5/recheck.json) records ten checks with three expected narrative failures. All pass/fail flags match the saved refuter. The rigour output matches exactly, including its sign bug. The insertion calculation at L=1000 agrees to less than 10^-12; small platform-level floating differences are explicitly retained in the receipt and log. A receipt labelled successful replay does not turn the three failed assertions into passes. The check based only on a literal source formula string is a source-presence check, not an independent proof of the operator contract.

### What the finite drift does and does not establish

F2's stored fixed-vector margins remain negative, from about -0.05199 at L=10^3 to -0.03124 at L=10^7. Its continuum value is approximately -0.014662375473371, consistent with Astra's independently certified fixed-vector limit. The finite data were received as diagnostics; this intake does not rerun the large computations or upgrade them to interval certificates.

Slow prime-discreteness drift, even through 10^8 in a semi-continuum diagnostic, does not refute an asymptotic O(1/log L) bound without a proved constant and threshold. Nor can a few competing curve fits establish the rate. Large finite differences between full and clean operators do not contradict a proved vanishing difference in a fixed-family limit.

F1/F2 were working from the earlier Astra input checkpoint 97df092. Subsequent Astra work supplies a [fixed-family arithmetic transfer proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/symmetric_prime_arithmetic_transfer.md) and [independent review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/reports/symmetric_prime_transfer_independent_review.md), with joint weak limits and bounded-operator control. For that fixed family an o(1) limit suffices; an explicit O(1/log L) rate is not logically required. The F1 prose cannot be used to reopen that specific gap solely because its own rate proof is unfinished. Conversely, the fixed-family proof does not validate arbitrary growing feature families or claim that this negative trial refutes AH.

### Reproduction and next use

From the public repository root:

```text
OPENBLAS_NUM_THREADS=1 python3 fable/reviews/pr11-89393d5/recheck.py
```

This verifies all source hashes, copies the complete snapshot to a temporary directory, runs only the two named refuters (bounded at L<=10^6), and runs the separate pole check. Logs and the structured receipt remain beside this review. The code was read before execution; no model call or network access is part of these checks. Imported proposers' large main blocks are not executed.

For collaboration, the useful corrections are the Pi_4 coefficient, the refuter sign, the fixed-v table, and the distinction between fixed-family convergence and a quantitative rate. A repaired draft needs its own new commit and review. Remaining RMT/heat-flow proposer reports require separate mathematical audits; this intake gives no blanket endorsement.


<a id="report-64"></a>

# Current report 64: Independent background and boundary objections to the same Fable snapshot

**Collection:** Fable intake — 89393d5 and 2073028, separate reviewed corrections.

**Source:** [fable/reviews/pr11-89393d5/BACKGROUND_AND_BOUNDARY_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-89393d5/BACKGROUND_AND_BOUNDARY_REVIEW.md).

**SHA-256:** `336ae8258325f935c8613659e4921c8ce610193fbdde54d3fca8e0aafa8ada61`. **Git blob:** `04708ef3d0f1fe32b033961794c89f73c0948a7d`. **Original bytes:** 6033.

## Independent background and boundary objections to the same Fable snapshot

Date: 2026-09-05. These findings came from the existing Astra coordination task's independent mathematical intake of commit `89393d5da61a45561ed199330c5b836f47fcd629`. Root checked the quoted source passages and the elementary algebra/counterexamples below. The original proposer files remain unchanged. This is a negative scope audit, not a complete acceptance review of every earlier constant or lemma.

### 1. A reversed inequality in the uniform CUE gap tail

In `r1_cue_background.md`, Proposition 3.3 regime 2 has L>4N^(1/3) and a preceding bound 16.47/N. Its next step replaces this by 16.47*64/L^3 as an upper bound. The inequality goes in the opposite direction: L^3>64N implies 1/N>64/L^3. The displayed uniform constant 1054, and the downstream constants 1055 derived from it, are not established by this proof as written.

A possible elementary repair is to use the deterministic fact delta_min<=2pi/N for N points on a circle of circumference 2pi. The event is empty for L>=2pi N^(1/3). In the remaining part of regime 2, 1/N<(2pi)^3/L^3, so the preceding bound implies a constant below 4100 in place of 1054. If all earlier estimates are accepted, a conservative 4101 can propagate through the stated stiffness tails. This repair preserves the qualitative tightness route. This review has not certified all the preceding numerical constants, and does not silently edit the source or label 1055 verified.

### 2. The C-beta-E local density hypothesis has the wrong scaling

The displayed BB-LD compares the n-point correlation density to N^n times the unscaled angular Vandermonde to power beta with constants independent of N. It is already false for beta=2, n=2. The exact CUE formula is

\[
\rho_2(\theta,\theta+d)
=\frac1{4\pi^2}\left[N^2-\left(\frac{\sin(Nd/2)}{\sin(d/2)}\right)^2\right]
=\frac{N^2(N^2-1)}{48\pi^2}d^2+O_N(d^4).
\]

Hence rho_2/(N^2 d^2) grows like N^2, contradicting an N-independent comparison. A microscopic statement must include scaled distances Nd, or the corresponding prefactor N^(n+beta*n*(n-1)/2), and specify its domain and the remaining marginal bounds. The source's later attempts at revised exponent counting do not fix the false starting definition merely by calling its normalization local. No general-beta density theorem is supplied by this audit.

The source's partition function formula is also wrong in its stated Lebesgue-angle convention, although it is marked unused. At N=2,beta=2 direct integration of 2-2cos(theta_1-theta_2) gives 2(2pi)^2. The displayed product formula gives 4(2pi)^2. This is an elementary normalization check, independent of a general Selberg integral.

### 3. Uniform one-point intensity does not control a selected close pair

The C-beta-E report attempts to obtain the one-sided density event needed for the selected pair from rho_1=N/(2pi). That implication is invalid. Take a deterministic cluster of N distinct angles in an arbitrarily short arc, with a unique smallest pair gap, and rotate the entire cluster by a uniform angle. The one-point intensity is exactly N/(2pi), because each labelled point is marginally uniform. Every realization still contains the same tight cluster. The selected pair's nearby counting function, and its sum of inverse-square distances to other points, can be arbitrarily large.

This example is not C-beta-E. It shows precisely that the claimed one-point input is insufficient. A proof for C-beta-E must use its additional correlation structure, Palm estimates, or an independently proved uniform density event. Static rotational invariance supplies none of these by itself. Claims A3(b)/(c) cannot be accepted from the stated one-point argument.

The assertion that DBM is the only known route to the required density theorem is a methodological opinion. It is not a mathematical proposition with status proved, and this audit makes no exhaustive claim about the literature.

### 4. Static stiffness does not automatically persist to collision

The CUE depth Theorem 2 explicitly assumes B*-0. The Theorem B repair requires stability on a time window and its kappa_0 condition. Tightness of S*(0)/N^2 is useful but is not the same assertion as a bound along the selected pair's evolution. The arc-sum lower bound in Lemma W may support a proof; its sufficient event H_C still has to be established for the selected pair before importing the depth conclusion.

The current intake therefore preserves both the conditional theorem and its missing event. It does not relabel the CUE or general-beta depth law as unconditional merely because a static background estimate was proposed.

### 5. A periodized window has an artificial gap

In `r1_levelB_barrier.md` the periodized version claims that a small normalized depth implies an actual zeta gap below 1/2 without additional hypotheses. Periodizing a finite real window of length H_T introduces the wrap gap H_T-(last-first). The smallest circle gap can be this artificial gap, with no small consecutive gap among the original zeros. A circle depth theorem alone identifies a circle gap, not necessarily a genuine zeta gap.

For example, points 0,1,...,n-1 in a window of length n-1+epsilon have all internal gaps one and circular wrap gap epsilon. This does not make a statement about actual zeta windows; it disproves the unqualified finite-window inference. A non-wrap witness or a valid boundary construction is needed for transfer. The actual-flow non-return/truncation assumptions must also remain explicit.

### Accepted use

The reports contain useful candidate lemmas and clearly exposed conditional inputs. The objections above identify specific places needing repair, not a refutation of every heat-flow idea. Until repaired and independently reviewed, these source status labels must not be used to claim a C-beta-E universality theorem, a true-zeta depth bound, or AH failure. The present main line remains the independently reviewed actual-prime estimates in Rounds 10 and 11.


<a id="report-65"></a>

# Current report 65: Fable 2073028: repaired arithmetic, finite Fock bound and retained gaps

**Collection:** Fable intake — 89393d5 and 2073028, separate reviewed corrections.

**Source:** [fable/reviews/pr11-2073028/INTAKE_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-2073028/INTAKE_REVIEW.md).

**SHA-256:** `51111bc72197254e92d3120f36b4f1278b8456eedd092c0d1a1362fe7b092f05`. **Git blob:** `260c5e94bbb68ae8c6b64ea2899e0825d0c75510`. **Original bytes:** 2671.

## Fable 2073028: repaired arithmetic, finite Fock bound and retained gaps

Date: 2026-09-05. Source: Alpha-devbox PR11 commit `20730285c8f9a81539e0662c6e015023c2ed107a`. The 160 received public research files are a separate verbatim snapshot. Earlier snapshots and their reviews remain unchanged.

Two previous F1 objections are repaired: the leading coefficient is now Pi4~6a epsilon^-4 and the fixed-v table now uses its actual v=1 rows. The unchanged refuter still tests the negative of the derivative that tends to positive six. The new finite prime sum is honestly inconclusive; its cutoff is explained by the independently reviewed incomplete-gamma limit in `F1_REPAIR_AND_CUTOFF_REVIEW.md`.

The F3 claim that the field norm is infinite is false for the stipulated g and mass cutoff. `F3_MASS_CUTOFF_BOUND.md` gives a direct, independently checked sector proof: ||K||<=2 integral_0^1 |g(u)|²/u² du. For g=2sin(pi u/2), this is 4pi Si(pi)-8, approximately 15.2721. It also uniformly bounds every literal finite grid. This finite upper bound is above the desired pi²/2 threshold; it supplies no spectral-wall or arithmetic-transfer theorem. The first-bin constant-basis normalization in the source is not defined in L²(du/u).

The bounded local check imports only the source matrix builder and checks grids M=6,8,10, every occupation coefficient, the finite mass inequality and the scalar integral. It uses floating arithmetic and is not a rigorous eigenvalue enclosure. It does not rerun the large source/refuter sweeps. The source's memory check occurs after matrix allocation, and its ru_maxrss/1024 conversion assumes Linux units; on macOS that is not an MB conversion. No runtime or memory claim is inferred from those old numbers.

The source script and JSON model description also omit 1/sqrt(j) from their opening formula, although the actual builder correctly includes it. All comparisons here use the builder's literal coefficients. Source bytes are preserved rather than silently corrected.

The general-beta background repair is reviewed separately in `CBETA_REPAIR_REVIEW.md`; its unresolved finite-N formulas and conditional flow assumptions must not be treated as a proved CbetaE-to-depth theorem. The older CUE and periodized-zeta objections remain applicable where their source files did not change.

The new contribution is a finite boundedness theorem for the idealized operator and a precise cutoff diagnosis. The separate Astra fixed-family arithmetic transfer remains valid with its currently negative certified margin. Full arithmetic-to-Fock convergence, a sharp spectral threshold and the actual-zeta signed covariance gain remain open.


<a id="report-66"></a>

# Current report 66: Independent audit of the F1 cutoff repair and F3 mass bound

**Collection:** Fable intake — 89393d5 and 2073028, separate reviewed corrections.

**Source:** [fable/reviews/pr11-2073028/F1_F3_INDEPENDENT_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-2073028/F1_F3_INDEPENDENT_AUDIT.md).

**SHA-256:** `5af35dcdf0120a5ab88c398f9b957e89587d7f12ea58ec207eb7e0f2f7d0c929`. **Git blob:** `512db81f74a04cf3f116fdac4780f66e1b1f6b95`. **Original bytes:** 6267.

## Independent audit of the F1 cutoff repair and F3 mass bound

Date: 2026-09-05. Independent reviewer: Astra subagent `yau_flow`. Verdict: **accepted for the stated mathematical scope**. This is a bounded ordinary-proof audit of the two authored notes, not a numerical rerun, an audit of every Fable script, or a proof of an arithmetic-to-Fock limit. The exact reviewed hashes are listed below.

### F1: the local remainder is uniform at the actual parameter

For the standard generalized-divisor Euler coefficients,
\[
d_\ell(p^j)=\frac{(\ell)_j}{j!}
=\prod_{r=1}^j\left(1+\frac{\ell-1}{r}\right),
\qquad \ell=16/15,\quad a=\ell^2=256/225.
\]
The elementary harmonic-sum bound gives
\(d_\ell(p^j)\ll_\ell(j+1)^{1/15}\). Set \(t=p^{-1-\varepsilon}\), with \(0<\varepsilon\le1\); then \(0\le t\le1/2\). Thus
\[
E(t)=\sum_{j\ge1}d_\ell(p^j)^2t^j
=at+O_\ell(t^2),\qquad E(t)=O_\ell(t),
\]
uniformly for every prime and every such \(\varepsilon\). The tail constant is bounded by the finite series
\(\sum_{j\ge2}O_\ell((j+1)^{2/15})2^{-(j-2)}\); it does not depend on the prime cutoff.

Since \(\rho=E/(1+E)\),
\[
\rho(1-\rho)=\frac E{(1+E)^2}=at+O_\ell(t^2).
\tag{A}
\]
Consequently the local error, summed against \((\log p)^4\) over any set \(p\le P\), is bounded uniformly in both \(P\) and \(\varepsilon\) by a constant times
\(\sum_p(\log p)^4p^{-2}<\infty\). Multiplication by \(\varepsilon^4\) makes this error vanish uniformly. No finite-prime experiment is needed to justify this step. In particular the coefficient is \(6a\), not \(6a^2\).

### F1: the PNT argument controls the joint cutoff limit

Put \(g_\varepsilon(x)=(\log x)^3x^{-1-\varepsilon}\). The leading prime sum in (A) is
\[
\sum_{p\le P}(\log p)^4p^{-1-\varepsilon}
=\int_{2^-}^{P}g_\varepsilon(x)\,d\theta(x).
\]
Write \(R(x)=\theta(x)-x\). Given \(\eta>0\), PNT supplies a fixed \(x_0\) such that \(|R(x)|\le\eta x\) for all \(x\ge x_0\). The contribution below \(x_0\), including endpoint conventions, is \(O_{x_0}(1)\) before scaling. For \(P\ge x_0\), integration by parts bounds the scaled upper-part error by
\[
\eta\varepsilon^4\left(P|g_\varepsilon(P)|
+x_0|g_\varepsilon(x_0)|
+\int_{x_0}^{P}x|g_\varepsilon'(x)|\,dx\right).
\tag{B}
\]
These terms are uniform in the arbitrary cutoff:
\[
\varepsilon^4P|g_\varepsilon(P)|
=\varepsilon z^3e^{-z}=O(\varepsilon),\qquad z=\varepsilon\log P,
\]
and, using
\(x|g_\varepsilon'(x)|\le x^{-1-\varepsilon}[3(\log x)^2+(1+\varepsilon)(\log x)^3]\),
\[
\varepsilon^4\int_{x_0}^{P}x|g_\varepsilon'(x)|\,dx
\le 6\varepsilon+6(1+\varepsilon)=6+12\varepsilon.
\tag{C}
\]
Here extending the positive comparison integral to \([1,\infty)\) uses the exact gamma integrals. Letting \(\varepsilon\downarrow0\), then \(\eta\downarrow0\), proves uniform convergence of this scaled PNT error over all cutoffs \(P\ge2\). This is an asymptotic uniformity argument; it supplies no explicit finite-data error constant without a quantitative PNT input.

The main integral is
\[
\frac{\varepsilon^4}{6}\int_2^P(\log x)^3x^{-1-\varepsilon}\,dx
=\frac16\int_{\varepsilon\log2}^{\varepsilon\log P}t^3e^{-t}\,dt.
\]
This proves the authored equation (1) for every joint limit with finite \(z_0\ge0\), including \(P\to\infty\) but \(z_0=0\), and for \(z_0=\infty\). It also permits \(P=\infty\) at each positive \(\varepsilon\), since the original prime sum then converges and the upper integration-by-parts boundary vanishes. If \(P\) remains fixed, the scaled finite sum tends to zero, as the note says. Thus no interchange of an uncontrolled joint limit is hidden in the proof.

The incomplete fraction at \(z_0=1\) is exactly \(1-8/(3e)\), not one. The cutoff warning and the explicit distinction from a finite-point error certificate are justified. I did not rerun the script or independently re-audit all its reported sign/output details.

### F3: discrete bound and first-bin criticism

The stated coefficients give, by exact algebra,
\[
B_M^2=\sum_{j=1}^M\frac{[2\sin(\pi j/(2M))/\sqrt j]^2}{j/M}
=\frac1M\sum_{j=1}^M f(j/M),
\qquad f(u)=\frac{4\sin^2(\pi u/2)}{u^2}.
\]
The function \(f\) extends continuously to \(f(0)=\pi^2\) and decreases on \((0,1]\). Indeed \(\sin x/x\) decreases on \((0,\pi/2]\), since the derivative numerator \(x\cos x-\sin x\) is negative there. The right-endpoint sum is therefore bounded by the integral on each bin, proving the exact inequality
\[
B_M^2\le\int_0^1 f(u)\,du=B_g^2
\]
for every positive integer \(M\), without an asymptotic quadrature claim. Integration by parts also checks the exact expression \(B_g^2=2\pi\operatorname{Si}(\pi)-4\). No certified decimal or spectral enclosure was recomputed.

The continuous sector argument uses \(\|a(g)\Psi\|^2\le B_g^2\langle\Psi,E\Psi\rangle\), not a particle-number bound. On the mass-cutoff space this gives a bounded annihilation map; its adjoint is the compressed creation extension. Different input sectors have different output sectors, so the infinite direct sum introduces no unaccounted cross terms. The resulting \(\|K\|\le2B_g^2\), and the analogous discrete bound, are consistent with the stated conventions.

Finally,
\(\int_0^{1/M}du/u=\infty\). A nonzero constant on the first bin is not an element of the one-particle Hilbert space and cannot be normalized into a piecewise-constant Galerkin basis. A profile proportional to \(g\) is square integrable there because \(g(u)=O(u)\), but that is a different construction and does not identify its compressed mass operator or creation coefficients with the literal grid model. The authored criticism is precise: it rules out the proposed normalization argument, **not** every possible convergent approximation. Uniform boundedness alone proves neither a sharp norm limit nor the desired spectral wall.

### Reviewed snapshots and limits

- `F1_REPAIR_AND_CUTOFF_REVIEW.md` — SHA256 `9f9cd67afbfd7d304f6eb42adcf34391972c54a9f49a2964be1d8fbb176da628`.
- `F3_MASS_CUTOFF_BOUND.md` — SHA256 `112eac7be3ed1294ea47c046eaa93720b170858350115960f8578e0301bb638b`.

Author files were preserved. This review accepts the local Euler remainder, incomplete-gamma limit, discrete mass bound, and first-bin objection. It does not convert the numerical Fock fits into enclosures or establish any new zeta-zero or prime-gap theorem.


<a id="report-67"></a>

# Current report 67: F1 repair: corrected coefficient, surviving sign issue, and cutoff scaling

**Collection:** Fable intake — 89393d5 and 2073028, separate reviewed corrections.

**Source:** [fable/reviews/pr11-2073028/F1_REPAIR_AND_CUTOFF_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-2073028/F1_REPAIR_AND_CUTOFF_REVIEW.md).

**SHA-256:** `9f9cd67afbfd7d304f6eb42adcf34391972c54a9f49a2964be1d8fbb176da628`. **Git blob:** `97d623fc0aaf6d71bb267dfbd1ca963f4e7a1fb8`. **Original bytes:** 4777.

## F1 repair: corrected coefficient, surviving sign issue, and cutoff scaling

Date: 2026-09-05. Review of Fable PR11 commit `20730285c8f9a81539e0662c6e015023c2ed107a`. This review supersedes the corresponding old-version objections only where an actual repair is present. It does not reopen the independently proved Astra fixed-family arithmetic transfer.

### Repairs that are present

The revised F1 text changes Pi_4's leading coefficient from 6a² to 6a and correctly combines it with Pi_2² to obtain a²+6a. The displayed local inclusion probability has leading a p^(-s), while its quadratic correction is summable with log^4 p near s=1. Together with the pole of zeta'/zeta, this is an adequate analytic derivation of the leading coefficient. A numerical experiment is not logically required to close that algebraic point.

The fixed-v normalization sequence is also corrected to the actual v=1 rows. Those two earlier text objections are therefore repaired in this snapshot. Fitting the revised finite values to a log-power rate remains numerical evidence, not a proved uniform error bound.

The new direct prime-sum script is honestly described in the revised report as inconclusive. Its code computes the local tail E=sum_(e>=1)d_ell(p^e)^2 p^(-es) and rho=E/(1+E), which is the correct inclusion probability. The script's opening docstring instead writes rho=1-1/E while defining E without its constant term; that docstring is inconsistent with the code. With E including the constant one, the latter formula would be correct.

### The refuter's probe sign remains wrong

The revised prose still cites the unchanged `refute_F1_rigour.py` probe as an independent confirmation of positive six. It is not: zz3 is the third derivative of zeta'/zeta, so eps^4 zz3 tends to +6 and the script's negative probe tends to -6. Its saved data are indeed -6. The earlier separate Astra correction remains applicable. This does not invalidate the revised analytic coefficient calculation.

### The finite cutoff has a predictable incomplete-gamma limit

The claim that primes merely up to exp(1/eps) resolve the leading fourth-order pole is misleading. Write P for the prime cutoff and z=eps log P. PNT and the local expansion rho_p(1+eps)(1-rho_p(1+eps))=a p^(-1-eps)+O_a(p^(-2-2eps)) give, as eps tends to zero and P tends to infinity with z tending to z_0 in [0,infinity],

\[
\frac{\varepsilon^4}{6a}
\sum_{p\le P}(\log p)^4\rho_p(1+\varepsilon)(1-\rho_p(1+\varepsilon))
\longrightarrow
1-e^{-z_0}\left(1+z_0+\frac{z_0^2}{2}+\frac{z_0^3}{6}\right),
\tag{1}
\]

with the right side interpreted as one at z_0=infinity. In particular exp(1/eps) corresponds to the fixed incomplete fraction at z_0=1, not the whole pole. Resolving most of the leading mass requires eps log P large, not merely P exceeding exp(1/eps).

For completeness, the proof is elementary. The local quadratic error has an absolutely convergent log^4-weighted prime sum for eps near zero, hence vanishes after multiplying by eps^4. For the leading term use Stieltjes summation with theta(x)~x and weight (log x)^3 x^(-1-eps). Splitting at a fixed large x_0 makes the PNT relative error uniformly small above x_0; the lower segment contributes o(1) after scaling. Weighted integration by parts controls that error by a fixed multiple of the full positive gamma integral. Substituting t=eps log x in the main integral gives integral_0^z t^3 e^(-t)dt. Sending the PNT error to zero proves (1), including a bounded or divergent z. If P stays fixed while eps tends to zero, the finite sum is bounded and its scaled value simply tends to zero.

For the actual fixed P=2*10^6, eps=.125 has z about 1.8136, and eps=.0625 has z about .9068. The leading-mass fractions are correspondingly small. The report's assertion that the first cutoff already exceeds P at eps=.125 also contradicts its own parenthetical exp(8)<P. More relevant than that typo is the fourth-order weighting: the transformed density is t^3 exp(-t), whose bulk lies beyond t=1.

Equation (1) is an asymptotic cutoff diagnosis, not a numerical error certificate for the five stored finite points. It explains why that particular experiment is unsuitable as a full-pole confirmation. The existing analytic proof already establishes 6a; larger prime scans are unnecessary for that purpose.

### Scope retained

The latest text still describes its broader M2/coincidence transfer as incomplete. That is its own derivation status. Astra's later independently reviewed fixed-family o(1) transfer remains a separate proved result and does not require the explicit rate missing from F1. Neither a repaired intermediate coefficient nor a finite drift fit gives a positive half-gap margin, a uniform full-operator limit, or a theorem about zeta pair correlation.


<a id="report-68"></a>

# Current report 68: The mass cutoff gives a finite Fock operator bound

**Collection:** Fable intake — 89393d5 and 2073028, separate reviewed corrections.

**Source:** [fable/reviews/pr11-2073028/F3_MASS_CUTOFF_BOUND.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-2073028/F3_MASS_CUTOFF_BOUND.md).

**SHA-256:** `112eac7be3ed1294ea47c046eaa93720b170858350115960f8578e0301bb638b`. **Git blob:** `0c8d3ebc50bfb4d717ac85d05f163788f8b61cc2`. **Original bytes:** 5598.

## The mass cutoff gives a finite Fock operator bound

Date: 2026-09-05. Author: root Astra. This is a self-contained bound for the idealized Fock operator defined in Fable PR11 commit `20730285c8f9a81539e0662c6e015023c2ed107a`. It corrects that report's assertions that the field norm is infinite or that multi-mode boundedness is still open. It does not prove a sharp spectral threshold, convergence of the displayed numerical discretization, or an arithmetic-to-Fock operator limit.

### Statement and exact conventions

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

### Sector proof, including the infinite direct sum

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

### The actual sine kernel and every reported grid

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

### Remaining modelling and numerical limits

The literal c_j coefficients are a quadrature rule, not an exact piecewise-constant Galerkin projection for the measure du/u. In particular the first interval (0,1/M] has infinite du/u mass, so a nonzero constant on that interval cannot be normalized in h. One can instead choose a normalized profile proportional to g on that bin, or an infrared cutoff, but those constructions and their mass-cutoff error require an actual comparison proof. The report's first-bin normalization heuristic does not supply one.

The matrix formula is unambiguous and can be tested as a finite model. Lanczos computations are floating eigensolver results, not exact diagonalization or rigorous enclosures. Stable fits near 4.6456 are numerical evidence only, and agreement with a different trial family does not prove either operator equality or a sharp norm limit. The main arithmetic research remains independent of those unproved transfers.

The earlier Astra Schur majorant search already gives finite but nonsharp upper candidates in a different formulation. No repeat optimization is proposed here. The new contribution of this note is the complete mass-weighted sector argument and its application to the erroneous infinity claim, with the continuous and literal discrete models distinguished.


<a id="report-69"></a>

# Current report 69: Independent follow-up: CβE background repair at 2073028

**Collection:** Fable intake — 89393d5 and 2073028, separate reviewed corrections.

**Source:** [fable/reviews/pr11-2073028/CBETA_REPAIR_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/fable/reviews/pr11-2073028/CBETA_REPAIR_REVIEW.md).

**SHA-256:** `3f60e18e4994a78aeab9b381213c07cf4316005741ceed1ed614a79c1708a4af`. **Git blob:** `76df35f900cef2db52596cc4ad0df66090451412`. **Original bytes:** 9931.

## Independent follow-up: CβE background repair at 2073028

**Verdict: partial repair, not an accepted proof as written.** The missing microscopic powers of N have been identified correctly, and the proposed triple-count exponents can be recovered under an explicit local three-point upper bound. However, the repaired text still contains a false finite-N identity, a false arbitrary-compact comparison, and a false uniform relative-error step. These defects prevent accepting the present BB-LD and Proposition 3.1 proof with their displayed status tags. The conditional replacement below is an ordinary mathematical derivation, not a proof of general-β BB-LD or a new CβE depth theorem.

Reviewed source: the preserved `PR11_2073028-source/r1_cbe_background.md`, with cross-checks against its companion `r1_cue_background.md`. Source SHA-256 values, exact line ranges, and the final review hash are in `CBETA_REPAIR_RECEIPT.json`. No source was edited, no Fable session was invoked, and no Monte Carlo run or large computation was repeated.

### 1. Coverage and change from the previous intake

The earlier independent `research-round3/fable_heat_sync_review.md` audited public SHA `a408e7050fffc74459b3c83fafa5ac03c8b7dea6`, where these written heat reports were absent. Its conclusions about that snapshot's evidence availability remain historically accurate. The present snapshot supplies the reports, including an explicit account of Fable's internal refutations. This follow-up independently checks the repaired mathematics; it does not infer validity from an internal refuter's completion status.

| Issue | Current source lines | Independent conclusion |
|---|---:|---|
| Missing N-rescaling in the old local density comparison | CβE 3–14, 95–109 | The diagnosis is correct. The replacement needs a power-distance comparator or an explicitly restricted sine cutoff. |
| Exact finite-N CUE two-point function | CβE 99–101, 117–123 | Incorrect as written: the sine-kernel limit was substituted for the finite-N kernel. |
| Claimed comparison on any compact rescaled interval | CβE 111–123 | False if the interval reaches 2π. The upper comparison fails at an exact zero of the proposed comparator. |
| Uniform relative replacement of the third distance | CβE 202–218 | False near an endpoint; the quoted N error exponent is also wrong. |
| Triple expectation exponents | CβE 194–253 | Recoverable conditionally by the direct integral in §3 below. Retain the finite-N correction and the order of limits. |
| BB-LD proved for β=1,2,4; general-β universality implication | CβE 137–168 | The claimed proofs are not supplied. Neither the repaired two-point check nor an unquantified universality citation establishes the needed three-point bound. |

### 2. Exact finite-N correction and explicit counterexamples

The companion CUE report, lines 52–55 and 145–146, correctly gives the ordered factorial correlation kernel. With q=Nd and N≥2,

\[
\rho_2(0,d)=\left(\frac N{2\pi}\right)^2
\left[1-\left(\frac{\sin(q/2)}{N\sin(q/(2N))}\right)^2\right].
\]

For fixed q, its normalized limit as N→∞ is \(1-\operatorname{sinc}(q/2)^2\). At fixed finite N, the Taylor coefficient at q=0 is instead

\[
1-\left(\frac{\sin(q/2)}{N\sin(q/(2N))}\right)^2
=\frac{1-N^{-2}}{12}q^2+O_N(q^4).
\]

Consequently the ratio to \((2\sin(q/2))^2\) tends to \((1-N^{-2})/12\), not 1/12. This does not destroy the intended small-q scaling, but it invalidates the claimed exact finite-N verification.

At q=2π, taking d=2π/N, the exact normalized density equals 1, whereas \((2\sin(q/2))^2=0\). This is an admissible circular separation for every N≥2. Thus no finite K gives the claimed **upper** bound there. The lower inequality alone becomes the harmless inequality 0≤ρ₂; it is the two-sided comparison and its bounded-ratio assertion that fail. For q beyond 2π the unsquared sine can also be negative, making its arbitrary-real-β power unsuitable without absolute values.

A minimal definition repair is to use \(\prod(Nd_{ij})^\beta\), with a fixed bounded microscopic cutoff, or to restrict the sine formulation to \(s_0<2\pi\). The application below only needs an upper bound for n=3. For the two-point CUE case on any fixed \(0\le q\le s_0<2\pi\), the corrected finite-N ratio does have uniform positive finite bounds for N≥2: away from q=0 it follows from the strict triangle inequality for the geometric sum, compactness, and convergence to the sine limit; at q=0 the displayed Taylor coefficient is uniformly positive. This observation does not establish the n=3 general-β claim. A two-sided n-point assertion also requires N₀≥n.

For the second error, take an endpoint pair x=0, y=u with u=ε/2, and put the third point at z=−v with v=ε²/w. When ε/w→0, z is closest to x, and

\[
v'=u+v,\qquad \frac{v'}v=1+\frac{w}{2\varepsilon}\longrightarrow\infty.
\]

Hence \(v'=v(1+O(\varepsilon/w))\) cannot hold uniformly on the integration region. Lipschitz continuity of sine controls an absolute error; it cannot supply a relative error at a vanishing sine. Independently, \(\varepsilon/w=(L/c)N^{-1/(\beta+1)}\) is not O(N⁻¹) for any fixed β>0. Finally, the largest distance is bounded by w+ε, not by max(w,ε): the cutoff check must require c+Nε≤s₀. Taking fixed c<s₀ and then sufficiently large N resolves that condition.

### 3. A correct conditional triple estimate

Assume, for every triple with all \(Nd_{ij}\le s_0\), the following **upper** bound:

\[
\rho_3(x,y,z)\le \frac{K}{(2\pi)^3}
N^{3+3\beta}d(x,y)^\beta d(x,z)^\beta d(y,z)^\beta. \tag{U3}
\]

This is the exact input needed here. It follows from a valid restricted sine upper bound using \(2\sin(t/2)\le t\), but is not proved here for general β.

Let T count ordered distinct triples with d(x,y)≤ε and dist(z,{x,y})≤w. Require ε+w<π and N(ε+w)≤s₀. Apply the union bound for the two endpoint neighborhoods, anchor x on the circle, and use signed coordinates u=y−x and v=z−x. Then

\[
\begin{aligned}
\mathbb ET
&\le 2(2\pi)\frac{K N^{3+3\beta}}{(2\pi)^3}
\int_{-\varepsilon}^{\varepsilon}\int_{-w}^{w}
|u|^\beta|v|^\beta(|u|+|v|)^\beta\,dv\,du\\
&=\frac{2K}{\pi^2}N^{3+3\beta}
\int_0^\varepsilon\int_0^w u^\beta v^\beta(u+v)^\beta\,dv\,du. \tag{1}
\end{aligned}
\]

All three factors remain present. The endpoint union bound deliberately overcounts overlapping neighborhoods and is therefore safe.

For a simple bound valid without ε/w tending to zero, replace (u+v)^β by (ε+w)^β in (1). With ε=LN^{−1−1/(β+1)} and w=c/N this gives

\[
\boxed{\mathbb ET\le
\frac{2K}{\pi^2(\beta+1)^2}
L^{\beta+1}c^{\beta+1}
\bigl(c+LN^{-1/(\beta+1)}\bigr)^\beta.} \tag{2}
\]

Thus the intended exponents survive, under (U3), after taking N→∞ at fixed L,c and then c↓0.

For the sharper leading constant put δ=ε/w. Scaling both integration variables in (1) gives

\[
\mathbb ET\le\frac{2K}{\pi^2}L^{\beta+1}c^{2\beta+1}J_\beta(\delta),\qquad
J_\beta(\delta)=\int_0^1\int_0^1s^\beta t^\beta(t+\delta s)^\beta\,dt\,ds.
\]

For 0≤δ≤1,

\[
J_\beta(\delta)\le\frac1{(\beta+1)(2\beta+1)}
\begin{cases}
1+\delta^\beta,&0<\beta\le1,\\
1+\dfrac{\beta2^{\beta-1}(2\beta+1)}{\beta+2}\delta,&\beta\ge1.
\end{cases} \tag{3}
\]

The first case uses subadditivity of t↦t^β. The second uses the mean-value estimate \((t+\delta s)^\beta-t^\beta\le\beta2^{\beta-1}\delta s\) on the unit square. This proves the leading asymptotic bound by integration, without the false pointwise comparison. It also makes its lack of uniformity in c↓0 before N→∞ explicit.

For β=2 the integral in (1) is exactly

\[
\frac{\varepsilon^3w^5}{15}
+\frac{\varepsilon^4w^4}{8}
+\frac{\varepsilon^5w^3}{15}.
\]

Using the stronger CUE coefficient \(\rho_3\le C_3(N)\prod d_{ij}^2\) yields \(16\pi C_3(N)\) times this polynomial, precisely the bound stated in the companion CUE report, lines 226–240. The small symbolic check verifies this integral, the finite-N Taylor coefficients, and the q=2π counterexample; it does not certify general-β density estimates.

If E₁ refers specifically to the closest pair, only \(E_1\subseteq\{T\ge1\}\) is required. The equality asserted at CβE line 246 is generally false, because a different short pair may have a nearby third point. The correct inclusion still gives the intended Markov upper bound.

### 4. Status and remaining scope

Accept the normalization diagnosis and the conditional consequence (1)–(3). Do not accept the current proof of Proposition 3.1 or the “[P] for β∈{1,2,4}” BB-LD row as written. An explicit source or proof for the actual n=3 uniform upper bound remains necessary; β=1,4 are only recalled in the source, and ordinary weak local-process convergence by itself does not justify density control on the shrinking rescaled gap \(N\varepsilon\to0\). The claimed “exactly” equivalent universality formulation at lines 144–148 and its qualitative consequence at lines 164–167 have not been established by this report. This is a missing implication, not a claim that the required bounds are absent from all literature.

This bounded review does not audit Fable's full stiffness/heat-flow argument, the recalled Feng–Wei theorem range, the seed-sweep data, or the methodological claim that DBM is the only route. Those items receive no status upgrade here.

One additional elementary normalization error was noticed but is not used above: at β=2,N=2 the partition function written at lines 58–60 equals \(4(2\pi)^2\), whereas direct integration of \(2-2\cos(\theta_1-\theta_2)\) gives \(2(2\pi)^2\). The source explicitly says that formula is unused; it should not be copied into a handoff as verified.

The finite checks are reproducible with `python3 check_cbeta_repair.py` from this intake directory and require SymPy. No numerical research claim, ζ statement, or new famous-conjecture result follows from this review.


# Source index and artifact receipt

This supplement includes **69 complete source reports**. Its companion JSON index verifies **297 associated repository objects** against the pinned Git tree. Code, arrays, logs, shorter READMEs and receipts are catalogued there without printing their complete machine data. The embedded proof/review text is not abridged.

Source checkpoint: `2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba`. Builder: `tools/build_round6_14_handoff.py`. Index: `docs/handoff/ROUNDS_6_14_ARCHIVE_INDEX.json`.

The source reports and their earlier checks determine the scope of every mathematical claim. This assembly verifies preservation and provenance; it supplies no new mathematical experiment.

