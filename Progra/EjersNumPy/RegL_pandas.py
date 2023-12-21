import pandas as p
import numpy as np
from sklearn import linear_model
from matplotlib import pyplot as plt

arch= p.read_csv("diabetes.csv")

X= arch[['Glucose']]
y= arch['Outcome']

x_new= np.linspace(X.Glucose.min(), X.Glucose.max()).reshape(-1,1)

logr= linear_model.LogisticRegression()

logr.fit(X,y)

predicted = logr.predict_proba(x_new)[:,1]

print(predicted)
plt.scatter(X, y)
plt.plot(x_new, predicted)
plt.savefig("grafica_logistica_pandas.png")
