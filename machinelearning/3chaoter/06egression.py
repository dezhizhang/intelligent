from sklearn.neighbors import KNeighborsClassifier


X = [[2,1],[3,1],[1, 4], [2,6]]
y = [0,1,0,1]

# 定义模型
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X,y)

# 预测
x = [[4,9]]
x_pred = knn.predict(x)
print(x_pred)
