import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")
rows,cols = img.shape[:2]

M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))

# 显示图像
fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("original")
axes[1].imshow(dst[:,:,::-1])
axes[1].set_title("translation")
plt.show()




