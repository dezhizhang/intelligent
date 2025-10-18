
import cv2 as cv
import matplotlib.pyplot as plt

dogsp = cv.imread("dogsp.jpeg")

# 中值滤
dog = cv.medianBlur(dogsp,3)

# 显示图像
plt.imshow(dog[:,:,::-1])
plt.show()
