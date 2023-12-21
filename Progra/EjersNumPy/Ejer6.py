import numpy as np
x= np.array([1, 2, -3, 4, np.nan, np.inf])
print("Infinitos")
print(np.isinf(x))
print("Positivos")
print(x>0)
print("Negativos")
print(x<0)