# load the iris dataset
from sklearn.datasets import load_iris
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
#iris = load_iris()
df= pd.read_csv('diabetes.csv')# Crear un gráfico de barras para visualizar la precisión
# store the feature matrix (X) and response vector (y)
#X = iris.data
#y = iris.target

X= df[['BMI']]
y=df['Outcome']
# splitting X and y into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)
print(X_test)

# training the model on training set

gnb = GaussianNB()
gnb.fit(X_train, y_train)

# making predictions on the testing set
y_pred = gnb.predict(X_test)
print("a: ", y_pred)
# comparing actual response values (y_test) with predicted response values (y_pred)

print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred) * 100)

