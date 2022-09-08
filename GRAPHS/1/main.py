from matplotlib import pyplot
import numpy

x_1 = [0, 1, 2, 3, 4, 5, 6]
y_1 = [200, 450, 660, 874, 1088, 1305, 1521]
y_1 = [x - 200 for x in y_1]

x_2 = [0, 1, 2, 3, 4, 5, 6]
y_2 = [202, 454, 666, 882, 1099, 1317, 1536]
y_2 = [x - 202 for x in y_2]

x_3 = [0, 1, 2, 3, 4, 5, 6]
y_3 = [203, 457, 670, 888, 1106, 1327, 1547]
y_3 = [x - 203 for x in y_3]

x_4 = [0, 1, 2, 3, 4, 5, 6]
y_4 = [205, 460, 675, 894, 1114, 1336, 1558]
y_4 = [x - 205 for x in y_4]

x_5 = [0, 1, 2, 3, 4, 5, 6]
y_5 = [206, 463, 680, 901, 1122, 1346, 1570]
y_5 = [x - 206 for x in y_5]

x_6 = [0, 1, 2, 3, 4, 5, 6]
y_6 = [207, 466, 684, 906, 1129, 1355, 1579]
y_6 = [x - 207 for x in y_6]

x_7 = [0, 1, 2, 3, 4, 5, 6]
y_7 = [209, 467, 686, 908, 1133, 1358, 1583]
y_7 = [x - 209 for x in y_7]

coeffs = numpy.polyfit(x_1, y_1, 1)
print(coeffs)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_1]
pyplot.scatter(x_1, y_1, s=7., color='red')
line1, = pyplot.plot(x_1, line_points, color='b')
print(k)

coeffs = numpy.polyfit(x_2, y_2, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_2]
pyplot.scatter(x_2, y_2, s=7., color='red')
line2, = pyplot.plot(x_2, line_points, color='g')
print(k)

coeffs = numpy.polyfit(x_3, y_3, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_3]
pyplot.scatter(x_3, y_3, s=7., color='red')
line3, = pyplot.plot(x_3, line_points, color='grey')
print(k)

coeffs = numpy.polyfit(x_4, y_4, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_4]
pyplot.scatter(x_4, y_4, s=7., color='red')
line4, = pyplot.plot(x_4, line_points, color='black')
print(k)

coeffs = numpy.polyfit(x_5, y_5, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_5]
pyplot.scatter(x_5, y_5, s=7., color='red')
line5, = pyplot.plot(x_5, line_points, color='black')
print(k)

coeffs = numpy.polyfit(x_6, y_6, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_6]
pyplot.scatter(x_6, y_6, s=7., color='red')
line6, = pyplot.plot(x_6, line_points, color='black')
print(k)

coeffs = numpy.polyfit(x_7, y_7, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_7]
pyplot.scatter(x_7, y_7, s=7., color='red')
line7, = pyplot.plot(x_4, line_points, color='black')
print(k)

pyplot.ylabel('f')
pyplot.xlabel('n')
pyplot.xlim(0, 6.5)
pyplot.ylim(0, 1500)
pyplot.grid()
pyplot.title("График зависимости \n f(n) ")
pyplot.legend((line1, line2, line3, line4, line5, line6, line7), ['t = 23,5 $^{\\circ}C$', 't = 30 $^{\\circ}C$',
                                                                  't = 35 $^{\\circ}C$', 't = 40 $^{\\circ}C$',
                                                                  't = 45 $^{\\circ}C$', 't = 50 $^{\\circ}C$',
                                                                  't = 52 $^{\\circ}C$'])
# pyplot.savefig('air.png')
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