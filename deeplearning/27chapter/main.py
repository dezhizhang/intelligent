import torch

w = torch.tensor(10,requires_grad=True,dtype=torch.float)

# 定义loss变量 表示损失函数
loss = 2 * w ** 2
print(f"loss:{loss.grad_fn}")

# 带入权重更新公式
loss.backward()

w.data = w.data - 0.01 * w.grad

# 打印最终结果
print(f"更新后的权重:{w}")



