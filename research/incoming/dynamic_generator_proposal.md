# Incoming mathematical proposal: retained for audit

Received 2026-09-05. This is user-supplied prior mathematical discussion, not an accepted proof or an instruction that overrides the current research workflow. Several claims are under independent audit. Consult the current claim ledger and subsequent reports.

可以，而且这里我觉得确实出现了一个比我们之前 **static ACUE counterexample search** 更强的方向。不过先纠正一个符号：

\[
\boxed{\text{RH}\iff \Lambda\le 0}
\]

而 **Rodgers–Tao 证明的是**

\[
\boxed{\Lambda\ge 0}.
\]

所以如果 RH 成立，结合两者就是

\[
\boxed{\Lambda=0}.
\]

Rodgers–Tao 的反证是假设 \(\Lambda<0\)。那么在整个 \(\Lambda<t\le0\) 区间，\(H_t\) 的 zeros 都是真实且 simple，并满足一个非常具体的 interacting-particle ODE：

\[
\boxed{
\partial_t x_k(t)
=
2\,\mathrm{PV}\sum_{j\neq k}
\frac1{x_k(t)-x_j(t)}
}
\]

也就是一个确定性的 logarithmic-Coulomb repulsion flow。Rodgers–Tao 证明这种 flow 如果能从某个负时间一路运行到 \(0\)，会强迫 \(H_0\) 的 zeros 在局部越来越接近 arithmetic progression；而这和 Montgomery 已知的 pair-correlation information 冲突，于是 \(\Lambda<0\) 不可能。

而你现在提出的东西，我认为可以被提炼成一个相当明确的新研究程序。

---

# 1. 真正值得借来的不是 heat equation，而是这个 proof architecture

我们以前 ACUE 的问题基本是：

\[
\mu_{\rm CUE}
\quad\text{vs}\quad
\mu_{\rm ACUE}
\]

寻找 observable \(F\)，使得

\[
\mathbf E_{\rm CUE}F
\neq
\mathbf E_{\rm ACUE}F.
\]

困难就在于 Tao 构造 ACUE 的目的，就是让它在大量 low-frequency / low-degree observables 上和 CUE 完全一样。

例如 Tao 明确指出，在相当大的 low-moment range 内，ACUE 和 CUE 完全匹配；ACUE 的相位则被限制在 \(2N\)-th roots of unity 的 lattice 上，是一个 discrete determinantal process。

所以 static observable 很难：

\[
F(X)
\]

看不出来。

但 Rodgers–Tao 告诉我们的新哲学是：

> **不要直接观察 configuration。**
>
> 先让 configuration 被一个 nonlinear dynamics amplify，然后观察它的 response。

也就是说，把 observable 换成

\[
F(\Phi_t(X)),
\]

甚至更好：

\[
\left.\frac{d^r}{dt^r}
F(\Phi_t(X))
\right|_{t=0}.
\]

这就是你说的 **dynamic observable**。

---

# 2. ACUE 恰好具有一种 dynamics 可能极度不喜欢的结构

Tao 的 ACUE 有两个性质：

### A. low Fourier data 假装成 CUE

例如对低频 \(j\)，它满足和 CUE 一样的 trace moments。

但是：

### B. microscopic geometry 被锁在 lattice 上

相邻 phase gap 是

\[
\frac{m}{2N},
\qquad m\in\mathbb Z_{>0}.
\]

而且 ACUE 本身可以看成 CUE determinantal process 在离散 \(2N\)-root lattice 上的限制。

这是个非常重要的不对称：

\[
\boxed{
\text{Fourier-low-frequency smooth}
\qquad\text{but}\qquad
\text{real-space microscopically singular}
}
\]

静态 low moments 看不到 lattice。

但是像

\[
\sum_{j\ne k}\frac1{x_k-x_j}
\]

这样的 Coulomb force **直接看到 gap denominators**。

于是 dynamics 很可能立即看到。

---

# 3. 第一件应该算的东西：ACUE configuration 的 initial velocity field

把 circle unwrap 到 microscopic scale。

令

\[
y_j=N\theta_j,
\]

于是 CUE 极限是 sine process，而 ACUE 位于

\[
y_j\in \frac12\mathbb Z
\]

的 lattice 上。

定义 Rodgers–Tao-type flow：

\[
\dot y_k
=
2\,\mathrm{PV}
\sum_{j\ne k}
\frac{1}{y_k-y_j}.
\tag{D}
\]

严格讲，对 circle 更自然的版本其实是

\[
\boxed{
\dot\theta_k
=
\sum_{j\ne k}
\cot\pi(\theta_k-\theta_j)
}
\tag{C}
\]

这是 circular logarithmic Coulomb flow。

现在取

\[
X\sim\mathrm{ACUE}_N.
\]

第一批 observable 不应该去算 evolved pair correlation；太重了。

先算：

\[
V_k(X)
=
\sum_{j\ne k}
\cot\pi(\theta_k-\theta_j).
\]

以及

\[
\mathcal V_2(X)
=
\frac1N\sum_k |V_k|^2.
\]

问题变成：

\[
\boxed{
\mathbf E_{\rm ACUE}\mathcal V_2
\stackrel{?}{\neq}
\mathbf E_{\rm CUE}\mathcal V_2
}
\]

甚至 scaling exponent 会不会不同。

这个量本身就是一个 dynamic observable：

\[
\mathcal V_2
=
\|\dot X(0)\|^2.
\]

它等于 configuration 对 Coulomb relaxation 的 instantaneous susceptibility。

---

# 4. 我怀疑最强信号其实不在 velocity，而在 acceleration / curvature

因为 CUE density 本身就是

\[
d\mu_{\rm CUE}
\propto
\prod_{i<j}
|e^{i\theta_i}-e^{i\theta_j}|^2d\theta,
\]

所以

\[
\nabla_{\theta_k}\log\mu_{\rm CUE}
=
2\sum_{j\ne k}
\cot\frac{\theta_k-\theta_j}{2}.
\]

也就是说 Coulomb vector field 正是 Vandermonde energy 的 gradient。

ACUE 则是**同一个 Vandermonde weight 被 restrict 到 lattice**。

因此这是一个非常特殊的 pair：

\[
\boxed{
\text{continuous Gibbs equilibrium}
\quad\text{vs}\quad
\text{lattice-restricted Gibbs equilibrium}
}
\]

Static polynomial observables 可以高度相同。

但它们对 continuous gradient flow 的响应完全没理由相同。

这意味着可以研究 infinitesimal generator。

设

\[
L
=
\sum_k V_k(\theta)\partial_{\theta_k}.
\]

那么对 Fourier observable

\[
p_m(\theta)
=
\operatorname{tr}U^m
=
\sum_k e^{im\theta_k},
\]

动态导数就是

\[
Lp_m.
\]

接着看

\[
L^2p_m,\quad L^3p_m,\dots
\]

我觉得这里可能出现一个非常漂亮的 phenomenon：

\[
\mathbf E_{\rm ACUE}[p_m]
=
\mathbf E_{\rm CUE}[p_m],
\]

甚至

\[
\mathbf E_{\rm ACUE}|p_m|^2
=
\mathbf E_{\rm CUE}|p_m|^2
\]

对 \(m<N\) 都成立，

**但是**

\[
\boxed{
\mathbf E_{\rm ACUE}[L^r |p_m|^2]
\neq
\mathbf E_{\rm CUE}[L^r |p_m|^2]
}
\]

可能在非常小的

\[
m\ll N,\qquad r=1,2,3
\]

就已经分开。

如果是真的，这就很重要。

因为我们把 Tao 的「必须进入 \(j>N\) 高频」障碍变成：

\[
\boxed{
\text{low spatial frequency}
+
\text{dynamic derivatives}
}
\]

而不是直接要求 high Fourier frequency。

---

# 5. 为什么 dynamics 会把 high frequency “fold back” 到 low frequency

这是我觉得这里最值得算的数学机制。

考虑

\[
p_m=\sum_kz_k^m,
\qquad z_k=e^{i\theta_k}.
\]

Coulomb interaction 里出现

\[
\frac{z_k+z_j}{z_k-z_j}.
\]

所以 \(Lp_m\) 会包含类似

\[
\sum_{j\ne k}
z_k^m
\frac{z_k+z_j}{z_k-z_j}.
\]

利用对称化，

\[
\frac{
z_k^m(z_k+z_j)-z_j^m(z_j+z_k)
}{z_k-z_j}
\]

变成一个 polynomial：

\[
(z_k+z_j)
\frac{z_k^m-z_j^m}{z_k-z_j}
=
(z_k+z_j)
\sum_{\ell=0}^{m-1}
z_k^{m-1-\ell}z_j^\ell.
\]

所以 generator 会把单个 Fourier mode 变成 **products of lower modes**。

schematically：

\[
\boxed{
Lp_m
=
a_m p_m+
\sum_{a+b=m}c_{a,b}p_ap_b.
}
\]

再施加一次 \(L\)：

\[
L^2p_m
\]

就出现 cubic trace products。

继续下去，就是一个不断增长的 moment algebra。

这很有意思，因为 ACUE 的 static protection 是：

\[
\sum j a_j\le N
\]

以内的 moment identities。

Dynamics 会使 degree 不断增长：

\[
m
\rightarrow
2m
\rightarrow
3m
\rightarrow\cdots.
\]

于是即使起始 observable 是

\[
m=1
\]

或者 \(m=2\)，

经过 \(r\) 次 dynamic derivative 后，**effective degree** 可能增长到 \(r\)。

所以存在一个 natural question：

\[
r_*(N)
=
\min\{r:
\mathbf E_{\rm ACUE}L^rF
\neq
\mathbf E_{\rm CUE}L^rF
\}.
\]

如果

\[
r_*(N)\sim N,
\]

那没太大帮助。

但如果由于 gap singularity / lattice aliasing，

\[
\boxed{r_*(N)=O(1)}
\]

或者

\[
O(\log N),
\]

这就完全不一样了。

这应该是我们最先 computationally attack 的问题。

---

# 6. 这里甚至可能有一个比 Tao static \(j>N\) barrier 更尖锐的机制：aliasing

ACUE 的 lattice 是

\[
z_k^{2N}=e^{i\phi}
\]

同一个 global phase。

因此 Fourier mode 有 exact aliasing：

\[
p_{m+2N}
=
e^{i\phi}p_m.
\]

Tao 已经利用这个观察到：

\[
\mathbf E_{\rm ACUE}
|\operatorname{tr}U^j|^2
=
\min_{k\in\mathbb Z}|j-2Nk|,
\]

所以 \(j>N\) 后直接偏离 CUE。

但 nonlinear dynamics 可以做一件 static linear Fourier observable 做不到的事：

\[
\text{low modes}
\xrightarrow{L}
\text{mode products}
\xrightarrow{L^r}
\text{total degree}\ge2N
\xrightarrow{\text{alias}}
\text{low mode again}.
\]

即

\[
\boxed{
\text{high-frequency defect}
\longrightarrow
\text{nonlinear aliasing}
\longrightarrow
\text{low-frequency observable}.
}
\]

这个机制非常像 signal processing 里的 frequency mixing。

这可能就是你寻找的：

> ACUE high-frequency defect 是否能够通过 zero dynamics 很快泄露到低频 observable？

我认为这是目前最清楚、最可计算的 formulation。

---

# 7. 甚至可以把它表成一个“ACUE dynamic instability conjecture”

我会先测试这样一个 finite-\(N\) conjecture。

设

\[
\mu_A=\mathrm{ACUE}_N,\qquad
\mu_C=\mathrm{CUE}_N.
\]

令 \(\Phi_t\) 为 circular Coulomb flow。

考虑 pushforward measure

\[
\mu_A^t=(\Phi_t)_*\mu_A,
\qquad
\mu_C^t=(\Phi_t)_*\mu_C.
\]

寻找一个低复杂度 observable \(F_N\)，例如

\[
F_N(U)=|\operatorname{tr}U^m|^2,
\qquad m=O(1),
\]

使得虽然

\[
\mathbf E_{\mu_A}F_N
=
\mathbf E_{\mu_C}F_N,
\]

但是存在

\[
t_N\to0
\]

满足

\[
\boxed{
\left|
\mathbf E_{\mu_A^{t_N}}F_N-
\mathbf E_{\mu_C^{t_N}}F_N
\right|
\gg1.
}
\]

最激进的版本是

\[
t_N\asymp N^{-2}
\]

这种 microscopic relaxation time。

如果成立，它说明：

> ACUE 只有 static camouflage，没有 dynamical camouflage。

---

# 8. 但需要特别小心：Rodgers–Tao flow 本身会趋向 arithmetic progression

这里有一个反直觉点。

Rodgers–Tao 的 zero flow **不是让 zeros 趋向 GUE**。

相反，在假设 \(\Lambda<0\) 后，足够长的 repulsive flow 会让它们趋向更 rigid 的 **local arithmetic progression**。这正是最终导致和 Montgomery statistics 冲突的地方。

而 ACUE 本身已经具有强 lattice structure。

所以如果我们只是问：

> “ACUE 在 Coulomb flow 下是否被破坏？”

答案未必。

甚至可能是：

\[
\mathrm{ACUE}
\rightarrow
\text{更加 rigid}.
\]

真正要看的不是 rigidity 本身。

而是：

\[
\boxed{
\text{ACUE 的 discrete lattice rigidity}
\quad\text{和}\quad
\text{zero-flow 产生的 continuous equilibrium rigidity}
}
\]

是不是兼容。

这是两个完全不同的 rigidity。

ACUE 要求：

\[
\Delta_j\in\frac1{2N}\mathbb Z.
\]

而 Coulomb equilibrium 要求局部 force balance：

\[
\sum_{j\ne k}
\frac1{x_k-x_j}\approx0.
\]

除非 configuration 真的是 arithmetic progression，否则两者一般冲突。

所以我们可以定义一个 **force defect**

\[
\boxed{
D(X)
=
\sum_k
\left|
\sum_{j\ne k}
\frac1{x_k-x_j}
\right|^2
}
\]

或者 circular version：

\[
D_{\rm circ}(X)
=
\sum_k
\left|
\sum_{j\ne k}
\cot\pi(\theta_k-\theta_j)
\right|^2.
\]

这可能就是最直接的 observable。

---

# 9. 甚至可以构造一个 Rodgers–Tao-style Lyapunov energy

Rodgers–Tao proof 真正有力量的部分不是 ODE 本身，而是他们控制一个 integrated local energy，然后证明它越来越小，最终逼近 classical locations / arithmetic progression。论文后半部分大量分析的正是这种 energy control。

我们可以为 ACUE 定义：

\[
E_{\rm force}(X)
=
\sum_k |V_k(X)|^2,
\]

或者 gap strain：

\[
E_{\rm gap}(X)
=
\sum_j
\left(
\frac{\Delta_j}{\bar\Delta}-1
\right)^2.
\]

然后研究：

\[
\frac{d}{dt}E(\Phi_t X).
\]

真正值得找的是一个 observable 满足：

\[
\boxed{
E_{\rm CUE}'(0)=O(1)
}
\]

但

\[
\boxed{
E_{\rm ACUE}'(0)\sim N^\alpha
}
\]

或者反过来。

那就得到一个 parametrically enhanced discriminator。

这比寻找一个 tiny static moment discrepancy 强得多。

---

# 10. 和我们已有的 ACOE counterexamples 怎么接

这里可能反而比 ACUE 更漂亮。

如果我们已经有一系列 **ACOE counterexamples**，它们保持了某些：

- rank；
- trace；
- low moments；
- Gram constraints；
- determinantal-type identities；

但沿某个 directional inverse-Gram / Schur complement 方向出现 pathological behavior，

那就可以给每个 counterexample \(X\) 加一个 deformation：

\[
X_t=X+tV(X)+O(t^2).
\]

然后研究我们之前的 calibrated pressure

\[
\Psi_N(\theta;X)
\]

沿这个 flow 的 response：

\[
\boxed{
\frac{d}{dt}
\Psi_N(\theta;X_t)\Big|_{t=0}
}
\]

和

\[
\boxed{
\frac{d^2}{dt^2}
\Psi_N(\theta;X_t)\Big|_{t=0}.
}
\]

这可能非常关键。

因为我们以前的反例证明的是：

\[
\text{static invariants}
\nRightarrow
\text{directional inverse control}.
\]

而 dynamics 本质上提供了一个 canonical direction \(V(X)\)。

于是问题变成：

\[
\boxed{
\text{static low-moment equivalence}
\nRightarrow
\text{dynamic response equivalence}.
}
\]

这个 statement 我觉得比原先 counterexample 本身更有数学结构。

---

# 11. 我会把计算项目分成四层

### Layer A — finite \(N\) exact symbolic

先做

\[
N=2,3,\dots,10.
\]

ACUE 可以 exact enumerate lattice subsets：

\[
\{k_1,\dots,k_N\}
\subset\mathbb Z/2N\mathbb Z
\]

用 Vandermonde-square weight。

然后 exact 计算

\[
\mathbf E_{\rm ACUE}L^r
|\operatorname{tr}U^m|^2
\]

对

\[
m=1,2,3,\qquad r=1,\dots,8.
\]

同时用 Selberg / Haar identities 算 CUE。

我们第一件要找的是：

\[
(r,m)
\]

最早在哪里 break。

---

### Layer B — generator algebra

符号化推导：

\[
Lp_m
\]

写成 power sums

\[
p_a p_b.
\]

然后自动生成

\[
L^rp_m.
\]

这其实非常适合 AI + symbolic algebra。

寻找：

\[
\text{degree growth},
\quad
\text{aliasing structure},
\quad
\text{first ACUE-sensitive term}.
\]

---

### Layer C — continuum asymptotics

证明：

\[
\mathbf E_{\rm ACUE}L^rF-
\mathbf E_{\rm CUE}L^rF
\]

的 asymptotic。

特别寻找：

\[
O(1),\quad N^\alpha,\quad e^{-cN}
\]

是哪种 scaling。

---

### Layer D — number theoretic lifting

最后才问：

是否存在 zeta-side deformation operator

\[
\mathcal L_\zeta
\]

使得这些 dynamic observables 可以写成 primes / Dirichlet-polynomial quantities。

这是最难的一步。

但是如果我们先发现一个 ridiculously simple observable，例如

\[
L^2|\operatorname{tr}U|^2,
\]

在 ACUE/CUE 之间已经不同，那么就可以 reverse engineer 它对应到 zeta 的什么 quantity。

---

# 12. 这条路线最大的潜在 payoff

Tao 在 2019 年指出，static pair correlation 如果想直接打掉 Alternative Hypothesis，你至少需要突破到相当于

\[
j>N
\]

的区间，而这已经接近 averaged Hardy–Littlewood with power-saving，现有技术非常难。

所以真正理想的结果不是：

\[
\text{再找到一个 }j>N\text{ observable}.
\]

而是证明：

\[
\boxed{
\text{nonlinear dynamics converts inaccessible }
j>N
\text{ information into accessible }j<N
\text{ response}.
}
\]

这才会改变 problem difficulty。

可以把整个目标压成一句：

\[
\boxed{
\textbf{Does ACUE remain indistinguishable from CUE under infinitesimal Coulomb evolution?}
}
\]

如果答案是 **no already at bounded dynamic order \(r\)**，那就非常值得追。

而且它和 Rodgers–Tao 的思想不是表面类比，而是很精确的同一种机制：

\[
\text{bad adversarial state}
\rightarrow
\text{evolve under canonical dynamics}
\rightarrow
\text{hidden rigidity becomes amplified}
\rightarrow
\text{low-complexity observable detects contradiction}.
\]

我认为我们下一步最应该做的，不是继续抽象讨论，而是直接把 **ACUE finite-\(N\) generator \(L\)** 写出来，然后 exact enumerate \(N\le10\)，计算

\[
L^r|\operatorname{tr}U^m|^2
\]

到底第几个 \(r\) 开始 distinguish CUE/ACUE。这个实验很便宜，却能直接判断这条路线究竟是“漂亮类比”还是有真正的新 obstruction。