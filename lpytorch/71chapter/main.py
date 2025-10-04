# import torch
#
# x = torch.randint(1,10,(3,2,3))
# print(id(x))
# x+=10
#
# print(x)
# print(id(x))

# import torch
#
# x = torch.randint(1,10,(3,2,3))
# print(id(x))
# x += 10
#
# print(x)
# print(id(x))

# import torch
#
# x = torch.randint(1,10,(3,2,4))
# y = torch.randint(1,10,(3,4,1))
#
# print(x.shape)
# print(id(x))

# import torch
#
# x = torch.randint(1,10,(3,2,4))
# y = torch.randint(1,10,(3,2,4))
#
# print(x.shape)
# print(id(x))
#

# import torch
#
# x = torch.randint(1,10,(3,2,4))
# y = torch.randint(1,10,(3,2,4))
#
# print(x.shape)
# print(id(x))

import torch

x = torch.randint(1,10,(3,2,4))
y = torch.randint(1,10,(3,4,1))

print(x.shape)
print(id(x))

x[:] = x @ y
print(x.shape)
print(id(x))











