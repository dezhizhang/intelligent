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

trainX,testX,trainY,testY = train_test_split(x,y,test_size=0.2,random_state=42)

# 定义模型
model = LinearRegression()

# 第一次拟合
x_train1 = trainX
x_test1 = testX

model.fit(x_train1,trainY)

# 打印查看模型参数
print(model.coef_)
print(model.intercept_)

#5. 预测结果计算误差
y_pred1 = model.predict(x_test1)
test_loss = mean_squared_error(testY,y_pred1)
train_loss1 = mean_squared_error(trainY,model.predict(x_train1))

# 画出拟合典线并写出训练误差与
ax[0].plot(x,model.predict(x),'r')
ax[0].text(-3,1,f"test loss: {test_loss:.4f}")
ax[1].text(-3,1.3,f"train loss: {train_loss1:.4f}")
plt.show()





