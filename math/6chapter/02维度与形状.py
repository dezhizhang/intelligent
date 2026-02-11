# import numpy as np
#
# arr1 = np.arange(1,5).reshape(2,2)
# arr2 = np.arange(6,10).reshape(2,2)
#
# arr = np.concatenate((arr1,arr2),axis=1)
# print(arr)

# import numpy as np
#
# a = np.arange(1,7).reshape((2,3))
# b = np.arange(7,13).reshape((2,3))
# c = np.arange(13,19).reshape((2,3))
# d = np.arange(19,25).reshape((2,3))
#
# t = np.stack([a,b,c,d],axis=0)
# print(f"axis=0 shape:{t.shape}\n")

import numpy as np


a = np.arange(1,7).reshape((2,3))
b = np.arange(7,13).reshape((2,3))
c = np.arange(13,19).reshape((2,3))
d = np.arange(19,25).reshape((2,3))

t = np.stack([a,b,c,d],axis=0)
print(f"axis=0 shape:{t.shape}")










