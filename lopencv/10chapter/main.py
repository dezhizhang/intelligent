# import cv2
#
# img = cv2.imread("img.png")
#
# gaussian = cv2.GaussianBlur(img,(5,5),1)
# cv2.imshow("gaussian",gaussian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import  cv2

img = cv2.imread("../11chapter/img.png")

gaussian = cv2.GaussianBlur(img,(5,5),1)
cv2.imshow("gaussian",gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()




