import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
import pandas as pd
df= pd.read_csv('../diabetes.csv')
x= df[['Glucose','BMI']]
y= df['BloodPressure']

regr= linear_model.LinearRegression()

regr.fit(x,y)
x_line = np.linspace(x.Glucose.min(), x.Glucose.max(), 100)
x1_line = np.linspace(x.BMI.min(), x.BMI.max(), 100)

predict= regr.predict(np.concatenate((x_line.reshape(-1,1), x1_line.reshape(-1,1)),axis=1))

fig= plt.figure()
ax= fig.add_subplot(projection='3d')
ax.scatter(x.Glucose, x.BMI, y)
ax.plot(x_line,x1_line,predict, c='red')
plt.show()