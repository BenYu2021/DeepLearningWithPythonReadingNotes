import numpy as np
import matplotlib.pylab as plt


# 3.2.3 阶跃函数的图形

def step_function(x):
    return np.array(x > 0, dtype=int)


# sigmoid  S 形;
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
y2 = sigmoid(x)
plt.plot(x, y, linestyle="--")
plt.plot(x, y2)
plt.ylim(-0.1, 1.1)  # 指定y轴的范围
plt.show()
