from audioop import reverse
from cProfile import label
from ctypes import sizeof
from math import sqrt, ceil
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x, A, B, C, D, E, F):
    return A/(1 + B/x + C/x**2) + D*((np.tanh(x/E))**(-1) - E/x) + F*x

# пермалой (все величины в СИ)
Kx = 20e-3 # Volt
Ky = 50e-3

N0 = 15
Nu = 300
S = 0.66e-4 # m^2
L = 14.1e-2 # m
i = np.array([232.46, 206.31, 198.66, 169.39, 158.38, 145.45, 133.18, 112.83, 100.64, 0.001]) /1000 # Amper
# coord of point
x = np.array([3.6, 3, 2.4, 2, 1.8, 1.6, 1.45, 1.4, 1.2, 0.001]) * Kx # Volt
y = np.array([1.8, 1.7, 1.45, 1.4, 1, 0.8, 0.45, 0.2, 0.1, 0.001]) * Ky # Volt
x_range = np.linspace(0, 25, 1000)
i_ef = x/0.2
B = y * (0.4/(S*Nu))
H = i*N0/L

popt, pcov = curve_fit(func, H, B, maxfev = 10**6)
A, b, C, D, E, F = popt

figure, ax = plt.subplots()
ax.scatter(H, B, s = 5, c = 'r')
ax.set_xlim(10, 26)
ax.set_ylim(0, 1.9)
ax.set_title("Initial Magnetization Curve for permalloy")
ax.set_xlabel('H, A/m')
ax.set_ylabel('B, T')
ax.plot(x_range, func(x_range, *popt))
ax.grid('major')
# plt.savefig('Permalloy_i_ef.png', bbox_inches = 'tight', pad_inches = 0, dpi = 480)
plt.show()