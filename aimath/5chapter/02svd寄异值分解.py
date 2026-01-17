import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [1,2],
    [5,6]
])

u,s,v = np.linalg.svd(A)

point = np.array([[1,0],[2,0],[3,0],[1,1],[2,1],[3,1]])

rotated = np.dot(point,u.T)
streched = rotated @ np.diag(s)
rotated2 = streched.dot(v)

transformed = point.dot(A)



