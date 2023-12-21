import numpy as np
x= np.array([1,2,3,4, np.nan, np.inf])
print("Complejos")
print(np.iscomplex(x))
print("Reales")
print(np.isreal(x))
print("Escalar")
print(np.isscalar(x))