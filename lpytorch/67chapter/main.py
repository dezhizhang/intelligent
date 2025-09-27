#import torch
#
# tensor = torch.rand(3,2)
# numpy_array = tensor.numpy()
#
# print(numpy_array)
#
# print(tensor == numpy_array)

# import torch
# import numpy as np
# np.set_printoptions(precision=6)
#
# tensor = torch.rand(3,2)
#
# numpy_array = tensor.numpy()
#
# print(numpy_array)
# print(tensor == numpy_array)

# import torch
# import numpy as np
#
# np.set_printoptions(precision=6)
#
# tensor = torch.rand(3,2)
#
# numpy_array = tensor.numpy()
# print(numpy_array)
# print(tensor == numpy_array)

import torch
import numpy as np

np.set_printoptions(precision=6)

tensor = torch.rand(3,2)

numpy_array = tensor.numpy()
print(numpy_array)
print(tensor == numpy_array)






