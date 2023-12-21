import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

x= np.array([34, 42, 100, 98, 18, 19, 18, 32, 100, 42, 45])
y= np.array([14, 34, 22, 6, 2, 47, 19, 87, 150, 12, 1])

slope, intercept, r, p, std_err = stats.linregress(x, y)
print("w1: ", slope)
print("w0: ", intercept)
print(p)
print(std_err)

def func(x):
    return slope * x + intercept
x_new= np.linspace(x.min(),x.max(), 100)

model= list(map(func, x_new))

plt.scatter(x,y)
plt.plot(x_new, model)
plt.show()