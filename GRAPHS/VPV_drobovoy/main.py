from matplotlib import pyplot
import numpy

x_1 = [60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94]
y_1 = [38, 42, 44, 47, 50, 53, 56, 60, 63, 66, 70, 74, 79, 83, 87, 91, 96, 100]
x_1 = [x ** 2 for x in x_1]
er_1 = [2 for item in x_1]

coeffs = numpy.polyfit(x_1, y_1, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_1]
line1 = pyplot.plot(x_1, line_points, color='b')
# pyplot.errorbar(x_1, y_1, yerr=er_1, fmt=' ', capsize=1, ecolor='g')
pyplot.scatter(x_1, y_1, s=10., color='r')
# print(k)
# print(b)
pyplot.xlabel('$U_г^2, мкВ^2$')
pyplot.ylabel('$I_д, мкА$')
pyplot.grid()
pyplot.legend(line1, ['$I_д(U^2_г)$'])
pyplot.savefig('Id(Ug)')
pyplot.show()
