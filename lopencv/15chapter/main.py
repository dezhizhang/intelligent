
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread("img.png")

# 防射变换
rows,cols = img.shape[:2]

# 创建变换矩阵
pst1 = np.float32([[50,50],[200,50],[50,200]])
pst2 = np.float32([[100,100],[200,50],[100,250]])

matrix = cv.getAffineTransform(pst1,pst2)
# 完成防射变换
dst = cv.warpAffine(img,matrix,(cols,rows))

# 显示图像
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("origin")
axes[1].imshow(dst[:,:,::-1])
axes[1].set_title("ray")
plt.show()
