# 第一章 复数与初等函数

## 1.1 数集与复数

常见数集：

- $\mathbb C$：复数集合；
- $\mathbb R$：实数集合；
- $\mathbb Z$：整数集合；
- $\mathbb N^+$：正整数集合；
- $\mathbb Q$：有理数集合；
- $\mathbb H$：四元数集合。

它们之间有包含关系

$$
\mathbb N^+\subset\mathbb Z\subset\mathbb Q\subset\mathbb R
\subset\mathbb C\subset\mathbb H.
$$

## 1.2 复数的表示

设非零复数

$$
z=x+iy=(x,y)\ne(0,0),
$$

其模为

$$
r=|z|=\sqrt{x^2+y^2}.
$$

在复平面中，若 $\theta$ 为 $z$ 的辐角，则

$$
x=r\cos\theta,\qquad y=r\sin\theta,
$$

所以

$$
z=x+iy=r(\cos\theta+i\sin\theta).
$$

由欧拉公式

$$
e^{i\theta}=\cos\theta+i\sin\theta,
$$

可得复数的指数形式

$$
z=re^{i\theta}.
$$

若取 $0\le\theta<2\pi$，则

$$
\tan\theta=\frac yx,
\qquad
\theta=\arg z.
$$

> 不能在所有象限中都直接写成 $\theta=\arctan(y/x)$；辐角还需要结合 $x,y$ 的符号确定。

## 1.3 复数的运算与几何意义

### 1.3.1 加法与减法

设

$$
z_1=x_1+iy_1=(x_1,y_1),\qquad
z_2=x_2+iy_2=(x_2,y_2),
$$

则

$$
z_1\pm z_2
=(x_1\pm x_2)+i(y_1\pm y_2)
=(x_1\pm x_2,\,y_1\pm y_2).
$$

在复平面中，复数加法满足平行四边形法则；$z_1+z_2$ 是以 $z_1,z_2$ 为邻边的平行四边形的对角线，而 $z_1-z_2$ 表示从点 $z_2$ 指向点 $z_1$ 的向量。

### 1.3.2 指数形式下的乘法与除法

设

$$
z_1=r_1e^{i\theta_1},\qquad
z_2=r_2e^{i\theta_2}.
$$

乘法为

$$
z_1z_2=r_1r_2e^{i(\theta_1+\theta_2)},
$$

因而

$$
|z_1z_2|=|z_1||z_2|,
\qquad
\arg(z_1z_2)=\arg z_1+\arg z_2
\pmod{2\pi}.
$$

当 $z_1\ne0$ 时，除法为

$$
\frac{z_2}{z_1}
=\frac{r_2e^{i\theta_2}}{r_1e^{i\theta_1}}
=\frac{r_2}{r_1}e^{i(\theta_2-\theta_1)},
$$

所以

$$
\left|\frac{z_2}{z_1}\right|
=\frac{|z_2|}{|z_1|},
\qquad
\arg\frac{z_2}{z_1}
=\arg z_2-\arg z_1
\pmod{2\pi}.
$$

### 1.3.3 复数的四次方根与旋转

设待开方的复数为

$$
w=r^4e^{i\theta},
\qquad r>0.
$$

由于复数的辐角相差 $2k\pi$ 时表示同一个复数，

$$
w=r^4e^{i(\theta+2k\pi)},
\qquad k\in\mathbb Z.
$$

若 $z^4=w$，则 $w$ 的四个四次方根为

$$
\boxed{
z_k=r e^{i\frac{\theta+2k\pi}{4}}
},
\qquad k=0,1,2,3.
$$

一般地，非零复数 $w=\rho e^{i\theta}$（$\rho>0$）有**恰好 $n$ 个互异的 $n$ 次方根**，应逐个记为

$$
z_k=\rho^{1/n}e^{i(\theta+2k\pi)/n},
\qquad k=0,1,\ldots,n-1.
$$

当 $w=0$ 时仅有一个根 $z=0$。这里的「$n$ 个根」针对整数 $n$ 次开方；后文用多值对数定义无理指数的复数幂时，则可能得到**无穷多个值**，同样可记作 $z_k$（$k\in\mathbb Z$）。

写成三角形式即

$$
z_k
=r\left(
\cos\frac{\theta+2k\pi}{4}
+i\sin\frac{\theta+2k\pi}{4}
\right).
$$

相邻两个根的比值为

$$
\frac{z_{k+1}}{z_k}
=e^{i\frac{2\pi}{4}}
=e^{i\pi/2}
=i,
$$

所以

$$
z_{k+1}=iz_k.
$$

这说明四个根的模均为 $r$，辐角依次相差 $\pi/2$，因此它们是圆周上一个正方形的四个顶点。

一般地，若

$$
z_0=r_0e^{i\theta_0},
$$

则

$$
z_0e^{i\varphi}
=r_0e^{i(\theta_0+\varphi)}.
$$

因此，复数乘以 $e^{i\varphi}$ 的几何意义是：保持模不变，并绕原点逆时针旋转角 $\varphi$。特别地，

$$
i=e^{i\pi/2},\qquad
i^2=e^{i\pi}=-1,\qquad
i^4=e^{i2\pi}=1.
$$

### 1.3.4 共轭复数与模

若 $z=x+iy$，则其共轭复数为 $\bar z=x-iy$，并且

$$
z\bar z=|z|^2.
$$

特别地，

$$
|z_1+z_2|^2
=(z_1+z_2)(\bar z_1+\bar z_2)
=z_1\bar z_1+z_1\bar z_2+z_2\bar z_1+z_2\bar z_2,
$$

而

$$
|z_1-z_2|^2
=(z_1-z_2)(\bar z_1-\bar z_2)
=z_1\bar z_1-z_1\bar z_2-z_2\bar z_1+z_2\bar z_2.
$$

将两式相加，得到平行四边形恒等式

$$
\boxed{
|z_1+z_2|^2+|z_1-z_2|^2
=2\left(|z_1|^2+|z_2|^2\right)
}.
$$

### 1.3.5 直线与圆的复数表示

复平面中的点 $(x,y)$ 与复数

$$
z=x+iy,\qquad \bar z=x-iy
$$

一一对应。由此可反解出

$$
x=\frac{z+\bar z}{2},
\qquad
y=\frac{z-\bar z}{2i}.
$$

#### 1.3.5.1 直线的复数表示

平面直线的一般方程为

$$
Ax+By+C=0,
\qquad A,B,C\in\mathbb R,
\qquad (A,B)\ne(0,0).
$$

代入 $x,y$ 的复数表达式，得到

$$
A\frac{z+\bar z}{2}
+B\frac{z-\bar z}{2i}
+C=0.
$$

令

$$
\alpha=\frac{A+iB}{2},
\qquad
\beta=C,
$$

则

$$
\bar\alpha=\frac{A-iB}{2},
$$

故直线可以写成

$$
\boxed{
\bar\alpha z+\alpha\bar z+\beta=0
},
\qquad
\alpha\in\mathbb C\setminus\{0\},
\quad
\beta\in\mathbb R.
$$

因为

$$
\bar\alpha z+\alpha\bar z
=2\operatorname{Re}(\bar\alpha z),
$$

所以也可写成

$$
\operatorname{Re}(\bar\alpha z)=-\frac{\beta}{2}.
$$

#### 1.3.5.2 圆的复数表示

设圆心为

$$
z_0=x_0+iy_0,
$$

半径为 $R>0$。圆上任一点 $z=x+iy$ 满足

$$
|z-z_0|=R.
$$

两边平方：

$$
|z-z_0|^2=R^2.
$$

利用 $|w|^2=w\bar w$，可得

$$
(z-z_0)(\bar z-\bar z_0)=R^2,
$$

即

$$
\boxed{
z\bar z-z\bar z_0-\bar z z_0+|z_0|^2-R^2=0
}.
$$

令

$$
\alpha=-z_0,
\qquad
\beta=|z_0|^2-R^2,
$$

则圆的一般复数方程可写为

$$
\boxed{
z\bar z+\alpha\bar z+\bar\alpha z+\beta=0
},
\qquad
\alpha\in\mathbb C,
\quad
\beta\in\mathbb R.
$$

将左端配方：

$$
|z+\alpha|^2=|\alpha|^2-\beta.
$$

因此，当 $|\alpha|^2-\beta>0$ 时，它表示圆心为

$$
z_0=-\alpha
$$

且半径为

$$
R=\sqrt{|\alpha|^2-\beta}
$$

的圆。

> 当 $|\alpha|^2-\beta=0$ 时，图形退化为单点 $z=-\alpha$；当 $|\alpha|^2-\beta<0$ 时，没有对应的平面点。

### 1.3.6 例题：证明三点构成等边三角形

若

$$
|z_1|=|z_2|=|z_3|=r>0,
\qquad
z_1+z_2+z_3=0,
$$

证明复平面中的三点 $z_1,z_2,z_3$ 构成等边三角形。

由

$$
z_1+z_2=-z_3
$$

可知

$$
|z_1+z_2|=|z_3|=r.
$$

将 $z_1,z_2$ 代入平行四边形恒等式：

$$
\begin{aligned}
|z_1-z_2|^2
&=2\left(|z_1|^2+|z_2|^2\right)-|z_1+z_2|^2\\
&=2(r^2+r^2)-r^2\\
&=3r^2.
\end{aligned}
$$

因此

$$
|z_1-z_2|=\sqrt3\,r.
$$

同理，

$$
|z_2-z_3|=|z_3-z_1|=\sqrt3\,r.
$$

三边相等，故 $z_1,z_2,z_3$ 构成等边三角形。

从几何上看，

$$
z_0=\frac{z_1+z_2+z_3}{3}=0,
$$

即三角形的重心位于圆心；三个顶点又都在半径为 $r$ 的同一圆上，因此它们在圆周上等间隔分布。

### 1.3.7 例题：证明四点构成矩形

设四个互异复数 $z_1,z_2,z_3,z_4$ 按圆周顺序排列，并满足

$$
|z_1|=|z_2|=|z_3|=|z_4|=r>0,
\qquad
z_1+z_2+z_3+z_4=0.
$$

证明以 $z_1,z_2,z_3,z_4$ 为顶点的四边形是矩形。

### 证明

按照提示，构造以 $z_1,z_2,z_3,z_4$ 为根的四次多项式

$$
f(z)=\prod_{j=1}^{4}(z-z_j).
$$

展开得

$$
f(z)
=z^4-s_1z^3+s_2z^2-s_3z+s_4,
$$

其中

$$
s_1=z_1+z_2+z_3+z_4=0
$$

且

$$
s_3
=z_1z_2z_3+z_1z_2z_4+z_1z_3z_4+z_2z_3z_4.
$$

因为 $|z_j|=r$，所以

$$
z_j\bar z_j=r^2,
\qquad
\bar z_j=\frac{r^2}{z_j}.
$$

对 $z_1+z_2+z_3+z_4=0$ 取共轭，得到

$$
\bar z_1+\bar z_2+\bar z_3+\bar z_4=0.
$$

代入 $\bar z_j=r^2/z_j$，再除以 $r^2$，可得

$$
\frac1{z_1}+\frac1{z_2}+\frac1{z_3}+\frac1{z_4}=0.
$$

由于各 $z_j\ne0$，两边乘以 $z_1z_2z_3z_4$，便有

$$
s_3
=z_2z_3z_4+z_1z_3z_4+z_1z_2z_4+z_1z_2z_3
=0.
$$

因此

$$
f(z)=z^4+s_2z^2+s_4,
$$

它是偶函数，即

$$
f(-z)=f(z).
$$

所以，只要 $z_j$ 是 $f$ 的根，$-z_j$ 也是 $f$ 的根。四个根因而组成两对关于原点对称的点。由于 $z_1,z_2,z_3,z_4$ 已按圆周顺序排列，相对的顶点必满足

$$
z_3=-z_1,
\qquad
z_4=-z_2.
$$

于是两条对角线的中点都是原点：

$$
\frac{z_1+z_3}{2}
=\frac{z_2+z_4}{2}
=0.
$$

所以该四边形是平行四边形。同时，

$$
|z_1-z_3|=2r,
\qquad
|z_2-z_4|=2r,
$$

即它的两条对角线相等。对角线相等的平行四边形是矩形，故

$$
\boxed{z_1z_2z_3z_4\text{ 构成矩形}}.
$$

> 条件中的编号必须按圆周顺序排列。
>
> 如果任意打乱四个顶点的编号，依次连接后可能得到自交四边形。
>
> 在这种编号下，依次连接所得图形不能称为矩形。

### 1.3.8 模相等的根何时构成正多边形

设 $m$ 次首一多项式

$$
f_m(z)
=\prod_{k=1}^{m}(z-z_k)
=z^m+a_{m-1}z^{m-1}+\cdots+a_1z+a_0,
$$

且所有根的模相等：

$$
|z_1|=|z_2|=\cdots=|z_m|=r>0.
$$

问题是：需要对系数施加多少个条件，才能保证这些根在复平面中构成正 $m$ 边形？

#### 1.3.8.1 正多边形对应的多项式

若 $z_1,\ldots,z_m$ 构成以原点为中心的正 $m$ 边形，则存在 $\rho$，使

$$
z_k=\rho\omega^k,
\qquad
\omega=e^{2\pi i/m}.
$$

因此所有顶点都满足

$$
z_k^m=\rho^m.
$$

它们正好是方程

$$
z^m-\rho^m=0
$$

的全部根，所以

$$
f_m(z)=z^m-\rho^m.
$$

反过来，如果

$$
f_m(z)=z^m+a_0,
$$

则其根可以写成

$$
z_k=(-a_0)^{1/m}e^{2k\pi i/m},
\qquad k=0,1,\ldots,m-1.
$$

这些根的模相等、相邻辐角相差 $2\pi/m$，故构成正 $m$ 边形。于是

$$
\boxed{
z_1,\ldots,z_m\text{ 构成正 }m\text{ 边形}
\iff
a_1=a_2=\cdots=a_{m-1}=0
}.
$$

表面上需要令 $m-1$ 个中间系数全部为零；但是在所有根模相等的前提下，前后对应的系数并不独立。

#### 1.3.8.2 模相等时的系数关系

记 $e_j$ 为根 $z_1,\ldots,z_m$ 的第 $j$ 个初等对称多项式：

$$
e_j
=\sum_{1\le k_1<\cdots<k_j\le m}
z_{k_1}\cdots z_{k_j}.
$$

由韦达定理，

$$
a_{m-j}=(-1)^je_j,
\qquad
a_0=(-1)^me_m.
$$

因为 $|z_k|=r$，所以

$$
\bar z_k=\frac{r^2}{z_k}.
$$

从而

$$
\begin{aligned}
\overline{e_j}
&=\sum_{1\le k_1<\cdots<k_j\le m}
\bar z_{k_1}\cdots\bar z_{k_j}\\
&=r^{2j}
\sum_{1\le k_1<\cdots<k_j\le m}
\frac{1}{z_{k_1}\cdots z_{k_j}}\\
&=r^{2j}\frac{e_{m-j}}{e_m}.
\end{aligned}
$$

因此

$$
e_{m-j}=\frac{e_m}{r^{2j}}\overline{e_j}.
$$

将韦达关系代入，得到

$$
\boxed{
a_jr^{2j}=a_0\overline{a_{m-j}},
\qquad j=0,1,\ldots,m
}.
$$

特别地，

$$
|a_0|=r^m.
$$

由于 $a_0\ne0$，上述关系说明

$$
\boxed{
a_j=0\iff a_{m-j}=0
}.
$$

这就是只需检查一半中间系数的原因。

#### 1.3.8.3 偶数次多项式

令 $m=2n$：

$$
f_{2n}(z)
=z^{2n}+a_{2n-1}z^{2n-1}
+\cdots+a_1z+a_0.
$$

各中间系数按照

$$
(a_1,a_{2n-1}),\ 
(a_2,a_{2n-2}),\ 
\ldots,\ 
(a_{n-1},a_{n+1})
$$

两两配对，而 $a_n$ 是中间系数，与自身对应。

因此，只需施加下面 $n$ 个系数条件：

$$
\boxed{
a_1=a_2=\cdots=a_n=0
}.
$$

由 $a_j=0\iff a_{2n-j}=0$，立即得到

$$
a_{n+1}=a_{n+2}=\cdots=a_{2n-1}=0.
$$

于是

$$
f_{2n}(z)=z^{2n}+a_0,
$$

其 $2n$ 个根构成正 $2n$ 边形。

> 这里所说的“$n$ 个条件”是 $n$ 个系数等式。若按独立实条件计数，前 $n-1$ 个是复条件，而中间条件 $a_n=0$ 只消去一个剩余的实自由度，共有 $2n-1$ 个独立实条件。

#### 1.3.8.4 奇数次多项式

令 $m=2n+1$：

$$
f_{2n+1}(z)
=z^{2n+1}+a_{2n}z^{2n}
+\cdots+a_1z+a_0.
$$

此时所有中间系数均两两配对：

$$
(a_1,a_{2n}),\ 
(a_2,a_{2n-1}),\ 
\ldots,\ 
(a_n,a_{n+1}).
$$

同样只需施加 $n$ 个系数条件：

$$
\boxed{
a_1=a_2=\cdots=a_n=0
}.
$$

系数配对关系随即给出

$$
a_{n+1}=a_{n+2}=\cdots=a_{2n}=0.
$$

故

$$
f_{2n+1}(z)=z^{2n+1}+a_0,
$$

其 $2n+1$ 个根构成正 $(2n+1)$ 边形。

> 对奇数次多项式，这 $n$ 个条件都是复条件，共相当于 $2n$ 个独立实条件。

综上，在“所有根的模已经相等”的前提下：

$$
\boxed{
\begin{array}{c|c}
\text{多项式次数} & \text{只需检查的条件}\\
\hline
2n & a_1=a_2=\cdots=a_n=0\\
2n+1 & a_1=a_2=\cdots=a_n=0
\end{array}
}
$$

两种情形都只需要检查 $n$ 个系数条件。

### 1.3.9 重要例题：圆盘上 $|z^n+\alpha|$ 的最值

\begin{center}
\fcolorbox{red}{white}{
\parbox{0.88\linewidth}{
\color{red}\bfseries
设 $n\in\mathbb N^+$、$r\ge0$、$\alpha\in\mathbb C$，且 $|z|\le r$。
求函数
\[
f(z)=|z^n+\alpha|
\]
的最大值、最小值及相应的取值条件。
}}
\end{center}

> **板书标准答案（两张照片）：**以下按 $\alpha=0$、$\alpha\ne0$ 以及 $|\alpha|$ 与 $r^n$ 的大小关系完整写出证明和全部取等点；取等点用 $z_k$ 编号。此处 $r=0$ 时圆盘只有 $z=0$，所有结论也成立。

#### 1.3.9.1 转化为圆盘内的距离问题

令

$$
w=z^n.
$$

由 $|z|\le r$ 可知

$$
|w|=|z|^n\le r^n.
$$

反过来，任意满足 $|w|\le r^n$ 的复数 $w$ 都存在一个 $n$ 次方根 $z$，并且

$$
|z|=|w|^{1/n}\le r.
$$

因此，$w=z^n$ 恰好遍历闭圆盘

$$
|w|\le r^n.
$$

原问题等价于：当 $w$ 在该圆盘中变化时，求

$$
|w+\alpha|
$$

的最大值和最小值。几何上，它表示圆盘内的点 $w$ 到固定点 $-\alpha$ 的距离。

#### 1.3.9.2 板书标准答案：最大值及取等条件

由三角不等式，

$$
|z^n+\alpha|
\le |z|^n+|\alpha|
\le r^n+|\alpha|.
$$

所以

$$
\boxed{
f_{\max}=r^n+|\alpha|
}.
$$

当 $\alpha\ne0$ 时，等号成立当且仅当

$$
|z|=r
$$

且 $z^n$ 与 $\alpha$ 同方向，即

$$
\boxed{
z^n=r^n\frac{\alpha}{|\alpha|}
}.
$$

若

$$
\alpha=|\alpha|e^{i\theta},
$$

则最大值在

$$
\boxed{
z_k=r e^{i(\theta+2k\pi)/n},
\qquad k=0,1,\ldots,n-1
}
$$

处取得。

若 $\alpha=0$，则

$$
f(z)=|z|^n,
$$

最大值 $r^n$ 在整个边界 $|z|=r$ 上取得（$r=0$ 时只有 $z=0$）。

#### 1.3.9.3 板书标准答案：最小值及取等条件

最小值取决于点 $-\alpha$ 是否位于圆盘 $|w|\le r^n$ 内。

先看 $\alpha=0$：这时 $f(z)=|z|^n$，最小值为 $0$，当且仅当 $z=0$ 时取得。下文设 $\alpha\ne0$，写成 $\alpha=|\alpha|e^{i\theta}$。

#### 情形一：$|\alpha|\le r^n$

此时可以取

$$
w=z^n=-\alpha,
$$

因此

$$
\boxed{
f_{\min}=0
}.
$$

用板书中的方程 $z^n+\alpha=0$ 求出所有取等点：

$$
z^n=-\alpha=|\alpha|e^{i(\theta+\pi+2k\pi)}.
$$

因此最小值在

$$
\boxed{
z_k
=|\alpha|^{1/n}
e^{i(\theta+\pi+2k\pi)/n},
\qquad k=0,1,\ldots,n-1
}
$$

处取得。

- 若 $|\alpha|<r^n$，这些点位于圆盘内部；
- 若 $|\alpha|=r^n$，这些点位于边界 $|z|=r$；
- $\alpha=0$ 的情形已在本节开头单独处理。

#### 情形二：$|\alpha|>r^n$

此时 $-\alpha$ 位于圆盘外。由反三角不等式，

$$
|z^n+\alpha|
\ge |\alpha|-|z|^n
\ge |\alpha|-r^n.
$$

故

$$
\boxed{
f_{\min}=|\alpha|-r^n
}.
$$

等号成立当且仅当 $|z|=r$，且 $z^n$ 与 $\alpha$ 方向相反，即

$$
\boxed{
z^n=-r^n\frac{\alpha}{|\alpha|}
}.
$$

按板书的向量作法，令 $z'=z^n+\alpha$。取等时 $z^n=-r^ne^{i\theta}$，于是

$$
z'=\alpha-r^ne^{i\theta}
=(|\alpha|-r^n)e^{i\theta},
\qquad |z'|=|\alpha|-r^n>0.
$$

板书再把 $z^n=-r^ne^{i\theta}$ 写成 $z^n=r^ne^{i(\theta+\pi+2k\pi)}$；因此最小值在

$$
\boxed{
z_k=r e^{i(\theta+\pi+2k\pi)/n},
\qquad k=0,1,\ldots,n-1
}
$$

处取得。

#### 1.3.9.4 结论

$$
\boxed{
\max_{|z|\le r}|z^n+\alpha|
=|\alpha|+r^n
}
$$

且

$$
\boxed{
\min_{|z|\le r}|z^n+\alpha|
=\max\{|\alpha|-r^n,0\}
}.
$$

因为 $f$ 连续且圆盘 $|z|\le r$ 是连通集，所以 $f$ 的值域是闭区间

$$
\boxed{
\max\{|\alpha|-r^n,0\}
\le f(z)\le
|\alpha|+r^n
}.
$$

## 1.4 复对数

设 $z=x+iy\ne0$，写成

$$
z=|z|e^{i\theta},\qquad
|z|=\sqrt{x^2+y^2},\qquad
\theta=\operatorname{Arg}z\in(-\pi,\pi].
$$

由于 $e^{i(\theta+2k\pi)}=e^{i\theta}$，满足 $e^w=z$ 的所有 $w$ 构成**多值复对数**：

$$
\boxed{\log z
=\left\{\ln|z|+i(\operatorname{Arg}z+2k\pi):k\in\mathbb Z\right\}.}
$$

取 $k=0$ 的一个值称为此处约定的**主值**：

$$
\boxed{\operatorname{Ln}z=\ln|z|+i\operatorname{Arg}z
=\frac12\ln(x^2+y^2)+i\operatorname{Arg}(x+iy).}
$$

因此可简记为 $\log z=\operatorname{Ln}z+2k\pi i$（$k\in\mathbb Z$），但须记住左侧表示一组值。特别地，仅在 $x>0$ 时，才可直接将 $\operatorname{Arg}(x+iy)$ 写成 $\arctan(y/x)$；其他象限须作辐角修正，$x=0$ 时该商也没有定义。

## 1.5 计算 $\ln(-1)$

取主值辐角 $\operatorname{Arg}(-1)=\pi$，则

$$
\begin{aligned}
\operatorname{Ln}(-1)
&=\ln|-1|+i\pi\\
&=\ln 1+i\pi\\
&=i\pi.
\end{aligned}
$$

从而，当 $x>0$ 时，

$$
\operatorname{Ln}(-x)=i\pi+\ln x.
$$

若考虑复对数的全部取值，则

$$
\log(-1)=\{i(2k+1)\pi:k\in\mathbb Z\}.
$$

## 1.6 复数幂与多值性

### 1.6.1 定义及与主值的区别

当 $a\in\mathbb C\setminus\{0\}$、$b\in\mathbb C$ 时，借助**全部对数值**定义复数幂：

$$
\boxed{a^b
=\left\{\exp\!\left[b\bigl(\operatorname{Ln}a+2k\pi i\bigr)\right]:k\in\mathbb Z\right\}.}
$$

这通常是一个多值集合。若**只取** $\exp(b\operatorname{Ln}a)$，得到的是按所选分支定义的一个主值。

本节讨论多值定义；计算时需要说明采用哪一种。若 $b$ 为整数，所有分支给出相同值，回到通常的整数次幂。

**关于取值个数和记号：**整数 $n$ 次开方（非零底数的 $n$ 次方根）恰有 $n$ 个值，记为 $z_0,\ldots,z_{n-1}$；无理指数的复数幂有无穷多个值，可记为 $z_k$（$k\in\mathbb Z$）。因此在求全部值时不能只写一个无下标的 $z$；是否有重复值仍须按指数差是否为 $2\pi i$ 的整数倍判定。

### 1.6.2 有理指数：有限多个值

第一张板书以 $1^{q/p}$ 为例。设 $p,q\in\mathbb N^+$，则

$$
1^{q/p}
=\left\{\exp\!\left(\frac{q}{p}\,2k\pi i\right):k\in\mathbb Z\right\}
=\left\{\cos\frac{2kq\pi}{p}
+i\sin\frac{2kq\pi}{p}:k\in\mathbb Z\right\}.
$$

若 $\gcd(p,q)=1$，取 $k=0,1,\ldots,p-1$ 恰好得到 $p$ 个互不相同的值，它们是单位圆上的 $p$ 次单位根。

若 $p,q$ 未约分，不同值的个数为 $p/\gcd(p,q)$。例如 $1^{1/n}$ 有 $n$ 个值；其中 $1^{1/4}=\{1,i,-1,-i\}$。

### 1.6.3 无理指数：无穷多个值

板书以 $i^{\sqrt2}$ 为例。由 $\operatorname{Ln}i=i\pi/2$，

$$
i^{\sqrt2}
=\left\{\exp\!\left[i\sqrt2\left(\frac{\pi}{2}+2k\pi\right)\right]:k\in\mathbb Z\right\}.
$$

若第 $k$ 个值与第 $j$ 个值相同，则

$$
e^{2\pi i\sqrt2(k-j)}=1
\quad\Longrightarrow\quad
\sqrt2(k-j)\in\mathbb Z.
$$

由于 $\sqrt2$ 是无理数，只能有 $k=j$。因此这些值**两两不同，有无穷多个**，且模都为 $1$；它们在单位圆上稠密。

注意：不能仅凭指数写法不同就断言复数不同。若 $u-v\in2\pi i\mathbb Z$，则 $e^u=e^v$。

另一个例子为正实数的无理次幂。即使底数 $\sqrt2>0$，在多值定义下仍有

$$
(\sqrt2)^{\sqrt2}
=\left\{\exp\!\left[\sqrt2\bigl(\ln\sqrt2+2k\pi i\bigr)\right]:k\in\mathbb Z\right\}
=\left\{e^{\sqrt2\ln\sqrt2}e^{2k\sqrt2\pi i}:k\in\mathbb Z\right\}.
$$

它的值两两不同，模均为 $e^{\sqrt2\ln\sqrt2}$。

通常实数运算中写的 $(\sqrt2)^{\sqrt2}>0$，是上述集合中 $k=0$ 的值，并非整个多值集合。

### 1.6.4 复指数例子：$e^{\,x+iy}$

若将底数 $e$ 按多值复数幂处理，并设 $b=x+iy$（$x,y\in\mathbb R$），则

$$
\operatorname{Ln}e=1,\qquad
e^{\,b}
=\left\{\exp\!\left[(x+iy)(1+2k\pi i)\right]:k\in\mathbb Z\right\}
=\left\{e^{x-2k\pi y}e^{i(y+2k\pi x)}:k\in\mathbb Z\right\}.
$$

当 $y\ne0$ 时，这些值具有不同的模，因而有无穷多个；当 $y=0$ 且 $x$ 为有理数时，只得到有限多个值。

**不要把这里的多值复数幂 $e^{\,b}$ 与单值指数函数 $\exp(b)$ 混为一谈**：后者始终只有一个函数值。

## 1.7 欧拉公式与指数函数展开

欧拉公式及其共轭形式为

$$
e^{i\theta}=\cos\theta+i\sin\theta,
\qquad
e^{-i\theta}=\cos\theta-i\sin\theta.
$$

因此，

$$
\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},
\qquad
\sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}.
$$

指数函数的幂级数展开为

$$
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!}.
$$

## 1.8 正弦函数与余弦函数的无穷乘积

$$
\sin x=x\prod_{n=1}^{\infty}\left(1-\frac{x^2}{n^2\pi^2}\right).
$$

两边取对数，得到

$$
\ln(\sin x)
=\ln x+
\sum_{n=1}^{\infty}
\ln\left(1-\frac{x^2}{n^2\pi^2}\right).
$$

余弦函数的无穷乘积为

$$
\cos x=
\prod_{n=0}^{\infty}
\left[
1-\frac{x^2}{\left(n+\frac12\right)^2\pi^2}
\right].
$$

由正弦函数的无穷乘积，

$$
\frac{\sin x}{x}
=\prod_{n=1}^{\infty}
\left(1-\frac{x^2}{n^2\pi^2}\right),
$$

并且

$$
\lim_{x\to0}\frac{\sin x}{x}=1.
$$

## 1.9 由复幂级数求三角级数

### 1.9.1 从 $-\ln(1-z)$ 出发

在 $|z|<1$ 内定义

$$
F(z)=\sum_{n=1}^{\infty}\frac{z^n}{n}.
$$

幂级数在收敛圆内可逐项求导，因此

$$
F'(z)=\sum_{n=1}^{\infty}z^{n-1}
=\sum_{m=0}^{\infty}z^m
=\frac{1}{1-z}.
$$

又 $F(0)=0$，且 $1-z$ 在单位圆盘内位于右半平面，可以取解析的对数主值，得到

$$
\boxed{F(z)=-\operatorname{Ln}(1-z),\qquad |z|<1.}
$$

这也可写成 $F(z)=\int_0^z (1-\zeta)^{-1}\,d\zeta$，其中积分路径完全位于 $|\zeta|<1$。

### 1.9.2 取实部与虚部

令 $z=re^{i\theta}$，其中 $0\le r<1$、$0<\theta<2\pi$。由欧拉公式，

$$
F(re^{i\theta})=f_r(\theta)+i g_r(\theta),
$$

其中

$$
f_r(\theta)=\sum_{n=1}^{\infty}\frac{r^n\cos(n\theta)}{n},
\qquad
g_r(\theta)=\sum_{n=1}^{\infty}\frac{r^n\sin(n\theta)}{n}.
$$

写 $1-re^{i\theta}=(1-r\cos\theta)-ir\sin\theta$。因为 $1-r\cos\theta>0$，其主辐角可直接用反正切表示：

$$
\operatorname{Arg}(1-re^{i\theta})
=-\arctan\frac{r\sin\theta}{1-r\cos\theta}.
$$

把 $F=-\operatorname{Ln}(1-z)$ 的实部、虚部分别写出，得到板书的两条公式：

$$
\boxed{\sum_{n=1}^{\infty}\frac{r^n\cos(n\theta)}{n}
=-\frac12\ln\!\left(1-2r\cos\theta+r^2\right),}
$$

$$
\boxed{\sum_{n=1}^{\infty}\frac{r^n\sin(n\theta)}{n}
=\arctan\frac{r\sin\theta}{1-r\cos\theta}.}
$$

### 1.9.3 令 $r\to1^-$：单位圆上的级数

固定 $0<\theta<2\pi$。部分和 $\sum_{n=1}^N e^{in\theta}$ 有界，而 $1/n$ 单调趋于 $0$，所以狄利克雷判别法保证 $\sum_{n\ge1}e^{in\theta}/n$ 收敛。由阿贝尔定理，它的和等于 $F(re^{i\theta})$ 在 $r\to1^-$ 时的极限；因此可以对上式**取极限**。这里不能直接把 $r=1$ 代入只在 $|z|<1$ 内建立的幂级数等式。

于是

$$
\sum_{n=1}^{\infty}\frac{\cos(n\theta)}{n}
=-\frac12\ln(2-2\cos\theta).
$$

利用 $2-2\cos\theta=4\sin^2(\theta/2)$ 及 $\sin(\theta/2)>0$，可改写为

$$
\boxed{\sum_{n=1}^{\infty}\frac{\cos(n\theta)}{n}
=-\ln\!\left(2\sin\frac{\theta}{2}\right),
\qquad 0<\theta<2\pi.}
$$

虚部的极限为 $\arctan\!\bigl(\sin\theta/(1-\cos\theta)\bigr)$。由半角公式，

$$
\frac{\sin\theta}{1-\cos\theta}
=\cot\frac{\theta}{2},
\qquad 0<\frac{\theta}{2}<\pi,
$$

故反正切取 $(-\pi/2,\pi/2)$ 中的值时，

$$
\boxed{\sum_{n=1}^{\infty}\frac{\sin(n\theta)}{n}
=\frac{\pi-\theta}{2},
\qquad 0<\theta<2\pi.}
$$

例如取 $\theta=\pi/2$，由余弦级数公式得

$$
\boxed{\sum_{n=1}^{\infty}\frac{\cos(n\pi/2)}{n}
=-\frac12\ln 2.}
$$

在 $\theta=0$（或 $2\pi$）时，余弦级数变为发散的调和级数；上述边界公式不适用于这些端点。

### 1.9.4 再积分一次：平方分母的级数

先在 $0<\theta<2\pi$ 内积分上一节的正弦级数。为了说明逐项积分，可以先给每项乘以 $r^n$（$0<r<1$），逐项积分后再令 $r\to1^-$。左边的积分级数因分母为 $n^2$ 而一致收敛；右边的带 $r$ 和式绝对值不超过 $\pi/2$，可用有界收敛定理取极限。因此

$$
\begin{aligned}
\sum_{n=1}^{\infty}\frac{1-\cos(n\theta)}{n^2}
&=\int_0^\theta\frac{\pi-t}{2}\,dt\\
&=\frac{\pi\theta}{2}-\frac{\theta^2}{4}.
\end{aligned}
$$

等式在 $\theta=0,2\pi$ 也由连续性成立。若记 $S=\sum_{n=1}^{\infty}1/n^2$，则移项后还需要知道这个**平方倒数和**：

$$
\sum_{n=1}^{\infty}\frac{\cos(n\theta)}{n^2}
=S-\frac{\pi\theta}{2}+\frac{\theta^2}{4}.
$$

此时使用第 1.8 节已记录的正弦无穷乘积。在 $x=0$ 附近，将它与泰勒级数都展开到二次项：

$$
\frac{\sin x}{x}
=\prod_{n=1}^{\infty}\left(1-\frac{x^2}{n^2\pi^2}\right)
=1-\frac{x^2}{\pi^2}S+O(x^4),
$$

$$
\frac{\sin x}{x}
=1-\frac{x^2}{3!}+\frac{x^4}{5!}-\cdots.
$$

乘积中涉及至少两个因子的交叉项均为 $O(x^4)$。比较 $x^2$ 系数，先求得

$$
\boxed{S=\sum_{n=1}^{\infty}\frac1{n^2}=\frac{\pi^2}{6}.}
$$

把这个值代入前面的含 $S$ 公式，才得到板书要算的余弦级数：

$$
\boxed{\sum_{n=1}^{\infty}\frac{\cos(n\theta)}{n^2}
=\frac{\pi^2}{6}-\frac{\pi\theta}{2}+\frac{\theta^2}{4},
\qquad 0\le\theta\le2\pi.}
$$

**详细计算 $\sum\sin(n\theta)/n^2$。** 记

$$
H(\theta)=\sum_{n=1}^{\infty}\frac{\sin(n\theta)}{n^2}.
$$

因 $\sum 1/n^2$ 收敛，此级数关于实数 $\theta$ 一致收敛。不能直接对它逐项求导并无条件得到 $\sum\cos(n\theta)/n$；先取 $0<r<1$，定义

$$
H_r(\theta)=\sum_{n=1}^{\infty}\frac{r^n\sin(n\theta)}{n^2},
\qquad H_r(0)=0.
$$

由于 $r<1$，可以逐项求导，再代入第 1.9.2 节的余弦公式：

$$
\begin{aligned}
H_r'(t)
&=\sum_{n=1}^{\infty}\frac{r^n\cos(nt)}{n}\\
&=-\frac12\ln(1-2r\cos t+r^2)\\
&=-\frac12\ln\!\left((1-r)^2+4r\sin^2\frac t2\right).
\end{aligned}
$$

从 $0$ 到 $\theta$ 积分，逐项积分得到

$$
H_r(\theta)
=-\frac12\int_0^\theta
\ln\!\left((1-r)^2+4r\sin^2\frac t2\right)\,dt.
$$

现在令 $r\to1^-$。左边由 $\sum 1/n^2<\infty$ 一致趋于 $H(\theta)$。对右边，在 $0<t<2\pi$，对数内的量趋于 $4\sin^2(t/2)$；且当 $r\ge1/2$ 时，上式的对数绝对值可用 $C+2|\ln\sin(t/2)|$ 控制。该函数在 $0$、$2\pi$ 附近分别只有可积的对数奇性。因此可将极限移入积分，得

$$
\boxed{H(\theta)
=-\int_0^\theta\ln\!\left(2\sin\frac t2\right)\,dt,
\qquad 0\le\theta\le2\pi.}
$$

由 $H(0)=H(2\pi)=0$ 也能确认两个端点；在 $0<\theta<2\pi$ 内，还可写成 $H'(\theta)=-\ln(2\sin(\theta/2))$。例如

$$
H(\pi)=0,\qquad
H\!\left(\frac\pi2\right)
=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^2}
=G,
$$

其中 $G$ 为卡塔兰常数；$H(2\pi-\theta)=-H(\theta)$。这个级数通常记为 $\operatorname{Cl}_2(\theta)$（二阶 Clausen 函数），一般不化成前面余弦级数那样的二次多项式。

此外，在 $\theta=\pi$ 处代入第 1.9.3 节的余弦级数公式，得到板书上的交错调和级数：

$$
\boxed{\sum_{n=1}^{\infty}\frac{(-1)^n}{n}
=-\ln 2,\qquad
1-\frac12+\frac13-\frac14+\cdots=\ln2.}
$$

**板书留问：**$\sum_{n=1}^{\infty}1/n^3$ 的值记作 $\zeta(3)$。上面的乘积与 $x^2$ 系数比较法只算出 $\zeta(2)$；正弦除以 $x$ 的展开没有 $x^3$ 项，不能照搬这一步求 $\zeta(3)$。

## 1.10 正弦无穷乘积的进一步应用

### 1.10.1 偶数次倒数和

板书将偶数次倒数和写成

$$
\sum_{n=1}^{\infty}\frac{1}{n^{2k}}=C_k\pi^{2k},
\qquad k=1,2,\ldots,\quad C_k\in\mathbb Q_{>0}.
$$

上一节已经用正弦无穷乘积的 $x^2$ 系数求出 $C_1=1/6$。更高次数也能通过该乘积与 $\sin x/x$ 的泰勒级数比较系数求得；例如

$$
\sum_{n=1}^{\infty}\frac1{n^4}=\frac{\pi^4}{90},
\qquad
\sum_{n=1}^{\infty}\frac1{n^6}=\frac{\pi^6}{945},
\qquad
\sum_{n=1}^{\infty}\frac1{n^8}=\frac{\pi^8}{9450}.
$$

注意比较 $x^4$ 及更高次项时，乘积中会出现不同因子之间的交叉项。例如设 $S_2=\sum_{n\ge1}n^{-2}$、$S_4=\sum_{n\ge1}n^{-4}$，则 $x^4$ 项的系数为

$$
\frac1{\pi^4}\sum_{m<n}\frac1{m^2n^2}
=\frac{S_2^2-S_4}{2\pi^4}
=\frac1{5!}.
$$

代入 $S_2=\pi^2/6$，即得 $S_4=\pi^4/90$。板书中的 $\sum_{n\ge1}n^{-10}$ 可用同样思路继续求系数。

### 1.10.2 在 $x=i\pi$ 处代入无穷乘积

正弦乘积也适用于复数 $x$。令 $x=i\pi$，每个因子变成 $1+1/n^2$，因此

$$
\prod_{n=1}^{\infty}\left(1+\frac1{n^2}\right)
=\frac{\sin(i\pi)}{i\pi}.
$$

由 $\sin z=(e^{iz}-e^{-iz})/(2i)$，有 $\sin(i\pi)=i\sinh\pi$，故

$$
\boxed{\prod_{n=1}^{\infty}\left(1+\frac1{n^2}\right)
=\frac{\sinh\pi}{\pi}
=\frac{e^\pi-e^{-\pi}}{2\pi}.}
$$

## 1.11 初等函数的复平面映射

### 1.11.1 指数函数：水平带映成角域

写 $w=e^z=e^xe^{iy}$。竖线 $x=x_0$ 映成半径为 $e^{x_0}$ 的圆周（竖线上的一段映成圆弧）；横线 $y=y_0$ 映成辐角为 $y_0$ 的射线。对固定 $y$，$x\to-\infty$ 时 $w\to0$，$x\to+\infty$ 时 $|w|\to\infty$。

尤其是水平带 $0<\operatorname{Im}z<\pi$ 经 $e^z$ 一一映成上半平面 $\operatorname{Im}w>0$。一般地，宽度小于 $2\pi$ 的水平带映成相应的角域；若包含跨越 $2\pi$ 的辐角范围，则会因 $e^{z+2\pi i}=e^z$ 而出现重叠。整个复平面的像是 $\mathbb C\setminus\{0\}$。

### 1.11.2 平移、旋转、缩放与斜带

仿射变换 $z\mapsto az+b$（$a\ne0$）依次包含缩放、旋转和平移。若两条斜直线之间的垂直距离为 $h>0$，可以先通过平移与旋转使它们成为 $\operatorname{Im}\zeta=0$ 与 $\operatorname{Im}\zeta=h$，再乘以 $\pi/h$，得到标准水平带 $0<\operatorname{Im}\xi<\pi$。最后使用 $w=e^\xi$，就把斜带映到上半平面。

板书图中，斜线与实轴夹角为 $\theta_0$，截距相差 $b-a$ 时，两条平行线的垂距为 $h=|b-a|\,|\sin\theta_0|$；选择旋转方向时还应保证变换后的带落在 $0<\operatorname{Im}\xi<\pi$ 一侧。

### 1.11.3 幂映射：角度相乘

设 $0<\theta_0<2\pi$。在不包含原点、可连续选取辐角 $0<\arg z<\theta_0$ 的扇形上，选择相应分支定义 $z^\alpha=r^\alpha e^{i\alpha\theta}$（$z=re^{i\theta}$，$\alpha>0$）。于是射线的辐角从 $\theta$ 变为 $\alpha\theta$。取 $\alpha=\pi/\theta_0$，可把角度为 $\theta_0$ 的扇形一一映成上半平面。

若 $\alpha$ 不是整数，$z^\alpha$ 需要先指定对数分支。一般的幂映射若把辐角区间放大到宽度超过 $2\pi$，像会绕原点重叠；上面取 $\alpha=\pi/\theta_0$ 时，像的辐角范围恰为 $(0,\pi)$，所以没有这种重叠。

## 1.12 方程 $\cos z=A+iB$ 的求解与值域

由 $\cos z=(e^{iz}+e^{-iz})/2$，设 $z=x+iy$、$A,B\in\mathbb R$，比较实部和虚部：

$$
\boxed{\cos x\cosh y=A,\qquad-\sin x\sinh y=B.}
$$

若 $B=0$ 且 $|A|\le1$，取 $y=0$ 并解 $\cos x=A$ 即可。若 $B=0$ 且 $A>1$，取 $x=0$、$\cosh y=A$；若 $A<-1$，取 $x=\pi$、$\cosh y=-A$。这些情形都有解。

若 $B\ne0$，可令 $y>0$。由上述两式得到

$$
\cos x=\frac{A}{\cosh y},\qquad
\sin x=-\frac{B}{\sinh y},
$$

因而求解条件是

$$
G(y)=\frac{A^2}{\cosh^2y}
+\frac{B^2}{\sinh^2y}=1.
$$

因 $B\ne0$，$G$ 在 $(0,\infty)$ 连续、严格递减，且 $G(y)\to\infty$（$y\to0^+$）、$G(y)\to0$（$y\to\infty$），故存在唯一的正数 $y$ 满足此式。对应的余弦值与正弦值平方和为 $1$，可选取实数 $x$。所以**对每个 $A+iB\in\mathbb C$，方程 $\cos z=A+iB$ 都有解**；由 $\sin z=\cos(\pi/2-z)$，正弦函数的值域也为 $\mathbb C$。

板书另列出几个值域例子：$e^z$ 的值域为 $\mathbb C\setminus\{0\}$；非常值复多项式 $P(z)$ 的值域为 $\mathbb C$，因为对任意常数 $c$，$P(z)-c$ 由代数基本定理有根。这些结论各有自己的证明，不应把其中一项直接当作另一项的推导。


