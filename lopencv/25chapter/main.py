import cv2 as cv
import matplotlib.pyplot as plt

dogsp = cv.imread("dogsp.jpeg")

# 均值滤婆
dog = cv.blur(dogsp,(5,5))
plt.imshow(dog[:,:,::-1])
plt.show()







