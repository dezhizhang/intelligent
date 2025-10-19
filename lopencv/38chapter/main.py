import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("bai.jpeg")
template = cv.imread("wulin.jpeg")

h,w,l = template.shape
res = cv.matchTemplate(img,template,cv.TM_CCORR)
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w,top_left[1] + h)
cv.rectangle(img,top_left,bottom_right,(0,255,0),2)

# 显示图像
plt.imshow(img[:,:,::-1])
plt.title("result")
plt.xticks([])
plt.yticks([])
plt.show()



