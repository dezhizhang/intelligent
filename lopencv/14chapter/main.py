import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")

# 图像旋转
rows,cols = img.shape[:2]
# 生成旋转矩阵
matrix = cv.getRotationMatrix2D((cols/2,rows/2),90,1)
# 进行旋转
dst = cv.warpAffine(img,matrix,(cols,rows))

# 显示图像
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(10,8),dpi=100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("origin")
axes[1].imshow(dst[:,:,::-1])
axes[1].set_title("rotate")
plt.show()

