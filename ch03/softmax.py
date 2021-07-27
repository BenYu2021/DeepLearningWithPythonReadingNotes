import numpy as np


def softmax(a):
    """
    softmax函数输出的是0.0到1.0之间的实数。并且，softmax函数输出值的总和为1。
    """
    c = np.max(a)
    exp_a = np.exp(a - c)  # 防止溢出
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)  # [0.01821127 0.24519181 0.73659691]
