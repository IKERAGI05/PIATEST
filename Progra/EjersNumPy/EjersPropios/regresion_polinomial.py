import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1, 2, 5, 3, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 60, 80, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

model3= numpy.poly1d(numpy.polyfit(x, y, 3))
model6= numpy.poly1d(numpy.polyfit(x, y, 6))
model9= numpy.poly1d(numpy.polyfit(x, y, 9))

line = numpy.linspace(0, 25, num=1000)

print(plt.subplot(2, 3, 2))
plt.scatter(x, y)
plt.plot(line, model3(line), label="3rd degree (x³)")
plt.plot(line, model6(line), label="6th degree (x⁶)")
plt.plot(line, model9(line), label="9th degree (x⁹)")
plt.legend(loc="lower right")
plt.title("Polinomial regression with NumPy")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.subplot(2, 3, 4)
plt.scatter(x, y)
plt.plot(line, model3(line))
plt.title("3rd degree (Linear Regression)")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.subplot(2, 3, 5)
plt.scatter(x, y)
plt.plot(line, model6(line))
plt.title("6th degree")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.subplot(2, 3, 6)
plt.scatter(x, y)
plt.plot(line, model9(line))
plt.title("9th degree")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()