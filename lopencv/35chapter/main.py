import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

img = cv.imread("horse.jpg",0)

result = cv.Laplacian(img,cv.CV_16S)
scale_abs = cv.convertScaleAbs(result)

# 显示图像
plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121)
plt.imshow(img,cmap=plt.cm.gray)
plt.title("origin")
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(scale_abs,cmap=plt.cm.gray)
plt.title("laplcian")
plt.xticks([])
plt.yticks([])
plt.show()
