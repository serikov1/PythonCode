import numpy as np

def f(x):
    return 25 * x**3 * (1 - 4 * x**2) * np.exp(-5 * x**2)

def df(x):
    return 25 * np.exp(-5*x**2) * (3*x**2 - 28*x**4 + 1) - 250*x**3*(1-4*x**2)*np.exp(-5*x**2)

x0 = 0

from scipy.optimize import minimize_scalar

res_global = minimize_scalar(f, bounds=(-0.5, 0), method='bounded')
x_global = res_global.x
y_global = f(x_global)
print('Global minimum: x = {:.10f}, y = {:.10f}'.format(x_global, y_global))
