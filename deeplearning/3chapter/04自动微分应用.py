import torch

x = torch.ones(2,5)

y = torch.zeros(2,3)


# 初始值（可自动微分的）权重和偏置
w = torch.randn(5,3,requires_grad=True,dtype=torch.float32)


b = torch.randn(3,requires_grad=True,dtype=torch.float32)

# 前向转播
z = torch.matmul(x,w) + b

# 定认损失函数
criterion = torch.nn.MSELoss()
loss = criterion(z,y)


# 进行自动微分，求导，结合返向传播
loss.backward()

# 打印更新的w,b
print(f"w的梯度:{w.grad}")


