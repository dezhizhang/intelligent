import torch
import torch.nn as nn


def dm02():
    # 设置真实值
    # y_true = torch.tensor([0,1,0],dtype=torch.float)
    #
    # # 设置预测值
    # y_pred = torch.tensor([0.690,0.5423,0.2639])
    # # 创建二分类交叉熵损失函数
    # criterion = nn.BCELoss()
    # # 计算损失值
    # loss = criterion(y_pred,y_true)
    # print(f"损失值:{loss}")

    y_true = torch.tensor([0,1,0],dtype=torch.float)

    # 设置预测值
    y_pred = torch.tensor([0.690,0.5423,0.2639])
    # 创建二分类交叉熵损失函数
    criterion = nn.BCELoss()
    #计算损失值
    loss = criterion(y_pred,y_true)
    print(f"损失值:{loss}")


if __name__ == "__main__":
    dm02()
