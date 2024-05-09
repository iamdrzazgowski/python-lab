import numpy as np
import matplotlib.pyplot as plt

def julia_set(z, c):
    for i in range(300):
        z = z ** 2 + c
        if abs(z) > 2:
            return i
    return 300

x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5

nx, ny = 400, 400

x, y = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))

z = x + y * 1j

c = -0.1 + 0.65j

julia = np.frompyfunc(julia_set, 2, 1)(z, c).astype(np.float64)
plt.figure(figsize=(10,10))
plt.scatter(x, y, c=julia, s=0.4)
plt.axis('square')
plt.show()