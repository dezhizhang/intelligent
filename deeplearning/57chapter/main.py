from logging import critical

import torch
import torch.nn as nn
import torch.optim as optim

def dm01():
    # 初始化权重参数
    w = torch.tensor([1,0],requires_grad=True,dtype=torch.float)
    # 定义损失函数
    criterion = ((w ** 2) / 2.0)
    # 定义优化器参量参数
    optimizer = optim.SGD(params=[w],lr=0.01,momentum=0.9)
    # 计算梯度值
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f"w:{w},w.grad:{w.grad}")


if __name__ == '__main__':
    dm01()
