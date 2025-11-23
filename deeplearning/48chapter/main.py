from logging import critical

import torch
import  torch.nn as nn


def dm01():
    #1. 手机创建样本的真实值
    # y_true = torch.tensor([[0,1,0],[1,0,0]],dtype=torch.float)
    # print(f"y_true:{y_true}")

    y_true = torch.tensor([1,2])


    y_pred = torch.tensor([[0.1,0.8,0.1],[0.7,0.2,0.3]],requires_grad=True,dtype=torch.float)

    #3.创建多分类交叉熵损失函数
    criterion = nn.CrossEntropyLoss() # 平均损失

    # 计算损失值
    loss = criterion(y_pred, y_true)
    print(f"损失值:{loss}")

if __name__ == '__main__':
    dm01()