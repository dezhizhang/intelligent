import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
from collections import Counter

# 1. 定义函数接收用户的索引
def show_digit(idx):
    # 读取数居集
    df = pd.read_csv("手写数字识别.csv")

    # 判断传入的索引是否越界
    if idx < 0 or idx >= len(df) - 1:
        print("索引越界!")
        return

    x = df.iloc[:,1:]
    y = df.iloc[:,0]

    # 查看用户传入的过引对应的图片
    # print(f"{y.iloc[idx]}")
    #
    # print(x.iloc[idx].shape)
    # print(x.iloc[idx].values)

    x = x.iloc[idx].values.reshape(28,28)

    plt.imshow(x,cmap="gray")
    plt.show()




if __name__ == "__main__":
    show_digit(9)