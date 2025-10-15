import cv2 as cv
import numpy as np
img = cv.imread("img.png")

# 绝对
rows,cols = img.shape[:2]
res = cv.resize(img,(2 * cols,2*rows),interpolation=cv.INTER_CUBIC)


# 相对
res1 = cv.resize(img,None,fx=0.5,fy=0.5)

img1 = np.hstack((res,res))


cv.imshow("img1",img1)
cv.waitKey(0)
cv.destroyAllWindows()


