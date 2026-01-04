import torch


# 参数1初始值，参数2是否自动微分
w = torch.tensor(10,requires_grad=True,dtype=torch.float)

# 2. 定义loss变量，表示损失函数
loss = 2 * w ** 2

# 3. 打印梯度函数类型
print(f"梯度函数类型:{type(loss.grad_fn)}")
# print(loss.sum())

#4. 计算梯度,梯度=损失函数的导数
loss.backward()

#5. 代入权重更新公式:w新=w旧-学习率*梯度
w = w.data - 0.01 * w.grad

# 打印最终结果
print(f"初始权重:{w.data}")

