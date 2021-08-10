import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)
y2 = sigmoid(x)
plt.plot(x, y2)
plt.ylim(-0.1, 1.1)  # 指定y轴的范围
plt.savefig("../images/图3-7sigmoid函数的图形.png")