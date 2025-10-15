import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 创建一个全黑的图像
img = np.zeros((256,256,3),np.uint8)

# 2 获取图像的属性
img[100,100] = (0,0,255)

print(img.shape)
print(img.size)
print(img.dtype)

# 图像的拆分与合并
b,g,r = cv.split(img)
img = cv.merge((b,g,r))

cv.cvtColor(img,cv.COLOR_BGR2HSV)


# 3 显示图像
plt.imshow(img[:,:,::-1])
plt.show()
