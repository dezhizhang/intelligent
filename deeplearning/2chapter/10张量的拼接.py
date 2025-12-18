import  torch


torch.manual_seed(0)

t1 = torch.randint(1,10,(2,3))
t2 = torch.randint(1,10,(2,3))

t = torch.stack([t1,t2],dim=0)
print(f"t:{t} shape:{t.shape}")


