import numpy as np


print(np.allclose([np.nan, 1e10, 1e90],[np.inf, 1e456,1e-987]))
