
import torch

torch.manual_seed(24)

t1 = torch.randint(1,10,(5,5))
print(f"1:{t1} type:{type(t1)}")

# 获取第二行数据
print("*" * 40)
print(t1[1,:])
print(t1[:,3])

print("*" * 40)

print(t1[[0,1],[1,2]])
print(t1[[1,3],[2,4]])

# 范围索引
print("*" * 40)
print(t1[:3,:2])

print("*" * 40)
print(t1[1::2,::2])

print("*" * 40)
print(t1[torch.tensor([True,False,False,True,True])])



