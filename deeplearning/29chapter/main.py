import torch

w = torch.tensor(10,requires_grad=True,dtype=torch.float32)

loss = w ** 2 + 20

print(f"开始权重初始值:{w} {loss} ")
