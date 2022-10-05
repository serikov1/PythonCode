import numpy
from matplotlib import pyplot
from scipy.optimize import curve_fit

x = [3.4, 3.1, 2.6, 2.2, 1.4, 1.0, 0.5, 0.3]
# x = [(-x_+0.6) * 90.9 for x_ in x][::-1]

y = [3.4, 3.3, 3.1, 2.8, 2.1, 1.5, 0.8, 0.2]
# y_1 = [(-x_+0.4) for x_ in y][::-1]
x = [x_ * 90.9 for x_ in x]
# x.extend(x_1)
# y.extend(y_1)
y = [y_ * 0.2 for y_ in y]

X_Final = numpy.linspace(min(x), max(x), 2000)
def func(x, A, B, C, D, E, F):
    return A/(1 + B/x + C/x**2) + D*((numpy.tanh(x/E))**(-1) - E/x) + F*x


popt, pcov = curve_fit(func, x, y)
A, B, C, D, E, F = popt

coeffs = numpy.polyfit(x[-4:-2], y[-4:-2], 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x[-3:-1]]
pyplot.plot(x[-3:-1], line_points, color='green')
print(k)

# line_points = [A/(1 + B/x + C/x**2) + D*((numpy.tanh(x/E))**(-1) - E/x) + F*x for x in x]
pyplot.scatter(x, y, s=7., color='red')
# pyplot.errorbar(x, y, yerr=error_y, fmt='.', color='r', ecolor='green', capsize=3)
pyplot.plot(X_Final, func(X_Final, *popt), color='b')

pyplot.ylabel('$B$, мТл')
pyplot.xlabel('$I$, А')
# pyplot.xlim(0, 1.4 * 10.6)
# pyplot.ylim(0, 1.7)
pyplot.grid()
pyplot.title('График зависимости \n  $B(H)$ для кремнистого железа')
# pyplot.legend(line1, ['$B(I)$'])
pyplot.savefig('3-4-5_KremnGeleso')
pyplot.show()