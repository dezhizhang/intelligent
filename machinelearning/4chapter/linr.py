import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


X = [[5],[8],[10],[12],[15],[3],[7],[9],[14],[6]]

y = [55,65,70,75,85,50,60,72,80,58]

# 创建模型
model = LinearRegression()
model.fit(X,y)


# print(model.coef_)
# print(model.intercept_)

# 预测
x_new = [[11]]
y_pred = model.predict(x_new)


x_line = np.arange(0,15,0.1).reshape(-1,1)
y_line = model.predict(x_line)


plt.scatter(X,y)
plt.plot(x_line,y_line,color='red')
plt.scatter(x_new,y_pred,color='yello')
plt.show()




