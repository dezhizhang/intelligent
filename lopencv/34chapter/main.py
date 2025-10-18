import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("horse.jpg",0)
x = cv.Sobel(img,cv.CV_16S,1,0)
y = cv.Sobel(img,cv.CV_16S,0,1)

# 将图像数据进行转换
absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)

# 结果合成
result = cv.addWeighted(absX,0.5,absY,0.5,0)

# 显示图像
plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121)
plt.imshow(img,cmap=plt.cm.gray)
plt.title("origin")
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(result,cmap=plt.cm.gray)
plt.title("result")
plt.xticks([])
plt.yticks([])
plt.show()






