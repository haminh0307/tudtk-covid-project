import numpy
import matplotlib.pyplot as plt
import data
from sklearn.metrics import r2_score, mean_squared_error

X, Y = data.get_data(period=4)
n = len(X)
n_train = int(0.9 * n)

mymodel = numpy.poly1d(numpy.polyfit(X[:n_train], Y[:n_train], 3))

print('Mean squared error:', mean_squared_error(Y, mymodel(X)))
print('RMSE mean squared error:', mean_squared_error(Y, mymodel(X), squared=False))
print('R-square:', r2_score(Y, mymodel(X)))

myline = numpy.linspace(0, 1, 100)

plt.scatter(X[:n_train], Y[:n_train])
plt.scatter(X[n_train:], Y[n_train:], color='red')
plt.plot(myline, mymodel(myline))
plt.show()