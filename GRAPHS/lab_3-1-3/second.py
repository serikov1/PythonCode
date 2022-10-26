import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import exp, polyfit, linspace, log

y = [223, 76, 26.6, 11.4, 6.2, 3.3, 2.0, 1.7, 1.4, 0.9, 227.5, 82.5, 28.2, 12.2, 6.2, 3.6, 2.4, 1.7, 1.2]
x = [-1, -8, -16, -23, -31, -38, -45, -53, -60, -67, 2, 9, 16, 23, 30, 37, 44, 51, 58]


def mapping(x_, a, r):
    return a * r**2 / (r**2 + x_**2)**1.5


args, cov = curve_fit(mapping, x[13:], y[13:])
print(args)
x_new = linspace(2, 62, 1000)
plt.plot(x_new, args[0] * 1 / x_new**3)
plt.scatter(x[13:], y[13:], s=7., color='red')

# args, cov = curve_fit(mapping, x[:10], y[:10])
# print(args)
# x_new = linspace(-70, -1, 1000)
# plt.plot(x_new, mapping(x_new, *args))

# plt.ylabel('$ ln(B)$')
# plt.xlabel('$ln(r)$')
plt.xlim(8, 60)
# plt.ylim(0, 25)
plt.grid()
# plt.title('График зависимости \n  $ B(r)$ для витка')
# plt.text(-60, 210, '$r_{витка}$ = 7,9 мм')
# plt.savefig('3-1-3_vitok')
plt.show()
