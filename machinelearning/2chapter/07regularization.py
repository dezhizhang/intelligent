import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


plt.rcParams['font.family'] = 'sans-serif'

plt.rcParams['axes.unicode_minus'] = False
# 生成数据
x = np.linspace(-3,3,300).reshape(-1,1)
y = np.sin(x) + np.random.uniform(low=-0.5,high=0.5,size=300).reshape(-1,1)


# 绘制散点图
fig,ax = plt.subplots(2,3,figsize=(15,8))
ax[0,0].scatter(x,y,c='y')
ax[0,1].scatter(x,y,c='y')
ax[0,2].scatter(x,y,c='y')
plt.show()


# 划分训练集与测试集
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.2,random_state=42)

# 过拟合情况
poly20 = PolynomialFeatures(degree=20)
x_train = poly20.fit_transform(train_x)
x_test = poly20.fit_transform(test_x)

print(x_train.shape)
print(x_test.shape)

# 定义模型
model = LinearRegression()

# 训练模型
model.fit(x_train,train_y)

# 预测结果，计算误差
y_pred1 = model.predict(x_test)
test_loss = mean_squared_error(test_y,y_pred1)

# 画出拟合曲线并
ax[0,0].plot(x,model.predict(poly20.fit_transform(x)),c='r')
ax[0,0].text(-3,1,f"测试误差:{test_loss:.4f}")
ax[1,0].bar(np.arange(21),model.coef_.reshape(-1))
plt.show()

