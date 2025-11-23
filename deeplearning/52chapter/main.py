import torch
import torch.nn as nn

def dm03():
    y_true = torch.tensor([2.0,2.0,2.0],dtype=torch.float)
    y_pred = torch.tensor([1.0,1.0,1.9],requires_grad=True)

    # 创建smooth l1 损失函数
    criterion = nn.SmoothL1Loss()

    # 计算损失
    loss = criterion(y_pred,y_true)

    # 输出损失
    print(f"{loss}")

if __name__ == '__main__':
    dm03()