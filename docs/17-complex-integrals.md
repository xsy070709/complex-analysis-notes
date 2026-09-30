# 第三章 复积分（Complex Integrals）

## 3.1 光滑曲线与分段光滑曲线

设有向曲线的参数方程为
$$
C:\quad z=z(t)=x(t)+iy(t),\qquad a\le t\le b.
$$
本章约定光滑曲线满足 $x,y\in C^1([a,b])$，且
$$
|z'(t)|^2=[x'(t)]^2+[y'(t)]^2>0.
$$
端点处导数理解为单侧导数。非零切向量确定切线方向；参数增大的方向为曲线的给定方向。

若有限条光滑曲线 $C_1,\ldots,C_m$ 按顺序首尾连接成 $C$，则称 $C$ 为**分段光滑曲线**，记作 $C=C_1+\cdots+C_m$。连接点可以有折角，例如多边形边界。

## 3.2 复积分的定义

设 $f$ 在分段光滑曲线 $C$ 上连续。取参数分割
$$
a=t_0<t_1<\cdots<t_n=b,\qquad \xi_k\in[t_{k-1},t_k],
$$
记
$$
\Delta z_k=z(t_k)-z(t_{k-1}),\qquad
\|\mathcal P\|=\max_{1\le k\le n}(t_k-t_{k-1}).
$$
定义
$$
\boxed{\int_C f(z)\,dz
=\lim_{\|\mathcal P\|\to0}\sum_{k=1}^n f(z(\xi_k))\Delta z_k.}
$$
这里 $z(t_k)$ 为分点，$z(\xi_k)$ 为取样点。不能仅用相邻端点距离控制分割，因为端点很近并不保证其间曲线段很短。

参数化计算公式为
$$
\boxed{\int_C f(z)\,dz=\int_a^b f(z(t))z'(t)\,dt.}
$$
复值定积分分别对实部与虚部积分。分段光滑时逐段计算并相加：
$$
\int_C f(z)\,dz=\sum_{j=1}^m\int_{C_j}f(z)\,dz.
$$
反向曲线记作 $-C$，满足
$$
\int_{-C}f(z)\,dz=-\int_C f(z)\,dz.
$$

## 3.3 闭曲线上的复积分

若 $z(a)=z(b)$，则曲线闭合，沿其积分记作
$$
\boxed{\oint_C f(z)\,dz=\int_a^b f(z(t))z'(t)\,dt.}
$$
分段光滑时仍逐段求和。闭合本身不意味着积分为零。

除起点与终点重合外没有自交的闭曲线称为**简单闭曲线**。若其内部为 $\Omega$，则边界 $C=\partial\Omega$ 的正向为行进时区域在左侧，即外边界逆时针方向。

## 3.4 Cauchy–Goursat 定理

**定理（常用版本）：**设 $C$ 为分段光滑的简单闭曲线，$\Omega$ 为其内部区域。若 $f$ 在包含 $\overline\Omega=\Omega\cup C$ 的某个开集上解析，则
$$
\boxed{\oint_C f(z)\,dz=0.}
$$
该定理不需要预先假设导数连续。

**边界版本：**若 $f$ 在 $\overline\Omega$ 上连续、在 $\Omega$ 内解析，则结论仍成立；但下节直接使用 Green 公式的证明需要更强条件。

**条件要点：**不能忽略曲线内部的奇点。例如 $1/z$ 在单位圆附近解析，却在圆内的原点无定义。对逆时针单位圆 $z=e^{it}$，
$$
\oint_{|z|=1}\frac1z\,dz
=\int_0^{2\pi}e^{-it}ie^{it}\,dt=2\pi i\ne0.
$$

## 3.5 利用 Green 公式证明：偏导连续的版本

本节对应板书的证明。除上述曲线、区域条件外，额外假设 $f=u+iv$ 的实部和虚部在包含 $\overline\Omega$ 的开集上具有连续的一阶偏导数。

### 3.5.1 Green 公式

若 $P,Q$ 在包含 $\overline\Omega$ 的开集上具有连续的一阶偏导数，且 $C=\partial\Omega$ 取正向，则
$$
\boxed{\oint_C P\,dx+Q\,dy
=\iint_\Omega(Q_x-P_y)\,dx\,dy.}
$$

### 3.5.2 展开复积分

由 $z=x+iy$、$dz=dx+i\,dy$，
$$
\begin{aligned}
f(z)\,dz
&=(u+iv)(dx+i\,dy)\\
&=(u\,dx-v\,dy)+i(v\,dx+u\,dy).
\end{aligned}
$$
因此
$$
\oint_C f(z)\,dz
=\oint_C(u\,dx-v\,dy)+i\oint_C(v\,dx+u\,dy).
$$

### 3.5.3 分别使用 Green 公式

实部取 $P=u,Q=-v$，得到
$$
\oint_C(u\,dx-v\,dy)
=\iint_\Omega(-v_x-u_y)\,dx\,dy.
$$
虚部取 $P=v,Q=u$，得到
$$
\oint_C(v\,dx+u\,dy)
=\iint_\Omega(u_x-v_y)\,dx\,dy.
$$
合并即
$$
\oint_C f(z)\,dz
=\iint_\Omega(-v_x-u_y)\,dx\,dy
+i\iint_\Omega(u_x-v_y)\,dx\,dy.
$$

### 3.5.4 使用 Cauchy–Riemann 方程

因 $f$ 解析，
$$
u_x=v_y,\qquad u_y=-v_x,
$$
故
$$
-v_x-u_y=0,\qquad u_x-v_y=0.
$$
两个面积分均为零，从而
$$
\boxed{\oint_C f(z)\,dz=0+i0=0.}
$$
这证明了偏导连续条件下的 Cauchy 积分定理。

## 3.6 证明条件与理论衔接

板书主线为：复积分定义与参数化计算、闭路积分、Cauchy–Goursat 定理，以及 Green 公式结合 C–R 方程的证明。

**Green 证明与 Goursat 加强：**Green 公式的直接应用要求实部、虚部的一阶偏导连续；Cauchy–Goursat 定理本身没有这一前提，其通常采用三角形细分法证明。解析函数实际上具有各阶连续导数，但若这一性质尚待通过柯西积分理论建立，就不能提前引用它消除额外假设，以免循环论证。

前文第 13.6 节的泰勒展开及第 16.1 节的刘维尔定理引用了柯西积分公式，属于提前记录的理论应用；本章从复积分开始建立其基础，后续还需引入柯西积分公式。

## 3.7 例题 1：圆周上的负整数次幂积分

**题目：**设 $n\in\mathbb Z$、$n>0$，$r>0$，计算
$$
I_n=\oint_{|z-z_0|=r}\frac{dz}{(z-z_0)^n},
$$
其中圆周按逆时针方向绕行一周。

**解：**将圆周参数化为
$$
z=z_0+re^{i\theta},\qquad 0\le\theta\le2\pi.
$$
于是
$$
z-z_0=re^{i\theta},\qquad dz=ire^{i\theta}\,d\theta.
$$
因此
$$
\begin{aligned}
I_n
&=\int_0^{2\pi}\frac{ire^{i\theta}}{(re^{i\theta})^n}\,d\theta\\
&=\frac{i}{r^{n-1}}\int_0^{2\pi}e^{i(1-n)\theta}\,d\theta.
\end{aligned}
$$
分两种情况讨论。

当 $n=1$ 时，指数因子恒为 $1$，所以
$$
I_1=i\int_0^{2\pi}d\theta=2\pi i.
$$
当 $n\ne1$ 时，
$$
\begin{aligned}
I_n
&=\frac{i}{r^{n-1}}
\left[\frac{e^{i(1-n)\theta}}{i(1-n)}\right]_0^{2\pi}\\
&=\frac{1}{r^{n-1}(1-n)}
\left(e^{2\pi i(1-n)}-1\right)=0,
\end{aligned}
$$
因为 $n$ 为整数，$e^{2\pi i(1-n)}=1$。

综上，
$$
\boxed{
\oint_{|z-z_0|=r}\frac{dz}{(z-z_0)^n}
=\begin{cases}
2\pi i,&n=1,\\[4pt]
0,&n\ne1.
\end{cases}}
$$

**推广（供下一例使用）：**同一参数化计算对任意整数 $k$ 都成立，因此
$$
\boxed{
\oint_{|z-z_0|=r}\frac{dz}{(z-z_0)^k}
=\begin{cases}
2\pi i,&k=1,\\[4pt]
0,&k\in\mathbb Z,\ k\ne1.
\end{cases}}
$$
其中 $k\le0$ 时，被积函数是非负整数次幂。路径反向时积分变号。

## 3.8 例题 2：余弦展开与逐项积分

**题目：**设 $n\in\mathbb Z$、$n>0$，计算
$$
J_n=\oint_{|z|=1}\frac{1-\cos z}{z^n}\,dz,
$$
其中单位圆按逆时针方向绕行一周。

**解：**由余弦函数的幂级数展开，
$$
\cos z=\sum_{m=0}^{\infty}\frac{(-1)^m z^{2m}}{(2m)!},
$$
可得
$$
\begin{aligned}
1-\cos z
&=1-\sum_{m=0}^{\infty}\frac{(-1)^m z^{2m}}{(2m)!}\\
&=\sum_{m=1}^{\infty}\frac{(-1)^{m+1}z^{2m}}{(2m)!}.
\end{aligned}
$$
因此在单位圆上，
$$
\frac{1-\cos z}{z^n}
=\sum_{m=1}^{\infty}\frac{(-1)^{m+1}}{(2m)!}z^{2m-n}
=\sum_{m=1}^{\infty}\frac{(-1)^{m+1}}{(2m)!}
\frac{1}{z^{n-2m}}.
$$
当 $|z|=1$ 时，各项绝对值为 $1/(2m)!$，而 $\sum_{m=1}^{\infty}1/(2m)!$ 收敛。由 Weierstrass 判别法，该级数在积分路径上一致绝对收敛，故可逐项积分：
$$
\begin{aligned}
J_n
&=\sum_{m=1}^{\infty}\frac{(-1)^{m+1}}{(2m)!}
\oint_{|z|=1}\frac{dz}{z^{n-2m}}.
\end{aligned}
$$
由例题 1 对任意整数指数的推广，
$$
\oint_{|z|=1}\frac{dz}{z^k}
=\begin{cases}
2\pi i,&k=1,\\[4pt]
0,&k\in\mathbb Z,\ k\ne1.
\end{cases}
$$
所以只有
$$
n-2m=1,\qquad m=\frac{n-1}{2}
$$
时对应项不为零。由于 $m$ 必须为正整数，即 $(n-1)/2\in\mathbb N^+$，故必须有
$$
n=3,5,7,\ldots.
$$
此时 $2m=n-1$，于是
$$
\begin{aligned}
J_n
&=\frac{(-1)^{m+1}}{(2m)!}\,2\pi i\\
&=\frac{(-1)^{(n-1)/2+1}}{(n-1)!}\,2\pi i\\
&=\frac{(-1)^{(n+1)/2}\,2\pi i}{(n-1)!}.
\end{aligned}
$$
若 $n=1$ 或 $n$ 为正偶数，则没有符合条件的项，积分为零。

因此
$$
\boxed{
\oint_{|z|=1}\frac{1-\cos z}{z^n}\,dz
=\begin{cases}
\dfrac{(-1)^{(n+1)/2}\,2\pi i}{(n-1)!},
&n=3,5,7,\ldots,\\[10pt]
0,&n=1,2,4,6,\ldots.
\end{cases}}
$$

## 3.9 复函数解析与 Taylor 展开

若 $f$ 在 $z_0$ 解析，即在 $z_0$ 的某个邻域内处处复可导，则在某个圆盘 $|z-z_0|<R$ 内有
$$
\boxed{f(z)=\sum_{k=0}^{\infty}\frac{f^{(k)}(z_0)}{k!}(z-z_0)^k.}
$$
板书特别强调：
$$
\boxed{
f\text{ 在 }z_0\text{ 解析}
\iff
f\text{ 在 }z_0\text{ 的某邻域内可展开为 Taylor 级数}.}
$$

> **评注：**这里是局部等价关系，不能将“某邻域内处处复可导”简化为“只在一点复可导”。实函数即使无限次可微，也未必等于其 Taylor 级数；前文第 13.6 节已给出这一等价关系的理论说明。

## 3.10 Cauchy 积分公式及其高阶导数形式

设 $f$ 在包含闭圆盘 $|z-z_0|\le r$ 的某个开集上解析，圆周按逆时针方向积分，则对任意 $n=0,1,2,\ldots$，
$$
\boxed{
f^{(n)}(z_0)=\frac{n!}{2\pi i}
\oint_{|z-z_0|=r}\frac{f(z)}{(z-z_0)^{n+1}}\,dz.}
$$
等价地，
$$
\boxed{
\frac{f^{(n)}(z_0)}{n!}
=\frac{1}{2\pi i}
\oint_{|z-z_0|=r}\frac{f(z)}{(z-z_0)^{n+1}}\,dz.}
$$

### 3.10.1 参数化后的形式

令
$$
z=z_0+re^{i\theta},\qquad 0\le\theta\le2\pi.
$$
则
$$
z-z_0=re^{i\theta},\qquad dz=ire^{i\theta}\,d\theta,
\qquad (z-z_0)^{n+1}=r^{n+1}e^{i(n+1)\theta}.
$$
代入得
$$
\begin{aligned}
f^{(n)}(z_0)
&=\frac{n!}{2\pi i}\int_0^{2\pi}
\frac{f(z_0+re^{i\theta})\,ire^{i\theta}}
{r^{n+1}e^{i(n+1)\theta}}\,d\theta\\
&=\boxed{\frac{n!}{2\pi r^n}\int_0^{2\pi}
f(z_0+re^{i\theta})e^{-in\theta}\,d\theta}.
\end{aligned}
$$

> **评注：**若 $a_n=f^{(n)}(z_0)/n!$，则圆周函数 $\theta\mapsto f(z_0+re^{i\theta})$ 的第 $n$ 个 Fourier 系数为 $a_n r^n$。这说明 Taylor 系数可由圆周上的函数值恢复。

## 3.11 Cauchy 平均值公式

在高阶导数公式中取 $n=0$：
$$
f(z_0)=\frac{1}{2\pi i}
\oint_{|z-z_0|=r}\frac{f(z)}{z-z_0}\,dz.
$$
利用圆周参数化，
$$
\begin{aligned}
f(z_0)
&=\frac{1}{2\pi i}\int_0^{2\pi}
\frac{f(z_0+re^{i\theta})}{re^{i\theta}}
ire^{i\theta}\,d\theta\\
&=\boxed{\frac{1}{2\pi}\int_0^{2\pi}
f(z_0+re^{i\theta})\,d\theta}.
\end{aligned}
$$
因此，解析函数在圆心处的值等于其在圆周上的平均值，称为**解析函数的平均值性质**。

> **评注：**因为圆周上 $ds=r\,d\theta$，该式也等于按弧长取平均：
> $f(z_0)=(2\pi r)^{-1}\oint_{|z-z_0|=r}f(z)\,ds$。内部函数值受到周围圆周函数值的约束，这是最大模原理的重要基础。

## 3.12 实函数光滑与复函数解析的区别

板书给出实函数
$$
g(x)=\begin{cases}
e^{-1/x^2},&x\ne0,\\[4pt]
0,&x=0.
\end{cases}
$$
它属于 $C^\infty(\mathbb R)$，并且
$$
g^{(n)}(0)=0,\qquad n=0,1,2,\ldots.
$$
因此在原点对应的 Taylor 级数为
$$
\sum_{n=0}^{\infty}\frac{g^{(n)}(0)}{n!}x^n=0,
$$
而 $x\ne0$ 时 $g(x)>0$，所以它不等于自己的 Taylor 级数。

板书进一步沿虚轴考察同一表达式。令 $z=iy$、$y\ne0$，则
$$
e^{-1/(iy)^2}=e^{1/y^2}\longrightarrow+\infty
\qquad(y\to0).
$$

> **评注：**此时考察的是穿孔复平面上的函数 $e^{-1/z^2}$，而不是把实变量 $x$ 当作仍为实数。它不能通过令原点值为 $0$ 连续延拓，更不能在原点解析。该例说明
> $C^\infty\not\Rightarrow\text{实解析}$；而复函数在一个邻域内处处复可导，就在那里解析，并自动具有各阶连续导数。实变量部分也见第 13.5 节。

## 3.13 最大模原理

设 $D$ 是简单闭曲线 $C$ 围成的内部区域，$f$ 在 $D$ 内解析、在 $\overline D=D\cup C$ 上连续，且不是常数。则 $|f|$ 不能在内部取得最大值，其最大值只能出现在边界：
$$
\boxed{
\max_{z\in\overline D}|f(z)|
=\max_{z\in\partial D}|f(z)|,\qquad \partial D=C.}
$$
若存在内部点 $z_0$ 满足 $|f(z)|\le |f(z_0)|$ 对整个 $D$ 成立，则 $f$ 必为常数。

> **评注（平均值公式的证明思路）：**记 $M=|f(z_0)|$。若 $M=0$，则整个区域内 $f=0$。若 $M>0$，令 $\lambda=\overline{f(z_0)}/M$，则 $|\lambda|=1$、$\lambda f(z_0)=M$。对完全位于 $D$ 内、以 $z_0$ 为圆心的小圆，平均值公式给出
> $$
> M=\frac1{2\pi}\int_0^{2\pi}
> \operatorname{Re}\!\left(\lambda f(z_0+re^{i\theta})\right)\,d\theta.
> $$
> 圆周上 $\operatorname{Re}(\lambda f)\le |f|\le M$；连续的非负函数 $M-\operatorname{Re}(\lambda f)$ 的积分为零，故它处处为零。结合 $|\lambda f|\le M$，得到圆周上 $\lambda f=M$，即 $f=f(z_0)$。任意充分小的半径均可采用，因此 $f$ 在一个邻域内为常数，再由恒等定理推广到连通区域 $D$。这也解释了平均值达到最大模时的等号条件。

### 3.13.1 板书应用：单位圆盘上的二次式极值

板书列出
$$
\max\{x^2-xy+y^2:x^2+y^2\le1\}.
$$

> **评注（补全计算并说明方法）：**令 $z=x+iy$，则
> $$
> x^2-xy+y^2=|z|^2-\frac12\operatorname{Im}(z^2).
> $$
> 该式不是已经写成某个解析函数的模，不能直接对目标二次式套用最大模原理。不过由 $|xy|\le(x^2+y^2)/2$，
> $$
> x^2-xy+y^2
> \le x^2+y^2+|xy|
> \le\frac32(x^2+y^2)\le\frac32.
> $$
> 等号当且仅当 $x^2+y^2=1$ 且 $x=-y$，即
> $$
> \boxed{\max=\frac32,\qquad
> (x,y)=\left(\frac1{\sqrt2},-\frac1{\sqrt2}\right)
> \text{ 或 }\left(-\frac1{\sqrt2},\frac1{\sqrt2}\right).}
> $$
> 也可令 $z=\rho e^{i\theta}$，得到 $\rho^2(1-\tfrac12\sin2\theta)$，从而先取 $\rho=1$，再取 $\sin2\theta=-1$。一般应用最大模原理时，应先验证所构造的函数确为解析函数，并准确建立目标量与其模的关系。

## 3.14 Cauchy 积分公式与 Taylor 系数的对应

设 $f$ 在圆盘 $|z-z_0|<R$ 内解析，取 $0<r<R$。由 Taylor 展开，
$$
f(z)=\sum_{k=0}^{\infty}\frac{f^{(k)}(z_0)}{k!}(z-z_0)^k.
$$
将其代入：
$$
\frac{f(z)}{(z-z_0)^{n+1}}
=\sum_{k=0}^{\infty}
\frac{f^{(k)}(z_0)}{k!}
\frac1{(z-z_0)^{n+1-k}}.
$$
该级数在圆周 $|z-z_0|=r$ 上一致收敛，故可逐项积分：
$$
\begin{aligned}
\frac{n!}{2\pi i}
\oint_{|z-z_0|=r}\frac{f(z)}{(z-z_0)^{n+1}}\,dz
&=\frac{n!}{2\pi i}
\sum_{k=0}^{\infty}\frac{f^{(k)}(z_0)}{k!}
\oint_{|z-z_0|=r}\frac{dz}{(z-z_0)^{n+1-k}}.
\end{aligned}
$$
由第 3.7 节对任意整数 $m$ 成立的公式，
$$
\oint_{|z-z_0|=r}\frac{dz}{(z-z_0)^m}
=\begin{cases}
2\pi i,&m=1,\\[4pt]
0,&m\in\mathbb Z,\ m\ne1,
\end{cases}
$$
只有 $n+1-k=1$，即 $k=n$ 的项保留下来。于是
$$
\begin{aligned}
\frac{n!}{2\pi i}
\oint_{|z-z_0|=r}\frac{f(z)}{(z-z_0)^{n+1}}\,dz
&=\frac{n!}{2\pi i}\frac{f^{(n)}(z_0)}{n!}\,2\pi i\\
&=f^{(n)}(z_0).
\end{aligned}
$$

> **评注：**积分在这里筛选 Taylor 系数。若 Taylor 展开本身通过 Cauchy 积分公式证明，上述推导应视为验证或系数解释，不能反过来当作不依赖该公式的首次证明，以免循环论证。取 $r<R$ 保证积分圆周处于幂级数收敛圆内部。

## 3.15 Cauchy 不等式

沿用第 3.10 节的解析性条件，记
$$
\boxed{M(r)=\max_{|z-z_0|=r}|f(z)|.}
$$
则对任意 $n=0,1,2,\ldots$，
$$
\boxed{|f^{(n)}(z_0)|\le\frac{M(r)n!}{r^n}.}
$$

### 3.15.1 证明（按板书保留参数化估值过程）

由 Cauchy 高阶导数公式，
$$
f^{(n)}(z_0)=\frac{n!}{2\pi i}
\oint_{|z-z_0|=r}\frac{f(z)}{(z-z_0)^{n+1}}\,dz.
$$
两边取模：
$$
|f^{(n)}(z_0)|=\frac{n!}{2\pi}
\left|\oint_{|z-z_0|=r}
\frac{f(z)}{(z-z_0)^{n+1}}\,dz\right|.
$$
利用积分模的估值
$$
\left|\oint_C g(z)\,dz\right|
\le\oint_C|g(z)|\,|dz|,
$$
得到
$$
\begin{aligned}
|f^{(n)}(z_0)|
&\le\frac{n!}{2\pi}
\oint_{|z-z_0|=r}
\left|\frac{f(z)}{(z-z_0)^{n+1}}\right|\,|dz|\\
&=\frac{n!}{2\pi}
\oint_{|z-z_0|=r}
\frac{|f(z)|}{|z-z_0|^{n+1}}\,|dz|.
\end{aligned}
$$
路径上 $|z-z_0|=r$，且 $|f(z)|\le M(r)$，故
$$
|f^{(n)}(z_0)|
\le\frac{n!}{2\pi}
\oint_{|z-z_0|=r}\frac{M(r)}{r^{n+1}}\,|dz|.
$$
对圆周参数化：
$$
z=z_0+re^{i\theta},\qquad 0\le\theta\le2\pi,
\qquad dz=ire^{i\theta}\,d\theta.
$$
因此
$$
|dz|=|ire^{i\theta}|\,d\theta=r\,d\theta.
$$
于是
$$
\begin{aligned}
|f^{(n)}(z_0)|
&\le\frac{n!}{2\pi}
\int_0^{2\pi}\frac{M(r)}{r^{n+1}}r\,d\theta\\
&=\frac{n!}{2\pi}\frac{M(r)}{r^n}
\int_0^{2\pi}d\theta\\
&=\frac{n!}{2\pi}\frac{M(r)}{r^n}\cdot2\pi\\
&=\frac{M(r)n!}{r^n}.
\end{aligned}
$$
故
$$
\boxed{|f^{(n)}(z_0)|\le\frac{M(r)n!}{r^n},
\qquad n=0,1,2,\ldots.}
$$

> **评注：**这里 $|dz|$ 表示弧长微元。板书通过 $|dz|=r\,d\theta$ 显式展示了分母中的 $r^{n+1}$ 如何降为 $r^n$，而没有直接以圆周长度一步带过。

### 3.15.2 对 Taylor 系数的估计

若
$$
f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^n,
\qquad a_n=\frac{f^{(n)}(z_0)}{n!},
$$
则
$$
\boxed{|a_n|\le\frac{M(r)}{r^n}.}
$$

> **评注：**圆周上的最大模控制圆心处所有阶导数和 Taylor 系数。对于整函数，可以令 $r\to\infty$，结合 $M(r)$ 的增长限制迫使某些导数为零。前文第 16.1 节的 Liouville 定理正是应用 $|f'(z_0)|\le M/r$；这一思想也用于代数基本定理的复分析证明。

## 3.16 例题：利用 Cauchy 不等式证明 Liouville 定理

**题目：**设 $f(z)$ 为整函数，且存在常数 $M>0$，使
$$
|f(z)|\le M,\qquad \forall z\in\mathbb C.
$$
证明：$f(z)$ 必为常数。

**证明：**因为 $f$ 为整函数，对任意 $r>0$ 都可在圆周 $|z|=r$ 上应用 Cauchy 不等式。记
$$
M(r)=\max_{|z|=r}|f(z)|,
$$
则题设给出 $M(r)\le M$。由 Cauchy 不等式，
$$
|f^{(n)}(0)|\le\frac{M(r)n!}{r^n},
\qquad n=0,1,2,\ldots.
$$
对任意固定的 $n\ge1$，
$$
0\le|f^{(n)}(0)|\le\frac{Mn!}{r^n}.
$$
令 $r\to+\infty$，右端趋于零，故由夹逼定理，
$$
f^{(n)}(0)=0,\qquad n=1,2,\ldots.
$$
由于整函数在原点的 Taylor 展开对整个复平面成立，
$$
f(z)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}z^n=f(0).
$$
因此
$$
\boxed{f(z)\equiv\text{常数}.}
$$
证毕。

> **评注：**这就是刘维尔（Liouville）定理：整函数允许令 $r\to\infty$，全局有界性使每个固定阶数 $n\ge1$ 的导数估值趋于零。下一例将“有界”推广为“至多多项式增长”。

## 3.17 例题：多项式增长的整函数必为多项式

**题目：**设 $f(z)$ 为整函数，且存在常数 $M>0$ 及非负整数 $m$，使得对任意 $z\in\mathbb C$，
$$
|f(z)|\le M\sum_{k=0}^m|z|^k.
$$
证明：$f(z)$ 是次数不超过 $m$ 的多项式。

**证明：**因为 $f$ 为整函数，对任意 $r>0$ 都可在圆周 $|z|=r$ 上使用 Cauchy 高阶导数公式：
$$
f^{(n)}(0)=\frac{n!}{2\pi i}
\oint_{|z|=r}\frac{f(z)}{z^{n+1}}\,dz.
$$
对任意固定的 $j=1,2,\ldots$，令 $n=m+j$，则
$$
f^{(m+j)}(0)=\frac{(m+j)!}{2\pi i}
\oint_{|z|=r}\frac{f(z)}{z^{m+j+1}}\,dz.
$$
两边取模，利用积分估值，
$$
|f^{(m+j)}(0)|
\le\frac{(m+j)!}{2\pi}
\oint_{|z|=r}\frac{|f(z)|}{|z|^{m+j+1}}\,|dz|.
$$
在圆周上，由题设，
$$
|f(z)|\le M\sum_{k=0}^m r^k.
$$
令 $z=re^{i\theta}$，$0\le\theta\le2\pi$，则 $|z|=r$、$|dz|=r\,d\theta$。因此
$$
\begin{aligned}
|f^{(m+j)}(0)|
&\le\frac{(m+j)!}{2\pi}
\int_0^{2\pi}\frac{M\sum_{k=0}^m r^k}{r^{m+j+1}}
r\,d\theta\\
&=(m+j)!M\,\frac{\sum_{k=0}^m r^k}{r^{m+j}}\\
&=(m+j)!M\left(
\frac1{r^{m+j}}+\frac1{r^{m+j-1}}+\cdots+\frac1{r^j}
\right).
\end{aligned}
$$
令 $r\to+\infty$，右端趋于零，故
$$
f^{(m+j)}(0)=0,\qquad j=1,2,\ldots.
$$
也就是说，
$$
f^{(m+1)}(0)=f^{(m+2)}(0)=\cdots=0.
$$
由于整函数的 Taylor 展开在整个复平面成立，
$$
f(z)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}z^n.
$$
当 $n\ge m+1$ 时系数均为零，因此
$$
\begin{aligned}
f(z)
&=\sum_{n=0}^m\frac{f^{(n)}(0)}{n!}z^n\\
&=f(0)+f'(0)z+\frac{f''(0)}{2!}z^2
+\cdots+\frac{f^{(m)}(0)}{m!}z^m.
\end{aligned}
$$
故
$$
\boxed{f(z)\text{ 是次数不超过 }m\text{ 的多项式}.}
$$
证毕。

> **评注：**这是上一例刘维尔定理的推广，$m=0$ 时即回到有界整函数的情形。增长阶数不超过 $m$，便迫使高于 $m$ 阶的 Taylor 系数全部为零；结论包含零多项式。

## 3.18 调和函数与最大、最小值原理

### 3.18.1 调和函数的定义

设二元实函数 $u=u(x,y)$ 在区域 $D\subset\mathbb R^2$ 内具有二阶连续偏导数。若满足二维 **Laplace 方程**
$$
\boxed{\Delta u=u_{xx}+u_{yy}=0,}
$$
则称 $u$ 为 $D$ 内的**调和函数**。其中
$$
\Delta=\frac{\partial^2}{\partial x^2}
+\frac{\partial^2}{\partial y^2}
$$
称为 Laplace 算子。

### 3.18.2 解析函数的实部与虚部都是调和函数

设 $f(z)=u(x,y)+iv(x,y)$ 在区域 $D$ 内解析。由 Cauchy–Riemann 方程，
$$
\boxed{u_x=v_y,\qquad u_y=-v_x.}
$$
解析函数具有任意阶连续导数，其实部、虚部也具有任意阶连续偏导数。对第一式关于 $x$ 求导，对第二式关于 $y$ 求导，得
$$
u_{xx}=v_{yx},\qquad u_{yy}=-v_{xy}.
$$
因此
$$
\begin{aligned}
\Delta u
&=u_{xx}+u_{yy}\\
&=v_{yx}-v_{xy}=0,
\end{aligned}
$$
其中使用了混合偏导可交换。故 $\boxed{\Delta u=0}$。

类似地，由 $v_y=u_x$、$v_x=-u_y$，
$$
v_{yy}=u_{xy},\qquad v_{xx}=-u_{yx}.
$$
从而
$$
\begin{aligned}
\Delta v
&=v_{xx}+v_{yy}\\
&=-u_{yx}+u_{xy}=0.
\end{aligned}
$$
故 $\boxed{\Delta v=0}$。综上，
$$
\boxed{f=u+iv\text{ 解析}\ \Longrightarrow\ u,v\text{ 都调和}.}
$$

> **评注：**若 $u+iv$ 解析，通常称 $v$ 为 $u$ 的调和共轭。次序涉及符号：与 $v$ 配成解析函数的是 $v-i u$，故 $-u$ 是 $v$ 的调和共轭。任意调和函数在小圆盘内都可找到共轭；在单连通区域上可以找到全局单值共轭，一般区域则未必可以。例如穿孔平面上的 $\ln|z|$ 调和，却没有全局单值的共轭辐角。

### 3.18.3 最大值原理：板书的指数函数方法

设实函数 $u$ 在有界区域 $D$ 内调和，并在 $\overline D$ 上连续。若它不是常数，则最大值只能在边界上取得：
$$
\boxed{\max_{\overline D}u=\max_{\partial D}u.}
$$

按板书思路，先在可取调和共轭的区域写成
$$
f(z)=u(x,y)+iv(x,y),
$$
并构造解析函数
$$
\boxed{g(z)=e^{f(z)}.}
$$
由于
$$
g=e^{u+iv}=e^u e^{iv},\qquad |e^{iv}|=1,
$$
故
$$
\boxed{|g(z)|=e^{u(x,y)}.}
$$
指数函数严格单调递增，因此 $u$ 的最大值点就是 $|g|$ 的最大值点。若内部点取得最大值，由最大模原理，$g$ 必为常数，从而 $e^u$ 为常数，$u$ 也为常数。因此非常数调和函数不可能在内部取得整个区域的最大值。

> **评注（一般区域的严谨衔接）：**这里不必假设整个 $D$ 有全局共轭，更不必假设共轭连续到边界。若 $u$ 在内部点 $P_0$ 取得全局最大值 $A$，取一个以 $P_0$ 为中心、完全位于 $D$ 内的小圆盘，在其中取共轭并构造 $e^f$。最大模原理使 $u$ 在该圆盘内恒等于 $A$。集合 $E=\{P\in D:u(P)=A\}$ 非空；同理它在 $D$ 中是开集，连续性又使它为闭集。由 $D$ 连通，$E=D$，故 $u$ 在整个区域为常数。最后，由有界性和闭包上的连续性，最大值必存在；非常数时只能落在边界。

### 3.18.4 最小值原理

按板书，构造
$$
\boxed{h(z)=e^{-f(z)}.}
$$
因为
$$
h=e^{-u-iv}=e^{-u}e^{-iv},
$$
所以
$$
\boxed{|h(z)|=e^{-u(x,y)}.}
$$
$e^{-u}$ 随 $u$ 严格递减，因此 $u$ 的最小值点对应 $|h|$ 的最大值点。若 $u$ 在内部取得最小值，在该点附近取局部共轭并使用最大模原理，即推出 $u$ 局部为常数，再用上一节同样的开闭集论证推广到整个 $D$。

于是，对非常数 $u$，
$$
\boxed{\min_{\overline D}u=\min_{\partial D}u.}
$$

> **评注：**也可直接对调和函数 $-u$ 使用最大值原理，得到最小值原理。若额外具备全局解析函数及其边界连续性，则板书的等式链可直接写为
> $$
> \max_{\overline D}|e^f|=e^{\max_{\overline D}u}
> =e^{\max_{\partial D}u},\qquad
> \max_{\overline D}|e^{-f}|=e^{-\min_{\overline D}u}
> =e^{-\min_{\partial D}u}.
> $$
> 一般区域中采用上述局部证明即可，不需要这些额外条件。

### 3.18.5 最大—最小值原理

**定理：**若 $u$ 在有界区域 $D$ 内调和、在 $\overline D$ 上连续，则
$$
\boxed{
\max_{\overline D}u=\max_{\partial D}u,\qquad
\min_{\overline D}u=\min_{\partial D}u.}
$$
若内部点 $P_0\in D$ 满足
$$
u(P_0)=\max_{\overline D}u
\quad\text{或}\quad
u(P_0)=\min_{\overline D}u,
$$
则
$$
\boxed{u\equiv\text{常数}.}
$$
因此，非常数调和函数的最大值与最小值都只能在边界取得。

> **评注：**强最大、最小值原理还排除非常数调和函数的任何内部局部极大、局部极小，即使极值不是严格的。局部取共轭，应用解析函数最大模原理的局部形式即可。边界极值等式对常数函数同样成立；有界性用于保证闭包紧致及极值存在，不能无条件删去。

> **评注：**板书用 $|e^f|=e^u$ 将最大值问题转为最大模问题，用 $|e^{-f}|=e^{-u}$ 处理最小值。这是 Dirichlet 边值问题唯一性的基础：两个调和解若具有相同边界值，其差在边界为零，由最大、最小值原理可知内部也恒为零。

## 3.19 例题：复合余弦函数的围道积分

**题目：**设 $n\in\mathbb N^+$，计算
$$
J_n=\oint_{|z|=1}\frac{1-\cos(4z^5)}{z^n}\,dz,
$$
其中单位圆按逆时针方向绕行一周。

**解：**令 $f(z)=1-\cos(4z^5)$，则 $f$ 为整函数。由 Cauchy 高阶导数公式，
$$
J_n=\frac{2\pi i}{(n-1)!}f^{(n-1)}(0)
=\frac{2\pi i}{(n-1)!}
\left.\frac{d^{n-1}}{dz^{n-1}}(1-\cos(4z^5))\right|_{z=0}.
$$
为了判断哪些阶数的系数非零，使用
$$
\cos x=\sum_{m=0}^{\infty}\frac{(-1)^m x^{2m}}{(2m)!},
\qquad
1-\cos x=\sum_{m=1}^{\infty}\frac{(-1)^{m+1}x^{2m}}{(2m)!}.
$$
令 $x=4z^5$，得
$$
1-\cos(4z^5)
=\sum_{m=1}^{\infty}\frac{(-1)^{m+1}4^{2m}}{(2m)!}z^{10m}.
$$
故
$$
\frac{1-\cos(4z^5)}{z^n}
=\sum_{m=1}^{\infty}\frac{(-1)^{m+1}4^{2m}}{(2m)!}z^{10m-n}.
$$
该级数在单位圆上一致绝对收敛，因为各项绝对值不超过 $4^{2m}/(2m)!$，而其和收敛。因此可以逐项积分：
$$
J_n=\sum_{m=1}^{\infty}\frac{(-1)^{m+1}4^{2m}}{(2m)!}
\oint_{|z|=1}z^{10m-n}\,dz.
$$
只有 $z^{-1}$ 项积分非零，故要求
$$
10m-n=-1,\qquad n=10m+1.
$$
因此
$$
\boxed{
J_n=\begin{cases}
\displaystyle
2\pi i\,\frac{(-1)^{m+1}4^{2m}}{(2m)!},
&n=10m+1,\quad m=1,2,\ldots,\\[10pt]
0,&\text{其他正整数 }n.
\end{cases}}
$$

因此非零的参数恰为
$$
\boxed{n=11,21,31,\ldots.}
$$

> **评注：**Taylor 展开直接给出 $z^{n-1}$ 的系数，比反复求复合函数的高阶导数更方便。

## 3.20 例题：复合正弦函数的围道积分

**题目：**设 $n,k\in\mathbb N^+$，计算
$$
J_{n,k}=\oint_{|z|=1}\frac{\sin(z^k)}{z^n}\,dz,
$$
其中单位圆按逆时针方向绕行一周。

**解：**$f(z)=\sin(z^k)$ 为整函数，所以也可写成
$$
J_{n,k}=\frac{2\pi i}{(n-1)!}f^{(n-1)}(0).
$$
为求相应的 Taylor 系数，由
$$
\sin x=\sum_{m=1}^{\infty}\frac{(-1)^{m-1}x^{2m-1}}{(2m-1)!},
$$
令 $x=z^k$，得到
$$
\sin(z^k)
=\sum_{m=1}^{\infty}\frac{(-1)^{m-1}z^{k(2m-1)}}{(2m-1)!}.
$$
因此
$$
\frac{\sin(z^k)}{z^n}
=\sum_{m=1}^{\infty}\frac{(-1)^{m-1}}{(2m-1)!}
z^{k(2m-1)-n}.
$$
在单位圆上，各项绝对值为 $1/(2m-1)!$，其和收敛，故级数一致绝对收敛，可以逐项积分：
$$
J_{n,k}=\sum_{m=1}^{\infty}\frac{(-1)^{m-1}}{(2m-1)!}
\oint_{|z|=1}z^{k(2m-1)-n}\,dz.
$$
由任意整数 $p$ 的基本积分公式
$$
\oint_{|z|=1}z^p\,dz
=\begin{cases}
2\pi i,&p=-1,\\
0,&p\ne-1,
\end{cases}
$$
只有满足
$$
k(2m-1)-n=-1,
\qquad\boxed{n-1=k(2m-1)}
$$
的项产生非零贡献。由于 $k>0$，若这样的正整数 $m$ 存在，则它唯一。因此
$$
\boxed{
J_{n,k}=\begin{cases}
\displaystyle\frac{(-1)^{m-1}2\pi i}{(2m-1)!},
&n-1=k(2m-1),\quad m\in\mathbb N^+,\\[10pt]
0,&\text{不存在这样的 }m.
\end{cases}}
$$

进一步将条件与答案完全写成 $n,k$ 的形式。由 $n-1=k(2m-1)$，
$$
\boxed{k\mid(n-1),\qquad \frac{n-1}{k}\in\{1,3,5,\ldots\}.}
$$
在这一条件下，
$$
m=\frac{n-1+k}{2k},\qquad
m-1=\frac{n-1-k}{2k},\qquad
2m-1=\frac{n-1}{k}.
$$
代入上式，得到
$$
\boxed{
J_{n,k}=
\begin{cases}
\displaystyle
\frac{(-1)^{\frac{n-1-k}{2k}}}
{\left(\frac{n-1}{k}\right)!}\,2\pi i,
&\displaystyle\frac{n-1}{k}\in\{1,3,5,\ldots\},\\[14pt]
0,&\text{其他}.
\end{cases}}
$$

> **评注：**两题都是先展开幂级数，再寻找 $z^{-1}$ 项，最后作整数指数匹配：第一题为 $n-1=10m$，第二题为 $n-1=(2m-1)k$。第二题仅有整除条件还不够，商必须为正奇数；例如 $n=1$ 时商为零，积分为零。这里 $\sin(z^k)$ 表示先求 $z^k$ 再取正弦，与 $(\sin z)^k$ 不同。
