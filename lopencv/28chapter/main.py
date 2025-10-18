
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg")

histr = cv.calcHist([img],[0],None,[256],[0,256])

# 绘图图像
plt.figure(figsize=(10,6),dpi=100)
plt.plot(histr)
plt.grid()
plt.show()



