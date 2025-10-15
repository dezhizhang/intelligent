import cv2

import numpy as np

img = cv2.imread("img.png")
kernel = np.ones((7,7),np.uint8)

dilate = cv2.dilate(img,kernel,iterations=5)
erosion = cv2.erode(img,kernel,iterations=5)

res = np.hstack((dilate,erosion))

cv2.imshow("res",res)
cv2.waitKey(0)
cv2.destroyAllWindows()

