import numpy as np
x= np.array([1, 2, 3, 4, np.nan, np.inf])
print(np.isfinite(x))
