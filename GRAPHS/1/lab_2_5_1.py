from matplotlib import pyplot
import numpy

y_1 = [63.8, 63, 62.4, 61.8, 61, 60.4, 60.1, 59.5]
x_1 = [298, 303, 308, 313, 318, 323, 328, 333]

coeffs = numpy.polyfit(x_1, y_1, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='r')
line1, = pyplot.plot(x_1, line_points, color='b')
print(k)

x_1_1 = [x * 0.12238095 for x in x_1]
y_1_1 = [x + y for x, y in zip(y_1, x_1_1)]

line2, = pyplot.plot(x_1, x_1_1, color='green')
line3, = pyplot.plot(x_1, y_1_1, color='black')

pyplot.ylabel('$\\sigma, мН/м$')
pyplot.xlabel('T, K')
pyplot.xlim(296, 335)
pyplot.ylim(35, 105)
pyplot.grid()
pyplot.title('График зависимости \n  $\\sigma (T)$')

pyplot.legend((line1, line2, line3), ['$\\sigma(T)$',
                                  '$q = - T \\frac{d\\sigma}{dT}$',
                                  '$\\frac{U}{F} = (\\sigma - T\\frac{d\\sigma}{dT})$'])
pyplot.savefig('surface_tension')
pyplot.show()
