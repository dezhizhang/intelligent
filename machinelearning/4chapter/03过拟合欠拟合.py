"""
案例:
    演示： 欠拟合，正好拟合，过拟合，L1正则化
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error,root_mean_squared_error,mean_absolute_error
from sklearn.linear_model import Ridge,RidgeCV


def dm01_under_fitting():
    # 1. 随机生成x轴100个数据，模拟：特征
    x = np.random.uniform(-3,3,100)
    # 2. 基于x轴值通过线生公式，生成y轴100个数据
    y = 0.5 * x * x **2 + x + 2 + np.random.normal(0,1,100)

    # 3. 数据预处理
    X = x.reshape(-1,1)

    # 4. 训练模型
    estimator = LinearRegression()
    estimator.fit(X,y)

    # 5. 模型预测
    y_pre = estimator.predict(X)

    # 6. 模型评估
    print(f"均方误差:{mean_squared_error(y,y_pre)}")

    # 7. 绘图
    plt.scatter(x,y)
    plt.plot(X,y_pre,color='red')
    plt.show()


def dm01_just_fitting():
    np.random.seed(23)

    x = np.random.uniform(-3,3,100)

    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0,1,100)
    print(f"特征:{x[:5]}")
    print(f"标签:{y[:5]}")

    X = x.reshape(-1,1)
    X2 = np.stack([x,X ** 2])

    # 模型训练
    estimator = LinearRegression()
    estimator.fit(X2,y)

    # 模型预测
    y_pre = estimator.predict(X2)

    plt.scatter(x,y)
    plt.plot(X,y_pre,color='red')
    plt.show()




if __name__ == '__main__':
    dm01_just_fitting()