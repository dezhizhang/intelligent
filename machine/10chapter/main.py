import numpy as np

x = np.array([2,5,8])
y = np.array([1,3,7])

print(x + y)

#

print(x.dot(y))

l0_norm = np.linalg.norm(x,ord=1)
print(l0_norm)
