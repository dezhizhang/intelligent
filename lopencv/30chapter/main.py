import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg",0)

dst = cv.equalizeHist(img)

# 显示结果
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img)
axes[0].set_title("origin")
axes[1].imshow(dst,cmap=plt.cm.gray)
axes[1].set_title("equalize")
plt.show()

