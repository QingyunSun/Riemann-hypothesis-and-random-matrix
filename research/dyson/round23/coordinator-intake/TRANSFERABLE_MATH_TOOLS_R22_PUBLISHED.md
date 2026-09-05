# 给 GPT-6 Astra：从 FLT 形式化与 prime gaps 186 提取的数学构造

## 任务与当前状态

用户要求认真研究三个链接中的数学思路，将真正可迁移的工具交给 Astra 主研究者，用于黎曼猜想、随机矩阵和零点间距方向的重要猜想。两个短链接分别是同一个 186 项目的论文与研究过程摘录；另一项是 FLT 形式化。

本文件区分：**原材料中的构造线索、下面直接推导的通用引理、尚待检验的本项目应用**。应用建议不代表已解决算术困难。没有在本次阅读中重跑两项工作的完整证明或证书。

研究负责人是 Codex 任务《整理数学研究进展与攻关方向》，任务 ID `01a0700a-2344-7691-9f09-a014e148d091`，模型 GPT-6 Astra。共享仓库为 [Riemann-hypothesis-and-random-matrix](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix)，本地根目录：

`/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research`

**最新检查点：2026-09-05，协调任务已完成第二十二轮所提交主要证明的普通审查；这不等同于外部审稿或 Lean 验证。** 当前已核实的最新公开版本为[第二十二轮提交 1c1335d74807dc1588077a9ac94c88f5aa02a54c](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/1c1335d74807dc1588077a9ac94c88f5aa02a54c/research/reports/dyson_round22.md)。公开报告已全文核对；55 份公开原始文件已从该固定提交独立下载，与清单及本地冻结稿逐字节一致；全部 58 份本地原始文件也通过清单核验。第二十二轮发布时，协调者对 Euclid 主 singleton 稿的审查确实仍待补；该项随后完成并单独记录，不回写当时的发布历史。此前第二十、二十一轮公开文件核验仍保留。当前准确目标已只含奇数端点、正偶数位移和中心常数 2；其严格双素数相关性上界仍未证明。

**第二轮原始材料精读已单独交付：**[186 与 FLT 的具体工具及接入任务](ASTRA_186_FLT_SECOND_READING_TOOLS.md)。Astra 已确认全文读取并冻结原文，选用真实模数/系数映射与零边缘构造。该文件把所需严格目标与更强充分基准区分，并给出正测度标记代数和 Godement 维数界的实际适用条件。Fable 的单一现有手动会话限制不变。

此前固定 ℓ≥1、H=f(v)+g(v)S₂ 的算术传递已获内部普通证明审查；这不是外部审稿或 Lean 验证。固定 ℓ=16/15 有理候选的归一化 margin 约为 −0.014662375473369，未越过半间距屏障；有限完整系数算子的负数值结果不能单独证明所有尺度上的障碍。该固定候选的重复验证已停止。

**保留已有 Fable 工作：仅一个现有 Claude Code 会话，用户手动粘贴任务；一次一个任务。不启动新的 Fable 会话、Claude 子代理、额外付费 API 或自动调用循环。已完成的固定候选审计保持关闭；本文件不触发新的 Fable 任务。**

## 原始材料与阅读定位

- [186 论文](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf)：互补支撑见 Proposition 2.3；算术实现见 §3.3；负部分控制见 Proposition 3.11；残差回收见 Theorem 4.5；支撑恢复见 Proposition 4.6。论文首页明确：其 Lean 部分仍以特定数值界和有限域指数和界为假设，另提供数值验证程序。
- [186 研究过程摘录](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps_abridged_cot.pdf)：印刷页 3–4 的算子方向与对偶界，页 28–34 的测度、截断与证书纠错。它展示探索和修正，具体结论应回到成稿或证书检查。
- [Anthropic FLT 介绍](https://www.anthropic.com/research/formalizing-fermats-last-theorem)、[17 页过程摘录](https://www-cdn.anthropic.com/9e431dff043da6538d99d6c2d231b670aa3da263.pdf)：页 4 的 Milnor patching，页 5 的 Godement 维数论证。过程摘录明确未逐条独立验证其中的数学断言。
- [FLT 实际证明范围](https://github.com/anthropics/fermats-last-theorem/blob/main/PROOF-PATH.md)：必须核对具体定义和假设；带有 Mazur、Langlands–Tunnell、Ribet 名字的步骤是此证明需要的特定版本。

## 1. 把不可直接使用的相关性变成带误差预算的正能量

**来源线索：**186 论文通过分别处理两个非负权重，利用带符号 minorant 的混合相关性回收残差能量，而没有把带符号权重当成正测度。

下面是为本项目重新写出的通用引理，可独立验证。设 μ、ν 为正测度，σ=μ−ν；R、C 在所需空间平方可积。已知

\[
|\langle R,C\rangle_\sigma-\widehat m|\le\epsilon,
\quad \|R\|_\nu^2\le E,
\quad \|C\|_\nu^2\le G_\nu,
\quad \|C\|_\mu^2\le G_\mu,\quad G_\mu>0.
\]

则

\[
\boxed{\|R\|_\mu^2\ge
\frac{\bigl(|\widehat m|-\epsilon-\sqrt{EG_\nu}\bigr)_+^2}{G_\mu}.}
\]

证明：相关性满足 mσ=mμ−mν，故 |mμ|≥|m̂|−ε−|mν|；在 ν 上用 Cauchy–Schwarz 控制 |mν|，再在 μ 上使用一次 Cauchy–Schwarz。负的下界先取正部，再平方。

**给 Astra 的具体任务：**从当前显式公式或算术二次型中，找出一个能获得更大合法支撑的混合相关性，并明确列出 μ、ν、R、C、m̂、ε、E、Gν、Gμ 的实际定义。目标是证明这项净增益覆盖当前候选的完整 deficit。不能直接沿用旧候选的 deficit 或只比较相关性的主项。

第一份产物只需是一页完整不等式及每个量的来源。若没有可控的正测度分解，或 ν 的加权能量已吞掉全部收益，应写出具体失败不等式并转向。此前 Gaussian 长支撑的 pole correction 反例没有被这个抽象引理消除。

## 2. 对实际组合对象分配支撑预算

**来源线索：**186 论文 Proposition 2.3 用互补条件控制真实的 lcm(D,E)，允许随素数尺度变化的分配 f(t)g(t)=t³；并保留对子因子的封闭性。

可迁移的设计方法是：先写实际相关性产生的对象 Q(D,E)，再从可用定理的假设倒推 D、E 应分担的约束。不要先独立削小两个支撑，再希望乘起来仍有足够空间。

一个抽象的工程化表示是：在尺度 u 上需要支付总预算 c(u)，选择

\[
\alpha(u)+\beta(u)=c(u),
\]

分别约束两侧的尾部。α、β 可随尺度变化；每个候选必须同时满足组合对象的真实约束、空尾部情形和必要的单调性。只有这些条件推出所需算术估计，支撑扩大才有效。

**给 Astra 的具体任务：**选定一项目前限制最大的混合项，写出其整数指标关系、截断和极限顺序；给出旧支撑集合与一个严格更大的候选集合。证明新集合的每一点落入哪条现成估计，或精确指出必须新证明的估计。随后用固定候选比较“主项增加 − 新增误差”，再决定是否优化。

必须明确区分素数等差数列中的模数估计与本项目的乘法相关性。前者的分布指数不能直接作为 ζ 零点问题的支撑许可。也不能用 smoothness 与 dense divisibility 的名称替代假设核对。

## 3. 用算子生成方向；同时寻找覆盖整个函数空间的上界

**来源线索：**186 过程记录用算子残差诊断多项式空间之外的收益，也讨论通过加权 Cauchy–Schwarz 构造统一上界。下面针对我们可能非正定的算子重新推导。

### 3.1 两维 Ritz 检查：适用于自伴算子

在真实 Hilbert 内积下，设 u 为单位向量，K 自伴且以下表达式有定义。令

\[
\lambda=\langle u,Ku\rangle,\quad
r=Ku-\lambda u,\quad s=\|r\|.
\]

若 s>0，取 v=r/s、b=⟨v,Kv⟩。在 span(u,v) 上的压缩矩阵是

\[
\begin{pmatrix}\lambda&s\\s&b\end{pmatrix},
\quad
\lambda_+=\frac{\lambda+b+\sqrt{(\lambda-b)^2+4s^2}}2.
\]

因此整个空间的 Rayleigh 上确界至少为 λ₊。这是明确的两维可达值，不是从度数序列外推。若 u 是旧试验空间中的精确 Ritz 向量，r 才进一步正交于整个旧空间；任意 u 只保证 r⊥u。

本项目的有限算子是

\[
K_L=A_L^*A_L+\tfrac12\{A_L^2+(A_L^*)^2\},
\qquad
J_L(x)=\frac{\langle x,K_Lx\rangle}{2\pi^2\|x\|^2}-\frac14.
\]

跨过 J=0 要求 Rayleigh quotient >π²/2。K 自伴不代表 K 半正定；不能未经证明套用只对正算子有效的矩比公式。若使用非正交基，须保留 Gram 内积，不能把系数向量的 Euclidean norm 当函数范数。

**具体任务：**在真实算子上计算 λ、s、b，报告两维新增收益、数值误差，以及新方向是否仍在已证明算术传递的类中。先用现有规模，只有结果揭示新信息才扩大。若转为固定有理向量，直接验证二次型差值。不要把旧空间中投影过的 Ku 当成完整 Ku。

### 3.2 用正超解构造上界证书

对有限实对称、逐项非负的 K，若存在 w_i>0 满足

\[
(Kw)_i\le M w_i\quad\text{对所有 }i,
\]

则对任意 x，|xᵀKx|≤M‖x‖²。证明可逐项应用

\[
2|x_ix_j|\le (w_j/w_i)|x_i|^2+(w_i/w_j)|x_j|^2
\]

并求和。这不要求 K 半正定。

**具体任务：**在当前参数确实使 A_L 逐项非负时，利用 K_L 的非负性寻找 w。可先试

\[
w_n=\frac{d_\ell(n)}{\sqrt n}\exp(q(\log n/\log L)),
\]

其中 q 为低阶实函数；这只是建议的正超解族。计算每个行比 (K_Lw)_n/w_n，定位真正的极端区域，再尝试从素数幂和推导对所有 n、所有足够大 L 的统一界。

若 M≤π²/2 且完整证明覆盖目标算子族，就能排除这一特定机制中的所有试验向量。有限 L 的证书只约束该 L；不能拿一串有限矩阵的最大值冒充统一界。超解族未找到也不说明上界不存在。

**用途：**尽快判断该继续构造新方向，还是必须改变算术信息或支撑。这个障碍结论是研究决策依据；本项目最终目标仍是重要猜想的正面进展。

## 4. 将“截断误差”改写成真正的跨区域泄漏

**来源线索：**186 过程记录页 29 明确撤回过一个把算子范数误当截断误差界的步骤。

取正交投影 P，Q=I−P。对于有界算子 T，正确恒等式是

\[
QTf=QTPf+QTQf,
\]

因此

\[
\|QTf\|\le\|QTP\|\,\|Pf\|+\|T\|\,\|Qf\|.
\]

一般不能丢掉第一项。直接反例：

\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
T=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad f=(1,0)^T.
\]

此时 ‖Qf‖=0，但 ‖QTf‖=1。

**具体任务：**审查当前支撑投影、热流窗口、频率截断中所有类似估计。对真正使用的 P、T，给出 QTP 的核、交换子界或跨区正积分。二维反例可作为误用回归测试；实际数学产物必须是本项目的泄漏界。若无有效界，原先的截断增益暂不计入证书。

## 5. 将固定试验的算术传递升级为共同的有限 Gram 传递

**来源线索：**186 论文 §3.3 从算术和建立碎片测度；过程记录强调固定分带后先取算术极限，再细化，以及共同测度和重合素因子的处理。

主任务刚完成固定 ℓ、H=f+gS₂ 的传递，应该复用而不是重证。下一项自然问题是：对选定的有限个新增方向 h₁,…,h_d，能否获得同一算术模型下的全部混合型极限？

对 Hermitian 型，可以由极化公式恢复交叉项。若 q(x)=B(x,x)，内积约定对第一变量共轭线性，则

\[
B(x,y)=\tfrac14\{q(x+y)-q(x-y)-i q(x+iy)+i q(x-iy)\}.
\]

实对称情形只需前两项。必须保证定理适用于这些和；对于固定 d，有限多个已证明极限可共同成立。d 随高度增长需要另行给出统一性。

**具体任务：**优先为第 3 项确实有收益的一个新方向建立混合型传递。给出 Gram 矩阵每一项的共同来源，保留同一整数模型产生的素因子重合和混合项。不要分别设计看似有利的 PSD 矩阵条目，再假定它们能由同一组算术系数实现。

若只是换基或重复当前闭包内的方向，记录等价性后停止；它没有增加新的算术信息。

## 6. 在正测度或平方层面认证，保留抵消

**来源线索：**186 过程记录后段显示，网格、支撑、正测度及损失项必须一致；零次观察到稀有坏事件不能代替其贡献上界。

这里给出一个可单独复用的 Gram 误差引理。设 h=(h₁,…,h_d)，

\[
G_\mu=\int h h^*\,d\mu.
\]

若 0≤ε<1 且在同一支撑上，以测度意义有

\[
(1-\epsilon)\mu\le\widetilde\mu\le(1+\epsilon)\mu,
\]

则

\[
(1-\epsilon)G_\mu\preceq G_{\widetilde\mu}\preceq(1+\epsilon)G_\mu.
\]

证明只需对任意 c 积分 |c*h|²。该形式可以整体保留带符号系数中的抵消。仅有总质量接近、节点值接近或 Monte Carlo 拟合，不满足这个假设；支撑变化与函数近似误差须另计。

**具体任务：**仅当出现接近或超过门槛的新候选时，冻结其有理系数，统一主项、分母和损失的物理测度与支撑，认证最终二次型差值。对坏事件列出覆盖证明和正的加权上界。重叠可导致保守上界，遗漏会使证书失效。

现在的负 margin 不需要靠更多精度反复认证；优先解决缺少的数学收益。

## 7. FLT 中值得保留的构造，及它们的实际适用范围

### 7.1 从点值控制直接得到维数界

Godement 型论证的可复用核心如下。设 V 是 L²(D) 的线性子空间，D 有有限测度，存在共同的点值代表和统一常数 C，使几乎处处

\[
|v(x)|\le C\|v\|_{L^2(D)}\quad(v\in V).
\]

对任意有限正交归一组 e₁,…,e_N，在每个 x 上对其线性组合取上确界，得 Σ|e_j(x)|²≤C²；积分后 N≤C²μ(D)。因此 dim V≤C²μ(D)，无需先建立一个更强的紧算子理论。

**对本项目：**只有在某个实际需要控制的观测子空间满足这个点值估计时，才用来控制维数或有限秩近似。全空间范数估计不能未经证明换成 D 上的局部范数；也不能由此推出零点统计或谱间隔。

### 7.2 Milnor patching：把拼接变成兼容数据

对于环纤维积 A×_C B，在适当满射假设下，可逆模可通过两侧的可逆模及其在 C 上的同构来拼接。它值得保留为遇到真实局部—整体问题时的标准工具。

**目前判断：**现有零点相关性路线中，尚未识别需要这种环纤维积的对象。先不投入抽象化工作。若使用，必须明确 A、B、C、满射和待拼接对象，不能把一般“协作”或“局部信息”比喻成 patching。

这两项都是已有数学工具的有效选用；此次 FLT 工作的新增贡献重点是形式化验证。对于我们，最实用的附加纪律是：每个关键节点先固定准确命题和定义，检查它足以推出最终目标，再投入证明。检验的是完整依赖闭包和最终声明，不能把任务看板上的完成状态当成证明。

## 给 Astra 的执行顺序与交付标准

1. **先做一次能改变研究决策的检查：**利用当前算子工作的积累，选择两维残差检验或正超解上界中成本较低的一项。报告候选是否值得继续扩展；不无限增加基或扫描 L。
2. **主攻收益来源：**围绕更大合法支撑，尝试第 1 项的净残差回收。先证明算术适用条件，再优化数字。目标是穿过核心门槛。
3. **发现新方向后补齐实现：**用第 5 项建立其共同算术传递，审查第 4 项的跨区泄漏，最后按第 6 项给出严格证书。
4. 每项产物写出：准确命题、当前假设、指向最终猜想的作用、证明或失败位置、可重复计算、净 margin 和下一决策。小引理只有用于这条主链时继续投入。

代码优先复用 `research/residual-gram/` 下现有 Python 与证书工具；若改实现，用隔离分支、窄 diff 和结构测试。没有性能瓶颈证据时不引入 Rust、框架或新的调度系统。

**暂缓：**全面 FLT 库迁移、全项目 Lean 化、没有收益诊断的高阶特征枚举、更大规模重复负结果、多个 Fable 会话。若本机制有严格障碍，明确切换需要新算术信息的路线；不把障碍定理包装成用户要求的重要猜想已经完成。

来源在各节与上方索引中给出。本文的抽象引理和应用任务是本次阅读后的推导与建议，不是宣称原作者已经给出了 RH 或随机矩阵问题上的这些结论。

## 首项执行反馈：有限算子的两维 Ritz 诊断

主任务已确认阅读本文件，并回报固定有理试验在 L=100000 上的计算：

| 量 | 回报数值 |
| --- | ---: |
| λ=⟨u,Ku⟩ | 4.192011775686907 |
| s=‖Ku−λu‖ | 0.17752123988758 |
| b=⟨v,Kv⟩ | 0.93354964158306 |
| 两维 Ritz 最大值 | 4.20165460874395 |
| 原 margin | −0.0376302025223922 |
| 新 margin | −0.0371416908928897 |
| margin 增加 | 0.0004885116295025 |

协调任务已用回报的 λ、s、b 独立重算两维公式和归一化，数值吻合。完整 K 的直接复核、脚本和 JSON 由主任务报告完成；协调任务没有重跑该整数算子。该结果属于有限数值诊断，不是严格区间证书，也不是算术极限定理。

**关键范围：**这里是 L=100000 的有限 margin，不能与本文开头约 −0.0146624 的连续极限 margin 混为同一个数值。Ku 新方向包含素因子移除和截断求和，不自动属于已经证明传递的固定 H=f+gS₂ 类。

**已执行的研究决策：**停止扩大旧负值扫描；主任务已写出 shifted Gaussian off-diagonal kernel E_T(U,V)，列出互补支撑需要新证明的算术估计。写出待证估计不等于已证明该估计；中心极点障碍和 signed residual 的全部误差仍须保留。

主任务报告保存位置为共享仓库的 `research/reports/transferable_tools_ritz_decision.md`，并有配套脚本与 JSON。下一次有价值的反馈应是更大支撑所需估计的证明、可验证反例或明确障碍，而不是重复上述有限数值。

## 后续执行反馈：正项回收已形成证书，目标缺口仍须单独衡量

主任务已在[公开提交 e3f5490](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/commit/e3f549000a94128d380d474e3b7f5744a2ddb09f)保存一个已知失败矩形上的正项回收证书及复核记录。利用论文已公布的基准端点，新增 credit 严格超过 1.5058119471 ppm；同一 k=40 试验的保证余量从约 23.360452297 ppm 提高到 24.866264244 ppm，素数间距结论仍为 186。

另一方面，当前 77 维空间内的 k=39 cap-only 数值优化约为 0.994396399364491，仍缺约 5603.60 ppm。这个有限空间的浮点结果不构成整个方法的严格上界。上述回收证书验证了工具能够产生真实收益，却尚未提供待攻目标所需的量级。

由此形成一条具体的研究决策规则：把每项净收益与**待攻目标自己的缺口**比较，同时更新参数变化引起的常数和支撑条件。已有目标的余量不能替代新目标的缺口；局部证书成功之后，仍须判断应扩大试验空间、改变合法支撑，还是寻找新的算术输入。

## 后续执行反馈：投影残差产生空间外方向，但必须保留真实交叉项

这是第 3 项工具在 k=39 筛函数空间上的新应用，与前述有限 ζ 算子 K_L 的试验不同。Astra 将完整筛算子产生的残差投影到“任意径向函数 × 现有乘积权重”的空间，再剔除旧 77 维部分，使计算能用一维卷积实现。

### 可单独复用的投影公式

设 T 在真实质量内积下自伴，f 是旧空间 U 中的单位向量；P_U、P_V 为两个正交投影，Q=I−P_U。不要求 U、V 嵌套或两个投影交换；若 T 无界，还要求下文涉及的算子作用均有定义。令

\[
h=P_VQTf,\qquad w=Qh.
\]

则 w⊥U，且

\[
\langle f,Tw\rangle=\|h\|^2,
\qquad \|w\|^2=\|h\|^2-\|P_Uh\|^2.
\]

第一式依次使用 T 的自伴性、Q 的自伴性和 P_V 的正交投影性质。若 w≠0，则在 f、w/‖w‖ 上的二维压缩矩阵，其交叉项是

\[
\beta=\frac{\|h\|^2}{\|w\|},
\]

**不能自动替换为 ‖w‖**：Q P_V Q 通常不是正交投影。若直接选其他方向，应直接计算真实混合积分，再使用一般二维 Ritz 公式。

最小反例：取 U=span(e₁)、V=span(e₁+e₂)、f=e₁，T 交换 e₁、e₂。此时 h=(1/2,1/2)、w=(0,1/2)，故 ‖w‖=1/2，而 β=1。这个例子检验投影公式；实际应用仍须使用完整质量内积与支撑。

### 本轮数值状态

结果已固定在[第六轮公开报告与证据](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/e890ce54dd9af66fa210114c4cb0677c160a6f04/research/reports/prime186_round6.md)。协调任务已阅读公开报告并独立重算二维公式及 ppm 差值，尚未自行重跑完整积分。主研究任务另在隔离副本中重放细网格计算，保存了逐项吻合的记录。

| 量 | 回报数值 |
| --- | ---: |
| 二维矩阵 a | 0.9943963991909279 |
| 二维矩阵 b | 0.043583189070450945 |
| 正确交叉项 β | 0.008217784708256407 |
| 二维最大值 | 0.9944674193880856 |
| 二维增益 | 71.0201971577 ppm |
| 旧 77 维直接计算值 | 0.994396399364491 |
| 加入新方向后 78 维重新优化的直接值 | 0.9944678209006830 |
| 78 维增益 | 71.4215361920 ppm |
| 78 维结果距离 1 的缺口 | 5532.1790993170 ppm |

这是 **cap-only 浮点诊断**，尚未恢复完整合法支撑，不能作为严格区间证书或新的素数间距定理。不同卷积归一化参数的矩阵值据报相差约 2×10⁻¹⁶；小密度截断变化引起约 0.0177 ppm 的变化。这些一致性检查不替代严格误差界。

报告另给出了方向独立性的精确证明：把冻结的 float64 径向剖面视为明确的二进制有理数。其前 13 个径向单元取值严格为零，而另一个单元的取值严格非零。固定其余 38 个坐标单元后，旧基函数除以共同的正乘积权重，沿剩余坐标至多是 12 次多项式，因此不可能等于该剖面。被选单元均具有正测度且满足精确支撑不等式，避免了仅在孤立点不同却在 L² 中相等的问题。独立审查直接解码数组验证了这一论证；另有模素数秩证据，但该审查未独立重做模秩计算。

**证书范围：**上述精确代数证明只证明新函数不在旧空间内，不给出它到旧空间的距离下界或严格 Rayleigh 增益。公开报告还保留了约 2.28×10¹⁰ 的缩放 Gram 条件数，以及未计算的完整残差范数、增益外包区间和真实支撑恢复。这些限制必须随候选一起传递。

新增方向填补了旧缺口的约 1.27%。实际结论是：算子生成方向能发现原有限试验空间遗漏的收益；本次收益仍不足以越过门槛。后续投入必须以新的收益来源、合法支撑或算术估计为依据，不从这一小步外推加维必然成功。

## 第七轮派生工具：用多个尺度消去未知参数

这项构造来自后续实际研究，已经写入[第七轮公开记录](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/e1dace3918412ac73f941a93b3018f85e748a3b1/research/reports/dyson_round7.md)。它不是声称三份原始材料直接给出了下面的 ζ 结论。

### 通用构造

若几个实际统计量组成的向量满足

\[
F_T=a+Bq_T+e_T,
\]

其中 q_T 是未知参数向量，选择 c 使 cᵀB=0，就得到

\[
c^TF_T=c^Ta+c^Te_T.
\]

不需要先证明 q_T 收敛。如果系数只在截断极限中趋向 B，还须证明系数误差乘以 ‖q_T‖ 趋零。应同时计算 c 对误差的放大，以及待区分模型在 cᵀF_T 上是否仍有非零差异。这里的线性代数很小，关键在于统计量具有共同、合法的算术来源。

### 本项目中的精确目标

AH-Pairs 的逐点配对密度公式在 RH 下保留一个有界但未必收敛的近对角参数 P₀(T)。Poisson 平滑宽度取 b/(4π) 时，在已证明的方差渐近公式中，该参数的贡献为 2(P₀(T)−1)/sinh(b)。组合 sinh(2)V(2)−sinh(1)V(1) 将其消去。具体来源、尾部与归一化证明见[完整两尺度归约](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/e1dace3918412ac73f941a93b3018f85e748a3b1/research/dyson/round7/poisson-resolvent/TWO_SCALE_ZETA_TARGET.md)。

对真实 ζ，定义

\[
I_T(c)=\int_0^T\left|\frac{\zeta'}{\zeta}
\left(\frac12+\frac c{\log T}+it\right)\right|^2dt,
\qquad
W_T=\frac{2[\sinh(2)I_T(1)-\sinh(1)I_T(1/2)]}{T\log^2T}.
\]

这里使用模平方已经过转换证明，不能在前面的 Poisson 密度公式中直接把实部平方换成模平方。

公开归约给出：在 **RH + 论文精确定义的 AH-Pairs** 下，W_T 趋于一个 C_AH，满足 0.06239<C_AH<0.06240；正弦核预测约为 0.08227144。因此，若能在 RH 下证明

\[
\boxed{\liminf_{T\to\infty}W_T\ge\frac1{16}},
\]

就足以排除这一 AH-Pairs。**所需算术下界尚未证明；这不是 RH 或完整 GUE 猜想的证明。**

协调任务另用有理数级数界独立认证了

\[
C_{\rm AH}=\frac{e^2}{4}-e+\frac32-\frac2e+\frac5{4e^2}<\frac1{16},
\]

间隔严格超过 0.00010758。完整有理端点保存在同目录的 `TWO_SCALE_THRESHOLD_CERTIFICATE.json`。该证书只认证模型常数与门槛之间的距离。

### 为什么仍须新的算术输入

两尺度组合的谱权重是

\[
K(u)=\sinh(2)e^{-2|u|}-\sinh(1)e^{-|u|}.
\]

它在 |u|=log(2cosh(1))≈1.126928 变号，此后为负。丢掉高频尾部不能给出所需下界。ACUE 满足已知低频关系和点过程的正性，却得到 C_AH<1/16，因而这些信息本身不足以完成证明。

另一个保留的实际算术目标使用支撑在 [6/5,7/5]、关于 13/10 对称且积分为 1 的非负光滑测试函数。其配对 Fourier 统计在 AH 下预测为 7/10，在正弦核下为 1；对应的中心化双素数协方差目标见[算术边界与完整素数核](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/e1dace3918412ac73f941a93b3018f85e748a3b1/research/dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md)。这条路线同样保留极点产生的连续均值，尚未证明所需协方差界。

下一步应攻这两个明确目标之一，指出新增算术信息如何控制余项；不能把可计算主项、模型差异或消参恒等式当成缺失的下界。

### 第八轮：缺失估计已写成实际算术余项

[第八轮公开证明与独立审核](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/f112310bac05bc0f3ed4d931ca716c970b0f8cb0/research/reports/dyson_round8.md)已经建立短素数投影分解。取 N=⌊T/log⁶T⌋，令

\[
s_c(t)=\tfrac12+c/\log T+it,\quad
H_c(t)=-\zeta'/\zeta(s_c(t)),\quad
R_c(t)=H_c(t)-\sum_{n\le N}\Lambda(n)n^{-s_c(t)}.
\]

在 RH 下，

\[
W_T=B+\mathcal E_T+o(1),\qquad
\mathcal E_T=\frac{2[\sinh(2)\|R_1\|_{L^2(0,T)}^2-
\sinh(1)\|R_{1/2}\|_{L^2(0,T)}^2]}{T\log^2T},
\]

其中 B=0.4560939793292317…，故充分目标为 liminf 𝓔_T≥1/16−B≈−0.3935939793292317。两个 R 来自同一个 ψ(x)−x 的收敛积分；它们不能被当成任意两个独立非负能量，也不能未经估计就假定这种共同来源足以推出目标。

**已完成：**分解、误差审查和常数认证。**未完成：**所需余项下界。后续优先寻找实际素数算术带来的平均抵消，保留极点、端点及交叉项的完整预算。

### 第九轮：互补支撑已接到一个真实算术分量

[第九轮报告及完整适用条件](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/0fa6504ee20ebced507dc1c98fd2418a235945fc/research/reports/dyson_round9.md)将 Λ=μ∗log 代入移位素数协方差。186 论文 Corollary 2.19 的参数可取 ω=3/250、δ=ε=1/1000，满足 240ω+80δ=2.96<3。由互补尾部条件得到三重稠密可除性后，一个特定的、去重后的平方自由模数集合可延伸到 X^0.523。

得到的是选定除数分量的逐移位误差 O_A(X log^(−A)X)。当自然平移长度 H=X/T 为 X 的正幂时，直接加总得到 H 倍损失，尚不足以达到所需的 X log X 波动尺度。未选中的 Möbius–log 分量、均值和中心化交叉项仍须处理；不能把局部分量当成整个协方差，也不能将它当作素数 minorant。

本轮另已定量移除素数幂尾部，并验证其在允许的慢增长阻尼尺度下仍可忽略。这清除了一个实际误差项，没有改善目标的极限常数。慢尺度审查也确认：可用误差允许选择足够慢的对角序列；真正未补上的，是 RH 下界中的下一阶修正，而非一概不可控的有限高度误差。

后续的[第十轮证明与独立审核](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/cf59c48c0480952470be8b5aca48e9920312ed6a/research/reports/dyson_round10.md)已经对明确的平滑窗口 V(h/H) 建立无条件界

\[
|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{HX(X+Q^2)}(\log X)^4,\qquad Q=X^{0.523}.
\]

构造先完成平移求和，合并相同的既约有理频率，保留 Ramanujan 主项，再用间距与平方范数估计。实际二变量 sinc 权重的分离也有统一导数界，未替换成另一个模型核。

忽略对数因子，误差相对逐平移累加节省 X 的 0.060333… 至 0.119857… 次幂；但其自身仍为 X 的 1.106333… 至 1.165857… 次幂，高于所需的 X log X。该界适用于特定平滑窗口，尚未覆盖完整尖锐窗口或全部协方差。它也尚未利用三重稠密可除性中的额外抵消，除用于选定模数集合之外。

下一项具体工作是控制 Möbius 除数系数与中心化素数指数和的联合配对，超越分别取平方范数后使用 Cauchy–Schwarz 的界；另一条仍是对数加权素数混合矩的严格修正。只改善对数因子不足以补上这里的幂次缺口。

### 第十一轮：局部均方界与局部取样结合

[第十一轮报告](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/fe52f8a7995b93b6e7a6610defda27955931ee65/research/reports/dyson_round11.md)对同一个平滑算术分量进一步证明，在 RH 下

\[
|\mathfrak D_{\mathcal Q}^{V}(X,T)|
\ll_{V,\chi}\sqrt{X(X+Q^2)}(\log X)^5
\ll X^{1.023}(\log X)^5.
\]

与上一轮相比消去了 √H，但新增 RH 假设。除以目标尺度 X log X 后仍为 O(X^0.023 log⁴X)，不趋零。完整尖锐窗口、其余除数分量和最终带符号协方差仍未被这个界覆盖。

**可迁移的方法是先保留局部能量，再做取样和 Cauchy–Schwarz。** 对间距至少为 δ 的取样点，取互不相交、长度与 δ 同阶的小区间，令它们的并为 U。微积分基本定理给出

\[
\sum_\beta |F(\beta)|^2
\ll \delta^{-1}\int_U|F|^2+\int_U|FF'|.
\]

若 F 在相关小弧上的均方界随弧宽 ρ 缩小，取样估计就能保留这个 ρ。这里移位权重集中在宽度约 1/H 的弧上；它的系数平方和中的 H，与素数局部能量中的 1/H 抵消。随后逐个二进频带求和，保留所有尾部。用整个圆上的能量界会丢掉这一收益；仅减少取样点数量也不足以得到同样结果。[完整应用与误差处理](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/fe52f8a7995b93b6e7a6610defda27955931ee65/research/dyson/round11/prime-frequency/CENTERED_SMALL_ARC_BOUND.md)保留了真实 sinc 核、整数均值、Ramanujan 均值及两次不同的素数幂误差。

算术输入是 [Bhowmik–Schlage-Puchta 的 Lemma 3](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/Goldbach4.2.10.pdf)：RH 下，有限和 Σ_(n≤x)(Λ(n)−1)e(βn) 在 [−1/y,1/y] 的均方为 O((x/y)log⁴x)。协调任务已读原文第 3 页及其端点处理。这只使用零频率附近的 RH 估计，没有暗中升级为 GRH。

本轮另证明，完整指定模数族的系数平方和至少为常数乘 H/log^348X，因而不能仅把该范数改成 O(HX^(−η)) 来获得任意固定 η>0 的幂次节省。该障碍不排除重新选择模数、改变权重或利用实际素数与系数之间的联合抵消；后者仍是主攻方向。

### 第十二轮：变换后必须重新检查定理假设

[第十二轮的具体检验](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c53c7cf151d111f9ddd78045017fe12329ac395e/research/reports/dyson_round12.md)没有改善实际素数误差界。它限定了三种直接尝试的有效范围：合法模数上存在足够拥挤的频率，现有局部能量条件不能支持正值取样的固定幂次改善；把相位吸收入短素数系数，可能违反原定理的 Siegel–Walfisz 条件；已知短区间上界仍不足以给出所需带符号的下一阶修正。这些结论都不排除实际联合算术抵消。

这里最值得传递的是两个检查。第一，系数乘以 e(amn/d) 后虽然模长不变，分布性质会变。[实际允许参数下的模 3 反例](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/c53c7cf151d111f9ddd78045017fe12329ac395e/research/dyson/round12/dispersion-transfer/DISPERSION_HYPOTHESIS_OBSTRUCTION.md)选合法 d、a=1 和 m，使 mn/d 在短素数区间内接近 n/3，产生 N/log N 量级的剩余类偏差。第二，将一个连贯的移位区间替换为各素数模数下像集的笛卡尔积，会丢失跨素数的相关性：本例原来只有 O(H) 个整体剩余类，乘积扩张却有约 d 个。原论文对有界局部类数的估计不能直接承担这个损失。

协调任务已核对原始 186 文本中的系数定义、分布条件及参数范围，也阅读了上述真实模数构造。下一步应保留 m、a、d、h 的联合依赖，分离小分母共振并估计带符号剩余类核；不能把这些受限反例扩张为目标猜想或所有联合估计的不可行性结论。

### 新协作材料的独立审查：只移植已核对的构造

旧 Claude 会话在提交 `89393d5da61a45561ed199330c5b836f47fcd629` 补交了提案和审查记录。协调任务读取固定版本后，将以下发现发给 Astra；原稿中的 `[P]` 标签不作为证明已通过审查的依据。

- **可保留的构造：**[CUE 背景提案](https://github.com/galpha-ai/Alpha-devbox/blob/89393d5da61a45561ed199330c5b836f47fcd629/research/riemann-rmt/overnight/fable/r1_cue_background.md)用 Cauchy–Binet 将相关函数写成行列式模平方和，再提出 Vandermonde 因子，以 Schur 多项式的非负系数得到全局聚簇上界。对由样本选出的最近点对，用所有近点对的加权计数控制选择偏差，是可复用的方法。其 Proposition 3.3 第二种情形却写反了不等号，现有证明不能认证常数 1054。利用最小圆周间距不超过 2π/N，可在该步骤用较保守的 4100 修复；下游常数须同步重查。
- **缩放与选择偏差：**[通用 β 提案](https://github.com/galpha-ai/Alpha-devbox/blob/89393d5da61a45561ed199330c5b836f47fcd629/research/riemann-rmt/overnight/fable/r1_cbe_background.md)的 BB-LD 少了 N^(βn(n−1)/2) 因子，连 β=2、n=2 的已知精确公式也不满足。其从均匀单点密度推出选定点对局部密度界的步骤也不成立：任意紧簇整体随机旋转后，单点密度仍均匀。相关概率结论不能据此接入证明。
- **从静态到时间窗口：**[修复后的 Theorem B](https://github.com/galpha-ai/Alpha-devbox/blob/89393d5da61a45561ed199330c5b836f47fcd629/research/riemann-rmt/overnight/fable/r1_theoremB_repair.md)保留每个间距的平方下界，再对固定的弧段求和，构造背景距离的收缩下界。这比假设所有根移动缓慢更具体；但其局部密度或弧段条件仍须在实际样本上证明。初始背景量有界不自动等于整个碰撞窗口有界，CUE 深度律仍有这一依赖。
- **周期化边界：**[Level B 提案](https://github.com/galpha-ai/Alpha-devbox/blob/89393d5da61a45561ed199330c5b836f47fcd629/research/riemann-rmt/overnight/fable/r1_levelB_barrier.md)把有限零点窗口接成圆时，会增加一个首尾间距。这个人为间距很小，并不说明真实连续零点间距很小；相关推论需要非首尾的间距见证或有效的边界定理。实际 ζ 热流中的非实根条件也不能省略。

这些审查用于选择和修复工具；主研究目标仍是实际算术余项的严格下界。模型结果和有限窗口转换不得替代该目标。

以上具体问题已由主研究任务复核并收入[固定版本的背景与边界审查](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/087a0e4a6c93bed4326625b8c61048586a99778e/fable/reviews/pr11-89393d5/BACKGROUND_AND_BOUNDARY_REVIEW.md)。另有[算术材料接收与重放记录](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/087a0e4a6c93bed4326625b8c61048586a99778e/fable/reviews/pr11-89393d5/INTAKE_REVIEW.md)：141 个原始文件独立保留，F1 的错误系数、反驳脚本的符号错误及混用 v 值的表格分别处理。新的 L=10⁷ 输出现已存在；其负裕量仍是有限诊断，不能据此推翻已独立审核的固定族渐近证明，也不构成新定理。

### 第十三至十四轮：保留共振主项，再寻找完整周期的抵消

[第十三轮](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/0e970090034c1950ce083969c305b4473ac8ef8a/research/reports/dyson_round13.md)在一个满足来源条件的固定区间双线性测试中，用普通 ζ 的 RH 提取零有理数附近的素数积分主项，误差为 O(X^0.923 log²X)。主项必须保留；这个测试的任意长因子系数也不能直接认作实际 ζ 分解的系数。正的受限共振子和很大，不意味着完整带符号式有同样下界。

下一步已落实为一个实际算术应用。令

\[
\Lambda_{\le U}(n)=\sum_{r\mid n,\ r\le U}\mu(r)\log(n/r),\qquad
\Lambda=\Lambda_{\le U}+\Lambda_{>U}.
\]

[第十四轮完整证明](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/smooth-long-factor/SMOOTH_LONG_FACTOR_REMOVAL.md)保留原始 sinc 核、两个对数权重和本原主项，无条件得到

\[
|\mathcal D^V_{\mathcal Q}[\Lambda_{\le U}]|
\ll_J HX(UQ/X)^J\log^2X,\quad Q=X^{0.523},\quad UQ\le X/2.
\]

对固定 0<η<0.477，取 U≤X^(0.477−η) 和固定 Jη>2/7，这部分就是 o(X log X)。常数可依赖 η，不允许据此令 η 任意随 X 趋零。

**通用构造：**先按短变量冻结参数，把实际光滑长变量沿完整剩余类做 Poisson 求和；零频恰好抵消本原平均，非零频通过统一导数界衰减。表面奇异的相位用积分表示消去小参数分母，再检查导数。判断条件落在一个真正光滑的独立变量上，不能只看若干变量乘积的长度。这里余项 Λ_{>U} 精确保留且仍未估计，其因子不一定平衡。这是经典方法的具体应用，尚未改善完整 ζ 协方差的目标下界。

### 选择出的极值对象：先构造可积的上界，再扩大计数集合

[完整 CUE 证明](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/cue-selected-background/SELECTED_CUE_BACKGROUND.md)对相邻间距 δᵢ 中点处的逆平方背景 Bᵢ 建立

\[
\mathbb E\sum_{\delta_i\le\varepsilon}B_i
\le N^6\varepsilon^3/18.
\]

工具由三步组成：精确 Gram 行列式分解保留短点对及第三点接近端点时的消失因子；在相邻点对上用端点背景控制中点背景；随后扩大到所有短点对，用相关函数积分。这个顺序使奇异权重可积。若先去掉相邻限制，中点附近的奇异性没有相应的行列式零点，积分会发散。

结合经典最小间距紧性和 Markov，可得所选最小点对的 B_N/N²=O_p(1)，无需杜撰选择后的条件密度。再接已审查的定量 Galilean 引理，得到有限标量热流的 8D_N/δ_min²−1=O_p(N^(−2/3))。这是近似误差的概率阶；没有证明极限分布的收敛速度，也没有向 ζ 零点迁移。协调任务已逐式阅读本轮两个证明；[独立复核](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba/research/dyson/round14/INDEPENDENT_ROOT_REVIEW.md)另保存了确定性引理的依赖检查。

### Fable 后续修复中可留下的两个计算工具

[2073028 版本的独立审查](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/220d7a4dbff2950b67337b86819d97720d208744/fable/reviews/pr11-2073028/CBETA_REPAIR_REVIEW.md)仅接受部分修复。一般 β 的三点密度上界仍需证明；有限 N 公式不能换成极限核，在接近零的量上不能从绝对误差推出一致相对误差。改为直接积分，可以保留正确缩放和有限 N 修正。

第一，**用被截断的能量控制算子，而非粒子数。** 在测度 du/u 的玻色 Fock 空间，令 E=dΓ(u)，限制 E≤1。若 B_g²=∫₀¹|g(u)|²du/u²<∞，加权 Cauchy–Schwarz 与扇区对称性给出

\[
\|a(g)\Psi\|^2\le B_g^2\langle\Psi,E\Psi\rangle.
\]

因此压缩后的产生、湮灭算子均有界，即使粒子数无界。对本例 g(u)=2sin(πu/2)，[完整证明](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/220d7a4dbff2950b67337b86819d97720d208744/fable/reviews/pr11-2073028/F3_MASS_CUTOFF_BOUND.md)也给出所有指定离散网格统一的有限上界。这个上界不够证明谱门槛；离散模型向连续算子的范数收敛、算术迁移均未因此解决。

第二，**计算前先找控制截断质量的无量纲参数。** 对四阶素数极点的有限截断，参数是 z=ε log P；其归一化主质量渐近为 1−e^(−z)(1+z+z²/2+z³/6)。P=exp(1/ε) 只对应 z=1，并未包含绝大部分质量。[截止范围证明](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/220d7a4dbff2950b67337b86819d97720d208744/fable/reviews/pr11-2073028/F1_REPAIR_AND_CUTOFF_REVIEW.md)说明该数值实验为何无力验证整个极点；原有解析推导已经足够，不应继续扩大素数扫描来重复确认。这里的渐近诊断也不能充当具体有限数据的误差证书。

这些补充已在 Astra 主任务形成公开证明和审查文件。下一项研究仍是实际算术余项的联合带符号估计；不新增 Fable 会话，不重做已经关闭的谱外推或固定族验证。

### 第十五轮：精确分解保留可用的系数性质

对实际 von Mangoldt 信号，先用 Vaughan 恒等式剥离可由光滑长变量处理的项，保留

\[
R_{A,B}=\mu_{>A}*\beta_B,\qquad
\beta_B(m)=\sum_{d\mid m,\ d>B}\Lambda(d).
\]

这里 Q=X^0.523，X=T^α，6/5≤α≤7/5，H=X/T；不是后面频率二测试的 α 范围。在原始光滑窗口、真实 sinc 核和两个中心项下，取 A,B≥1、B<X、ABQ≤X/2 和固定整数 J≥2，已审查的差额为

\[
\mathcal D[\Lambda]-\mathcal D[R_{A,B}]
=O_J\!\left(HX(ABQ/X)^J\log^2X\right).
\]

通用做法是让恒等式同时保留三件事：可估计的光滑部分、剩余系数的精确定义、下一条定理要求的分布性质。本例在固定 b₀>0、C>0，X^b₀≤B≤2M、M≤X^C 的区间尺度下，未加相位的 β_B 具有所需的 Siegel–Walfisz 性质；乘上依赖其他变量的振荡因子后必须重查。R_{A,B} 带符号，而且仍有不平衡的因子区间；不能把它叫作正的素数尾部，也不能把一个平衡区间的分布估计扩展成整个余项界。[完整分解及范围](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/ccf65601c94150e65b74ef63f1084683cb4aa3f4/research/dyson/round15/signed-arithmetic/VAUGHAN_SIGNED_REMAINDER.md)。

### 第十六轮：把模型的饱和等号改写成非负相位缺口

这是一个更直接的反例检测构造。令 μ_T 为实际零点的正的加权配对测度，F_T 为其 Fourier 变换；选固定、非负、光滑的自相关函数 ψ，满足支撑在 [−1,1]、ψ(0)=1、ψ̂≥0。对固定 0<ε<1，定义

\[
C_{\varepsilon,T}(b)=\int\psi((\alpha-b)/\varepsilon)F_T(\alpha)\,d\alpha,
\]

**不乘 1/ε。** 在采用 e^(2πiαu) 的 Fourier 约定下，精确缺口为

\[
D_{\varepsilon,T}=C_{\varepsilon,T}(0)-C_{\varepsilon,T}(2)
=\varepsilon\int\widehat\psi(\varepsilon u)
\bigl(1-\cos(4\pi u)\bigr)\,d\mu_T(u)\ge0.
\]

半整数格点恰好使相位因子为零。RH 下，已知低频定理给出 C(0)→1+ε²m₁，其中 m₁=∫|v|ψ(v)dv；精确 AH-Pairs 假说进一步迫使 D→0，无需先假设近对角参数有极限。因此，对一个固定 ε 证明 **limsup D>0 已足够排除 AH-Pairs**。liminf D>0 或 limsup C(2)<1 都是额外加强，不应成为必需门槛。

可迁移的原则是：找出候选结构使哪个正性不等式达到等号，把等号缺口写成非负积分，再寻找足够的质量偏离等号集合。少数例外点对通常不够；需要归一化后仍可检测的质量。ε 固定在 T→∞ 之前，不能暗中改用收缩窗口。[完整目标、尾部和原始文献核对](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/1be9a652626028515723ee71b4faa20976fdd488/research/dyson/round16/bragg-atom/BRAGG_ATOM_TARGET.md)。这是一项尚未得到严格正下界的目标。

### 第十六至十七轮：按极点阶数设计非负且 Fourier 紧支撑的权

设 RH 成立，H(s)=−ζ′(s)/ζ(s)，1/2<σ<1，a=1−σ，W≥1。已完成的两个实例为

\[
w_1(t)=\frac{t^2+a^2}{W^2}\operatorname{sinc}^4(t/(2W)),\qquad
w_2(t)=\frac{(t^2+a^2)^2}{W^4}\operatorname{sinc}^6(t/(2W)).
\]

两者都在实轴非负、整解析并以 t^(−2) 衰减；在 ±ia 分别有一阶、二阶零点。取 B₄、B₆ 为相应个数的 [−1/2,1/2] 均匀密度卷积，b=a/W。这里改用角频率约定 ŵ(λ)=∫w(t)e^(−itλ)dt，则

\[
\widehat w_1(\lambda)=2\pi W[-B_4''+b^2B_4](W\lambda),
\quad\operatorname{supp}\widehat w_1\subset[-2/W,2/W],
\]

\[
\widehat w_2(\lambda)=2\pi W[(D_y^2-b^2)^2B_6](W\lambda),
\quad\operatorname{supp}\widehat w_2\subset[-3/W,3/W].
\]

构造顺序可复用：先匹配 Laurent 极点的阶数，再选择足够高的偶数 sinc 次数保持可积性；Fourier 端用样条导数给出精确支撑。权函数消掉 H 或 H² 在 s=1 的极点，随后移线到绝对收敛区域展开。结果分别是有限的 Λ 和 Λ*Λ 加权和，所有素数幂都保留。它们的连续极点密度也精确消失；二阶情形需要两个带指数倾斜的矩同时为零。

这里有一个可用的正能量结论。取载波 X=1、W≥3，由于 Λ*Λ 的首个非零系数在 n=4，而 Fourier 支撑只允许 n<e，得到

\[
\int H(\sigma+it)^2w_2(t)\,dt=0,
\qquad
\int|H(\sigma+it)|^2w_2(t)\,dt
=2\int(\Re H(\sigma+it))^2w_2(t)\,dt>0.
\]

这允许将实际 ζ 的模平方能量转成带完整 gamma 中心的零点 Poisson 和的平方。**它没有把正能量变成有限素数和。** 模平方移线产生反射零点极点 s=2σ−ρ；这些残数仍在。所得配对核也依赖两个零点的位置，尚未成为上面的频率二缺口。[线性实例](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/1be9a652626028515723ee71b4faa20976fdd488/research/dyson/round16/compact-packet/COMPACT_POLE_PACKET.md)、[二阶实例及全部残数](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/e2099bb15623c2293c15fdc85b49ce247d1d260c/research/dyson/round17/quadratic-packet/QUADRATIC_COMPACT_PACKET.md)。

两个迁移限制已由精确计算暴露。第一，时间权非负保证完整 Gram 矩阵半正定，不保证 Fourier 核逐项非负；这里核确实变号。第二，权依赖 σ，求导必须保留 ∂σw。二阶实例的两个导数积分恰为相反的非零量 ±16πa²h₆(−ia)/W⁴。对 W 求导时，sinc⁶ 只留下 O(1/|t|) 衰减，原有绝对控制不足；可以改设计更快衰减的权，但须重新证明相应恒等式。固定参数恒等式也不自动提供 σ→1/2 时的统一估计。

### 第十七轮：先检验目标波动尺度，再决定是否优化常数

对实际中心化素数信号 P_x，令 A_x(v) 为对数长度 1/T 的短区间加权 Λ 和，m_x(v) 为同一区间的连续均值。完整 Plancherel 恒等式为

\[
\int_{\mathbb R}|P_x(t)|^2\operatorname{sinc}^2(t/(2T))\,dt
=2\pi T^2\int_{\mathbb R}|A_x(v)-m_x(v)|^2\,dv.
\]

正的时间上界作用于整个中心化信号，不需要对振荡核逐项比大小。应用 [Yamada 的 Theorem 2，式 (13)](https://arxiv.org/pdf/2312.16090v1) 时保留其 u>0、h>1 范围和所有素数幂；若 x=T^α，得到局部上限 A≤(2α/(α−1)+o(1))m。α=2 时常数为 4，因为 Λ 权带来 log x，筛分母却是 log(x/T)。

即使完整保留 −2∫Am，利用 A²≤cAm 和一阶均值仍只给出均值平方尺度；目标需要均值乘 log T 的波动尺度。严格算出的 Bragg 上界在 α=2 为 O(T/log T)，比已有常数界弱。发散的是这个上界表达式，不能据此说实际统计量发散。[完整中心化推导和两端尾部](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/e2099bb15623c2293c15fdc85b49ce247d1d260c/research/dyson/round17/bragg-sieve/BRAGG_SHORT_INTERVAL_CAP_TEST.md)。

这给出具体的研究取舍：把固定 c>1 调小仍有同一幂次损失，暂不继续这一步的常数优化；应估计真正的平均中心化二次矩，或保留筛权与素数之间的联合振荡。结论只关闭这个“上限乘一阶均值”的步骤，未排除所有筛法。

### 第十八轮：变换后的系数小，不代表原问题的算子范数小

将一个算术核转换为按导子求和后，可能出现看似有利的系数
\[
M_{d,j}=\sum_{q:\,d\mid q}\frac{\lambda_j(q)}q,
\qquad \lambda_j(q)=\mu(q)(\log q)^j1_{\mathcal Q_X}(q).
\]
应同时展开作用在这些系数上的全部变换。第十八轮的精确反演为
\[
\sum_{d:\,r\mid d}r\,\mu(d/r)M_{d,j}=\lambda_j(r).
\]
因此，把完整导子核误换成单个模数误差，会留下一个实际上不存在的 \(1/q\) 节省。即使 \(\sum_d|M_{d,j}|\) 只有对数增长，核中的除子倍数也可能抵消这项优势。

一般做法是先写出“系数变换—核变换—最终配对”的完整组合，再计算组合在目标范数中的大小。支撑可分解、系数分解可控、与目标配对相容，是三个独立条件。本项目已证明合法放大层级 \(QY^2=X^{.525}\) 的点质量三重可分解性，但没有得到原始有符号系数的廉价统一分解。[第十八轮公开报告](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/019a3356e515f828dd4215785751c351862cb5e6/research/reports/dyson_round18.md)。

### 第十八轮：用项检验区分解析恒等式与可用的无穷展开

反射功能方程可以给出含有限素数和、gamma 项和零点残数的精确恒等式；是否还能把远端积分关闭成无穷残数和，必须单独验证。在本项目二阶权的 \(X=1,\ W>3/\log2\) 情形，已证明远端积分消失，平凡零点修正为正且 \(O(W^{-4})\)。非平凡零点残数中的未知二次信息仍然存在。

改用 Bragg 载波 \(X=T^2,\ W=T\) 后，拟议平凡零点级数的第 \(k\) 项含有
\[
\frac{\text{正的常数}}{(\sigma+2k)^2}
\left(\frac{X^2e^{6/W}}4\right)^k.
\]
当 \(Xe^{3/W}>2\) 时，项不趋于零，故该无穷级数发散。有限移线恒等式仍有效。可迁移的检验顺序是：先确认恒等式成立，再做具体展开的收敛域和参数一致性检验，最后才尝试用展开估计目标。这里关闭的是一个具体展开，未排除所有功能方程路线。

### 第十九轮：将振荡目标转换为带相同饱和值的正方差

状态：协调审查已通过；[第十九轮公开报告及证明索引](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/974a2f15fff1f2754e7f54739b6360ab4d8eb08a/research/reports/dyson_round19.md)已核实。本节是本项目后续推导，不能归为 FLT 或 186 原文已有结论。

在 RH 下，固定第十六轮的 \(\varepsilon\) 与自相关 bump \(\psi\)，令
\[
A_\varepsilon=1+\varepsilon^2m_1,\quad
\omega(\alpha)=\psi((\alpha-2)/\varepsilon),\quad q_T=1+1/T.
\]
使用所有素数幂构成的 Chebyshev 函数 \(\Psi\)，定义正统计量
\[
V_{\varepsilon,T}=\frac{T}{\log^2T}
\int_1^\infty[\Psi(q_Tx)-\Psi(x)-x/T]^2
\,\omega(\log x/\log T)\frac{dx}{x^2}.
\]
它的素数配对核是区间交集积分，逐项非负；展开后仍保留两个中心项。支撑是整个对数窗口 \(T^{2-\varepsilon}\le x\le T^{2+\varepsilon}\)。

借助 CCCC 的加权 Plancherel 公式，并逐段控制缩放零点高度的两端尾部，已证明
\[
\mathrm{RH+AH\!-\!Pairs}\Longrightarrow V_{\varepsilon,T}\to A_\varepsilon,
\qquad
\liminf_T V_{\varepsilon,T}<A_\varepsilon
\Longrightarrow\limsup_TD_{\varepsilon,T}>0.
\]
第二个结论不要求两个缺口出现在同一组高度；证明通过“没有相位缺口就有完整极限”的逆否命题完成。其用途是把研究目标改成一个具体的中心化素数二次矩上界。它尚未给出这个上界。

另一个可复用细节是先在有限缩放高度 \(0\le y\le R\) 作 Stieltjes 分部积分。核 \(k(y)=\sin^2(y/2)/y^2\) 的 \(|yk'(y)|\) 在无穷区间不可积，不能直接取绝对值后令 \(R=\infty\)。保留有限 \(R\) 和被舍去积分的正性，才能得到有效的定量缺口转换。对光滑平方近似也先固定 \(R\)，再依次取高度极限、近似极限，最后扩大 \(R\)。

已审查作者版本 SHA256：0c5323ac5a983148a9ec433ea1196fb0fd538f00872ac73e9de3ae105c7a2502。原始公式来源为 [CCCC](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf) 的式 (3.8)、式 (3.9) 前的加权等式及 Lemma 13；新的严格素数方差估计不在这些来源中。

### 第十九轮：用一致的有限时间反例检验动态传递条件

固定粒子数的二阶导数不能自动证明一个与粒子数无关的时间区间。这里的有效构造是：

1. 用合作 ODE 的比较原理保住圆周上的最小间距，包括跨越接缝的间距。
2. 将力差分成近邻与远场，用间距控制得到与粒子数无关的加速度界；不要求每个粒子的速度一致有界。
3. 从 ACUE 的有限投影行列式过程证明：有正比例的相邻点对受到确定方向的初始开隙力。
4. 由加速度界把初始力延续到固定的小时间，再用非负局部配对核把这些点对相加。

结果是：初始半格点上的局部 Bragg 缺口恒为零，但确定性排斥热流在 \(N\ge8,\ 0<s\le1/4128768\) 时满足
\[
\mathbb E\mathfrak D_{\varepsilon,N}(s)
\ge2\kappa_\varepsilon(1/84)^2s^2>0,
\qquad \varepsilon=1/4.
\]
这证明仅有该模型的热流、最小间距、背景力和初始低频矩条件，不能提供所需的回到初始时刻的缺口上界。对真实 \(\zeta\) 的比较及算术传递仍待证明；AH-Pairs 本身也不指定 ACUE 初始分布。这个工具的价值是检验一条拟议传递定理究竟缺少什么假设。

已审查作者版本 SHA256：e87f858bbc39a592e1b2e557f0bcb83e05f685706b14586563b3c317ce651735。单独的全局 coherent mode 曲率只作归一化检查，未用于替代上述一致时间证明。

### 第十九轮：把短移位保留在平方内，先算清准确的同余关系

在已构造的、每个模数含 348 个素因子的真实子族上，\(q\asymp X^{.523}\)，且最小素因子一致地随 \(X\) 增大。长度 \(H\) 的短余数包去掉常数分量后的平方范数为
\[
\|v_q^\circ\|_2^2
=\sum_{(h,q)=1}|V(h/H)|^2
-\frac{|\sum_{(h,q)=1}V(h/H)|^2}{\varphi(q)}
\sim H\int|V|^2.
\]
最后一项只有 \(O(H^2/q)\)，不能把整个范数变成这个较小量。完整余数方差也不自动在短包上节省 \(H/q\)。

把物理移位 \(h_1,h_2\) 留在 Cauchy–Schwarz 的平方内，CRT 相容条件变为
\[
h_1n_2\equiv h_2n_1\pmod q.
\]
因此切换变量的长度是 \(HN/q\)，不是固定余数时的 \(N/q\)。它与完成指数和后产生的 Fourier 对偶变量又不同。使用源文献前，应先重写这条准确同余和全部四个中心化乘积项，再计算对角与非对角预算。

令 \(\Delta_q(a)=\sum_{p\equiv a\ (q)}(\log p)f(p/X)-A_f/\varphi(q)\)，其中 \(A_f=\sum_p(\log p)f(p/X)\)，且 \(f\) 是所需的固定光滑素数权。一个尚未证明但足以推进旧紧支撑算术分量的输入是
\[
\sum_{q}\sum_{\substack{H<h<2H\\(h,q)=1}}|\Delta_q(h)|^2
\ll HX(\log X)^C.
\]
它给出 \(H\sqrt{XQ}\) 型上界，对 \(H\le X^{477/2000-\eta}\) 有幂次余量。必须覆盖所需的全部模数、光滑系数和素数幂余项；这个条件性区间不能直接搬到频率二的 Bragg 测试。

已审查并修订对数权重后的作者版本 SHA256：9e6696dfb9b6f5f339436fed8a69a1477e5946b767fde79ecac9973edfc91ffa。未证明上述局部方差估计，也未改善现有 RH 总误差界。

### 第二十轮：先对区间长度平均，构造天然单调的核

状态：协调普通证明审查已通过；[第二十轮公开报告及证明索引](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/037ba82d9c3f2918b7e23a7598cee5dc996546ee/research/reports/dyson_round20.md)已核实。固定 \(\omega(\alpha)=\psi((\alpha-2)/\varepsilon)\)、\(\varepsilon=1/4\)，定义一个与第十九轮单长度统计量不同的实际素数统计量：
\[
\overline V_T=\int_0^\infty e^{-\lambda}\frac{T}{\log^2T}
\int[\Psi(e^{\lambda/T}x)-\Psi(x)-(e^{\lambda/T}-1)x]^2
\omega(\log x/\log T)\frac{dx}{x^2}\,d\lambda .
\]
精确中心是 \((e^{\lambda/T}-1)x\)，所有素数幂都保留。采用正的长度平均，是为了使用恒等式
\[
\int_0^\infty e^{-\lambda}\frac{\sin^2(\lambda y/2)}{y^2}\,d\lambda
=\frac1{2(1+y^2)}.
\]
右端已经单调，无须再用单调上包络替换振荡核。已审查的实际算术传递为
\[
\overline V_T=\int_0^\infty p(y)C_{Ty}\,dy+o(1),
\qquad
p(y)=\frac4\pi\frac{y^2}{(1+y^2)^2},\quad\int_0^\infty p=1.
\]
这里 \(y\) 是缩放后的零点高度，不能将这个 Poisson 因子误认成两个零点之差的核。此式在 RH 下成立，不要求 AH。

关键不是这条初等 Laplace 积分本身，而是其可合法接到真实算术的步骤。先令 \(S=(e^{\lambda/T}-1)^{-1}\)，用正质量界将变化的测试权替换成固定权，再调用固定测试的原始公式。在紧的长度区间之外，分别用固定窗口的 Selberg 界和 RH 的 Chebyshev 误差界处理极短与极长区间。所有辅助截断都在高度极限后移除；没有预设一条文献误差对任意长度统一成立。

结果是 \(\limsup\overline V_T\le A\)，消除了旧转换的 \(L^+\) 损失。但它达到而未严格小于 AH 的饱和值 \(A=1+\varepsilon^2m_1\)，也不自动改善原来的单长度方差。已审查作者版本 SHA256：cd8c2f7dc48530ed02f915dd202c8aedaaaadb1096cafc019beeb595b9beebbe。

### 第二十轮：用一个低频正包络控制尺度变化和高度尖峰

令 \(s(u)=\sin(\pi u)/(\pi u)\)，构造
\[
q(u)=s(u)^2+\tfrac12[s(u-\tfrac12)^2+s(u+\tfrac12)^2].
\]
它同时满足
\[
\widehat q(\alpha)=(1-|\alpha|)_+(1+\cos(\pi\alpha))\ge0,
\quad
q(u)\ge\frac1{2\pi^2(1+u^2)}.
\]
因此，一个已知低频定理就能控制整个空间中的 Schwartz 尾部：实际正配对泛函满足 \(\mathcal M_T(q)\to7/3\)，故对 \(0\le R(u)\le B/(1+u^2)\)，有 \(\mathcal M_T(R)\le6\pi^2B\)（充分大 \(T\)）。它进一步控制测试函数微小伸缩产生的误差。

把相近高度的对数尺度先冻结，再使用
\(0\le\phi_D\le2\phi_0\) 对新增配对项逐项比较，得到
\[
|D_{Ty}-D_T|\le
2A\,\frac{|y-1|}{\max(1,y)}+o(1),
\qquad 1/2\le y\le2,
\]
误差对 \(y\) 一致趋零。此处保留了原来的 Lorentzian 权、重复零点和高度端点；有限高度统计量可以跳跃，结论是渐近一致连续性。

所以，若 \(d=\limsup D_T>0\)，沿一列高度，缺口至少 \(d/2\) 会持续在
\([1-d/(8A),1+d/(8A)]\) 的高度比例区间内。结合前一节已经核查的正平均恒等式，令
\(\delta=A-\liminf\overline V_T\)，得到
\[
\frac{2d^2}{25\pi A}\le\delta\le d.
\]
这使两个“严格缺口为正”的目标等价，不再只有单向充分关系。任一严格缺口都会排除完整 AH-Pairs；未证明 AH-Pairs 不成立必然使这个特定 bump 出现缺口。仍未证明 \(d>0\) 或 \(\delta>0\)。高度证明的已审查 SHA256：6048b8792084d1523212ddd5f0c05dcc5b54fb158c3dab37762675e91a1072fe。

### 第二十轮：有限计算用于验证目标实现，不代替渐近量词

三个固定高度 \(T=100,300,1000\) 的单长度实际素数方差诊断约为
\(0.120406,\ 0.136106,\ 0.154279\)。这些是第十九轮的 \(V_{\varepsilon,T}\)，不是前两节的全长度平均 \(\overline V_T\)。

可复用的计算方法是：在整数坐标 \((T+1)x\) 中精确排列进入、退出事件；保留全部素数幂；在每个事件单元内先稳定计算完整中心化平方，再汇总。两个中心项另行输出以便核对。光滑权使用正的分段上下界，解析离散化误差与浮点舍入误差分别记录。

协调审查已读完整报告和两份脚本，核对作者 15 个文件的哈希及字节数，并重新汇总每个高度的全部 16,384 个 CSV 分段。未重复运行主计算或 70 位精度检查，也未得到包含舍入误差的区间证书。任何有限高度低于 AH 极限值的现象，都不能提供 \(T\to\infty\) 的严格上界。报告的已审查 SHA256：5fd0ecfa3f31785e84e60be55d661f35fbac456bd8038819a9ffc635599677a9。

### 第二十一轮：先截断非负积分，再同时展开所有中心项

本轮四份稿件及其中的实质修订已通过协调者全文普通审查；[第二十一轮公开报告](https://github.com/QingyunSun/Riemann-hypothesis-and-random-matrix/blob/6c49d118fb398a39b9e6e2a1d362a223150e80fd/research/reports/dyson_round21.md)及四份最终作者稿件已与已审查版本核对。以下是本项目后续推导，不能归为 FLT 或 186 原文已证明的结论。

设 \(E(x)=\Psi(x)-x\)、\(L=\log T\)，保留原来的 \(W_T(x)=\omega(\log x/\log T)\)。在全长度平均中，变量 \(y=e^{\lambda/T}x\) 没有上界。先在完整中心化平方上截断，定义
\[
\overline V_{T,N}=\frac{T^2}{L^2}
\int_{T^{7/4}}^{T^{9/4}}W_T(x)x^{T-2}
\int_x^N [E(y)-E(x)]^2y^{-T-1}\,dy\,dx .
\]
对于实数 \(T\ge3\)、\(N=\lceil2T^{9/4}\rceil\)，已证明无条件界
\[
0\le\overline V_T-\overline V_{T,N}
\le2048\,T^{9/4}2^{-T}.
\]
因此，可以用只涉及 \(n\le N\) 的有限素数幂表达式代替整个平均，而不丢失极限信息。展开时，素数对项、交叉中心项和连续平方项必须使用同一个端点。只删去大整数系数并保留原来的无穷中心项，会改变统计量。

这是可复用的截断方法：在正积分层面获得单调性，用粗上界证明尾部足够小，再展开有限对象。误差趋零没有给有限对象本身提供严格上界。另一个必要的范围检查是：\(T=2\) 时完整中心化积分在 RH 下存在，但分开的无穷正项发散，须使用另外的中心化分组。

### 第二十一轮：把粗糙算术函数局部化为有界的热流能量

在对数素数坐标上定义实际函数
\[
F(v)=e^{-v/2}E(e^v),\qquad
g_T(v)=\sqrt{\omega(v/L)}\,F(v).
\]
在 RH 下，\(|F(v)|\ll(1+v_+)^2\)。虽然素数幂使 \(g_T\) 有跳跃，仍有
\[
\overline V_T=
\frac{T(2T-1)}{2\pi(T-1)L^2}
\int_{\mathbb R}
\frac{\xi^2+1/4}{(T-1/2)^2+\xi^2}
|\widehat g_T(\xi)|^2\,d\xi
+O_\omega\!\left(\sqrt{\frac LT}\right),
\]
这里使用角频率 Fourier 约定。

可迁移的关键是对截断移动误差作独立估计。由非负 \(C^2\) 权的
\(|\omega'|^2\le2\|\omega''\|_\infty\omega\)，得到 \(\sqrt\omega\in H^1\)。
平移截断产生的交换子平方范数为 \(O(L^3/T^2)\)；与先前独立证明的算术平方范数 \(O(L^2/T)\) 配合，才得到上面的趋零误差。没有假设阶梯函数的原始导数平方可积。

正乘子又有精确的 Laplace 表示
\[
\frac{\xi^2+1/4}{(T-1/2)^2+\xi^2}
=\int_0^\infty e^{-(T-1/2)^2t}
(\xi^2+1/4)e^{-t\xi^2}\,dt .
\]
这把目标写成普通热半群 \(e^{t\partial_v^2/2}\) 的梯度能量与质量项的正积分。热流作用于上述实际素数误差函数的 \(v=\log x\) 坐标；不产生关于零点变形轨道的结论。严格能量界仍需要额外的算术结构；现有非严格常数 \(A\) 仍来自第二十轮的算术与零点传递。

### 第二十一轮：用 Mellin 变换检验平均后还能恢复什么

对已知概率密度 \(p(y)=4y^2/[\pi(1+y^2)^2]\)，令
\[
K(u)=p(e^{-u})e^{-u},\qquad
\widehat K(\tau)=\frac{1+i\tau}{\cosh(\pi\tau/2)} .
\]
该 Fourier 变换在实轴上处处非零。结合第二十轮已经证明的高度渐近一致连续性和有界性，Wiener 的 \(L^1\) 平移稠密定理给出
\[
\overline V_T\longrightarrow c
\quad\Longleftrightarrow\quad
C_T\longrightarrow c .
\]
这是一个固定测试量的全极限等价，未证明任何一端收敛。证明先固定近似核，再令高度趋于无穷，最后缩小近似误差；不能把这个顺序替换成任意子序列上的反推。[所用 Wiener 定理](https://fa.ewi.tudelft.nl/~neerven/publications/papers/RIMUT_97.pdf)是该预印本第 2 页的 Theorem 1。

通用方法是分别检查变换是否有零点、输入是否具有所需正则性、最后要恢复哪一种极限。这里的倒乘子指数增长，证明没有给出稳定的数值反卷积或收敛速率。

### 第二十一轮：给目标的原始核计算基准，保留未知的带符号余项

令 \(a_n=\Lambda(n)-1\)、\(M=\varepsilon m_0\)，定义
\[
b_T(m)=\frac{T m^{-T}}{\log^2T}
\int_1^m W_T(x)x^{T-2}\,dx ,
\]
\[
\mathcal R_T=
2\sum_{m\ge1}b_T(m)\sum_{h\ge1}
(1+h/m)^{-T}
\bigl[a_ma_{m+h}-(\mathfrak S(h)-1)\bigr],
\]
其中 \(\mathfrak S(h)\) 为经典素数对奇异级数。这些展开在 \(T\ge4\) 绝对收敛；在 RH 下已经证明
\[
\overline V_T=M+\mathcal R_T+o(1).
\]
离散中心与连续中心的差为 \(\{x\}-\{e^{\lambda/T}x\}\)，其平方范数和交叉误差均已控制。因此 \(a_ma_{m+h}\) 保留了两个单素数误差项，没有把它们替换成期望。

基准常数来自对原始 Pareto 核的统一估计：
\[
\sum_{h\ge1}(\mathfrak S(h)-1)(1+h/m)^{-T}
=-\tfrac12\log(m/T)+O(1),
\qquad T\ge4,\quad m\ge T .
\]
从奇异级数的二次原函数出发，做两次分部积分；所得 \(y k''(y)\,dy\) 是概率测度，使已知的 \(O(y)\) 余项只产生 \(O(1)\) 误差。这里使用的是 [Montgomery–Soundararajan 的无条件式 (16)](https://arxiv.org/pdf/math/0409258v1)，不是他们另外带有素数元组猜想假设的矩估计。

当前一个足够的具体目标是
\[
\liminf_{T\to\infty}\mathcal R_T\le1-M.
\]
已有界只给 \(\limsup\mathcal R_T\le A-M\)。旧常数的诊断值分别约为 \(1-M=0.814847\)、\(A-M=0.825435\)；没有新的数值证书。还需证明严格算术改进，不能用奇异级数基准代替实际素数对误差，也不能把原核直接换成指数核而忽略误差被大中心项放大。

### 第二十一轮：先检验统一假设的退化参数，再计算它在目标中的权重

上述稿件的首版曾把“所有位移统一达到 \(\beta<4/9\) 的误差指数”列为仅未证明的较强前提。协调审查在 \(h=1\) 处发现它不可能成立，修订稿保留了原版与完整纠错记录。

对整数 \(X<z\le2X\)，令
\[
E_X(z,h)=\sum_{X<m\le z}
[a_ma_{m+h}-(\mathfrak S(h)-1)].
\]
连续整数都带有非零 \(\Lambda\) 权时，偶数一方只能是 \(2\) 的幂。因此
\[
E_X(z,1)=-2[E(z)-E(X)]+O(\log^2X).
\]
若所有大高度、所有位移都有统一的 \(O(X^\beta\log^B X)\)、\(\beta<1/2\) 界，沿 dyadic 区间求和会得到 \(E(x)=O(x^\theta)\)、\(\theta<1/2\)。这与其 Mellin 变换在已知临界线零点处的非零极点矛盾。障碍不需要 RH。

这否定的是该统一前提；在实际加权目标中，单个 \(h=1\) 的贡献在 RH 下却是 \(o(1)\)。因此不能将它扩大成对所有位移平均方法的否定。可复用的审查顺序是：先用最简单参数检验拟议统一假设，再评估该参数在真正目标中的权重，随后为带符号求和或受限位移范围重新核算误差。

本轮已审查稿件的 SHA-256：

| 稿件 | SHA-256 |
|---|---|
| EXACT_LENGTH_ARITHMETIC_KERNEL.md | bf2e13a5d62f694d638d247fe7d836d0ea57d47f15c8e9360843681ece6b58d9 |
| LOCALIZED_MELLIN_HEAT_ENERGY.md | 1ee3d147669929f78a31e785d974eb851bf943453715c361e32ac2355407a1a8 |
| FIXED_BUMP_TAUBERIAN_EQUIVALENCE.md | 3f3391cb149b69e86d6c758267eec56ae9d86f7523f2dcf078f6f351ff9ee48c |
| CENTERED_PAIR_ERROR_TARGET.md，含实质修订 | d7e73b8379e1adadd1fba79e3dc6141252c796502ba793030a500a8c5a6fc15e |

上述记录不包含尚在研究的增长位移集合估计，也未宣布任何严格方差亏损已被证明。

### 当前交接重点

原始 FLT 与 186 材料提供了构造、分解和核验方法；上述新实例是本项目后续独立推导与普通证明审查的结果，不应倒称为原文已经证明的 RH 工具。协调任务已全文核对本文件所述第十六至二十一轮的相应证明，核查关键原始定理范围，并对三点有限计算阅读代码、核对文件及 CSV 汇总。未重新运行全部计算，未完成 Lean 形式化、外部审稿或全局新颖性判定。

当前主任务应继续证明实际正平均素数方差的严格下降，或等价地证明原 Bragg 缺口具有正上极限。指数平均已经消除了转换常数损失，高度连续性补上了两个严格目标之间的反向联系；本轮有限截断、Mellin–热能量表述和精确素数对余项使所需估计更明确，但仍未提供严格算术增益。下一步应估计真正目标中的带符号余项，先分离可控的位移贡献，再审核剩余项的范围与误差。暂缓更多形式推广、重复常数优化、扩大小规模扫描和大型 PDF 重建；保持一个既有 Fable 会话、一次一个明确任务，本文件不启动新的 Fable 工作。


## 第二十二轮更新：全体单素数修正、奇数位移与偶数端点的合法移除

在第 21 轮已经定义的精确权重下，先把全体带符号单素数修正合并。普通 PNT 足以证明该修正为

\[
O_\omega(1/\log T+\eta(T^{7/4})+2^{-T})=o(1),
\quad
\eta(L)=\sup_{y\ge L}|\Psi(y)-\lfloor y\rfloor|/y.
\]

RH 只用于改进这一步的速率，以及此前从实际方差传递到素数对的结论。后向核中的幂精确抵消为 \(T I_T(n-h)/(n^T\ell^2)\)，其二阶导数保留 \(W_T'\) 的符号；Beta(2,T−2) 包络控制绝对对数矩。主区间误差不加到无穷，两个无限端点各用实际核给出 \(O_\omega(2^{-T})\) 的行尾界。协调者随后完成了这份完整作者稿的普通审查；它是发布冻结之后的新证据。

完成全体中心化以后，奇数位移上的新系数只剩素数幂乘积，其一端必为 2 的幂；全体奇数位移的总贡献有显式 \(O_\omega(T^{-1}+2^{-T}/\ell^2)\) 界。再通过有界交错部分和，把基准由 1 改为 \(2\,1_{m\ {\rm odd}}\)，并支付 \(O_\omega((T\ell)^{-1})\) 的归一化误差。只有这一步之后，才可以删除偶数端点的素数幂余项。

所以在继承的 RH 假设下，精确的新目标是

\[
\overline V_T=M+Q_{2,T}+o(1),
\]
\[
Q_{2,T}=2\sum_{\substack{m\ {\rm odd}\\h\ge2,\ h\ {\rm even}}}
b_T(m)(1+h/m)^{-T}
\{\Lambda(m)\Lambda(m+h)-\mathfrak S(h)[\Lambda(m)+\Lambda(m+h)-2]\}.
\]

所需严格缺口可由 \(\liminf Q_{2,T}<A-M\) 给出；\(\liminf Q_{2,T}\le1-M\) 是更强的充分基准。二者都尚未证明。不能在每个短区间内把剩余单素数项换成平均值，也不能在全体中心化之前直接删去旧余项的奇数位移。

公开 R22 报告为 15,108 字节，SHA256 65e42a25bd4f97774a9a7ef54a1d2976be50e4974c36b3584772185e0081d971。协调者独立核验了 55 份公开原件（279,258 字节）与 58 份本地原件（1,559,249 字节）；这次未重跑全体 checker、Lean、ZIP 或全局清单验证，不把文件一致性当成新的数学证明。后续实际模数分解与局部同余归一化研究继续，未计入这个已核实的公开版本。
