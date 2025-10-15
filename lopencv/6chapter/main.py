import cv2 as cv
img = cv.imread("img.png",0)
# 显示图像
cv.imshow("img",img)
# 等待时间
cv.waitKey(0)
# 保存图像
cv.imwrite("6chapter/test.png",img)






