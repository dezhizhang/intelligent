"""
案例：演示KNN算法识别图片，即:手写数字识别
介始:
    每张图片都是由28 *  28
"""

import matplotlib.pyplot as plt
import pandas as pd
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



if __name__ == '__main__':
    show_digit(9)



