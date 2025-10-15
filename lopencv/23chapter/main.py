import cv2

img = cv2.imread("lena.jpg",0)
template = cv2.imread("face.jpg",0)

h,w = template.shape[:2]

print(img.shape)


res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)

min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
print(max_loc,min_loc)
