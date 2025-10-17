import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

close = cv.imread("letterclose.png")
open = cv.imread("letteropen.png")

kernel = np.ones((10,10),np.uint8)

# 图像的开闭运算
cvOpen = cv.morphologyEx(open,cv.MORPH_OPEN,kernel)
cvClose = cv.morphologyEx(close,cv.MORPH_CLOSE,kernel)


# 图像显示
fix,axes = plt.subplots(nrows=2,ncols=2,figsize=(10,8))
axes[0,0].imshow(close)
axes[0,0].set_title("origin")
axes[0,1].imshow(cvOpen)
axes[0,1].set_title("open")
axes[1,0].imshow(open)
axes[1,1].imshow(cvClose)
axes[1,1].set_title("close")
plt.show()



