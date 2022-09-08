from matplotlib import pyplot
import numpy

x_1 = [0.75, 1.5, 3]
y_1 = [2.7, 3.4, 5.4]
er_1 = [0.8, 1, 1.7]

coeffs = numpy.polyfit(x_1, y_1, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='green')
line1, = pyplot.plot(x_1, line_points, color='b')
pyplot.errorbar(x_1, y_1, yerr=er_1, fmt='.', color='r', ecolor='b', capsize=3)
print(k)
RT = k * 368
print(RT)
pyplot.ylabel('$P_{осм},$ кПа')
pyplot.xlabel('$C, г/л$')
pyplot.xlim(0, 3.5)
pyplot.ylim(2.15, 5.75)
pyplot.grid()
pyplot.title("График зависимости \n $P_{осм}(C)$ ")
pyplot.legend((line1,), ['$P_{осм} = k \\cdot C$ \n$k = 1,2  \\frac{ кПа \\cdot л}{г}$'], loc='upper left')
pyplot.savefig('P(C)')
pyplot.show()