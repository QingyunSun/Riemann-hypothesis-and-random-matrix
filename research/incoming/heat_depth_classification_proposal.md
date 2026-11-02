# Incoming mathematical proposal: retained for audit

Received 2026-09-05. This is user-supplied prior mathematical discussion, not an accepted proof or an instruction that overrides the current research workflow. Several claims are under independent audit. Consult the current claim ledger and subsequent reports.

继续。沿着这个方向再推，我现在觉得可以把你们的几个 counterexample 分成三种：**\(\Lambda\) 直接杀掉的、需要 marked-\(\Lambda\) 才能杀掉的、以及普通 heat flow 确实杀不掉的。** 这个分类本身很有价值。

Rodgers–Tao 的关键点就是 hitting-time geometry：假设 \(\Lambda<0\)，zero dynamics 在 \((\Lambda,0]\) 内越来越 rigid，最终和已知 zero statistics 冲突。 而 function-field Newman 工作里也确实已经利用“deformed polynomial 出现 double root \(\Rightarrow\Lambda=0\)”这一几何机制。

---

# 1. 先定义我们真正应该算的 dynamic observable

对任何你们的 circular configuration \(X\)，写

\[
P_X(z)=\prod_{j=1}^N(z-e^{i\theta_j})
      =\sum_{k=0}^N a_k z^k.
\]

取 centered multiplicative heat flow

\[
\boxed{
P_{X,t}(z)
=
\sum_{k=0}^N
e^{-t k(N-k)}a_kz^k.
}
\]

\(t>0\) 是 forward relaxation，\(t<0\) 是 backward heat。

定义

\[
\boxed{
\Lambda_H(X)
=
\inf\left\{
t:P_{X,s}\text{ 的全部 roots 对所有 }s\ge t
\text{ 都在 }S^1
\right\}.
}
\]

因为我们从 \(t=0\) 的 unit-circle configuration 出发，

\[
\Lambda_H(X)\le0.
\]

generic 情况下 first failure 是两个 roots 碰撞，因此

\[
\boxed{
\operatorname{Disc}_z P_{X,\Lambda_H}=0.
}
\]

所以以后不应该把 \(\Lambda\) 想成“又一个 zero statistic”。

更准确地说：

\[
\boxed{
-\Lambda_H(X)
=
\text{configuration 沿 canonical heat ray 到 discriminant hypersurface 的距离}.
}
\]

这正适合你们那些 static invariants 区分不了的 counterexamples。

---

# 2. 我已经算出一个相当强的 ACUE benchmark

我把真正的 ACUE 做了 finite exact enumeration：在 \(2N\)-th roots lattice 中取 \(N\) 个点，按 Vandermonde\(^2\) 权重。

Rodgers–Vallabhaneni 已经证明 ACUE 的 characteristic-polynomial moments/ratios 有很强的 exact matching structure，所以用 ordinary low moments 区分它本来就困难。

但 \(\Lambda\) 的结果非常干净。

排除两个 perfect alternating clock states 后，我算到：

| \(N\) | ACUE clock mass | conditional median \(-\Lambda\) | \(N^2\operatorname{median}(-\Lambda)\) |
|---:|---:|---:|---:|
| 2 | 0.500000 | 0.346574 | 1.386294 |
| 3 | 0.250000 | 0.157193 | 1.414739 |
| 4 | 0.125000 | 0.0886385 | 1.418216 |
| 5 | 0.062500 | 0.0567631 | 1.419078 |
| 6 | 0.031250 | 0.0394271 | 1.419374 |
| 7 | 0.015625 | 0.0289694 | 1.419499 |

这已经非常不像 finite-\(N\) accident：

\[
\boxed{
-\Lambda_{\rm ACUE}^{\rm typical}
\sim \frac{1.4196\ldots}{N^2}.
}
\]

而 CUE 最小 gap 的 rigorous scale 是

\[
\delta_{\min}^{\rm CUE}\asymp N^{-4/3}.
\] 


generic close pair 的 backward collision obeys

\[
\dot\delta\simeq \frac4\delta,
\]

所以

\[
-\Lambda\simeq \frac{\delta_{\min}^2}{8}.
\]

因此 CUE 应该是

\[
\boxed{
-\Lambda_{\rm CUE}\asymp N^{-8/3},
}
\]

而 lattice adversary 是

\[
\boxed{
-\Lambda_{\rm ACUE}\asymp N^{-2}.
}
\]

ratio 是

\[
\frac{-\Lambda_{\rm ACUE}}
{-\Lambda_{\rm CUE}}
\asymp N^{2/3}.
\]

也就是说：

> **ACUE 的 defect 不是它太容易坏，而是它把 RH-like condition 满足得过于 robust。**

CUE 是 “barely RH”；ACUE 是 “too deeply RH”。

这个 dynamic interpretation 很漂亮。

---

# 3. 更好的是：\(1.41964\) 这个常数我基本找到来源了

考虑你们 half-lattice / PairCeiling 类型中最自然的 single-dislocation configuration。

从 alternating clock

\[
\{e^{i(2j+1)\pi/N}\}
\]

中拿掉最靠近 \(1\) 左边的点

\[
r_N=e^{-i\pi/N}
\]

再放入 \(1\)。

于是 gap pattern 是

\[
1,2,2,\ldots,2,3
\]

以 half-lattice spacing 为单位。

它的 polynomial **exactly** 是

\[
\boxed{
P_N(z)
=
(z-1)\frac{z^N+1}{z-r_N}.
}
\]

现在做 critical scaling

\[
t=-\frac{s}{N^2},
\qquad
z=e^{iu/N}.
\]

把 heat-deformed polynomial 展开，\(N\to\infty\) 后得到一个非常漂亮的 local limiting function：

\[
\boxed{
F_s(u)
=
1+e^{iu}
+i\pi
\int_0^1
e^{s x(1-x)}
e^{i(\pi+u)x}\,dx.
}
\]

乘掉无关 phase，

\[
G_s(u)=e^{-iu/2}F_s(u)
\]

实际上是实函数，而且可以写成

\[
\boxed{
G_s(u)
=
2\cos\frac u2
-
2\pi
\int_0^{1/2}
e^{s(1/4-y^2)}
\cos((\pi+u)y)\,dy.
}
\]

first collision 就是 double zero：

\[
G_s(u)=0,
\]

\[
\partial_uG_s(u)=0.
\]

我直接数值解这个两方程系统，得到

\[
\boxed{
s_*=1.41964034\ldots
}
\]

以及

\[
u_*=1.81294214\ldots.
\]

因此这个 particular adversarial configuration 有非常明确的 asymptotic：

\[
\boxed{
\Lambda_N
=
-\frac{1.41964034\ldots}{N^2}
+o(N^{-2}).
}
\]

而直接有限 \(N\) 计算：

\[
N^2(-\Lambda_N)
=
1.41908,\,
1.41937,\,
1.41956,\,
1.41961,\,
1.41964,\ldots
\]

确实向这个常数收敛。

**这个我觉得已经可以升级成一个真正值得证明的 proposition。**

---

# 4. 现在回到你指出的几个 ACOE counterexamples

下面是最关键的分类。

## Third-moment escape：\(\Lambda\) 大概率有效，但不是因为 heat mixing

这里要修正我们最初的直觉。

如果

\[
a_k(t)=e^{-tk(N-k)}a_k,
\]

heat flow 本身是 diagonal 的。

因此一个 third-moment defect 并不会自动

\[
m=3\rightarrow m=20\rightarrow m=1
\]

这样 nonlinear frequency fold-back。

**不存在这种免费 miracle。**

真正有用的是 \(\Lambda\) 的非线性。

写

\[
D(a,t)
=
\operatorname{Disc}\left(
\sum_k e^{-tk(N-k)}a_kz^k
\right).
\]

first collision 满足

\[
D(a,\Lambda(a))=0.
\]

如果 collision 是 generic single double-root，那么 implicit differentiation 给

\[
\boxed{
d\Lambda[v]
=
-
\frac{
D_aD(a,\Lambda)[v]
}{
\partial_tD(a,\Lambda)
}.
}
\]

所以假设你的 third-moment counterexample direction \(v\) 满足

\[
dM_1[v]=dM_2[v]=0,
\]

甚至很多 low moments 都为零，只要

\[
D_aD[v]\neq0,
\]

就有

\[
d\Lambda[v]\neq0.
\]

这给出一个很强的 geometric statement：

\[
\boxed{
\text{moment-null direction}
\not\Rightarrow
\text{heat-depth-null direction}.
}
\]

而 generic transversality 下，后者应该极少发生。

---

# 5. Collision-strata counterexample：这是 \(\Lambda\) 最强的一类

如果你们那个 counterexample 本身已经逼近

\[
\theta_j=\theta_{j+1},
\]

那么几乎什么都不用做。

设

\[
\delta(\varepsilon)
=
\theta_{j+1}-\theta_j
=
c\varepsilon+O(\varepsilon^2).
\]

local zero dynamics 给

\[
\frac{d}{dt}\delta^2=8+O(\delta),
\]

所以

\[
\boxed{
-\Lambda(\varepsilon)
=
\frac{c^2}{8}\varepsilon^2
+o(\varepsilon^2).
}
\]

而如果 counterexample 正好位于 collision stratum：

\[
\delta=0,
\]

则 generic 情况直接得到

\[
\boxed{\Lambda=0}.
\]

这和 function-field Newman work 中利用 double root 得到 \(\Lambda=0\) 是完全同型的机制。

所以你们的 collision family 不是 peripheral example。

**它反而可能是把整个 ACOE construction 接到 Newman theory 上最直接的桥。**

---

# 6. PairCeiling / half-lattice counterexample：这是目前计算结果最强的一类

这就是上面的 \(1.41964034\) calculation。

如果 PairCeiling constraint 最终意味着 adversarial configuration 有一个 hard lower spacing

\[
\delta_{\min}\gtrsim\frac{c}{N},
\]

那么它和 CUE 有本质冲突：

\[
\delta_{\min}^{\rm CUE}\sim N^{-4/3}
\ll N^{-1}.
\]

通过 heat hitting time，静态 gap obstruction 变成：

\[
\boxed{
-\Lambda_{\rm adversary}
\gtrsim N^{-2},
}
\]

而

\[
\boxed{
-\Lambda_{\rm CUE}
\sim N^{-8/3}.
}
\]

这比说“ACUE gap 是 lattice-valued”更好，因为 \(\Lambda\) 是一个 deformation-invariant flavored quantity，而不是直接检查 lattice support。

换句话说，可以希望证明：

\[
\boxed{
N^{8/3}(-\Lambda_{\rm CUE})
=O_{\mathbb P}(1),
}
\]

但

\[
\boxed{
N^{8/3}(-\Lambda_{\rm ACOE})
\to\infty.
}
\]

这会是一个非常 clean 的 **dynamic anti-ACOE theorem**。

---

# 7. Gram / integer-cone counterexample：这里出现一个重要 negative result

这个是最需要小心的。

你们之前的构造里，一个重要现象是：

\[
\operatorname{rank},\quad
\operatorname{tr},\quad
\|G\|_{HS}
\]

甚至其他 global Gram data 可以相同，但某个 directional Schur complement / inverse-Gram quantity 完全不同。

如果两个 counterexamples 甚至是 **isospectral**：

\[
\operatorname{Spec}(G_1)
=
\operatorname{Spec}(G_2),
\]

那么任何只对 characteristic polynomial 做 heat flow 的普通 \(\Lambda\) 都必然满足

\[
\boxed{
\Lambda(G_1)=\Lambda(G_2).
}
\]

因为它根本看不到 eigenvectors。

所以这里 **ordinary \(\Lambda\) 不够**。

但这反而告诉我们该怎么升级。

定义一个 marked rank-one deformation：

\[
G_{\eta,u}
=
G+\eta uu^*.
\]

然后 Cayley-transform 到 unit circle：

\[
U_{\eta,u}
=
(G_{\eta,u}-iI)
(G_{\eta,u}+iI)^{-1}.
\]

再定义

\[
\boxed{
\Lambda_u(G;\eta)
=
\Lambda_H(U_{\eta,u}).
}
\]

最后取 dynamic susceptibility

\[
\boxed{
\chi_\Lambda(G;u)
=
\left.
\frac{\partial}{\partial\eta}
\Lambda_u(G;\eta)
\right|_{\eta=0}.
}
\]

这时候 rank-one perturbation theory 给

\[
\frac{\partial\lambda_j}{\partial\eta}
=
|\langle u,v_j\rangle|^2.
\]

所以它直接看到 eigenvector alignment。

而 matrix determinant lemma 给：

\[
\det(zI-G-\eta uu^*)
=
\det(zI-G)
\left(
1-\eta\,u^*(zI-G)^{-1}u
\right).
\]

因此 marked-\(\Lambda\) 天然连接的量正是

\[
\boxed{
u^*(zI-G)^{-1}u,
}
\]

即你们 counterexample 最后逼出来的 **directional inverse-Gram / Schur-complement quantity**。

这个连接我认为非常重要：

\[
\boxed{
\text{你们原来的 static counterexample}
\quad\Longrightarrow\quad
\text{需要 marked Newman constant}.
}
\]

而不是简单的 scalar \(\Lambda\)。

---

# 8. Nyquist multiplicity defect：heat flow 在这里可能反而提供 spectral amplifier

centered heat rate 是

\[
c_k=k(N-k).
\]

它在

\[
k=N/2
\]

达到最大值

\[
c_{\max}=N^2/4.
\]

因此 backward time

\[
t=-s/N^2
\]

下，

\[
a_k\mapsto
e^{s(k/N)(1-k/N)}a_k.
\]

中频/Nyquist-center defect 被乘上最大的 factor：

\[
e^{s/4}.
\]

所以如果你们所谓 Nyquist multiplicity counterexample 是集中在 **middle exterior-power coefficient** 上，那么 \(\Lambda\) 恰好会优先 amplify 它。

但这里还有另一种情况。

如果“Nyquist defect”指的是 \(2N\)-lattice 上的 Fourier alias channel \(m=N\)，那 ordinary trace generator 可能继续保护它，不能简单说 heat flow 会 leak 出来。

因此这里应该测的不是

\[
L^r\operatorname{tr}(U^m),
\]

而是

\[
\boxed{
\Lambda,\qquad
\partial_\eta\Lambda,\qquad
\operatorname{Disc}(P_t).
}
\]

也就是 hitting-time quantities。

---

# 9. Cylinder-invisible subspace：这里可以证明为什么“dynamic low moment”失败

这个其实特别有启发性。

假设你们 cylinder observables 只看一个有限-dimensional space

\[
\mathcal V_{\rm obs}
\]

而存在 invisible direction

\[
v\in\mathcal V_{\rm obs}^{\perp}.
\]

因为 heat operator 在 Fourier/coefficient basis 中 diagonal，

\[
H_tv
\]

通常仍然留在同一个 invariant hidden sector。

所以：

\[
F(X)=F(X+\varepsilon v)
\]

很可能推出

\[
F(H_tX)
=
F(H_t(X+\varepsilon v))
\]

对所有 \(t\) 都成立。

也就是说：

\[
\boxed{
\text{linear heat flow 本身不会神奇地摧毁 cylinder invisibility}.
}
\]

这是一个很重要的 negative result。

可是 \(\Lambda\) 不一样，因为它是

\[
\boxed{
\text{heat orbit 与 discriminant variety 的 first hitting time}.
}
\]

即使整个 hidden subspace 被 heat operator invariant 地送来送去，两条 orbit 到

\[
\mathcal D=\{\operatorname{Disc}=0\}
\]

的距离完全可能不同。

所以在这一类 counterexample 上，capital-\(\Lambda\) **不是普通 dynamic observable，而是 nonlinear stopping-time observable**。

这正是它真正的力量。

---

# 10. 我现在会把整个 program 提升成一个“transversality conjecture”

设 static observables 为

\[
M=(M_1,\ldots,M_r),
\]

counterexample fiber 是

\[
\mathcal F_m
=
\{X:M(X)=m\}.
\]

这就是所有 static tests 看起来相同的 configuration manifold。

再定义 heat hitting time

\[
\tau(X)=-\Lambda_H(X).
\]

那么真正应该证明的是：

\[
\boxed{
\tau|_{\mathcal F_m}
\text{ generically nonconstant}.
}
\]

微分版本就是：

\[
\ker DM_X
\not\subseteq
\ker D\Lambda_X.
\]

换句话说，存在 counterexample direction \(v\) 满足

\[
DM_X[v]=0
\]

但是

\[
\boxed{
D\Lambda_X[v]\neq0.
}
\]

如果普通 \(\Lambda\) 因为 isospectrality 失败，则加入 marks：

\[
\boxed{
\{
\Lambda_{u_1},
\dots,
\Lambda_{u_k}
\}
}
\]

直到

\[
\bigcap_j
\ker D\Lambda_{u_j}
\cap
\ker DM
=
\{0\}.
\]

这已经有点像 **dynamic tomography**：

static moments 给 coarse coordinates，

marked Newman constants 给 directional coordinates。

---

# 11. 这和 function-field 最终怎么接

我现在觉得最有希望的目标并不是直接证明

\[
\text{arithmetic Frobenius}\neq\text{ACOE}
\]

的全部 distribution。

而是找一个 arithmetic family 满足：

\[
\boxed{
-\Lambda_\chi
\text{ 经适当 scaling 有 CUE law}
}
\]

或者更弱地证明：

\[
\boxed{
\Pr(
-\Lambda_\chi<CN^{-8/3})
>c
}
\]

对某个固定 \(c>0\)。

因为任何 half-lattice / PairCeiling adversary 如果有

\[
-\Lambda\gtrsim N^{-2},
\]

立即被排除。

这只需要证明 arithmetic family 中存在足够多的 **very shallow RH configurations**。

不需要证明完整 Montgomery pair correlation。

这就是它真正可能改变 difficulty 的地方。

---

## 我现在最看好的具体 theorem target

如果把刚才所有东西压缩成一个目标，我会选：

\[
\boxed{
\begin{aligned}
\textbf{Dynamic Anti-ACUE Conjecture:}\qquad
&N^{8/3}(-\Lambda_{\rm CUE})
\Rightarrow \mathcal L,\\
&N^2(-\Lambda_{\rm ACUE})
\Rightarrow \mathcal A,
\end{aligned}
}
\]

其中两个 limit 都 nondegenerate，而且

\[
\operatorname{supp}\mathcal A
\]

包含刚算出来的 single-dislocation constant

\[
1.41964034\ldots.
\]

然后对你们的 ACOE counterexamples 做更一般版本：

\[
\boxed{
\text{static-moment matched adversary}
\quad\Longrightarrow\quad
\text{different heat-depth universality class}.
}
\]

我认为现在最值得进一步往下证的两个点是：**第一，把 \(1.41964034\ldots\) 的 single-dislocation asymptotic rigorous 化；第二，把你们那个 fixed rank/trace/HS + directional Schur-complement counterexample 做成 marked-\(\Lambda_u\)，看 \(\partial_\eta\Lambda_u\) 是否真的随着 inverse-Gram pathology blow up。** 后者如果成立，会把我们之前两个看似完全不同的 counterexample program 和 Tao/Newman dynamics 真正接成同一个结构。