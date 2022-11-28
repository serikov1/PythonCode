import matplotlib.pyplot as plt
import matplotlib
from math import log
import numpy

matplotlib.use('TkAgg')

x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y0 = [3.5, 11.3, 22.8, 37.1, 52.6, 69.8, 89.5, 107.35, 129.1, 151.5, 176.4, 202, 252.8, 316, 376.6, 441.5, 865, 1361,
     1946, 2589, 3279, 4031, 4832, 5776]
y20 = [7.3, 17.4, 28.6, 45.4, 63.0, 79.8, 101, 121.6, 146.2, 166.8, 194.3, 220.1, 279, 339, 403.8, 473, 915.5, 1423,
      2011, 2661, 3374, 4133, 4945, 5897]
y30 = [14, 24.4, 40.6, 59, 77.7, 98.1, 118.6, 142.0, 166, 189.5, 217, 241, 301.2, 366.4, 434, 503.8, 960, 1482, 2081,
      2747, 3467, 4237, 5126, 6016]
y40 = [21.2, 35.5, 52.4, 72.8, 93.7, 116.2, 136.1, 160.4, 187.2, 213.4, 240.1, 270.8, 332.8, 398.8, 471.9, 577, 1014,
      1542, 2157, 2832, 3555, 4335, 5250, 6138]

x_32 = [x ** (3 / 2) for x in x]
x = [log(x_) for x_ in x]
y = [log(x) for x in y0]
y2 = [log(x) for x in y20]
y3 = [log(x) for x in y30]
y4 = [log(x) for x in y40]

coeffs = numpy.polyfit(x[4:-8], y[4:-8], 1)
k = coeffs[0]
b = coeffs[1]

line_points = [k * number + b for number in x[4:-8]]
plt.scatter(x, y, s=7., color='red')
line, = plt.plot(x[4:-8], line_points, color='green')
print(k)

coeffs = numpy.polyfit(x[4:-8], y2[4:-8], 1)
k2 = coeffs[0]
b = coeffs[1]
line_points = [k2 * number + b for number in x[4:-8]]
plt.scatter(x, y2, s=7., color='blue')
line2, = plt.plot(x[4:-8], line_points, color='black')
print(k2)

coeffs = numpy.polyfit(x[7:-6], y3[7:-6], 1)
k3 = coeffs[0]
b = coeffs[1]
line_points = [k3 * number + b for number in x[7:-6]]
plt.scatter(x, y3, s=7., color='yellow')
line3, = plt.plot(x[7:-6], line_points, color='grey')
print(k3)

coeffs = numpy.polyfit(x[9:-4], y4[9:-4], 1)
k4 = coeffs[0]
b = coeffs[1]
line_points = [k4 * number + b for number in x[9:-4]]
plt.scatter(x, y4, s=7., color='blue')
line4, = plt.plot(x[9:-4], line_points, color='purple')
print(k4)

plt.ylabel('$\\ln I$')
plt.xlabel('$\\ln U$')
# plt.xlim(10, 40)
# plt.ylim(0, 2)
plt.grid()
plt.title('График зависимости \n  $ \\ln I (\\ln U)$')
plt.legend((line, line2, line3, line4), [f'k = {k: .2f}', f'k = {k2: .2f}', f'k = {k3: .2f}', f'k = {k4: .2f}'])
# plt.savefig('lnI(lnU)')
plt.show()

# //------------------------------------------//

coeffs = numpy.polyfit(x_32[4:-8], y0[4:-8], 1)
k = coeffs[0]
b = coeffs[1]
print(b)

line_points = [k * number + b for number in x_32[4:-8]]
plt.scatter(x_32[4:-8], y0[4:-8], s=7., color='red')
line, = plt.plot(x_32[4:-8], line_points, color='green')
print(k)

coeffs = numpy.polyfit(x_32[4:-8], y20[4:-8], 1)
k2 = coeffs[0]
b = coeffs[1]
print(b)

line_points = [k2 * number + b for number in x_32[4:-8]]
plt.scatter(x_32[4:-8], y20[4:-8], s=7., color='blue')
line2, = plt.plot(x_32[4:-8], line_points, color='black')
print(k2)

coeffs = numpy.polyfit(x_32[7:-6], y30[7:-6], 1)
k3 = coeffs[0]
b = coeffs[1]
print(b)

line_points = [k3 * number + b for number in x_32[7:-6]]
plt.scatter(x_32[7:-6], y30[7:-6], s=7., color='yellow')
line3, = plt.plot(x_32[7:-6], line_points, color='grey')
print(k3)

coeffs = numpy.polyfit(x_32[7:-6], y40[7:-6], 1)
k4 = coeffs[0]
b = coeffs[1]
print(b)

line_points = [k4 * number + b for number in x_32[7:-6]]
plt.scatter(x_32[7:-6], y40[7:-6], s=7., color='blue')
line4, = plt.plot(x_32[7:-6], line_points, color='purple')
print(k4)

plt.ylabel('$ I, мкА$')
plt.xlabel('$U^{3/2}, В^{3/2}$')
plt.xlim(3, 33)
plt.ylim(50, 600)
plt.grid()
plt.title('График зависимости \n  $I (U^{3/2})$')
plt.legend((line, line2, line3, line4), [f'k = {k: .2f}', f'k = {k2: .2f}', f'k = {k3: .2f}', f'k = {k4: .2f}'])
# plt.savefig('I(U32)')
plt.show()
