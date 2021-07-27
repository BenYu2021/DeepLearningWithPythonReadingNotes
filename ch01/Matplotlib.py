import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imread

# 生成数据
x = np.arange(0, 6, 0.1)  # 以0.1为单位，生成0到6的数据
y = np.sin(x)
y2 = np.cos(x)
# 绘制图形
plt.plot(x, y, label="sin")
plt.plot(x, y2, linestyle="--",
         label="cos")  # '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.show()


