import matplotlib
import numpy
from scipy.interpolate import make_interp_spline
from matplotlib import pyplot
from scipy.optimize import curve_fit
matplotlib.use('TkAgg')

x = [3.6, 3, 2.4, 2, 1.8, 1.6, 1.45, 1.4, 1.2, 0.001]

y = [1.8, 1.7, 1.45, 1.4, 1, 0.8, 0.45, 0.2, 0.1, 0.001]
x = [x_ * 10.6 for x_ in x]

x_ = [1.8 * 10.6, 15]
y_ = [1, 0.44]
coeffs = numpy.polyfit(x_, y_, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_]
pyplot.plot(x_, line_points, color='green')
print(k)

# x_1 = [(-x_+2.39) * 10.6 for x_ in x][::-1]
# y_1 = [(-x_+0.1) for x_ in y][::-1]
# x.extend(x_1)
# y.extend(y_1)

# B_spline_coeff = make_interp_spline(sorted(x), sorted(y))
X_Final = numpy.linspace(min(x), max(x), 2000)
# Y_Final = B_spline_coeff(X_Final)

# coeffs = numpy.polyfit(x, y, 2)
# a = coeffs[0]
# b = coeffs[1]
# c = coeffs[2]

# A, B, C, D, E, F = 1, 2, 20, 0.5, 4, 0.01


def func(x, A, B, C, D, E, F):
    return A/(1 + B/x + C/x**2) + D*((numpy.tanh(x/E))**(-1) - E/x) + F*x


popt, pcov = curve_fit(func, x, y)
A, B, C, D, E, F = popt

# line_points = [A/(1 + B/x + C/x**2) + D*((numpy.tanh(x/E))**(-1) - E/x) + F*x for x in x]
pyplot.scatter(x, y, s=7., color='red')
# pyplot.errorbar(x, y, yerr=error_y, fmt='.', color='r', ecolor='green', capsize=3)
pyplot.plot(X_Final, func(X_Final, *popt), color='b')

# pyplot.plot(x, y, color='r')

pyplot.ylabel('$B$, Тл')
pyplot.xlabel('$H$, Ам/м')
pyplot.xlim(10, 40)
pyplot.ylim(0, 2)
pyplot.grid()
pyplot.title('График зависимости \n  $B(H)$ для пермаллоя')
pyplot.legend(['$B(H)$'])
# pyplot.savefig('3-4-5_Permalloiy')



pyplot.show()
