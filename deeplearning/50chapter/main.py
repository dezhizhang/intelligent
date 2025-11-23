import torch
import torch.nn as nn


def dm01():

    # 定义真实值
    y_true = torch.tensor([2.0,2.0,2.0],dtype=torch.float)
    # 定义预测值
    y_pred = torch.tensor([1.0,1.0,1.9],requires_grad=True)

    # 创建损失函数
    criterion = nn.L1Loss()

    # 计算损失函数
    loss = criterion(y_pred, y_true)

    print(f"损失函数:{loss}")

if __name__ == '__main__':
    dm01()