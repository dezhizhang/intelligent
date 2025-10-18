import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg",0)

clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1 = clahe.apply(img)

# 显示图像
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img,cmap=plt.cm.gray)
axes[0].set_title("origin")
axes[1].imshow(cl1,cmap=plt.cm.gray)
axes[1].set_title("clahe")
plt.show()


