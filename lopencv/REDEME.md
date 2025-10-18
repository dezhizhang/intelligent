# opencv

### opencv的安装

```bash
pip install opencv-python
pip install opencv-contrib-python
```

### 图像的io操作

```python
import cv2 as cv

# 读取图像
img = cv.imread("img.png", 0)
# 显示图像
cv.imshow("img", img)
# 等待时间
cv.waitKey(0)
# 保存图像
cv.imwrite("test.png", img)
cv.destroyAllWindows()

```

### 图像上绘制图形

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1 创建一个空白图形
img = np.zeros((512, 512, 3), np.uint8)

# 2 绘制图形
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "opencv", (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

# 图像显示
plt.imshow(img[:, :, ::-1])
plt.title('draw'), plt.xticks([]), plt.yticks([])
plt.show()

```

### 获取并修改图像中的像素点

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 创建一个全黑的图像
img = np.zeros((256, 256, 3), np.uint8)

# 2 获取图像的属性
img[100, 100] = (0, 0, 255)

print(img.shape)
print(img.size)
print(img.dtype)

# 图像的拆分与合并
b, g, r = cv.split(img)
img = cv.merge((b, g, r))

cv.cvtColor(img, cv.COLOR_BGR2HSV)

# 3 显示图像
plt.imshow(img[:, :, ::-1])
plt.show()

```

### 图像的拆分与合并

```python

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")

# 通道的拆分
b, g, r = cv.split(img)
# plt.imshow(b,cmap=plt.cm.gray)

img2 = cv.merge((b, g, r))

plt.imshow(img2[:, :, ::-1])
plt.show()

```

### 图像的加法操作

```python

import cv2 as cv
import matplotlib.pyplot as plt

rain = cv.imread("rain.jpg")

view = cv.imread("view.jpg")

img1 = cv.add(rain, view)

plt.imshow(img1[:, :, ::-1])
plt.show()

```

### 图像的混合

```python
import cv2 as cv
import matplotlib.pyplot as plt

# 读取图像
view = cv.imread("view.jpg")
rain = cv.imread("rain.jpg")

# 图像混合
img = cv.addWeighted(view, 0.7, rain, 0.3, 0)

# 图像的显示
plt.figure(figsize=(8, 8))
plt.imshow(img[:, :, ::-1])
plt.show()

```

### 图像的缩放

```python
import cv2 as cv
import numpy as np

img = cv.imread("img.png")

# 绝对
rows, cols = img.shape[:2]
res = cv.resize(img, (2 * cols, 2 * rows), interpolation=cv.INTER_CUBIC)

# 相对
res1 = cv.resize(img, None, fx=0.5, fy=0.5)

img1 = np.hstack((res, res))

cv.imshow("img1", img1)
cv.waitKey(0)
cv.destroyAllWindows()


```

### 图像的平移

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")

rows, cols = img.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))

# 图像显示
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img[:, :, ::-1])
axes[0].set_title("Original")
axes[1].imshow(dst[:, :, ::-1])
axes[1].set_title("Translation")
plt.show()


```

### 图像旋转

```python
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")

# 图像旋转
rows, cols = img.shape[:2]
# 生成旋转矩阵
matr = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
# 进行旋转变换
dst = cv.warpAffine(img, matr, (cols, rows))

# 显示图像
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img[:, :, ::-1])
axes[0].set_title("origin")
axes[1].imshow(dst[:, :, ::-1])
axes[1].set_title("rotate")
plt.show()

```

### 图像的防射变换

```python

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread("img.png")

# 防射变换
rows, cols = img.shape[:2]

# 创建变换矩阵
pst1 = np.float32([[50, 50], [200, 50], [50, 200]])
pst2 = np.float32([[100, 100], [200, 50], [100, 250]])

matrix = cv.getAffineTransform(pst1, pst2)
# 完成防射变换
dst = cv.warpAffine(img, matrix, (cols, rows))

# 显示图像
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img[:, :, ::-1])
axes[0].set_title("origin")
axes[1].imshow(dst[:, :, ::-1])
axes[1].set_title("ray")
plt.show()

```

### 图像的透射变换

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")

# 透射变换
rows, cols = img.shape[:2]

# 创建变换矩阵
pst1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pst2 = np.float32([[100, 145], [300, 100], [80, 290], [310, 300]])

matrix = cv.getPerspectiveTransform(pst1, pst2)
# 进行变换
dst = cv.warpPerspective(img, matrix, (cols, rows))

# 显示图像
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img[:, :, ::-1])
axes[0].set_title("origin")
axes[1].imshow(dst[:, :, ::-1])
axes[1].set_title("opacity")
plt.show()

```

### 图像金字塔

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")
# 进行图像采样
up_img = cv.pyrUp(img)
down_img = cv.pyrDown(img)

# 显示图像
cv.imshow("enlarge", up_img)
cv.imshow("origin", img)
cv.imshow("shrink", down_img)
cv.waitKey(0)
cv.destroyAllWindows()

```

### 膨胀与腐蚀

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("img.png")

kernel = np.ones((5, 5), np.uint8)

# 图像蚀和膨胀
erosion = cv.erode(img, kernel)
dilate = cv.dilate(img, kernel)

# 显示图像
fix, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 8), dpi=100)
axes[0].imshow(img[:, :, ::-1])
axes[0].set_title("origin")
axes[1].imshow(erosion[:, :, ::-1])
axes[1].set_title("erosion")
axes[2].imshow(dilate[:, :, ::-1])
axes[2].set_title("dilate")
plt.show()


```

### 图像的开闭运算

```python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

close = cv.imread("letterclose.png")
open = cv.imread("letteropen.png")

kernel = np.ones((10, 10), np.uint8)

# 图像的开闭运算
cvOpen = cv.morphologyEx(open, cv.MORPH_OPEN, kernel)
cvClose = cv.morphologyEx(close, cv.MORPH_CLOSE, kernel)

# 图像显示
fix, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].imshow(close)
axes[0, 0].set_title("origin")
axes[0, 1].imshow(cvOpen)
axes[0, 1].set_title("open")
axes[1, 0].imshow(open)
axes[1, 1].imshow(cvClose)
axes[1, 1].set_title("close")
plt.show()

```

### 均值滤波

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

dogsp = cv.imread("dogsp.jpeg")

doggau = cv.imread("dogGauss.jpeg")

# 均值滤波
dog = cv.blur(dogsp, (5, 5))
plt.imshow(dog[:, :, ::-1])
plt.show()

```

### 高斯滤波

```python
import cv2 as cv
import matplotlib.pyplot as plt

dogGauss = cv.imread("dogGauss.jpeg")

dog = cv.GaussianBlur(dogGauss, (3, 3), 1)
plt.imshow(dog[:, :, ::-1])
plt.show()

```

### 中值滤波

```python
import cv2 as cv
import matplotlib.pyplot as plt

dogsp = cv.imread("dogsp.jpeg")

# 中值滤
dog = cv.medianBlur(dogsp, 3)

# 显示图像
plt.imshow(dog[:, :, ::-1])
plt.show()

```

### 直方图

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg")

histr = cv.calcHist([img], [0], None, [256], [0, 256])

# 绘制灰度图
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(histr)
plt.grid()
plt.show()

```

### 掩膜的应用

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg")
mask = np.zeros(img.shape[:2], np.uint8)
mask[400:650, 200:500] = 255

mask_img = cv.bitwise_and(img, img, mask=mask)

mask_histr = cv.calcHist([img], [0], mask, [256], [1, 256])

# 显示图像
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].imshow(img, cmap=plt.cm.gray)
axes[0, 0].set_title("origin")
axes[0, 1].imshow(mask, cmap=plt.cm.gray)
axes[0, 1].set_title("mask")
axes[1, 0].imshow(mask_img, cmap=plt.cm.gray)
axes[1, 1].plot(mask_histr)
axes[1, 1].grid()
axes[1, 1].set_title('grid')

plt.show()

```

### 直方向均化

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg", 0)

dst = cv.equalizeHist(img)

# 显示结果
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img)
axes[0].set_title("origin")
axes[1].imshow(dst, cmap=plt.cm.gray)
axes[1].set_title("equalize")
plt.show()


```

### 自适应均衡化

```python
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("cat.jpeg", 0)

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

# 显示图像
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img, cmap=plt.cm.gray)
axes[0].set_title("origin")
axes[1].imshow(cl1, cmap=plt.cm.gray)
axes[1].set_title("clahe")
plt.show()

```