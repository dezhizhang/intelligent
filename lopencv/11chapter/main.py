import cv2 as cv
import matplotlib.pyplot as plt

# 读取图像
view = cv.imread("view.jpg")
rain = cv.imread("rain.jpg")

# 图像混合
img = cv.addWeighted(view,0.7,rain,0.3,0)

# 图像的显示
plt.figure(figsize=(8,8))
plt.imshow(img[:,:,::-1])
plt.show()

