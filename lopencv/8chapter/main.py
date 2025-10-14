import cv2
img_gray = cv2.imread("img.png")

ret,thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
print(ret,thresh)
