import numpy as np
import matplotlib.pyplot as plt


def J(x):
    return (x ** 2 - 2) ** 2


def gradient(x):
    return 4 * x ** 3 - 8 * x


# 定义超参数
alpha = 0.1
x = 1
x_list = []
y_list = []

while np.abs(grad := gradient(x)) > 1e-10:
    y = J(x)
    x_list.append(x)
    y_list.append(y)
    grad = gradient(x)
    x = x - alpha * grad


# 画图
x = np.arange(0.9,1.6,0.01)
plt.plot(x,J(x))
plt.plot(x_list,y_list,'r')
plt.scatter(x_list,y_list,color="r")
plt.show()

# 局部放大
fig,ax = plt.subplots(1,2,figsize=(15,4))
ax[0].plot(x,J(x))
ax[0].plot(x_list,y_list,'r')
ax[0].plot(x_list,y_list,color='r')

x_list2 = x_list[1:]
y_list2 = y_list[1:]

x = np.arange(1.399,1.425,0.001)
plt.plot(x,J(x))
plt.plot(x_list2,y_list2,'r')
plt.scatter(x_list2,y_list2,color="r")
plt.show()







