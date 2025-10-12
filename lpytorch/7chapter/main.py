# import torch
#
# a = torch.ones(2,3)
# b = torch.ones(2,3)
#
# print(torch.eq(a,b))
# print(torch.equal(a,b))
# print(torch.ge(a,b))
# print(torch.gt(a,b))
# print(torch.lt(a,b))
# print(torch.ne(a,b))

# import torch
#
# a = torch.ones(2,3)
# b = torch.ones(2,3)
#
# print(torch.eq(a,b))
# print(torch.equal(a,b))
# print(torch.ge(a,b))
# print(torch.gt(a,b))
# print(torch.lt(a,b))
# print(torch.ne(a,b))


# import torch
# a = torch.tensor([
#     [2,4,3,1,5],
#     [2,3,5,1,4]
# ])
# print(a.shape)
# print(torch.topk(a,k=2,dim=0))
#
# import torch
#
# a = torch.tensor([
#     [2,4,3,1,5],
#     [2,3,5,1,4]
# ])
#
# print(a.shape)
# print(torch.topk(a,k=2,dim=0))
#
# import torch
#
# a = torch.tensor(
#     [
#         [2,4,3,1,5],
#         [2,3,5,1,4]
#     ]
# )
#
# print(torch.topk(a,k=2,dim=0))

# 有限性判断
import torch
a = torch.rand(2,3)

print(a/ 0)
print(torch.isfinite(a))
print(torch.isfinite(a/0))
print(torch.isinf(a/0))










