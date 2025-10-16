
import cv2 as cv
import numpy as np

img = cv.imread("img.png")

# 绝对变换
rows,cols = img.shape[:2]
res = cv.resize(img,(2 *cols,2 *rows),interpolation=cv.INTER_CUBIC)

# 相对变换
res1 = cv.resize(img,None,fx=0.5,fy=0.5)

cv.imshow("res1",res1)
cv.waitKey(0)
cv.destroyAllWindows()


