import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error


# 生成数据

x = np.linspace(-3,3,300).reshape(-1,1)
y = np.sin(x) + np.random.uniform(low=-0.5, high=0.5, size=x.shape).reshape(-1,1)

print(x.shape)
print(y.shape)
print("" * 30)

# 绘制图像
fig,ax = plt.subplots(1,3,figsize=(15,4))
ax[0].scatter(x,y)
ax[1].scatter(x,y)
ax[2].scatter(x,y)

plt.show()


