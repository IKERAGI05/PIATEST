import numpy as np
x= np.array([1,2,3,4,5])
print("Array")
print(x)
print("True si hay numeros que no se han 0 en el array False si no los hay")
print(np.any(x))
x=np.array([0, 0])
print(x)
print("Segunda comprobación")
print(np.any(x))