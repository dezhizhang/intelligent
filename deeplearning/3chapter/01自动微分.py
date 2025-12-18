import torch

w = torch.tensor(10,requires_grad=True,dtype=torch.float)

# 定义loss表示损失函数
loss = 2 * w ** 2

# 打印梯度函数类型
print(f"梯度函数类型:{type(loss.grad_fn)}")

# 计算梯度。梯度=损失函数的导数
loss.backward()

# 权重公司
w.data = w.data - 0.01 * w.grad

print(f"更新后的权重:{w}")