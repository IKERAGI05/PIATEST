import numpy
from sklearn import linear_model
from matplotlib import pyplot as plt

X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
x_new = numpy.linspace(X.min(), X.max()).reshape(-1,1)
logr = linear_model.LogisticRegression()
logr.fit(X,y)


predicted = logr.predict_proba(x_new)[:,1]

print(predicted)
plt.scatter(X, y)
plt.plot(x_new, predicted)
plt.savefig("grafica_logistica.png")
