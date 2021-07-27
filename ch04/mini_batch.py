import numpy as np
import sys, os
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape)  # (60000, 784)
print(t_train.shape)  # (60000, 10)

train_size = x_train.shape[0]  # 60000
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)  # 60000随机数选10个
x_batch = x_train[batch_mask]
t_batch = x_train[batch_mask]


def cross_entropy_error(y, t):
    """
    mini-batch版交叉熵误，监督数据是one-hot表示
    :param y:
    :param t:
    :return:
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.reshape[0]
    return -np.sum(t * np.log(y + 1e7)) / batch_size

def cross_entropy_error(y, t):
    """
    mini-batch版交叉熵误，监督数据是one-hot表示
    :param y:
    :param t:
    :return:
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.reshape[0]
    return -np.sum(t * np.log(y[np.arange(batch_size), t] + 1e7)) / batch_size