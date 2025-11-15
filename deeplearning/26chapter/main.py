#
# import torch
#
# t1 = torch.randint(1,10,(2,3))
# print(f"t1:{t1}")
#
# t2 = torch.randint(1,10,(2,3))
# print(f"t2:{t2}")
#
# # 拼接张量
# t3 = torch.cat([t1,t2],0)
# print(f"t3:{t3}")
#
# import torch
#
# torch.manual_seed(26)
# t1 = torch.randint(1,10,(2,3))
# t2 = torch.randint(1,10,(2,3))
#
# t3 = torch.stack([t1,t2],0)
# print(f"t3:{t3} shape:{t3.shape}")

import  torch
torch.manual_seed(23)

t1 = torch.randint(1,10,(2,3))
t2 = torch.randint(1,10,(2,3))

t3 = torch.stack([t1,t2],0)
print(f"t3:{t3} shape:{t3.shape}")



