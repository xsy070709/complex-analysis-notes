# 第六章 分式线性变换与共形映射

## 6.1 扩充复平面与几何背景

### 6.1.1 扩充复平面与广义圆

在复平面 $\mathbb C$ 中添入一个无穷远点，得到扩充复平面

$$
\widehat{\mathbb C}=\mathbb C\cup\{\infty\}.
$$

这里的 $\infty$ 是一个点。复数沿任意方向趋于无穷大，在扩充复平面中都表示趋于同一个无穷远点。

扩充复平面可以通过球极投影与一个球面建立一一对应，称为 **Riemann 球面**。球面上选定的投影极点对应于 $\infty$，其余各点对应于有限复数。

**定义（广义圆）。** 扩充复平面上的广义圆，是指通常的圆，或一条直线连同无穷远点。因此，直线可以看成经过 $\infty$ 的广义圆。

在球极投影下，球面与平面的这种对应将球面上的圆对应为平面中的广义圆：经过投影极点的圆对应于直线，不经过投影极点的圆对应于通常的圆。

### 6.1.2 平面几何与曲面几何

在 Euclid 平面几何中，两点间的最短曲线是线段。过一条直线外的一点，有且只有一条直线与已知直线平行，这是平行公设的一种等价表述。在通常的 Euclid 几何公理体系中，平行公设也与三角形内角和等于 $\pi$ 相联系。

在曲面上，研究曲面内的距离与最短曲线时，需要使用曲面自身的几何结构。**测地线**是“直线”概念在曲面上的推广；足够短的测地线段具有局部最短性质。

以球面为例：

- 球面上的测地线是大圆，即球面与经过球心的平面相交得到的圆。
- 非对径的两点之间，较短的大圆弧给出最短路径。
- 对径两点之间有无穷多条最短半大圆弧。
- 两个不同的大圆总在一对对径点处相交。

例如，在单位球面上，北极与赤道上相差 $90^\circ$ 的两点构成的球面三角形，其三个内角均为 $\pi/2$，故内角和为

$$
\frac{3\pi}{2}>\pi.
$$

Riemann 球面把有限点与无穷远点统一起来。将球面用作扩充复平面的复结构模型，与在球面上研究大圆距离，是两个不同层面的几何问题。

## 6.2 分式线性变换的定义与基本性质

### 6.2.1 定义及无穷远点处的取值

**定义（分式线性变换）。** 形如

$$
\boxed{w=T(z)=\frac{az+b}{cz+d},\qquad ad-bc\ne0}
$$

的变换称为分式线性变换，也称 Möbius 变换，其中 $a,b,c,d\in\mathbb C$。

条件 $ad-bc\ne0$ 保证变换不是常值映射。若系数矩阵奇异且分母不是恒等于零，则分子与分母成比例，在分母不为零处所得的是常值函数。

若 $c\ne0$，则定义

$$
T\!\left(-\frac dc\right)=\infty,
\qquad T(\infty)=\frac ac.
$$

由于

$$
a\left(-\frac dc\right)+b=\frac{bc-ad}{c}\ne0,
$$

分子与分母不会在极点处同时为零。

若 $c=0$，则由 $ad\ne0$ 可知 $a,d\ne0$，从而

$$
T(z)=\frac adz+\frac bd,\qquad T(\infty)=\infty.
$$

所以分式线性变换自然定义在整个扩充复平面上。

### 6.2.2 系数的比例不唯一性与矩阵表示

对任意 $\lambda\ne0$，有

$$
\frac{az+b}{cz+d}
=\frac{\lambda az+\lambda b}{\lambda cz+\lambda d}.
$$

因此，系数四元组 $(a,b,c,d)$ 与 $(\lambda a,\lambda b,\lambda c,\lambda d)$ 表示同一个变换。

用矩阵表示时，记

$$
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad \det M=ad-bc\ne0.
$$

则 $M$ 与 $\lambda M$ 表示同一个分式线性变换。

可以选择 $\lambda$，使归一化后的矩阵满足 $\det(\lambda M)=1$。事实上，

$$
\det(\lambda M)=\lambda^2(ad-bc),
$$

故只需取

$$
\lambda^2=\frac1{ad-bc},
\qquad \lambda=\pm\frac1{\sqrt{ad-bc}}.
$$

归一化后，$M$ 与 $-M$ 仍表示同一个变换。

### 6.2.3 逆变换与一一对应性

由

$$
w=\frac{az+b}{cz+d}
$$

得到

$$
cwz+dw=az+b,\qquad (cw-a)z=b-dw.
$$

所以

$$
\boxed{z=T^{-1}(w)=\frac{dw-b}{a-cw}.}
$$

逆变换的系数矩阵可以取为

$$
\begin{pmatrix}d&-b\\-c&a\end{pmatrix},
$$

其行列式仍为 $ad-bc\ne0$。

因此，分式线性变换是 $\widehat{\mathbb C}$ 到自身的一一对应。

### 6.2.4 导数与共形性

在有限的非极点处，

$$
\begin{aligned}
T'(z)
&=\frac{a(cz+d)-c(az+b)}{(cz+d)^2}\\
&=\boxed{\frac{ad-bc}{(cz+d)^2}}\ne0.
\end{aligned}
$$

所以分式线性变换在每个有限的非极点处都是共形的，即保持有向夹角。局部长度伸缩比例为 $|T'(z)|$，局部旋转角为 $\arg T'(z)$。

在极点与无穷远点附近，应改用合适的局部坐标。

若 $c\ne0$，在极点 $p=-d/c$ 处使用目标坐标 $1/w$，则

$$
\frac1{T(z)}=\frac{cz+d}{az+b},
\qquad
\left(\frac1T\right)'(p)=-\frac{c^2}{ad-bc}\ne0.
$$

在源点 $\infty$ 处令 $\zeta=1/z$，则

$$
T(1/\zeta)=\frac{a+b\zeta}{c+d\zeta},
\qquad
\left.\frac{d}{d\zeta}T(1/\zeta)\right|_{\zeta=0}
=\frac{bc-ad}{c^2}\ne0.
$$

若 $c=0$，源点和像点均为 $\infty$，同时使用 $\zeta=1/z$ 与 $\eta=1/w$，有

$$
\eta=\frac{d\zeta}{a+b\zeta},
\qquad \eta'(0)=\frac da\ne0.
$$

因此，分式线性变换是整个 Riemann 球面上的共形自同构。

## 6.3 复合、矩阵表示与变换群

设

$$
T_1(z)=\frac{a_1z+b_1}{c_1z+d_1},
\qquad T_2(z)=\frac{a_2z+b_2}{c_2z+d_2}.
$$

则

$$
\begin{aligned}
T_2(T_1(z))
&=\frac{a_2\frac{a_1z+b_1}{c_1z+d_1}+b_2}
{c_2\frac{a_1z+b_1}{c_1z+d_1}+d_2}\\
&=\frac{(a_2a_1+b_2c_1)z+(a_2b_1+b_2d_1)}
{(c_2a_1+d_2c_1)z+(c_2b_1+d_2d_1)}.
\end{aligned}
$$

若记

$$
T_2\circ T_1(z)=\frac{Az+B}{Cz+D},
$$

则

$$
\begin{pmatrix}A&B\\C&D\end{pmatrix}
=\begin{pmatrix}a_2&b_2\\c_2&d_2\end{pmatrix}
\begin{pmatrix}a_1&b_1\\c_1&d_1\end{pmatrix}.
$$

注意复合的顺序：

$$
\boxed{T_2\circ T_1\ \longleftrightarrow\ M_2M_1.}
$$

并且

$$
AD-BC=(a_2d_2-b_2c_2)(a_1d_1-b_1c_1)\ne0,
$$

所以复合后仍是分式线性变换。

全体分式线性变换在复合运算下构成一个群：复合满足结合律，恒等变换 $I(z)=z$ 是单位元，每个变换都有分式线性逆变换。

这个群通常不交换。例如，取

$$
T_1(z)=z+1,\qquad T_2(z)=2z,
$$

则

$$
T_2(T_1(z))=2z+2,
\qquad T_1(T_2(z))=2z+1.
$$

因此 $T_2\circ T_1\ne T_1\circ T_2$。

## 6.4 三种基本变换及其几何意义

### 6.4.1 平移

设

$$
w=z+\beta,\qquad \beta=\beta_1+i\beta_2.
$$

若 $z=x+iy$、$w=x'+iy'$，则

$$
x'=x+\beta_1,\qquad y'=y+\beta_2,
$$

即

$$
\begin{pmatrix}x'\\y'\end{pmatrix}
=\begin{pmatrix}x\\y\end{pmatrix}
+\begin{pmatrix}\beta_1\\\beta_2\end{pmatrix}.
$$

这就是沿向量 $(\beta_1,\beta_2)$ 的平移。平移保持距离、角度、圆和直线，并固定无穷远点。其分式线性系数矩阵可取

$$
\begin{pmatrix}1&\beta\\0&1\end{pmatrix}.
$$

### 6.4.2 旋转与伸缩

设

$$
w=\alpha z,\qquad \alpha\ne0.
$$

写成极坐标形式

$$
\alpha=\rho e^{i\varphi},\qquad z=re^{i\theta},
\qquad \rho=|\alpha|>0,
$$

则

$$
w=\rho r e^{i(\theta+\varphi)}.
$$

因此，该变换是以原点为中心按比例 $\rho$ 伸缩，再绕原点旋转角 $\varphi$：$\rho>1$ 表示放大，$0<\rho<1$ 表示缩小。其分式线性系数矩阵可取

$$
\begin{pmatrix}\alpha&0\\0&1\end{pmatrix}.
$$

特别地，当 $\alpha=e^{i\varphi}$ 时，$w=e^{i\varphi}z$ 是纯旋转。在实坐标下，

$$
\begin{pmatrix}x'\\y'\end{pmatrix}
=R_\varphi\begin{pmatrix}x\\y\end{pmatrix},
\qquad
R_\varphi=\begin{pmatrix}
\cos\varphi&-\sin\varphi\\
\sin\varphi&\cos\varphi
\end{pmatrix}.
$$

这里的实坐标旋转矩阵与表示分式线性系数的复矩阵，作用对象不同。旋转矩阵满足

$$
R_\varphi^{-1}=R_\varphi^{\mathsf T}=R_{-\varphi}.
$$

### 6.4.3 倒数变换

考虑

$$
w=\frac1z.
$$

若 $z=re^{i\theta}$，则

$$
\boxed{w=\frac1r e^{-i\theta}.}
$$

所以 $r\mapsto1/r$，$\theta\mapsto-\theta$。它可以看成先作关于单位圆的反演，再作关于实轴的反射：

$$
z\longmapsto\frac1{\bar z}\longmapsto\frac1z.
$$

由此得到：

- $0$ 与 $\infty$ 互换；
- 单位圆内部与外部互换；
- 单位圆上的点映为其共轭点；
- 上半平面与下半平面互换。

需要区分 $1/z$ 与 $1/\bar z$：前者是解析的分式线性变换，后者是含有共轭运算的圆反演。倒数变换虽然可分解为两个反向变换，但其复合保持有向夹角。

倒数变换的系数矩阵可取

$$
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

### 6.4.4 一般分式线性变换的分解

若 $c=0$，则

$$
T(z)=\frac adz+\frac bd,
$$

由旋转伸缩和平移组成。

若 $c\ne0$，则

$$
\begin{aligned}
T(z)&=\frac{az+b}{cz+d}\\
&=\frac ac+\frac{bc-ad}{c(cz+d)}\\
&=\boxed{\frac ac+\frac{bc-ad}{c^2}\frac1{z+d/c}}.
\end{aligned}
$$

由于 $(bc-ad)/c^2\ne0$，该变换可以依次分解为

$$
\begin{aligned}
z_1&=z+\frac dc,\\
z_2&=\frac1{z_1},\\
z_3&=\frac{bc-ad}{c^2}z_2,\\
w&=z_3+\frac ac.
\end{aligned}
$$

因此，任意分式线性变换都可由有限次平移、旋转伸缩与倒数变换复合而成。

## 6.5 分式线性变换的不动点

### 6.5.1 不动点与周期点

**定义（不动点）。** 若 $T(z_0)=z_0$，则称 $z_0$ 为 $T$ 的不动点。

更一般地，若存在正整数 $n$，使

$$
T^{\circ n}(z_0)=z_0,
$$

则称 $z_0$ 为周期点。满足该式的最小正整数称为最小周期。不动点就是最小周期为 $1$ 的周期点。

### 6.5.2 有限不动点方程

设 $T(z)=(az+b)/(cz+d)$。有限不动点满足

$$
z=\frac{az+b}{cz+d},
$$

从而

$$
\boxed{cz^2+(d-a)z-b=0.}
$$

当 $c\ne0$ 时，极点 $-d/c$ 不是上述方程的根，因为

$$
c\left(-\frac dc\right)^2
+(d-a)\left(-\frac dc\right)-b
=\frac{ad-bc}{c}\ne0.
$$

所以交叉相乘不会引入极点作为增根。

### 6.5.3 不动点个数的分类

**一、$c=0$。** 此时 $a,d\ne0$，且 $\infty$ 是不动点。有限不动点方程为

$$
(d-a)z=b.
$$

若 $d-a\ne0$，则有唯一有限不动点

$$
z=\frac b{d-a}.
$$

连同 $\infty$，共有两个不同的不动点。

若 $d-a=0$ 且 $b\ne0$，则 $T(z)=z+b/d$ 为非平凡平移。此时无有限不动点，在扩充复平面上只有一个不动点 $\infty$。

若 $d-a=0$ 且 $b=0$，则 $T(z)=z$ 为恒等变换，所有点都是不动点。

**二、$c\ne0$。** 由于 $T(\infty)=a/c\ne\infty$，无穷远点不是不动点。令

$$
\Delta=(d-a)^2+4bc.
$$

若 $\Delta\ne0$，有两个不同的有限不动点

$$
\boxed{z_\pm=\frac{a-d\pm\sqrt{(d-a)^2+4bc}}{2c}.}
$$

若 $\Delta=0$，有唯一的不动点

$$
\boxed{z_0=\frac{a-d}{2c},}
$$

它是二次方程的二重根。

综上：

| 变换条件 | 有限不动点个数 | 扩充复平面上的不同不动点个数 |
| --- | ---: | ---: |
| $c=0,\ a\ne d$ | $1$ | $2$ |
| $c=0,\ a=d,\ b\ne0$ | $0$ | $1$ |
| $c\ne0,\ \Delta\ne0$ | $2$ | $2$ |
| $c\ne0,\ \Delta=0$ | $1$ | $1$ |
| 恒等变换 | 无穷多 | 所有点 |

**结论。** 非恒等的分式线性变换，在扩充复平面上恰有一个或两个不同的不动点。若一个分式线性变换固定三个不同的点，则它必为恒等变换。

### 6.5.4 三点决定唯一性

若两个分式线性变换 $T_1,T_2$ 在三个不同的点 $z_1,z_2,z_3$ 处取相同的值，则 $T_2^{-1}\circ T_1$ 固定这三个点，因而是恒等变换。所以

$$
\boxed{T_1=T_2.}
$$

特别地，若

$$
T(0)=0,\qquad T(1)=1,\qquad T(\infty)=\infty,
$$

则 $T(z)=z$。也可直接验证：由 $T(\infty)=\infty$ 得 $c=0$，由 $T(0)=0$ 得 $b=0$，再由 $T(1)=1$ 得 $a=d$。

## 6.6 保圆性

### 6.6.1 广义圆的统一方程

圆或直线可以统一写成

$$
\boxed{
A z\bar z+Bz+\bar B\bar z+C=0,
\qquad A,C\in\mathbb R,\ B\in\mathbb C
}.
$$

对于非退化广义圆，要求 $|B|^2-AC>0$。

若 $A\ne0$，配方得

$$
\left|z+\frac{\bar B}{A}\right|^2
=\frac{|B|^2-AC}{A^2},
$$

表示一个圆。

若 $A=0$，则 $B\ne0$，方程成为

$$
Bz+\bar B\bar z+C=0,
\qquad 2\operatorname{Re}(Bz)+C=0,
$$

表示一条直线。

### 6.6.2 倒数变换的保圆性

平移与旋转伸缩显然将圆或直线映成圆或直线。下面考察 $w=1/z$。

将 $z=1/w$、$\bar z=1/\bar w$ 代入广义圆方程，得

$$
\frac A{w\bar w}+\frac B w+\frac{\bar B}{\bar w}+C=0.
$$

乘以 $w\bar w$，得到

$$
\boxed{Cw\bar w+\bar B w+B\bar w+A=0,}
$$

它仍是广义圆方程，其非退化条件仍为 $|B|^2-AC>0$。

原广义圆经过 $z=0$ 当且仅当 $C=0$。此时像方程没有 $w\bar w$ 项，因此像为直线；原广义圆不经过 $0$ 时，$C\ne0$，像为通常的圆。

在 $0,\infty$ 处的对应按扩充复平面的意义理解。

### 6.6.3 一般分式线性变换的保圆性

**定理（保圆性）。** 分式线性变换把广义圆映成广义圆。

**证明。** 任意分式线性变换都可以分解成平移、旋转伸缩和倒数变换。这三类基本变换都保持广义圆，所以它们的复合也保持广义圆。证毕。

若 $c\ne0$，极点为 $p=-d/c$。由于 $T(p)=\infty$，且直线是经过 $\infty$ 的广义圆，所以

$$
\boxed{
\begin{aligned}
&\text{原广义圆经过极点}
&&\Longleftrightarrow\ \text{像为直线};\\
&\text{原广义圆不经过极点}
&&\Longleftrightarrow\ \text{像为通常的圆}.
\end{aligned}}
$$

保圆性确定的是边界的像。要确定圆内部或外部映到哪一侧，还可取区域内一点，计算其像所在的位置。

## 6.7 关于圆的对称与对称性保持

### 6.7.1 关于直线的对称

关于实轴对称的两点满足 $z^*=\bar z$。

关于经过 $z_0$、方向角为 $\varphi$ 的直线，对称变换为

$$
\boxed{z^*=z_0+e^{2i\varphi}\overline{z-z_0}.}
$$

它可以通过“先平移到原点、旋转到实轴、取共轭，再作逆变换”得到。

### 6.7.2 关于圆的对称及其公式

设

$$
C:\ |z-z_0|=r,\qquad r>0.
$$

**定义。** 对于 $z\ne z_0$，若 $z^*$ 与 $z$ 位于从 $z_0$ 出发的同一条射线上，且

$$
|z-z_0|\,|z^*-z_0|=r^2,
$$

则称 $z^*$ 是 $z$ 关于圆 $C$ 的对称点。

由同射线条件，可设

$$
z^*-z_0=\lambda(z-z_0),\qquad \lambda>0.
$$

取模并利用距离乘积条件，得到

$$
\lambda|z-z_0|^2=r^2,
\qquad \lambda=\frac{r^2}{|z-z_0|^2}.
$$

于是

$$
\begin{aligned}
z^*&=z_0+\frac{r^2(z-z_0)}{|z-z_0|^2}\\
&=z_0+\frac{r^2(z-z_0)}{(z-z_0)(\bar z-\bar z_0)}.
\end{aligned}
$$

因此

$$
\boxed{z^*=z_0+\frac{r^2}{\bar z-\bar z_0}.}
$$

在扩充复平面上，补充规定 $z_0^*=\infty$、$\infty^*=z_0$。

该对称变换将圆内与圆外互换，圆周上的点保持不动；连续作两次对称回到原点，即 $(z^*)^*=z$。

特别地，对于单位圆 $|z|=1$，

$$
\boxed{z^*=\frac1{\bar z}.}
$$

### 6.7.3 分式线性变换保持广义圆对称性

**定理（对称性保持）。** 若 $z,z^*$ 关于广义圆 $C$ 对称，$T$ 是分式线性变换，则 $T(z),T(z^*)$ 关于像广义圆 $T(C)$ 对称。

**证明。** 先把关于圆的对称化为关于实轴的对称。对于圆 $C:|z-z_0|=r$，令

$$
u=\frac{z-z_0}{r},\qquad P(z)=i\frac{1+u}{1-u}.
$$

变换 $P$ 将 $C$ 映为实轴连同无穷远点。由 $u^*=1/\bar u$，可验证

$$
\begin{aligned}
P(z^*)&=i\frac{1+1/\bar u}{1-1/\bar u}
=-i\frac{1+\bar u}{1-\bar u}
=\overline{P(z)}.
\end{aligned}
$$

对于直线，也可用平移和旋转得到同样的关系。

再取分式线性变换 $Q$，将 $T(C)$ 映为扩充实轴，并使关于 $T(C)$ 的对称对应于共轭。令

$$
H=Q\circ T\circ P^{-1}.
$$

则 $H$ 将扩充实轴映到自身。考虑

$$
\widetilde H(\zeta)=\overline{H(\bar\zeta)}.
$$

它仍是分式线性变换。在实轴上避开极点取三个不同的有限点，由于 $H$ 在这些点取实值，有 $\widetilde H(\zeta)=H(\zeta)$。由三点决定唯一性，$\widetilde H=H$，所以

$$
H(\bar\zeta)=\overline{H(\zeta)}.
$$

取 $\zeta=P(z)$，结合 $P(z^*)=\overline{P(z)}$，得到

$$
Q(T(z^*))=\overline{Q(T(z))}.
$$

这恰好表示 $T(z^*)$ 与 $T(z)$ 关于 $T(C)$ 对称。各特殊点的关系由连续延拓成立。证毕。

这一性质可用于确定零点与极点：若某圆被映为单位圆，且圆内点 $z_1$ 被映为 $0$，则它关于原圆的对称点必被映为 $\infty$。

## 6.8 单位圆盘到自身的分式线性映射

记

$$
\mathbb D=\{z\in\mathbb C:|z|<1\}.
$$

这里“将单位圆盘映为单位圆盘”是指将 $\mathbb D$ 一一映到整个 $\mathbb D$。这样的映射称为单位圆盘的分式线性自同构。仅要求像包含于单位圆盘时，结论不同；例如 $w=z/2$ 将单位圆盘映入自身，但不是满射。

### 6.8.1 一般形式的推导

设 $T$ 是单位圆盘到自身的分式线性自同构。因为 $0\in\mathbb D$，存在唯一的 $z_1\in\mathbb D$，使

$$
T(z_1)=0.
$$

分式线性变换是球面同胚，因此将单位圆盘的边界映为单位圆周。

先设 $z_1\ne0$。它关于单位圆的对称点为

$$
z_2=\frac1{\bar z_1}.
$$

由于 $0$ 关于单位圆的对称点为 $\infty$，由对称性保持，

$$
T(z_2)=\infty.
$$

所以

$$
T(z)=\alpha\frac{z-z_1}{z-z_2},\qquad \alpha\ne0.
$$

这也可由一般形式直接看出：有限零点给出 $z_1=-b/a$，有限极点给出 $z_2=-d/c$，于是 $T(z)=(a/c)(z-z_1)/(z-z_2)$。

代入 $z_2=1/\bar z_1$，有

$$
\begin{aligned}
T(z)&=\alpha\frac{z-z_1}{z-1/\bar z_1}\\
&=-\alpha\bar z_1\frac{z-z_1}{1-\bar z_1z}\\
&=\beta\frac{z-z_1}{1-\bar z_1z},
\end{aligned}
$$

其中 $\beta=-\alpha\bar z_1$。

当 $|z|=1$ 时，$\bar z=1/z$，从而

$$
1-\bar z_1z=z(\bar z-\bar z_1)
=z\,\overline{z-z_1}.
$$

所以

$$
|1-\bar z_1z|=|z-z_1|.
$$

又因边界上 $|T(z)|=1$，得到

$$
1=|\beta|\frac{|z-z_1|}{|1-\bar z_1z|}=|\beta|.
$$

于是 $\beta=e^{i\theta}$，其中 $\theta\in\mathbb R$。

若 $z_1=0$，则对称性保持给出 $T(\infty)=\infty$，所以 $T(z)=\beta z$。由单位圆周映为自身得 $|\beta|=1$，仍包含在同一公式中。

**定理（单位圆盘的分式线性自同构）。** 将单位圆盘一一映为自身的分式线性变换的一般形式为

$$
\boxed{
w=e^{i\theta}\frac{z-z_1}{1-\bar z_1z},
\qquad |z_1|<1,\quad 0\le\theta<2\pi
}.
$$

其中 $z_1$ 是被映到原点的点。

### 6.8.2 公式的充分性验证

设

$$
w=e^{i\theta}\frac{z-z_1}{1-\bar z_1z},\qquad |z_1|<1.
$$

当 $|z|\le1$ 时，$|\bar z_1z|<1$，故分母不为零。

计算

$$
\begin{aligned}
&|1-\bar z_1z|^2-|z-z_1|^2\\
&=(1-\bar z_1z)(1-z_1\bar z)
 -(z-z_1)(\bar z-\bar z_1)\\
&=1-\bar z_1z-z_1\bar z+|z_1|^2|z|^2\\
&\quad-|z|^2+z\bar z_1+\bar z z_1-|z_1|^2\\
&=(1-|z_1|^2)(1-|z|^2).
\end{aligned}
$$

因此

$$
\boxed{
1-|w|^2=
\frac{(1-|z_1|^2)(1-|z|^2)}{|1-\bar z_1z|^2}
}.
$$

当 $|z|<1$ 时，右端为正，所以 $|w|<1$。

为证明满射，令 $\eta=e^{-i\theta}w$。由

$$
\eta=\frac{z-z_1}{1-\bar z_1z}
$$

解得

$$
\boxed{
z=\frac{\eta+z_1}{1+\bar z_1\eta}
=\frac{e^{-i\theta}w+z_1}{1+\bar z_1e^{-i\theta}w}
}.
$$

将前面的模平方恒等式中的参数换为 $-z_1$，得

$$
1-|z|^2
=\frac{(1-|z_1|^2)(1-|\eta|^2)}{|1+\bar z_1\eta|^2}>0
\qquad (|w|<1).
$$

所以逆变换也将单位圆盘映入自身，原变换确实将单位圆盘一一映为自身。

其系数可以取为

$$
a=e^{i\theta},\quad b=-e^{i\theta}z_1,
\quad c=-\bar z_1,\quad d=1,
$$

且

$$
ad-bc=e^{i\theta}(1-|z_1|^2)\ne0.
$$

### 6.8.3 固定原点的圆盘自同构

若还要求 $T(0)=0$，则一般形式中的 $z_1=0$，从而

$$
\boxed{T(z)=e^{i\theta}z.}
$$

因此，固定原点的单位圆盘分式线性自同构都是绕原点的旋转。

## 6.9 单位圆盘上的微分不变式

### 6.9.1 定理及完整证明

**定理。** 设

$$
w=e^{i\theta}\frac{z-z_1}{1-\bar z_1z},\qquad |z_1|<1.
$$

则在单位圆盘内，

$$
\boxed{\frac{|dw|}{1-|w|^2}=\frac{|dz|}{1-|z|^2}.}
$$

这里 $|dw|=|w'(z)|\,|dz|$，等式表示相应线元在圆盘自同构下保持不变。

**证明。** 首先求导：

$$
\begin{aligned}
\frac{dw}{dz}
&=e^{i\theta}
\frac{(1-\bar z_1z)+\bar z_1(z-z_1)}{(1-\bar z_1z)^2}\\
&=e^{i\theta}\frac{1-|z_1|^2}{(1-\bar z_1z)^2}.
\end{aligned}
$$

取模得

$$
\boxed{\left|\frac{dw}{dz}\right|
=\frac{1-|z_1|^2}{|1-\bar z_1z|^2}.}
$$

另一方面，

$$
\begin{aligned}
1-|w|^2
&=1-\frac{|z-z_1|^2}{|1-\bar z_1z|^2}\\
&=\frac{|1-\bar z_1z|^2-|z-z_1|^2}{|1-\bar z_1z|^2}\\
&=\frac{(1-|z|^2)(1-|z_1|^2)}{|1-\bar z_1z|^2}.
\end{aligned}
$$

所以

$$
\boxed{
\frac{1-|w|^2}{1-|z|^2}
=\frac{1-|z_1|^2}{|1-\bar z_1z|^2}
=\left|\frac{dw}{dz}\right|
}.
$$

再乘以 $|dz|$ 并整理，得到

$$
\frac{|dw|}{1-|w|^2}=\frac{|dz|}{1-|z|^2}.
$$

证毕。

### 6.9.2 几何意义

单位圆盘上的线元

$$
ds=\frac{|dz|}{1-|z|^2}
$$

在所有圆盘分式线性自同构下保持不变。对分段光滑曲线 $\gamma$，相应长度

$$
L(\gamma)=\int_\gamma\frac{|dz|}{1-|z|^2}
$$

满足 $L(T(\gamma))=L(\gamma)$。

这一线元给出圆盘上的一种双曲度量。常用的另一种归一化是

$$
ds_{\mathrm{hyp}}=\frac{2|dz|}{1-|z|^2},
$$

它同样满足不变性。

## 6.10 一般圆盘之间的分式线性映射

### 6.10.1 题目

设

$$
D=\{z:|z-z_0|<r\},\qquad
G=\{w:|w-w_0|<R\},
$$

其中 $r,R>0$。给定 $z_1\in D$，即 $|z_1-z_0|<r$，求将 $D$ 一一映为 $G$，并满足 $w(z_1)=w_0$ 的分式线性映射的一般形式。

### 6.10.2 归一化推导

先把源圆盘化为单位圆盘：

$$
\zeta=\frac{z-z_0}{r}.
$$

于是 $z_1$ 对应于

$$
\zeta_1=\frac{z_1-z_0}{r},\qquad |\zeta_1|<1.
$$

再把目标圆盘化为单位圆盘：

$$
\eta=\frac{w-w_0}{R}.
$$

条件 $w(z_1)=w_0$ 等价于 $\eta(\zeta_1)=0$，因此

$$
\eta=e^{i\theta}\frac{\zeta-\zeta_1}{1-\bar\zeta_1\zeta}.
$$

代回原变量，

$$
\frac{w-w_0}{R}
=e^{i\theta}
\frac{\frac{z-z_0}{r}-\frac{z_1-z_0}{r}}
{1-\frac{\overline{z_1-z_0}}r\frac{z-z_0}r}.
$$

化简得

$$
\boxed{
w=w_0+
\frac{e^{i\theta}rR(z-z_1)}
{r^2-\overline{(z_1-z_0)}(z-z_0)},
\qquad 0\le\theta<2\pi
}.
$$

### 6.10.3 条件验证及特殊情形

当 $|z-z_0|<r$ 时，

$$
\left|\overline{(z_1-z_0)}(z-z_0)\right|<r^2,
$$

所以分母不为零。在 $z=z_1$ 处，

$$
r^2-\overline{(z_1-z_0)}(z_1-z_0)
=r^2-|z_1-z_0|^2>0,
$$

故 $w(z_1)=w_0$。

整个映射由源圆盘归一化、单位圆盘自同构及目标圆盘的逆归一化复合而成，因此确实将 $D$ 一一映为 $G$。

反过来，任一满足条件的分式线性映射，经上述源、目标归一化后，都是将 $\zeta_1$ 映为 $0$ 的单位圆盘自同构，故一定具有上述形式。这说明公式同时给出了全部解。

特别地，若 $z_1=z_0$，公式化为

$$
\boxed{w=w_0+\frac Rr e^{i\theta}(z-z_0).}
$$

所以把源圆心映为目标圆心的圆盘间分式线性映射，只需旋转、按比例 $R/r$ 伸缩，再平移到目标圆心。

### 6.10.4 极点与圆对称

若 $z_1\ne z_0$，上述变换的极点满足

$$
r^2-\overline{(z_1-z_0)}(z-z_0)=0,
$$

即

$$
\boxed{z=z_0+\frac{r^2}{\overline{z_1-z_0}}.}
$$

这正是 $z_1$ 关于源圆周 $|z-z_0|=r$ 的对称点。

在目标平面中，$w_0$ 关于目标圆周 $|w-w_0|=R$ 的对称点是 $\infty$。因此

$$
z_1\longmapsto w_0,\qquad z_1^*\longmapsto\infty,
$$

与分式线性变换保持广义圆对称性的结论一致。

### 6.10.5 一般圆盘之间的微分不变式

设 $w=T(z)$ 将 $|z-z_0|<r$ 一一映为 $|w-w_0|<R$。令

$$
\zeta=\frac{z-z_0}{r},\qquad
\eta=\frac{w-w_0}{R}.
$$

在归一化坐标中，这是单位圆盘到自身的分式线性自同构。因此

$$
\frac{|d\eta|}{1-|\eta|^2}
=\frac{|d\zeta|}{1-|\zeta|^2}.
$$

由于 $r,R$ 是正常数，

$$
|d\zeta|=\frac{|dz|}{r},\qquad
|d\eta|=\frac{|dw|}{R},
$$

代入得

$$
\frac{|dw|/R}{1-|w-w_0|^2/R^2}
=\frac{|dz|/r}{1-|z-z_0|^2/r^2}.
$$

也就是

$$
\boxed{
\frac{R|dw|}{R^2-|w-w_0|^2}
=\frac{r|dz|}{r^2-|z-z_0|^2}
}.
$$

等价的导数形式为

$$
\boxed{
|T'(z)|
=\frac Rr
\frac{1-|w-w_0|^2/R^2}{1-|z-z_0|^2/r^2}
=\frac rR
\frac{R^2-|w-w_0|^2}{r^2-|z-z_0|^2}
}.
$$

其中的半径因子来自源、目标坐标的伸缩。

还可由映射公式直接求导。记

$$
\delta=z_1-z_0,\qquad
D(z)=r^2-\bar\delta(z-z_0).
$$

由

$$
T(z)=w_0+e^{i\theta}rR\frac{z-z_1}{D(z)},
$$

可得

$$
\begin{aligned}
T'(z)
&=e^{i\theta}rR
\frac{D(z)+\bar\delta(z-z_1)}{D(z)^2}\\
&=e^{i\theta}rR
\frac{r^2-\bar\delta(z-z_0)+\bar\delta(z-z_1)}{D(z)^2}\\
&=\boxed{
e^{i\theta}rR
\frac{r^2-|z_1-z_0|^2}
{\left[r^2-\overline{(z_1-z_0)}(z-z_0)\right]^2}
}.
\end{aligned}
$$

所以

$$
|T'(z)|
=\frac{rR\left(r^2-|z_1-z_0|^2\right)}
{\left|r^2-\overline{(z_1-z_0)}(z-z_0)\right|^2}.
$$

另一方面，归一化的模平方恒等式给出

$$
1-\frac{|w-w_0|^2}{R^2}
=\frac{
\left(r^2-|z_1-z_0|^2\right)
\left(r^2-|z-z_0|^2\right)
}{\left|r^2-\overline{(z_1-z_0)}(z-z_0)\right|^2}.
$$

将这两个等式相比较，也可得到上述导数形式及微分不变式。

## 6.11 上半平面到单位圆盘的分式线性映射

### 6.11.1 零点、极点与一般形式

记上半平面为

$$
\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\}.
$$

给定 $z_0\in\mathbb H$，求将 $\mathbb H$ 一一映为单位圆盘，并满足 $T(z_0)=0$ 的分式线性映射。

源区域的边界是实轴连同无穷远点，目标区域的边界是单位圆周。$z_0$ 关于实轴的对称点是 $\bar z_0$；$0$ 关于单位圆的对称点是 $\infty$。由对称性保持，

$$
T(\bar z_0)=\infty.
$$

所以零点是 $z_0$，极点是 $\bar z_0$，变换必为

$$
w=\alpha\frac{z-z_0}{z-\bar z_0},\qquad \alpha\ne0.
$$

对任意实数 $x$，有

$$
\overline{x-z_0}=x-\bar z_0,
\qquad |x-z_0|=|x-\bar z_0|.
$$

由于实轴映为单位圆周，

$$
1=|T(x)|
=|\alpha|\frac{|x-z_0|}{|x-\bar z_0|}
=|\alpha|.
$$

于是 $\alpha=e^{i\theta}$。

**定理。** 将上半平面一一映为单位圆盘，且将 $z_0\in\mathbb H$ 映为原点的分式线性映射的一般形式为

$$
\boxed{
w=e^{i\theta}\frac{z-z_0}{z-\bar z_0},
\qquad \operatorname{Im}z_0>0,\quad 0\le\theta<2\pi
}.
$$

### 6.11.2 圆盘内部与半平面的对应

设

$$
z=x+iy,\qquad z_0=x_0+iy_0,\qquad y_0>0.
$$

则

$$
\begin{aligned}
|z-\bar z_0|^2&=(x-x_0)^2+(y+y_0)^2,\\
|z-z_0|^2&=(x-x_0)^2+(y-y_0)^2.
\end{aligned}
$$

相减得到

$$
|z-\bar z_0|^2-|z-z_0|^2=4yy_0.
$$

所以

$$
\boxed{
1-|w|^2=\frac{4yy_0}{|z-\bar z_0|^2}
}.
$$

由于 $y_0>0$，有如下对应：

| 源平面中的位置 | 像平面中的位置 |
| --- | --- |
| $\operatorname{Im}z>0$ | $|w|<1$ |
| $\operatorname{Im}z=0$ | $|w|=1$ |
| $\operatorname{Im}z<0$ | $|w|>1$，包括极点的像 $\infty$ |

此外，

$$
T(\infty)=e^{i\theta},
$$

所以边界上的无穷远点也映到单位圆周上。

为验证满射，令 $q=e^{-i\theta}w$。由

$$
q=\frac{z-z_0}{z-\bar z_0}
$$

解得

$$
\boxed{
z=\frac{z_0-q\bar z_0}{1-q}
=\frac{z_0-e^{-i\theta}w\bar z_0}{1-e^{-i\theta}w}
}.
$$

当 $|w|<1$ 时，$1-q\ne0$，且

$$
\operatorname{Im}z
=y_0\frac{1-|q|^2}{|1-q|^2}>0.
$$

因此逆变换将整个单位圆盘映入上半平面，原变换确实是上半平面到单位圆盘的一一映射。

### 6.11.3 例：Cayley 变换

取 $z_0=i$、$\theta=0$，得到

$$
\boxed{w=\frac{z-i}{z+i}.}
$$

它将上半平面映为单位圆盘，并满足

$$
i\longmapsto0,\qquad
-i\longmapsto\infty,\qquad
0\longmapsto-1,\qquad
\infty\longmapsto1.
$$

逆变换为

$$
\boxed{z=i\frac{1+w}{1-w}.}
$$

对于 $|w|<1$，

$$
\operatorname{Im}z=\frac{1-|w|^2}{|1-w|^2}>0.
$$

### 6.11.4 半平面与圆盘之间的线元对应

对一般形式求导，有

$$
\begin{aligned}
T'(z)
&=e^{i\theta}
\frac{(z-\bar z_0)-(z-z_0)}{(z-\bar z_0)^2}\\
&=e^{i\theta}\frac{z_0-\bar z_0}{(z-\bar z_0)^2}
=e^{i\theta}\frac{2iy_0}{(z-\bar z_0)^2}.
\end{aligned}
$$

因此

$$
|T'(z)|=\frac{2y_0}{|z-\bar z_0|^2}.
$$

结合 $1-|w|^2=4yy_0/|z-\bar z_0|^2$，得到

$$
\boxed{
\frac{|dw|}{1-|w|^2}
=\frac{|dz|}{2\operatorname{Im}z}
}.
$$

若圆盘上采用线元 $2|dw|/(1-|w|^2)$，则对应的上半平面线元为 $|dz|/\operatorname{Im}z$。

## 6.12 一般半平面到圆盘的映射

### 6.12.1 平移与旋转归一化

设边界直线为

$$
L=\{p+te^{i\varphi}:t\in\mathbb R\},
$$

其中 $p\in\mathbb C$ 是直线上一点，$\varphi$ 为直线的方向角。选择它的一侧

$$
H_{p,\varphi}
=\left\{z:\operatorname{Im}\left[(z-p)e^{-i\varphi}\right]>0\right\}.
$$

先平移、再旋转：

$$
\zeta=(z-p)e^{-i\varphi}.
$$

这样 $L$ 映为实轴，$H_{p,\varphi}$ 映为上半平面。

设 $z_0\in H_{p,\varphi}$ 是要映到圆心的点，记

$$
\zeta_0=(z_0-p)e^{-i\varphi},
\qquad \operatorname{Im}\zeta_0>0.
$$

由上半平面到单位圆盘的一般形式，

$$
w=e^{i\theta}\frac{\zeta-\zeta_0}{\zeta-\bar\zeta_0}.
$$

代回原变量：

$$
w=e^{i\theta}
\frac{(z-p)e^{-i\varphi}-(z_0-p)e^{-i\varphi}}
{(z-p)e^{-i\varphi}-\overline{(z_0-p)}e^{i\varphi}}.
$$

分子、分母同时乘以 $e^{i\varphi}$，得到

$$
w=e^{i\theta}
\frac{z-z_0}{z-p-e^{2i\varphi}\overline{(z_0-p)}}.
$$

### 6.12.2 用关于边界的对称点表示

令

$$
z_0^*=p+e^{2i\varphi}\overline{(z_0-p)},
$$

则 $z_0^*$ 是 $z_0$ 关于边界直线 $L$ 的对称点。因此

$$
\boxed{
w=e^{i\theta}\frac{z-z_0}{z-z_0^*},
\qquad 0\le\theta<2\pi
}.
$$

这给出了将 $H_{p,\varphi}$ 一一映为单位圆盘、且将 $z_0$ 映为 $0$ 的全部分式线性映射。

若目标圆盘为 $|w-w_c|<R$，只需再作伸缩与平移，得到

$$
\boxed{
w=w_c+R e^{i\theta}\frac{z-z_0}{z-z_0^*}
}.
$$

其中 $z_0\mapsto w_c$，而对称点 $z_0^*\mapsto\infty$。若选择边界的另一侧作为源半平面，也可通过将方向角改为 $\varphi+\pi$，使用同样的归一化方法。

## 6.13 实系数分式线性变换与半平面

### 6.13.1 实部、虚部的计算

设

$$
w=T(z)=\frac{az+b}{cz+d},
\qquad a,b,c,d\in\mathbb R,\quad ad-bc\ne0.
$$

令 $z=x+iy$、$w=u+iv$，则

$$
w=\frac{(ax+b)+iay}{(cx+d)+icy}.
$$

分子、分母同乘分母的共轭，得

$$
w=\frac{[(ax+b)+iay][(cx+d)-icy]}
{(cx+d)^2+c^2y^2}.
$$

展开分子：

$$
\begin{aligned}
&[(ax+b)+iay][(cx+d)-icy]\\
&=(ax+b)(cx+d)+acy^2\\
&\quad+i\bigl[ay(cx+d)-cy(ax+b)\bigr]\\
&=(ax+b)(cx+d)+acy^2+i(ad-bc)y.
\end{aligned}
$$

所以

$$
\boxed{
u=\frac{(ax+b)(cx+d)+acy^2}{(cx+d)^2+c^2y^2}
},
$$

$$
\boxed{
v=\operatorname{Im}T(z)
=\frac{(ad-bc)y}{(cx+d)^2+c^2y^2}
=\frac{(ad-bc)\operatorname{Im}z}{|cz+d|^2}
}.
$$

当 $y\ne0$ 时，分母严格为正。若 $c\ne0$，因为 $c^2y^2>0$；若 $c=0$，则由 $ad\ne0$ 得 $d\ne0$，分母为 $d^2>0$。

### 6.13.2 行列式符号与半平面对应

由虚部公式，

$$
\operatorname{sgn}(\operatorname{Im}T(z))
=\operatorname{sgn}(ad-bc)\,
\operatorname{sgn}(\operatorname{Im}z).
$$

因此：

| 行列式条件 | 上半平面的像 | 下半平面的像 |
| --- | --- | --- |
| $ad-bc>0$ | 上半平面 | 下半平面 |
| $ad-bc<0$ | 下半平面 | 上半平面 |

这些对应都是一一映到整个半平面。以 $ad-bc>0$ 为例，逆变换

$$
T^{-1}(w)=\frac{dw-b}{-cw+a}
$$

仍有实系数，且其系数行列式仍为 $ad-bc>0$，所以逆变换也将上半平面映入上半平面，因而原变换是满射。行列式为负时同理。

实轴上的非极点映为实数，实极点映为 $\infty$，而 $\infty$ 映为实数或 $\infty$，所以扩充实轴总是映为自身。

**结论。** 对于实系数分式线性变换，保持上半平面的充要条件为

$$
\boxed{ad-bc>0.}
$$

这里的行列式符号针对实系数表示。若以非零实数 $\lambda$ 同乘全部系数，行列式变为 $\lambda^2(ad-bc)$，故符号不变。

### 6.13.3 在一点处判断映向哪一侧

代入上半平面中的点 $z=i$：

$$
\begin{aligned}
T(i)&=\frac{ai+b}{ci+d}\\
&=\frac{(ai+b)(d-ci)}{c^2+d^2}\\
&=\boxed{
\frac{ac+bd}{c^2+d^2}
+i\frac{ad-bc}{c^2+d^2}
}.
\end{aligned}
$$

因为 $c^2+d^2>0$，有

$$
\operatorname{Im}T(i)>0
\quad\Longleftrightarrow\quad ad-bc>0.
$$

因此，在已知边界实轴映为自身的前提下，计算一个内部点的像，就能判断上半平面究竟映为上半平面还是下半平面。

例如，$T(z)=-1/z$ 的实系数行列式为 $1$，故保持上半平面；$T(z)=1/z$ 的实系数行列式为 $-1$，故交换上下半平面。两者在各自的解析点处都保持有向夹角；交换上下半平面并不意味着反共形。

### 6.13.4 上半平面的分式线性自同构的一般形式

**定理。** 将上半平面一一映为自身的分式线性变换，恰好是能够写成

$$
\boxed{
T(z)=\frac{az+b}{cz+d},
\qquad a,b,c,d\in\mathbb R,\quad ad-bc>0
}
$$

的变换。

**证明。** 实系数且行列式为正的充分性已证。下面证明必要性。

设 $T$ 将上半平面一一映为自身。它将边界扩充实轴映为自身。从扩充实轴上选三个互异有限点 $x_1,x_2,x_3$，避开极点，则对应的 $y_j=T(x_j)$ 也是三个互异有限实数。

对任意三个互异有限实数 $t_1,t_2,t_3$，变换

$$
P_t(z)=\frac{(z-t_1)(t_2-t_3)}{(z-t_3)(t_2-t_1)}
$$

有实系数，并依次将 $t_1,t_2,t_3$ 映为 $0,1,\infty$。取 $P_x$ 和 $P_y$，则 $P_y\circ T$ 与 $P_x$ 在 $x_1,x_2,x_3$ 三点取相同值。由三点决定唯一性，

$$
P_y\circ T=P_x,\qquad T=P_y^{-1}\circ P_x.
$$

实系数分式线性变换的逆与复合仍有实系数，所以 $T$ 可以用实系数表示。再由它保持上半平面及虚部公式，必有 $ad-bc>0$。证毕。

此时可以用正实数 $1/\sqrt{ad-bc}$ 同乘全部系数，使系数矩阵满足 $ad-bc=1$；矩阵与其相反数表示同一个变换。

### 6.13.5 上半平面线元的不变性

对于实系数、$ad-bc>0$ 的变换，

$$
|T'(z)|=\frac{ad-bc}{|cz+d|^2},
\qquad
\operatorname{Im}w=\frac{(ad-bc)\operatorname{Im}z}{|cz+d|^2}.
$$

两式相除，即得

$$
\boxed{\frac{|dw|}{\operatorname{Im}w}
=\frac{|dz|}{\operatorname{Im}z}.}
$$

这与通过 Cayley 变换从单位圆盘得到的半平面线元一致。
