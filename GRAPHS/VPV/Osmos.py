from matplotlib import pyplot
import numpy

x_1 = [0.75, 1.5, 3]
y_1 = [11.235, 14.17, 22.76]

coeffs = numpy.polyfit(x_1, y_1, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='red')
line1, = pyplot.plot(x_1, line_points, color='b')
print(k)

pyplot.ylabel('$P_{осм}$')
pyplot.xlabel('$C$')
pyplot.xlim(0, 3.5)
pyplot.ylim(10, 25)
pyplot.grid()
pyplot.title("График зависимости \n $P_{осм}(C)$ ")
pyplot.legend((line1,), ['$P_{осм} = k \\cdot C$'])

pyplot.show()
# pyplot.savefig('P(C)')