import cv2
import numpy as np

img = cv2.imread("../15chapter/img.png")

kernel = np.ones((3,3),np.uint8)
dige_erosion = cv2.erode(img,kernel,iterations=1)

dige_dilate = cv2.dilate(dige_erosion,kernel,iterations=1)

cv2.imshow("dilate",dige_dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()



