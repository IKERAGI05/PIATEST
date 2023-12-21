import pandas as p
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df= p.read_csv("diabetes.csv") #leemos el archivo

d = {'UK': 0, 'USA': 1, 'N': 2} #creamos una tupla dando valores númericos a los paises
df['Nationality'] = df['Nationality'].map(d) #inicializamos los valores de los paises en los numericos
d = {'YES': 1, 'NO': 0} #hacemos los mismo que en lo anterior para el GO
df['Go'] = df['Go'].map(d)#1 para ir y 0 para no ir

features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier() #Inicializamos el modelo
dtree = dtree.fit(X, y) #le damos los valores x y

tree.plot_tree(dtree, feature_names=features)

plt.savefig("tree.png")
