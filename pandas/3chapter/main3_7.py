import torch

# # 加法运算
# a = torch.rand(2,3)
# b = torch.rand(2,3)
#
# print(a)
# print(b)
#
#
# print(a + b)
# print(a.add(b))
# print(torch.add(a,b))
# print(a.add_(b))

# a = torch.ones(2,1)
# b = torch.ones(1,2)
#
# print(a @ b)
# print(a.matmul(b))
# print(torch.matmul(a,b))
# print(torch.mm(a,b))


a =torch.ones(2,1)
b = torch.ones(1,2)

print(a @ b)
print(a.matmul(b))
print(torch.matmul(a,b))
print(torch.mm(a,b))





