"""
线性回归介绍(Linear Regressor)
    概述/目的:

    分类:
        一元线性回归：1个特征+1个标签列
        多元线性回归：多个特征+1个标签列

    公式:
    一元线性回归:
        y=kx+b=> wx+b
    多元线性回归:

"""

from sklearn.linear_model import LinearRegression

# 1. 准备数据
x_train = [[160],[166],[172],[174],[180]] # 训练集的特征
y_train = [56.3,60.6,65.1,68.5,75]        # 训练集的标签
x_test = [[176]]                          # 测试集的特征



# 模型训练
estimator = LinearRegression()
estimator.fit(x_train,y_train)
print(f"权重:{estimator.coef_}")
print(f"偏置:{estimator.intercept_}")

# 模型预测
y_pre = estimator.predict(x_test)
print(f"预测值为:{y_pre}")


