### 11. 正弦无穷乘积的进一步应用

#### 11.1 偶数次倒数和

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

#### 11.2 在 $x=i\pi$ 处代入无穷乘积

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

