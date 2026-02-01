# import torch
#
# a = torch.rand(4,4)
# b = torch.rand(4,4)
#
#
# out = torch.where(a > 0.5,a,b)
# print(out)
#

# import torch
# a = torch.rand(4,4)
# b = torch.rand(4,4)
#
# out = torch.where(a > 0.5,a,b)
# print(out)

# import torch
#
# a = torch.rand(4,4)
# b = torch.rand(4,4)
#
# out = torch.where(a > 0.5,a,b)
# print(out)

# import torch
# a = torch.rand(4,4)
# b = torch.rand(4,4)
#
# out = torch.index_select(a,0,index=torch.tensor([0,3,2]))
# print(out)

# import torch
#
# a = torch.rand(4,4)
# b = torch.rand(4,4)
#
# out = torch.index_select(a,0,index=torch.tensor([0,3,2]))
# print(out)

import torch

a = torch.rand(4,4)
b = torch.rand(4,4)

out = torch.index_select(a,0,index=torch.tensor([0,3,2]))
print(out)






