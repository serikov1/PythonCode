from matplotlib import pyplot
import numpy

x_1 = [4, 3.5, 3, 2.5]
y_1 = [3.09, 2.65, 2.18, 1.5]

coeffs = numpy.polyfit(x_1, y_1, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='r')
line1, = pyplot.plot(x_1, line_points, color='grey')
print(k)

y_2 = [3.02, 2.58, 2.04, 1.6]
x_2 = x_1

coeffs = numpy.polyfit(x_2, y_2, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_2]
pyplot.scatter(x_2, y_2, s=7., color='r')
line2, = pyplot.plot(x_2, line_points, color='black')
print(k)

y_3 = [2.98, 2.36, 2.07, 1.37]
x_3 = x_1

coeffs = numpy.polyfit(x_3, y_3, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_3]
pyplot.scatter(x_3, y_3,  s=7., color='r')
line3, = pyplot.plot(x_3, line_points, color='green')
print(k)

y_4 = [2.66, 2.24, 1.72, 1.22]
x_4 = x_1
coeffs = numpy.polyfit(x_4, y_4, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_4]
pyplot.scatter(x_4, y_4, s=7., color='r')
line4, =pyplot.plot(x_4, line_points, color='b')
print(k)

pyplot.ylabel('$\\Delta T, К$')
pyplot.xlabel('$P, атм$')
pyplot.xlim(2.4, 4.1)
pyplot.ylim(1.1, 3.2)
pyplot.grid()
pyplot.title('График зависимости \n  $\\Delta T(P)$')

pyplot.legend((line1, line2, line3, line4), ['T = 296 К,      $\\mu = 10,5  \\frac{К}{МПа}$',
                                             'T = 301 K,      $\\mu = 9,6   \\frac{К}{МПа}$',
                                             'T = 306 К,      $\\mu = 10,2  \\frac{К}{МПк}$',
                                             'T = 316 K,      $\\mu = 9,7   \\frac{К}{МПа}$'])
pyplot.savefig('lab 2_1_6')
pyplot.show()
