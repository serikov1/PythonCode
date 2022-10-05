import matplotlib
import numpy
from matplotlib import pyplot
from scipy.optimize import curve_fit
matplotlib.use('TkAgg')

x = [3.6, 3.0, 2.5, 1.7, 1.0, 0.8, 0.4, 0.2]
# x_1 = [(-x_+0.4) * 18 for x_ in x][::-1]

y = [2.5, 2.3, 2.2, 1.9, 1.5, 1.4, 0.6, 0.2]
# y_1 = [(-x_+0.4) for x_ in y][::-1]
x = [x_ * 18 for x_ in x]
# x.extend(x_1)
# y.extend(y_1)
y = [y_ * 0.066 for y_ in y]


# B_spline_coeff = make_interp_spline(sorted(x), sorted(y))
X_Final = numpy.linspace(min(x), max(x), 2000)
# Y_Final = B_spline_coeff(X_Final)

# coeffs = numpy.polyfit(x, y, 2)
# a = coeffs[0]
# b = coeffs[1]
# c = coeffs[2]

# A, B, C, D, E, F = 1, 2, 20, 0.5, 4, 0.01

x_ = [5.7, 6.8]
y_ = [0.005, 0.036]

coeffs = numpy.polyfit(x_, y_, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in x_]
pyplot.plot(x_, line_points, color='green')
print(k)

def func(x, A, B, C, D, E, F):
    return A/(1 + B/x + C/x**2) + D*((numpy.tanh(x/E))**(-1) - E/x) + F*x


popt, pcov = curve_fit(func, x, y)
A, B, C, D, E, F = popt

# line_points = [A/(1 + B/x + C/x**2) + D*((numpy.tanh(x/E))**(-1) - E/x) + F*x for x in x]
pyplot.scatter(x, y, s=7., color='red')
# pyplot.errorbar(x, y, yerr=error_y, fmt='.', color='r', ecolor='green', capsize=3)
pyplot.plot(X_Final, func(X_Final, *popt), color='b')



pyplot.ylabel('$B$, мТл')
pyplot.xlabel('$I$, А')
pyplot.xlim(4, 69)
pyplot.ylim(0, 0.175)
pyplot.grid()
pyplot.title('График зависимости \n  $B(H)$ для феррита')
# pyplot.legend(line1, ['$B(I)$'])
pyplot.savefig('3-4-5_Ferrit')
pyplot.show()