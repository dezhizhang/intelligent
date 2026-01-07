import torch
import torch.nn as nn


def dm01():
    y_true = torch.tensor([2.0,2.0,2.0],dtype=torch.float32)

    # 定义变量记录预测值
    y_pred = torch.tensor([11.0,1.0,1.9],requires_grad=True)

    criterion = nn.L1Loss()

    # 计算损失
    loss = criterion(y_pred,y_true)

    # 打印损失
    print(f"MAE:{loss}")


if __name__ == '__main__':
    dm01()
