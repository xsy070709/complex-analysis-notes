### 14. 初等函数的复平面映射

#### 14.1 指数函数：水平带映成角域

写 $w=e^z=e^xe^{iy}$。竖线 $x=x_0$ 映成半径为 $e^{x_0}$ 的圆周（竖线上的一段映成圆弧）；横线 $y=y_0$ 映成辐角为 $y_0$ 的射线。对固定 $y$，$x\to-\infty$ 时 $w\to0$，$x\to+\infty$ 时 $|w|\to\infty$。

尤其是水平带 $0<\operatorname{Im}z<\pi$ 经 $e^z$ 一一映成上半平面 $\operatorname{Im}w>0$。一般地，宽度小于 $2\pi$ 的水平带映成相应的角域；若包含跨越 $2\pi$ 的辐角范围，则会因 $e^{z+2\pi i}=e^z$ 而出现重叠。整个复平面的像是 $\mathbb C\setminus\{0\}$。

#### 14.2 平移、旋转、缩放与斜带

仿射变换 $z\mapsto az+b$（$a\ne0$）依次包含缩放、旋转和平移。若两条斜直线之间的垂直距离为 $h>0$，可以先通过平移与旋转使它们成为 $\operatorname{Im}\zeta=0$ 与 $\operatorname{Im}\zeta=h$，再乘以 $\pi/h$，得到标准水平带 $0<\operatorname{Im}\xi<\pi$。最后使用 $w=e^\xi$，就把斜带映到上半平面。

板书图中，斜线与实轴夹角为 $\theta_0$，截距相差 $b-a$ 时，两条平行线的垂距为 $h=|b-a|\,|\sin\theta_0|$；选择旋转方向时还应保证变换后的带落在 $0<\operatorname{Im}\xi<\pi$ 一侧。

#### 14.3 幂映射：角度相乘

设 $0<\theta_0<2\pi$。在不包含原点、可连续选取辐角 $0<\arg z<\theta_0$ 的扇形上，选择相应分支定义 $z^\alpha=r^\alpha e^{i\alpha\theta}$（$z=re^{i\theta}$，$\alpha>0$）。于是射线的辐角从 $\theta$ 变为 $\alpha\theta$。取 $\alpha=\pi/\theta_0$，可把角度为 $\theta_0$ 的扇形一一映成上半平面。

若 $\alpha$ 不是整数，$z^\alpha$ 需要先指定对数分支。一般的幂映射若把辐角区间放大到宽度超过 $2\pi$，像会绕原点重叠；上面取 $\alpha=\pi/\theta_0$ 时，像的辐角范围恰为 $(0,\pi)$，所以没有这种重叠。

