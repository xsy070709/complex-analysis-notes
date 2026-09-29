### 10. 由复幂级数求三角级数

#### 10.1 从 $-\ln(1-z)$ 出发

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

#### 10.2 取实部与虚部

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

#### 10.3 令 $r\to1^-$：单位圆上的级数

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

#### 10.4 再积分一次：平方分母的级数

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

此时使用第 7 节已记录的正弦无穷乘积。在 $x=0$ 附近，将它与泰勒级数都展开到二次项：

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

由于 $r<1$，可以逐项求导，再代入第 10.2 节的余弦公式：

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

此外，在 $\theta=\pi$ 处代入第 10.3 节的余弦级数公式，得到板书上的交错调和级数：

$$
\boxed{\sum_{n=1}^{\infty}\frac{(-1)^n}{n}
=-\ln 2,\qquad
1-\frac12+\frac13-\frac14+\cdots=\ln2.}
$$

**板书留问：**$\sum_{n=1}^{\infty}1/n^3$ 的值记作 $\zeta(3)$。上面的乘积与 $x^2$ 系数比较法只算出 $\zeta(2)$；正弦除以 $x$ 的展开没有 $x^3$ 项，不能照搬这一步求 $\zeta(3)$。

