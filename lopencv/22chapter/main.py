import cv2

img = cv2.imread("car.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()
