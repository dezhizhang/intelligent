
import cv2 as cv
import matplotlib.pyplot as plt

rain = cv.imread("rain.jpg")
view = cv.imread("view.jpg")

img = cv.add(rain,view)

plt.imshow(img[:,:,::-1])
plt.show()








