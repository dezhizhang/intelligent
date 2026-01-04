import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
from torch import nn
from torch import optim
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt


# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_mins'] = False


#1. 定义函数创建线性回归样本数据
def create_dataset():
    x,y,coef = make_regression(
        n_samples=100,
        n_features=1,
        noise=10,
        coef=True,
        random_state=3
    )

    x1 = torch.tensor(x,dtype=torch.float32)
    y1 = torch.tensor(y,dtype=torch.float32)
    return x1,y1,coef

def train(x,y,coef):
    #1. 创建数据集对像
    dataset = TensorDataset(x,y)

    #2. 创建数据加载器对像
    dataloader = DataLoader(dataset,batch_size=16,shuffle=True)

    #3. 创建初始的线性回归模型
    model = nn.Linear(1,1)

    #4.创建损失函数对像
    criterion = nn.MSELoss()

    #5. 创建优化器
    optimizer = optim.SGD(model.parameters(),lr=0.01)

    #6. 具体的训练过程
    epochs,loss_list,total_loss,total_samples = 100,[],0.0,0

    for epoch in range(epochs):
        for train_x,train_y in dataloader:
            # 模型的预测
            y_pred = model(train_x)
            #  计算每批的平均损失值
            loss = criterion(y_pred,train_y.reshape(-1,1))
            # 计算总损失和样本批次数
            total_loss += loss.item()

            total_samples +=1
            # 梯度清零+返向传播+梯度更新
            optimizer.zero_grad()
            #反向转播
            loss.backward()
            optimizer.step()
            # 把本轮的平均损失值添加到列表中
            loss_list.append(total_loss / total_samples)
            print(f"轮数:{epoch + 1}")

            # 打印最终的训练结果
    print(f"{epochs}平均损失为:{loss_list}")
    print(f"模型参数:{model.weight}偏置:{model.bias}")


    plt.plot(range(epochs),loss_list)
    plt.grid()
    plt.show()






if __name__ == '__main__':
    x,y,coef = create_dataset()
    train(x,y,coef)

