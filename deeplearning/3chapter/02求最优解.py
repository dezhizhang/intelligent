import torch

w = torch.tensor(10,requires_grad=True,dtype=torch.float32)

# 2. 定义损失函数
loss = w ** 2 + 20

# 3. 正向传播
for i  in range(1,101):
    loss = w ** 2 + 20

    # 梯度清零, 默认梯度会累国
    if w.grad is not None:
        w.grad.zero_()

    # 反向传播
    loss.sum().backward()

    # 梯度更新
    w.data = w.data - 0.01 * w.grad

# 打印最终结果
print(f"最终结果:{w.grad} loss:{loss}")


