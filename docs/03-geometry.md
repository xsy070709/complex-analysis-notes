### 3. 复数的运算与几何意义

#### 3.1 加法与减法

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

#### 3.2 指数形式下的乘法与除法

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

#### 3.3 复数的四次方根与旋转

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

#### 3.4 共轭复数与模

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

#### 3.5 直线与圆的复数表示

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

##### 3.5.1 直线的复数表示

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

##### 3.5.2 圆的复数表示

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

#### 3.6 例题：证明三点构成等边三角形

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

#### 3.7 例题：证明四点构成矩形

设四个互异复数 $z_1,z_2,z_3,z_4$ 按圆周顺序排列，并满足

$$
|z_1|=|z_2|=|z_3|=|z_4|=r>0,
\qquad
z_1+z_2+z_3+z_4=0.
$$

证明以 $z_1,z_2,z_3,z_4$ 为顶点的四边形是矩形。

##### 证明

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

#### 3.8 模相等的根何时构成正多边形

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

##### 3.8.1 正多边形对应的多项式

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

##### 3.8.2 模相等时的系数关系

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

##### 3.8.3 偶数次多项式

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

##### 3.8.4 奇数次多项式

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

#### 3.9 重要例题：圆盘上 $|z^n+\alpha|$ 的最值

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

##### 3.9.1 转化为圆盘内的距离问题

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

##### 3.9.2 板书标准答案：最大值及取等条件

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

##### 3.9.3 板书标准答案：最小值及取等条件

最小值取决于点 $-\alpha$ 是否位于圆盘 $|w|\le r^n$ 内。

先看 $\alpha=0$：这时 $f(z)=|z|^n$，最小值为 $0$，当且仅当 $z=0$ 时取得。下文设 $\alpha\ne0$，写成 $\alpha=|\alpha|e^{i\theta}$。

##### 情形一：$|\alpha|\le r^n$

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

##### 情形二：$|\alpha|>r^n$

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

##### 3.9.4 结论

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

