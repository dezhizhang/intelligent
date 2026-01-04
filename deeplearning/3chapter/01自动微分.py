import torch

x = torch.tensor(10,requires_grad=True,dtype=torch.float)

print("x->",x)

y = 2 *x **2
print("y->",y)


print(y.grad_fn)

print("y.sum",y.sum())

