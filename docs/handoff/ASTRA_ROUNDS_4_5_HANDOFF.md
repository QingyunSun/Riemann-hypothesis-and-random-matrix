# 第 4-5 轮详细研究补编

本补编接续 333 页公开交接档案（检查点 055a4a0），保留随后两轮的完整证明报告和审查记录。资料源检查点为 c74b326。此前的 ACUE、零点热流、算术相关性、反例与历史路线仍应连同主档案阅读。

本轮严格结果是：同一 k=40 筛法的新增正项使已发表基线上的证明余量从 23.36045 ppm 增至 24.86626 ppm；素数间隙结论仍为 186。另有变量半径异常平方估计、足够的支撑几何条件、一个网格修复，以及完整保存的 k=39 负向搜索。没有证明 RH、Alternative Hypothesis 的反驳、新的 zeta 半间隙结果或低于 186 的素数间隙。

正文区分普通数学证明、独立内部审查、精确有理数证书、浮点计算、原论文输入和未完成义务。普通证明及内部审查尚不等于 Lean 形式验证或外部同行评审。53 项平方积分逐项区间、矩阵、参数、执行日志和哈希清单另存于仓库，不把大型数组印成难以核查的页面。

第 5 轮综合报告澄清原搜索报告的数值最大误差范围：较小的最大值只对应 12 个完整 77 维候选；仓库另存的截断候选有不同的全矩阵残差。所有 36 个向量均经过集成核查。

为便于机器和人工追溯，每篇报告列出原路径和 SHA256，文内相对链接指向该固定 Git 提交。报告文字及数学内容保留；只调整标题层级、链接、过长公式的换行，并补齐原始数据表缺少的 Markdown 表头分隔线。原文中关于暂缓、下一步或代理的描述属于研究记录。

## 接手顺序

先读两轮综合报告，接着审查新增正项及其独立证明，再查看完整 k=39 搜索的缺口。变量半径估计与几何条件可以作为后续新支撑的输入，但不能替代新的失败覆盖及物理积分证书。避免重复相同端点扫描；寻找能改变当前缺口的产品权重、可证明支撑或算术混合项。


# Current report 01: prime186_round4

Source: [research/reports/prime186_round4.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/reports/prime186_round4.md). SHA256: `ef0b060fc8bb1ac91844e08ac540973634ceb6f9ca2d64da3f8ef32f66855565`.

## A certified restoration credit and the remaining k=39 deficit

2026-09-05. This is a new research checkpoint after the 333-page handoff at commit `055a4a0`. **The prime-gap bound remains 186.** No new zeta gap, AH refutation, or Dyson–Montgomery theorem is proved.

The useful completed result is a strictly positive, outward-enclosed integral that the published sufficient criterion discards. On the same published 40-coordinate trial, it improves the certified normalized sieve margin from about **23.36045 ppm to 24.86626 ppm**, conditional on the original published cap and loss endpoints. Independently, a complete 77-coefficient cap-only optimization at dimension 39 remains about **5603.60 ppm below one**. That second result is a floating-point diagnosis, not a rigorous upper bound for the whole coefficient family.

### 1. Exact new positive credit

Proposition 4.6 of [Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf) gives

\[
\rho_*\langle P_OF,BP_OF\rangle-\|P_OF\|^2
\ge \rho_*(J_{\lambda,H}-\beta-E_O)-I_H+c_\alpha\alpha,
\]

where

\[
\alpha=\|(1-P_O)F\|^2,\qquad
c_\alpha=1-4\rho_*|b_h|
=\frac{2497786653900013}{2500000000000000}>0.
\]

The paper drops the last term in its convenient sufficient criterion. Its existing positive error covers provide upper estimates, so they cannot be reused as lower estimates for this credit.

We instead select a true sufficient-failure event. In units of the official mesh

\[
h=\frac{2742997}{258046918656},
\]

there are exactly two global fragments above \(b=18800h\), uniquely labelled by

\[
p\in[26400,29100]h,\qquad q\in[32400,36700]h.
\]

All residual coordinate totals are at most \(b\). The official radial cell index is restricted to \(95639\le r\le98263\). This event lies within the cap domain and violates an actual retained new-ladder order-three row, with a strictly positive rational failure margin. Both fragments can belong to one coordinate or to different coordinates; both cases are necessary.

Restricting the remaining fragments to total at most \(b\) makes their one-coordinate total measure exactly Lebesgue measure. Replacing \(1/p\) and \(1/q\) by their lower endpoint-independent constants yields a single coherent positive lower measure. Its cell kernels are rational box-sum volumes, computed by integer positive-part polynomials. There is no Dickman quadrature error in these new kernels.

The two-mark ring gives exactly 40 same-owner terms and \(40\cdot39\) different-owner terms, with no factor \(1/2\). The 53 signed polynomial terms all integrate the square of the same step trial against that same positive lower measure. Their signs cannot be discarded individually.

The outward calculation gives, in the official common normalization,

\[
\alpha_{\rm rect}\in
[3.5697238789\times10^{-20},\;3.5697238869\times10^{-20}],
\]

where these decimals are rounded outwards from the exact rational endpoints saved in the receipt. Safe downward-rounded consequences are

\[
\boxed{\alpha/I_H^+>1.5071462817\times10^{-6}},
\qquad
\boxed{c_\alpha\alpha/I_H^+>1.5058119471\times10^{-6}}.
\]

The original complete normalized lower margin, replayed from the published endpoints, is

\[
0.000023360452297044097\ldots.
\]

Adding only the new proved credit gives

\[
0.000024866264244232060\ldots,
\]

an increase of about 6.45 percent of that small margin. It is an improvement in the certificate for the same trial and same theorem, not a reduction of 186.

The larger two-fragment triangle gives an exploratory estimate around 9.76 ppm, while the one certified rectangle gives 1.5058 ppm. We do not promote the triangle estimate to a certified credit. The tiny exact rational anchor in the working files is only a strict-positivity/normalization regression; the meaningful quantitative result is the outward rectangle contraction.

Evidence:

* [Complete event, kernel and credit proof](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/prime-credit/prime_alpha_credit.md).
* [Outward rectangle receipt](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/prime-credit/alpha_rectangle_certificate.json) and [exact complete-margin replay](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/prime-credit/alpha_credit_margin_replay.json).
* [Independent mathematical review](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/restoration-proof/ALPHA_RECTANGLE_INDEPENDENT_REVIEW.md), including an independent integer-cell/Eulerian reconstruction of every entry in all three marked kernels.
* [Separate-process rerun](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/independent-rectangle-recheck/alpha_rectangle_certificate.json): all 53 term intervals and the final rational endpoints agree exactly with the first run. Runtimes were about 92.6 and 90.2 seconds on this host.

### 2. The actual k=39 scale

The independent cap implementation reconstructs the published physical radii, nested fragment caps and step masks, then changes the outer/retained dimensions to 39/38. It uses the correct \(39h/Z\) face normalization. No dimension-40 integral endpoint is inherited.

On the official 98,304-cell grid:

| Trial | Cap-only quotient \(\rho_*J/I\) | Status |
|---|---:|---|
| k=40, original 77 coefficients | 1.000206086776951 | Positive control; denominator lies in the published interval |
| k=39, original coefficients | 0.994361581476018 | Fixed-vector floating evaluation |
| k=39, optimized full 77 coefficients | 0.994396399364491 | Independent direct evaluation of the numerical Ritz candidate |
| k=40, optimized full 77 coefficients | 1.000213743639754 | Optimized positive control |

The original k=39 deficit is about 5638.42 ppm. Reoptimizing the coefficients recovers about 34.82 ppm, leaving about 5603.60 ppm. This is a useful reason to change the support or trial structure instead of repeatedly evaluating the old vector.

The scaled k=39 Gram matrix has condition number about \(2.28\times10^{10}\). The optimized matrix quotient and direct scalar reevaluation differ by \(1.74\times10^{-10}\), and the numerical generalized residual is small. Those checks support the computation; they do **not** establish an interval upper bound for all possible coefficients. Likewise, the k=40 alpha lower bound cannot be inserted into a k=39 proof, nor used as an upper bound on all recoverable alpha mass.

The implementation uses exponential tilting as a numerically cancelling normalization, not as a change of trial. Two tilt values give the same fixed-grid result to about \(4.2\times10^{-15}\). NumPy's requested `longdouble` is actually binary64 on this machine; that limitation is recorded in the JSON and report.

See [full k=39 report, matrix data and returned coefficients](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/k39-trial/REPORT.md). Neither a cap-only quotient nor a numerical family maximum pays the rootwise source-restoration costs or proves DHL[39,2].

### 3. Sharper restoration identities and a quantified failure

The exact projection identity retains both signed cross terms and removed face squares. For \(e=(1-P_O)F\), \(V_i=E_iF\) and \(W_i=E_ie\),

\[
\mathcal Q(P_OF)=\mathcal Q(F)+\alpha+
\rho_*\sum_i\int m_i\bigl(|W_i|^2-2\operatorname{Re}(\overline W_iV_i)\bigr).
\]

This identifies the actual projected-marginal matrix as the useful future optimization object. A completed-square bound instead requires an upper estimate for \(\int_{H_O\setminus O}|BF|^2\). Applying only the generic factor 40 to the old face ledger is worse than the existing Young bound. A certified effective factor below about 14.9573 would improve that particular comparison. Merely writing a sharper identity does not supply such cancellation.

There is also an exact positive inner-overlap correction, but the published ledger caps its benefit for this fixed trial at \(7.8813\times10^{-8}\) of the normalized margin. It is too small to explain the k=39 deficit. The old upper ledger gives only a loose 1.9344 percent ceiling on possible alpha credit, not any positive lower credit by itself.

The [independent restoration proof and exact ledger replay](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/restoration-proof/RESTORATION_PROOF_AUDIT.md) state these alternatives and prevent double counting. They include 200 finite signed-product diagnostics; ordinary written arguments, not those tests, supply the identities.

### 4. Corrected runtime and verification limits

The unchanged official regression failed in the earlier packaged FLINT environment. We built a separate FLINT 3.6.0 with [the upstream signed-conversion fix](https://github.com/flintlib/flint/commit/7ad753d51c82fdec115cb179b41d0e581f1cb0ec), then built Python-FLINT against it. The native integer/polynomial and Arb suites pass, as do the original certificate checks and 467 full plus 2,188 truncated products compared with an independent Python integer implementation.

The complete Python binding suite has a separately documented assertion failure in a Jacobi test that calls the native function outside its odd-positive-denominator contract. Assertions remain enabled. The certificate does not use Jacobi, and the directly used binding APIs were tested independently. We do not claim a universally verified arithmetic library or that the whole binding suite passed.

The [runtime record and build scripts](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/repro-flint/README.md) preserve source hashes, actual library linkage, successful checks, failed build configurations and the full-suite failure. The official PrimeGaps186 source was not modified. The new credit inherits the original published cap/loss endpoints; all 149 old physical forms were not recomputed in this round.

### 5. Reproduce and continue

Use an isolated copy when executing scripts that write adjacent JSON outputs. External primary inputs can be selected explicitly:

```sh
export PRIME186_SOURCE=/path/to/PrimeGaps186/prime_gap_186_certificate.py
export PRIME186_NUMERICS_TEXT=/path/to/short_gaps_numerics.txt
```

The latter is a `pdftotext` extraction of the pinned official numerical companion; its hash is recorded by the ledger replay. The public package does not duplicate the full third-party paper text. In the relevant copied subfolders:

```sh
python certify_alpha_rectangle.py                    # exact kernel/geometry checks
CORRECTED_PYTHON certify_alpha_rectangle.py --certify # outward integral
python replay_credit_margin.py                      # exact final inequality
python rectangle_independent_checks.py              # different integer kernel construction
python restoration_checks.py                       # source ledger + signed identities
OPENBLAS_NUM_THREADS=1 python cap_trial.py --k 39 --intervals 98304 --tilt 20
```

New code in the public copy differs from staging only where explicitly recorded in [the intake manifest](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/INTAKE_MANIFEST.json), principally to select the external source paths. Original output receipts are retained.

The next active experiment changes the radius/plateau support geometry and recomputes any affected exceptional-square constant. It must retain actual lcm conditions, both source ladders, inner-domain intersections, the negative full-face term and inward masks. A new outward positive **complete** k=39 inequality would be needed before claiming a smaller gap. Repeated fixed-vector scans, a new full handoff rendering, and Jacobi-wrapper repair are postponed in this slice.


# Current report 02: prime_alpha_credit

Source: [research/prime-gaps/round4/prime-credit/prime_alpha_credit.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/prime-credit/prime_alpha_credit.md). SHA256: `59791f04d6917f447382083612eea4c311f3ec74cb427c37cbac49619ba046ec`.

## Retained positive deletion credit for the published prime-gap-186 trial

Status: the failure-region inclusion is proved and one meaningful rational-kernel rectangle has been contracted with outward arithmetic. It certifies $\alpha/I_H^+\geq1.5071462817258709\cdot10^{-6}$ (decimal display of an exact rational lower endpoint). The retained credit improves the source-inherited fixed-trial margin from about 23.36045 ppm to 24.86626 ppm. The larger triangle estimate remains diagnostic. This note makes no smaller prime-gap claim and does not discharge the three project inputs in the official Lean development.

### 1. The exact quantity and its scale

For the actual published $k=40$ midpoint step trial, Proposition 4.6 of the main paper gives

$$
\rho_*\langle P_OF,BP_OF\rangle-\|P_OF\|^2
\geq \rho_*(J_{\lambda,H}-\beta-E_O)-I_H+c_\alpha\alpha,
\qquad
\alpha=\|(1-P_O)F\|^2,
$$

where

$$
c_\alpha=1-4\rho_*|b_h|=0.9991146615600052\ldots>0.
$$

The published sufficient inequality drops this positive term. A lower bound on the **actual $F^2$-weighted deleted mass**, rather than the measure of a covering set, can therefore be inserted without changing the previously paid upper bounds on $\beta$ and $E_O$. This does not recover the outer cross-term for free; that cross-term remains fully charged through $E_O$.

The common normalized denominator is source-certified as

$$
23685317816\cdot10^{-24}\leq I_H\leq23685317890\cdot10^{-24}.
$$

All numerical forms in this note use the numerical companion's normalization $(hZ)^{-40}$, where $Z=\sum_{j=0}^{98263}g((j+1/2)h)^2$ and $h=2742997/258046918656$. This is essential: the main paper uses unscaled forms, whereas the companion divides every form by this same factor.

The previously replayed complete margin is about $23.3604523$ parts per million. The new, explicitly contained failure region below has a diagnostic mass of about $9.75897$ parts per million of $I_H$. Its retained credit would be about $9.75033$ parts per million if this size is certified. The diagnostic alone is not a valid replacement for an outward lower endpoint.

### 2. A disjoint lower-bound event

Let $\nu_c=e^\gamma c\,\mathcal L(\Pi_c)$, with Poisson intensity $du/u$ on $(0,c]$. Its total-size pushforward is $\rho_D(t/c)\,dt$. In particular, restricting the residual total to $0\leq t\leq c$ gives exactly Lebesgue measure, because $\rho_D(t/c)=1$ there.

Set

$$
b=18800h=0.19984095864653703\ldots,
\qquad c=46580h=0.49513786456147313\ldots.
$$

Use the actual retained new-ladder row 24, not a failure-cover threshold assembled from different rows. Its parameters are

$$
\begin{aligned}
a&=1.0166236774089747\ldots,& A&=1.0449558074337872\ldots,\\
L&=0.5498119373071242\ldots,& \xi&=0.028332320501728507\ldots.
\end{aligned}
$$

The exact fractions are regenerated from the preserving official source and saved in the JSON outputs. Its outer predicate is

$$
\{s\leq a\}\ \cup\
\{H_{\phi_D,\xi}\leq A,\ \phi_E(M_\xi)\leq C\},
\qquad \phi_D(u)=\min(3u/2,L).
$$

Consider configurations having precisely two global fragments above $b$, ordered as $p<q$, with

$$
b<p<q\leq c,
\qquad q+p+\min(3p/2,L)>A.
$$

Remove these two fragments. Require every residual coordinate total $x_i$ to lie in $[0,b]$, and require the restored total $s=\sum_i x_i+p+q$ to exceed $a$. Finally retain only the official radial cells $\sum_i\lfloor t_i/h\rfloor<98264$.

Every residual fragment is at most $b<p$, so the inclusive tail at the witness $p$ consists exactly of $p$ and $q$. The displayed strict inequality therefore violates this actual row. Every fragment is at most the smallest outer cap $c$, so all three outer-shell fragment caps hold. The retained radial cells put the configuration in $H_O$. Consequently this region is a subset of $H_O\setminus O$.

There is no Palm multiplicity loss here. The two large fragments are globally unique and ordered. Their coordinate owners produce disjoint cases:

- distinct owners: $40\cdot39$ ordered choices;
- one common owner: $40$ choices.

The Poisson decomposition gives the measure $\prod_i dx_i\,dp\,dq/(pq)$ on each such case. No additional $1/2$ occurs after imposing $p<q$. The same-owner case has both marked fragments in a single coordinate; it is not represented by the distinct-owner integral.

Define

$$
t^D=(x_1+p,x_2+q,x_3,\ldots,x_{40}),
\qquad
 t^S=(x_1+p+q,x_2,\ldots,x_{40}),
$$

and let $F_\square(t)$ be the **official step function**, including its exact midpoint polynomial and profile, evaluated at these totals. Let $R_D,R_S$ impose the preceding radial conditions. With

$$
\mathcal T=\{(p,q):p<q\leq c,\ q+p+\min(3p/2,L)>A\},
$$

we obtain the proved lower-bound formula

$$
\alpha\geq\frac{1}{(hZ)^{40}}\left[
1560\int_{\mathcal T}\int_{[0,b]^{40}}
1_{R_D}F_\square(t^D)^2\,dx\,\frac{dp\,dq}{pq}
+
40\int_{\mathcal T}\int_{[0,b]^{40}}
1_{R_S}F_\square(t^S)^2\,dx\,\frac{dp\,dq}{pq}
\right].
$$

Here $\mathcal T$ may equivalently start at

$$
p_{\min}=(A-c)/(5/2)=0.21992717714892562\ldots>b,
\qquad q>\max\{p,A-p-\min(3p/2,L)\}.
$$

Thus the apparently additional condition $p>b$ is automatic in the implemented triangle. These inequalities are checked with exact fractions when constructing the event.

### 3. Measured mass of this genuine subset

`alpha_credit.py` uses scrambled Sobol sampling with an explicitly evaluated importance density. Unmarked residual cells are sampled with probabilities proportional to $g_j^2e^{-\lambda jh}$; conditional positions are uniform in the selected fine cell. Marked residuals use truncated exponential densities. The code evaluates the exact published midpoint step trial, and cancels the proposal factors explicitly. The proposal tilt is 45 and the cutoff is exactly $18800h$.

Eight independent scrambles, each with $2^{20}$ points for each owner case, give:

| Disjoint event | Estimated mass divided by published $I_H^+$ | Standard error across scrambles |
|---|---:|---:|
| Distinct coordinate owners | $4.2125098941\cdot10^{-6}$ | $1.72\cdot10^{-8}$ |
| Same coordinate owner | $5.5464619292\cdot10^{-6}$ | $2.11\cdot10^{-8}$ |
| Sum | $9.7589718233\cdot10^{-6}$ | No deterministic enclosure |

The run evaluated 16,777,216 points and took about 40 seconds on this host. The same-owner contribution is about 57% of the total. The weighted fragment locations are approximately $p=0.293$–$0.294$, $q=0.362$–$0.365$, and the weighted full total is about $1.032$.

These are reproducible randomized-quadrature diagnostics. Across-scramble standard errors are not rigorous integration-error bounds; ordinary floating-point evaluation is also not an outward enclosure. The estimates do not prove $\alpha/I_H\geq9.7\cdot10^{-6}$.

### 4. Exact rational positive kernels for a certifiable rectangle

One disjoint rectangle inside the failure triangle is

$$
P=[26400h,29100h],\qquad Q=[32400h,36700h].
$$

Indeed, $P$ lies below $Q$, all marks are above $b$ and below $c$, and throughout the rectangle

$$
q+p+\phi_D(p)=q+\frac52p\geq98400h>A.
$$

The source-core condition is guaranteed on every cell with index sum

$$
95639\leq r\leq98263,
$$

since $95638h\leq a<95639h$ and the actual total is at least $rh$. This deliberately discards cells that straddle the activation boundary.

Replace the positive fragment density $1/(pq)$ by the smaller constant $1/(P_+Q_+)$. This defines a coherent positive submeasure. Its cell kernels involve **only rational box volumes**, not Dickman quadrature or a critical-line approximation.

For a vector of positive integer lengths $w=(w_1,\ldots,w_d)$ and integer offset $o$, define

$$
V_{o,w}(j)=\frac1{d!}\sum_{\epsilon\in\{0,1\}^d}(-1)^{|\epsilon|}
\left[(j+1-o-\epsilon\cdot w)_+^d-(j-o-\epsilon\cdot w)_+^d\right].
$$

It is exactly the volume of $\{0\leq y_i\leq w_i:j\leq o+\sum_i y_i<j+1\}$. In units of cell measure $h$, the four coordinate kernels are

$$
u_j=1_{0\leq j<18800},
\quad
v_j=\frac{V_{26400,(2700,18800)}(j)}{29100},
\quad
w_j=\frac{V_{32400,(4300,18800)}(j)}{36700},
$$

$$
z_j=\frac{V_{58800,(2700,4300,18800)}(j)}{29100\cdot36700}.
$$

The last channel is the same-owner measure. Multiply each by $g_j^2/Z$ and place them in the positive marking ring

$$
K_j=\frac{g_j^2}{Z}(u_j+av_j+bw_j+abz_j),\qquad a^2=b^2=0.
$$

The $ab$ coefficient of the 40-coordinate moment contraction automatically includes both $40z u^{39}$ and $40\cdot39vw u^{38}$. These multiplicities must not be added a second time.

The official finite symmetric-moment identity (numerical companion (2.10)–(2.12)) now evaluates this lower submeasure against the **same signed expansion of $F_\square^2$**. Taking signed coefficient terms separately as nonnegative would be invalid. The adapter accumulates their full outward intervals before assessing the lower endpoint.

`certify_alpha_rectangle.py` supplies the four exact integer-numerator arrays and rational denominators. Its standalone structural checks pass:

- every cell coefficient is nonnegative;
- the exact numerator mass sums are $18800$, $101520000$, $161680000$, and $1309608000000$;
- denominators are $1$, $58200$, $73400$, and $6407820000$;
- known two- and three-unit box-sum distributions agree;
- the marking-ring mass agrees exactly with the independent same/distinct owner formula;
- every rectangle point satisfies the actual source failure and cap inequalities.

A separate QMC evaluation of **this lower constant-density rectangle**, using the stricter cell mask, estimates

$$
\alpha_{\rm rect}/I_H^+\approx1.5111578472\cdot10^{-6}
$$

with distinct-owner $0.6524769$ ppm and same-owner $0.8586809$ ppm. The outward contraction subsequently completed all 53 signed square signatures in 92.582 seconds on one worker. It enclosed the normalized rectangle mass in

$$
[3.5697238789408751\cdot10^{-20},\ 3.5697238868155496\cdot10^{-20}],
$$

where the exact dyadic endpoints, not these decimal displays, are stored in `alpha_rectangle_certificate.json`. Consequently

$$
\frac{\alpha}{I_H^+}\geq
\frac{9050325235576887333393096923828125}
{6004941487970983985258771441262503395328}
=1.507146281725870950\ldots\cdot10^{-6},
$$

and the retained margin credit is at least

$$
\frac{c_\alpha\alpha^-}{I_H^+}
=1.505811947187963804\ldots\cdot10^{-6}.
$$

Replaying the printed original $I^\pm,J^-,L^+$ endpoints with this newly certified lower mass gives

$$
\mathcal M_{\rm new}\geq0.000024866264244232\ldots,
$$

a 6.44598798% increase over the previous lower-margin endpoint. This strengthens a certificate for the same trial and $k=40$; its admissible tuple and gap 186 are unchanged. `replay_credit_margin.py` records the complete exact rational addition in `alpha_credit_margin_replay.json`.

The QMC estimates at proposal tilts 45 and 35 bracket the certified value within their empirical fluctuation scale. They served as diagnostics, not as input to the proof. Tiling the larger triangle with disjoint rectangles can retain more mass; overlapping rectangle sums would not be valid lower bounds.

### 5. What is already rigorous, and the next executable obligation

`exact_cell_anchor.py` gives a completely rational positive anchor $\alpha/I_H^+\geq10^{-197}$. It uses two explicit owner types with all residual totals in one fine-cell subinterval, evaluates the constant step-trial values exactly, and proves the auxiliary bound $hZ<11/500$ by a rational monotone Riemann sum. This tiny result verifies strict positivity and normalization. It has no useful effect on the sieve margin.

The meaningful rectangle calculation uses the official `CapEngine` and `SourceJets` implementations without changing their source. `CapEngine` executes the mandatory signed-FLINT regression. The adapter does not catch, disable, replace, or bypass that check. It introduces new rational lower kernels and the proven radial mask, then asks the existing outward machinery to contract them on all 98,264 retained indices.

The completed run used `/Users/qingyunsun/.cache/astra-research/flint-3.6.0-patched/venv/bin/python`, 160-bit Arb precision, 224-bit fixed-point positive convolutions, and one worker. The original signed-FFT startup regression passed unchanged. The root agent separately reports exact signed-convolution comparisons and passing native `fmpz_poly`/`fmpz_vec` tests for this corrected build. This is not a claim that the entire Python-FLINT test suite passed: the root identified an unrelated assert-enabled Jacobi test with an even denominator. Native assertions and the certificate regression remained enabled.

The rectangle now has an actual outward lower endpoint. The remaining work is independent review/replay of this new adapter and, if the larger approximately 9.76-ppm mass is worth pursuing, a disjoint finite rectangle cover from inside followed by its outward contractions. The full triangle estimate remains uncertified.

Commands, from this directory:

```sh
python3 certify_alpha_rectangle.py
python3 exact_cell_anchor.py
python3 alpha_credit.py --power 20 --repeats 8 --output alpha_credit_p20.json
python3 alpha_credit.py --region rectangle_lower --power 19 --repeats 4 --output alpha_rectangle_p19.json
## Only a corrected runtime which passes the unmodified signed regression:
/Users/qingyunsun/.cache/astra-research/flint-3.6.0-patched/venv/bin/python certify_alpha_rectangle.py --certify --threads 1
python3 replay_credit_margin.py
```

The files `alpha_rectangle_kernel_checks.json`, `exact_cell_anchor.json`, `alpha_credit_p20.json`, and `alpha_rectangle_p19.json` record the present evidence. The completed outward run wrote `alpha_rectangle_certificate.json` and `alpha_rectangle_certificate.log`; the positive credit is taken from its exact rational lower endpoint. Independent review of the adapter and subset proof remains appropriate before publication.

### 6. Relevance to $k=39$

The adjacent independent round-four experiment reports that the published coefficient vector reused at $k=39$ gives cap-only quotient $\rho_*J/I\approx0.994361581476$, a deficit of about 5638 ppm before restoring supports. The demonstrated $k=40$ region is about 10 ppm and cannot close that particular numerical deficit. Nor can its mass be inherited by dimension 39: the trial, measure, source masks, operator constants, and their normalization must all be reevaluated.

This does not establish a global $k=39$ obstruction. It establishes a concrete scale comparison for one inherited trial and identifies a previously dropped positive term with an inexpensive rational-kernel route to certification. A better vector or changed support geometry remains a separate optimization problem.

### Sources and provenance

The mathematical sources are the [official PrimeGaps186 repository](https://github.com/openai/PrimeGaps186), its main manuscript (Proposition 4.6 and (4.40)), and [the numerical companion](https://github.com/openai/PrimeGaps186/blob/61340d0b74163003b32756bb16e91d9209a5e330/short_gaps_numerics.pdf), §§1.1–1.3 and (2.10)–(2.12). The preserving clone is at commit `61340d0b74163003b32756bb16e91d9209a5e330`; the official certificate file SHA256 is `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`.

The scripts read that source and write only in this owned staging directory. The published denominator and previous margin are inherited primary-source enclosures; they were not recomputed in this subtask. No external paid model calls, source-clone mutations, or unrelated toolchain rebuilds were used by this agent.


# Current report 03: ALPHA_RECTANGLE_INDEPENDENT_REVIEW

Source: [research/prime-gaps/round4/restoration-proof/ALPHA_RECTANGLE_INDEPENDENT_REVIEW.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/restoration-proof/ALPHA_RECTANGLE_INDEPENDENT_REVIEW.md). SHA256: `22796ab5c24508df097e913595f76519d5fe7002df75de7584653142e2e7c196`.

## Independent audit of the positive-alpha rectangle certificate

2026-09-05. Reviewed files: ../prime-credit/alpha_credit.py, certify_alpha_rectangle.py, prime_alpha_credit.md, and the completed alpha_rectangle_certificate.json. This review is independent of their author. It reads the preserving official certificate source and inspects the completed outward receipt; it does not rerun the large contraction.

### 1. Verdict and certified scope

I found no mathematical or normalization defect in the rectangle lower-event construction or its adapter to the official outward moment engine. The following points are correct:

- the rectangle belongs to the actual deleted outer support, not merely an upper failure cover;
- the residual total law is exactly Lebesgue measure on the selected interval;
- the marked densities have no missing exponential normalizer, cap factor, or factor \(1/2\);
- the same-owner and different-owner cases are both included, once each;
- all coordinate kernel factors of \(h\) cancel against the published \((hZ)^{40}\) normalization correctly;
- the adapter uses the actual midpoint step trial, its full signed square expansion, and a valid inward radial mask;
- the completed receipt contains a positive outward lower endpoint.

The new receipt proves a lower credit of approximately

$$
\frac{c_\alpha\alpha_{\rm rect}}{I_H^+}
\ge1.50581194718\times10^{-6},
\qquad
c_\alpha=1-4\rho_*|b_h|.
\tag{1.1}
$$

The exact rational endpoint is in the receipt and in rectangle_independent_checks.json; the displayed decimal is descriptive. A simpler strictly lower rational bound is \(1.5058\times10^{-6}\).

This improves the inherited published \(k=40\) trial's certified normalized margin from approximately \(23.3604523\) ppm to at least \(24.8662642\) ppm. The published cap and loss endpoints are inherited source inputs, not recomputed by the new run. This is a strict improvement of the fixed-trial margin, not a smaller prime-gap theorem or a \(k=39\) certificate.

Our earlier restoration report correctly said the old upper ledger alone yields no positive alpha lower bound. This new, separate lower-event calculation supplies such a bound and does not conflict with that statement.

### 2. Proof that the event really is deleted

Use the exact official grid

$$
h=\frac{2742997}{258046918656},\qquad n=98264.
$$

The residual cutoff is \(b=18800h\), and the two marked intervals are

$$
P=[26400h,29100h],\qquad Q=[32400h,36700h].
$$

These intervals are strictly ordered and lie above \(b\). All residual coordinate totals are at most \(b\), so every residual fragment is at most \(b\). Hence \(p\in P\) and \(q\in Q\) are the unique two fragments above \(b\) in the entire outer root, with \(p<q\).

The source row used is the retained new-ladder row of index 24. I checked the official ladder generation and row-retention filter: this row is included among the 39 retained new rows, and its order is three. Its relevant outer condition is

$$
s\le a
\quad\text{or}\quad
\bigl(H_{\phi_D,\xi}\le A
\text{ and the opposite-root condition}\bigr),
\qquad
\phi_D(u)=\min(3u/2,L).
$$

Throughout the selected rectangle, exact rational inequalities give

$$
p>\xi,\qquad
\frac32p\le\frac32(29100h)<L,
$$

and

$$
q+p+\phi_D(p)
=q+\frac52p
\ge(32400+\tfrac52\,26400)h
=98400h>A.
\tag{2.1}
$$

The inclusive tail at the witness \(p\) contains exactly \(p+q\), because all other fragments are smaller than \(p\). Thus (2.1) violates the actual owner condition. The opposite-root condition need not be analyzed to establish failure of the conjunction.

The inward radial mask is

$$
95639\le r=\sum_i\lfloor t_i/h\rfloor\le98263.
$$

The exact core comparison is \(95638h\le a<95639h\), while the actual total satisfies

$$
s=\sum_i t_i\ge rh>a.
$$

This excludes the safe-core alternative. On the other side,

$$
s<(r+40)h\le98303h<S=98304h,
$$

and the coordinate-index sum belongs to the retained official outer cells.

Finally, every fragment is at most \(36700h\), strictly below the smallest official outer-shell cap \(46580h\). Therefore the event lies inside the actual cap domain \(H_O\), regardless of which outer shell contains its total. Combining these facts proves it lies in \(H_O\setminus O\).

The proof uses the actual row predicate, not a rounded common failure threshold from the old covering argument. Thus it is a legitimate source of lower mass.

### 3. Residual measure and the missing-factor audit

The source's coordinate measure is

$$
\nu_c=e^\gamma c\,\mathcal L(\Pi_c),
$$

where \(\Pi_c\) is the Poisson point process of intensity \(du/u\) on \((0,c]\). For \(b<c\), the probability of no points in \((b,c]\) is \(b/c\). Hence

$$
\nu_c\big|_{\{\max X\le b\}}=\nu_b.
\tag{3.1}
$$

This identity includes the normalizing factor: \(e^\gamma c\cdot(b/c)=e^\gamma b\). It must not be followed by an additional \(b/c\) or \(e^{-\gamma}\) factor.

The total-size pushforward of \(\nu_b\) is

$$
\rho_D(x/b)\,dx.
$$

For \(0\le x\le b\), \(\rho_D(x/b)=1\). Consequently the selected residual total has exactly the measure \(dx\). It is not a probability-uniform density \(dx/b\); its mass on this interval is \(b\).

For a coordinate with one selected large fragment, Poisson decomposition adds \(dp/p\) or \(dq/q\). For a coordinate with both, it adds \(dp\,dq/(pq)\). Since \(P\) and \(Q\) are disjoint, the two selected fragments have unique labels determined by their intervals. There is no \(1/2!\): one may derive the same fact by first using the unordered two-point density with \(1/2!\), then summing its two disjoint orderings.

Across all coordinates the event measure is therefore

$$
\prod_{i=1}^{40}dx_i\,\frac{dp\,dq}{pq},
$$

with the chosen marks assigned to their coordinate owners. The interval restrictions and total caps merely restrict this measure.

### 4. Owner counting: the same-coordinate term is essential

There are two disjoint owner classes:

1. \(p\) and \(q\) belong to different coordinates: \(40\cdot39=1560\) ordered choices.
2. Both belong to one coordinate: 40 choices.

The owners are ordered by the labels \(p\in P\) and \(q\in Q\). An additional factor two would duplicate configurations. Omitting the second class would lose genuine positive mass.

For the moment computation, let \(u_j,v_j,w_j,z_j\) be the four coordinate cell measures for no mark, only \(p\), only \(q\), and both marks. The ring

$$
\mathbb R[a,b]/(a^2,b^2)
$$

with coordinate element \(u+av+bw+abz\) has product rule

$$
(u,v,w,z)(u',v',w',z')
=
(uu',\,vu'+uv',\,wu'+uw',\,
zu'+uz'+vw'+wv').
$$

The coefficient of \(ab\) in its 40-fold product is precisely the sum of same-owner and different-owner assignments. For constant integrated channel masses it is

$$
40zu^{39}+40\cdot39vwu^{38}.
$$

This is exactly the official SourceJets “palm” multiplication and “both” channel. Those factors are already generated by the ring and must not be applied again outside the contraction.

The equality between some integrated channel masses does not permit replacing the same-owner cell kernel by a product of the separate-owner kernels. The same-owner total is \(x+p+q\), and it requires the separate three-variable box kernel used in the adapter.

### 5. Exact box volumes and normalization by \(hZ\)

Replace \(1/(pq)\) on the marked rectangle by its lower constant

$$
\frac1{P_+Q_+},\qquad P_+=29100h,\quad Q_+=36700h.
$$

This produces one coherent positive submeasure. Since the final integrand is \(F_{\rm step}^2\ge0\), its integral is a lower bound on the event's mass.

Scale all variables by \(h\). A coordinate with one mark has two integration variables \(x,p\), so its cell measure is

$$
\frac{h^2}{29100h}\,
\operatorname{Vol}\{(x',p'):
0\le x'\le18800,\ 26400\le p'\le29100,\
j\le x'+p'<j+1\}.
$$

Dividing by \(h\), as needed for the normalized coordinate array, leaves the two-dimensional volume divided by 29100. The analogous \(q\) channel divides by 36700.

The same-owner channel has three integration variables and two mark denominators. Its cell measure is \(h\) times the corresponding three-dimensional volume divided by \(29100\cdot36700\). Thus the four dimensionless arrays in the adapter are exactly cell mass divided by \(h\).

The inclusion-exclusion routine returns \(d!\) times the \(d\)-dimensional cell volume. Therefore the denominators

$$
1,\quad 2\cdot29100,\quad 2\cdot36700,\quad
6\cdot29100\cdot36700
$$

are correct.

On an actual coordinate cell, the official step profile contributes \(g_j^2\). The adapter's weight is

$$
\frac{g_j^2}{Z}\frac{\text{cell mass}}h
=\frac{g_j^2\,\text{cell mass}}{hZ}.
$$

Multiplication across 40 coordinates supplies exactly the companion paper's \((hZ)^{-40}\) normalization. No extra \(h\), \(40\), \(Z\), or physical-scale multiplier belongs after the moment contraction.

This point distinguishes the new norm lower integral from the official source-loss routines, some of which integrate an extra erased coordinate and accordingly have additional factors. The adapter correctly uses only the coordinate product law needed here.

### 6. Actual step trial and signed-square coherence

I checked that the official CapEngine aliases its signature and coefficient arrays directly to the printed rational trial data. Its square_groups are obtained by the exact full quadratic expansion of the 77 coefficients, including a factor two for distinct coefficient pairs.

The radial polynomial argument is

$$
(r+20)h-\frac9{10},
$$

the sum of the 40 coordinate midpoints minus the fixed center. The angular moments use the same coordinate midpoints. Hence the adapter evaluates the published **step trial**, not a continuous polynomial approximation at the original real totals.

Every kernel channel, radial mask, and signature uses the same positive lower submeasure. Some coefficients of the polynomial-square expansion are negative, but their sum represents the nonnegative square. The adapter:

- obtains two-sided outward intervals for the positive moment coefficients;
- multiplies by two-sided intervals for the signed radial polynomial;
- uses the official signed interval product and outward reduction;
- adds all 53 signed signature contributions before testing the final lower endpoint.

It does not freeze upper moment bounds and then multiply them by negative coefficients, and it does not clamp negative signature terms to zero. Several negative partial sums in the run log are consistent with the necessary signed cancellation.

The proof therefore rests on ordinary interval enclosure of one fixed coherent integral. Independence between numerical interval errors is not required.

### 7. Independent checks performed

The companion rectangle_independent_checks.py does not import CapEngine, SourceJets, or the rectangle certifier as a module.

It reconstructs all three marked cell-numerator arrays by a different exact method: decompose each integer-length interval into unit intervals, convolve their integer location counts using prefix sums, and finish with the Eulerian unit-cube cell-volume numerators

$$
(1,1)\quad\text{in dimension two},\qquad
(1,4,1)\quad\text{in dimension three}.
$$

All 98,264 entries of each reconstructed array agree exactly with the proposed inclusion-exclusion routine. Their sums are respectively

$$
101520000,\quad161680000,\quad1309608000000.
$$

The script also verifies the owner expansion with exact fractions on a four-coordinate, three-cell toy measure, using a nonconstant squared trial and a radial mask. The ring contraction equals a separate explicit sum over all 4 same-owner and 12 different-owner choices. This checks more than the unweighted total mass.

Finally, it checks the completed receipt's endpoint ordering, positive lower endpoint, alpha normalization by the published \(I_H^+\), and multiplication by the exact coefficient \(c_\alpha\), all using exact fractions.

These checks passed. The source adapter hash and receipt hash are stored in rectangle_independent_checks.json.

### 8. Completed outward receipt and evidence boundary

The receipt records:

- the unmodified mandatory signed-convolution regression passed;
- 160-bit Arb working precision and 224-bit fixed-point source arrays;
- one worker thread;
- all 53 signed signatures completed;
- a final normalized rectangle interval approximately

$$
[3.569723878940875\times10^{-20},
\ 3.569723886815550\times10^{-20}].
$$

Using the source-inherited bound \(I_H^+=23685317890\cdot10^{-24}\), the exact lower endpoint gives

$$
\frac{\alpha_{\rm rect}}{I_H^+}
\ge1.50714628172\times10^{-6},
$$

and the exact \(c_\alpha\) gives (1.1). The contraction took about 92.6 seconds according to its receipt.

This is stronger evidence than the earlier randomized-QMC estimate: it is a completed outward enclosure of the explicit lower submeasure. The QMC code's proposal factors, owner split, and midpoint evaluation are also consistent with this same integral, but its standard errors were never deterministic certificates and are not used here.

The remaining trust boundary is the official outward arithmetic implementation and the corrected runtime that passed its unchanged regression, together with the published denominator and previous upper-loss inputs. This review checks the mathematical adapter, event inclusion, normalization, and scalar receipt; it is not a formal verification of FLINT or a fresh proof of all 149 original physical bounds.

The improved \(k=40\) margin follows by adding this lower credit once to Proposition 4.6 while retaining all existing outer and inner debts. It does not justify removing the mixed-term debt, transferring the mass to dimension 39, or adding the same credit again through a separately restored denominator.


# Current report 04: RESTORATION_PROOF_AUDIT

Source: [research/prime-gaps/round4/restoration-proof/RESTORATION_PROOF_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/restoration-proof/RESTORATION_PROOF_AUDIT.md). SHA256: `fbbaa5293ea486e643cecc78d7651487448b54f3dbe0840cce8ac61d4089645f`.

## Exact projection restoration, positive norm credit, and the limits of the published ledger

2026-09-05. Independent proof/audit task, confined to Proposition 4.6 of the prime-gap-186 paper and the structural frontier identified in round three. No official physical-integral computation was rerun, no Claude session was started, and no repository source was edited.

Primary source: [Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), §§4.3–4.6, especially Proposition 4.6, displayed equations (4.30)–(4.43). Numerical source: the [official certificate repository](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330), Numerical certificate for prime gaps at most 186, Proposition 1.3 and Tables 2.1–2.7. Locally read files and exact scalar replay are recorded in restoration_checks.py/json/log.

The formulas below are consequences of the source's Hilbert-space setup. They are not a claim that the needed new physical integrals have been evaluated, nor a claim of priority for elementary projection identities.

### 1. Findings

There is a completely exact restoration identity that avoids Young debts:

$$
\mathcal Q(PF)=\mathcal Q(F)+\alpha+
\rho\sum_i\int m_i\bigl(|W_i|^2-2\operatorname{Re}(\overline{W_i}V_i)\bigr),
\tag{1.1}
$$

where \(\mathcal Q(F)=\rho\langle F,BF\rangle-\|F\|^2\), \(P=1_O\), \(e=(1-P)F\), \(\alpha=\|e\|^2\), \(V_i=E_iF\), and \(W_i=E_ie\). Computing or bounding the actual removed marginals \(W_i\) is the direct route to a stronger restoration calculation.

Three useful rigorous lower bounds follow:

1. Keep the paper's Young upper bound and restore a separately certified lower bound for \(\alpha\).
2. Integrate a signed root residual on the true failure set. A pointwise completion of the square yields a new upper-cost target \(\int_{H_O\setminus O}|BF|^2\), which retains cancellation between face terms.
3. Use sharp pointwise quadratic bounds for \(W_i\), including its squared term, rather than discarding all positive face squares.

The old/new inner-domain overlap also gives an exact positive correction. The published constants cap its normalized margin benefit at \(7.8813\times10^{-8}\), so that particular overlap recovery is small for the published \(k=40\) trial.

The 52 outer root-square ledger entries imply

$$
0\le \frac{\alpha}{I_H}\le0.019361160920,
\qquad
0\le \frac{(1-4\rho|b_h|)\alpha}{I_H}\le0.019344019740.
\tag{1.2}
$$

These are upper bounds on possible credit, not positive lower bounds. The published upper ledger alone supplies no guaranteed new credit. They are also deliberately loose, and do not establish whether a \(k=39\) trial can succeed.

### 2. Setup and the exact signs

Work in the source's Hilbert space \(L^2(H_O,\nu^k)\), extending profiles by zero. Let

$$
U=H_O\setminus O,\quad P=1_O,\quad e=1_UF,\quad f=PF=F-e.
$$

Since \(P\) is an orthogonal multiplication projection,

$$
\langle f,e\rangle=0,\qquad
\|f\|^2=I_H-\alpha,\qquad
\alpha=\int_U|F|^2.
\tag{2.1}
$$

The actual face operator is

$$
B=\sum_i E_i^*m_iE_i,\qquad
m_i=d_0\,1_{L_0}+a_h\,1_{L_1}+b_h.
\tag{2.2}
$$

Put \(b=|b_h|=-b_h>0\). Its three values are

$$
m_i=
\begin{cases}
1,&Y\in L_0,\\
a_h-b,&Y\in L_1\setminus L_0,\\
-b,&Y\notin L_1.
\end{cases}
\tag{2.3}
$$

The first two are positive for the published constants. The source proves

$$
-bC_{\rm op}I\le B\le C_{\rm op}I,\qquad C_{\rm op}=4.
\tag{2.4}
$$

It also defines \(A\) using the larger cap domains, \(D=A-B\ge0\), and

$$
J_{\lambda,H}=\langle F,AF\rangle,\qquad
\beta=\langle F,DF\rangle,\qquad
\langle F,BF\rangle=J_{\lambda,H}-\beta.
\tag{2.5}
$$

Thus \(\mathcal Q(F)\) in (1.1) uses the actual \(B\) but the unprojected \(F\). It is not the cap form \(\rho J_{\lambda,H}-I_H\).

Expanding \(f=F-e\) gives, with no estimate,

$$
\mathcal Q(f)
=\rho(J_{\lambda,H}-\beta)-I_H+
\alpha-2\rho\operatorname{Re}\langle e,BF\rangle
+\rho\langle e,Be\rangle.
\tag{2.6}
$$

Applying the adjoint relation to the last two terms gives (1.1).

All face products in these equations are products of conditional integrals. In particular,

$$
|W_i(Y)|^2
=\iint e(Y\oplus_iX)\overline{e(Y\oplus_iX')}\,d\nu(X)d\nu(X').
\tag{2.7}
$$

The two integrated coordinates are independent copies conditional on the same retained configuration \(Y\). Replacing this expression with \(E_i(|e|^2)\) is incorrect.

No positivity of \(F\) is assumed. The research record explicitly notes sign changes of the optimized polynomial. In the signed hybrid form, replacing \(F\) by \(|F|\) is not automatically monotone because \(b_h<0\).

### 3. Positive-alpha credit: what is sufficient and what is not

The source's spectral lower bound gives

$$
\langle e,Be\rangle\ge-bC_{\rm op}\alpha.
$$

Define

$$
c_\alpha=1-\rho bC_{\rm op}>0.
\tag{3.1}
$$

If \(E_O\) is any valid upper bound for \(2\operatorname{Re}\langle e,BF\rangle\), then

$$
\mathcal Q(PF)\ge
\rho(J_{\lambda,H}-\beta-E_O)-I_H+c_\alpha\alpha.
\tag{3.2}
$$

Consequently, for outward bounds and a **separately proved lower bound** \(\alpha^-\le\alpha\), the strengthened sufficient criterion is

$$
\rho\bigl(J^-_{\lambda,H}-E_O^+-\beta^+\bigr)-I_H^+
+c_\alpha\alpha^->0.
\tag{3.3}
$$

The alpha term is not multiplied by another \(\rho\). It already comes from the denominator restoration \(\|PF\|^2=I_H-\alpha\), together with the small negative spectral correction.

#### 3.1 Disjoint sufficient-failure regions

If \(A_1,\ldots,A_r\subset U\) are pairwise disjoint up to null sets, then

$$
\alpha\ge\sum_{\ell=1}^r\int_{A_\ell}|F|^2.
\tag{3.4}
$$

Certified lower integral enclosures on these sets can be added. The inclusion \(A_\ell\subset U\) must use the **actual complete outer-domain predicate**, including activations, row membership, radial cells, and fragment caps.

A practical construction is an inward fragment region on which one actual outer support inequality fails by a strict rational margin. Order the witness coordinates or assign the first failing row and the largest relevant fragment to half-open intervals, so the selected regions are disjoint. A lower integral requires a lower probability or a two-sided enclosure of that region. A Chernoff upper bound is not a lower probability.

More generally, nonnegative weights \(w_\ell(X)\) may be used if

$$
\sum_\ell w_\ell(X)\le1_U(X)\quad\text{a.e.}
$$

Then \(\alpha\ge\sum_\ell\int w_\ell|F|^2\). This is the appropriate partition-of-unity direction for credit.

#### 3.2 Existing overlapping positive covers

The paper uses nonnegative majorants \(M_j\) with

$$
1_U\le\sum_jM_j.
\tag{3.5}
$$

The inequality is in the opposite direction. It produces upper bounds on nonnegative integrals over \(U\); it does not prove any of the \(M_j\) is supported in \(U\), or any positive lower bound on \(\alpha\).

Even if every cover set happened to lie in \(U\), adding their masses would overcount intersections. Two identical sets of mass one give a sum two and a union mass one. Remedies are disjointification, a proved multiplicity bound, Bonferroni lower bounds with correctly directed intersection enclosures, or nonnegative credit weights summing at most one.

The current Palm–Chernoff and factorial majorants can be positive outside the failure event and can exceed one. They therefore cannot simply be normalized or relabeled as disjoint lower-mass contributions.

For signed residual integrands, the restriction is stronger: multiplying by an upper event cover preserves inequalities only for a nonnegative integrand. Its positive and negative parts must be treated separately.

### 4. Signed root restoration and an optimized quadratic bound

Let

$$
G(X)=(BF)(X)=\sum_i m_i(\widehat X_i)V_i(\widehat X_i).
\tag{4.1}
$$

The adjoint formula is understood on \(H_O\), with zero extension. From (2.6) and (2.4),

$$
\mathcal Q(PF)\ge\mathcal Q(F)+
\int_U r(X)\,d\nu^k(X),
\qquad
r=c_\alpha|F|^2-2\rho\operatorname{Re}(\overline F G).
\tag{4.2}
$$

This is sharper in its treatment of the mixed term than replacing every \(m_iF V_i\) by \(h_i|F V_i|\) and applying Young separately. It retains cancellation across faces and the sign of the summed mixed term.

Completing the square pointwise gives

$$
r=c_\alpha\left|F-\frac{\rho}{c_\alpha}G\right|^2
-\frac{\rho^2}{c_\alpha}|G|^2,
$$

and hence

$$
\boxed{\quad
\mathcal Q(PF)\ge
\rho(J_{\lambda,H}-\beta)-I_H
-\frac{\rho^2}{c_\alpha}\int_U|BF|^2.
\quad}
\tag{4.3}
$$

This is an optimized quadratic bound in which the favorable denominator loss pays for part of the mixed term. It is optimal pointwise if only \(G\) is retained and \(F\) is otherwise unrestricted. It is not claimed to dominate the paper's optimized componentwise Young estimate for every trial.

#### 4.1 Partial exact integration

If \(A\subset U\) is a known-failure region and \(1_{U\setminus A}\le\sum_jM_j\), then

$$
\int_Ur\ge\int_Ar-\sum_j\int M_jr_-,
\qquad r_-=\max(-r,0).
\tag{4.4}
$$

Thus one can retain signed residual on a certified region and upper-bound only the harmful residual on the remainder. The old positive-cover machinery can act on \(r_-\), provided its new weighted physical integrals are actually enclosed.

One must not add the right sides of different lower bounds such as (3.2) and (4.3). They are alternative estimates of the same correction; taking their maximum is valid, adding their claimed gains is generally double counting.

#### 4.2 If only an alpha interval and a residual Gram upper bound are known

Suppose \(\alpha\in[a_-,a_+]\) and

$$
\int_U|G|^2\le K.
$$

Cauchy–Schwarz gives a rigorous correction

$$
\mathcal Q(PF)-\mathcal Q(F)
\ge\min_{a\in[a_-,a_+]}\bigl(c_\alpha a-2\rho\sqrt{aK}\bigr).
\tag{4.5}
$$

The minimizing \(\sqrt a\) is the projection of \(\rho\sqrt K/c_\alpha\) onto \([\sqrt{a_-},\sqrt{a_+}]\). Substituting a lower bound for \(\alpha\) directly into the negative square-root term is not valid: the correction need not be increasing in \(\alpha\) on the whole interval.

### 5. Retain the removed face squares

For each face let

$$
a_i(Y)=\int1_U(Y\oplus_iX)\,d\nu(X),\quad
z_i(Y)=\int1_U(Y\oplus_iX)|F(Y\oplus_iX)|^2\,d\nu(X).
$$

Then \(|W_i|^2\le a_i z_i\). Put \(R_i=\sqrt{a_i z_i}\) and \(m_i^\pm=\max(\pm m_i,0)\). Minimizing the exact quadratic term over the disk \(|W_i|\le R_i\) yields

$$
m_i\bigl(|W_i|^2-2\operatorname{Re}(\overline W_iV_i)\bigr)
\ge
-m_i^+\left[|V_i|^2-(|V_i|-R_i)_+^2\right]
-m_i^-\left[R_i^2+2R_i|V_i|\right].
\tag{5.1}
$$

For \(m_i\ge0\), write the quadratic as
\(m_i(|W_i-V_i|^2-|V_i|^2)\) and take the closest point in the disk to \(V_i\). For \(m_i<0\), take the farthest point; its distance is \(|V_i|+R_i\). This proves both signs and shows the bound is optimal under that single disk constraint.

Integrating (5.1) and adding \(\alpha\) in (1.1) gives a valid lower restoration bound. In contrast to Proposition 4.6's final estimate, it retains favorable curvature of the positive-face square. But it requires certified functions \(a_i,z_i,V_i\), not just global masses.

For real \(F\), an interval enclosure \(W_i\in[\ell_i,u_i]\) can be better. On a positive face, minimize at the point of \([\ell_i,u_i]\) closest to \(V_i\); on a negative face, minimize at an endpoint farthest from \(V_i\). If the actual \(W_i\) is computed, (1.1) is exact and no auxiliary Young parameter is needed.

For a fixed finite trial basis \(\phi_a\) and fixed support, the most direct optimization object is the exact compressed matrix

$$
M_{ab}
=\rho\sum_i\int m_i E_i(P\phi_a)\overline{E_i(P\phi_b)}
-\int P\phi_a\overline{\phi_b}.
\tag{5.2}
$$

A rational vector \(v\) with \(v^*Mv>0\), certified using outward enclosures and the source hypotheses, would establish the sieve criterion for that trial. The computational obstacle is the physical projection integral; writing the matrix does not evaluate it.

The source projection does not commute with \(E_i\). Replacing \(E_i(PF)\) by a face indicator times \(E_iF\) would discard exactly the difficult dependence on the erased coordinate.

### 6. Exact old/new inner-overlap credit

Retain the paper's order of operations: inner deletion is evaluated at the unprojected \(F\), then the outer projection is restored. On a face write

$$
A_i=H_0\setminus L_{\rm old},\qquad
C_i=H_1\setminus L_1.
$$

Because \(L_0=L_{\rm old}\cap L_1\) on the base domain and \(H_0\subset H_1\),

$$
H_0\setminus L_0=A_i\cup(C_i\cap H_0).
$$

The exact inner loss is therefore

$$
\beta=d_0\beta_{\rm old}+(1-b_h)\beta_{\rm new}
-d_0\Gamma_{\rm in},
\tag{6.1}
$$

where

$$
\Gamma_{\rm in}
=\sum_i\int_{(C_i\setminus H_0)\,\sqcup\,(A_i\cap C_i)}
|V_i|^2.
\tag{6.2}
$$

The displayed union is disjoint and lies inside \(C_i\), so

$$
0\le\Gamma_{\rm in}\le\beta_{\rm new}.
\tag{6.3}
$$

This simultaneously accounts for the unnecessary \(d_0\) charge on new failures outside the base and the duplicated \(d_0\) charge where old and new failures overlap inside the base.

To use it as a positive credit, one needs a lower bound for the true integral in (6.2). Intersections of the existing upper majorants are not lower bounds for intersections of the true failure events.

If the exact projected matrix (5.2) is used instead, this inner correction is already built in. It must not be added again.

### 7. Exact replay of what the published numerical upper ledger can say

The script reads the 52 outer rows of numerical Tables 2.1 and 2.2, checks every rational Young rounding inequality, and sums the printed integers using exact fractions. It does not import the official numerical certificate. Its conclusions remain conditional on the correctness of the published physical upper bounds.

For the common normalization used in the numerical paper, set

$$
\rho=\frac{2624989}{10^7},\quad
b=\frac{843183}{10^9},\quad
d_0=\frac{44415113}{5\cdot10^9},\quad
c_\alpha=\frac{2497786653900013}{2500000000000000}.
$$

Thus \(c_\alpha=0.9991146615600052\).

#### 7.1 Upper cap on possible alpha credit

Writing \(R_j,V_j\) for the published outer root-square and outer face-square upper forms, the table sums give

$$
\frac{\sum_jR_j}{I_H^-}\le0.000653000069917512,
$$

$$
\frac{\sum_jV_j}{I_H^-}\le0.000168396875617848,
$$

$$
\frac{E_O}{I_H^-}\le0.000661756763.
\tag{7.1}
$$

The first form majorizes \(\sum_i\int_Uh_i(\widehat X_i)|F(X)|^2\,d\nu^k\). Every \(h_i\ge b\), so

$$
kb\,\alpha\le\sum_jR_j.
$$

Since \(I_H^-\le I_H\), at \(k=40\),

$$
\frac{\alpha}{I_H}
\le\frac{0.000653000069917512}{40b}
=\frac{9069445415521}{468435000000000}
=0.0193611609199163\ldots.
\tag{7.2}
$$

Multiplying by \(c_\alpha\) gives the credit cap in (1.2). The guaranteed lower bound remains zero. In particular, it is invalid to insert \(0.01936\) as the recovered mass: it is an upper ceiling obtained from overlapping majorants and a very small universal weight \(40b\).

This does not prove the actual credit is close to that ceiling, nor that a redesigned \(k=39\) profile has the same ceiling.

#### 7.2 The exact inner-overlap improvement is tightly bounded

The published two new-inner weighted groups sum to

$$
\frac{(1+b)\beta_{\rm new}}{I_H}
\le\frac{1405159+32422390}{10^{12}}
=0.000033827549.
$$

Using (6.3), the normalized sieve-margin benefit from correcting only the duplicated \(d_0\) charge is at most

$$
\frac{\rho d_0\Gamma_{\rm in}}{I_H}
\le
\frac{\rho d_0}{1+b}\,0.000033827549
=7.88120730556\ldots\times10^{-8}.
\tag{7.3}
$$

This is an absolute cap for that specific correction and the published \(k=40\) profile. It does not cap all possible changes to the inner support or trial.

#### 7.3 Completion of the square needs real cancellation to beat the old debt

Let \(H(X)=\sum_i h_i(\widehat X_i)\le k\). Weighted Cauchy–Schwarz gives

$$
|BF(X)|^2
\le H(X)\sum_i h_i(\widehat X_i)|V_i(\widehat X_i)|^2.
$$

The positive cover then yields the crude bound

$$
\int_U|BF|^2\le k\sum_jV_j.
\tag{7.4}
$$

For the published ledger, plugging this into (4.3) produces a normalized outer debt no larger than

$$
\frac{\rho^2k}{c_\alpha}\,0.000168396875617848
=0.000464551283571\ldots.
$$

That certified upper debt is **worse** than the published Young debt

$$
\rho\,0.000661756763
=0.000173710422355\ldots.
$$

Thus the generic completed-square inequality is not by itself an improvement. It requires a stronger bound on the actual signed sum \(BF\), or smaller effective \(H\) on failures.

Measured against the same published face ledger, a sufficient comparison target is

$$
\frac{\int_U|BF|^2/I_H^-}
{0.000168396875617848}
<14.957265516079\ldots,
\tag{7.5}
$$

instead of the crude factor \(k=40\). This is a concrete target for a new physical integral, not evidence that it holds. The quotient merely compares two certified upper-bound schemes; a larger ratio would not establish that the actual restoration fails.

### 8. Verification and unresolved proof obligation

The accompanying script performs exact fraction arithmetic on all 52 published outer table rows and their rounded Young costs. It also tests the exact projection identity, exact inner-overlap identity, signed root bound, completed-square bound, and optimal disk bound on 200 independent signed examples on a \(3\times3\times3\) product space with nested cap and actual face domains. The largest floating identity discrepancy was below \(4.5\times10^{-16}\). These finite tests are diagnostics; the arguments in §§2–6 supply the proofs.

Files:

- RESTORATION_PROOF_AUDIT.md — this derivation and audit;
- restoration_checks.py — exact ledger replay and finite-product diagnostics;
- restoration_checks.json — extracted 52 rows, exact fractions, numerical summaries;
- restoration_checks.log — complete run output.

The shortest substantive next obligation is now explicit: evaluate a certified lower mass on **true sufficient-failure regions**, or a certified signed residual/removed-marginal form for the actual source projection. Existing upper error ledgers cannot supply that lower mass. A successful new calculation must preserve independent erased-coordinate copies, retain the negative full-face term, and use one consistent restoration identity without adding the same credit twice.

No new \(k=39\) physical integral, restored positive margin, or prime-gap theorem is established by this audit.


# Current report 05: REPORT

Source: [research/prime-gaps/round4/k39-trial/REPORT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/k39-trial/REPORT.md). SHA256: `4c95f1f51767c736a5a48f4d58338ae6c617b9899ff18484fc915789a12a6be4`.

## A direct k=39 cap-only trial with the published physical geometry

2026-09-05. **Exploratory numerical result; no interval certificate, support-restored criterion, or new prime-gap bound.**

**Completed finite-family optimization:** after optimizing all 77 polynomial coefficients at the same frozen geometry, the best directly re-evaluated \(k=39\) candidate has cap quotient approximately **0.99439639936**, still **0.00560360064** below one. The full scaled Gram condition number is \(2.28\times10^{10}\); the matrix and direct scalar evaluations agree within \(1.74\times10^{-10}\). This is numerical evidence about the fixed family, not a certified upper bound. The corresponding \(k=40\) optimized positive control is approximately **1.00021374364**. Details and the retained-dimension checks are below.

The complete published 77-coefficient rational polynomial, evaluated in **39 outer coordinates and 38 retained coordinates** with the original physical radii, fragment caps and 98,304-cell grid, gives
\[
\frac{\rho_*J_{\rm cap}}I=0.994361581476018.
\]
The cap-only shortfall is approximately **0.005638418524**, or **5,638 parts per million**. This is a concrete fixed-trial deficit, not a bound on all 77-dimensional coefficients.

The independent \(k=40\) control gives
\[
\rho_*J_{\rm cap}/I=1.000206086776951,\qquad
I=2.36853178533315\times10^{-14},
\]
with \(I\) inside the published interval
\[
[2.3685317816,\;2.3685317890]\times10^{-14}.
\]
The published cap quotient lower endpoint is \(1.0002060794024186\ldots\), consistent with the independent value. No official FLINT check was bypassed; the program does not import FLINT or execute the official certificate.

### Fixed input and dimension changes

Source: [OpenAI PrimeGaps186, commit 61340d0b74163003b32756bb16e91d9209a5e330](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330), especially the companion numerical paper §§1.1–1.2 and the two literal coefficient tables in the certificate.

The source script SHA256 is **7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4**. Only its literal signatures and integer coefficients are parsed as data. The exploratory implementation independently reconstructs the rational ladder and cap geometry.

The parameters retained are
\[
\rho_*=\frac{2624989}{10^7},\quad
S=\frac{2742997}{2624989},\quad
T_0=\frac{2499106033}{2624989000},\quad
T_1=\frac{2510000}{2624989}.
\]
Thus the physical outer/base/enlarged radii remain \(0.2742997\), \(0.2499106033\), \(0.251\). The fragment-cap indices at the official mesh remain
\[
35265,\ 35419,\ 44781,\ 44976,\ 46580,\ 49152,\ 68225.
\]
These are fragment caps; coordinate totals above a cap are retained with their Dickman density.

For \(k=39\), the convolution length is \(98304-39=98265\), outer cell assignment uses \((r+39)h\), the retained-face assignment uses \((r+38)h\), and the radial midpoint is \((r+39/2)h\). The erased-coordinate normalization is **\(39h/Z\)**, not \(40h/Z\). Moment falling factorials use 39 or 38 as appropriate. No \(k=40\) denominator, source-loss bound or alpha estimate is inherited.

The fixed profile is
\[
g(t)=\frac{21/200}{1+t/100}+\frac{179/200}{1+(907/5)t},
\]
and the polynomial is the published rational linear combination of
\[
(s-9/10)^d P_\sigma(t),\quad0\le d\le6,\quad
\sigma\in\{\varnothing,2,3,4,5,6,22,23,24,33,222\}.
\]
The same outer trial is used in every face form.

### Independent numerical method

Conditional on a largest-fragment cap \(z\), the total-size measure is \(\rho_D(t/z)\,dt\). All needed arguments satisfy \(t/z<3\). The implementation uses
\[
\rho_D(x)=1\ (x\le1),\qquad \rho_D(x)=1-\log x\ (1<x\le2),
\]
\[
\rho_D(x)=1-\log x+\log(x-1)\log x+\operatorname{Li}_2(1-x)+\pi^2/12
\quad(2<x\le3).
\]
Eight-point Gauss integration computes each cell mass. The rational midpoint profile and polynomial are constant within each cell, as in the official trial.

Power-sum products are reduced by set partitions to convolutions of coordinate measures with monomial weights. Erasing a coordinate uses the exact expansion
\[
P_\sigma(t_1,\ldots,t_{k-1},u)
=\prod_{q\in\sigma}(P_q(t_1,\ldots,t_{k-1})+u^q).
\]
The two erased-coordinate copies are integrated independently before squaring and integrating the retained configuration. Nested fragment-cap layers are handled by differences of the corresponding retained-coordinate moments.

An explicit exponential change of numerical normalization prevents the extremely small original denominator from being swamped by FFT roundoff. Put
\[
Z_\tau=\sum_jg(t_j)^2e^{-\tau t_j},\qquad
w_j=\frac{g(t_j)^2e^{-\tau t_j}}{Z_\tau}.
\]
Every denominator contraction restores \(e^{\tau s}\); every retained-face contraction restores \(e^{\tau s_{\rm face}}\), with normalization \(kh/Z_\tau\). The erased fiber still uses the original \(g\). Thus the trial and geometry are unchanged. To return to the published normalization multiply every form by \((Z_\tau/Z_0)^k\), which cancels from the quotient.

The code requests NumPy longdouble but records the actual dtype. On this macOS runtime it is **float64**, so no extra-precision claim is made.

### Completed values

| \(k\) | cells | tilt \(\tau\) | \(\rho_*J/I\) |
|---:|---:|---:|---:|
| 40 | 4,096 | 20 | 0.995271191907594 |
| 40 | 16,384 | 20 | 0.999149113371267 |
| 40 | 98,304 | 20 | 1.000206086776951 |
| 39 | 16,384 | 20 | 0.993352220411709 |
| 39 | 98,304 | 20 | 0.994361581476018 |
| 39 | 98,304 | 25 | 0.994361581476014 |

Coarse rows change the step grid and its inward rounding; they are diagnostics, not the official fixed-grid certificate. The final two \(k=39\) rows retain the official grid and differ only in an algebraically cancelling numerical normalization. Their difference is \(4.22\times10^{-15}\).

At \(k=39,N=98304,\tau=20\), the separated face values are
\[
J_0/I=3.780455375344233,\quad
J_+/I=0.007728822713122185,\quad
J_t/I=0.06588020236568319.
\]
The signed cap form uses the published minorant parameters
\[
\text{mass}=49999/50000,\quad K=17/50,\quad\lambda=1/125,
\]
\[
a=\text{mass}^2-\text{mass}\lambda,\qquad
b=(1-\text{mass}/\lambda)(1-\text{mass})K,
\qquad J_{\rm cap}=J_0+(a+b)J_++bJ_t.
\]
The ratio of absolute contraction sums to the final denominator is about 183; the corresponding ratios for the face pieces are about 93, 530 and 1033. These measure cancellation in the chosen representation, not rigorous error bounds.

### Interpretation and earliest proof debt

The fixed \(k=39\) profile requires a change on the order of \(0.00564\) in the normalized criterion before it reaches one. The currently demonstrated \(k=40\) alpha-credit region is on the order of ten parts per million, roughly hundreds of times smaller. That comparison is a scale diagnostic only: a \(k=40\) alpha estimate is not a \(k=39\) bound, and a lower bound for one alpha region is not an upper bound for all possible alpha credit.

The remaining obligations are:

1. A genuine outward enclosure for this \(k=39\) cap form; current quadrature and FFT arithmetic are floating.
2. Separate treatment of the actual \(k=39\) rootwise support predicates and all restoration terms, including any credit attached to removal of failed outer roots.
3. An optimization or certified upper bound for the finite polynomial family before interpreting this fixed-vector deficit as a family-wide limitation.
4. The complete arithmetic sieve criterion, rather than a cap-only inequality, before any DHL[39,2] or prime-gap conclusion.

No restored \(k=39\) margin is asserted. Even a positive optimized cap-only quotient would not prove DHL[39,2].

### Files and reproduction

- **cap_trial.py**: independently implemented cap-only computation; only coefficient literals are read from the preserved official clone.
- **k39_n98304_tilt20_longdouble.json**, **k39_n98304_tilt25_longdouble.json**: final fixed-grid \(k=39\) trials. Despite the requested-type filename, each JSON records the actual dtype as float64.
- **k40_n98304_tilt20_longdouble.json**: official-grid positive control.
- Other JSON files: coarse-grid diagnostics.
- **official_numerics.txt**: local pdftotext extraction of the unchanged official companion PDF, for equation review.

Run:

    OPENBLAS_NUM_THREADS=1 python3 cap_trial.py --k 39 --intervals 98304 --tilt 20

The official-grid fixed-vector run took about 10.5 seconds in the observed concurrent run; this is a local observation, not a general performance claim.

### Completed 77-dimensional optimization at frozen geometry

**optimize_cap.py** assembles the denominator Gram \(G\) and the numerator matrix \(B=\rho_*J_{\rm cap}\) directly, without searching coefficients during integration. All coefficients vary in the same 77-dimensional polynomial space; the physical support and coordinate profile \(g\) remain frozen.

For the denominator, entries with the same joined power-sum signature and summed radial degree share one moment contraction. For the numerator, the exact erased-coordinate expansion expresses each basis function as a finite sum of retained power-sum signatures times one-dimensional fiber kernels. Weighted matrix products assemble their shared retained-coordinate integrals. This is a different contraction order from evaluating one fixed coefficient vector.

The matrices are diagonally scaled by \(\sqrt{G_{ii}}\). Three relative eigenvalue thresholds are applied to the scaled Gram before whitening: \(10^{-8},10^{-10},10^{-12}\). At the last threshold all 77 dimensions survive. Each resulting candidate is then passed to the separate scalar-form implementation in **cap_trial.py**.

At \(N=98304\), the results are:

| \(k\) | retained dimension | scaled Gram condition | matrix quotient | direct candidate quotient |
|---:|---:|---:|---:|---:|
| 39 | 62 | \(9.01\times10^7\) | 0.994371194303 | 0.994371194271 |
| 39 | 75 | \(3.65\times10^9\) | 0.994396034484 | 0.994396034594 |
| 39 | 77 | \(2.28\times10^{10}\) | 0.994396399191 | 0.994396399364 |
| 40 | 62 | \(9.49\times10^7\) | 1.000188112833 | 1.000188112844 |
| 40 | 75 | \(3.86\times10^9\) | 1.000213094616 | 1.000213094394 |
| 40 | 77 | \(2.42\times10^{10}\) | 1.000213743635 | 1.000213743640 |

For \(k=39\), the scaled Gram eigenvalues range from \(2.30246\times10^{-9}\) to \(52.4410\). The full-dimensional projected eigen-residual is \(1.24\times10^{-12}\); the residual of the scaled generalized pencil, divided by the documented matrix-norm bound, is \(7.36\times10^{-17}\). These residuals concern the assembled numerical matrices, not unknown integration errors.

The separate scalar evaluation of the 77-dimensional candidate has an absolute denominator-contraction ratio around 368 and face-contraction ratios around 180, 1194 and 1805. It differs from the matrix quotient by \(1.74\times10^{-10}\), far below the observed shortfall of \(0.00560\), but this discrepancy is not itself a rigorous error enclosure.

The optimization recovers only approximately **34.82 parts per million** relative to the published coefficients transplanted to \(k=39\). It leaves approximately **5603.60 parts per million** of cap-only shortfall. The 75-to-77-dimensional change is under one part per million. On this frozen geometry the existing polynomial coefficients are numerically close to the best found value.

The \(k=40\) control is positive in every retained subspace, and the full-family optimization improves its existing cap value by approximately 7.66 parts per million. Thus the experiment is not globally misnormalized so that every trial fails.

The complete matrix-plus-three-validation run took about 58 seconds for each dimension in the observed concurrent run. Files:

- **optimize_cap.py**
- **ritz_k39_n98304.json**, **ritz_k39_n98304.npz**
- **ritz_k40_n98304.json**, **ritz_k40_n98304.npz**
- **ritz_k39_n16384.json**, **ritz_k39_n16384.npz**: initial coarse-grid assembly check.

The JSON retains floating coefficient vectors, all scaled Gram eigenvalues, thresholds, residuals and direct candidate evaluations. The NPZ retains the raw denominator and numerator matrices and original coefficient vector.

Reproduce:

    OPENBLAS_NUM_THREADS=1 python3 optimize_cap.py --k 39 --intervals 98304 --validate

### Structural checks and next decision

**check_structure.py** checks the set-partition moment expansion against exhaustive three-coordinate summation on a four-point measure, and checks the erased-coordinate polynomial identity for all 11 signatures. Errors are below \(3\times10^{-17}\). It also verifies the exact \(k=40\) cap-index ranges against the companion paper's table and compares the closed Dickman expression at \(3\) against an independent integral. Results are in **structural_check_results.json**.

The official clone's git status remains clean. No official certificate code, dependency or assertion was modified. All three local scripts pass Python compilation.

The appropriate next mathematical decision is to stop repeated scans of these 77 coefficients at the frozen geometry. A rigorous finite-family upper bound would require outward enclosures for the two matrices and a certified positive-definiteness test for \(cG-B\), for some explicit \(c<1\), after a numerically suitable basis change. The current float64 matrices and eigensolver output do not supply that certificate.

A different radius/owner-support allocation may change the cap form substantially. Such a proposal must recompute its source-dependent caps and support restoration; it cannot simply retain the current cap arrays while changing \(S\) or \(T\). No radius scan or new support claim is included here.


# Current report 06: README

Source: [research/prime-gaps/round4/repro-flint/README.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round4/repro-flint/README.md). SHA256: `4612dce4b1824923b559ee988f531c6a65c01f2cf46214a4e72261c1dffb04b8`.

## Corrected arithmetic runtime for the prime-186 interval certificate

2026-09-05. This removes a specific reproducibility obstacle. It does not prove a prime-gap bound, discharge a Lean axiom, or replace the source certificate's checks.

The unchanged official signed-convolution regression fails with the previously installed Python-FLINT 0.9.0 / FLINT 3.6.0 wheel. A separate source-built FLINT 3.6.0 with the upstream correction passes that regression. Python-FLINT is built from source against the corrected prefix. No monkeypatch, replacement convolution, disabled assertion, or edited official certificate is used.

### Pinned inputs

* FLINT v3.6.0 archive: <https://codeload.github.com/flintlib/flint/tar.gz/refs/tags/v3.6.0>, SHA256 `4307a504622702bf0be6d8969791f7d7ff378645cf2ae3bb5a7a2b56653d97f1`.
* [Upstream signed FFT fix](https://github.com/flintlib/flint/commit/7ad753d51c82fdec115cb179b41d0e581f1cb0ec), from [PR2790](https://github.com/flintlib/flint/pull/2790). Download its `.patch` URL as `flint-7ad753d.patch`; SHA256 `333788fe3d7fe1c24ca10e5ef33f492eae68de6202568e75e18e1bcd7bfb71ff`.
* Official PrimeGaps186 source at `61340d0b74163003b32756bb16e91d9209a5e330`; `prime_gap_186_certificate.py` SHA256 `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`.
* Host build: Apple Silicon macOS, clang, Python 3.12.9, Python-FLINT 0.9.0, NumPy 2.2.6, Homebrew GMP 6.3.0 and MPFR 4.2.2. FLINT was configured with `--enable-assert --disable-static`.

The upstream fix corrects the conversion of a residue near the halfway point of the FFT coefficient ring into a signed integer. Testing only the leading limbs misses boundary cases with nonzero lower limbs. The patch contains both the correction and targeted native test cases. The version string remains 3.6.0; the patch hash and actual linked-library path distinguish this runtime from the failing wheel.

### What passed

1. Native FLINT suites `fmpz_vec`, `fmpz_poly`, `arb`, `arb_poly`.
2. The original certificate's `check_flint_signed_fft()` and `_cap_check_environment()`, called unchanged.
3. 467 full products and 2,188 truncated products compared with an independently implemented Python integer double loop. These include both signs, limb boundaries, the original 509/510-bit failure, zero polynomials, and deterministic random coefficients. The comparison took approximately 0.80 seconds here.
4. Ten selected Python binding tests for the integer/rational polynomial and Arb APIs used by the certificate.

`otool -L` confirms that the extension loads the corrected isolated `libflint.24.0.dylib`. The old wheel remains available and fails as a negative control, as recorded in `negative-wheel-control.json`.

### A separately disclosed full-suite failure

The **complete** Python-FLINT suite did not pass: with native assertions enabled, `test_fmpz_functions` aborts in `_n_jacobi_unsigned`. Its test table invokes `fmpz(2).jacobi(n)` at zero and even denominators. The installed FLINT source documentation for `fmpz_jacobi` specifies an odd positive denominator and says parity/sign are not checked. The Python wrapper forwards the input without enforcing that precondition.

The certificate uses no Jacobi call. The native integer/polynomial and Arb suites, its own regression, and the selected binding tests passed independently. We retain the abort logs and keep assertions enabled; we do not claim that all Python-FLINT tests passed or that the library has been universally verified. Resolving the separate Jacobi wrapper/test contract is postponed.

### Reproduction on this host

The source/build/install cache is separate from the Dropbox research record. The original PrimeGaps186 clone is unchanged. For a fresh directory without spaces:

```sh
bash build_runtime.sh DOWNLOAD_DIRECTORY BUILD_DIRECTORY
bash build_python_binding.sh BUILD_DIRECTORY PYTHON_EXECUTABLE
BUILD_DIRECTORY/venv/bin/python signed_convolution_check.py \
  --official-script PATH_TO_UNCHANGED_CERTIFICATE \
  --output NEW_RECEIPT.json
```

The first script verifies both source download hashes, refuses to overwrite an existing checkout, applies the upstream patch, compiles, runs the four native suites, and installs to `BUILD_DIRECTORY/prefix`. The second creates a fresh virtual environment and builds the binding with the needed macOS GMP link path. GMP, MPFR, autoconf, automake and libtool must already be installed. The script assumes the Homebrew paths used on this host; other platforms should adjust the toolchain paths while preserving source hashes and the regression.

On this run the usable interpreter is:

```text
/Users/qingyunsun/.cache/astra-research/flint-3.6.0-patched/venv/bin/python
```

The binding build first encountered two configuration errors: the optional `add_flint_rpath` setting emitted a linker flag unsupported by Apple's linker; without it, the transitive GMP library still needed an explicit `-L` path. The successful build omits the former and supplies the latter. These errors and the exact successful commands are retained in their separate logs. They caused no change to the mathematics or the official certificate.

### Acceptance and limits

The purpose of this runtime is to execute new outward-enclosed integrals with the original arithmetic safeguards. Round four's first application is a positive lower integral on one genuine outer failure rectangle. It does not require recomputing all 149 existing upper integrals merely to validate the new rectangle; combining the new credit with the old final margin explicitly inherits the published upper endpoints.

Full new `k=39` support restoration, complete physical-integral replay, a portable binary distribution, and proof-assistant verification remain separate work. The runtime can be abandoned by using another interpreter; the original wheel and official source were not overwritten.


# Current report 07: prime186_round5

Source: [research/reports/prime186_round5.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/reports/prime186_round5.md). SHA256: `7ad8c798736bd40b7125784af7ec69a208075665c8efcfd69d4c33adf68b447e`.

## Round 5: radius-dependent sieve bounds and a negative geometry search

The bounded search is complete. Ten radius/plateau configurations were evaluated with all 77 polynomial coefficients reoptimized at a coarse grid, and two nearby candidates were refined at the official grid. **Neither geometry change improves the original k=39 result.** The useful mathematical output is a proved variable-radius exceptional-square estimate, an exact sufficient source template, and a precise repair for a newly activated source row. None proves DHL(39,2), a prime-gap bound below 186, or a global obstruction to those goals.

This report follows [Round 4](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/reports/prime186_round4.md), where a new outward lower integral increased the fixed k=40 proof margin to 24.86626 ppm by combining the new credit with inherited published endpoints. That result remains valid in its stated scope. Its approximately 1.5 ppm credit cannot be assigned to new k=39 vectors or supports without computing their own integrals.

### 1. Evidence and proof status

Three independently assigned research components are preserved with their original scripts, outputs and reports:

| Component | Result | Evidence status |
|---|---|---|
| [Exceptional-square extension](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round5/exceptional-radius/EXCEPTIONAL_RADIUS_EXTENSION.md) | A radius-dependent constant follows from the existing counting argument over an explicit open interval | Ordinary written proof plus exact rational certificate; not Lean formalization |
| [Source geometry audit](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round5/geometry-audit/GEOMETRY_SOURCE_AUDIT.md) | Twelve of fifteen natural cap templates pass, with a uniform one-layer mesh repair and a common inner-square source | Exact arithmetic and a sufficient-template proof; no physical sieve integrals |
| [Finite geometry search](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round5/geometry-trial/REPORT.md) | Ten coarse points and two refinements give no improvement from changing radius/plateau | Floating cap-only optimization; no interval optimum or support restoration |

The primary proof is [Improved short gaps between primes](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), especially Propositions 3.10, 3.11, 4.2 and 4.6. The companion certificate is pinned to [PrimeGaps186 commit 61340d0](https://github.com/openai/PrimeGaps186/tree/61340d0b74163003b32756bb16e91d9209a5e330). Its Python source SHA256 is `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`. The preserved source is unchanged.

### 2. A parameterized exceptional-square estimate

The original proposition bounds an exceptional square with a coefficient-root radius at most 11/40. Its proof uses this radius in the ordinary CRT error, not in a new prime-distribution hypothesis. Let r bound **every** outer, inner, correction and exact-face coefficient root in the finite canonical combination. Retain the original global physical prime cap 0.19037, the fixed-profile assumptions and the original exceptional majorant.

Set

\[
\xi_*=0.19038,\quad a_*=0.40481,\quad
h_{\rm ex}=\frac{a_*-2\xi_*}{1024},\quad
s_j=2\xi_*+j h_{\rm ex},\quad
z_j=\frac{1-2r-s_j}{2}-10^{-4}.
\]

The stronger convenient range

\[
\frac{4879903}{40960000}<r<\frac{59499}{200000}
\quad (0.1191382568359375<r<0.297495)
\]

makes every auxiliary exponent positive and smaller than 0.19037. Each bin has the identical strict counting slack

\[
s_j+2r+2z_j=\frac{4999}{5000}<1.
\]

The limiting unordered-pair measure has density

\[
f(s)=\frac1s\log\frac{s-\xi_*}{\xi_*}.
\]

This density increases on the required interval. A right-endpoint bound for its 1024 bin masses, the odd degree-21 logarithm upper polynomial, and upward rounding at scale 10 to the power minus 25 give an exact rational upper constant. The resulting exceptional-square estimate has the same full fragment norm as the primary proposition. The detailed proof checks marked-prime separation, exact-face support, nonsquarefree error, and the finite canonical class; it is not a claim for arbitrary coefficient arrays.

| Physical radius r | Exact certified terminating-decimal upper constant | Convenient safe bound |
|---|---:|---:|
| 0.272 | 0.3014041534851816226069683 | 0.301405 |
| 0.2742997 | 0.3273225381113663650584938 | 0.327323 |
| 0.275 | 0.3361336040272905676441604 | 0.336134 |
| 0.276 | 0.3495799968949037559942978 | 0.349580 |
| 0.278 | 0.3800259215656200578230129 | 0.380026 |
| 0.280 | 0.4163697504037337478611794 | 0.416370 |
| 0.282 | 0.4605417963468921175216614 | 0.460542 |

At r=0.275 the script exactly reproduces the paper's fraction

\[
\frac{840334010068226419110401}{2500000000000000000000000}.
\]

Two independent implementations agree on the five radii used in the search. The parametric proof also constructs a downward lower bound on the actual bin constant. At r=0.276 it exceeds 0.3489733171, so this unchanged bin mechanism truly cannot retain 0.34 there. An upper bound exceeding 0.34 alone would not establish that conclusion. No claim is made that every different exceptional-square argument must have this loss.

The constant must be propagated into the hybrid coefficient

\[
b_h=-\frac{49599}{20000000}K,
\]

and all derived costs. The convenient old shortcut \(|b_h|<10^{-3}\) fails with the displayed constants at 0.280 and 0.282. The counting proposition remains valid there, but downstream restoration needs its actual operator bound and coefficient checks. Only radii through 0.278 were used in the present cap search.

### 3. Geometry that preserves the distribution ladders

The screen keeps \(\rho=0.262499\), \(\rho_*=0.2624989\) and imposes

\[
S=r/\rho_*,\qquad T_1=(0.5252997-r)/\rho_*,\qquad T_0=1.997-S.
\]

Thus the old and new combined root sums stay fixed. The nominal distribution ladders remain the same. Their root thresholds, actual grid endpoints, and retained rows do not all remain the same.

For \(\epsilon=10^{-7}/\rho\), put \(A=S+\epsilon/2\) and \(C_\nu=T_\nu+\epsilon/2\). The complementary allocations

\[
\phi_D(t)=\min(3t/2,L_\nu),\qquad \phi_E(t)=3t-\phi_D(t)
\]

give a sufficient natural plateau template when

\[
\frac{3A-C_\nu}{4}\le L_\nu\le\frac{3C_\nu}{5}.
\]

The audit checks the largest-fragment owner and opposite-root inequalities and the nonlargest-witness reduction. Both common-height choices

\[
L_0=L_1=(3A-C_0)/4\quad\hbox{or}\quad L_0=L_1=3C_0/5
\]

preserve both source intervals and nested inner caps. Equal heights avoid an unnecessary extra outer-cap cost caused by the larger new inner radius. This is a valid exact simplification even though the sampled numerical values did not improve.

Fifteen radius/plateau cases were audited: five radii and three choices each. Twelve pass. The unchanged published fraction \(L_\nu/C_\nu=0.575\) fails the natural cap formulas at 0.275, 0.276 and 0.278. Those failures concern this sufficient cap template; they do not invalidate all sieve supports at those radii. The original fraction was used in the numerical screen only where it passes.

At r=0.272 the old inner-square source level 0.5062 is too small. A common replacement \((\omega_s,\delta_s)=(0.0035,0.025)\) gives level 0.507 and satisfies the requisite source and row-12 containment inequalities throughout the screened interval. A rational exponential-sum inequality also rechecks \(C_{\rm op}=4\) at k=39 throughout this interval. No k=40 operator constant is silently inherited.

### 4. An actual numerical-cover obstruction and its repair

At the official 98,304 grid, the untrimmed points r=0.272, 0.275, 0.276 and 0.278 retain new-ladder row 39. Its activation width is approximately \(1.8866250\times10^{-5}\), less than two grid cells. The source theorem is still applicable, but the original low-witness numerical implementation's two-cell guard fails.

Let \(h=S/98304\), \(J_1=\lfloor T_1/h\rfloor\) and

\[
J_O=\min\{98303,\lfloor B_{n,39}/h\rfloor-J_1\}.
\]

Restrict the outer index sum to \(\sum_i j_i\le J_O-k\). This removes at most one outer layer throughout the entire interval \([0.272,0.278]\), excludes row 39, retains row 38, and leaves its activation width greater than two cells. The exact audit proves the uniform statement using endpoint inequalities; it is not an interpolation from the five sampled radii.

The repair keeps h, the normalizer, the convolution length and nominal S fixed. Every erased face must be derived again from the trimmed outer function. **The numerical trials reported here are untrimmed.** Neither their quotients nor the original 97-component numerical cover can be represented as a completed repaired certificate.

Even after trimming, the failure cover must be regenerated from the new source thresholds, caps, core boundaries and same-coordinate terms. All resulting physical integrals need fresh outward evaluation. The old 149 upper integrals and Young-cost values are not transferable solely because the analytic inequalities pass.

### 5. What the finite search found

All configurations retain the original product profile and the 77-dimensional polynomial span. Every vector is optimized afresh. The exact configuration files, full matrices, eigenvectors, conditioning, scalar reevaluations and run times are in the [search archive](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round5/geometry-trial).

| Fine-grid candidate | Direct cap quotient | Difference from the Round 4 optimized original geometry |
|---|---:|---:|
| Round 4 original r=0.2742997, original plateaus | 0.9943963993644909 | reference |
| r=0.2742997, common maximum height | 0.9943734016224463 | −22.9977 ppm |
| r=0.275, common maximum height | 0.9943501891039260 | −46.2103 ppm |

Ten coarse configurations covered r=0.272 through 0.278. The only coarse increase over the original baseline, approximately 0.6183 ppm, came from improving the exceptional constant at the unchanged original geometry; it did not come from a radius/plateau change. Only the two nearby geometry candidates above were refined. The full coarse table is preserved in the detailed report.

The scaled Gram condition number reaches approximately \(4.307\times10^{10}\). For the twelve full-77 candidates used in the comparisons above, matrix and direct candidate evaluations disagree by at most \(2.884\times10^{-10}\), and the full scaled-pencil relative residual is at most \(5.30\times10^{-16}\). Across all thirty-six saved candidates, including truncated whitening spaces, those maxima are instead \(3.0281\times10^{-10}\) and \(4.915\times10^{-9}\). This qualifies the scope of the smaller maxima in the original search report. The truncated residual is measured against the full pencil, so it need not be at roundoff scale.

These comparisons support the observed ordering at the tens-of-ppm scale. They do not provide outward error bounds, a certified finite-family maximum, or a no-go theorem for larger trial spaces. The host's NumPy long-double type has only 64 bits; no extended precision is claimed.

The approximately 5604 ppm original k=39 deficit remains far larger than the particular fixed-k=40 credit recovered in Round 4. This comparison guides effort; it does not upper-bound every possible restoration credit.

### 6. Integration verification and next decision

The primary integration replay runs in a temporary copy. It checks the seven exact exceptional constants, all fifteen source cases, twenty grid-mask nesting cases, and the saved twelve 77-by-77 matrix archives with their thirty-six candidate vectors. Source SHA verification is mandatory. Original outputs are preserved; only timing and optional source-text metadata are excluded from exact replay comparisons. See [recheck.py](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/logs/round5-integration/recheck.py) and [receipt](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/logs/round5-integration/recheck.json).

The 53-file [intake manifest](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round5/INTAKE_MANIFEST.json) records original and published hashes. The only two code changes made for publication let an external primary-source path be supplied through `PRIME186_SOURCE`. Original per-run manifests remain intact and describe their own execution snapshots.

The next meaningful prime-gap experiment should change a component large enough to affect the k=39 deficit, such as the product profile or an analytically justified support family, or establish a certified upper bound for the currently searched finite family. Repeating these endpoint scans is postponed. Full restored certificates for the present negative candidates are also postponed. This prime-sieve work supports the wider research programme but supplies no new arithmetic transfer theorem for zeta zeros.

This is a checkpoint in an active research goal. The 333-page public handoff remains the earlier `055a4a0` snapshot; Rounds 4 and 5 are separate subsequent reports. No major-conjecture completion is claimed.


# Current report 08: EXCEPTIONAL_RADIUS_EXTENSION

Source: [research/prime-gaps/round5/exceptional-radius/EXCEPTIONAL_RADIUS_EXTENSION.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round5/exceptional-radius/EXCEPTIONAL_RADIUS_EXTENSION.md). SHA256: `70326c9bd4430855349a64fc2863e0dcccd80f40e9b0b5b28750925e0c7de54b`.

## A variable-radius version of the exceptional-square estimate

**Status:** ordinary written derivation from the primary paper, with an exact rational reproduction of its finite numerical certificate. This extends the stated parameter range of Proposition 3.11 without adding a prime-distribution hypothesis. It does not establish a new prime-gap bound or certify a new support geometry.

**Primary source:** OpenAI, *Improved short gaps between primes*, dated 30 August 2026, Propositions 2.23, 3.10 and 3.11, Lemmas 3.2, 3.3 and 3.9, equations (3.26)–(3.35). The [primary PDF](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf) has Proposition 3.11 on page 23. The locally retained text is ../../sources/openai-short-gaps.txt, lines 1522–1607. The local text is the source actually checked in this audit; its SHA256 is ded13a7c74fcfce64e85769e05b5869803dccdf53b88be2c2f3c0b344f95ee84.

**Artifacts:** certify_exceptional_radius.py is a standalone Python-standard-library certificate. certify_exceptional_radius.json contains the exact reduced rational upper bounds and all endpoint checks. No float arithmetic or numerical quadrature enters those upper bounds.

### 1. Conclusion and certified constants

Replace the fixed physical coefficient radius 11/40 in Proposition 3.11 by a fixed radius r. Keep the same prime cap, exceptional minorant, fixed-profile assumptions, 1024 bins, and strict CRT slack. The same argument works throughout

\[
\frac{4879903}{40960000}<r<\frac{59499}{200000},
\qquad 0.1191382568359375<r<0.297495.
\tag{1}
\]

This range has the convenient stronger condition 0<z_j<xi_0<\(\xi_*\) for every bin. Proposition 3.10 itself only requires z_j<\(\xi_*\), giving the slightly wider lower endpoint in Section 3.

The following terminating decimals are **exact rational upper bounds**, rather than rounded numerical approximations. Every last printed digit belongs to the certificate.

| Physical coefficient radius r | Certified K_1024^+(r), exact decimal | Simpler safe upper bound |
|---|---:|---:|
| 0.272 | 0.3014041534851816226069683 | 0.301405 |
| 0.2742997 | 0.3273225381113663650584938 | 0.327323 |
| 0.275 | 0.3361336040272905676441604 | 0.336134 |
| 0.276 | 0.3495799968949037559942978 | 0.349580 |
| 0.278 | 0.3800259215656200578230129 | 0.380026 |
| 0.280 | 0.4163697504037337478611794 | 0.416370 |
| 0.282 | 0.4605417963468921175216614 | 0.460542 |

At r=11/40 the exact reduced fraction is

\[
K_{1024}^{+}(11/40)=
\frac{840334010068226419110401}
{2500000000000000000000000},
\tag{2}
\]

which reproduces equation (3.35) of the paper exactly. In particular, the scale printed as “1025” by the text extraction is **10 to the power 25**, not the integer 1025.

One may safely use any K at least K_1024^+(r) in the exceptional-square conclusion. The same finite-bin proof cannot justify retaining K=0.34 at r≥0.276: a separate exact lower bound on its bin constant already exceeds 0.34 there; see Section 5. This does not assert that every other possible method of bounding the exceptional sum must fail with 0.34. Conversely, using the actual physical radius 0.2742997 in this proposition permits the smaller exceptional constant in the table, subject to the common-support condition below.

### 2. Precise parametric proposition

Keep the setting and normalization P_x of Proposition 3.11. Fix

\[
a_* = \frac{40481}{100000},\qquad
\xi_* = \frac{9519}{50000},\qquad
\xi_0 = \frac{19037}{100000} < \xi_*.
\]

Let C_i be a finite real linear combination, with coefficients independent of x, of the same canonical (k−1)-coordinate sums and exact faces used in that proposition. Assume their profiles are fixed and bounded and have limiting-null discontinuity sets. Let H_i denote their corresponding combination of canonical profiles and marginals.

Assume every summand has physical coefficient-root radius at most r, and every outer and inner coefficient root satisfies the original global largest-prime-factor cap

\[
P^+\!\left(\prod_j d_j\right)\le x^{\xi_0}.
\tag{3}
\]

The radius assumption must hold for **all roots actually used in the linear combination**. In particular, it is insufficient to use the radius of an outer trial function if an inner correction, another summand, or a separately constructed exact-face array has larger retained-coordinate radius. A valid sufficient choice is the maximum over all outer, inner, correction and exact-face radii. An exact face obtained through Lemma 3.3 retains the same total support bound as its parent array.

For fixed r in (1), define K_1024^+(r) by equation (12) below. Then

\[
\sum_n' b(n+h_i;x)\,C_i(n)^2
\le P_x\left(K_{1024}^{+}(r)\,\|H_i\|_2^2+o(1)\right).
\tag{4}
\]

The norm remains the full fragment norm. Every profile, radius, cutoff and finite band choice is fixed before x tends to infinity; exact face arrays may depend on x as in the original proposition. No assertion uniform as r approaches the upper endpoint is made.

This is deliberately stated for the same canonical class as the source. It does not assert that an arbitrary coefficient array has a bounded inverse diagonal merely from a radius bound.

### 3. Exact parameter range and the strict counting slack

Write

\[
h=\frac{a_*-2\xi_*}{1024}=\frac{481}{20480000},
\qquad s_j=2\xi_*+jh\quad(1\le j\le1024),
\]

\[
c(r)=1-2r-\frac1{5000},\qquad
z_j(r)=\frac{c(r)-s_j}{2}
=\frac{1-2r-s_j}{2}-\frac1{10000}.
\tag{5}
\]

Since s_j increases, the minimum z occurs at j=1024 and the maximum at j=1. Direct rational arithmetic gives

\[
z_{1024}(r)=\frac{59499}{200000}-r=0.297495-r,
\]

\[
z_1(r)=0.3095082568359375-r.
\tag{6}
\]

Thus all z_j are positive exactly when r<0.297495. The stronger condition z_1<xi_0 is exactly the lower bound in (1). The necessary condition for Proposition 3.10 is only z_1<\(\xi_*\), which gives

\[
\frac{24397467}{204800000}<r<\frac{59499}{200000},
\qquad 0.1191282568359375<r<0.297495.
\tag{7}
\]

Both are strict ranges. At the upper endpoint the last auxiliary exponent is zero, and the proof's Selberg-energy asymptotic with a fixed positive exponent is unavailable.

For every bin, every valid r has exactly the original counting margin:

\[
s_j+2r+2z_j=1-\frac1{5000}=\frac{4999}{5000}<1.
\tag{8}
\]

The following endpoint values show the requested radii lie comfortably inside the valid range.

| r | Minimum z_j | Maximum z_j |
|---|---:|---:|
| 0.272 | 0.025495 | 0.0375082568359375 |
| 0.2742997 | 0.0231953 | 0.0352085568359375 |
| 0.275 | 0.022495 | 0.0345082568359375 |
| 0.276 | 0.021495 | 0.0335082568359375 |
| 0.278 | 0.019495 | 0.0315082568359375 |
| 0.280 | 0.017495 | 0.0295082568359375 |
| 0.282 | 0.015495 | 0.0275082568359375 |

The original displayed bound z_j<863/25000=0.03452 is specific to r=0.275 and need not be retained. The operative inequalities are positivity, z_j<\(\xi_*\), the global coefficient cap xi_0<\(\xi_*\), and (8).

### 4. Arithmetic proof of the extension

**Diagonal reduction.** Apply exactly the inversion and face identities from Lemmas 3.2 and 3.3, as in the first paragraph of Proposition 3.11. They express C_i as B_{y_x,i} for a uniformly bounded raw array with the same physical radius bound and hereditary prime cap. The full diagonal norm converges to the norm of H_i. Neither identity uses the numerical value 11/40.

**Marked-prime separation.** In Proposition 3.10 use the ambient retained-index cap min{zeta,xi_0/\(\rho_*\)}. Its physical exponent is at most xi_0. Every marked prime p or q has exponent at least \(\xi_*\), so it exceeds both that cap and the auxiliary cutoff exponent z_j. These are exactly the separation hypotheses \(\xi_*\)>max{\(\rho_*\) zeta_eff,z_j} needed by Proposition 3.10.

**Nonsquarefree exceptions.** Proposition 2.23 bounds the number of nonsquarefree points in the exceptional support by O(x^(1−\(\xi_*\))). Lemma 3.2 and the divisor bound make each fixed canonical sum x^o(1) pointwise; a finite linear combination and its square have the same form of bound. Consequently their total contribution is x^(1−\(\xi_*\)+o(1))=o(P_x). A fixed change of radius does not remove this fixed power saving. The same original fixed-shift endpoint treatment remains applicable.

**Positive majorant.** On the remaining squarefree support, Proposition 2.23 gives b≤(12/5)N_2, where N_2 counts unordered marked pairs p<q with p,q≥x^(\(\xi_*\)) and pq<x^(a_*). On the exceptional support all prime factors are at least x^(\(\xi_*\)); Lemma 3.9 therefore gives L_{x^(z_j)}=1 for every selected bin. The majorant is positive before opening any signed coefficient expansion, so the full square C_i^2 remains intact.

**Counting each bin.** For pairs in the jth logarithmic-product bin, pq≤x^(s_j). Apply Proposition 3.10 with radius r and exponent z_j. Its ordinary CRT error is x^(s_j+2r+2z_j+o(1))=x^(4999/5000+o(1))=o(P_x), by (8). No distribution theorem for primes or the minorant enters this counting step. There are only 1024 bins, fixed independently of x.

**Limiting pair measure.** The same prime harmonic measure as in the source gives

\[
d\mu_2(s)=f(s)\,ds,\qquad
f(s)=\frac1s\log\frac{s-\xi_*}{\xi_*},
\qquad 2\xi_*\le s\le a_*.
\tag{9}
\]

The strict arithmetic condition pq<x^(a_*) remains in the last bin. Its limiting measure is unchanged by inclusion of the endpoint because this measure has no atom there. Thus the exact limiting constant supplied by the bin argument is

\[
K_{\mathrm{bin}}(r)=
\frac{12}{5}\sum_{j=1}^{1024}
\frac{\mu_2((s_{j-1},s_j])}{z_j(r)}.
\tag{10}
\]

It remains to certify a number above this finite sum; Section 5 does so. This proves (4). All applications are instances of the primary ordinary-counting argument with a fixed changed radius.

### 5. Finite-sum certificate and why the continuum integral alone is insufficient

The natural continuous expression is

\[
K_{\mathrm{cont}}(r)=\frac{24}{5}
\int_{2\xi_*}^{a_*}
\frac{\log((s-\xi_*)/\xi_*)}{s(c(r)-s)}\,ds.
\tag{11}
\]

Within each bin, 1/(c(r)−s) is increasing. Therefore K_cont(r)≤K_bin(r). A good approximation or even a certified upper bound for K_cont alone does **not** automatically upper-bound the larger K_bin delivered by the actual arithmetic proof. We retain the paper's finite-bin certificate.

First, f in (9) is increasing throughout the interval. Differentiation yields

\[
f'(s)=\frac{s/(s-\xi_*)-\log((s-\xi_*)/\xi_*)}{s^2}.
\]

Set y=(s−\(\xi_*\))/\(\xi_*\). Here 1≤y<2, since a_*<3xi_*. Hence log y<1 while s/(s−\(\xi_*\))=1+1/y>1. The derivative is positive. In consequence, the measure of each bin is at most h f(s_j).

Set t_j=(s_j−2xi_*)/\(\xi_*\). These rational numbers belong to (0,1). The degree-21 alternating polynomial

\[
L_{21}(t)=\sum_{m=1}^{21}\frac{(-1)^{m+1}t^m}{m}
\]

satisfies log(1+t)≤L_21(t) by the alternating-series remainder. Each bin contribution in (10) is therefore at most

\[
u_j(r)=\frac{24hL_{21}(t_j)}{5s_j(c(r)-s_j)}.
\]

Every u_j(r) is positive and rational for rational r. Define

\[
K_{1024}^{+}(r)=\frac1{10^{25}}
\sum_{j=1}^{1024}\left\lceil10^{25}u_j(r)\right\rceil.
\tag{12}
\]

Then, in the correct direction,

\[
K_{\mathrm{cont}}(r)\le K_{\mathrm{bin}}(r)
\le\sum_j u_j(r)\le K_{1024}^{+}(r).
\tag{13}
\]

The script implements (12) with exact integers and fractions. Its ceiling operation is −floor(−numerator/denominator), with positive denominator. It never converts an input radius or an intermediate summand to binary floating point. An input decimal such as 0.2742997 is parsed as its exact rational value.

The accumulated upward-rounding excess is strictly below 1024×10^(−25)=1.024×10^(−22). The alternating-polynomial excess in the sum is at most

\[
\sum_j\frac{24h}{5s_j(c(r)-s_j)}\frac{t_j^{22}}{22}.
\]

For the requested radii this latter bound is between 1.87×10^(−22) and 3.06×10^(−22). The coarser right-endpoint discretization remains the main deliberate overestimate. Reducing it is a separate possible numerical refinement, not needed here.

For an additional check, the script also constructs a lower bound on K_bin. Since f is increasing and the even alternating polynomial L_22 lies below log(1+t), the jth bin contribution is at least

\[
\ell_j(r)=\frac{24hL_{22}(t_{j-1})}
{5s_{j-1}(c(r)-s_j)}.
\]

Rounding each nonnegative term down at scale 10^(−25) gives a rigorous rational lower bound on K_bin. At r=0.276 it equals 0.3489733171373295715615596, which already exceeds 0.34. At r=0.280 and r=0.282 these lower bounds are respectively 0.4156565419431563765185887 and 0.4597595157187387148411848. Thus the need to update the constant in this bin proof is not inferred merely from its upper bound exceeding 0.34.

All factors depending on r are increasing as r increases within the valid interval. In particular, both the continuum constant and the finite-bin bound are increasing, and the rounded bound in (12) is nondecreasing. A constant certified at an upper radius R consequently applies to all smaller radii for which the same proof conditions hold.

### 6. What must change downstream when this constant is used

This result supplies an exceptional-square input to the hybrid sieve; it does not certify new mixed-modulus factorizations or source conditions. Those conditions, support realizability, the actual retained prime cap and the root radii require their own checks.

If the original choices m_0=49999/50000, lambda=1/125 and kappa_def=1/50000 are retained, equation (4.28) becomes

\[
b_h(r)=\left(1-\frac{m_0}{\lambda}\right)
\kappa_{\mathrm{def}}K
=-\frac{49599}{20000000}K,
\qquad K\ge K_{1024}^{+}(r).
\tag{14}
\]

One must therefore recompute b_h, d_0 and every numerical functional or cover weight depending on them. The source's convenient assertion |b_h|<1/1000 is equivalent here to K<20000/49599. It fails for the constants in the table at r=0.280 and r=0.282. This failure does not invalidate the hybrid algebra: it means that a downstream proof cannot cite that old numerical shortcut unchanged.

In particular, restoration should check its actual coefficient

\[
1-\rho_*|b_h(r)|C_{\mathrm{op}}>0
\]

using the operator bound justified for the new support. Do not reuse C_op=4 beyond its proved support range simply because the exceptional counting proof remains valid there. The primary statement also requires d_0>0 and 0<a_h+b_h<1 wherever those multiplier bounds are invoked.

The exceptional proposition is dimension-independent at the level of this displayed constant for fixed k, but that observation does not transfer a k=40 numerical trial, norm certificate or prime-gap conclusion to k=39.

### 7. Reproduction and audit record

Run the standalone script with Python 3:

    python3 certify_exceptional_radius.py

It writes certify_exceptional_radius.json next to itself. Optional radii can be supplied as exact decimal or rational strings with --radii. The implemented certificate deliberately enforces the stronger range (1), even though Section 3 explains the slightly weaker necessary condition.

Checks completed in this audit:

1. Read the primary proofs of Propositions 2.23, 3.10 and 3.11 and the relevant support/face identities; identified exactly where radius enters.
2. Verified every one of the 1024 rational auxiliary exponents is positive, below xi_0, and has the identical strict CRT margin, for all seven requested radii.
3. Verified the odd/even alternating-polynomial difference is t^22/22 and positivity holds at every endpoint.
4. Reproduced the primary fraction in (3.35) exactly, not only its decimal digits.
5. Verified the rounding excess bound and monotonic order of the seven certified constants.
6. Cross-checked the first five values against the prime agent's separate implementation; they agree to all communicated digits, with differences in the final displayed digit explained by rounding versus this document's exact terminating decimals.
7. Added a separately directed L_22/left-density/downward-rounding lower bound on the actual bin constant to verify the strict obstruction to retaining 0.34 in this proof at r≥0.276.

Large integer numerator and denominator fields are serialized as decimal strings in the JSON, to prevent loss when it is read by a JavaScript consumer. Reconstruct the exact fraction from those strings rather than passing the decimal display through a binary float.

The certificate is exact arithmetic accompanying an ordinary proof. It has not been formalized in Lean, and this note makes no claim that an improved global prime-gap inequality has yet been certified.


# Current report 09: GEOMETRY_SOURCE_AUDIT

Source: [research/prime-gaps/round5/geometry-audit/GEOMETRY_SOURCE_AUDIT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round5/geometry-audit/GEOMETRY_SOURCE_AUDIT.md). SHA256: `c2870e1d539e1be90e82131671ec15b85d74a0a886bad299270a20cb87ecc7c9`.

## Exact source geometry for the bounded radius and plateau screen

This audit establishes a sufficient source and cap template for the round-five $k=39$ screen. It evaluates no sieve integrals and proves no smaller prime gap. The accompanying exact arithmetic checks cover physical outer radii $0.272$, $0.2742997$, $0.275$, $0.276$, and $0.278$, together with three specified plateau choices at each radius. The original source's numerical failure schedule and its 97 component bounds are **not inherited**.

The main findings are concrete. The distribution ladders themselves stay fixed, but the retained rows change after the physical grid is changed. A single inward outer index layer removes the problematic extra row. The old inner-square source fails at the smallest radius; a common replacement works throughout the screen. The exceptional-square constant and hybrid coefficients must be recomputed when the outer radius exceeds $0.275$.

### 1. Parameters and what really remains invariant

Retain the exact source constants

$$
\rho=0.262499,\qquad \rho_*=0.2624989,\qquad
 e=10^{-7}/\rho,\qquad h=S/98304,
$$

and write $r=\rho_*S$. The proposed search fixes

$$
S+T_0=\Sigma_0=1.997,
\qquad
\rho_*(S+T_1)=0.5252997.
$$

Thus $T_\nu=\Sigma_\nu-S$, where $\Sigma_1=0.5252997/\rho_*$. In particular $T_1>T_0$ throughout the screen, and their difference is constant.

The official ladder recurrence depends on $S,T_\nu$ through $E_\nu=\rho(S+T_\nu)-1/2$. Consequently **every** $\omega_{\nu,t},\delta_{\nu,t},B_{\nu,t},B^+_{\nu,t},\xi_{\nu,t}$ is unchanged. The exact script regenerates all 29 old and 43 new rows and verifies this invariance, rather than copying a rounded table.

The root-specific quantities change:

$$
a_{\nu,t}=B_{\nu,t}-T_\nu,
\qquad b_{\nu,t}=B_{\nu,t}-S.
$$

On every retained nonterminal row the recurrence gives

$$
(A,C_\nu)=
\begin{cases}
(S+e,T_\nu+e),&\text{orders 1 and 2},\\
(S+e/2,T_\nu+e/2),&\text{order 3}.
\end{cases}
$$

The exact script verifies the prime distribution inequalities of Corollary 2.19 and all minorant inequalities of Proposition 2.22. Their strict margins remain positive. Lower-order transfer requires $S-T_\nu+e\geq0$ and $\min(2S-T_\nu,2T_\nu-S)+e\geq0$, which hold here. In order three, $A+C=B+\xi$ and $\eta_D=\eta_E=\xi-e/2>0$. These are the actual combined-divisor hypotheses; a scalar modulus level alone is insufficient.

### 2. Valid plateau intervals and all largest-fragment constraints

For each ladder choose $L_\nu$ and use

$$
\phi_D(t)=\min(3t/2,L_\nu),\qquad
\phi_E(t)=3t-\phi_D(t).
$$

Both functions are nonnegative and nondecreasing, and their sum is $3t$. In the natural plateau branch used by this screen, set

$$
u_\nu=A-L_\nu,\qquad v_\nu=(C_\nu+L_\nu)/4.
$$

Here $u_\nu$ is the outer largest-fragment cap and $v_\nu$ the inner cap. The complete checks at a largest activated fragment are

$$
u+\phi_D(u)\leq A,\quad\phi_E(u)\leq C,
\qquad v+\phi_E(v)\leq C,\quad\phi_D(v)\leq A.
$$

They include both opposite-root conditions. Requiring both endpoints to lie on their plateau branches gives, in our regime $A>C>0$,

$$
\boxed{\frac{3A-C}{4}\leq L\leq\frac{3C}{5}.}
$$

The lower bound is the outer opposite-root constraint $3(A-L)-L\leq C$. The upper bound makes $v\geq2L/3$; it also implies the required outer-branch bound. The interval exists precisely when $A/C\leq17/15$ within this branch.

The balanced nonlargest-witness reduction in numerical Lemma 1.4 additionally needs

$$
\max(A,C)\leq7L/3.
$$

This was checked explicitly. It already follows from the lower endpoint here: $(3A-C)/4\geq3A/7$ since $A>C$. Below $2L/3$, both allocations equal $3t/2$; above it a nonlargest witness has inclusive tail at least $2t$, so both nonlinear obstructions and the balanced one exceed $7L/3$. This reproduces the actual reduction to nonlargest $H_{5/2}$ failures.

The intervals for $q_\nu=L_\nu/C_\nu$ are:

| Physical outer radius | Old $q_{\min}$ | New $q_{\min}$ | Upper endpoint |
|---|---:|---:|---:|
| 0.272 | 0.5588487836871093 | 0.5553700704402632 | 0.6 |
| 0.2742997 | 0.5731934484723361 | 0.5696206036612396 | 0.6 |
| 0.275 | 0.5776142414184422 | 0.5740121594208600 | 0.6 |
| 0.276 | 0.5839701980513703 | 0.5803258928258113 | 0.6 |
| 0.278 | 0.5968370022033588 | 0.5931065437793680 | 0.6 |

The exact fractions are in the JSON; decimal table entries are displays, not substitutes for endpoint tests. The original common fraction $q=23/40$ fails this natural cap template at 0.275, 0.276, and 0.278. In particular, the old opposite-root inequality still fails at the shared minimum outer cap for that unchanged choice.

The old-ladder upper radius for this branch is

$$
r\leq\frac{17\rho_*\Sigma_0+\rho_*e}{32}
=0.2784867267531238\ldots;
$$

the new-ladder bound is $0.2790654687499988\ldots$. These bound this cap parameterization, not every possible sieve support. Outside this interval one could choose smaller piecewise caps, a different allocation, or pay for additional largest-fragment failures; none is certified by the present template.

For completeness, the unrestricted largest-fragment inverse constraints can be computed piecewise. The outer owner inverse is $2A/5$ if $A\leq5L/3$, otherwise $A-L$; its opposite inverse is $2C/3$ if $C\leq L$, otherwise $(C+L)/3$. Take their minimum. The inner owner inverse is $2C/5$ if $C\leq5L/3$, otherwise $(C+L)/4$; intersect it with $t\leq2A/3$ when $L>A$. This explains precisely what ceases to hold when the simple endpoint formulas are used outside their range.

### 3. Shared supports, nested faces, and inward caps

The usable outer domain retains **both** source ladders. For a root of total $s$, each row has its original safe-core alternative $s\leq a_{\nu,t}$ and, outside it, its full owner-tail and opposite-root predicates. The inner base requires both old and new inner predicates:

$$
O=H_O\cap\bigcap O_{\nu,t},\qquad
L_1=H_1\cap L_{\rm new},\qquad
L_0=H_0\cap L_{\rm old}\cap L_{\rm new}.
$$

The exact script constructs each cap envelope as the running minimum of every applicable row cap, starting with the global cap $\zeta=0.19037/\rho$. The radius where a row becomes active is its own $a_{\nu,t}$ or $b_{\nu,t}$. It does not assume that the original three-shell comparator continues to hold after independent plateau changes.

For independent $L_0,L_1$, the final inner caps must satisfy $C_0+L_0\leq C_1+L_1$ to preserve their simple nesting. Otherwise clip the base cap to the enlarged cap on each overlapping radial interval. The implemented base envelope takes the running minimum of the old and new inner cap constraints, so $H_0\subseteq H_1$ holds cell by cell. This largest-fragment clipping does not replace the full inner tail predicates in $L_0$.

The two common-height choices used by the bounded screen,

$$
L_0=L_1=(3A-C_0)/4\quad\text{or}\quad L_0=L_1=3C_0/5,
$$

satisfy both ladders' intervals and nested caps automatically. At the common minimum, the physical caps $\rho_*u$, $\rho_*v_0$, and $\rho_*v_1$ are constant as $r$ varies under the fixed-sum constraints. The source activation radii still move. Thus this is a redistribution of radial room, not a simultaneous increase of all prime-factor allowances.

For a $d$-coordinate radial shell $(l,u]$, retain index sums

$$
\max(0,\lfloor l/h\rfloor-d+1)\leq j\leq
\min(n-1,\lfloor u/h\rfloor-d),\qquad n=98304-k,
$$

and round each fragment cap down to $h\lfloor z/h\rfloor$. Using the full upper cell endpoint is what safely handles a cell crossing an activation core. The output records all resulting cells and verifies nesting directly. The global physical cap remains $\rho_*\zeta<0.19037<\xi_*$, including inside radial cores, so the roughness restriction used in the exact-face identity is preserved.

### 4. The extra row 39 and the one-layer repair

With the untrimmed outer mask, its largest total is $98303h$; the enlarged inner largest total is $J_1h$, where $J_1=\lfloor T_1/h\rfloor$. Retain a row precisely when $B_{\nu,t}$ is strictly below the corresponding actual combined upper bound. The exact results are:

| Radius | Untrimmed new retained rows | Outer layers to trim |
|---|---|---:|
| 0.272 | 0 through 39 | 1 |
| 0.2742997 | 0 through 38 | 0 |
| 0.275 | 0 through 39 | 1 |
| 0.276 | 0 through 39 | 1 |
| 0.278 | 0 through 39 | 1 |

The old retained rows remain 0 through 27. The new extra row has

$$
\xi_{n,39}=1.886625042412619\ldots\cdot10^{-5},
$$

only 1.75–1.79 cells at these meshes. It violates the old numerical prerequisite $\xi>2h$ and the implementation's first-bin assertion. The analytic source remains valid because $\xi>0$; the breakdown concerns reuse of that numerical cover.

A rigorous inexpensive repair is

$$
J_O=\min\{98303,\lfloor B_{n,39}/h\rfloor-J_1\},
\qquad
\sum_i j_i\leq J_O-k.
$$

Then $(J_O+J_1)h\leq B_{n,39}$, so row 39 is unnecessary. At $k=39$, the trimmed outer index maximum is 98263; the untrimmed maximum is 98264. Keep $h$, $n$, the normalizer $Z$, and nominal $S$ fixed; trim the outer radial mask and derive every erased face from that changed $F$.

This repair is uniform for the whole radius interval $[0.272,0.278]$, not merely the five sampled points. Writing $\Delta=\Sigma_1-B_{n,39}$, the exact script verifies

$$
h_{\max}<\Delta<2h_{\min},\quad
B_{n,39}-B_{n,38}>h_{\max},\quad
\xi_{n,38}>2h_{\max}.
$$

Thus at most one layer is removed, row 38 remains active, and its two-cell guard holds. Separate exact inequalities keep old row 27 active and old row 28 excluded. Merely increasing grid resolution is not an automatic repair: the larger actual endpoint can activate still later rows.

### 5. Common inner-square source and the exceptional constant

The original inner-square level $0.5062$ is insufficient at $r=0.272$, where $2\rho_*T_1=0.5065994$. Use instead

$$
\omega_s=0.0035,\qquad\delta_s=0.025,
\qquad 1/2+2\omega_s=0.507.
$$

The prime order-two criterion has margin $3-280\omega_s-80\delta_s=0.02$; the fixed-$\sigma_0$ bilinear margin is $0.003996$. Every minorant inequality is also checked exactly. Put

$$
B_{\rm BV}=1/(2\rho),\quad c_s=B_{\rm BV}-T_1,\quad \xi_s=\delta_s/\rho.
$$

The retained new row 12 implies the required inner-square predicate because $c_s\geq b_{n,12}$ and $\xi_s\geq\xi_{n,12}$. The minimum core containment margin on this interval is greater than $0.02539$; the activation margin is greater than $0.04470$. The common source level exceeds every actual inner-square radius by at least $0.0004006$. The retreat $\rho_*<\rho$ retains room for the presieving modulus.

The exceptional-square proof also depends on the maximum radius of **all** coefficient roots, including exact faces. Here it is safe to use $r_c=r$. Repeating the original 1024-bin rational upper sum gives:

| $r_c$ | Safe upward six-decimal $K_{\rm ex}$ |
|---|---:|
| 0.272 | 0.301405 |
| 0.2742997 | 0.327323 |
| 0.275 | 0.336134 |
| 0.276 | 0.349580 |
| 0.278 | 0.380026 |

The script reproduces the paper's exact $r_c=0.275$ endpoint before evaluating the new radii. The separate independent proof is in `../exceptional-radius/EXCEPTIONAL_RADIUS_EXTENSION.md`. It confirms positive auxiliary cutoffs below the global cap and the unchanged counting margin $1/5000$. It also proves that this finite-bin mechanism already exceeds 0.34 at radius 0.276; that is not a universal lower bound on the best possible exceptional-square constant.

With the unchanged minorant mass and $\lambda=1/125$, recompute

$$
a_h=m^2-m\lambda,\qquad
b_h=(1-m/\lambda)(1-m)K_{\rm ex},\qquad d_0=1-a_h-b_h.
$$

Every screened radius retains $-10^{-3}<b_h<0$, $0<a_h+b_h<1$, and $d_0>0$ with the displayed safe constants. The script records these updated coefficients. Keeping the old $K=0.34$ beyond the old radius hypothesis is not justified by that proposition.

Finally, $C_{\rm op}=4$ remains valid at $k=39$: an exact finite exponential sum proves $\log39<3.664$, and

$$
\frac{39S\log39}{38}<\frac{39S\cdot3.664}{38}\leq3.982482<4.
$$

This rechecks the operator bound rather than importing the original $k=40$ estimate at changed $S$.

### 6. What remains before a sieve certificate

The exact script examined 15 radius/plateau cases in about two seconds. Twelve satisfy the natural cap template; the unchanged $q=23/40$ choices at 0.275, 0.276, and 0.278 are explicitly rejected. For the accepted cases it verifies ladder invariance, strict analytic source inequalities, natural plateau conditions, opposite-root caps, cap nesting, actual combined-modulus bands, the one-layer repair, common inner-square coverage, and the updated hybrid signs. `geometry_feasibility.json` stores exact fractions and regenerated cell masks; `geometry_feasibility.log` records the run.

No original integral bound survives merely because these hypotheses pass. The next obligation is to regenerate the nonnegative failure cover from the new thresholds, core boundaries, rounded caps, and originating rows, including low-witness clipping and same-coordinate contributions. Then evaluate the changed cap and restoration forms with outward arithmetic. The original 97-component numerical values and frozen Young parameters are not a ready-made certificate for a new point. Keeping positive old Young parameters is algebraically possible, but their new costs require fresh integrals and their previous optimality is not inherited.

No further geometry scan is part of this audit. The adjacent numerical agent's candidate screening remains a cap-only experiment until those restored forms are available. A negative candidate quotient does not prove a global sieve obstruction, and a positive cap quotient alone would not prove a smaller prime gap.

Run `python3 geometry_feasibility.py` to reproduce the certificate. The sources are the [official main proof](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf), especially Propositions 3.11, 4.2, 4.6 and Lemma 4.3, and the [numerical companion](https://github.com/openai/PrimeGaps186/blob/61340d0b74163003b32756bb16e91d9209a5e330/short_gaps_numerics.pdf), §§1.1–1.5. The preserving official certificate file has SHA256 `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`. No official source was modified.


# Current report 10: REPORT

Source: [research/prime-gaps/round5/geometry-trial/REPORT.md](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c74b326afb90b79d16ce480b183111e0d5f7daf6/research/prime-gaps/round5/geometry-trial/REPORT.md). SHA256: `a0d2aa154e278797bd1065d7a5c78fc8d0c650e14c6b43b4d0200f84465f9462`.

## Round 5: bounded radius and plateau search at k = 39

**Status:** completed exploratory cap-only search. Ten configurations were screened at 16,384 intervals; only two were refined at the published 98,304 intervals. Every configuration reassembled and optimized all 77 polynomial coefficients. No improved cap candidate was found from the radius/plateau changes. No support-restored certificate, DHL(39,2), smaller prime gap, or global variational upper bound is asserted.

The best original-geometry Round 4 value remains `0.9943963993644909`. At the fine grid, the two nearby Round 5 geometry choices gave `0.9943734016224463` and `0.9943501891039260`. Their deficits from one remain about 5,627 and 5,650 parts per million. This is substantially larger than the approximately 1.5 ppm rigorously recovered alpha credit in Round 4.

### 1. Exact scope and objects

The starting point is the official [PrimeGaps186 repository](https://github.com/openai/PrimeGaps186), pinned in our preserved clone to `61340d0b74163003b32756bb16e91d9209a5e330`. The independent engine reads only the two literal coefficient tables from `prime_gap_186_certificate.py`; it neither imports nor changes the official runtime. The source SHA256 is `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`.

We vary the physical outer radius r while imposing the exact constraints

    rho = 0.262499, rho_star = 0.2624989,
    S = r / rho_star,
    T1 = (0.5252997 - r) / rho_star,
    T0 = 1.997 - S.

Thus both `rho_star*(S+T1)=0.5252997` and `S+T0=1.997` are fixed. The radial sums governing the two distribution ladders stay fixed, so the nominal omega/delta ladder values remain unchanged. The actual mesh, all radial masks, cap indices, Gram matrices, erased-coordinate integrals and optimized vectors are recomputed for each configuration. In particular, an invariant nominal ladder does not imply an invariant retained-row list or support-repair schedule.

The trial retains the published product weight g and the 77-dimensional polynomial span: eleven symmetric signatures, each multiplied by radial powers zero through six about 0.9. It changes neither k=39 nor the analytic structure of that finite span. The success criterion for this bounded search was a material increase of the fine-grid cap quotient toward one, followed by a separately valid support-repair calculation. The first criterion was not met.

### 2. Plateau geometry and a reduced parameter choice

Write `epsilon=10^-7/rho`, `A=S+epsilon/2` and `Cnu=Tnu+epsilon/2`. For a source with plateau height L, the core decomposition is

    phi_D(u) = min(3u/2, L),
    phi_E(u) = 3u - phi_D(u).

In the tested regime A>C1>C0, the active largest-tail conditions allow

    (3A-Cnu)/4 <= Lnu <= 3Cnu/5.

The additional 5/2 tail-reduction guard `Lnu >= 3A/7` also holds. The corresponding final-shell caps are

    outer cap = min(A-L0, A-L1),
    old inner cap = (C0+L0)/4,
    new inner cap = (C1+L1)/4.

The old/new inner regions must be nested. The original equal fraction `Lnu=.575*Cnu` is one option. Two other useful choices share the *height* of the plateau rather than its fraction:

    common_min: L0=L1=(3A-C0)/4,
    common_max: L0=L1=.6*C0.

Both preserve the required interval for each source and give nested inner caps automatically. Equal heights avoid spending extra outer-cap width merely because the new source has larger C1. This exact geometric simplification is valid even though the numerical search did not benefit from the tested endpoints.

Every rational radius, L, L/C, frontier slack, cap, and integer shell range at both meshes is saved in `geometry_checks.json`. `validate_geometry.py` verifies the fixed sums, both plateau frontiers and guards, and actual old/new/full mask nesting on all twenty configuration/grid pairs. These checks are necessary structural checks; the separate source-geometry audit supplies the remaining distribution and repair constraints.

### 3. Exceptional square constant must change with physical radius

The original exceptional-square statement uses radius at most 11/40 and the convenient bound K=17/50. It is incorrect to reuse that constant at r=.276 or .278 without a new calculation.

The independent exact rational computation in `../exceptional-radius/certify_exceptional_radius.py` repeats the original 1,024-bin, 21-term alternating-logarithm upper certificate. It reproduces the published baseline rational sum exactly and gives safe rounded-up constants:

| r | K used here | certified upper bound, approximately |
|---|---:|---:|
| .272 | .301405 | .301404153485181623 |
| .2742997 | .327323 | .327322538111366366 |
| .275 | .34 | .336133604027290568 |
| .276 | .349580 | .349579996894903756 |
| .278 | .380026 | .380025921565620058 |

The `.275` trial intentionally retains the still-valid conservative `.34`; the exact calculation would also allow `.336134`. The original-geometry baseline likewise retains `.34` to check agreement with Round 4.

Both matrix and direct evaluation use the changed K in the signed hybrid:

    m=.99998, lambda=.008,
    a=m*m-m*lambda,
    b=(1-m/lambda)*(1-m)*K,
    Jcap=Jbase+(a+b)*Jplus+b*Jtail.

Thus higher-radius trials do not inherit an unjustified exceptional constant. Reducing K at the original radius improves the coarse optimized cap value by only about 0.6183 ppm. This calculation concerns the cap form; it is not a new fully certified prime-gap margin.

### 4. Bounded numerical results

All entries below are the direct scalar reevaluation of the optimized 77-vector. The independent matrix value, vector, conditioning, residuals, and three whitening-cutoff results are retained in each JSON file. Corresponding NPZ files hold the full Gram matrix, numerator matrix and original coefficient vector.

| tag | physical r | plateau | K | grid | rho_star Jcap/I |
|---|---:|---|---:|---:|---:|
| baseline | .2742997 | original | .34 | 16384 | 0.993379352892581 |
| r272_min | .272 | common_min | .301405 | 16384 | 0.992837127339583 |
| r272_original | .272 | original | .301405 | 16384 | 0.992825152057240 |
| r274_max | .2742997 | common_max | .327323 | 16384 | 0.993356576365699 |
| r274_original | .2742997 | original | .327323 | 16384 | 0.993379971225379 |
| r275_max | .275 | common_max | .34 | 16384 | 0.993324871060043 |
| r276_max | .276 | common_max | .349580 | 16384 | 0.993147338997495 |
| r276_min | .276 | common_min | .349580 | 16384 | 0.993160475207861 |
| r278_max | .278 | common_max | .380026 | 16384 | 0.992272698494233 |
| r278_min | .278 | common_min | .380026 | 16384 | 0.992274861882488 |
| r274_max | .2742997 | common_max | .327323 | 98304 | 0.994373401622446 |
| r275_max | .275 | common_max | .34 | 98304 | 0.994350189103926 |

The original-geometry coarse matrix value agrees bit for bit with the unchanged Round 4 program. Against that coarse control, the other tested radii all lose: approximately 542 ppm at .272, 54 ppm at .275, 219 ppm at .276, and 1,104 ppm at .278, using the better of the tested plateau choices at each radius.

The two most competitive nearby alternatives were refined. At the fine grid, original radius/common_max loses 22.9977 ppm relative to the Round 4 optimized original geometry; .275/common_max loses 46.2103 ppm. The ordering agrees with the coarse evidence. The search stopped at these ten configurations and two refinements. There is no extrapolation from these values to every plateau height, every radius, every product weight, or every finite family.

### 5. Numerical audit and its limits

The engine uses a positive exponential tilt of 20 in convolution weights and restores the exact balancing factors. This avoids evaluating the tiny un-tilted convolution left tail by cancellation. It is the same independent cap engine developed and checked in Round 4. `numpy.longdouble` on this host is actually 64 bits; no extra precision or outward enclosure is claimed.

Across all twelve computations:

- all 77 dimensions were retained at the smallest tested scaled-Gram cutoff;
- the maximum full scaled-Gram condition number was about 4.307e10;
- matrix versus direct candidate quotient disagreement was at most 2.884e-10;
- full scaled-pencil relative residual was at most 5.30e-16;
- the summed recorded compute time was 175.3 seconds on this host, excluding orchestration.

These checks give meaningful numerical evidence at the tens-of-ppm scale at issue, but they are not interval-arithmetic error bounds. The generalized eigenvalue is an observed numerical optimum of the assembled finite matrix. We do not label it a certified upper bound or a no-go theorem. Direct reevaluation uses a different contraction order but shares the cap model and one-dimensional moment primitives; it does not independently prove that model.

### 6. Support and source obligations discovered during this search

The following are substantive constraints, not bookkeeping details.

1. **The inner-square auxiliary source must be updated at smaller r.** At r=.272, the published omega=.0031 gives a level smaller than twice the new physical inner radius. The separate exact source audit supplies a common replacement `omega_s=.0035`, `delta_s=.025`, which passes the tested source and row-12 containment inequalities. Those source facts do not by themselves evaluate the cap's support losses.

2. **A new retained row can violate the original low-witness mesh guard.** At the fine grid, r=.272,.275,.276,.278 can retain new-ladder row 39. Its activation coordinate is about 1.886625e-5, which is less than two mesh cells for these cases. The original low-witness implementation requires at least two cells. The source theorem does not fail, but the original support-repair engine cannot be inherited unchanged.

3. **An explicit inward restriction can remove that extra row.** With `h=S/98304`, `J1=floor(T1/h)`, define

       Jo=min(98303, floor(B_new39/h)-J1).

   Restrict the outer sum of coordinate indices to `r_total <= Jo-k`. In the affected tested cases Jo=98302, one layer less than the ordinary Jo=98303; this restores the retained range 0 through 38. Keep h, nominal S, convolution length and Z fixed, but recompute every face from the trimmed F. The current reported trials are **not trimmed**. No numerical loss estimate for that modification is included here.

4. **Every schedule still needs rebuilding.** Even after trimming, actual integer thresholds, caps, source-specific masks, failure forms and outward quadrature bounds must be regenerated. The approximately 1.5 ppm alpha rectangle proved for the fixed published k40 profile cannot simply be transferred to these optimized k39 vectors or these radii.

Since none of the screened geometry changes gave a promising cap value, a full repaired certificate for these particular vectors is postponed. This is a prioritization decision based on the observed finite trials, not a proof that repair or a different profile cannot succeed.

### 7. Reproducibility and archive contents

Run from this directory:

```sh
OPENBLAS_NUM_THREADS=1 python3 validate_geometry.py
OPENBLAS_NUM_THREADS=1 python3 run_bounded_screen.py
OPENBLAS_NUM_THREADS=1 python3 run_bounded_screen.py --refine
```

Dependencies are recorded in `manifest.json`: Python, NumPy and SciPy, platform, actual long-double bit count, and SHA256 of all computation inputs and outputs. The parser's only upstream file dependency is

    ../../research-round1/prime186-work/PrimeGaps186/prime_gap_186_certificate.py

relative to this directory. That file provides the literal published coefficient signatures and integer coefficient matrix. An exported archive must preserve this relative layout or set `SOURCE` to the pinned copy. The two distribution-ladder recurrences and geometry are independently implemented in `cap_trial.py`; no FLINT module is imported and no official regression guard is disabled. The preserved upstream clone remained clean after all computations.

Files are intentionally small-purpose: `cap_trial.py` evaluates a vector; `optimize_cap.py` builds and solves the finite pencil; `validate_geometry.py` checks exact parameters and actual masks; `run_bounded_screen.py` replays the declared finite list. Ten `*.config.json` files contain every parameter choice. Each computed point has JSON evidence and a compressed NPZ matrix archive. `summary.json` is the compact comparison surface.

### 8. Conclusion for the next research step

The tested radius/plateau degrees of freedom do not erase the k39 cap deficit. The useful output is a fully recomputed negative trial, a simpler common-height plateau parameterization, a valid radius-dependent exceptional constant, and an explicit identification of the new mesh obstruction. A more serious search should change a mathematically justified larger component, such as the product profile or support geometry, or derive a certified finite-family upper bound before expending effort on full support restoration. Arbitrary radius scans and inherited k40 constants are not justified by these results.

