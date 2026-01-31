# import torch
#
# a = torch.rand(4,4)
# b = torch.rand(4,4)
# print(a,b)
#
# out = torch.where(a > 0.5,a,b)
# print(out)

# import torch
# a = torch.rand(4,4)
# b = torch.rand(4,4)
#
# print(a,b)
#
# out = torch.where(a > 0.5,a,b)
# print(out)


# import torch
#
# a = torch.rand(4,4)
# out = torch.index_select(a,dim=0,index=torch.tensor([0,3,2]))
# print(out)

# import  torch
#
# a = torch.rand(4,4)
# out = torch.index_select(a,dim=0,index=torch.tensor([0,3,2]))
# print(out.shape)

# gethor
import torch

a = torch.linspace(1,16,16).view(4,4)
print(a)

out = torch.gather(a,dim=0,index=torch.tensor([[0,1,1,1],[0,1,2,2],[0,1,3,2]]))
print(out)

