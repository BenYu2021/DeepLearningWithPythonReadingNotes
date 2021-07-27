import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

print(x)  # [1. 2. 3.]
print(type(x))  # <class 'numpy.ndarray'>
print(x + y)  # [3. 6. 9.]
print(x - y)
print(x * y)
print(x / y)

# 广播
print(x / 2)  # [0.5 1.  1.5]

A = np.array([[1, 2], [3, 4]])
print(A.shape)  # (2, 2)
print(A.dtype)  # int32
B = np.array([10, 20])

'''
[[1 2]
 [3 4]]
 '''
print(A)

'''
广播机制

[[10 40]
 [30 80]]
'''
print(A * B)

# 访问元素
X = np.array([[51, 55], [14, 19], [0, 4]])
'''
[[51 55]
 [14 19]
 [ 0  4]]
 '''
print(X)
'''
第一行
[51 55]
'''
print(X[0])
'''

55
'''
print(X[0][1])
X = X.flatten()  # 把X转换为一维数组

'''
[51 55 14 19  0  4]
'''
print(X)
print(X > 15)  # [ True  True False  True False False]
print(X[X > 15])  # [51 55 19]
