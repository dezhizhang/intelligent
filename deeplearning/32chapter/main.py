import torch
from numpy import dtype
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
from torch import nn
from torch import optim
from sklearn.datasets import make_regression

import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_mins'] = False

# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_mins'] = False

# 1. 定义函数，创建线性回归样本数居
def create_dataset():
    x,y,coef = make_regression(
        n_samples=100,
        n_targets=1,
        noise=10,
        coef=True,
        random_state=3
    )

    # 将数据封装成张量类型
    x = torch.tensor(x,dtype=torch.float32)
    y = torch.tensor(y,dtype=torch.float32)

    return x,y,coef

#2. 定义函数，表示模型训练
def train(x,y,coef):
    dataset = TensorDataset(x,y)
    dataloader = DataLoader(dataset,batch_size=16,shuffle=True)

    model = nn.Linear(100, 1)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(),lr=0.01)

    epochs = 100
    loss_list = []

    for epoch in range(epochs):
        total_loss = 0.0
        total_samples = 0

        for train_x,train_y in dataloader:
            y_pred = model(train_x)
            loss = criterion(y_pred,train_y.reshape(-1,1))

            total_loss += loss.item()
            total_samples += 1

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # 每轮平均损失
        loss_list.append(total_loss / total_samples)

        print(f"epoch: {epoch}, loss: {loss_list[-1]}")


    plt.plot(range(epochs), loss_list)
    plt.grid()
    plt.show()

    plt.scatter(x,y)
    plt.show()


if __name__ == "__main__":
    x,y,coef = create_dataset()
    train(x,y,coef)



