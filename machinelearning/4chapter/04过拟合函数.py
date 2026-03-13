import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def dm03_over_fitting():
    # 1. 准备数据
    np.random.seed(23)
    # 2. 生成随机X轴100个数据
    x = np.random.uniform(-3,3,100)

    # 3. 线性回归方程
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0,1,100)
    # 4. 数据预处理
    X = x.reshape(-1,1)

    X3 = np.hstack([X,X ** 2,X ** 3,X ** 4,X ** 5,X ** 6,X ** 7,X ** 8,X ** 9,X ** 10])

    # 5. 模型训练
    estimator = LinearRegression()
    estimator.fit(X3,y)

    # 6. 模型预测
    y_predict = estimator.predict(X3)

    plt.scatter(X,y)
    plt.plot(np.sort(x),y_predict[np.argsort(x)],color='red')
    plt.show()

if __name__ == '__main__':
    dm03_over_fitting()





