import cv2

img = cv2.imread("../6chapter/16853.jpg")
cat = img[0:200,0:200]
b,g,r = cv2.split(img)
# print(b,g,r)
print("b",b.shape)
print("g",b.shape)
print("r",r.shape)

# 合并
img = cv2.merge((b,g,r))
print(img.shape)







