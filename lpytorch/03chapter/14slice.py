import torch

# a = torch.rand((3,4))
# out = torch.chunk(a,2,dim=1)
# print(out[0],out[0].shape)
# print(out[1],out[1].shape)

a = torch.rand(3,4)
out = torch.chunk(a,2,dim=1)
print(out[0],out[0].shape)
print(out[1],out[1].shape)






