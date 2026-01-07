import torch
import torch.nn as nn
import torch.optim as optim
def dm01():
    w = torch.tensor([1.0],requires_grad=True,dtype=torch.float32)

    # 定义损失函数
    criterion = ((w ** 2) / 2.0)

    # 自适应优化器
    optimizer = optim.Adagrad(params=[w],lr=0.01)

    # 计算梯度值
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f"w:{w} w.grad:{w.grad}")


if __name__ == '__main__':
    dm01()



