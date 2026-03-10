"""
案例：演示KNN算法识别图片，即:手写数字识别
介始:
    每张图片都是由28 *  28
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
from collections import Counter


# 1 定义函数，接收用户传入的索引，展示索引对应的图片
def show_digit(idx):
    # 1. 读取数据集,获取到数据源
    df = pd.read_csv('../assets/手写数字识别.csv')

    # 2. 判断传入的索引是否越界
    if idx < 0 or idx >= len(df) - 1:
        raise ValueError('索引越界')

    # 3. 获取训练集数据
    x = df.iloc[:,1:]
    y = df.iloc[:,0]


    # 4.查看用户传入索引对应的图片
    print(f"该图片对应的数字是:{y.iloc[idx]}")

    # 5. 转换数据把(784,) 转换成(28,28)
    x = x.iloc[idx].values.reshape(28, 28)


    # 具体的绘制恢度图
    plt.imshow(x, cmap='gray')
    plt.axis('off')
    plt.show()


def train_model():
    # 1. 加载数据集
    df = pd.read_csv('../assets/手写数字识别.csv')
    # 2. 数据预处理
    x = df.iloc[:,1:]
    y = df.iloc[:,0]

    # 3. 数据归一化处理
    x = x / 255

    x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2, random_state=23,stratify=y)

    # 4. 模型训练
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)

    # 5. 模型评估
    print(f"准确率:{estimator.score(x_train, y_train)}")
    print(f"准确率：{accuracy_score(y_test,estimator.predict(x_test))}")

    # 6. 保存模型
    joblib.dump(estimator, '../model/手写数字识别.pkl')

def use_model():
    # 1. 加载图片
    x = plt.imread('../assets/demo.png')
    # 2. 绘制图片
    plt.imshow(x,cmap='gray')
    plt.show()

    # 3. 加载模型
    estimator = joblib.load('../model/手写数字识别.pkl')

    # 4. 模型预测
    x = x.reshape(1,-1) / 255

    # 5. 模型预测
    y_pre = estimator.predict(x)

    # 6. 打印预测结果
    print(f"预测值为:{y_pre}")



if __name__ == '__main__':
    use_model()



