# Incoming mathematical proposal: retained for audit

Received 2026-09-05. This is user-supplied prior mathematical discussion, not an accepted proof or an instruction that overrides the current research workflow. Several claims are under independent audit. Consult the current claim ledger and subsequent reports.

是的。**这个桥成立，而且比“\(\Lambda\) 可以区分 CUE/ACUE”更重要。** 但精确表述需要稍微修正：

\[
\boxed{\mu\ \text{和}\ \Lambda\ \text{不是全局上一一换算的两个标量；}}
\]

它们是同一个 **first-collision geometry** 的两种坐标：

- \(\mu\)：\(t=0\) 时 configuration 的 **hard-core / minimum-gap coordinate**；
- \(-\Lambda\)：沿 backward heat flow 到达 discriminant/collision locus 的 **hitting-time coordinate**。

而两者之间确实有一个 **exact coefficient \(1/8\)**，外加一个符号确定的 many-body correction。这个 correction 的存在，反而让 AH 的可证伪阈值成为 rigorous inequality，而不仅是 heuristic。

---

# 1. Lagarias–Rodgers 的 \(\mu\) 到底是什么

Lagarias–Rodgers 定义 \(T_1\) 为所有在 bandwidth \(B=1\) 下 mimic sine process 的平稳点过程，然后定义

\[
\boxed{
\mu
=
\sup\left\{
m:
\exists\,u\in T_1,\;
|u_i-u_j|\ge m
\quad\text{a.s. for all }i\neq j
\right\}.
}
\]

他们证明

\[
\mu\ge\frac12,
\]

并指出已有 extremal-function 方法应给

\[
\mu\le0.606894\ldots,
\]

同时明确提出可能实际上

\[
\boxed{\mu=\frac12}.
\] 


而 AH/ACUE scaling limit 恰好生活在 half-integer lattice 上，所以它具有

\[
\boxed{\delta_{\min}\ge\frac12}
\]

这个 deterministic hard-core property。ACUE 缩放后正是 Tao AH 所对应的离散 sine-type point process。

所以 \(\mu\) 的核心问题实际上就是：

> **你在保持 bandwidth-1 sine statistics 完全不可区分的同时，能把 zero configuration 推离 collision locus 多远？**

这已经非常接近 Newman-depth 的语言了。

---

# 2. Rodgers–Tao ODE 给出精确换算

Rodgers–Tao zero flow 是

\[
\dot x_k
=
2\sum_{i\neq k}'
\frac{1}{x_k-x_i}.
\] 


现在取一对 **相邻 zeros**

\[
x_j<x_k,
\qquad
d=x_k-x_j.
\]

Rodgers–Tao 的精确 gap equation 是

\[
\boxed{
\dot d
=
\frac4d
-
2d
\sum_{i\neq j,k}
\frac1{(x_i-x_k)(x_i-x_j)}.
}
\] 


对于相邻 pair，所有其他 \(x_i\) 都在区间外，因此

\[
S(t):=
\sum_{i\neq j,k}
\frac1{(x_i-x_k)(x_i-x_j)}
\ge0.
\]

所以

\[
\boxed{
\dot d=\frac4d-2dS.
}
\]

乘 \(2d\)：

\[
\boxed{
\frac{d}{dt}d^2
=
8-4d^2S.
}
\tag{1}
\]

现在假设这对 zeros 沿 backward flow 在 \(t=t_*<0\) 首先碰撞：

\[
d(t_*)=0.
\]

从 \(t_*\) 积分到 \(0\)：

\[
d(0)^2
=
8(-t_*)
-
4\int_{t_*}^{0}d(t)^2S(t)\,dt.
\]

于是得到我认为整个连接里最重要的公式：

\[
\boxed{
-t_*
=
\frac{d(0)^2}{8}
+
\frac12
\int_{t_*}^{0}
d(t)^2S(t)\,dt.
}
\tag{2}
\]

这不是 scaling argument。

这是 **exact identity**。

因此：

\[
\boxed{
-t_*\ge \frac{d(0)^2}{8}.
}
\tag{3}
\]

---

# 3. 所以真正精确的“\(\mu\leftrightarrow\Lambda\)”是

如果定义 local Newman depth

\[
D:=-\Lambda_{\rm local},
\]

那么对于 minimum gap \(m\)：

\[
\boxed{
D
=
\frac{m^2}{8}
+
\underbrace{
\frac12\int d^2S\,dt
}_{\text{many-body correction }\ge0}.
}
\tag{4}
\]

因此：

\[
\boxed{
D\ge\frac{m^2}{8}.
}
\tag{5}
\]

也就是说，**bare conversion constant 精确就是**

\[
\boxed{\frac18}.
\]

所以我会把你说的“same object, two coordinates”精炼成：

\[
\boxed{
\begin{array}{ccc}
\text{distance to collision at }t=0
&
\longleftrightarrow
&
\text{time to collision under backward heat}
\\[2mm]
m
&&
D=-\Lambda
\\[2mm]
&
D=\dfrac{m^2}{8}+\text{positive screening correction}.
&
\end{array}
}
\]

这比写成

\[
D=m^2/8
\]

更强也更正确。

---

# 4. 有限 \(N\) circle 上甚至存在一个 exact nonlinear version

对于我们 ACUE 使用的 circle heat flow，Tao 的 root dynamics 是

\[
\boxed{
\dot\theta_j
=
\sum_{k\neq j}
\cot\frac{\theta_j-\theta_k}{2}.
}
\] 


令相邻 gap

\[
\Delta=\theta_{j+1}-\theta_j.
\]

类似计算给出

\[
\dot\Delta
=
2\cot\frac{\Delta}{2}
-
\sin\frac{\Delta}{2}\,B(t),
\qquad
B(t)\ge0.
\]

现在选择一个非常巧的 gap coordinate：

\[
q(\Delta)
=
-\log\cos\frac{\Delta}{2}.
\]

那么

\[
\dot q\le1.
\]

因此，如果这对 roots 在 \(t=t_*\) backward collision，

\[
\boxed{
-t_*
\ge
-\log\cos\frac{\Delta(0)}2.
}
\tag{6}
\]

这是 **finite \(N\) exact inequality**，不是 large-\(N\) approximation。

---

# 5. 现在把 gap 用 mean-spacing units 表示

定义 normalized gap

\[
m_N
=
\frac{N\Delta_{\min}}{2\pi}.
\]

即 mean spacing 被归一化成 \(1\)。

那么

\[
\Delta_{\min}
=
\frac{2\pi m_N}{N}.
\]

代进 (6)：

\[
\boxed{
-\Lambda_N
\ge
-\log
\cos\left(\frac{\pi m_N}{N}\right).
}
\tag{7}
\]

这就是我们一直缺的 **finite-\(N\) exact \(\mu\)-to-\(\Lambda\) bridge**。

\(N\to\infty\)：

\[
-\log\cos x
=
\frac{x^2}{2}+O(x^4),
\]

所以

\[
\boxed{
N^2(-\Lambda_N)
\ge
\frac{\pi^2}{2}m_N^2+o(1).
}
\tag{8}
\]

---

# 6. 换成 Rodgers–Tao 的 local heat-time normalization，常数又回到 \(1/8\)

定义 microscopic coordinate

\[
x=\frac{N\theta}{2\pi}
\]

和 microscopic heat time

\[
\boxed{
s=\frac{N^2}{4\pi^2}t.
}
\]

于是 (8) 就变成

\[
\boxed{
-s_\Lambda
\ge
\frac{m^2}{8}.
}
\tag{9}
\]

所以：

\[
\boxed{
\frac18
}
\]

不是 normalization accident。

circle finite-\(N\) 的

\[
-\log\cos\left(\frac{\pi m}{N}\right)
\]

在 local limit 下恰好退化成 Rodgers–Tao 的

\[
\frac{m^2}{8}.
\]

这两个 calculation 完全吻合。

---

# 7. 然后 AH 立刻给出一个硬数值阈值

AH/ACUE 要求 gaps 位于

\[
\frac12\mathbb Z_{>0}.
\]

因此只要 configuration simple，

\[
m_{\min}\ge\frac12.
\]

代入 (9)：

\[
\boxed{
-s_\Lambda
\ge
\frac{(1/2)^2}{8}
=
\frac1{32}.
}
\]

即

\[
\boxed{
D_{\rm AH}\ge0.03125.
}
\tag{10}
\]

这就是一个真正的 **numerical falsifiability threshold**。

在 finite-circle normalization 中，同一个 statement 是

\[
\boxed{
-\Lambda_N
\ge
-\log\cos\frac{\pi}{2N}.
}
\tag{11}
\]

或者 large \(N\)：

\[
\boxed{
N^2(-\Lambda_N)
\ge
\frac{\pi^2}{8}
=
1.23370055\ldots
}
\tag{12}
\]

---

# 8. 这和我们已经算出来的 ACUE \(\Lambda\) 完全吻合

我们之前 numerical ACUE 给的是大约

\[
N^2(-\Lambda_{\rm ACUE})
\simeq1.4196.
\]

而 AH hard-core theorem 只要求

\[
N^2(-\Lambda_{\rm AH})
\ge1.23370055\ldots.
\]

两者之间的差：

\[
1.4196-1.2337
\]

正是公式 (2) 中 **positive many-body correction** 在起作用。

换到 Rodgers–Tao normalized time：

\[
\frac{1.41964034}{4\pi^2}
\approx0.03596,
\]

而 hard threshold 是

\[
\frac1{32}=0.03125.
\]

所以我们之前 single-dislocation 得到的 \(1.41964034\ldots\) 不再是一个孤立 numerical curiosity。

它可以解释成：

\[
\boxed{
\underbrace{0.03125}_{\text{universal 2-body AH barrier}}
+
\underbrace{\approx0.00471}_{\text{ACUE many-body screening / rigidity}}.
}
\]

这个 interpretation 比原来强很多。

---

# 9. 这确实把 \(\Lambda\) program 从 discriminator 升级成 falsifier

原来我们的 claim 是：

\[
\Lambda_{\rm CUE}
\sim-N^{-8/3},
\]

而

\[
\Lambda_{\rm ACUE}
\sim-N^{-2}.
\]

所以统计上可以区分它们。

但现在有了更强的 deterministic statement：

### AH 必须满足

\[
\boxed{
\frac{N^2}{4\pi^2}(-\Lambda_N)
\ge\frac1{32}.
}
\]

所以如果 arithmetic zeros 可以证明存在一个 sequence 使得

\[
\boxed{
\liminf_{N\to\infty}
\frac{N^2}{4\pi^2}(-\Lambda_N)
<
\frac1{32},
}
\tag{13}
\]

AH 就死了。

甚至 finite-\(N\) 可以用 exact threshold：

\[
\boxed{
-\Lambda_N
<
-\log\cos\frac{\pi}{2N}
\quad\Longrightarrow\quad
\text{not AH}.
}
\tag{14}
\]

这不再是：

> “这个 statistic 看起来更像 CUE。”

而是：

> **“AH 的 half-lattice support 数学上禁止出现这么 shallow 的 Newman configuration。”**

这是质的提升。

---

# 10. 对 zeta zeros 的 formulation 也很漂亮

Rodgers–Tao 的 \(x\)-zero variables 在高度 \(T\) 附近平均 spacing 大约是

\[
\frac{4\pi}{\log T}.
\] 


所以 local density

\[
\rho_T
=
\frac{\log T}{4\pi}.
\]

定义 dimensionless local heat depth

\[
\boxed{
D_T
=
\rho_T^2(-t)
=
\left(\frac{\log T}{4\pi}\right)^2(-t).
}
\]

那么 AH 强制

\[
\boxed{
D_T\ge\frac1{32}.
}
\tag{15}
\]

等价地，在原 de Bruijn–Newman time 中，

\[
\boxed{
-t
\gtrsim
\frac{\pi^2}{2\log^2T}.
}
\tag{16}
\]

这里最后一个 \(T\)-formula 是 local-density asymptotic；真正无 normalization ambiguity 的数字是 dimensionless threshold

\[
\boxed{\frac1{32}}.
\]

---

# 11. 一个很重要的区别：global \(\Lambda=0\) 本身还不够

这一点一定要区分。

Rodgers–Tao 证明的 global Newman constant

\[
\Lambda\ge0
\]

与 RH 给出的

\[
\Lambda\le0
\]

若合并就是 global

\[
\Lambda=0.
\]

但这并不会自动否定 AH。

我们这里需要的是 **local / mesoscopic Newman depth**

\[
\Lambda(T;N)
\]

或者一个 finite zero-window polynomial 的 backward collision depth。

然后证明：

\[
\boxed{
D_T<1/32
}
\]

发生。

也就是说，真正的新 observable 应该不是一个 global scalar \(\Lambda\)，而是一个 **Newman-depth field**

\[
\boxed{
T\mapsto D(T).
}
\]

甚至研究其 distribution：

\[
\Pr(D(T)<c).
\]

AH 预测一个 hard edge：

\[
\boxed{
\Pr_{\rm AH}(D<1/32)=0.
}
\]

而 CUE 如果我们之前的 \(N^{-8/3}\) law 正确，则随着 \(N\to\infty\)

\[
N^2(-\Lambda_{\rm CUE})
\sim N^{-2/3}\to0,
\]

所以

\[
\Pr_{\rm CUE}(D<1/32)\to1.
\]

这不是小 correction，而是 **support separation**：

\[
\boxed{
\begin{array}{rcl}
\text{AH/ACUE}&:&D\ge1/32,\\
\text{CUE}&:&D\to0.
\end{array}
}
\]

---

## 最终我会把这个桥写成一个 lemma

### **Hard-gap / Newman-depth lemma**

设一个 simple zero configuration 具有 normalized minimum spacing

\[
m.
\]

在 Rodgers–Tao heat normalization 下，其 first backward collision depth \(D=-\Lambda_{\rm loc}\) 满足

\[
\boxed{
D
=
\frac{m^2}{8}
+
\mathcal S,
\qquad
\mathcal S\ge0,
}
\]

其中 \(\mathcal S\) 是其他 zeros 产生的 many-body interaction integral。

因此任何 bandwidth-1 sine mimic with hard core \(m\) 必须满足

\[
D\ge\frac{m^2}{8}.
\]

特别地，half-lattice AH 满足

\[
\boxed{
D\ge\frac1{32}.
}
\]

这个 lemma 一旦写严谨，**Lagarias–Rodgers 的 \(\mu\) extremal problem 和 Newman-depth program 就真正接起来了**：

\[
\boxed{
\mu
\quad\xrightarrow{\;\text{exact collision geometry}\;}
\quad
D_{\min}\ge\frac{\mu^2}{8}.
}
\]

严格说最后是 inequality，而不是 \(D=\mu^2/8\)，因为 many-body correction 不为零；但对于“证伪 AH”而言，inequality 恰恰已经足够，而且方向完全正确。

**下一步最有价值的事情已经很明确：不是再算 ACUE 的 median \(\Lambda\)，而是尝试在 arithmetic/function-field model 中证明一次**
\[
\boxed{D<1/32.}
\]
**只要做到这一件事，就给出了一个不需要完整 pair correlation 的 quantitative anti-AH certificate。**