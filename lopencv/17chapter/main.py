import cv2
import numpy as np
img = cv2.imread("lena.jpg",cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobel_y = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
sobel_xy = cv2.addWeighted(sobel_x,0.5,sobel_y,0.5,0)


laplacian = cv2.Laplacian(img,cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

res = np.hstack((sobel_xy,laplacian))

cv2.imshow("res",res)
cv2.waitKey(0)
cv2.destroyAllWindows()


