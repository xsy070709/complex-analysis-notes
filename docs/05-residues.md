# 第五章 留数

## 5.1 解析函数零点的孤立性

### 5.1.1 零点的阶数与局部分解

设 $f$ 在 $z_0$ 的某邻域内解析，$f(z_0)=0$，且 $f$ 在 $z_0$ 的任意邻域内都不恒等于零。则存在正整数 $n$ 和在 $z_0$ 附近解析的函数 $\varphi$，使

$$
\boxed{f(z)=(z-z_0)^n\varphi(z),\qquad \varphi(z_0)\ne0.}
$$

称 $z_0$ 为 $f$ 的 **$n$ 阶零点**。等价地，

$$
f(z_0)=f'(z_0)=\cdots=f^{(n-1)}(z_0)=0,
\qquad f^{(n)}(z_0)\ne0.
$$

**证明：** 在 $z_0$ 附近作 Taylor 展开：

$$
f(z)=\sum_{k=0}^{\infty}\frac{f^{(k)}(z_0)}{k!}(z-z_0)^k.
$$

若所有系数都为零，则 $f$ 在某邻域内恒为零，与假设矛盾。因此存在最小的正整数 $n$，使 $f^{(n)}(z_0)\ne0$。提取首个非零项对应的因子，得

$$
\begin{aligned}
f(z)&=(z-z_0)^n\varphi(z),\\
\varphi(z)&=\sum_{j=0}^{\infty}
\frac{f^{(n+j)}(z_0)}{(n+j)!}(z-z_0)^j.
\end{aligned}
$$

$\varphi$ 在同一小圆内解析，且

$$
\varphi(z_0)=\frac{f^{(n)}(z_0)}{n!}\ne0.
$$

**用可去奇点判据补全商函数在中心的解析性：** 也可以先只在 $z\ne z_0$ 时定义

$$
\varphi(z)=\frac{f(z)}{(z-z_0)^n}.
$$

它在某个去心邻域内解析。由 Taylor 展开，

$$
\varphi(z)=\frac{f^{(n)}(z_0)}{n!}
+\frac{f^{(n+1)}(z_0)}{(n+1)!}(z-z_0)
+o(z-z_0),
$$

因而

$$
\lim_{z\to z_0}\varphi(z)
=\frac{f^{(n)}(z_0)}{n!}
$$

存在且有限。由第 5.4.1 节的可去奇点判据，补定义

$$
\varphi(z_0)=\frac{f^{(n)}(z_0)}{n!}
$$

后，$\varphi$ 在 $z_0$ 解析，且中心值非零，于是得到所需的局部分解。这里的解析性来自可去奇点判据；仅仅补定义使函数连续，还不能直接断言其解析。前面的幂级数证明则直接给出了这个解析延拓。

### 5.1.2 零点为什么是孤立的

由 $\varphi$ 的连续性及 $\varphi(z_0)\ne0$，可取 $\delta>0$，使 $|z-z_0|<\delta$ 时 $\varphi(z)\ne0$。于是

$$
\boxed{0<|z-z_0|<\delta\quad\Longrightarrow\quad f(z)\ne0.}
$$

这就是零点的孤立性：在 $z_0$ 附近，除 $z_0$ 本身外没有其他零点。

因此，一个解析函数在某点附近只有两种情形：或者在该点的某邻域内恒为零，或者该点若为零点，就必为有限阶孤立零点。

这里的“不恒为零”必须作用于所讨论的邻域。若 $f$ 在一个区域 $D$ 内解析，则由下一节的唯一性定理，只需假设 $f\not\equiv0$ 于 $D$，就能保证 $D$ 中每个零点都是孤立的。“区域”包含连通性要求；在不连通的开集上，各个连通分支可以有不同情形。

## 5.2 解析函数的唯一性定理

### 5.2.1 定理及条件

设 $D$ 为区域，$f,g$ 在 $D$ 内解析。如果存在两两不同的点 $z_k\in D$，满足

$$
f(z_k)=g(z_k),\qquad k=1,2,\ldots,
$$

且

$$
z_k\longrightarrow z_0\in D,
$$

则

$$
\boxed{f(z)\equiv g(z),\qquad z\in D.}
$$

也就是说，只要两个解析函数在具有**区域内聚点**的一组点上相等，它们就在整个区域内相等。

### 5.2.2 证明：由聚点推广到整个区域

令 $h=f-g$，则 $h$ 在 $D$ 内解析，且 $h(z_k)=0$。连续性给出

$$
h(z_0)=\lim_{k\to\infty}h(z_k)=0.
$$

由于 $z_k$ 两两不同，$z_0$ 不是孤立零点。由上一节的局部结论，$h$ 必在 $z_0$ 的某邻域内恒为零。

还需说明这一局部结论为何能推广至整个 $D$。令

$$
E=\{a\in D:\ h\text{ 在 }a\text{ 的某邻域内恒为零}\}.
$$

$E$ 非空，且显然在 $D$ 中为开集。若 $a\in D$ 是 $E$ 的聚点，则 $a$ 附近有趋向于 $a$ 的不同零点；再次利用零点的局部结论，$h$ 在 $a$ 的某邻域内恒为零，所以 $a\in E$。故 $E$ 在 $D$ 中也为闭集。

由 $D$ 连通，得到 $E=D$，从而 $h\equiv0$，即 $f\equiv g$。

**条件辨析：**

- 点列必须包含无限多个不同的点；重复同一个相等点不能确定解析函数。
- 聚点必须在 $D$ 内。仅在边界处聚集，不能直接使用本定理。
- 结论依赖区域的连通性。

## 5.3 奇点与孤立奇点

### 5.3.1 定义

若 $z_0$ 是所讨论解析函数的异常点，即 $f$ 在 $z_0$ 处不解析或尚未定义，则称其为奇点。若存在 $R>0$，使 $f$ 在去心邻域

$$
0<|z-z_0|<R
$$

内处处解析，则称 $z_0$ 为 **孤立奇点**。

孤立性使我们能够在这一去心圆内使用第四章的 Laurent 展开：

$$
f(z)=\sum_{k=-\infty}^{\infty}c_k(z-z_0)^k.
$$

其中 $k<0$ 的部分称为**主要部分**，$k\ge0$ 的部分称为**解析部分**。根据主要部分的情形，孤立奇点分为可去奇点、极点和本性奇点。

### 5.3.2 非孤立情形

**例一：** $f(z)=|z|^2=z\overline z$ 在任何开邻域内都不能成为解析函数，不能把其中的点当作孤立奇点处理。孤立奇点分类的前提是函数在某个去心邻域内处处解析。

**例二：**

$$
f(z)=\frac1{\sin(1/z)}.
$$

其奇点包括

$$
z_k=\frac1{k\pi},\qquad k\in\mathbb Z\setminus\{0\},
$$

且 $z_k\to0$。所以 $0$ 的任意去心邻域内都含有其他奇点，$0$ 不是孤立奇点。

## 5.4 可去奇点

### 5.4.1 Laurent 展开与极限判据

设 $z_0$ 是孤立奇点。若其 Laurent 展开中所有负次幂系数均为零，即

$$
c_{-n}=0,\qquad n=1,2,\ldots,
$$

则

$$
f(z)=\sum_{n=0}^{\infty}c_n(z-z_0)^n,
\qquad 0<|z-z_0|<R.
$$

右端的幂级数在中心也有意义，因此只需补定义或重新定义 $f(z_0)=c_0$，便可使函数在 $z_0$ 解析。这时称 $z_0$ 为 **可去奇点**。

其等价的极限判据为

$$
\boxed{z_0\text{ 是可去奇点}
\quad\Longleftrightarrow\quad
\lim_{z\to z_0}f(z)\text{ 存在且有限}.}
$$

极限值就是解析延拓在 $z_0$ 处应取的值 $c_0$。这里的极限是复平面中沿任意路径趋近的极限。

### 5.4.2 例：正弦函数的商

在 $z=0$ 附近，

$$
\frac{\sin z}{z}
=1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots.
$$

没有负次幂项，所以 $0$ 是可去奇点；补定义函数在 $0$ 处的值为 $1$，即可得到整函数。

### 5.4.3 例：余弦函数的商

由 $\cos z$ 的 Taylor 展开，

$$
\frac{1-\cos z}{z^2}
=\frac1{2!}-\frac{z^2}{4!}+\frac{z^4}{6!}-\cdots.
$$

因此 $0$ 也是可去奇点，且

$$
\lim_{z\to0}\frac{1-\cos z}{z^2}=\frac12.
$$

## 5.5 极点

### 5.5.1 定义与阶数

设 $z_0$ 是孤立奇点。若 Laurent 展开的主要部分仅有有限多个非零项，设其中最低次幂为 $-m$，$m\ge1$，则

$$
\begin{aligned}
f(z)={}&\frac{c_{-m}}{(z-z_0)^m}
+\frac{c_{-(m-1)}}{(z-z_0)^{m-1}}+\cdots
+\frac{c_{-1}}{z-z_0}\\
&+\sum_{n=0}^{\infty}c_n(z-z_0)^n,
\qquad c_{-m}\ne0.
\end{aligned}
$$

称 $z_0$ 为 $f$ 的 **$m$ 阶极点**。等价地，可写为

$$
\boxed{f(z)=\frac{\varphi(z)}{(z-z_0)^m},
\qquad \varphi\text{ 在 }z_0\text{ 附近解析},\quad
\varphi(z_0)\ne0.}
$$

因此，在上述孤立奇点的前提下，

$$
\boxed{z_0\text{ 是极点}
\quad\Longleftrightarrow\quad
\lim_{z\to z_0}|f(z)|=+\infty.}
$$

通常也将右侧记作 $\lim_{z\to z_0}f(z)=\infty$，它表示模趋于无穷，并非实数轴上带符号的正无穷。

### 5.5.2 例：分母的次数不等于极点阶数

考察

$$
f(z)=\frac{\sin z}{z^2}.
$$

展开得

$$
\frac{\sin z}{z^2}
=\frac1z-\frac z{3!}+\frac{z^3}{5!}-\cdots.
$$

主要部分只有 $1/z$，所以 $0$ 是**一阶极点**。虽然分母为 $z^2$，分子的 $\sin z$ 在 $0$ 有一阶零点，抵消了一次。

也可直接计算

$$
\lim_{z\to0}z\frac{\sin z}{z^2}
=\lim_{z\to0}\frac{\sin z}{z}=1\ne0,
$$

由此确定极点阶数为 $1$。

## 5.6 本性奇点

### 5.6.1 定义与第三个例子

设 $z_0$ 是孤立奇点。如果 Laurent 展开的主要部分有无限多个非零项，则称 $z_0$ 为 **本性奇点**。

第三个例子为

$$
f(z)=e^{1/z},\qquad z_0=0.
$$

利用指数函数的幂级数，在整个去心平面 $0<|z|<\infty$ 内有

$$
\boxed{e^{1/z}
=\sum_{n=0}^{\infty}\frac1{n!z^n}
=1+\frac1z+\frac1{2!z^2}+\frac1{3!z^3}+\cdots.}
$$

其中 $c_{-n}=1/n!\ne0$（$n\ge1$），负次幂项有无限多个，所以 $0$ 是本性奇点。

### 5.6.2 趋近奇点时没有极限

沿正实轴与负实轴分别趋于 $0$，有

$$
\lim_{x\to0^+}e^{1/x}=+\infty,
\qquad
\lim_{x\to0^-}e^{1/x}=0.
$$

因此 $\lim_{z\to0}e^{1/z}$ 不存在，既没有有限极限，也不趋于无穷。

对一般孤立奇点，这也给出三类奇点的极限辨别：有有限极限时为可去奇点，模趋于无穷时为极点，两者均不成立时为本性奇点。

### 5.6.3 任意小去心邻域内的取值

指数函数不取零值，所以 $e^{1/z}\ne0$。反过来，任给非零复数 $w$，求解

$$
e^{1/z}=w.
$$

取 $w$ 的一个辐角 $\theta$，复对数的所有值为

$$
\ln|w|+i(\theta+2k\pi),\qquad k\in\mathbb Z.
$$

因此，除去分母为零的情形，所有解为

$$
\boxed{z_k=\frac1{\ln|w|+i(\theta+2k\pi)}.}
$$

当 $|k|\to\infty$ 时，分母的模趋于无穷，故 $z_k\to0$。于是对任意 $\delta>0$，都有无限多个不同的解满足

$$
0<|z_k|<\delta,\qquad e^{1/z_k}=w.
$$

这说明：**$e^{1/z}$ 在 $0$ 的任意小去心邻域内，都无限多次取到每一个非零复数值，而始终不取零值。** 上述结论直接由本例的方程求解得到。

## 5.7 留数的定义与局部积分公式

### 5.7.1 留数是 Laurent 展开的一个系数

设 $z_0$ 为 $f$ 的孤立奇点，且在 $0<|z-z_0|<R$ 内有 Laurent 展开

$$
f(z)=\sum_{n=-\infty}^{\infty}c_n(z-z_0)^n.
$$

定义 $f$ 在 $z_0$ 处的**留数**为其中 $(z-z_0)^{-1}$ 项的系数：

$$
\boxed{\operatorname{Res}(f;z_0)=c_{-1}.}
$$

留数只取决于这一个系数。极点或本性奇点的留数都可能为零；可去奇点的留数必为零。

### 5.7.2 为什么围道积分只留下这一项

取正向（逆时针）圆周

$$
C_0:\quad |z-z_0|=\delta,\qquad 0<\delta<R.
$$

Laurent 级数的正、负次幂两部分在 $C_0$ 上均一致收敛，所以可以逐项积分：

$$
\oint_{C_0}f(z)\,dz
=\sum_{n=-\infty}^{\infty}c_n
\oint_{C_0}(z-z_0)^n\,dz.
$$

利用第三章已计算的圆周积分，

$$
\oint_{C_0}(z-z_0)^n\,dz
=\begin{cases}
2\pi i,&n=-1,\\
0,&n\ne-1,
\end{cases}
\qquad n\in\mathbb Z.
$$

于是所有项都消失，只有 $n=-1$ 的一项保留下来：

$$
\boxed{\oint_{C_0}f(z)\,dz
=2\pi i\,c_{-1}
=2\pi i\,\operatorname{Res}(f;z_0).}
$$

等价地，

$$
\boxed{\operatorname{Res}(f;z_0)
=\frac1{2\pi i}\oint_{C_0}f(z)\,dz.}
$$

这解释了留数与积分的联系：围绕孤立奇点正向积分一周，会选出 Laurent 展开中的 $-1$ 次幂系数。只要圆周仍位于上述去心邻域内，改变半径 $\delta$ 不改变积分值。

## 5.8 一阶极点处留数的计算

### 5.8.1 乘去极点后取极限

若 $z_0$ 为 $f$ 的一阶极点，则在其附近有

$$
f(z)=\frac{c_{-1}}{z-z_0}
+c_0+c_1(z-z_0)+o(z-z_0),\qquad c_{-1}\ne0.
$$

两边同乘 $z-z_0$，再令 $z\to z_0$，得到

$$
\boxed{\operatorname{Res}(f;z_0)
=c_{-1}=\lim_{z\to z_0}(z-z_0)f(z).}
$$

这里乘以 $z-z_0$，正好消去一阶极点，余下函数在中心的解析延拓值就是留数。

### 5.8.2 商函数在分母单零点处的公式

设

$$
f(z)=\frac{P(z)}{Q(z)},
$$

其中 $P,Q$ 在 $z_0$ 附近解析，且

$$
P(z_0)\ne0,\qquad Q(z_0)=0,\qquad Q'(z_0)\ne0.
$$

由于 $Q$ 在 $z_0$ 有一阶零点，$f$ 在此处有一阶极点，并且

$$
\boxed{\operatorname{Res}\left(\frac{P}{Q};z_0\right)
=\frac{P(z_0)}{Q'(z_0)}.}
$$

**证明：** 令 $h=z-z_0$，在中心作 Taylor 展开：

$$
\begin{aligned}
P(z)&=P(z_0)+P'(z_0)h+o(h),\\
Q(z)&=Q'(z_0)h+\frac{Q''(z_0)}{2}h^2+o(h^2).
\end{aligned}
$$

于是

$$
\begin{aligned}
(z-z_0)f(z)
&=\frac{P(z_0)+P'(z_0)h+o(h)}
{Q'(z_0)+\frac{Q''(z_0)}{2}h+o(h)}\\
&\longrightarrow\frac{P(z_0)}{Q'(z_0)}.
\end{aligned}
$$

再用上一小节的极限公式即得结论。

使用时应先检查分母在该点是否为单零点。若 $Q'(z_0)=0$，就不能直接套用此式；若 $P(z_0)=0$ 而 $Q'(z_0)\ne0$，则该点为可去奇点，留数为零。

## 5.9 高阶极点处留数的计算

### 5.9.1 一般公式及推导

若 $z_0$ 是 $f$ 的 $m$ 阶极点，则

$$
f(z)=\frac{c_{-m}}{(z-z_0)^m}
+\cdots+\frac{c_{-1}}{z-z_0}
+\sum_{j=0}^{\infty}c_j(z-z_0)^j.
$$

令 $H(z)=(z-z_0)^m f(z)$，并在 $z_0$ 处作解析延拓。其 Taylor 展开为

$$
\begin{aligned}
H(z)={}&c_{-m}+c_{-(m-1)}(z-z_0)+\cdots\\
&+c_{-1}(z-z_0)^{m-1}
+c_0(z-z_0)^m+\cdots.
\end{aligned}
$$

对上式求 $m-1$ 阶导数，再令 $z\to z_0$。次数低于 $m-1$ 的项求导后为零，次数高于 $m-1$ 的项在中心为零，故

$$
H^{(m-1)}(z_0)=(m-1)!\,c_{-1}.
$$

因此

$$
\boxed{\operatorname{Res}(f;z_0)
=\frac1{(m-1)!}\lim_{z\to z_0}
\frac{d^{m-1}}{dz^{m-1}}
\left[(z-z_0)^m f(z)\right].}
$$

也可简写为 $H^{(m-1)}(z_0)/(m-1)!$。这里求导的对象是整个乘积 $(z-z_0)^m f(z)$。当 $m=1$ 时，零阶导数就是函数本身，公式退化为上一节的一阶极点公式。

### 5.9.2 例一：再次计算正弦商的留数

设

$$
f(z)=\frac{\sin z}{z^2}.
$$

$0$ 为一阶极点，所以

$$
\operatorname{Res}(f;0)
=\lim_{z\to0}zf(z)
=\lim_{z\to0}\frac{\sin z}{z}=1.
$$

### 5.9.3 例二：正弦商的一般情形

设

$$
g(z)=\frac{\sin z}{z^n},\qquad n\ge2.
$$

因为 $\sin z$ 在 $0$ 有一阶零点，所以 $0$ 是 $g$ 的 **$n-1$ 阶极点**。乘去极点后，

$$
z^{n-1}g(z)=\frac{\sin z}{z}
=\sum_{k=0}^{\infty}\frac{(-1)^k z^{2k}}{(2k+1)!}.
$$

代入公式（取 $m=n-1$），得

$$
\operatorname{Res}(g;0)
=\frac1{(n-2)!}
\left.\frac{d^{n-2}}{dz^{n-2}}
\left(\frac{\sin z}{z}\right)\right|_{z=0},
$$

其中 $\sin z/z$ 在 $0$ 处按解析延拓取值。它的展开只有偶次幂，故 $n$ 为奇数时，上式为零；$n$ 为偶数时，提取 $z^{n-2}$ 项即可。于是

$$
\boxed{\operatorname{Res}\left(\frac{\sin z}{z^n};0\right)
=\begin{cases}
\displaystyle\frac{(-1)^{(n-2)/2}}{(n-1)!},&n\text{ 为偶数},\\
0,&n\text{ 为奇数}.
\end{cases}}
$$

直接从 $\sin z/z^n$ 的 Laurent 展开中寻找 $z^{-1}$ 项，也得到同一结果：该项要求 $2k+1-n=-1$，即 $2k=n-2$。

例如，$n=2,3,4$ 时的留数依次为 $1,0,-1/6$。其中 $\sin z/z^3$ 在 $0$ 有二阶极点，留数却为零，说明极点的存在并不保证留数非零。

## 5.10 从局部积分公式到留数定理

为衔接下面的实积分例题，先写出所用的留数定理。

设 $C$ 为正向、分段光滑的简单闭曲线，$f$ 在 $C$ 及其内部除有限个孤立奇点 $a_1,\ldots,a_N$ 外解析，且奇点均不在 $C$ 上，则

$$
\boxed{\oint_C f(z)\,dz
=2\pi i\sum_{j=1}^{N}\operatorname{Res}(f;a_j).}
$$

这里假设 $f$ 在包含闭曲线及其内部的某个开集中，除上述点外解析。证明可沿用第三章复合闭路定理：在每个奇点附近取互不相交、位于 $C$ 内的小圆 $C_j$，各小圆均按逆时针方向定向。挖去这些小圆内部后，$f$ 在剩余区域及其边界解析，所以

$$
\oint_C f(z)\,dz=\sum_{j=1}^{N}\oint_{C_j}f(z)\,dz.
$$

对每个小圆使用第 5.7 节的局部积分公式，即得留数定理。计算时只需累加围道内部奇点的留数。

## 5.11 应用：三角函数的定积分

### 5.11.1 题目与正弦、余弦形式的等价性

设 $a,b$ 为实数，且 $a>|b|\ge0$，求

$$
I_{a,b}=\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}.
$$

因为分母始终满足 $a+b\cos\theta\ge a-|b|>0$，积分不存在路径上的奇性。

先说明，若 $F\in C[-1,1]$，则

$$
\int_0^{2\pi}F(\cos\theta)\,d\theta
=\int_0^{2\pi}F(\sin\theta)\,d\theta.
$$

令 $t=\theta+\pi/2$，则 $\cos\theta=\sin t$；再利用 $F(\sin t)$ 的 $2\pi$ 周期性，任何长度为 $2\pi$ 的区间上的积分都相等。因此本题将余弦换成正弦，结果不变。

### 5.11.2 单位圆代换

当 $b=0$ 时，直接得到 $I_{a,0}=2\pi/a$。下面先设 $b>0$；$b<0$ 的情形可由 $\theta$ 平移 $\pi$ 化为 $-b>0$。

令

$$
z=e^{i\theta},\qquad 0\le\theta\le2\pi.
$$

当 $\theta$ 增加时，$z$ 沿单位圆逆时针一周，且

$$
dz=iz\,d\theta,\qquad d\theta=\frac{dz}{iz}.
$$

由 Euler 公式，

$$
\cos\theta=\frac{z+z^{-1}}2,
\qquad
\sin\theta=\frac{z-z^{-1}}{2i}.
$$

因此

$$
\begin{aligned}
I_{a,b}
&=\oint_{|z|=1}
\frac1{a+\frac b2(z+z^{-1})}\frac{dz}{iz}\\
&=\frac2i\oint_{|z|=1}\frac{dz}{bz^2+2az+b}\\
&=\frac2{ib}\oint_{|z|=1}
\frac{dz}{z^2+\frac{2a}{b}z+1}.
\end{aligned}
$$

化简后被积函数在 $z=0$ 解析（分母的常数项为 $1$）。代换中出现的 $z^{-1}$ 并未给最终围道积分额外引入一个原点极点。

### 5.11.3 判断哪个极点在单位圆内

记 $\Delta=\sqrt{a^2-b^2}>0$。二次方程的根为

$$
z_1=\frac{-a+\Delta}{b},\qquad
z_2=\frac{-a-\Delta}{b},\qquad z_1z_2=1.
$$

由于 $a>b>0$，将 $z_1$ 有理化可得

$$
z_1=-\frac{b}{a+\Delta},\qquad -1<z_1<0,
$$

而

$$
z_2=-\frac{a+\Delta}{b}<-1.
$$

所以两个极点都在负实轴上，只有 $z_1$ 在单位圆内；二者均不在围道上。

### 5.11.4 计算留数与积分

令

$$
f(z)=\frac1{Q(z)},\qquad
Q(z)=z^2+\frac{2a}{b}z+1.
$$

两根不同，故 $z_1$ 为一阶极点。用商函数留数公式，

$$
\begin{aligned}
\operatorname{Res}(f;z_1)
&=\frac1{Q'(z_1)}
=\frac1{2z_1+2a/b}\\
&=\frac{b}{2\Delta}.
\end{aligned}
$$

代入留数定理，注意保留积分外的因子 $2/(ib)$：

$$
I_{a,b}
=\frac2{ib}\,2\pi i\,\frac{b}{2\Delta}
=\frac{2\pi}{\Delta}.
$$

结合 $b=0$ 以及平移处理的 $b<0$ 情形，最终得到

$$
\boxed{\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}
=\int_0^{2\pi}\frac{d\theta}{a+b\sin\theta}
=\frac{2\pi}{\sqrt{a^2-b^2}},\qquad a>|b|.}
$$

这类计算的步骤是：用单位圆代换化为有理函数的围道积分，确定单位圆内的极点，再计算相应留数。

## 5.12 应用：分母含正弦、余弦平方的积分

### 5.12.1 题目与倍角解法

设 $A,B\in\mathbb R$，且 $AB>0$，求

$$
J_{A,B}=\int_0^{2\pi}
\frac{d\theta}{A^2\cos^2\theta+B^2\sin^2\theta}.
$$

利用倍角公式，

$$
\cos^2\theta=\frac{1+\cos2\theta}{2},\qquad
\sin^2\theta=\frac{1-\cos2\theta}{2},
$$

可得

$$
J_{A,B}=2\int_0^{2\pi}
\frac{d\theta}{(A^2+B^2)+(A^2-B^2)\cos2\theta}.
$$

令 $\varphi=2\theta$，则 $d\varphi=2\,d\theta$，积分区间变为 $[0,4\pi]$。记

$$
a=A^2+B^2,\qquad b=A^2-B^2,
$$

利用被积函数的 $2\pi$ 周期性，得到

$$
J_{A,B}=\int_0^{4\pi}\frac{d\varphi}{a+b\cos\varphi}
=2\int_0^{2\pi}\frac{d\varphi}{a+b\cos\varphi}.
$$

因为 $A,B$ 都非零，所以 $a>|b|$。由上一节的结果，

$$
\begin{aligned}
J_{A,B}
&=\frac{4\pi}{\sqrt{(A^2+B^2)^2-(A^2-B^2)^2}}\\
&=\frac{4\pi}{2|AB|}
=\boxed{\frac{2\pi}{AB}},\qquad AB>0.
\end{aligned}
$$

换元时必须同时改变积分上限；这里出现的 $[0,4\pi]$ 包含两个周期。

### 5.12.2 补充解法：上下同除以余弦平方

被积函数只含 $\cos^2\theta$ 与 $\sin^2\theta$，四个象限的积分相等，因此

$$
J_{A,B}=4\int_0^{\pi/2}
\frac{d\theta}{A^2\cos^2\theta+B^2\sin^2\theta}.
$$

在 $0\le\theta<\pi/2$ 内，分子分母同除以 $\cos^2\theta$，得

$$
\frac{d\theta}{A^2\cos^2\theta+B^2\sin^2\theta}
=\frac{\sec^2\theta\,d\theta}{A^2+B^2\tan^2\theta}.
$$

令 $t=\tan\theta$，则 $dt=\sec^2\theta\,d\theta$，且当 $\theta\to(\pi/2)^-$ 时，$t\to+\infty$。于是

$$
J_{A,B}=4\int_0^{\infty}\frac{dt}{A^2+B^2t^2}.
$$

再令 $u=|B/A|t$，可得

$$
\begin{aligned}
J_{A,B}
&=\frac4{|AB|}\int_0^{\infty}\frac{du}{1+u^2}\\
&=\frac4{|AB|}\left[\arctan u\right]_0^{\infty}
=\frac{2\pi}{|AB|}.
\end{aligned}
$$

在题设 $AB>0$ 下，同样得到 $J_{A,B}=2\pi/(AB)$。实际上，对任意非零实数 $A,B$，更一般的结果都是 $2\pi/|AB|$。

这里先分象限再换元，是因为 $\tan\theta$ 在 $[0,2\pi]$ 上有间断点，不能将整段积分直接用两端的 $\tan0=\tan2\pi=0$ 作为换元上下限。原被积函数在 $\pi/2$ 处连续；无穷上限只来自正切换元。

## 5.13 参数代入与对参数求导

### 5.13.1 分母为一减余弦项加参数平方

设 $q\in(-1,1)$，求

$$
I_q=\int_0^{2\pi}
\frac{d\theta}{1-2q\cos\theta+q^2}.
$$

在第 5.11 节的公式中取

$$
a=1+q^2,\qquad b=-2q.
$$

因为

$$
a-|b|=1+q^2-2|q|=(1-|q|)^2>0,
$$

满足公式的适用条件。于是

$$
\begin{aligned}
I_q
&=\frac{2\pi}{\sqrt{(1+q^2)^2-4q^2}}\\
&=\frac{2\pi}{\sqrt{(1-q^2)^2}}
=\boxed{\frac{2\pi}{1-q^2}}.
\end{aligned}
$$

最后一步使用了 $|q|<1$，所以 $1-q^2>0$，能将根号下的平方化为 $1-q^2$。

### 5.13.2 对参数求导：分母平方的积分

仍设 $a>|b|$，记

$$
K_{a,b}=\int_0^{2\pi}\frac{d\theta}{(a+b\cos\theta)^2}.
$$

从已知结果

$$
I_{a,b}=\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}
=2\pi(a^2-b^2)^{-1/2}
$$

出发，保持 $b$ 不变，对 $a$ 求偏导。在给定 $a>|b|$ 的附近可选一个小的参数区间，使分母有统一的正下界；被积函数及其对 $a$ 的偏导在该区间与 $[0,2\pi]$ 的乘积上连续，因而允许交换求导与积分。

左侧为

$$
\frac{\partial I_{a,b}}{\partial a}
=-\int_0^{2\pi}\frac{d\theta}{(a+b\cos\theta)^2}
=-K_{a,b}.
$$

右侧为

$$
\begin{aligned}
\frac{\partial}{\partial a}
\left[2\pi(a^2-b^2)^{-1/2}\right]
&=2\pi\left(-\frac12\right)
(a^2-b^2)^{-3/2}\cdot2a\\
&=-\frac{2\pi a}{(a^2-b^2)^{3/2}}.
\end{aligned}
$$

两侧负号抵消，得到

$$
\boxed{\int_0^{2\pi}\frac{d\theta}{(a+b\cos\theta)^2}
=\frac{2\pi a}{(a^2-b^2)^{3/2}},\qquad a>|b|.}
$$

这里 $K_{a,b}$ 是分母平方的积分，等于 $-\partial I_{a,b}/\partial a$。用独立符号记它，可以避免将板书中的带撇记号误认为不带负号的参数导数。

### 5.13.3 推广：分母的任意正整数次幂

设 $a>|b|$，$n\ge1$ 为整数，记

$$
I_n(a,b)=\int_0^{2\pi}\frac{d\theta}{(a+b\cos\theta)^n}.
$$

其中 $I_1(a,b)=I_{a,b}$，$I_2(a,b)=K_{a,b}$。保持 $b$ 不变，反复对 $a$ 求导，有

$$
\frac{\partial^{n-1}}{\partial a^{n-1}}
\frac1{a+b\cos\theta}
=\frac{(-1)^{n-1}(n-1)!}{(a+b\cos\theta)^n}.
$$

由于在给定参数附近分母有统一正下界，每一有限阶参数导数都连续且一致有界，可以逐次将求导移入积分。因此

$$
\boxed{I_n(a,b)
=\frac{2\pi(-1)^{n-1}}{(n-1)!}
\frac{\partial^{n-1}}{\partial a^{n-1}}
(a^2-b^2)^{-1/2}.}
$$

这给出了所有正整数 $n$ 的计算公式。也可以直接对 $I_n$ 求一次参数导数：

$$
\begin{aligned}
\frac{\partial I_n(a,b)}{\partial a}
&=\int_0^{2\pi}\frac{-n\,d\theta}{(a+b\cos\theta)^{n+1}}\\
&=-nI_{n+1}(a,b).
\end{aligned}
$$

整理后，得到逐次计算的递推关系：

$$
\boxed{I_{n+1}(a,b)=-\frac1n\frac{\partial I_n(a,b)}{\partial a},
\qquad n\ge1.}
$$

例如，令 $D=a^2-b^2$，则

$$
\begin{aligned}
I_1&=\frac{2\pi}{D^{1/2}},\\
I_2&=\frac{2\pi a}{D^{3/2}},\\
I_3&=-\frac12\frac{\partial I_2}{\partial a}
=\frac{\pi(2a^2+b^2)}{D^{5/2}},\\
I_4&=-\frac13\frac{\partial I_3}{\partial a}
=\frac{\pi a(2a^2+3b^2)}{D^{7/2}}.
\end{aligned}
$$

当 $b=0$ 时，这些结果都退化为 $I_n(a,0)=2\pi/a^n$，与直接积分一致。将余弦换成正弦，由整周期平移，所有公式仍成立。

## 5.14 应用：含正弦因子的无穷积分

### 5.14.1 题目、收敛性与复指数

设 $a,b,k>0$，先设 $a\ne b$，求

$$
I_{a,b,k}=\int_0^{\infty}
\frac{x^3\sin(kx)}{(x^2+a^2)(x^2+b^2)}\,dx.
$$

当 $x\to\infty$ 时，

$$
\frac{x^3}{(x^2+a^2)(x^2+b^2)}
=\frac1x+O(x^{-3}).
$$

由 Dirichlet 判别法，$\int_1^\infty\sin(kx)/x\,dx$ 收敛；余项对应的积分绝对收敛。原被积函数在 $0$ 附近连续，所以本题作为普通反常积分收敛。它并非绝对收敛。

令

$$
F(z)=\frac{z^3e^{ikz}}{(z^2+a^2)(z^2+b^2)}.
$$

对每个有限的 $R>0$，由于有理因子关于 $x$ 为奇函数，$\cos(kx)$ 为偶函数、$\sin(kx)$ 为奇函数，得到

$$
\int_{-R}^{R}F(x)\,dx
=2i\int_0^R
\frac{x^3\sin(kx)}{(x^2+a^2)(x^2+b^2)}\,dx.
$$

因此

$$
I_{a,b,k}=\frac12\operatorname{Im}
\lim_{R\to\infty}\int_{-R}^{R}F(x)\,dx.
$$

这里先在对称的有限区间上取虚部，再取极限；不需要预先假设复函数 $F$ 在整条实轴上的普通反常积分存在。

### 5.14.2 上半圆围道与大圆弧估计

取 $R>\max(a,b)$，以实轴线段 $[-R,R]$ 和上半圆弧

$$
C_R:\quad z=Re^{i\theta},\qquad 0\le\theta\le\pi
$$

组成正向闭围道。因为 $k>0$，在上半平面有

$$
|e^{ikz}|=e^{-k\operatorname{Im}z}
=e^{-kR\sin\theta}\le1.
$$

在充分大的圆周上，利用 $|z^2+a^2|\ge R^2-a^2$ 及对应的 $b$ 的不等式，可取与 $R$ 无关的常数 $M$，使

$$
\left|\frac{z^3}{(z^2+a^2)(z^2+b^2)}\right|
\le\frac{M}{R}.
$$

仅用指数因子的上界 $1$，乘以弧长只能得到常数上界。需要进一步保留它的衰减：

$$
\left|\int_{C_R}F(z)\,dz\right|
\le M\int_0^\pi e^{-kR\sin\theta}\,d\theta.
$$

利用对称性及 $0\le\theta\le\pi/2$ 时 $\sin\theta\ge2\theta/\pi$，有

$$
\begin{aligned}
\int_0^\pi e^{-kR\sin\theta}\,d\theta
&\le2\int_0^{\pi/2}e^{-2kR\theta/\pi}\,d\theta\\
&=\frac{\pi}{kR}(1-e^{-kR})
\le\frac{\pi}{kR}\longrightarrow0.
\end{aligned}
$$

所以大圆弧上的积分趋于零。这给出了本例所需的 Jordan 型估计。

### 5.14.3 两个一阶极点的留数

上半平面的极点为 $ia$、$ib$。当 $a\ne b$ 时，两者都是一阶极点：

$$
\begin{aligned}
\operatorname{Res}(F;ia)
&=\frac{(ia)^3e^{-ak}}{(2ia)(b^2-a^2)}
=\frac{a^2e^{-ak}}{2(a^2-b^2)},\\
\operatorname{Res}(F;ib)
&=\frac{(ib)^3e^{-bk}}{(2ib)(a^2-b^2)}
=-\frac{b^2e^{-bk}}{2(a^2-b^2)}.
\end{aligned}
$$

由留数定理及大圆弧积分的极限，

$$
\lim_{R\to\infty}\int_{-R}^{R}F(x)\,dx
=\pi i\,\frac{a^2e^{-ak}-b^2e^{-bk}}{a^2-b^2}.
$$

取虚部并除以 $2$，得到

$$
\boxed{I_{a,b,k}
=\frac{\pi}{2}\,
\frac{a^2e^{-ak}-b^2e^{-bk}}{a^2-b^2},
\qquad a,b,k>0,\quad a\ne b.}
$$

### 5.14.4 两个参数相等：二阶极点的情形

若 $a=b$，上半平面内的两个极点合并为 $ia$ 处的二阶极点，不能再分别使用上一小节的两个一阶极点公式。此时

$$
F(z)=\frac{z^3e^{ikz}}{(z-ia)^2(z+ia)^2},
$$

由二阶极点公式，

$$
\begin{aligned}
\operatorname{Res}(F;ia)
&=\left.\frac{d}{dz}\left[\frac{z^3e^{ikz}}{(z+ia)^2}\right]\right|_{z=ia}\\
&=\left.e^{ikz}\left[
\frac{3z^2+ikz^3}{(z+ia)^2}
-\frac{2z^3}{(z+ia)^3}\right]\right|_{z=ia}\\
&=e^{-ak}\left(\frac{3-ak}{4}-\frac14\right)\\
&=\frac{2-ak}{4}e^{-ak}.
\end{aligned}
$$

同样的大圆弧估计仍成立，故

$$
\boxed{\int_0^\infty\frac{x^3\sin(kx)}{(x^2+a^2)^2}\,dx
=\frac{\pi}{4}(2-ak)e^{-ak},\qquad a,k>0.}
$$

这一表达式也与上一小节结果在 $b\to a$ 时的代数极限一致。

### 5.14.5 多个因子与重复因子的推广

同样的方法可用于

$$
\int_0^\infty
\frac{x^3\sin(kx)}{(x^2+a^2)(x^2+b^2)(x^2+c^2)}\,dx,
\qquad a,b,c,k>0.
$$

若 $a,b,c$ 两两不同，上半平面的极点为 $ia,ib,ic$，均为一阶极点；参数相等时，极点合并，须按合并后的阶数计算留数。

相应地，可考虑

$$
J_n(a,k)=\int_0^\infty\frac{x^3\sin(kx)}{(x^2+a^2)^n}\,dx,
\qquad n\ge2,\quad a,k>0.
$$

此时 $ia$ 是复函数 $z^3e^{ikz}/(z^2+a^2)^n$ 的 $n$ 阶极点。在上半圆围道中使用高阶极点公式，得到

$$
\boxed{J_n(a,k)=\frac{\pi}{(n-1)!}\operatorname{Re}
\left\{\left.
\frac{d^{n-1}}{dz^{n-1}}
\left[\frac{z^3e^{ikz}}{(z+ia)^n}\right]
\right|_{z=ia}\right\}.}
$$

其中实部的出现来自 $\operatorname{Im}(i\,w)=\operatorname{Re}w$。$n=2$ 时积分条件收敛，需要前述指数衰减估计；$n\ge3$ 时被积函数在无穷远处为 $O(x^{3-2n})$，积分绝对收敛。

## 5.15 有理函数无穷积分的次数条件

设 $P_p,Q_m$ 分别为次数为 $p,m$ 的多项式，且有理函数在所讨论的实积分路径上没有极点。次数条件主要控制无穷远处的行为，路径上有限点的奇性仍须另行检查。

### 5.15.1 不含振荡因子

若

$$
p\le m-2,
$$

则 $P_p(x)/Q_m(x)=O(x^{-2})$ 或衰减得更快，实轴尾部积分绝对收敛。同时，在充分大的半圆上有

$$
\left|\int_{C_R}\frac{P_p(z)}{Q_m(z)}\,dz\right|
\le\pi R\cdot O(R^{p-m})
=O(R^{p-m+1})\longrightarrow0.
$$

所以可以用上半圆闭合围道，计算整条实轴上的积分。若目标是 $[0,\infty)$ 上的积分，还需利用偶性等关系，才能由整轴积分还原。

### 5.15.2 含复指数振荡因子

若 $k>0$，考虑

$$
\frac{P_p(z)}{Q_m(z)}e^{ikz}.
$$

指数在上半平面衰减。借助第 5.14.2 节的估计，次数条件可以放宽为

$$
\boxed{p\le m-1.}
$$

特别地，当 $p=m-1$ 时，有理因子仅为 $O(1/z)$，但指数因子使大圆弧积分仍趋于零。实轴上的振荡尾部积分由 Dirichlet 判别法等收敛，未必绝对收敛。当 $k<0$ 时应改用下半平面；此时闭合围道方向为顺时针，留数定理带负号。

上述条件是这类方法常用的充分条件，不能在忽略实轴极点、围道方向及半轴与整轴关系的情况下直接套用。

## 5.16 Dirichlet 积分与参数处的间断

### 5.16.1 积分结果

将前面例子的参数形式上取 $a=b=0$，会得到

$$
D(k)=\int_0^\infty\frac{\sin(kx)}x\,dx.
$$

在 $x=0$ 处，被积函数的极限为 $k$，原点并不妨碍实积分收敛；当 $k\ne0$ 时，无穷远处由 Dirichlet 判别法保证条件收敛。结果为

$$
\boxed{D(k)=
\begin{cases}
\pi/2,&k>0,\\
0,&k=0,\\
-\pi/2,&k<0.
\end{cases}}
$$

这里的 $a=b=0$ 超出了此前 $a,b>0$ 的条件，所以应单独证明，不能只靠形式代入。

### 5.16.2 补全证明：绕开原点的小半圆

先设 $k>0$。取 $F(z)=e^{ikz}/z$，以实轴线段 $[-R,-\varepsilon]$、$[\varepsilon,R]$、上半平面的大半圆，以及绕开原点的小上半圆组成围道。小圆弧按顺时针方向从 $-\varepsilon$ 走向 $\varepsilon$，因此原点被排除在围道内部，内部没有极点。

大圆弧积分由指数衰减估计趋于零。对小圆弧令 $z=\varepsilon e^{i\theta}$，$\theta$ 从 $\pi$ 降至 $0$，则

$$
\int_{C_\varepsilon}F(z)\,dz
=i\int_\pi^0e^{ik\varepsilon e^{i\theta}}\,d\theta
\longrightarrow-i\pi.
$$

由闭围道积分为零，得到

$$
\lim_{\substack{R\to\infty\\\varepsilon\to0^+}}
\left(\int_{-R}^{-\varepsilon}+
\int_\varepsilon^R\right)\frac{e^{ikx}}x\,dx=i\pi.
$$

左侧实部因奇性抵消，虚部为 $2\int_\varepsilon^R\sin(kx)/x\,dx$，故 $D(k)=\pi/2$。再用 $D(-k)=-D(k)$ 及 $D(0)=0$，即得全部结果。

### 5.16.3 为什么积分结果在零处跳跃

对每个固定 $x>0$，$\sin(kx)/x$ 关于 $k$ 连续；但积分后的函数 $D(k)$ 在 $k=0$ 处左右极限分别为 $-\pi/2$ 与 $\pi/2$，是跳跃间断点（第一类间断点）。

原因在于积分区间无界，不能仅凭逐点连续就交换参数极限与反常积分。更具体地，任给固定 $R>0$，当 $k\to0^+$ 时，

$$
\int_0^R\frac{\sin(kx)}x\,dx\longrightarrow0,
\qquad
\int_R^\infty\frac{\sin(kx)}x\,dx\longrightarrow\frac\pi2.
$$

尾部并未对靠近 $0$ 的参数一致变小，因此反常积分在这里不具备所需的一致收敛性。

## 5.17 应用：分母为一加偶次幂

计算

$$
L_n=\int_0^\infty\frac{dx}{1+x^{2n}},
\qquad n\in\mathbb N^+.
$$

### 5.17.1 偶性与上半圆围道

被积函数为偶函数，且在实轴上没有奇点，所以

$$
L_n=\frac12\int_{-\infty}^{\infty}\frac{dx}{1+x^{2n}}.
$$

取 $R>1$，用实轴线段 $[-R,R]$ 与正向上半圆弧 $C_R$ 闭合围道。圆弧上

$$
\left|\int_{C_R}\frac{dz}{1+z^{2n}}\right|
\le\frac{\pi R}{R^{2n}-1}\longrightarrow0.
$$

因此整轴积分可由上半平面内的留数之和求出。

### 5.17.2 上半平面的全部极点

由

$$
z^{2n}=-1=e^{i(2k+1)\pi},
$$

上半平面内恰有 $n$ 个根，统一记为

$$
z_k=e^{i(2k+1)\pi/(2n)},\qquad k=0,1,\ldots,n-1.
$$

它们的辐角均在 $(0,\pi)$ 内，都是一阶极点。若改从 $k=1$ 编号，应写 $z_k=e^{i(2k-1)\pi/(2n)}$，$k=1,\ldots,n$；两种编号不能混用。

由一阶极点的商函数公式，

$$
\operatorname{Res}\left(\frac1{1+z^{2n}};z_k\right)
=\frac1{2n z_k^{2n-1}}
=-\frac{z_k}{2n}.
$$

最后一步使用了 $z_k^{2n}=-1$，故 $1/z_k^{2n-1}=-z_k$。于是

$$
L_n=\frac12\cdot2\pi i
\sum_{k=0}^{n-1}\left(-\frac{z_k}{2n}\right)
=-\frac{\pi i}{2n}\sum_{k=0}^{n-1}z_k.
$$

### 5.17.3 用等比数列求极点之和

令 $\alpha=\pi/(2n)$，$q=e^{i\pi/n}=e^{2i\alpha}$，则 $z_k=e^{i\alpha}q^k$。由于 $q^n=-1$，有

$$
\begin{aligned}
\sum_{k=0}^{n-1}z_k
&=e^{i\alpha}\frac{1-q^n}{1-q}
=\frac{2e^{i\alpha}}{1-e^{2i\alpha}}\\
&=\frac{2e^{i\alpha}}{-2i e^{i\alpha}\sin\alpha}
=\frac{i}{\sin\alpha}.
\end{aligned}
$$

代回得到

$$
\boxed{L_n=\int_0^\infty\frac{dx}{1+x^{2n}}
=\frac{\pi}{2n\sin\bigl(\pi/(2n)\bigr)},
\qquad n\ge1.}
$$

例如，$L_1=\pi/2$，与反正切积分一致；$L_2=\pi/(2\sqrt2)$。这里的因子 $1/2$ 来自偶性，留数中的负号来自 $z_k^{2n}=-1$，计算时都应保留。
