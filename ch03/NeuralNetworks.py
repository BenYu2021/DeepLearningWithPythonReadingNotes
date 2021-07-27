# 3.3.3 神经网络的内积
import numpy as np

X = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])
Y = np.dot(X, W)
print(Y) # [ 5 11 17]
