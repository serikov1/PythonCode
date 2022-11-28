import matplotlib.pyplot as plt
import numpy

# x = [12, 10, 8, 7, 6, 4, 3]
# y = [4.9, 3.9, 2.9, 2.7, 2.2, 2.0, 1.2]
#
# coeffs = numpy.polyfit(x, y, 1)
# k = coeffs[0]
# b = coeffs[1]
# line_points = [k * number + b for number in x]
# plt.scatter(x, y, s=7., color='red')
# line = plt.plot(x, line_points, color='green')
# print(k)
#
# plt.ylabel('$T$, с')
# plt.xlabel('$n$')
# # plt.xlim(10, 40)
# # plt.ylim(0, 2)
# plt.grid()
# plt.title('График зависимости \n  $T(n)$')
# plt.legend(line, ['k = 0,382 $\\pm 0,003 $ c'])
# plt.savefig('3-1-3_horizontal')
# plt.show()

x = [10, 8, 6, 4]
y = [274, 183, 115, 100]

coeffs = numpy.polyfit(x, y, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x]
plt.scatter(x, y, s=7., color='red')
line = plt.plot(x, line_points, color='green')
print(k)

plt.ylabel('$ M$, $ дин \\cdot см$')
plt.xlabel('$n$')
# plt.xlim(10, 40)
# plt.ylim(0, 2)
plt.grid()
plt.title('График зависимости \n  $ M(n)$')
plt.legend(line, ['k = 29,5 $\\pm 0,5 $ c'])
# plt.savefig('3-1-3_vertical')
plt.show()
