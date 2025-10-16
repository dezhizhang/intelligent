import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")
# 进行图像采样
up_img = cv.pyrUp(img)
down_img = cv.pyrDown(img)

# 显示图像
cv.imshow("enlarge",up_img)
cv.imshow("origin",img)
cv.imshow("shrink",down_img)
cv.waitKey(0)
cv.destroyAllWindows()


