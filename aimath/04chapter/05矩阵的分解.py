import numpy as np

A = np.array([
    [1,1],
    [1,2],
    [2,1]
])

b = np.array([1,2,3])

Q,R = np.linalg.qr(A)

c = Q.T.dot(b)

x = np.linalg.solve(R,c)

print("解x为:",x)
