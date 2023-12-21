import numpy as np
x = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])

print("Iguales?")
print(np.equal(x,y))
print("Iguales con tolerancia?")
print(np.allclose(x,y))