import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('l_hires.jpg', format='jpg')  # 读入图像
plt.imshow(img)
plt.show()
