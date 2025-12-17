from random import randint

import torch

torch.manual_seed(24)

t1 = torch.randint(1,10,(5,5))


t2 = torch.randint(1,10,(2,3,4))
print("t2",t2)






