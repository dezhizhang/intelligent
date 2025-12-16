import torch

t1 = torch.tensor([1,2,3,4,5],dtype=torch.float32)
print(f"t1:{t1} type:{t1.dtype}")


t2 = t1.type(torch.int16)
print(f"t2:{t2} type:{t2.dtype}")