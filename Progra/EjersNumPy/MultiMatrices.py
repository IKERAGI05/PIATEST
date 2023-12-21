import numpy as np

m1= np.array([[1,6,0],[-1,3,1]])
m2=np.array([[0,4],[2,1],[-2,1]])
m3=np.empty((2,2))

f1, c1= m1.shape
f2, c2= m2.shape
print(f1,c1)
print(len(m1))

for z in range(0,m1):
    for x in range(0,m1[z]):
         for y in range(0,m2[x]):
            m3[x][y]+= m1[x][y]*m2[x+1][y]

print(m3)
