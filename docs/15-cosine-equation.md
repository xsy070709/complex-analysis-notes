### 15. 方程 $\cos z=A+iB$ 的求解与值域

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

