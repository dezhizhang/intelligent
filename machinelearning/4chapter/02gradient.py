import numpy as np



X = np.array([[5], [8], [8], [10], [12], [15], [3], [7], [9], [14], [14], [6]])

y = np.array([[55], [65], [70], [75], [85], [50], [50], [60], [72], [80], [58]])

n = X.shape[0]


# 损失函数
def J(beta):
    return np.sum((X @ beta - y) ** 2) / n


def gradient(beta):
    return X.T @ (X @ beta - y) / n * 2


# 数据处理
X = np.hstack((np.ones((n, 1)), X))

# 定义超参数
alpha = 0.01
iter = 10000

beta = np.array([[1],[1]])


for i in range(iter):
    grad = gradient(beta)

    beta = beta - alpha * grad

    if i % 100 == 0:
        print(f"beat:{beta.reshape(-1)}\t:{J(beta)}")

