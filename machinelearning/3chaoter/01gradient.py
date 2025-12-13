import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def gradient(x):
    return 2*x

# 用列表保存点的变化轨迹
x_list = []
y_list = []

# 定义超参数和x的初始值
alpha = 0.1
x = 1

# 重复迭代100次
for i in range(100):
    y = f(x)
    x_list.append(x)
    y_list.append(y)

    grad = gradient(x)
    x = x - alpha*grad



x = np.arange(-1,1,0.01)
print(x,f(x))
plt.plot(x,f(x))
plt.plot(x_list,y_list,"r")
plt.scatter(x_list,y_list,color="r")
plt.show()


