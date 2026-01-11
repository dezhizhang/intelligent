import numpy as np

A = np.array(
    [
        [1,1,1],
        [1,1,2],
        [1,2,1]
    ],
    dtype=float
)

b = np.array([1,2,3],dtype=float)

aInv = np.linalg.inv(A)
x = np.dot(aInv,b)

print(f"x,y,z:{x}")
print(f"result:{np.dot(A,x)}")