# Rectified Linear Unit
'''
线性整流函数（Rectified Linear Unit, ReLU）,又称修正线性单元,
是一种人工神经网络中常用的激活函数（activation function），
通常指代以斜坡函数及其变种为代表的非线性函数。
'''
import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # 指定y轴的范围
plt.show()
