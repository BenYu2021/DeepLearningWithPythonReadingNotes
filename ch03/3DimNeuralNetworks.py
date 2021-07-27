# 3.3.3 神经网络的内积
import numpy as np

'''
一般，输出层激活函数，回归函问题可以使用恒等函数
二元分类问题可以使用sigmoid函数，
多元分类问题可以使用softmax函数
'''


def identity_function(x):
    return x


# sigmoid  S 形;
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 权重和偏置的初始化
def init_network():
    network = {}  # 字典
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network


#
def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    return y
