import  cv2 as cv
import matplotlib.pyplot as plt

dogGausss = cv.imread("dogGauss.jpeg")

dog = cv.GaussianBlur(dogGausss,(3,3),1)
plt.imshow(dog[:,:,::-1])
plt.show()

