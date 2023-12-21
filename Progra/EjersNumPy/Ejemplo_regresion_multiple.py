import numpy as np
import pandas
from matplotlib import pyplot as plt
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight']]
y = df['CO2']
x_new = np.linspace(X.Weight.min(), X.Weight.max()).resize(36,1)
print(x_new)
regr = linear_model.LinearRegression()
regr.fit(X, y)

plt.scatter(X, y)

plt.plot(X, regr.predict(x_new))
plt.savefig("grafica.png")

