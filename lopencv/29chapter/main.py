import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg")
mask = np.zeros(img.shape[:2],np.uint8)
mask[400:650,200:500] = 255

mask_img = cv.bitwise_and(img,img,mask=mask)

mask_histr = cv.calcHist([img],[0],mask,[256],[1,256])

# 显示图像
fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(10,8))
axes[0,0].imshow(img,cmap=plt.cm.gray)
axes[0,0].set_title("origin")
axes[0,1].imshow(mask,cmap=plt.cm.gray)
axes[0,1].set_title("mask")
axes[1,0].imshow(mask_img,cmap=plt.cm.gray)
axes[1,1].plot(mask_histr)
axes[1,1].grid()
axes[1,1].set_title('grid')


plt.show()




