from sklearn.preprocessing import MinMaxScaler

x_train = [
    [90, 3, 10, 40],
    [60, 4, 15, 45],
    [75, 3, 13, 46]
]

# 创建归一化
transfer = MinMaxScaler()

# 对原如数据进行归一化
x_train_new = transfer.fit_transform(x_train)

print(x_train_new)
