import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 线检测
img = cv.imread("rili.jpg",0)
edges = cv.Canny(img,50,150)


lines = cv.HoughLines(edges,0.8,np.pi / 180,150)
# 先转成彩色图方便画线
color_img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)

    x0 = rho * a
    y0 = rho * b

    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)

    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)

    cv.line(color_img,(x1,y1),(x2,y2),(0,255,0))


plt.imshow(cv.cvtColor(color_img, cv.COLOR_BGR2RGB))
plt.show()




