import numpy
import numpy as np
from sklearn import linear_model
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
import pandas as pd

x = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88])
x=x.reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

lr= linear_model.LogisticRegression()
lr.fit(x,y)
x=x.reshape(1,-1)

arr = np.linspace(x.min(), x.max(), 50)

def logit2prob(logr, X):
  log_odds = logr.coef_ * X + logr.intercept_
  odds = numpy.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)


plt.scatter(x,y)
plt.plot(arr, logit2prob(lr, arr)[0])
plt.show()
