from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

# 训练数据
X_train = np.array([[2,1],[3,1],[1,4],[2,6]])
y = np.array([0,0,1,1])

# 模型
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train,y)

# 预测数据
X_test = np.array([[4,9]])
y_pred = knn.predict(X_test)
print(y_pred)

# 画图
X0 = X_train[y == 0]        
X1 = X_train[y == 1]             

plt.scatter(X0[:,0], X0[:,1], c='C0', label='Class 0')
plt.scatter(X1[:,0], X1[:,1], c='C1', label='Class 1')
color = 'C0' if y_pred[0] == 0 else 'C1'
plt.scatter(X_test[:,0], X_test[:,1], c=color, marker='x', s=100)

plt.legend()
plt.show()


