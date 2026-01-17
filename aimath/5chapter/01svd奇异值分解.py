import numpy as np

A = np.arange(1,7).reshape(3,2)
print(A)

u,s,v = np.linalg.svd(A)
print(u)
print(s)
print(v)



