import torch

t1 = torch.tensor([10,20],requires_grad=True,dtype=torch.float32)

print(f"t1:{t1} type:{type(t1)}")

t2 = t1.detach()

# 把t2转换成numpy
n1 = t2.numpy()
print(f"n1:{n1} type:{type(n1)}")



