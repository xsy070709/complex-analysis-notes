### 6. 复数幂与多值性

#### 6.1 定义及与主值的区别

当 $a\in\mathbb C\setminus\{0\}$、$b\in\mathbb C$ 时，借助**全部对数值**定义复数幂：

$$
\boxed{a^b
=\left\{\exp\!\left[b\bigl(\operatorname{Ln}a+2k\pi i\bigr)\right]:k\in\mathbb Z\right\}.}
$$

这通常是一个多值集合。若**只取** $\exp(b\operatorname{Ln}a)$，得到的是按所选分支定义的一个主值。

本节讨论多值定义；计算时需要说明采用哪一种。若 $b$ 为整数，所有分支给出相同值，回到通常的整数次幂。

**关于取值个数和记号：**整数 $n$ 次开方（非零底数的 $n$ 次方根）恰有 $n$ 个值，记为 $z_0,\ldots,z_{n-1}$；无理指数的复数幂有无穷多个值，可记为 $z_k$（$k\in\mathbb Z$）。因此在求全部值时不能只写一个无下标的 $z$；是否有重复值仍须按指数差是否为 $2\pi i$ 的整数倍判定。

#### 6.2 有理指数：有限多个值

第一张板书以 $1^{q/p}$ 为例。设 $p,q\in\mathbb N^+$，则

$$
1^{q/p}
=\left\{\exp\!\left(\frac{q}{p}\,2k\pi i\right):k\in\mathbb Z\right\}
=\left\{\cos\frac{2kq\pi}{p}
+i\sin\frac{2kq\pi}{p}:k\in\mathbb Z\right\}.
$$

若 $\gcd(p,q)=1$，取 $k=0,1,\ldots,p-1$ 恰好得到 $p$ 个互不相同的值，它们是单位圆上的 $p$ 次单位根。

若 $p,q$ 未约分，不同值的个数为 $p/\gcd(p,q)$。例如 $1^{1/n}$ 有 $n$ 个值；其中 $1^{1/4}=\{1,i,-1,-i\}$。

#### 6.3 无理指数：无穷多个值

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

#### 6.4 复指数例子：$e^{\,x+iy}$

若将底数 $e$ 按多值复数幂处理，并设 $b=x+iy$（$x,y\in\mathbb R$），则

$$
\operatorname{Ln}e=1,\qquad
e^{\,b}
=\left\{\exp\!\left[(x+iy)(1+2k\pi i)\right]:k\in\mathbb Z\right\}
=\left\{e^{x-2k\pi y}e^{i(y+2k\pi x)}:k\in\mathbb Z\right\}.
$$

当 $y\ne0$ 时，这些值具有不同的模，因而有无穷多个；当 $y=0$ 且 $x$ 为有理数时，只得到有限多个值。

**不要把这里的多值复数幂 $e^{\,b}$ 与单值指数函数 $\exp(b)$ 混为一谈**：后者始终只有一个函数值。

