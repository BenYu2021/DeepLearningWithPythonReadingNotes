import numpy as np
import matplotlib.pylab as plt


# 3.2.3 阶跃函数的图形

def step_function(x):
    return np.array(x > 0, dtype=int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # 指定y轴的范围
# plt.show()
plt.savefig("../images/图3-6阶跃函数的图形1.png")
plt.savefig("../images/图3-6阶跃函数的图形2.png", bbox_inches='tight')
