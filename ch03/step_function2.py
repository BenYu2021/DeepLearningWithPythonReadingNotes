import numpy as np


# 3.2.2 阶跃函数的实现

def step_function(x):
    y = x > 0
    return y.astype(np.int)


x = np.array([-1.0, 1.0, 2.0])
print(x)  # [-1.  1.  2.]
y = x > 0
print(y)  # [False  True  True]
y = y.astype(int)  # 把布尔转换为整型[0 1 1]
print(y)
