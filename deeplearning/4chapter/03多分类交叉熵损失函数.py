import torch
import torch.nn as nn

def dm01():
    # 手机创建样本的真实值
    y_true = torch.tensor([0,1,0],dtype=torch.float32)

    # 设置预测
    y_pred = torch.tensor([0.6901,0.5423,0.2639])

    # 创建二叉类熵损失函数
    criterion = nn.MSELoss()

    # 计算损失值
    loss = criterion(y_pred,y_true).detach().numpy()
    print(f"损失值:{loss}")

if __name__ == '__main__':
    dm01()
