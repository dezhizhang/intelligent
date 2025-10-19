import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

star = cv.imread("star.jpeg")
gray_img = cv.cvtColor(star, cv.COLOR_BGR2GRAY)

img = cv.medianBlur(gray_img, 7)

circles = cv.HoughCircles(
    img,
    cv.HOUGH_GRADIENT,
    dp=1,
    minDist=200,
    param1=100,
    param2=50,
    minRadius=0,
    maxRadius=100
)

if circles is not None:
    circles = np.uint16(np.around(circles))  # 转为整数方便绘制
    for i in circles[0, :]:
        # 画圆
        cv.circle(star, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # 画圆心
        cv.circle(star, (i[0], i[1]), 2, (0, 0, 255), 3)

plt.imshow(cv.cvtColor(star, cv.COLOR_BGR2RGB))
plt.show()
