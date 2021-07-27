# coding: utf-8
import os
import sys
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

sys.path.append(os.pardir)  # 导入父目录文件的设置


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]  # 训练图像
label = t_train[0] # 训练标签（数字是几）
print(label)  # 5 (训练数据的结果)

print(img.shape)  # (784,) 图像的一维数组形式
img = img.reshape(28, 28)  # 28*28图像
print(img.shape)  # (28, 28)

img_show(img)
