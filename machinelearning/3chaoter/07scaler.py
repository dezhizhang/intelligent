from sklearn.preprocessing import MinMaxScaler

X = [[2,1],[3,1],[1, 4], [2,6]]

# 定义归一化对像
scaler = MinMaxScaler()
scaler.fit(X)

# 将缩放应用到特征上
x_scaled = scaler.transform(X)
print(x_scaled)

