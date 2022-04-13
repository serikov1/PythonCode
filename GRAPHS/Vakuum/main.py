import numpy
from matplotlib import pyplot

y_1 = []
try:
    with open("Data_1.txt", "r") as f:
        word = "E"
        value = '9.90E+09'
        for line in f:
            line = line.replace(',', '.')
            if word in line and value not in line:
                y_1.append(float(line))
    #             print(line)
    # print(y_1)
finally:
    f.close()

x_1 = []
for i in range(len(y_1)):
    x_1.append(i * 2)
y_1 = [numpy.log(x) for x in y_1]

pyplot.scatter(x_1, y_1, s=1., color='r')
# pyplot.plot(x_2, line_points, color='b')

pyplot.ylabel('ln(p)')
pyplot.xlabel('t, с')
pyplot.xlim(0, 400)

pyplot.grid()
pyplot.title('График зависимости \n  ln p(t)')
# pyplot.savefig('first6')
# pyplot.legend(line1, ['$C_p^{уд}$ = 1,046 Дж/г$\\cdot$К,    $\\alpha = 0,0312$ Вт/К'])
pyplot.show()

# y_2 = []
# try:
#     with open("Data_2.txt", "r") as f:
#         word = "TIC Gauge 2"
#         for line in f:
#             line = line.replace(',', '.')
#             if word in line:
#                 x = line.split()[3:4]
#                 y_2.append(x)
# finally:
#     f.close()
# y_2 = list(map(float, sum(y_2, [])))
#
# x_2 = []
# for i in range(len(y_2)):
#     x_2.append(i * 2)
# y_2 = [numpy.log(x) for x in y_2]
#
# # coeffs = numpy.polyfit(x_2, y_2, 1)
# # k = coeffs[0]
# # b = coeffs[1]
# # line_points = [k * number + b for number in x_2]
# pyplot.scatter(x_2, y_2, s=1., color='r')
# # print(k)
#
# pyplot.ylabel('ln(p)')
# pyplot.xlabel('t, с')
# pyplot.xlim(0, 220)
#
# pyplot.grid()
# pyplot.title('График зависимости \n  ln p(t)')
# # pyplot.savefig('first6')
# # pyplot.legend(line1, ['$C_p^{уд}$ = 1,046 Дж/г$\\cdot$К,    $\\alpha = 0,0312$ Вт/К'])
# pyplot.show()
#
#
# y_3 = []
# try:
#     with open("Data_3.txt", "r") as f:
#         word = "TIC Gauge 2"
#         for line in f:
#             line = line.replace(',', '.')
#             if word in line:
#                 x = line.split()[3:4]
#                 y_3.append(x)
# finally:
#     f.close()
# y_3 = list(map(float, sum(y_3, [])))
#
# x_3 = []
# for i in range(len(y_3)):
#     x_3.append(i * 2)
# y_3 = [numpy.log(x) for x in y_3]
#
# # coeffs = numpy.polyfit(x_2, y_2, 1)
# # k = coeffs[0]
# # b = coeffs[1]
# # line_points = [k * number + b for number in x_2]
# pyplot.scatter(x_3, y_3, s=1., color='r')
# # print(k)
#
# pyplot.ylabel('ln(p)')
# pyplot.xlabel('t, с')
# pyplot.xlim(0, 220)
#
# pyplot.grid()
# pyplot.title('График зависимости \n  ln p(t)')
# # pyplot.savefig('first6')
# # pyplot.legend(line1, ['$C_p^{уд}$ = 1,046 Дж/г$\\cdot$К,    $\\alpha = 0,0312$ Вт/К'])
# pyplot.show()