from sklearn.preprocessing import  StandardScaler
x_train = [
    [90, 3, 10, 40],
    [60, 4, 15, 45],
    [75, 3, 13, 46]
]

# 创建标准化对像
transfer = StandardScaler()

x_train_new = transfer.fit_transform(x_train)

print(f"标准化后的数据集:\n")
print(x_train_new)