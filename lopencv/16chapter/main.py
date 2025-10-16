import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")

# 透射变换
rows,cols = img.shape[:2]

# 创建变换矩阵
pst1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pst2 = np.float32([[100,145],[300,100],[80,290],[310,300]])

matrix = cv.getPerspectiveTransform(pst1,pst2)

# 进行变换
dst = cv.warpPerspective(img,matrix,(cols,rows))

# 显示图像
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("origin")
axes[1].imshow(dst[:,:,::-1])
axes[1].set_title("opacity")
plt.show()
