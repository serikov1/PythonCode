from matplotlib import pyplot
import numpy

y_1 = [3.604, 3.767, 4.13]
x_1 = [0.236, 0.223, 0.202]
y_1 = [1/x for x in y_1]
print(y_1)
coeffs = numpy.polyfit(x_1, y_1, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='r')
line1 = pyplot.plot(x_1, line_points, color='b')
print(k)
print(b)


# y_2 = [0.81, 1.6, 2.5, 3.36]
# x_2 = [0.232, 0.442, 0.686, 0.907]
# y_2 = [x - 0.81 for x in y_2]
# coeffs = numpy.polyfit(x_2, y_2, 1)
# k = coeffs[0]
# b = coeffs[1]
# line_points = [k * number + b for number in x_2]
# pyplot.scatter(x_2, y_2, s=7., color='r')
# line2, = pyplot.plot(x_2, line_points, color='black')
# print(k)
#
#
#
# y_3 = [0.76, 1.6, 2.28, 3.14]
# x_3 = [0.215, 0.425, 0.587, 0.792]
# y_3 = [x - 0.76 for x in y_3]
# coeffs = numpy.polyfit(x_3, y_3, 1)
# k = coeffs[0]
# b = coeffs[1]
# line_points = [k * number + b for number in x_3]
# pyplot.scatter(x_3, y_3,  s=7., color='r')
# line3, = pyplot.plot(x_3, line_points, color='green')
#
# print(k)



# y_4 = [262, 524, 786, 1048, 1312, 1575, 1837, 2099, 2366]
# x_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# coeffs = numpy.polyfit(x_4, y_4, 1)
# k = coeffs[0]
# b = coeffs[1]
# line_points = [k * number + b for number in x_4]
# pyplot.scatter(x_4, y_4, color='r')
# pyplot.plot(x_4, line_points, color='b')
# print(k)

pyplot.ylabel('1/k')
pyplot.xlabel('q, г/с')
pyplot.xlim(0.2, 0.24)
pyplot.ylim(0.24, 0.28)
pyplot.grid()
pyplot.title('График зависимости \n  1/k(q)')
# pyplot.savefig('first6')
pyplot.legend(line1, ['$C_p^{уд}$ = 1,046 Дж/г$\\cdot$К,    $\\alpha = 0,0312$ Вт/К'])
pyplot.show()
