# import numpy as np
#
# A = np.array([[1,2,3,4],[5,6,7,8]])
# A = np.arange(1,9).reshape(2,4)
# print(A)
# print(A.T)
#

# import numpy as np
#
# A = np.array([

# ])
#
# b = np.array([8,-11,-3,9])
# Ain = np.linalg.inv(A)
# x = Ain @ b
#
# print(np.round(x,2))

import numpy as np

A = np.array([
    [2, 1, -1, 2],
    [-3, -1, 2, -4],
    [-2, 1, 2, -3],
    [1, 1, -2, 5]
])


b = np.array([8,-11,-3,9])
Ain = np.linalg.inv(A)
x = Ain @ b

print(np.round(x,2))
