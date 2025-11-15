from sklearn.linear_model import LinearRegression

#1. 准备数据
x_train = [[160], [166], [172], [174], [180]]
y_train = [56.3, 60.6, 65.1, 68.5, 75]
x_test = [[176]]
#2. 数据预处理

#4. 模型训练
estimator = LinearRegression()

#4.2 具体的训练动作
estimator.fit(x_train,y_train)

#4.3 模型回归
print(f"权重:{estimator.coef_}")
print(f"偏重:{estimator.intercept_}")