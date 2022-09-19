from matplotlib import pyplot
import numpy

y = [41.7, 90.3, 173.6, 222.2, 278.8, 368.1, 430.6, 472.2]
x = [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8]
error_y = [12.5, 13.9, 13.9, 13.9, 13.9, 13.9, 13.9, 13.9]

coeffs = numpy.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
pyplot.scatter(x, y, s=7., color='red')
pyplot.errorbar(x, y, yerr=error_y, fmt='.', color='r', ecolor='green', capsize=3)
line1 = pyplot.plot(x, line_points, color='b')

pyplot.ylabel('$B$, мТл')
pyplot.xlabel('$I$, А')
pyplot.xlim(-0.05, 3)
pyplot.ylim(28, 490)
pyplot.grid()
pyplot.title('График зависимости \n  $B(I)$')
pyplot.legend(line1, ['$B(I)$'])
pyplot.savefig('3-4-1_first')
pyplot.show()
