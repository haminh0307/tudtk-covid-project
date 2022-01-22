import numpy
import matplotlib.pyplot as plt
import data
from sklearn.metrics import r2_score, mean_squared_error

X, Y = data.get_data()
n = len(X)

mymodel = numpy.poly1d(numpy.polyfit(X, Y, 3))

print('Mean squared error:', mean_squared_error(Y, mymodel(X)))
print('RMSE mean squared error:', mean_squared_error(Y, mymodel(X), squared=False))
print('R-square:', r2_score(Y, mymodel(X)))

myline = numpy.linspace(0, 1, 100)

plt.scatter(X, Y)
plt.plot(myline, mymodel(myline), color='red')
plt.xlabel('Twice injected percentage')
plt.ylabel('Death rate')
plt.title('Death rate vs. twice injected percentage, from 13/9/2021 to 21/1/2022')
plt.savefig('plot/regression.pdf', format='pdf')
plt.show()