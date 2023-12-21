import numpy as np
import matplotlib.pyplot as plt

# IMPORTAR LIBRERÍAS NECESARIAS AQUÍ ######################
from sklearn.metrics import r2_score
###########################################################

X = np.arange(0, 20, 0.2)
y = np.cos(X)


# INSERTAR CÓDIGO AQUÍ ####################################
grad=0
for n in y:
    if(round(n,1)==0.9):
        grad=grad+1
modelo= np.poly1d(np.polyfit(X, y, grad))
linea= np.linspace(0, 20, num=1000)
plt.scatter(X,y)
plt.plot(linea, modelo(linea))
plt.title("Regresion polinomial")
###########################################################

plt.show()
