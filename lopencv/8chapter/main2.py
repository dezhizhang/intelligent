
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")


# 通道的拆分
b,g,r = cv.split(img)
# plt.imshow(b,cmap=plt.cm.gray)

img2 = cv.merge((b,g,r))

plt.imshow(img2[:,:,::-1])
plt.show()
