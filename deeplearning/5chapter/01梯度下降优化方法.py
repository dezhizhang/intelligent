import torch
import torch.nn as nn

# 演示梯度下降优化方法
def dm01():
    #1. 初始化权重参数
    w = torch.tensor([1.0],requires_grad=True,dtype=torch.float32)
    #2.定义损失函数
    criterion = ((w ** 2) / 2.0)

    # 创建优化器
    optimizer = torch.optim.SGD([w], lr=0.01, momentum=0.9)
    # 计算梯度值:梯度清零+反向传播+参数更新
    optimizer.zero_grad()
    criterion.sum().backward()

    optimizer.step()
    print(f"w:{w} w.grad:{w.grad}")





if __name__ == '__main__':
    dm01()
