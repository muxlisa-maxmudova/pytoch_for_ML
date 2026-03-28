import torch
import numpy as np

# 1. From a list
data = [[1,2], [3,4]]
t = torch.tensor(data)

# 2. From NumPy
np_array = np.array([1,2,3])
t_from_np = torch.from_numpy(np_array)

