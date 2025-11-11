import numpy as np
from sklearn.preprocessing import MinMaxScaler


x_train = [
    [90,3,10,40],
    [60,4,15,45],
    [75,3,13,46]
]

# 创建归一化对像
scaler = MinMaxScaler()

# 对原数据集进行归一化
x_train_new = scaler.fit_transform(x_train)


print(x_train_new)


