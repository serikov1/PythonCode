import numpy
import numpy as np

def mnk(x_,y_):
    # запишите далее ваш код
    A = np.vstack([x_, np.ones(len(x_))]).T
    a, b = np.linalg.lstsq(A, y_, rcond=None)[0]
    return a, b