import random

from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("diabetes.csv")
x = df['BMI']
y = df['Glucose']
classes = df['Outcome']

data = list(zip(x, y))
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, classes)

new_x = random.randint(int(x.min()),int(x.max()))
new_y = random.randint(int(y.min()),int(y.max()))
print(new_x, ", ", new_y)
new_point = [(new_x, new_y)]
prediction = knn.predict(new_point)
print(prediction)
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.scatter(new_x, new_y, c='red', marker='x')
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
plt.show()
