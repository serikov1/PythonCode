import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import sqrt, linspace, log

x = [62, 55, 47, 40, 32, 24, 16, 8, 0, -8, -16, -24, -32, -40, -47, -55, -61]
y = [15.6, 26.6, 52, 137, 354, 583, 661, 685, 705, 682, 667, 578, 340, 125, 51, 26, 15]


def mapping(x_, a, r, b):
    return a * (-((x_ - b) / sqrt(r**2 + (x_ - b)**2)) + (x_ + b) / sqrt(r**2 + (x_ + b)**2))


args, cov = curve_fit(mapping, x[:9], y[:9])
print(args)
x_new = linspace(0, 62, 100)
plt.plot(log(x_new), log(mapping(x_new, *args)))
# plt.scatter(x, y, s=7., color='red')

# args, cov = curve_fit(mapping, x[9:], y[9:])
# print(args)
# x_new = linspace(-61, 0, 100)
# plt.plot(log(x_new), log(mapping(x_new, *args)))
# plt.scatter(x, y, s=7., color='red')

plt.ylabel('$ ln(B) $')
plt.xlabel('$ln(r)$')
# plt.xlim(10, 40)
# plt.ylim(0, 2)
plt.grid()
plt.title('График зависимости \n  $ lnB(ln(r))$ для соленоида')
# plt.text(-20, 410,'$r_{соленоида} = 9.8$ мм')
# plt.savefig('3-1-3_solenoid')
plt.show()