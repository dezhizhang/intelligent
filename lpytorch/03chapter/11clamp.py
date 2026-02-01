import torch
a = torch.rand(2,2) * 10
a.clamp(min=0,max=10)
print(a)





