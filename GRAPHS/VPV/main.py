
from matplotlib import pyplot
import numpy

x_1 = [0.54, 0.48, 0.41, 0.34, 0.22, 0.11, -0.06]
y_1 = [204, 180, 160, 140, 100, 60, 0]
er_1 = [0.05, 0.05, 0.04, 0.03, 0.02, 0.02, 0.01]

x_2 = [0.9, 0.77, 0.66, 0.56, 0.37, 0.19, -0.021]
y_2 = [200, 180, 160, 140, 100, 60, 0]
er_2 = [0.1, 0.08, 0.07, 0.06, 0.04, 0.04, 0.006]

x_3 = [1.07, 0.9, 0.79, 0.68, 0.46, 0.24, -0.019]
y_3 = [200, 180, 160, 140, 100, 60, 0]
er_3 = [0.1, 0.1, 0.08, 0.07, 0.05, 0.05, 0.06]


coeffs = numpy.polyfit(x_1, y_1, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='b')
line1, = pyplot.plot(x_1, line_points, color='b')
pyplot.errorbar(x_1, y_1, xerr=er_1, fmt='.', capsize=3)
print(k)
print(b)

coeffs = numpy.polyfit(x_2, y_2, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_2]
pyplot.scatter(x_2, y_2, s=7., color='g')
line2, = pyplot.plot(x_2, line_points, color='g')
pyplot.errorbar(x_2, y_2, xerr=er_2, fmt='.', color ='g', ecolor='g', capsize=3)
print(b)

coeffs = numpy.polyfit(x_3, y_3, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_3]
pyplot.scatter(x_3, y_3, s=7., color='black')
line3, = pyplot.plot(x_3, line_points, color='black')
pyplot.errorbar(x_3, y_3, xerr=er_3, fmt='.', color='black', ecolor='black', capsize=3)
print(b)

pyplot.ylabel('$P, дел.$')
pyplot.xlabel('$v, мм/с$')
pyplot.xlim(-0.1, 1.2)
pyplot.ylim(0, 220)
pyplot.grid(which='major', linestyle=':', linewidth=0.5)
pyplot.gca().spines['left'].set_position('zero')
pyplot.title("График зависимости \n $P(v)$ ")
pyplot.legend((line1, line2, line3), ['$ P_{осм}$ = 22 дел.     (С = 3 $\\frac{г}{л})$',
                                      '$P_{осм}$ = 14 дел.     (С = 1,5 $\\frac{г}{л}$)',
                                      '$P_{осм}$ = 11 дел.     (С = 0,75 $\\frac{г}{л}$)'], loc='lower right')
# pyplot.savefig('P(v)')
pyplot.show()

# x = [float(number) for number in input().split()]
# with open('ys.txt') as file:
#     x = [float(number) for number in file.readline().split()]
#     y = [float(number) for number in file.readline().split()]
# print(x, y, sep='\n')

# 34.4
# 38.3
# 42.0
# 46.400000000000006


# 28.1
# 34.1
# 35.900000000000006
# 42.3
