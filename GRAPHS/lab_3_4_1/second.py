from matplotlib import pyplot
import numpy

y = [0, 2, 4.5, 10, 17.5, 24.5, 33.5, 42.5]
x = [1.738, 8.154, 30.136, 40.372, 77.172, 135.497, 185.416, 222.972]
# error_y = [12.5, 13.9, 13.9, 13.9, 13.9, 13.9, 13.9, 13.9]

coeffs = numpy.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='green')
# pyplot.errorbar(x, y, yerr=error_y, fmt='.', color='r', ecolor='green', capsize=3)
line1, = pyplot.plot(x, line_points, color='b')
print(k)

y_1 = [0, 1, 2, 4.5, 8, 12, 16.5, 20]
# error_y = [12.5, 13.9, 13.9, 13.9, 13.9, 13.9, 13.9, 13.9]

coeffs = numpy.polyfit(x, y_1, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y_1, s=7., color='red')
# pyplot.errorbar(x, y, yerr=error_y, fmt='.', color='r', ecolor='green', capsize=3)
line2, = pyplot.plot(x, line_points, color='b', linestyle='--')
print(k)

pyplot.ylabel('$\\Delta P \\cdot 10^{-5}$, Н')
pyplot.xlabel('$B^2 \\cdot 10^{-3}, Тл^2$')
pyplot.xlim(0, 230)
pyplot.ylim(0, 45)
pyplot.grid()
pyplot.title('График зависимости \n  $\\Delta P(B^2)$')
pyplot.legend([line1, line2], ['$\\frac{\\Delta P}{B^2} = 0.184 \\cdot 10^{-2} \\frac{Н}{Тл^{2}}$ $- Al$', '$\\frac{\\Delta P}{B^2} = 0.089 \\cdot 10^{-2} \\frac{Н}{Тл^{2}}$ $- Cu$'])
pyplot.savefig('3-4-1_second')
pyplot.show()
