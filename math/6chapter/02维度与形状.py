import numpy as np

arr1 = np.arange(1,5).reshape(2,2)
arr2 = np.arange(6,10).reshape(2,2)

arr = np.concatenate((arr1,arr2),axis=1)
print(arr)




