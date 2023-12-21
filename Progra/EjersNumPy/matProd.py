import numpy as np

m1 = np.array([[1, 2, 3],
               [4, 5, 6]])

m2 = np.array([[7, 8],
               [9, 10],
               [11, 12]])

f1, c1 = m1.shape
f2, c2 = m2.shape

if c1 != f2:
    print("Las matrices no son multiplicables")
    exit(-1)

res = np.zeros((f1, c2), dtype='i4')

for i in range(0, f1):
    for j in range(0, c2):
        for k in range(0, c1):
            res[i, j] = res[i, j] + (m1[i, k] * m2[k, j])

print(res)

res = np.zeros((f1, c2), dtype='i4')

for idx, x in np.ndenumerate(res):
    for k in range(0, c1):
        res[idx] = res[idx] + (m1[idx[0], k] * m2[k, idx[1]])

print(res)
