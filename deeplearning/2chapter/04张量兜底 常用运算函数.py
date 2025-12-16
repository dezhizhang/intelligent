import torch

t1 = torch.tensor([[1,2,3],[4,5,6]])

print(f"按列求和:{t1.sum(dim=0)}")
print(f"按行求和:{t1.sum(dim=1)}")
print(f"整体求和:{t1.sum()}")

