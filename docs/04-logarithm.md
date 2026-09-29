### 4. 复对数

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

