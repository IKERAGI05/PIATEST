import numpy as np
x= np.array([1,2,3,4,5])
print("Array")
print(x)
print("True si no hay 0 en el array False si lo hay")
print(np.all(x))
x=np.array([0,1,2,3])
print(x)
print("Segunda comprobación")
print(np.all(x))