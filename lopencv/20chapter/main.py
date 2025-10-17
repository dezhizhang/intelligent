import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")

kernel = np.ones((5,5),np.uint8)

# 图像蚀和膨胀
erosion = cv.erode(img,kernel)
dilate = cv.dilate(img,kernel)


# 显示图像
fix,axes = plt.subplots(nrows=1,ncols=3,figsize=(10,8),dpi=100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("origin")
axes[1].imshow(erosion[:,:,::-1])
axes[1].set_title("erosion")
axes[2].imshow(dilate[:,:,::-1])
axes[2].set_title("dilate")
plt.show()

